from __future__ import annotations

import dataclasses
from collections import defaultdict
from dataclasses import fields
from typing import Any, Callable, Optional

_MISSING = dataclasses.MISSING

from .domain import (
    ClaimClass,
    Communication,
    Concept,
    ConditionPrecedent,
    Control,
    Deadline,
    DecisionPoint,
    Document,
    Entity,
    Event,
    ExtractionHint,
    ExtractionResult,
    LegalAuthority,
    Obligation,
    OwnershipLink,
    Party,
    Relationship,
    RiskItem,
    Transfer,
)

from .schema import Candidate, EvidencePacket, PromotionDecision
from .utils import amount_number, clean_text, deadline_text, strip_diacritics

PREFIXES = {
    "obligations": "OBL",
    "controls": "CTRL",
    "conditions": "COND",
    "concepts": "CON",
    "process_steps": "STEP",
    "investigation_steps": "INV",
    "negotiation_issues": "NEG",
}


def materialize_result(
    candidates: list[Candidate],
    decisions: list[PromotionDecision],
    evidence_packets: list[EvidencePacket],
    *,
    matter_type: Optional[str] = None,
    input_source: Optional[str] = None,
    truncated: bool = False,
) -> tuple[ExtractionResult, list[PromotionDecision]]:
    result = ExtractionResult(matter_type=matter_type, input_source=input_source, truncated=truncated)
    decisions_by_id = {d.candidate_id: d for d in decisions}
    evidence_by_id = {e.id: e for e in evidence_packets}
    counters: defaultdict[str, int] = defaultdict(int)

    for cand in candidates:
        decision = decisions_by_id.get(cand.id)
        if decision is None:
            continue
        if decision.action == "promote":
            entity, missing = candidate_to_entity(cand, counters)
            if missing:
                decision.action = "hint"
                decision.reason = "missing_required_fields: " + ",".join(missing)
                decision.final_entity_id = None
                _append_hint(result, cand, evidence_by_id)
                continue
            getattr(result, cand.target_field).append(entity)
            decision.final_entity_id = getattr(entity, "id", None) or f"candidate:{cand.id}"
        elif decision.action == "hint":
            _append_hint(result, cand, evidence_by_id)

    result.signal_map = build_signal_map(candidates)
    result.hierarchy = build_hierarchy(candidates, decisions)
    return result, decisions


def candidate_to_entity(cand: Candidate, counters: defaultdict[str, int]) -> tuple[Any, list[str]]:
    value = dict(cand.normalized_value)
    field = cand.target_field
    make_id = lambda: _next_id(field, counters)
    builders: dict[str, Callable[[], Any]] = {
        "parties": lambda: Party(name=value.get("name", ""), role=value.get("role") or "party", type=value.get("type") or "party"),
        "entities": lambda: Entity(name=value.get("name", ""), type=value.get("type") or value.get("entity_type") or "entity", attributes=_extra_attributes(Entity, value)),
        "events": lambda: Event(date=value.get("date", "") or value.get("date_or_timing", ""), description=value.get("description", ""), actor=value.get("actor")),
        "deadlines": lambda: Deadline(date=value.get("date") or value.get("date_or_timing") or deadline_text(value.get("description", "")) or "", description=value.get("description", ""), party=value.get("party") or "unspecified", consequence=value.get("consequence")),
        "obligations": lambda: Obligation(id=make_id(), description=value.get("description", ""), party=value.get("party") or "unspecified", source_law=value.get("source_law"), risk_level=value.get("risk_level"), verify_method=value.get("verify_method"), status=value.get("status"), deadline=value.get("deadline")),
        "controls": lambda: Control(id=make_id(), description=value.get("description", ""), obligation_id=value.get("obligation_id") or "unlinked", owner=value.get("owner"), evidence_documents=list(value.get("evidence_documents") or []), audit_status=value.get("audit_status"), audit_date=value.get("audit_date")),
        "conditions": lambda: ConditionPrecedent(id=make_id(), description=value.get("description", ""), responsible_party=value.get("responsible_party"), evidence_needed=value.get("evidence_needed"), satisfied=bool(value.get("satisfied", False)), satisfaction_date=value.get("satisfaction_date")),
        "relationships": lambda: Relationship(from_entity=value.get("from_entity", ""), to_entity=value.get("to_entity", ""), type=value.get("type") or cand.frame_type, description=value.get("description"), cardinality_from=value.get("cardinality_from"), cardinality_to=value.get("cardinality_to")),
        "ownership_links": lambda: OwnershipLink(parent=value.get("parent", ""), child=value.get("child", ""), percentage=value.get("percentage")),
        "decision_points": lambda: DecisionPoint(question=value.get("question", ""), yes_path=value.get("yes_path") or "yes", no_path=value.get("no_path") or "no"),
        "communications": lambda: Communication(from_party=value.get("from_party") or "unspecified", to_party=value.get("to_party") or "unspecified", date=value.get("date"), comm_type=value.get("comm_type") or "notice", description=value.get("description", ""), delivery_method=value.get("delivery_method"), sequence_order=value.get("sequence_order")),
        "concepts": lambda: Concept(id=make_id(), name=value.get("name", ""), concept_type=value.get("concept_type") or cand.frame_type, description=value.get("description"), supporting_facts=list(value.get("supporting_facts") or [])),
        "risk_items": lambda: RiskItem(label=value.get("label", ""), x_score=float(value.get("x_score", 0.5)), y_score=float(value.get("y_score", 0.5)), description=value.get("description"), category=value.get("category")),
        "transfers": lambda: Transfer(from_party=value.get("from_party") or "unspecified", to_party=value.get("to_party") or "unspecified", description=value.get("description", ""), amount=amount_number(value.get("amount_text")) if value.get("amount") is None else value.get("amount"), mechanism=value.get("mechanism"), triggered_by=value.get("triggered_by")),
        "claim_classes": lambda: ClaimClass(priority_rank=int(value.get("priority_rank") or 1), name=value.get("name", ""), claim_amount=value.get("claim_amount"), claim_type=value.get("claim_type")),
        "documents": lambda: Document(name=value.get("name", ""), type=value.get("type") or cand.frame_type, date=value.get("date"), parties=list(value.get("parties") or [])),
        "legal_authorities": lambda: LegalAuthority(citation=value.get("citation", ""), authority_type=value.get("authority_type") or cand.frame_type, jurisdiction=value.get("jurisdiction"), hierarchy_level=value.get("hierarchy_level"), cites=list(value.get("cites") or [])),
    }
    builder = builders.get(field)
    if builder is None:
        return None, [field]
    entity = builder()
    missing = _missing_required(entity)
    return entity, missing


def _slug(text: str) -> str:
    # W3.4: NFD transliteration runs before the existing ID normalisation so that
    # accented FR headings yield ASCII-safe Mermaid node IDs; labels keep accents.
    return "".join(ch for ch in strip_diacritics(text).lower() if ch.isalnum()) or "x"


def build_hierarchy(
    candidates: list[Candidate],
    decisions: list[PromotionDecision],
    *,
    max_depth: int = 2,
) -> list[dict[str, Any]]:
    """Deterministic hierarchy seed from promoted candidates' heading paths.

    Each distinct heading-path prefix (capped at max_depth + 1 levels) becomes one
    node: {id, label, parent, depth, source}. Depth 0 = outermost heading.
    """
    decisions_by_id = {d.candidate_id: d for d in decisions}
    nodes: dict[str, dict[str, Any]] = {}
    for cand in candidates:
        decision = decisions_by_id.get(cand.id)
        if decision is None or decision.action != "promote":
            continue
        parent_id = None
        for depth, heading in enumerate(cand.source_ref.heading_path or []):
            if depth > max_depth:
                break
            node_id = f"{parent_id}-{_slug(heading)}" if parent_id else f"H-{_slug(heading)}"
            nodes.setdefault(node_id, {"id": node_id, "label": heading, "parent": parent_id,
                                       "depth": depth, "source": "deterministic"})
            parent_id = node_id
    return list(nodes.values())


def build_signal_map(candidates: list[Candidate]) -> dict[str, float]:
    signal_map: dict[str, float] = {}
    for cand in candidates:
        key = f"extractor.{cand.target_field}.{cand.frame_type}"
        signal_map[key] = max(signal_map.get(key, 0.0), cand.confidence)
        signal_map["extractor"] = max(signal_map.get("extractor", 0.0), cand.confidence)
    return signal_map


def _append_hint(result: ExtractionResult, cand: Candidate, evidence_by_id: dict[str, EvidencePacket]) -> None:
    evidence = evidence_by_id.get(cand.evidence_ids[0]) if cand.evidence_ids else None
    source_ref = evidence.source_ref if evidence else cand.source_ref
    try:
        idx = int(source_ref.block_id)
        span = (idx, idx)
    except (TypeError, ValueError):
        span = (0, 0)
    result.extraction_hints.append(
        ExtractionHint(
            hint_type=cand.frame_type,
            suggested_field=cand.target_field,
            snippet=evidence.snippet if evidence else clean_text(str(cand.normalized_value)),
            confidence=cand.confidence,
            anchor=source_ref.anchor,
            span=span,
            context_heading=" > ".join(source_ref.heading_path) if source_ref.heading_path else None,
            matched_signals=list(cand.signals),
        )
    )


def _next_id(field: str, counters: defaultdict[str, int]) -> str:
    counters[field] += 1
    prefix = PREFIXES.get(field, field[:3].upper())
    return f"{prefix}-{counters[field]:04d}"


def _missing_required(entity: Any) -> list[str]:
    missing = []
    for field in fields(entity):
        if field.default is not _MISSING or field.default_factory is not _MISSING:
            continue
        value = getattr(entity, field.name)
        if value is None or value == "":
            missing.append(field.name)
    return missing


def _extra_attributes(dc: type, value: dict[str, Any]) -> dict[str, Any]:
    valid = {f.name for f in fields(dc)}
    return {k: v for k, v in value.items() if k not in valid}
