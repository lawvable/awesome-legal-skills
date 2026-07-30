"""Smoke E2E test: fixture -> extract -> select -> render -> HTML artefact.

Covers the product surface (subprocess entrypoints only) without re-testing
extraction accuracy, selector calibration, or UX unit details.  One smoke
function runs the full pipeline and checks that each stage exits 0 and
produces the expected output contract.

House conventions (mirror run_golden.py / test_render_ux.py):
  - Bare __main__ runner iterating test_* via globals(); no pytest fixtures or
    parametrize; exits non-zero on any failure.
  - Also passes under pytest (plain functions, no pytest-specific constructs).
  - Uses subprocess + tempdir throughout (product surface only).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

_HERE = Path(__file__).resolve()
_SKILL_ROOT = _HERE.parents[2]  # scripts/tests/test_e2e_smoke.py -> skill root

_EXTRACT_SCRIPT = _SKILL_ROOT / "scripts" / "extract_entities.py"
_SELECTOR_SCRIPT = _SKILL_ROOT / "scripts" / "diagram_selector.py"
_RENDER_SCRIPT = _SKILL_ROOT / "scripts" / "render_html.py"
_FIXTURE = _SKILL_ROOT / "scripts" / "tests" / "fixtures" / "en_employment.md"


def _run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        cmd,
        capture_output=True,
        text=True,
        env=env,
        timeout=90,
        cwd=str(_SKILL_ROOT),
    )


def test_smoke_e2e_fixture_extract_select_render_html() -> None:
    """Full pipeline smoke: extract -> select -> render -> HTML artefact.

    Stage 1: extract_entities.py on en_employment.md with matter_type=employment
             (mirrors run_golden.py invocation pattern exactly).
    Stage 2: diagram_selector.py fed the extraction JSON.
    Stage 3: render_html.py with a minimal mermaid block and figure-desc.
    Stage 4: artefact sanity (exists, non-trivial, disclaimer banner, tablist role).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        # ── Stage 1: extraction ──────────────────────────────────────────────
        # Mirror run_golden.py: relative path from skill root, --matter_type flag.
        relative_fixture = _FIXTURE.relative_to(_SKILL_ROOT)
        extract_cmd = [
            sys.executable, str(_EXTRACT_SCRIPT),
            "--input", str(relative_fixture),
            "--matter_type", "employment",
        ]
        extract_proc = _run(extract_cmd)
        assert extract_proc.returncode == 0, (
            f"extract_entities.py exited {extract_proc.returncode}:\n{extract_proc.stderr}"
        )

        extraction_json = extract_proc.stdout
        manifest = json.loads(extraction_json)

        # Manifest must have candidates in candidate_manifest
        candidate_manifest = manifest.get("candidate_manifest", {})
        candidates = candidate_manifest.get("candidates", [])
        assert len(candidates) > 0, (
            f"Extraction produced no candidates; candidate_manifest keys: "
            f"{list(candidate_manifest.keys())}"
        )

        # Write extraction JSON to temp file for selector input
        extraction_path = Path(tmpdir) / "extraction.json"
        extraction_path.write_text(extraction_json, encoding="utf-8")

        # ── Stage 2: selector ────────────────────────────────────────────────
        # Mirror run_golden.py: pass extraction_result + intent via --extraction-json.
        selector_payload = {
            "extraction_result": manifest["extraction_result"],
            "intent": "general",
        }
        selector_cmd = [
            sys.executable, str(_SELECTOR_SCRIPT),
            "--extraction-json", json.dumps(selector_payload),
        ]
        selector_proc = _run(selector_cmd)
        assert selector_proc.returncode == 0, (
            f"diagram_selector.py exited {selector_proc.returncode}:\n{selector_proc.stderr}"
        )

        selector_result = json.loads(selector_proc.stdout)
        assert "recommended_type" in selector_result, (
            f"Selector output missing 'recommended_type'; got keys: {list(selector_result.keys())}"
        )
        # Must carry a recommendation type (string, non-empty)
        rec_type = selector_result["recommended_type"]
        assert isinstance(rec_type, str) and rec_type, (
            f"recommended_type must be a non-empty string, got: {rec_type!r}"
        )

        # ── Stage 3: render ──────────────────────────────────────────────────
        # Minimal valid mermaid block (mirror test_render_ux.py _render helper).
        mermaid_block = "flowchart TD\n  A-->B"
        figure_desc = json.dumps({"title": "Smoke Test"})
        output_html = Path(tmpdir) / "smoke_output.html"

        render_cmd = [
            sys.executable, str(_RENDER_SCRIPT),
            "--mermaid-block", mermaid_block,
            "--figure-desc", figure_desc,
            "--output-path", str(output_html),
        ]
        render_proc = _run(render_cmd)
        assert render_proc.returncode == 0, (
            f"render_html.py exited {render_proc.returncode}:\n{render_proc.stderr}"
        )

        render_result = json.loads(render_proc.stdout)
        assert render_result.get("ok") is True, (
            f"render_html.py returned ok=False: {render_result}"
        )
        assert "output_path" in render_result, (
            f"render_html.py output missing 'output_path'; got: {render_result}"
        )
        assert "file_size_kb" in render_result, (
            f"render_html.py output missing 'file_size_kb'; got: {render_result}"
        )

        # ── Stage 4: artefact sanity ─────────────────────────────────────────
        assert output_html.exists(), (
            f"HTML artefact not found at {output_html}"
        )
        file_size = output_html.stat().st_size
        assert file_size > 4096, (
            f"HTML artefact is suspiciously small ({file_size} bytes); expected > 4096"
        )

        html_content = output_html.read_text(encoding="utf-8")

        # Disclaimer banner must be present (core accessibility/legal requirement).
        assert 'class="disclaimer-banner"' in html_content, (
            "HTML artefact must contain the disclaimer banner (class='disclaimer-banner')"
        )

        # ARIA tablist role must be present (W5.4 requirement).
        assert 'role="tablist"' in html_content, (
            "HTML artefact must contain role='tablist' (W5.4 ARIA tabs requirement)"
        )


if __name__ == "__main__":
    _tests = [
        v for name, v in sorted(globals().items())
        if name.startswith("test_") and callable(v)
    ]
    _failed = 0
    for _test in _tests:
        try:
            _test()
            print(f"ok : {_test.__name__}")
        except Exception as _exc:
            print(f"FAIL: {_test.__name__}: {_exc}")
            _failed += 1
    print(f"\n{len(_tests) - _failed} tests passed, {_failed} failed")
    if _failed:
        sys.exit(1)
