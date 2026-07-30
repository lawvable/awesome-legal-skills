from __future__ import annotations

import re

PROMOTE_AUTO = 0.85
PROMOTE_WITH_CORROBORATION = 0.65
HINT_MIN = 0.45

SENTENCE_SPLIT = re.compile(r"(?<=[.;!?])\s+")
SPACE_RE = re.compile(r"\s+")
MONEY_RE = re.compile(r"\$\s?[\d,]+(?:\.\d{2})?|\bUSD\s?[\d,]+(?:\.\d{2})?\b", re.I)
DATE_RE = re.compile(
    r"\b(?:\d{4}-\d{2}-\d{2}|"
    r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t)?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4}|"
    r"\d{1,2}\s+(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t)?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4})\b",
    re.I,
)

LEGAL_ACTION_VERBS = re.compile(
    r"\b(deliver|provide|furnish|make available|submit|file|send|notify|pay|reimburse|fund|deposit|remit|wire|transfer|"
    r"maintain|keep|preserve|retain|obtain|perform|comply|execute|cause|procure|ensure|approve|consent|waive|terminate|cure|remedy)\b",
    re.I,
)

KNOWN_ROLE_WORDS = {
    "buyer", "seller", "borrower", "lender", "issuer", "company", "parent", "subsidiary", "affiliate",
    "agent", "trustee", "representative", "obligor", "guarantor", "tenant", "landlord", "licensor", "licensee",
    # Litigation roles
    "appellant", "respondent", "plaintiff", "defendant", "applicant", "petitioner",
    "intervener", "moving party", "responding party", "crown",
}

ANTI_SIGNAL_PATTERNS = [
    ("including_example", re.compile(r"\bincluding(?:\s+without\s+limitation)?\b|\bfor example\b|\be\.g\.\b", re.I)),
    ("descriptive_may", re.compile(r"\bmay\s+(?:include|contain|consist)\b", re.I)),
    ("generic_affiliate", re.compile(r"^\s*affiliates?\s*$", re.I)),
    ("generic_qualifier", re.compile(r"^\s*(?:material|reasonable)\s*$", re.I)),
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

HEADING_PRIORS = {
    "obligations": re.compile(r"obligations?|covenants?|deliver(?:y|ies)|notices?|reporting|closing", re.I),
    "conditions": re.compile(r"conditions?|closing|precedent|dependency|deliver(?:y|ies)", re.I),
    "deadlines": re.compile(r"deadlines?|timeline|schedule|closing|notices?|cure", re.I),
    "documents": re.compile(r"documents?|deliver(?:y|ies)|certificates?|filings?|records?|schedules?|exhibits?", re.I),
    "transfers": re.compile(r"payment|funds?|waterfall|purchase price|escrow|holdback|expense", re.I),
    "communications": re.compile(r"notices?|communications?|delivery method", re.I),
    "controls": re.compile(r"controls?|audit|evidence|verified|review|approv|sign-?off|compliance", re.I),
    "relationships": re.compile(r"ownership|control|authority|governance|affiliate|assignment", re.I),
}
