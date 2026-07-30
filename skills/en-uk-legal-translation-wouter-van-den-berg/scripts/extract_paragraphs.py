"""Extract paragraphs from a .docx file with formatting metadata for translation.

Accepts either a .docx file (reads word/document.xml from the ZIP) or a raw document.xml path.

Instead of extracting individual w:t elements (which fragment sentences and lose context),
this script extracts full paragraphs with metadata about which character ranges are bold,
italic, etc. This gives the translator full sentence context while preserving formatting info.

Output JSON format:
[
  {
    "idx": 0,
    "text": "full paragraph text in source language",
    "runs": [
      {"start": 0, "end": 15, "text": "defined term", "bold": true, "italic": false},
      {"start": 15, "end": 45, "text": " means the meaning...", "bold": false, "italic": false}
    ],
    "style": "Heading1",
    "numId": "5",
    "ilvl": "0",
    "en": null,
    "en_runs": null
  },
  ...
]

The "en" field should be filled with the full translated paragraph text.
The "en_runs" field should be filled with formatting instructions for the English text:
[
  {"start": 0, "end": 12, "bold": true},    // defined term in bold
  {"start": 12, "end": 60, "bold": false}   // rest in normal
]

If en_runs is null, the script will try to auto-detect defined terms and apply bold.
"""
import os
import sys
import json
import zipfile
from lxml import etree

def _check_self_integrity():
    """Rev27: detect install-time truncation"""
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

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

# ECMA-376 ST_OnOff lexical space: true|false|1|0|on|off (case-insensitive).
# previously this excluded only '0' and 'false'; 'off' now also
# treated as falsy to match the spec.
_ST_ONOFF_FALSE = {'false', '0', 'off'}

def has_prop(rpr, prop_name):
    """Check if a run property element exists and is not val=false."""
    if rpr is None:
        return False
    elem = rpr.find(f'{{{W}}}{prop_name}')
    if elem is None:
        return False
    val = elem.get(f'{{{W}}}val')
    if val is not None and val.strip().lower() in _ST_ONOFF_FALSE:
        return False
    return True


def get_prop_tristate(rpr, prop_name):
    """Tri-state ST_OnOff lookup: 'true', 'false', or None (absent).

    Distinguishes between (a) the property is explicitly set to false (the
    author wrote <w:b w:val="0"/>) — which DEFEATS any style-inherited bold —
    versus (b) the property is absent — which lets the paragraph's pStyle
    cascade decide. has_prop() collapses both into False, but the per-paragraph
    bold/italic decision in 04-translate's heading rule needs the distinction:
    only an explicit "false" at the paragraph-mark level (pPr/rPr) overrides
    a Heading-style cascade.
    """
    if rpr is None:
        return None
    elem = rpr.find(f'{{{W}}}{prop_name}')
    if elem is None:
        return None
    val = elem.get(f'{{{W}}}val')
    if val is None:
        return 'true'  # <w:b/> with no val attribute = true (ECMA-376 default)
    return 'false' if val.strip().lower() in _ST_ONOFF_FALSE else 'true'

def get_font_info(rpr):
    """Extract font name and size from run properties."""
    if rpr is None:
        return None, None
    font_elem = rpr.find(f'{{{W}}}rFonts')
    font = font_elem.get(f'{{{W}}}ascii') if font_elem is not None else None
    sz_elem = rpr.find(f'{{{W}}}sz')
    sz = sz_elem.get(f'{{{W}}}val') if sz_elem is not None else None
    return font, sz

def get_color(rpr):
    """Extract text colour if set."""
    if rpr is None:
        return None
    c = rpr.find(f'{{{W}}}color')
    return c.get(f'{{{W}}}val') if c is not None else None

def extract_paragraphs(input_path, output_json):
    # Accept either .docx (ZIP) or raw .xml path
    if input_path.lower().endswith('.docx'):
        with zipfile.ZipFile(input_path) as zf:
            xml_bytes = zf.read('word/document.xml')
        root = etree.fromstring(xml_bytes)
    else:
        tree = etree.parse(input_path)
        root = tree.getroot()

    paragraphs = []

    # IMPORTANT: root.iter() is recursive — it finds ALL w:p elements including those
    # nested inside tables (w:tbl/w:tr/w:tc/w:p), text boxes, and other containers.
    # This is critical for legal documents which often have signature blocks, schedules,
    # and form fields inside tables. The apply script MUST use the same recursive search
    # (findall('.//{W}p')) to match paragraphs correctly.
    for p_idx, p in enumerate(root.iter(f'{{{W}}}p')):
        ppr = p.find(f'{{{W}}}pPr')

        # Style
        style = None
        if ppr is not None:
            style_elem = ppr.find(f'{{{W}}}pStyle')
            if style_elem is not None:
                style = style_elem.get(f'{{{W}}}val')

        # Numbering
        num_id = None
        ilvl = None
        if ppr is not None:
            numpr = ppr.find(f'{{{W}}}numPr')
            if numpr is not None:
                numid_elem = numpr.find(f'{{{W}}}numId')
                ilvl_elem = numpr.find(f'{{{W}}}ilvl')
                num_id = numid_elem.get(f'{{{W}}}val') if numid_elem is not None else None
                ilvl = ilvl_elem.get(f'{{{W}}}val') if ilvl_elem is not None else None

        # Paragraph-level formatting (from pPr > rPr, the "default run props")
        p_bold = False
        p_italic = False
        p_font = None
        p_sz = None
        # rev38: tri-state captures of pPr/rPr bold/italic. The
        # paragraph-mark rPr can EXPLICITLY defeat a Heading-style bold or
        # italic by setting `<w:b w:val="0"/>` / `<w:i w:val="0"/>` on the
        # paragraph mark. has_prop() collapses absent and explicit-false
        # into the same False; the tri-state lets 04-translate's heading
        # rule distinguish "author defeated style" from "style cascade
        # wins". See post-mortem rev38 / Defect 3.
        p_rpr_b = None
        p_rpr_i = None
        if ppr is not None:
            p_rpr = ppr.find(f'{{{W}}}rPr')
            if p_rpr is not None:
                p_bold = has_prop(p_rpr, 'b')
                p_italic = has_prop(p_rpr, 'i')
                p_font, p_sz = get_font_info(p_rpr)
                p_rpr_b = get_prop_tristate(p_rpr, 'b')
                p_rpr_i = get_prop_tristate(p_rpr, 'i')

        # Extract runs with formatting
        runs = []
        char_offset = 0

        for r in p.iter(f'{{{W}}}r'):
            rpr = r.find(f'{{{W}}}rPr')

            # Collect text from ALL w:t elements in this run, not just the first.
            # A single w:r may contain multiple w:t elements separated by w:tab
            # or w:br elements (e.g. "11.3.1<tab>Il 10% del Corrispettivo...").
            # Using r.find('{W}t') would only return the first w:t, silently
            # dropping all subsequent text — a critical data-loss bug for
            # paragraphs where numbering and content share a single run.
            #
            # IMPORTANT: Do NOT insert tab/newline chars for w:tab / w:br here.
            # The apply_translations_textmatch.py script's get_paragraph_text()
            # joins w:t texts with no separator, and normalize_text() collapses
            # whitespace. Inserting separators here would cause text-match
            # failures. The w:tab / w:br elements are preserved in the XML
            # (only w:r content is replaced), so visual formatting is retained.
            text_parts = []
            for child in r:
                ctag = child.tag.split('}')[1] if '}' in child.tag else child.tag
                if ctag == 't' and child.text:
                    text_parts.append(child.text)

            text = ''.join(text_parts)

            if text:
                bold = has_prop(rpr, 'b') if rpr is not None else p_bold
                italic = has_prop(rpr, 'i') if rpr is not None else p_italic
                underline = has_prop(rpr, 'u')
                font, sz = get_font_info(rpr)
                color = get_color(rpr)

                run_info = {
                    "start": char_offset,
                    "end": char_offset + len(text),
                    "text": text,
                    "bold": bold,
                    "italic": italic,
                }
                if underline:
                    run_info["underline"] = True
                if font:
                    run_info["font"] = font
                elif p_font:
                    run_info["font"] = p_font
                if sz:
                    run_info["sz"] = sz
                elif p_sz:
                    run_info["sz"] = p_sz
                if color:
                    run_info["color"] = color

                runs.append(run_info)
                char_offset += len(text)

        # build full_text by walking the paragraph in document
        # order, emitting <w:t> text content AND ``\n`` at plain
        # ``<w:br/>`` positions (line breaks). Page breaks
        # (``<w:br w:type="page"/>``) emit no ``\n`` — they are
        # structural and irrelevant to the text content. The
        # ``\n`` emission is mirrored in
        # ``apply_translations_textmatch.py::get_paragraph_text`` so
        # text-matching at apply time stays aligned. Operators see
        # the ``\n`` in paragraphs.json's ``text`` field and naturally
        # write the same ``\n`` in their ``en`` translation; the
        # apply step's run-rebuilder converts ``\n`` in en back to
        # a real ``<w:br/>`` element (Fix 2a).
        full_text_pieces = []
        for child in p.iter():
            tag = child.tag
            if tag == f'{{{W}}}t' and child.text:
                full_text_pieces.append(child.text)
            elif tag == f'{{{W}}}br':
                br_type = child.get(f'{{{W}}}type', '')
                if br_type != 'page':
                    full_text_pieces.append('\n')
        full_text = ''.join(full_text_pieces)

        # For tracked-change paragraphs, also extract deleted text from w:delText
        # elements. These live inside w:del > w:r > w:delText and contain the
        # struck-through text that Word shows in redline view. The translator
        # must translate this separately (as "en_deleted") so the apply script
        # can replace it without leaving source-language remnants in the TC markup.
        deleted_text = None
        has_tc = False
        for tc_tag in ('ins', 'del', 'moveFrom', 'moveTo'):
            if p.find(f'{{{W}}}{tc_tag}') is not None:
                has_tc = True
                break
        if has_tc:
            dt_parts = []
            for dt in p.iter(f'{{{W}}}delText'):
                if dt.text:
                    dt_parts.append(dt.text)
            if dt_parts:
                deleted_text = ''.join(dt_parts)

        # For TC paragraphs, build an ordered segment list that captures the
        # paragraph's tracked-change structure: regular runs, insertions, and
        # deletions in document order. This lets the translator translate each
        # segment separately so the apply script can distribute each segment's
        # translation to only its own runs, keeping TC boundaries coherent.
        #
        # Phantom ins-wraps-del ("author A inserted, author B deleted A's
        # insertion") is a net no-op under both accept-all and reject-all
        # but is still visible with "Show Markup" on. It is emitted as a
        # distinct segment type ``ins_then_del`` so the translator can fill
        # in ``en`` and the apply step can write that English back into the
        # nested ``<w:delText>``. Without this, the source-language text
        # inside the nested del is unreachable by apply (which walks direct
        # children and collects only ``<w:t>`` under a top-level ``<w:ins>``)
        # and is also invisible to the accept-all remnant scanner (which
        # sees the phantom as empty).
        tc_segments = None
        # Detection for consecutive same-type ins/del XML-element clusters.
        # When two or more adjacent <w:ins> (or <w:del>) elements carry
        # fragmentary text like <w:ins>P</w:ins><w:ins>S</w:ins>, the merge
        # loop below collapses them into one tc_segment — but the XML still
        # holds them as separate elements at apply time. distribute_text_
        # across_elements then splits the English back into those same
        # fragments, and post_process.fix_spacing's alpha+alpha rule sees
        # the adjacency and inserts a space ("PS" becomes "P S"). The fix
        # is to insert ZWSP between such fragments when writing the
        # translation, so fix_spacing sees a separator and leaves them
        # alone. Flag the paragraph here so downstream tooling (the ZWSP
        # helper script and validate_apply's error output) can route to
        # the fix without the translator reverse-engineering the pattern.
        tc_cluster_hits = []
        if has_tc:
            raw_segs = []
            # Track the preceding XML-sibling's tc type so we can detect
            # adjacent same-type <w:ins> / <w:del> runs in raw XML order.
            prev_xml_tc_type = None
            run_span_count = 0
            for child in p:
                ctag = child.tag.split('}')[1] if '}' in child.tag else child.tag
                if ctag == 'pPr':
                    continue
                current_tc_type = None  # 'ins' / 'del' / 'ins_then_del' / None
                if ctag == 'del':
                    seg_text = ''.join(
                        dt.text or '' for dt in child.iter(f'{{{W}}}delText')
                    )
                    if seg_text:
                        raw_segs.append({'type': 'del', 'text': seg_text})
                        current_tc_type = 'del'
                elif ctag == 'ins':
                    # Does this ins contain any *non-nested* w:t runs? An
                    # ordinary insertion has <w:r><w:t>...</w:t></w:r> under
                    # it. A phantom ins-wraps-del instead has a <w:del>
                    # descendant and no top-level <w:t>.
                    has_top_t = any(
                        t.text for t in child.iter(f'{{{W}}}t')
                    )
                    # delText descendants — only populated when a <w:del>
                    # sits inside this <w:ins>.
                    nested_del_text = ''.join(
                        dt.text or '' for dt in child.iter(f'{{{W}}}delText')
                    )
                    if has_top_t:
                        seg_text = ''.join(
                            t.text or '' for t in child.iter(f'{{{W}}}t')
                        )
                        if seg_text:
                            raw_segs.append({'type': 'ins', 'text': seg_text})
                            current_tc_type = 'ins'
                    elif nested_del_text:
                        # Phantom: inserted-then-deleted content. No visible
                        # text in accept-all or reject-all view, but visible
                        # (as strike-through) with markup on. Emit as a
                        # dedicated segment so it round-trips through the
                        # translator.
                        raw_segs.append({
                            'type': 'ins_then_del',
                            'text': nested_del_text,
                        })
                        current_tc_type = 'ins_then_del'
                elif ctag == 'r':
                    seg_text = ''.join(
                        t.text or '' for t in child.iter(f'{{{W}}}t')
                    )
                    if seg_text:
                        raw_segs.append({'type': 'regular', 'text': seg_text})
                # bookmarkStart, bookmarkEnd, proofErr, etc — skip
                # (current_tc_type remains None, which correctly breaks the run)

                # Track adjacent-same-type runs. Bump run_span_count when
                # current and previous tc types match; record the hit when
                # the run ends (or at end of paragraph below) with 2+.
                if current_tc_type is not None:
                    if current_tc_type == prev_xml_tc_type:
                        run_span_count += 1
                    else:
                        if run_span_count >= 2:
                            tc_cluster_hits.append({
                                'type': prev_xml_tc_type,
                                'count': run_span_count,
                            })
                        run_span_count = 1
                        prev_xml_tc_type = current_tc_type
                else:
                    # Break the run (regular text or phantom segment between
                    # two ins/del clusters).
                    if run_span_count >= 2:
                        tc_cluster_hits.append({
                            'type': prev_xml_tc_type,
                            'count': run_span_count,
                        })
                    run_span_count = 0
                    prev_xml_tc_type = None
            # Flush pending run at end of paragraph.
            if run_span_count >= 2:
                tc_cluster_hits.append({
                    'type': prev_xml_tc_type,
                    'count': run_span_count,
                })

            # Merge consecutive segments of the same type
            if raw_segs:
                tc_segments = [dict(raw_segs[0])]
                for seg in raw_segs[1:]:
                    if tc_segments[-1]['type'] == seg['type']:
                        tc_segments[-1]['text'] += seg['text']
                    else:
                        tc_segments.append(dict(seg))

        entry = {
            "idx": p_idx,
            "text": full_text,
            "runs": runs,
            "en": None,
            "en_runs": None,
        }
        if deleted_text:
            entry["deleted_text"] = deleted_text
        if has_tc:
            entry["has_track_changes"] = True
        if tc_segments:
            entry["tc_segments"] = tc_segments
        if tc_cluster_hits:
            # Advisory flag — marks paragraphs where 2+ adjacent <w:ins> or
            # <w:del> XML elements will be merged into a single tc_segment
            # but remain as separate XML elements at apply time. The
            # translator / ZWSP helper / validate_apply error output use
            # this hint to route to the "Scrambled / character-fragmented
            # whole-word edits" fix in `skill-docs/04-translate.md` without reverse-
            # engineering the pattern each time.
            entry["tc_cluster_hits"] = tc_cluster_hits
        if style:
            entry["style"] = style
        if num_id:
            entry["numId"] = num_id
        if ilvl:
            entry["ilvl"] = ilvl
        if p_bold:
            entry["p_bold"] = True
        if p_italic:
            entry["p_italic"] = True
        # rev38: emit tri-state pPr/rPr only when the paragraph mark
        # carries an explicit setting (non-null). The translator uses
        # `p_rpr_b == "false"` to recognise a paragraph that explicitly
        # defeats style-inherited bold (ditto p_rpr_i for italic). When
        # both are null (the common case), the field is omitted to keep
        # the JSON small and visually identical to the pre-rev38 output
        # for documents that don't exercise this defect class.
        if p_rpr_b is not None:
            entry["p_rpr_b"] = p_rpr_b
        if p_rpr_i is not None:
            entry["p_rpr_i"] = p_rpr_i

        paragraphs.append(entry)

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(paragraphs, f, ensure_ascii=False, indent=1)

    non_empty = sum(1 for p in paragraphs if p["text"].strip())
    print(f"Extracted {len(paragraphs)} paragraphs ({non_empty} non-empty) to {output_json}")

    # Highlight consecutive-same-type TC clusters so the translator sees
    # them BEFORE burning cycles on the translation pass. Each entry lists
    # the paragraph idx and the type+count of the merged XML-element cluster.
    cluster_entries = [
        (e["idx"], e.get("tc_cluster_hits") or [])
        for e in paragraphs
        if e.get("tc_cluster_hits")
    ]
    if cluster_entries:
        total_clusters = sum(len(hits) for _, hits in cluster_entries)
        print(
            f"  TC-CLUSTER WARNING: {len(cluster_entries)} paragraph(s) "
            f"contain {total_clusters} consecutive-same-type <w:ins>/<w:del> "
            f"cluster(s). apply_translations_textmatch.py inserts a ZWSP at "
            f"the wrapper boundary automatically ; run "
            f"'python scripts/validate_apply.py <paragraphs.json> "
            f"--report-clusters' for a belt-and-suspenders inspection:"
        )
        for idx, hits in cluster_entries[:10]:
            summary = ', '.join(
                f"{h['count']}× <w:{h['type']}>" for h in hits
            )
            print(f"    idx={idx}: {summary}")
        if len(cluster_entries) > 10:
            print(f"    ... {len(cluster_entries) - 10} more (suppressed)")

    # aux-file content summary. Print every substantive
    # footnote / endnote / comment found in the source document so the
    # operator sees the content upfront and cannot conclude "no
    # substantive content" from a partial preview of the raw XML. This
    # is the primary mechanism that surfaces aux content for
    # translation in Step 8c (comments) / Step 8d (footnotes,
    # endnotes). Skipped when the input was a raw document.xml (no
    # access to the surrounding ZIP).
    if input_path.lower().endswith('.docx'):
        try:
            with zipfile.ZipFile(input_path) as zf:
                names = set(zf.namelist())
                summaries = []
                # Footnotes
                if 'word/footnotes.xml' in names:
                    fn_summary = _summarise_aux_xml(
                        zf.read('word/footnotes.xml').decode(
                            'utf-8', errors='replace'),
                        'footnote', label='word/footnotes.xml')
                    if fn_summary['substantive']:
                        summaries.append(fn_summary)
                # Endnotes
                if 'word/endnotes.xml' in names:
                    en_summary = _summarise_aux_xml(
                        zf.read('word/endnotes.xml').decode(
                            'utf-8', errors='replace'),
                        'endnote', label='word/endnotes.xml')
                    if en_summary['substantive']:
                        summaries.append(en_summary)
                # Comments
                if 'word/comments.xml' in names:
                    cm_summary = _summarise_aux_xml(
                        zf.read('word/comments.xml').decode(
                            'utf-8', errors='replace'),
                        'comment', label='word/comments.xml')
                    if cm_summary['substantive']:
                        summaries.append(cm_summary)
                if summaries:
                    print()
                    print('=' * 60)
                    print('AUX-FILE CONTENT SUMMARY (Step 2)')
                    print('=' * 60)
                    print('The source document contains substantive '
                          'auxiliary content that you MUST translate:')
                    print()
                    for s in summaries:
                        print(f"  {s['label']} — {len(s['substantive'])} "
                              f"substantive {s['kind']}(s):")
                        for entry_id, snippet in s['substantive'][:10]:
                            print(f"    id={entry_id}: {snippet[:120]!r}")
                        if len(s['substantive']) > 10:
                            print(f"    ... {len(s['substantive']) - 10} "
                                  f"more (suppressed)")
                    print()
                    print('Translate these in Step 8c (comments) and '
                          'Step 8d (footnotes/endnotes) before Step 9 '
                          '(quality check).')
                    print('Pass the corresponding --comments / '
                          '--footnotes / --endnotes flag to '
                          'repack_docx.py in Step 10 so the '
                          'translated copies are bundled.')
        except (zipfile.BadZipFile, OSError):
            # Source not a zip — skip the aux summary.
            pass

def _summarise_aux_xml(raw_xml, kind, label):
    """Parse an OOXML aux-file string and return a dict
    ``{'label': ..., 'kind': ..., 'substantive': [(id, snippet), ...]}``
    listing every entry that has translatable text after stripping the
    well-known structural placeholders.

    For footnotes / endnotes: any ``<w:footnote>`` / ``<w:endnote>``
    whose ``w:type`` is NOT ``separator`` or ``continuationSeparator``
    AND has at least one ``<w:t>`` with non-whitespace text.

    For comments: any ``<w:comment>`` with at least one ``<w:t>`` of
    non-whitespace text.
    """
    import re as _re
    # regex compilation moved up; var renamed pattern_re to
    # shift content past the byte position where install pipeline was
    # observed truncating extract_paragraphs.py.
    if kind in ('footnote', 'endnote'):
        pattern_re = _re.compile(
            r'<w:(?:footnote|endnote)\b([^>]*)>(.*?)</w:(?:footnote|endnote)>',
            _re.DOTALL)
    else:
        pattern_re = _re.compile(
            r'<w:comment\b([^>]*)>(.*?)</w:comment>',
            _re.DOTALL)
    substantive = []
    for m in pattern_re.finditer(raw_xml):
        attrs = m.group(1)
        body = m.group(2)
        if 'w:type=' in attrs:
            type_match = _re.search(
                r'w:type="(separator|continuationSeparator)"', attrs)
            if type_match:
                continue
        id_match = _re.search(r'w:id="([^"]+)"', attrs)
        entry_id = id_match.group(1) if id_match else '?'
        # Concatenate all <w:t> contents
        text_parts = _re.findall(r'<w:t[^>]*>([^<]*)</w:t>', body)
        text = ''.join(text_parts).strip()
        if text:
            substantive.append((entry_id, text))
    return {'label': label, 'kind': kind, 'substantive': substantive}

if __name__ == '__main__':
    _check_self_integrity()
    if len(sys.argv) != 3:
        print("Usage: extract_paragraphs.py <input.docx|document.xml> <output.json>")
        print()
        print("Accepts either a .docx file (reads from ZIP) or a raw document.xml path.")
        sys.exit(1)
    extract_paragraphs(sys.argv[1], sys.argv[2])

# === SKILL FILE COMPLETE ===
