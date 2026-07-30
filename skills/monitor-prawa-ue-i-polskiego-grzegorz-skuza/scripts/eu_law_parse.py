#!/usr/bin/env python3
"""Parse final provisions and implementation cues from legal text."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


MONTHS = {
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

FINAL_EVENT_PATTERNS: dict[str, list[str]] = {
    "entry_into_force": [
        r"\bwchodzi\s+w\s+życie\b",
        r"\bwchodzi\s+w\s+zycie\b",
        r"\bentry\s+into\s+force\b",
        r"\bshall\s+enter\s+into\s+force\b",
    ],
    "application_start": [
        r"\bstosuje\s+się\s+od\b",
        r"\bstosuje\s+sie\s+od\b",
        r"\bshall\s+apply\s+from\b",
        r"\bapplies\s+from\b",
    ],
    "transitional_provisions": [
        r"\bprzepisy\s+przejściowe\b",
        r"\bprzepisy\s+przejsciowe\b",
        r"\btransitional\s+provisions\b",
        r"\btransitional\s+arrangements\b",
    ],
    "derogation": [
        r"\bodstępstw\w*\b",
        r"\bodstepstw\w*\b",
        r"\bby\s+way\s+of\s+derogation\b",
        r"\bderogation\b",
    ],
    "repeal": [
        r"\buchyla\s+się\b",
        r"\buchyla\s+sie\b",
        r"\btraci\s+moc\b",
        r"\bshall\s+be\s+repealed\b",
        r"\brepealed\b",
    ],
    "amendment": [
        r"\bzmienia\s+się\b",
        r"\bzmienia\s+sie\b",
        r"\bis\s+amended\b",
        r"\bamended\s+as\s+follows\b",
    ],
    "commission_implementing": [
        r"\bkomisja\s+przyjmuje\b",
        r"\bkomisja\s+ustanawia\b",
        r"\bthe\s+commission\s+shall\s+adopt\b",
        r"\bcommission\s+adopts\b",
    ],
    "member_state_obligation": [
        r"\bpaństwa\s+członkowskie\s+ustanawiają\b",
        r"\bpaństwa\s+członkowskie\s+wyznaczają\b",
        r"\bpanstwa\s+czlonkowskie\s+ustanawiaja\b",
        r"\bpanstwa\s+czlonkowskie\s+wyznaczaja\b",
        r"\bmember\s+states\s+shall\s+designate\b",
        r"\bmember\s+states\s+shall\s+establish\b",
    ],
    "sanctions": [
        r"\bsankcj\w*\b",
        r"\bkara\w*\b",
        r"\bpenalt(y|ies)\b",
        r"\bsanction(s)?\b",
    ],
    "competent_authority": [
        r"\bwłaściw\w*\s+organ\w*\b",
        r"\bwlasciw\w*\s+organ\w*\b",
        r"\bcompetent\s+authorit(y|ies)\b",
    ],
    "deadline": [
        r"\bnajpóźniej\s+do\b",
        r"\bnajpozniej\s+do\b",
        r"\bdo\s+dnia\b",
        r"\bno\s+later\s+than\b",
        r"\bby\s+\d{1,2}\b",
    ],
}

ACTOR_PATTERNS: dict[str, list[str]] = {
    "commission": [r"\bkomisj\w*\b", r"\bcommission\b"],
    "member_states": [
        r"\bpaństwa\s+członkowskie\b",
        r"\bpanstwa\s+czlonkowskie\b",
        r"\bmember\s+states\b",
    ],
    "competent_authority": [
        r"\bwłaściw\w*\s+organ\w*\b",
        r"\bwlasciw\w*\s+organ\w*\b",
        r"\bcompetent\s+authorit(y|ies)\b",
    ],
    "operators": [r"\boperator\w*\b", r"\bimporter\w*\b", r"\bdeclarant\w*\b"],
}

DATE_PATTERNS = [
    r"\b\d{4}-\d{2}-\d{2}\b",
    r"\b\d{1,2}[./]\d{1,2}[./]\d{4}\b",
    r"\b\d{1,2}\s+[A-Za-ząćęłńóśźżĄĆĘŁŃÓŚŹŻ]+\s+\d{4}\b",
]

RELATIVE_TIME_PATTERNS = [
    r"\bw\s+terminie\s+\d+\s+(dni|dnia|miesięcy|miesiecy|lat)\b",
    r"\bwithin\s+\d+\s+(day|days|month|months|year|years)\b",
    r"\b\d+\s+(dni|dnia|miesięcy|miesiecy|lat)\s+od\s+dnia\b",
    r"\b\d+\s+(day|days|month|months|year|years)\s+after\b",
]

ARTICLE_RE = re.compile(r"\bart\.?\s*\d+[a-z]?\b|\barticle\s+\d+[a-z]?\b", re.IGNORECASE)
COMPILED_EVENT_PATTERNS = {
    event: [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    for event, patterns in FINAL_EVENT_PATTERNS.items()
}
COMPILED_ACTOR_PATTERNS = {
    actor: [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    for actor, patterns in ACTOR_PATTERNS.items()
}
COMPILED_DATE_PATTERNS = [re.compile(pattern, re.IGNORECASE) for pattern in DATE_PATTERNS]
COMPILED_RELATIVE_TIME_PATTERNS = [
    re.compile(pattern, re.IGNORECASE) for pattern in RELATIVE_TIME_PATTERNS
]


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


def _normalize_date(value: str) -> str | None:
    token = value.strip()

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
        month = MONTHS.get(_normalize_token(textual_match.group("month")))
        if month is None:
            return None
        try:
            return dt.date(year, month, day).isoformat()
        except ValueError:
            return None

    return None


def _extract_dates(line: str) -> tuple[list[str], list[str]]:
    dates: list[str] = []
    normalized_dates: list[str] = []

    for pattern in COMPILED_DATE_PATTERNS:
        for match in pattern.finditer(line):
            raw = match.group(0)
            dates.append(raw)
            normalized = _normalize_date(raw)
            if normalized:
                normalized_dates.append(normalized)

    return sorted(set(dates)), sorted(set(normalized_dates))


def _extract_relative_timeframes(line: str) -> list[str]:
    hits: list[str] = []
    for pattern in COMPILED_RELATIVE_TIME_PATTERNS:
        hits.extend(match.group(0) for match in pattern.finditer(line))
    return sorted(set(hits))


def _classify_events(line: str) -> tuple[list[str], dict[str, list[str]]]:
    events: list[str] = []
    evidence: dict[str, list[str]] = {}

    for event, patterns in COMPILED_EVENT_PATTERNS.items():
        matched = [pattern.pattern for pattern in patterns if pattern.search(line)]
        if matched:
            events.append(event)
            evidence[event] = matched

    return sorted(set(events)), evidence


def _extract_actors(line: str) -> list[str]:
    actors: list[str] = []
    for actor, patterns in COMPILED_ACTOR_PATTERNS.items():
        if any(pattern.search(line) for pattern in patterns):
            actors.append(actor)
    return sorted(set(actors))


def extract_final_provisions(text: str, detailed: bool = False) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    lines = text.splitlines()

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped:
            continue

        events, evidence = _classify_events(stripped)
        article_refs = sorted(set(match.strip() for match in ARTICLE_RE.findall(stripped)))
        dates, normalized_dates = _extract_dates(stripped)
        relative_timeframes = _extract_relative_timeframes(stripped)
        actors = _extract_actors(stripped)

        # Keep only legally meaningful lines with at least one structural signal.
        if not (events or article_refs or dates or relative_timeframes):
            continue

        row: dict[str, Any] = {
            "line": idx,
            "text": stripped,
            "article_refs": article_refs,
            "event_types": events,
            "actors": actors,
            "dates": dates,
            "normalized_dates": normalized_dates,
            "relative_timeframes": relative_timeframes,
        }
        if detailed:
            row["event_evidence"] = evidence

        results.append(row)

    return results


def summarize(final_provisions: list[dict[str, Any]]) -> dict[str, Any]:
    event_counter: Counter[str] = Counter()
    actor_counter: Counter[str] = Counter()

    lines_with_dates = 0
    lines_with_deadlines = 0

    for row in final_provisions:
        event_counter.update(row.get("event_types", []))
        actor_counter.update(row.get("actors", []))
        if row.get("normalized_dates"):
            lines_with_dates += 1
        if row.get("relative_timeframes") or "deadline" in row.get("event_types", []):
            lines_with_deadlines += 1

    return {
        "total_lines_matched": len(final_provisions),
        "lines_with_dates": lines_with_dates,
        "lines_with_deadlines": lines_with_deadlines,
        "event_type_counts": dict(event_counter),
        "actor_counts": dict(actor_counter),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", required=True, help="Path to legal text file")
    parser.add_argument(
        "--detailed",
        action="store_true",
        help="Include regex evidence for classified event types",
    )
    parser.add_argument(
        "--with-summary",
        action="store_true",
        help="Include aggregate summary for event and actor distribution",
    )
    args = parser.parse_args()

    text = Path(args.input_file).read_text(encoding="utf-8", errors="ignore")
    extracted = extract_final_provisions(text, detailed=args.detailed)

    payload: dict[str, Any] = {
        "final_provisions": extracted,
        "disclaimer": "Wynik pomocniczy. Potwierdź przepisy i daty w EUR-Lex/OJ oraz źródłach PL.",
    }
    if args.with_summary:
        payload["summary"] = summarize(extracted)

    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

