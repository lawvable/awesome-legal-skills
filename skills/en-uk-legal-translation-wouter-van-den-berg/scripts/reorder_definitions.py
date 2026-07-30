"""
Reorder definitions alphabetically by the English defined term.

This script finds the definitions section in a .docx document.xml,
groups multi-paragraph definitions together, sorts them alphabetically,
and reorders the XML elements accordingly.

Detection heuristics (tried in order):
  1. Bold-term definitions: paragraph starts with a bold run followed
     by ":" — the most common pattern in Italian law firm drafting.
  2. Quote-mark definitions: paragraph starts with a quote character
     followed by the defined term.

Section boundaries:
  - Start: paragraph flagged with role 'definitions_intro' in
    paragraphs.json , OR a paragraph whose English text matches
    one of the case-insensitive intro triggers (legacy fallback).
  - End: next major heading (all-caps paragraph, or a paragraph whose
    style is Heading 1 / Heading 2).

Run with --dry-run --expected-defs N first to confirm the script sees
the right number of definitions before mutating the XML. If the
extracted count or any extracted term looks suspicious, the script
aborts loudly rather than silently producing a corrupted document.
"""
import sys
import re
import json
import argparse
from lxml import etree
import os

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

# ECMA-376 ST_OnOff lexical space: true | false | 1 | 0 | on | off
# (case-insensitive). Element absent → caller's default. Element present
# with no @w:val → True. Anything not in the falsy set → True.
#  only excluded the literal string 'false' here, which
# misread `<w:b w:val="0"/>` (LibreOffice's explicit-off) as bold-on.
# That silently corrupted the definitions reorder on .odt-converted
# inputs. is_on() fixes the bug class for every ST_OnOff attribute.
ST_ONOFF_FALSE = {'false', '0', 'off'}

def is_on(elem, default=False):
    """Read an OOXML ST_OnOff attribute. Element absent → ``default``.
    Element present with no @w:val → True. @w:val ∈ {false,0,off}
    (case-insensitive) → False. Anything else → True."""
    if elem is None:
        return default
    val = elem.get(f'{{{W}}}val')
    if val is None:
        return True
    return val.strip().lower() not in ST_ONOFF_FALSE

def extract_header(xml_text):
    """Extract XML declaration and root element opening tag from raw XML text.
    This captures the original double-quote declaration and all namespace
    declarations exactly as the source file had them."""
    m = re.match(r'(<\?xml[^?]*\?>\s*<w:document[^>]*>)', xml_text, re.DOTALL)
    return m.group(1) if m else None

def get_texts(p):
    """Get all w:t text content from a paragraph."""
    return [t.text or '' for t in p.iter(f'{{{W}}}t')]

def get_full_text(p):
    """Get concatenated text of a paragraph."""
    return ''.join(get_texts(p))

def is_heading(p):
    """Check if a paragraph uses a Heading style (including custom ones)."""
    ppr = p.find(f'{{{W}}}pPr')
    if ppr is None:
        return False
    pstyle = ppr.find(f'{{{W}}}pStyle')
    if pstyle is None:
        return False
    val = pstyle.get(f'{{{W}}}val', '').lower()
    # Standard heading styles
    if val.startswith('heading'):
        return True
    # Custom heading styles used by Italian law firms (Legance, BonelliErede, etc.)
    # FWBL1/FWBL2 = clause headings; Legance Title = section titles
    heading_patterns = ('fwbl', 'legance title', 'titulo', 'titolo',
                        'clausola', 'articolo')
    for pat in heading_patterns:
        if val.startswith(pat):
            return True
    # Also check outline level — a paragraph with outlineLvl is a heading
    outline = ppr.find(f'{{{W}}}outlineLvl')
    if outline is not None:
        return True
    return False

# Rev45 Fix A: stop-list of bold prefixes that look like definitions
# structurally (bold word(s) followed by ":") but are NOT real defined
# terms. Letter subject lines ("Subject:"), recital openers ("WHEREAS:"
# / "PREMESSO:"), notice-block labels ("Address:", "Attention:"),
# operative-clause openers ("NOW, THEREFORE:") all trip the primary
# detector and either spoil the cluster guard (account-pledge post-
# mortem: two cover-letter Subject: lines pushed the first three
# candidates 61 paragraphs apart, just over the K*3=60 cap) or hijack
# the section start (quota-pledge post-mortem: WHEREAS: at P[28] sat
# 34 paragraphs before the real definitions cluster at P[62+] and the
# cluster-extension loop broke at the first gap, sorting only WHEREAS
# as a single fake definition). The stop-list rejects them at
# get_bold_term, so they never enter def_starts_idx.
#
# Conservative: only words extremely unlikely to be defined terms in
# legal English. Step 7 runs AFTER translation, so the post-translation
# English form is what we match. Source-language equivalents are
# included as belt-and-suspenders in case Step 8b leaves boilerplate
# untranslated.
_NON_DEFINITION_BOLD_PREFIXES_EXACT = frozenset({
    # English letter headers
    'subject', 're', 'from', 'to', 'date', 'sent', 'cc', 'bcc',
    # English recital + operative openers
    'whereas', 'now therefore', 'now, therefore',
    'witnesseth', 'in witness whereof',
    # English notice-block labels
    'attention', 'attn', 'address', 'fax', 'tel', 'telephone', 'phone',
    'email', 'e-mail', 'pec',
    # Italian (may survive translation in edge cases)
    'oggetto', 'premesso', 'considerato', 'visto',
    'tanto premesso', 'tutto ciò premesso', 'ora pertanto',
    'indirizzo', "all'attenzione", 'all’attenzione',
    # Spanish / Portuguese
    'asunto', 'assunto', 'considerando', 'considerandos', 'visto que',
    # French
    'objet', 'attendu', 'attendu que', 'considérant',
    # German
    'betreff', 'erwägung', 'in erwägung',
    # Dutch
    'onderwerp', 'overwegende', 'aangezien',
    # Polish
    'temat', 'zważywszy', 'mając na uwadze',
    # Hungarian
    'tárgy', 'mivel', 'tekintettel arra',
    # Finnish
    'aihe', 'ottaen huomioon', 'koska',
})

_NON_DEFINITION_BOLD_PREFIX_STARTS = (
    # Notice-block addressee lines: "If to the Borrower:",
    # "If to the Agent:", "If to the Lender:" etc.
    'if to ',
    'with copy to ',
    # Italian addressee patterns
    'se a ',
    'in caso di ',
)

def _is_non_definition_bold_prefix(term):
    """Return True if ``term`` looks like a non-definition bold heading
    (letter subject line, recital opener, notice-block label, addressee
    label). Rev45 Fix A — surgically rejects the bold-then-colon false
    positives identified in the rev45 account-pledge / quota-pledge
    post-mortems.

    Conservative scope: only words and phrase-starts that are vanishingly
    unlikely to be real defined terms in legal English. Normalisation:

      * Trailing punctuation stripped (``Subject:``, ``Subject,``,
        ``Subject.`` all compare as ``subject``).
      * When the captured bold prefix extends past the colon (a
        fully-bolded cover-letter line such as
        ``Subject: Account Pledge Agreement - Acceptance``), we
        match against the substring BEFORE the first colon — so the
        bold continuing past the colon does not defeat the stop-list.
    """
    if not term:
        return False
    # Bold may extend through a colon when the whole line is bolded
    # (cover-letter subject lines, fully-bolded recital headers).
    # Take the head before the first colon, if any.
    head = term.split(':', 1)[0].strip().rstrip(',. ').lower()
    if not head:
        return False
    if head in _NON_DEFINITION_BOLD_PREFIXES_EXACT:
        return True
    for start in _NON_DEFINITION_BOLD_PREFIX_STARTS:
        if head.startswith(start):
            return True
    return False

def get_bold_term(p):
    """If paragraph starts with a bold run followed by ':', return the
    bold text (the defined term). Otherwise return None."""
    runs = list(p.iter(f'{{{W}}}r'))
    if not runs:
        return None

    # Collect text from consecutive bold runs at the start
    bold_parts = []
    for r in runs:
        rpr = r.find(f'{{{W}}}rPr')
        is_bold = False
        if rpr is not None:
            b = rpr.find(f'{{{W}}}b')
            bi = rpr.find(f'{{{W}}}bCs')
            # Use is_on() helper — recognises 'false', '0', 'off'
            # (case-insensitive) as off. The previous strict
            # `!= 'false'` test misread <w:b w:val="0"/> as on.
            #
            # <w:b> takes precedence over <w:bCs>. Per
            # ECMA-376 §17.3.2.2/3, <w:bCs> only applies to complex-
            # script characters (Arabic, Hebrew, Devanagari); for
            # Latin / CJK text <w:b> is authoritative. the
            # OR combination read a run as bold-on whenever a bare
            # <w:bCs/> (which defaults to ON per ST_OnOff) sat
            # alongside an explicit <w:b w:val="0"/> — a real-world failure mode
            # flagged in a post-mortem. Use
            # is_on(b) when <w:b> is present; fall back to
            # is_on(bCs) only when <w:b> is absent.
            if b is not None:
                is_bold = is_on(b, default=False)
            else:
                is_bold = is_on(bi, default=False)
        t = r.find(f'{{{W}}}t')
        text = (t.text or '') if t is not None else ''

        if is_bold and text.strip():
            bold_parts.append(text.strip())
        elif text.strip() == ':' or text.strip().startswith(':'):
            # The colon run — we're done collecting bold parts
            break
        elif not is_bold and bold_parts:
            # Non-bold run after bold runs — check if it starts with ':'
            if text.strip().startswith(':'):
                break
            # Otherwise this isn't a definition pattern
            return None
        else:
            # First run isn't bold — not a definition
            return None

    if bold_parts:
        term = ' '.join(bold_parts).rstrip(':').strip()
        # Verify there's a colon somewhere after the bold text
        full = get_full_text(p)
        if ':' in full:
            # Rev45 Fix A: reject bold-then-colon paragraphs that are
            # structurally definition-shaped but semantically letter
            # subject lines, recital openers, notice-block labels, or
            # addressee labels. The stop-list is conservative — only
            # words extremely unlikely to be real defined terms.
            if _is_non_definition_bold_prefix(term):
                return None
            return term
    return None

_QUOTE_OPEN_CHARS = {'"', '\u201c', '\u2018', '\u00ab'}

# Map open-quote -> plausible close-quote characters. Tolerates
# mismatched pairing (smart open with straight close after a
# copy-paste round-trip).
_QUOTE_CLOSE_OPTIONS = {
    '"':       {'"', '\u201d'},
    '\u201c':  {'\u201d', '"'},
    '\u2018':  {'\u2019', "'"},
    '\u00ab':  {'\u00bb'},
}

def extract_quoted_term(text):
    """Extract the term between an opening quote at the start of ``text``
    and the matching close quote within the first 80 characters.
    Returns the term (stripped) or None if no quote-bound term is found.

    Tolerates mismatched quote pairing (smart open with straight close,
    etc. — uses _QUOTE_CLOSE_OPTIONS). Used by both
    ``looks_like_definition_start`` (to detect quote-bound definitions)
    and by ``group_definitions`` (to extract the term from the
    paragraph's full text without depending on per-run text splits).
    """
    if not text:
        return None
    s = text.lstrip()
    if not s:
        return None
    open_ch = s[0]
    if open_ch not in _QUOTE_OPEN_CHARS:
        return None
    close_options = _QUOTE_CLOSE_OPTIONS.get(
        open_ch, {'"', '\u201d', '\u2019', '\u00bb'})
    earliest = -1
    for close in close_options:
        idx = s.find(close, 1, 80)
        if idx > 0 and (earliest < 0 or idx < earliest):
            earliest = idx
    if earliest < 1:
        return None
    term = s[1:earliest].strip()
    if not term or len(term) > 80:
        return None
    return term

def looks_like_definition_start(p):
    """Return True if paragraph ``p`` looks like the start of a defined
    term. Two structural patterns recognised:

    1. Bold-run-then-colon (handled by ``get_bold_term``).
    2. Quote-bound term followed by body text -- paragraph starts with
       a quote character (\", smart-open, single-smart-open,
       guillemet), has a matching close quote within the first 80
       characters, and has substantive body text (>=5 chars) after
       the close quote.

    pattern 2 no longer requires a colon to be present. Italian
    (and other) legal docs commonly write definitions as
    ``\u201cTerm\u201d ha il significato di X.`` or
    ``\u201cTerm\u201d indica X.`` with no colon -- these were missed
    by because the old detector required ``:`` within the
    first 200 characters. The cluster requirement (>=2 paragraphs
    within window 20) still protects against false positives on
    isolated paragraphs that happen to contain a quoted phrase.

    Language-agnostic: works on any source text because we check
    structure (quote pairs + body), not vocabulary (no
    ``ha il significato`` / ``indica`` / ``means`` matching).
    """
    if get_bold_term(p) is not None:
        return True
    full = get_full_text(p)
    if not full:
        return False
    s = full.lstrip()
    if not s:
        return False
    open_ch = s[0]
    if open_ch not in _QUOTE_OPEN_CHARS:
        return False
    close_options = _QUOTE_CLOSE_OPTIONS.get(
        open_ch, {'"', '\u201d', '\u2019', '\u00bb'})
    # Find the earliest matching close quote within first 80 chars.
    earliest = -1
    for close in close_options:
        idx = s.find(close, 1, 80)
        if idx > 0 and (earliest < 0 or idx < earliest):
            earliest = idx
    if earliest < 1:
        return False
    # Term must be non-empty and reasonably short.
    term = s[1:earliest].strip()
    if not term or len(term) > 80:
        return False
    # After the close quote, substantive body text. Definitions have a
    # body ("indica X.", ":", "ha il significato..."). Bare
    # quoted-phrase paragraphs typically have no body or just a short
    # connective.
    rest = s[earliest + 1:].strip()
    if len(rest) < 5:
        return False
    return True

_FALLBACK_HEADING_RE = re.compile(
    r'^\s*'
    # Optional prefix: "Article 1", "Clause 1", "Section 1",
    # "1", "1.", "1 –" (en-dash), "1 —" (em-dash), "1:"
    r'(?:'
    r'(?:Article|Clause|Section|Art\.|Cl\.|Sec\.)\s*'
    r'\d+\s*[\.\:–—\-]?\s*'
    r'|'
    r'\d+\s*[\.\:–—\-]?\s+'
    r')?'
    # The definitional heading word(s)
    r'(Definitions(?:\s+and\s+Interpretation)?'
    r'|Defined\s+Terms'
    r'|Interpretation)'
    r'\s*\.?\s*$',
    re.IGNORECASE,
)

_FALLBACK_PREDICATE_RE = re.compile(
    # Term (capitalised, no terminal punctuation in the term itself).
    # Note: NO ``re.IGNORECASE`` flag at the top — the term-must-start-
    # with-uppercase check would otherwise be meaningless. The predicate
    # itself uses an inline-case-insensitive group so ``means`` / ``Means``
    # both match.
    r'^\s*[“”"«»‘’\']?\s*'
    r'[A-Z][\w\-/&’\']*'
    r'(?:\s+[A-Z\d][\w\-/&’\']*)*'
    # Optional closing quote and optional space
    r'\s*[”"»]?\s*'
    # Separator: explicit (colon / hyphen / en-dash / em-dash) OR just
    # whitespace. Real definitions appear in both forms — "Schedules:
    # means all..." (Italian-tradition colon) and "Business Day means
    # a day..." (English-tradition no separator).
    r'(?:\s*[:–—\-]\s*|\s+)'
    # Predicate (case-insensitive subgroup so we don't enumerate
    # capitalisation variants of every verb)
    r'(?i:means|shall\s+mean|has\s+the\s+meaning'
    r'|indicates|signifies|refers\s+to)\b',
)

def _find_definition_bounds_by_heading(all_p):
    """Rev21 fallback: locate a definitions section by its heading and
    a predicate-cluster anchor.

    Used only when the primary detector (bold-term-then-colon or quoted-
    term cluster in :func:`find_definition_bounds`) returns ``None,
    None`` — typically because the operator did not supply ``en_runs``
    on the definition paragraphs and ``apply_translations_textmatch``'s
    default-off override stripped the style-provided bold from the
    defined terms (Doc 1  post-mortem; cascade root cause).

    Two anchors required (both, not either) to keep false-positive
    risk near zero:
      1. A heading paragraph whose entire text matches a recognised
         definitions-section heading: ``Definitions``, ``Defined
         Terms``, ``Definitions and Interpretation``, ``Interpretation``
         — optionally prefixed by ``Article N`` / ``Clause N`` /
         ``Section N`` / ``N.`` / ``N``.
      2. ≥3 of the 8 paragraphs immediately after the heading match
         the predicate shape ``Term : means / shall mean / has the
         meaning / indicates / signifies / refers to`` (with optional
         quote characters around the term, separator may be ``:``,
         ``-``, en-dash, or em-dash).

    Returns (def_start, def_end) on success, (None, None) otherwise.
    Window of 8 paragraphs after the heading is generous enough for an
    intro paragraph + ≥3 definition starts but tight enough that we
    don't conflate the definitions section with whatever follows it.
    Bold is not consulted — that's the whole point of the fallback.
    """
    for i, p in enumerate(all_p):
        text = get_full_text(p).strip()
        if not text or len(text) > 80:
            # Definition headings are short labels.
            continue
        if not _FALLBACK_HEADING_RE.match(text):
            continue
        # Heading found at index i. Look ahead at the next 8 paragraphs.
        window_end = min(i + 1 + 8, len(all_p))
        predicate_hits = []
        for j in range(i + 1, window_end):
            jtext = get_full_text(all_p[j]).strip()
            if jtext and _FALLBACK_PREDICATE_RE.match(jtext):
                predicate_hits.append(j)
        if len(predicate_hits) < 3:
            continue  # Not a definitions section per the predicate anchor.
        # Loud canary: when this fallback fires, the primary bold-anchor
        # detector found nothing — which usually means the operator did
        # not supply ``en_runs`` on definition paragraphs and apply has
        # stripped the style-provided bold. Print prominently so the
        # operator notices, even if the script still proceeds with the
        # sort.
        print(
            "\n" + "=" * 60 + "\n"
            "[reorder_definitions] WARNING — heading+predicate fallback used.\n"
            "The primary bold-anchor / quote-anchor detector did not\n"
            "produce a clean definitions cluster. Two common causes:\n"
            "  1. Operator did not supply en_runs on definition paragraphs\n"
            "     and apply stripped the style-provided bold. Bold/italic\n"
            "     on defined terms will be missing in the output.\n"
            "     Re-author paragraphs.json with en_runs per Step 4 rule 3\n"
            "     and re-run from Step 5 BEFORE shipping.\n"
            "  2. The document contains bold-then-colon paragraphs that\n"
            "     are not definitions (letter Subject lines, recital\n"
            "     openers, addressee labels) and Rev45 Fix A's stop-list\n"
            "     did not catch them. Inspect the dry-run output and\n"
            "     consider whether the stop-list needs extending.\n"
            "The sort below is a recovery action; review the output\n"
            "before shipping.\n"
            + "=" * 60 + "\n",
            file=sys.stderr,
        )
        # def_start is the first predicate paragraph; def_end walks
        # forward past predicate-shape and continuation paragraphs to
        # the next non-definition heading or end of document.
        def_start = predicate_hits[0]
        last_def = predicate_hits[-1]
        K = 20  # Same continuation window as the primary detector.
        # Extend last_def while subsequent paragraphs continue the
        # cluster (predicate match within K, or intervening blank /
        # continuation prose with no heading style).
        for k in range(last_def + 1, len(all_p)):
            ktext = get_full_text(all_p[k]).strip()
            if not ktext:
                continue
            if _FALLBACK_PREDICATE_RE.match(ktext):
                if k - last_def <= K:
                    last_def = k
                else:
                    break
                continue
            # Non-predicate paragraph: stop if it's a heading, otherwise
            # treat as continuation (e.g., a definition's sub-paragraph).
            if is_heading(all_p[k]):
                break
            if (ktext == ktext.upper() and len(ktext) > 5
                    and not any(c.isdigit() for c in ktext[:3])):
                # All-caps heading fallback (matches the primary
                # detector's terminal-heading rule).
                break
            if k - last_def > K:
                break
        def_end = last_def + 1
        return def_start, def_end
    return None, None

def find_definitions_section_in_texts(texts):
    """Text-only definitions-section detector for use by callers that
    don't have lxml ``<w:p>`` elements (e.g. the pre-apply gate in
    ``apply_translations_textmatch.py`` which only has the ``en``
    strings from ``paragraphs.json``).

    Same heading + predicate-cluster logic as
    :func:`_find_definition_bounds_by_heading` — both anchors required:

      1. A short heading paragraph (≤80 chars) whose entire text matches
         a recognised definitions heading: ``Definitions``, ``Defined
         Terms``, ``Definitions and Interpretation``, ``Interpretation``,
         optionally prefixed by ``Article N`` / ``Clause N`` / ``Section
         N`` / ``N.`` / ``N``.
      2. ≥3 of the 8 paragraphs immediately after match the predicate
         shape (``Term : means / shall mean / has the meaning / indicates
         / signifies / refers to``).

    Returns (start, end) for the predicate cluster, or (None, None).
    The terminal-heading detection is text-only — uses the all-caps
    short-paragraph heuristic from the primary detector — since lxml
    style metadata is not available on plain strings.
    """
    if not texts:
        return None, None
    n = len(texts)
    for i, raw in enumerate(texts):
        text = (raw or '').strip()
        if not text or len(text) > 80:
            continue
        if not _FALLBACK_HEADING_RE.match(text):
            continue
        window_end = min(i + 1 + 8, n)
        predicate_hits = []
        for j in range(i + 1, window_end):
            jtext = (texts[j] or '').strip()
            if jtext and _FALLBACK_PREDICATE_RE.match(jtext):
                predicate_hits.append(j)
        if len(predicate_hits) < 3:
            continue
        last_def = predicate_hits[-1]
        K = 20
        for k in range(last_def + 1, n):
            ktext = (texts[k] or '').strip()
            if not ktext:
                continue
            if _FALLBACK_PREDICATE_RE.match(ktext):
                if k - last_def <= K:
                    last_def = k
                else:
                    break
                continue
            # All-caps heading fallback: terminates the section.
            if (ktext == ktext.upper() and len(ktext) > 5
                    and not any(c.isdigit() for c in ktext[:3])):
                break
            if k - last_def > K:
                break
        return predicate_hits[0], last_def + 1
    return None, None

def find_definition_bounds(all_p):
    """Find the start and end indices of the definitions section by
    structural pattern matching — no language-specific phrase list.

    A definitions section is detected when ≥3 paragraphs in the
    document match the "definition start" shape (bold-term-then-colon,
    or quote-mark-wrapped term-then-colon) within a reasonably tight
    cluster. The first such paragraph is ``def_start``; ``def_end`` is
    the next non-definition heading after the cluster (or end of doc).

    previously matched English intro phrases case-insensitively
    (and previously-previously, case-sensitively). Both approaches
    forced the translator to use a specific English wording for the
    intro paragraph, and missed source-language-only documents at extract
    time. The structural approach works for every supported source
    language — Chinese, Dutch, Finnish, French, German, Hungarian,
    Italian, Japanese, Polish, Portuguese, Spanish — without
    hardcoding any phrase.

    when the primary detector returns no section (commonly
    because the operator did not supply ``en_runs`` and
    ``apply_translations_textmatch.py`` stripped the style-provided
    bold from defined terms — cascade root cause from the Doc 1
    post-mortem), a heading-anchored fallback runs. It requires both a
    section heading paragraph (``Definitions`` / ``Defined Terms`` /
    ``Definitions and Interpretation`` / ``Interpretation``, optionally
    prefixed by ``Article N`` etc.) AND ≥3 predicate-shape paragraphs
    (``Term : means / has the meaning / indicates / signifies``) within
    8 paragraphs after the heading, so false-positive risk on Recitals
    or Interpretation Rules sections stays near zero. See
    :func:`_find_definition_bounds_by_heading`."""
    def_starts_idx = [
        i for i, p in enumerate(all_p)
        if looks_like_definition_start(p)
    ]

    if len(def_starts_idx) < 2:
        # < 2 candidates: not a definitions section by the primary
        # bold-anchor / quote-anchor detector. Try the heading-
        # anchored fallback before giving up — it does not consult bold
        # at all and so survives the Doc 1 cascade where missing
        # en_runs led to apply stripping the style-provided bold.
        return _find_definition_bounds_by_heading(all_p)

    K = 20

    # Rev45 Fix C: drop leading isolated false-positive candidates.
    # If def_starts_idx[0] is more than K paragraphs away from
    # def_starts_idx[1] AND the tail def_starts_idx[1:] forms a tight
    # cluster (first three within K * 3, or first two within K), drop
    # the head and retry. Recovery path for the quota-pledge post-
    # mortem failure where a recital opener (WHEREAS:) sat 34
    # paragraphs before the real definitions cluster; the cluster-
    # extension loop locked onto the recital opener as a single fake
    # definition. Bounded by max_trims to avoid pathological inputs
    # walking the whole candidate list.
    max_trims = 5
    while max_trims > 0 and len(def_starts_idx) >= 2:
        if def_starts_idx[1] - def_starts_idx[0] <= K:
            break
        tail = def_starts_idx[1:]
        if len(tail) >= 3 and tail[2] - tail[0] <= K * 3:
            def_starts_idx = tail
            max_trims -= 1
            continue
        if len(tail) == 2 and tail[1] - tail[0] <= K:
            def_starts_idx = tail
            max_trims -= 1
            continue
        break

    if len(def_starts_idx) < 2:
        return _find_definition_bounds_by_heading(all_p)

    # Cluster check: the first three definition-shaped paragraphs must
    # appear within a reasonably tight window. K=20 covers definitions
    # that span multiple continuation paragraphs (e.g. a definition
    # with sub-bullets like "Current Account" with 3 sub-paragraphs).
    #
    # Rev45 Fix B: when the cluster guard fails, fall through to the
    # heading-anchored fallback instead of returning (None, None). The
    # fallback's two-anchor requirement (Definitions heading + ≥3
    # predicate-shape paragraphs within 8 paragraphs after) keeps
    # false-positive risk near zero. Recovery path for the account-
    # pledge post-mortem failure where two cover-letter Subject: lines
    # spread the first three candidates across 61 paragraphs (one over
    # the K * 3 = 60 cap) and locked out the fallback path.
    if len(def_starts_idx) >= 3:
        if def_starts_idx[2] - def_starts_idx[0] > K * 3:
            return _find_definition_bounds_by_heading(all_p)
    elif def_starts_idx[1] - def_starts_idx[0] > K:
        # With only 2 candidates, require they be close together.
        return _find_definition_bounds_by_heading(all_p)

    def_start = def_starts_idx[0]

    # Find the last definition-shaped paragraph in the cluster: walk
    # def_starts_idx and break when the gap to the next becomes > K.
    last_def_in_cluster = def_start
    for idx in def_starts_idx[1:]:
        if idx - last_def_in_cluster <= K:
            last_def_in_cluster = idx
        else:
            break

    # Find def_end: walk forward from the last definition in the
    # cluster looking for a non-definition heading.
    def_end = None
    for i in range(last_def_in_cluster + 1, len(all_p)):
        p = all_p[i]
        stripped = get_full_text(p).strip()
        if not stripped:
            continue
        # A heading paragraph that is NOT a definition ends the section
        if is_heading(p) and not looks_like_definition_start(p):
            def_end = i
            break
        # All-caps heading fallback (for unstyled docs)
        if (stripped == stripped.upper() and
            len(stripped) > 5 and
            not stripped.startswith(tuple(_QUOTE_OPEN_CHARS)) and
            not any(c.isdigit() for c in stripped[:3]) and
            ':' not in stripped[:30] and
            not looks_like_definition_start(p)):
            def_end = i
            break

    if def_end is None:
        # Cluster runs to end of document (no terminal heading).
        def_end = last_def_in_cluster + 1
        # Walk forward to include any continuation paragraphs (sub-bullets
        # of the last definition) until we hit a heading or the doc ends.
        for i in range(last_def_in_cluster + 1, len(all_p)):
            p = all_p[i]
            if is_heading(p) and not looks_like_definition_start(p):
                def_end = i
                break
            def_end = i + 1

    return def_start, def_end

# Rev11 A2: sanity-check extracted terms before sorting. Catches the
# bug class where bold detection misfires and pieces of body text
# (quote marks, "means", colons) get extracted as defined terms. The
# script runs in Step 7 — AFTER apply — so body text is always English
# at this point. No source-language markers needed.
_SUSPICIOUS_TOKENS = (
    '"', '\u201c', '\u201d', '\u00ab', '\u00bb',
    ' means', ' shall mean', ' has the meaning',
    ' is defined as',
)

def looks_like_real_term(term):
    """Return True if ``term`` looks like a plausible defined term.
    Reject any term that contains quotes, the word 'means', or ends
    with a colon — these are signs that bold-run detection has
    misfired and pulled in body text."""
    if not term:
        return False
    s = term.strip()
    if not s:
        return False
    if len(s) > 60:
        return False
    if any(m in s for m in _SUSPICIOUS_TOKENS):
        return False
    if s.endswith(':'):
        return False
    return True

def group_definitions(all_p, def_start, def_end):
    """Group paragraphs into definitions using both bold-term and
    quote-mark heuristics."""
    definitions = []
    current_group = []
    current_term = None

    quote_chars = {'"', '\u201c', '\u2018', '\u00ab'}

    for i in range(def_start, def_end):
        p = all_p[i]
        texts = get_texts(p)
        full_text = ''.join(texts).strip()

        if not full_text:
            # Empty paragraph — include in current group
            if current_group:
                current_group.append(p)
            continue

        # Try bold-term detection first
        bold_term = get_bold_term(p)
        starts_new = bold_term is not None

        # Fall back to quote-mark detection
        if not starts_new:
            first_text = texts[0].strip() if texts else ''
            if first_text in quote_chars or (full_text and
                                              full_text[0] in quote_chars):
                starts_new = True

        if starts_new:
            # Save previous group
            if current_group and current_term:
                definitions.append((current_term, current_group))

            # Start new group
            current_group = [p]

            # Extract the defined term
            if bold_term:
                current_term = bold_term
            else:
                # Quote-mark extraction. use the full text (not
                # per-run texts[1]) because OOXML may split a defined
                # term across multiple runs (e.g. "Banca Finanziatrice"
                # → runs ['\u201c', 'Banc', 'a', ' Finanziatric', 'e',
                # '\u201d ...']). Picking texts[1] would yield 'Banc'.
                # extract_quoted_term() finds the matching close quote
                # in the concatenated text and slices between them.
                extracted = extract_quoted_term(full_text)
                if extracted:
                    current_term = extracted
                elif full_text:
                    current_term = full_text[:50]
                else:
                    current_term = f"_unknown_{i}"
        else:
            # Continuation paragraph
            current_group.append(p)

    # Save last group
    if current_group and current_term:
        definitions.append((current_term, current_group))

    # Rev11 A2: sanity-check every extracted term. If any term looks
    # like body text rather than a real defined term, refuse to
    # proceed — the document gets shipped unchanged rather than
    # silently corrupted.
    suspicious = [(t, p) for (t, p) in definitions
                  if not looks_like_real_term(t)]
    if suspicious:
        msg = [
            "reorder_definitions: extracted term(s) do not look like real",
            "defined terms — bold-run detection probably misfired",
            "(common cause: w:b/@w:val=\"0\" emitted by LibreOffice).",
            "Refusing to reorder; document unchanged.",
            "Suspicious terms:",
        ]
        for t, paras in suspicious:
            msg.append(f"  '{t}' (~{len(paras)} paras)")
        msg.append(
            "Re-run with --dry-run to inspect, or leave definitions in"
        )
        msg.append("source order and accept the warnings.")
        raise SystemExit('\n'.join(msg))

    return definitions

def reorder(xml_path, output_path=None, dry_run=False, expected_defs=None):
    """Main entry point: reorder definitions in the document XML.

    Behaviour:
      - ``dry_run=True`` prints the detection results without modifying
        the XML.
      - ``expected_defs`` aborts if the count of extracted definitions
        does not match the expected number.
      - Definitions-intro detection is purely structural (no language-
        specific phrase list).
      - Before writing back, every paragraph index outside the
        definitions window must be unchanged or the script aborts.
    """
    if output_path is None:
        output_path = xml_path

    # Capture original header BEFORE parsing (preserves double-quote XML
    # declaration and all namespace declarations exactly as Word wrote them).
    with open(xml_path, 'r', encoding='utf-8') as f:
        raw_xml = f.read()
    orig_header = extract_header(raw_xml)

    tree = etree.parse(xml_path)
    root = tree.getroot()
    all_p = list(root.iter(f'{{{W}}}p'))

    def_start, def_end = find_definition_bounds(all_p)

    if def_start is None or def_end is None:
        # No definitions section is expected for many document types
        # (POAs, guarantees, short deeds). Emit to stderr so stdout stays
        # quiet for the common "nothing to do" case; exit code stays 0
        # (caller treats False as "skipped", not as a failure).
        print(
            "reorder_definitions: no definitions section found "
            "(skipping — expected for many document types).",
            file=sys.stderr,
        )
        return False

    print(f"Definitions: P[{def_start}] to P[{def_end - 1}] "
          f"({def_end - def_start} paragraphs)")

    # Snapshot every paragraph's full text BEFORE grouping so we can
    # later assert that paragraphs outside [def_start, def_end) are
    # untouched (A3 invariant check). Text-based comparison rather than
    # `is` because lxml proxy identity is not stable across separate
    # iter() calls.
    paras_before = list(all_p)
    paras_text_before = [get_full_text(p) for p in paras_before]

    definitions = group_definitions(all_p, def_start, def_end)

    if not definitions:
        print("No individual definitions detected. Check the document "
              "structure.")
        return False

    # Compute paragraph-index map for each definition (A6 dry-run output)
    # — i.e. which index in all_p each definition's paragraphs occupy.
    para_id_to_idx = {id(p): i for i, p in enumerate(paras_before)}
    def_para_indices = []
    for term, paras in definitions:
        idxs = [para_id_to_idx.get(id(p), -1) for p in paras]
        def_para_indices.append((term, idxs))

    print(f"Found {len(definitions)} definitions:")
    for (term, paras), (_, idxs) in zip(definitions, def_para_indices):
        idx_str = ','.join(str(x) for x in idxs)
        print(f"  '{term}' ({len(paras)} paras) [{idx_str}]")

    # Rev11 A6: --expected-defs cross-check
    if expected_defs is not None and len(definitions) != expected_defs:
        raise SystemExit(
            f"reorder_definitions: extracted {len(definitions)} definitions, "
            f"--expected-defs={expected_defs}. "
            f"Re-run with --dry-run to inspect, or correct the expected count."
        )

    # Sort alphabetically (case-insensitive)
    definitions.sort(key=lambda x: x[0].lower())

    print(f"\nSorted order:")
    for term, _ in definitions:
        print(f"  {term}")

    # Rev11 A6: in dry-run mode, stop here without mutating the XML.
    if dry_run:
        print("\n--dry-run: no changes written.")
        return True

    # Reorder in the XML.
    # Detect whether definitions live in table rows (each <w:p> inside its
    # own <w:tc>/<w:tr>) or directly under a shared parent (e.g. <w:body>).
    # When inside a table, we must move the entire <w:tr> element — not
    # just the <w:p> — to preserve the table structure.  Moving only the
    # <w:p> leaves behind empty <w:tc> elements, which Word rejects as
    # "unreadable content".
    #
    # NOTE: lxml uses proxy objects whose Python id() is NOT stable across
    # separate .getparent() calls.  We avoid id()-based deduplication and
    # instead navigate the tree structurally using the table's child list.

    first_p = definitions[0][1][0]
    first_parent = first_p.getparent()
    in_table = first_parent.tag == f'{{{W}}}tc'

    if in_table:
        print("  Definitions are inside table rows — reordering <w:tr> elements.")

        # Navigate structurally: <w:p> → <w:tc> → <w:tr> → <w:tbl>
        # Each definition paragraph sits at tbl > tr > tc > p.
        # We walk up from the first paragraph to find the <w:tbl>.
        first_tc = first_parent
        first_tr = first_tc.getparent()     # <w:tr>
        tbl = first_tr.getparent()          # <w:tbl>

        if (first_tr.tag != f'{{{W}}}tr' or
                tbl.tag != f'{{{W}}}tbl'):
            print("WARNING: unexpected table structure. "
                  "Skipping reorder to avoid corruption.")
            return False

        # Build an index: paragraph text → row index in the table.
        # Each definition occupies one row (single-column table), so we
        # match each definition's first paragraph to a table row.
        tbl_children = list(tbl)  # mix of w:tr, w:tblPr, w:tblGrid, etc.
        tr_indices = []  # (row_index_in_tbl, child_element) for w:tr only
        for ci, child in enumerate(tbl_children):
            if child.tag == f'{{{W}}}tr':
                tr_indices.append((ci, child))

        # For each definition, find which table row(s) contain its paragraphs.
        # We match by finding the <w:tr> that is the grandparent of each <w:p>.
        def_rows = []  # [(term, [row_element, ...])]
        for term, paras in definitions:
            rows_for_def = []
            seen_row_positions = set()
            for p in paras:
                # Walk up: p → tc → tr
                tc = p.getparent()
                tr = tc.getparent()
                # Find this tr's position in tbl_children by identity
                # (within the same list traversal, lxml proxies are stable)
                for ci, child in enumerate(tbl_children):
                    if child is tr:
                        if ci not in seen_row_positions:
                            rows_for_def.append(child)
                            seen_row_positions.add(ci)
                        break
            def_rows.append((term, rows_for_def))

        # Find the range of row positions in the table
        all_row_positions = []
        for _, rows in def_rows:
            for row in rows:
                for ci, child in enumerate(tbl_children):
                    if child is row:
                        all_row_positions.append(ci)
                        break

        if not all_row_positions:
            print("WARNING: could not locate definition rows in table.")
            return False

        anchor_idx = min(all_row_positions)

        # Remove all definition rows from the table
        for _, rows in def_rows:
            for row in rows:
                tbl.remove(row)

        # Re-insert in sorted order at the anchor position.
        # After removal, the anchor index shifts — we insert at the
        # current anchor position and increment.
        idx = anchor_idx
        for term, rows in def_rows:
            for row in rows:
                tbl.insert(idx, row)
                idx += 1

    else:
        # Non-table case: definitions are direct children of a shared parent.
        parent = first_parent

        # Collect old definition paragraphs (the order doesn't matter
        # for removal, but for the anchor we MUST use the source-order
        # minimum position — not the position of definitions[0] after
        # the sort. Using the post-sort first definition would leave
        # the anchor pointing at the wrong place when the
        # alphabetically-first def lived later in the source order than
        # other defs, causing reordered defs to land after subsequent
        # paragraphs (e.g. a section heading). Rev11 A3's invariant
        # check now catches this; the fix is to anchor at the earliest
        # source-order def position regardless of sort.
        old_def_paras = []
        for _, paras in definitions:
            old_def_paras.extend(paras)

        if not old_def_paras:
            print("No definition paragraphs to reorder.")
            return False

        parent_children = list(parent)
        anchor_idx = min(parent_children.index(p) for p in old_def_paras)

        # Remove old paragraphs
        for p in old_def_paras:
            try:
                parent.remove(p)
            except ValueError:
                pass

        # Insert in sorted order at the source-order anchor.
        idx = anchor_idx
        for term, paras in definitions:
            for p in paras:
                parent.insert(idx, p)
                idx += 1

    # Rev11 A3: invariant — every paragraph outside the definitions
    # window must be in the same position (and have the same text) as
    # before reordering. If anything outside the window moved, the
    # reorder has gone off-rails — abort rather than write a corrupt
    # document.
    paras_after = list(root.iter(f'{{{W}}}p'))
    paras_text_after = [get_full_text(p) for p in paras_after]
    if len(paras_text_after) != len(paras_text_before):
        raise SystemExit(
            f"reorder_definitions: paragraph count changed "
            f"({len(paras_text_before)} → {len(paras_text_after)}). "
            f"The reorder added or removed paragraphs. Aborting."
        )
    for i in range(len(paras_text_before)):
        if i < def_start or i >= def_end:
            if paras_text_after[i] != paras_text_before[i]:
                raise SystemExit(
                    f"reorder_definitions: paragraph {i} content changed "
                    f"but is outside the definitions window "
                    f"[{def_start}, {def_end}). This indicates the reorder "
                    f"is moving paragraphs it should not. Aborting; document "
                    f"unchanged.\n  before: '{paras_text_before[i][:80]}'\n"
                    f"   after: '{paras_text_after[i][:80]}'"
                )

    # Save — with header grafting to preserve the original XML declaration
    # and namespace declarations. lxml's tree.write() produces its own
    # declaration (single quotes, possibly different standalone value) which
    # Word may reject.
    tree.write(output_path, xml_declaration=True, encoding='UTF-8',
               standalone=True)

    if orig_header:
        with open(output_path, 'r', encoding='utf-8') as f:
            written = f.read()
        written = re.sub(
            r'^<\?xml[^?]*\?>\s*<w:document[^>]*>',
            orig_header,
            written,
            count=1,
            flags=re.DOTALL
        )
        with open(output_path, 'wb') as f:
            f.write(written.encode('utf-8'))

    print(f"\nDefinitions reordered and saved to {output_path}")
    return True

if __name__ == '__main__':
    ap = argparse.ArgumentParser(
        description=(
            "Reorder definitions alphabetically by the English defined term. "
            "Run with --dry-run --expected-defs N first to confirm "
            "detection before mutating the XML."
        )
    )
    # Backwards-compatible positional usage:
    #   reorder_definitions.py document.xml [output.xml]
    ap.add_argument('xml_path', nargs='?',
                    help='Path to document.xml (required unless --doc given)')
    ap.add_argument('positional_output', nargs='?',
                    help='Optional output path (defaults to xml_path)')
    ap.add_argument('--doc',
                    help='Path to document.xml (alternate to positional)')
    ap.add_argument('--output',
                    help='Output path (defaults to --doc / xml_path)')
    ap.add_argument('--dry-run', action='store_true',
                    help='Print detection results and proposed sort order '
                         'without modifying the XML (A6).')
    ap.add_argument('--expected-defs', type=int, default=None,
                    help='Abort if the extracted definition count does not '
                         'match this value (A6).')
    args = ap.parse_args()

    xml_path = args.doc or args.xml_path
    if not xml_path:
        ap.error("provide a document.xml path (positional or --doc)")
    output_path = (args.output or args.positional_output or xml_path)

    reorder(
        xml_path,
        output_path,
        dry_run=args.dry_run,
        expected_defs=args.expected_defs,
    )

# === SKILL FILE COMPLETE ===
