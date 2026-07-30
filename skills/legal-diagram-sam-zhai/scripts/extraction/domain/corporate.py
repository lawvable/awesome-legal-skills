from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class OwnershipLink:
    parent: str
    child: str
    percentage: Optional[float] = None


@dataclass
class ConditionPrecedent:
    id: str
    description: str
    responsible_party: Optional[str] = None
    evidence_needed: Optional[str] = None
    satisfied: bool = False
    satisfaction_date: Optional[str] = None
