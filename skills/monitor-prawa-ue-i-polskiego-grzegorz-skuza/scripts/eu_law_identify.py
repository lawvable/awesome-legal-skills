#!/usr/bin/env python3
"""Identify likely EU regulation from alias, CELEX-like token, or free text."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, TypedDict


CELEX_RE = re.compile(r"\b(?:3)?(19|20)\d{2}[A-Z]\d{4}\b", re.IGNORECASE)
ACT_NUMBER_RE = re.compile(
    r"\b(?:19|20)\d{2}/\d{2,4}(?:/(?:EU|UE|WE|EC|EWG|EEC))?\b",
    re.IGNORECASE,
)
ELI_RE = re.compile(r"\b/eli/[a-z]+/\d{4}/\d+\b", re.IGNORECASE)

STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "this",
    "that",
    "regulation",
    "directive",
    "rozporzadzenie",
    "rozporządzenie",
    "dyrektywa",
    "oraz",
    "or",
    "i",
    "na",
    "w",
    "z",
    "ue",
    "eu",
}


class AliasRecord(TypedDict):
    canonical: str
    hints: list[str]


class AliasCandidate(TypedDict):
    alias: str
    canonical: str
    score: int
    reasons: list[str]
    matched_hints: list[str]


class IdentifierMatches(TypedDict):
    celex: list[str]
    act_numbers: list[str]
    eli: list[str]


def _normalize_text(value: str) -> str:
    return (
        value.lower()
        .replace("ą", "a")
        .replace("ć", "c")
        .replace("ę", "e")
        .replace("ł", "l")
        .replace("ń", "n")
        .replace("ó", "o")
        .replace("ś", "s")
        .replace("ź", "z")
        .replace("ż", "z")
    )


def _tokenize(value: str) -> set[str]:
    tokens = re.findall(r"[a-z0-9-]{3,}", _normalize_text(value))
    return {token for token in tokens if token not in STOPWORDS}


def _normalize_celex(token: str) -> str:
    upper = token.upper()
    if len(upper) == 9 and upper[0].isdigit():
        return f"3{upper}"
    return upper


def _extract_identifiers(query: str) -> IdentifierMatches:
    celex = sorted({_normalize_celex(match.group(0)) for match in CELEX_RE.finditer(query)})
    act_numbers = sorted({match.group(0).upper() for match in ACT_NUMBER_RE.finditer(query)})
    eli = sorted({match.group(0) for match in ELI_RE.finditer(query)})
    return {"celex": celex, "act_numbers": act_numbers, "eli": eli}


def parse_aliases_minimal_yaml(path: Path) -> dict[str, AliasRecord]:
    aliases: dict[str, AliasRecord] = {}
    current_key: str | None = None
    in_aliases = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line.strip() == "aliases:":
            in_aliases = True
            continue
        if not in_aliases:
            continue
        if re.match(r"^\S", line):
            break

        key_match = re.match(r"^\s{2}([a-z0-9-]+):\s*$", line)
        if key_match:
            key = key_match.group(1)
            current_key = key
            aliases[key] = {"canonical": "", "hints": []}
            continue

        if current_key is None:
            continue

        canon_match = re.match(r'^\s{4}canonical:\s*["\']?(.*?)["\']?\s*$', line)
        if canon_match:
            aliases[current_key]["canonical"] = canon_match.group(1)
            continue

        hint_match = re.match(r'^\s{6}-\s*["\']?(.*?)["\']?\s*$', line)
        if hint_match:
            aliases[current_key]["hints"].append(hint_match.group(1))

    return {key: value for key, value in aliases.items() if value["canonical"] or value["hints"]}


def _rank_aliases(query: str, aliases: dict[str, AliasRecord]) -> list[AliasCandidate]:
    query_norm = _normalize_text(query)
    query_tokens = _tokenize(query)
    candidates: list[AliasCandidate] = []

    for key, data in aliases.items():
        score = 0
        reasons: list[str] = []
        matched_hints: list[str] = []

        key_norm = _normalize_text(key)
        canonical = data.get("canonical", "")
        canonical_norm = _normalize_text(canonical)

        if key_norm and re.search(rf"\b{re.escape(key_norm)}\b", query_norm):
            score += 6
            reasons.append("alias key matched in query")

        if canonical_norm and canonical_norm in query_norm:
            score += 4
            reasons.append("canonical phrase matched")

        for hint in data.get("hints", []):
            hint_norm = _normalize_text(hint)
            if hint_norm and hint_norm in query_norm:
                score += 3
                reasons.append(f"hint matched: {hint}")
                matched_hints.append(hint)

        canonical_tokens = _tokenize(canonical)
        overlap = len(query_tokens & canonical_tokens)
        if overlap >= 2:
            score += overlap
            reasons.append(f"canonical token overlap: {overlap}")

        if score > 0:
            candidates.append(
                {
                    "alias": key,
                    "canonical": canonical,
                    "score": score,
                    "reasons": reasons,
                    "matched_hints": matched_hints,
                }
            )

    candidates.sort(
        key=lambda candidate: (candidate["score"], len(candidate["matched_hints"])),
        reverse=True,
    )
    return candidates


def identify(query: str, aliases: dict[str, AliasRecord]) -> dict[str, Any]:
    stripped_query = query.strip()
    identifiers = _extract_identifiers(stripped_query)
    candidates = _rank_aliases(stripped_query, aliases)

    if identifiers["celex"]:
        return {
            "input": query,
            "match_type": "celex",
            "primary": {"celex": identifiers["celex"][0]},
            "identifiers": identifiers,
            "candidates": candidates,
            "confidence": "high",
            "note": "CELEX detected; validate current legal status in EUR-Lex.",
        }

    if identifiers["eli"]:
        return {
            "input": query,
            "match_type": "eli",
            "primary": {"eli": identifiers["eli"][0]},
            "identifiers": identifiers,
            "candidates": candidates,
            "confidence": "high",
            "note": "ELI path detected; verify target page in official source.",
        }

    if candidates:
        top = candidates[0]
        confidence = "high" if top["score"] >= 6 else "medium"
        if identifiers["act_numbers"] and top["score"] < 6:
            confidence = "medium"
        return {
            "input": query,
            "match_type": "alias",
            "primary": top,
            "identifiers": identifiers,
            "candidates": candidates,
            "confidence": confidence,
            "note": "Alias ranking used; confirm CELEX/ELI in official sources.",
        }

    if identifiers["act_numbers"]:
        return {
            "input": query,
            "match_type": "act_number",
            "primary": {"act_number": identifiers["act_numbers"][0]},
            "identifiers": identifiers,
            "candidates": [],
            "confidence": "medium",
            "note": "Act number detected; resolve to CELEX/ELI in EUR-Lex.",
        }

    return {
        "input": query,
        "match_type": "topic",
        "primary": None,
        "identifiers": identifiers,
        "candidates": [],
        "confidence": "low",
        "note": "No structured identifier or alias match found. Use EUR-Lex topic search.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True, help="Alias/CELEX/act number/topic")
    parser.add_argument("--aliases", required=True, help="Path to regulation-aliases.yaml")
    args = parser.parse_args()

    aliases = parse_aliases_minimal_yaml(Path(args.aliases))
    print(json.dumps(identify(args.query, aliases), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

