"""Strip no-op tracked-change markers from the translated document.xml.

Run AFTER `apply_translations_textmatch.py` and `post_process.py`, BEFORE
`repack_docx.py`.

============================================================================
WHY THIS EXISTS
============================================================================

Source-language concept drafts commonly contain tracked-change edits that fix
source-language orthography only:

    Dutch    `mn`            -> `m.n.`           (abbreviation punctuation)
    Dutch    `pro-actief`    -> `proactief`      (spelling reform)
    Dutch    `zonneenergie`  -> `zonne-energie`  (hyphenation of a triple-vowel)
    Dutch    `coordinaat`    -> `coördinaat`     (diacritic restoration)
    Italian  `pò`            -> `po'`            (accent/apostrophe fix)
    German   `daß`           -> `dass`           (1996 spelling reform)

When translated into English, both sides collapse to the same English text:
`mn` and `m.n.` both become "in particular,"; `zonneenergie` and
`zonne-energie` both become "solar energy". The corresponding `<w:ins>`/`<w:del>`
markers in the translated output are no-ops — accepting or rejecting them
produces identical English. They add nothing for the reader and make the
redline look nonsensical.

This script removes them.

============================================================================
WHAT IT DOES
============================================================================

For each `<w:p>` in the document:

1. **Adjacent `<w:del>` + `<w:ins>` pair with identical text** (in either
   order, with optional "transparent" elements in between — `w:commentRangeStart`,
   `w:commentRangeEnd`, `w:bookmarkStart`, `w:bookmarkEnd`, `w:proofErr`):
   remove the `<w:del>` entirely and unwrap the `<w:ins>` (its `<w:r>`
   children remain in place as regular text).

2. **`<w:del>` with empty text content** (after whitespace normalisation):
   remove the wrapper entirely — there is nothing to delete.

3. **`<w:ins>` with empty text content**: remove the wrapper entirely —
   there is nothing to insert.

4. **Phantom `<w:ins>` wrapping only `<w:del>`** ("author A inserted,
   author B deleted A's insertion"): remove the outer wrapper entirely.
   Under both accept-all and reject-all the phantom is empty — the
   insertion was deleted, so accept yields nothing and reject rejects
   the insertion. Keeping it only pollutes the markup view with
   strike-through source-language text that no downstream scanner sees.
   Gated off by `--keep-phantom-tcs`.

Non-trivial edits — where del and ins have genuinely different English (e.g.
a date digit change, a defined-term substitution, or a real content edit) —
are left completely untouched.

============================================================================
WHAT IT DOES NOT DO
============================================================================

- It does not alter the translation itself. By the time this runs, apply
  has already put English into every `<w:t>` / `<w:delText>`; this script
  only restructures the XML wrappers around that text.
- It does not touch auxiliary XML files (comments / headers / footers /
  footnotes / endnotes). Those rarely carry meaningful tracked changes, and
  when they do, they have already been translated by the namespace-safe
  scripts in this skill.
- It does not drop substantive edits. Even a single-character difference
  between del and ins disqualifies the cluster from stripping.

============================================================================
USAGE
============================================================================

    python strip_noop_tracked_changes.py <workdir>/final/word/document.xml

Idempotent: running twice has no effect.
"""
import sys
import os
import re
import argparse

from lxml import etree

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



W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

# Elements that can appear between a <w:del> and a <w:ins> without breaking
# their adjacency for the purposes of no-op detection. These are OOXML metadata
# markers that do not produce visible output in Word.
_TRANSPARENT_LOCALNAMES = {
    'commentRangeStart',
    'commentRangeEnd',
    'bookmarkStart',
    'bookmarkEnd',
    'proofErr',
}

def _localname(element):
    return etree.QName(element).localname

def _element_text(element):
    """Return the concatenated text of every <w:t> and <w:delText> descendant."""
    pieces = []
    for node in element.iter():
        tag = _localname(node)
        if tag in ('t', 'delText') and node.text:
            pieces.append(node.text)
    return ''.join(pieces)

def _normalise(text):
    """Whitespace-collapse and strip — used when comparing del and ins text."""
    return re.sub(r'\s+', ' ', text).strip()

def _unwrap(element):
    """Remove `element` from its parent, promoting each of its direct children
    into the same position in document order."""
    parent = element.getparent()
    idx = parent.index(element)
    for offset, child in enumerate(list(element)):
        parent.insert(idx + offset, child)
    parent.remove(element)

def _find_next_tc_sibling(children, start_index):
    """From position `start_index`, return (tc_index, sibling) for the next
    <w:del> or <w:ins>, skipping over transparent elements. If the first
    non-transparent sibling is neither del nor ins, return (None, None)."""
    j = start_index
    while j < len(children):
        tag = _localname(children[j])
        if tag in ('ins', 'del'):
            return j, children[j]
        if tag in _TRANSPARENT_LOCALNAMES:
            j += 1
            continue
        return None, None
    return None, None

def _is_noise_only(text):
    """Return True if `text` is empty, whitespace, or contains only punctuation
    and whitespace characters (no letters, digits, or currency symbols).

    Punctuation-only TCs are orthographic fragments carried over from the source
    language — a straggling period from a Dutch `. .` deletion, a lone comma
    from a punctuation-style edit. They have no semantic content in English and
    the reader does not benefit from seeing them flagged in the redline.
    """
    if not text:
        return True
    normalised = _normalise(text)
    if not normalised:
        return True
    # A character is "meaningful" if it could plausibly carry content in any
    # language: letters (Unicode), digits, currency symbols, the percent sign,
    # and ampersand. Pure punctuation, whitespace, and decorative characters
    # are ignored.
    for ch in normalised:
        if ch.isalnum() or ch in '%&$€£¥':
            return False
    return True

# Brackets that commonly signal "to-be-confirmed" placeholders in European
# legal drafts. When these appear as ins/del content adjacent to a content-
# bearing ins/del segment, they are NOT noise — they are part of a coherent
# semantic unit (e.g. `[1.2020]` as a placeholder date). Stripping the bracket
# wrappers while keeping the date insertion produces an output where the
# reviewer cannot see the Accept/Reject of the placeholder-resolution gesture.
_BRACKET_PAIRS = {'[': ']', '(': ')', '{': '}', '〈': '〉', '《': '》'}
_ALL_BRACKETS = set(_BRACKET_PAIRS.keys()) | set(_BRACKET_PAIRS.values())

def _is_bracket_only(text):
    """Return True if `text` consists entirely of bracket characters."""
    if not text:
        return False
    normalised = _normalise(text)
    if not normalised:
        return False
    return all(ch in _ALL_BRACKETS for ch in normalised)

def _has_content_bearing_tc_neighbour(paragraph, element, max_skip=8):
    """Check whether `element` (an ins/del) sits adjacent — within `max_skip`
    siblings in either direction — to another ins/del whose text is content-
    bearing (contains alphanumerics). Used to protect bracket ins/del that
    form a semantic unit with a neighbouring date/number/word insertion."""
    siblings = list(paragraph)
    try:
        idx = siblings.index(element)
    except ValueError:
        return False
    for step in range(1, max_skip + 1):
        for j in (idx - step, idx + step):
            if 0 <= j < len(siblings):
                sib = siblings[j]
                tag = _localname(sib)
                if tag not in ('ins', 'del'):
                    continue
                sib_text = _element_text(sib)
                if sib_text and any(ch.isalnum() for ch in sib_text):
                    return True
    return False

def _strip_empty_wrappers(paragraph):
    """Pass 1: strip any <w:del> or <w:ins> whose text content is empty, all
    whitespace, or all punctuation after normalisation. Returns count stripped.

    Exception: bracket-only ins/del (`[`, `]`, `(`, `)`, etc.) are PRESERVED
    when they sit adjacent to a content-bearing ins/del neighbour. This keeps
    placeholder-date tracked changes coherent in the redline — e.g. in a
    paragraph with `<ins>[</ins> ... <ins>15 January 2021</ins> ... <ins>]</ins>`,
    stripping the two bracket wrappers alone would leave the date insertion
    orphaned and the reviewer's Accept/Reject gesture would lose the "confirm
    this placeholder" context.
    """
    removed = 0
    for element in list(paragraph):
        tag = _localname(element)
        if tag not in ('ins', 'del'):
            continue
        text = _element_text(element)
        if not _is_noise_only(text):
            continue
        # Bracket-aware exception: keep bracket-only wrappers that flank a
        # content-bearing insertion/deletion.
        if _is_bracket_only(text) and _has_content_bearing_tc_neighbour(paragraph, element):
            continue
        element.getparent().remove(element)
        removed += 1
    return removed

def _strip_matching_pairs(paragraph):
    """Pass 2: strip adjacent (w:del, w:ins) and (w:ins, w:del) pairs whose
    normalised text is equal. Iterates until a pass produces no change.

    Returns count stripped.
    """
    total = 0
    while True:
        changed = False
        children = list(paragraph)
        for i, el in enumerate(children):
            tag = _localname(el)
            if tag not in ('ins', 'del'):
                continue
            j, neighbour = _find_next_tc_sibling(children, i + 1)
            if neighbour is None:
                continue
            neighbour_tag = _localname(neighbour)
            if {tag, neighbour_tag} != {'ins', 'del'}:
                continue
            if _normalise(_element_text(el)) != _normalise(_element_text(neighbour)):
                continue
            # No-op substitution: remove the del, unwrap the ins.
            ins_el = el if tag == 'ins' else neighbour
            del_el = el if tag == 'del' else neighbour
            del_el.getparent().remove(del_el)
            _unwrap(ins_el)
            total += 1
            changed = True
            break
        if not changed:
            break
    return total

def _strip_phantom_ins_wraps_del(paragraph):
    """Pass 3: remove <w:ins> elements whose only meaningful descendants are
    <w:del> / <w:delText>. By construction those "insert-then-delete" wrappers
    contribute nothing to either the accept-all or the reject-all view — the
    insertion was itself deleted, so accept yields nothing and reject rejects
    the insertion. Keeping them only pollutes the markup view with a
    strike-through source-language remnant that no downstream scanner sees.

    Returns count stripped. Metadata-only descendants (w:rPr, w:proofErr,
    bookmarkStart/End, commentRangeStart/End) do not disqualify the wrapper.
    """
    total = 0
    for element in list(paragraph.iter(f'{{{W}}}ins')):
        # Has any top-level <w:t> descendant with text? If so, this is a real
        # insertion and we must leave it alone.
        has_text_t = False
        has_nested_del = False
        for desc in element.iter():
            tag = _localname(desc)
            if tag == 't' and (desc.text or '').strip():
                has_text_t = True
                break
            if tag == 'del':
                has_nested_del = True
        if has_text_t:
            continue
        if not has_nested_del:
            # Empty ins with no nested del — handled by _strip_empty_wrappers.
            continue
        # Remove the entire wrapper. The nested <w:del> disappears with it,
        # which is the desired behaviour — the phantom was the nested del.
        parent = element.getparent()
        if parent is None:
            continue
        parent.remove(element)
        total += 1
    return total

def strip_noops(document_xml_path, keep_phantom_tcs=False):
    """Main entry point. Edits the file in place. Returns a summary dict."""

    # Capture the original root header so that we can graft it back after
    # lxml re-serialises. lxml preserves namespace prefixes much better than
    # ElementTree, but it still drops unused declarations — grafting is the
    # belt-and-braces approach used elsewhere in this skill.
    with open(document_xml_path, 'rb') as f:
        original_bytes = f.read()
    original_text = original_bytes.decode('utf-8')
    header_match = re.match(
        r'(<\?xml[^?]*\?>\s*<w:document[^>]*>)',
        original_text,
        re.DOTALL,
    )
    original_header = header_match.group(1) if header_match else None

    tree = etree.parse(document_xml_path)
    root = tree.getroot()

    empties = 0
    pairs = 0
    phantoms = 0
    for paragraph in root.iter(f'{{{W}}}p'):
        pairs += _strip_matching_pairs(paragraph)
        empties += _strip_empty_wrappers(paragraph)
        # Run the pair pass once more because stripping empties may have
        # exposed new adjacencies.
        pairs += _strip_matching_pairs(paragraph)
        if not keep_phantom_tcs:
            phantoms += _strip_phantom_ins_wraps_del(paragraph)

    tree.write(
        document_xml_path,
        xml_declaration=True,
        encoding='UTF-8',
        standalone=True,
    )

    if original_header:
        with open(document_xml_path, 'rb') as f:
            out_text = f.read().decode('utf-8')
        out_text = re.sub(
            r'^<\?xml[^?]*\?>\s*<w:document[^>]*>',
            original_header,
            out_text,
            count=1,
            flags=re.DOTALL,
        )
        with open(document_xml_path, 'wb') as f:
            f.write(out_text.encode('utf-8'))

    return {
        'pairs_stripped': pairs,
        'empty_wrappers_stripped': empties,
        'phantom_ins_del_stripped': phantoms,
    }

def main():
    parser = argparse.ArgumentParser(
        description='Strip no-op tracked-change markers from a translated document.xml'
    )
    parser.add_argument(
        'document_xml',
        help='Path to the translated document.xml (output of apply_translations_textmatch.py)',
    )
    parser.add_argument(
        '--keep-phantom-tcs',
        action='store_true',
        help='Preserve phantom ins-wraps-del wrappers (author A inserted, '
             'author B deleted A\'s insertion). Default behaviour strips them '
             'because they are a no-op in both accept-all and reject-all.',
    )
    args = parser.parse_args()

    if not os.path.exists(args.document_xml):
        print(f'ERROR: file not found: {args.document_xml}', file=sys.stderr)
        return 2

    summary = strip_noops(
        args.document_xml,
        keep_phantom_tcs=args.keep_phantom_tcs,
    )
    print(
        'Stripped {pairs_stripped} no-op del/ins pair(s), '
        '{empty_wrappers_stripped} empty wrapper(s) and '
        '{phantom_ins_del_stripped} phantom ins-wraps-del wrapper(s).'.format(**summary)
    )
    return 0

if __name__ == '__main__':
    sys.exit(main())

# === SKILL FILE COMPLETE ===
