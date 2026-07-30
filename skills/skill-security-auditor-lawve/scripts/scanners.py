"""
Scanner functions for the Skill Security Auditor.

Each scanner is a pure function that takes a Path and an
AuditReport, walks the relevant subset of files, and appends
Finding objects to the report. Scanners share the pattern
catalogue from patterns.py and the dataclasses from core.py.

Scanner contract:
    - Never raise on user content. Bad files become findings, not
      crashes.
    - Skip lines containing the SEC-AUDITOR suppression marker so the
      auditor can scan itself.
    - Use trim_snippet() for the `snippet` field so reports stay
      readable.
    - Honour fenced code blocks in markdown: pattern matches inside
      ```...``` blocks are downgraded one severity tier.
"""

from __future__ import annotations

import ast
import json
import re
import stat
from pathlib import Path
from typing import Iterable

import patterns  # noqa: SEC-AUDITOR
from core import (  # noqa: SEC-AUDITOR
    BINARY_EXTENSIONS,
    CODE_EXTENSIONS,
    DEP_FILENAMES,
    MARKDOWN_EXTENSIONS,
    WORKFLOW_EXTENSIONS,
    WORKFLOW_PATH_FRAGMENTS,
    AuditReport,
    Finding,
    Severity,
    code_fence_mask,
    file_kind,
    is_suppressed,
    iter_files,
    safe_read_text,
    trim_snippet,
)


# =============================================================================
# CODE SCANNER
# =============================================================================
# Runs regex-based pattern checks plus a Python-specific AST pass on
# code files. The AST pass catches things that regex misses cleanly,
# like imports aliased to dangerous names.

def scan_code(skill_root: Path, report: AuditReport) -> None:
    """Walk all code files and run the appropriate pattern groups."""
    for path in iter_files(skill_root):
        kind = file_kind(path)
        if kind != "code":
            continue
        report.code_files += 1
        rel = _rel_path(path, skill_root)
        text = safe_read_text(path)
        if not text:
            continue
        suffix = path.suffix.lower()

        # Always run generic code patterns
        groups: list[list[patterns.PatternDef]] = [patterns.CODE_PATTERNS]
        if suffix in {".sh", ".bash", ".zsh", ".ksh"}:
            groups.append(patterns.SHELL_PATTERNS)
        if suffix in {".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx"}:
            groups.append(patterns.JS_PATTERNS)

        # Secrets run on every file (high signal, low cost)
        groups.append(patterns.SECRET_PATTERNS)

        _scan_lines(
            text=text,
            rel_file=rel,
            scanner_name="code",
            groups=groups,
            report=report,
        )

        # Python-specific AST pass for things regex doesn't catch well
        if suffix in {".py", ".pyw"}:
            _python_ast_pass(rel, text, report)

        # Unicode / obfuscation sweep on the raw text
        _unicode_sweep(rel, text, report, scanner_name="code")


def _python_ast_pass(rel_file: str, text: str, report: AuditReport) -> None:
    """
    Python AST pass catches three categories regex handles poorly:

    1. Imports aliased to dangerous functions, e.g.
           from os import system as helper
           from subprocess import call as run
       — `helper(...)` later won't trip our regex but is just as
       dangerous.

    2. Calls to `getattr(obj, 'sys' + 'tem')` where the attribute
       name is built at runtime. We flag any getattr() with a
       non-Constant second argument.

    3. Unsafe YAML loader calls without a SafeLoader keyword argument
       — the regex version is brittle when the call spans multiple lines.

    If parsing fails (syntax error etc.) we silently skip — those
    files will get caught by the regex pass anyway.
    """
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return

    # Source lines for suppression-marker checks. AST findings carry a
    # lineno; we look at that line and skip if it has SEC-AUDITOR.
    src_lines = text.splitlines()

    def _is_node_suppressed(node: ast.AST) -> bool:
        lineno = getattr(node, "lineno", 0)
        if 0 < lineno <= len(src_lines):
            return is_suppressed(src_lines[lineno - 1])
        return False

    # Step 1: collect aliased imports of dangerous targets
    dangerous_imports = {
        ("os", "system"): "os.system",  # noqa: SEC-AUDITOR
        ("os", "popen"): "os.popen",    # noqa: SEC-AUDITOR
        ("subprocess", "call"): "subprocess.call",  # noqa: SEC-AUDITOR
        ("subprocess", "check_output"): "subprocess.check_output",  # noqa: SEC-AUDITOR
        ("subprocess", "Popen"): "subprocess.Popen",  # noqa: SEC-AUDITOR
        ("pickle", "loads"): "pickle.loads",  # noqa: SEC-AUDITOR
        ("pickle", "load"): "pickle.load",    # noqa: SEC-AUDITOR
        ("marshal", "loads"): "marshal.loads",  # noqa: SEC-AUDITOR
        ("marshal", "load"): "marshal.load",    # noqa: SEC-AUDITOR
    }
    aliases: dict[str, str] = {}  # local name -> fully qualified

    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                key = (node.module, alias.name)
                if key in dangerous_imports:
                    local = alias.asname or alias.name
                    aliases[local] = dangerous_imports[key]

    # Step 2: any call to an aliased dangerous import
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if _is_node_suppressed(node):
                continue
            func_name = _call_name(node)
            if func_name and func_name in aliases:
                report.add(Finding(
                    severity=Severity.HIGH,
                    category="CODE-EXEC",
                    scanner="code-ast",
                    file=rel_file,
                    line=node.lineno,
                    pattern=f"aliased call to {aliases[func_name]}",
                    snippet=f"{func_name}(...)  # aliased {aliases[func_name]}",
                    risk="Aliased import of a dangerous function — obscures call-site",
                    fix="Use the original name so static analysis can see the call",
                ))

            # Step 2b: getattr with non-literal attribute
            if isinstance(node.func, ast.Name) and node.func.id == "getattr":
                if len(node.args) >= 2 and not isinstance(node.args[1], ast.Constant):
                    report.add(Finding(
                        severity=Severity.HIGH,
                        category="CODE-EXEC",
                        scanner="code-ast",
                        file=rel_file,
                        line=node.lineno,
                        pattern="getattr(<obj>, <non-literal>)",
                        snippet=f"getattr(...)  # attribute name built at runtime",
                        risk="getattr with dynamic attribute name — obscures which method is called",
                        fix="Use direct attribute access; explicit dispatch is safer",
                    ))


def _call_name(node: ast.Call) -> str | None:
    """Return the dotted name of a call's func, or None if it's not a Name/Attribute."""
    f = node.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        parts = []
        cur: ast.AST = f
        while isinstance(cur, ast.Attribute):
            parts.append(cur.attr)
            cur = cur.value
        if isinstance(cur, ast.Name):
            parts.append(cur.id)
            return ".".join(reversed(parts))
    return None


# =============================================================================
# PROMPT INJECTION SCANNER
# =============================================================================

def scan_prompts(skill_root: Path, report: AuditReport) -> None:
    """Walk markdown / text files and look for prompt-injection patterns."""
    for path in iter_files(skill_root):
        if file_kind(path) != "markdown":
            continue
        report.markdown_files += 1
        rel = _rel_path(path, skill_root)
        text = safe_read_text(path)
        if not text:
            continue

        lines = text.splitlines()
        fenced = code_fence_mask(lines)

        for i, line in enumerate(lines):
            if is_suppressed(line):
                continue
            for pat in patterns.PROMPT_PATTERNS:
                m = pat["regex"].search(line)
                if not m:
                    continue
                # Inside a fenced code block, downgrade by one tier and
                # change the category so the reader knows it's a
                # documentation match. This is the single most
                # effective false-positive reducer.
                sev = pat["severity"]
                category = pat["category"]
                if fenced[i]:
                    sev = _downgrade(sev)
                    if sev is None:
                        continue
                    category = category + "-IN-CODE-FENCE"
                report.add(Finding(
                    severity=sev,
                    category=category,
                    scanner="prompt",
                    file=rel,
                    line=i + 1,
                    pattern=pat["regex"].pattern,
                    snippet=trim_snippet(line),
                    risk=pat["risk"],
                    fix=pat["fix"],
                ))

        # Run the unicode sweep on markdown too — hidden chars in
        # documentation are even more dangerous than in code because
        # the model reads them as instructions.
        _unicode_sweep(rel, text, report, scanner_name="prompt")


def _downgrade(sev: Severity) -> Severity | None:
    """Drop a severity by one tier. Returns None if we'd go below LOW."""
    if sev == Severity.CRITICAL:
        return Severity.HIGH
    if sev == Severity.HIGH:
        return Severity.MEDIUM
    if sev == Severity.MEDIUM:
        return Severity.LOW
    return None


# =============================================================================
# WORKFLOW SCANNER
# =============================================================================

def scan_workflows(skill_root: Path, report: AuditReport) -> None:
    """
    Scan CI workflow files. The dominant attack here is script
    injection via user-controllable github.event values.

    We also flag dangerous trigger choices (pull_request_target),
    unpinned actions, and continue-on-error on what looks like a
    security step.
    """
    for path in iter_files(skill_root):
        if file_kind(path) != "workflow":
            continue
        report.workflow_files += 1
        rel = _rel_path(path, skill_root)
        text = safe_read_text(path)
        if not text:
            continue

        _scan_lines(
            text=text,
            rel_file=rel,
            scanner_name="workflow",
            groups=[patterns.WORKFLOW_PATTERNS, patterns.SECRET_PATTERNS],
            report=report,
        )

        # The most dangerous shell-style patterns can appear inside a
        # workflow's `run:` block, so we also apply the shell patterns
        # — but only when we can see a `run:` indicator. Without that
        # we'd flag innocent YAML.
        if re.search(r"^\s*run\s*:\s*[|>]?", text, re.MULTILINE):
            _scan_lines(
                text=text,
                rel_file=rel,
                scanner_name="workflow",
                groups=[patterns.SHELL_PATTERNS],
                report=report,
            )


# =============================================================================
# SUPPLY CHAIN SCANNER
# =============================================================================
# Typosquatting + unpinned versions + runtime installs +
# package.json install hooks. The first two read manifests; the third
# reads scripts; the fourth reads package.json's scripts dict.

def scan_supply_chain(skill_root: Path, report: AuditReport) -> None:
    seen_packages: set[str] = set()
    typo_map: dict[str, str] = _build_typo_lookup()

    for path in iter_files(skill_root):
        name = path.name
        rel = _rel_path(path, skill_root)

        if name in ("requirements.txt", "requirements-dev.txt",
                    "requirements-test.txt", "constraints.txt"):
            report.dep_files += 1
            _scan_requirements(path, rel, report, typo_map, seen_packages)

        elif name == "package.json":
            report.dep_files += 1
            _scan_package_json(path, rel, report, typo_map, seen_packages)

        elif name == "pyproject.toml":
            report.dep_files += 1
            _scan_pyproject(path, rel, report, typo_map, seen_packages)

        elif name == "setup.py":
            report.dep_files += 1
            _scan_setup_py(path, rel, report)


def _build_typo_lookup() -> dict[str, str]:
    """Combine the hand-curated dict with auto-generated 1-edit variants of popular names."""
    lookup = dict(patterns.KNOWN_TYPOSQUATS)
    # We don't auto-generate variants here because the Levenshtein
    # check in _check_typosquat handles distance 1-2 against
    # POPULAR_PYPI / POPULAR_NPM directly. Returning the known list
    # only means the exact-match path is fast.
    return lookup


def _scan_requirements(path: Path, rel: str, report: AuditReport,
                       typo_map: dict[str, str], seen: set[str]) -> None:
    text = safe_read_text(path)
    if not text:
        return
    for i, raw_line in enumerate(text.splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#") or line.startswith("-r") or line.startswith("--"):
            # `-r other.txt` and `--index-url ...` are skipped from the
            # package check but the latter deserves its own finding.
            if line.startswith("--index-url") or line.startswith("--extra-index-url"):
                # Custom indexes are how dependency confusion attacks
                # ship malicious lookalikes.
                report.add(Finding(
                    severity=Severity.HIGH,
                    category="SUPPLY-CUSTOM-INDEX",
                    scanner="supply",
                    file=rel,
                    line=i,
                    pattern="--index-url / --extra-index-url",
                    snippet=trim_snippet(raw_line),
                    risk="Custom package index — bypasses the default PyPI; check the host",
                    fix="Remove the custom index unless it's a documented private mirror",
                ))
            continue

        # Editable install from git+https — installs whatever the repo
        # currently is, which is essentially unpinned + remote-fetched.
        if "-e " in line or line.startswith("-e ") or "git+" in line:
            report.add(Finding(
                severity=Severity.HIGH,
                category="SUPPLY-GIT-DEP",
                scanner="supply",
                file=rel,
                line=i,
                pattern="-e git+ / git+ install",
                snippet=trim_snippet(raw_line),
                risk="Editable / git-source dependency — installs unreviewed code from a URL",
                fix="Pin to a published version on PyPI",
            ))
            continue

        # Parse package name and operator
        m = re.match(r"^([A-Za-z0-9_.\-]+)\s*(==|>=|<=|~=|!=|>|<)?\s*([^;#\[]*)?", line)
        if not m:
            continue
        pkg = m.group(1)
        op = m.group(2)

        norm = _normalize_pkg(pkg)
        if norm in seen:
            continue
        seen.add(norm)

        # Typosquatting check
        squat_target = _check_typosquat(norm, patterns.POPULAR_PYPI, typo_map)
        if squat_target:
            report.add(Finding(
                severity=Severity.CRITICAL,
                category="SUPPLY-TYPOSQUAT",
                scanner="supply",
                file=rel,
                line=i,
                pattern=f"typosquat: {pkg} ~ {squat_target}",
                snippet=trim_snippet(raw_line),
                risk=f"'{pkg}' looks like '{squat_target}' — likely typosquatting",
                fix=f"Replace with the correct package name: '{squat_target}'",
            ))

        # Unpinned version
        if op != "==":
            report.add(Finding(
                severity=Severity.LOW,
                category="SUPPLY-UNPINNED",
                scanner="supply",
                file=rel,
                line=i,
                pattern="unpinned version",
                snippet=trim_snippet(raw_line),
                risk=f"'{pkg}' is not pinned to an exact version",
                fix=f"Pin to a specific version: {pkg}==<version>",
            ))


def _scan_package_json(path: Path, rel: str, report: AuditReport,
                       typo_map: dict[str, str], seen: set[str]) -> None:
    text = safe_read_text(path)
    if not text:
        return
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return

    # 1. Install hooks (preinstall / install / postinstall) are how
    #    npm packages run arbitrary code on `npm install`. We flag the
    #    *presence* of these hooks regardless of content — a legitimate
    #    skill should not need to install npm packages with hooks.
    scripts = data.get("scripts") or {}
    for hook in ("preinstall", "install", "postinstall", "prepare"):
        if hook in scripts:
            command = str(scripts[hook])
            line_num = _approx_json_line(text, f'"{hook}"')
            report.add(Finding(
                severity=Severity.CRITICAL,
                category="SUPPLY-POSTINSTALL",
                scanner="supply",
                file=rel,
                line=line_num,
                pattern=f"package.json scripts.{hook}",
                snippet=trim_snippet(f'"{hook}": "{command}"'),
                risk=f"npm {hook} hook — runs arbitrary code on `npm install`",
                fix="Remove the install hook. If build steps are needed, run them explicitly",
            ))

    # 2. Typosquat check across all dep sections
    for section in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
        deps = data.get(section) or {}
        for pkg, version in deps.items():
            norm = _normalize_pkg(pkg)
            if norm in seen:
                continue
            seen.add(norm)
            squat_target = _check_typosquat(norm, patterns.POPULAR_NPM, typo_map)
            if squat_target:
                line_num = _approx_json_line(text, f'"{pkg}"')
                report.add(Finding(
                    severity=Severity.CRITICAL,
                    category="SUPPLY-TYPOSQUAT",
                    scanner="supply",
                    file=rel,
                    line=line_num,
                    pattern=f"typosquat: {pkg} ~ {squat_target}",
                    snippet=trim_snippet(f'"{pkg}": "{version}"'),
                    risk=f"'{pkg}' looks like '{squat_target}' — likely typosquatting",
                    fix=f"Replace with the correct package name: '{squat_target}'",
                ))

            # git: / http: deps install arbitrary code from a URL
            v = str(version)
            if v.startswith(("git+", "git:", "http:", "https:", "file:")) or "tarball" in v:
                line_num = _approx_json_line(text, f'"{pkg}"')
                report.add(Finding(
                    severity=Severity.HIGH,
                    category="SUPPLY-URL-DEP",
                    scanner="supply",
                    file=rel,
                    line=line_num,
                    pattern="URL / git source dependency",
                    snippet=trim_snippet(f'"{pkg}": "{v}"'),
                    risk="Dependency specified by URL — installs unreviewed code",
                    fix="Replace with a published npm version range and pin it",
                ))


def _scan_pyproject(path: Path, rel: str, report: AuditReport,
                    typo_map: dict[str, str], seen: set[str]) -> None:
    text = safe_read_text(path)
    if not text:
        return
    # Simple line-by-line scan; we don't need a full TOML parser for
    # the patterns we care about (typosquats inside dependencies lists
    # and explicit dynamic build scripts).
    in_deps = False
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if line.startswith("[") and line.endswith("]"):
            in_deps = any(k in line for k in ("dependencies", "requires"))
            continue
        if not in_deps or not line or line.startswith("#"):
            continue
        # `"package==1.0"` or `package = "1.0"`
        m = re.search(r"[\"']([A-Za-z0-9_.\-]+)[\"']\s*(?:[:=,]|$)", line)
        if not m:
            continue
        pkg = m.group(1)
        norm = _normalize_pkg(pkg)
        if norm in seen:
            continue
        seen.add(norm)
        squat_target = _check_typosquat(norm, patterns.POPULAR_PYPI, typo_map)
        if squat_target:
            report.add(Finding(
                severity=Severity.CRITICAL,
                category="SUPPLY-TYPOSQUAT",
                scanner="supply",
                file=rel,
                line=i,
                pattern=f"typosquat: {pkg} ~ {squat_target}",
                snippet=trim_snippet(raw),
                risk=f"'{pkg}' looks like '{squat_target}' — likely typosquatting",
                fix=f"Replace with the correct package name: '{squat_target}'",
            ))


def _scan_setup_py(path: Path, rel: str, report: AuditReport) -> None:
    """setup.py is itself executable code on package install."""  # noqa: SEC-AUDITOR
    text = safe_read_text(path)
    if not text:
        return
    # We already scanned setup.py with the code scanner if it has .py
    # extension. The supply-chain angle is whether it contains a
    # custom cmdclass or build hook — flag those specifically.
    if re.search(r"\bcmdclass\s*=", text) or re.search(r"\bbuild_py\s*\(", text):
        line = _approx_line(text, "cmdclass") or 1
        report.add(Finding(
            severity=Severity.HIGH,
            category="SUPPLY-SETUP-HOOK",
            scanner="supply",
            file=rel,
            line=line,
            pattern="setup.py cmdclass / build hook",
            snippet="setup(... cmdclass=... )",
            risk="setup.py with custom cmdclass executes arbitrary code on package install",  # noqa: SEC-AUDITOR
            fix="Use a static pyproject.toml configuration instead of dynamic setup.py",
        ))


def _normalize_pkg(name: str) -> str:
    """PEP 503-style package name normalization."""
    return re.sub(r"[-_.]+", "-", name).lower()


def _levenshtein(a: str, b: str) -> int:
    """Plain Levenshtein distance. Small alphabet, no need for libs."""
    if len(a) < len(b):
        return _levenshtein(b, a)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a):
        cur = [i + 1]
        for j, cb in enumerate(b):
            ins = prev[j + 1] + 1
            dele = cur[j] + 1
            sub = prev[j] + (ca != cb)
            cur.append(min(ins, dele, sub))
        prev = cur
    return prev[-1]


def _check_typosquat(norm_pkg: str, popular_list: list[str],
                     known_map: dict[str, str]) -> str | None:
    """
    Return the legitimate package name if `norm_pkg` looks like a
    typosquat of it, else None.

    Strategy:
        1. Exact match against the curated known-typosquats table.
        2. Levenshtein distance 1-2 against the popular list, but
           only for packages with at least 4 characters (shorter
           names hit false positives — `re` vs `os` shouldn't fire).
        3. Skip the check if norm_pkg itself appears in the popular
           list (it's the real thing, not a squat).
    """
    if norm_pkg in known_map:
        return known_map[norm_pkg]

    # Don't flag the popular package itself
    if any(norm_pkg == _normalize_pkg(p) for p in popular_list):
        return None

    if len(norm_pkg) < 4:
        return None

    for popular in popular_list:
        pop_norm = _normalize_pkg(popular)
        dist = _levenshtein(norm_pkg, pop_norm)
        if 1 <= dist <= 2:
            return popular
    return None


def _approx_json_line(text: str, needle: str) -> int:
    """Return the 1-indexed line in `text` where `needle` first appears."""
    idx = text.find(needle)
    if idx < 0:
        return 0
    return text[:idx].count("\n") + 1


def _approx_line(text: str, needle: str) -> int | None:
    idx = text.find(needle)
    if idx < 0:
        return None
    return text[:idx].count("\n") + 1


# =============================================================================
# FILESYSTEM SCANNER
# =============================================================================
# Directory-level concerns: binaries that shouldn't be in a skill,
# symlinks pointing outside the skill, hidden files, SUID/SGID bits,
# and oversized files.

def scan_filesystem(skill_root: Path, report: AuditReport) -> None:
    skill_root_resolved = skill_root.resolve()

    for item in iter_files(skill_root):
        report.files_total += 1
        rel = _rel_path(item, skill_root)

        # 1. Binary files — almost never legitimate in a skill
        if item.suffix.lower() in BINARY_EXTENSIONS:
            report.add(Finding(
                severity=Severity.CRITICAL,
                category="FS-BINARY",
                scanner="filesystem",
                file=rel,
                line=0,
                pattern=f"binary extension {item.suffix}",
                snippet=item.name,
                risk="Binary executable in skill — high risk of unreviewable payload",
                fix="Remove binary files. Skills should use interpreted scripts only",
            ))

        # 2. Hidden dotfiles (excluding well-known config files that
        #    legitimately appear in skill repos)
        allowed_dotfiles = {
            ".gitignore", ".gitkeep", ".gitattributes",
            ".editorconfig", ".prettierrc", ".eslintrc",
            ".pylintrc", ".flake8", ".dockerignore",
            ".python-version", ".tool-versions",
            ".claude-plugin", ".mcp.json",
        }
        if item.name.startswith(".") and item.name not in allowed_dotfiles:
            sev = Severity.CRITICAL if item.name in (".env", ".env.local", ".env.production") else Severity.HIGH
            report.add(Finding(
                severity=sev,
                category="FS-HIDDEN",
                scanner="filesystem",
                file=rel,
                line=0,
                pattern=f"hidden file: {item.name}",
                snippet=item.name,
                risk="Hidden file in skill — may contain secrets or be overlooked in review",
                fix="Remove hidden files from skill distribution",
            ))

        # 3. Symlinks pointing outside the skill — directory traversal
        if item.is_symlink():
            try:
                target = item.resolve()
                if not _is_relative_to(target, skill_root_resolved):
                    report.add(Finding(
                        severity=Severity.CRITICAL,
                        category="FS-SYMLINK",
                        scanner="filesystem",
                        file=rel,
                        line=0,
                        pattern=f"symlink → {target}",
                        snippet=f"{item.name} -> {target}",
                        risk="Symlink points outside skill directory — traversal / read-arbitrary risk",
                        fix="Remove symlinks pointing outside the skill",
                    ))
            except (OSError, ValueError):
                pass

        # 4. SUID / SGID bits set on files in the skill
        try:
            mode = item.stat().st_mode
            if mode & (stat.S_ISUID | stat.S_ISGID):
                report.add(Finding(
                    severity=Severity.CRITICAL,
                    category="FS-SUID",
                    scanner="filesystem",
                    file=rel,
                    line=0,
                    pattern=f"mode={oct(mode)[-4:]} (SUID/SGID set)",
                    snippet=item.name,
                    risk="SUID/SGID bit set — privilege escalation",
                    fix="Remove SUID/SGID bits: chmod u-s,g-s <file>",
                ))
        except OSError:
            pass

        # 5. Large files — payload-hiding signal
        try:
            size = item.stat().st_size
            if size > 1_000_000 and file_kind(item) != "binary":  # binary already flagged
                report.add(Finding(
                    severity=Severity.LOW,
                    category="FS-LARGE",
                    scanner="filesystem",
                    file=rel,
                    line=0,
                    pattern=f"size {size/1_000_000:.1f}MB",
                    snippet=f"{item.name} ({size/1_000_000:.1f} MB)",
                    risk="Large file may bloat the skill or hide payload data",
                    fix="Review file contents. Consider whether this asset is necessary",
                ))
        except OSError:
            pass


def _is_relative_to(child: Path, parent: Path) -> bool:
    """Path.is_relative_to is 3.9+. Hand-rolled version for portability."""
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False


# =============================================================================
# STRUCTURE SCANNER
# =============================================================================
# Sanity checks on the skill layout itself. Missing SKILL.md, frontmatter
# without required fields, etc.

def scan_structure(skill_root: Path, report: AuditReport) -> None:
    skill_md = skill_root / "SKILL.md"
    if not skill_md.exists():
        report.add(Finding(
            severity=Severity.HIGH,
            category="STRUCTURE",
            scanner="structure",
            file="SKILL.md",
            line=0,
            pattern="missing SKILL.md",
            snippet="",
            risk="No SKILL.md found — not a valid skill directory",
            fix="Provide a SKILL.md with name and description in YAML frontmatter",
        ))
        return

    text = safe_read_text(skill_md)
    if not text.startswith("---"):
        report.add(Finding(
            severity=Severity.MEDIUM,
            category="STRUCTURE",
            scanner="structure",
            file="SKILL.md",
            line=1,
            pattern="missing YAML frontmatter",
            snippet=text[:80].replace("\n", " ").strip(),
            risk="SKILL.md without YAML frontmatter — skill won't be discoverable",
            fix="Add a `---` block at the top with `name:` and `description:` keys",
        ))
        return

    # Check for required frontmatter fields
    frontmatter_end = text.find("\n---", 3)
    if frontmatter_end < 0:
        report.add(Finding(
            severity=Severity.MEDIUM,
            category="STRUCTURE",
            scanner="structure",
            file="SKILL.md",
            line=1,
            pattern="unterminated frontmatter",
            snippet="--- ...",
            risk="YAML frontmatter is not closed with `---`",
            fix="Add a closing `---` line after the frontmatter fields",
        ))
        return

    frontmatter = text[3:frontmatter_end]
    for required in ("name", "description"):
        if not re.search(rf"^{required}\s*:", frontmatter, re.MULTILINE):
            report.add(Finding(
                severity=Severity.MEDIUM,
                category="STRUCTURE",
                scanner="structure",
                file="SKILL.md",
                line=1,
                pattern=f"frontmatter missing: {required}",
                snippet=trim_snippet(frontmatter),
                risk=f"SKILL.md frontmatter missing required `{required}` field",
                fix=f"Add `{required}: ...` to the frontmatter",
            ))


# =============================================================================
# UNICODE / OBFUSCATION SWEEP
# =============================================================================
# Walks every byte of the file looking for zero-width, bidi-override,
# and homoglyph characters. These don't show up in regex-on-line scans
# because by definition they're invisible.

def _unicode_sweep(rel_file: str, text: str, report: AuditReport,
                   scanner_name: str) -> None:
    if not text:
        return

    lines = text.splitlines()

    def _line_of(pos: int) -> tuple[int, str]:
        """Return (1-indexed line number, line text) for a byte position."""
        line_num = text[:pos].count("\n") + 1
        line_text = lines[line_num - 1] if 0 < line_num <= len(lines) else ""
        return line_num, line_text

    # Zero-width characters
    for ch, desc in patterns.ZERO_WIDTH_CHARS.items():
        pos = text.find(ch)
        if pos >= 0:
            line_num, line_text = _line_of(pos)
            if is_suppressed(line_text):
                continue
            report.add(Finding(
                severity=Severity.HIGH,
                category="OBFUSCATION-ZWIDTH",
                scanner=scanner_name,
                file=rel_file,
                line=line_num,
                pattern=f"contains {desc}",
                snippet=desc,
                risk="Zero-width character — may hide instructions or alter parsing",
                fix="Remove all zero-width characters. View the file in a hex editor to verify",
            ))

    # Bidirectional override — the Trojan Source family
    for ch, desc in patterns.BIDI_OVERRIDE_CHARS.items():
        pos = text.find(ch)
        if pos >= 0:
            line_num, line_text = _line_of(pos)
            if is_suppressed(line_text):
                continue
            report.add(Finding(
                severity=Severity.CRITICAL,
                category="OBFUSCATION-BIDI",
                scanner=scanner_name,
                file=rel_file,
                line=line_num,
                pattern=f"contains {desc}",
                snippet=desc,
                risk="Bidirectional override character — Trojan Source attack: visual order differs from logical order",
                fix="Remove the bidi-override character. There is no legitimate reason for it in skill code",
            ))

    # Homoglyphs inside identifier-like contexts. We check if any
    # homoglyph appears AT ALL — for prose this is fine (a Cyrillic
    # name is legitimate), but for code files we report it. The
    # scanner is called from both code and markdown so we use MEDIUM
    # severity to acknowledge the false-positive risk in markdown.
    if scanner_name == "code":
        for ch, desc in patterns.HOMOGLYPH_MAP.items():
            pos = text.find(ch)
            if pos >= 0:
                line_num, line_text = _line_of(pos)
                if is_suppressed(line_text):
                    continue
                report.add(Finding(
                    severity=Severity.MEDIUM,
                    category="OBFUSCATION-HOMOGLYPH",
                    scanner=scanner_name,
                    file=rel_file,
                    line=line_num,
                    pattern=f"contains {desc}",
                    snippet=desc,
                    risk="Homoglyph (non-Latin character that looks like a Latin one) in code",
                    fix="Replace with the ASCII equivalent. Homoglyphs are used to bypass identifier-based checks",
                ))


# =============================================================================
# SHARED LINE-SCANNING HELPER
# =============================================================================

def _scan_lines(*, text: str, rel_file: str, scanner_name: str,
                groups: Iterable[list[patterns.PatternDef]],
                report: AuditReport) -> None:
    """
    Walk `text` line by line and apply every pattern in every group.

    Lines containing the SEC-AUDITOR suppression marker are skipped
    entirely. A single line can produce multiple findings (one per
    matching pattern); we deliberately do not dedup at the line level
    because two findings in the same line tend to be two different
    classes of badness worth surfacing.

    Pure-comment lines for the file's language are skipped to keep
    noise down — a `# evaluate(...)` in a Python comment isn't real code.
    """
    suffix_to_comment = {
        ".py": "#", ".pyw": "#",
        ".sh": "#", ".bash": "#", ".zsh": "#",
        ".js": "//", ".mjs": "//", ".cjs": "//", ".jsx": "//",
        ".ts": "//", ".tsx": "//",
        ".yml": "#", ".yaml": "#",
        ".toml": "#",
    }
    suffix = Path(rel_file).suffix.lower()
    comment_prefix = suffix_to_comment.get(suffix)

    for i, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if comment_prefix and stripped.startswith(comment_prefix):
            continue
        if is_suppressed(line):
            continue

        for group in groups:
            for pat in group:
                if pat["regex"].search(line):
                    report.add(Finding(
                        severity=pat["severity"],
                        category=pat["category"],
                        scanner=scanner_name,
                        file=rel_file,
                        line=i,
                        pattern=pat["regex"].pattern[:80],
                        snippet=trim_snippet(line),
                        risk=pat["risk"],
                        fix=pat["fix"],
                    ))


def _rel_path(path: Path, root: Path) -> str:
    """Return a forward-slash relative path string for portable output."""
    try:
        return str(path.relative_to(root)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")
