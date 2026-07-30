"""conftest.py — pytest configuration for scripts/tests.

Registers custom markers and isolates the suite from a locally-fetched Mermaid bundle.
"""
import sys
from pathlib import Path

import pytest

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "mmdc_golden: render-regression test requiring mermaid-cli (mmdc); opt-in",
    )


@pytest.fixture(autouse=True)
def _ignore_vendored_mermaid(tmp_path, monkeypatch):
    """Pin the Mermaid loader to ignore any locally-fetched assets/vendor bundle.

    The render tests assume no vendored engine in the test env (they assert the
    source-only and CDN loader modes). Running `fetch_mermaid` drops a ~3 MB
    bundle into assets/vendor/ that would flip the loader to 'vendored', which
    breaks and drastically slows those tests. Forcing the path to a nonexistent
    file keeps the whole suite deterministic regardless of tree state. No test
    relies on a real vendored bundle (vendored-mode tests pass script_body
    directly).
    """
    try:
        import render_html
    except Exception:
        return
    monkeypatch.setattr(
        render_html,
        "_vendored_mermaid_path",
        lambda: tmp_path / "no-vendored-mermaid.js",
        raising=False,
    )
