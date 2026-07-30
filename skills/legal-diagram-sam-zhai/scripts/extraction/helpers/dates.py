"""Date and deadline helpers: deadline text extraction and deadline-signal detection.

Domain-free utilities shared by deadlines.py, obligations.py, payments.py, and
materialize.py.  Depends on the lexicon package for DATE_RE.
"""
from __future__ import annotations

import re
from typing import Optional

from ..lexicon import DATE_RE


def has_deadline_signal(text: str) -> bool:
    """Return True if *text* contains a date or temporal-deadline keyword."""
    return bool(
        DATE_RE.search(text)
        or re.search(
            r"\b(by|within|before|after|following|prior\s+to|no\s+later\s+than|not\s+later\s+than|on\s+or\s+before|promptly\s+after|as\s+soon\s+as\s+practicable|cure\s+period|written\s+notice)\b",
            text,
            re.I,
        )
    )


def deadline_text(text: str) -> Optional[str]:
    """Extract the first deadline phrase from *text*, or None.

    Preference order: explicit date > relative-day formula > other temporal phrase.
    """
    m = DATE_RE.search(text)
    if m:
        return m.group(0)
    m = re.search(
        r"\b(?:within\s+\d+\s+(?:business\s+)?days?\s+(?:after|of)|prior\s+to\s+Closing|following\s+Closing|promptly\s+after[^.;,]{0,60}|as\s+soon\s+as\s+practicable\s+after[^.;,]{0,60}|\d+\s+(?:business\s+)?days?[']?\s+(?:prior\s+)?written\s+notice)\b",
        text,
        re.I,
    )
    return m.group(0) if m else None
