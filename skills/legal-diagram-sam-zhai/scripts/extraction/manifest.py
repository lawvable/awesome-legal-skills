import re
from typing import Any, Dict, List

from extraction.domain import ENTITY_FIELDS, ExtractionResult
from extraction.handoff import build_legacy_directives

LLM_ONLY = {
    "decision_points": "Scan obligations, conditions, and process_steps for if/then logic.",
}
NULL_FIELDS = [
    ("obligations", "risk_level", "Classify each obligation high/medium/low from language."),
]
HINT_GATE = 0.75

# Lowercase substring stems used to score document profiles from raw text.
PROFILE_KEYWORDS: Dict[str, List[str]] = {
    "privacy": [
        "personal data",
        "personal information",
        "data subject",
        "controller",
        "processor",
        "consent",
        "retention",
        "safeguard",
        "disclosure",
        "data breach",
    ],
    "litigation": [
        "plaintiff",
        "defendant",
        "appellant",
        "respondent",
        " v. ",
        "court",
        "judge",
        "motion",
        "appeal",
        "hearing",
        "tribunal",
    ],
    "governance": [
        "board",
        "director",
        "resolution",
        "quorum",
        "committee",
        "shareholder",
        "by-law",
        "minutes",
        "approval",
    ],
    "risk_assessment": [
        "risk",
        "likelihood",
        "impact",
        "mitigat",
        "residual",
        "exposure",
        "control gap",
        "rating",
    ],
}

# Fields to populate via directed_inference when a profile is active and the field is absent.
PROFILE_TARGETS: Dict[str, List[str]] = {
    "privacy": ["data_flows", "risk_items", "controls"],
    "litigation": ["decision_points", "concepts", "legal_authorities", "events"],
    "governance": ["decision_points", "process_steps"],
    "risk_assessment": ["risk_items", "controls"],
}


# Pre-compiled word-boundary patterns for each keyword/stem.
# Multi-word phrases (e.g. "personal data", " v. ", "control gap") are matched
# with a leading \b on the first word character; single-word stems use \b<stem>.
def _compile_keyword_pattern(kw: str) -> re.Pattern[str]:
    """Return a compiled regex that matches kw at a word boundary."""
    stripped = kw.strip()
    # Escape special regex chars in the keyword, then anchor with \b at start.
    escaped = re.escape(stripped)
    return re.compile(r"\b" + escaped, re.I)


_PROFILE_PATTERNS: Dict[str, list] = {
    profile: [_compile_keyword_pattern(kw) for kw in keywords]
    for profile, keywords in PROFILE_KEYWORDS.items()
}


def profile_signals(doc_text: str) -> Dict[str, float]:
    """Score each profile against raw document text.

    For each profile, count DISTINCT keyword stems present in the lowercased text
    using word-boundary anchored regex so substrings inside longer words do not
    trigger a match (e.g. 'risk' must not match inside 'brisket' or 'frisky').
    Score = round(min(count / 3.0, 1.0), 2). A profile is active when score >= 0.34
    (i.e. at least 2 distinct keywords matched).
    """
    scores: Dict[str, float] = {}
    for profile, patterns in _PROFILE_PATTERNS.items():
        distinct_hits = sum(1 for pat in patterns if pat.search(doc_text))
        scores[profile] = round(min(distinct_hits / 3.0, 1.0), 2)
    return scores


def build_manifest(
    r: ExtractionResult | None = None,
    candidate_manifest: Dict[str, Any] | None = None,
    llm_enrichment: Dict[str, Any] | None = None,
    doc_text: str = "",
    *,
    doc: Any = None,
    extraction_result: ExtractionResult | None = None,
    candidates: list | None = None,
    decisions: list | None = None,
    evidence_packets: list | None = None,
) -> Dict[str, Any]:
    # Support new keyword-based call style: build_manifest(doc=..., extraction_result=..., ...)
    if r is None and extraction_result is not None:
        r = extraction_result
    if r is None:
        r = ExtractionResult()

    populated = [k for k in ENTITY_FIELDS if getattr(r, k)]
    hint_fields = sorted({h.suggested_field for h in r.extraction_hints})
    hint_only = [f for f in hint_fields if f not in populated]
    absent = [k for k in ENTITY_FIELDS if k not in populated and k not in hint_only]

    signals = profile_signals(doc_text)

    candidate_manifest = candidate_manifest or {
        "schema_version": "legal-diagram-candidates",
        "structure_metrics": {},
        "warning_codes": [],
        "evidence_packets": [],
        "candidates": [],
        "promotion_decisions": [],
    }
    llm_enrichment = llm_enrichment or {"mode": "json_patch_only", "evidence_packets": [], "directives": []}

    # Merge legacy directives into the single canonical directive lane.
    legacy = build_legacy_directives(r, doc_text)
    merged_directives = list(llm_enrichment.get("directives", [])) + legacy
    llm_enrichment = {**llm_enrichment, "directives": merged_directives}

    return {
        "extraction_result": r.to_dict(),
        "extraction_hints": [{"id": f"H{i}", **_hint(h)} for i, h in enumerate(r.extraction_hints)],
        "coverage": {
            "populated_fields": populated,
            "hint_only_fields": hint_only,
            "absent_fields": absent,
            "signal_map": r.signal_map,
        },
        "matter_type_evidence": _matter_evidence(r),
        "candidate_manifest": candidate_manifest,
        "llm_enrichment": llm_enrichment,
        "profile_signals": signals,
    }


def _hint(h) -> Dict[str, Any]:
    return {
        "hint_type": h.hint_type,
        "suggested_field": h.suggested_field,
        "snippet": h.snippet,
        "confidence": h.confidence,
        "anchor": h.anchor,
        "context_heading": h.context_heading,
    }


def _matter_evidence(r: ExtractionResult) -> Dict[str, Any]:
    signals: List[str] = []
    scores: Dict[str, float] = {}
    if r.legal_authorities:
        scores["litigation"] = scores.get("litigation", 0) + 0.3
    if r.ownership_links or r.entities:
        scores["corporate"] = scores.get("corporate", 0) + 0.3
    if r.obligations and r.controls:
        scores["compliance"] = scores.get("compliance", 0) + 0.3
    if r.ip_assets:
        scores["ip"] = scores.get("ip", 0) + 0.4
    if r.claim_classes:
        scores["bankruptcy"] = scores.get("bankruptcy", 0) + 0.4
    return {"candidates": scores, "signals": signals}
