#!/usr/bin/env python3
"""Classify legal relation snippets from plain text lines."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


RELATION_PATTERNS = {
    "repeals": [
        r"\buchyla\s+się\b",
        r"\btraci\s+moc\b",
        r"\buchyla\b",
        r"\brepeal(s|ed)?\b",
        r"\bshall\s+be\s+repealed\b",
    ],
    "amends": [
        r"\bzmienia\s+się\b",
        r"\bw\s+art\.[^\n]{0,80}\botrzymuje\s+brzmienie\b",
        r"\bamend(s|ed|ment)?\b",
        r"\bis\s+amended\b",
    ],
    "supplements": [
        r"\buzupełnia\b",
        r"\bdodaje\s+się\b",
        r"\bsupplement(s|ed)?\b",
        r"\badd(s|ed)?\b",
    ],
    "implements": [
        r"\bwykonawcz\w*\b",
        r"\bwdraża\b",
        r"\bimplement(ing|s|ed)?\b",
        r"\bimplementation\s+of\b",
    ],
    "corrigendum": [
        r"\bsprostowanie\b",
        r"\bcorrigendum\b",
        r"\brectification\b",
    ],
    "consolidated_version": [
        r"\bwersja\s+skonsolidowana\b",
        r"\btekst\s+jednolity\b",
        r"\bconsolidated\s+version\b",
        r"\bcodified\s+version\b",
    ],
    "procedure": [
        r"\bprocedur\w*\b",
        r"\btryb\s+ustawodawczy\b",
        r"\blegislative\s+procedure\b",
        r"\bcomitology\b",
    ],
    "national_adaptation": [
        r"\bdostosow\w*\b",
        r"\bprzepisy\s+krajowe\b",
        r"\bnational\s+adaptation\b",
        r"\btransposition\b",
    ],
    "national_sanctions": [
        r"\bsankcj\w*\b",
        r"\bkara\w*\b",
        r"\bpenalt(y|ies)\b",
        r"\bsanction(s)?\b",
    ],
    "competent_authority": [
        r"\bwłaściw\w*\s+organ\w*\b",
        r"\bwlasciw\w*\s+organ\w*\b",
        r"\borgan\s+właściwy\b",
        r"\borgan\s+wlasciwy\b",
        r"\bcompetent\s+authorit(y|ies)\b",
    ],
}

COMPILED_RELATION_PATTERNS = {
    relation: [re.compile(pattern, flags=re.IGNORECASE) for pattern in patterns]
    for relation, patterns in RELATION_PATTERNS.items()
}


def classify_line(line: str) -> list[str]:
    found = []
    for relation, patterns in COMPILED_RELATION_PATTERNS.items():
        if any(pattern.search(line) for pattern in patterns):
            found.append(relation)
    return found


def explain_line(line: str) -> dict[str, list[str]]:
    evidence: dict[str, list[str]] = {}
    for relation, patterns in COMPILED_RELATION_PATTERNS.items():
        hits = [pattern.pattern for pattern in patterns if pattern.search(line)]
        if hits:
            evidence[relation] = hits
    return evidence


def extract(text: str, detailed: bool = False) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for index, line in enumerate(text.splitlines(), start=1):
        stripped_line = line.strip()
        if not stripped_line:
            continue
        relations = classify_line(stripped_line)
        if relations:
            row: dict[str, Any] = {
                "line": index,
                "relations": relations,
                "text": stripped_line,
            }
            if detailed:
                row["evidence"] = explain_line(stripped_line)
            out.append(row)
    return out


def summarize(relations_output: list[dict[str, Any]]) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for row in relations_output:
        counter.update(row["relations"])
    return dict(counter)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", required=True, help="Path to plain text file")
    parser.add_argument(
        "--detailed",
        action="store_true",
        help="Include evidence showing which regex patterns matched each line",
    )
    parser.add_argument(
        "--with-summary",
        action="store_true",
        help="Include count of each relation type",
    )
    args = parser.parse_args()

    text = Path(args.input_file).read_text(encoding="utf-8", errors="ignore")
    extracted = extract(text, detailed=args.detailed)

    payload: dict[str, Any] = {"relations": extracted}
    if args.with_summary:
        payload["summary"] = summarize(extracted)

    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

