"""extraction.helpers: domain-free utilities shared across harvesters.

Sub-modules
-----------
money.py    -- amount parsing, money text, payment-party extraction
dates.py    -- deadline text extraction, deadline-signal detection
subjects.py -- subject extraction, entity-name cleaning
scoring.py  -- confidence scoring, boost weights, anti-signal penalty

All public names from the four sub-modules are re-exported here so callers
can use ``from extraction.helpers import money_text`` directly.
"""
from __future__ import annotations

from .money import (
    amount_number,
    extract_payment_parties,
    has_payment_verb,
    money_text,
)
from .dates import (
    deadline_text,
    has_deadline_signal,
)
from .subjects import (
    clean_entity,
    clean_party,
    extract_entity_like_names,
    extract_subject,
)
from .scoring import (
    anti_penalty,
    score_boost,
    score_confidence,
)

__all__ = [
    # money
    "amount_number",
    "extract_payment_parties",
    "has_payment_verb",
    "money_text",
    # dates
    "deadline_text",
    "has_deadline_signal",
    # subjects
    "clean_entity",
    "clean_party",
    "extract_entity_like_names",
    "extract_subject",
    # scoring
    "anti_penalty",
    "score_boost",
    "score_confidence",
]
