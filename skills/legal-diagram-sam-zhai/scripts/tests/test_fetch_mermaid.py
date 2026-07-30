"""Tests for fetch_mermaid.ensure_vendored and render_html fetch_engine integration.

All tests are network-free: urllib is monkeypatched throughout.
"""
from __future__ import annotations

import sys
import types
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Ensure scripts/ is importable
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


# ---------------------------------------------------------------------------
# fetch_mermaid.ensure_vendored tests
# ---------------------------------------------------------------------------

class TestEnsureVendored:
    """Unit tests for fetch_mermaid.ensure_vendored. No real network."""

    def test_successful_download_writes_file_and_returns_ok(self, tmp_path: Path) -> None:
        """When network succeeds and file size >= 100 KB, ok=True, mode='vendored'."""
        import fetch_mermaid

        dest = tmp_path / "vendor" / "mermaid.min.js"
        fake_content = b"x" * (110 * 1024)  # 110 KB — above threshold

        fake_response = MagicMock()
        fake_response.read.return_value = fake_content
        fake_response.__enter__ = lambda s: s
        fake_response.__exit__ = MagicMock(return_value=False)

        with patch("urllib.request.urlopen", return_value=fake_response) as mock_open:
            result = fetch_mermaid.ensure_vendored(
                version="11.15.0",
                dest=dest,
                allow_network=True,
                timeout=5,
            )

        assert result["ok"] is True
        assert result["mode"] == "vendored"
        assert "path" in result
        assert dest.exists()
        assert dest.read_bytes() == fake_content
        mock_open.assert_called_once()

    def test_network_error_returns_ok_false_no_exception(self, tmp_path: Path) -> None:
        """On any network/IO failure, ok=False, graceful message, no exception raised."""
        import fetch_mermaid

        dest = tmp_path / "vendor" / "mermaid.min.js"

        with patch("urllib.request.urlopen", side_effect=OSError("timeout")):
            result = fetch_mermaid.ensure_vendored(
                version="11.15.0",
                dest=dest,
                allow_network=True,
                timeout=5,
            )

        assert result["ok"] is False
        assert "error" in result
        # Must contain a helpful offline message
        assert "offline" in result["error"].lower() or "network" in result["error"].lower() or "timeout" in result["error"].lower()
        # No file left behind
        assert not dest.exists()

    def test_dest_already_present_skips_download(self, tmp_path: Path) -> None:
        """If dest exists and is non-trivial (>100 KB), return ok=True without downloading."""
        import fetch_mermaid

        dest = tmp_path / "vendor" / "mermaid.min.js"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(b"y" * (120 * 1024))  # 120 KB pre-existing

        with patch("urllib.request.urlopen") as mock_open:
            result = fetch_mermaid.ensure_vendored(
                version="11.15.0",
                dest=dest,
                allow_network=True,
                timeout=5,
            )

        assert result["ok"] is True
        mock_open.assert_not_called()

    def test_download_below_minimum_size_returns_error(self, tmp_path: Path) -> None:
        """If downloaded content is too small (< 100 KB), treat as failure."""
        import fetch_mermaid

        dest = tmp_path / "vendor" / "mermaid.min.js"
        fake_content = b"too small"

        fake_response = MagicMock()
        fake_response.read.return_value = fake_content
        fake_response.__enter__ = lambda s: s
        fake_response.__exit__ = MagicMock(return_value=False)

        with patch("urllib.request.urlopen", return_value=fake_response):
            result = fetch_mermaid.ensure_vendored(
                version="11.15.0",
                dest=dest,
                allow_network=True,
                timeout=5,
            )

        assert result["ok"] is False
        assert "error" in result

    def test_allow_network_false_skips_download_when_not_vendored(self, tmp_path: Path) -> None:
        """When allow_network=False and file absent, no download; ok=False."""
        import fetch_mermaid

        dest = tmp_path / "vendor" / "mermaid.min.js"

        with patch("urllib.request.urlopen") as mock_open:
            result = fetch_mermaid.ensure_vendored(
                version="11.15.0",
                dest=dest,
                allow_network=False,
                timeout=5,
            )

        mock_open.assert_not_called()
        assert result["ok"] is False

    def test_cdn_url_uses_version(self, tmp_path: Path) -> None:
        """The download URL must embed the requested version."""
        import fetch_mermaid

        dest = tmp_path / "vendor" / "mermaid.min.js"
        captured_urls: list[str] = []

        def fake_urlopen(url, timeout=None):
            captured_urls.append(url)
            raise OSError("intentional stop")

        with patch("urllib.request.urlopen", side_effect=fake_urlopen):
            fetch_mermaid.ensure_vendored(
                version="11.15.0",
                dest=dest,
                allow_network=True,
                timeout=5,
            )

        assert captured_urls, "urlopen must have been called"
        assert "11.15.0" in captured_urls[0]
        assert "cdn.jsdelivr.net" in captured_urls[0]


# ---------------------------------------------------------------------------
# render_html fetch_engine integration tests
# ---------------------------------------------------------------------------

class TestRenderFetchEngineFlag:
    """Test that render(..., fetch_engine=False) never calls ensure_vendored,
    and render(..., fetch_engine=True) invokes it."""

    @pytest.fixture(autouse=True)
    def _restore_modules(self):
        """Reloading render_html mid-test swaps sys.modules. Restore the originals
        afterwards so later test modules (e.g. test_render_ux) keep using the same
        render_html object the autouse conftest fixture patches; otherwise the patch
        misses and a present vendored bundle flips those tests to vendored mode."""
        saved = {name: sys.modules.get(name) for name in ("render_html", "fetch_mermaid")}
        yield
        for name, mod in saved.items():
            if mod is not None:
                sys.modules[name] = mod
            else:
                sys.modules.pop(name, None)

    def _fresh_render_module(self):
        """Reload render_html so patch state is clean each test."""
        if "render_html" in sys.modules:
            del sys.modules["render_html"]
        import render_html
        return render_html

    def test_fetch_engine_false_makes_no_fetch_call(self, tmp_path: Path) -> None:
        """Default render() (fetch_engine=False) must not call ensure_vendored."""
        render_html = self._fresh_render_module()

        out = tmp_path / "out.html"
        mock_ensure = MagicMock(return_value={"ok": True, "mode": "vendored", "path": str(tmp_path)})
        with patch.dict(sys.modules, {"fetch_mermaid": MagicMock(ensure_vendored=mock_ensure)}):
            render_html.render(
                "flowchart TD\nA-->B",
                {"title": "Test"},
                str(out),
                fetch_engine=False,
            )
        mock_ensure.assert_not_called()

    def test_fetch_engine_true_invokes_ensure_vendored(self, tmp_path: Path) -> None:
        """render(..., fetch_engine=True) must call ensure_vendored before _mermaid_loader."""
        render_html = self._fresh_render_module()

        out = tmp_path / "out.html"
        mock_ensure = MagicMock(return_value={"ok": False, "error": "offline; engine not vendored, falling back"})

        fake_fetch_module = types.ModuleType("fetch_mermaid")
        fake_fetch_module.ensure_vendored = mock_ensure  # type: ignore[attr-defined]

        with patch.dict(sys.modules, {"fetch_mermaid": fake_fetch_module}):
            # Reload so render_html picks up the patched module
            if "render_html" in sys.modules:
                del sys.modules["render_html"]
            import render_html as rh
            rh.render(
                "flowchart TD\nA-->B",
                {"title": "Test"},
                str(out),
                fetch_engine=True,
            )

        mock_ensure.assert_called_once()
