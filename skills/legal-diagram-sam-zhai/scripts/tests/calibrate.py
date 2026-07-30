"""Calibration harness for legal-diagram extraction + selector.

Usage (from skill root):
    python scripts/tests/calibrate.py            # default: score all fixtures, emit JSON to stdout
    python scripts/tests/calibrate.py --tune     # same + advisory tuning proposals appended after JSON

Design:
  - stdlib only; deterministic (stable sorts, no randomness, no clock).
  - Reads labels.json siblings for each fixture; imports FIXTURE_MATTER_TYPE from run_golden.py.
  - Runs extraction in-process via the canonical scripts.extraction / scripts.normalize stack.
  - Runs selector in-process via scripts.diagram_selector.recommend.
  - Tier vocabulary:
      promoted = resolver-approved candidates materialised into extraction_result fields.
      hint     = candidates kept below promotion with evidence packets, in extraction_hints.
  - Matching rule: documented in _match_label_to_extractions(); normalise + equality/substring/Jaccard.
  - The 0.50 selector-interrupt confidence line is never a tunable parameter (see comment in _tune).
  - pytest must not collect this file (no test_ function names; no module-level asserts).
  - Standalone-runnable from skill root.
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Path setup: allow imports from scripts/ when run as a script
# ---------------------------------------------------------------------------

_HERE = Path(__file__).resolve()
_SKILL_ROOT = _HERE.parents[2]        # scripts/tests/calibrate.py -> skill root
_FIXTURES_DIR = _HERE.parent / "fixtures"

if str(_SKILL_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(_SKILL_ROOT / "scripts"))

# Import the single source of truth for fixture-to-matter-type mapping.
# calibrate.py must not duplicate this map.
from tests.run_golden import FIXTURE_MATTER_TYPE  # noqa: E402


# ---------------------------------------------------------------------------
# Field ownership table: maps each scored field to its population owner.
# Derived from references/extraction-schema.md detection-tier catalogue.
# "script" = script-direct or script-hint populates the field in prose docs.
# "llm"    = requires LLM enrichment to populate in non-tabular prose
#            (data_flows, relationships, conditions per schema tiering).
# ---------------------------------------------------------------------------

FIELD_OWNERSHIP: dict[str, str] = {
    "conditions":       "llm",
    "controls":         "script",
    "data_flows":       "llm",
    "deadlines":        "script",
    "documents":        "script",
    "entities":         "script",
    "events":           "script",
    "legal_authorities": "script",
    "obligations":      "script",
    "ownership_links":  "script",
    "parties":          "script",
    "relationships":    "llm",
    "transfers":        "script",
}


# ---------------------------------------------------------------------------
# Lazy imports from extraction stack (after path setup)
# ---------------------------------------------------------------------------

def _import_stack():
    """Import extraction and selector modules.

    Deferred import keeps module load fast and ensures sys.path is set first.
    Returns (normalize_fn, extract_fn, recommend_fn, lexicon_module, resolver_module, RULES).
    """
    from normalize import normalize as _normalize
    from extraction import extract as _extract
    from diagram_selector import recommend as _recommend, RULES as _RULES
    import extraction.lexicon as _lex
    import extraction.resolver as _res
    return _normalize, _extract, _recommend, _lex, _res, _RULES


# ---------------------------------------------------------------------------
# Entity-to-string: flatten each extracted entity type to a matchable string.
#
# Strategy: pick the field(s) that most faithfully represent what a human
# analyst would write in a label.  Composed fields are joined with a single
# space.  None/missing values are dropped.
# ---------------------------------------------------------------------------

def _entity_to_str(field_name: str, entity: Any) -> str:
    """Convert an extracted entity dict (from JSON) to a plain string for matching."""
    if isinstance(entity, str):
        return entity

    def g(k: str) -> str:
        v = entity.get(k) if isinstance(entity, dict) else getattr(entity, k, None)
        return str(v).strip() if v is not None else ""

    if field_name == "parties":
        return g("name")

    if field_name == "entities":
        return g("name")

    if field_name == "events":
        # Labels use date strings; fall back to description for substring matching.
        date = g("date") or g("date_or_timing")
        desc = g("description")
        return date if date else desc

    if field_name == "deadlines":
        date = g("date") or g("date_or_timing")
        desc = g("description")
        return f"{date} {desc}".strip() if date else desc

    if field_name == "obligations":
        return g("description")

    if field_name == "controls":
        return g("description")

    if field_name == "conditions":
        return g("description")

    if field_name == "relationships":
        # Labels are free-text sentences; compose from available parts.
        desc = g("description")
        if desc:
            return desc
        from_e = g("from_entity")
        to_e = g("to_entity")
        rel_type = g("type")
        return " ".join(p for p in [from_e, rel_type, to_e] if p)

    if field_name == "ownership_links":
        # Labels: "Parent owns X% of Child."  Compose a matchable string.
        parent = g("parent")
        child = g("child")
        pct_raw = (entity.get("percentage") if isinstance(entity, dict)
                   else getattr(entity, "percentage", None))
        if pct_raw is not None:
            try:
                pct = int(float(pct_raw))
                return f"{parent} owns {pct}% of {child}"
            except (TypeError, ValueError):
                pass
        return f"{parent} {child}"

    if field_name == "legal_authorities":
        return g("citation")

    if field_name == "transfers":
        desc = g("description")
        from_p = g("from_party")
        to_p = g("to_party")
        return desc if desc else f"{from_p} to {to_p}"

    if field_name == "data_flows":
        from_s = g("from_system")
        to_s = g("to_system")
        return f"{from_s} {to_s}"

    if field_name == "documents":
        return g("name")

    if field_name == "states":
        return g("name") or g("description")

    if field_name == "transitions":
        return f"{g('from_state')} {g('to_state')}"

    if field_name == "communications":
        return g("description")

    if field_name == "concepts":
        return g("name") or g("description")

    # Generic fallback: join all non-empty string values.
    if isinstance(entity, dict):
        parts = [str(v).strip() for v in entity.values()
                 if v is not None and isinstance(v, str) and str(v).strip()]
        return " ".join(parts[:3])

    return str(entity)


# ---------------------------------------------------------------------------
# Matching rule (documented here; used throughout).
#
# Normalise both sides: casefold, collapse whitespace, strip enclosing
# punctuation (leading/trailing .,;:"'() ).
#
# A label matches an extraction if any of, tried in this order:
#   (a) normalised equality
#   (b) one side is a substring of the other
#   (c) token-set Jaccard of whitespace-split tokens >= 0.5
#   (d) date equivalence: both sides canonicalise to the SAME ISO date
#       (a verbatim locale label matches an ISO candidate for the same day).
#       Rule (d) fires ONLY when the caller sets date_rule=True, which is
#       gated to date-bearing fields ("events", "deadlines") at the
#       _score_fixture call site via _DATE_BEARING_FIELDS.  Without this
#       gate, two strings with disjoint content but a shared date token
#       would falsely match (Jaccard ~0.14 on the probe pair), inflating
#       precision when one field carries two same-date facts.
#
# After all four rules fail against the primary extraction strings, the
# greedy matcher tries an evidence-snippet fallback (see _match_label_to_
# extractions): a label matches when its normalised form is a substring of a
# candidate's normalised verbatim evidence snippet.  The fallback is ordered
# strictly LAST so the primary semantics keep priority.
#
# Matching is one-to-one greedy in stable sorted order (sorted labels x
# sorted extractions); each extraction string consumes at most one label.
# ---------------------------------------------------------------------------

# Fields whose primary extraction strings are date tokens: rule (d) is
# applicable for these fields and must not fire for the rest.
_DATE_BEARING_FIELDS: frozenset[str] = frozenset({"events", "deadlines"})

def _normalise(s: str) -> str:
    """Casefold, collapse whitespace, strip enclosing punctuation.

    Also folds typographic apostrophes / right-single-quotation-marks to the
    straight ASCII apostrophe (U+0027) so that a label authored with U+0027
    matches an extraction that carries U+2019 (RIGHT SINGLE QUOTATION MARK)
    or U+02BC (MODIFIER LETTER APOSTROPHE).  This is Unicode equivalence, not
    threshold relaxation; W1.5 scoring constants are not affected.
    """
    # Fold typographic apostrophes to straight apostrophe before casefolding.
    s = s.replace("’", "'").replace("ʼ", "'")
    s = s.casefold().strip()
    # collapse internal whitespace
    s = " ".join(s.split())
    # strip common enclosing punctuation
    s = s.strip(".,;:\"'()")
    return s



# ---------------------------------------------------------------------------
# Stopword set for Jaccard token filtering (EN + FR function words).
#
# Purpose: prevent function-word dilution from inflating the union while
# content tokens are absent, and prevent two strings sharing only stopwords
# from matching through Jaccard.
#
# Modals (shall/must/will/doit/doivent) and negation (not/no/ne/pas) are
# deliberately excluded: they carry meaning in legal text.
# ---------------------------------------------------------------------------
_JACCARD_STOPWORDS: frozenset[str] = frozenset({
    # EN articles / determiners
    "the", "a", "an", "this", "that", "such", "any", "all", "its", "their",
    # EN prepositions
    "of", "to", "in", "with", "for", "by", "on", "at", "as", "from",
    "under", "upon",
    # EN conjunctions / pronouns
    "and", "or", "is", "are", "be",
    # FR articles / determiners
    "le", "la", "les", "l", "un", "une", "des", "ce", "cette", "ses",
    "leur",
    # FR prepositions / contractions
    "de", "du", "d", "à", "au", "aux", "en", "dans", "par", "pour", "sur",
    # FR conjunctions / pronouns
    "et", "ou", "que", "qui",
})

# Token punctuation characters to strip from each token's enclosing positions.
_TOKEN_STRIP_CHARS = ".,;:\"'()«»…"


def _filter_jaccard_token(tok: str) -> str | None:
    """Strip enclosing punctuation from *tok* and return it, or None if it is a stopword.

    Returns None when the stripped token is empty or is a known function-word
    stopword.  Modals and negation are not stopwords and pass through intact.
    Hyphen-to-space folding is applied so '15-business-day' becomes
    '15 business day' tokens that each tokenize independently on re-split.
    """
    stripped = tok.strip(_TOKEN_STRIP_CHARS)
    if not stripped:
        return None
    if stripped.lower() in _JACCARD_STOPWORDS:
        return None
    return stripped


def _jaccard_tokens(a: str, b: str) -> float:
    """Token-set Jaccard on content tokens after stopword filtering.

    Each whitespace-split token is stripped of enclosing punctuation
    (.,;:\"'()«»…) and then filtered against a closed set of EN+FR function
    words (articles, prepositions, conjunctions, pronouns).  Modals
    (shall/must/will/doit/doivent) and negation (not/no/ne/pas) are NOT
    filtered: they carry legal meaning.

    Hyphen-split: hyphens within tokens are folded to spaces before splitting
    so '15-business-day' contributes the individual content tokens '15',
    'business', and 'day' rather than one opaque string.

    Empty-after-filter token sets return 0.0 (never match).
    """
    def _tokenize(s: str) -> set[str]:
        raw_tokens = s.replace("-", " ").split()
        result: set[str] = set()
        for tok in raw_tokens:
            cleaned = _filter_jaccard_token(tok)
            if cleaned is not None:
                result.add(cleaned.lower())
        return result

    ta = _tokenize(a)
    tb = _tokenize(b)
    if not ta or not tb:
        return 0.0
    union = ta | tb
    return len(ta & tb) / len(union)


# ---------------------------------------------------------------------------
# Date equivalence (match rule d).
#
# Verbatim locale date labels ("1er février 2023", "March 1, 2024") must match
# ISO candidate dates ("2023-02-01", "2024-03-01") for the SAME calendar day.
# Canonicalisation reuses the lexicon bundles' date machinery rather than a new
# parser: the FR bundle's normalize_date already returns ISO for FR month names
# and passes ISO through, so it resolves both FR labels and ISO candidates.  The
# EN bundle keeps dates as written (its golden contract), so an EN month-name
# label is canonicalised with a tiny local month map keyed off the EN date_re
# match.  Each call canonicalises at most the first date token in the string.
# ---------------------------------------------------------------------------

_EN_MONTH_NUMBERS: dict[str, int] = {
    "jan": 1, "january": 1, "feb": 2, "february": 2, "mar": 3, "march": 3,
    "apr": 4, "april": 4, "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7,
    "aug": 8, "august": 8, "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10, "nov": 11, "november": 11, "dec": 12, "december": 12,
}


def _to_iso_date(s: str) -> str | None:
    """Canonicalise the first date token in *s* to ISO 8601 (YYYY-MM-DD).

    Tries the FR bundle first (handles FR month names, FR date ranges, and ISO
    passthrough), then falls back to an EN month-name parse keyed off the EN
    bundle's date_re.  Returns None when no parseable date token is present.
    """
    from extraction.lexicon import get_bundle

    iso = get_bundle("fr").normalize_date(s)
    if iso is not None:
        return iso

    en = get_bundle("en")
    m = en.date_re.search(s)
    if not m:
        return None
    raw = m.group(0)
    iso_match = re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw)
    if iso_match:
        return raw
    # EN date_re matches "Month D[,] YYYY" or "D Month YYYY".  Pull the parts.
    tokens = raw.replace(",", " ").split()
    month_tok = next((t for t in tokens if t.lower() in _EN_MONTH_NUMBERS), None)
    nums = [t for t in tokens if t.isdigit()]
    if month_tok is None or len(nums) != 2:
        return None
    month = _EN_MONTH_NUMBERS[month_tok.lower()]
    day = int(nums[0]) if len(nums[0]) <= 2 else int(nums[1])
    year = int(nums[1]) if len(nums[1]) == 4 else int(nums[0])
    return f"{year:04d}-{month:02d}-{day:02d}"


def _dates_equivalent(norm_label: str, norm_extraction: str) -> bool:
    """True when both sides canonicalise to the same non-None ISO date."""
    iso_label = _to_iso_date(norm_label)
    if iso_label is None:
        return False
    iso_extraction = _to_iso_date(norm_extraction)
    return iso_extraction is not None and iso_label == iso_extraction


def _is_match(norm_label: str, norm_extraction: str, *, date_rule: bool = False) -> bool:
    """Return True if a normalised label matches a normalised extraction string.

    ``date_rule`` enables rule (d) date equivalence.  Pass True only for
    date-bearing fields (see _DATE_BEARING_FIELDS); leaving it False prevents
    two strings with disjoint content but a shared date token from falsely
    matching via rule (d).
    """
    if not norm_label or not norm_extraction:
        return False
    if norm_label == norm_extraction:
        return True
    if norm_label in norm_extraction or norm_extraction in norm_label:
        return True
    if _jaccard_tokens(norm_label, norm_extraction) >= 0.5:
        return True
    if date_rule and _dates_equivalent(norm_label, norm_extraction):
        return True
    return False


def _match_label_to_extractions(
    labels: list[str],
    extractions: list[str],
    fallback_pool: list[str] | None = None,
    *,
    date_rule: bool = False,
) -> tuple[int, int]:
    """Greedy one-to-one matching in stable sorted order.

    Returns (matched_count, len(extractions)).
    Each extraction string is consumed by at most one label.  Both lists are
    sorted for determinism before matching.

    ``date_rule`` threads the flag into every _is_match call.  Pass True only
    for date-bearing fields (see _DATE_BEARING_FIELDS at the _score_fixture
    call site).

    ``fallback_pool`` carries the candidates' verbatim evidence snippets.  A
    label that fails every primary rule (_is_match) against the still-unused
    extraction strings is retried against the still-unused snippets: it matches
    when its normalised form is a substring of a normalised snippet.  The
    fallback runs strictly AFTER the primary pass for every label, so primary
    semantics keep priority; each snippet is consumed by at most one label.

    Total matches are capped at ``len(extractions)``: each extraction is one
    promoted (or pooled) entity and its evidence snippet is the same entity seen
    through its source span, so a label recovered through a snippet must occupy
    one of the entity slots.  The cap keeps the invariant matched <= len(
    extractions), so precision (tp / n_promoted) can never exceed 1.0 even when
    a label matches the snippet of an entity already matched for a merged fact.
    """
    sorted_labels = sorted(labels)
    sorted_extractions = sorted(extractions)
    norm_labels = [_normalise(lb) for lb in sorted_labels]
    norm_extractions = [_normalise(ex) for ex in sorted_extractions]

    sorted_fallback = sorted(fallback_pool or [])
    norm_fallback = [_normalise(fb) for fb in sorted_fallback]
    used_fallback: list[bool] = [False] * len(norm_fallback)

    used_extraction: list[bool] = [False] * len(norm_extractions)
    primary_matched = 0
    fallback_matched = 0
    fallback_budget = len(norm_extractions)  # total cannot exceed #extractions
    for norm_lb in norm_labels:
        primary_hit = False
        for i, norm_ex in enumerate(norm_extractions):
            if not used_extraction[i] and _is_match(norm_lb, norm_ex, date_rule=date_rule):
                primary_matched += 1
                used_extraction[i] = True
                primary_hit = True
                break  # one label consumes at most one extraction; move to next label
        if primary_hit:
            continue
        if primary_matched + fallback_matched >= fallback_budget:
            continue  # no remaining extraction slot for a fallback match
        # Evidence-snippet fallback: ordered last, substring containment only.
        for j, norm_fb in enumerate(norm_fallback):
            if not used_fallback[j] and norm_lb and norm_lb in norm_fb:
                fallback_matched += 1
                used_fallback[j] = True
                # Consume one unused extraction slot so primary matches on
                # subsequent labels cannot push the total above n_extractions.
                # (Without this, a fallback hit followed by a primary hit on a
                # previously-free slot can cause tp > n_promoted, yielding a
                # negative fp_promoted in the scorer.)
                for _fi in range(len(used_extraction)):
                    if not used_extraction[_fi]:
                        used_extraction[_fi] = True
                        break
                break

    return primary_matched + fallback_matched, len(extractions)


# ---------------------------------------------------------------------------
# Hint-candidate extraction: pull hint-tier candidates from candidate_manifest.
#
# "hint" = candidates whose promotion_decision action == "hint".
# Hint candidates carry normalized_value dicts (not yet materialised entities).
# ---------------------------------------------------------------------------

def _hint_strings_for_field(candidate_manifest: dict, field_name: str) -> list[str]:
    """Return string representations of hint-tier candidates for one field."""
    candidates = candidate_manifest.get("candidates", [])
    pd_by_id = {pd["candidate_id"]: pd["action"]
                for pd in candidate_manifest.get("promotion_decisions", [])}
    result = []
    for cand in candidates:
        if cand.get("target_field") != field_name:
            continue
        if pd_by_id.get(cand["id"]) != "hint":
            continue
        nv = cand.get("normalized_value", {})
        s = _entity_to_str(field_name, nv)
        if s:
            result.append(s)
    return result


def _evidence_snippets_for_field(
    candidate_manifest: dict, field_name: str, actions: tuple[str, ...],
) -> list[str]:
    """Return verbatim evidence snippets for one field's candidates.

    ``actions`` filters by promotion action ("promote" and/or "hint").  Each
    candidate contributes its evidence snippets (resolved through evidence_ids
    against the manifest's evidence_packets).  These verbatim source spans feed
    the matcher's evidence-snippet fallback so a label authored as a verbatim
    subspan matches even when the reconstructed primary string fails.
    """
    candidates = candidate_manifest.get("candidates", [])
    pd_by_id = {pd["candidate_id"]: pd["action"]
                for pd in candidate_manifest.get("promotion_decisions", [])}
    snippet_by_id = {e["id"]: e.get("snippet", "")
                     for e in candidate_manifest.get("evidence_packets", [])}
    result: list[str] = []
    for cand in candidates:
        if cand.get("target_field") != field_name:
            continue
        if pd_by_id.get(cand["id"]) not in actions:
            continue
        for eid in cand.get("evidence_ids", []):
            snippet = snippet_by_id.get(eid, "")
            if snippet:
                result.append(snippet)
    return result


# ---------------------------------------------------------------------------
# Instance-level miss collection and formatting (--dump-misses)
# ---------------------------------------------------------------------------

# Separator that splits the JSON document from the miss-audit section.
# Mirrors how --tune appends after JSON.  Must not appear in any JSON value.
_MISS_AUDIT_SEPARATOR = "=== MISS AUDIT ==="

# Maximum characters shown verbatim for an evidence snippet in the dump.
_SNIPPET_DISPLAY_LIMIT = 160

# Maximum characters for each quoted text inside a NOTE slot-consumed line.
_NOTE_TRUNCATE = 80


def _promoted_candidates_for_field(
    candidate_manifest: dict, field_name: str
) -> list[dict]:
    """Return promoted-tier candidate dicts for one field, in manifest order."""
    pd_by_id = {pd["candidate_id"]: pd["action"]
                for pd in candidate_manifest.get("promotion_decisions", [])}
    return [
        c for c in candidate_manifest.get("candidates", [])
        if c.get("target_field") == field_name
        and pd_by_id.get(c["id"]) == "promote"
    ]


def _all_candidates_for_field(
    candidate_manifest: dict, field_name: str
) -> list[dict]:
    """Return all candidates for one field with their action, in manifest order."""
    pd_by_id = {pd["candidate_id"]: pd["action"]
                for pd in candidate_manifest.get("promotion_decisions", [])}
    return [
        {**c, "_action": pd_by_id.get(c["id"], "unknown")}
        for c in candidate_manifest.get("candidates", [])
        if c.get("target_field") == field_name
    ]


def _first_snippet(candidate: dict, snippet_by_id: dict[str, str]) -> str:
    """Return the first non-empty evidence snippet for a candidate."""
    for eid in candidate.get("evidence_ids", []):
        s = snippet_by_id.get(eid, "")
        if s:
            return s
    return ""


def _collect_misses(
    er_dict: dict,
    candidate_manifest: dict,
    labels: dict,
) -> dict[str, list[dict]]:
    """Collect per-field instance-level misses (FPs and FNs) for one fixture.

    Returns a dict keyed by field name, each value a list of miss dicts.

    FP item keys: kind="FP", field, value, tier, frame_type, evidence_snippet.
    FN item keys: kind="FN", field, expected_value, closest_value, closest_tier.
    NOTE item keys: kind="NOTE", field, suppressed_value, label, snippet_owner_value.
      NOTE items arise when a snippet fallback hit finds the snippet's owning promoted
      candidate is ALREADY consumed by a primary match (merged-fact case).  Slot
      arithmetic still counts the match as TP, but an anonymous promoted slot is
      consumed instead of the already-used owner.  The NOTE annotation records the
      suppressed item, the label, and the owner so the auditor can judge whether the
      suppressed item is a genuine FP.  NOTE lines are intentionally excluded from
      "FP " and "FN " grep counts so reconciliation stays clean.

    The matching logic mirrors _score_fixture exactly (same normalisation,
    same matching helpers, same date-rule gate) so counts are consistent.
    Ordering within each field list: FPs first (by value), then NOTEs (by
    suppressed_value), then FNs (by expected_value) -- deterministic, no wall
    clock, no randomness.
    """
    fields_in_labels = labels.get("fields", {})
    snippet_by_id: dict[str, str] = {
        e["id"]: e.get("snippet", "")
        for e in candidate_manifest.get("evidence_packets", [])
    }

    result: dict[str, list[dict]] = {}

    for field_name, label_list in fields_in_labels.items():
        if not isinstance(label_list, list):
            continue

        promoted_candidates = _promoted_candidates_for_field(candidate_manifest, field_name)
        promoted_items = er_dict.get(field_name, [])
        promoted_strs = [_entity_to_str(field_name, e) for e in promoted_items
                         if _entity_to_str(field_name, e)]

        use_date_rule = field_name in _DATE_BEARING_FIELDS

        # --- Identify which promoted strings matched at least one label ---
        # Re-run greedy matching tracking used_extraction indices.
        sorted_labels = sorted(label_list)
        sorted_prom_strs = sorted(promoted_strs)
        norm_labels = [_normalise(lb) for lb in sorted_labels]
        norm_prom = [_normalise(ex) for ex in sorted_prom_strs]

        # Build (snippet, owner_sorted_prom_idx) pairs so ownership survives
        # the deterministic sort.  Each promoted candidate's string is looked up
        # in sorted_prom_strs; the first matching index is the owner's slot.
        # Candidates are processed in manifest order; within a candidate, evidence
        # packets are processed in evidence_ids order -- same order as
        # _evidence_snippets_for_field, preserving consistency with the scorer.
        _pd_by_id: dict[str, str] = {
            pd["candidate_id"]: pd["action"]
            for pd in candidate_manifest.get("promotion_decisions", [])
        }
        snippet_owner_pairs: list[tuple[str, int]] = []  # (snippet_str, sorted_prom_idx)
        # Track which sorted_prom_strs indices have already been assigned an
        # owner pair so duplicates bind to distinct indices (stable, left-to-right).
        _assigned_owner_indices: set[int] = set()
        for cand in candidate_manifest.get("candidates", []):
            if cand.get("target_field") != field_name:
                continue
            if _pd_by_id.get(cand["id"]) != "promote":
                continue
            cand_str = _entity_to_str(field_name, cand.get("normalized_value", {}))
            # Find this candidate's slot in sorted_prom_strs (first unassigned match).
            owner_idx: int = -1
            for _pi, _pstr in enumerate(sorted_prom_strs):
                if _pstr == cand_str and _pi not in _assigned_owner_indices:
                    owner_idx = _pi
                    _assigned_owner_indices.add(_pi)
                    break
            if owner_idx == -1:
                # Candidate string not in sorted_prom_strs (e.g. empty string
                # filtered by the _entity_to_str check above).  Skip.
                continue
            for eid in cand.get("evidence_ids", []):
                snippet = snippet_by_id.get(eid, "")
                if snippet:
                    snippet_owner_pairs.append((snippet, owner_idx))

        # Sort by snippet text for determinism; ownership is preserved in the tuple.
        snippet_owner_pairs.sort(key=lambda t: t[0])
        norm_snippet_owner_pairs: list[tuple[str, int]] = [
            (_normalise(s), oi) for s, oi in snippet_owner_pairs
        ]

        used_prom: list[bool] = [False] * len(norm_prom)
        used_snippet: list[bool] = [False] * len(norm_snippet_owner_pairs)
        matched_labels: set[int] = set()
        prom_budget = len(norm_prom)
        primary_count = 0
        fallback_count = 0
        # slot_consumed_notes: list of (suppressed_sorted_prom_idx, label_str,
        #                               snippet_owner_sorted_prom_idx)
        slot_consumed_notes: list[tuple[int, str, int]] = []

        for li, norm_lb in enumerate(norm_labels):
            primary_hit = False
            for pi, norm_ex in enumerate(norm_prom):
                if not used_prom[pi] and _is_match(norm_lb, norm_ex, date_rule=use_date_rule):
                    used_prom[pi] = True
                    primary_count += 1
                    primary_hit = True
                    matched_labels.add(li)
                    break
            if primary_hit:
                continue
            if primary_count + fallback_count >= prom_budget:
                continue
            for si, (norm_fb, owner_idx) in enumerate(norm_snippet_owner_pairs):
                if not used_snippet[si] and norm_lb and norm_lb in norm_fb:
                    used_snippet[si] = True
                    fallback_count += 1
                    matched_labels.add(li)
                    if not used_prom[owner_idx]:
                        # Rule 1: owner is unused -- identity-faithful suppression.
                        used_prom[owner_idx] = True
                    else:
                        # Rule 2: owner already consumed (merged-fact case) -- pick
                        # the first unused promoted slot anonymously, record NOTE.
                        for pi2 in range(len(used_prom)):
                            if not used_prom[pi2]:
                                used_prom[pi2] = True
                                slot_consumed_notes.append(
                                    (pi2, sorted_labels[li], owner_idx)
                                )
                                break
                    break

        # Promoted items consumed by primary hits or fallback hits are TPs.
        matched_prom_strs: set[int] = {pi for pi, used in enumerate(used_prom) if used}

        # --- FP: promoted strings that consumed no label ---
        # Map sorted promoted strings back to candidates (best-effort: same sorted order).
        fp_items: list[dict] = []
        for pi, pstr in enumerate(sorted_prom_strs):
            if pi not in matched_prom_strs:
                # Find a matching candidate by value equality.
                cand_info: dict | None = None
                for cand in promoted_candidates:
                    cand_str = _entity_to_str(field_name, cand.get("normalized_value", {}))
                    if cand_str == pstr:
                        cand_info = cand
                        break
                snippet = _first_snippet(cand_info, snippet_by_id) if cand_info else ""
                display_snip = (snippet[:_SNIPPET_DISPLAY_LIMIT] + "…"
                                if len(snippet) > _SNIPPET_DISPLAY_LIMIT else snippet)
                fp_items.append({
                    "kind": "FP",
                    "field": field_name,
                    "value": pstr,
                    "tier": "promote",
                    "frame_type": cand_info.get("frame_type", "") if cand_info else "",
                    "evidence_snippet": display_snip,
                })
        fp_items.sort(key=lambda x: x["value"])

        # --- NOTE: slot-consumed annotations (merged-fact fallback, rule 2) ---
        note_items: list[dict] = []
        for suppressed_pi, label_str, owner_pi in slot_consumed_notes:
            suppressed_val = sorted_prom_strs[suppressed_pi]
            owner_val = sorted_prom_strs[owner_pi]
            note_items.append({
                "kind": "NOTE",
                "field": field_name,
                "suppressed_value": suppressed_val,
                "label": label_str,
                "snippet_owner_value": owner_val,
            })
        note_items.sort(key=lambda x: x["suppressed_value"])

        # --- FN: labels not matched by any promoted item (or its snippets) ---
        all_cands = _all_candidates_for_field(candidate_manifest, field_name)
        all_cand_strs: list[tuple[str, str]] = [  # (str, action)
            (_entity_to_str(field_name, c.get("normalized_value", {})), c["_action"])
            for c in all_cands
            if _entity_to_str(field_name, c.get("normalized_value", {}))
        ]

        fn_items: list[dict] = []
        for li, label_str in enumerate(sorted_labels):
            if li in matched_labels:
                continue
            norm_lb = norm_labels[li]
            # Closest candidate: first match at any tier using _is_match.
            closest_value: str | None = None
            closest_tier: str | None = None
            for cstr, caction in all_cand_strs:
                if _is_match(norm_lb, _normalise(cstr), date_rule=use_date_rule):
                    closest_value = cstr
                    closest_tier = caction
                    break
            fn_items.append({
                "kind": "FN",
                "field": field_name,
                "expected_value": label_str,
                "closest_value": closest_value,
                "closest_tier": closest_tier,
            })
        fn_items.sort(key=lambda x: x["expected_value"])

        misses = fp_items + note_items + fn_items
        result[field_name] = misses

    return result


def format_miss_dump(misses_by_fixture: dict[str, dict[str, list[dict]]]) -> str:
    """Format instance-level misses as human-readable, grep-friendly text.

    Fixtures are sorted alphabetically; within each fixture, fields are sorted
    alphabetically; within each field, FP lines precede NOTE lines precede FN
    lines (matching _collect_misses ordering).

    Line prefixes:
      "FP "   -- false positive promoted item
      "NOTE " -- slot-consumed annotation (merged-fact fallback, rule 2);
                 intentionally excluded from "FP "/"FN " grep counts
      "FN "   -- false negative label

    Output is deterministic: no wall clock, no randomness, no env-dependent
    ordering.
    """
    def _trunc(s: str) -> str:
        return (s[:_NOTE_TRUNCATE] + "...") if len(s) > _NOTE_TRUNCATE else s

    lines: list[str] = []
    for fixture_stem in sorted(misses_by_fixture.keys()):
        field_misses = misses_by_fixture[fixture_stem]
        has_any = any(v for v in field_misses.values())
        if not has_any:
            continue
        lines.append(f"fixture: {fixture_stem}")
        for field_name in sorted(field_misses.keys()):
            items = field_misses[field_name]
            if not items:
                continue
            lines.append(f"  field: {field_name}")
            for item in items:
                kind = item["kind"]
                if kind == "FP":
                    tier = item.get("tier", "")
                    frame = item.get("frame_type", "")
                    val = item.get("value", "")
                    snip = item.get("evidence_snippet", "")
                    provenance = f"[tier={tier} frame={frame}]" if frame else f"[tier={tier}]"
                    line = f"FP {provenance} {val!r}"
                    if snip:
                        line += f"  // {snip}"
                    lines.append(line)
                elif kind == "NOTE":
                    suppressed = _trunc(item.get("suppressed_value", ""))
                    label = _trunc(item.get("label", ""))
                    owner = _trunc(item.get("snippet_owner_value", ""))
                    lines.append(
                        f"NOTE slot-consumed: {suppressed!r} suppressed from FP list by"
                        f" fallback slot arithmetic (label {label!r} matched snippet of"
                        f" already-matched {owner!r}); treat as possible FP."
                    )
                else:
                    exp = item.get("expected_value", "")
                    cv = item.get("closest_value")
                    ct = item.get("closest_tier")
                    if cv is not None:
                        closest_str = f"closest=[{ct}] {cv!r}"
                    else:
                        closest_str = "no candidate"
                    lines.append(f"FN {exp!r}  // {closest_str}")
        lines.append("")
    return "\n".join(lines)


def _run_miss_audit(normalize_fn: Any, extract_fn: Any) -> dict[str, dict[str, list[dict]]]:
    """Run instance-level miss collection over all fixtures.

    Mirrors _run_calibration's fixture loop but collects per-instance misses
    instead of aggregating counts.  Returns a dict keyed by fixture stem.
    """
    from extraction.language import annotate_blocks as _annotate_blocks

    fixtures = sorted(_FIXTURES_DIR.glob("*.md"))
    misses_by_fixture: dict[str, dict[str, list[dict]]] = {}

    for fixture in fixtures:
        stem = fixture.stem
        labels_path = fixture.parent / (fixture.name + ".labels.json")
        if not labels_path.exists():
            continue
        labels = json.loads(labels_path.read_text(encoding="utf-8"))
        matter_type = FIXTURE_MATTER_TYPE.get(stem)

        doc = normalize_fn(str(fixture), "md")
        _annotate_blocks(getattr(doc, "blocks", []) or [], override=None)
        _extract_result = extract_fn(doc, matter_type=matter_type, input_source=fixture.name)
        result = _extract_result[0]
        candidate_manifest = _extract_result[1]
        er_dict = result.to_dict()

        misses_by_fixture[stem] = _collect_misses(er_dict, candidate_manifest, labels)

    return misses_by_fixture


# ---------------------------------------------------------------------------
# Per-fixture scoring
# ---------------------------------------------------------------------------

def _score_fixture(
    extraction_result: dict,
    candidate_manifest: dict,
    labels: dict,
) -> dict:
    """Compute per-field precision/recall/F1 for one fixture.

    Returns a dict keyed by field name, each with:
      {tp_promoted, fp_promoted, fn_labels, tp_hint,
       precision, recall_promoted, recall_combined, f1}

    Metric definitions:
      precision       = matched_promoted / all_promoted   (how much of what we promoted is correct)
      recall_promoted = labels matched by promoted / labels
      recall_combined = labels matched by (promoted + hint) / labels
      f1              = harmonic mean of precision and recall_promoted

    Raw counts are included for human audit.

    NOTE: _collect_misses mirrors this function's greedy walk for the
    --dump-misses audit; a change to scoring semantics here (or in
    _match_label_to_extractions) must be mirrored there.
    """
    fields_in_labels = labels.get("fields", {})
    per_field: dict[str, dict] = {}

    for field_name, label_list in fields_in_labels.items():
        if not isinstance(label_list, list):
            continue

        promoted_items = extraction_result.get(field_name, [])
        promoted_strs = [_entity_to_str(field_name, e) for e in promoted_items
                         if _entity_to_str(field_name, e)]
        hint_strs = _hint_strings_for_field(candidate_manifest, field_name)

        # Verbatim evidence snippets back the matcher's substring fallback.
        # Promoted-tier matching sees promoted-candidate snippets only; the
        # combined pool adds hint-candidate snippets for recall_combined.
        promoted_snippets = _evidence_snippets_for_field(
            candidate_manifest, field_name, ("promote",))
        combined_snippets = _evidence_snippets_for_field(
            candidate_manifest, field_name, ("promote", "hint"))

        n_labels = len(label_list)
        n_promoted = len(promoted_strs)
        use_date_rule = field_name in _DATE_BEARING_FIELDS

        # Match promoted against labels
        tp_promoted, _ = _match_label_to_extractions(
            label_list, promoted_strs, fallback_pool=promoted_snippets,
            date_rule=use_date_rule)
        fp_promoted = n_promoted - tp_promoted

        # For combined recall, pool promoted + hint (labels already consumed by promoted match first)
        # Re-run matching on combined pool; do NOT double-count labels.
        combined_strs = promoted_strs + hint_strs
        tp_combined, _ = _match_label_to_extractions(
            label_list, combined_strs, fallback_pool=combined_snippets,
            date_rule=use_date_rule)

        fn_labels = n_labels - tp_promoted  # labels not matched by promoted

        precision = tp_promoted / n_promoted if n_promoted else 0.0
        recall_promoted = tp_promoted / n_labels if n_labels else 0.0
        recall_combined = tp_combined / n_labels if n_labels else 0.0
        f1 = (2 * precision * recall_promoted / (precision + recall_promoted)
              if (precision + recall_promoted) else 0.0)

        per_field[field_name] = {
            "tp_promoted": tp_promoted,
            "fp_promoted": fp_promoted,
            "fn_labels": fn_labels,
            "n_labels": n_labels,
            "n_promoted": n_promoted,
            "tp_combined": tp_combined,
            "precision": round(precision, 4),
            "recall_promoted": round(recall_promoted, 4),
            "recall_combined": round(recall_combined, 4),
            "f1": round(f1, 4),
        }

    return per_field


# ---------------------------------------------------------------------------
# Selector accuracy block
# ---------------------------------------------------------------------------

def _score_selector(
    extraction_result: dict,
    labels: dict,
    recommend_fn: Any,
) -> dict:
    """Score selector accuracy for one fixture.

    Returns:
      {no_intent: {recommended, expected, match, confidence},
       with_intent: {recommended, expected, match, confidence, intent},
       clears_0.50: bool}

    clears_0.50 = with_intent: confidence >= 0.50 AND match.
    """
    from extraction.domain import ExtractionResult
    er = ExtractionResult.from_dict(extraction_result)

    expected_type = labels.get("expected_type", "")
    intent_block = labels.get("expected_type_with_intent", {})
    intent = intent_block.get("intent", "general")
    expected_type_with_intent = intent_block.get("type", expected_type)

    result_no_intent = recommend_fn(er, "general")
    result_with_intent = recommend_fn(er, intent)

    rec_no = result_no_intent.get("recommended_type", "")
    conf_no = result_no_intent.get("confidence", 0.0)
    match_no = rec_no == expected_type

    rec_wi = result_with_intent.get("recommended_type", "")
    conf_wi = result_with_intent.get("confidence", 0.0)
    match_wi = rec_wi == expected_type_with_intent

    # W1-gate condition: confidence >= 0.50 AND match with labelled type (with_intent path).
    clears_050 = bool(conf_wi >= 0.50 and match_wi)

    return {
        "no_intent": {
            "recommended": rec_no,
            "expected": expected_type,
            "match": match_no,
            "confidence": round(conf_no, 4),
        },
        "with_intent": {
            "recommended": rec_wi,
            "expected": expected_type_with_intent,
            "intent": intent,
            "match": match_wi,
            "confidence": round(conf_wi, 4),
        },
        "clears_0.50": clears_050,
    }


# ---------------------------------------------------------------------------
# Main calibration run
# ---------------------------------------------------------------------------

def _run_calibration(normalize_fn, extract_fn, recommend_fn) -> dict:
    """Run calibration over all fixtures; return the full JSON-serialisable report dict."""
    from extraction.language import annotate_blocks as _annotate_blocks

    fixtures = sorted(_FIXTURES_DIR.glob("*.md"))

    per_fixture_extraction: dict[str, dict] = {}
    per_fixture_selector: dict[str, dict] = {}

    # Accumulate counts for micro-averaging
    # per_field_counts: field_name -> {tp_p, fp_p, fn, n_lbl, n_prom, tp_c}
    per_field_counts: dict[str, dict] = {}
    all_tp: int = 0
    all_fp: int = 0
    all_fn: int = 0
    all_n_labels: int = 0
    all_n_promoted: int = 0
    all_tp_combined: int = 0

    selector_totals = {"no_intent_match": 0, "with_intent_match": 0, "total": 0, "clears_050": 0}

    for fixture in fixtures:
        stem = fixture.stem
        labels_path = fixture.parent / (fixture.name + ".labels.json")
        if not labels_path.exists():
            continue
        labels = json.loads(labels_path.read_text(encoding="utf-8"))

        matter_type = FIXTURE_MATTER_TYPE.get(stem)

        # In-process extraction: annotate block language before extracting so
        # FR harvesters activate on FR fixtures (mirrors extract_entities.py
        # auto-path: override=None, argument-for-argument match).
        doc = normalize_fn(str(fixture), "md")
        _annotate_blocks(getattr(doc, "blocks", []) or [], override=None)
        _extract_result = extract_fn(doc, matter_type=matter_type, input_source=fixture.name)
        result = _extract_result[0]
        candidate_manifest = _extract_result[1]
        er_dict = result.to_dict()

        # Score fields
        pf = _score_fixture(er_dict, candidate_manifest, labels)
        per_fixture_extraction[stem] = pf

        # Accumulate for micro-average
        for field_name, stats in pf.items():
            if field_name not in per_field_counts:
                per_field_counts[field_name] = {
                    "tp_promoted": 0, "fp_promoted": 0, "fn_labels": 0,
                    "n_labels": 0, "n_promoted": 0, "tp_combined": 0,
                }
            pfc = per_field_counts[field_name]
            pfc["tp_promoted"] += stats["tp_promoted"]
            pfc["fp_promoted"] += stats["fp_promoted"]
            pfc["fn_labels"] += stats["fn_labels"]
            pfc["n_labels"] += stats["n_labels"]
            pfc["n_promoted"] += stats["n_promoted"]
            pfc["tp_combined"] += stats["tp_combined"]

            all_tp += stats["tp_promoted"]
            all_fp += stats["fp_promoted"]
            all_fn += stats["fn_labels"]
            all_n_labels += stats["n_labels"]
            all_n_promoted += stats["n_promoted"]
            all_tp_combined += stats["tp_combined"]

        # Score selector
        sel = _score_selector(er_dict, labels, recommend_fn)
        per_fixture_selector[stem] = sel
        selector_totals["total"] += 1
        if sel["no_intent"]["match"]:
            selector_totals["no_intent_match"] += 1
        if sel["with_intent"]["match"]:
            selector_totals["with_intent_match"] += 1
        if sel["clears_0.50"]:
            selector_totals["clears_050"] += 1

    # Build per_field aggregate metrics
    per_field_agg: dict[str, dict] = {}
    for field_name, counts in sorted(per_field_counts.items()):
        tp_p = counts["tp_promoted"]
        fp_p = counts["fp_promoted"]
        n_lbl = counts["n_labels"]
        n_prom = counts["n_promoted"]
        tp_c = counts["tp_combined"]
        prec = tp_p / n_prom if n_prom else 0.0
        rec_p = tp_p / n_lbl if n_lbl else 0.0
        rec_c = tp_c / n_lbl if n_lbl else 0.0
        f1 = (2 * prec * rec_p / (prec + rec_p)) if (prec + rec_p) else 0.0
        per_field_agg[field_name] = {
            "ownership": FIELD_OWNERSHIP.get(field_name, "script"),
            "tp_promoted": tp_p,
            "fp_promoted": fp_p,
            "fn_labels": n_lbl - tp_p,
            "n_labels": n_lbl,
            "n_promoted": n_prom,
            "tp_combined": tp_c,
            "precision": round(prec, 4),
            "recall_promoted": round(rec_p, 4),
            "recall_combined": round(rec_c, 4),
            "f1": round(f1, 4),
        }

    # Aggregate micro-average (all fields)
    agg_prec = all_tp / all_n_promoted if all_n_promoted else 0.0
    agg_rec_p = all_tp / all_n_labels if all_n_labels else 0.0
    agg_rec_c = all_tp_combined / all_n_labels if all_n_labels else 0.0
    agg_f1 = ((2 * agg_prec * agg_rec_p / (agg_prec + agg_rec_p))
               if (agg_prec + agg_rec_p) else 0.0)

    # Micro-average over script-owned fields only
    scr_tp: int = 0
    scr_fp: int = 0
    scr_fn: int = 0
    scr_n_lbl: int = 0
    scr_n_prom: int = 0
    scr_tp_c: int = 0
    for field_name, counts in per_field_counts.items():
        if FIELD_OWNERSHIP.get(field_name, "script") != "script":
            continue
        scr_tp += counts["tp_promoted"]
        scr_fp += counts["fp_promoted"]
        scr_fn += counts["n_labels"] - counts["tp_promoted"]
        scr_n_lbl += counts["n_labels"]
        scr_n_prom += counts["n_promoted"]
        scr_tp_c += counts["tp_combined"]
    scr_prec = scr_tp / scr_n_prom if scr_n_prom else 0.0
    scr_rec_p = scr_tp / scr_n_lbl if scr_n_lbl else 0.0
    scr_rec_c = scr_tp_c / scr_n_lbl if scr_n_lbl else 0.0
    scr_f1 = ((2 * scr_prec * scr_rec_p / (scr_prec + scr_rec_p))
               if (scr_prec + scr_rec_p) else 0.0)

    total = selector_totals["total"]
    sel_acc_no = selector_totals["no_intent_match"] / total if total else 0.0
    sel_acc_wi = selector_totals["with_intent_match"] / total if total else 0.0

    return {
        "per_field": per_field_agg,
        "per_fixture": {
            stem: {
                "extraction": per_fixture_extraction[stem],
                "selector": per_fixture_selector[stem],
            }
            for stem in sorted(per_fixture_extraction.keys())
        },
        "aggregate": {
            "tp_promoted": all_tp,
            "fp_promoted": all_fp,
            "fn_labels": all_fn,
            "n_labels": all_n_labels,
            "n_promoted": all_n_promoted,
            "tp_combined": all_tp_combined,
            "precision": round(agg_prec, 4),
            "recall_promoted": round(agg_rec_p, 4),
            "recall_combined": round(agg_rec_c, 4),
            "f1": round(agg_f1, 4),
        },
        "aggregate_script_scope": {
            "tp_promoted": scr_tp,
            "fp_promoted": scr_fp,
            "fn_labels": scr_fn,
            "n_labels": scr_n_lbl,
            "n_promoted": scr_n_prom,
            "tp_combined": scr_tp_c,
            "precision": round(scr_prec, 4),
            "recall_promoted": round(scr_rec_p, 4),
            "recall_combined": round(scr_rec_c, 4),
            "f1": round(scr_f1, 4),
        },
        "selector": {
            "per_fixture": per_fixture_selector,
            "totals": {
                "no_intent_match": selector_totals["no_intent_match"],
                "with_intent_match": selector_totals["with_intent_match"],
                "total": total,
                "clears_0.50": selector_totals["clears_050"],
                "accuracy_no_intent": round(sel_acc_no, 4),
                "accuracy_with_intent": round(sel_acc_wi, 4),
            },
        },
    }


# ---------------------------------------------------------------------------
# Advisory tuning loop
# ---------------------------------------------------------------------------

def _tune(
    normalize_fn, extract_fn, recommend_fn,
    baseline: dict,
    lex_module: Any,
    res_module: Any,
    rules_list: list,
) -> str:
    """Grid-search threshold and selector-weight proposals; return advisory text.

    Mechanics:
      - All patching is in-process only; no files are written.
      - Thresholds are re-applied by patching both extraction.lexicon and
        extraction.resolver (the resolver imports constants at module load; both
        must be patched for consistent behaviour).
      - Selector-weight variants patch the RULES list in-place via a multiplier
        applied to one rule's weight at a time.
      - The 0.50 selector-interrupt line is NOT in the search grid.  It is a
        hard W1-gate condition, not a quality objective; tuning it would
        conflate acceptance criteria with fitness metric.
      - A try/finally block restores every patched value regardless of errors.
      - Runtime target: under ~3 minutes; coarse grid keeps it well under that.

    Primary metric: aggregate F1 (extraction quality).
    Secondary metric: selector accuracy with_intent.
    Proposals emitted only when primary metric strictly improves.
    """
    base_f1 = baseline["aggregate"]["f1"]
    base_sel = baseline["selector"]["totals"]["accuracy_with_intent"]

    proposals: list[dict] = []

    # ----- Threshold grid -----
    # Combos that preserve the ordering HINT_MIN < PROMOTE_WITH_CORROBORATION < PROMOTE_AUTO.
    # The selector-interrupt 0.50 confidence line is excluded by design: it is not
    # one of the swept parameters (changing it requires the Ask-first boundary).
    promote_auto_grid = [0.75, 0.80, 0.85, 0.90]
    pwc_grid = [0.55, 0.60, 0.65, 0.70]
    hint_min_grid = [0.35, 0.40, 0.45, 0.50]

    orig_lex_pa = lex_module.PROMOTE_AUTO
    orig_lex_pwc = lex_module.PROMOTE_WITH_CORROBORATION
    orig_lex_hm = lex_module.HINT_MIN
    orig_res_pa = res_module.PROMOTE_AUTO
    orig_res_pwc = res_module.PROMOTE_WITH_CORROBORATION
    orig_res_hm = res_module.HINT_MIN

    # Record current (baseline) threshold values for proposal block.
    current_pa = orig_lex_pa
    current_pwc = orig_lex_pwc
    current_hm = orig_lex_hm

    try:
        for pa in promote_auto_grid:
            for pwc in pwc_grid:
                for hm in hint_min_grid:
                    # Enforce ordering: HINT_MIN < PWC < PA
                    if not (hm < pwc < pa):
                        continue
                    # Skip if this is the baseline (no change)
                    if (abs(pa - current_pa) < 1e-9
                            and abs(pwc - current_pwc) < 1e-9
                            and abs(hm - current_hm) < 1e-9):
                        continue

                    lex_module.PROMOTE_AUTO = pa
                    lex_module.PROMOTE_WITH_CORROBORATION = pwc
                    lex_module.HINT_MIN = hm
                    res_module.PROMOTE_AUTO = pa
                    res_module.PROMOTE_WITH_CORROBORATION = pwc
                    res_module.HINT_MIN = hm
                    try:
                        variant = _run_calibration(normalize_fn, extract_fn, recommend_fn)
                    finally:
                        lex_module.PROMOTE_AUTO = orig_lex_pa
                        lex_module.PROMOTE_WITH_CORROBORATION = orig_lex_pwc
                        lex_module.HINT_MIN = orig_lex_hm
                        res_module.PROMOTE_AUTO = orig_res_pa
                        res_module.PROMOTE_WITH_CORROBORATION = orig_res_pwc
                        res_module.HINT_MIN = orig_res_hm

                    new_f1 = variant["aggregate"]["f1"]
                    new_sel = variant["selector"]["totals"]["accuracy_with_intent"]
                    if new_f1 > base_f1:
                        proposals.append({
                            "type": "threshold",
                            "params": {"PROMOTE_AUTO": pa,
                                       "PROMOTE_WITH_CORROBORATION": pwc,
                                       "HINT_MIN": hm},
                            "current": {"PROMOTE_AUTO": current_pa,
                                        "PROMOTE_WITH_CORROBORATION": current_pwc,
                                        "HINT_MIN": current_hm},
                            "delta_f1": round(new_f1 - base_f1, 4),
                            "delta_sel": round(new_sel - base_sel, 4),
                            "new_f1": round(new_f1, 4),
                            "new_sel": round(new_sel, 4),
                        })
    finally:
        # Guarantee restoration even if interrupted mid-loop.
        lex_module.PROMOTE_AUTO = orig_lex_pa
        lex_module.PROMOTE_WITH_CORROBORATION = orig_lex_pwc
        lex_module.HINT_MIN = orig_lex_hm
        res_module.PROMOTE_AUTO = orig_res_pa
        res_module.PROMOTE_WITH_CORROBORATION = orig_res_pwc
        res_module.HINT_MIN = orig_res_hm

    # ----- Selector weight grid -----
    # One-rule-at-a-time multipliers; other rules stay at baseline weight.
    # The 0.50 interrupt line (hard W1-gate) is not a RULES weight; it is
    # derived in recommend() via confidence thresholding and is excluded here.
    weight_multipliers = [0.6, 0.8, 1.2, 1.4]

    for rule_idx, (fld, types, weight) in enumerate(rules_list):
        orig_weight = weight
        for mult in weight_multipliers:
            new_weight = round(orig_weight * mult, 4)
            if abs(new_weight - orig_weight) < 1e-9:
                continue
            # Patch in-place; rules_list is the mutable RULES object from diagram_selector.
            rules_list[rule_idx] = (fld, types, new_weight)
            try:
                variant = _run_calibration(normalize_fn, extract_fn, recommend_fn)
            finally:
                rules_list[rule_idx] = (fld, types, orig_weight)

            new_f1 = variant["aggregate"]["f1"]
            new_sel = variant["selector"]["totals"]["accuracy_with_intent"]
            if new_f1 > base_f1:
                proposals.append({
                    "type": "selector_weight",
                    "params": {"rule_field": fld, "weight": new_weight},
                    "current": {"rule_field": fld, "weight": orig_weight},
                    "delta_f1": round(new_f1 - base_f1, 4),
                    "delta_sel": round(new_sel - base_sel, 4),
                    "new_f1": round(new_f1, 4),
                    "new_sel": round(new_sel, 4),
                })

    # Sort by delta_f1 descending; take top 10 for the proposal block.
    proposals.sort(key=lambda p: p["delta_f1"], reverse=True)

    lines: list[str] = [
        "",
        "WARNING: proposals tuned on a small fixture corpus; high overfit risk. "
        "Adopt only via reviewed commit; regenerate goldens after adoption.",
        "",
        f"Baseline: aggregate_f1={round(base_f1, 4)}, "
        f"selector_accuracy_with_intent={round(base_sel, 4)}",
        "",
    ]

    if not proposals:
        lines.append("No proposals: no parameter change produced a strictly positive F1 delta.")
    else:
        lines.append(f"Top proposals (of {len(proposals)} with positive F1 delta):")
        for rank, prop in enumerate(proposals[:10], 1):
            p_type = prop["type"]
            delta_f1 = prop["delta_f1"]
            delta_sel = prop["delta_sel"]
            new_f1 = prop["new_f1"]
            new_sel = prop["new_sel"]
            if p_type == "threshold":
                curr = prop["current"]
                proposed = prop["params"]
                lines.append(
                    f"  #{rank} [threshold] "
                    f"PROMOTE_AUTO {curr['PROMOTE_AUTO']}->{proposed['PROMOTE_AUTO']}  "
                    f"PROMOTE_WITH_CORROBORATION {curr['PROMOTE_WITH_CORROBORATION']}->"
                    f"{proposed['PROMOTE_WITH_CORROBORATION']}  "
                    f"HINT_MIN {curr['HINT_MIN']}->{proposed['HINT_MIN']}  "
                    f"| F1 +{delta_f1} (={new_f1})  sel_acc_wi {delta_sel:+.4f} (={new_sel})"
                )
            else:
                curr = prop["current"]
                proposed = prop["params"]
                lines.append(
                    f"  #{rank} [selector_weight] "
                    f"rule '{proposed['rule_field']}' weight "
                    f"{curr['weight']}->{proposed['weight']}  "
                    f"| F1 +{delta_f1} (={new_f1})  sel_acc_wi {delta_sel:+.4f} (={new_sel})"
                )

    lines.append("")
    lines.append("Note: the 0.50 selector-interrupt confidence line is not a tunable parameter")
    lines.append("      (it is the W1-gate acceptance criterion, not a quality objective).")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Calibration harness for legal-diagram extraction + selector. "
                    "Run from skill root: python scripts/tests/calibrate.py"
    )
    parser.add_argument(
        "--tune",
        action="store_true",
        help="Append advisory tuning proposals after JSON output.",
    )
    parser.add_argument(
        "--dump-misses",
        action="store_true",
        help=(
            "Append instance-level miss audit (FPs and FNs per fixture+field) "
            "after JSON output.  Prefixes FP lines with 'FP ' and FN lines "
            "with 'FN ' for grep-friendly filtering."
        ),
    )
    args = parser.parse_args()

    normalize_fn, extract_fn, recommend_fn, lex_module, res_module, rules_list = _import_stack()

    report = _run_calibration(normalize_fn, extract_fn, recommend_fn)

    # Default mode: exactly one JSON document to stdout (machine-parseable).
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if args.tune:
        t0 = time.monotonic()
        proposal_text = _tune(
            normalize_fn, extract_fn, recommend_fn,
            baseline=report,
            lex_module=lex_module,
            res_module=res_module,
            rules_list=rules_list,
        )
        elapsed = time.monotonic() - t0
        # Append human-readable proposals after the JSON.
        print(proposal_text)
        print(f"Tuning wall time: {elapsed:.1f}s")

    if args.dump_misses:
        misses_by_fixture = _run_miss_audit(normalize_fn, extract_fn)
        dump_text = format_miss_dump(misses_by_fixture)
        # Append miss audit after JSON (and after --tune block if both flags set).
        # The separator keeps downstream JSON consumers safe: parse up to separator.
        print(_MISS_AUDIT_SEPARATOR)
        print(dump_text)


if __name__ == "__main__":
    main()
