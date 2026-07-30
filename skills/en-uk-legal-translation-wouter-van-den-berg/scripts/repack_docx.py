"""Repack a translated document.xml back into the original .docx.

Uses Python's zipfile to copy the original ZIP structure byte-for-byte,
replacing only word/document.xml (and optionally word/numbering.xml,
word/settings.xml, word/headerN.xml, word/footerN.xml). This avoids
the case-sensitivity and directory-entry issues that arise when using
shell unzip + zip, which can produce files that Word on Windows refuses
to open.

Post-repack scan
----------------
After writing the final .docx, the script re-opens it and runs
``source_language_markers.scan_remnants`` over every XML part. The source
language is auto-detected from the ORIGINAL .docx's word/document.xml.
Any source-language remnants surviving in the delivered .docx are
printed as WARNING lines with their XML-file location so the operator
can decide whether to re-run translation on the affected part. The scan
is additive — the repack still exits 0 regardless of hits.

Usage:
    python repack_docx.py <original.docx> <translated_document.xml> <output.docx> [--numbering <translated_numbering.xml>] [--headers-footers-dir <dir>] [--clean-track-revisions]
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



# Make scripts/ importable so we can reach source_language_markers when
# repack_docx.py is invoked from an arbitrary working directory.
_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)
try:
    from source_language_markers import detect_language as _detect_lang
    from source_language_markers import scan_remnants as _scan_remnants
except Exception:  # pragma: no cover — scan is best-effort.
    _detect_lang = None
    _scan_remnants = None

def _run_pre_repack_validator(label, args):
    """Auto-invoke a validator script as a subprocess before bundling.
    Mandatory pre-repack gate — refuses to bundle on non-zero exit."""
    import subprocess
    print(f"\n{'=' * 60}\n[repack] auto-running {label}\n{'=' * 60}")
    result = subprocess.run(args, capture_output=False)
    if result.returncode != 0:
        raise RuntimeError(
            f"{label} returned exit code {result.returncode}. Repack "
            f"aborted; no .docx written. Fix the issues above and re-run."
        )

def repack(orig_docx, translated_doc_xml, output_docx,
           translated_numbering_xml=None, headers_footers_dir=None,
           translated_comments_xml=None,
           translated_footnotes_xml=None, translated_endnotes_xml=None,
           clean_track_revisions=True,
           paragraphs_json=None):
    """Copy orig_docx to output_docx, replacing word/document.xml and any
    optionally-supplied auxiliary XML parts (numbering, headers/footers,
    comments, footnotes, endnotes).

    CRITICAL: every auxiliary XML passed in MUST have been produced by a
    namespace-safe translator (translate_comments.py, translate_headers_footers.py,
    translate_numbering.py). Do NOT hand this function XML that was round-tripped
    through ElementTree — it will have mangled namespace prefixes (ns1:, ns2:, etc.)
    and Word will refuse to open the .docx.

    Rev11 (final): auto-runs two MANDATORY pre-bundle validators:

    * ``lexicon_compliance.py --stage pre-repack`` on the translated
      document.xml — catches calque-drift introduced after apply by
      post_process / strip_noop / reorder_definitions.
    * ``validate_apply.py --strict`` if ``paragraphs_json`` is supplied
      — re-checks token presence in the post-modification document.xml.

    Both used to be separate operator-invoked steps (Step 8d, Step 8e);
     folds them into repack so the operator runs ONE command and
    cannot accidentally skip either gate.
    """
    scripts_dir = os.path.dirname(os.path.abspath(__file__))

    # --- PRE-REPACK MANDATORY GATES ------------------------------------
    # Run before any byte is written to output_docx so failures abort
    # cleanly without producing a half-baked .docx.
    _run_pre_repack_validator(
        'lexicon_compliance.py --stage pre-repack',
        [sys.executable,
         os.path.join(scripts_dir, 'lexicon_compliance.py'),
         translated_doc_xml,
         '--stage', 'pre-repack'],
    )
    if paragraphs_json:
        _run_pre_repack_validator(
            'validate_apply.py --strict (post-modification check)',
            [sys.executable,
             os.path.join(scripts_dir, 'validate_apply.py'),
             paragraphs_json,
             translated_doc_xml,
             '--strict'],
        )
    else:
        print(
            "\n[repack] WARNING: --paragraphs not supplied; "
            "skipping validate_apply.py --strict pre-bundle check. "
            "Pass --paragraphs <paragraphs.json> to enable."
        )

    with open(translated_doc_xml, 'rb') as f:
        new_doc_xml = f.read()

    # Clean empty rPr elements that Word flags as errors
    new_doc_xml = re.sub(rb'<w:rPr/>', b'', new_doc_xml)
    new_doc_xml = re.sub(rb'<w:rPr></w:rPr>', b'', new_doc_xml)

    # --- Silent-regression guard ---
    # If the directory containing the translated document.xml also holds
    # auxiliary translated parts (numbering.xml / comments.xml / headerN.xml /
    # footerN.xml / footnotes.xml / endnotes.xml) but the corresponding flag
    # was not passed, the delivered .docx will silently keep the original
    # (untranslated) part. Warn loudly so the operator can re-run.
    _doc_dir = os.path.dirname(os.path.abspath(translated_doc_xml))
    _warn_lines = []
    if _doc_dir:
        # numbering.xml
        if (not translated_numbering_xml and
                os.path.exists(os.path.join(_doc_dir, 'numbering.xml'))):
            _warn_lines.append(
                f"{os.path.join(_doc_dir, 'numbering.xml')} appears translated "
                "but --numbering was not passed."
            )
        # comments.xml
        if (not translated_comments_xml and
                os.path.exists(os.path.join(_doc_dir, 'comments.xml'))):
            _warn_lines.append(
                f"{os.path.join(_doc_dir, 'comments.xml')} appears translated "
                "but --comments was not passed."
            )
        # footnotes.xml
        if (not translated_footnotes_xml and
                os.path.exists(os.path.join(_doc_dir, 'footnotes.xml'))):
            _warn_lines.append(
                f"{os.path.join(_doc_dir, 'footnotes.xml')} appears translated "
                "but --footnotes was not passed."
            )
        # endnotes.xml
        if (not translated_endnotes_xml and
                os.path.exists(os.path.join(_doc_dir, 'endnotes.xml'))):
            _warn_lines.append(
                f"{os.path.join(_doc_dir, 'endnotes.xml')} appears translated "
                "but --endnotes was not passed."
            )
        # headerN.xml / footerN.xml — the translate_headers_footers.py script
        # writes them next to document.xml, so checking _doc_dir catches them
        # when --headers-footers-dir wasn't passed (which would have pointed at
        # the parent of _doc_dir, i.e. the 'final' folder).
        if not headers_footers_dir:
            for hf_name in ('header1', 'header2', 'header3', 'header4',
                            'footer1', 'footer2', 'footer3', 'footer4'):
                hf_path = os.path.join(_doc_dir, f'{hf_name}.xml')
                if os.path.exists(hf_path):
                    _warn_lines.append(
                        f"{hf_path} appears translated but --headers-footers-dir "
                        "was not passed."
                    )
    if _warn_lines:
        print("WARNING: auxiliary translated XML detected but not wired into repack:")
        for _w in _warn_lines:
            print(f"  - {_w}")
        print(
            "         The delivered .docx will contain the original "
            "(untranslated) part(s). Re-run with the appropriate flag(s) if "
            "that is not intentional."
        )

    new_numbering_xml = None
    if translated_numbering_xml and os.path.exists(translated_numbering_xml):
        with open(translated_numbering_xml, 'rb') as f:
            new_numbering_xml = f.read()

    # --- Optional replacements for comments / footnotes / endnotes ---
    aux_replacements = {}  # zip path -> bytes
    for zip_path, src_path in [
        ('word/comments.xml', translated_comments_xml),
        ('word/footnotes.xml', translated_footnotes_xml),
        ('word/endnotes.xml', translated_endnotes_xml),
    ]:
        if src_path and os.path.exists(src_path):
            with open(src_path, 'rb') as f:
                aux_replacements[zip_path] = f.read()
            print(f"  Will replace {zip_path} with translated version")

    # --- Load translated header/footer XML files ---
    # headers_footers_dir should contain word/headerN.xml and word/footerN.xml
    # for any headers/footers that were translated. Files not present in the
    # directory will use the original from the source .docx.
    hf_replacements = {}  # normalized zip path -> bytes
    if headers_footers_dir:
        for hf_name in ['header1', 'header2', 'header3', 'header4',
                         'footer1', 'footer2', 'footer3', 'footer4']:
            hf_path = os.path.join(headers_footers_dir, 'word', f'{hf_name}.xml')
            if os.path.exists(hf_path):
                with open(hf_path, 'rb') as f:
                    hf_replacements[f'word/{hf_name}.xml'] = f.read()
                print(f"  Will replace word/{hf_name}.xml with translated version")

        # --- Loud failure if the flag was passed but nothing was found ---
        # The user's workflow is: --headers-footers-dir <dir> means "replace
        # my translated header/footer XML files into the output docx". If we
        # silently find zero files, the delivered docx keeps the original
        # (untranslated) source-language headers — exactly the defect the
        # post-repack remnant scanner had to chase down. Fail loud.
        if not hf_replacements:
            # Look for the common misconfig: user pointed at word/ instead
            # of its parent. The loop above expects <dir>/word/headerN.xml.
            # If the supplied dir is itself named 'word/' OR already contains
            # headerN.xml at its top level, the likely fix is to pass its
            # parent directory.
            likely_misconfig = False
            suggested = None
            if os.path.isdir(headers_footers_dir):
                dir_base = os.path.basename(os.path.abspath(headers_footers_dir.rstrip('/\\')))
                own_entries = set(os.listdir(headers_footers_dir))
                own_has_hf = any(
                    f'{hf}.xml' in own_entries
                    for hf in ('header1', 'header2', 'header3', 'header4',
                               'footer1', 'footer2', 'footer3', 'footer4')
                )
                if dir_base.lower() == 'word' or own_has_hf:
                    likely_misconfig = True
                    suggested = os.path.dirname(
                        os.path.abspath(headers_footers_dir.rstrip('/\\')))

            msg_lines = [
                f"--headers-footers-dir was passed but no "
                f"word/headerN.xml or word/footerN.xml files were found "
                f"under {headers_footers_dir!r}.",
                "",
                "The script expects the layout:",
                f"    {headers_footers_dir}/word/header1.xml",
                f"    {headers_footers_dir}/word/footer1.xml",
                "    ... etc",
            ]
            if likely_misconfig and suggested:
                msg_lines += [
                    "",
                    "It looks like you passed the inner word/ directory. "
                    f"Try passing its parent instead:",
                    f"    --headers-footers-dir {suggested!r}",
                ]
            msg_lines += [
                "",
                "Refusing to repack: the delivered .docx would contain the "
                "original (untranslated) headers/footers and the defect "
                "would only surface via the post-repack remnant scan.",
            ]
            raise RuntimeError('\n'.join(msg_lines))

    # --- Normalize case-inconsistent paths ---
    # Some .docx files (especially from older Word versions) contain paths
    # like customXML/ alongside customXml/. Word tolerates this in its own
    # files but flags it as "unreadable content" after a Python repack.
    # We normalize all paths to the canonical lowercase form.
    CASE_NORMALIZATIONS = {
        'customxml/': 'customXml/',  # customXML/ → customXml/
    }

    def normalize_path(path):
        """Normalize known case-inconsistent directory prefixes."""
        lower = path.lower()
        for pattern, replacement in CASE_NORMALIZATIONS.items():
            if lower.startswith(pattern) and not path.startswith(replacement):
                return replacement + path[len(pattern):]
        return path

    with zipfile.ZipFile(orig_docx, 'r') as zin:
        # --- Identify orphaned customXml items (no itemProps/rels) ---
        # These are third-party metadata (e.g. iManage) that were injected
        # without proper OOXML companion files.  Rather than trying to
        # generate companions (which Word still rejects for UTF-16 items
        # and non-standard encodings), we strip them entirely — item file,
        # relationship entries, and Content_Types entries.
        all_names = set(zin.namelist())
        all_names_lower = {n.lower() for n in all_names}
        orphan_items = set()          # normalized paths to skip
        orphan_nums = set()           # item numbers that are orphaned
        item_pat = re.compile(r'^customXml/item(\d+)\.xml$', re.IGNORECASE)
        for name in all_names:
            norm = normalize_path(name)
            m = item_pat.match(norm)
            if m:
                num = m.group(1)
                props_exists = f'customxml/itemprops{num}.xml' in all_names_lower
                rels_exists = f'customxml/_rels/item{num}.xml.rels' in all_names_lower
                if not props_exists or not rels_exists:
                    orphan_items.add(norm.lower())
                    orphan_nums.add(num)
                    print(f"  Stripping orphaned customXml item{num} "
                          f"(props={props_exists}, rels={rels_exists})")

        # Also fix relationships and Content_Types that reference wrong-case paths
        rels_fixups = {}  # filename -> fixed content bytes
        for item in zin.infolist():
            if item.filename.endswith('.rels') or item.filename == '[Content_Types].xml':
                content = zin.read(item.filename).decode('utf-8')
                new_content = content
                for pattern, replacement in CASE_NORMALIZATIONS.items():
                    for variant in re.findall(r'(?<=/)(customXML|CUSTOMXML|CustomXml|CustomXML)(?=/)', new_content, re.IGNORECASE):
                        canonical = replacement.rstrip('/')
                        if variant != canonical:
                            new_content = new_content.replace('/' + variant + '/', '/' + canonical + '/')
                            new_content = new_content.replace('/' + variant + '"', '/' + canonical + '"')

                # --- Remove relationship entries for orphaned customXml items ---
                for num in orphan_nums:
                    # Remove <Relationship ... Target="...itemN.xml" .../>
                    new_content = re.sub(
                        r'<Relationship[^>]*Target="[^"]*item' + num + r'\.xml"[^/]*/>\s*',
                        '', new_content)

                # --- Fix absolute Target paths in word/_rels/document.xml.rels ---
                if item.filename.startswith('word/_rels/'):
                    new_content = re.sub(
                        r'Target="/customXml/',
                        'Target="../customXml/',
                        new_content,
                        flags=re.IGNORECASE
                    )

                # --- Fix non-standard relationship IDs ---
                if item.filename.endswith('.rels') and item.filename != '[Content_Types].xml':
                    existing_rids = set(re.findall(r'Id="(rId\d+)"', new_content))
                    max_rid = 0
                    for rid in existing_rids:
                        num_r = int(rid[3:])
                        if num_r > max_rid:
                            max_rid = num_r
                    all_ids = re.findall(r'Id="([^"]+)"', new_content)
                    for old_id in all_ids:
                        if not re.match(r'^rId\d+$', old_id):
                            max_rid += 1
                            new_id = f'rId{max_rid}'
                            new_content = new_content.replace(
                                f'Id="{old_id}"', f'Id="{new_id}"')
                            print(f"  Fixed non-standard rel Id: {old_id} → {new_id}")

                if new_content != content:
                    rels_fixups[item.filename] = new_content.encode('utf-8')

        with zipfile.ZipFile(output_docx, 'w', zipfile.ZIP_DEFLATED) as zout:
            seen_normalized = set()  # track normalized paths to skip duplicates
            for item in zin.infolist():
                if item.is_dir():
                    continue

                norm_filename = normalize_path(item.filename)
                if norm_filename != item.filename:
                    print(f"  Normalized path: {item.filename} → {norm_filename}")

                # Skip orphaned customXml items
                if norm_filename.lower() in orphan_items:
                    print(f"  Skipped orphan: {norm_filename}")
                    continue

                # Skip duplicates after normalization
                if norm_filename.lower() in seen_normalized:
                    print(f"  Skipped duplicate: {item.filename}")
                    continue
                seen_normalized.add(norm_filename.lower())

                new_item = zipfile.ZipInfo(norm_filename)
                new_item.compress_type = item.compress_type

                if norm_filename == 'word/document.xml':
                    zout.writestr(new_item, new_doc_xml)

                elif norm_filename == 'word/numbering.xml' and new_numbering_xml:
                    zout.writestr(new_item, new_numbering_xml)

                elif norm_filename in hf_replacements:
                    zout.writestr(new_item, hf_replacements[norm_filename])

                elif norm_filename in aux_replacements:
                    zout.writestr(new_item, aux_replacements[norm_filename])

                elif norm_filename == 'word/settings.xml' and clean_track_revisions:
                    content = zin.read(item.filename).decode('utf-8')
                    content = re.sub(r'<w:trackRevisions[^/]*/>', '', content)
                    content = re.sub(r'<w:trackRevisions[^>]*>[^<]*</w:trackRevisions>', '', content)
                    zout.writestr(new_item, content.encode('utf-8'))

                elif item.filename in rels_fixups:
                    zout.writestr(new_item, rels_fixups[item.filename])

                else:
                    data = zin.read(item.filename)
                    zout.writestr(new_item, data)

    print(f"Repacked: {output_docx}")
    # Verify
    with zipfile.ZipFile(output_docx) as z:
        bad = z.testzip()
        if bad:
            print(f"  WARNING: ZIP integrity check failed on: {bad}")
        else:
            print(f"  ZIP OK ({len(z.namelist())} files)")

        # Check for case conflicts
        lower_map = {}
        for name in z.namelist():
            ln = name.lower()
            if ln in lower_map and lower_map[ln] != name:
                print(f"  WARNING: case conflict: {lower_map[ln]} vs {name}")
            lower_map[ln] = name

    # --- Post-repack source-language remnant scan ---
    # Re-open the delivered .docx and scan every XML part for source-language
    # remnants using the same marker lists the apply step already uses. This
    # catches untranslated parts (comments.xml, footnotes.xml, headerN.xml,
    # text boxes inside document.xml, etc.) that would otherwise ship silently.
    #
    # Source language is auto-detected from the ORIGINAL .docx's
    # word/document.xml. If detection fails (too little body text, unsupported
    # language, or source_language_markers not importable), the scan is
    # skipped silently — the repack itself is not affected.
    if _detect_lang is not None and _scan_remnants is not None:
        _TAG_STRIP_RE = re.compile(r'<[^>]+>')
        try:
            with zipfile.ZipFile(orig_docx) as zin:
                orig_doc_xml = ''
                if 'word/document.xml' in zin.namelist():
                    orig_doc_xml = zin.read('word/document.xml').decode(
                        'utf-8', errors='ignore')
            # Strip XML tags BEFORE auto-detecting. Otherwise single-letter
            # function-word markers (Polish `\bw\b`, `\bz\b`, `\bi\b`;
            # Dutch `\bde\b`) false-match against `<w:r>`, `<w:p>`, attribute
            # names like `w:rsidR`, etc., and dominate the score.
            orig_doc_text = _TAG_STRIP_RE.sub(' ', orig_doc_xml)
            src_lang = _detect_lang(orig_doc_text)
        except Exception:
            src_lang = None

        if src_lang:
            print(
                f"  Post-repack remnant scan: language={src_lang}, "
                "scanning every XML part in the delivered .docx..."
            )
            total_hits = 0
            per_part_hits = []
            with zipfile.ZipFile(output_docx) as zout_check:
                xml_parts = [
                    n for n in zout_check.namelist()
                    if n.lower().endswith('.xml')
                    and (n.startswith('word/') or n == 'word/document.xml')
                ]
                # Narrow to the parts that actually carry user-visible prose.
                # Settings/styles/fontTable/theme etc. are structural and can
                # contain source-language strings that are never shown.
                _PROSE_PARTS = {
                    'word/document.xml',
                    'word/comments.xml',
                    'word/footnotes.xml',
                    'word/endnotes.xml',
                }
                for part_name in xml_parts:
                    # Include headerN.xml, footerN.xml, and the fixed list above.
                    base = os.path.basename(part_name)
                    is_header_footer = (
                        base.startswith('header') and base.endswith('.xml')
                    ) or (
                        base.startswith('footer') and base.endswith('.xml')
                    )
                    if part_name not in _PROSE_PARTS and not is_header_footer:
                        continue
                    try:
                        part_bytes = zout_check.read(part_name)
                        part_text = part_bytes.decode('utf-8', errors='ignore')
                    except Exception:
                        continue
                    # Strip XML tags so we scan only the text that the reader sees,
                    # not attribute names / rsid values / style IDs.
                    text_only = _TAG_STRIP_RE.sub(' ', part_text)
                    hits = _scan_remnants(text_only, src_lang)
                    if hits:
                        per_part_hits.append((part_name, hits))
                        total_hits += len(hits)

            if total_hits:
                print(
                    f"  WARNING: post-repack scan found {total_hits} "
                    f"{src_lang} remnant(s) in the delivered .docx:"
                )
                for part_name, hits in per_part_hits:
                    print(f"    {part_name}: {len(hits)} hit(s)")
                    for pat, ctx in hits[:5]:
                        snippet = ' '.join(ctx.split())[:120]
                        print(f"      {pat}: ...{snippet}...")
                    if len(hits) > 5:
                        print(f"      ... {len(hits) - 5} more (suppressed)")
                print(
                    "           Some hits may be verbatim-preserved content "
                    "(project names, entity names, reference codes) — review\n"
                    "           before delivering. Hits inside comments.xml, "
                    "footnotes.xml, or headerN.xml typically indicate the\n"
                    "           corresponding auxiliary part was not wired "
                    "into this repack. Re-run with the right flag."
                )
            else:
                print(
                    f"  Post-repack scan clean: no {src_lang} remnants "
                    "detected in the delivered .docx's prose parts."
                )
        else:
            print(
                "  Post-repack scan skipped: source language could not be "
                "auto-detected from the original .docx."
            )

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Repack translated document.xml (and optional auxiliary XML parts) '
                    'into a .docx')
    parser.add_argument('original', help='Original .docx file')
    parser.add_argument('translated_xml', help='Translated word/document.xml')
    parser.add_argument('output', help='Output .docx file path')
    parser.add_argument('--numbering', default=None,
                        help='Translated word/numbering.xml')
    parser.add_argument('--headers-footers-dir', default=None,
                        help='Directory containing translated word/headerN.xml '
                             'and word/footerN.xml (produced by translate_headers_footers.py)')
    parser.add_argument('--comments', default=None,
                        help='Translated word/comments.xml '
                             '(produced by translate_comments.py)')
    parser.add_argument('--footnotes', default=None,
                        help='Translated word/footnotes.xml '
                             '(produced via the regex-only approach — NOT ElementTree)')
    parser.add_argument('--endnotes', default=None,
                        help='Translated word/endnotes.xml '
                             '(produced via the regex-only approach — NOT ElementTree)')
    parser.add_argument('--no-clean-track-revisions', action='store_true',
                        help='Do not remove trackRevisions from settings.xml')
    parser.add_argument('--paragraphs', default=None,
                        help='Path to paragraphs.json (enables auto-run of '
                             'validate_apply.py --strict pre-bundle to catch token '
                             'drift introduced by post_process / strip_noop / '
                             'reorder_definitions). Strongly recommended.')
    args = parser.parse_args()
    repack(args.original, args.translated_xml, args.output,
           translated_numbering_xml=args.numbering,
           headers_footers_dir=args.headers_footers_dir,
           translated_comments_xml=args.comments,
           translated_footnotes_xml=args.footnotes,
           translated_endnotes_xml=args.endnotes,
           clean_track_revisions=not args.no_clean_track_revisions,
           paragraphs_json=args.paragraphs)

# === SKILL FILE COMPLETE ===
