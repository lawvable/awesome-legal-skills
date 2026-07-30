from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

SCHEMA_VERSION = "legal-diagram-candidates"


@dataclass
class SourceRef:
    source: str = ""
    block_id: str = ""
    anchor: str = ""
    page: Optional[int] = None
    slide: Optional[int] = None
    sheet: Optional[str] = None
    heading_path: list[str] = field(default_factory=list)
    table_coords: Optional[tuple[int, int]] = None
    char_span: Optional[tuple[int, int]] = None


@dataclass
class EvidencePacket:
    id: str
    snippet: str
    source_ref: SourceRef
    heading_path: list[str] = field(default_factory=list)
    candidate_fields: list[str] = field(default_factory=list)
    confidence: float = 0.0
    neighboring_context_ids: list[str] = field(default_factory=list)


@dataclass
class Candidate:
    id: str
    target_field: str
    frame_type: str
    normalized_value: dict[str, Any]
    signals: list[str] = field(default_factory=list)
    anti_signals: list[str] = field(default_factory=list)
    confidence: float = 0.0
    evidence_ids: list[str] = field(default_factory=list)
    source_ref: SourceRef = field(default_factory=SourceRef)


@dataclass
class PromotionDecision:
    candidate_id: str
    action: str
    reason: str
    final_entity_id: Optional[str] = None


@dataclass
class CandidateManifest:
    schema_version: str
    structure_metrics: dict[str, int] = field(default_factory=dict)
    warning_codes: list[str] = field(default_factory=list)
    evidence_packets: list[EvidencePacket] = field(default_factory=list)
    candidates: list[Candidate] = field(default_factory=list)
    promotion_decisions: list[PromotionDecision] = field(default_factory=list)
