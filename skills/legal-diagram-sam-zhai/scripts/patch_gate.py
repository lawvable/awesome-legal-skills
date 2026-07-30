"""Patch-gate CLI: validate and optionally apply LLM-produced JSON Patch ops.

Usage:
    python patch_gate.py --manifest <manifest.json> --patch <patch.json> [--apply]

Exit codes:
    0 -- ok (no error-severity findings; warn-only patches still exit 0)
    1 -- blocking findings (one or more error-severity findings)
    2 -- usage error or JSON parse error
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from extraction.patching import gate


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate (and optionally apply) a JSON Patch against an extraction manifest."
    )
    parser.add_argument("--manifest", required=True, help="Path to the manifest JSON file.")
    parser.add_argument("--patch", required=True, help="Path to the JSON Patch file (RFC 6902 array).")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply the patch and include enriched_extraction_result in output when ok.",
    )
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    patch_path = Path(args.patch)

    try:
        manifest_text = manifest_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(json.dumps({"ok": False, "findings": [], "error": str(exc)}))
        sys.exit(2)

    try:
        patch_text = patch_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(json.dumps({"ok": False, "findings": [], "error": str(exc)}))
        sys.exit(2)

    try:
        manifest = json.loads(manifest_text)
    except json.JSONDecodeError as exc:
        print(json.dumps({"ok": False, "findings": [], "error": f"Manifest JSON parse error: {exc}"}))
        sys.exit(2)

    try:
        patch_ops = json.loads(patch_text)
    except json.JSONDecodeError as exc:
        print(json.dumps({"ok": False, "findings": [], "error": f"Patch JSON parse error: {exc}"}))
        sys.exit(2)

    result = gate(manifest, patch_ops, apply=args.apply)
    print(json.dumps(result.to_dict(), ensure_ascii=False))
    sys.exit(0 if result.ok else 1)


if __name__ == "__main__":
    main()
