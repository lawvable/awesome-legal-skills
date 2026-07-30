from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .schema import Candidate, CandidateManifest, EvidencePacket, PromotionDecision, SCHEMA_VERSION


def build_candidate_manifest(
    doc: Any,
    evidence_packets: list[EvidencePacket],
    candidates: list[Candidate],
    decisions: list[PromotionDecision],
    synthetic_table_block_count: int = 0,
) -> dict[str, Any]:
    used_evidence = filter_evidence(evidence_packets, candidates)
    manifest = CandidateManifest(
        schema_version=SCHEMA_VERSION,
        structure_metrics=structure_metrics(doc, synthetic_table_block_count),
        warning_codes=warning_codes(doc, candidates),
        evidence_packets=used_evidence,
        candidates=candidates,
        promotion_decisions=decisions,
    )
    return asdict(manifest)


def build_llm_enrichment(candidate_manifest: dict[str, Any]) -> dict[str, Any]:
    decisions = {d.get("candidate_id"): d for d in candidate_manifest.get("promotion_decisions", [])}
    candidates = candidate_manifest.get("candidates", [])
    evidence_by_id = {e.get("id"): e for e in candidate_manifest.get("evidence_packets", [])}
    wanted_evidence: dict[str, dict[str, Any]] = {}
    directives: list[dict[str, Any]] = []
    for cand in candidates:
        decision = decisions.get(cand.get("id"), {})
        if decision.get("action") != "hint":
            continue
        evidence_ids = list(cand.get("evidence_ids", []))
        for evidence_id in evidence_ids:
            if evidence_id in evidence_by_id:
                wanted_evidence[evidence_id] = evidence_by_id[evidence_id]
        confidence = float(cand.get("confidence", 0.0) or 0.0)
        read_policy = "snippet_plus_neighboring_block" if confidence < 0.50 else "snippet_only"
        directives.append(
            {
                "type": "resolve_candidate",
                "candidate_id": cand.get("id"),
                "field": cand.get("target_field"),
                "frame_type": cand.get("frame_type"),
                "confidence": confidence,
                "targets": [],
                "hint_ids": [],
                "evidence_ids": evidence_ids,
                "read_policy": read_policy,
                "instruction": "Resolve only from supplied evidence. Return JSON Patch operations with evidence_id and source_ref, or add an extraction_warning if unsupported.",
            }
        )
    return {
        "mode": "json_patch_only",
        "read_policy": {
            "high_confidence": "no_reread",
            "medium_confidence": "snippet_only",
            "low_confidence": "snippet_plus_neighboring_block",
            "contradiction_or_missing_role_date": "heading_section_window",
        },
        "evidence_packets": list(wanted_evidence.values()),
        "directives": directives,
    }


def build_legacy_directives(r: Any, doc_text: str) -> list[dict[str, Any]]:
    """Build the six legacy directive types from an ExtractionResult and raw document text.

    These directives are merged into ``llm_enrichment["directives"]`` by
    ``build_manifest`` so that all directive types share one canonical lane.

    Normalised shape for every directive:
        type, field, instruction, targets[], hint_ids[], evidence_ids[], read_policy
    ``resolve_candidate`` directives (produced by ``build_llm_enrichment``) additionally
    carry ``candidate_id``, ``frame_type``, and ``confidence``.
    Absent values are empty lists or empty strings, never missing keys.
    """
    # Import manifest constants lazily to avoid a circular import at module level.
    from .manifest import (
        NULL_FIELDS,
        HINT_GATE,
        LLM_ONLY,
        ENTITY_FIELDS,
        PROFILE_TARGETS,
        profile_signals,
    )

    populated = [k for k in ENTITY_FIELDS if getattr(r, k)]
    hint_fields = sorted({h.suggested_field for h in r.extraction_hints})
    hint_only = [f for f in hint_fields if f not in populated]
    absent = [k for k in ENTITY_FIELDS if k not in populated and k not in hint_only]

    directives: list[dict[str, Any]] = []

    _empty: dict[str, Any] = {
        "targets": [],
        "hint_ids": [],
        "evidence_ids": [],
        "read_policy": "",
    }

    for field_name, attr, instr in NULL_FIELDS:
        items = getattr(r, field_name)
        targets = [getattr(it, "id", str(i)) for i, it in enumerate(items) if getattr(it, attr, None) is None]
        if targets:
            directives.append({
                **_empty,
                "type": "null_field_classification",
                "field": f"{field_name}[].{attr}",
                "instruction": instr,
                "targets": targets,
            })

    for i, h in enumerate(r.extraction_hints):
        if h.confidence < HINT_GATE:
            directives.append({
                **_empty,
                "type": "hint_resolution",
                "field": h.suggested_field,
                "instruction": f"Resolve hint into {h.suggested_field} from snippet at {h.anchor}.",
                "hint_ids": [f"H{i}"],
            })

    for field_name, instr in LLM_ONLY.items():
        directives.append({
            **_empty,
            "type": "implicit_inference",
            "field": field_name,
            "instruction": instr,
        })

    if r.obligations and (r.controls or "controls" in hint_only):
        directives.append({
            **_empty,
            "type": "cross_linking",
            "field": "controls[].obligation_id",
            "instruction": "Link each control to the obligation it satisfies by proximity/id.",
            "targets": [o.id for o in r.obligations],
        })

    if not r.matter_type:
        directives.append({
            **_empty,
            "type": "matter_type_resolution",
            "field": "matter_type",
            "instruction": "Pick highest-evidence candidate; ask only if tied in tutorial mode.",
        })

    signals = profile_signals(doc_text)
    emitted_fields: set[str] = set()
    for profile, score in signals.items():
        if score < 0.34:
            continue
        for field in PROFILE_TARGETS.get(profile, []):
            if field in absent and field not in emitted_fields:
                emitted_fields.add(field)
                directives.append({
                    **_empty,
                    "type": "directed_inference",
                    "field": field,
                    "instruction": (
                        f"Profile '{profile}' active (score {score}); '{field}' is absent."
                        f" Populate {field} from a bounded read of the source around"
                        " supporting spans only; every added entity carries evidence_id"
                        " and source_ref. No textual support: leave empty and add an"
                        " extraction_warning."
                    ),
                })

    return directives


def filter_evidence(evidence: list[EvidencePacket], candidates: list[Candidate]) -> list[EvidencePacket]:
    used = {eid for cand in candidates for eid in cand.evidence_ids}
    return [e for e in evidence if e.id in used]


def structure_metrics(doc: Any, synthetic_table_blocks: int = 0) -> dict[str, int]:
    base = dict(getattr(doc, "structure_metrics", None) or {})
    if not base:
        blocks = list(getattr(doc, "blocks", []) or [])
        base = {
            "headings": sum(1 for b in blocks if getattr(b, "block_type", "") == "heading"),
            "lists": sum(1 for b in blocks if getattr(b, "block_type", "") == "list_item"),
            "tables": len(list(getattr(doc, "tables", []) or [])),
            "paragraphs": sum(1 for b in blocks if getattr(b, "block_type", "") == "paragraph"),
            "blocks": len(blocks),
        }
    return {**base, "table_rows": synthetic_table_blocks}


def warning_codes(doc: Any, candidates: list[Candidate]) -> list[str]:
    warnings: list[str] = []
    for code in getattr(doc, "warning_codes", []) or []:
        if code not in warnings:
            warnings.append(code)
    if getattr(doc, "truncated", False):
        warnings.append("SOURCE_TRUNCATED")
    if not getattr(doc, "blocks", None) and not getattr(doc, "tables", None):
        if "SOURCE_UNPARSEABLE_OR_EMPTY" not in warnings:
            warnings.append("SOURCE_UNPARSEABLE_OR_EMPTY")
    if getattr(doc, "source_format", "") == "pdf" and not getattr(doc, "blocks", None):
        warnings.append("PDF_NO_TEXT_BLOCKS")
    if not candidates:
        warnings.append("NO_CANDIDATES")
    return warnings
