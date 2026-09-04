#!/usr/bin/env python3
"""Apply footnote-relegation moves to an unpacked .docx as tracked changes.

Usage:
    python docx_redline.py unpacked_dir plan.json [--endnotes]

plan.json:
{
  "author": "footnote-relegator",
  "date": "2026-01-01T00:00:00Z",          // optional
  "moves": [
    {"delete": "<exact body text>",          // new-note move
     "anchor_after": "<exact text ending where the note ref goes>",
     "note": "<footnote text>"},
    {"delete": "<exact body text>",          // merge move: append to an
     "merge_note_contains": "<substring>",   // existing footnote instead of
     "note": "<text appended to that note>"},// creating a new one
    {"replace_find": "<exact body text>",    // tracked replacement (seam
     "replace_with": "<replacement text>"}   // repair): del + ins inline
  ]
}

New-note moves wrap the deleted text in <w:del>, insert an ins-marked
footnote reference after anchor_after, and append an ins-marked footnote to
word/footnotes.xml (creating that part, its relationship, and its
content-type entry if absent). Merge moves locate the existing footnote whose
text contains merge_note_contains (must match exactly one) and append the
note text there as an ins-marked run — no new reference is created, since the
anchor already carries one. Replace moves record a tracked substitution.

Each plan string must occur exactly once within one paragraph. The script can
match across consecutive text runs; failures are reported per move and do not
stop other moves.
"""

import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
CT = "http://schemas.openxmlformats.org/package/2006/content-types"
ET.register_namespace("w", W)
ET.register_namespace("r", R)


def w(tag):
    return f"{{{W}}}{tag}"


EMPTY_FOOTNOTES = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:footnotes xmlns:w="{W}">
<w:footnote w:type="separator" w:id="-1"><w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr><w:r><w:separator/></w:r></w:p></w:footnote>
<w:footnote w:type="continuationSeparator" w:id="0"><w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr><w:r><w:continuationSeparator/></w:r></w:p></w:footnote>
</w:footnotes>"""


def parse(path):
    # register every prefix the file declares so ET serializes attributes
    # (e.g. w14:paraId) with their original prefixes instead of ns0/ns1/...
    head = open(path, encoding="utf-8").read(8192)
    for pfx, uri in re.findall(r'xmlns:([A-Za-z0-9]+)="([^"]+)"', head):
        ET.register_namespace(pfx, uri)
    tree = ET.parse(path)
    return tree


def write_preserving_root(tree, path, original_text):
    """ET.write drops xmlns declarations it considers unused, which breaks
    mc:Ignorable. Restore the original root open tag after serializing."""
    import io
    buf = io.BytesIO()
    tree.write(buf, xml_declaration=True, encoding="UTF-8")
    out = buf.getvalue().decode("utf-8")
    m_orig = re.search(r"<w:(document|footnotes|endnotes)[^>]*>", original_text)
    m_new = re.search(r"<[^?!][^>]*>", out[out.index("?>") + 2:])
    if m_orig:
        start = out.index("?>") + 2
        m_new = re.search(r"<[^>]+>", out[start:])
        out = out[:start + m_new.start()] + m_orig.group(0) + out[start + m_new.end():]
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)


def iter_runs(root):
    """Yield (paragraph, run) for every run directly under paragraphs."""
    for p in root.iter(w("p")):
        for r in list(p):
            if r.tag == w("r"):
                yield p, r
            elif r.tag in (w("ins"), w("del")):
                for rr in list(r):
                    if rr.tag == w("r"):
                        yield p, rr


def run_text(r):
    t = r.find(w("t"))
    return t.text or "" if t is not None else ""


def find_unique(root, needle):
    """Find (paragraph, run, start_index) of the unique occurrence of needle
    within a single run's text. Returns error string on failure."""
    hits = []
    for p, r in iter_runs(root):
        txt = run_text(r)
        start = 0
        while True:
            i = txt.find(needle, start)
            if i == -1:
                break
            hits.append((p, r, i))
            start = i + 1
    if not hits:
        return f"not found in any single run (spans runs, or typo): {needle[:80]!r}"
    if len(hits) > 1:
        return f"matches {len(hits)} times, extend with context: {needle[:80]!r}"
    return hits[0]


def clone_rpr(r):
    rpr = r.find(w("rPr"))
    if rpr is None:
        return None
    return ET.fromstring(ET.tostring(rpr))


def make_run(rpr, tag, text):
    nr = ET.Element(w("r"))
    if rpr is not None:
        nr.append(ET.fromstring(ET.tostring(rpr)))
    t = ET.SubElement(nr, w(tag))
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text
    return nr


def split_run(p, r, start, length):
    """Split run r so [start, start+length) is its own run; return that run."""
    txt = run_text(r)
    before, mid, after = txt[:start], txt[start:start + length], txt[start + length:]
    rpr = r.find(w("rPr"))
    idx = list(p).index(r)
    p.remove(r)
    new = []
    if before:
        new.append(make_run(rpr, "t", before))
    target = make_run(rpr, "t", mid)
    new.append(target)
    if after:
        new.append(make_run(rpr, "t", after))
    for j, el in enumerate(new):
        p.insert(idx + j, el)
    return target


def track_attrs(el, rid, author, date):
    el.set(w("id"), str(rid))
    el.set(w("author"), author)
    el.set(w("date"), date)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("unpacked")
    ap.add_argument("plan")
    ap.add_argument("--endnotes", action="store_true")
    args = ap.parse_args()

    part = "endnotes" if args.endnotes else "footnotes"
    ref_el = "endnoteReference" if args.endnotes else "footnoteReference"
    note_el = "endnote" if args.endnotes else "footnote"
    ref_style = "EndnoteReference" if args.endnotes else "FootnoteReference"

    plan = json.load(open(args.plan, encoding="utf-8"))
    author = plan.get("author", "footnote-relegator")
    date = plan.get("date", "2026-01-01T00:00:00Z")

    doc_path = os.path.join(args.unpacked, "word", "document.xml")
    doc_orig_text = open(doc_path, encoding="utf-8").read()
    doc_tree = parse(doc_path)
    doc_root = doc_tree.getroot()

    # Normalize: a run holding several children (multiple w:t, embedded
    # footnote refs, page-break markers) is split into one run per child so
    # find/split logic can operate run-by-run.
    for p in doc_root.iter(w("p")):
        for r in list(p):
            if r.tag != w("r"):
                continue
            kids = [c for c in r if c.tag != w("rPr")]
            if len(kids) <= 1:
                continue
            rpr = r.find(w("rPr"))
            idx = list(p).index(r)
            p.remove(r)
            for j, kid in enumerate(kids):
                nr = ET.Element(w("r"))
                if rpr is not None:
                    nr.append(ET.fromstring(ET.tostring(rpr)))
                nr.append(kid)
                p.insert(idx + j, nr)

    # ensure footnotes part exists
    fn_path = os.path.join(args.unpacked, "word", f"{part}.xml")
    if not os.path.exists(fn_path):
        with open(fn_path, "w", encoding="utf-8") as f:
            f.write(EMPTY_FOOTNOTES if not args.endnotes else
                    EMPTY_FOOTNOTES.replace("footnote", "endnote"))
        # content types
        ct_path = os.path.join(args.unpacked, "[Content_Types].xml")
        ct = open(ct_path, encoding="utf-8").read()
        if f"/word/{part}.xml" not in ct:
            ov = (f'<Override PartName="/word/{part}.xml" ContentType='
                  f'"application/vnd.openxmlformats-officedocument.'
                  f'wordprocessingml.{part}+xml"/>')
            ct = ct.replace("</Types>", ov + "</Types>")
            open(ct_path, "w", encoding="utf-8").write(ct)
        # relationship
        rel_path = os.path.join(args.unpacked, "word", "_rels", "document.xml.rels")
        rels = open(rel_path, encoding="utf-8").read()
        if f"{part}.xml" not in rels:
            ids = re.findall(r'Id="rId(\d+)"', rels)
            nid = max(int(i) for i in ids) + 1 if ids else 1
            rel = (f'<Relationship Id="rId{nid}" Type="http://schemas.'
                   f'openxmlformats.org/officeDocument/2006/relationships/'
                   f'{part}" Target="{part}.xml"/>')
            rels = rels.replace("</Relationships>", rel + "</Relationships>")
            open(rel_path, "w", encoding="utf-8").write(rels)

    fn_orig_text = open(fn_path, encoding="utf-8").read()
    fn_tree = parse(fn_path)
    fn_root = fn_tree.getroot()
    existing_ids = [int(n.get(w("id"))) for n in fn_root.findall(w(note_el))]
    next_note_id = max(existing_ids + [0]) + 1

    rev_ids = [int(el.get(w("id"))) for el in doc_root.iter()
               if el.tag in (w("ins"), w("del")) and el.get(w("id"))
               and el.get(w("id")).lstrip("-").isdigit()]
    next_rev = max(rev_ids + [1000]) + 1

    def note_texts(el):
        return "".join(t.text or "" for t in el.iter(w("t")))

    def last_text_rpr(scope):
        """Clone the rPr of the last text run under scope — inserted text
        must match the formatting (esp. font size) of the text it joins,
        or it renders at the document default size."""
        rpr = None
        for r in scope.iter(w("r")):
            if r.find(w("t")) is not None and r.find(w("rPr")) is not None:
                rpr = r.find(w("rPr"))
        return ET.fromstring(ET.tostring(rpr)) if rpr is not None else None

    def existing_note_rpr():
        """rPr template for text in a brand-new footnote: borrow from any
        existing real footnote's text; None if the part was just created."""
        for n in fn_root.findall(w(note_el)):
            try:
                if int(n.get(w("id"))) > 0:
                    rpr = last_text_rpr(n)
                    if rpr is not None:
                        return rpr
            except (TypeError, ValueError):
                continue
        return None

    def template_note():
        """First real footnote, used as the formatting template for new
        notes — documents that use direct formatting instead of styles
        (common) make hardcoded style names render at the wrong size."""
        for n in fn_root.findall(w(note_el)):
            try:
                if int(n.get(w("id"))) > 0 and n.find(w("p")) is not None:
                    return n
            except (TypeError, ValueError):
                continue
        return None

    def clone(el):
        return ET.fromstring(ET.tostring(el)) if el is not None else None

    def body_ref_rpr():
        """rPr for the inserted reference mark in the body: copy whatever an
        existing reference run uses; fall back to the style name."""
        for r in doc_root.iter(w("r")):
            if r.find(w(ref_el)) is not None:
                return clone(r.find(w("rPr")))
        rpr = ET.Element(w("rPr"))
        st = ET.SubElement(rpr, w("rStyle"))
        st.set(w("val"), ref_style)
        return rpr

    def find_span(needle):
        """Locate needle across consecutive runs of one paragraph.
        Returns (p, [(run, s, e), ...]) covering the needle, or error str."""
        hits = []

        def ignorable(r):
            kids = [c for c in r if c.tag != w("rPr")]
            return len(kids) == 1 and kids[0].tag == w("lastRenderedPageBreak")

        for p in doc_root.iter(w("p")):
            runs = [r for r in p if r.tag == w("r")
                    and (r.find(w("t")) is not None or ignorable(r))]
            texts = [run_text(r) for r in runs]
            joined = "".join(texts)
            start = joined.find(needle)
            if start == -1:
                continue
            if joined.find(needle, start + 1) != -1:
                return f"matches twice within a paragraph: {needle[:80]!r}"
            # check no non-text run (e.g. footnote ref) interrupts the span
            end = start + len(needle)
            pos, cover = 0, []
            for r, txt in zip(runs, texts):
                rs, re_ = pos, pos + len(txt)
                if re_ > start and rs < end:
                    cover.append((r, max(0, start - rs), min(len(txt), end - rs)))
                pos = re_
            # spans must be consecutive children of p
            idxs = [list(p).index(r) for r, _, _ in cover]
            if idxs != list(range(idxs[0], idxs[0] + len(idxs))):
                return (f"span interrupted by a non-text run (footnote ref?) — "
                        f"handle by hand: {needle[:80]!r}")
            hits.append((p, cover))
        if not hits:
            return f"not found: {needle[:80]!r}"
        if len(hits) > 1:
            return f"matches {len(hits)} paragraphs, extend context: {needle[:80]!r}"
        return hits[0]

    def tracked_delete(move_text, i):
        """Wrap move_text (possibly spanning runs) in one w:del. Returns
        (paragraph, index after deletion) or None on failure."""
        nonlocal next_rev
        hit = find_span(move_text)
        if isinstance(hit, str):
            failures.append((i, "delete", hit))
            return None
        p, cover = hit
        # split partial boundary runs so covered runs contain exactly the span
        if len(cover) == 1:
            r, s, e = cover[0]
            covered = [split_run(p, r, s, e - s)]
        else:
            (r0, s0, e0), (rn, sn, en) = cover[0], cover[-1]
            first = split_run(p, r0, s0, e0 - s0) if s0 > 0 else r0
            last = split_run(p, rn, sn, en - sn) if en < len(run_text(rn)) else rn
            i0, i1 = list(p).index(first), list(p).index(last)
            covered = list(p)[i0:i1 + 1]
        idx = list(p).index(covered[0])
        d = ET.Element(w("del"))
        track_attrs(d, next_rev, author, date); next_rev += 1
        for r in covered:
            p.remove(r)
            t = r.find(w("t"))
            if t is not None:
                t.tag = w("delText")
            d.append(r)
        p.insert(idx, d)
        return p, idx

    failures = []
    for i, move in enumerate(plan["moves"]):
        # --- tracked replacement (seam repair)
        if "replace_find" in move:
            res = tracked_delete(move["replace_find"], i)
            if res is None:
                continue
            p, idx = res
            ins = ET.Element(w("ins"))
            track_attrs(ins, next_rev, author, date); next_rev += 1
            deleted = list(p)[idx]  # the w:del we just created
            ins.append(make_run(last_text_rpr(deleted), "t", move["replace_with"]))
            p.insert(idx + 1, ins)
            continue

        # --- merge into an existing footnote
        if "merge_note_contains" in move:
            res = tracked_delete(move["delete"], i)
            if res is None:
                continue
            key = move["merge_note_contains"]
            targets = [n for n in fn_root.findall(w(note_el))
                       if key in note_texts(n)]
            if len(targets) != 1:
                failures.append((i, "merge_note_contains",
                                 f"{len(targets)} footnotes match {key!r}"))
                continue
            last_p = targets[0].findall(w("p"))[-1]
            nins = ET.SubElement(last_p, w("ins"))
            track_attrs(nins, next_rev, author, date); next_rev += 1
            nins.append(make_run(last_text_rpr(last_p) or existing_note_rpr(),
                                 "t", " " + move["note"]))
            continue

        # --- new-note move
        # 1. deletion
        res = tracked_delete(move["delete"], i)
        if res is None:
            continue

        # 2. reference insertion
        hit = find_span(move["anchor_after"])
        if isinstance(hit, str):
            failures.append((i, "anchor_after", hit))
            continue
        ap_, cover = hit
        ar, sn, en = cover[-1]
        anchor_run = split_run(ap_, ar, sn, en - sn) if (sn > 0 or en < len(run_text(ar))) else ar
        ins = ET.Element(w("ins"))
        track_attrs(ins, next_rev, author, date); next_rev += 1
        ref_run = ET.Element(w("r"))
        rpr = body_ref_rpr()
        if rpr is not None:
            ref_run.append(rpr)
        fr = ET.SubElement(ref_run, w(ref_el))
        fr.set(w("id"), str(next_note_id))
        ins.append(ref_run)
        ap_.insert(list(ap_).index(anchor_run) + 1, ins)

        # 3. the note itself (ins-marked content), formatted like the
        # document's own notes: clone paragraph props + run props from an
        # existing footnote rather than assuming style names exist
        tmpl = template_note()
        note = ET.SubElement(fn_root, w(note_el))
        note.set(w("id"), str(next_note_id))
        np = ET.SubElement(note, w("p"))
        mark_run = None
        if tmpl is not None:
            tp = tmpl.find(w("p"))
            if tp.find(w("pPr")) is not None:
                np.append(clone(tp.find(w("pPr"))))
            for r in tp.iter(w("r")):
                if r.find(w(ref_el.replace("Reference", "Ref"))) is not None:
                    mark_run = clone(r)
                    break
        else:
            npr = ET.SubElement(np, w("pPr"))
            ps = ET.SubElement(npr, w("pStyle"))
            ps.set(w("val"), "FootnoteText" if not args.endnotes else "EndnoteText")
        if mark_run is None:
            mark_run = ET.Element(w("r"))
            mrpr = ET.SubElement(mark_run, w("rPr"))
            mst = ET.SubElement(mrpr, w("rStyle"))
            mst.set(w("val"), ref_style)
            ET.SubElement(mark_run, w(ref_el.replace("Reference", "Ref")))
        nins = ET.SubElement(np, w("ins"))
        track_attrs(nins, next_rev, author, date); next_rev += 1
        nins.append(mark_run)
        nins.append(make_run(existing_note_rpr(), "t", " " + move["note"]))
        next_note_id += 1

    write_preserving_root(doc_tree, doc_path, doc_orig_text)
    write_preserving_root(fn_tree, fn_path, fn_orig_text)

    ok = len(plan["moves"]) - len(failures)
    print(f"Applied {ok}/{len(plan['moves'])} moves as tracked changes.")
    for i, field, msg in failures:
        print(f"  FAILED move {i} ({field}): {msg}")
    if failures:
        print("Apply failed moves by hand (see word-redline.md), then re-validate.")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
