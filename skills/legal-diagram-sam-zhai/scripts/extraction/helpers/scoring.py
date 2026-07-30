"""Scoring helpers: confidence calculation, boost weights, and anti-signal penalty.

Extraction-domain logic shared across all harvesters; placed in helpers/ by
spec deliberate choice (extraction-domain but cross-harvester).
"""
from __future__ import annotations


def score_boost(signals: list[str]) -> float:
    """Return the total additive boost for *signals* (duplicates counted once)."""
    weights = {
        "table_row_binding": 0.18,
        "known_party_subject": 0.08,
        "legal_action_object": 0.07,
        "deadline_signal": 0.06,
        "heading_prior": 0.05,
        "alias_match": 0.08,
        "defined_term": 0.10,
        "sender_signal": 0.04,
        "recipient_signal": 0.05,
        "payment_signal": 0.06,
        "delivery_method_signal": 0.04,
    }
    return sum(weights.get(signal, 0.0) for signal in set(signals))


def anti_penalty(anti: list[str]) -> float:
    """Return the total penalty for *anti* signals (capped at 0.28)."""
    return min(0.28, 0.07 * len(set(anti)))


def score_confidence(base: float, signals: list[str], anti: list[str]) -> float:
    """Compute final confidence: base + boost - penalty."""
    return base + score_boost(signals) - anti_penalty(anti)
