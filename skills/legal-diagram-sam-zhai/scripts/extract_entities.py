"""Orchestrator: normalize -> extract -> manifest -> emit JSON manifest.

Usage:
  python extract_entities.py --input <path> [--pages R] [--sheets A,B] [--matter_type T]
  python extract_entities.py --stdin
  python extract_entities.py --probe <pdf>
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from extraction import extract
from extraction.language import annotate_blocks
from extraction.manifest import build_manifest
from normalize import DEFAULT_LIMITS, normalize, normalize_stdin_text

EXT_KIND = {
    ".md": "md",
    ".txt": "txt",
    ".docx": "docx",
    ".pdf": "pdf",
    ".xlsx": "xlsx",
    ".xls": "xlsx",
    ".csv": "csv",
    ".pptx": "pptx",
}


def _safe_matter_name(path: str) -> str:
    name = Path(path).stem
    return re.sub(r"[^A-Za-z0-9._ -]+", "_", name).strip(" ._") or "matter"


def _safe_source(path: str, include_source_path: bool) -> str:
    return path if include_source_path else Path(path).name


def _parse_pages(value: str | None) -> list[int] | None:
    if not value:
        return None
    pages: list[int] = []
    for part in value.split(","):
        item = part.strip()
        if not item:
            continue
        if "-" in item:
            start_s, end_s = item.split("-", 1)
            start, end = int(start_s), int(end_s)
            if start <= 0 or end < start:
                raise ValueError("pages must use 1-based ranges like 1-3,5")
            pages.extend(range(start - 1, end))
        else:
            page = int(item)
            if page <= 0:
                raise ValueError("pages must be 1-based")
            pages.append(page - 1)
    return pages


def _enforce_file_size(path: str, max_file_bytes: int) -> None:
    if max_file_bytes < 0:
        print("Error: max_file_bytes must be non-negative.", file=sys.stderr)
        sys.exit(1)
    if max_file_bytes and os.path.getsize(path) > max_file_bytes:
        print(
            f"Error: file exceeds max_file_bytes ({max_file_bytes}). "
            "Use --max-file-bytes 0 only for trusted local inputs.",
            file=sys.stderr,
        )
        sys.exit(1)


def _probe(path: str) -> dict:
    import fitz  # type: ignore[reportMissingImports]  # PyMuPDF: runtime dep, no type stubs

    doc = fitz.open(path)
    try:
        total = len(doc)
        sample = "\n".join(doc[i].get_text() for i in range(min(3, total)))
        est = int(len(sample.split()) * 1.3 * total / max(1, min(3, total)))
        return {"pages": total, "estimated_tokens": est}
    finally:
        doc.close()


def main() -> None:
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--input")
    g.add_argument("--stdin", action="store_true")
    g.add_argument("--probe")
    p.add_argument("--pages")
    p.add_argument("--sheets")
    p.add_argument("--matter_type")
    p.add_argument("--lang", choices=("auto", "en", "fr"), default="auto")
    p.add_argument("--include-source-path", action="store_true")
    for key, default in DEFAULT_LIMITS.items():
        p.add_argument(f"--{key.replace('_', '-')}", type=int, default=default, dest=key)
    args = p.parse_args()

    if args.probe:
        if not os.path.exists(args.probe):
            print(f"Error: file not found: {args.probe}", file=sys.stderr)
            sys.exit(1)
        print(json.dumps(_probe(args.probe)))
        return

    if args.stdin:
        doc = normalize_stdin_text(sys.stdin.read())
        source = "stdin"
        matter_name = None
    else:
        path = args.input
        if not os.path.exists(path):
            print(f"Error: file not found: {path}", file=sys.stderr)
            sys.exit(1)
        _enforce_file_size(path, args.max_file_bytes)
        kind = EXT_KIND.get(Path(path).suffix.lower())
        if not kind:
            print(f"Error: unsupported file type: {Path(path).suffix}", file=sys.stderr)
            sys.exit(1)
        opts = {k: getattr(args, k) for k in DEFAULT_LIMITS if k != "max_file_bytes"}
        if args.pages:
            try:
                opts["pages"] = _parse_pages(args.pages)
            except ValueError as e:
                print(f"Error: {e}", file=sys.stderr)
                sys.exit(1)
        if args.sheets:
            opts["sheets"] = args.sheets.split(",")
        doc = normalize(path, kind, **opts)
        source = _safe_source(path, args.include_source_path)
        matter_name = _safe_matter_name(path)

    # W3.1 block-level language pass: per-block lang stays internal; only the
    # aggregate language_profile is emitted in the manifest.
    override = args.lang if args.lang in ("en", "fr") else None
    language_profile = annotate_blocks(getattr(doc, "blocks", []) or [], override=override)

    result, candidate_manifest, llm_enrichment = extract(doc, matter_type=args.matter_type, input_source=source)
    if not result.matter_name and matter_name:
        result.matter_name = matter_name

    doc_text = "\n".join(
        str(getattr(b, "text", "") or "") for b in (getattr(doc, "blocks", []) or [])
    )[:20000]

    manifest = build_manifest(result, candidate_manifest, llm_enrichment, doc_text=doc_text)
    manifest["language_profile"] = language_profile
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
