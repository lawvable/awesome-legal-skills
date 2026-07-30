"""extraction.lexicon package: language-bearing pattern bundles.

Public API
----------
get_bundle(lang: str) -> LexiconBundle
    Return the bundle for the requested language.  Unknown language codes fall
    back to EN (W3 contract: get_bundle("xx") is get_bundle("en")).

LexiconBundle
    Frozen dataclass; all language-bearing regex patterns for one locale.

All names that were previously exported by extraction/lexicon.py are re-exported
here so that existing ``from ..lexicon import NAME`` calls in harvesters and
utils continue to work unchanged during the W2.x migration.  W2.2 threads the
bundle through a context object; once all call sites are updated this
compatibility shim can be removed.
"""
from __future__ import annotations

import re as _re

from .base import LexiconBundle
from .en import _EN_BUNDLE
from .fr import _FR_BUNDLE


def get_bundle(lang: str) -> LexiconBundle:
    """Return the LexiconBundle for *lang*, falling back to EN for unknown codes."""
    _lang = (lang or "").strip().lower()
    if _lang == "en":
        return _EN_BUNDLE
    if _lang == "fr":
        return _FR_BUNDLE
    # All other codes fall back to EN per contract.
    return _EN_BUNDLE


# ---------------------------------------------------------------------------
# Backward-compatibility re-exports from the old extraction/lexicon.py module.
# Harvesters and utils currently import these names directly; they stay valid
# until W2.2 finishes threading the bundle through the context object.
# ---------------------------------------------------------------------------

# Re-export the EN bundle's compiled patterns under their original module-level
# names so that the existing ``from ..lexicon import NAME`` import style still
# resolves.

# These were top-level constants in the old lexicon.py:
from .en import (
    _DATE_RE as DATE_RE,
    _LEGAL_ACTION_VERBS as LEGAL_ACTION_VERBS,
    _MONEY_RE as MONEY_RE,
)

# These were also top-level in the old lexicon.py (promote thresholds, role
# words, anti-signals, header synonyms, heading priors):
PROMOTE_AUTO = 0.85
PROMOTE_WITH_CORROBORATION = 0.65
HINT_MIN = 0.45

from .en import _SENTENCE_SPLIT as SENTENCE_SPLIT  # noqa: F401 -- re-exported compat name
SPACE_RE = _re.compile(r"\s+")

KNOWN_ROLE_WORDS = {
    "buyer", "seller", "borrower", "lender", "issuer", "company", "parent", "subsidiary", "affiliate",
    "agent", "trustee", "representative", "obligor", "guarantor", "tenant", "landlord", "licensor", "licensee",
    # Litigation roles
    "appellant", "respondent", "plaintiff", "defendant", "applicant", "petitioner",
    "intervener", "moving party", "responding party", "crown",
}

ANTI_SIGNAL_PATTERNS = [
    ("including_example", _re.compile(r"\bincluding(?:\s+without\s+limitation)?\b|\bfor example\b|\be\.g\.\b", _re.I)),
    ("descriptive_may", _re.compile(r"\bmay\s+(?:include|contain|consist)\b", _re.I)),
    ("generic_affiliate", _re.compile(r"^\s*affiliates?\s*$", _re.I)),
    ("generic_qualifier", _re.compile(r"^\s*(?:material|reasonable)\s*$", _re.I)),
]

HEADER_SYNONYMS = {
    "party": {"party", "entity", "obligor", "borrower", "seller", "buyer", "responsible party", "owner"},
    "obligation": {"obligation", "action", "requirement", "covenant", "task", "deliverable"},
    "deadline": {"due date", "deadline", "timing", "when due", "delivery date", "date"},
    "status": {"status", "open/closed", "completed", "pending", "resolved"},
    "risk": {"risk", "issue", "concern", "exception", "finding"},
    "control": {"control", "approver", "reviewer", "sign-off", "signoff", "verification"},
    "document": {"document", "agreement", "certificate", "notice", "filing", "schedule", "exhibit"},
    "amount": {"amount", "price", "payment", "fee", "expense", "escrow", "holdback"},
}

# FR twins of HEADER_SYNONYMS (W3.3).  Table rows are synthetic blocks that
# carry no block.lang, so classify_headers (utils.py) consults the EN table
# first and falls back to this FR table; the two live side by side here.
HEADER_SYNONYMS_FR = {
    "party": {"partie", "entité", "débiteur", "emprunteur", "vendeur", "acheteur", "partie responsable", "propriétaire"},
    "obligation": {"obligation", "exigence", "engagement", "tâche", "livrable"},
    "deadline": {"échéance", "date limite", "délai", "date d'échéance", "date de livraison", "date"},
    "status": {"statut", "état", "terminé", "en cours", "résolu"},
    "risk": {"risque", "enjeu", "préoccupation", "exception", "constat"},
    "control": {"contrôle", "approbateur", "réviseur", "vérification", "signature"},
    "document": {"document", "convention", "entente", "certificat", "avis", "annexe", "pièce"},
    "amount": {"montant", "prix", "paiement", "frais", "dépense", "entiercement", "retenue"},
}

HEADING_PRIORS = {
    "obligations": _re.compile(r"obligations?|covenants?|deliver(?:y|ies)|notices?|reporting|closing", _re.I),
    "conditions": _re.compile(r"conditions?|closing|precedent|dependency|deliver(?:y|ies)", _re.I),
    "deadlines": _re.compile(r"deadlines?|timeline|schedule|closing|notices?|cure", _re.I),
    "documents": _re.compile(r"documents?|deliver(?:y|ies)|certificates?|filings?|records?|schedules?|exhibits?", _re.I),
    "transfers": _re.compile(r"payment|funds?|waterfall|purchase price|escrow|holdback|expense", _re.I),
    "communications": _re.compile(r"notices?|communications?|delivery method", _re.I),
    "controls": _re.compile(r"controls?|audit|evidence|verified|review|approv|sign-?off|compliance", _re.I),
    "relationships": _re.compile(r"ownership|control|authority|governance|affiliate|assignment", _re.I),
}

__all__ = [
    "LexiconBundle",
    "get_bundle",
    # Backward-compatible names:
    "DATE_RE",
    "LEGAL_ACTION_VERBS",
    "MONEY_RE",
    "PROMOTE_AUTO",
    "PROMOTE_WITH_CORROBORATION",
    "HINT_MIN",
    "SENTENCE_SPLIT",
    "SPACE_RE",
    "KNOWN_ROLE_WORDS",
    "ANTI_SIGNAL_PATTERNS",
    "HEADER_SYNONYMS",
    "HEADER_SYNONYMS_FR",
    "HEADING_PRIORS",
]
