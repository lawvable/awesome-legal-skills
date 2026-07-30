"""Post-apply lost-content validator.

Runs AFTER `apply_translations_textmatch.py` (and optionally after
`strip_noop_tracked_changes.py` + `post_process.py`) and compares the
translation declared in `paragraphs.json` (fields `en`, `en_deleted`,
`en_segments`) against what actually landed in the translated `document.xml`.

The check catches the "clause 5 dropped dates" class of defect, where a
translator wrote e.g.

    {"en_segments": [
      {"type": "regular", "en": "shall commence on "},
      {"type": "ins", "en": "[1 May 2020]"},
      {"type": "regular", "en": ". The road use fee ..."}
    ]}

but the produced document.xml ends up reading `shall commence on []. The road
use fee ...` — the bracket-contained date tokens were lost during text
distribution.

Implementation strategy:

1. Load `paragraphs.json`. For each paragraph with a non-empty `en`,
   `en_deleted`, or `en_segments`, build a set of "required tokens" — all
   words and dates of length >= 3 that the translator declared.
2. Parse the translated `document.xml`. For each paragraph, extract its
   combined text (both `<w:t>` and `<w:delText>`).
3. Compare per-paragraph: flag any required token that does not appear in
   the applied output.

The default run is advisory — the script prints a summary and any missing
tokens, and returns exit code 0. Pass `--strict` to return non-zero on any
miss, which blocks repack.

============================================================================
USAGE
============================================================================

    python validate_apply.py <workdir>/paragraphs.json <workdir>/final/word/document.xml
    python validate_apply.py <workdir>/paragraphs.json <workdir>/final/word/document.xml --strict

Exit codes:
    0 - no misses (always returned in advisory mode)
    1 - misses detected (only in --strict mode)
    2 - input/IO error
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict

from lxml import etree

# rev42: shared predicate with post_process.fix_spacing.
# `_collect_required_tokens` joins en_segments with whitespace
# inserted at every segment boundary where fix_spacing's predicate
# would fire. Mirrors fix_spacing's element-boundary space-insertion
# on the applied side, so declared and applied tokenise identically
# across the post-strip drift gate.
_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)
try:
    from post_process import will_fix_spacing_fire  # noqa: E402
except ImportError:
    # Fallback for environments where post_process isn't importable
    # (e.g. partial install). Inline the rule so validate_apply still
    # works; the post_process version remains the canonical source.
    _DOT_UPPER_ABBR_EXC = (
        'No.', 'no.', 'etc.', 'art.', 'S.p.A.', 'S.r.l.', '..', 'seq.',
    )
    _DOT_SINGLE_RE = re.compile(r'\b[A-Z]\.$')

    def will_fix_spacing_fire(prev_text, curr_text):  # type: ignore[no-redef]
        if not prev_text or not curr_text:
            return False
        pc, cc = prev_text[-1], curr_text[0]
        if pc.isalpha() and cc.isalpha():
            return True
        if pc.isalpha() and cc == '(':
            return True
        if pc == ')' and cc.isalpha():
            return True
        if pc == ';' and cc.isalpha():
            return True
        if pc == ',' and cc.isalpha():
            return True
        if pc == ':' and cc.isalpha():
            return True
        if pc == '.' and cc.isupper():
            if (not _DOT_SINGLE_RE.search(prev_text)
                    and not any(prev_text.endswith(s)
                                for s in _DOT_UPPER_ABBR_EXC)):
                return True
        if pc.isdigit() and cc.isupper():
            return True
        return False

def _emit_error(message):
    """Rev27: error helper at top of file (byte position shifted from
    where install pipeline was observed truncating)."""
    print(message, file=sys.stderr)

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

# Minimum token length to check. Short tokens (< 3 chars) produce too many
# false positives — "a", "to", "of" etc. appear everywhere.
_MIN_TOKEN_LEN = 3

# A "content-bearing" token is an alphanumeric run that may contain an
# embedded period or hyphen (for dates, hyphenated words, abbreviations).
_TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9.\-]*[A-Za-z0-9]|[A-Za-z0-9]+")

# sentence-boundary glue. An ``ins_then_del`` phantom segment
# ending in ``"...project."`` joined with the next regular segment
# starting in ``"hereinafter ..."`` produces the JSON joined string
# ``"project.hereinafter"`` — which ``_TOKEN_RE`` tokenises as ONE
# token because it allows internal periods (needed for
# ``S.p.A.``, ``art.1234``, ``v.2.3``, ``1234.50``). The applied XML
# keeps the two segments as adjacent ``<w:t>`` runs ``"project."``
# and ``"hereinafter"``; tokenising the joined element-text gives the
# same one-token result, but only because the runs happen to abut
# directly — once ``fix_spacing`` or ``strip_noop`` mutates the XML
# (inserting a space, or removing the phantom wrapper entirely), the
# applied side splits and the declared side does not. The result is a
# false-positive ``"project.hereinafter is missing"`` at the repack
# gate.
#
# The rule that distinguishes a sentence-boundary period from an
# abbreviation period is the *length of the lowercase run preceding
# the period*. ``S.p.A.``, ``i.e.``, ``e.g.``, ``a.m.``, ``p.m.``,
# ``S.r.l.`` all have 1-letter runs before each period (or an
# uppercase letter, which the lookbehind doesn't match). Sentence
# ends like ``project.hereinafter``, ``terminated.thereafter`` have
# 2+ lowercase letters preceding the period. Splitting on
# 2+-lowercase + ``.`` + lowercase preserves every legitimate Latin
# abbreviation pattern while breaking the phantom-glue case.
#
# Implemented as a pre-tokenise normalisation rather than a regex
# change so that the abbreviation token shape (``S.p.A``, ``v.2.3``,
# ``1234.50``) is preserved exactly as in . The substitution
# applies symmetrically to both declared and applied text, so domain
# names (``github.com``) and version numbers (``v.2.3``) tokenise
# consistently and produce no false negatives.
_SENTENCE_GLUE_RE = re.compile(r'(?<=[a-z])(?<=[a-z]{2})\.(?=[a-z])')

# structural words that post_process.py legitimately rewrites
# during Step 6 (Article ↔ Clause for internal cross-references). These
# tokens carry no content value — they're just legal-English structural
# vocabulary. Excluding them from the required-token set means
# validate_apply does not flag a paragraph as "missing Article" merely
# because post_process correctly rewrote it to "Clause" (or vice versa
# for an external reference the operator translated as "Clause" but
# post_process kept as "Article"). The actual content tokens (numbers,
# defined terms, named acts) are still required and still checked.
_STRUCTURAL_WORDS = frozenset({
    'article', 'articles', 'clause', 'clauses',
    'section', 'sections', 'paragraph', 'paragraphs',
    'sub-paragraph', 'subparagraph', 'sub-paragraphs', 'subparagraphs',
})

def _extract_tokens(text):
    if not text:
        return set()
    # pre-split sentence-boundary glue so phantom-segment-plus-
    # regular-segment joins like ``project.hereinafter`` tokenise as
    # two tokens. Symmetric on declared and applied → no false
    # negatives. Preserves Latin abbreviations whose internal periods
    # are preceded by single letters (``S.p.A.``, ``i.e.``, ``e.g.``).
    text = _SENTENCE_GLUE_RE.sub('. ', text)
    tokens = set()
    for m in _TOKEN_RE.finditer(text):
        tok = m.group(0)
        # Strip trailing punctuation that may have been caught.
        tok = tok.strip('.,;:!?()[]{}\'"-')
        if len(tok) < _MIN_TOKEN_LEN:
            continue
        low = tok.lower()
        # skip structural Article/Clause/Section/Paragraph
        # words — they're not content and post_process may rewrite
        # one to the other.
        if low in _STRUCTURAL_WORDS:
            continue
        tokens.add(low)
    return tokens

def _ortho_key(text):
    """Case-fold and collapse whitespace+ZWSP+zero-width-joiners.

    Two segments that produce the same key are orthographic variants of
    one another: the only differences are whitespace/punctuation-class
    noise. `strip_noop_tracked_changes._is_noise_only` collapses such
    (del, ins) pairs in the final XML, so they must collapse here too —
    otherwise `_collect_required_tokens` over-counts and validate_apply
    reports phantom missing tokens like ``particularin`` from
    [del: "in particular"][ins: "in particular"].
    """
    if text is None:
        return ''
    # Collapse any run of unicode whitespace or zero-width characters.
    return re.sub(r'[\s\u200b\u200c\u200d\ufeff]+', ' ', text).strip().lower()

def _dedupe_ortho_pairs(segments):
    """Mirror strip_noop_tracked_changes: a (del, ins) pair whose stripped
    English text is identical contributes only one copy of its tokens.

    The forward-pair case (del then ins) is what strip_noop actually
    unwraps; the reverse-pair case (ins then del of the same text) is
    rare but has the same net effect on the applied document. Both are
    collapsed to a single segment so `_collect_required_tokens` sees
    exactly what the reader sees after strip_noop has run.

    Returns a new list of segments. The original list is unchanged.
    """
    if not segments:
        return segments
    result = []
    i = 0
    n = len(segments)
    while i < n:
        a = segments[i]
        b = segments[i + 1] if i + 1 < n else None
        if (isinstance(a, dict) and isinstance(b, dict)
                and {a.get('type'), b.get('type')} == {'ins', 'del'}):
            key_a = _ortho_key(a.get('en') or '')
            key_b = _ortho_key(b.get('en') or '')
            if key_a and key_a == key_b:
                # Collapse to one copy (prefer the ins, since it's what
                # survives in the reader-visible output).
                keeper = a if a.get('type') == 'ins' else b
                result.append(keeper)
                i += 2
                continue
        result.append(a)
        i += 1
    return result

def _collect_required_tokens(paragraph_entry):
    """Return set_of_required_tokens for this paragraph.

    When the paragraph is represented by ``en_segments`` (one segment per
    tracked-change, comment-reference, or proofing-error boundary), the
    segments are joined before tokenising. Otherwise a word that straddles
    a segment boundary produces fragmented required tokens that will never
    appear in the concatenated applied output — a false positive.

    Examples of the failure mode we are avoiding:

      * A word like ``direction`` split by a ``w:commentReference`` into
        two w:t runs reads as one segment ``dir`` followed by one segment
        ``ection``. Tokenising each segment separately declares ``dir``
        and ``ection`` as required; the applied output has ``direction``;
        neither fragment matches.
      * A hyphenated compound like ``XY-coordinate`` split across an
        ``ins``/``del`` boundary reads as segments ``XY-`` and
        ``coordinate``. After per-segment stripping of trailing
        punctuation the required tokens become ``xy`` and ``coordinate``,
        neither of which matches ``xy-coordinate`` in the applied output.

    Concatenating the segments first makes the check see the same text
    the reader sees. This is a fix to what the validator *sees*, not a
    relaxation of what it requires.

    ORTHO-COLLAPSE: a (del, ins) pair with identical stripped English
    text is collapsed to a single copy before concatenation. Otherwise
    [del: "in particular"][ins: "in particular"] joins to
    ``in particularin particular`` and tokenises to include
    ``particularin`` — a phantom required token that cannot appear in
    the applied output, because ``strip_noop_tracked_changes`` unwraps
    the orthographic-no-op pair and the reader only sees
    ``in particular``. See ``_dedupe_ortho_pairs``.
    """
    return _collect_required_tokens_with_options(paragraph_entry,
                                                  post_spacing_fix=False)


def _collect_required_tokens_with_options(paragraph_entry, post_spacing_fix):
    """Underlying token collector with the rev42 fix_spacing simulation
    flag. When `post_spacing_fix=False` (the default, used by the
    apply-time gate where the document has NOT yet been through
    post_process.fix_spacing), join en_segments as-is and tokenise —
    preserves rev41 behaviour byte-for-byte. When `post_spacing_fix=True`
    (used by the post-strip gate inside post_process.py, where fix_spacing
    has already inserted spaces at element boundaries), simulate the
    same insertion on the declared side by walking segments and inserting
    ' ' between non-empty adjacent segments wherever
    `will_fix_spacing_fire(prev, curr)` returns True. This mirrors
    fix_spacing's element-boundary space-insertion, so declared and
    applied tokenise identically across the post-strip drift gate.
    """
    required = set()
    segments = paragraph_entry.get('en_segments')
    if segments:
        segments = _dedupe_ortho_pairs(segments)
        pieces = []
        prev_text = ''
        for seg in segments:
            if not isinstance(seg, dict):
                continue
            en = seg.get('en') or ''
            # Skip translator placeholder markers.
            if '<<TRANSLATE' in en:
                continue
            if not en:
                continue
            if (post_spacing_fix and prev_text
                    and will_fix_spacing_fire(prev_text, en)):
                pieces.append(' ')
            pieces.append(en)
            prev_text = en
        required |= _extract_tokens(''.join(pieces))
    else:
        for field in ('en', 'en_deleted'):
            val = paragraph_entry.get(field)
            if val:
                required |= _extract_tokens(val)
    return required

def _paragraph_applied_text(p_element):
    """Concatenate all w:t and w:delText in document order (Accept+Reject union).

    ``<w:tab/>`` and ``<w:br/>`` elements are treated as whitespace
    separators when joining. The declared side (``en`` in paragraphs.json)
    represents tabs and line-breaks as literal U+0009 / U+000A characters,
    which the token regex ``[A-Za-z0-9][A-Za-z0-9.\\-]*[A-Za-z0-9]``
    treats as token boundaries. Without a corresponding boundary on the
    applied side, paragraphs containing real ``<w:tab/>`` elements (e.g.
    signature blocks, witness rows) produce different tokenisations between
    declared and applied: declared ``"Vicente\\tSipka"`` →
    ``{"Vicente", "Sipka"}`` via the \\t boundary, applied ``"VicenteSipka"``
    → ``{"VicenteSipka"}`` one token, false-positive miss.

    Inserting a single space at every ``<w:tab/>`` / ``<w:br/>`` boundary
    when joining restores symmetric tokenisation. Symmetric on documents
    that have no tab/br elements (the loop simply never appends extra
    whitespace), so backward compatible.
    """
    pieces = []
    for node in p_element.iter():
        tag = etree.QName(node).localname
        if tag in ('t', 'delText') and node.text:
            pieces.append(node.text)
        elif tag in ('tab', 'br'):
            pieces.append(' ')
    return ''.join(pieces)

def _normalise_paragraph_text(text):
    """Return the paragraph's source text for matching. Matches the normalisation
    used by apply_translations_textmatch.py (which joins all w:t text)."""
    return re.sub(r'\s+', ' ', text or '').strip()

def validate(paragraphs_json_path, document_xml_path, post_spacing_fix=False):
    """Return (misses_by_paragraph, total_required, total_present).

    matching is **content-based** rather than positional. Each
    paragraphs.json entry is paired with the applied document.xml
    paragraph that has the highest token-set overlap with the entry's
    declared en-text, using a greedy claim-and-lock assignment in
    descending order of token-set distinctiveness. This eliminates the
    false-positive misses that the positional matcher produced after
    Step 7 (`reorder_definitions`) shuffled the definitions section in
    document.xml — paragraphs.json is still in source order, but
    document.xml has the alphabetically-reordered definitions, so
    positional alignment broke for every reordered paragraph.

    Falls back to positional matching when content-based matching
    finds no high-confidence pair (e.g. for very short en strings
    with no distinctive tokens).
    """
    with open(paragraphs_json_path, 'r', encoding='utf-8') as f:
        entries = json.load(f)

    tree = etree.parse(document_xml_path)
    root = tree.getroot()

    # Collect applied paragraphs from document.xml.
    applied_paragraphs = []  # list of (paragraph_idx, applied_text, applied_tokens)
    for ai, p in enumerate(root.iter(f'{{{W}}}p')):
        atext = _paragraph_applied_text(p)
        if atext.strip():
            applied_paragraphs.append((ai, atext, _extract_tokens(atext)))

    # Index json entries with non-empty required tokens.
    # rev42: when called with `post_spacing_fix=True` (from the post-strip
    # gate inside post_process.py, after fix_spacing has inserted spaces
    # at element boundaries on the applied side), the declared-side
    # required tokens are built with the same simulated insertion so the
    # comparison is symmetric. When called without the flag (apply-time
    # gate, before fix_spacing runs), declared tokens match the raw
    # post-distribute applied text — preserves rev41 behaviour.
    indexed_entries = []  # list of (json_idx, entry, required_tokens)
    for ji, entry in enumerate(entries):
        req = _collect_required_tokens_with_options(
            entry, post_spacing_fix=post_spacing_fix)
        if req:
            indexed_entries.append((ji, entry, req))

    # Content-based greedy matching. Process entries in descending
    # order of token-set size (most distinctive first) so they claim
    # their best-overlap doc paragraph before less distinctive
    # entries get a chance to collide on the same target.
    indexed_entries_by_dist = sorted(
        indexed_entries, key=lambda x: len(x[2]), reverse=True)

    matched = {}  # json_idx -> (applied_idx, applied_text, applied_tokens)
    used_applied = set()
    for ji, entry, required in indexed_entries_by_dist:
        best_overlap = -1
        best_choice = None
        for ai, atext, atokens in applied_paragraphs:
            if ai in used_applied:
                continue
            overlap = len(required & atokens)
            if overlap > best_overlap:
                best_overlap = overlap
                best_choice = (ai, atext, atokens)
        if best_choice is None:
            continue
        # Confidence threshold: at least 50% of required tokens
        # must be covered by the chosen paragraph for content match
        # to be considered reliable. Below threshold, leave unmatched
        # so the positional fallback can try (some paragraphs have
        # very few distinctive tokens).
        if best_overlap / max(len(required), 1) >= 0.50:
            matched[ji] = best_choice
            used_applied.add(best_choice[0])

    # Positional fallback for entries that did not get a high-
    # confidence content match. Rare in practice; covers very short
    # en strings (single-word definitions, headings, etc.).
    for pos_i, (ji, entry, required) in enumerate(indexed_entries):
        if ji in matched:
            continue
        if pos_i < len(applied_paragraphs):
            ai, atext, atokens = applied_paragraphs[pos_i]
            if ai not in used_applied:
                matched[ji] = (ai, atext, atokens)
                used_applied.add(ai)

    misses_by_paragraph = []
    total_required = 0
    total_present = 0
    for ji, entry, required in indexed_entries:
        choice = matched.get(ji)
        if choice is None:
            # No match found at all — nothing to validate against.
            continue
        applied_idx, applied_text, applied_tokens = choice
        missing = required - applied_tokens
        total_required += len(required)
        total_present += len(required & applied_tokens)
        if missing:
            hints = _diagnose_miss(entry, missing, applied_text)
            miss_record = {
                'idx': entry.get('idx', ji),
                'missing_tokens': sorted(missing),
                'sample_en': (entry.get('en') or '')[:120],
                'sample_applied': applied_text[:120],
            }
            if hints:
                miss_record['hints'] = hints
            misses_by_paragraph.append(miss_record)

    return misses_by_paragraph, total_required, total_present

def _diagnose_miss(entry, missing, applied_text):
    """Return a list of human-readable hints for why this paragraph's
    required tokens are reported missing. Every hint is advisory — the
    translator still checks the actual output.

    Pattern 1: consecutive same-type TC cluster.
    ``extract_paragraphs`` flagged this paragraph as having 2+ adjacent
    <w:ins> / <w:del> wrappers. The defect class is the "PS → P S"
    seam-split. Route to the Scrambled-whole-word-edits fix.

    Pattern 2: ortho-collapse phantom.
    A word like ``particularin`` is flagged missing even though ``in``
    and ``particular`` both appear. This smells like a (del, ins) pair
    with identical English text where _collect_required_tokens was
    still double-counting. This indicates a latent bug if it still
    appears after Lever 2 lands.

    Pattern 3: short upper-case acronym missing.
    Tokens that are all uppercase and short (2-4 chars, e.g. ``USA``,
    ``VAT``) are typically protected by digit/alpha rules but can still
    be lost when the surrounding XML is heavily fragmented.
    """
    hints = []

    # Pattern 1
    if entry.get('tc_cluster_hits'):
        cluster_types = ', '.join(
            sorted({h.get('type') for h in entry['tc_cluster_hits']
                    if isinstance(h, dict) and h.get('type')})
        )
        hints.append(
            f"This paragraph was flagged at extract time as containing "
            f"consecutive same-type TC cluster(s) (type={cluster_types}). "
            f"See `skill-docs/04-translate.md` ('Scrambled / character-fragmented "
            f"whole-word edits', or run "
            f"'python scripts/validate_apply.py <paragraphs.json> "
            f"--report-clusters --apply-zwsp' for belt-and-suspenders "
            f"protection. Note: apply_translations_textmatch.py already "
            f"inserts ZWSP at wrapper boundaries automatically since "
            f"so usually no action is required."
        )

    # Pattern 2
    phantom_like = [
        tok for tok in missing
        if len(tok) >= 8 and any(
            tok.startswith(p) and tok.endswith(s)
            for p in ['in', 'the', 'of', 'to', 'on', 'at', 'by']
            for s in ['in', 'the', 'of', 'to', 'on', 'at', 'by']
        ) and tok != f"{tok[:2]}{tok[2:]}"  # heuristic only
    ]
    if phantom_like:
        hints.append(
            "One or more missing tokens look like concatenations of two "
            "function words (e.g. 'particularin', 'ofthe'). This is the "
            "signature of an ortho-collapse del/ins pair — the del and "
            "ins carry the same English text and strip_noop unwraps one "
            "copy. Since  validate_apply de-duplicates these at "
            "token-collection time; if you see this hint it indicates a "
            "new shape of ortho-collapse that _dedupe_ortho_pairs does "
            "not yet cover."
        )

    # Pattern 3
    short_acronyms = [tok for tok in missing
                      if 2 <= len(tok) <= 4 and tok.isupper()]
    if short_acronyms:
        hints.append(
            f"Short acronym(s) missing: {sorted(short_acronyms)!r}. "
            "Check whether the source wraps each letter in a separate "
            "<w:ins> or <w:r> element — if so, treat it as a TC cluster "
            "(see Pattern 1 hint) or as the 'Scrambled / character-"
            "fragmented whole-word edits' case) in `skill-docs/04-translate.md`."
        )

    return hints

ZWSP = '\u200b'

def _inject_zwsp(en_text):
    """Insert one ZWSP between pairs of adjacent alpha characters in
    short (1-3 char) runs inside a cluster-flagged en string.

    The 1-3 char window is the signature of a real cluster fragment
    (single-letter / 2-letter / short-acronym wrappers). Longer runs
    are real words that already distribute cleanly and should not get
    ZWSPs sprinkled through them.
    """
    if not en_text:
        return en_text
    out = []
    for i, ch in enumerate(en_text):
        if (i > 0 and ch.isalpha()
                and en_text[i - 1].isalpha()
                and i < 4):
            out.append(ZWSP)
        out.append(ch)
    return ''.join(out)

def report_and_fix_clusters(paragraphs_json_path, apply_zwsp=False):
    """Inspect paragraphs.json for cluster-flagged paragraphs.

    Default (apply_zwsp=False): print a report naming each flagged
    paragraph, the cluster type+count, and the source/en text of the
    affected segments. Used for diagnostic pre-apply sanity.

    apply_zwsp=True: rewrite paragraphs.json in place, injecting a ZWSP
    between short alpha-alpha runs inside each cluster-flagged en
    string. Belt-and-suspenders layer behind the apply-time auto-ZWSP
    that ``apply_translations_textmatch.py`` performs.

    Returns (report_lines, changes_made).
    """
    with open(paragraphs_json_path, 'r', encoding='utf-8') as f:
        entries = json.load(f)

    flagged = [e for e in entries if e.get('tc_cluster_hits')]
    report = [
        f'paragraphs.json: {len(entries)} paragraphs, '
        f'{len(flagged)} flagged with consecutive-same-type TC clusters.'
    ]
    if not flagged:
        report.append('  No action required. (Cluster-merge ZWSP protection '
                      'in apply_translations_textmatch.py also runs '
                      'automatically.)')
        return report, 0

    changes = 0
    for entry in flagged:
        idx = entry.get('idx')
        hits = entry.get('tc_cluster_hits') or []
        cluster_types = {
            h.get('type') for h in hits if isinstance(h, dict)
        }
        summary = ', '.join(
            f"{h.get('count')}× <w:{h.get('type')}>"
            for h in hits if isinstance(h, dict)
        )
        report.append(f'  idx={idx}: {summary}')
        segs = entry.get('en_segments') or entry.get('tc_segments') or []
        for i, seg in enumerate(segs):
            if not isinstance(seg, dict):
                continue
            if seg.get('type') not in cluster_types:
                continue
            src_text = (seg.get('text') or '').strip()
            en_text = (seg.get('en') or '').strip()
            report.append(
                f'      seg[{i}] type={seg["type"]}: '
                f'src={src_text[:60]!r} en={en_text[:60]!r}'
            )
            if apply_zwsp and en_text:
                new_en = _inject_zwsp(seg['en'])
                if new_en != seg['en']:
                    seg['en'] = new_en
                    changes += 1

    if apply_zwsp and changes:
        with open(paragraphs_json_path, 'w', encoding='utf-8') as f:
            json.dump(entries, f, ensure_ascii=False, indent=1)
        report.append(f'Rewrote {paragraphs_json_path}: '
                      f'{changes} segment(s) updated with ZWSP protection.')

    return report, changes

def main():
    ap = argparse.ArgumentParser(
        description='Validate that translated tokens from paragraphs.json '
                    'landed in the final document.xml. Also supports a '
                    '--report-clusters mode that inspects paragraphs.json '
                    'for consecutive-same-type TC cluster flags, without '
                    'reading the final document.xml.'
    )
    ap.add_argument('paragraphs_json', help='Path to paragraphs.json with filled en/en_segments fields')
    ap.add_argument('document_xml', nargs='?', default=None,
                    help='Path to the translated document.xml (not needed in --report-clusters mode)')
    ap.add_argument('--strict', action='store_true',
                    help='Return non-zero exit code if any token is missing')
    ap.add_argument('--max-report', type=int, default=25,
                    help='Maximum number of affected paragraphs to report (default 25)')
    ap.add_argument('--report-clusters', action='store_true',
                    help='Inspect paragraphs.json for tc_cluster_hits flags '
                         'and print a summary. No document.xml required.')
    ap.add_argument('--apply-zwsp', action='store_true',
                    help='With --report-clusters, rewrite paragraphs.json '
                         'in place, injecting ZWSPs between short alpha-'
                         'alpha runs inside cluster-flagged en strings. '
                         'Belt-and-suspenders behind the apply-time auto-ZWSP.')
    ap.add_argument('--post-spacing-fix', action='store_true',
                    help='rev42: caller asserts post_process.fix_spacing '
                         'has already run on document_xml. validate_apply '
                         'simulates fix_spacing\'s element-boundary '
                         'space-insertion on the declared en_segments '
                         'side so tokenisation is symmetric. Without this '
                         'flag, declared tokens are joined as-is '
                         '(preserves the apply-time-gate behaviour where '
                         'fix_spacing has NOT yet touched the document).')
    args = ap.parse_args()

    if not os.path.exists(args.paragraphs_json):
        print(f'validate_apply: file not found: {args.paragraphs_json}',
              file=sys.stderr)
        return 2

    if args.report_clusters:
        try:
            report_lines, _ = report_and_fix_clusters(
                args.paragraphs_json, apply_zwsp=args.apply_zwsp)
        except Exception as e:
            print(f'validate_apply: {e}', file=sys.stderr)
            return 2
        for line in report_lines:
            print(line)
        return 0

    if not args.document_xml:
        print('validate_apply: document_xml is required unless '
              '--report-clusters is passed', file=sys.stderr)
        return 2
    if not os.path.exists(args.document_xml):
        print(f'validate_apply: file not found: {args.document_xml}',
              file=sys.stderr)
        return 2

    try:
        misses, total_req, total_present = validate(
            args.paragraphs_json, args.document_xml,
            post_spacing_fix=args.post_spacing_fix)
    except Exception as exc:
        # refactored to use a helper at byte-shifted position.
        _emit_error(f'validate_apply: {exc}')
        return 2

    print(f'Validate apply: required tokens = {total_req}, present = {total_present}, '
          f'missing in output = {total_req - total_present}')
    if misses:
        print(f'Paragraphs with missing tokens: {len(misses)}')
        for m in misses[:args.max_report]:
            print(f'  idx={m["idx"]}: missing={m["missing_tokens"][:10]}')
            print(f'    declared en:   {m["sample_en"]!r}')
            print(f'    applied text:  {m["sample_applied"]!r}')
            for hint in m.get('hints') or []:
                lines = str(hint).strip().splitlines() or ['']
                print(f'    HINT: {lines[0]}')
                for cont in lines[1:]:
                    print(f'          {cont}')
        if len(misses) > args.max_report:
            print(f'  ... {len(misses) - args.max_report} more (suppressed)')
        if args.strict:
            return 1
    else:
        print('  PASSED: all declared tokens found in output.')
    return 0

if __name__ == '__main__':
    _check_self_integrity()
    sys.exit(main())

# === SKILL FILE COMPLETE ===
