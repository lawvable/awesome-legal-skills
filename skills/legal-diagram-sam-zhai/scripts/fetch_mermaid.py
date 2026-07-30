"""fetch_mermaid.py -- stdlib-only Mermaid engine vendor helper.

Fetches the pinned Mermaid JS bundle from jsDelivr CDN into assets/vendor/ so
the CLI HTML export works offline on subsequent runs.

Usage:
    python scripts/fetch_mermaid.py [--version X.Y.Z]

Always exits 0. Always prints exactly one JSON object. Never raises on network/IO error.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

# Single source of truth: version, path, and CDN URL all live in render_html.
# render_html has no top-level fetch_mermaid import (its import is lazy inside
# render()), so this import is safe and creates no circular dependency.
from render_html import MERMAID_VERSION, _vendored_mermaid_path, cdn_url

_MIN_SIZE_BYTES = 100 * 1024  # 100 KB sanity check


def vendor_status() -> dict:
    """Report whether the vendored Mermaid bundle is present. No network call."""
    path = _vendored_mermaid_path()
    return {
        "present": path.exists(),
        "path": str(path),
        "hint": "run: python scripts/fetch_mermaid.py to vendor the engine for offline use",
    }


def ensure_vendored(
    version: str | None = None,
    dest: Path | None = None,
    allow_network: bool = True,
    timeout: int = 10,
) -> dict:
    """Ensure mermaid.min.js is present at *dest*.

    Parameters
    ----------
    version:
        Mermaid version string to fetch. Defaults to MERMAID_VERSION from render_html.
    dest:
        Destination path for the vendored file. Defaults to
        ``assets/vendor/mermaid.min.js`` relative to the project root.
    allow_network:
        When False, never attempt a download even if the file is absent.
    timeout:
        HTTP request timeout in seconds.

    Returns
    -------
    dict with keys:
        ok      -- bool
        mode    -- "vendored" | "skipped" | "no_network"
        path    -- str (absolute path) when ok is True
        error   -- str when ok is False
    """
    if version is None:
        version = MERMAID_VERSION

    if dest is None:
        dest = _vendored_mermaid_path()

    # Already vendored and non-trivial?
    if dest.exists() and dest.stat().st_size >= _MIN_SIZE_BYTES:
        return {"ok": True, "mode": "vendored", "path": str(dest)}

    # Network disabled?
    if not allow_network:
        return {
            "ok": False,
            "mode": "no_network",
            "error": "offline; engine not vendored, falling back (allow_network=False)",
        }

    url = cdn_url(version)
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(url, timeout=timeout) as resp:  # noqa: S310
            data = resp.read()
        if len(data) < _MIN_SIZE_BYTES:
            return {
                "ok": False,
                "error": (
                    f"offline; engine not vendored, falling back: "
                    f"download from {url} returned only {len(data)} bytes "
                    f"(expected >= {_MIN_SIZE_BYTES})"
                ),
            }
        dest.write_bytes(data)
        return {"ok": True, "mode": "vendored", "path": str(dest)}
    except Exception as exc:
        return {
            "ok": False,
            "error": (
                f"offline; engine not vendored, falling back: "
                f"network error fetching {url}: {exc}"
            ),
        }


def _main() -> None:
    parser = argparse.ArgumentParser(
        description="Vendor the Mermaid JS engine into assets/vendor/mermaid.min.js."
    )
    parser.add_argument(
        "--version",
        default=None,
        help=f"Mermaid version to fetch (default: {MERMAID_VERSION}).",
    )
    parser.add_argument(
        "--dest",
        default=None,
        help="Destination path for mermaid.min.js (default: assets/vendor/mermaid.min.js).",
    )
    parser.add_argument(
        "--no-network",
        action="store_true",
        help="Dry-run: skip download even if file absent.",
    )
    args = parser.parse_args()

    dest = Path(args.dest) if args.dest else None
    result = ensure_vendored(
        version=args.version,
        dest=dest,
        allow_network=not args.no_network,
    )
    print(json.dumps(result))


if __name__ == "__main__":
    _main()
    sys.exit(0)
