#!/usr/bin/env python3
"""Validate a skill folder against Lawve packaging requirements.

Usage: python validate.py <skill-folder>

Read-only: reads the folder it is pointed at, writes nothing, no network calls,
spawns nothing, standard library only. Exit 0 on a clean pass, 1 otherwise.
Mirrors the manual checklist in resources/requirements.md.
"""
import os
import re
import sys

DESC_LIMIT = 1024
# Built by concatenation so this file never matches its own token list.
LEFTOVER_TOKENS = ["refer" + "ences/", "mcp" + "__", "CLAUDE_PLUGIN" + "_ROOT", ".mcp" + ".json"]
# Files may opt out of the leftover-token scan (documentation that discusses
# the tokens) by containing this marker, e.g. in an HTML comment. Exemptions
# are reported, never silent.
EXEMPT_MARKER = "token-scan:" + " exempt"
BUNDLE_DIRS = ["resources", "scripts", "assets", "templates"]
SCRIPT_RED_FLAGS = [
    "url" + "lib", "requ" + "ests", "sock" + "et", "http." + "client",
    "subpro" + "cess", "os.sys" + "tem", "ev" + "al(", "ex" + "ec(",
    "__imp" + "ort__",
]

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def parse_frontmatter(text):
    """Minimal frontmatter reader. Returns (description, has_metadata, meta_keys, name)."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, False, [], None
    fm = m.group(1)
    name_m = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    name = name_m.group(1).strip("\"'") if name_m else None
    # description: single line, or folded block (>- / >) of indented lines
    desc = None
    dm = re.search(r"^description:\s*(.*)$", fm, re.M)
    if dm:
        first = dm.group(1).strip()
        if first in (">", ">-", "|", "|-", ""):
            lines = []
            started = False
            for line in fm[dm.end():].splitlines():
                if line.startswith("  ") and line.strip():
                    lines.append(line.strip())
                    started = True
                elif started or (line.strip() and not line.startswith(" ")):
                    break
            desc = " ".join(lines)
        else:
            desc = first
    meta_keys = []
    mm = re.search(r"^metadata:\s*$", fm, re.M)
    if mm:
        for line in fm[mm.end():].splitlines():
            km = re.match(r"^\s{2,}(\w+):", line)
            if km:
                meta_keys.append(km.group(1))
            elif line.strip() and not line.startswith(" "):
                break
    return desc, bool(mm), meta_keys, name


def main(folder):
    folder = folder.rstrip("/")
    base = os.path.basename(folder)
    skill_md = os.path.join(folder, "SKILL.md")

    # 1. Structure
    if not os.path.isfile(skill_md):
        err("SKILL.md missing at folder root")
        return
    text = open(skill_md, encoding="utf-8").read()

    desc, has_meta, meta_keys, name = parse_frontmatter(text)

    # 2. Frontmatter
    if name is None:
        err("frontmatter: no name")
    elif name != base:
        err(f"frontmatter name '{name}' != folder name '{base}'")
    if name and not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        err(f"name '{name}' is not lowercase-hyphen")
    if desc is None:
        err("frontmatter: no description")
    else:
        if len(desc) > DESC_LIMIT:
            err(f"description {len(desc)} chars > {DESC_LIMIT} limit")
        else:
            print(f"  description: {len(desc)}/{DESC_LIMIT} chars")
        if re.search(r"[\U0001F300-\U0001FAFF✅❌❗]", desc):
            warn("description contains emoji")
    if not has_meta:
        err("frontmatter: no metadata block")
    else:
        for k in ("author", "license", "version"):
            if k not in meta_keys:
                err(f"metadata missing '{k}'")

    # 3. Links resolve
    refs = set()
    for d in BUNDLE_DIRS:
        refs |= set(re.findall(rf"{d}/[\w./-]+\.\w+", text))
    for r in sorted(refs):
        if not os.path.exists(os.path.join(folder, r)):
            err(f"broken link: {r}")

    # 4. Orphans — every bundled file referenced from SKILL.md or a referenced file
    all_text = text
    for r in refs:
        p = os.path.join(folder, r)
        if os.path.exists(p) and p.endswith((".md", ".txt")):
            try:
                all_text += open(p, encoding="utf-8").read()
            except UnicodeDecodeError:
                pass
    for d in BUNDLE_DIRS:
        dp = os.path.join(folder, d)
        if os.path.isdir(dp):
            for root, _, files in os.walk(dp):
                for f in files:
                    if f not in all_text:
                        err(f"orphaned file: {os.path.relpath(os.path.join(root, f), folder)}")

    # 5. Leftover tokens (skip exempt documentation files, and say so)
    scan_text = text if EXEMPT_MARKER not in text else ""
    exempt = ["SKILL.md"] if EXEMPT_MARKER in text else []
    for r in refs:
        p = os.path.join(folder, r)
        if os.path.exists(p) and p.endswith((".md", ".txt")):
            try:
                body = open(p, encoding="utf-8").read()
            except UnicodeDecodeError:
                continue
            if EXEMPT_MARKER in body:
                exempt.append(r)
            else:
                scan_text += body
    if exempt:
        print(f"  note: exempt from token scan: {', '.join(sorted(exempt))}")
    for tok in LEFTOVER_TOKENS:
        n = scan_text.count(tok)
        if n:
            err(f"leftover '{tok}' ({n} occurrence(s))")

    # 6. LICENSE / NOTICE / limitations
    if not os.path.isfile(os.path.join(folder, "LICENSE")):
        err("LICENSE missing (full licence text, inside the folder)")
    if not os.path.isfile(os.path.join(folder, "NOTICE")):
        warn("NOTICE missing (attribution / origin / code disclosure)")
    if not re.search(r"^#+.*[Ll]imitations", text, re.M):
        err("no Limitations (risks) section in SKILL.md")

    # 7. Script red flags
    sp = os.path.join(folder, "scripts")
    if os.path.isdir(sp):
        for root, _, files in os.walk(sp):
            for f in files:
                if f.endswith(".py"):
                    src = open(os.path.join(root, f), encoding="utf-8").read()
                    for flag in SCRIPT_RED_FLAGS:
                        if flag in src:
                            warn(f"scripts/{f}: contains '{flag}' — verify and disclose in NOTICE")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        print("usage: python validate.py <skill-folder>")
        sys.exit(2)
    print(f"validating {sys.argv[1]}")
    main(sys.argv[1])
    for w in warnings:
        print(f"  WARN: {w}")
    for e in errors:
        print(f"  FAIL: {e}")
    if errors:
        print(f"RESULT: {len(errors)} error(s), {len(warnings)} warning(s)")
        sys.exit(1)
    print(f"RESULT: clean pass ({len(warnings)} warning(s))")
    sys.exit(0)
