"""Tests for scripts/verify_render.py — TDD coverage for render-verification gate.

All tests are self-contained: no network, no real mmdc, no Chromium.
HTML fixtures are built from render_html.render() to ensure the #mermaid-source
element is real and consistent with the actual template.
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import render_html
from verify_render import extract_mermaid_source, verify_render as vr, _mmdc_adapter


# ── HTML fixture builder ──────────────────────────────────────────────────────

_SAMPLE_MERMAID = "flowchart TD\n    A[Alice] --> B[Bob]"
# The arrow sequence '-->' must survive JSON round-trip; used by test (a).

def _make_html(mermaid_block: str = _SAMPLE_MERMAID) -> str:
    """Render a real HTML string via render_html.render() into a temp file and read it back."""
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8") as f:
        tmp_path = f.name
    try:
        render_html.render(
            mermaid_block=mermaid_block,
            figure_desc={"title": "Test", "caption": "test cap"},
            output_path=tmp_path,
            allow_cdn=False,
        )
        return Path(tmp_path).read_text(encoding="utf-8")
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


# ── (a) extract_mermaid_source from #mermaid-source JSON script ───────────────

def test_extract_from_json_script_roundtrip():
    """JSON-encoded source in #mermaid-source survives round-trip, including '-->' arrow."""
    html = _make_html(_SAMPLE_MERMAID)
    result = extract_mermaid_source(html)
    assert result is not None
    assert "-->" in result
    assert "flowchart TD" in result


# ── (b) extract from <pre class="mermaid"> fallback ──────────────────────────

def test_extract_from_pre_mermaid_fallback():
    """When #mermaid-source is absent, fall back to <pre class="mermaid"> (HTML-unescaped)."""
    # Construct a minimal HTML with only a <pre class="mermaid"> and HTML-escaped content.
    escaped_source = "flowchart TD\n    A[&amp;] --&gt; B"
    html = f'<html><body><pre class="mermaid">{escaped_source}</pre></body></html>'
    result = extract_mermaid_source(html)
    assert result is not None
    assert "&" in result    # unescaped from &amp;
    assert "-->" in result  # unescaped from --&gt;
    assert "&amp;" not in result
    assert "--&gt;" not in result


# ── (c) extract returns None when neither present ─────────────────────────────

def test_extract_returns_none_when_absent():
    html = "<html><body><p>No diagram here.</p></body></html>"
    result = extract_mermaid_source(html)
    assert result is None


# ── (d) verify_render with stub adapter returning clean ──────────────────────

def test_verify_render_clean_with_stub_adapter():
    html = _make_html()

    def _clean_adapter(source: str) -> dict:
        assert isinstance(source, str) and source  # adapter receives the extracted source
        return {"status": "clean", "ok": True, "error": None}

    result = vr(html_path=None, adapter=_clean_adapter, _html_content=html)
    assert result["status"] == "clean"
    assert result["ok"] is True
    assert result["error"] is None


# ── (e) stub adapter raising / returning failure → syntax_error ──────────────

def test_verify_render_syntax_error_with_stub_adapter():
    html = _make_html()

    def _error_adapter(source: str) -> dict:
        assert isinstance(source, str) and source  # adapter receives the extracted source
        return {"status": "syntax_error", "ok": False, "error": "Syntax error near '-->'"}

    result = vr(html_path=None, adapter=_error_adapter, _html_content=html)
    assert result["status"] == "syntax_error"
    assert result["ok"] is False
    assert result["error"] is not None
    assert "Syntax" in result["error"]


# ── (f) verify_render with adapter=None and mmdc absent → unverified ─────────

def test_verify_render_unverified_when_no_mmdc(monkeypatch):
    html = _make_html()
    monkeypatch.setattr("shutil.which", lambda _: None)

    result = vr(html_path=None, adapter=None, _html_content=html)
    assert result["status"] == "unverified"
    assert result["ok"] is None
    assert result["error"] is not None


# ── (g) _mmdc_adapter with subprocess monkeypatched ──────────────────────────

def test_mmdc_adapter_nonzero_exit_syntax_error(monkeypatch):
    """Nonzero exit + stderr containing 'Syntax error' → syntax_error."""
    mock_result = MagicMock()
    mock_result.returncode = 1
    mock_result.stdout = ""
    mock_result.stderr = "Error: Syntax error in graph at line 2"

    monkeypatch.setattr("subprocess.run", lambda *a, **kw: mock_result)

    result = _mmdc_adapter(_SAMPLE_MERMAID)
    assert result["status"] == "syntax_error"
    assert result["ok"] is False
    assert "Syntax" in result["error"]


def test_mmdc_adapter_zero_exit_clean(monkeypatch):
    """Zero exit → clean."""
    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = ""
    mock_result.stderr = ""

    monkeypatch.setattr("subprocess.run", lambda *a, **kw: mock_result)

    result = _mmdc_adapter(_SAMPLE_MERMAID)
    assert result["status"] == "clean"
    assert result["ok"] is True
    assert result["error"] is None
