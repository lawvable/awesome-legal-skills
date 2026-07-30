"""Domain package for legal-diagram extraction entities.

Re-exports every public name from the old domain.py so that all existing
import sites (``from extraction.domain import X``) keep working unchanged.
Internal modules may import from submodules directly.
"""
from .core import (
    CoverageMap,
    Communication,
    Concept,
    Deadline,
    DecisionPoint,
    Document,
    EnrichmentDirective,
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
from .result import ENTITY_FIELDS, ExtractionResult

# Expose submodules so callers can reach extraction.domain.core etc.
from . import compliance, core, corporate, litigation
from . import result

__all__ = [
    # core
    "Communication",
    "Concept",
    "CoverageMap",
    "Deadline",
    "DecisionPoint",
    "Document",
    "EnrichmentDirective",
    "Entity",
    "Event",
    "ExtractionHint",
    "InvestigationStep",
    "IPAsset",
    "NegotiationIssue",
    "Obligation",
    "Party",
    "Phase",
    "ProcessStep",
    "Relationship",
    "RiskItem",
    "State",
    "Task",
    "Transfer",
    "Transition",
    # litigation
    "ClaimClass",
    "LegalAuthority",
    "WitnessMap",
    # corporate
    "ConditionPrecedent",
    "OwnershipLink",
    # compliance
    "Control",
    "DataFlow",
    # result
    "ENTITY_FIELDS",
    "ExtractionResult",
    # submodules
    "compliance",
    "core",
    "corporate",
    "litigation",
    "result",
]
