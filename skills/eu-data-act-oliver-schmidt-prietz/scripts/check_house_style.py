#!/usr/bin/env python3
"""House-style linter for the EU Data Act skill.

Scans target files for violations of the discipline codified in
`references/method/house-style.md`. Exits non-zero if any violation
is found.

Usage:
    python3 scripts/check_house_style.py [PATH ...]

If no paths are given, the linter scans `references/scenarios/`,
`templates/`, and `templates/_drafter-notes/` by default. Source files
under `sources/`, gate files, the method files, and the gotchas
catalogue are excluded from the linter, since they intentionally
contain quotations from the regulation (which may legitimately use
banned phrases in the regulator's voice) and metalinguistic mention
of banned terms.

Run with `--verbose` to show passing files too. Run with
`--report-only` to suppress the non-zero exit (useful for CI builds
that want a soft report without failing).
"""

import argparse
import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent

# Default paths to lint. Each entry is either a directory (recursed) or a glob.
DEFAULT_TARGETS = [
    SKILL_ROOT / "references" / "scenarios",
    SKILL_ROOT / "templates",
]

# Files to skip even if they match the default targets.
SKIP_PATHS = {
    # No exclusions today; reserved.
}

# Banned patterns. Each entry: (pattern, label, severity).
# Severity is informational only; any hit fails the run.
RULES = [
    # Em dash (U+2014). Use commas, parens, colons, or periods.
    (re.compile(r"—"), "em dash", "form"),
    # AI-tic connectors.
    (re.compile(r"\b(Furthermore|Moreover|Indeed|It should be noted|It is worth noting|It is important to note|Notably|Importantly)\b"), "banned connector", "voice"),
    # Conclusory padding.
    (re.compile(r"\b(In conclusion|In summary|To summarise|To summarize|All things considered|Ultimately)\b"), "conclusory padding", "voice"),
    # Preamble openings.
    (re.compile(r"\b(Let me walk you through|I'd be happy to help|Great question|Here is an analysis of|This is a complex area but)\b", re.IGNORECASE), "preamble", "voice"),
    # Marketing language.
    (re.compile(r"\b(best-in-class|cutting-edge|thought leadership|value proposition)\b", re.IGNORECASE), "marketing language", "voice"),
    # "leverage" as a verb (heuristic: followed by an article, pronoun, or noun start).
    (re.compile(r"\bleverage\s+(the|a|an|our|its|their|your|this|these|those|[A-Z])"), "marketing language: 'leverage' as verb", "voice"),
    # "actionable" anywhere.
    (re.compile(r"\bactionable\b", re.IGNORECASE), "marketing language: 'actionable'", "voice"),
    # "robust" (banned). Word boundary; allow "robustness" and quoted "robust" to slip — but the house style says "Banned: 'robust'" without qualification, so flag bare "robust" only.
    (re.compile(r"\brobust\b"), "marketing language: 'robust'", "voice"),
    # Exclamation marks (excluding URLs).
    (re.compile(r"!"), "exclamation mark", "form"),
]

# Allow-list: lines containing any of these phrases are skipped (they are
# meta-references to the rules themselves, not actual violations).
META_PATTERNS = [
    re.compile(r"banned"),
    re.compile(r"forbidden"),
    re.compile(r"em dash"),
    re.compile(r"em-dash"),
    re.compile(r"AI tics"),
    re.compile(r"house[- ]style"),
    re.compile(r"NO\s+em dashes", re.IGNORECASE),
    re.compile(r"NO\s+banned", re.IGNORECASE),
    re.compile(r"BLOCKING", re.IGNORECASE),
    re.compile(r'"Furthermore"'),
    re.compile(r'"Moreover"'),
    re.compile(r'"Indeed"'),
    re.compile(r'"It should be noted"'),
    re.compile(r"actionable.*deliverable"),
]


def is_meta_line(line: str) -> bool:
    """Return True if a line is metalinguistic and should not trigger rules.

    Lines that quote or mention the banned phrases as part of describing
    house style or grading rubric should not themselves trigger the
    linter. The meta-line heuristic is conservative: short markdown
    lists or quoted phrases referring to the rules are exempt; prose
    that uses the banned phrase outside such a context is not.
    """
    return any(p.search(line) for p in META_PATTERNS)


def iter_files(paths):
    """Yield Path objects for every text file under the given paths.

    Markdown, Python, and JSON files are linted; other extensions are
    skipped. Directories are recursed.
    """
    extensions = {".md", ".py", ".json"}
    seen = set()
    for raw in paths:
        path = Path(raw).resolve()
        if path in SKIP_PATHS or not path.exists():
            continue
        if path.is_file():
            if path.suffix in extensions and path not in seen:
                seen.add(path)
                yield path
        else:
            for sub in sorted(path.rglob("*")):
                if sub.is_file() and sub.suffix in extensions and sub not in seen:
                    seen.add(sub)
                    yield sub


def lint_file(path: Path):
    """Return a list of (line_number, label, match_text) for the file."""
    findings = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return findings
    for lineno, line in enumerate(text.splitlines(), 1):
        if is_meta_line(line):
            continue
        for pattern, label, _severity in RULES:
            for m in pattern.finditer(line):
                findings.append((lineno, label, m.group(0)))
    return findings


def main(argv):
    parser = argparse.ArgumentParser(description="Lint EU Data Act skill files for house-style violations.")
    parser.add_argument("paths", nargs="*", help="Files or directories to lint. Defaults to references/scenarios/ and templates/.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show passing files too.")
    parser.add_argument("--report-only", action="store_true", help="Exit 0 even if violations are found.")
    args = parser.parse_args(argv)

    targets = [Path(p) for p in args.paths] if args.paths else DEFAULT_TARGETS
    total_findings = 0
    files_scanned = 0
    files_with_findings = 0

    for path in iter_files(targets):
        files_scanned += 1
        findings = lint_file(path)
        if findings:
            files_with_findings += 1
            total_findings += len(findings)
            rel = path.relative_to(SKILL_ROOT) if SKILL_ROOT in path.parents or path == SKILL_ROOT else path
            print(f"[FAIL] {rel}")
            for lineno, label, match in findings:
                print(f"  L{lineno}  {label}: {match!r}")
        elif args.verbose:
            rel = path.relative_to(SKILL_ROOT) if SKILL_ROOT in path.parents or path == SKILL_ROOT else path
            print(f"[OK]   {rel}")

    print(f"\nSummary: {files_scanned} files scanned, {files_with_findings} files with findings, {total_findings} violations total.")

    if total_findings and not args.report_only:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
