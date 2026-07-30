from __future__ import annotations

import re

from ..context import HarvestContext
from ..lexicon.base import LexiconBundle
from ..utils import clean_entity, clean_role, extract_entity_like_names, infer_role_from_text, norm
from ._patterns import CORP_SUFFIX_ALT

# ---------------------------------------------------------------------------
# Privacy party frames (W6 T3)
# ---------------------------------------------------------------------------

# Policy-operator declaration: "how X collects..." or "X (\"we\", ...)" org header.
_PRIVACY_OPERATOR_RE = re.compile(
    r"(?:(?:Policy|Notice)\s+describes\s+how\s+|"
    r"Privacy\s+Policy\s+describes\s+how\s+)"
    r"(?P<name>[A-Z][A-Za-zÀ-ÿ0-9.&'', \-]+?\s+"
    r"(?:" + CORP_SUFFIX_ALT + r"))\b",
    re.I,
)

# Organisation header bold: "**Organization:** X Inc."
_PRIVACY_ORG_HEADER_RE = re.compile(
    r"\*\*Organ(?:ization|isation)\*\*\s*[:\-]\s*"
    r"(?P<name>[A-Z][A-Za-zÀ-ÿ0-9.&'', \-]+?\s+"
    r"(?:" + CORP_SUFFIX_ALT + r"))\b",
    re.I,
)

# Service-provider / disclosed-recipient enumeration:
# "- **Name Corp.**: receives ... data" or "**Name Corp.**: ..." (bullet stripped by MD parser)
# The Markdown adapter strips the leading "- " bullet from list_item blocks, so
# both patterns must be accepted.
_SERVICE_PROVIDER_LIST_RE = re.compile(
    r"^(?:\s*[-*]\s+)?\*\*"
    r"(?P<name>[A-Z][A-Za-zÀ-ÿ0-9.&'', \-]+?\s+"
    r"(?:" + CORP_SUFFIX_ALT + r"))"
    r"\*\*\s*:",
)

# Inline disclosure: "to X Corp." / "through our integration with X Corp."
_INLINE_SERVICE_PROVIDER_RE = re.compile(
    r"(?:transfers?\s+(?:personal\s+information\s+to|data\s+to)|"
    r"integration\s+with|processor,\s+|payment\s+processor,\s+)"
    r"(?P<name>[A-Z][A-Za-zÀ-ÿ0-9.&'', \-]+?\s+"
    r"(?:" + CORP_SUFFIX_ALT + r"))",
    re.I,
)

# Leading words that may appear as sentence-initial capitals but are not party
# names.  Stripped from the front of a captured caption side iteratively so
# that "In re The Estate" reduces to "Estate" rather than keeping "In".
_CAPTION_LEADING_STOPWORDS = frozenset({
    "in", "the", "on", "at", "for", "see", "per", "under",
    "re", "between", "cf", "compare",
})

# Words that indicate the captured "name" is a sentence fragment, not a
# corporate name.  If a captured name starts with one of these (case-insensitive),
# it is rejected from party promotion.
_SENTENCE_OPENER_STOPWORDS = frozenset({
    "this", "these", "the", "a", "an", "pursuant", "entered", "herein",
    "whereby", "whereas", "now", "therefore", "in", "on", "at", "by",
    "as", "for", "with", "to", "from", "between", "among",
    "and", "or", "but",
})

# Maximum token count for a valid corporate party name (principled threshold:
# real corporate names are ≤ 10 words; sentence fragments are longer).
_MAX_PARTY_NAME_TOKENS = 10

# Compiled corporate-suffix word-boundary check used when recording corporate
# names into ctx.corporate_names for first-person resolution (Item 6).
_CORP_SUFFIX_INLINE_RE = re.compile(r"\b(?:" + CORP_SUFFIX_ALT + r")\b", re.I)


def _is_sentence_fragment_name(name: str) -> bool:
    """Return True if *name* looks like a sentence fragment rather than a party name.

    Checks: (1) first token is a sentence-opener stopword; (2) name has more
    than _MAX_PARTY_NAME_TOKENS whitespace-delimited tokens.
    """
    tokens = name.split()
    if not tokens:
        return True
    if tokens[0].lower() in _SENTENCE_OPENER_STOPWORDS:
        return True
    if len(tokens) > _MAX_PARTY_NAME_TOKENS:
        return True
    return False


# Module-level compiled pattern for _last_corporate_name: 1-6 strictly
# CAPITALISED word tokens + corporate suffix.  Hoisted from per-call re.compile.
# Note: NOT case-insensitive -- each token must start with a literal uppercase
# letter to prevent matching lowercase-word runs ("into by and among Corp").
_LAST_CORP_NAME_RE = re.compile(
    r"(?<!\w)([A-Z][A-Za-zÀ-ÿ0-9.&'-]*(?:\s+[A-Z][A-Za-zÀ-ÿ0-9.&'-]*){0,5}"
    r"\s+(?:" + CORP_SUFFIX_ALT + r"))"
    r"(?!\s+\w)",
)


def _last_corporate_name(name: str) -> str:
    """Extract the trailing corporate name token run from a sentence fragment.

    When the defined_party_markers regex captures a sentence prefix such as
    'This Share Purchase Agreement is entered into by and among Northgate
    Acquisitions Corp', this function returns just 'Northgate Acquisitions Corp'
    by locating the LAST run of 1-6 capitalized tokens ending in a corporate suffix.
    """
    last_match = None
    for m in _LAST_CORP_NAME_RE.finditer(name):
        last_match = m
    if last_match:
        candidate = clean_entity(last_match.group(1))
        # Only accept if it looks shorter (fewer words) than the input.
        if candidate and len(candidate.split()) <= 6:
            return candidate
    return name


def _clean_caption_side(raw: str) -> str:
    """Strip trailing punctuation, whitespace, and leading function words."""
    s = raw.strip().rstrip(".,;: ")
    # Strip consecutive leading stop words (one pass, case-insensitive).
    tokens = s.split()
    while tokens and tokens[0].lower() in _CAPTION_LEADING_STOPWORDS:
        tokens = tokens[1:]
    return " ".join(tokens)


def harvest_party_alias(ctx: HarvestContext, sent: str) -> None:
    anti = ctx.anti
    # Work item 3: global dedup set across all party frames within one sentence.
    seen_names: set[str] = set()

    for rx in ctx.bundle.defined_party_markers:
        for m in rx.finditer(sent):
            raw_name = clean_entity(m.group("name"))
            role = clean_role(m.group("role"))
            if not raw_name or not role:
                continue
            # Reject sentence-fragment names; attempt to recover the trailing
            # corporate name when the match captured a sentence prefix.
            if _is_sentence_fragment_name(raw_name):
                raw_name = _last_corporate_name(raw_name)
                if not raw_name or _is_sentence_fragment_name(raw_name):
                    continue
            name = raw_name
            dedup_key = norm(name)
            if dedup_key in seen_names:
                continue
            seen_names.add(dedup_key)
            ctx.known_aliases.add(dedup_key)
            ctx.known_aliases.add(norm(role))
            # Bug 8: record the legal-name → role mapping for subject substitution.
            if hasattr(ctx, "party_role_map"):
                ctx.party_role_map[dedup_key] = norm(role)
            # Item 6: track original-cased corporate names for first-person resolution.
            if _CORP_SUFFIX_INLINE_RE.search(name):
                ctx.corporate_names.add(name)
            ctx.add_candidate("parties", "defined_party_alias", {"name": name, "role": role, "type": "party"}, sent, ctx.source_ref, 0.88, ["defined_term", "alias_match"], anti)

    # W6 T4 Item C: 'between' alone is too broad -- it fires on corp-structure
    # sentences like "X is a joint venture vehicle between A and B".  Require an
    # agreement-intro context: 'by and among' is self-sufficient; bare 'between'
    # or 'entered into by' must co-occur with an agreement-context marker
    # ('agreement', 'entered into', 'by and between', 'is made', 'this ... is').
    _has_agreement_intro = bool(
        re.search(r"\bby\s+and\s+among\b", sent, re.I)
        or re.search(r"\b(this\s+\w+\s+(?:agreement|contract|deed|indenture)|agreement\s+is\s+(?:entered|made)|entered\s+into|is\s+made\s+(?:as\s+of|this))\b", sent, re.I)
        or re.search(r"\bby\s+and\s+between\b", sent, re.I)
    )
    if _has_agreement_intro:
        for name in extract_entity_like_names(sent)[:4]:
            # Reject sentence fragments and deduplicate across the whole function.
            if _is_sentence_fragment_name(name):
                continue
            dedup_key = norm(name)
            if dedup_key in seen_names:
                continue
            seen_names.add(dedup_key)
            ctx.known_aliases.add(dedup_key)
            ctx.add_candidate("parties", "agreement_intro_party", {"name": name, "role": infer_role_from_text(name), "type": "party"}, sent, ctx.source_ref, 0.68, ["agreement_intro", "alias_match"], anti)

    if re.search(r"\bBy:\s*|\bName:\s*|\bTitle:\s*", sent, re.I):
        ctx.add_candidate("parties", "signature_block", {"name": sent, "role": "signatory", "type": "party"}, sent, ctx.source_ref, 0.62, ["signature_block"], anti)
    # Litigation caption detection is handled at block level via
    # harvest_litigation_captions because the sentence splitter splits at "v."
    # which prevents the caption from surviving as a single sentence.


def harvest_privacy_parties(ctx: HarvestContext, sent: str) -> None:
    """Harvest privacy-policy-specific party frames (W6 T3).

    Frames:
      privacy_operator -- policy-operator self-identification sentence or org header.
      service_provider -- disclosed-recipient corp name in third-party enumeration.
    """
    anti = ctx.anti

    # Frame 1: Policy-operator declaration
    for rx in (_PRIVACY_OPERATOR_RE, _PRIVACY_ORG_HEADER_RE):
        m = rx.search(sent)
        if m:
            name = clean_entity(m.group("name") or "")
            if name:
                dedup_key = norm(name)
                ctx.known_aliases.add(dedup_key)
                ctx.add_candidate(
                    "parties",
                    "privacy_operator",
                    {"name": name, "role": "operator", "type": "party"},
                    sent,
                    ctx.source_ref,
                    0.80,
                    ["privacy_operator", "defined_term"],
                    anti,
                )

    # Frame 2a: Service-provider list item "- **Name Corp.**: ..."
    # Only fire when the item description contains data/privacy keywords, OR
    # when the heading path indicates a data-flows/third-parties/transfers section.
    # This prevents FPs in corporate-structure "Entities" sections.
    m2 = _SERVICE_PROVIDER_LIST_RE.match(sent)
    if m2:
        name = clean_entity(m2.group("name") or "")
        if name:
            heading_text_inner = " > ".join(ctx.source_ref.heading_path or [])
            under_data_heading = bool(re.search(
                r"\b(data\s+flow|third.part|transfer|processor|privacy|disclosure|recipient)\b",
                heading_text_inner, re.I,
            ))
            item_body = sent[m2.end():]
            has_data_context = bool(re.search(
                r"\b(data|personal\s+information|privacy|process(?:ing)?|"
                r"bound\s+by\s+a\s+data|PCI|compliance|payment|access|"
                r"cloud|infrastructure|support|analytics|ticketing)\b",
                item_body, re.I,
            ))
            if under_data_heading or has_data_context:
                dedup_key = norm(name)
                ctx.known_aliases.add(dedup_key)
                ctx.add_candidate(
                    "parties",
                    "service_provider",
                    {"name": name, "role": "service provider", "type": "party"},
                    sent,
                    ctx.source_ref,
                    0.78,
                    ["service_provider"],
                    anti,
                )

    # Frame 2b: Inline service-provider reference "payment processor, X Corp."
    # Only fires when the sentence also contains privacy/data processing context.
    if re.search(r"\b(?:personal\s+information|personal\s+data|payment\s+data|"
                 r"processor|service\s+provider|data\s+processing|privacy)\b", sent, re.I):
        m3 = _INLINE_SERVICE_PROVIDER_RE.search(sent)
        if m3:
            name = clean_entity(m3.group("name") or "")
            if name:
                dedup_key = norm(name)
                ctx.known_aliases.add(dedup_key)
                ctx.add_candidate(
                    "parties",
                    "service_provider",
                    {"name": name, "role": "service provider", "type": "party"},
                    sent,
                    ctx.source_ref,
                    0.72,
                    ["service_provider"],
                    anti,
                )

    # Frame 2c: Inline enumeration after "transfers personal information to ... Corp."
    # Only fires when the sentence explicitly mentions personal information / data transfer.
    if re.search(r"\b(?:transfer|disclose|share)\s+(?:personal\s+information|personal\s+data)\b", sent, re.I):
        for m4 in ctx.bundle.corporate_suffixes[0].finditer(sent):
            name = clean_entity(m4.group(1) or "")
            if name:
                dedup_key = norm(name)
                ctx.known_aliases.add(dedup_key)
                ctx.add_candidate(
                    "parties",
                    "service_provider",
                    {"name": name, "role": "service provider", "type": "party"},
                    sent,
                    ctx.source_ref,
                    0.70,
                    ["service_provider"],
                    anti,
                )


def harvest_litigation_captions(h, block_text: str, source_ref, anti: list[str], bundle: LexiconBundle) -> None:
    """Detect case captions (e.g. 'Smith v. Jones', 'Tremblay c. Daigle') in raw block text.

    Called once per block before sentence iteration, so the full caption token
    sequence is visible even though the sentence splitter breaks at 'v.'/'c.'.
    Receives the orchestrator (h) directly (not via HarvestContext) because it
    is not in SENTENCE_HARVESTERS; the per-block *bundle* supplies the caption
    style for the block's language (W3).
    """
    for rx in bundle.caption_patterns:
        for m in rx.finditer(block_text):
            left = _clean_caption_side(m.group(1))
            right = _clean_caption_side(m.group(2))
            # Both sides must begin with an uppercase letter and have at least two
            # characters to avoid matching lone initials or noise tokens.
            if not left or not right:
                continue
            if not left[0].isupper() or not right[0].isupper():
                continue
            if len(left) < 2 or len(right) < 2:
                continue
            for side_name in (left, right):
                h.known_aliases.add(norm(side_name))
                h._add_candidate(
                    "parties",
                    "litigation_caption",
                    {"name": side_name, "role": "party", "type": "party"},
                    block_text,
                    source_ref,
                    0.60,
                    ["litigation_caption"],
                    anti,
                )
