#!/usr/bin/env python3
"""Normalize footnote typography in a .docx (typically the pandoc-produced
clean copy, whose --reference-doc may lack footnote styles entirely).

Usage:
    python polish_footnotes.py in.docx out.docx [--size 18] [--no-period]

What it does:
  1. styles.xml — define (or replace) FootnoteReference as a superscript
     character style and FootnoteText as a paragraph style at --size
     half-points (default 18 = 9pt). Documents that format footnotes with
     direct run properties often have neither style, so runs that reference
     them render at full body size on the baseline.
  2. footnotes.xml — for each real footnote: strip the superscript style
     from the note's own number mark (so it renders full-size at note size,
     law-review fashion) and insert a period after it: "27. See ...".
     Body calls keep the FootnoteReference style and become superscript.

Skip the period with --no-period for house styles that use a bare number.
"""
import argparse
import os
import re
import shutil
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def w(tag):
    return f"{{{W}}}{tag}"


def register_namespaces(text):
    for pfx, uri in re.findall(r'xmlns:([A-Za-z0-9]+)="([^"]+)"', text[:8192]):
        ET.register_namespace(pfx, uri)
    ET.register_namespace("w", W)


def preserve_root(out_bytes, original_text, rootname):
    out = out_bytes.decode("utf-8")
    m_orig = re.search(rf"<w:{rootname}[^>]*>", original_text)
    if not m_orig:
        return out
    start = out.index("?>") + 2
    m_new = re.search(r"<[^>]+>", out[start:])
    return out[:start + m_new.start()] + m_orig.group(0) + out[start + m_new.end():]


STYLE_REF = """<w:style w:type="character" w:styleId="FootnoteReference">
<w:name w:val="footnote reference"/><w:uiPriority w:val="99"/>
<w:rPr><w:vertAlign w:val="superscript"/></w:rPr></w:style>"""

STYLE_TEXT = """<w:style w:type="paragraph" w:styleId="FootnoteText">
<w:name w:val="footnote text"/><w:uiPriority w:val="99"/>
<w:pPr><w:spacing w:after="40" w:line="240" w:lineRule="auto"/></w:pPr>
<w:rPr><w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/></w:rPr></w:style>"""


def safe_extract(zf, destination):
    """Extract a caller-supplied docx without path traversal or symlinks."""
    root = os.path.realpath(destination) + os.sep
    for info in zf.infolist():
        target = os.path.realpath(os.path.join(destination, info.filename))
        if not target.startswith(root):
            raise ValueError(f"unsafe archive path: {info.filename!r}")
        mode = (info.external_attr >> 16) & 0o170000
        if mode == 0o120000:
            raise ValueError(f"symlink not allowed in docx: {info.filename!r}")
    zf.extractall(destination)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("infile")
    ap.add_argument("outfile")
    ap.add_argument("--size", type=int, default=18,
                    help="footnote text size in half-points (18 = 9pt)")
    ap.add_argument("--no-period", action="store_true")
    ap.add_argument("--endnotes", action="store_true")
    args = ap.parse_args()

    part = "endnotes" if args.endnotes else "footnotes"
    note_el = "endnote" if args.endnotes else "footnote"
    ref_mark = "endnoteRef" if args.endnotes else "footnoteRef"

    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(args.infile) as z:
        try:
            safe_extract(z, tmp)
        except ValueError as exc:
            shutil.rmtree(tmp)
            ap.error(str(exc))

    # --- 1. styles.xml: drop any existing definitions, append proper ones
    st_path = os.path.join(tmp, "word", "styles.xml")
    st = open(st_path, encoding="utf-8").read()
    for sid in ("FootnoteReference", "FootnoteText"):
        st = re.sub(
            rf'<w:style [^>]*w:styleId="{sid}".*?</w:style>', "", st, flags=re.S)
    add = STYLE_REF + STYLE_TEXT.format(sz=args.size)
    if args.endnotes:
        add = add.replace("Footnote", "Endnote").replace("footnote", "endnote")
    st = st.replace("</w:styles>", add + "</w:styles>")
    open(st_path, "w", encoding="utf-8").write(st)

    # --- 2. footnotes.xml: number style + period
    fn_path = os.path.join(tmp, "word", f"{part}.xml")
    if os.path.exists(fn_path):
        orig = open(fn_path, encoding="utf-8").read()
        register_namespaces(orig)
        tree = ET.parse(fn_path)
        root = tree.getroot()
        for note in root.findall(w(note_el)):
            try:
                if int(note.get(w("id"))) <= 0:
                    continue
            except (TypeError, ValueError):
                continue
            for p in note.findall(w("p")):
                for scope in [p] + [el for el in p if el.tag in (w("ins"),)]:
                    for r in list(scope):
                        if r.tag != w("r") or r.find(w(ref_mark)) is None:
                            continue
                        # note number: explicit superscript + note size so
                        # Word and LibreOffice render identically (style
                        # references may be undefined in this document)
                        rpr = r.find(w("rPr"))
                        if rpr is None:
                            rpr = ET.Element(w("rPr"))
                            r.insert(0, rpr)
                        for rs in rpr.findall(w("rStyle")):
                            rpr.remove(rs)
                        for va in rpr.findall(w("vertAlign")):
                            rpr.remove(va)
                        # schema order: sz, szCs before vertAlign
                        for tag in ("sz", "szCs"):
                            if rpr.find(w(tag)) is None:
                                e = ET.SubElement(rpr, w(tag))
                                e.set(w("val"), str(args.size))
                        va = ET.SubElement(rpr, w("vertAlign"))
                        va.set(w("val"), "superscript")
                        if not args.no_period:
                            dot = ET.Element(w("r"))
                            if rpr is not None:
                                dot.append(ET.fromstring(ET.tostring(rpr)))
                            t = ET.SubElement(dot, w("t"))
                            t.text = "."
                            scope.insert(list(scope).index(r) + 1, dot)
        import io
        buf = io.BytesIO()
        tree.write(buf, xml_declaration=True, encoding="UTF-8")
        open(fn_path, "w", encoding="utf-8").write(
            preserve_root(buf.getvalue(), orig, part))

    # --- rezip
    if os.path.exists(args.outfile):
        os.remove(args.outfile)
    with zipfile.ZipFile(args.outfile, "w", zipfile.ZIP_DEFLATED) as zf:
        for base, _, files in os.walk(tmp):
            for f in files:
                full = os.path.join(base, f)
                zf.write(full, os.path.relpath(full, tmp))
    shutil.rmtree(tmp)
    print(f"polished: styles injected (size {args.size} half-points), "
          f"note numbers {'left bare' if args.no_period else 'given periods'}")


if __name__ == "__main__":
    main()
