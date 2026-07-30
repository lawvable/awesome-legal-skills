#!/usr/bin/env python3
"""
Skill Security Auditor — main CLI entry point.

Walks a skill directory (or fetches a git URL) and runs every
registered scanner against it, then emits a structured report.

Usage:
    audit.py PATH [--strict] [--json|--markdown|--html|--text]
                   [--output FILE] [--baseline FILE]
                   [--skill SUBDIR] [--cleanup]
                   [--severity-floor LEVEL]

Exit codes:
    0 — PASS  (no blocking findings)
    1 — FAIL  (CRITICAL findings, or HIGH in --strict)
    2 — WARN  (HIGH findings or many MEDIUMs, non-strict mode)
    3 — usage / I/O error

The exit code is what CI uses to decide whether to merge or block;
a wrapper script can collapse 2 → 0 if you only want to gate on
hard failures.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# When invoked directly as a script the scripts/ directory may not be
# on sys.path. Add it ourselves so `python audit.py` works as well as
# `python -m audit`.
_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

import reporter  # noqa: E402, SEC-AUDITOR
import scanners  # noqa: E402, SEC-AUDITOR
from core import (  # noqa: E402, SEC-AUDITOR
    SEVERITY_FROM_NAME,
    AuditReport,
    Finding,
    Severity,
    file_kind,
    iter_files,
)


SCANNER_VERSION = "1.0.0"


# =============================================================================
# GIT SUPPORT
# =============================================================================
# Skills are often distributed as git repos. We optionally clone the
# repo into a temporary directory, audit it, and clean up. The clone
# is shallow because we only need a snapshot.

_GIT_URL_RE = re.compile(
    r"^(https?://|git@|ssh://|git\+https?://|git://)"
)


def is_git_url(s: str) -> bool:
    """True if the argument looks like a git URL rather than a path."""
    return bool(_GIT_URL_RE.match(s))


def clone_repo(url: str, dest: Path) -> Path:
    """
    Shallow-clone `url` into `dest`. Returns the clone directory.

    Uses --depth 1 to keep network usage low; we only audit the
    current state of the repo. Stderr is captured so a clone failure
    produces a clear message rather than a wall of git output.
    """
    cmd = ["git", "clone", "--depth", "1", "--quiet", "--no-tags", url, str(dest)]
    try:
        subprocess.run(  # noqa: SEC-AUDITOR
            cmd, check=True, capture_output=True, text=True, timeout=180
        )
    except subprocess.CalledProcessError as e:
        stderr = (e.stderr or "").strip()
        raise RuntimeError(f"git clone failed: {stderr or e}") from e
    except subprocess.TimeoutExpired as e:
        raise RuntimeError(f"git clone timed out after 180s: {e}") from e
    except FileNotFoundError as e:
        raise RuntimeError("git executable not found on PATH") from e
    return dest


# =============================================================================
# BASELINE SUPPRESSION
# =============================================================================
# A baseline file lists fingerprints of findings that have been
# manually reviewed and accepted. Subsequent runs filter those
# findings out, so reviewers only see new/changed issues.

def load_baseline(path: Path) -> set[str]:
    """
    Parse the baseline file and return the set of accepted
    fingerprints. Supports a simple subset of YAML so we don't need
    a YAML dependency at runtime — the on-disk format is:

        suppressions:
          - fingerprint: abcdef0123456789
            reason: reviewed by alice 2025-01-15
          - fingerprint: 1234567890abcdef
            ...

    Lines that don't match the expected shape are skipped silently.
    A JSON file (e.g. {"fingerprints": [...]}) is also accepted.
    """
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8", errors="replace")
    # Try JSON first — strict and unambiguous
    try:
        data = json.loads(text)
        if isinstance(data, dict) and "fingerprints" in data:
            return {str(x) for x in data["fingerprints"]}
        if isinstance(data, list):
            return {str(x) for x in data}
    except json.JSONDecodeError:
        pass
    # Fall back to mini-YAML parsing
    fingerprints: set[str] = set()
    fp_re = re.compile(r"^\s*-?\s*fingerprint:\s*['\"]?([0-9a-fA-F]+)['\"]?\s*$")
    for line in text.splitlines():
        m = fp_re.match(line)
        if m:
            fingerprints.add(m.group(1).lower())
    return fingerprints


def apply_baseline(report: AuditReport, baseline: set[str]) -> int:
    """
    Drop findings whose fingerprint is in the baseline. Returns the
    number of findings filtered out.
    """
    if not baseline:
        return 0
    kept: list[Finding] = []
    dropped = 0
    for f in report.findings:
        if f.fingerprint() in baseline:
            dropped += 1
            continue
        kept.append(f)
    report.findings = kept
    return dropped


# =============================================================================
# SEVERITY FLOOR
# =============================================================================

def apply_severity_floor(report: AuditReport, floor: Severity) -> int:
    """Drop findings below the given severity. Returns drop count."""
    before = len(report.findings)
    report.findings = [f for f in report.findings if f.severity >= floor]
    return before - len(report.findings)


# =============================================================================
# FILE COUNTING
# =============================================================================
# Done up-front so the report has accurate coverage stats even if a
# scanner short-circuits.

def count_files(skill_root: Path, report: AuditReport) -> None:
    """Populate the file-count fields on the report."""
    total = code = md = wf = dep = 0
    for path in iter_files(skill_root):
        total += 1
        k = file_kind(path)
        if k == "code":
            code += 1
        elif k == "markdown":
            md += 1
        elif k == "workflow":
            wf += 1
        elif k == "dep":
            dep += 1
    report.files_total = total
    report.code_files = code
    report.markdown_files = md
    report.workflow_files = wf
    report.dep_files = dep


# =============================================================================
# ORCHESTRATION
# =============================================================================

def run_audit(skill_root: Path, *, strict: bool = False) -> AuditReport:
    """
    Execute every scanner against `skill_root` and return the
    aggregated report. The scanners are deliberately ordered from
    cheapest (structure) to most thorough (code) so a malformed skill
    surfaces a clear error first.
    """
    skill_name = skill_root.name or "skill"
    report = AuditReport(
        skill_name=skill_name,
        skill_path=str(skill_root.resolve()),
        strict=strict,
        started_at=dt.datetime.now(dt.timezone.utc).isoformat(),
        scanner_versions={"auditor": SCANNER_VERSION},
    )
    count_files(skill_root, report)
    scanners.scan_structure(skill_root, report)
    scanners.scan_filesystem(skill_root, report)
    scanners.scan_supply_chain(skill_root, report)
    scanners.scan_workflows(skill_root, report)
    scanners.scan_prompts(skill_root, report)
    scanners.scan_code(skill_root, report)
    report.finished_at = dt.datetime.now(dt.timezone.utc).isoformat()
    return report


# =============================================================================
# CLI
# =============================================================================

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="audit.py",
        description="Audit an AI agent skill for malicious patterns before installing it.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  audit.py ./my-skill\n"
            "  audit.py https://github.com/user/skill.git --strict\n"
            "  audit.py ./skill --json --output report.json\n"
            "  audit.py ./skill --markdown --output review.md\n"
            "  audit.py ./skill --baseline baseline.yml\n"
            "\n"
            "Exit codes: 0=PASS, 1=FAIL, 2=WARN, 3=error.\n"
        ),
    )
    p.add_argument(
        "path",
        help="Path to a skill directory, or a git URL to clone and audit.",
    )
    p.add_argument(
        "--skill",
        default=None,
        help="Subdirectory inside the path or repo containing the skill "
             "(useful when a repo holds multiple skills).",
    )
    p.add_argument(
        "--strict",
        action="store_true",
        help="Treat HIGH findings as blocking (PASS only if no HIGH or CRITICAL).",
    )

    # Output format flags. The text report is the default; passing a
    # format flag switches the *primary* output. --output redirects
    # the primary output to a file; in that case the text summary is
    # still printed to stdout so the user knows what happened.
    fmt = p.add_argument_group("output format (default: text)")
    fmt.add_argument("--json", action="store_true", help="Emit JSON report.")
    fmt.add_argument("--markdown", action="store_true", help="Emit Markdown report.")
    fmt.add_argument("--html", action="store_true", help="Emit HTML report.")
    fmt.add_argument(
        "--output", "-o",
        default=None,
        help="Write report to FILE instead of stdout. With --json/--markdown/--html, "
             "writes that format; otherwise writes the text report.",
    )

    p.add_argument(
        "--baseline",
        default=None,
        help="Path to a baseline file (.yml or .json) listing accepted finding fingerprints.",
    )
    p.add_argument(
        "--severity-floor",
        choices=["LOW", "MEDIUM", "HIGH", "CRITICAL"],
        default="LOW",
        help="Suppress findings below this severity (default: LOW = show everything).",
    )
    p.add_argument(
        "--cleanup",
        action="store_true",
        help="Delete the cloned repo after auditing (when path is a git URL).",
    )
    p.add_argument(
        "--no-color",
        action="store_true",
        help="Disable ANSI color in the text report.",
    )
    p.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Only print the verdict line (still uses normal exit codes).",
    )
    return p


def _picked_format(args: argparse.Namespace) -> str:
    """Resolve the primary output format from CLI flags. Default is text."""
    chosen = [name for name in ("json", "markdown", "html") if getattr(args, name)]  # noqa: SEC-AUDITOR argparse namespace dispatch
    if len(chosen) > 1:
        raise SystemExit(f"error: choose at most one of --json/--markdown/--html (got: {chosen})")
    return chosen[0] if chosen else "text"


def _render(report: AuditReport, fmt: str, *, color_stream=None) -> str:
    if fmt == "json":
        return reporter.format_json(report)
    if fmt == "markdown":
        return reporter.format_markdown(report)
    if fmt == "html":
        return reporter.format_html(report)
    return reporter.format_text(report, stream=color_stream)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.no_color:
        # Honor explicit user opt-out by setting the env var the
        # reporter already checks. Avoids passing a flag through.
        import os
        os.environ["NO_COLOR"] = "1"

    # --------- Resolve skill_root ---------
    cleanup_dir: Path | None = None
    raw = args.path
    try:
        if is_git_url(raw):
            tmp = Path(tempfile.mkdtemp(prefix="skill-audit-"))
            try:
                clone_repo(raw, tmp)
            except RuntimeError as e:
                shutil.rmtree(tmp, ignore_errors=True)  # noqa: SEC-AUDITOR cleanup of own temp dir
                print(f"error: {e}", file=sys.stderr)
                return 3
            cleanup_dir = tmp if args.cleanup else None
            skill_root = tmp
        else:
            skill_root = Path(raw)

        if args.skill:
            skill_root = skill_root / args.skill

        if not skill_root.exists():
            print(f"error: path does not exist: {skill_root}", file=sys.stderr)
            return 3
        if not skill_root.is_dir():
            print(f"error: not a directory: {skill_root}", file=sys.stderr)
            return 3

        # --------- Run scanners ---------
        report = run_audit(skill_root, strict=args.strict)

        # --------- Baseline filter ---------
        if args.baseline:
            baseline_path = Path(args.baseline)
            try:
                baseline = load_baseline(baseline_path)
            except OSError as e:
                print(f"error: cannot read baseline {baseline_path}: {e}", file=sys.stderr)
                return 3
            dropped = apply_baseline(report, baseline)
            if dropped and not args.quiet:
                print(f"# baseline: suppressed {dropped} finding(s) by fingerprint", file=sys.stderr)

        # --------- Severity floor ---------
        floor = SEVERITY_FROM_NAME[args.severity_floor]
        if floor > Severity.LOW:
            dropped = apply_severity_floor(report, floor)
            if dropped and not args.quiet:
                print(f"# severity-floor: hid {dropped} finding(s) below {args.severity_floor}", file=sys.stderr)

        # --------- Render ---------
        fmt = _picked_format(args)
        if args.output:
            out_path = Path(args.output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_text = _render(report, fmt)
            out_path.write_text(out_text, encoding="utf-8")
            if not args.quiet:
                summary = reporter.format_text(report, stream=sys.stdout)
                print(summary)
                print(f"\n# report written to {out_path}")
        else:
            text = _render(report, fmt, color_stream=sys.stdout)
            if args.quiet and fmt == "text":
                # Just the verdict line
                print(f"{report.verdict}: {report.verdict_explanation}")
            else:
                print(text)

        # --------- Exit code ---------
        v = report.verdict
        if v == "FAIL":
            return 1
        if v == "WARN":
            return 2
        return 0
    finally:
        if cleanup_dir:
            shutil.rmtree(cleanup_dir, ignore_errors=True)  # noqa: SEC-AUDITOR cleanup of own temp dir


if __name__ == "__main__":
    raise SystemExit(main())
