"""Post-processing script for translated legal documents.

Runs all quality fixes in a single pass:
1. Spacing fixes (cross-element gaps)
2. Definition boundary fixes ("Xmeans" -> "X means")
3. Double punctuation fixes (::, .., ,,, ;;)
4. Terminology/lexicon fixes (including standalone "Financing", Italian remnants, word order)
5. UK spelling
6. Annex -> Schedule
7. Article -> Clause for internal cross-references
8. Double-word deduplication (within and across elements)
9. Quote balancing on defined terms
10. Definition line-break removal (w:br in definition paragraphs)
11. Spurious italic removal (italic on substantive body text)
12. Schedule page-break insertion (pageBreakBefore on Schedule/Annex headings)

Usage:
    python post_process.py <document.xml> [--fix] [--report-only]

Without --fix, prints a report of issues found.
With --fix, applies all fixes and saves.
"""
import os
import sys
import re
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

# ============================================================
# TERMINOLOGY REPLACEMENTS  (order matters: longer matches first)
# ============================================================
TERM_REPLACEMENTS = [
    # (pattern, replacement, is_regex)

    # --- Financing / Facility ---
    ('Financing Agreement', 'Facility Agreement', False),
    ('Financing Bank', 'Lender', False),
    ('Description of Financing', 'Description of the Facility', False),
    ('Description of the Financing', 'Description of the Facility', False),

    # --- Banking Transparency -> Transparency of Banking Conditions ---
    ('BANKING TRANSPARENCY', 'TRANSPARENCY OF BANKING CONDITIONS', False),
    ('Banking Transparency', 'Transparency of Banking Conditions', False),
    ('banking transparency', 'transparency of banking conditions', False),

    # --- Structural / cross-ref ---
    ('Domicile Election', 'Service of Process', False),
    ('DOMICILE ELECTION', 'SERVICE OF PROCESS', False),
    ('Election of Domicile', 'Service of Process', False),
    ('ELECTION OF DOMICILE', 'SERVICE OF PROCESS', False),
    ('election of domicile', 'service of process', False),
    ('Partial Invalidity', 'Severability', False),
    ('PARTIAL INVALIDITY', 'SEVERABILITY', False),
    ('which intervenes as', 'acting as', False),
    ('who intervenes as', 'acting as', False),
    ('intervenes as', 'acts as', False),
    ('Business Register', 'Companies Register', False),
    ('Lien Assets', 'Secured Assets', False),

    # --- "that precedes/follows" (singular AND plural) ---
    ('that precedes', 'above', False),
    ('that precede,', 'above,', False),
    ('that precede ', 'above ', False),
    ('that follows', 'below', False),
    ('that follow,', 'below,', False),
    ('that follow ', 'below ', False),

    # --- Publicity -> Perfection (project finance term) ---
    ('REGISTRATION AND PUBLICITY', 'REGISTRATION AND PERFECTION', False),
    ('Registration and Publicity', 'Registration and Perfection', False),
    ('registration and publicity', 'registration and perfection', False),
    ('TRANSCRIPTION AND PUBLICITY', 'REGISTRATION AND PERFECTION', False),
    ('Transcription and Publicity', 'Registration and Perfection', False),
    ('transcription and publicity', 'registration and perfection', False),

    # --- Literal translation patterns ---
    ('by universal or singular title', 'whether by way of universal or individual succession', False),
    # 'stipulated' is calque ONLY in verb-of-contracting context.
    # The  blanket replacement broke legitimate adjective use
    # ("in the proportions stipulated in the Memorandum" = "set out
    # in the Memorandum"). Narrow patterns capture only the calque
    # ("hereby stipulate", "to stipulate", "the parties stipulate")
    # and leave the adjective alone. Preserves correctness on every
    # document that uses "stipulated" in its non-calque sense — which
    # is most of them.
    ('hereby stipulate', 'hereby agree', False),
    ('hereby Stipulate', 'hereby agree', False),
    ('the parties stipulate', 'the parties agree', False),
    ('the Parties stipulate', 'the Parties agree', False),
    ('to stipulate', 'to enter into', False),
    ('to Stipulate', 'to enter into', False),

    # --- Finance / LMA ---
    ('cash line', 'term facility', False),
    ('Cash line', 'Term facility', False),
    ('revolving line', 'revolving facility', False),
    ('Revolving line', 'Revolving facility', False),
    ('credit lines', 'credit facilities', False),
    ('Credit lines', 'Credit facilities', False),
    ('credit line', 'credit facility', False),
    ('Credit line', 'Credit facility', False),

    # --- Title/header fixes ---
    ('DEED OF CONSTITUTION OF PLEDGE', 'DEED OF PLEDGE', False),
    ('Deed of Constitution of Pledge', 'Deed of Pledge', False),
    ('deed of constitution of pledge', 'deed of pledge', False),
    ('deed of constitution of the pledge', 'deed of pledge', False),
    ('Deed of constitution of the Pledge', 'Deed of Pledge', False),
    ('deed of creation of the pledge', 'deed of pledge of quotas', False),
    ('deed of creation of the Pledge', 'Deed of Pledge of Quotas', False),
    ('Deed of Establishment of Special Lien', 'Deed of Special Lien', False),
    ('DEED OF ESTABLISHMENT OF SPECIAL LIEN', 'DEED OF SPECIAL LIEN', False),
    ('Deed of establishment of special lien', 'Deed of Special Lien', False),
    ('Deed of Creation of Mortgage', 'Deed of Mortgage', False),
    ('DEED OF CREATION OF MORTGAGE', 'DEED OF MORTGAGE', False),
    ('deed of creation of mortgage', 'deed of mortgage', False),
    ('Deed of Establishment of Mortgage', 'Deed of Mortgage', False),
    ('DEED OF ESTABLISHMENT OF MORTGAGE', 'DEED OF MORTGAGE', False),

    # --- Italian remnant defined terms ---
    # These are common Italian terms that sometimes survive translation
    ('\u201cParti\u201d', '\u201cParties\u201d', False),
    ('"Parti"', '"Parties"', False),
    ('\u201cParte\u201d', '\u201cParty\u201d', False),
    ('"Parte"', '"Party"', False),
    ('cinquanta per cento', 'fifty per cent', False),
]

# Regex-based replacements (applied after literal ones)
TERM_REGEX_REPLACEMENTS = [
    # Standalone "Financing" -> "Facility" (but NOT "Project Financing")
    (r'(?<!Project )\bFinancing\b(?! Bank)', 'Facility'),

    # Word order: "X existing and future" -> "existing and future X"
    (r'\b(plants?\s+and\s+works?)\s+existing\s+and\s+future\b', r'existing and future \1'),
    (r'\b(assets?)\s+existing\s+and\s+future\b', r'existing and future \1'),
    (r'\b(receivables?)\s+existing\s+and\s+future\b', r'existing and future \1'),
    (r'\b(goods?)\s+existing\s+and\s+future\b', r'existing and future \1'),
    (r'\b(works?)\s+existing\s+and\s+future\b', r'existing and future \1'),
    (r'\b(rights?)\s+existing\s+and\s+future\b', r'existing and future \1'),
    (r'\b(obligations?)\s+existing\s+and\s+future\b', r'existing and future \1'),
    (r'\b(claims?)\s+existing\s+and\s+future\b', r'existing and future \1'),
    (r'\b(credits?)\s+existing\s+and\s+future\b', r'existing and future \1'),
    (r'\b(sums?)\s+existing\s+and\s+future\b', r'existing and future \1'),

    # "ciascuna" -> "each" (common Italian remnant)
    (r'\bciascuna\b', 'each'),
    (r'\bciascuno\b', 'each'),
    (r'\bciascun\b', 'each'),
]

# UK SPELLING
UK_SPELLING = [
    (r'\bauthorize\b', 'authorise'),
    (r'\bauthorized\b', 'authorised'),
    (r'\bAuthorized\b', 'Authorised'),
    (r'\bAUTHORIZATION\b', 'AUTHORISATION'),
    (r'\bAuthorization\b', 'Authorisation'),
    (r'\bauthorization\b', 'authorisation'),
    (r'\brecognize\b', 'recognise'),
    (r'\brecognized\b', 'recognised'),
    (r'\brecognition\b', 'recognition'),  # no change — same in UK
    (r'\borganize\b', 'organise'),
    (r'\borganized\b', 'organised'),
    (r'\borganization\b', 'organisation'),
    (r'\bfavor\b', 'favour'),
    (r'\bfavored\b', 'favoured'),
    (r'\bfavorable\b', 'favourable'),
    (r'\bhonor\b', 'honour'),
    (r'\bhonored\b', 'honoured'),
    (r'\bcenter\b', 'centre'),
    (r'\bdefense\b', 'defence'),
    (r'\boffense\b', 'offence'),
    (r'\bfulfill\b', 'fulfil'),
    (r'\bfulfillment\b', 'fulfilment'),
    (r'\bjudgment\b', 'judgement'),
    (r'\bjudgments\b', 'judgements'),
    (r'\bJudgment\b', 'Judgement'),
    (r'\backnowledgment\b', 'acknowledgement'),
    (r'\backnowledgments\b', 'acknowledgements'),
    (r'\butilize\b', 'utilise'),
    (r'\butilized\b', 'utilised'),
    (r'\butilization\b', 'utilisation'),
    (r'\bcanceled\b', 'cancelled'),
    (r'\bcanceling\b', 'cancelling'),
    (r'\blabor\b', 'labour'),
    (r'\bpractice\b(?=\s+(?:of|the|in|by))', 'practice'),  # noun OK in UK
    (r'\bpractise\b', 'practise'),  # verb form
    (r'\banalyze\b', 'analyse'),
    (r'\banalyzed\b', 'analysed'),
]

# ANNEX -> Schedule (but not in legislation refs)
ANNEX_EXCLUDE = ['Regulation', 'Directive', 'Law', 'Decree', 'Regolamento']

# LEGISLATION KEYWORDS (paragraphs containing these keep "Article")
# replaced the LEGISLATION_KW hardcoded list (which had to
# enumerate "Civil Code", "Royal Decree", "T.U.B.", etc. and missed
# "Code of Civil Procedure", "Resolution of the CICR", etc.) with a
# language-agnostic structural detector. See _is_external_article_ref().
#
# The discriminator is the linguistic shape of what follows "Article N":
#
#   "Article N of <Capitalized Proper Noun>"     → external (keep)
#   "Article N of this/the present/the said X"   → internal (rewrite)
#   "Article N of <internal anchor>"             → internal (rewrite)
#       internal anchors: Schedule, Annex, Section, Paragraph, Clause,
#       Article, Chapter, Exhibit, Appendix, Attachment, Annexure
#   bare "Article N." or "(Article N)"           → internal (rewrite,
#                                                    matches v5 default)
#
# No keyword list; works for any source-language legislation reference
# the LLM rendered into English in the conventional "of <Capitalized
# Act Name>" shape.

# Internal-reference determiners (lowercase). When "Article N" is
# followed by " of <one of these>", it is an internal cross-reference.
_INTERNAL_DETERMINERS = (
    'this ', 'the present ', 'the said ', 'this same ',
    'that precedes ', 'that follows ', 'the foregoing ',
    'the preceding ', 'the following ',
)

# Internal anchor words. When "Article N" is followed by
# " of [the/a] <one of these>", it is an internal cross-reference
# (e.g. "Article 5 of Schedule B" → "Clause 5 of Schedule B").
_INTERNAL_ANCHOR_WORDS = (
    'Schedule', 'Schedules', 'Annex', 'Annexes', 'Annexure', 'Annexures',
    'Attachment', 'Attachments', 'Appendix', 'Appendices', 'Appendixes',
    'Exhibit', 'Exhibits', 'Section', 'Sections', 'Paragraph', 'Paragraphs',
    'Subparagraph', 'Subparagraphs', 'Clause', 'Clauses',
    'Article', 'Articles', 'Chapter', 'Chapters', 'Part', 'Parts',
)

# Internal locator words that follow "Article N" without "of":
# "Article N above", "Article N hereof", "Article N below", etc.
_INTERNAL_LOCATORS = (
    'above', 'below', 'hereof', 'hereto', 'herein',
    'hereinafter', 'hereinabove', 'hereinbelow', 'hereunder',
    'foregoing', 'preceding', 'following', 'said',
)

def _skip_noise_after_article(text):
    """Given text starting right after "Article N", skip past optional
    sub-numbering (".M.K"), parenthetical letters/numbers ("(b)",
    "(i)"), and number-list conjunctions (" and 6", ", 7"). Return the
    position in ``text`` where the next content word starts, or -1 if
    we hit a sentence boundary first."""
    pos = 0
    while pos < len(text):
        ch = text[pos]
        # Whitespace
        if ch.isspace():
            pos += 1
            continue
        # Sub-numbering ".M" / ".M.K"
        if ch == '.' and pos + 1 < len(text) and text[pos + 1].isdigit():
            pos += 1
            while pos < len(text) and (
                    text[pos].isdigit() or text[pos] == '.'):
                pos += 1
            continue
        # Sentence-ending punctuation
        if ch in '.!?;':
            return -1
        # Parenthetical letter / roman / short number ("(a)", "(iii)", "(2)")
        if ch == '(':
            close = text.find(')', pos)
            if 0 < close - pos <= 6:
                pos = close + 1
                continue
        # "and N(-bis)?", "or N", "to N" — conjunction with another
        # number. Also consumes hyphenated alpha suffix on the trailing
        # number ("Articles 2482-bis and 2482-ter").
        m = re.match(
            r'(?:and|or|to)\s+\d+(?:[.:]\d+)*(?:-[A-Za-z]{1,15})*',
            text[pos:])
        if m:
            pos += m.end()
            continue
        # ", N" / ", N.M" — comma-separated number list (also hyphen-
        # suffix-aware).
        m2 = re.match(
            r',\s*\d+(?:[.:]\d+)*(?:-[A-Za-z]{1,15})*',
            text[pos:])
        if m2:
            pos += m2.end()
            continue
        # Anything else — start of the next content word
        return pos
    return -1

def _is_external_article_ref(joined_text, match_end):
    """Decide whether the "Article N" / "Articles N" match ending at
    ``match_end`` in ``joined_text`` is an EXTERNAL legislation /
    regulatory reference (keep as Article) or an INTERNAL
    cross-reference (rewrite to Clause).

    Returns True if external (keep). Default on ambiguity: False
    (rewrite), preserving the v5 default for bare "Article N." with
    no qualifier.

    **Rev16 — pure structural walk.** Instead of enumerating the
    civil-law citation modifiers that can appear between an article
    number and the named act ("et seq.", "ff.", ", first paragraph",
    ", letter X", ", comma N", ", second sub-paragraph", ...), this
    function walks the entire sentence after "Article N" word by word
    and classifies based on the FIRST decisive token:

      * an internal locator ("above", "below", "hereof", ...)
        → internal (rewrite to Clause)
      * an internal anchor word ("Schedule", "Annex", "Section",
        "Paragraph", "Clause", "Chapter", "Part", ...)
        → internal cross-reference (rewrite)
      * a Capitalised Proper Noun preceded by an internal determiner
        ("this", "the said", "the present", ...)
        → internal (e.g. "this Agreement")
      * a Capitalised Proper Noun NOT preceded by an internal
        determiner → EXTERNAL (keep Article)
      * end of sentence reached without any decisive token
        → internal default

    Lowercase noise words (et, seq, of, the, paragraph, first, second,
    letter, comma, etc.) are simply skipped — no need to enumerate
    them. Chained "Article(s) N" references in the same sentence are
    skipped past as continuations of the same citation chain.

    Works for any source language (the rewrite operates on translated
    English, where capitalisation conventions are uniform). Length
    cap of 250 characters on the tail is structural protection
    against runaway scanning.
    """
    tail = joined_text[match_end:match_end + 250]
    # Smart sentence-end truncation: a "." is a sentence end only if
    # followed by whitespace + Uppercase (start of new sentence) or
    # end-of-text. "." inside a number or before a lowercase word
    # (like "et seq. of") is NOT a sentence end.
    end = len(tail)
    i = 0
    while i < len(tail):
        ch = tail[i]
        if ch in '!?\n':
            end = i
            break
        if ch == '.':
            if i + 1 >= len(tail):
                end = i
                break
            nxt = tail[i + 1]
            if nxt.isdigit():
                i += 1
                continue
            # Period followed by space + uppercase = sentence end.
            j = i + 1
            while j < len(tail) and tail[j] == ' ':
                j += 1
            if j < len(tail) and tail[j].isupper():
                end = i
                break
            # Otherwise (period before lowercase) — abbreviation, keep
        i += 1
    tail = tail[:end]

    # Walk word by word.
    word_re = re.compile(r"[A-Za-z][A-Za-z0-9\'\-]*")
    chain_re = re.compile(
        r"\bArticles?\s+\d[\d.:]*(?:-[A-Za-z]{1,15})*")
    pos = 0
    while pos < len(tail):
        # Skip whitespace
        if tail[pos].isspace():
            pos += 1
            continue
        # Skip past chained "Article(s) N" — it's a continuation of
        # the same citation, not a target anchor.
        cm = chain_re.match(tail, pos)
        if cm:
            pos = cm.end()
            continue
        # Try to read a word at pos
        wm = word_re.match(tail, pos)
        if not wm:
            # Not a word — punctuation, digit, parenthesis, comma, etc.
            # Just advance one character.
            pos += 1
            continue
        word = wm.group(0)
        word_start = wm.start()
        # Internal locator? ("above", "below", "hereof", etc.)
        if word.lower() in _INTERNAL_LOCATORS:
            return False
        # Lowercase word — pure noise; skip.
        if not word[0].isupper():
            pos = wm.end()
            continue
        # Internal anchor? ("Schedule", "Annex", "Section", ...)
        if word in _INTERNAL_ANCHOR_WORDS:
            return False  # internal cross-reference
        # Capitalised non-anchor — check for an internal-determiner
        # immediately preceding ("this", "the said", "the present",
        # etc.). Strip trailing whitespace from the prefix and look
        # for an exact-determiner ending.
        before = tail[:word_start].rstrip()
        before_lower = before.lower()
        for det in _INTERNAL_DETERMINERS:
            det = det.rstrip()  # _INTERNAL_DETERMINERS includes trailing space
            if (before_lower == det or
                    before_lower.endswith(' ' + det)):
                return False  # "this Agreement", "the said Deed", etc.
        # Capitalised, not an anchor, not preceded by internal
        # determiner → external Proper Noun (Civil Code, Italian Code
        # of Civil Procedure, Resolution of the CICR, EU Regulation,
        # Presidential Decree, BGB, T.U.B., etc.)
        return True
    # No decisive token found within the same sentence → internal
    # default (matches v5 behaviour for bare "Article N.").
    return False

# rev42: Predicate for fix_spacing's space-insertion rules. Extracted to
# module level so apply_translations_textmatch.py can import it for the
# rev42 auto-ZWSP injection on non-Latin source paragraphs. The two
# scripts MUST use the same predicate so that auto-ZWSP fires at every
# boundary fix_spacing would otherwise space. Any change to a rule below
# changes the auto-ZWSP scope automatically — single source of truth.
_DOT_UPPER_ABBREVIATION_EXCEPTIONS = (
    'No.', 'no.', 'etc.', 'art.', 'S.p.A.', 'S.r.l.', '..', 'seq.',
)
_DOT_SINGLE_LETTER_ABBR_RE = re.compile(r'\b[A-Z]\.$')


def will_fix_spacing_fire(prev_text, curr_text):
    """Return True iff fix_spacing would insert a space between
    `prev_text` (last char) and `curr_text` (first char) at a
    text-bearing element boundary. Mirrors the 7 rules used inside
    fix_spacing below (alpha+alpha, alpha+'(', ')'+alpha, ';'+alpha,
    ','+alpha, ':'+alpha, '.'+upper-with-abbreviation-exceptions,
    digit+upper). Cheap: 1 char lookup + ≤2 string-end checks for the
    abbreviation exceptions when the dot-upper rule is candidate.
    """
    if not prev_text or not curr_text:
        return False
    pc = prev_text[-1]
    cc = curr_text[0]
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
        if (not _DOT_SINGLE_LETTER_ABBR_RE.search(prev_text)
                and not any(prev_text.endswith(s)
                            for s in _DOT_UPPER_ABBREVIATION_EXCEPTIONS)):
            return True
    if pc.isdigit() and cc.isupper():
        return True
    return False


def fix_spacing(root):
    """Fix missing spaces between adjacent text elements within paragraphs.

    now iterates ``<w:t>`` AND ``<w:delText>`` together in
    document order. The  version only walked ``<w:t>``, so the
    seam between an inserted run and a struck-through deletion was
    never inspected — the reject-all view of paragraphs with
    del-then-regular structure showed cosmetic glue
    (``"theInvestment Insurance"`` instead of
    ``"the Investment Insurance"``) that survived every gate. The
    fix preserves accept-all readability because the inserted space
    is prepended to the second element's text only — when one of
    the two elements is a delText, the fix-up applies inside the
    deletion side, so the accept-all view (which strips deleted
    text) is unaffected.

    rev42: the per-boundary rule check is now ``will_fix_spacing_fire``
    (module-level) so apply_translations_textmatch.py can pre-empt this
    function for non-Latin source paragraphs by injecting ZWSP at the
    same boundaries — fix_spacing then sees ZWSP at the seam, the rules
    don't fire, and the post-strip drift gate stays clean.
    """
    fixes = 0
    text_tag = f'{{{W}}}t'
    deltext_tag = f'{{{W}}}delText'
    for p in root.iter(f'{{{W}}}p'):
        # Collect text-bearing elements (both kinds) in document order.
        text_elems = [
            e for e in p.iter()
            if (e.tag == text_tag or e.tag == deltext_tag) and e.text
        ]
        for i in range(1, len(text_elems)):
            prev_elem = text_elems[i-1]
            curr_elem = text_elems[i]
            prev = prev_elem.text
            curr = curr_elem.text
            if will_fix_spacing_fire(prev, curr):
                curr_elem.text = ' ' + curr_elem.text
                curr_elem.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
                fixes += 1
    return fixes

def fix_definition_boundaries(root):
    """Fix missing spaces before 'means', 'shall mean', 'has the meaning', 'indicates'.

    Catches patterns like:
      - 'Termmeans' -> 'Term means'
      - 'Termshall mean' -> 'Term shall mean'
      - 'Termhas the meaning' -> 'Term has the meaning'
      - 'Termindicates' -> 'Term indicates'
    Both within single elements and across element boundaries.
    """
    fixes = 0

    # Within single elements
    for t in root.iter(f'{{{W}}}t'):
        if t.text is None:
            continue
        orig = t.text
        # "Xmeans" -> "X means" (but not "it means", "which means" etc.)
        t.text = re.sub(r'([A-Z\u201d"\)])means\b', r'\1 means', t.text)
        t.text = re.sub(r'([A-Z\u201d"\)])shall mean\b', r'\1 shall mean', t.text)
        t.text = re.sub(r'([A-Z\u201d"\)])has the meaning\b', r'\1 has the meaning', t.text)
        t.text = re.sub(r'([A-Z\u201d"\)])indicates\b', r'\1 indicates', t.text)
        if t.text != orig:
            fixes += 1

    # Across element boundaries: prev ends with term, curr starts with "means"
    for p in root.iter(f'{{{W}}}p'):
        t_elems = [(t, t.text) for t in p.iter(f'{{{W}}}t') if t.text]
        for i in range(1, len(t_elems)):
            prev = t_elems[i-1][1]
            curr_elem, curr = t_elems[i]
            if not prev or not curr:
                continue
            # Check if curr starts with definition verb and prev doesn't end with space
            if prev[-1] != ' ' and re.match(r'^(means|shall mean|has the meaning|indicates)\b', curr):
                curr_elem.text = ' ' + curr_elem.text
                curr_elem.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
                fixes += 1

    return fixes

def fix_double_punctuation(root):
    """Fix double colons, double periods (not ellipsis), double commas, double semicolons."""
    fixes = 0
    for t in root.iter(f'{{{W}}}t'):
        if t.text is None:
            continue
        orig = t.text
        # Double colon
        t.text = t.text.replace('::', ':')
        # Double period (but not ellipsis "...")
        t.text = re.sub(r'\.\.(?!\.)', '.', t.text)
        # Double comma
        t.text = t.text.replace(',,', ',')
        # Double semicolon
        t.text = t.text.replace(';;', ';')
        if t.text != orig:
            fixes += 1
    return fixes

def fix_terminology(root):
    """Apply terminology replacements to all w:t elements."""
    fixes = 0
    for t in root.iter(f'{{{W}}}t'):
        if t.text is None:
            continue
        orig = t.text

        # Literal replacements
        for old, new, is_regex in TERM_REPLACEMENTS:
            if is_regex:
                t.text = re.sub(old, new, t.text)
            else:
                t.text = t.text.replace(old, new)

        # Regex replacements
        for pattern, replacement in TERM_REGEX_REPLACEMENTS:
            t.text = re.sub(pattern, replacement, t.text)

        if t.text != orig:
            fixes += 1
    return fixes

def fix_uk_spelling(root):
    """Replace US spellings with UK equivalents (UK is the hardcoded default variant)."""
    fixes = 0
    for t in root.iter(f'{{{W}}}t'):
        if t.text is None:
            continue
        orig = t.text
        for pattern, replacement in UK_SPELLING:
            t.text = re.sub(pattern, replacement, t.text)
        if t.text != orig:
            fixes += 1
    return fixes

# US_SPELLING is the inverse mapping, used ONLY when the user has explicitly
# requested US English in their original prompt. UK is the hardcoded default;
# never fall back to this list on ambiguity.
US_SPELLING = [
    (r'\bauthorise\b', 'authorize'),
    (r'\bauthorised\b', 'authorized'),
    (r'\bAuthorised\b', 'Authorized'),
    (r'\bAUTHORISATION\b', 'AUTHORIZATION'),
    (r'\bAuthorisation\b', 'Authorization'),
    (r'\bauthorisation\b', 'authorization'),
    (r'\brecognise\b', 'recognize'),
    (r'\brecognised\b', 'recognized'),
    (r'\borganise\b', 'organize'),
    (r'\borganised\b', 'organized'),
    (r'\borganisation\b', 'organization'),
    (r'\bfavour\b', 'favor'),
    (r'\bfavoured\b', 'favored'),
    (r'\bfavourable\b', 'favorable'),
    (r'\bhonour\b', 'honor'),
    (r'\bhonoured\b', 'honored'),
    (r'\bcentre\b', 'center'),
    (r'\bdefence\b', 'defense'),
    (r'\boffence\b', 'offense'),
    (r'\bfulfil\b', 'fulfill'),
    (r'\bfulfilment\b', 'fulfillment'),
    (r'\bjudgement\b', 'judgment'),
    (r'\bjudgements\b', 'judgments'),
    (r'\bJudgement\b', 'Judgment'),
    (r'\backnowledgement\b', 'acknowledgment'),
    (r'\backnowledgements\b', 'acknowledgments'),
    (r'\butilise\b', 'utilize'),
    (r'\butilised\b', 'utilized'),
    (r'\butilisation\b', 'utilization'),
    (r'\bcancelled\b', 'canceled'),
    (r'\bcancelling\b', 'canceling'),
    (r'\blabour\b', 'labor'),
    (r'\banalyse\b', 'analyze'),
    (r'\banalysed\b', 'analyzed'),
]

def fix_us_spelling(root):
    """Replace UK spellings with US equivalents. Only invoked when --variant us
    is explicitly passed. Do NOT call this on ambiguity — UK is the default."""
    fixes = 0
    for t in root.iter(f'{{{W}}}t'):
        if t.text is None:
            continue
        orig = t.text
        for pattern, replacement in US_SPELLING:
            t.text = re.sub(pattern, replacement, t.text)
        if t.text != orig:
            fixes += 1
    return fixes

def fix_annex(root):
    """Replace 'Annex' with 'Schedule' except in legislation references."""
    fixes = 0
    for t in root.iter(f'{{{W}}}t'):
        if t.text is None or 'Annex' not in t.text:
            continue
        if any(kw in t.text for kw in ANNEX_EXCLUDE):
            continue
        orig = t.text
        t.text = re.sub(r'\bAnnex\b', 'Schedule', t.text)
        t.text = re.sub(r'\bANNEX\b', 'SCHEDULE', t.text)
        t.text = re.sub(r'\bAnnexes\b', 'Schedules', t.text)
        if t.text != orig:
            fixes += 1
    return fixes

def fix_article_to_clause(root):
    """Replace 'Article X' with 'Clause X' for INTERNAL cross-references
    only. EXTERNAL references to legislation, codes, regulatory acts,
    or other authoritative sources keep 'Article'.

    per-match decision via the structural detector
    ``_is_external_article_ref`` (no hardcoded keyword list). The
    detector looks at what follows "Article N" within the same
    sentence:

      * " of <Capitalized Proper Noun>" → external (keep Article)
      * " of this/the present/the said X" → internal (rewrite to Clause)
      * " of <internal anchor>" (Schedule, Annex, ...) → internal
      * bare "Article N." or "(Article N)" → internal (rewrite)

    The decision is per-match, so a single paragraph can contain a
    mix of internal and external references and each will be handled
    correctly.
    """
    fixes = 0
    article_re = re.compile(r'\bArticles?\s+\d[\d.:]*(?:-[A-Za-z]{1,15})*')
    for p in root.iter(f'{{{W}}}p'):
        # Build the joined paragraph text once for context lookup.
        t_elems = list(p.iter(f'{{{W}}}t'))
        joined = ''.join((t.text or '') for t in t_elems)
        if not article_re.search(joined):
            continue
        # Find absolute start positions in `joined` of all "Article N"
        # matches that should KEEP Article (external references).
        external_starts = set()
        for m in article_re.finditer(joined):
            if _is_external_article_ref(joined, m.end()):
                external_starts.add(m.start())
        # Walk t_elems and rewrite per-element. Only rewrite matches
        # whose absolute start position is NOT in external_starts.
        running = 0
        local_re = re.compile(r'\b(Articles?)\s+(\d[\d.:]*(?:-[A-Za-z]{1,15})*)')
        for t in t_elems:
            txt = t.text or ''
            if not txt:
                running += len(txt)
                continue
            new_pieces = []
            last = 0
            for m in local_re.finditer(txt):
                abs_start = running + m.start()
                new_pieces.append(txt[last:m.start()])
                if abs_start in external_starts:
                    # External — keep Article(s)
                    new_pieces.append(m.group(0))
                else:
                    # Internal — rewrite Article→Clause / Articles→Clauses
                    word = ('Clauses' if m.group(1) == 'Articles'
                            else 'Clause')
                    new_pieces.append(f'{word} {m.group(2)}')
                last = m.end()
            new_pieces.append(txt[last:])
            new_txt = ''.join(new_pieces)
            if new_txt != txt:
                t.text = new_txt
                fixes += 1
            running += len(txt)
    return fixes

def fix_duplicates(root):
    """Fix duplicate words both within elements and across element boundaries."""
    fixes = 0

    # Within elements — catch any word duplicated (not just a fixed list)
    for t in root.iter(f'{{{W}}}t'):
        if t.text is None:
            continue
        orig = t.text
        # Generic: any word of 3+ chars duplicated with space
        t.text = re.sub(r'\b(\w{3,})\s+\1\b', r'\1', t.text, flags=re.IGNORECASE)
        if t.text != orig:
            fixes += 1

    # Across element boundaries
    for p in root.iter(f'{{{W}}}p'):
        t_elems = [(t, t.text) for t in p.iter(f'{{{W}}}t') if t.text and t.text.strip()]
        for i in range(1, len(t_elems)):
            prev_elem, prev = t_elems[i-1]
            curr_elem, curr = t_elems[i]
            prev_words = prev.split()
            curr_words = curr.split()
            if prev_words and curr_words:
                pw = re.sub(r'[,;:."\'\)\]]+$', '', prev_words[-1])
                cw = re.sub(r'^["\'\(\[]+', '', curr_words[0])
                if pw and cw and pw.lower() == cw.lower() and len(pw) > 2 and pw.isalpha():
                    # Remove the duplicate from the current element
                    curr_elem.text = re.sub(r'^\s*' + re.escape(curr_words[0]) + r'\s*', ' ', curr)
                    fixes += 1

    return fixes

def fix_quotes(root):
    """Fix missing closing quotes on defined terms before definition verbs.

    Finds patterns like:
      "Security Period has the meaning...
    and adds the missing closing quote:
      "Security Period" has the meaning...
    """
    fixes = 0
    OPEN_Q = '\u201c'
    CLOSE_Q = '\u201d'

    for p in root.iter(f'{{{W}}}p'):
        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))

        # Only process paragraphs with definition verbs
        if not any(v in full for v in ['means', 'shall mean', 'has the meaning', 'indicates']):
            continue

        # Work element by element to find open-quote elements that need closing
        t_elems = list(p.iter(f'{{{W}}}t'))
        for i, t in enumerate(t_elems):
            if t.text is None:
                continue

            # Check for pattern: element ends with term text and next element starts
            # with "means"/"shall mean"/"has the meaning" but no close quote between
            if t.text.rstrip().endswith(CLOSE_Q) or t.text.rstrip().endswith('"'):
                continue  # Already has closing quote

            # Look ahead: does next text element start with a definition verb?
            for j in range(i + 1, min(i + 3, len(t_elems))):
                if t_elems[j].text is None:
                    continue
                next_text = t_elems[j].text.lstrip()
                if re.match(r'^(means|shall mean|has the meaning|indicates)\b', next_text):
                    # Check if there's an open quote earlier that's unmatched
                    preceding = ''.join(te.text or '' for te in t_elems[:i+1])
                    open_count = preceding.count(OPEN_Q) + preceding.count('\u201e')
                    close_count = preceding.count(CLOSE_Q)
                    if open_count > close_count:
                        # Add closing quote to the end of this element
                        t.text = t.text.rstrip() + CLOSE_Q
                        fixes += 1
                break  # Only check the next non-empty element

    return fixes

def fix_definition_line_breaks(root):
    """Remove unwanted line breaks (w:br) within definition paragraphs.

    In Italian documents, a definition often has the term on one line and the meaning
    on the next. After translation, this creates an ugly break:
        "Potential Event of Default"
        means any event which...

    This should be a single flowing line:
        "Potential Event of Default" means any event which...

    We detect definition paragraphs (containing "means"/"shall mean"/"has the meaning"
    plus a quote character) and remove any w:br elements found within them.
    """
    fixes = 0
    for p in root.iter(f'{{{W}}}p'):
        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))

        # Only process definition paragraphs
        if not any(v in full for v in ['means', 'shall mean', 'has the meaning', 'indicates']):
            continue
        if not any(q in full for q in ['\u201c', '"', '\u201e']):
            continue

        # Find and remove w:br elements in runs
        for r in p.iter(f'{{{W}}}r'):
            br = r.find(f'{{{W}}}br')
            if br is not None:
                r.remove(br)
                fixes += 1

    return fixes

def fix_spurious_italic_runs(root):
    """Remove italic from runs in body paragraphs where italic is not appropriate.

    In Italian legal documents, defined terms are sometimes italic in the source, and
    after translation the italic sticks to runs that should be normal weight in English.

    Rules:
    - In definition paragraphs: only the cross-reference heading in parentheses should
      be italic (e.g., "(Preservation of the Security)"). The defined term should be
      bold, the meaning should be normal.
    - In body paragraphs: italic is appropriate only for cross-reference headings in
      parentheses and for Latin terms. All other text should be normal.
    - Headings: italic is OK if the paragraph style says so (inherited from pPr).

    This function removes italic from runs that contain substantive English text (more
    than 3 words, not in parentheses, not a Latin term) in non-heading paragraphs.
    """
    fixes = 0
    latin_terms = {
        'inter alia', 'mutatis mutandis', 'pari passu', 'pro rata', 'bona fide',
        'vis-à-vis', 'de facto', 'de jure', 'prima facie', 'sui generis', 'et seq.',
        'ad hoc', 'ab initio', 'ultra vires', 'per se', 'in rem',
    }

    for p in root.iter(f'{{{W}}}p'):
        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))
        if not full.strip():
            continue

        # Skip headings (all caps or very short)
        if full.strip() == full.strip().upper() and len(full.split()) < 10:
            continue

        # Check if paragraph-level properties set italic (then it's intentional)
        # ST_OnOff falsy set extended to include 'off'
        # (case-insensitive) per ECMA-376.
        _ST_ONOFF_FALSE_PP = {'false', '0', 'off'}

        def _is_off(val):
            return val is not None and val.strip().lower() in _ST_ONOFF_FALSE_PP

        ppr = p.find(f'{{{W}}}pPr')
        if ppr is not None:
            p_rpr = ppr.find(f'{{{W}}}rPr')
            if p_rpr is not None:
                i_elem = p_rpr.find(f'{{{W}}}i')
                if i_elem is not None:
                    val = i_elem.get(f'{{{W}}}val')
                    if not _is_off(val):
                        continue  # Paragraph style is italic — leave it

        for r in p.iter(f'{{{W}}}r'):
            rpr = r.find(f'{{{W}}}rPr')
            if rpr is None:
                continue
            i_elem = rpr.find(f'{{{W}}}i')
            if i_elem is None:
                continue
            val = i_elem.get(f'{{{W}}}val')
            if _is_off(val):
                continue

            t = r.find(f'{{{W}}}t')
            if t is None or not t.text:
                continue

            text = t.text.strip()
            # Keep italic if: in parentheses, a Latin term, a short cross-ref heading,
            # or a numbering label (e.g., "1.1", "(a)")
            if not text:
                continue
            if text.startswith('(') and text.endswith(')'):
                continue  # Cross-ref heading in parentheses
            if any(lt in text.lower() for lt in latin_terms):
                continue
            if len(text) <= 5 and re.match(r'^[\d\.\(\)a-z]+$', text):
                continue  # Numbering label like "1.1" or "(a)"

            # If it's substantive text (more than 2 words) and italic, remove italic
            if len(text.split()) > 2:
                rpr.remove(i_elem)
                fixes += 1

    return fixes

def fix_schedule_page_breaks(root):
    """Insert page breaks before Schedule/Annex headings.

    In Italian legal documents, each Schedule (Allegato) starts on a new page. After
    translation, these page breaks may be lost. This function finds Schedule heading
    paragraphs and ensures they have a w:pageBreakBefore element in their paragraph
    properties (w:pPr).

    Matches paragraphs whose full text (stripped) matches patterns like:
    - "SCHEDULE 1", "SCHEDULE A", "Schedule 1"
    - "ANNEX 1", "ANNEX A", "Annex 1"
    - "ALLEGATO 1", "ALLEGATO A"  (Italian remnants)

    Skips paragraphs that are TOC entries (style starts with "TOC") or body-content
    schedule reference lists (styles like FWBL2, FWBCont1, FWBCont2, Normal) which
    merely *mention* schedules but are not actual schedule heading pages. Only
    dedicated schedule heading styles (e.g. ITScheduleL1, or paragraphs with no
    body-content style) receive page breaks.
    """
    fixes = 0
    schedule_pattern = re.compile(
        r'^\s*(SCHEDULE|Schedule|ANNEX|Annex|ALLEGATO|Allegato)\s+[\dA-Za-z]',
        re.IGNORECASE
    )

    # Styles that should NEVER receive schedule page breaks:
    # - TOC styles: these are table-of-contents entries
    # - Body-content styles: these are in-text references to schedules
    SKIP_STYLES = {
        'TOC1', 'TOC2', 'TOC3', 'TOC4', 'TOC5', 'TOC6', 'TOC7', 'TOC8', 'TOC9',
        'FWBL2', 'FWBL3', 'FWBL4', 'FWBL5',
        'FWBCont1', 'FWBCont2', 'FWBCont3',
        'Normal',
    }

    for p in root.iter(f'{{{W}}}p'):
        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t')).strip()
        if not full:
            continue

        if not schedule_pattern.match(full):
            continue

        # language-agnostic length cap. Schedule headings are short
        # labels — the longest legitimate heading observed in real legal
        # docs ("Schedule 4 — Form of Notice of Drawdown and Form of Notice
        # of Conversion", "SCHEDULE 7 — REPRESENTATIONS, WARRANTIES,
        # COVENANTS, AND OTHER UNDERTAKINGS") sits under ~90 chars; the
        # 120-char threshold gives generous headroom while still catching
        # body prose that begins with a schedule reference and continues
        # into a sentence ("Schedule G (Construction Budget) sets out the
        # schedule of costs of the works approved by the Parties..." is
        # 100+ chars on the first sentence alone). The cap is target-
        # language-only — it depends on English heading conventions, not
        # on source-language style names — so it works equally well on
        # Polish, Hungarian, Italian or any other source.
        if len(full) > 120:
            continue

        # label-token check. A real schedule heading's second
        # token is the schedule's label — "G", "5", "III", "1.A", "12" —
        # all-uppercase letters, digits, or roman numerals; never a
        # lowercase preposition. A clause heading whose English
        # rendering happens to start with the word "Schedule" has a
        # lowercase preposition or proper noun there (e.g. "Schedule
        # for Performance of the Works" — "for" is a lowercase
        # preposition, not a label). The  length cap doesn't
        # catch the short variant of this defect (the offending para
        # is 36 chars, well under 120). Strip trailing punctuation
        # from the label token before the lowercase check so dash- or
        # colon-suffixed labels ("G-", "5:", "III—") aren't false-
        # negatived. Leaves real headings untouched, eliminates the
        # "Schedule for X" / "Schedule of Y" / "Schedule by Z" body-
        # prose class.
        m_label = re.match(
            r'^\s*(?:SCHEDULE|ANNEX|ALLEGATO)\s+(\S+)',
            full, re.IGNORECASE)
        if m_label and any(
                c.islower()
                for c in m_label.group(1).rstrip(':,;.-—–')):
            continue

        # Check paragraph style — skip TOC entries and body-content references
        ppr = p.find(f'{{{W}}}pPr')
        style = None
        if ppr is not None:
            style_elem = ppr.find(f'{{{W}}}pStyle')
            if style_elem is not None:
                style = style_elem.get(f'{{{W}}}val', '')

        if style and (style in SKIP_STYLES or style.upper().startswith('TOC')):
            continue
        if ppr is None:
            ppr = etree.SubElement(p, f'{{{W}}}pPr')
            # Move pPr to be the first child
            p.remove(ppr)
            p.insert(0, ppr)

        # Check if pageBreakBefore already exists
        pb = ppr.find(f'{{{W}}}pageBreakBefore')
        if pb is None:
            pb = etree.Element(f'{{{W}}}pageBreakBefore')
            # Insert pageBreakBefore in correct OOXML pPr order (before rPr)
            # Canonical ordering: pStyle, keepNext, keepLines, pageBreakBefore, ...
            # rPr must always be last child of pPr
            PPR_ORDER = [
                'pStyle', 'keepNext', 'keepLines', 'pageBreakBefore',
                'framePr', 'widowControl', 'numPr', 'suppressLineNumbers',
                'pBdr', 'shd', 'tabs', 'suppressAutoHyphens', 'kinsoku',
                'wordWrap', 'overflowPunct', 'topLinePunct', 'autoSpaceDE',
                'autoSpaceDN', 'bidi', 'adjustRightInd', 'snapToGrid',
                'spacing', 'ind', 'contextualSpacing', 'mirrorIndents',
                'suppressOverlap', 'jc', 'textDirection', 'textAlignment',
                'textboxTightWrap', 'outlineLvl', 'divId', 'cnfStyle',
                'rPr',
            ]
            target_idx = PPR_ORDER.index('pageBreakBefore')
            inserted = False
            for i, child in enumerate(ppr):
                child_local = child.tag.split('}')[1] if '}' in child.tag else child.tag
                child_order = PPR_ORDER.index(child_local) if child_local in PPR_ORDER else len(PPR_ORDER) - 1
                if child_order > target_idx:
                    ppr.insert(i, pb)
                    inserted = True
                    break
            if not inserted:
                ppr.append(pb)
            fixes += 1

    return fixes

def extract_header(xml_text):
    """Extract XML declaration and root element opening tag from raw XML text."""
    m = re.match(r'(<\?xml[^?]*\?>\s*<w:document[^>]*>)', xml_text, re.DOTALL)
    return m.group(1) if m else None

def _xml_has_tracked_changes(xml_path):
    """Cheap check: does document.xml contain any <w:ins>, <w:del>, or
    <w:delText> elements? Used to gate the auto-invoke of
    strip_noop_tracked_changes.py at the end of post_process."""
    try:
        with open(xml_path, 'rb') as f:
            content = f.read()
    except OSError:
        return False
    return (b'<w:ins ' in content or b'<w:ins>' in content or
            b'<w:del ' in content or b'<w:del>' in content or
            b'<w:delText' in content)

def _run_strip_noop_subprocess(xml_path):
    """Auto-invoke strip_noop_tracked_changes.py as a subprocess.
    Mandatory for TC documents — refuses to leave post_process if the
    strip step fails."""
    import subprocess
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"\n{'=' * 60}\n[post_process] auto-running "
          f"strip_noop_tracked_changes.py (TC document)\n{'=' * 60}")
    result = subprocess.run(
        [sys.executable,
         os.path.join(scripts_dir, 'strip_noop_tracked_changes.py'),
         xml_path],
        capture_output=False)
    if result.returncode != 0:
        raise RuntimeError(
            f"strip_noop_tracked_changes.py returned exit code "
            f"{result.returncode}. post_process aborted; document may be "
            f"in an inconsistent state."
        )

def _autodetect_paragraphs_json(xml_path):
    """Rev18: locate the paragraphs.json that produced this document.xml.

    Convention from `skill-docs/06-postprocess-and-reorder.md`:
        ``python post_process.py <workdir>/final/word/document.xml ...``
    so paragraphs.json is at ``<workdir>/paragraphs.json``. Walk up two
    parents from the xml file (``word`` → ``final`` → ``workdir``) and
    look for ``paragraphs.json`` next to the ``final/`` directory.
    Returns the path if found, else None.
    """
    try:
        xml_abs = os.path.abspath(xml_path)
        # <workdir>/final/word/document.xml — walk up 3 parents to <workdir>
        workdir = os.path.dirname(os.path.dirname(os.path.dirname(xml_abs)))
        candidate = os.path.join(workdir, 'paragraphs.json')
        if os.path.isfile(candidate):
            return candidate
    except (OSError, ValueError):
        pass
    return None

def _run_validate_apply_post_strip(xml_path, paragraphs_json_path):
    """Rev18: run validate_apply.py --strict at the end of post_process,
    AFTER strip_noop_tracked_changes has already run.

    Why this exists: ``apply_translations_textmatch.py`` already runs
    ``validate_apply --strict`` at end-of-apply, but at that point the
    XML still contains phantom (``ins_then_del``) wrappers and any
    placeholder symbols (``○``, ``□``) that ``strip_noop`` will later
    remove during post_process. Those wrappers/symbols are still
    declared in paragraphs.json. So a doc that drifts during strip_noop
    passes the apply-time gate and only fails at repack-time
    ``validate_apply``, after Steps 6→9 have burned wall-clock.

    Adding a second invocation here means strip_noop-induced drift
    surfaces at the END of Step 6, not at Step 10. Step 9 (quality
    check) and the repack itself are skipped on a doomed doc, saving
    15-60 seconds per failed iteration on top of the diagnostic time
    already saved by surfacing the failure immediately.

    Same script, same flag, same exit semantics — ``_run_validator``-
    style block on exit code != 0.
    """
    import subprocess
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"\n{'=' * 60}\n[post_process] auto-running "
          f"validate_apply.py --strict (post-strip drift gate)\n"
          f"{'=' * 60}")
    result = subprocess.run(
        [sys.executable,
         os.path.join(scripts_dir, 'validate_apply.py'),
         paragraphs_json_path,
         xml_path,
         '--strict',
         # rev42: fix_spacing has already inserted spaces at
         # element boundaries by this point. Tell validate_apply
         # to simulate the same insertion on the declared side
         # so tokenisation is symmetric and the gate doesn't
         # false-fire on the post-mortem digit→upper class.
         '--post-spacing-fix'],
        capture_output=False)
    if result.returncode != 0:
        raise RuntimeError(
            f"SKILL GATE FIRED — INTENTIONAL BLOCK, NOT A SCRIPT ERROR. "
            f"validate_apply.py --strict returned exit code "
            f"{result.returncode} after post_process / strip_noop. "
            f"The document drifted from paragraphs.json during Step 6 "
            f"(typically: phantom segment glued to next regular by "
            f"period-lowercase, or symbol placeholder stripped as noise). "
            f"Fix paragraphs.json and re-run from Step 5 (apply). "
            f"Do NOT work around this gate by skipping the post-strip "
            f"validate_apply check — doing so silently ships output below "
            f"the quality the skill is designed to deliver. Surfaces the "
            f"failure ~4 minutes earlier than the repack-time gate would."
        )

def post_process(xml_path, fix=True, variant='uk', paragraphs_json=None):
    """Run all post-processing fixes on a document.xml file.

    Rev11 (final): auto-invokes strip_noop_tracked_changes.py at the end
    when the document contains tracked changes. The previous Step 6b is
    folded into Step 6 — operator runs ONE command and gets both passes
    on TC documents.

    also auto-invokes ``validate_apply.py --strict`` after the
    strip pass, so any drift between paragraphs.json and the post-
    stripped document.xml (phantom-segment glue, symbol-placeholder
    strips) is caught at end of Step 6 instead of at repack time. The
    paragraphs.json path is auto-detected from the conventional layout
    (``<workdir>/final/word/document.xml`` → ``<workdir>/paragraphs.json``);
    the explicit ``paragraphs_json`` argument overrides auto-detection.
    Skips silently if no paragraphs.json is found (post_process is also
    used standalone for non-TC documents and ad-hoc XML).
    """

    # Capture original header before parsing
    with open(xml_path, 'r', encoding='utf-8') as f:
        raw_xml = f.read()
    orig_header = extract_header(raw_xml)

    tree = etree.parse(xml_path)
    root = tree.getroot()

    results = {}
    results['spacing'] = fix_spacing(root)
    results['definition_boundaries'] = fix_definition_boundaries(root)
    results['double_punctuation'] = fix_double_punctuation(root)
    results['terminology'] = fix_terminology(root)
    if variant == 'uk':
        results['uk_spelling'] = fix_uk_spelling(root)
    elif variant == 'us':
        results['us_spelling'] = fix_us_spelling(root)
    results['annex_to_schedule'] = fix_annex(root)
    results['article_to_clause'] = fix_article_to_clause(root)
    results['duplicates'] = fix_duplicates(root)
    results['quotes'] = fix_quotes(root)
    results['definition_line_breaks'] = fix_definition_line_breaks(root)
    results['spurious_italic'] = fix_spurious_italic_runs(root)
    results['schedule_page_breaks'] = fix_schedule_page_breaks(root)

    total = sum(results.values())

    for name, count in results.items():
        if count:
            print(f"  {name}: {count} fixes")
    print(f"  TOTAL: {total} fixes")

    if fix and total > 0:
        tree.write(xml_path, xml_declaration=True, encoding='UTF-8',
                   standalone=True)

        # Restore original header (lxml's write changes quotes/namespaces)
        if orig_header:
            with open(xml_path, 'r', encoding='utf-8') as f:
                written = f.read()
            written = re.sub(
                r'^<\?xml[^?]*\?>\s*<w:document[^>]*>',
                orig_header,
                written,
                count=1,
                flags=re.DOTALL
            )
            with open(xml_path, 'wb') as f:
                f.write(written.encode('utf-8'))

        print(f"  Saved to {xml_path}")

    # Rev11 (final): auto-run strip_noop_tracked_changes.py for TC docs.
    # Replaces the previous Step 6b as a separate operator command —
    # post_process now does both passes in one invocation.
    if fix and _xml_has_tracked_changes(xml_path):
        _run_strip_noop_subprocess(xml_path)

    # post-strip drift gate. Auto-detect paragraphs.json by
    # convention if not supplied explicitly. Surfaces phantom-glue and
    # placeholder-strip failures at end of Step 6 rather than at Step 10.
    if fix:
        pjson = paragraphs_json or _autodetect_paragraphs_json(xml_path)
        if pjson:
            _run_validate_apply_post_strip(xml_path, pjson)

    return results

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Post-process translated legal document XML')
    parser.add_argument('xml_path', help='Path to document.xml')
    parser.add_argument('--fix', action='store_true', default=True,
                        help='Apply fixes (default: True)')
    parser.add_argument('--report-only', action='store_true',
                        help='Only report issues, do not fix')
    parser.add_argument('--variant', choices=['uk', 'us'], default='uk',
                        help='English variant (default: uk)')
    parser.add_argument('--paragraphs', dest='paragraphs_json', default=None,
                        help=('Rev18: explicit paragraphs.json path for the '
                              'post-strip validate_apply --strict drift gate. '
                              'When omitted, auto-detected from the convention '
                              '<workdir>/paragraphs.json; if neither is found '
                              'the post-strip gate is skipped.'))
    args = parser.parse_args()

    if args.report_only:
        args.fix = False

    post_process(args.xml_path, fix=args.fix, variant=args.variant,
                 paragraphs_json=args.paragraphs_json)

# === SKILL FILE COMPLETE ===
