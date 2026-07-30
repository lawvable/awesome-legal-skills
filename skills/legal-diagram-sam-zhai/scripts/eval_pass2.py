"""Pass-2 eval CLI: grade an LLM patch against user-owned label expectations.

Usage:
    python eval_pass2.py --manifest <frozen.json> --patch <patch.json> --labels <labels.json>

Output: single JSON object on stdout.

Exit codes:
    0 -- graded (patch passed gate; regardless of score)
    1 -- gate blocked the patch (no-error findings blocked; ok=false; grading aborted)
    2 -- usage or parse error (malformed JSON input, invalid predicate shape, missing file)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from extraction.evaluation import grade, PredicateError


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Grade an LLM patch against pass-2 label expectations."
    )
    parser.add_argument("--manifest", required=True, help="Path to the frozen manifest JSON file.")
    parser.add_argument("--patch", required=True, help="Path to the JSON Patch file (RFC 6902 array).")
    parser.add_argument("--labels", required=True, help="Path to the pass-2 labels JSON file.")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    patch_path = Path(args.patch)
    labels_path = Path(args.labels)

    # Read files; exit 2 on any OS error.
    try:
        manifest_bytes = manifest_path.read_bytes()
    except OSError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        sys.exit(2)

    try:
        patch_text = patch_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        sys.exit(2)

    try:
        labels_text = labels_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        sys.exit(2)

    # Parse JSON; exit 2 on parse error.
    try:
        manifest = json.loads(manifest_bytes)
    except json.JSONDecodeError as exc:
        print(json.dumps({"ok": False, "error": f"Manifest JSON parse error: {exc}"}))
        sys.exit(2)

    try:
        patch_ops = json.loads(patch_text)
    except json.JSONDecodeError as exc:
        print(json.dumps({"ok": False, "error": f"Patch JSON parse error: {exc}"}))
        sys.exit(2)

    try:
        labels = json.loads(labels_text)
    except json.JSONDecodeError as exc:
        print(json.dumps({"ok": False, "error": f"Labels JSON parse error: {exc}"}))
        sys.exit(2)

    # Grade; PredicateError maps to exit 2.
    try:
        result = grade(manifest_bytes, manifest, patch_ops, labels)
    except PredicateError as exc:
        print(json.dumps({"ok": False, "error": f"Predicate error: {exc}"}))
        sys.exit(2)

    print(json.dumps(result.to_dict(), ensure_ascii=False))
    sys.exit(0 if result.ok else 1)


if __name__ == "__main__":
    main()
