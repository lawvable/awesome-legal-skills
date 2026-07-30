"""verify_render.py — Tier-1 optional render-verification gate for legal-diagram HTML exports.

Contract:
    verify_render(html_path, adapter=None) -> dict
        {
            "status": "clean" | "syntax_error" | "unverified",
            "ok":     True    | False           | None,
            "error":  str     | None,
        }

Design constraints:
    - DO NOT shell out to a host browser-automation wrapper from Python.
      (Some wrappers are shell-only; a Python subprocess can deadlock.)
    - Only mmdc (mermaid-cli) is used as the built-in Python subprocess adapter.
    - Headless-browser verification is a documented shell step in workflows/html-export.md.
    - Degrades gracefully to 'unverified' (never a silent pass) when no renderer
      is available.

CLI usage:
    python scripts/verify_render.py <html_path>

    Exit codes:
        0  — clean or unverified (safe to proceed)
        2  — syntax_error (Mermaid parse failure detected)
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from typing import Callable


# ── HTML extraction helpers ───────────────────────────────────────────────────


class _ScriptExtractor(HTMLParser):
    """Minimal HTML parser that captures the text content of <script id="mermaid-source">."""

    def __init__(self) -> None:
        super().__init__()
        self._in_target = False
        self.content: str | None = None

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag == "script":
            attr_dict = dict(attrs)
            if attr_dict.get("id") == "mermaid-source":
                self._in_target = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "script":
            self._in_target = False

    def handle_data(self, data: str) -> None:
        if self._in_target:
            self.content = data


class _PreExtractor(HTMLParser):
    """Captures the raw (HTML-escaped) text content of <pre class="mermaid">."""

    def __init__(self) -> None:
        super().__init__()
        self._in_target = False
        self._raw_parts: list[str] = []
        self.content: str | None = None
        self._done = False

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if self._done:
            return
        if tag == "pre":
            attr_dict = dict(attrs)
            classes = attr_dict.get("class", "").split()
            if "mermaid" in classes:
                self._in_target = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "pre" and self._in_target and not self._done:
            self._in_target = False
            self._done = True
            self.content = "".join(self._raw_parts)

    def handle_data(self, data: str) -> None:
        if self._in_target:
            self._raw_parts.append(data)

    def handle_entityref(self, name: str) -> None:
        # Named entity references (e.g. &amp;) — unescape via the entity table.
        import html as _html
        self._raw_parts.append(_html.unescape(f"&{name};"))

    def handle_charref(self, name: str) -> None:
        # Numeric character references (e.g. &#62;).
        import html as _html
        self._raw_parts.append(_html.unescape(f"&#{name};"))


def extract_mermaid_source(html: str) -> str | None:
    """Extract the Mermaid source diagram from an HTML string.

    Extraction strategy:
      1. JSON.parse the text content of <script id="mermaid-source" type="application/json">.
      2. Fall back to the HTML-unescaped text content of <pre class="mermaid">.
      3. Return None when neither is present.
    """
    # Strategy 1: #mermaid-source JSON script element.
    extractor = _ScriptExtractor()
    try:
        extractor.feed(html)
    except Exception:
        pass
    if extractor.content is not None:
        try:
            decoded = json.loads(extractor.content)
            if isinstance(decoded, str) and decoded:
                return decoded
        except (json.JSONDecodeError, ValueError):
            pass

    # Strategy 2: <pre class="mermaid"> fallback (HTML-unescape handled in parser).
    pre_extractor = _PreExtractor()
    try:
        pre_extractor.feed(html)
    except Exception:
        pass
    if pre_extractor.content is not None and pre_extractor.content.strip():
        import html as _html
        return _html.unescape(pre_extractor.content)

    return None


# ── Built-in mmdc adapter ─────────────────────────────────────────────────────


def _mmdc_adapter(source: str) -> dict:
    """Run mmdc (mermaid-cli) on *source* and return a result dict.

    Uses two temp files: one .mmd input, one .svg output.
    Subprocess errors, timeouts, and OSErrors are caught and returned as
    'unverified' (graceful degradation, never raises).

    Return shape: {"status": str, "ok": bool|None, "error": str|None}
    """
    tmp_mmd: str | None = None
    tmp_svg: str | None = None
    try:
        # Write source to a named temp file.
        with tempfile.NamedTemporaryFile(
            suffix=".mmd", delete=False, mode="w", encoding="utf-8"
        ) as mmd_f:
            mmd_f.write(source)
            tmp_mmd = mmd_f.name

        tmp_svg = tmp_mmd.replace(".mmd", ".svg")

        proc = subprocess.run(  # audit-ok: fixed command [mmdc], no user input in argv
            ["mmdc", "-i", tmp_mmd, "-o", tmp_svg],
            capture_output=True,
            text=True,
            timeout=60,
        )

        combined_output = (proc.stderr or "") + (proc.stdout or "")
        has_error_keyword = any(
            kw in combined_output for kw in ("error", "Error", "Syntax", "Parse", "syntax", "parse")
        )

        if proc.returncode != 0 or has_error_keyword:
            msg = combined_output.strip() or f"mmdc exited with code {proc.returncode}"
            return {"status": "syntax_error", "ok": False, "error": msg}

        return {"status": "clean", "ok": True, "error": None}

    except subprocess.TimeoutExpired:
        return {
            "status": "unverified",
            "ok": None,
            "error": "mmdc timed out (60 s); diagram not verified",
        }
    except OSError as exc:
        return {
            "status": "unverified",
            "ok": None,
            "error": f"mmdc could not be launched: {exc}",
        }
    except Exception as exc:  # pylint: disable=broad-except
        return {
            "status": "unverified",
            "ok": None,
            "error": f"unexpected error in mmdc adapter: {exc}",
        }
    finally:
        for path in (tmp_mmd, tmp_svg):
            if path:
                try:
                    os.unlink(path)
                except OSError:
                    pass


# ── Public API ────────────────────────────────────────────────────────────────

_AdapterFn = Callable[[str], dict]

_UNVERIFIED_NO_RENDERER = {
    "status": "unverified",
    "ok": None,
    "error": (
        "no renderer available "
        "(install @mermaid-js/mermaid-cli or pass an adapter)"
    ),
}


def verify_render(
    html_path: str | Path | None,
    adapter: _AdapterFn | None = None,
    *,
    _html_content: str | None = None,
) -> dict:
    """Verify that the Mermaid diagram in *html_path* renders without parse errors.

    Parameters
    ----------
    html_path:
        Path to the HTML file produced by render_html.render().  May be None
        only when *_html_content* is supplied directly (test convenience).
    adapter:
        Optional callable ``(source: str) -> dict`` following the same return
        shape as this function.  When None, auto-detection is applied:
        - mmdc on PATH → use _mmdc_adapter
        - otherwise → return unverified
    _html_content:
        Internal parameter for tests; bypasses file I/O.

    Returns
    -------
    dict with keys:
        status  "clean" | "syntax_error" | "unverified"
        ok      True    | False           | None
        error   str     | None
    """
    # 1. Load HTML.
    if _html_content is not None:
        html = _html_content
    elif html_path is None:
        return {
            "status": "unverified",
            "ok": None,
            "error": "no HTML path or content provided",
        }
    else:
        try:
            html = Path(html_path).read_text(encoding="utf-8")
        except OSError as exc:
            return {
                "status": "unverified",
                "ok": None,
                "error": f"could not read HTML file: {exc}",
            }

    # 2. Extract Mermaid source.
    source = extract_mermaid_source(html)
    if not source:
        return {
            "status": "unverified",
            "ok": None,
            "error": "no Mermaid source found in HTML",
        }

    # 3. Resolve adapter (adapter is callable or None per the signature).
    resolved_adapter: _AdapterFn
    if callable(adapter):
        resolved_adapter = adapter
    elif shutil.which("mmdc"):
        resolved_adapter = _mmdc_adapter
    else:
        return dict(_UNVERIFIED_NO_RENDERER)

    # 4. Run adapter; map result to canonical shape.
    try:
        raw = resolved_adapter(source)
    except Exception as exc:  # pylint: disable=broad-except
        return {
            "status": "syntax_error",
            "ok": False,
            "error": f"adapter raised: {exc}",
        }

    # Normalise: ensure canonical keys are present.
    status = raw.get("status", "unverified")
    ok = raw.get("ok", None)
    error = raw.get("error", None)

    if status not in ("clean", "syntax_error", "unverified"):
        status = "unverified"

    return {"status": status, "ok": ok, "error": error}


# ── CLI entrypoint ────────────────────────────────────────────────────────────


def _main() -> None:  # pragma: no cover — thin I/O shell
    import argparse

    parser = argparse.ArgumentParser(
        description="Tier-1 render-verification gate for legal-diagram HTML exports."
    )
    parser.add_argument("html_path", help="Path to the HTML file to verify.")
    args = parser.parse_args()

    result = verify_render(args.html_path)
    print(json.dumps(result, indent=2))

    if result["status"] == "syntax_error":
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    _main()
