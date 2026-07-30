"""Tests for render_html UI_STRINGS -- W3.5 EN/FR chrome scaffolding (W5 extends).

Conventions (mirror scripts/tests/test_render_classdef.py):
  - Plain functions, no pytest fixtures (tempfile used inline).
  - Standalone __main__ block iterating test_* callables; exit non-zero on failure.
  - Works under pytest too.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import render_html
from render_html import UI_STRINGS

_FR_DISCLAIMER = (
    "Sortie d'IA générative · Aide visuelle seulement. Ne constitue pas un avis "
    "juridique. Vérifiez tous les faits contre les documents sources."
)

_DIGEST_ROWS = [{
    "row_num": 1, "category": "Obligation", "finding": "Le vendeur doit livrer",
    "party": "Vendeur", "verbatim": "Le vendeur doit livrer les documents",
    "anchor": "§1", "page": None, "slide": None, "unverified": False,
}]


def _render(out: Path, **kwargs) -> str:
    render_html.render("flowchart TD\n  A-->B", {"title": "T"}, str(out), **kwargs)
    return out.read_text(encoding="utf-8")


def test_ui_strings_fr_covers_en_keys():
    """The fr table must cover exactly the same keys as the en table."""
    assert "en" in UI_STRINGS and "fr" in UI_STRINGS
    assert set(UI_STRINGS["fr"]) == set(UI_STRINGS["en"]), (
        f"key mismatch -- en-only: {set(UI_STRINGS['en']) - set(UI_STRINGS['fr'])}, "
        f"fr-only: {set(UI_STRINGS['fr']) - set(UI_STRINGS['en'])}"
    )


def test_default_render_keeps_en_strings():
    """Default (no ui_lang) rendering must keep the current EN chrome verbatim."""
    with tempfile.TemporaryDirectory() as d:
        html = _render(Path(d) / "out.html", digest_table=_DIGEST_ROWS)
    assert '<html lang="en">' in html
    for label in ("Overview", "How to Read", "Observations", "⚠ Limitations", "Source Docs"):
        assert f">{label}</button>" in html, f"EN tab label {label!r} missing"
    assert "GenAI Output" in html
    assert "Not legal advice." in html


def test_ui_lang_fr_swaps_tabs_disclaimer_and_lang():
    """ui_lang='fr' must swap tab labels, the disclaimer banner, and <html lang>."""
    with tempfile.TemporaryDirectory() as d:
        html = _render(Path(d) / "out.html", digest_table=_DIGEST_ROWS, ui_lang="fr")
    assert '<html lang="fr">' in html
    for label in ("Aperçu", "Comment lire", "Observations", "⚠ Limites", "Documents sources"):
        assert f">{label}</button>" in html, f"FR tab label {label!r} missing"
    assert _FR_DISCLAIMER in html, "FR disclaimer banner must appear verbatim"
    assert "GenAI Output" not in html


def test_cli_ui_lang_flag():
    """render_html.py --ui-lang fr must produce FR chrome via the CLI."""
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "out.html"
        r = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, "render_html.py",
             "--mermaid-block", "flowchart TD\n  A-->B",
             "--figure-desc", '{"title": "T"}',
             "--output-path", str(out),
             "--ui-lang", "fr"],
            capture_output=True, text=True, cwd=str(ROOT),
        )
        assert r.returncode == 0, r.stderr
        assert json.loads(r.stdout)["ok"] is True
        html = out.read_text(encoding="utf-8")
    assert '<html lang="fr">' in html
    assert "Aperçu" in html


if __name__ == "__main__":
    _tests = [
        v for name, v in sorted(globals().items())
        if name.startswith("test_") and callable(v)
    ]
    _failed = 0
    for _test in _tests:
        try:
            _test()
        except Exception as _exc:
            print(f"FAIL: {_test.__name__}: {_exc}")
            _failed += 1
    print(f"{len(_tests) - _failed} tests passed, {_failed} failed")
    if _failed:
        sys.exit(1)
