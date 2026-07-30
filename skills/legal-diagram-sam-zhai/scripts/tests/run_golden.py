"""Golden snapshot runner for legal-diagram.

Usage (from skill root):
    python scripts/tests/run_golden.py               # compare mode; exit 0 = all match
    python scripts/tests/run_golden.py --update-golden  # write mode; regenerates all snapshots

Design constraints:
  - stdlib only; no pytest fixtures; standalone-runnable from skill root.
  - Two strictly separate code paths: compare never writes; update never compares-then-silently-passes.
  - Fixture discovery via glob so W3's FR fixtures join automatically; set never hardcoded.

Serialisation rules:
  MANIFEST snapshots:
    Raw bytes of extract_entities.py stdout (UTF-8, verbatim as emitted, including its own
    formatting and trailing newline as-is).  Zero parsing or re-serialisation on this path.
    Parsing is still done to feed the manifest dict to the selector step, but the bytes
    captured from stdout are stored/compared directly.

  SELECTOR snapshots:
    Runner-built wrapper: {"no_intent": ..., "with_intent": {"intent": ..., "result": ...}}
    Serialised with json.dumps(wrapper, ensure_ascii=False, indent=2) + "\\n", WITHOUT sort_keys.
    Insertion order is: no_intent, then with_intent with intent before result.
    Inner result objects are passed through json.loads() of the selector CLI stdout, so their
    key order follows Python dict insertion from the parsed JSON (deterministic for fixed CLI).
"""
from __future__ import annotations

import difflib
import json
import os
import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Paths (all relative to skill root; runner must be invoked from skill root)
# ---------------------------------------------------------------------------

_HERE = Path(__file__).resolve()
_SKILL_ROOT = _HERE.parents[2]          # scripts/tests/run_golden.py -> skill root
_FIXTURES_DIR = _HERE.parent / "fixtures"
_GOLDEN_DIR = _HERE.parent / "golden"
_EXTRACT_SCRIPT = _SKILL_ROOT / "scripts" / "extract_entities.py"
_SELECTOR_SCRIPT = _SKILL_ROOT / "scripts" / "diagram_selector.py"

# Maximum diff lines to print per mismatching fixture before truncating.
_DIFF_MAX_LINES = 40


# ---------------------------------------------------------------------------
# Per-fixture matter_type mapping (data, not branching).
# Keys are fixture stems (without .md); values must be accepted by --matter_type.
# Valid values mirror MATTER_BOOSTS keys in diagram_selector.py:
#   litigation, corporate, compliance, employment, ip, bankruptcy, tax,
#   privacy, real_estate, arbitration, deal, tech
# Fixtures not listed here receive no --matter_type flag (CLI default applies).
# ---------------------------------------------------------------------------

FIXTURE_MATTER_TYPE: dict[str, str] = {
    "en_judgment":            "litigation",    # court judgment with parties and events
    "en_spa_contract":        "deal",          # share purchase agreement: deal phases/deadlines
    "en_employment":          "employment",    # employment agreement: compliance/obligations
    "en_corp_structure":      "corporate",     # corporate org chart: entities and ownership
    "en_obligation_schedule": "compliance",    # multi-obligation schedule: compliance checklist
    "en_privacy_policy":      "privacy",       # privacy policy: data flows and controls
    "fr_contract":            "deal",          # FR share-purchase contract: parties/deadlines/payments
    "fr_judgment":            "litigation",    # FR civil judgment: events and citations
    "bilingual_contract":     "deal",          # clause-paired EN/FR licence and distribution contract
}


# ---------------------------------------------------------------------------
# Serialisation helper (selector path only)
# ---------------------------------------------------------------------------

def _serialise_selector(wrapper: dict) -> str:
    """Serialise a selector wrapper dict to a canonical string.

    Insertion order: no_intent, then with_intent (intent before result).
    json.dumps without sort_keys so insertion order is preserved verbatim.
    Inner result objects pass through json.loads of selector CLI stdout, so their
    key order follows Python dict insertion from the parsed JSON (deterministic
    for a fixed CLI output).
    ensure_ascii=False preserves non-ASCII characters (e.g. French fixtures).
    Trailing newline matches standard POSIX text-file convention.
    """
    return json.dumps(wrapper, ensure_ascii=False, indent=2) + "\n"


# ---------------------------------------------------------------------------
# Extraction and selector invocation
# ---------------------------------------------------------------------------

def _run_extraction(fixture: Path, matter_type: str | None) -> tuple[bytes, dict]:
    """Run extract_entities.py on fixture; return (raw_stdout_bytes, parsed_dict).

    raw_stdout_bytes is the verbatim UTF-8 bytes of stdout as emitted by the CLI,
    including its own key ordering and trailing newline.  It is used directly for
    manifest snapshot storage and comparison (zero re-serialisation).

    parsed_dict is json.loads of the same bytes and is used only to feed the
    selector step.

    The relative path from skill root keeps input_source free of absolute path
    leaks.  Subprocess timeout: 60 s per fixture.
    """
    # Relative path from skill root so no absolute path leaks into the snapshot.
    relative_input = fixture.relative_to(_SKILL_ROOT)
    cmd = [sys.executable, str(_EXTRACT_SCRIPT), "--input", str(relative_input)]
    if matter_type:
        cmd += ["--matter_type", matter_type]

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    try:
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            cmd,
            capture_output=True,
            env=env,
            timeout=60,
            cwd=str(_SKILL_ROOT),
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(
            f"Extraction timed out for {fixture.name} after 60 seconds"
        )
    if proc.returncode != 0:
        raise RuntimeError(
            f"Extraction failed for {fixture.name}:\n{proc.stderr.decode('utf-8', errors='replace')}"
        )
    raw_bytes = proc.stdout
    parsed = json.loads(raw_bytes.decode("utf-8"))
    return raw_bytes, parsed


def _run_selector(manifest: dict, intent: str, fixture_name: str) -> dict:
    """Invoke diagram_selector.recommend via subprocess.

    Using subprocess (not direct import) mirrors the actual skill workflow
    invocation path and avoids any module-state pollution between fixtures.
    """
    payload = {
        "extraction_result": manifest["extraction_result"],
        "intent": intent,
    }
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    try:
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, str(_SELECTOR_SCRIPT), "--extraction-json", json.dumps(payload)],
            capture_output=True,
            text=True,
            env=env,
            timeout=30,
            cwd=str(_SKILL_ROOT),
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(
            f"Selector timed out for {fixture_name} after 30 seconds"
        )
    if proc.returncode != 0:
        raise RuntimeError(
            f"Selector failed for {fixture_name}:\n{proc.stderr}"
        )
    return json.loads(proc.stdout)


# ---------------------------------------------------------------------------
# Fixture discovery and snapshot path helpers
# ---------------------------------------------------------------------------

def _discover_fixtures() -> list[Path]:
    """Return sorted list of .md fixtures from the fixtures directory.

    Sorted order is stable across runs and OS platforms; new fixtures (e.g. W3 FR)
    join automatically without any change to this file.
    """
    return sorted(_FIXTURES_DIR.glob("*.md"))


def _labels_path(fixture: Path) -> Path:
    return fixture.parent / (fixture.name + ".labels.json")


def _manifest_golden_path(fixture: Path) -> Path:
    return _GOLDEN_DIR / (fixture.stem + ".manifest.json")


def _selector_golden_path(fixture: Path) -> Path:
    return _GOLDEN_DIR / (fixture.stem + ".selector.json")


def _load_intent(fixture: Path) -> str:
    """Read the intent string from the fixture's labels file.

    The labels file is the single source of truth for the with_intent selector
    golden; the intent is never duplicated in run_golden.py itself.
    """
    labels_file = _labels_path(fixture)
    if not labels_file.exists():
        return "general"
    try:
        data = json.loads(labels_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"WARNING: malformed JSON in {labels_file}; falling back to intent='general'")
        return "general"
    return data.get("expected_type_with_intent", {}).get("intent", "general")


# ---------------------------------------------------------------------------
# Update mode (--update-golden): write snapshots, never compare
# ---------------------------------------------------------------------------

def update_golden() -> int:
    """Regenerate all snapshot files and report what changed.

    Never performs a comparison; the git diff is the review artefact.
    Returns 0 always (update is not a pass/fail operation).
    """
    _GOLDEN_DIR.mkdir(exist_ok=True)
    fixtures = _discover_fixtures()

    if not fixtures:
        print("No fixtures found; nothing to update.")
        return 0

    changed: list[str] = []
    written: list[str] = []

    for fixture in fixtures:
        stem = fixture.stem
        matter_type = FIXTURE_MATTER_TYPE.get(stem)
        intent = _load_intent(fixture)

        # --- manifest snapshot (verbatim CLI bytes) ---
        raw_manifest_bytes, manifest_dict = _run_extraction(fixture, matter_type)
        manifest_path = _manifest_golden_path(fixture)

        prev_manifest_bytes = manifest_path.read_bytes() if manifest_path.exists() else None
        manifest_path.write_bytes(raw_manifest_bytes)
        if prev_manifest_bytes is None:
            written.append(manifest_path.name)
        elif prev_manifest_bytes != raw_manifest_bytes:
            changed.append(manifest_path.name)

        # --- selector snapshot ---
        no_intent_result = _run_selector(manifest_dict, "general", fixture.stem)
        with_intent_result = _run_selector(manifest_dict, intent, fixture.stem)

        # Wrapper insertion order: no_intent first, then with_intent with intent before result.
        selector_wrapper = {
            "no_intent": no_intent_result,
            "with_intent": {
                "intent": intent,
                "result": with_intent_result,
            },
        }
        selector_bytes = _serialise_selector(selector_wrapper).encode("utf-8")
        selector_path = _selector_golden_path(fixture)

        prev_selector_bytes = selector_path.read_bytes() if selector_path.exists() else None
        selector_path.write_bytes(selector_bytes)
        if prev_selector_bytes is None:
            written.append(selector_path.name)
        elif prev_selector_bytes != selector_bytes:
            changed.append(selector_path.name)

    total = len(fixtures)
    snapshot_count = total * 2

    print(f"Updated {snapshot_count} snapshots ({total} fixtures x 2).")
    if written:
        print(f"  New:     {', '.join(written)}")
    if changed:
        print(f"  Changed: {', '.join(changed)}")
    if not written and not changed:
        print("  No changes (all snapshots already current).")

    return 0


# ---------------------------------------------------------------------------
# Compare mode (default): byte-for-byte comparison, never writes
# ---------------------------------------------------------------------------

def compare_golden() -> int:
    """Compare current extraction output against frozen snapshots.

    Exit 0 = all fixtures match.  Non-zero = one or more mismatches; prints a
    per-fixture unified diff.  Never writes to the golden directory.
    """
    fixtures = _discover_fixtures()

    if not fixtures:
        print("No fixtures found; nothing to compare.")
        return 0

    failures: list[str] = []

    for fixture in fixtures:
        stem = fixture.stem
        matter_type = FIXTURE_MATTER_TYPE.get(stem)
        intent = _load_intent(fixture)

        # Run extraction once per fixture; both manifest and selector comparisons use it.
        # Extraction is always run so the selector comparison can proceed even when the
        # manifest snapshot is missing.
        raw_manifest_bytes, manifest_dict = _run_extraction(fixture, matter_type)

        # --- manifest comparison (raw bytes, verbatim) ---
        manifest_path = _manifest_golden_path(fixture)
        if not manifest_path.exists():
            failures.append(
                f"MISSING  {manifest_path.name}  (run --update-golden to create)"
            )
        else:
            expected_manifest_bytes = manifest_path.read_bytes()
            if raw_manifest_bytes != expected_manifest_bytes:
                failures.append(
                    _diff_summary(
                        fixture.stem + " manifest",
                        expected_manifest_bytes.decode("utf-8"),
                        raw_manifest_bytes.decode("utf-8"),
                    )
                )

        # --- selector comparison ---
        selector_path = _selector_golden_path(fixture)
        if not selector_path.exists():
            failures.append(
                f"MISSING  {selector_path.name}  (run --update-golden to create)"
            )
        else:
            no_intent_result = _run_selector(manifest_dict, "general", fixture.stem)
            with_intent_result = _run_selector(manifest_dict, intent, fixture.stem)

            # Wrapper insertion order: no_intent first, then with_intent with intent before result.
            selector_wrapper = {
                "no_intent": no_intent_result,
                "with_intent": {
                    "intent": intent,
                    "result": with_intent_result,
                },
            }
            actual_selector_str = _serialise_selector(selector_wrapper)
            expected_selector_str = selector_path.read_bytes().decode("utf-8")
            if actual_selector_str != expected_selector_str:
                failures.append(
                    _diff_summary(
                        fixture.stem + " selector",
                        expected_selector_str,
                        actual_selector_str,
                    )
                )

    if failures:
        print(f"FAIL: {len(failures)} snapshot(s) differ:\n")
        for msg in failures:
            print(msg)
            print()
        return 1

    total = len(fixtures)
    print(f"OK: {total * 2} snapshots match ({total} fixtures x 2).")
    return 0


# ---------------------------------------------------------------------------
# Diff summary helper (readable per-fixture unified diff report)
# ---------------------------------------------------------------------------

def _diff_summary(label: str, expected: str, actual: str) -> str:
    """Return a human-readable unified diff for one snapshot mismatch.

    Shows the first _DIFF_MAX_LINES diff lines with a truncation note when the
    diff exceeds that limit.  Uses difflib.unified_diff so positional context
    and duplicate-line count changes are always visible.
    """
    exp_lines = expected.splitlines(keepends=True)
    act_lines = actual.splitlines(keepends=True)

    diff_iter = difflib.unified_diff(
        exp_lines,
        act_lines,
        fromfile=f"{label} (expected)",
        tofile=f"{label} (actual)",
    )
    diff_lines = list(diff_iter)

    parts = [f"MISMATCH {label}"]
    if not diff_lines:
        # Bytes differed but line-level diff is empty (e.g. BOM or line-ending encoding difference).
        parts.append("  (content differs at byte level; no line-level diff)")
    else:
        truncated = len(diff_lines) > _DIFF_MAX_LINES
        shown = diff_lines[:_DIFF_MAX_LINES]
        for line in shown:
            parts.append("  " + line.rstrip("\n"))
        if truncated:
            parts.append(
                f"  ... diff truncated ({len(diff_lines) - _DIFF_MAX_LINES} more lines not shown)"
            )

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(
        description="Golden snapshot runner for legal-diagram. "
                    "Run from skill root: python scripts/tests/run_golden.py"
    )
    parser.add_argument(
        "--update-golden",
        action="store_true",
        help="Regenerate all snapshots (write mode). Never runs comparisons.",
    )
    args = parser.parse_args()

    if args.update_golden:
        sys.exit(update_golden())
    else:
        sys.exit(compare_golden())


if __name__ == "__main__":
    main()
