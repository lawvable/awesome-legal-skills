"""Per-language marker word lists for detecting untranslated source-language
remnants in translated output.

Used by `apply_translations_textmatch.py` and `quality_check.py`.

============================================================================
WHY THIS MODULE EXISTS
============================================================================

Earlier versions of the skill hard-coded an Italian word list (`della`, `allo`,
`alle`, `Committente`, `Appaltatore`, etc.) into both the apply script and the
quality check. When translating from any non-Italian language, the scanner
produced false positives against English fragments: `allo` matches "allocated",
`alle` matches "already", `della` matches "challenge", and so on. Meanwhile, a
Dutch, German, or Polish source-language remnant in the output would sail
through undetected because no marker list for those languages existed.

This module defines:

* `LANGUAGE_MARKERS` — a dict mapping each supported source language to a
  list of distinctive function words / legal terms that virtually never appear
  inside English words. All entries are matched with **whole-word** regex
  (`\bword\b`) to prevent substring false positives.

* `AUTO_DETECT_MARKERS` — a denser function-word list per language used for
  automatically guessing the source language from a block of source text.

* `WHITESPACE_OK_CONTEXTS` — fragments that legitimately contain what looks
  like a source-language word in English legal drafting (for example, proper
  nouns that happen to contain "della").

* Helper functions `scan_remnants()` and `detect_language()`.

============================================================================
DESIGN PRINCIPLES FOR MARKERS
============================================================================

Each list is hand-curated to minimise false positives against English:

* **Latin-script languages**: entries are at least four characters long and
  chosen to have no common English substring hits (so `il`, `la`, `de`, `het`,
  `een`, `und`, `una`, etc. are deliberately excluded — they would false-match
  against English words like "Illinois", "laundry", "detail", "etcetera").

* **Distinctive legal vocabulary**: party-role words (Dutch `Partijen`, Italian
  `Committente`, French `lequel`, German `Vertragspartei`), common civil-law
  connectives (Dutch `hierbij`, Italian `ai sensi`, German `gemäß`, Spanish
  `conforme a`), and contract-header vocabulary (Dutch `Overeenkomst`, Italian
  `Contratto`, German `Vertrag`).

* **CJK languages**: character-based matching. Chinese uses ideograph
  sequences common in legal drafting (协议, 各方, 根据, 鉴于). Japanese uses
  contract-specific kanji combinations (契約, 当事者, 甲, 乙).

If a genuine remnant is missed, add to the relevant list. Never add entries
with fewer than four Latin characters; always prefer multi-word phrases.
"""
import re
import os
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
# LANGUAGE_MARKERS — distinctive source-language words / phrases that
# should never appear in translated output. Matched with \b word boundaries.
#
# These lists are scan-only (used to flag remnants in translated output).
# They are NOT the scheme for choosing English translations.
# ──────────────────────────────────────────────────────────────────────
LANGUAGE_MARKERS = {
    'italian': [
        r'\bdelle\b', r'\bdegli\b', r'\bdella\b', r'\bdello\b',
        r'\bnelle\b', r'\bnegli\b', r'\bnella\b', r'\bnello\b',
        r'\balla\b', r'\ballo\b', r'\balle\b', r'\bagli\b',
        r'\bsulla\b', r'\bsullo\b', r'\bsulle\b', r'\bsugli\b',
        r'\bai sensi\b', r'\bin conformità\b',
        r'\bpresente Contratto\b', r'\bpresente contratto\b',
        r'\bCommittente\b', r'\bAppaltatore\b', r'\bCorrispettivo\b',
        r'\bNormativa Applicabile\b',
        r'\bobbligazioni\b', r'\badempimento\b', r'\bsottoscrizione\b',
        r'\brappresentare\b', r'\bcomunicazioni con\b',
        r'\bcontestazioni\b', r'\bpredisposizione\b',
        r'\bnonché\b', r'\bladdove\b', r'\bqualora\b', r'\bpertanto\b',
        r'\baltresì\b', r'\bfermo restando\b', r'\bivi inclus',
    ],
    'dutch': [
        r'\bPartijen\b', r'\bOvereenkomst\b', r'\bhierbij\b', r'\bhierna\b',
        r'\boverkomstig\b', r'\bovereenkomstig\b',
        r'\bhetgeen\b', r'\bderhalve\b', r'\bonverminderd\b',
        r'\bverplichtingen\b', r'\bvertegenwoordigd\b',
        r'\bPlangebied\b', r'\bGrondeigenaren\b', r'\bWindpark\b',
        r'\bStuurgroep\b', r'\bProjectteam\b', r'\bgrondrechten\b',
        r'\bomgevingsvergunning\b', r'\bconcessieverlener\b',
        r'\bopzegging\b', r'\bontbinding\b', r'\bingebrekestelling\b',
        r'\bfaillissement\b', r'\bsurs[eé]ance\b',
        r'\buit hoofde van\b', r'\bvoor zover\b', r'\bten deze\b',
        r'\bte dezen\b', r'\bbestuurder\b', r'\bvennootschap\b',
        r'\bartikel [0-9]+\b',  # Dutch internal Article references
    ],
    'german': [
        r'\bgemäß\b', r'\bhinsichtlich\b', r'\bdergestalt\b',
        r'\bmithin\b', r'\bsofern\b', r'\bvorliegend\w*\b',
        r'\bVertragspartei\w*\b', r'\bverpflichtet sich\b',
        r'\bVertragsgegenstand\b', r'\bGeschäftsführer\w*\b',
        r'\bProkurist\w*\b', r'\bBevollmächtigt\w*\b',
        r'\bim Rahmen\b', r'\bgegenüber\b', r'\bdes Weiteren\b',
        r'\bAbschluss\b', r'\bUnternehmen\b', r'\bAusübung\b',
        r'\bVertragsschluss\b',
    ],
    'french': [
        r'\blequel\b', r'\blaquelle\b', r'\blesquels\b', r'\blesquelles\b',
        r'\bconformément\b', r'\btoutefois\b', r'\bnéanmoins\b',
        r'\baux termes\b', r'\ben vertu\b', r'\bledit\b', r'\bladite\b',
        r'\blesdits\b', r'\blesdites\b',
        r'\bdûment\b', r'\bhabilité\b', r'\bhabilitée\b',
        r'\bétant entendu\b', r'\bétant précisé\b',
        r'\bReprésentant Légal\b', r'\bSociété\b',
        r'\bconvention\b', r'\bchacune des parties\b',
    ],
    'spanish': [
        r'\bconforme a\b', r'\ben virtud de\b',
        r'\basimismo\b', r'\bno obstante\b',
        r'\bdicho\b', r'\bdicha\b', r'\bdichos\b', r'\bdichas\b',
        r'\bmediante\b', r'\baquél\b', r'\baquélla\b',
        r'\bla sociedad\b', r'\bel presente\b', r'\ba efectos de\b',
        r'\bConsejero Delegado\b', r'\bApoderado\b',
    ],
    'portuguese': [
        r'\bem virtude\b', r'\bconforme\b', r'\boutrossim\b',
        r'\bnos termos\b', r'\bmediante\b',
        r'\bo presente\b', r'\ba presente\b',
        r'\bPresidente do Conselho\b', r'\bAdministrador\w*\b',
        r'\bSociedade\b', r'\bfica acordado\b',
    ],
    'polish': [
        r'\bniniejszy\b', r'\bniniejsza\b', r'\bniniejszej\b', r'\bniniejszym\b',
        r'\boraz\b', r'\bzgodnie z\b', r'\bw szczególności\b',
        r'\bStrony\b', r'\bUmowa\b', r'\bSpółka\b',
        r'\bPrezes Zarządu\b', r'\bCzłonek Zarządu\b',
        r'\bPełnomocnik\b',
    ],
    'finnish': [
        r'\bettä\b', r'\bsekä\b', r'\bkuitenkin\b',
        r'\bsopimus\b', r'\bosapuolet\b', r'\btämän\b',
        r'\bToimitusjohtaja\b', r'\bHallituksen puheenjohtaja\b',
    ],
    'hungarian': [
        r'\bvalamint\b', r'\btovábbá\b', r'\billetve\b',
        r'\bszerint\b', r'\balapján\b', r'\bvonatkozóan\b',
        r'\bFelek\b', r'\bSzerződés\b', r'\ba jelen Szerződés\b',
        r'\bÜgyvezető\b', r'\bVezérigazgató\b',
    ],
    'chinese': [
        '协议', '各方', '甲方', '乙方', '本协议', '根据', '鉴于',
        '董事长', '法定代表人', '授权代表',
    ],
    'japanese': [
        '契約', '甲', '乙', '当事者', '本契約', '本書',
        '代表取締役', '取締役', '支配人',
        # romanised era names with a year digit. Catches the
        # "Reiwa 5" / "Heisei 29" / "Showa 64.1.7" defect class — era
        # references that walked through every gate in  because
        # the Japanese remnant list was CJK-only. Era + digit is
        # unambiguous: under the strict Gregorian-only rule
        # (references/general-legal.md and japanese-general-legal.md),
        # any era name followed by a year number in the English output
        # is a translation defect. The pattern deliberately requires
        # the digit so legitimate proper nouns ("Reiwa Corp.", "Mr.
        # Heisei Tanaka") are not false-positived.
        r'\b(Reiwa|Heisei|Showa|Taisho|Meiji)\s+\d',
    ],
}

# Fragments that legitimately contain what looks like a source-language word
# in properly translated English legal drafting. Scanner skips a match if
# any of these contexts surround it.
WHITESPACE_OK_CONTEXTS = [
    # Italian proper nouns / common transliterations that may remain in English
    'Banca d\'Italia', 'Cassa Depositi e Prestiti',
    'Contratto di Finanziamento',
    # Other defined-term proper nouns that might otherwise trip false positives
]

# ──────────────────────────────────────────────────────────────────────
# AUTO_DETECT_MARKERS — function-word lists used to guess the source
# language from a block of SOURCE text. Use more common (shorter) words here
# since we are scanning Dutch/Italian/etc. source text, not English output.
# ──────────────────────────────────────────────────────────────────────
AUTO_DETECT_MARKERS = {
    'italian': [
        r'\bdella\b', r'\bdelle\b', r'\bdegli\b', r'\bche\b', r'\be\b',
        r'\bnel\b', r'\bnei\b', r'\bper\b', r'\bsono\b', r'\bsulla\b',
        r'\bai sensi\b', r'\bdeve\b', r'\bogni\b', r'\bpresente\b',
    ],
    'dutch': [
        r'\bhet\b', r'\bde\b', r'\ben\b', r'\bvan\b', r'\bdat\b',
        r'\bzijn\b', r'\bdeze\b', r'\bomtrent\b', r'\bvoor\b',
        r'\bPartijen\b', r'\bOvereenkomst\b', r'\bhierna\b', r'\bhierbij\b',
    ],
    'german': [
        r'\bund\b', r'\bder\b', r'\bdie\b', r'\bdas\b', r'\bdes\b',
        r'\bdem\b', r'\bden\b', r'\bmit\b', r'\bim\b', r'\bzu\b',
        r'\bgemäß\b', r'\bVertrag\b', r'\bParteien\b',
    ],
    'french': [
        r'\bles\b', r'\bdes\b', r'\baux\b', r'\bdu\b', r'\bque\b',
        r'\bet\b', r'\bune\b', r'\bdans\b', r'\bpar\b',
        r'\bconformément\b', r'\blequel\b',
    ],
    'spanish': [
        r'\blos\b', r'\blas\b', r'\bde\b', r'\bdel\b', r'\bque\b',
        r'\by\b', r'\ben\b', r'\bpor\b', r'\bpara\b', r'\bcon\b',
        r'\bconforme\b', r'\bmediante\b',
    ],
    'portuguese': [
        r'\bos\b', r'\bas\b', r'\bdos\b', r'\bdas\b', r'\bque\b',
        r'\be\b', r'\bem\b', r'\bpor\b', r'\bpara\b',
        r'\bconforme\b', r'\bnos termos\b',
    ],
    'polish': [
        r'\bw\b', r'\bna\b', r'\bz\b', r'\bdo\b', r'\bże\b',
        r'\bi\b', r'\bsię\b', r'\boraz\b', r'\bniniejszy\b',
    ],
    'finnish': [
        r'\bettä\b', r'\bja\b', r'\bsekä\b', r'\btämän\b',
        r'\bosapuolet\b', r'\bsopimus\b',
    ],
    'hungarian': [
        r'\bés\b', r'\ba\b', r'\baz\b', r'\bhogy\b', r'\bvalamint\b',
        r'\bFelek\b', r'\bSzerződés\b',
    ],
    'chinese': ['的', '是', '本', '各方', '协议'],
    'japanese': ['の', 'は', 'に', 'を', '本', '契約'],
}

def detect_language(source_text, default=None):
    """Guess the source language from a sample of source-language text.

    Returns the language key with the highest marker count, or `default` if
    no language scores above a small threshold (avoids false positives on
    short/empty inputs).
    """
    if not source_text:
        return default
    best_lang = default
    best_score = 0
    for lang, patterns in AUTO_DETECT_MARKERS.items():
        score = 0
        for pat in patterns:
            if isinstance(pat, str) and not pat.startswith(r'\b'):
                # Character-level match (CJK)
                score += source_text.count(pat)
            else:
                score += len(re.findall(pat, source_text, flags=re.IGNORECASE))
        if score > best_score:
            best_score = score
            best_lang = lang
    # Require at least a few hits to consider detection reliable.
    return best_lang if best_score >= 5 else default

def scan_remnants(text, source_language):
    """Return a list of (marker_pattern, match_snippet) for every source-language
    marker found in `text`. `source_language` is one of the LANGUAGE_MARKERS keys
    (case-insensitive). Returns [] if language is unknown or has no markers.

    Matches inside any WHITESPACE_OK_CONTEXTS substring are suppressed.
    """
    if not source_language:
        return []
    patterns = LANGUAGE_MARKERS.get(source_language.lower())
    if not patterns:
        return []
    hits = []
    for pat in patterns:
        if isinstance(pat, str) and not pat.startswith(r'\b'):
            # Character-level match for CJK
            for i, ch_group in enumerate(re.finditer(re.escape(pat), text)):
                start, end = ch_group.span()
                context = text[max(0, start - 30): end + 30]
                if any(ok in context for ok in WHITESPACE_OK_CONTEXTS):
                    continue
                hits.append((pat, context))
        else:
            for m in re.finditer(pat, text, flags=re.IGNORECASE):
                start, end = m.span()
                context = text[max(0, start - 30): end + 30]
                if any(ok in context for ok in WHITESPACE_OK_CONTEXTS):
                    continue
                hits.append((pat, context))
    return hits

SUPPORTED_LANGUAGES = sorted(LANGUAGE_MARKERS.keys())

def is_supported_language(language):
    """Return True if ``language`` has a curated marker word-list.
    callers should use this to detect "source language is not
    in the curated 11 supported list" so they can warn loudly rather
    than silently skip the remnant scan. The skill works on documents
    in any source language, but only the 11 listed have automatic
    untranslated-remnant detection."""
    if not language:
        return False
    return language.lower() in LANGUAGE_MARKERS

# === SKILL FILE COMPLETE ===
