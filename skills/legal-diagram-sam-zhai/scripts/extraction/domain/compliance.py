from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List


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
class DataFlow:
    from_system: str
    to_system: str
    data_categories: List[str] = field(default_factory=list)
    purpose: Optional[str] = None
    transfer_mechanism: Optional[str] = None
    requires_consent: bool = False
