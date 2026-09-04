#!/usr/bin/env python3
"""Detect likely verbatim confidential-fact leakage across mediation packets."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.casefold()).strip()


def load_text(path: Path | None) -> str:
    return normalize(path.read_text(encoding="utf-8")) if path else ""


def appears(fact: str, document: str) -> bool:
    needle = normalize(fact)
    if len(needle) < 30 or len(needle.split()) < 6:
        return False
    return needle in document


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    parser.add_argument("general", type=Path)
    parser.add_argument("--party-a", type=Path)
    parser.add_argument("--party-b", type=Path)
    args = parser.parse_args()

    model = json.loads(args.model.read_text(encoding="utf-8"))
    party_ids = [party["id"] for party in model.get("parties", [])]
    if len(party_ids) != 2:
        parser.error("case model must contain exactly two parties")
    documents = {
        "public": load_text(args.general),
        party_ids[0]: load_text(args.party_a),
        party_ids[1]: load_text(args.party_b),
    }
    findings: list[str] = []
    for fact in model.get("facts", []):
        visibility = fact.get("visibility")
        text = fact.get("text", "")
        fact_id = fact.get("id", "unknown")
        if visibility == "author_only":
            forbidden = list(documents)
        elif isinstance(visibility, str) and visibility.startswith("party:"):
            permitted = visibility.split(":", 1)[1]
            forbidden = [name for name in documents if name != permitted]
        elif visibility == "shared_private":
            forbidden = ["public"]
        else:
            continue
        for destination in forbidden:
            document = documents[destination]
            if document and appears(text, document):
                findings.append(f"{fact_id} ({visibility}) appears verbatim in {destination}")
    for finding in findings:
        print(f"POSSIBLE LEAK: {finding}")
    print(f"Information-firewall check complete: {len(findings)} possible leak(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
