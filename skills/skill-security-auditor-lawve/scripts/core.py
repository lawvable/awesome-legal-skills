"""
Core data structures, severity model, and shared utilities for the
Skill Security Auditor.

Anything that more than one scanner needs lives here. Keeping the
dataclasses and verdict logic in one place means every scanner
produces findings the orchestrator and reporters can consume the
same way.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass, field
from enum import IntEnum
from pathlib import Path
from typing import Iterable


# =============================================================================
# SEVERITY MODEL
# =============================================================================

class Severity(IntEnum):
    """
    Four-tier severity used across all scanners.

    The numeric values let us sort and compare. Higher = worse.
    CRITICAL findings should be treated as malicious until proven
    otherwise. HIGH findings need human eyes. MEDIUM/LOW are
    informational and don't block by default.
    """
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3


SEVERITY_NAME = {
    Severity.LOW: "LOW",
    Severity.MEDIUM: "MEDIUM",
    Severity.HIGH: "HIGH",
    Severity.CRITICAL: "CRITICAL",
}

SEVERITY_BADGE = {
    Severity.LOW: "⚪ LOW",
    Severity.MEDIUM: "🔵 MEDIUM",
    Severity.HIGH: "🟡 HIGH",
    Severity.CRITICAL: "🔴 CRITICAL",
}

SEVERITY_FROM_NAME = {v: k for k, v in SEVERITY_NAME.items()}


# =============================================================================
# FINDING
# =============================================================================

@dataclass
class Finding:
    """
    A single security observation about one location in the skill.

    Fields:
        severity:   tier from the Severity enum
        category:   short tag like "CODE-EXEC", "NET-EXFIL". The category
                    is what humans skim for. Categories are stable; new
                    patterns reuse existing categories where possible.
        scanner:    which scanner produced the finding (for filtering)
        file:       relative path inside the skill (or absolute if the
                    caller passed an absolute path)
        line:       1-indexed line number; 0 means file-level finding
        pattern:    the regex / structural signature that fired
        snippet:    up to ~120 chars of the matching line (or "" for
                    file-level findings)
        risk:       one-sentence explanation of why this is dangerous
        fix:        one-sentence remediation hint
    """
    severity: Severity
    category: str
    scanner: str
    file: str
    line: int
    pattern: str
    snippet: str
    risk: str
    fix: str

    def fingerprint(self) -> str:
        """
        Stable identifier for delta tracking and baseline suppression.

        Combines file path, line content (not number — line numbers
        drift when files are edited), and pattern. If we ever need to
        suppress this specific finding in a baseline.yml, this is the
        key the suppression list uses.
        """
        h = hashlib.sha256()
        h.update(self.file.encode("utf-8", errors="replace"))
        h.update(b"\x00")
        h.update(self.snippet.encode("utf-8", errors="replace"))
        h.update(b"\x00")
        h.update(self.pattern.encode("utf-8", errors="replace"))
        h.update(b"\x00")
        h.update(self.category.encode("utf-8", errors="replace"))
        return h.hexdigest()[:16]

    def to_dict(self) -> dict:
        d = asdict(self)
        d["severity"] = SEVERITY_NAME[self.severity]
        d["fingerprint"] = self.fingerprint()
        return d


# =============================================================================
# REPORT
# =============================================================================

@dataclass
class AuditReport:
    """
    Aggregate result of running every scanner on one skill.

    The report carries findings plus enough metadata that the
    reporter can show useful counts and the CI step can decide
    whether to block.
    """
    skill_name: str
    skill_path: str
    findings: list[Finding] = field(default_factory=list)

    # Per-scanner file counts (filled in by scanners as they run)
    files_total: int = 0
    code_files: int = 0
    markdown_files: int = 0
    workflow_files: int = 0
    dep_files: int = 0

    # Mode flags affecting the verdict
    strict: bool = False

    # Optional metadata captured at scan time
    started_at: str = ""
    finished_at: str = ""
    scanner_versions: dict[str, str] = field(default_factory=dict)

    def add(self, finding: Finding) -> None:
        """Append a finding. Centralised so we can later add dedup or
        suppression hooks without changing every scanner."""
        self.findings.append(finding)

    def count(self, severity: Severity) -> int:
        return sum(1 for f in self.findings if f.severity == severity)

    @property
    def critical(self) -> int:
        return self.count(Severity.CRITICAL)

    @property
    def high(self) -> int:
        return self.count(Severity.HIGH)

    @property
    def medium(self) -> int:
        return self.count(Severity.MEDIUM)

    @property
    def low(self) -> int:
        return self.count(Severity.LOW)

    @property
    def verdict(self) -> str:
        """
        Three-tier verdict that CI gates and humans both consume.

        - FAIL: at least one CRITICAL, or HIGH in strict mode
        - WARN: at least one HIGH (normal mode) or a pile of MEDIUMs
        - PASS: nothing of concern (LOW findings are OK)

        Strict mode collapses WARN into FAIL — recommended for any
        automated gate.
        """
        if self.critical > 0:
            return "FAIL"
        if self.high > 0:
            return "FAIL" if self.strict else "WARN"
        # Lots of MEDIUMs is a smell even without HIGH
        if self.medium >= 5:
            return "WARN"
        return "PASS"

    @property
    def verdict_explanation(self) -> str:
        """One-line human-readable reason for the current verdict."""
        v = self.verdict
        if v == "FAIL" and self.critical > 0:
            return f"{self.critical} critical finding(s) — install blocked"
        if v == "FAIL" and self.high > 0:
            return f"{self.high} high finding(s) in strict mode — install blocked"
        if v == "WARN" and self.high > 0:
            return f"{self.high} high finding(s) — manual review required"
        if v == "WARN":
            return f"{self.medium} medium finding(s) — review before install"
        if not self.findings:
            return "No security issues found"
        return "Only low-severity informational findings"

    def to_dict(self) -> dict:
        return {
            "schema_version": 1,
            "skill_name": self.skill_name,
            "skill_path": self.skill_path,
            "verdict": self.verdict,
            "verdict_explanation": self.verdict_explanation,
            "strict_mode": self.strict,
            "summary": {
                "critical": self.critical,
                "high": self.high,
                "medium": self.medium,
                "low": self.low,
                "total": len(self.findings),
            },
            "stats": {
                "files_total": self.files_total,
                "code_files": self.code_files,
                "markdown_files": self.markdown_files,
                "workflow_files": self.workflow_files,
                "dep_files": self.dep_files,
            },
            "timing": {
                "started_at": self.started_at,
                "finished_at": self.finished_at,
            },
            "scanner_versions": self.scanner_versions,
            "findings": [f.to_dict() for f in self.findings],
        }


# =============================================================================
# SUPPRESSION
# =============================================================================

# Inline suppression marker. If a line in user code contains this
# token, the line is skipped during scanning. This is essential
# because this auditor itself contains many "dangerous" strings
# (regexes for eval, os.system, etc.). Authors of legitimate skills
# that genuinely need a flagged pattern can use the same marker
# after manual review.
#
# We deliberately use a hyphen-separated marker that's unlikely to
# appear by accident.
SUPPRESS_MARKERS = (
    "noqa: SEC-AUDITOR",
    "auditor:ignore-line",
    "audit-skip",
)


def is_suppressed(line: str) -> bool:
    """True if the line contains any of our suppression markers."""
    return any(marker in line for marker in SUPPRESS_MARKERS)


# =============================================================================
# FILE TYPE CLASSIFICATION
# =============================================================================

# Treated as executable / scriptable code
CODE_EXTENSIONS: frozenset[str] = frozenset({
    ".py", ".pyw",
    ".sh", ".bash", ".zsh", ".ksh",
    ".js", ".mjs", ".cjs", ".jsx",
    ".ts", ".tsx",
    ".rb",
    ".pl", ".pm",
    ".php",
    ".lua",
    ".ps1",   # PowerShell
})

# Treated as prose / documentation where prompt injection lives
MARKDOWN_EXTENSIONS: frozenset[str] = frozenset({
    ".md", ".mdx", ".markdown", ".rst", ".txt",
})

# CI/CD workflow files — special handling for template injection
WORKFLOW_PATH_FRAGMENTS: frozenset[str] = frozenset({
    ".github/workflows",
    ".gitlab-ci.yml",
    ".circleci/config.yml",
    ".drone.yml",
})

WORKFLOW_EXTENSIONS: frozenset[str] = frozenset({".yml", ".yaml"})

# Dependency manifests
DEP_FILENAMES: frozenset[str] = frozenset({
    "requirements.txt",
    "requirements-dev.txt",
    "requirements-test.txt",
    "constraints.txt",
    "package.json",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "Pipfile",
    "Pipfile.lock",
    "pyproject.toml",
    "poetry.lock",
    "setup.py",
    "setup.cfg",
    "Gemfile",
    "Cargo.toml",
    "go.mod",
})

# Anything binary should be flagged regardless of contents
BINARY_EXTENSIONS: frozenset[str] = frozenset({
    ".exe", ".dll", ".so", ".dylib", ".bin", ".elf", ".com",
    ".msi", ".deb", ".rpm", ".apk", ".pkg", ".dmg",
    ".class", ".jar", ".war",
    ".pyc", ".pyo",
    ".o", ".obj",
})


def file_kind(path: Path) -> str:
    """
    Coarse classification of a path used by the orchestrator to
    decide which scanners apply.

    Returns one of: "code", "markdown", "workflow", "dep", "binary",
    "other".
    """
    name = path.name
    suffix = path.suffix.lower()
    parts_str = str(path).replace("\\", "/")

    if suffix in BINARY_EXTENSIONS:
        return "binary"
    if name in DEP_FILENAMES:
        return "dep"
    if any(frag in parts_str for frag in WORKFLOW_PATH_FRAGMENTS) and suffix in WORKFLOW_EXTENSIONS:
        return "workflow"
    if suffix in CODE_EXTENSIONS:
        return "code"
    if suffix in MARKDOWN_EXTENSIONS:
        return "markdown"
    return "other"


# =============================================================================
# CODE-FENCE AWARENESS
# =============================================================================

# Markdown code fences. We track which lines are *inside* a fence so
# pattern matches there can be downgraded or skipped — a SKILL.md
# documenting "ignore previous instructions" as a known attack
# pattern shouldn't itself trip the prompt-injection scanner.
_FENCE_RE = re.compile(r"^\s*```")


def code_fence_mask(lines: list[str]) -> list[bool]:
    """
    Return a boolean array the same length as `lines`. Entry i is
    True if line i (0-indexed) is inside a triple-backtick fenced
    code block.

    We toggle state on every line that starts (after whitespace)
    with three backticks. This is the same approximation pandoc
    uses and handles 99% of real-world markdown correctly.
    """
    inside = False
    mask = []
    for line in lines:
        if _FENCE_RE.match(line):
            inside = not inside
            # Fence boundary lines themselves are part of the block
            mask.append(True)
        else:
            mask.append(inside)
    return mask


# =============================================================================
# FILE READING
# =============================================================================

# Cap any individual file at 5 MB. Anything larger is either a data
# asset (which gets a filesystem-level finding) or a deliberately
# oversized payload designed to wedge the scanner.
MAX_SCAN_BYTES = 5 * 1024 * 1024


def safe_read_text(path: Path) -> str:
    """
    Read a file as text without throwing. We replace undecodable
    bytes rather than failing — a skill that contains binary trash
    in a .py file is itself suspicious and we want to scan whatever
    text we can.

    Returns "" if the file is unreadable or larger than MAX_SCAN_BYTES.
    """
    try:
        size = path.stat().st_size
    except OSError:
        return ""
    if size > MAX_SCAN_BYTES:
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except (OSError, ValueError):
        return ""


def iter_files(root: Path) -> Iterable[Path]:
    """
    Yield every file under root, skipping .git directories and
    common cache directories that aren't part of the skill itself.
    """
    skip_dirs = {".git", "__pycache__", "node_modules", ".venv", "venv", ".tox", ".mypy_cache"}
    for item in root.rglob("*"):
        if any(part in skip_dirs for part in item.parts):
            continue
        if item.is_file():
            yield item


# =============================================================================
# LINE TRUNCATION
# =============================================================================

# Findings include a snippet of the matching line. We truncate to
# keep terminal output readable and JSON reports small. The original
# pattern is preserved in the `pattern` field separately.
SNIPPET_MAX = 140


def trim_snippet(line: str) -> str:
    s = line.strip()
    if len(s) <= SNIPPET_MAX:
        return s
    return s[: SNIPPET_MAX - 3] + "..."
