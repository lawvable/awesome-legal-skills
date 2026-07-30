"""extraction.utils: shared utilities for the extraction package.

After W2.4 this module is organised as follows:

  Helpers (four named groups re-exported from extraction.helpers):
    money     -- money_text, amount_number, extract_payment_parties, has_payment_verb
    dates     -- deadline_text, has_deadline_signal
    subjects  -- extract_subject, clean_party, clean_entity, extract_entity_like_names
    scoring   -- score_confidence, score_boost, anti_penalty

  Residual (owned here, not extracted):
    Sentence splitting      -- ABBREVIATION_GUARDS_EN, _GUARD_PLACEHOLDER,
                               _guard_split, sentences_with_offsets
    Normalisation / clean   -- clean_text, clean_value, clean_role, norm, clamp
    Snippets                -- snippet, uniq
    Anchor helpers          -- neighbor_ids, page_from_anchor, slide_from_anchor,
                               sheet_from_anchor
    Heading / signal utils  -- heading_prior_signals, anti_signals,
                               condition_corrob_signals
    Table-row helpers       -- classify_headers, row_values, render_row_text
    Document / party util   -- document_name, control_documents, delivery_method,
                               rank_from_text, infer_role_from_text,
                               extract_procurement_target, extract_notice_parties,
                               extract_object_entity, has_payment_verb (re-export),
                               is_rep_warranty

Every name that harvesters and tests currently import from this module remains
importable here unchanged (zero import-site edits outside the four harvesters
whose inline duplications are redirected by W2.4).
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any, Iterable, Optional

from .lexicon import (
    ANTI_SIGNAL_PATTERNS,
    DATE_RE,
    HEADING_PRIORS,
    HEADER_SYNONYMS,
    HEADER_SYNONYMS_FR,
    KNOWN_ROLE_WORDS,
    MONEY_RE,
    SENTENCE_SPLIT,
    SPACE_RE,
)
from .schema import SourceRef

# ---------------------------------------------------------------------------
# W2.4: helpers package re-exports (single source of truth for these groups)
# ---------------------------------------------------------------------------
from .helpers.scoring import anti_penalty, score_boost, score_confidence  # noqa: F401
from .helpers.dates import deadline_text, has_deadline_signal  # noqa: F401
from .helpers.subjects import (  # noqa: F401
    clean_entity,
    clean_party,
    extract_entity_like_names,
    extract_subject,
)
from .helpers.money import (  # noqa: F401
    amount_number,
    extract_payment_parties,
    has_payment_verb,
    money_text,
)

# ---------------------------------------------------------------------------
# W2.4 / W2.1: ABBREVIATION_GUARDS_EN -- single source of truth in lexicon/en.py
#
# Previously utils.py held a verbatim copy; the canonical tuple now lives in
# en.py (_ABBREVIATION_GUARDS_EN) and is re-exported here under the same public
# name so that all existing imports keep working unchanged.
# ---------------------------------------------------------------------------
from .lexicon.en import _ABBREVIATION_GUARDS_EN as ABBREVIATION_GUARDS_EN  # noqa: F401

# Private sentinel inserted between a guarded abbreviation and the original
# whitespace that follows it.  The sentinel breaks SENTENCE_SPLIT's lookbehind
# (which requires punctuation immediately before the whitespace) so no split
# fires.  Sentinel collision is resolved by skipping guards entirely for
# NUL-bearing input, never by stripping characters, because offsets must stay
# exact: text[start:end] == sent must hold for all inputs.
_GUARD_PLACEHOLDER = "\x00"


def _guard_split(text: str, guards: tuple[str, ...] = ABBREVIATION_GUARDS_EN) -> list[str]:
    """Split text on SENTENCE_SPLIT while honouring abbreviation guards.

    The capture group in each guard pattern preserves the original whitespace
    verbatim; the sentinel is removed on restore so sentences_with_offsets can
    locate every part in the original text via str.find without offset drift.
    NUL-bearing input bypasses guards entirely so no character mutation occurs;
    such text splits on raw SENTENCE_SPLIT boundaries and offsets remain exact.
    Each guard matches only at a word boundary (not preceded by a word
    character), so guards never fire on the tail of a longer word (W4.0a).
    Guards sourced from the EN lexicon bundle (ABBREVIATION_GUARDS_EN) via W2.4.
    """
    # Early exit for NUL-bearing input: sentinel collision cannot be resolved
    # without mutating characters, which would break offset correctness.
    if _GUARD_PLACEHOLDER in text:
        return SENTENCE_SPLIT.split(text)
    protected = text
    for abbrev in guards:
        protected = re.sub(
            r"(?<!\w)" + re.escape(abbrev) + r"(\s+)",
            abbrev + _GUARD_PLACEHOLDER + r"\1",
            protected,
        )
    parts = SENTENCE_SPLIT.split(protected)
    return [part.replace(_GUARD_PLACEHOLDER, "") for part in parts]


def classify_headers(headers: list[str]) -> dict[int, str]:
    # Table rows are synthetic blocks with no block.lang, so headers are
    # classified bilingually: the EN table is consulted first (preserving EN
    # behaviour exactly), then the FR twin table on no match (W3.3).
    mapped: dict[int, str] = {}
    for idx, header in enumerate(headers):
        h = norm(header)
        for synonym_table in (HEADER_SYNONYMS, HEADER_SYNONYMS_FR):
            if idx in mapped:
                break
            for canonical, synonyms in synonym_table.items():
                if any(h == syn or syn in h for syn in synonyms):
                    mapped[idx] = canonical
                    break
    return mapped


def row_values(headers: list[str], cells: list[str], header_map: dict[int, str]) -> dict[str, str]:
    values: dict[str, str] = {}
    for idx, canonical in header_map.items():
        if idx < len(cells) and cells[idx]:
            values.setdefault(canonical, cells[idx])
    return values


def render_row_text(headers: list[str], cells: list[str]) -> str:
    parts = []
    for idx, cell in enumerate(cells):
        if not cell:
            continue
        header = headers[idx] if idx < len(headers) and headers[idx] else f"Column {idx + 1}"
        parts.append(f"{header}: {cell}")
    return " | ".join(parts)


def sentences_with_offsets(text: str, guards: tuple[str, ...] = ABBREVIATION_GUARDS_EN) -> Iterable[tuple[str, int, int]]:
    # W3: the dispatcher passes the per-block bundle's abbreviation_guards;
    # the EN default keeps every existing call site byte-identical.
    start = 0
    for part in _guard_split(text, guards):
        stripped = part.strip()
        if not stripped:
            start += len(part)
            continue
        pos = text.find(stripped, start)
        if pos < 0:
            pos = start
        yield stripped, pos, pos + len(stripped)
        start = pos + len(stripped)


def anti_signals(text: str) -> list[str]:
    return [name for name, rx in ANTI_SIGNAL_PATTERNS if rx.search(text)]


def heading_prior_signals(source_ref: SourceRef, field_name: str) -> list[str]:
    text = " > ".join(source_ref.heading_path)
    rx = HEADING_PRIORS.get(field_name)
    return ["heading_prior"] if rx is not None and rx.search(text) else []


def condition_corrob_signals(text: str) -> list[str]:
    signals = []
    if re.search(r"\b(shall|must|agrees?|required|obligated|pay|payment|closing|consent|deliver|certificate|notice|deadline|within|by)\b", text, re.I):
        signals.append("legal_action_object")
    if has_deadline_signal(text):
        signals.append("deadline_signal")
    return signals


def extract_procurement_target(text: str) -> str:
    m = re.search(r"(?:shall\s+cause|cause)\s+(?P<target>[^.;,]{1,80}?)\s+to\s+", text, re.I)
    return clean_entity(m.group("target")) if m else ""


def extract_notice_parties(text: str) -> tuple[str, str]:
    m = re.search(r"(?P<sender>[A-Z][A-Za-z .&']+?)\s+(?:shall\s+|must\s+|will\s+)?(?:notify|give\s+notice\s+to|send\s+notice\s+to)\s+(?P<recipient>[A-Z][A-Za-z .&']+)", text)
    if m:
        return clean_party(m.group("sender")), clean_party(m.group("recipient"))
    m = re.search(r"notice\s+shall\s+be\s+sent\s+to\s+(?P<recipient>[A-Z][A-Za-z .&']+)", text, re.I)
    return "", clean_party(m.group("recipient")) if m else ""


def extract_object_entity(text: str) -> str:
    names = extract_entity_like_names(text)
    subject = norm(extract_subject(text))
    for name in names:
        if norm(name) != subject:
            return name
    return ""


def is_rep_warranty(text: str) -> bool:
    return bool(re.search(r"\b(represents\s+and\s+warrants|representations?|warranties|true\s+and\s+correct|to\s+the\s+knowledge\s+of|except\s+as\s+disclosed|set\s+forth\s+on\s+Schedule)\b", text, re.I))


def document_name(text: str) -> str:
    # W6 T4 Item D: priority order for document name extraction.
    # 1. Numbered schedule/exhibit/annex references: "Schedule No. 4", "Exhibit A",
    #    "Annexe 2", "Schedule 1.1", "Annex III" -- these are the most specific.
    m = re.search(
        r"\b(Schedule(?:\s+No\.?)?\s+\d+(?:\.\d+)*"
        r"|Exhibit\s+[A-Z0-9]+(?:\.\d+)?"
        r"|Annexe?\s+(?:No\.?\s*)?\d+(?:\.\d+)*"
        r"|Exhibit\s+No\.?\s*\d+"
        r"|Schedule\s+[A-Z](?:\.\d+)?)\b",
        text,
        re.I,
    )
    if m:
        return m.group(0)
    # 2. Named certificate or formal document types (unambiguous multi-word forms).
    m2 = re.search(
        r"\b(officer's\s+certificate|secretary's\s+certificate"
        r"|bring-down\s+certificate|compliance\s+certificate"
        r"|executed\s+counterpart|books\s+and\s+records)\b",
        text,
        re.I,
    )
    if m2:
        return m2.group(0)
    # 3. Title-Case multi-word phrase ending before a verb or punctuation --
    #    heuristic for named agreements/instruments cited in a delivery clause.
    #    Captures things like "Platform Licence Agreement" but not bare "notice"
    #    or lone generic words.
    m3 = re.search(
        r"\b((?:[A-Z][A-Za-z]+\s+){1,6}(?:Agreement|Contract|Deed|Instrument"
        r"|Certificate|Notice|Licence|License|Policy|Plan|Report|Statement"
        r"|Order|Approval|Consent|Letter|Opinion|Release|Amendment|Waiver))\b",
        text,
    )
    if m3 and len(m3.group(1).split()) >= 2:
        return m3.group(1).strip()
    # 4. No specific document name found: return a short snippet so the caller
    #    can still emit a candidate, but NOT bare single-word nouns like "notice"
    #    which are too generic.  Return empty string to signal no document name.
    return ""


def control_documents(text: str) -> list[str]:
    docs = []
    for pattern in [
        r"audit\s+report",
        r"board\s+certificate",
        r"officer's\s+certificate",
        r"secretary's\s+certificate",
        r"compliance\s+certificate",
        r"evidence\s+document",
    ]:
        m = re.search(pattern, text, re.I)
        if m:
            docs.append(m.group(0))
    return uniq(docs)


def delivery_method(text: str) -> Optional[str]:
    m = re.search(r"\b(email|overnight\s+courier|certified\s+mail|personal\s+delivery)\b", text, re.I)
    return m.group(0).lower() if m else None


def rank_from_text(text: str) -> int:
    words = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5}
    m = re.search(r"\b(first|second|third|fourth|fifth)\b", text, re.I)
    if m:
        return words[m.group(1).lower()]
    m = re.search(r"\b(\d+)[.)]", text)
    return int(m.group(1)) if m else 1


def infer_role_from_text(text: str) -> str:
    lowered = text.lower()
    for role in KNOWN_ROLE_WORDS:
        if role in lowered:
            return role
    return "party"


def clean_value(value: dict[str, Any]) -> dict[str, Any]:
    cleaned = {}
    for key, val in value.items():
        if isinstance(val, str):
            cleaned[key] = clean_text(val)
        elif isinstance(val, list):
            cleaned[key] = [clean_text(v) if isinstance(v, str) else v for v in val if v]
        else:
            cleaned[key] = val
    return cleaned


def clean_text(value: str) -> str:
    return SPACE_RE.sub(" ", str(value or "")).strip(" .,;:")


# W3.4: Œ/œ carry no NFD decomposition (no Unicode decomposition mapping), so the
# ligature maps to its ASCII digraph explicitly before NFD strips combining marks.
_LIGATURE_MAP = str.maketrans({"Œ": "OE", "œ": "oe"})


def strip_diacritics(value: str) -> str:
    """Transliterate accents to ASCII: NFD-decompose, then drop combining marks.

    `é` → `e`, `ç` → `c`, `Œ` → `OE`; ASCII input passes through unchanged.
    Used to make Mermaid node IDs ASCII-safe; display labels keep accents verbatim.
    """
    decomposed = unicodedata.normalize("NFD", str(value or "").translate(_LIGATURE_MAP))
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))


def clean_role(value: str) -> str:
    return clean_text(value).lower()[:80]


def norm(value: str) -> str:
    return SPACE_RE.sub(" ", str(value or "").strip().lower()).strip(" .,;:")


def clamp(value: float) -> float:
    return round(max(0.0, min(1.0, float(value))), 2)


def snippet(text: str, limit: int = 650) -> str:
    return clean_text(text)[:limit]


def uniq(items: Iterable[str]) -> list[str]:
    seen = set()
    out = []
    for item in items:
        if not item or item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out


def neighbor_ids(block_id: str) -> list[str]:
    try:
        idx = int(block_id)
    except (TypeError, ValueError):
        return []
    return [str(max(0, idx - 1)), str(idx + 1)]


def page_from_anchor(anchor: str) -> Optional[int]:
    m = re.search(r"page(\d+)", anchor or "", re.I)
    return int(m.group(1)) if m else None


def slide_from_anchor(anchor: str) -> Optional[int]:
    m = re.search(r"slide(\d+)", anchor or "", re.I)
    return int(m.group(1)) if m else None


def sheet_from_anchor(anchor: str) -> Optional[str]:
    return str(anchor).split(":", 1)[1] if str(anchor).startswith("sheet:") else None
