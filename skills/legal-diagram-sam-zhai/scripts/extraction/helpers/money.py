"""Money-related helpers: amount parsing, money text extraction, payment-party extraction.

Domain-free utilities shared by payments.py, tables.py, and materialize.py.
Depends on the lexicon package for MONEY_RE (kept there as the single-pattern home).
"""
from __future__ import annotations

import re
from typing import Optional

from ..lexicon import MONEY_RE


def has_payment_verb(text: str) -> bool:
    """Return True if *text* contains a payment-action verb."""
    return bool(re.search(r"\b(pay|reimburse|fund|deposit|remit|wire|transfer|payable|due\s+and\s+payable)\b", text, re.I))


def money_text(text: str) -> Optional[str]:
    """Extract the first money amount or money-noun phrase from *text*, or None."""
    m = MONEY_RE.search(text)
    if m:
        return m.group(0)
    m = re.search(r"\b(purchase\s+price|fee|expense|escrow\s+amount|holdback)\b", text, re.I)
    return m.group(0) if m else None


def amount_number(text: Optional[str]) -> Optional[float]:
    """Parse the first numeric amount from *text*, stripping commas. Returns None if absent."""
    if not text:
        return None
    m = re.search(r"[\d,]+(?:\.\d{2})?", text)
    return float(m.group(0).replace(",", "")) if m else None


def extract_payment_parties(text: str) -> tuple[str, str]:
    """Return (payer, payee) extracted from a payment sentence.

    Falls back to (extract_subject(text), "") when the explicit payer-payee
    pattern is absent.
    """
    # Import here to avoid a circular dependency: subjects.py also imports
    # nothing from money.py, so this one-way dependency is safe.
    from .subjects import extract_subject, clean_party

    m = re.search(
        r"(?P<payer>[A-Z][A-Za-z .&']+?)\s+(?:shall\s+|must\s+|will\s+|agrees?\s+to\s+)?(?:pay|reimburse|fund|deposit|remit|wire|transfer)\s+.+?\s+to\s+(?P<payee>[A-Z][A-Za-z .&']+?)(?:\s+(?:on|within|at|by|upon|following|after)\b|[.;,]|$)",
        text,
    )
    if not m:
        return extract_subject(text), ""
    return clean_party(m.group("payer")), clean_party(m.group("payee"))
