"""Pre-apply gate: BLOCK if a detected definitions section in
paragraphs.json has any paragraph without `en_runs`(gate introduced) and  (extracted to standalone file).

Auto-invoked by apply_translations_textmatch.py before the main
translation step. Operators don't run this directly; the subprocess
call from apply produces the BLOCK message and exit code.

Usage:
    python validate_en_runs.py <paragraphs.json> [--allow-bold-loss]

Exit codes:
    0 — PASS (no definitions section, or all paragraphs have en_runs)
    1 — WARN (--allow-bold-loss passed; missing en_runs ignored)
    2 — BLOCK (missing en_runs without override)
"""
import argparse
import json
import os
import sys

def _check_self_integrity():
    """Rev29: detect install-time truncation"""
    try:
        with open(os.path.abspath(__file__), 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError:
        return
    if '\n# === SKILL FILE COMPLETE ===' not in content:
        msg = (
            "\n" + "=" * 60 + "\n"
            "[skill] FILE INTEGRITY CHECK FAILED — script truncated.\n"
            f"  File: {os.path.abspath(__file__)}\n"
            f"  Size: {len(content):,} bytes (sentinel marker missing).\n"
            "  Re-install the skill from the .skill / .zip archive.\n"
            + "=" * 60 + "\n"
        )
        print(msg, file=sys.stderr)
        sys.exit(3)


_check_self_integrity()

def main():
    parser = argparse.ArgumentParser(
        description='Pre-apply gate: BLOCK if a detected definitions section '
                    'has paragraphs without en_runs.')
    parser.add_argument('paragraphs_json', help='Path to paragraphs.json')
    parser.add_argument('--allow-bold-loss', action='store_true',
                        help='Bypass the gate. Use only when bold loss is '
                             'genuinely acceptable (e.g., simple drafts).')
    args = parser.parse_args()

    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import reorder_definitions

    with open(args.paragraphs_json, 'r', encoding='utf-8') as f:
        paras = json.load(f)

    # Prefer en text; fall back to source text for untranslated paragraphs.
    texts = []
    for p in paras:
        en = (p.get('en') or '').strip()
        src = (p.get('text') or '').strip()
        texts.append(en if en else src)

    start, end = reorder_definitions.find_definitions_section_in_texts(texts)
    if start is None:
        return 0

    missing = []
    for i in range(start, end):
        if i >= len(paras):
            break
        p = paras[i]
        en_runs = p.get('en_runs')
        if not en_runs:
            missing.append(p.get('idx', i))

    if not missing:
        return 0

    if args.allow_bold_loss:
        print(
            "\n" + "=" * 60 + "\n"
            f"[validate_en_runs] WARNING — definitions section at paragraphs "
            f"{start}-{end - 1} has {len(missing)} entries without "
            f"en_runs.\n"
            f"--allow-bold-loss was passed; proceeding anyway. Bold/italic\n"
            f"on defined terms will be missing in the output.\n"
            f"Affected indices: {missing[:20]}"
            + (f" ... +{len(missing) - 20} more" if len(missing) > 20 else "")
            + "\n" + "=" * 60 + "\n",
            file=sys.stderr,
        )
        return 1

    print(
        "\n" + "=" * 60 + "\n"
        f"[validate_en_runs] SKILL GATE FIRED — INTENTIONAL BLOCK, NOT A SCRIPT ERROR.\n"
        f"The script is working as designed. The skill is enforcing a rule;\n"
        f"read the explanation below, fix paragraphs.json, then re-run apply.\n"
        f"Do NOT work around this by patching the script or skipping gates —\n"
        f"doing so silently ships output below the quality the skill is\n"
        f"designed to deliver.\n"
        + "=" * 60 + "\n"
        f"[validate_en_runs] BLOCK — definitions section detected without en_runs.\n"
        f"\n"
        f"A definitions section was detected at paragraphs {start}-{end - 1}\n"
        f"by the heading + predicate-cluster pattern. {len(missing)} of the\n"
        f"{end - start} paragraphs in the section lack `en_runs`.\n"
        f"\n"
        f"Without en_runs on each definition paragraph, apply emits\n"
        f'<w:b w:val="0"/> to prevent style-bold from leaking into body\n'
        f"text — and that off-override strips the style-provided bold-italic\n"
        f"that defines the term in this document family. The defined terms\n"
        f"will render plain in the output. Re-author paragraphs.json to\n"
        f"include en_runs for every paragraph in the section, e.g.:\n"
        f"\n"
        f'  "en_runs": [\n'
        f'    {{"start": 0,           "end": <term_end>, '
        f'"bold": true,  "italic": true}},\n'
        f'    {{"start": <term_end>, "end": <text_len>, '
        f'"bold": false, "italic": false}}\n'
        f"  ]\n"
        f"\n"
        f"Affected paragraph indices ({len(missing)}):\n"
        f"  {missing[:30]}"
        + (f"\n  ... +{len(missing) - 30} more" if len(missing) > 30 else "")
        + "\n"
        f"\n"
        f"To override (only when bold loss is genuinely acceptable), pass\n"
        f"--allow-bold-loss to apply_translations_textmatch.py.\n"
        + "=" * 60 + "\n",
        file=sys.stderr,
    )
    return 2

if __name__ == '__main__':
    _check_self_integrity()
    sys.exit(main())

# === SKILL FILE COMPLETE ===
