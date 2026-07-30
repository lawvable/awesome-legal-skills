from __future__ import annotations
import dataclasses
from dataclasses import dataclass, field
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
class Relationship:
    from_entity: str
    to_entity: str
    type: str
    description: Optional[str] = None
    cardinality_from: Optional[str] = None
    cardinality_to: Optional[str] = None


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


# Transfer lives here (not litigation.py beside ClaimClass, its schema-doc
# Financial pair) because payment transfers appear across deal, employment,
# and compliance matters; only claim waterfalls are litigation-specific.
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
class Document:
    name: str
    type: str
    date: Optional[str] = None
    parties: List[str] = field(default_factory=list)


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
