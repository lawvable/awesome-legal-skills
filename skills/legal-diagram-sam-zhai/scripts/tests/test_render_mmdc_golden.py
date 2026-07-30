"""test_render_mmdc_golden.py — mmdc render-regression guard.

Exercises the specific Mermaid construct that failed under the old 10.9.1 pin:
  - Two subgraphs each with their own `direction` directive (LR and TB)
  - A subgraph-to-subgraph edge between them

The test is opt-in via the `mmdc_golden` marker and self-skips when
mermaid-cli (mmdc) is not installed, keeping the default suite green in
environments without Node/Chromium.

Run selectively:
    python -m pytest -m mmdc_golden -v

Run as part of default suite (will skip if mmdc absent):
    python -m pytest scripts/tests/test_render_mmdc_golden.py -q -rs
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import render_html
from verify_render import verify_render


# ── Diagram fixture ───────────────────────────────────────────────────────────

# Two subgraphs with per-subgraph `direction` + a subgraph-to-subgraph link.
# This is the construct that broke on Mermaid 10.9.1.
_GOLDEN_DIAGRAM = """\
flowchart TD
    subgraph SG_A
        direction LR
        A1[Claimant files] --> A2[Served on respondent]
    end

    subgraph SG_B
        direction TB
        B1[Registry receives] --> B2[Tribunal schedules hearing]
    end

    SG_A --> SG_B
"""


# ── Test ──────────────────────────────────────────────────────────────────────


@pytest.mark.mmdc_golden
def test_subgraph_direction_and_cross_link_renders_clean(tmp_path):
    """Pinned mmdc engine must render subgraph-to-subgraph links with per-subgraph
    direction directives without a parse or syntax error.

    Self-skips when mmdc is not on PATH so the default suite stays green.
    """
    if not shutil.which("mmdc"):
        pytest.skip("mmdc (mermaid-cli) not installed")

    html_path = tmp_path / "golden_test.html"

    render_html.render(
        mermaid_block=_GOLDEN_DIAGRAM,
        figure_desc={"title": "Golden render test", "caption": "mmdc regression guard"},
        output_path=str(html_path),
        allow_cdn=False,
    )

    result = verify_render(str(html_path))

    assert result["status"] == "clean", (
        f"mmdc reported a render error for the golden diagram.\n"
        f"status={result['status']!r}  ok={result['ok']!r}  error={result['error']!r}\n"
        "This indicates the pinned Mermaid engine cannot render subgraph-to-subgraph "
        "links with per-subgraph direction -- the same regression as 10.9.1."
    )
    assert result["ok"] is True, (
        f"verify_render returned ok=False: {result['error']}"
    )
