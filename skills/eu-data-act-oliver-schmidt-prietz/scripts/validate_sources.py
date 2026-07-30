#!/usr/bin/env python3
"""
validate_sources.py — heading taxonomy and integrity checks for the EU Data Act skill source layer.

What this script verifies, in order:

1. `sources/_versions.json` parses as valid JSON and contains the expected top-level keys.
2. Every file listed in `_versions.json` with `status: ingested` exists on disk.
3. `sources/regulation-2023-2854.md` contains all 119 recitals (1-119) and all 50 articles (1-50)
   under the expected `## Recital N` and `## Article N` heading patterns.
4. `sources/faq-v1-4.md` contains all 84 expected questions (Q1-Q74 plus 10 letter variants:
   Q5a, Q13a, Q22a, Q25a, Q25b, Q34a, Q42a, Q42b, Q58a, Q58b) under `## FAQ QN` headings.
5. `sources/digital-omnibus-amendments-tracker.md` exists.
6. `sources/mcts-sccs-recommendation-pointer.md` and `sources/vehicle-data-guidance-pointer.md` exist.
7. SHA256 checksums in `sources/_manifest.sha256` match the current file contents.

The script exits with code 0 if all checks pass and a non-zero code on the first failure.
Output is human-readable and uses ASCII status markers so it works in any terminal.

Usage:
    python3 scripts/validate_sources.py
    python3 scripts/validate_sources.py --verbose   # also prints OK lines, not just FAIL lines

This script is run before any release of the skill and as part of CI in Phase 9.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

EXPECTED_FAQ_QUESTIONS: set[str] = (
    {f"Q{i}" for i in range(1, 75)}
    | {"Q5a", "Q13a", "Q22a", "Q25a", "Q25b", "Q34a", "Q42a", "Q42b", "Q58a", "Q58b"}
)
EXPECTED_RECITAL_RANGE = range(1, 120)   # 1..119 inclusive
EXPECTED_ARTICLE_RANGE = range(1, 51)    # 1..50 inclusive

# Paths are computed relative to the script's parent directory so the script
# can be run from any working directory.
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent
SOURCES_DIR = SKILL_ROOT / "sources"

REGULATION_FILE = SOURCES_DIR / "regulation-2023-2854.md"
FAQ_FILE = SOURCES_DIR / "faq-v1-4.md"
OMNIBUS_FILE = SOURCES_DIR / "digital-omnibus-amendments-tracker.md"
MCTS_POINTER = SOURCES_DIR / "mcts-sccs-recommendation-pointer.md"
VEHICLE_POINTER = SOURCES_DIR / "vehicle-data-guidance-pointer.md"
VERSIONS_JSON = SOURCES_DIR / "_versions.json"
MANIFEST_FILE = SOURCES_DIR / "_manifest.sha256"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


class CheckResult:
    """A single check's outcome. Aggregated by Validator for the final report."""

    def __init__(self, name: str, passed: bool, detail: str = "") -> None:
        self.name = name
        self.passed = passed
        self.detail = detail

    def __str__(self) -> str:
        marker = "[OK]  " if self.passed else "[FAIL]"
        return f"{marker} {self.name}" + (f": {self.detail}" if self.detail else "")


class Validator:
    """Runs checks and tracks results. Exits non-zero if any check failed."""

    def __init__(self, verbose: bool = False) -> None:
        self.results: list[CheckResult] = []
        self.verbose = verbose

    def add(self, name: str, passed: bool, detail: str = "") -> None:
        result = CheckResult(name, passed, detail)
        self.results.append(result)
        if self.verbose or not passed:
            print(result)

    def report(self) -> int:
        passed = sum(1 for r in self.results if r.passed)
        total = len(self.results)
        failed = total - passed
        print()
        print(f"Summary: {passed}/{total} checks passed, {failed} failed.")
        return 0 if failed == 0 else 1


def sha256_of(path: Path) -> str:
    """Compute SHA256 of a file's contents, returned as a lowercase hex string."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------


def check_versions_json(v: Validator) -> dict | None:
    """Parse _versions.json and verify top-level structure. Returns parsed dict on success."""
    if not VERSIONS_JSON.exists():
        v.add("versions.json exists", False, f"{VERSIONS_JSON} not found")
        return None
    try:
        data = json.loads(VERSIONS_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        v.add("versions.json parses", False, f"JSON decode error: {e}")
        return None
    v.add("versions.json parses", True)

    if "sources" not in data or not isinstance(data["sources"], dict):
        v.add("versions.json has sources object", False)
        return None
    v.add("versions.json has sources object", True)
    return data


def check_ingested_files_exist(v: Validator, versions: dict) -> None:
    """For every source with status=ingested, verify the referenced file exists."""
    for key, entry in versions.get("sources", {}).items():
        if not isinstance(entry, dict):
            continue
        status = entry.get("status")
        file_name = entry.get("file")
        if status == "ingested" and file_name:
            path = SOURCES_DIR / file_name
            v.add(
                f"ingested file present: {file_name}",
                path.exists(),
                "" if path.exists() else f"{path} missing",
            )


def check_regulation_headings(v: Validator) -> None:
    if not REGULATION_FILE.exists():
        v.add("regulation file exists", False, f"{REGULATION_FILE} not found")
        return
    v.add("regulation file exists", True)

    text = REGULATION_FILE.read_text(encoding="utf-8")

    # Recitals
    recital_re = re.compile(r"^## Recital (\d+)$", re.MULTILINE)
    found = [int(m.group(1)) for m in recital_re.finditer(text)]
    missing = sorted(set(EXPECTED_RECITAL_RANGE) - set(found))
    duplicates = sorted({n for n in found if found.count(n) > 1})
    v.add(
        "regulation: all 119 recitals present",
        not missing and not duplicates,
        f"missing={missing}, duplicates={duplicates}" if (missing or duplicates) else "",
    )

    # Articles
    article_re = re.compile(r"^## Article (\d+)$", re.MULTILINE)
    found = [int(m.group(1)) for m in article_re.finditer(text)]
    missing = sorted(set(EXPECTED_ARTICLE_RANGE) - set(found))
    duplicates = sorted({n for n in found if found.count(n) > 1})
    v.add(
        "regulation: all 50 articles present",
        not missing and not duplicates,
        f"missing={missing}, duplicates={duplicates}" if (missing or duplicates) else "",
    )

    # Chapters (sanity: 11 chapter headings expected, I-XI)
    chapter_re = re.compile(r"^## Chapter ([IVX]+)", re.MULTILINE)
    chapters = [m.group(1) for m in chapter_re.finditer(text)]
    expected_chapters = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]
    v.add(
        "regulation: all 11 chapters present in order",
        chapters == expected_chapters,
        f"found={chapters}" if chapters != expected_chapters else "",
    )


def check_faq_questions(v: Validator) -> None:
    if not FAQ_FILE.exists():
        v.add("FAQ file exists", False, f"{FAQ_FILE} not found")
        return
    v.add("FAQ file exists", True)

    text = FAQ_FILE.read_text(encoding="utf-8")
    q_re = re.compile(r"^## FAQ (Q\d+[ab]?)$", re.MULTILINE)
    found = [m.group(1) for m in q_re.finditer(text)]
    missing = sorted(EXPECTED_FAQ_QUESTIONS - set(found))
    extra = sorted(set(found) - EXPECTED_FAQ_QUESTIONS)
    duplicates = sorted({q for q in found if found.count(q) > 1})
    ok = not missing and not extra and not duplicates
    detail_parts = []
    if missing:
        detail_parts.append(f"missing={missing}")
    if extra:
        detail_parts.append(f"extra={extra}")
    if duplicates:
        detail_parts.append(f"duplicates={duplicates}")
    v.add("FAQ: all 84 questions present (Q1-Q74 plus 10 letter variants)", ok, ", ".join(detail_parts))


def check_supporting_files(v: Validator) -> None:
    for label, path in [
        ("Digital Omnibus tracker", OMNIBUS_FILE),
        ("MCTs/SCCs pointer", MCTS_POINTER),
        ("Vehicle Data Guidance pointer", VEHICLE_POINTER),
    ]:
        v.add(
            f"{label} file present",
            path.exists(),
            "" if path.exists() else f"{path} missing",
        )


def check_manifest(v: Validator) -> None:
    """Verify SHA256 sums in _manifest.sha256 match current file contents."""
    if not MANIFEST_FILE.exists():
        v.add("manifest file exists", False, f"{MANIFEST_FILE} not found")
        return
    v.add("manifest file exists", True)

    # Parse `sha256sum`-style format: "<hash>  <relative_path>"
    entries: list[tuple[str, str]] = []
    for line in MANIFEST_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        if len(parts) != 2:
            v.add("manifest line malformed", False, f"line: {line!r}")
            continue
        entries.append((parts[0].lower(), parts[1]))

    if not entries:
        v.add("manifest has at least one entry", False)
        return
    v.add("manifest has at least one entry", True)

    # Manifest paths are relative to the skill root (e.g. "sources/regulation-2023-2854.md").
    for expected_hash, rel_path in entries:
        path = SKILL_ROOT / rel_path
        if not path.exists():
            v.add(f"manifest entry file exists: {rel_path}", False, f"{path} missing")
            continue
        actual = sha256_of(path)
        v.add(
            f"manifest checksum matches: {rel_path}",
            actual == expected_hash,
            f"expected={expected_hash}, actual={actual}" if actual != expected_hash else "",
        )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--verbose", "-v", action="store_true", help="print OK lines too")
    args = parser.parse_args(argv)

    v = Validator(verbose=args.verbose)

    versions = check_versions_json(v)
    if versions is not None:
        check_ingested_files_exist(v, versions)
    check_regulation_headings(v)
    check_faq_questions(v)
    check_supporting_files(v)
    check_manifest(v)

    return v.report()


if __name__ == "__main__":
    sys.exit(main())
