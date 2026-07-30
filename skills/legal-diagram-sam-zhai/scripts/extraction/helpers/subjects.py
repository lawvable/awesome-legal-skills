"""Subject and entity-name helpers: extract_subject, entity-name cleaning.

Domain-free utilities shared by conditions.py, deadlines.py, obligations.py,
notices.py, ownership.py, parties.py, reps.py, and materialize.py.
"""
from __future__ import annotations

import re
from typing import Optional

# Local whitespace collapser: helpers/ stays free of lexicon/ imports so the
# package can be tested in isolation (same pattern as lexicon's SPACE_RE).
_SPACE_RE = re.compile(r"\s+")


def extract_subject(text: str, trigger_start: Optional[int] = None) -> str:
    """Return the grammatical subject of an obligation clause.

    When *trigger_start* is given, the subject is extracted from the prefix
    before that offset.  When absent, a leading-verb pattern is tried first.
    """
    prefix = text[:trigger_start].strip() if trigger_start is not None else text.strip()
    if not prefix or trigger_start is None:
        m = re.match(
            r"^(?:The\s+)?(?P<party>[A-Z][A-Za-z0-9 .&'/-]{1,80}?|no\s+party)\s+(?:shall|must|will|agrees?|undertakes|covenants|is\s+required|is\s+obligated|is\s+responsible|may|notify|deliver|provide|pay|reimburse|fund|transfer|remit|wire)\b",
            text,
            re.I,
        )
        return clean_party(m.group("party")) if m else ""
    prefix = re.sub(r"^(?:if|provided that|subject to|upon|following|after)\s+", "", prefix, flags=re.I).strip(" ,;:")
    if not prefix:
        return ""
    return clean_party(re.split(r",|;|\band\b", prefix)[-1].strip())


def clean_party(value: str) -> str:
    """Normalise a party name: strip leading 'the', trailing verbs, and punctuation."""
    value = _SPACE_RE.sub(" ", str(value or "")).strip(" .,;:")
    value = re.sub(r"^(?:the\s+)", "", value, flags=re.I)
    value = re.sub(r"\b(?:shall|must|will|may|agrees?|undertakes|covenants)$", "", value, flags=re.I).strip()
    return value.strip(" .,;:")[:120]


def clean_entity(value: str) -> str:
    """Normalise an entity name: same as clean_party plus bracket/quote stripping."""
    return clean_party(value).strip("()[]{}\"'")[:140]


def extract_entity_like_names(text: str) -> list[str]:
    """Return a deduplicated list of corporate-suffix entity names found in *text*."""
    names: list[str] = []
    suffix_rx = re.compile(
        r"\b([A-Z][A-Za-z0-9&.,' -]+?\s+(?:Inc\.?|LLC|Ltd\.?|Corp(?:oration)?\.?|Company|LP|LLP|PLC|GmbH))\b"
    )
    for m in suffix_rx.finditer(text):
        name = clean_entity(m.group(1))
        if name and name not in names:
            names.append(name)
    return names
