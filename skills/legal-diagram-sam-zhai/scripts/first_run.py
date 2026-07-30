"""first_run.py -- stdlib-only first-run state detector for the legal-diagram skill.

Usage:
    python first_run.py          # detect mode: prints JSON {state, state_path}
    python first_run.py --mark   # mark mode:   prints JSON {state, state_path, marked}

State file location (in priority order):
    1. $LEGAL_DIAGRAM_STATE  (if set and non-empty)
    2. ~/.legal-diagram/state.json

Always exits 0. Always prints exactly one JSON object. Never raises on filesystem errors.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

_ENV_VAR = "LEGAL_DIAGRAM_STATE"
_DEFAULT_STATE = Path("~/.legal-diagram/state.json").expanduser()


def _state_path() -> Path:
    env = os.environ.get(_ENV_VAR, "").strip()
    return Path(env) if env else _DEFAULT_STATE


def _read_marker(path: Path) -> bool | None:
    """Return True if marker is present, False if file absent/not-true, None on OSError."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    try:
        data = json.loads(text)
        return isinstance(data, dict) and data.get("tutorial_offered") is True
    except (json.JSONDecodeError, ValueError):
        return False


def _is_writable(path: Path) -> bool:
    """Return True if the state file's parent can be created or is already writable."""
    parent = path.parent
    try:
        parent.mkdir(parents=True, exist_ok=True)
        return os.access(str(parent), os.W_OK)
    except OSError:
        return False


def detect(path: Path) -> dict:
    """Detect first-run state for *path* and return a result dict."""
    marked = _read_marker(path)
    if marked:
        return {"state": "returning", "state_path": str(path)}

    if _is_writable(path):
        return {"state": "first_run", "state_path": str(path)}

    return {"state": "unknown", "state_path": None}


def mark(path: Path) -> dict:
    """Write the tutorial-offered marker to *path* and return a result dict."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"tutorial_offered": True}), encoding="utf-8")
        return {"state": "returning", "state_path": str(path), "marked": True}
    except OSError:
        return {"state": "unknown", "state_path": None, "marked": False}


try:
    from fetch_mermaid import vendor_status as _vendor_status
except Exception:
    def _vendor_status() -> dict:  # type: ignore[misc]
        vendor_path = Path(__file__).parent.parent / "assets" / "vendor" / "mermaid.min.js"
        return {
            "present": vendor_path.exists(),
            "path": str(vendor_path),
            "hint": "run: python scripts/fetch_mermaid.py to vendor the engine for offline use",
        }


def _main() -> None:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--mark", action="store_true")
    args, _ = parser.parse_known_args()

    path = _state_path()
    result = mark(path) if args.mark else detect(path)
    result["mermaid_vendor"] = _vendor_status()
    print(json.dumps(result))


if __name__ == "__main__":
    _main()
    sys.exit(0)
