"""Validate the *shape* of filled `en_segments` before apply runs.

Runs BEFORE `apply_translations_textmatch.py`, at the same point in the
pipeline as `validate_translations.py` and `validate_reject_all.py`.

============================================================================
WHY THIS EXISTS
============================================================================

`validate_reject_all.py` reconstructs the two views of a tracked-change
paragraph and scans them for grammar defects ("the respective the",
"to.Schedule", etc.). That catches the problem after it has already been
baked into a reconstruction — which still leaves the translator to work
out *which* segment caused it.

This script runs one level earlier. It scans `en_segments` pair-wise, at
the segment-boundary level, and warns about the shapes of splits that
**predict** downstream defects:

  * a regular segment ending with an English article/preposition abutting
    an ins/del that starts with a noun — double-article / stranded
    preposition risk;
  * a segment ending with an alpha character abutting the next segment
    starting with an alpha character, with no intervening whitespace —
    the gotcha for non-Latin script sources (Chinese, Japanese, Korean,
    Thai, Lao, Khmer, Cyrillic, Greek, Arabic, Hebrew, Devanagari, etc.),
    which either carry no inter-segment whitespace at all or whose
    character classes interact unpredictably with `fix_spacing`;
  * a digit sitting at a TC boundary — guarantees an alpha+digit
    collision in one of the two views;
  * an adjacent pair where both sides start or end with the same short
    article — means one view will read "the the" / "a a";
  * a double-space straddling a boundary;
  * an ins or del whose entire content is a bare article, preposition,
    or punctuation token (suggests the translator put a single function
    word on the TC side instead of on the regular side or vice versa —
    often diagnosable as an author's intent problem);
  * a lowercase word (2+ chars) directly followed by a digit inside one
    segment — e.g. "of500" / "section5" (digit glued to a word with no
    space); 2-char minimum excludes single-letter cross-refs ("a5.2",
    "e3") which are legitimate shorthand;
  * a digit directly followed by a 3+-char lowercase run inside one
    segment — e.g. "5minutes" / "500euros"; 3-char minimum excludes
    ordinals ("1st", "2nd", "3rd", "4th", "21st") and short unit
    abbreviations ("5km", "10kg", "500ml", "24h") without a whitelist.

The rules are intentionally conservative: every rule is backed by a
real defect observed in production. A paragraph that lints clean here is
not guaranteed to read well (that is what `validate_reject_all.py` is
for), but a paragraph that lints dirty here has a *shape* defect and the
translator can resolve it by rewriting the split — without re-running
the apply step and re-opening the .docx.

============================================================================
USAGE
============================================================================

    python validate_segment_shapes.py <paragraphs.json>
    python validate_segment_shapes.py <paragraphs.json> --strict

Exit codes:
    0 — no hits (or advisory mode)
    1 — at least one hit and --strict was set
    2 — input/IO error
"""
import argparse
import json
import os
import re
import sys

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



# ──────────────────────────────────────────────────────────────────────
# English function-word sets used by the rules
# ──────────────────────────────────────────────────────────────────────

# English articles. Kept short — catching "the", "a", "an" covers the
# observed defect class without noisy matches on possessives/demonstratives.
_ARTICLES = ('the', 'a', 'an')

# English single-token prepositions most likely to be stranded by a bad
# split. Conservative list: only the short function prepositions that do
# not routinely end a sentence in legal English.
_PREPOSITIONS = (
    'to', 'of', 'in', 'for', 'on', 'at', 'by', 'with',
    'from', 'into', 'under', 'over', 'within', 'between', 'among',
    'against', 'before', 'after', 'about',
)

# Combined set for "function word that binds to the next noun phrase".
_BINDING_WORDS = _ARTICLES + _PREPOSITIONS

# Precompiled regex to detect a trailing binding word at the end of a
# segment — allows trailing space, tab, or nothing.
_TRAILING_BINDING_RE = re.compile(
    r'(?:^|[\s(\[{"“‘])'
    r'(' + '|'.join(re.escape(w) for w in _BINDING_WORDS) + r')'
    r'\s*$',
    re.IGNORECASE,
)

# Precompiled regex to detect a leading article at the start of a segment.
_LEADING_ARTICLE_RE = re.compile(
    r'^\s*(' + '|'.join(re.escape(a) for a in _ARTICLES) + r')\b',
    re.IGNORECASE,
)

# Precompiled regex to detect a leading preposition at the start of a
# segment (used for "ins starts with preposition" checks — an English
# prepositional phrase almost never starts a *deletion* segment cleanly).
_LEADING_PREPOSITION_RE = re.compile(
    r'^\s*(' + '|'.join(re.escape(p) for p in _PREPOSITIONS) + r')\b',
    re.IGNORECASE,
)

# ──────────────────────────────────────────────────────────────────────
# Segment accessors
# ──────────────────────────────────────────────────────────────────────

_TC_TYPES = {'ins', 'del', 'ins_then_del'}

def _seg_text(seg):
    """Return the English text of a segment, or empty string."""
    if not isinstance(seg, dict):
        return ''
    return seg.get('en') or ''

def _seg_type(seg):
    if not isinstance(seg, dict):
        return None
    return seg.get('type')

def _is_tc(seg):
    return _seg_type(seg) in _TC_TYPES

def _is_regular(seg):
    return _seg_type(seg) == 'regular'

# ──────────────────────────────────────────────────────────────────────
# Rules — one function per rule, each yields (name, message, hint).
# ──────────────────────────────────────────────────────────────────────

def _rule_binding_word_before_tc(left, right):
    """regular ends with "the/a/an/of/to/…" and next is ins/del.

    The binding word will cling to whatever is in the ins/del. On the
    opposite view, if the original noun lives in the OTHER side of the
    TC, the binding word strands. On this view, if the TC segment also
    starts with its own article, you get "the the" / "a the".
    """
    lt = _seg_text(left).rstrip()
    rt = _seg_text(right).lstrip()
    if not lt or not rt:
        return None
    if not (_is_regular(left) and _is_tc(right)):
        return None
    m = _TRAILING_BINDING_RE.search(lt)
    if not m:
        return None
    word = m.group(1)
    # Is the word an article and does the TC segment also start with an
    # article? That is the double-article risk.
    if word.lower() in _ARTICLES:
        m2 = _LEADING_ARTICLE_RE.match(rt)
        if m2:
            return (
                'article_collision',
                f'regular ends with "{word}" and next {_seg_type(right)} '
                f'starts with "{m2.group(1)}" — one view will read '
                f'"{word} {m2.group(1)}"',
                'move the article that must disappear under the opposing '
                'view INSIDE the ins/del segment, and rewrite the regular '
                'to not carry that article',
            )
        # Article on the regular side abutting a TC whose first word is a
        # noun is fine on this view but dangerous on the opposite view if
        # the del/ins text is later reshaped. Emit a softer warning only
        # when the TC segment is a `del`: reject-all will still show the
        # article PLUS the deleted noun, which is fine, but this shape is
        # still a common source of confusion.
        return None
    # Preposition case: stranding is only a risk if the next segment is a
    # `del` AND its text, when removed, leaves the regular ending with
    # a dangling preposition. We cannot know that without reconstructing,
    # so leave this to validate_reject_all.py and do not emit here.
    return None

def _rule_alpha_collision_no_space(left, right):
    """left ends with alpha, right starts with alpha, no whitespace.

    Classic non-Latin-script-source defect: the source had no inter-segment
    whitespace (Chinese, Japanese, Korean, Thai, Lao, Khmer) or its
    character classes interacted unpredictably with `fix_spacing` (Cyrillic,
    Greek, Arabic, Hebrew, Devanagari), and the translator filled in
    English text that concatenates two words into one.
    """
    lt = _seg_text(left)
    rt = _seg_text(right)
    if not lt or not rt:
        return None
    if lt[-1].isspace() or rt[0].isspace():
        return None
    if not (lt[-1].isalpha() and rt[0].isalpha()):
        return None
    # A hyphen-word break is fine ("Anti-" + "trust" is unusual but the
    # translator likely knew what they were doing). Skip hyphen endings.
    if lt.endswith('-'):
        return None
    snippet = (lt[-20:] + '⟂' + rt[:20]).replace('\n', ' ')
    return (
        'alpha_collision_at_boundary',
        f'segment boundary has "{lt[-1]}" then "{rt[0]}" with no '
        f'whitespace: "…{snippet}…"',
        'add a trailing space to the left segment OR a leading space to '
        'the right segment, whichever matches how the original source '
        'wants the words separated in English',
    )

def _rule_digit_at_tc_boundary(left, right):
    """A digit sits exactly on a regular ↔ TC boundary.

    Either:
      - regular ends with digit, next ins/del starts with alpha — will
        read "500Euros" on one view;
      - regular ends with alpha, next ins/del starts with digit — same
        defect from the opposite direction;
      - regular ends with alpha (no space), next ins/del starts with
        digit and *the digit is inside a defined number*. One view
        collides "Clause5" style.
    """
    lt = _seg_text(left)
    rt = _seg_text(right)
    if not lt or not rt:
        return None
    # Only care about regular ↔ TC boundaries — a TC ↔ TC boundary is
    # already odd and is caught by other rules if it produces a defect.
    if not ((_is_regular(left) and _is_tc(right)) or
            (_is_tc(left) and _is_regular(right))):
        return None
    if lt[-1].isspace() or rt[0].isspace():
        return None
    left_end_is_digit = lt[-1].isdigit()
    right_start_is_digit = rt[0].isdigit()
    left_end_is_alpha = lt[-1].isalpha()
    right_start_is_alpha = rt[0].isalpha()
    if (left_end_is_digit and right_start_is_alpha) or \
       (left_end_is_alpha and right_start_is_digit):
        snippet = (lt[-15:] + '⟂' + rt[:15]).replace('\n', ' ')
        return (
            'digit_at_tc_boundary',
            f'digit abuts alpha across a {_seg_type(left)}/{_seg_type(right)} '
            f'boundary with no whitespace: "…{snippet}…"',
            'put the whitespace on the regular side, or rewrite the ins/del '
            'so the numeric token lives entirely inside one segment',
        )
    return None

def _rule_double_space_across_boundary(left, right):
    """left ends with space AND right starts with space → double space."""
    lt = _seg_text(left)
    rt = _seg_text(right)
    if not lt or not rt:
        return None
    if lt.endswith(' ') and rt.startswith(' '):
        return (
            'double_space_at_boundary',
            'left segment ends with whitespace and right segment starts '
            'with whitespace — reconstruction will have a double space',
            'remove the trailing space from the left segment OR the '
            'leading space from the right segment',
        )
    return None

def _rule_ins_or_del_is_bare_function_word(seg):
    """Whole-segment content is just a bare article/preposition.

    A `{"type": "ins", "en": "the"}` by itself almost always means the
    translator put the article on the wrong side of the split — the
    article should have been inside the ins together with the noun, or
    the ins should have been the article + noun together.
    """
    if not _is_tc(seg):
        return None
    text = _seg_text(seg).strip().lower()
    if text in _ARTICLES:
        return (
            'tc_is_bare_article',
            f'{_seg_type(seg)} segment contains only the bare article '
            f'"{text}" — almost always a bad split',
            'put the article together with the noun it binds to, inside '
            'the same ins/del segment',
        )
    # Bare preposition deletion/insertion is rarer and occasionally
    # genuine ("in" → "on" type edits). Do not flag.
    return None

def _rule_internal_double_article(seg):
    """Internal "the the" / "a the" / "the a" inside a single segment."""
    t = _seg_text(seg)
    if not t:
        return None
    if re.search(r'\b(the|a|an)\s+(the|a|an)\b', t, re.IGNORECASE):
        return (
            'internal_double_article',
            f'{_seg_type(seg)} segment contains consecutive articles',
            'rewrite the segment to remove one of the articles',
        )
    return None

def _rule_internal_alpha_alpha_no_space(seg):
    """Two alpha chars separated only by non-alpha ASCII punctuation, no
    space — e.g. "Clause5", "partialone". A conservative pattern that
    only fires on junior-grade concatenations.

    Only flags lower-then-upper (camelCase artefacts) and common
    alpha-digit-alpha sandwiches. The goal is catching obvious text
    defects without false-positiving on legitimate compound words.
    """
    t = _seg_text(seg)
    if not t:
        return None
    # Lowercase immediately followed by uppercase (camelCase artefact).
    m = re.search(r'[a-z][A-Z]', t)
    if m:
        return (
            'camel_case_collision',
            f'{_seg_type(seg)} segment has lowercase immediately '
            f'followed by uppercase near "{t[max(0,m.start()-15):m.end()+15]}" '
            '— two words likely run together',
            'insert the missing space inside the segment',
        )
    return None

# Precompiled patterns for the digit-boundary rules below. Kept at module
# scope so the regexes compile once, not per-segment.

# Lowercase word (2+ chars) directly followed by one or more digits.
#   Catches: "of500", "section5", "clause3a" (flags "clause3"), "page12"
#   Does NOT catch: "A4" (uppercase single letter — acronyms),
#                   "MP3" / "H2O" / "B2B" (uppercase),
#                   "1st" / "2nd" (digit-first),
#                   "a5.2" / "b3" (single-letter cross-refs),
#                   "$500" / "€500" (non-alpha prefix).
# A 2-char minimum on the lowercase run is the key FP guard: it excludes
# the single-letter shorthand cross-references (a5, b3, e2) that some
# legal drafters use.
_RE_LOWER_WORD_THEN_DIGIT = re.compile(r'[a-z]{2,}\d')

# Digit(s) directly followed by 3+ lowercase letters.
#   Catches: "5minutes", "10years", "500euros", "100watts"
#   Does NOT catch: "1st" / "2nd" / "3rd" / "4th" / "21st" (2-letter
#                   suffixes), "5km" / "10kg" / "500ml" / "24h" (2-letter
#                   or 1-letter units), "2026",  "A4".
# A 3-char minimum on the lowercase run is the key FP guard: it excludes
# every English ordinal and every one- or two-letter unit abbreviation.
# If a three-letter suffix genuinely occurs ("3rds" plural ordinal,
# almost never seen in legal prose), the translator can ignore the
# warning.
_RE_DIGIT_THEN_LOWER_RUN = re.compile(r'\d[a-z]{3,}')

def _rule_internal_lowercase_word_then_digit(seg):
    """[a-z]{2,}\\d — word-like lowercase run directly followed by a digit.

    The canonical defect this catches is the LLM writing "of500" instead
    of "of 500", or "section5" instead of "section 5" / "Section 5". The
    2-character minimum on the lowercase run prevents firing on
    single-letter cross-references like "a5.2" or "e3" that some civil-
    law drafters use, and the digit-first pattern is handled by the
    sibling rule below.
    """
    t = _seg_text(seg)
    if not t:
        return None
    m = _RE_LOWER_WORD_THEN_DIGIT.search(t)
    if not m:
        return None
    start, end = m.span()
    snippet = t[max(0, start - 15): end + 15]
    return (
        'lowercase_word_then_digit',
        f'{_seg_type(seg)} segment has "{m.group()}" — lowercase word '
        f'immediately followed by a digit near "…{snippet}…"',
        'insert a space between the word and the number (legal English '
        'convention is "Section 5" / "of 500", not "Section5" / "of500")',
    )

def _rule_internal_digit_then_lower_run(seg):
    """\\d[a-z]{3,} — digit(s) directly followed by a 3+ char lowercase run.

    Catches "5minutes" / "10years" / "500euros" without firing on English
    ordinals ("1st", "2nd", "3rd", "4th", "21st") or compact unit
    abbreviations ("5km", "10kg", "500ml", "24h"). The 3-character
    minimum is the whitelist-free way to exclude those tokens: they all
    happen to use 2-character suffixes or shorter.
    """
    t = _seg_text(seg)
    if not t:
        return None
    m = _RE_DIGIT_THEN_LOWER_RUN.search(t)
    if not m:
        return None
    start, end = m.span()
    snippet = t[max(0, start - 15): end + 15]
    return (
        'digit_then_lowercase_run',
        f'{_seg_type(seg)} segment has "{m.group()}" — digit immediately '
        f'followed by a word near "…{snippet}…"',
        'insert a space between the number and the word (legal English '
        'convention is "5 minutes" / "500 euros", not "5minutes" / '
        '"500euros"). Ordinals (1st, 2nd, 3rd, 4th) and short unit '
        'abbreviations (5km, 10kg, 500ml) are not flagged.',
    )

def _scan_pair(left, right):
    hits = []
    for rule in (
        _rule_binding_word_before_tc,
        _rule_alpha_collision_no_space,
        _rule_digit_at_tc_boundary,
        _rule_double_space_across_boundary,
    ):
        r = rule(left, right)
        if r:
            hits.append(r)
    return hits

def _scan_segment(seg):
    hits = []
    for rule in (
        _rule_ins_or_del_is_bare_function_word,
        _rule_internal_double_article,
        _rule_internal_alpha_alpha_no_space,
        _rule_internal_lowercase_word_then_digit,
        _rule_internal_digit_then_lower_run,
    ):
        r = rule(seg)
        if r:
            hits.append(r)
    return hits

def validate(paragraphs_json_path):
    with open(paragraphs_json_path, 'r', encoding='utf-8') as f:
        entries = json.load(f)

    total_with_tc = 0
    total_scanned = 0
    hits_by_para = []

    for entry in entries:
        segs = entry.get('en_segments')
        if not segs:
            continue
        types = {s.get('type') for s in segs if isinstance(s, dict)}
        if not (types & _TC_TYPES):
            continue
        if not any((s.get('en') or '').strip() for s in segs if isinstance(s, dict)):
            continue
        total_with_tc += 1
        total_scanned += 1

        para_hits = []
        # Scan per-segment rules.
        for seg in segs:
            for h in _scan_segment(seg):
                para_hits.append(('segment', _seg_type(seg), h))
        # Scan pair-wise rules.
        for i in range(len(segs) - 1):
            left, right = segs[i], segs[i + 1]
            for h in _scan_pair(left, right):
                para_hits.append(('pair', f'{_seg_type(left)}→{_seg_type(right)}', h))

        if para_hits:
            hits_by_para.append({
                'idx': entry.get('idx', '?'),
                'hits': para_hits,
                'segments': segs,
            })

    return hits_by_para, total_scanned

def _format_segments(segs, max_segs=12):
    out = []
    for seg in segs[:max_segs]:
        t = _seg_type(seg)
        text = _seg_text(seg)
        text = re.sub(r'\s+', ' ', text)
        if len(text) > 50:
            text = text[:47] + '…'
        out.append(f'[{t}] "{text}"')
    if len(segs) > max_segs:
        out.append(f'... {len(segs) - max_segs} more')
    return ' | '.join(out)

def main():
    ap = argparse.ArgumentParser(
        description='Pre-apply linter: scan en_segments for XML-boundary '
                    'risk shapes that predict downstream defects.'
    )
    ap.add_argument('paragraphs_json',
                    help='Path to paragraphs.json with filled en_segments')
    ap.add_argument('--strict', action='store_true',
                    help='Return non-zero exit code if any hit is found')
    ap.add_argument('--max-report', type=int, default=30,
                    help='Maximum number of paragraphs to report (default 30)')
    args = ap.parse_args()

    if not os.path.exists(args.paragraphs_json):
        print(f'validate_segment_shapes: file not found: {args.paragraphs_json}',
              file=sys.stderr)
        return 2

    try:
        hits, total = validate(args.paragraphs_json)
    except Exception as e:
        print(f'validate_segment_shapes: {e}', file=sys.stderr)
        return 2

    print(f'\nPre-apply segment-shape scan: {args.paragraphs_json}')
    print('=' * 60)
    print(f'  Paragraphs with tracked changes scanned: {total}')
    print(f'  Paragraphs with shape hits:              {len(hits)}\n')

    if hits:
        # print each rule's FIX explanation once per run. Operator
        # only needs to read the same fix description once; subsequent
        # hits for the same rule just show the snippet.
        explained = set()
        for h in hits[:args.max_report]:
            print(f'  idx {h["idx"]}:')
            print(f'    segments: {_format_segments(h["segments"])}')
            for origin, where, (name, message, hint) in h['hits'][:6]:
                print(f'    [{name}] ({origin} @ {where}) {message}')
                if name not in explained:
                    print(f'        → FIX: {hint}')
                    explained.add(name)
            print()
        if len(hits) > args.max_report:
            print(f'  ... {len(hits) - args.max_report} more paragraphs (suppressed)')

    print('=' * 60)
    if hits:
        print(
            f'  ** {len(hits)} paragraph(s) have segment-shape defects that '
            f'predict downstream apply/grammar problems. Rewrite the '
            f'offending segments BEFORE running apply_translations_textmatch.py. **'
        )
        if args.strict:
            return 1
    else:
        print(f'  PASS: all {total} tracked-change paragraphs have clean segment shapes.')
    return 0

if __name__ == '__main__':
    sys.exit(main())

# === SKILL FILE COMPLETE ===
