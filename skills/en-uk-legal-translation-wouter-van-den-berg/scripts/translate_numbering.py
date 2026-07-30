"""Translate numbering format strings in word/numbering.xml.

OOXML stores list/heading numbering definitions in word/numbering.xml.
Each numbering level has a w:lvlText element whose w:val attribute defines
the format string displayed as the list prefix — e.g. "%1. sz. Melléklet"
produces "1. sz. Melléklet", "2. sz. Melléklet", etc.

If these format strings contain source-language text, the translated document
will show mixed-language numbering (e.g. "Schedule 1. sz. Melléklet" or just
"1. sz. Melléklet" when only the paragraph body is translated). This script
extracts those format strings, applies a translation map, and writes the
modified numbering.xml.

Usage:
    python translate_numbering.py <original.docx> <output_numbering.xml> [--language <lang>]

The script also accepts a JSON file with custom translations:
    python translate_numbering.py <original.docx> <output_numbering.xml> --custom <translations.json>

The JSON format is: {"source pattern": "target pattern", ...}
where patterns can use %1, %2, etc. as numbering placeholders.
"""
import sys
import os
import re
import json
import zipfile
import xml.etree.ElementTree as ET

def _check_self_integrity():
    """Detect install-time truncation. Whole-file scan tolerates null-padding."""
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



W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

# Built-in translation maps per source language.
# Keys are lowercase source patterns (with %N placeholders preserved).
# Values are English replacements.
#
# The matching is case-insensitive on the source side but preserves the
# exact replacement string on the target side.

HUNGARIAN_MAP = {
    # Schedules / Annexes
    r'%(\d+)\.\s*sz\.\s*melléklet':  r'Schedule %\1',
    r'%(\d+)\.\s*melléklet':         r'Schedule %\1',
    r'melléklet\s*%(\d+)':           r'Schedule %\1',
    # Appendix
    r'%(\d+)\.\s*sz\.\s*függelék':   r'Appendix %\1',
    r'%(\d+)\.\s*függelék':          r'Appendix %\1',
    # Chapter
    r'%(\d+)\.\s*fejezet':           r'Chapter %\1',
    # Part
    r'%(\d+)\.\s*rész':              r'Part %\1',
    # Article (internal)
    r'%(\d+)\.\s*cikk':              r'Clause %\1',
    # Section
    r'%(\d+)\.\s*szakasz':           r'Section %\1',
    # Simple "sz." (abbreviation for "számú" = "numbered")
    r'%(\d+)\.\s*sz\.':              r'%\1.',
}

ITALIAN_MAP = {
    r'%(\d+)\.\s*allegato':          r'Schedule %\1',
    r'allegato\s*%(\d+)':            r'Schedule %\1',
    r'%(\d+)\.\s*appendice':         r'Appendix %\1',
    r'%(\d+)\.\s*capitolo':          r'Chapter %\1',
    r'%(\d+)\.\s*articolo':          r'Article %\1',
    r'%(\d+)\.\s*sezione':           r'Section %\1',
    r'%(\d+)\.\s*parte':             r'Part %\1',
}

GERMAN_MAP = {
    r'%(\d+)\.\s*anlage':            r'Schedule %\1',
    r'anlage\s*%(\d+)':              r'Schedule %\1',
    r'%(\d+)\.\s*anhang':            r'Appendix %\1',
    r'%(\d+)\.\s*abschnitt':         r'Section %\1',
    r'%(\d+)\.\s*teil':              r'Part %\1',
    r'%(\d+)\.\s*kapitel':           r'Chapter %\1',
    r'%(\d+)\.\s*artikel':           r'Article %\1',
}

FRENCH_MAP = {
    r'%(\d+)\.\s*annexe':            r'Schedule %\1',
    r'annexe\s*%(\d+)':              r'Schedule %\1',
    r'%(\d+)\.\s*appendice':         r'Appendix %\1',
    r'%(\d+)\.\s*chapitre':          r'Chapter %\1',
    r'%(\d+)\.\s*article':           r'Article %\1',
    r'%(\d+)\.\s*section':           r'Section %\1',
    r'%(\d+)\.\s*partie':            r'Part %\1',
}

SPANISH_MAP = {
    r'%(\d+)\.\s*anexo':             r'Schedule %\1',
    r'anexo\s*%(\d+)':               r'Schedule %\1',
    r'%(\d+)\.\s*apéndice':          r'Appendix %\1',
    r'%(\d+)\.\s*capítulo':          r'Chapter %\1',
    r'%(\d+)\.\s*artículo':          r'Article %\1',
    r'%(\d+)\.\s*sección':           r'Section %\1',
    r'%(\d+)\.\s*parte':             r'Part %\1',
}

PORTUGUESE_MAP = {
    r'%(\d+)\.\s*anexo':             r'Schedule %\1',
    r'anexo\s*%(\d+)':               r'Schedule %\1',
    r'%(\d+)\.\s*apêndice':          r'Appendix %\1',
    r'%(\d+)\.\s*capítulo':          r'Chapter %\1',
    r'%(\d+)\.\s*artigo':            r'Article %\1',
    r'%(\d+)\.\s*secção':            r'Section %\1',
    r'%(\d+)\.\s*parte':             r'Part %\1',
}

DUTCH_MAP = {
    r'%(\d+)\.\s*bijlage':           r'Schedule %\1',
    r'bijlage\s*%(\d+)':             r'Schedule %\1',
    r'%(\d+)\.\s*aanhangsel':        r'Appendix %\1',
    r'%(\d+)\.\s*hoofdstuk':         r'Chapter %\1',
    r'%(\d+)\.\s*artikel':           r'Article %\1',
    r'%(\d+)\.\s*afdeling':          r'Section %\1',
    r'%(\d+)\.\s*deel':              r'Part %\1',
}

POLISH_MAP = {
    r'%(\d+)\.\s*załącznik':         r'Schedule %\1',
    r'załącznik\s*%(\d+)':           r'Schedule %\1',
    r'%(\d+)\.\s*dodatek':           r'Appendix %\1',
    r'%(\d+)\.\s*rozdział':          r'Chapter %\1',
    r'%(\d+)\.\s*artykuł':           r'Article %\1',
    r'%(\d+)\.\s*sekcja':            r'Section %\1',
    r'%(\d+)\.\s*część':             r'Part %\1',
}

FINNISH_MAP = {
    r'%(\d+)\.\s*liite':             r'Schedule %\1',
    r'liite\s*%(\d+)':               r'Schedule %\1',
    r'%(\d+)\.\s*lisäys':            r'Appendix %\1',
    r'%(\d+)\.\s*luku':              r'Chapter %\1',
    r'%(\d+)\.\s*artikla':           r'Article %\1',
    r'%(\d+)\.\s*jakso':             r'Section %\1',
    r'%(\d+)\.\s*osa':               r'Part %\1',
}

LANGUAGE_MAPS = {
    'hungarian': HUNGARIAN_MAP,
    'italian': ITALIAN_MAP,
    'german': GERMAN_MAP,
    'french': FRENCH_MAP,
    'spanish': SPANISH_MAP,
    'portuguese': PORTUGUESE_MAP,
    'dutch': DUTCH_MAP,
    'polish': POLISH_MAP,
    'finnish': FINNISH_MAP,
}

def detect_language_from_numbering(numbering_xml_text):
    """Try to auto-detect the source language from numbering format strings."""
    text_lower = numbering_xml_text.lower()
    scores = {}
    for lang, tmap in LANGUAGE_MAPS.items():
        score = 0
        for pattern in tmap:
            # Convert regex pattern to a simpler search
            simple = re.sub(r'%\(\\d\+\)', '%', pattern)
            simple = re.sub(r'\\[sd.]', '.', simple)
            # Extract just the word parts
            words = re.findall(r'[a-záéíóöőúüűàèìòùâêîôûäëïöüçñãõżźćśłńęąščřžďťňůĺĽ]+', pattern)
            for word in words:
                if len(word) > 2 and word in text_lower:
                    score += 1
        if score > 0:
            scores[lang] = score
    if scores:
        return max(scores, key=scores.get)
    return None

def translate_numbering(orig_docx, output_xml, language=None, custom_map=None):
    """Extract, translate, and write word/numbering.xml."""

    # Read numbering.xml from the .docx
    with zipfile.ZipFile(orig_docx, 'r') as zf:
        if 'word/numbering.xml' not in zf.namelist():
            print("No word/numbering.xml found in this .docx — nothing to translate.")
            return False
        numbering_bytes = zf.read('word/numbering.xml')

    numbering_text = numbering_bytes.decode('utf-8')

    # Auto-detect language if not specified
    if language is None:
        language = detect_language_from_numbering(numbering_text)
        if language:
            print(f"Auto-detected numbering language: {language}")
        else:
            print("Could not auto-detect numbering language. No translations applied.")
            if not custom_map:
                # Write unchanged
                with open(output_xml, 'w', encoding='utf-8') as f:
                    f.write(numbering_text)
                return False

    # Build translation map
    tmap = {}
    if language and language.lower() in LANGUAGE_MAPS:
        tmap.update(LANGUAGE_MAPS[language.lower()])
    if custom_map:
        tmap.update(custom_map)

    if not tmap:
        print(f"No translation map for language '{language}'. Writing unchanged.")
        with open(output_xml, 'w', encoding='utf-8') as f:
            f.write(numbering_text)
        return False

    # Find and translate w:lvlText val attributes
    # These look like: <w:lvlText w:val="%1. sz. Melléklet"/>
    changes = 0

    def replace_lvltext(match):
        nonlocal changes
        prefix = match.group(1)   # everything before the val content
        val = match.group(2)      # the format string
        suffix = match.group(3)   # closing quote + rest

        translated = val
        for pattern, replacement in tmap.items():
            new_val, n = re.subn(pattern, replacement, translated, flags=re.IGNORECASE)
            if n > 0:
                translated = new_val
                break

        if translated != val:
            changes += 1
            print(f"  Translated: '{val}' → '{translated}'")
            return f'{prefix}{translated}{suffix}'
        return match.group(0)

    # Match w:lvlText elements with their val attribute
    numbering_text = re.sub(
        r'(<w:lvlText\s+w:val=")([^"]*?)(")',
        replace_lvltext,
        numbering_text
    )

    # Also check for any other translatable text in w:t elements within numbering.xml
    # (some documents embed text directly in numbering definitions)

    os.makedirs(os.path.dirname(output_xml) or '.', exist_ok=True)
    with open(output_xml, 'w', encoding='utf-8') as f:
        f.write(numbering_text)

    if changes:
        print(f"\nTranslated {changes} numbering format string(s).")
    else:
        print("\nNo translatable format strings found (all pure numeric/symbol patterns).")

    return changes > 0

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Translate numbering format strings in word/numbering.xml')
    parser.add_argument('original', help='Original .docx file')
    parser.add_argument('output', help='Output numbering.xml path')
    parser.add_argument('--language', help='Source language (hungarian, italian, german, french, spanish, portuguese, dutch, polish, finnish)', default=None)
    parser.add_argument('--custom', help='JSON file with custom translations', default=None)
    args = parser.parse_args()

    custom = None
    if args.custom:
        with open(args.custom) as f:
            custom = json.load(f)

    translate_numbering(args.original, args.output, language=args.language, custom_map=custom)

# === SKILL FILE COMPLETE ===
