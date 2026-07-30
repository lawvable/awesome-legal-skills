from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class ClaimClass:
    priority_rank: int
    name: str
    claim_amount: Optional[float] = None
    claim_type: Optional[str] = None


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
