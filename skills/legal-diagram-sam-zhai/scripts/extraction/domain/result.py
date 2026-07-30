from __future__ import annotations
import dataclasses
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Any, Dict

from .core import (
    Communication,
    Concept,
    Deadline,
    DecisionPoint,
    Document,
    Entity,
    Event,
    ExtractionHint,
    InvestigationStep,
    IPAsset,
    NegotiationIssue,
    Obligation,
    Party,
    Phase,
    ProcessStep,
    Relationship,
    RiskItem,
    State,
    Task,
    Transfer,
    Transition,
)
from .litigation import ClaimClass, LegalAuthority, WitnessMap
from .corporate import ConditionPrecedent, OwnershipLink
from .compliance import Control, DataFlow


ENTITY_FIELDS: Dict[str, Any] = {
    "parties": Party,
    "entities": Entity,
    "events": Event,
    "deadlines": Deadline,
    "phases": Phase,
    "tasks": Task,
    "obligations": Obligation,
    "controls": Control,
    "conditions": ConditionPrecedent,
    "relationships": Relationship,
    "ownership_links": OwnershipLink,
    "states": State,
    "transitions": Transition,
    "decision_points": DecisionPoint,
    "process_steps": ProcessStep,
    "investigation_steps": InvestigationStep,
    "communications": Communication,
    "concepts": Concept,
    "risk_items": RiskItem,
    "negotiation_issues": NegotiationIssue,
    "transfers": Transfer,
    "claim_classes": ClaimClass,
    "data_flows": DataFlow,
    "witnesses": WitnessMap,
    "legal_authorities": LegalAuthority,
    "ip_assets": IPAsset,
    "documents": Document,
}

_ENTITY_KEYS = list(ENTITY_FIELDS.keys())


def _build(dc: Any, item: Dict[str, Any]) -> Any:
    valid = {f.name for f in dataclasses.fields(dc)}
    kwargs = {k: v for k, v in item.items() if k in valid}
    if "span" in kwargs and isinstance(kwargs["span"], list):
        kwargs["span"] = tuple(kwargs["span"])
    return dc(**kwargs)


@dataclass
class ExtractionResult:
    matter_name: Optional[str] = None
    matter_type: Optional[str] = None
    input_source: Optional[str] = None
    truncated: bool = False
    extraction_warnings: List[str] = field(default_factory=list)
    signal_map: Dict[str, Any] = field(default_factory=dict)
    hierarchy: List[Dict[str, Any]] = field(default_factory=list)
    extraction_hints: List[ExtractionHint] = field(default_factory=list)
    parties: List[Party] = field(default_factory=list)
    entities: List[Entity] = field(default_factory=list)
    events: List[Event] = field(default_factory=list)
    deadlines: List[Deadline] = field(default_factory=list)
    phases: List[Phase] = field(default_factory=list)
    tasks: List[Task] = field(default_factory=list)
    obligations: List[Obligation] = field(default_factory=list)
    controls: List[Control] = field(default_factory=list)
    conditions: List[ConditionPrecedent] = field(default_factory=list)
    relationships: List[Relationship] = field(default_factory=list)
    ownership_links: List[OwnershipLink] = field(default_factory=list)
    states: List[State] = field(default_factory=list)
    transitions: List[Transition] = field(default_factory=list)
    decision_points: List[DecisionPoint] = field(default_factory=list)
    process_steps: List[ProcessStep] = field(default_factory=list)
    investigation_steps: List[InvestigationStep] = field(default_factory=list)
    communications: List[Communication] = field(default_factory=list)
    concepts: List[Concept] = field(default_factory=list)
    risk_items: List[RiskItem] = field(default_factory=list)
    negotiation_issues: List[NegotiationIssue] = field(default_factory=list)
    transfers: List[Transfer] = field(default_factory=list)
    claim_classes: List[ClaimClass] = field(default_factory=list)
    data_flows: List[DataFlow] = field(default_factory=list)
    witnesses: List[WitnessMap] = field(default_factory=list)
    legal_authorities: List[LegalAuthority] = field(default_factory=list)
    ip_assets: List[IPAsset] = field(default_factory=list)
    documents: List[Document] = field(default_factory=list)

    def is_empty(self) -> bool:
        for key in _ENTITY_KEYS:
            if getattr(self, key):
                return False
        return True

    def has_hints(self) -> bool:
        return bool(self.extraction_hints)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ExtractionResult:
        valid_fields = {f.name for f in dataclasses.fields(cls)}
        result = cls()
        for key, value in data.items():
            if key not in valid_fields:
                continue
            if key == "extraction_hints" and isinstance(value, list):
                setattr(result, key, [_build(ExtractionHint, item) for item in value])
            elif key in ENTITY_FIELDS and isinstance(value, list):
                dc = ENTITY_FIELDS[key]
                setattr(result, key, [_build(dc, item) for item in value])
            else:
                setattr(result, key, value)
        return result
