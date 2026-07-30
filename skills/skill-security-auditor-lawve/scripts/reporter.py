"""
Output formatters for the Skill Security Auditor.

Every formatter consumes an AuditReport and produces a string. The
CLI picks one or more based on --json / --markdown / --html flags;
the default is the human-readable text report.

Design notes:
- Findings are grouped first by severity (worst → best), then by
  file within each severity bucket. That matches how reviewers
  actually read these reports: triage the critical stuff, then
  walk file-by-file.
- Color is gated by stdout being a TTY so piping into a file or CI
  log doesn't litter the output with ANSI escapes.
- The HTML report is self-contained (no external CSS/JS) so it can
  be attached to a PR review or emailed without breaking.
"""

from __future__ import annotations

import html
import json
import os
import sys
from collections import defaultdict
from typing import TextIO

from core import (  # noqa: SEC-AUDITOR
    SEVERITY_BADGE,
    SEVERITY_NAME,
    AuditReport,
    Finding,
    Severity,
)


# =============================================================================
# COLOR HELPERS
# =============================================================================
# ANSI escapes for the text report. Only enabled on TTY stdout — when
# the report is captured to a file or piped to CI logs, colors would
# show up as literal escape sequences and clutter the output.

_ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "red": "\033[31m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "cyan": "\033[36m",
    "green": "\033[32m",
    "white": "\033[37m",
    "grey": "\033[90m",
}

_SEV_COLOR = {
    Severity.CRITICAL: "red",
    Severity.HIGH: "yellow",
    Severity.MEDIUM: "blue",
    Severity.LOW: "grey",
}


def _use_color(stream: TextIO) -> bool:
    """Color only when writing to an interactive terminal. CI envs
    that set NO_COLOR (the de facto standard) opt out unconditionally."""
    if os.environ.get("NO_COLOR"):
        return False
    return hasattr(stream, "isatty") and stream.isatty()


def _c(text: str, color: str, use_color: bool) -> str:
    if not use_color:
        return text
    return f"{_ANSI[color]}{text}{_ANSI['reset']}"


# =============================================================================
# GROUPING
# =============================================================================

def _group_findings(report: AuditReport) -> dict[Severity, dict[str, list[Finding]]]:
    """
    Bucket findings by severity then by file. Order within each file
    is line-number ascending so reports read top-to-bottom like the
    source they describe.
    """
    out: dict[Severity, dict[str, list[Finding]]] = {
        s: defaultdict(list) for s in (Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW)
    }
    for f in report.findings:
        out[f.severity][f.file].append(f)
    for sev in out:
        for file in out[sev]:
            out[sev][file].sort(key=lambda f: (f.line, f.category))
    return out


# =============================================================================
# TEXT REPORT
# =============================================================================

def format_text(report: AuditReport, stream: TextIO | None = None) -> str:
    """
    Build the human-readable report. Stream argument is only used to
    decide whether to emit ANSI color; the formatter always returns
    a string so callers can also capture it to disk.
    """
    stream = stream or sys.stdout
    use_color = _use_color(stream)
    lines: list[str] = []

    # ---- Header ----
    verdict = report.verdict
    verdict_color = {"PASS": "green", "WARN": "yellow", "FAIL": "red"}[verdict]
    bar = "=" * 72
    lines.append(bar)
    lines.append(_c("  SKILL SECURITY AUDITOR", "bold", use_color))
    lines.append(bar)
    lines.append(f"Skill:     {report.skill_name}")
    lines.append(f"Path:      {report.skill_path}")
    lines.append(f"Verdict:   {_c(verdict, verdict_color, use_color)}  —  {report.verdict_explanation}")
    if report.strict:
        lines.append(_c("Mode:      strict (HIGH findings will block install)", "dim", use_color))
    lines.append("")

    # ---- Summary table ----
    lines.append(_c("Findings by severity:", "bold", use_color))
    for sev in (Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW):
        count = report.count(sev)
        badge = SEVERITY_BADGE[sev]
        line = f"  {badge:<14} {count}"
        if count > 0:
            line = _c(line, _SEV_COLOR[sev], use_color)
        lines.append(line)
    lines.append(f"  {'TOTAL':<14} {len(report.findings)}")
    lines.append("")

    # ---- Stats ----
    lines.append(_c("Scan coverage:", "bold", use_color))
    lines.append(f"  Files total:     {report.files_total}")
    lines.append(f"  Code files:      {report.code_files}")
    lines.append(f"  Markdown files:  {report.markdown_files}")
    lines.append(f"  Workflow files:  {report.workflow_files}")
    lines.append(f"  Dep manifests:   {report.dep_files}")
    lines.append("")

    # ---- Findings ----
    if not report.findings:
        lines.append(_c("✓ No security issues detected.", "green", use_color))
        lines.append("")
        return "\n".join(lines)

    grouped = _group_findings(report)

    for sev in (Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW):
        files = grouped[sev]
        if not files:
            continue
        sev_label = SEVERITY_BADGE[sev]
        n = sum(len(fs) for fs in files.values())
        header = f"{sev_label}  ({n} finding{'s' if n != 1 else ''})"
        lines.append(_c(header, _SEV_COLOR[sev], use_color))
        lines.append(_c("─" * 72, "dim", use_color))

        for file_path, file_findings in sorted(files.items()):
            lines.append(_c(file_path, "cyan", use_color))
            for f in file_findings:
                line_label = f":{f.line}" if f.line > 0 else ""
                lines.append(f"  {file_path}{line_label}  [{f.category}]")
                if f.snippet:
                    lines.append(f"    {_c('│', 'dim', use_color)} {f.snippet}")
                lines.append(f"    {_c('Risk:', 'dim', use_color)} {f.risk}")
                lines.append(f"    {_c('Fix:', 'dim', use_color)}  {f.fix}")
                lines.append("")

    # ---- Footer ----
    lines.append(_c("─" * 72, "dim", use_color))
    if verdict == "FAIL":
        lines.append(_c("✗ FAIL — do not install this skill without addressing critical findings.", "red", use_color))
    elif verdict == "WARN":
        lines.append(_c("⚠ WARN — review the findings above before installing.", "yellow", use_color))
    else:
        lines.append(_c("✓ PASS — no blocking issues found.", "green", use_color))
    lines.append("")
    lines.append(_c("Tip: re-run with --strict to treat HIGH findings as blocking.", "dim", use_color))
    lines.append(_c("Tip: use --json for CI integration, --markdown for PR comments.", "dim", use_color))
    return "\n".join(lines)


# =============================================================================
# JSON REPORT
# =============================================================================

def format_json(report: AuditReport, *, indent: int | None = 2) -> str:
    """
    Stable, machine-readable representation. Carries schema_version
    so CI systems can detect format changes. Field order is preserved
    by the dataclass conversion in AuditReport.to_dict.
    """
    return json.dumps(report.to_dict(), indent=indent, sort_keys=False, ensure_ascii=False)


# =============================================================================
# MARKDOWN REPORT
# =============================================================================

def format_markdown(report: AuditReport) -> str:
    """
    Format suitable for pasting into a PR comment or GitHub issue.
    Uses tables for the summary, collapsible <details> blocks per
    severity so a PR reviewer sees the headline first.
    """
    out: list[str] = []
    verdict_emoji = {"PASS": "✅", "WARN": "⚠️", "FAIL": "❌"}[report.verdict]

    out.append(f"# Skill Security Audit — {report.skill_name}")
    out.append("")
    out.append(f"**Verdict:** {verdict_emoji} **{report.verdict}** — {report.verdict_explanation}")
    out.append("")
    out.append(f"- Skill path: `{report.skill_path}`")
    out.append(f"- Strict mode: `{report.strict}`")
    out.append(f"- Files scanned: {report.files_total} "
               f"(code: {report.code_files}, markdown: {report.markdown_files}, "
               f"workflow: {report.workflow_files}, deps: {report.dep_files})")
    out.append("")

    # Summary table
    out.append("## Summary")
    out.append("")
    out.append("| Severity | Count |")
    out.append("|----------|-------|")
    for sev in (Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW):
        out.append(f"| {SEVERITY_BADGE[sev]} | {report.count(sev)} |")
    out.append(f"| **Total** | **{len(report.findings)}** |")
    out.append("")

    if not report.findings:
        out.append("_No security issues detected._")
        out.append("")
        return "\n".join(out)

    # Findings, severity-bucketed
    out.append("## Findings")
    out.append("")
    grouped = _group_findings(report)
    for sev in (Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW):
        files = grouped[sev]
        if not files:
            continue
        n = sum(len(fs) for fs in files.values())
        # Critical and High are expanded by default; others collapsed.
        open_attr = " open" if sev in (Severity.CRITICAL, Severity.HIGH) else ""
        out.append(f"<details{open_attr}>")
        out.append(f"<summary><strong>{SEVERITY_BADGE[sev]}</strong> — {n} finding{'s' if n != 1 else ''}</summary>")
        out.append("")
        for file_path, file_findings in sorted(files.items()):
            out.append(f"#### `{file_path}`")
            out.append("")
            for f in file_findings:
                line_label = f":{f.line}" if f.line > 0 else ""
                out.append(f"- **{f.category}** at `{file_path}{line_label}`")
                if f.snippet:
                    # Triple-backtick fence so MD readers render snippet verbatim
                    out.append(f"  ```")
                    out.append(f"  {f.snippet}")
                    out.append(f"  ```")
                out.append(f"  - Risk: {f.risk}")
                out.append(f"  - Fix: {f.fix}")
            out.append("")
        out.append("</details>")
        out.append("")

    return "\n".join(out)


# =============================================================================
# HTML REPORT
# =============================================================================

def format_html(report: AuditReport) -> str:
    """
    Self-contained single-file HTML report. No external CSS or JS.
    Suitable for attaching to an email or hosting as a static
    artifact in CI.
    """
    verdict = report.verdict
    verdict_color = {"PASS": "#15803d", "WARN": "#b45309", "FAIL": "#b91c1c"}[verdict]

    # Build finding rows
    grouped = _group_findings(report)
    finding_blocks: list[str] = []
    sev_colors = {
        Severity.CRITICAL: "#dc2626",
        Severity.HIGH: "#d97706",
        Severity.MEDIUM: "#2563eb",
        Severity.LOW: "#6b7280",
    }
    for sev in (Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW):
        files = grouped[sev]
        if not files:
            continue
        sev_name = SEVERITY_NAME[sev]
        sev_color = sev_colors[sev]
        n = sum(len(fs) for fs in files.values())
        # Critical/High open by default for the same reason as in markdown
        open_attr = " open" if sev in (Severity.CRITICAL, Severity.HIGH) else ""
        finding_blocks.append(
            f'<details class="sev" style="border-left-color:{sev_color}"{open_attr}>'
            f'<summary><span class="badge" style="background:{sev_color}">{sev_name}</span> {n} finding{"s" if n != 1 else ""}</summary>'
        )
        for file_path, file_findings in sorted(files.items()):
            finding_blocks.append(f'<div class="file"><code>{html.escape(file_path)}</code></div>')
            for f in file_findings:
                line_label = f":{f.line}" if f.line > 0 else ""
                finding_blocks.append('<div class="finding">')
                finding_blocks.append(
                    f'<div class="meta"><strong>{html.escape(f.category)}</strong> '
                    f'<span class="loc">{html.escape(file_path)}{line_label}</span></div>'
                )
                if f.snippet:
                    finding_blocks.append(f'<pre class="snippet">{html.escape(f.snippet)}</pre>')
                finding_blocks.append(f'<div class="rf"><span class="lbl">Risk:</span> {html.escape(f.risk)}</div>')
                finding_blocks.append(f'<div class="rf"><span class="lbl">Fix:</span> {html.escape(f.fix)}</div>')
                finding_blocks.append('</div>')
        finding_blocks.append('</details>')

    findings_html = "\n".join(finding_blocks) if finding_blocks else '<p class="ok">No security issues detected.</p>'

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Skill Audit — {html.escape(report.skill_name)}</title>
<style>
* {{ box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; max-width: 980px; margin: 2rem auto; padding: 0 1.5rem; color: #1f2937; background: #f9fafb; }}
h1 {{ margin: 0 0 0.5rem; font-size: 1.6rem; }}
h2 {{ margin-top: 2rem; font-size: 1.2rem; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.3rem; }}
.verdict {{ font-size: 1.3rem; font-weight: 700; color: {verdict_color}; }}
.meta-block {{ background: white; border: 1px solid #e5e7eb; border-radius: 8px; padding: 1rem 1.25rem; margin: 1rem 0; }}
.meta-block dl {{ display: grid; grid-template-columns: max-content 1fr; column-gap: 1rem; row-gap: 0.4rem; margin: 0; }}
.meta-block dt {{ font-weight: 600; color: #4b5563; }}
.meta-block dd {{ margin: 0; font-family: ui-monospace, "SF Mono", Consolas, monospace; font-size: 0.9rem; }}
table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }}
th, td {{ padding: 0.5rem 0.75rem; text-align: left; border-bottom: 1px solid #e5e7eb; }}
th {{ background: #f3f4f6; font-weight: 600; }}
tr:last-child td {{ border-bottom: none; }}
.sev {{ background: white; border: 1px solid #e5e7eb; border-left: 4px solid #9ca3af; border-radius: 6px; margin: 0.75rem 0; padding: 0.5rem 1rem; }}
.sev summary {{ cursor: pointer; font-weight: 600; padding: 0.25rem 0; }}
.badge {{ display: inline-block; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; margin-right: 0.5rem; font-weight: 700; letter-spacing: 0.03em; }}
.file {{ margin-top: 1rem; padding-bottom: 0.25rem; border-bottom: 1px dashed #e5e7eb; }}
.file code {{ font-weight: 600; }}
.finding {{ margin: 0.75rem 0 0.75rem 1rem; padding-left: 0.75rem; border-left: 2px solid #e5e7eb; }}
.meta {{ font-size: 0.9rem; }}
.meta .loc {{ color: #6b7280; font-family: ui-monospace, monospace; font-size: 0.85rem; margin-left: 0.5rem; }}
.snippet {{ background: #f3f4f6; padding: 0.5rem 0.75rem; border-radius: 4px; font-size: 0.85rem; overflow-x: auto; margin: 0.4rem 0; }}
.rf {{ font-size: 0.9rem; margin: 0.2rem 0; }}
.rf .lbl {{ color: #6b7280; font-weight: 600; margin-right: 0.25rem; }}
.ok {{ color: #15803d; font-weight: 600; }}
.footer {{ margin-top: 2rem; color: #6b7280; font-size: 0.85rem; }}
</style>
</head>
<body>
<h1>Skill Security Audit</h1>
<div class="meta-block">
  <dl>
    <dt>Skill</dt><dd>{html.escape(report.skill_name)}</dd>
    <dt>Path</dt><dd>{html.escape(report.skill_path)}</dd>
    <dt>Verdict</dt><dd><span class="verdict">{verdict}</span> &nbsp; {html.escape(report.verdict_explanation)}</dd>
    <dt>Strict</dt><dd>{report.strict}</dd>
  </dl>
</div>

<h2>Summary</h2>
<table>
  <tr><th>Severity</th><th>Count</th></tr>
  <tr><td>Critical</td><td>{report.critical}</td></tr>
  <tr><td>High</td><td>{report.high}</td></tr>
  <tr><td>Medium</td><td>{report.medium}</td></tr>
  <tr><td>Low</td><td>{report.low}</td></tr>
  <tr><td><strong>Total</strong></td><td><strong>{len(report.findings)}</strong></td></tr>
</table>

<h2>Coverage</h2>
<table>
  <tr><th>Metric</th><th>Value</th></tr>
  <tr><td>Files total</td><td>{report.files_total}</td></tr>
  <tr><td>Code files</td><td>{report.code_files}</td></tr>
  <tr><td>Markdown files</td><td>{report.markdown_files}</td></tr>
  <tr><td>Workflow files</td><td>{report.workflow_files}</td></tr>
  <tr><td>Dep manifests</td><td>{report.dep_files}</td></tr>
</table>

<h2>Findings</h2>
{findings_html}

<p class="footer">Generated by Skill Security Auditor.</p>
</body>
</html>
"""
