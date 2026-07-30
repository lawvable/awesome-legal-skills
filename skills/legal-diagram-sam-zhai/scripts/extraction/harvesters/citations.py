from __future__ import annotations

import re
from typing import Any

from ..context import HarvestContext
from ..schema import SourceRef
from ..utils import score_confidence

# Paragraph cross-references -- internal, not authorities.  Not a citation
# pattern; stays in the harvester as a local filter.
_PARA_REF = re.compile(
    r"\b(?:at\s+)?para(?:s|graph(?:s)?)?\.\s*\d+(?:\s*[-–]\s*\d+)?\b",
    re.I,
)

# Own-citation metadata header: bold labels that introduce the document's own
# citation, not a cited authority.  Examples:
#   "**Citation:** 2025 ONSC 4812"   (EN judgment)
#   "**Référence :** Tremblay c. ..."  (FR judgment -- own document reference)
# Suppressed for EN (labels exclude own-citations); see harvester logic.
_OWN_CITATION_HEADER_RE = re.compile(
    r"^\*\*(?:Citation|Référence|Reference|Ref\.?)\s*:?\*\*\s*:?\s*",
    re.I,
)

# Bare section/article reference WITHOUT an accompanying act name.
# "section 7" or "s. 7" alone is an internal cross-reference; "section 7 of
# the Courts of Justice Act" names an act.  Demoted unless the sentence also
# has an Act-name pattern.
_ACT_NAME_INLINE_RE = re.compile(
    r"\b(?:[A-Z][A-Za-z]+ ){1,6}Act\b",
    re.I,
)

# CanLII citation pattern: "YYYY CanLII NNNN (court)"
_CANLII_RE = re.compile(
    r"\b((?:19|20)\d{2})\s+CanLII\s+\d+\s*\([^)]{2,25}\)",
    re.I,
)

# Act-name citation: "<Words> Act" optionally followed by a jurisdiction token.
#
# Pattern structure:
#   - First token: starts with uppercase letter (A-Z)
#   - Middle tokens (0-10): either starts with uppercase OR is a lowercase
#     function word (of, and, the, for, in, to, an, a, or, with, on, de, du,
#     des, et, la, le, les) -- allows "Courts of Justice Act",
#     "Personal Information Protection and Electronic Documents Act"
#   - Last token before jurisdiction: the literal word "Act"
#   - Optional: (Canada), (Ontario), etc.
#   - Optional: R.S.O. / S.C. / L.R.C. + year + chapter citation
#
# Guard: entire match must start at a word boundary and the first captured word
# must be uppercase-initial so we don't match mid-sentence fragments.
_ACT_CITATION_RE = re.compile(
    r"\b([A-Z][A-Za-z0-9]+"
    r"(?:\s+(?:[A-Z][A-Za-z0-9]*|of|and|the|for|in|to|an|a|or|with|on)){0,10}"
    r"\s+Act)\b"
    r"(?:\s*\([A-Za-z ,]+?\))?"              # optional jurisdiction "(Canada)" etc.
    r"(?:,\s*(?:R\.S\.O\.|S\.C\.|L\.R\.C\.|R\.S\.C\.|R\.S\.Q\.|S\.Q\.|RLRQ)"
    r"\s*\(?\d{4}\)?,?\s*(?:c\.|ch\.)\s*[A-Z0-9.\-]+)?",  # optional statutory citation tail
)

# Classic case name WITHOUT a following year/citation: harvested when the
# sentence has a legal-authority context word (principle, test, rule, case,
# held, applied).  Confidence is lower (0.62) because no year corroborates.
_LEGAL_CONTEXT_RE = re.compile(
    r"\b(principle|test|rule|doctrine|standard|held|applied|confirmed|affirmed"
    r"|refined|set\s+out|established|case|decision|authority|judgment"
    r"|principe|critère|règle|affaire|arrêt)\b",
    re.I,
)

# Parenthetical case name pattern: "Victoria Laundry (Windsor) Ltd. v. Newman Industries Ltd."
# The EN case_citation pattern requires a following year; this supplements it
# for sentences where the case name appears without an adjacent year but the
# sentence has legal context.
# Uses token-based run to avoid capturing sentence-prefix context.
_CASE_NAME_WITH_PAREN_RE = re.compile(
    r"\b([A-Z][A-Za-z0-9.'&-]+"  # first capital token
    r"(?:\s+(?:[A-Z][A-Za-z0-9.'&-]+|of|the|de|du|and|&))*"  # optional more tokens
    r"\s+\([A-Za-z ]+\)"            # parenthetical qualifier "(Windsor)"
    r"(?:\s+[A-Z][A-Za-z0-9.'&-]+)+"  # suffix tokens like "Ltd."
    r"\s+v\.?\s+"                   # separator
    r"[A-Z][A-Za-z0-9.'&-]+"       # first respondent token
    r"(?:\s+(?:[A-Z][A-Za-z0-9.'&-]+|of|the|de|du|and|&|[A-Za-z0-9.'&-]+))*"  # respondent run
    r"[A-Za-z0-9.])"               # ensure ends with alnum
    r"(?=[,\s]|$)",
    re.MULTILINE,
)

# Case name without parenthetical, no following year -- requires legal context.
# Pattern: one or more capitalized tokens (optionally joined by lowercase
# prepositions "of", "v", "de") followed by "v." then another capitalized run.
# Excludes sentences where a year follows within 30 chars (those are handled
# by the main case_citation pattern above).
# Token = capital letter start + alphanumeric/dot/apostrophe (no spaces to
# prevent matching sentence fragments).
_CASE_NAME_TOKEN = r"[A-Z][A-Za-z0-9.'&-]*"
_CASE_NAME_WORD_RUN = (
    r"(?:" + _CASE_NAME_TOKEN + r")"
    r"(?:\s+(?:of|the|de|du|and|&|" + _CASE_NAME_TOKEN + r"))*"
)
_CASE_NAME_NO_YEAR_RE = re.compile(
    r"\b(" + _CASE_NAME_WORD_RUN + r")"
    r"\s+v\.?\s+"
    r"(" + _CASE_NAME_WORD_RUN + r"[A-Za-z0-9.])"
    r"(?=[,\s]|$)"
    r"(?!.{0,50}(?:19|20)\d{2})",  # no year within 50 chars (handled by main pattern)
    re.MULTILINE | re.DOTALL,
)


def _is_own_citation_header(sent: str) -> bool:
    """Return True when *sent* is a metadata citation-header line."""
    return bool(_OWN_CITATION_HEADER_RE.match(sent.strip()))


def _has_act_name(sent: str) -> bool:
    """Return True when *sent* names a statute (Act-name present)."""
    return bool(_ACT_NAME_INLINE_RE.search(sent))


# Compiled pattern for _clean_case_name: extracts the trailing "Name v. Name"
# portion from an over-captured case citation string.
# Used to strip prefix context like "The Court set out in" from the front.
_CLEAN_CASE_RE = re.compile(
    r"\b(" + _CASE_NAME_WORD_RUN + r"(?:\s+\([A-Za-z ]+\))?(?:\s+" + _CASE_NAME_TOKEN + r")*)"
    r"\s+(?P<connector>[vc]\.?)\s+"
    r"(" + _CASE_NAME_WORD_RUN + r"[A-Za-z0-9.]?)\s*$",
    re.DOTALL,
)


# Stopwords that can appear as the first token of an over-captured case name
# prefix, but are not valid starts of a party name.  When the RIGHTMOST
# "Name v./c. Name" match's first token is one of these, retry with the
# next possible start position.
_CASE_NAME_INTRO_STOPWORDS = frozenset({
    "applying", "applied", "see", "in", "per", "under", "using",
    "following", "citing", "noting", "compare", "cf", "the", "a", "an",
    "this", "these", "those", "for", "on", "at", "by", "as", "or", "and",
})


def _clean_case_name(raw: str) -> str:
    """Extract the genuine case name from a possibly over-captured match.

    The EN/FR case_citation patterns capture from the first capital letter in
    the sentence through 'v./c. Respondent', which can include sentence-prefix
    context like 'The applicable standard for assessing ... is set out in'
    or 'Applying Renwick...'.

    Strategy:
    1. Strip any leading tokens that are known intro stopwords (verbs, articles).
    2. Apply _CLEAN_CASE_RE to the stripped text to find 'Name v. Name'.
    3. Fall back to the raw stripped string.
    """
    s = raw.strip().rstrip(".,;")
    # Step 1: strip leading stopword tokens iteratively
    tokens = s.split()
    while tokens and tokens[0].lower().rstrip(".") in _CASE_NAME_INTRO_STOPWORDS:
        tokens = tokens[1:]
    s = " ".join(tokens)
    if not s:
        return raw.strip().rstrip(".,;")
    # Step 2: _CLEAN_CASE_RE extracts 'Name v./c. Name' from the (now shorter) string
    m = _CLEAN_CASE_RE.search(s)
    if m:
        claimant = m.group(1).strip()
        connector = m.group("connector")
        respondent = m.group(3).strip()
        return f"{claimant} {connector} {respondent}".rstrip(".,;")
    # Step 3: fallback
    return s.rstrip(".,;")


def harvest_citation(ctx: HarvestContext, sent: str) -> None:
    """Detect legal authorities in *sent* and emit legal_authorities candidates.

    W6 T4 additions:
    - Compose case name + adjacent neutral citation into ONE candidate.
    - Demote own-citation metadata header lines (EN: suppress; FR: allow if
      the labels include the own-citation, but resolver dedup handles it).
    - Demote bare section/article refs that lack an accompanying act name.
    - Harvest Act-name citations (Courts of Justice Act, Competition Act, etc.).
    - Harvest CanLII citations.
    - Harvest classic case names without neutral citation when legal context present.
    """
    anti = ctx.anti
    # Index contract (per LexiconBundle.citation_patterns):
    # [0] neutral_citation, [1] case_citation, [2] statutory_ref, [3] rule_ref
    neutral_citation = ctx.bundle.citation_patterns[0]
    case_citation = ctx.bundle.citation_patterns[1]
    statutory_ref = ctx.bundle.citation_patterns[2]
    rule_ref = ctx.bundle.citation_patterns[3]

    # --- Own-citation header detection ---
    # EN own-citation metadata (**Citation:** ...) is not a cited authority;
    # demote it by treating the whole sentence as an anti-signal.  FR own-
    # citation headers (Référence) also excluded because the labels for
    # fr_judgment show the case name is cited in the body text too, so the
    # body-text hit is the authoritative candidate.
    is_own_header = _is_own_citation_header(sent)
    if is_own_header:
        # Skip this sentence entirely for legal_authorities -- it is metadata.
        return

    # --- Case + neutral citation composition ---
    # The case_citation regex may fire on a sentence like:
    #   "Morin c. Entreprises Casgrain, 2026 QCCA 217"
    # and the neutral_citation regex may ALSO fire on "2026 QCCA 217" in that
    # same sentence.  Compose them into ONE candidate; suppress the bare
    # neutral citation when a case name was found in the same sentence.
    case_matches: list[str] = []
    for m in case_citation.finditer(sent):
        full_match = m.group(0).strip().rstrip(".")
        if _PARA_REF.search(full_match):
            continue
        # W6 T4: The EN case_citation pattern can over-capture prefix context
        # ("The applicable standard... is set out in Renwick...").  Clean the
        # captured match to extract just the trailing "Name v. Name" portion.
        cleaned = _clean_case_name(full_match)
        case_matches.append(cleaned)

    neutral_matches: list[str] = []
    for m in neutral_citation.finditer(sent):
        neutral_matches.append(m.group(0))

    if case_matches and neutral_matches:
        # Compose: pair each case match with the adjacent neutral citation.
        # Strategy: build one composed entry per case match, appending the
        # nearest neutral citation.  If counts differ, emit the leftover
        # neutral citations separately (they may be stand-alone citations).
        used_neutrals: set[int] = set()
        for case_text in case_matches:
            # Find the first unused neutral citation that appears AFTER the
            # case name in the sentence, or if none, take the first unused.
            case_pos = sent.find(case_text)
            paired_idx: int | None = None
            for ni, nc in enumerate(neutral_matches):
                if ni in used_neutrals:
                    continue
                nc_pos = sent.find(nc)
                # Accept if neutral citation is adjacent (within 50 chars)
                if abs(nc_pos - (case_pos + len(case_text))) <= 50:
                    paired_idx = ni
                    break
            if paired_idx is None:
                # No adjacent neutral -- try first unused as fallback
                for ni in range(len(neutral_matches)):
                    if ni not in used_neutrals:
                        paired_idx = ni
                        break
            if paired_idx is not None:
                used_neutrals.add(paired_idx)
                composed = f"{case_text}, {neutral_matches[paired_idx]}"
            else:
                composed = case_text
            signals = ["case_citation", "neutral_citation", "citation_signal"]
            confidence = score_confidence(0.86, signals, anti)
            ctx.add_candidate(
                "legal_authorities",
                "neutral_citation",
                {"citation": composed, "authority_type": "case", "jurisdiction": None},
                sent,
                ctx.source_ref,
                confidence,
                signals,
                anti,
            )
        # Emit leftover neutral citations (not paired with a case match)
        for ni, nc in enumerate(neutral_matches):
            if ni not in used_neutrals:
                signals = ["neutral_citation", "citation_signal"]
                ctx.add_candidate(
                    "legal_authorities",
                    "neutral_citation",
                    {"citation": nc, "authority_type": "case", "jurisdiction": None},
                    sent,
                    ctx.source_ref,
                    0.86,
                    signals,
                    anti,
                )
    elif neutral_matches:
        # No case match -- emit neutral citations on their own
        for nc in neutral_matches:
            signals = ["neutral_citation", "citation_signal"]
            ctx.add_candidate(
                "legal_authorities",
                "neutral_citation",
                {"citation": nc, "authority_type": "case", "jurisdiction": None},
                sent,
                ctx.source_ref,
                0.86,
                signals,
                anti,
            )
    else:
        # Case matches with NO neutral citation -- emit each case match alone
        for case_text in case_matches:
            signals = ["case_citation", "citation_signal"]
            confidence = score_confidence(0.70, signals, anti)
            ctx.add_candidate(
                "legal_authorities",
                "case_citation",
                {"citation": case_text, "authority_type": "case", "jurisdiction": None},
                sent,
                ctx.source_ref,
                confidence,
                signals,
                anti,
            )

    # --- CanLII citation ---
    # Harvest "YYYY CanLII NNNN (court)" and compose with adjacent case name.
    # The case name appears in the text BEFORE the CanLII year.  Extract it by
    # scanning backwards from the CanLII match position.
    # Uses token-based case name pattern to avoid capturing sentence-prefix
    # context ("The Court also considered...").
    for m in _CANLII_RE.finditer(sent):
        citation_text = m.group(0)
        # Find adjacent case name: look back from the CanLII year's position.
        # We scan the prefix for a "Name v./c. Name" using the same token-based
        # approach to avoid matching "The Court also considered Transamerica..."
        pos = m.start()
        prefix = sent[:pos].rstrip(" ,\n")
        # Build a right-anchored pattern: token runs joined by "v." or "c."
        # Each token = [A-Z][A-Za-z0-9.'&-]* (no spaces within token)
        # Allow "of", "the" prepositions between tokens on each side
        _CANLII_CASE_RE = re.compile(
            r"\b("
            + _CASE_NAME_WORD_RUN
            + r"(?:\s+\([A-Za-z ]+\))?"     # optional parenthetical "(ON SC)"
            + r"(?:\s+" + _CASE_NAME_TOKEN + r")*"  # suffix tokens
            + r"\s+[vc]\.\s+"
            + _CASE_NAME_WORD_RUN
            + r"[A-Za-z0-9.]"
            + r")\s*$",
            re.DOTALL,
        )
        case_m = _CANLII_CASE_RE.search(prefix)
        if case_m:
            composed_case = case_m.group(1).strip().rstrip(",. ")
            citation_text = f"{composed_case}, {citation_text}"
        signals = ["neutral_citation", "citation_signal"]
        ctx.add_candidate(
            "legal_authorities",
            "neutral_citation",
            {"citation": citation_text, "authority_type": "case", "jurisdiction": None},
            sent,
            ctx.source_ref,
            0.84,
            signals,
            anti,
        )

    # --- Statutory section reference ---
    # Demote bare section/article refs that lack an act name AND a statutory
    # citation context (like "pursuant to", "under", "as defined in").
    # Internal agreement cross-references ("Article 5", "section 7") lack both
    # and should be demoted.  "Pursuant to section 12(1)(a)" has statutory
    # context and should promote even without an explicit act name.
    _STATUTORY_CONTEXT_RE = re.compile(
        r"\b(pursuant\s+to|under\s+(?:the\s+)?(?:provisions?\s+of\s+)?(?:section|s\.)"
        r"|as\s+defined\s+(?:in|under)\s+(?:the\s+)?(?:section|s\.)"
        r"|within\s+the\s+meaning\s+of\s+(?:section|s\.)"
        r"|section\s+\d+\s+(?:of\s+the\s+[A-Z]|provides|states|requires|prohibits)"
        # FR statutory citation contexts
        r"|en\s+vertu\s+de|aux\s+termes\s+(?:de\s+)?l['']art"
        r"|selon\s+l['']art|conformément\s+(?:à\s+)?l['']art"
        r"|C\.c\.Q\.|Code\s+civil"
        r")\b",
        re.I,
    )
    # Anti-context: "of this Agreement/Contract" signals an internal cross-reference
    # even when a statutory context keyword is also present.
    _INTERNAL_REF_RE = re.compile(
        r"\bof\s+(?:this|the)\s+(?:Agreement|Contract|Deed|Plan|Policy|Order)\b",
        re.I,
    )
    for m in statutory_ref.finditer(sent):
        citation_text = m.group(0)
        has_act = _has_act_name(sent)
        has_context = bool(_STATUTORY_CONTEXT_RE.search(sent))
        is_internal = bool(_INTERNAL_REF_RE.search(sent))
        # Demote when: no act name AND (no statutory context OR clearly internal)
        if not has_act and (not has_context or is_internal):
            # Bare internal cross-reference (e.g. "section 7", "Article 5")
            # without act name or statutory context -- demote below HINT_MIN.
            ctx.add_candidate(
                "legal_authorities",
                "statutory_reference",
                {"citation": citation_text, "authority_type": "statute", "jurisdiction": None},
                sent,
                ctx.source_ref,
                0.35,  # below HINT_MIN threshold -- suppressed
                ["statutory_reference"],
                [*anti, "bare_section_no_act"],
            )
        else:
            signals = ["statutory_reference", "citation_signal"]
            confidence = score_confidence(0.78, signals, anti)
            ctx.add_candidate(
                "legal_authorities",
                "statutory_reference",
                {"citation": citation_text, "authority_type": "statute", "jurisdiction": None},
                sent,
                ctx.source_ref,
                confidence,
                signals,
                anti,
            )

    # --- Rule / Article reference ---
    # Demote bare "Article N" / "Rule N" that lack an act/agreement name
    # AND appear in a conditions/deliverables context (internal cross-reference).
    for m in rule_ref.finditer(sent):
        citation_text = m.group(0)
        if not _has_act_name(sent):
            # Internal cross-reference -- demote.
            ctx.add_candidate(
                "legal_authorities",
                "rule_reference",
                {"citation": citation_text, "authority_type": "rule", "jurisdiction": None},
                sent,
                ctx.source_ref,
                0.35,  # suppressed
                ["rule_reference"],
                [*anti, "bare_article_no_act"],
            )
        else:
            signals = ["rule_reference", "citation_signal"]
            confidence = score_confidence(0.72, signals, anti)
            ctx.add_candidate(
                "legal_authorities",
                "rule_reference",
                {"citation": citation_text, "authority_type": "rule", "jurisdiction": None},
                sent,
                ctx.source_ref,
                confidence,
                signals,
                anti,
            )

    # --- Act-name citations ---
    # Harvest "Courts of Justice Act, R.S.O. 1990, c. C.43" and similar.
    for m in _ACT_CITATION_RE.finditer(sent):
        act_text = m.group(0).strip().rstrip(",")
        if len(act_text) < 5:
            continue
        signals = ["act_citation", "citation_signal"]
        confidence = score_confidence(0.80, signals, anti)
        ctx.add_candidate(
            "legal_authorities",
            "act_citation",
            {"citation": act_text, "authority_type": "statute", "jurisdiction": None},
            sent,
            ctx.source_ref,
            confidence,
            signals,
            anti,
        )

    # --- Classic case name without neutral citation ---
    # Harvest case names that appear WITHOUT a following year/neutral citation.
    # These are classic common-law names like "Hadley v. Baxendale" or names
    # with parentheticals like "Victoria Laundry (Windsor) Ltd. v. Newman
    # Industries Ltd.".
    #
    # Strategy: always run when the sentence has legal context, regardless of
    # whether other year-bearing cases were already found.  Skip any case name
    # already captured in case_matches (it had a year and is already emitted).
    if _LEGAL_CONTEXT_RE.search(sent):
        # Build set of already-captured case name texts for dedup
        already_captured: set[str] = set(case_matches)

        # Try parenthetical form first (higher priority / more specific)
        parenthetical_hits: list[str] = []
        for m in _CASE_NAME_WITH_PAREN_RE.finditer(sent):
            case_text = m.group(0).strip().rstrip(".")
            if _PARA_REF.search(case_text):
                continue
            # Skip if this name was already captured as a year-bearing match
            if any(case_text in captured or captured in case_text
                   for captured in already_captured):
                continue
            parenthetical_hits.append(case_text)
            signals = ["case_citation", "citation_signal", "legal_context"]
            # Use 0.70 base: classic case + legal context = reliable authority.
            confidence = score_confidence(0.70, signals, anti)
            ctx.add_candidate(
                "legal_authorities",
                "case_citation",
                {"citation": case_text, "authority_type": "case", "jurisdiction": None},
                sent,
                ctx.source_ref,
                confidence,
                signals,
                anti,
            )

        # Non-parenthetical form (no following year)
        for m in _CASE_NAME_NO_YEAR_RE.finditer(sent):
            full_match = m.group(0).strip().rstrip(".")
            if _PARA_REF.search(full_match):
                continue
            # Skip if already captured by main case_citation pass (had a year)
            if any(full_match in captured or captured in full_match
                   for captured in already_captured):
                continue
            # Skip if already covered by parenthetical pass above
            if any(full_match in p or p in full_match for p in parenthetical_hits):
                continue
            signals = ["case_citation", "citation_signal", "legal_context"]
            # Use 0.70 base: classic case + legal context = reliable authority.
            confidence = score_confidence(0.70, signals, anti)
            ctx.add_candidate(
                "legal_authorities",
                "case_citation",
                {"citation": full_match, "authority_type": "case", "jurisdiction": None},
                sent,
                ctx.source_ref,
                confidence,
                signals,
                anti,
            )


# ---------------------------------------------------------------------------
# Block-level citation harvester
# ---------------------------------------------------------------------------
# Two citation patterns span abbreviations that the sentence splitter would
# fragment, making per-sentence harvesting impossible:
#
#  1. CanLII where the case name contains "Co." (e.g. "Canada Life Assurance
#     Co., 1996 CanLII 7979 (ON SC)").
#  2. Classic case names with "v." that span what would be a sentence split
#     (e.g. "Hadley v. Baxendale" in "...Hadley v.\nBaxendale principle...").
#
# To avoid adding "Co." and "v." to ABBREVIATION_GUARDS_EN (which would
# violate the W0.6 seeded-guard contract of exactly 7 EN guards), we run a
# SEPARATE block-level pass on the full paragraph text BEFORE sentence
# splitting.  This mirrors how harvest_litigation_captions runs on the full
# block text.
#
# Candidates emitted here may overlap with per-sentence candidates; the
# resolver deduplicates by semantic_key so no double-counting occurs.

# Suffix-only tokens that cannot stand alone as a claimant name.
# If the last token before "v." is one of these, the pattern matched a
# fragment like "Ltd. v. Newman ..." which is not a real party name.
_COMPANY_SUFFIX_ONLY: frozenset[str] = frozenset({
    "ltd", "inc", "co", "corp", "llc", "llp",
})

# Compiled once at module level for performance.
_CANLII_CASE_BLOCK_RE = re.compile(
    r"\b("
    + _CASE_NAME_WORD_RUN
    + r"(?:\s+\([A-Za-z ]+\))?"     # optional parenthetical
    + r"(?:\s+" + _CASE_NAME_TOKEN + r")*"  # suffix tokens (e.g. "Co.")
    + r"\s+[vc]\.\s+"
    + _CASE_NAME_WORD_RUN
    + r"[A-Za-z0-9.]"
    + r")\s*$",
    re.DOTALL,
)


def _is_valid_case_name(text: str) -> bool:
    """Return True if *text* is a plausible case name (not just a suffix token).

    Guards against spurious matches like "Ltd. v. Newman Industries Ltd." where
    the claimant side is only a company-suffix abbreviation.
    """
    # Split off the "v." connector
    parts = re.split(r"\s+[vc]\.\s+", text, maxsplit=1)
    if not parts:
        return False
    claimant = parts[0].strip()
    # Strip trailing punctuation
    claimant = claimant.rstrip(".,")
    # Last token of claimant (what comes right before "v.")
    claimant_tokens = claimant.split()
    if not claimant_tokens:
        return False
    last_token = claimant_tokens[-1].rstrip(".,").lower()
    # Reject if the entire claimant is just a suffix abbreviation
    if len(claimant_tokens) == 1 and last_token in _COMPANY_SUFFIX_ONLY:
        return False
    # Require at least 2 tokens OR the first token is a real word (not just "Ltd.")
    first_token = claimant_tokens[0].rstrip(".,").lower()
    if len(claimant_tokens) == 1 and first_token in _COMPANY_SUFFIX_ONLY:
        return False
    return True


def harvest_citation_block(
    add_candidate: Any,
    text: str,
    source_ref: SourceRef,
    anti: list[str],
) -> None:
    """Harvest CanLII and classic case citations from full block text.

    Operates on the unsplit paragraph text so that abbreviation-boundary
    fragments ("Co.", "v.") do not prevent composition.  Candidates emitted
    here may overlap with per-sentence candidates; the resolver deduplicates
    by semantic_key.
    """
    # 1. CanLII with adjacent case name (handles "Co." splits)
    for m in _CANLII_RE.finditer(text):
        citation_text = m.group(0)
        pos = m.start()
        prefix = text[:pos].rstrip(" ,\n")
        case_m = _CANLII_CASE_BLOCK_RE.search(prefix)
        if case_m:
            composed_case = case_m.group(1).strip().rstrip(",. ")
            citation_text = f"{composed_case}, {citation_text}"
        signals = ["neutral_citation", "citation_signal"]
        add_candidate(
            "legal_authorities",
            "neutral_citation",
            {"citation": citation_text, "authority_type": "case", "jurisdiction": None},
            text[:min(len(text), pos + len(m.group(0)) + 40)],
            source_ref,
            0.84,
            signals,
            anti,
        )

    # 2. Classic case names with "v." (handles sentence-boundary "v." splits)
    if _LEGAL_CONTEXT_RE.search(text):
        # Parenthetical form: "Victoria Laundry (Windsor) Ltd. v. Newman Industries Ltd."
        for m in _CASE_NAME_WITH_PAREN_RE.finditer(text):
            case_text = m.group(0).strip().rstrip(".")
            if _PARA_REF.search(case_text):
                continue
            if not _is_valid_case_name(case_text):
                continue
            signals = ["case_citation", "citation_signal", "legal_context"]
            confidence = score_confidence(0.70, signals, anti)
            add_candidate(
                "legal_authorities",
                "case_citation",
                {"citation": case_text, "authority_type": "case", "jurisdiction": None},
                case_text,
                source_ref,
                confidence,
                signals,
                anti,
            )
        # Simple form: "Hadley v. Baxendale"
        for m in _CASE_NAME_NO_YEAR_RE.finditer(text):
            full_match = m.group(0).strip().rstrip(".")
            if _PARA_REF.search(full_match):
                continue
            if not _is_valid_case_name(full_match):
                continue
            signals = ["case_citation", "citation_signal", "legal_context"]
            confidence = score_confidence(0.70, signals, anti)
            add_candidate(
                "legal_authorities",
                "case_citation",
                {"citation": full_match, "authority_type": "case", "jurisdiction": None},
                full_match,
                source_ref,
                confidence,
                signals,
                anti,
            )
