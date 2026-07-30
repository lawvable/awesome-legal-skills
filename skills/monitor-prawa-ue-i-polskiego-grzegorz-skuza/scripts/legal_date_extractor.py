#!/usr/bin/env python3
"""Extract legal dates, timeline phrases and obligations from plain text."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


MONTHS = {
    # Polish
    "stycznia": 1,
    "styczen": 1,
    "lutego": 2,
    "luty": 2,
    "marca": 3,
    "marzec": 3,
    "kwietnia": 4,
    "kwiecien": 4,
    "maja": 5,
    "maj": 5,
    "czerwca": 6,
    "czerwiec": 6,
    "lipca": 7,
    "lipiec": 7,
    "sierpnia": 8,
    "sierpien": 8,
    "wrzesnia": 9,
    "wrzesien": 9,
    "pazdziernika": 10,
    "pazdziernik": 10,
    "listopada": 11,
    "listopad": 11,
    "grudnia": 12,
    "grudzien": 12,
    # English
    "january": 1,
    "jan": 1,
    "february": 2,
    "feb": 2,
    "march": 3,
    "mar": 3,
    "april": 4,
    "apr": 4,
    "may": 5,
    "june": 6,
    "jun": 6,
    "july": 7,
    "jul": 7,
    "august": 8,
    "aug": 8,
    "september": 9,
    "sep": 9,
    "october": 10,
    "oct": 10,
    "november": 11,
    "nov": 11,
    "december": 12,
    "dec": 12,
}

DATE_PATTERNS = [
    r"\b\d{4}-\d{2}-\d{2}\b",
    r"\b\d{1,2}[./]\d{1,2}[./]\d{4}\b",
    r"\b\d{1,2}\s+[A-Za-ząćęłńóśźżĄĆĘŁŃÓŚŹŻ]+\s+\d{4}\b",
]

RELATIVE_TIME_PATTERNS = [
    r"\bw\s+terminie\s+\d+\s+(dni|dnia|miesięcy|miesiąc(y|e)?|lat)\b",
    r"\bw\s+terminie\s+\d+\s+(dni|dnia|miesiecy|miesiac(y|e)?|lat)\b",
    r"\bwithin\s+\d+\s+(day|days|month|months|year|years)\b",
    r"\b\d+\s+(dni|dnia|miesięcy|miesiąc(y|e)?|lat)\s+od\s+dnia\b",
    r"\b\d+\s+(dni|dnia|miesiecy|miesiac(y|e)?|lat)\s+od\s+dnia\b",
    r"\b\d+\s+(day|days|month|months|year|years)\s+after\b",
    r"\bz\s+dniem\s+następującym\s+po\s+dniu\s+publikacji\b",
    r"\bz\s+dniem\s+nastepujacym\s+po\s+dniu\s+publikacji\b",
    r"\bon\s+the\s+day\s+following\s+publication\b",
]

LEGAL_EVENT_PATTERNS: dict[str, list[str]] = {
    "entry_into_force": [
        r"\bwchodzi\s+w\s+życie\b",
        r"\bwchodzi\s+w\s+zycie\b",
        r"\bentry\s+into\s+force\b",
        r"\bshall\s+enter\s+into\s+force\b",
    ],
    "application_start": [
        r"\bstosuje\s+się\s+od\b",
        r"\bma\s+zastosowanie\s+od\b",
        r"\bshall\s+apply\s+from\b",
        r"\bapplies\s+from\b",
    ],
    "application_end": [
        r"\bstosuje\s+się\s+do\b",
        r"\bobowiązuje\s+do\b",
        r"\bshall\s+apply\s+until\b",
        r"\bapply\s+until\b",
    ],
    "deadline_general": [
        r"\bnajpóźniej\s+do\b",
        r"\bdo\s+dnia\b",
        r"\bno\s+later\s+than\b",
        r"\bby\s+\d{1,2}\b",
    ],
    "transposition_deadline": [
        r"\bpaństwa\s+członkowskie\s+przyjm\w+\b",
        r"\bpanstwa\s+czlonkowskie\s+przyjm\w+\b",
        r"\btranspozycj\w*\b",
        r"\bmember\s+states\s+shall\s+adopt\b",
        r"\bshall\s+transpose\b",
    ],
    "repeal_effective": [
        r"\btraci\s+moc\s+z\s+dniem\b",
        r"\buchyla\s+się\s+z\s+dniem\b",
        r"\bshall\s+be\s+repealed\s+with\s+effect\s+from\b",
        r"\brepealed\s+from\b",
    ],
    "review_clause": [
        r"\bkomisja\s+dokonuje\s+przeglądu\b",
        r"\bprzegląd\s+niniejszego\s+rozporządzenia\b",
        r"\bcommission\s+shall\s+review\b",
        r"\breview\s+this\s+regulation\b",
    ],
    "reporting_deadline": [
        r"\bprzedkłada\s+sprawozdanie\b",
        r"\bsprawozdanie\s+do\b",
        r"\bshall\s+submit\s+a\s+report\b",
        r"\bsubmit\s+their\s+reports?\b",
    ],
    "publication_reference": [
        r"\bdzienniku\s+urzędowym\s+unii\s+europejskiej\b",
        r"\bopublikowan\w*\b",
        r"\bofficial\s+journal\s+of\s+the\s+european\s+union\b",
        r"\bpublished\s+in\s+the\s+official\s+journal\b",
    ],
}

COMPILED_DATE_PATTERNS = [re.compile(p, re.IGNORECASE) for p in DATE_PATTERNS]
COMPILED_RELATIVE_TIME_PATTERNS = [
    re.compile(p, re.IGNORECASE) for p in RELATIVE_TIME_PATTERNS
]
COMPILED_LEGAL_EVENT_PATTERNS = {
    event: [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    for event, patterns in LEGAL_EVENT_PATTERNS.items()
}


def _normalize_token(token: str) -> str:
    return (
        token.lower()
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


def _normalize_date(date_str: str) -> str | None:
    token = date_str.strip()

    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", token):
        try:
            return dt.date.fromisoformat(token).isoformat()
        except ValueError:
            return None

    if re.fullmatch(r"\d{1,2}[./]\d{1,2}[./]\d{4}", token):
        delimiter = "." if "." in token else "/"
        day_s, month_s, year_s = token.split(delimiter)
        try:
            return dt.date(int(year_s), int(month_s), int(day_s)).isoformat()
        except ValueError:
            return None

    textual_match = re.fullmatch(
        r"(?P<day>\d{1,2})\s+(?P<month>[A-Za-ząćęłńóśźżĄĆĘŁŃÓŚŹŻ]+)\s+(?P<year>\d{4})",
        token,
    )
    if textual_match:
        day = int(textual_match.group("day"))
        year = int(textual_match.group("year"))
        month_token = _normalize_token(textual_match.group("month"))
        month = MONTHS.get(month_token)
        if month is None:
            return None
        try:
            return dt.date(year, month, day).isoformat()
        except ValueError:
            return None

    return None


def _extract_dates(line: str) -> tuple[list[str], list[str]]:
    raw_dates: list[str] = []
    normalized_dates: list[str] = []

    for pattern in COMPILED_DATE_PATTERNS:
        for match in pattern.finditer(line):
            raw = match.group(0)
            raw_dates.append(raw)
            normalized = _normalize_date(raw)
            if normalized:
                normalized_dates.append(normalized)

    return sorted(set(raw_dates)), sorted(set(normalized_dates))


def _extract_relative_timeframes(line: str) -> list[str]:
    hits: list[str] = []
    for pattern in COMPILED_RELATIVE_TIME_PATTERNS:
        hits.extend(match.group(0) for match in pattern.finditer(line))
    return sorted(set(hits))


def _classify_legal_events(line: str) -> tuple[list[str], dict[str, list[str]]]:
    events: list[str] = []
    evidence: dict[str, list[str]] = {}

    for event_type, patterns in COMPILED_LEGAL_EVENT_PATTERNS.items():
        matched_patterns = [p.pattern for p in patterns if p.search(line)]
        if matched_patterns:
            events.append(event_type)
            evidence[event_type] = matched_patterns

    return events, evidence


def extract(text: str, detailed: bool = False) -> list[dict[str, Any]]:
    lines = text.splitlines()
    results: list[dict[str, Any]] = []

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped:
            continue

        dates, normalized_dates = _extract_dates(stripped)
        relative_timeframes = _extract_relative_timeframes(stripped)
        event_types, event_evidence = _classify_legal_events(stripped)

        if not event_types and not dates and not relative_timeframes:
            continue

        row: dict[str, Any] = {
            "line": i,
            "text": stripped,
            "dates": dates,
            "normalized_dates": normalized_dates,
            "relative_timeframes": relative_timeframes,
            "event_types": sorted(set(event_types)),
        }
        if detailed:
            row["event_evidence"] = event_evidence
        results.append(row)

    return results


def summarize(matches: list[dict[str, Any]]) -> dict[str, Any]:
    event_counter: Counter[str] = Counter()
    relative_counter = 0
    dated_counter = 0

    for row in matches:
        event_counter.update(row.get("event_types", []))
        if row.get("relative_timeframes"):
            relative_counter += 1
        if row.get("normalized_dates"):
            dated_counter += 1

    return {
        "total_matches": len(matches),
        "lines_with_dates": dated_counter,
        "lines_with_relative_timeframes": relative_counter,
        "event_type_counts": dict(event_counter),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", required=True, help="Path to plain text file")
    parser.add_argument(
        "--detailed",
        action="store_true",
        help="Include regex evidence for legal event classification",
    )
    parser.add_argument(
        "--with-summary",
        action="store_true",
        help="Include aggregated summary of detected event types",
    )
    args = parser.parse_args()

    text = Path(args.input_file).read_text(encoding="utf-8", errors="ignore")
    matches = extract(text, detailed=args.detailed)

    payload: dict[str, Any] = {"matches": matches}
    if args.with_summary:
        payload["summary"] = summarize(matches)

    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

