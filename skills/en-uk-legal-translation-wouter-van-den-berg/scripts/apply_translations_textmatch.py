"""Apply translations from paragraphs.json onto original document.xml using TEXT MATCHING.

Instead of mapping by idx (which is wrong for this document due to extraction artifacts),
this script matches each paragraphs.json entry to the original paragraph whose Italian
text matches the entry's 'text' field. This handles any offset or misalignment.

For duplicate Italian texts (e.g., "[●]", "PEC: [●]"), it uses positional order:
first occurrence matches first duplicate, second matches second, etc.
"""
import sys
import os
import re
import io
import json
import zipfile
import copy
import xml.etree.ElementTree as ET

# Import the shared per-language marker module. It lives in the same scripts/
# directory, so we extend sys.path before importing.
_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)
from source_language_markers import (  # noqa: E402
    scan_remnants,
    detect_language,
    SUPPORTED_LANGUAGES,
)

def _check_self_integrity():
    """Rev27: detect install-time truncation by reading the script's own
    source and checking for the sentinel at the bottom. Marketplace
    install pipelines have been observed cutting files mid-content; the
    sentinel + check turn that into a clear RE-INSTALL message before
    any work is done."""
    try:
        with open(os.path.abspath(__file__), 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError:
        return  # Can't check; proceed
    if '\n# === SKILL FILE COMPLETE ===' not in content:
        msg = (
            "\n" + "=" * 60 + "\n"
            "[skill] FILE INTEGRITY CHECK FAILED — script truncated.\n"
            f"  File: {os.path.abspath(__file__)}\n"
            f"  Size: {len(content):,} bytes (sentinel marker missing).\n"
            "\n"
            "  The skill install copy is incomplete. The .skill / .zip\n"
            "  archive is intact; only the local install was truncated\n"
            "  during marketplace transfer. Re-install the skill from\n"
            "  the archive. If the problem persists across re-installs,\n"
            "  contact support.\n"
            + "=" * 60 + "\n"
        )
        print(msg, file=sys.stderr)
        sys.exit(3)


_check_self_integrity()

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

# Static namespace list (safety net). Primary mechanism is
# register_document_namespaces() — dynamically registers what's on the
# source document's root. w16* family added for Word 2023 compat.
NAMESPACES = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'o': 'urn:schemas-microsoft-com:office:office',
    'v': 'urn:schemas-microsoft-com:vml',
    'w10': 'urn:schemas-microsoft-com:office:word',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
    'wps': 'http://schemas.microsoft.com/office/word/2010/wordprocessingShape',
    'wpg': 'http://schemas.microsoft.com/office/word/2010/wordprocessingGroup',
    'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
    'wp14': 'http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing',
    'w14': 'http://schemas.microsoft.com/office/word/2010/wordml',
    'w15': 'http://schemas.microsoft.com/office/word/2012/wordml',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'wne': 'http://schemas.microsoft.com/office/word/2006/wordml',
    # Word 2015-2024 TC / content-control metadata (w16* family).
    'w16': 'http://schemas.microsoft.com/office/word/2018/wordml',
    'w16cex': 'http://schemas.microsoft.com/office/word/2018/wordml/cex',
    'w16cid': 'http://schemas.microsoft.com/office/word/2016/wordml/cid',
    'w16du': 'http://schemas.microsoft.com/office/word/2023/wordml/word16du',
    'w16sdtdh': 'http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash',
    'w16sdtfl': 'http://schemas.microsoft.com/office/word/2024/wordml/sdtformatlock',
    'w16se': 'http://schemas.microsoft.com/office/word/2015/wordml/symex',
}
for prefix, uri in NAMESPACES.items():
    ET.register_namespace(prefix, uri)


def register_document_namespaces(orig_xml_bytes):
    """Register xmlns:PREFIX declarations from the source document's root
    so ET doesn't synthesize incompatible ns3:/ns4: prefixes at write time.
    Covers namespaces beyond the static NAMESPACES list."""
    try:
        head = orig_xml_bytes[:8000].decode('utf-8', errors='replace')
    except Exception:
        return
    m = re.search(r'<w:document\b([^>]*)>', head, re.DOTALL)
    if not m:
        return
    attrs = m.group(1)
    registered = []
    for pm in re.finditer(r'xmlns:([A-Za-z_][\w.-]*)\s*=\s*"([^"]+)"', attrs):
        prefix, uri = pm.group(1), pm.group(2)
        try:
            ET.register_namespace(prefix, uri)
            registered.append(prefix)
        except Exception:
            pass
    if registered:
        print(f"  Registered {len(registered)} namespace prefix(es) from source: {registered}")

def get_paragraph_text(p_elem):
    """Get plain text from a paragraph. emits \\n at plain
    <w:br/> (mirrors extract_paragraphs.py for matching). Page breaks
    emit no \\n"""
    pieces = []
    for child in p_elem.iter():
        tag = child.tag
        if tag == f'{W}t' and child.text:
            pieces.append(child.text)
        elif tag == f'{W}br':
            br_type = child.get(f'{W}type', '')
            if br_type != 'page':
                pieces.append('\n')
    return ''.join(pieces).strip()

def normalize_text(t):
    """Normalize text for matching: collapse whitespace, strip."""
    return re.sub(r'\s+', ' ', t).strip()

def get_default_rpr_et(p_elem):
    """Get run properties from the first text-bearing run."""
    for r in p_elem.findall(f'{W}r'):
        t = r.find(f'{W}t')
        if t is not None and t.text and t.text.strip():
            rpr = r.find(f'{W}rPr')
            if rpr is not None:
                return copy.deepcopy(rpr)
    return None

def is_subheader_paragraph(en_text, original_runs):
    """Detect if a paragraph is a sub-header that should preserve bold."""
    if not original_runs:
        return False
    word_count = len(en_text.split())
    if word_count > 10:
        return False
    has_bold = False
    has_non_bold_text = False
    for run in original_runs:
        text = run.get("text", "").strip()
        if not text:
            continue
        if run.get("bold"):
            has_bold = True
        else:
            has_non_bold_text = True
    return has_bold and not has_non_bold_text

def has_track_changes(p_elem):
    """True if paragraph contains <w:ins>/<w:del>/<w:moveFrom>/<w:moveTo>.
    TC paragraphs take a separate apply path (apply_trackchanges_inplace)
    so the wrapper structure is preserved."""
    for tag in ('ins', 'del', 'moveFrom', 'moveTo'):
        if p_elem.find(f'.//{W}{tag}') is not None:
            return True
    return False

def snap_to_whitespace(pos, text, window=20):
    """Move pos to the nearest whitespace within +/- window characters,
    preferring positions AFTER whitespace so the next segment starts
    with a full word. Returns the original pos if no whitespace is
    nearby."""
    if pos <= 0 or pos >= len(text):
        return max(0, min(pos, len(text)))
    for off in range(0, window + 1):
        for candidate in (pos - off, pos + off):
            if 0 < candidate <= len(text) and text[candidate - 1] == ' ':
                return candidate
    return pos

def distribute_text_across_elements(elements, text, preserve_source_boundary_whitespace=True):
    """Distribute text proportionally across w:t/w:delText elements,
    snapping boundaries to whitespace. Restores source-side leading/
    trailing whitespace on first/last elements if upstream .strip()
    lost it"""
    if not elements or not text:
        return

    # Capture boundary whitespace from the source BEFORE we overwrite .text.
    first_src = elements[0].text or ''
    last_src = elements[-1].text or ''
    src_leading_ws = ''
    src_trailing_ws = ''
    if preserve_source_boundary_whitespace:
        # Only preserve spaces/tabs (not newlines) that were actually in the source.
        m_lead = re.match(r'^[ \t]+', first_src)
        if m_lead:
            src_leading_ws = m_lead.group(0)
        m_trail = re.search(r'[ \t]+$', last_src)
        if m_trail:
            src_trailing_ws = m_trail.group(0)

    src_lengths = [len(e.text or '') for e in elements]
    total_src = sum(src_lengths)
    if total_src == 0:
        # All elements empty — put everything in the first one
        elements[0].text = text
        if text and (text[0] == ' ' or text[-1] == ' '):
            elements[0].set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        return

    text_len = len(text)
    boundaries = [0]
    cum = 0
    for length in src_lengths[:-1]:
        cum += length
        ideal = round(cum / total_src * text_len)
        boundaries.append(snap_to_whitespace(ideal, text))
    boundaries.append(text_len)

    # Ensure monotonic
    for i in range(1, len(boundaries)):
        if boundaries[i] < boundaries[i - 1]:
            boundaries[i] = boundaries[i - 1]

    for i, elem in enumerate(elements):
        slice_text = text[boundaries[i]:boundaries[i + 1]]
        # Restore source boundary whitespace if upstream .strip() removed it.
        if preserve_source_boundary_whitespace:
            if i == 0 and src_leading_ws and not slice_text.startswith((' ', '\t')):
                slice_text = src_leading_ws + slice_text
            if i == len(elements) - 1 and src_trailing_ws and not slice_text.endswith((' ', '\t')):
                slice_text = slice_text + src_trailing_ws
        elem.text = slice_text
        if slice_text and (slice_text[0] == ' ' or slice_text[-1] == ' '):
            elem.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')

def apply_trackchanges_inplace(orig_p, en_text, it_text,
                               en_deleted=None, it_deleted=None,
                               en_segments=None,
                               en_runs_spec=None,
                               original_runs=None):
    """Apply English translation to a tracked-change paragraph in place.
    Segment-aware (en_segments) or legacy proportional fallback. Returns
    True on success, False if the paragraph has no text content.

    rev38: en_runs_spec and original_runs are read by the bold-off-override
    decision below. The override unconditionally applied <w:b w:val="0"/>
    on every run of any non-heading-styled TC paragraph, which strips
    intentional bold from heading paragraphs that get their bold from
    run-level <w:b/> rather than from a Heading-N pStyle (the Japanese-MOU
    Clause 3 pattern in the rev38 post-mortem). Two new bypasses:

    1. If the translator emitted en_runs_spec with at least one entry
       whose `bold: True`, the operator has explicitly authored bold for
       this paragraph — respect that authorial intent and skip the
       blanket bold-off.
    2. If every source run in `original_runs` (the JSON `runs` array)
       has `bold: True`, the source paragraph is *uniformly* bold — a
       strong signal that bold is the genuine paragraph formatting (not
       a TC-styling leak), so skip the blanket bold-off.

    These bypasses are conservative: paragraphs with NO en_runs and a
    mix of bold and non-bold source runs (the original Italian-body-text
    case the override was written for) still get the blanket bold-off,
    so the original defect class — bold leak from <w:ins> styling into
    body text — remains defended.
    """
    # Build parent map for is_inside_del
    parent_map = {c: p for p in orig_p.iter() for c in p}

    def is_inside_del(elem):
        current = elem
        while current is not None and current is not orig_p:
            if current.tag == f'{W}del':
                return True
            current = parent_map.get(current)
        return False

    # Heading detection: only truly short heading-style paragraphs keep bold
    ppr = orig_p.find(f'{W}pPr')
    is_heading = False
    full_text = ''.join(t.text or '' for t in orig_p.iter(f'{W}t'))
    if ppr is not None:
        style_elem = ppr.find(f'{W}pStyle')
        if style_elem is not None:
            sv = (style_elem.get(f'{W}val') or '').lower()
            if any(h in sv for h in ('heading', 'cmsor', 'title', 'titre')):
                if len(full_text.strip()) < 120:
                    is_heading = True

    # rev38: two additional bypasses for the bold-off-override.
    # If neither pStyle-based heading detection fires AND the paragraph is
    # genuinely bold (operator-authored or uniformly source-bold), skip the
    # bold-off. See docstring above + rev38 post-mortem / Defect 4.
    skip_bold_override = False
    if en_runs_spec:
        # Operator authored at least one run with bold=True → respect intent.
        try:
            for seg in en_runs_spec:
                if isinstance(seg, dict) and seg.get('bold') is True:
                    skip_bold_override = True
                    break
        except (TypeError, AttributeError):
            pass
    if not skip_bold_override and original_runs:
        # Every source run is bold → genuine paragraph-bold. Filter out
        # zero-text runs (e.g. structural runs) before checking — only
        # text-bearing runs vote.
        try:
            text_runs = [r for r in original_runs
                         if isinstance(r, dict) and r.get('text')]
            if text_runs and all(
                    r.get('bold') is True for r in text_runs):
                skip_bold_override = True
        except (TypeError, AttributeError):
            pass

    # ---- Segment-aware mode ----
    if en_segments:
        # Build XML segments parallel to en_segments: regular/ins/del/
        # ins_then_del. The phantom ins_then_del case (ins wrapping
        # delText) is emitted by extract as a distinct segment so the
        # translator's en lands in the nested delText.
        xml_segs = []  # list of {'type': str, 'elements': [ET.Element]}
        for child in orig_p:
            ctag = child.tag.split('}')[1] if '}' in child.tag else child.tag
            if ctag == 'pPr':
                continue
            if ctag == 'del':
                dts = list(child.iter(f'{W}delText'))
                seg_text = ''.join(dt.text or '' for dt in dts)
                if seg_text or dts:
                    xml_segs.append({'type': 'del', 'elements': dts})
            elif ctag == 'ins':
                ts = list(child.iter(f'{W}t'))
                seg_text = ''.join(t.text or '' for t in ts)
                if seg_text or ts:
                    xml_segs.append({'type': 'ins', 'elements': ts})
                else:
                    # No top-level <w:t> under this <w:ins>. Check for
                    # a nested <w:del> — the phantom ins_then_del shape.
                    nested_dts = list(child.iter(f'{W}delText'))
                    nested_text = ''.join(dt.text or '' for dt in nested_dts)
                    if nested_text:
                        xml_segs.append({
                            'type': 'ins_then_del',
                            'elements': nested_dts,
                        })
            elif ctag == 'r':
                ts = list(child.iter(f'{W}t'))
                seg_text = ''.join(t.text or '' for t in ts)
                if seg_text or ts:
                    xml_segs.append({'type': 'regular', 'elements': ts})

        # Merge consecutive XML segments of the same type, recording
        # wrapper boundaries for ZWSP injection. See `skill-docs/04-translate.md`
        # "Scrambled / character-fragmented whole-word edits".
        merged_xml = []
        for xs in xml_segs:
            if merged_xml and merged_xml[-1]['type'] == xs['type']:
                # Record the wrapper-boundary element index so we can
                # inject a ZWSP there after distribute.
                merged_xml[-1]['wrapper_boundaries'].append(
                    len(merged_xml[-1]['elements'])
                )
                merged_xml[-1]['elements'].extend(xs['elements'])
            else:
                merged_xml.append({
                    'type': xs['type'],
                    'elements': list(xs['elements']),
                    'wrapper_boundaries': [],
                })

        # Match en_segments to xml segments by type sequence.
        # Both should have the same type pattern; if not, fall through to legacy.
        en_types = [s['type'] for s in en_segments]
        xml_types = [s['type'] for s in merged_xml]

        if en_types == xml_types:
            applied = False
            for en_seg, xml_seg in zip(en_segments, merged_xml):
                # 'en' missing/None: leave source text. '' or whitespace:
                # clear run (coalesce-to-first-segment trick — see
                # `skill-docs/04-translate.md` "Scrambled edits"). Else: distribute.
                if 'en' not in en_seg or en_seg.get('en') is None:
                    continue
                # rev42: keep the operator's boundary whitespace alive into
                # the rendered document. `en_seg_stripped` is used ONLY for
                # the "is the segment empty?" branch (en="" / en="  " both
                # mean clear-this-segment). When non-empty, distribute the
                # UNSTRIPPED text so leading/trailing spaces the operator
                # authored as element-boundary separators survive into the
                # `<w:t>` / `<w:delText>` content. This eliminates the
                # rev41 structural conflict where:
                #   (a) apply.strip removed operator boundary whitespace,
                #   (b) source-restoration only worked for European scripts
                #       (non-Latin <w:t> has no inter-word whitespace),
                #   (c) fix_spacing later inserted spaces at element
                #       boundaries to repair the visible glue, and
                #   (d) the post-strip drift gate failed because declared
                #       and applied tokenisations diverged.
                # By preserving operator whitespace here, applied text
                # matches declared at apply time AND fix_spacing rarely
                # needs to fire (operator's separators are already in
                # the document). When fix_spacing DOES fire on a boundary
                # the operator left glued, validate_apply's --post-
                # spacing-fix simulation (rev42) keeps the post-strip
                # drift gate symmetric.
                en_seg_stripped = (en_seg['en'] or '').strip()
                if not xml_seg['elements']:
                    continue
                if en_seg_stripped:
                    en_seg_text = en_seg['en']
                    distribute_text_across_elements(xml_seg['elements'], en_seg_text)
                    # Inject ZWSP at wrapper boundaries inside cluster-
                    # merged xml_segs to defeat fix_spacing's alpha+alpha
                    # rule. Skip if edges already have non-alpha chars.
                    boundaries = xml_seg.get('wrapper_boundaries') or []
                    for boundary_idx in boundaries:
                        if boundary_idx <= 0 or boundary_idx >= len(xml_seg['elements']):
                            continue
                        prev_elem = xml_seg['elements'][boundary_idx - 1]
                        curr_elem = xml_seg['elements'][boundary_idx]
                        prev_text = prev_elem.text or ''
                        curr_text = curr_elem.text or ''
                        if not prev_text or not curr_text:
                            continue
                        pc = prev_text[-1]
                        cc = curr_text[0]
                        if pc.isalpha() and cc.isalpha():
                            curr_elem.text = '\u200b' + curr_text
                            curr_elem.set(
                                '{http://www.w3.org/XML/1998/namespace}space',
                                'preserve')
                else:
                    # Explicit empty-string request: clear every element in this
                    # XML segment. Preserves the w:t / w:delText element itself
                    # (so the w:ins / w:del wrapper survives for subsequent
                    # strip_noop / coalesce passes) but drops the source text.
                    for el in xml_seg['elements']:
                        el.text = ''
                applied = True
            if not applied:
                return False
        else:
            print(f"    WARNING: segment type mismatch: en={en_types} vs xml={xml_types}")
            print(f"    Falling back to legacy proportional distribution.")
            # Fall through to legacy mode below
            en_segments = None

    # ---- Legacy proportional mode (fallback) ----
    if not en_segments:
        active_ts = []
        for t in orig_p.iter(f'{W}t'):
            if not is_inside_del(t):
                active_ts.append(t)
        deleted_dts = list(orig_p.iter(f'{W}delText'))

        if not active_ts and not deleted_dts:
            return False

        if active_ts and en_text:
            distribute_text_across_elements(active_ts, en_text)
        if deleted_dts and en_deleted:
            distribute_text_across_elements(deleted_dts, en_deleted)
        elif deleted_dts and not en_deleted:
            del_src = ''.join(dt.text or '' for dt in deleted_dts)
            if del_src.strip():
                print(f"    WARNING: TC paragraph has untranslated deleted text: {del_src[:80]}...")

    # --- Fix bold leak ---
    RPR_ORDER = [
        'rStyle', 'rFonts', 'b', 'bCs', 'i', 'iCs', 'caps', 'smallCaps',
        'strike', 'dstrike', 'outline', 'shadow', 'emboss', 'imprint',
        'noProof', 'snapToGrid', 'vanish', 'webHidden', 'color', 'spacing',
        'w', 'kern', 'position', 'sz', 'szCs', 'highlight', 'u', 'effect',
        'bdr', 'shd', 'fitText', 'vertAlign', 'rtl', 'cs', 'em', 'lang',
    ]
    if not is_heading and not skip_bold_override:
        val_attr = f'{W}val'
        for r_elem in orig_p.iter(f'{W}r'):
            rpr = r_elem.find(f'{W}rPr')
            if rpr is None:
                rpr = ET.Element(f'{W}rPr')
                r_elem.insert(0, rpr)
            b_elem = rpr.find(f'{W}b')
            if b_elem is None:
                b_elem = ET.Element(f'{W}b')
                b_order = RPR_ORDER.index('b')
                inserted = False
                for i, existing in enumerate(rpr):
                    ex_tag = existing.tag.split('}')[1] if '}' in existing.tag else existing.tag
                    ex_order = RPR_ORDER.index(ex_tag) if ex_tag in RPR_ORDER else len(RPR_ORDER)
                    if ex_order > b_order:
                        rpr.insert(i, b_elem)
                        inserted = True
                        break
                if not inserted:
                    rpr.append(b_elem)
            b_elem.set(val_attr, '0')

    # post-pass — collapse adjacent ins+del with identical English
    # text (source-language-only orthographic edits) and absorb pure-
    # whitespace ins/del wrappers into adjacent regulars. Both patterns
    # have no English meaning and produce validate_apply false-positives
    # when left as TC structure.
    _collapse_orthographic_tc_pairs(orig_p)
    _absorb_whitespace_only_tc_wrappers(orig_p)

    return True

def auto_detect_formatting(en_text, original_runs):
    """Auto-detect which parts of the English text should be bold/italic."""
    if is_subheader_paragraph(en_text, original_runs):
        return [{"start": 0, "end": len(en_text), "bold": True, "italic": False}]

    def_pattern = re.compile(
        r'([\u201c"\u201e])'
        r'([^"\u201d\u201c]+?)'
        r'([\u201d"])'
        r'(\s*)'
        r'(means|shall mean|has the meaning|indicates)',
        re.IGNORECASE
    )

    bold_ranges = []
    for m in def_pattern.finditer(en_text):
        bold_ranges.append((m.start(2), m.end(2)))

    if not bold_ranges:
        return [{"start": 0, "end": len(en_text), "bold": False, "italic": False}]

    segments = []
    pos = 0
    for b_start, b_end in sorted(bold_ranges):
        if pos < b_start:
            segments.append({"start": pos, "end": b_start, "bold": False, "italic": False})
        segments.append({"start": b_start, "end": b_end, "bold": True, "italic": False})
        pos = b_end
    if pos < len(en_text):
        segments.append({"start": pos, "end": len(en_text), "bold": False, "italic": False})

    return segments

def make_run_et(text, template_rpr, bold=False, italic=False):
    """Create a new w:r element with the given text and formatting."""
    r = ET.Element(f'{W}r')

    if template_rpr is not None:
        rpr = copy.deepcopy(template_rpr)
        # Strip w:lang elements — these carry the source-language tag (e.g. it-IT)
        # and cause Word to show "Changed to English (UK)" tracked changes on every run.
        # Removing them lets Word auto-detect the language from the English text.
        for lang_elem in list(rpr.findall(f'{W}lang')):
            rpr.remove(lang_elem)
    else:
        rpr = ET.SubElement(r, f'{W}rPr')

    # OOXML schema ordering for w:rPr children (ISO 29500-1 §17.3.2.28).
    # Word validates this ordering and shows "unreadable content" if violated.
    RPR_ORDER = [
        'rStyle', 'rFonts', 'b', 'bCs', 'i', 'iCs', 'caps', 'smallCaps',
        'strike', 'dstrike', 'outline', 'shadow', 'emboss', 'imprint',
        'noProof', 'snapToGrid', 'vanish', 'webHidden', 'color', 'spacing',
        'w', 'kern', 'position', 'sz', 'szCs', 'highlight', 'u', 'effect',
        'bdr', 'shd', 'fitText', 'vertAlign', 'rtl', 'cs', 'em', 'lang',
        'eastAsianLayout', 'specVanish', 'oMath',
    ]

    def insert_rpr_child(rpr_elem, new_child):
        """Insert a child element into rPr at the correct schema-ordered position."""
        new_tag = new_child.tag.split('}')[1] if '}' in new_child.tag else new_child.tag
        new_order = RPR_ORDER.index(new_tag) if new_tag in RPR_ORDER else len(RPR_ORDER)
        for i, existing in enumerate(rpr_elem):
            ex_tag = existing.tag.split('}')[1] if '}' in existing.tag else existing.tag
            ex_order = RPR_ORDER.index(ex_tag) if ex_tag in RPR_ORDER else len(RPR_ORDER)
            if ex_order > new_order:
                rpr_elem.insert(i, new_child)
                return
        rpr_elem.append(new_child)

    val_attr = f'{W}val'

    # Explicit bold override:
    #   bold=True  → emit <w:b/>             (turns bold ON, overriding any style that turns it off)
    #   bold=False → emit <w:b w:val="0"/>   (turns bold OFF, overriding any style that turns it on)
    #
    # We MUST emit the explicit off-override rather than simply omitting <w:b>, because paragraph
    # styles can inherit bold from basedOn parents (e.g. Cmsor2 → Cmsor1 → bold=1). If we omit <w:b>
    # in that case, the style's inherited bold shows through and the entire body renders bold.
    b_elem = rpr.find(f'{W}b')
    if b_elem is None:
        b_elem = ET.Element(f'{W}b')
        insert_rpr_child(rpr, b_elem)
    if bold:
        if val_attr in b_elem.attrib:
            del b_elem.attrib[val_attr]
    else:
        b_elem.set(val_attr, '0')

    # keep <w:bCs> paired with <w:b>. Bare <w:bCs/> defaults
    # to ON per ECMA-376; without this the rPr emits a contradiction
    # that get_bold_term reads as bold-on
    bcs_elem = rpr.find(f'{W}bCs')
    if bcs_elem is None:
        bcs_elem = ET.Element(f'{W}bCs')
        insert_rpr_child(rpr, bcs_elem)
    if bold:
        if val_attr in bcs_elem.attrib:
            del bcs_elem.attrib[val_attr]
    else:
        bcs_elem.set(val_attr, '0')

    # Same logic for italic — styles can inherit italic from basedOn parents, so omitting <w:i>
    # lets style italic leak through. Always emit an explicit override.
    i_elem = rpr.find(f'{W}i')
    if i_elem is None:
        i_elem = ET.Element(f'{W}i')
        insert_rpr_child(rpr, i_elem)
    if italic:
        if val_attr in i_elem.attrib:
            del i_elem.attrib[val_attr]
    else:
        i_elem.set(val_attr, '0')

    # same paired-off treatment for <w:iCs>.
    ics_elem = rpr.find(f'{W}iCs')
    if ics_elem is None:
        ics_elem = ET.Element(f'{W}iCs')
        insert_rpr_child(rpr, ics_elem)
    if italic:
        if val_attr in ics_elem.attrib:
            del ics_elem.attrib[val_attr]
    else:
        ics_elem.set(val_attr, '0')

    if template_rpr is not None:
        r.insert(0, rpr)

    t = ET.SubElement(r, f'{W}t')
    t.text = text
    if text and (text[0] == ' ' or text[-1] == ' '):
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')

    return r

def _run_is_text_bearing(r):
    """Rev26: True if <w:r> has <w:t> or <w:delText> with text."""
    for child in r:
        tag = child.tag
        if tag in (f'{W}t', f'{W}delText') and child.text:
            return True
    return False

def _norm_ortho_text(s):
    """Rev28: strip ZWSP + surrounding whitespace for ortho-pair compare.
    Handles  hybrid bookends correctly"""
    if not s:
        return ''
    return s.replace('​', '').strip()

def _tc_text(elem):
    """Rev28: concatenate <w:t> + <w:delText> content inside elem (any
    depth). Used by the ortho-pair collapse to compare ins/del payload."""
    pieces = []
    for child in elem.iter():
        tag = child.tag
        if tag in (f'{W}t', f'{W}delText') and child.text:
            pieces.append(child.text)
    return ''.join(pieces)

def _is_orthographic_xml_pair(elem_a, elem_b):
    """Rev28: True if a/b are adjacent <w:ins>+<w:del> with identical
    normalised English text — source-language-only ortho edits."""
    tag_a = elem_a.tag.split('}')[-1] if '}' in elem_a.tag else elem_a.tag
    tag_b = elem_b.tag.split('}')[-1] if '}' in elem_b.tag else elem_b.tag
    if {tag_a, tag_b} != {'ins', 'del'}:
        return False
    norm_a = _norm_ortho_text(_tc_text(elem_a))
    norm_b = _norm_ortho_text(_tc_text(elem_b))
    return bool(norm_a) and norm_a == norm_b

def _collapse_orthographic_tc_pairs(orig_p):
    """Rev28: collapse adjacent ins+del pairs with identical English
    text into a single regular <w:r>. Eliminates the
    proactivelyproactively false positive in validate_apply"""
    children = list(orig_p)
    new_children = []
    i = 0
    while i < len(children):
        cur = children[i]
        nxt = children[i + 1] if i + 1 < len(children) else None
        if nxt is not None and _is_orthographic_xml_pair(cur, nxt):
            # Build replacement: a regular <w:r> with the merged text.
            merged_text = _norm_ortho_text(_tc_text(cur))
            new_r = ET.Element(f'{W}r')
            t = ET.SubElement(new_r, f'{W}t')
            t.text = merged_text
            if merged_text and (merged_text[0] == ' '
                                or merged_text[-1] == ' '):
                t.set('{http://www.w3.org/XML/1998/namespace}space',
                      'preserve')
            new_children.append(new_r)
            i += 2
        else:
            new_children.append(cur)
            i += 1
    if len(new_children) == len(children):
        return  # No collapse needed.
    for child in children:
        orig_p.remove(child)
    for child in new_children:
        orig_p.append(child)

def _absorb_whitespace_only_tc_wrappers(orig_p):
    """Rev28: absorb pure-whitespace ins/del into adjacent regular run.
    ZWSP-only/ZWSP-bearing wrappers are preserved (boundary
    scaffolding)"""
    children = list(orig_p)
    to_remove = []
    for i, child in enumerate(children):
        tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
        if tag not in ('ins', 'del'):
            continue
        text = _tc_text(child)
        if not text:
            continue
        if '​' in text:
            continue  # ZWSP-only or ZWSP-bearing — leave alone
        if text.strip():
            continue  # Has non-whitespace content — leave alone
        # Pure whitespace; absorb into adjacent regular run.
        absorbed = False
        # Prefer preceding regular w:r.
        for j in range(i - 1, -1, -1):
            prev = children[j]
            ptag = prev.tag.split('}')[-1] if '}' in prev.tag else prev.tag
            if ptag == 'r':
                # Append whitespace to the LAST <w:t> in this run.
                ts = list(prev.iter(f'{W}t'))
                if ts:
                    last_t = ts[-1]
                    last_t.text = (last_t.text or '') + text
                    last_t.set(
                        '{http://www.w3.org/XML/1998/namespace}space',
                        'preserve')
                    absorbed = True
                break
        if not absorbed:
            # Try following regular w:r.
            for j in range(i + 1, len(children)):
                nxt = children[j]
                ntag = nxt.tag.split('}')[-1] if '}' in nxt.tag else nxt.tag
                if ntag == 'r':
                    ts = list(nxt.iter(f'{W}t'))
                    if ts:
                        first_t = ts[0]
                        first_t.text = text + (first_t.text or '')
                        first_t.set(
                            '{http://www.w3.org/XML/1998/namespace}space',
                            'preserve')
                        absorbed = True
                    break
        if absorbed:
            to_remove.append(child)
    for child in to_remove:
        orig_p.remove(child)

def _run_should_be_preserved(r):
    """Rev26: preserve runs with page breaks, drawings, fields, etc.;
    drop plain <w:br/> (recreated from \\n in en) and empty runs"""
    for child in r:
        tag = child.tag
        if tag == f'{W}br':
            br_type = child.get(f'{W}type', '')
            if br_type == 'page':
                return True
            # plain line break — not preserved
        elif tag in (f'{W}drawing', f'{W}pict',
                     f'{W}fldChar', f'{W}instrText',
                     f'{W}lastRenderedPageBreak',
                     f'{W}tab'):
            return True
    return False

def extract_header(xml_text):
    """Extract XML declaration and root element opening tag from raw XML text."""
    m = re.match(r'(<\?xml[^?]*\?>\s*<w:document[^>]*>)', xml_text, re.DOTALL)
    return m.group(1) if m else None

def build_text_index(orig_paras):
    """Build a mapping from normalized Italian text to list of (paragraph_index) in order."""
    text_to_indices = {}
    for i, p in enumerate(orig_paras):
        text = normalize_text(get_paragraph_text(p))
        if text:
            if text not in text_to_indices:
                text_to_indices[text] = []
            text_to_indices[text].append(i)
    return text_to_indices

def find_match(entry_text, text_to_indices, used_indices, entry_idx):
    """Find the best matching original paragraph for a given Italian text.

    Strategy:
    1. Exact match on normalized text
    2. Prefix match (first 30 chars) for texts that might have been truncated
    3. For duplicate texts, use positional order (closest to expected idx)
    """
    norm = normalize_text(entry_text)

    if not norm:
        return None

    # Try exact match
    if norm in text_to_indices:
        candidates = [i for i in text_to_indices[norm] if i not in used_indices]
        if candidates:
            # Pick the one closest to expected position
            return min(candidates, key=lambda x: abs(x - entry_idx))

    # Try prefix match (first 30 chars)
    prefix = norm[:30]
    if len(prefix) >= 10:
        for text, indices in text_to_indices.items():
            if text.startswith(prefix):
                candidates = [i for i in indices if i not in used_indices]
                if candidates:
                    return min(candidates, key=lambda x: abs(x - entry_idx))

    return None

def _doc_has_tracked_changes(paragraphs_json_path):
    """Return True if any paragraph entry in paragraphs.json carries
    tracked-change metadata (has_track_changes, tc_segments, or
    en_segments). Used to gate the TC-only pre-apply validators."""
    try:
        with open(paragraphs_json_path, 'r', encoding='utf-8') as f:
            entries = json.load(f)
    except (OSError, json.JSONDecodeError):
        return False
    for e in entries:
        if not isinstance(e, dict):
            continue
        if e.get('has_track_changes'):
            return True
        if e.get('tc_segments') or e.get('en_segments'):
            return True
    return False

def _run_validator(label, args, block_codes=None):
    """Invoke a validator subprocess; raise RuntimeError on block.
    block_codes={set} or None (any non-zero blocks)."""
    import subprocess
    print(f"\n{'=' * 60}\n[apply] auto-running {label}\n{'=' * 60}")
    result = subprocess.run(args, capture_output=False)
    rc = result.returncode
    if block_codes is None:
        if rc != 0:
            raise RuntimeError(
                f"SKILL GATE FIRED — INTENTIONAL BLOCK, NOT A SCRIPT ERROR. "
                f"{label} returned exit code {rc}. Apply aborted by design; "
                f"the script is working as intended. Read the gate's "
                f"explanation above (printed by {label}), fix paragraphs.json "
                f"or run with the gate's documented override flag, then re-run "
                f"apply. Do NOT work around this by calling textmatch_apply() "
                f"from a wrapper that skips gates — doing so silently ships "
                f"output below the quality the skill is designed to deliver."
            )
    else:
        if rc in block_codes:
            raise RuntimeError(
                f"SKILL GATE FIRED — INTENTIONAL BLOCK, NOT A SCRIPT ERROR. "
                f"{label} returned exit code {rc} (BLOCK). Apply aborted by "
                f"design. Read the gate's explanation above (printed by "
                f"{label}), fix the underlying issue, then re-run."
            )
        elif rc != 0:
            print(f"\n[apply] {label} returned WARN (exit {rc}). Continuing.")

def textmatch_apply(orig_docx_path, paragraphs_json_path, output_xml_path,
                    allow_bold_loss=False):
    """Apply translations using text matching. Auto-invokes mandatory
    validators (segment_shapes, reject_all, validate_apply) the full gate sequence."""
    scripts_dir = os.path.dirname(os.path.abspath(__file__))

    # Pre-apply: en_runs gate (extracted to validate_en_runs.py).
    en_runs_args = [sys.executable,
                    os.path.join(scripts_dir, 'validate_en_runs.py'),
                    paragraphs_json_path]
    if allow_bold_loss:
        en_runs_args.append('--allow-bold-loss')
    _run_validator(
        'validate_en_runs.py (pre-apply en_runs gate)',
        en_runs_args,
        block_codes={2},
    )

    # Pre-apply: validate_translations (final pass; also enforces the
    #  per-batch cap if the operator skipped batching).
    _run_validator(
        'validate_translations.py (final pre-apply pass)',
        [sys.executable,
         os.path.join(scripts_dir, 'validate_translations.py'),
         paragraphs_json_path],
        block_codes={2},
    )

    # Pre-apply (TC docs only): segment_shapes + reject_all.
    if _doc_has_tracked_changes(paragraphs_json_path):
        _run_validator(
            'validate_segment_shapes.py (pre-apply, TC docs)',
            [sys.executable,
             os.path.join(scripts_dir, 'validate_segment_shapes.py'),
             paragraphs_json_path,
             '--strict'],
        )
        _run_validator(
            'validate_reject_all.py (pre-apply, TC docs)',
            [sys.executable,
             os.path.join(scripts_dir, 'validate_reject_all.py'),
             paragraphs_json_path],
        )

    # Read original document.xml
    with zipfile.ZipFile(orig_docx_path) as zf:
        orig_bytes = zf.read('word/document.xml')

    # Dynamically register whatever xmlns prefixes the source document actually
    # uses. This MUST happen before ET.fromstring, or ET will assign synthetic
    # prefixes like ns3:/ns4: at serialization time for namespaces it doesn't
    # know, and those end up undeclared once we restore the original header.
    register_document_namespaces(orig_bytes)

    orig_header = extract_header(orig_bytes.decode('utf-8'))
    orig_root = ET.fromstring(orig_bytes)
    orig_body = orig_root.find(f'{W}body')
    # IMPORTANT: use recursive search to include paragraphs nested inside tables,
    # text boxes, and other container elements — not just direct children of w:body.
    # The extraction script (extract_paragraphs.py) uses root.iter() which is recursive,
    # so the apply script must search the same way to find all paragraphs.
    orig_paras = list(orig_body.findall(f'.//{W}p'))

    print(f"Original document has {len(orig_paras)} paragraphs (including table cells)")

    # Read translations
    with open(paragraphs_json_path, 'r', encoding='utf-8') as f:
        translations = json.load(f)

    print(f"paragraphs.json has {len(translations)} entries")

    # Build text index from original
    text_to_indices = build_text_index(orig_paras)

    # Match and apply translations
    used_indices = set()
    changes = 0
    matched_exact = 0
    matched_offset = 0
    not_found = 0
    skipped_same = 0
    skipped_empty = 0

    # Sort entries by idx to process in order (helps with duplicate disambiguation)
    entries_sorted = sorted(translations, key=lambda e: e.get('idx', 0))

    for entry in entries_sorted:
        idx = entry.get('idx', 0)
        it_text = (entry.get('text') or '').strip()
        en_text = (entry.get('en') or '').strip()
        en_deleted = (entry.get('en_deleted') or '').strip()
        en_runs_spec = entry.get('en_runs')
        original_runs = entry.get('runs', [])

        if not it_text or not en_text:
            skipped_empty += 1
            continue

        # skip-same-text only if no en_segments (TC paragraphs
        # may have segment-level work even when flat text matches).
        if it_text == en_text and not entry.get('en_segments'):
            skipped_same += 1
            continue

        # Find matching original paragraph
        match_idx = find_match(it_text, text_to_indices, used_indices, idx)

        if match_idx is None:
            not_found += 1
            if not_found <= 10:
                print(f"  NOT FOUND idx={idx}: {it_text[:60]}")
            continue

        used_indices.add(match_idx)
        offset = match_idx - idx

        if offset == 0:
            matched_exact += 1
        else:
            matched_offset += 1

        # Apply translation to the matched original paragraph
        orig_p = orig_paras[match_idx]

        # Tracked-change fast path: if the paragraph contains <w:ins>/<w:del>
        # markup, use the in-place text-distribution strategy so we preserve
        # the tracked-change wrappers and their author/date metadata. The
        # standard rebuild path below would wipe <w:r> direct children (and
        # so leave the runs nested inside <w:ins>/<w:del> unchanged, i.e.
        # still in the source language) while discarding the rest of the
        # paragraph's text — a silent data-loss bug.
        if has_track_changes(orig_p):
            en_segs = entry.get('en_segments')
            if apply_trackchanges_inplace(orig_p, en_text, it_text,
                                          en_deleted=en_deleted,
                                          en_segments=en_segs,
                                          en_runs_spec=en_runs_spec,
                                          original_runs=original_runs):
                changes += 1
            continue

        default_rpr = get_default_rpr_et(orig_p)

        # Determine formatting
        if en_runs_spec:
            if is_subheader_paragraph(en_text, original_runs):
                segments = [{"start": 0, "end": len(en_text), "bold": True, "italic": False}]
            else:
                segments = en_runs_spec
        else:
            segments = auto_detect_formatting(en_text, original_runs)

        # walk children, classify, preserve structural runs.
        # Text-bearing runs and hyperlinks are removed and replaced;
        # structural runs (page breaks, drawings, fields, etc.) stay
        # in place. See _run_should_be_preserved + 
        children_to_remove = []
        insertion_index = None
        for i, child in enumerate(list(orig_p)):
            if child.tag == f'{W}hyperlink':
                children_to_remove.append((i, child))
                if insertion_index is None:
                    insertion_index = i
            elif child.tag == f'{W}r':
                if _run_is_text_bearing(child):
                    children_to_remove.append((i, child))
                    if insertion_index is None:
                        insertion_index = i
                elif not _run_should_be_preserved(child):
                    # Empty run, plain <w:br/> line break, or other
                    # non-preserved non-text content — drop. Doesn't
                    # update insertion_index because we'd rather
                    # insert new content at a text-bearing position
                    # if any exists.
                    children_to_remove.append((i, child))

        # If no text-bearing run was found, fall back to "append at
        # end of paragraph" (existing behaviour for the rare case
        # where a paragraph has no text but apply was still called).
        if insertion_index is None:
            insertion_index = len(orig_p)

        # Compute the position where new runs will be inserted, after
        # accounting for removals that happen at lower indices.
        removals_before_insert = sum(
            1 for i, _ in children_to_remove if i < insertion_index)
        final_insertion_index = insertion_index - removals_before_insert

        # Now actually remove the marked children.
        for _, child in children_to_remove:
            orig_p.remove(child)

        # Build new translated runs as a Python list (not yet attached
        # to orig_p) so we can insert them all at the right position.
        new_runs = []
        for seg in segments:
            start = seg.get('start', 0)
            end = seg.get('end', len(en_text))
            seg_text = en_text[start:end]
            if not seg_text:
                continue
            bold = seg.get('bold', False)
            italic = seg.get('italic', False)
            # \t in en → <w:tab/>; \n → <w:br/>.
            if '\t' in seg_text or '\n' in seg_text:
                parts = re.split(r'([\t\n])', seg_text)
                for part in parts:
                    if part == '\t':
                        tab_run = ET.Element(f'{W}r')
                        ET.SubElement(tab_run, f'{W}tab')
                        new_runs.append(tab_run)
                    elif part == '\n':
                        br_run = ET.Element(f'{W}r')
                        ET.SubElement(br_run, f'{W}br')
                        new_runs.append(br_run)
                    elif part:
                        new_runs.append(make_run_et(
                            part, default_rpr, bold=bold, italic=italic))
            else:
                new_runs.append(make_run_et(
                    seg_text, default_rpr, bold=bold, italic=italic))

        # Insert all new runs at the computed insertion position.
        for offset, new_run in enumerate(new_runs):
            orig_p.insert(final_insertion_index + offset, new_run)

        changes += 1

    print(f"\nResults:")
    print(f"  Matched at correct idx: {matched_exact}")
    print(f"  Matched with offset: {matched_offset}")
    print(f"  Not found: {not_found}")
    print(f"  Skipped (same text): {skipped_same}")
    print(f"  Skipped (empty): {skipped_empty}")
    print(f"  Total changes applied: {changes}")

    # Serialize
    buf = io.BytesIO()
    tree = ET.ElementTree(orig_root)
    tree.write(buf, xml_declaration=True, encoding='UTF-8')
    rebuilt_xml = buf.getvalue().decode('utf-8')

    # Restore namespace declarations
    if orig_header:
        rebuilt_xml = re.sub(
            r'^<\?xml[^?]*\?>\s*<w:document[^>]*>',
            orig_header,
            rebuilt_xml,
            count=1,
            flags=re.DOTALL
        )

    # --- Namespace validation ---
    # Scan body for used-but-undeclared namespace prefixes; inject their
    # xmlns declarations into the root. Catches prefixes (a:, pic:, etc.)
    # that ET would otherwise emit without declaration.
    KNOWN_NS = {
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
        'o': 'urn:schemas-microsoft-com:office:office',
        'v': 'urn:schemas-microsoft-com:vml',
        'w10': 'urn:schemas-microsoft-com:office:word',
        'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
        'wps': 'http://schemas.microsoft.com/office/word/2010/wordprocessingShape',
        'wpg': 'http://schemas.microsoft.com/office/word/2010/wordprocessingGroup',
        'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
        'wp14': 'http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing',
        'w14': 'http://schemas.microsoft.com/office/word/2010/wordml',
        'w15': 'http://schemas.microsoft.com/office/word/2012/wordml',
        'wne': 'http://schemas.microsoft.com/office/word/2006/wordml',
        # w16* family — must mirror NAMESPACES above.
        'w16': 'http://schemas.microsoft.com/office/word/2018/wordml',
        'w16cex': 'http://schemas.microsoft.com/office/word/2018/wordml/cex',
        'w16cid': 'http://schemas.microsoft.com/office/word/2016/wordml/cid',
        'w16du': 'http://schemas.microsoft.com/office/word/2023/wordml/word16du',
        'w16sdtdh': 'http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash',
        'w16sdtfl': 'http://schemas.microsoft.com/office/word/2024/wordml/sdtformatlock',
        'w16se': 'http://schemas.microsoft.com/office/word/2015/wordml/symex',
    }
    declared = set(re.findall(r'xmlns:([\w.-]+)=', rebuilt_xml[:5000]))
    # Prefixes used on element tags or attribute names. Allow digits and the
    # w16* family (which contains no digits but has letters only, so the
    # original \w{1,5} matches; we widen to \w{1,8} to cover w16sdtdh etc.).
    used_in_tags = set(re.findall(r'<(\w{1,8}):', rebuilt_xml))
    used_in_attrs = set(re.findall(r'[\s"](\w{1,8}):[A-Za-z_]', rebuilt_xml[:200000]))
    real_prefixes = {p for p in (used_in_tags | used_in_attrs) if p in KNOWN_NS}
    missing = real_prefixes - declared
    if missing:
        inject = ' '.join(f'xmlns:{p}="{KNOWN_NS[p]}"' for p in sorted(missing))
        rebuilt_xml = rebuilt_xml.replace(
            '<w:document ',
            f'<w:document {inject} ',
            1
        )
        print(f"  Injected missing namespace declarations: {sorted(missing)}")

    # --- Synthetic-prefix leak detection ---
    # If, despite everything above, any `nsN:` prefix (ElementTree's synthetic
    # fallback) leaked into the output, fail loudly rather than silently
    # producing a Word-incompatible file. LibreOffice will happily open such
    # files — Word will not — so this is the last defence against regressions.
    synthetic = sorted(set(re.findall(r'[\s"<](ns\d+):[A-Za-z_]', rebuilt_xml)))
    if synthetic:
        raise RuntimeError(
            "Namespace corruption: ElementTree assigned synthetic prefixes "
            f"{synthetic} to namespaces it did not recognise. The resulting "
            ".docx will not open in Microsoft Word. This usually means a new "
            "OOXML namespace appeared in the source document that is not yet "
            "covered by NAMESPACES / register_document_namespaces(). Inspect "
            "the original word/document.xml root element for the offending "
            "xmlns:* declarations and add them to NAMESPACES."
        )

    # --- Strip revision tracking attributes ---
    # These cause Word to show tracked changes (formatting changes, rsid markers).
    # Remove w:rsidR, w:rsidRDefault, w:rsidRPr, w:rsidP, w:rsidDel, w:rsidSect
    # from all elements. This is safe because revision tracking is not needed in
    # the translated output.
    rebuilt_xml = re.sub(r' w:rsid\w+="[^"]*"', '', rebuilt_xml)
    print("  Stripped revision tracking attributes (rsid*)")

    # --- Strip w:lang from paragraph-level rPr as well ---
    # The make_run_et function strips w:lang from run-level rPr, but paragraph-
    # level rPr can also carry language tags that trigger tracked changes.
    rebuilt_xml = re.sub(
        r'<w:lang[^/]*/>', '', rebuilt_xml
    )
    print("  Stripped language tags (w:lang)")

    # --- Source-language remnant scan ---
    # Scan translated text for source-language marker words via
    # source_language_markers. Whole-word matching avoids false
    # positives like "allocated"/"already".
    source_lang = None
    # Prefer the language stored on paragraphs.json, if the caller set one.
    if hasattr(textmatch_apply, '_source_language_override'):
        source_lang = textmatch_apply._source_language_override
    if not source_lang:
        # Auto-detect from the source-language text in paragraphs.json.
        try:
            with open(paragraphs_json_path, 'r', encoding='utf-8') as _f:
                _data = json.load(_f)
            sample = ' '.join(
                (p.get('text') or '') for p in _data[:60]
            )
            source_lang = detect_language(sample)
        except Exception:
            source_lang = None

    # Scan both the accept-all view (<w:t>) and the reject-all / markup view
    # (<w:delText>). A nested <w:ins><w:del>SOURCE</w:del></w:ins> phantom
    # renders as empty under accept-all, so scanning only <w:t> misses the
    # source-language strike-through that a reviewer with "Show Markup" on
    # still sees. Reporting the two views separately tells the translator
    # exactly which view to inspect.
    remnants_accept = []
    remnants_reject = []
    if source_lang:
        accept_text = ' '.join(
            m.group(1) for m in re.finditer(r'<w:t[^>]*>([^<]+)</w:t>', rebuilt_xml)
        )
        del_text = ' '.join(
            m.group(1) for m in re.finditer(r'<w:delText[^>]*>([^<]+)</w:delText>', rebuilt_xml)
        )
        remnants_accept = scan_remnants(accept_text, source_lang)
        # Reject-all view is the union of w:t outside w:ins and w:delText
        # content. Rather than re-walk the XML we approximate by scanning the
        # union of accept_text + del_text — any source-language hit in either
        # bucket is a real remnant. This over-reports slightly for an ins
        # whose source was already translated, but in practice the translator
        # will have filled that in so both views are clean.
        remnants_reject = scan_remnants(del_text, source_lang)

    if source_lang:
        label = source_lang.capitalize()
    else:
        label = 'source-language'

    def _print_hits(view_label, hits):
        print(f"\n  WARNING: {len(hits)} possible {label} remnant(s) detected ({view_label}):")
        seen = set()
        for marker, ctx in hits[:15]:
            key = ctx[:60]
            if key not in seen:
                seen.add(key)
                print(f"    -> '{marker}' in: {ctx}...")
        if len(hits) > 15:
            print(f"    ... and {len(hits) - 15} more")
        print(f"  Review these and fix manually if they are genuine {label} remnants.")

    if not source_lang:
        # Unknown source language — we cannot scan reliably. Announce, don't fail.
        print("  Source-language scan: SKIPPED "
              "(could not auto-detect source language — pass --source-language)")
    else:
        any_hit = False
        if remnants_accept:
            _print_hits('accept-all view', remnants_accept)
            any_hit = True
        if remnants_reject:
            _print_hits('reject-all / markup view', remnants_reject)
            any_hit = True
        if not any_hit:
            print(
                f"  Source-language scan: CLEAN (no {label} remnants in "
                f"accept-all or reject-all view)"
            )

    os.makedirs(os.path.dirname(output_xml_path) or '.', exist_ok=True)
    with open(output_xml_path, 'wb') as f:
        f.write(rebuilt_xml.encode('utf-8'))

    print(f"\nOutput written to {output_xml_path}")

    # --- POST-APPLY MANDATORY GATE -------------------------------------
    # validate_apply.py confirms every declared token from paragraphs.json
    # landed in the produced document.xml. MANDATORY for every document.
    _run_validator(
        'validate_apply.py --strict (post-apply)',
        [sys.executable,
         os.path.join(scripts_dir, 'validate_apply.py'),
         paragraphs_json_path,
         output_xml_path,
         '--strict'],
    )

    return changes

if __name__ == '__main__':
    _check_self_integrity()
    import argparse
    parser = argparse.ArgumentParser(
        description='Apply translations from paragraphs.json onto original document.xml.')
    parser.add_argument('original_docx', help='Path to original .docx')
    parser.add_argument('paragraphs_json', help='Path to paragraphs.json')
    parser.add_argument('output_xml', help='Path to write output document.xml')
    parser.add_argument('--allow-bold-loss', action='store_true',
                        help=('Bypass the en_runs gate on detected definitions '
                              'sections. Use only when bold loss is genuinely '
                              'acceptable (e.g., simple drafts where the '
                              'defined-term bold-italic is not needed).'))
    args = parser.parse_args()
    textmatch_apply(args.original_docx, args.paragraphs_json, args.output_xml,
                    allow_bold_loss=args.allow_bold_loss)

# === SKILL FILE COMPLETE ===
