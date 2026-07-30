from __future__ import annotations

import re
from typing import Any, Callable, Optional

from ..context import HarvestContext
from ..lexicon.base import LexiconBundle
from ..schema import SourceRef
from ..utils import deadline_text, extract_procurement_target, extract_subject, has_deadline_signal, heading_prior_signals, is_rep_warranty, norm, score_confidence
from ._patterns import CORP_SUFFIX_ALT

# ---------------------------------------------------------------------------
# Defect R4-3: sentence fragments that begin with a lowercase letter or a
# dangling preposition are citation continuations, not obligation sentences.
# Reject them before any frame matching.
# ---------------------------------------------------------------------------
_DANGLING_PREP_RE = re.compile(
    r"^(?:of|to|in|pursuant|from|by|at|under|with|for|on|per)\b",
    re.I,
)


def _is_fragment_sentence(sent: str) -> bool:
    """Return True when *sent* looks like a citation/sentence fragment.

    Rejects sentences that: (a) start with a lowercase letter (continuation
    fragments), or (b) start with a dangling preposition ('of', 'to', 'in',
    'pursuant', 'from', 'by', 'at', 'under', 'with', 'for', 'on', 'per').
    """
    stripped = sent.strip()
    if not stripped:
        return True
    if stripped[0].islower():
        return True
    if _DANGLING_PREP_RE.match(stripped):
        return True
    return False


# ---------------------------------------------------------------------------
# Defect C: boilerplate / junk demotion patterns
#
# These patterns identify sentences that match an obligation frame but carry
# no actionable duty.  They are checked BEFORE frame matching; a hit causes
# the sentence to be skipped entirely for the obligations field.
#
# Principles:
#   - governing_law: "shall be governed by and construed" + governing-law verbs
#   - term_clause: "shall commence on" / "shall continue until" (term/duration)
#   - condition_precedent_perf: "shall have <past-participle>" (EN perfect aspect
#     signals a condition precedent state, not an affirmative duty)
#   - purpose_list: sentences starting with "To <infinitive>" (purpose-list items
#     that lack a modal + party subject)
#   - exclusive_jurisdiction: "shall be subject to the exclusive jurisdiction of"
#   - survival_clause: "shall survive termination" boilerplate
#   - condition_precedent_frame: "obligations ... are subject to the condition that"
#   - closing_logistics: "shall occur at <time>" closing-meeting logistics
#   - procedural_channel: "must be submitted in writing to <email/address>"
# ---------------------------------------------------------------------------

_GOVERNING_LAW_RE = re.compile(
    r"\bshall\s+be\s+governed\s+by\b"
    r"|\bconstrued\s+in\s+accordance\s+with\b",
    re.I,
)

_TERM_CLAUSE_RE = re.compile(
    r"\bshall\s+commence\s+on\b"
    r"|\bshall\s+(?:come\s+into\s+force|take\s+effect)\b",
    re.I,
)

# "shall have <past-participle>" -- perfective modal signals a condition
# precedent satisfied-state, not a prospective duty.
_SHALL_HAVE_PARTICIPLE_RE = re.compile(
    r"\bshall\s+have\s+(?:been\s+)?[a-z]+ed\b"
    r"|\bshall\s+have\s+(?:been\s+)?[a-z]+en\b"
    r"|\bshall\s+have\s+(?:been\s+)?[a-z]+t\b",  # sent/kept/built etc.
    re.I,
)

# Purpose-list opener: "To <verb>..." with no modal/subject before it.
# This matches standalone infinitive-purpose fragments as list items.
_PURPOSE_LIST_RE = re.compile(
    r"^To\s+[a-z]",
)

# Exclusive-jurisdiction clauses: "shall be subject to the exclusive jurisdiction of..."
_EXCLUSIVE_JURISDICTION_RE = re.compile(
    r"\bshall\s+be\s+subject\s+to\s+the\s+exclusive\s+jurisdiction\b"
    r"|\bsoumis\s+à\s+la\s+juridiction\s+exclusive\b",
    re.I,
)

# Survival clauses: "shall survive termination" (confidentiality/obligation survival boilerplate)
_SURVIVAL_CLAUSE_RE = re.compile(
    r"\bshall\s+survive\s+(?:termination|expiry|expiration|résiliation)\b",
    re.I,
)

# Condition-precedent frame: "obligations of X ... are subject to the condition that"
# These express prerequisites, not affirmative duties.
_CONDITION_PRECEDENT_FRAME_RE = re.compile(
    r"\bobligations?\s+of\b.{0,80}\bsubject\s+to\s+the\s+condition\b"
    r"|\bobligations?\s+de\b.{0,80}\bsoumises?\s+à\s+la\s+condition\b",
    re.I | re.DOTALL,
)

# Closing-logistics: "shall occur at <time>" -- scheduling of the closing meeting
_CLOSING_LOGISTICS_RE = re.compile(
    r"\bshall\s+occur\s+at\s+\d",
    re.I,
)

# Procedural-channel: "must be submitted in writing to <contact>"
# These are form-submission instructions, not substantive obligations.
_PROCEDURAL_CHANNEL_RE = re.compile(
    r"\b(?:must|shall)\s+be\s+submitted\s+in\s+writing\s+to\b",
    re.I,
)

# Bug 9: passive-voice (shall/must be ...) where the grammatical subject is not
# a party actor.  Sentences like "The register shall be made available to the
# board" have an inanimate subject and describe a state, not a party obligation.
# The pattern matches the passive construction; the caller guards against
# demoting party-subject passives (e.g. "Employer shall be notified") by
# checking is_known_subject first.
# Matches: "shall be <word>" / "shall not be <word>" / "must be <word>".
# Excludes progressive "-ing" forms which are future-state, not passive.
_PASSIVE_VOICE_RE = re.compile(
    r"\b(?:shall|must)\s+(?:not\s+)?be\s+(?!(?:\w+ing)\b)\w+",
    re.I,
)

# Determiners that signal an inanimate/non-party subject when they appear
# at the start of the subject phrase (before the modal).
_NON_PARTY_DETERMINER_RE = re.compile(
    r"^(?:the|this|that|each|any|all|such|no|a|an)\s+"
    r"(?!(?:"
    r"purchaser|vendor|seller|buyer|borrower|lender|employer|employee"
    r"|licensor|licensee|landlord|tenant|lessor|lessee|assignor|assignee"
    r"|transferor|transferee|party|parties|contractor|subcontractor|consultant"
    r"|agent|trustee|guarantor|obligor|representative|appellant|respondent"
    r"|plaintiff|defendant|applicant|petitioner|company|corporation|issuer"
    r")\b)",
    re.I,
)


def _is_junk_obligation(sent: str) -> bool:
    """Return True when *sent* is a boilerplate / non-duty sentence.

    Covers governing-law frames, term/duration clauses,
    'shall have <participle>' condition-precedent states, purpose-list items,
    exclusive-jurisdiction clauses, survival clauses, condition-precedent
    frames, closing-logistics sentences, and procedural-channel sentences.

    Checks are independent and order-insensitive; new frames may be appended
    in any position.
    All patterns are principled: no fixture-text hard-coding.
    """
    if _GOVERNING_LAW_RE.search(sent):
        return True
    if _TERM_CLAUSE_RE.search(sent):
        return True
    if _SHALL_HAVE_PARTICIPLE_RE.search(sent):
        return True
    if _PURPOSE_LIST_RE.match(sent.strip()):
        return True
    if _EXCLUSIVE_JURISDICTION_RE.search(sent):
        return True
    if _SURVIVAL_CLAUSE_RE.search(sent):
        return True
    if _CONDITION_PRECEDENT_FRAME_RE.search(sent):
        return True
    if _CLOSING_LOGISTICS_RE.search(sent):
        return True
    if _PROCEDURAL_CHANNEL_RE.search(sent):
        return True
    return False


# ---------------------------------------------------------------------------
# Item 5: Description tail-trimming
#
# Obligation descriptions are full sentences; analyst labels are condensations.
# Trailing subordinate boilerplate that dilutes the label match is stripped
# from the description only.  Evidence snippets are never trimmed (verbatim).
#
# Trim rules (EN + FR):
#   - ", in accordance with X"  /  ", conformément à X"
#   - ", pursuant to X"         /  ", en vertu de X"
#   - ", to the reasonable satisfaction of X"  /  ", à la satisfaction de X"
#   - ", as are assigned by X"
#   - ", in a form satisfactory to X"
#   - trailing "subject to X" tails (not full "subject to the condition that" frames)
#
# NEVER trim a tail containing: a date/deadline expression, monetary amount,
# or percentage.  Those carry label-relevant content.
# ---------------------------------------------------------------------------

# Trim markers: patterns matched at the tail of a description.
# Each pattern anchors to `,` or ` ` before the connector phrase.
_TRIM_MARKERS_RE = re.compile(
    r"(?:,\s*|\s+)"                                     # leading separator
    r"(?:"
    r"in\s+accordance\s+with\s+\S.*"                   # "in accordance with X"
    r"|pursuant\s+to\s+\S.*"                            # "pursuant to X"
    r"|at\s+the\s+rate\s+prescribed\s+under\s+\S.*"    # "at the rate prescribed under X"
    r"|to\s+the\s+reasonable\s+satisfaction\s+of\s+\S.*"  # "to the reasonable satisfaction of X"
    r"|in\s+a\s+form\s+satisfactory\s+to\s+\S.*"       # "in a form satisfactory to X"
    r"|as\s+(?:are|may\s+be)\s+assigned\s+by\s+\S.*"  # "as are assigned by X"
    r"|subject\s+to\s+(?:the\s+)?(?:employee|employer|party|parties|contractor)\b.*"  # "subject to X remaining employed..."
    r"|conformément\s+à\s+\S.*"                         # FR "conformément à X"
    r"|en\s+vertu\s+de\s+\S.*"                          # FR "en vertu de X"
    r"|à\s+la\s+satisfaction\s+(?:raisonnable\s+)?de\s+\S.*"  # FR "à la satisfaction de X"
    r")"
    r"$",
    re.I | re.DOTALL,
)

# Bug 6: strip markdown emphasis markers and 'Label:' bold-prefix heads
# from the description start.  Pattern: '**X**: ' or '*X*: ' at the start.
# Only the description field is stripped; evidence snippets remain verbatim.
_MARKDOWN_PREFIX_RE = re.compile(
    r"^\*{1,2}[^*]+\*{1,2}\s*:\s*",  # **Label**: or *Label*:
)

# Guard: patterns that indicate a tail must NOT be trimmed.
# A tail containing any of these is kept verbatim.
_TRIM_GUARD_RE = re.compile(
    r"[$€£¥][\d,.]"                    # monetary amount following currency symbol
    r"|\b\d+[\d,.]*\s*(?:%|percent|per\s+cent)\b"  # percentage
    r"|\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\b"
    r"|\b(?:jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\b"
    r"|\b\d{4}-\d{2}-\d{2}\b"          # ISO date
    r"|\b\d{1,2}/\d{1,2}/\d{2,4}\b"    # slash date
    r"|\bno\s+later\s+than\b"
    r"|\bwithin\s+\d"
    r"|\bprior\s+to\b"
    r"|\bafter\s+\d"
    r"|\bdays?\b",
    re.I,
)


# Compiled pattern that matches the main obligation modal/verb so we can
# guard against trimming before it.  If a trim marker fires before the first
# main modal in the sentence, the sentence is a complex NP+subordinate-then-main
# structure (e.g. FR "Tout avis requis en vertu de ... doit être transmis")
# and the trim must be skipped.
_MAIN_MODAL_RE = re.compile(
    r"\b(?:shall|must|doit|doivent|devra|devront"
    r"|agrees?\s+to|s['']\s*engage(?:nt)?\s+à"
    r"|est\s+tenu[e]?\s+de|sont\s+tenu[e]?s\s+de"
    r"|is\s+required\s+to|is\s+obligated\s+to)\b",
    re.I,
)

# Minimum number of content tokens the trimmed description must retain.
# A description with fewer tokens than this after trimming is likely a fragment;
# the trim is suppressed to avoid producing junk values like "Tout avis requis".
_TRIM_MIN_TOKENS = 5


def _trim_obligation_description(desc: str) -> str:
    """Return *desc* with trailing boilerplate subordinate clauses removed.

    Applies the closed list of trim markers from _TRIM_MARKERS_RE.  If the
    matched tail contains a date, deadline expression, monetary amount, or
    percentage (_TRIM_GUARD_RE), the tail is kept intact.

    Additional guards (Bug 4):
    - If the trim marker fires BEFORE the first main modal in the sentence,
      the description is a complex NP+subordinate-then-modal structure; skip.
    - If the trimmed prefix has fewer than _TRIM_MIN_TOKENS content tokens or
      loses the modal, skip the trim.

    The evidence snippet is always the untrimmed source sentence; only the
    description field (used for label matching) is shortened here.
    """
    # Bug 6: strip leading markdown bold-prefix heads ('**Label**: ') before trimming.
    desc = _MARKDOWN_PREFIX_RE.sub("", desc).strip()
    m = _TRIM_MARKERS_RE.search(desc)
    if m is None:
        return desc
    tail = desc[m.start():]
    if _TRIM_GUARD_RE.search(tail):
        return desc
    # Guard: the trim must not fire before the main modal.
    # Find the first main modal position in the full description.
    modal_m = _MAIN_MODAL_RE.search(desc)
    if modal_m is not None and m.start() < modal_m.start():
        return desc
    candidate = desc[:m.start()].rstrip(".").rstrip(", ").strip()
    # Guard: the trimmed result must keep enough content tokens.
    if len(candidate.split()) < _TRIM_MIN_TOKENS:
        return desc
    # Guard: the trimmed result must still contain the main modal.
    if modal_m is not None and not _MAIN_MODAL_RE.search(candidate):
        return desc
    return candidate


# ---------------------------------------------------------------------------
# Item 6: first-person corporate subject resolution
#
# When a document declares a single unambiguous corporate operator (detectable
# from known_aliases by the presence of a corporate-suffix pattern), resolve
# leading "We " / "Our " subjects in the description to the operator name.
#
# Applies to the description only; evidence snippets remain verbatim.
# Skipped when known_aliases contains no corporate name, or more than one.
# ---------------------------------------------------------------------------

_CORPORATE_SUFFIX_RE = re.compile(
    r"\b(?:" + CORP_SUFFIX_ALT + r")\b",
    re.I,
)

# First-person subject prefixes to replace in description.
_FIRST_PERSON_RE = re.compile(r"^(We|Our)\s+", re.I)


def _resolve_first_person(desc: str, known_aliases: set[str], corporate_names: set[str] | None = None) -> str:
    """Replace a leading 'We '/'Our ' subject in *desc* with the single unambiguous
    corporate operator name, if exactly one exists.

    *corporate_names* (original-cased, populated by harvest_party_alias) is the
    primary lookup.  Falls back to *known_aliases* when corporate_names is None
    (e.g. list-block path that passes known_aliases directly).

    If zero or more than one corporate name exists, returns *desc* unchanged.
    Only the description field is modified; evidence snippets are never passed here.
    """
    if not _FIRST_PERSON_RE.match(desc):
        return desc
    if corporate_names is not None:
        candidates = list(corporate_names)
    else:
        # Fallback: scan known_aliases for corporate-suffix entries.
        candidates = [
            alias for alias in known_aliases
            if _CORPORATE_SUFFIX_RE.search(alias) and len(alias.split()) >= 2
        ]
    if len(candidates) != 1:
        return desc
    operator = candidates[0]
    return _FIRST_PERSON_RE.sub(operator + " ", desc)


# ---------------------------------------------------------------------------
# Bug 8: party legal-name → role-alias substitution in description subjects.
#
# When a document declares e.g. 'Northgate Acquisitions Corp. ("Purchaser")',
# an obligation sentence like 'Northgate Acquisitions Corp. shall deliver...'
# should be normalised to 'Purchaser shall deliver...' so the description
# subject matches the role-based label.
#
# Substitution applies to the description field only; evidence snippets are
# always verbatim source text.
#
# Strategy: try each known legal-name (longest first to avoid partial
# prefix matches) against the normalised start of the description; if found,
# replace with the title-cased role alias.
# ---------------------------------------------------------------------------

def _substitute_party_role(desc: str, party_role_map: dict[str, str]) -> str:
    """Replace a leading legal-name subject with its defined role alias.

    *party_role_map* maps norm(legal_name) → norm(role) and is populated by
    harvest_party_alias.  Only the description subject (prefix of the string)
    is substituted; evidence snippets are never passed here.

    The replacement is title-cased so 'purchaser' becomes 'Purchaser'.
    """
    if not party_role_map:
        return desc
    # Sort by length descending so longer names match before prefixes.
    for legal_name_norm, role_norm in sorted(
        party_role_map.items(), key=lambda x: len(x[0]), reverse=True
    ):
        if not legal_name_norm:
            continue
        # Check if description starts with the legal name (case-insensitive,
        # ignoring punctuation like trailing dots in 'Corp.').
        # We match on norm() of the description prefix rather than regex to
        # avoid escaping; compute a comparison window.
        token_count = len(legal_name_norm.split())
        words = desc.split()
        if len(words) < token_count:
            continue
        prefix_norm = norm(" ".join(words[:token_count]))
        # Strip trailing punctuation from the prefix before comparing.
        prefix_norm_clean = re.sub(r"[^\w\s]", "", prefix_norm).strip()
        if prefix_norm_clean == legal_name_norm or prefix_norm == legal_name_norm:
            role_display = role_norm.title()
            rest = " ".join(words[token_count:]).lstrip(".,; ")
            return role_display + (" " + rest if rest else "")
    return desc


# Defect E: explicit positive-modal patterns whose presence makes a sentence
# a near-certain obligation even when the subject is first-person or a
# collective noun not in known_aliases (e.g. "We", "All employees").
# These are canonical duty-imposing modals; the signal is added only for
# positive_obligation frame so other frames are unaffected.
# Includes FR modals (doit, doivent, devra, s'engage à, est tenu de) so that
# split obligations from FR conjunct/list patterns also gain explicit_modal.
_EXPLICIT_MODAL_RE = re.compile(
    r"\b(shall|must|(?:is|are)\s+required\s+to|(?:is|are)\s+obligated\s+to|"
    r"covenants?\s+to|undertakes\s+to|agrees?\s+to"
    r"|doit|doivent|devra|devront"
    r"|s['']\s*engage(?:nt)?\s+à"
    r"|est\s+tenu[e]?\s+de|sont\s+tenu[e]?s\s+de)\b",
    re.I,
)

# ---------------------------------------------------------------------------
# Defect B: lead-in detection
#
# A "lead-in" is a paragraph block whose text ends with a colon (optionally
# followed by whitespace) and whose block_type is "paragraph".  The items of
# the list that follows are the obligation items; the lead-in itself carries
# the subject and modal that must be prepended to each item.
# ---------------------------------------------------------------------------

# Colon-at-end-of-text detector (handles French « : » spacing too).
_COLON_TAIL_RE = re.compile(r":\s*$")

# Item 2c: lead-in connector phrase to strip before composing item descriptions.
# These trailing phrases ("as follows", "comme suit", "the following") introduce
# a list; they add noise to the composed description and dilute label matching.
_LEAD_IN_CONNECTOR_RE = re.compile(
    r"\s*(?:as\s+follows|comme\s+suit|the\s+following|les\s+suivants?|ce\s+qui\s+suit)\s*$",
    re.I,
)

# Modal-and-subject extractor for a lead-in sentence.  Group 1 = subject
# (everything before the modal); group 2 = modal + optional particles;
# group 3 = optional single verb word immediately after the modal (e.g. "pay",
# "deliver", "provide") used to build the composed item core.
_LEAD_IN_MODAL_RE = re.compile(
    r"^(?P<subject>.{1,120}?)\s+(?P<modal>"
    r"(?:shall|must|doit|doivent|devra|devront)"
    r"|(?:agrees?\s+to|s['']\s*engage(?:nt)?\s+à)"
    r"|(?:is\s+required\s+to|is\s+obligated\s+to)"
    r")\b\s*(?P<verb>[a-zÀ-ÿ]+)?",
    re.I,
)

# Pattern to detect that a lead-in has its own substantive content beyond the
# subject+modal+verb (i.e. has an amount or specific object that is also worth
# promoting as a standalone obligation).  Checks for: monetary amounts,
# specific noun phrases (not just a colon-tail), or date expressions.
_LEAD_IN_HAS_OWN_CONTENT_RE = re.compile(
    r"[$€£¥][\d,.]"
    r"|\b\d+[\d,.]*\s*(?:%|percent|per\s+cent)\b"
    r"|\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\b"
    r"|\b\d{4}-\d{2}-\d{2}\b"
    r"|\b\d{1,2}/\d{1,2}/\d{2,4}\b"
    r"|\bno\s+later\s+than\b",
    re.I,
)

# EN coordinated-conjunct splitter: ", and <Subject> <modal>..." or
# ", et <Sujet> <modal>..." -- splits obligation compound sentences.
# Group 1 = first conjunct (from sentence start), group 2 = second subject,
# group 3 = second modal + tail.
_CONJUNCT_SPLIT_RE = re.compile(
    r"^(?P<first_half>.+?)"
    r",\s+(?:and|et)\s+"
    r"(?P<second_subj>[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÿ''0-9.&, ]{1,80}?)\s+"
    r"(?P<second_modal>"
    r"(?:shall|must|doit|doivent|devra|devront)"
    r"|(?:agrees?\s+to|s['']\s*engage(?:nt)?\s+à)"
    r"|(?:is\s+required\s+to)"
    r")\b"
    r"(?P<second_tail>.+)$",
    re.I | re.DOTALL,
)

# FR "ainsi que" second-amount connector: splits "... X, ainsi que Y."
# Group 1 = first clause (carries subject+modal), group 2 = second amount.
_AINSI_QUE_RE = re.compile(
    r"^(?P<first_clause>.+?)"
    r",\s+ainsi\s+que\s+"
    r"(?P<second_part>.+)$",
    re.I | re.DOTALL,
)


def _obligation_frame_and_subject(
    sent: str, bundle: LexiconBundle
) -> Optional[tuple[str, re.Match[str], float, str]]:
    """Return (frame, match, base_confidence, subject) for the first matching
    obligation frame in *sent*, or None if no frame matches."""
    for frame, rx, base in bundle.obligation_patterns:
        m = rx.search(sent)
        if m:
            subject = extract_subject(sent, m.start())
            return frame, m, base, subject
    return None


def _make_obligation_value(
    subject: str,
    description: str,
    frame: str,
    bundle: LexiconBundle,
) -> dict[str, Any]:
    """Build the obligation candidate value dict.

    Item 5: applies _trim_obligation_description to the description field so
    trailing subordinate boilerplate (", in accordance with X", etc.) is
    stripped before matching.  The evidence snippet is always the verbatim
    source sentence passed separately.
    """
    trimmed_desc = _trim_obligation_description(description)
    return {
        "party": subject or "unspecified",
        "description": trimmed_desc,
        "kind": frame,
        "deadline": bundle.normalize_date(description) or deadline_text(description),
    }


def _add_obligation_candidate(
    add_candidate: Callable[..., None],
    bundle: LexiconBundle,
    frame: str,
    base: float,
    subject: str,
    description: str,
    evidence_text: str,
    source_ref: SourceRef,
    known_aliases: set[str],
    anti: list[str],
    extra_signals: Optional[list[str]] = None,
) -> None:
    """Emit a single obligation candidate."""
    signals = [frame, "obligation_strength"]
    norm_subject = subject.strip().lower()
    if norm_subject and any(
        norm_subject == alias or norm_subject.endswith(" " + alias) or alias.endswith(" " + norm_subject)
        for alias in known_aliases if alias
    ):
        signals.append("known_party_subject")
    if frame == "positive_obligation" and _EXPLICIT_MODAL_RE.search(description):
        signals.append("explicit_modal")
    if bundle.legal_action_verbs.search(description):
        signals.append("legal_action_object")
    if has_deadline_signal(description):
        signals.append("deadline_signal")
    signals.extend(heading_prior_signals(source_ref, "obligations"))
    if extra_signals:
        for sig in extra_signals:
            if sig not in signals:
                signals.append(sig)
    confidence = score_confidence(base, signals, anti)
    add_candidate(
        "obligations",
        frame,
        _make_obligation_value(subject, description, frame, bundle),
        evidence_text,
        source_ref,
        confidence,
        signals,
        anti,
    )


def harvest_obligation_list_blocks(
    blocks: list[Any],
    add_candidate: Callable[..., None],
    block_source_ref_fn: Callable[[Any], SourceRef],
    anti_fn: Callable[[str], list[str]],
    bundle_fn: Callable[[Any], LexiconBundle],
    known_aliases: set[str],
) -> set[int]:
    """Detect obligation lead-in+list patterns across consecutive blocks.

    Returns the set of block indices (lead-in paragraphs) that were expanded
    into per-item obligations.  The caller should skip these blocks from its
    normal sentence-level obligation harvesting to avoid double-promotion.

    A lead-in block is a paragraph whose text ends with ':' and that is followed
    by one or more list_item blocks.  Each list item is combined with the
    lead-in's subject+modal to produce one obligation per item.

    Evidence text for each item is the full combination (lead-in + item) so the
    span is always a verbatim source region.

    Item 2b: deduplicate promoted obligations on normalised description so that
    concurrent promotion paths (list pre-pass + sentence harvester) cannot emit
    the same obligation 2+ times.

    Item 2c: strip trailing connector phrases ("as follows", "comme suit",
    "the following") from the lead-in before composing item descriptions so the
    composed description reads naturally (e.g. "Purchaser shall pay A deposit
    of ..." not "Purchaser shall pay as follows A deposit of ...").
    """
    consumed: set[int] = set()
    # Item 2b: track normalised descriptions emitted this call to prevent duplicates.
    emitted_descs: set[str] = set()
    n = len(blocks)
    for i, blk in enumerate(blocks):
        if getattr(blk, "block_type", "") != "paragraph":
            continue
        text = str(getattr(blk, "text", "") or "").strip()
        if not _COLON_TAIL_RE.search(text):
            continue
        # Check if next non-empty block is a list item.
        j = i + 1
        while j < n and not str(getattr(blocks[j], "text", "") or "").strip():
            j += 1
        if j >= n or getattr(blocks[j], "block_type", "") != "list_item":
            continue
        # Collect the run of list_item blocks as (block, raw_text, desc_text) triples.
        # raw_text = verbatim stripped block text (used for evidence_text).
        # desc_text = raw_text with trailing list punctuation stripped (used for description).
        items: list[tuple[Any, str, str]] = []
        k = j
        while k < n and getattr(blocks[k], "block_type", "") == "list_item":
            raw_text = str(getattr(blocks[k], "text", "") or "").strip()
            desc_text = raw_text.rstrip(";,")
            if desc_text:
                items.append((blocks[k], raw_text, desc_text))
            k += 1
        if not items:
            continue
        # Determine the obligation frame and subject from the lead-in.
        bundle = bundle_fn(blk)
        result = _obligation_frame_and_subject(text, bundle)
        if result is None:
            continue
        frame, _match, base, subject = result
        # Skip junk lead-ins.
        if _is_junk_obligation(text):
            continue
        # Item 2c: strip colon tail then strip trailing connector phrase.
        lead_in_bare = _COLON_TAIL_RE.sub("", text).strip()
        lead_in_bare = _LEAD_IN_CONNECTOR_RE.sub("", lead_in_bare).strip()
        source_ref = block_source_ref_fn(blk)
        anti = anti_fn(text)
        consumed.add(i)

        # Bug 7 (a): when the lead-in carries its own amount/date, also promote
        # the lead-in alone as a standalone obligation.
        if _LEAD_IN_HAS_OWN_CONTENT_RE.search(lead_in_bare):
            norm_lead_in = " ".join(lead_in_bare.lower().split())
            if norm_lead_in not in emitted_descs:
                emitted_descs.add(norm_lead_in)
                _add_obligation_candidate(
                    add_candidate, bundle, frame, base, subject,
                    lead_in_bare, lead_in_bare, source_ref, known_aliases, anti,
                    extra_signals=["list_split", "lead_in_standalone"],
                )

        # Bug 7 (b): compute the composition core = subject + modal + optional verb.
        # Use the core (not the full lead-in) when composing item descriptions so
        # that extra content in the lead-in ("the Purchase Price of $12,500,000")
        # does not bleed into each composed item.
        lead_in_core = lead_in_bare  # fallback: full lead-in
        modal_m = _LEAD_IN_MODAL_RE.match(lead_in_bare)
        if modal_m:
            subj_part = modal_m.group("subject").strip()
            modal_part = modal_m.group("modal").strip()
            verb_part = (modal_m.group("verb") or "").strip()
            core_parts = [subj_part, modal_part]
            if verb_part:
                core_parts.append(verb_part)
            lead_in_core = " ".join(core_parts)

        for item_blk, item_raw, item_desc in items:
            # Compose the combined description: core lead-in + item text.
            combined = f"{lead_in_core} {item_desc}"
            # Item 2b: skip if this normalised description was already emitted.
            norm_combined = " ".join(combined.lower().split())
            if norm_combined in emitted_descs:
                continue
            emitted_descs.add(norm_combined)
            # Evidence must be verbatim source text: use the item block's raw text
            # and anchor the source_ref to the item block.
            item_source_ref = block_source_ref_fn(item_blk)
            _add_obligation_candidate(
                add_candidate,
                bundle,
                frame,
                base,
                subject,
                combined,
                item_raw,
                item_source_ref,
                known_aliases,
                anti,
                extra_signals=["list_split"],
            )
    return consumed


def harvest_obligation(ctx: HarvestContext, sent: str) -> None:
    if _is_fragment_sentence(sent):
        return
    if is_rep_warranty(sent) and not re.search(r"\bshall\s+(?:update|notify|cause|deliver|provide|file|submit)\b", sent, re.I):
        return
    if _is_junk_obligation(sent):
        return

    # ---------------------------------------------------------------------------
    # Defect B: Coordinated-conjunct splitting.
    #
    # Pattern: 'The Vendor agrees to sell, and the Purchaser agrees to purchase,
    # <shared object tail>...'  Each conjunct is an independent obligation; the
    # shared object tail (the remainder after the second modal) is appended to
    # both conjuncts so each obligation is complete and self-contained.
    #
    # The split is principled: the second conjunct must begin with a capitalised
    # subject followed by a modal from the bundle lexicon.  No fixture-keyed text.
    # ---------------------------------------------------------------------------
    conj_m = _CONJUNCT_SPLIT_RE.match(sent)
    if conj_m:
        first_half = conj_m.group("first_half").strip()
        second_subj = conj_m.group("second_subj").strip()
        second_modal = conj_m.group("second_modal").strip()
        raw_tail = conj_m.group("second_tail").strip()
        shared_tail = raw_tail
        # When the modal ends with "to"/"à", the tail may begin with
        # the second conjunct's own infinitive verb followed by a comma
        # (e.g. "purchase, <shared object>").  Strip that verb so the first
        # conjunct's description does not include it, but keep it for the
        # second conjunct so the obligation carries its own verb.
        second_verb: str = ""
        modal_ends_with_to = re.search(r"\b(?:to|à)\s*$", second_modal, re.I)
        if modal_ends_with_to:
            verb_comma_m = re.match(r"^([a-zÀ-ÿ]+),\s*", shared_tail, re.I)
            if verb_comma_m:
                second_verb = verb_comma_m.group(1)
                shared_tail = shared_tail[verb_comma_m.end():]
        second_tail = shared_tail.lstrip(",").strip()
        # Carry the shared object tail onto both conjuncts.
        first_desc = first_half + " " + second_tail if second_tail else first_half
        # Second conjunct: re-insert the verb so the obligation reads naturally
        # (e.g. "the Purchaser agrees to purchase all issued and outstanding shares").
        if second_verb and second_tail:
            second_desc = second_subj + " " + second_modal + " " + second_verb + " " + second_tail
        elif second_tail:
            second_desc = second_subj + " " + second_modal + " " + second_tail
        else:
            second_desc = second_subj + " " + second_modal + (" " + second_verb if second_verb else "")
        for conjunct_sent in (first_desc, second_desc):
            if _is_junk_obligation(conjunct_sent):
                continue
            result = _obligation_frame_and_subject(conjunct_sent, ctx.bundle)
            if result is None:
                continue
            frame, _m, base, subject = result
            signals = [frame, "obligation_strength", "conjunct_split"]
            if ctx.is_known_subject(subject):
                signals.append("known_party_subject")
            if frame == "positive_obligation" and _EXPLICIT_MODAL_RE.search(conjunct_sent):
                signals.append("explicit_modal")
            if ctx.bundle.legal_action_verbs.search(conjunct_sent):
                signals.append("legal_action_object")
            if has_deadline_signal(conjunct_sent):
                signals.append("deadline_signal")
            signals.extend(heading_prior_signals(ctx.source_ref, "obligations"))
            anti = ctx.anti
            confidence = score_confidence(base, signals, anti)
            ctx.add_candidate(
                "obligations",
                frame,
                _make_obligation_value(subject, conjunct_sent, frame, ctx.bundle),
                sent,
                ctx.source_ref,
                confidence,
                signals,
                anti,
            )
        return

    # ---------------------------------------------------------------------------
    # Defect B: FR "ainsi que" second-item splitting.
    #
    # Pattern: 'La défenderesse doit verser ... X, ainsi que des dommages-intérêts
    # de Y ...'.  The second clause introduced by "ainsi que" carries the same
    # subject+modal; emit two obligations, each self-contained.
    # ---------------------------------------------------------------------------
    ainsi_m = _AINSI_QUE_RE.match(sent)
    if ainsi_m:
        first_clause = ainsi_m.group("first_clause").strip()
        second_part = ainsi_m.group("second_part").strip()
        # Extract subject+modal from the first clause for the second.
        first_result = _obligation_frame_and_subject(first_clause, ctx.bundle)
        if first_result is not None:
            frame, _m, base, subject = first_result
            # Reconstruct second obligation: subject + modal + second_part.
            modal_m = _LEAD_IN_MODAL_RE.match(first_clause)
            if modal_m:
                modal_str = modal_m.group("modal")
                second_desc = f"{subject} {modal_str} {second_part}"
                for desc in (first_clause, second_desc):
                    if _is_junk_obligation(desc):
                        continue
                    result2 = _obligation_frame_and_subject(desc, ctx.bundle)
                    if result2 is None:
                        continue
                    f2, _m2, b2, subj2 = result2
                    signals2 = [f2, "obligation_strength", "ainsi_que_split"]
                    if ctx.is_known_subject(subj2):
                        signals2.append("known_party_subject")
                    if f2 == "positive_obligation" and _EXPLICIT_MODAL_RE.search(desc):
                        signals2.append("explicit_modal")
                    if ctx.bundle.legal_action_verbs.search(desc):
                        signals2.append("legal_action_object")
                    if has_deadline_signal(desc):
                        signals2.append("deadline_signal")
                    signals2.extend(heading_prior_signals(ctx.source_ref, "obligations"))
                    anti2 = ctx.anti
                    confidence2 = score_confidence(b2, signals2, anti2)
                    ctx.add_candidate(
                        "obligations",
                        f2,
                        _make_obligation_value(subj2, desc, f2, ctx.bundle),
                        sent,
                        ctx.source_ref,
                        confidence2,
                        signals2,
                        anti2,
                    )
            return

    # ---------------------------------------------------------------------------
    # Default single-sentence obligation harvesting.
    # ---------------------------------------------------------------------------
    for frame, rx, base in ctx.bundle.obligation_patterns:
        m = rx.search(sent)
        if not m:
            continue
        subject = extract_subject(sent, m.start())
        # Bug 9: passive voice (shall/must be <past-participle>) with a non-party
        # subject describes an object's state, not an actor's duty.  Skip these
        # unless the subject is a known party alias (e.g. "Employer shall be
        # notified" is party-subject despite passive voice).
        if (
            _PASSIVE_VOICE_RE.search(sent)
            and not ctx.is_known_subject(subject)
            and _NON_PARTY_DETERMINER_RE.match(sent.strip())
        ):
            continue
        # Bug 8: substitute leading legal-name subjects with their defined role
        # aliases BEFORE first-person resolution so 'We'/'Our' resolution (which
        # injects a corporate name) is not re-substituted back to the role.
        # Item 6: resolve leading "We"/"Our" to the single corporate operator.
        # Both applied to description only; evidence snippet (sent) stays verbatim.
        resolved_sent = _substitute_party_role(
            sent, getattr(ctx, "party_role_map", {})
        )
        resolved_sent = _resolve_first_person(
            resolved_sent, ctx.known_aliases, getattr(ctx, "corporate_names", None)
        )
        signals = [frame, "obligation_strength"]
        if ctx.is_known_subject(subject):
            signals.append("known_party_subject")
        # Defect E: explicit positive modal ("shall", "must", "are required to",
        # etc.) is self-corroborating for the positive_obligation frame.  Add
        # explicit_modal so has_corroboration() returns True even when the
        # subject is a collective noun or first-person pronoun that is not in
        # known_aliases.  Other frames (continuing_duty, best_efforts_duty, …)
        # are NOT boosted to avoid promoting generic maintenance / best-efforts
        # sentences without a party context.
        if frame == "positive_obligation" and _EXPLICIT_MODAL_RE.search(sent):
            signals.append("explicit_modal")
        if ctx.bundle.legal_action_verbs.search(sent):
            signals.append("legal_action_object")
        if has_deadline_signal(sent):
            signals.append("deadline_signal")
        signals.extend(heading_prior_signals(ctx.source_ref, "obligations"))
        anti = ctx.anti
        confidence = score_confidence(base, signals, anti)
        # Bundle date normalisation first (W3.3): EN is byte-identical to
        # deadline_text's date branch; FR yields ISO dates for the deadline.
        # Item 5: _make_obligation_value applies tail trimming to description.
        # Evidence snippet (sent) is verbatim; description uses resolved_sent
        # with trimming applied.
        ctx.add_candidate(
            "obligations",
            frame,
            _make_obligation_value(subject, resolved_sent, frame, ctx.bundle),
            sent,
            ctx.source_ref,
            confidence,
            signals,
            anti,
        )
        if frame == "procurement_duty":
            target = extract_procurement_target(sent)
            ctx.add_candidate("relationships", "procurement_edge", {"from_entity": subject or "unspecified", "to_entity": target or "controlled party", "type": "shall_cause", "description": sent}, sent, ctx.source_ref, confidence, [*signals, "shall_cause_edge"], anti)
        break
