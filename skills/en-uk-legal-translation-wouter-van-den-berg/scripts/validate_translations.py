"""Validate translation completeness before applying to the document.

Checks character ratios between source and target for every paragraph.
Flags paragraphs where the English translation is suspiciously short
relative to the source — a strong indicator of truncated translation.

Also enforces the per-batch translation cap. The skill's Step 4
mandates ≤35 paragraphs per batch with this script run between
batches; bulk translation of more than 35 paragraphs in one go has
been the recurring "operator deviates from skill when task feels
laborious" failure mode. The state file ``<workdir>/.validate-state.json``
tracks which paragraphs have already been validated; on each
invocation, only paragraphs newly translated since the last
validation are checked against the per-batch cap. To override (e.g.,
bulk re-validation after a regex fix that touches all paragraphs),
pass ``--accept-large-batch``.

Usage:
    python validate_translations.py <paragraphs.json> [--accept-large-batch]

Exit codes:
    0 — PASS (all ratios acceptable)
    1 — WARN (some paragraphs flagged but none critical)
    2 — BLOCK (critically short translations OR per-batch cap exceeded)
"""
import os
import re
import sys
import json
import datetime

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

# Thresholds
WARN_RATIO = 0.6       # EN/IT ratio below this triggers a warning
BLOCK_RATIO = 0.3      # EN/IT ratio below this blocks application
MIN_IT_LENGTH = 150    # Only check paragraphs with IT text longer than this
BATCH_CAP = 35         # Hard cap on newly-translated paragraphs per call

# Rev41: quoted-phrase retention thresholds.
# Single quotes (' ' / ' '): typically wrap project names, brand names,
# place designations that are preserved verbatim in legal translation.
# Threshold 2+ words catches "Wind Farm Foo", "Compañía Acme S.A.", etc.
# Double quotes (" " / " " / « »): typically wrap defined terms (1–4 words,
# legitimately replaced by the English equivalent during translation) OR
# statute / treaty / long entity names (5+ words, usually preserved verbatim
# or kept parenthetically). Threshold 5+ words keeps short defined-term
# substitutions out of the warning stream.
QUOTE_SINGLE_MIN_WORDS = 2
QUOTE_DOUBLE_MIN_WORDS = 5

# Quote-pair definitions used by the retention check. Each entry is
# (opener, closer). For ASCII single/double quotes opener == closer; the
# regex uses non-greedy matching scoped by character-class exclusion to
# pick out the shortest enclosed text.
_QUOTE_PAIRS_SINGLE = [
    ("'", "'"),                # ASCII apostrophe (U+0027)
    ('‘', '’'),      # ' ' typographic single
]
_QUOTE_PAIRS_DOUBLE = [
    ('"', '"'),                # ASCII double (U+0022)
    ('“', '”'),      # " " typographic double
    ('«', '»'),      # « » guillemets
]


def _extract_quoted_phrases(text, opener, closer):
    """Yield content of every <opener>…<closer> pair in text. Uses a
    non-greedy character-class-excluded inner pattern so back-to-back
    quotations match independently. ASCII apostrophes inside English
    contractions (don't, Paul's) match only when surrounded by another
    apostrophe — the word-count filter at the call site rejects those."""
    # Escape for regex; if opener == closer this is fine, the pattern
    # `<opener>([^<closer>]+)<closer>` matches the shortest enclosed text.
    pat = re.escape(opener) + r'([^' + re.escape(closer) + r']+)' + re.escape(closer)
    for m in re.finditer(pat, text):
        yield m.group(1)


def _check_quoted_phrase_retention(p):
    """Return list of (style, phrase) for source-quoted phrases that do
    NOT appear in the English translation.

    Rationale: in legal translation, quoted multi-word phrases are
    nearly always preserved verbatim — project names, brand names,
    place designations, statute names, treaty names. A quoted phrase
    in the source `text` that has no matching substring in `en` is a
    HIGH-suspicion missing-content defect (typical case: a quoted
    project name silently dropped from the English).

    Style-aware thresholds (see QUOTE_SINGLE_MIN_WORDS /
    QUOTE_DOUBLE_MIN_WORDS rationale above). Returns:
      [('single', phrase), ('double', phrase), ...]

    Skips paragraphs that are themselves a definition body — detected
    by the `… : significa / means / shall mean / has the meaning…`
    predicate immediately following the quoted term — to avoid warning
    on legitimate defined-term substitutions like
    `"Acuerdo" significa el contrato dated…` → `"Agreement" means the
    agreement dated…` where the source quoted term gets replaced.
    """
    text = (p.get('text') or '').strip()
    en = (p.get('en') or '').strip()
    if not text or not en:
        return []

    # Skip: paragraph is a textbook definition body. Heuristic — text
    # begins with a quoted term (any style) immediately followed by a
    # definitional predicate within the next ~8 chars.
    def_predicates = (
        'significa', 'shall mean', 'means', 'has the meaning',
        'indica', 'signifies', 'indicates', 'tiene el significado',
        'le sens',  # French
        'bedeutet',  # German
        'oznacza',  # Polish
    )
    head = text[:100].lower()
    if any(pred in head for pred in def_predicates):
        # Likely a definition entry — substitution is expected.
        # Run the check anyway for the *trailing* phrases (which may
        # be project/place names inside a definition) but skip the
        # leading quoted defined term.
        # Implementation: extract the leading quoted term and remove
        # it from the candidate set.
        leading_quoted = None
        for opener, closer in _QUOTE_PAIRS_SINGLE + _QUOTE_PAIRS_DOUBLE:
            patt = (re.escape(opener) + r'([^' + re.escape(closer)
                    + r']+)' + re.escape(closer))
            m = re.match(r'\s*' + patt, text)
            if m:
                leading_quoted = m.group(1)
                break
    else:
        leading_quoted = None

    findings = []
    for opener, closer in _QUOTE_PAIRS_SINGLE:
        for phrase in _extract_quoted_phrases(text, opener, closer):
            phrase_stripped = phrase.strip()
            if leading_quoted is not None and phrase_stripped == leading_quoted:
                continue
            if len(phrase_stripped.split()) < QUOTE_SINGLE_MIN_WORDS:
                continue
            if phrase_stripped not in en:
                findings.append(('single', phrase_stripped))
    for opener, closer in _QUOTE_PAIRS_DOUBLE:
        for phrase in _extract_quoted_phrases(text, opener, closer):
            phrase_stripped = phrase.strip()
            if leading_quoted is not None and phrase_stripped == leading_quoted:
                continue
            if len(phrase_stripped.split()) < QUOTE_DOUBLE_MIN_WORDS:
                continue
            if phrase_stripped not in en:
                findings.append(('double', phrase_stripped))
    return findings

def _state_path(json_path):
    """State file lives next to paragraphs.json as
    ``.validate-state.json`` so it sits in the same workdir."""
    return os.path.join(os.path.dirname(os.path.abspath(json_path)),
                        '.validate-state.json')

def _load_state(json_path):
    """Load the per-workdir validation state. Returns the default
    structure if absent."""
    sp = _state_path(json_path)
    if not os.path.isfile(sp):
        return {'validated_indices': [], 'history': []}
    try:
        with open(sp, 'r', encoding='utf-8') as f:
            state = json.load(f)
        # Migrate legacy / partial states.
        state.setdefault('validated_indices', [])
        state.setdefault('history', [])
        return state
    except (OSError, ValueError):
        return {'validated_indices': [], 'history': []}

def _save_state(json_path, state):
    sp = _state_path(json_path)
    with open(sp, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2)

def validate(json_path, accept_large_batch=False):
    with open(json_path, 'r', encoding='utf-8') as f:
        paras = json.load(f)

    # Per-batch cap enforcement. Compare the current set of translated
    # paragraphs against the state file's record of paragraphs already
    # validated. Anything new in this invocation is "this batch".
    state = _load_state(json_path)
    already_validated = set(state.get('validated_indices', []))
    newly_translated = []
    for p in paras:
        if not (p.get('text') or '').strip():
            continue
        if not (p.get('en') or '').strip():
            continue
        idx = p.get('idx')
        if idx is None:
            continue
        if idx not in already_validated:
            newly_translated.append(idx)

    if len(newly_translated) > BATCH_CAP and not accept_large_batch:
        print(
            "\n" + "=" * 60 + "\n"
            f"[validate_translations] SKILL GATE FIRED — INTENTIONAL BLOCK,\n"
            f"NOT A SCRIPT ERROR. The script is working as designed.\n"
            + "=" * 60 + "\n"
            f"[validate_translations] BLOCK — per-batch cap exceeded.\n"
            f"\n"
            f"{len(newly_translated)} paragraphs translated since the\n"
            f"last validation; the skill's hard cap is {BATCH_CAP} per\n"
            f"batch. Translation quality degrades with larger batches\n"
            f"because per-paragraph attention drops — this is exactly\n"
            f"the failure mode the skill is structured around.\n"
            f"\n"
            f"Re-author paragraphs.json so only ≤{BATCH_CAP} paragraphs\n"
            f"have new `en` fields beyond what's already validated, run\n"
            f"validate_translations again, then continue with the next\n"
            f"batch of ≤{BATCH_CAP}.\n"
            f"\n"
            f"To override (only when re-validating after a bulk fix that\n"
            f"touches every paragraph at once), pass --accept-large-batch.\n"
            f"Doing so leaves an audit-trail entry in .validate-state.json.\n"
            + "=" * 60 + "\n",
            file=sys.stderr,
        )
        return 2

    warnings = []
    blocks = []
    missing = []
    quoted_phrase_warnings = []  # rev41: quoted-phrase retention
    total = 0
    translated = 0

    for p in paras:
        it_text = (p.get('text') or '').strip()
        en_text = (p.get('en') or '').strip()

        if not it_text:
            continue

        total += 1

        if not en_text:
            missing.append(p.get('idx', '?'))
            continue

        translated += 1

        if it_text == en_text:
            continue

        # rev41: quoted-phrase retention check. Catches missing-content
        # defects where source quoted phrases (project names, place
        # names, statute names) silently fail to appear in the English.
        # See `_check_quoted_phrase_retention` docstring for thresholds
        # and definition-paragraph skipping.
        qp_missing = _check_quoted_phrase_retention(p)
        if qp_missing:
            quoted_phrase_warnings.append({
                'idx': p.get('idx', '?'),
                'phrases': qp_missing,
                'it_preview': it_text[:120],
                'en_preview': en_text[:120],
            })

        it_len = len(it_text)
        en_len = len(en_text)

        if it_len < MIN_IT_LENGTH:
            continue

        ratio = en_len / it_len

        if ratio < BLOCK_RATIO:
            blocks.append({
                'idx': p.get('idx', '?'),
                'ratio': ratio,
                'it_len': it_len,
                'en_len': en_len,
                'it_preview': it_text[:100],
                'en_preview': en_text[:100],
            })
        elif ratio < WARN_RATIO:
            warnings.append({
                'idx': p.get('idx', '?'),
                'ratio': ratio,
                'it_len': it_len,
                'en_len': en_len,
                'it_preview': it_text[:100],
                'en_preview': en_text[:100],
            })

    # Report
    print(f"\nTranslation Validation: {json_path}")
    print("=" * 60)
    print(f"  Total non-empty paragraphs: {total}")
    print(f"  Translated: {translated}")
    print(f"  Missing translation: {len(missing)}")

    if missing:
        print(f"\n  MISSING (no 'en' field):")
        for idx in missing[:20]:
            print(f"    -> idx {idx}")
        if len(missing) > 20:
            print(f"    ... and {len(missing) - 20} more")

    if blocks:
        print(f"\n  BLOCK — Critically short translations (ratio < {BLOCK_RATIO}):")
        print(f"  These are almost certainly truncated. Re-translate before proceeding.\n")
        for b in blocks:
            print(f"    idx {b['idx']}: ratio={b['ratio']:.2f} "
                  f"(IT={b['it_len']} chars, EN={b['en_len']} chars)")
            print(f"      IT: {b['it_preview']}...")
            print(f"      EN: {b['en_preview']}...")
            print()

    if warnings:
        print(f"\n  WARN — Possibly incomplete translations (ratio < {WARN_RATIO}):")
        print(f"  Review these paragraphs — they may be truncated.\n")
        for w in warnings:
            print(f"    idx {w['idx']}: ratio={w['ratio']:.2f} "
                  f"(IT={w['it_len']} chars, EN={w['en_len']} chars)")
            print(f"      IT: {w['it_preview']}...")
            print(f"      EN: {w['en_preview']}...")
            print()

    if quoted_phrase_warnings:
        print(f"\n  WARN — Quoted source phrases NOT found in en (rev41):")
        print(f"  These are likely project / place / statute names that")
        print(f"  should be preserved verbatim or with a parenthetical")
        print(f"  retention. Review each finding — silent omission of a")
        print(f"  quoted multi-word phrase is a known missing-content")
        print(f"  defect class. (single-quote threshold ≥{QUOTE_SINGLE_MIN_WORDS} words; "
              f"double-quote threshold ≥{QUOTE_DOUBLE_MIN_WORDS} words.)\n")
        for w in quoted_phrase_warnings:
            print(f"    idx {w['idx']}:")
            for style, phrase in w['phrases']:
                quote_label = 'single' if style == 'single' else 'double/guillemet'
                print(f"      missing ({quote_label}): {phrase!r}")
            print(f"      IT: {w['it_preview']}...")
            print(f"      EN: {w['en_preview']}...")
            print()

    # Verdict
    print("=" * 60)
    if blocks:
        print(f"  *** BLOCK: {len(blocks)} critically short translations. "
              f"Do NOT apply until re-translated. ***")
        # Don't update state on a hard block — operator must fix and
        # re-run, and the re-run should re-validate the same indices.
        return 2

    # Persist state: every paragraph in `newly_translated` is now
    # validated. Append a history entry for audit (also lets the
    # ``apply`` step gate later check that no single batch exceeded
    # the cap, even if ``--accept-large-batch`` was used).
    state['validated_indices'] = sorted(
        set(state.get('validated_indices', [])) | set(newly_translated))
    history_entry = {
        'timestamp': datetime.datetime.now(
            datetime.timezone.utc).isoformat(),
        'count': len(newly_translated),
        'indices': newly_translated,
    }
    if accept_large_batch and len(newly_translated) > BATCH_CAP:
        history_entry['accept_large_batch'] = True
    state.setdefault('history', []).append(history_entry)
    _save_state(json_path, state)

    if warnings:
        print(f"  ** WARN: {len(warnings)} possibly incomplete translations. "
              f"Review before applying. **")
        return 1
    elif quoted_phrase_warnings:
        print(f"  ** WARN: {len(quoted_phrase_warnings)} paragraph(s) with "
              f"quoted source phrases not found in en (rev41 retention check). "
              f"Review before applying. **")
        return 1
    elif missing:
        print(f"  ** WARN: {len(missing)} paragraphs without translations. **")
        return 1
    else:
        print(f"  PASS: All {translated} translations have acceptable character ratios.")
        if newly_translated:
            print(f"  Batch state updated: {len(newly_translated)} new indices "
                  f"validated this call ({len(state['validated_indices'])} total).")
        return 0

if __name__ == '__main__':
    _check_self_integrity()
    import argparse
    parser = argparse.ArgumentParser(
        description='Validate translation completeness and enforce per-batch cap.')
    parser.add_argument('paragraphs_json',
                        help='Path to paragraphs.json')
    parser.add_argument('--accept-large-batch', action='store_true',
                        help=('Bypass the per-batch hard cap of 35 paragraphs. '
                              'Use only when re-validating after a bulk fix '
                              'that legitimately touches every paragraph at '
                              'once. Audit trail kept in .validate-state.json.'))
    args = parser.parse_args()
    sys.exit(validate(args.paragraphs_json,
                      accept_large_batch=args.accept_large_batch))

# === SKILL FILE COMPLETE ===
