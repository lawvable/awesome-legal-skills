from __future__ import annotations
import dataclasses
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Any, Dict, Tuple


@dataclass
class Party:
    name: str
    role: str
    type: str


@dataclass
class Entity:
    name: str
    type: str
    jurisdiction: Optional[str] = None
    entity_type: Optional[str] = None
    system_type: Optional[str] = None
    attributes: Dict[str, Any] = field(default_factory=dict)
    anchor: Optional[str] = None


@dataclass
class Event:
    date: str
    description: str
    actor: Optional[str] = None
    anchor: Optional[str] = None


@dataclass
class Deadline:
    date: str
    description: str
    party: str
    consequence: Optional[str] = None


@dataclass
class Phase:
    name: str
    start_date: str
    end_date: str
    dependencies: List[str] = field(default_factory=list)


@dataclass
class Task:
    id: str
    name: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    duration_days: Optional[int] = None
    dependencies: List[str] = field(default_factory=list)
    responsible_party: Optional[str] = None
    is_milestone: bool = False
    section: Optional[str] = None


@dataclass
class Obligation:
    id: str
    description: str
    party: str
    source_law: Optional[str] = None
    risk_level: Optional[str] = None
    verify_method: Optional[str] = None
    status: Optional[str] = None
    deadline: Optional[str] = None


@dataclass
class Control:
    id: str
    description: str
    obligation_id: str
    owner: Optional[str] = None
    evidence_documents: List[str] = field(default_factory=list)
    audit_status: Optional[str] = None
    audit_date: Optional[str] = None


@dataclass
class ConditionPrecedent:
    id: str
    description: str
    responsible_party: Optional[str] = None
    evidence_needed: Optional[str] = None
    satisfied: bool = False
    satisfaction_date: Optional[str] = None


@dataclass
class Relationship:
    from_entity: str
    to_entity: str
    type: str
    description: Optional[str] = None
    cardinality_from: Optional[str] = None
    cardinality_to: Optional[str] = None


@dataclass
class OwnershipLink:
    parent: str
    child: str
    percentage: Optional[float] = None


@dataclass
class State:
    name: str
    description: Optional[str] = None


@dataclass
class Transition:
    from_state: str
    to_state: str
    trigger: Optional[str] = None


@dataclass
class DecisionPoint:
    question: str
    yes_path: str
    no_path: str


@dataclass
class ProcessStep:
    id: str
    name: str
    actor: Optional[str] = None
    condition: Optional[str] = None
    next_steps: List[str] = field(default_factory=list)
    sequence: Optional[int] = None
    step_type: str = "action"
    status: Optional[str] = None


@dataclass
class InvestigationStep:
    id: str
    step_number: int
    description: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    findings: Optional[str] = None
    participants: List[str] = field(default_factory=list)
    responsible_party: Optional[str] = None


@dataclass
class Communication:
    from_party: str
    to_party: str
    date: Optional[str] = None
    comm_type: str = "notice"
    description: str = ""
    delivery_method: Optional[str] = None
    sequence_order: Optional[int] = None


@dataclass
class Concept:
    id: str
    name: str
    concept_type: str = "issue"
    parent_id: Optional[str] = None
    children: List[str] = field(default_factory=list)
    description: Optional[str] = None
    supporting_facts: List[str] = field(default_factory=list)


@dataclass
class RiskItem:
    label: str
    x_score: float
    y_score: float
    description: Optional[str] = None
    x_axis_label: Optional[str] = None
    y_axis_label: Optional[str] = None
    category: Optional[str] = None


@dataclass
class NegotiationIssue:
    id: str
    term: str
    our_position: Optional[str] = None
    counterparty_position: Optional[str] = None
    x_score: Optional[float] = None
    y_score: Optional[float] = None
    fallback: Optional[str] = None
    status: Optional[str] = None


@dataclass
class Transfer:
    from_party: str
    to_party: str
    description: str = ""
    amount: Optional[float] = None
    sequence_order: Optional[int] = None
    mechanism: Optional[str] = None
    triggered_by: Optional[str] = None


@dataclass
class ClaimClass:
    priority_rank: int
    name: str
    claim_amount: Optional[float] = None
    claim_type: Optional[str] = None


@dataclass
class DataFlow:
    from_system: str
    to_system: str
    data_categories: List[str] = field(default_factory=list)
    purpose: Optional[str] = None
    transfer_mechanism: Optional[str] = None
    requires_consent: bool = False


@dataclass
class WitnessMap:
    witness_name: str
    topics: List[str] = field(default_factory=list)
    documents: List[str] = field(default_factory=list)
    target_admissions: List[str] = field(default_factory=list)
    affiliation: Optional[str] = None


@dataclass
class LegalAuthority:
    citation: str
    authority_type: str
    jurisdiction: Optional[str] = None
    hierarchy_level: Optional[int] = None
    cites: List[str] = field(default_factory=list)
    anchor: Optional[str] = None


@dataclass
class IPAsset:
    name: str
    asset_type: str
    identifier: Optional[str] = None
    filing_date: Optional[str] = None
    status: Optional[str] = None
    jurisdictions: List[str] = field(default_factory=list)
    claims: List[str] = field(default_factory=list)


@dataclass
class Document:
    name: str
    type: str
    date: Optional[str] = None
    parties: List[str] = field(default_factory=list)


@dataclass
class ExtractionHint:
    hint_type: str
    suggested_field: str
    snippet: str
    confidence: float
    anchor: str = ""
    span: Tuple[int, int] = field(default_factory=lambda: (0, 0))
    context_heading: Optional[str] = None
    docx_style: Optional[str] = None
    matched_signals: List[str] = field(default_factory=list)


@dataclass
class EnrichmentDirective:
    type: str
    field: str
    instruction: str
    targets: List[str] = dataclasses.field(default_factory=list)
    hint_ids: List[str] = dataclasses.field(default_factory=list)


@dataclass
class CoverageMap:
    populated_fields: List[str] = field(default_factory=list)
    hint_only_fields: List[str] = field(default_factory=list)
    absent_fields: List[str] = field(default_factory=list)
    signal_map: Dict[str, Any] = field(default_factory=dict)


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
