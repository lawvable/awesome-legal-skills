"""Accept conversion-artifact tracked changes (.doc -> .docx).

Usage: python clean_conversion_artifacts.py <file.docx>
                                            [--accept-conversion-artifacts]

Modifies the .docx in place. Blocks by default if author/ratio heuristics
suggest authored TC (a redline). See `skill-docs/01-setup-and-extract.md` for full guidance.
"""
import sys
import os
import re
import zipfile
import shutil

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



# Authors emitted by .doc -> .docx conversion pipelines (LibreOffice,
# MS Office). Real human-author names are NOT in this set.
ARTIFACT_AUTHORS = {'', 'Unknown', 'LibreOffice', 'OpenOffice',
                    'Microsoft Office', 'Office'}

def clean_revision_markup(xml_text):
    """Accept TC in raw XML. 4 repetitive blocks → one loop."""
    n = 0
    # 'u'=unwrap (keep content); 's'=strip (drop content)
    for tag, mode in (('w:ins', 'u'), ('w:moveTo', 'u'),
                      ('w:del', 's'), ('w:moveFrom', 's')):
        before = len(xml_text)
        xml_text = re.sub(rf'<{tag}\b[^>]*/>', '', xml_text)
        if mode == 'u':
            xml_text = re.sub(rf'<{tag}\b[^>]*>', '', xml_text)
            xml_text = re.sub(rf'</{tag}>', '', xml_text)
        else:
            xml_text = re.sub(rf'<{tag}\b[^>]*>.*?</{tag}>', '',
                              xml_text, flags=re.DOTALL)
        if len(xml_text) != before:
            n += 1
    before = len(xml_text)
    xml_text = re.sub(r'<w:del\s*/>', '', xml_text)
    xml_text = re.sub(
        r'<w:bookmarkStart[^>]*w:name="_GoBack"[^>]*/>', '', xml_text)
    for t in ('moveFromRangeStart', 'moveFromRangeEnd',
              'moveToRangeStart', 'moveToRangeEnd'):
        xml_text = re.sub(rf'<w:{t}[^>]*/>', '', xml_text)
    if len(xml_text) != before:
        n += 1
    return xml_text, n

def count_revision_elements(xml_text):
    """Count revision markup elements."""
    counts = {}
    for tag in ('w:ins', 'w:del', 'w:moveFrom', 'w:moveTo'):
        n = (len(re.findall(rf'<{tag}\b[^/]*[^/]>', xml_text))
             + len(re.findall(rf'<{tag}\b[^>]*/>', xml_text)))
        if n > 0:
            counts[tag] = n
    return counts

def extract_authors(xml_text):
    """w:author values across w:ins/w:del/w:moveFrom/w:moveTo."""
    authors = set()
    for m in re.finditer(
            r'<w:(?:ins|del|moveFrom|moveTo)\b[^>]*\bw:author="([^"]*)"',
            xml_text):
        authors.add(m.group(1))
    return sorted(authors)

def looks_like_real_editing(counts, authors):
    """Real authored TC has human authors and/or lopsided ratios."""
    for a in authors:
        if a not in ARTIFACT_AUTHORS:
            return True, f'author "{a}" is not a known conversion artifact'
    ins = counts.get('w:ins', 0)
    dels = counts.get('w:del', 0)
    if ins + dels >= 10:
        ratio = max(ins, dels) / max(min(ins, dels), 1)
        if ratio >= 5:
            return True, f'lopsided ratio (ins={ins}, del={dels}); ≥5:1'
    return False, None

def clean_docx(docx_path, accept=False):
    """Clean conversion artifacts from .docx in place."""
    with zipfile.ZipFile(docx_path, 'r') as zin:
        if 'word/document.xml' not in zin.namelist():
            print("No word/document.xml found in the .docx file.")
            return
        doc_xml = zin.read('word/document.xml').decode('utf-8')

    before = count_revision_elements(doc_xml)
    if not before:
        print("No revision markup found — file is already clean.")
        return

    authors = extract_authors(doc_xml)
    print(f"Found revision markup: {before}")
    print(f"Authors: {authors}")

    real, why = looks_like_real_editing(before, authors)
    if real and not accept:
        bar = "=" * 60
        print(
            f"\n{bar}\n"
            "[clean_conversion_artifacts] SKILL GATE FIRED — BLOCK.\n"
            f"  Reason: {why}\n  Counts: {before}\n  Authors: {authors}\n"
            "\n  Looks like authored TC, not conversion noise.\n"
            "  Accepting it would flatten the redline and the\n"
            "  translation would lose every ins/del. See skill-docs/\n"
            "  Step 1: if this is a redline, skip this script.\n"
            "  Override after inspection: --accept-conversion-artifacts.\n"
            f"{bar}", file=sys.stderr)
        sys.exit(2)

    cleaned_xml, _ = clean_revision_markup(doc_xml)
    after = count_revision_elements(cleaned_xml)
    if after:
        print(f"WARNING: Some revision markup remains: {after}")
    else:
        print("All revision markup accepted/removed.")

    tmp = docx_path + '.tmp'
    with zipfile.ZipFile(docx_path, 'r') as zin:
        with zipfile.ZipFile(tmp, 'w') as zout:
            for item in zin.infolist():
                if item.filename == 'word/document.xml':
                    zout.writestr(item, cleaned_xml.encode('utf-8'))
                else:
                    zout.writestr(item, zin.read(item.filename))
    shutil.move(tmp, docx_path)
    print(f"Cleaned: {docx_path}")

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    accept = '--accept-conversion-artifacts' in sys.argv[1:]
    if len(args) != 1:
        print("Usage: clean_conversion_artifacts.py <file.docx> "
              "[--accept-conversion-artifacts]")
        sys.exit(1)
    clean_docx(args[0], accept=accept)

# === SKILL FILE COMPLETE ===
