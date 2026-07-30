"""Shared regex fragments for harvesters.

Central source of truth for corporate-suffix patterns used across all
harvester modules.  Import these constants; do not re-define the alternation
locally.

Exports
-------
CORP_SUFFIX_ALT : str
    Regex alternation fragment (no surrounding group) for all recognised
    corporate suffixes -- EN (Inc., LLC, Ltd., Corp., Company, LP, LLP,
    PLC, GmbH) and FR (Ltée, S.E.N.C., S.E.N.C.R.L., s.r.l., S.A.R.L.,
    S.A., S.E.C.).  Suitable for embedding inside a larger pattern via
    f-string interpolation or string concatenation.

CORP_NAME_RE : re.Pattern[str]
    Compiled pattern matching a typical corporate name: one or more
    capitalised/mixed-case word tokens followed by a recognised suffix.
    Group 1 captures the full name including suffix.  Case-insensitive.
"""
from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# Superset suffix alternation (EN + FR forms).
#
# Ordering rationale:
#   - Multi-character abbreviations first so the regex engine does not
#     short-circuit on a prefix alternative (e.g. "S.A." vs "S.A.R.L.").
#   - FR dotted forms placed after their EN cousins for readability.
# ---------------------------------------------------------------------------
CORP_SUFFIX_ALT: str = (
    r"Inc\.?"
    r"|LLC"
    r"|Ltd\.?"
    r"|Ltée\.?"
    r"|Corp(?:oration)?\.?"
    r"|Company"
    r"|LLP"
    r"|LP"
    r"|PLC"
    r"|GmbH"
    r"|S\.E\.N\.C\.?(?:R\.L\.?)?"
    r"|S\.A\.R\.L\.?"
    r"|s\.r\.l\.?"
    r"|S\.A\.?"
    r"|S\.E\.C\.?"
)

# ---------------------------------------------------------------------------
# Compiled corporate-name pattern.
#
# Matches: 1 to 6 capitalised/mixed-case word tokens (with common
# name characters) followed by a recognised suffix.  Group 1 captures
# the full name including the suffix.  The leading negative look-behind
# prevents matching mid-word.
# ---------------------------------------------------------------------------
CORP_NAME_RE: re.Pattern[str] = re.compile(
    r"(?<!\w)"
    r"([A-Z][A-Za-zÀ-ÿ0-9.&'-]*"
    r"(?:\s+[A-Z][A-Za-zÀ-ÿ0-9.&'-]*){0,5}"
    r"\s+(?:" + CORP_SUFFIX_ALT + r"))"
    r"(?!\s+\w)",
    re.I,
)
