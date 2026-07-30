"""Validate the reject-all (and accept-all) reconstructions of tracked-change
paragraphs.

Runs BEFORE `apply_translations_textmatch.py` on the filled `paragraphs.json`
(same point in the pipeline as `validate_translations.py`).

============================================================================
WHY THIS EXISTS
============================================================================

The skill's invariant for segment-aware tracked-change translation is:

    If the deleted text were reinstated (reject-all view), the sentence
    should still read well — no double articles, no repeated words, no
    run-together words, no dangling prepositions.

Earlier gates do not enforce this mechanically:

* `validate_translations.py` only checks character-length ratios.
* `validate_apply.py` checks token presence — text must appear somewhere
  in the applied output, but grammar is not checked.
* `quality_check.py` has categories for spacing and terminology in the
  applied document, but none of them reconstruct the reject-all view from
  `en_segments` and scan that reconstruction for readability defects.

The defect this script is designed to catch looks like this:

    en_segments:
      regular: " to "
      del:     "the respective "
      regular: "the addressees, and"

    Accept-all (ins kept, del removed):  " to the addressees, and"       ✓
    Reject-all (del kept, ins removed):  " to the respective the addressees, and"  ✗
                                                         ^^^^^^^^^^^^
                                                         double article

The root cause is that an English article ("the") that binds to the noun
lives in the *regular* span adjacent to the del, so reinstating the del
produces two articles in a row. The same class of defect appears when two
defined-term phrases abut because a deleted phrase and a regular phrase
meet with no intervening punctuation.

The rule: articles, prepositions, and any word whose grammaticality depends
on whether the neighbouring tracked-change is accepted or rejected must live
*inside* the del or ins, not in the regular span adjacent to it.

============================================================================
USAGE
============================================================================

    python validate_reject_all.py <paragraphs.json>
    python validate_reject_all.py <paragraphs.json> --strict
    python validate_reject_all.py <paragraphs.json> --extra-collocation "A/C Memorandum"

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
# Deterministic readability rules
# ──────────────────────────────────────────────────────────────────────
# Each rule is (name, compiled_pattern, description).
#
# Keep the set conservative. Patterns must not false-positive on well-formed
# English legal prose. The skill's invariant is that the two views should
# both read well; anything that reads well in one view cannot match these.

_RULES = [
    (
        'double_article',
        re.compile(r'\b(?:the|a|an)\s+(?:the|a|an)\b', re.IGNORECASE),
        'Two consecutive articles (e.g. "the respective the addressees"). '
        'An article probably lives on the wrong side of a del/ins boundary.',
    ),
    (
        'repeated_word',
        re.compile(r'\b(\w{3,})\s+\1\b', re.IGNORECASE),
        'The same word appears twice in a row. Either an accidental '
        'duplicate inside a segment or a word that sits on both sides of '
        'a del/ins boundary.',
    ),
    (
        'stranded_preposition',
        re.compile(r'\b(?:to|of|in|for|on|at|by|with|from|into|under|over|within|between|among)\s*[.,;:)]'),
        'Preposition followed immediately by punctuation. Usually means a '
        'noun was removed from one view but its preposition was left behind '
        'in the adjacent regular segment.',
    ),
    (
        'missing_space_between_words',
        re.compile(r'\S[.,;:)](?=[A-Za-z])'),
        'Punctuation immediately followed by a letter with no space. '
        'Usually two defined-term phrases colliding because a deleted '
        'phrase abuts a regular phrase without whitespace.',
    ),
    (
        'double_space',
        re.compile(r'[^\S\n]{2,}'),
        'Two or more consecutive spaces. Usually a leading or trailing '
        'space ended up in both a regular segment and the adjacent del/ins.',
    ),
    (
        'empty_parens',
        re.compile(r'\(\s*\)'),
        'Empty parentheses. A parenthetical was wholly deleted under one '
        'view but the brackets survived as regular segments.',
    ),
    (
        'empty_quotes',
        re.compile(r'"\s*"'),
        'Empty quotation marks. A quoted phrase was wholly deleted.',
    ),
    (
        'double_comma',
        re.compile(r',\s*,'),
        'Two consecutive commas. Usually means a parenthetical clause was '
        'removed in one view but a flanking comma survived in the regular '
        'segment on each side.',
    ),
]

# Collocations that are always wrong in either view, regardless of
# structural cause. Extend with --extra-collocation for document-specific
# red flags.
# Lookup table: rule name → short FIX description. Built once at module
# load. previously the _desc third tuple element was discarded by
# _scan_view, so the operator only saw `[double_article] "..."` with no
# explanation of what to do. Now every hit prints with its FIX line.
_RULE_FIX = {name: desc for name, _pat, desc in _RULES}

# Generic FIX hint for forbidden-collocation hits (no per-collocation
# description, all share the same root cause + fix).
_FORBIDDEN_FIX = (
    'A forbidden collocation appears in the reconstructed view. Almost '
    'always means an article/preposition/whitespace character is on the '
    'wrong side of a del/ins boundary. Move it INTO the del/ins that '
    'contains the noun it binds to, then re-run.'
)

_DEFAULT_FORBIDDEN_COLLOCATIONS = [
    'the respective the',
    'a respective the',
    'respective the respective',
    'and and',
    'of of',
    'to to',
    '. .',
    ',,',
]

def _reconstruct(en_segments, mode):
    """Concatenate en_segments into an accept-all or reject-all reconstruction.

    ``mode`` is 'accept' or 'reject'.

      * accept-all: keep 'regular' + 'ins'; drop 'del' and 'ins_then_del'.
      * reject-all: keep 'regular' + 'del'; drop 'ins' and 'ins_then_del'.

    ``ins_then_del`` (the phantom "inserted then deleted" wrapper) is a
    true no-op in both views, so we drop it from both reconstructions.
    """
    pieces = []
    for seg in en_segments:
        if not isinstance(seg, dict):
            continue
        stype = seg.get('type')
        text = seg.get('en') or ''
        if not text:
            continue
        if mode == 'accept':
            if stype in ('regular', 'ins'):
                pieces.append(text)
        elif mode == 'reject':
            if stype in ('regular', 'del'):
                pieces.append(text)
    return ''.join(pieces)

def _scan_view(text, extra_collocations):
    """Return a list of (rule_name, snippet) hits."""
    hits = []
    for name, pattern, _desc in _RULES:
        for m in pattern.finditer(text):
            start, end = m.span()
            snippet = text[max(0, start - 25): end + 25]
            hits.append((name, snippet.strip()))
    lower = text.lower()
    for col in _DEFAULT_FORBIDDEN_COLLOCATIONS + list(extra_collocations):
        idx = 0
        needle = col.lower()
        while True:
            j = lower.find(needle, idx)
            if j < 0:
                break
            snippet = text[max(0, j - 25): j + len(needle) + 25]
            hits.append(('forbidden_collocation: ' + col, snippet.strip()))
            idx = j + len(needle)
    return hits

def _diff_views(accept, reject):
    """Return a two-line diff of accept-vs-reject, truncated to 160 chars each."""
    def _trunc(s):
        s = re.sub(r'\s+', ' ', s).strip()
        return s[:160] + ('…' if len(s) > 160 else '')
    return f"      accept: {_trunc(accept)}\n      reject: {_trunc(reject)}"

def validate(paragraphs_json_path, extra_collocations):
    with open(paragraphs_json_path, 'r', encoding='utf-8') as f:
        entries = json.load(f)

    hits_by_para = []
    total_checked = 0

    for entry in entries:
        segs = entry.get('en_segments')
        if not segs:
            continue
        # Only check paragraphs that actually have a del or ins segment —
        # a paragraph of only regular segments has no tracked change and
        # therefore no accept-vs-reject divergence to validate.
        types = {s.get('type') for s in segs if isinstance(s, dict)}
        if not (types & {'ins', 'del', 'ins_then_del'}):
            continue
        # Skip paragraphs whose segments are not filled in yet.
        if not any((s.get('en') or '').strip() for s in segs if isinstance(s, dict)):
            continue
        total_checked += 1

        accept = _reconstruct(segs, 'accept')
        reject = _reconstruct(segs, 'reject')

        accept_hits = _scan_view(accept, extra_collocations)
        reject_hits = _scan_view(reject, extra_collocations)

        if accept_hits or reject_hits:
            hits_by_para.append({
                'idx': entry.get('idx', '?'),
                'accept': accept,
                'reject': reject,
                'accept_hits': accept_hits,
                'reject_hits': reject_hits,
            })

    return hits_by_para, total_checked

def main():
    ap = argparse.ArgumentParser(
        description='Reconstruct accept-all and reject-all views from '
                    'en_segments and scan both for readability defects.'
    )
    ap.add_argument('paragraphs_json',
                    help='Path to paragraphs.json with filled en_segments')
    ap.add_argument('--strict', action='store_true',
                    help='Return non-zero exit code if any hit is found')
    ap.add_argument('--extra-collocation', action='append', default=[],
                    help='Additional forbidden collocation (may be passed '
                         'multiple times). Case-insensitive substring match.')
    ap.add_argument('--max-report', type=int, default=25,
                    help='Maximum number of paragraphs to report (default 25)')
    args = ap.parse_args()

    if not os.path.exists(args.paragraphs_json):
        print(f'validate_reject_all: file not found: {args.paragraphs_json}', file=sys.stderr)
        return 2

    try:
        hits, total = validate(args.paragraphs_json, args.extra_collocation)
    except Exception as e:
        print(f'validate_reject_all: {e}', file=sys.stderr)
        return 2

    print(f'\nReject-all / accept-all readability scan: {args.paragraphs_json}')
    print('=' * 60)
    print(f'  Paragraphs with tracked changes checked: {total}')
    print(f'  Paragraphs with readability hits:        {len(hits)}\n')

    if hits:
        # Track which rule names have already been explained in this run
        # to avoid repeating the FIX line for the same rule on every
        # paragraph (operator only needs the FIX explanation once).
        explained = set()
        for h in hits[:args.max_report]:
            print(f'  idx {h["idx"]}:')
            if h['accept_hits']:
                print(f'    accept-all hits:')
                for name, snippet in h['accept_hits'][:5]:
                    print(f'      [{name}] …{snippet}…')
                    fix = _RULE_FIX.get(name) or (
                        _FORBIDDEN_FIX if name.startswith('forbidden_collocation')
                        else None)
                    if fix and name not in explained:
                        print(f'        → FIX: {fix}')
                        explained.add(name)
            if h['reject_hits']:
                print(f'    reject-all hits:')
                for name, snippet in h['reject_hits'][:5]:
                    print(f'      [{name}] …{snippet}…')
                    fix = _RULE_FIX.get(name) or (
                        _FORBIDDEN_FIX if name.startswith('forbidden_collocation')
                        else None)
                    if fix and name not in explained:
                        print(f'        → FIX: {fix}')
                        explained.add(name)
            print(_diff_views(h['accept'], h['reject']))
            print()
        if len(hits) > args.max_report:
            print(f'  ... {len(hits) - args.max_report} more paragraphs (suppressed)')

    print('=' * 60)
    if hits:
        print(
            f'  ** {len(hits)} paragraph(s) have readability defects in the '
            f'accept-all or reject-all view. Rewrite the segments so that '
            f'articles/prepositions live inside the del or ins, not in the '
            f'regular span adjacent to it. **'
        )
        if args.strict:
            return 1
    else:
        print(f'  PASS: all {total} tracked-change paragraphs read cleanly in '
              f'both views.')
    return 0

if __name__ == '__main__':
    sys.exit(main())

# === SKILL FILE COMPLETE ===
