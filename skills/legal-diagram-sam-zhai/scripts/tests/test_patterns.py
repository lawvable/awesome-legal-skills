"""TDD tests for shared _patterns.py module.

Verifies that _patterns.py exports:
  - CORP_SUFFIX_ALT: str fragment covering all corporate suffix variants
  - CORP_NAME_RE: compiled pattern matching capitalized-run + suffix
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from extraction.harvesters._patterns import CORP_SUFFIX_ALT, CORP_NAME_RE  # noqa: E402


def test_corp_suffix_alt_is_string() -> None:
    assert isinstance(CORP_SUFFIX_ALT, str), "CORP_SUFFIX_ALT must be a plain string"


def test_corp_suffix_alt_covers_en_forms() -> None:
    rx = re.compile(r"\b(?:" + CORP_SUFFIX_ALT + r")\b", re.I)
    for suffix in ("Inc.", "Inc", "LLC", "Ltd.", "Ltd", "Corp.", "Corp",
                   "Corporation", "Company", "LP", "LLP", "PLC", "GmbH"):
        assert rx.search(suffix), f"CORP_SUFFIX_ALT must match EN suffix: {suffix!r}"


def test_corp_suffix_alt_covers_fr_forms() -> None:
    rx = re.compile(r"\b(?:" + CORP_SUFFIX_ALT + r")\b", re.I)
    for suffix in ("Ltée", "S.E.N.C.", "S.E.N.C.R.L.", "s.r.l.", "S.A.R.L.", "S.A.", "S.E.C."):
        assert rx.search(suffix), f"CORP_SUFFIX_ALT must match FR suffix: {suffix!r}"


def test_corp_name_re_is_compiled() -> None:
    assert isinstance(CORP_NAME_RE, type(re.compile(""))), "CORP_NAME_RE must be a compiled Pattern"


def test_corp_name_re_matches_typical_names() -> None:
    for name in (
        "Cedarbrook Group Inc.",
        "Lakeview Distribution Corp.",
        "Maplewood Technologies Ltd.",
        "Technologies Malouin Ltée",
        "Acme LLC",
        "Northgate Acquisitions Corp.",
        "Example Digital Services Inc.",
    ):
        assert CORP_NAME_RE.search(name), f"CORP_NAME_RE must match: {name!r}"


def test_corp_name_re_group1_captures_name() -> None:
    m = CORP_NAME_RE.search("Cedarbrook Group Inc. owns 100% of something")
    assert m is not None, "CORP_NAME_RE must match in context"
    assert "Cedarbrook Group Inc" in m.group(1), (
        f"Group 1 must capture the name, got: {m.group(1)!r}"
    )


if __name__ == "__main__":
    import traceback
    tests = [v for k, v in globals().items() if k.startswith("test_") and callable(v)]
    passed = failed = 0
    for fn in tests:
        try:
            fn()
            print(f"  PASS  {fn.__name__}")
            passed += 1
        except Exception:
            print(f"  FAIL  {fn.__name__}")
            traceback.print_exc()
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
