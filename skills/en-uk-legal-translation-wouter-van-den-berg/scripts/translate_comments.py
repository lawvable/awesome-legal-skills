"""Translate text inside word/comments.xml while preserving namespace declarations.

OOXML stores Word comments (margin annotations) in word/comments.xml. Because
the main translation pipeline only processes document.xml, comment text is
silently left in the source language. This is a HIGH severity defect — comments
are highly visible to anyone reviewing the document.

============================================================================
WHY THIS SCRIPT EXISTS — DO NOT RE-INVENT WITH ElementTree
============================================================================

Earlier versions of the skill told the user to translate comments.xml with
ElementTree and graft the original root-element opening tag back on. That
approach is WRONG and produces .docx files that Word refuses to open with an
"unreadable content" error.

ElementTree renames namespace prefixes during serialisation:
  * `w14:paraId`  -> `ns2:paraId`
  * `mc:Ignorable`-> `ns1:Ignorable`
  * ... and so on, deep inside the body of the XML.

Grafting the original root tag back restores the namespace *declarations* at
the top, but the body still uses `ns1:`, `ns2:`, etc. — prefixes that are no
longer declared anywhere. Word reads the file, finds unbound prefixes, and
refuses to open it.

The only reliable fix is to avoid XML parsing altogether for this file:
match the text inside <w:t> and <w:delText> nodes with a regex and replace
just that text. Everything else in the file passes through byte-for-byte.

============================================================================

Usage
-----
    # Step 1 — list source comments so you can draft the translations
    python translate_comments.py <original.docx> --list

    # Step 2 — supply translations via a JSON file (comment-id -> English)
    python translate_comments.py <original.docx> <output_dir> --translations comments.json

Inputs
------
    <original.docx>     The source-language .docx
    <output_dir>        The skill work directory (e.g. workdir/final).
                        The translated file is written to
                        <output_dir>/word/comments.xml.

Translations JSON format
------------------------
    {
      "19": "To be named as \"the Plots\"?",
      "29": "To be discussed with Acme",
      "31": "Possibly include a definition",
      ...
    }

    Keys are comment IDs as strings (use quotes even if the ID is numeric).
    Values are the English translation of the full comment body. One entry
    per comment — any cross-run formatting inside the comment is flattened.

How text replacement works
--------------------------
    For each <w:comment w:id="N"> block, the script finds the first <w:t>
    inside it and puts the full English translation there. Every other <w:t>
    and every <w:delText> inside the same block is emptied. This is the
    correct treatment for comment bodies, because comments rarely carry
    meaningful cross-run formatting and the reviewer only reads the
    concatenated text.

Output
------
    <output_dir>/word/comments.xml

    The repack script handles comments.xml automatically if you pass
    --comments-dir. If your repack command does not support that flag, add
    comments.xml manually after repacking:

        with zipfile.ZipFile(output_docx, 'a') as zout:
            zout.writestr('word/comments.xml', open(translated_comments_path,'rb').read())
"""
import sys
import os
import re
import json
import zipfile
import argparse

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



# Match <w:t ...>TEXT</w:t>.  Captures: opening tag, text, closing tag.
_WT_RE = re.compile(r'(<w:t(?:\s[^>]*)?>)([^<]*)(</w:t>)')
# Match <w:delText ...>TEXT</w:delText>
_WDELTEXT_RE = re.compile(r'(<w:delText(?:\s[^>]*)?>)([^<]*)(</w:delText>)')
# Match a whole <w:comment ... w:id="X" ...> ... </w:comment> block
_COMMENT_RE = re.compile(
    r'(<w:comment\b[^>]*?\sw:id="([^"]+)"[^>]*>)(.*?)(</w:comment>)',
    re.DOTALL,
)

def parse_source_comments(xml_text):
    """Return [(comment_id, concatenated_source_text), ...] in document order."""
    out = []
    for m in _COMMENT_RE.finditer(xml_text):
        cid = m.group(2)
        body = m.group(3)
        texts = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', body)
        out.append((cid, ''.join(texts)))
    return out

def _xml_escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def _ensure_xml_space_preserve(opening_tag):
    """Insert xml:space="preserve" into a <w:t ...> opening tag if missing."""
    if 'xml:space' in opening_tag:
        return opening_tag
    # opening_tag is e.g. '<w:t>' or '<w:t rsidR="..">'
    return opening_tag[:-1] + ' xml:space="preserve">'

def translate_comments_xml(xml_text, translations):
    """Replace the text in each <w:comment> whose id is in translations.

    Returns (new_xml_text, translated_ids, untranslated_ids).
    """
    translated = []
    untranslated = []

    def rewrite_comment(m):
        opening, cid, body, closing = m.group(1), m.group(2), m.group(3), m.group(4)
        if cid not in translations:
            # Leave comments without a translation alone so the reviewer can
            # see which ones still need work. parse_source_comments will
            # report them in untranslated_ids.
            src = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', body))
            if src.strip():
                untranslated.append(cid)
            return m.group(0)

        new_text = translations[cid]
        translated.append(cid)
        first = {'done': False}

        def wt(mm):
            op, _txt, cl = mm.group(1), mm.group(2), mm.group(3)
            if not first['done']:
                first['done'] = True
                return _ensure_xml_space_preserve(op) + _xml_escape(new_text) + cl
            # Empty out subsequent <w:t> runs in this comment block.
            return op + cl

        def dt(mm):
            op, _txt, cl = mm.group(1), mm.group(2), mm.group(3)
            return op + cl

        new_body = _WT_RE.sub(wt, body)
        new_body = _WDELTEXT_RE.sub(dt, new_body)
        if not first['done']:
            # The comment had no <w:t> at all (unusual) — skip silently.
            translated.pop()
            return m.group(0)
        return opening + new_body + closing

    new_xml = _COMMENT_RE.sub(rewrite_comment, xml_text)
    return new_xml, translated, untranslated

def main():
    p = argparse.ArgumentParser(
        description='Translate text inside word/comments.xml without mangling namespaces.'
    )
    p.add_argument('original', help='Original .docx file')
    p.add_argument(
        'output_dir',
        nargs='?',
        help='Output directory — translated file written to <dir>/word/comments.xml',
    )
    p.add_argument(
        '--translations',
        help='JSON file mapping comment IDs (strings) to English translations',
    )
    p.add_argument(
        '--list',
        action='store_true',
        help='List source comments and exit (to help draft the translations JSON)',
    )
    args = p.parse_args()

    with zipfile.ZipFile(args.original, 'r') as zf:
        if 'word/comments.xml' not in zf.namelist():
            print('No word/comments.xml found in this .docx — nothing to translate.')
            return 0
        xml_text = zf.read('word/comments.xml').decode('utf-8')

    if args.list:
        # Surface the same English-passthrough rule the body translator
        # already follows, at the moment the operator is about to decide
        # what to write into the translations JSON. No detection, no
        # tagging — just a reminder. If a comment below is already in
        # English, copy it verbatim into "en"; do not rewrite or polish.
        print(
            'REMINDER: If a comment below is already in English, copy the source\n'
            "into 'en' verbatim. Do not rewrite or polish — the parties wrote those\n"
            'words and will read them back.\n'
        )
        for cid, text in parse_source_comments(xml_text):
            if text.strip():
                print(f'[{cid}] {text}')
        return 0

    if not args.output_dir:
        p.error('output_dir is required (unless --list is used)')
    if not args.translations:
        p.error('--translations is required (unless --list is used)')

    with open(args.translations, 'r', encoding='utf-8') as f:
        translations = {str(k): v for k, v in json.load(f).items()}

    new_xml, translated, untranslated = translate_comments_xml(xml_text, translations)

    out_path = os.path.join(args.output_dir, 'word', 'comments.xml')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'wb') as f:
        f.write(new_xml.encode('utf-8'))

    total_with_text = sum(
        1 for _, t in parse_source_comments(xml_text) if t.strip()
    )
    print(f'Wrote translated comments.xml -> {out_path}')
    print(f'  {len(translated)} of {total_with_text} source comments translated.')
    if untranslated:
        print(
            f'  WARNING: {len(untranslated)} comment(s) without a translation: '
            f'{untranslated[:20]}'
        )
        print(
            '           Add entries for these IDs to the translations JSON and re-run.'
        )

    # Quick self-check: make sure no unbound prefixes ended up in the output.
    # Find the root element (first `<w:comments ...>` or similar) and inspect
    # only its namespace declarations.
    root_match = re.search(r'<w:comments\b[^>]*>', new_xml)
    declared = set()
    if root_match:
        declared = set(re.findall(r'xmlns:(\w+)=', root_match.group(0)))
    used = set(re.findall(r'<(\w+):', new_xml)) | set(
        re.findall(r'\s(\w+):[A-Za-z]', new_xml)
    )
    unbound = used - declared - {'xml', 'xmlns'}
    if unbound:
        print(f'  ERROR: unbound namespace prefix(es) in output: {sorted(unbound)}')
        print('         This .docx will not open in Word. Re-run or file a bug.')
        return 2

    return 0

if __name__ == '__main__':
    sys.exit(main())

# === SKILL FILE COMPLETE ===
