"""Comprehensive quality check for translated legal documents.

Checks (all must pass zero for delivery):
 1. Missing spaces between adjacent w:t elements
 2. Definition boundary spacing ("Xmeans" etc.)
 3. Double punctuation (::, .., ,,)
 4. Terminology/lexicon violations
 5. Standalone "Financing" (not "Project Financing")
 6. Duplicate words (within and across elements)
 7. Missing/broken quotes on defined terms
 8. Italian remnants (words and full paragraphs)
 9. Title/header issues
10. Word order issues ("X existing and future")
11. UK spelling violations
12. Article vs Clause for internal cross-references
13. "that precedes"/"that follows" remnants (including plural "that precede")
14. Truncation detection (sentences cut mid-thought)
15. Formatting: bold on definitions, spurious italic, line breaks in definitions
16. Numbering: level jumps, orphaned sub-items
17. Definition alphabetical order verification

Usage:
    python quality_check.py <document.xml> [--verbose] [--with-source <paragraphs.json>]

The --with-source flag enables truncation detection by comparing English length
against the Italian source stored in paragraphs.json.
"""
import sys
import os
import json
import re
from lxml import etree

# Import the shared per-language marker module from the same scripts/ folder.
_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)
from source_language_markers import (  # noqa: E402
    scan_remnants,
    detect_language,
    SUPPORTED_LANGUAGES,
)

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

# ======================================================================
# CONFIGURATION
# ======================================================================

TERM_VIOLATIONS = [
    'Financing Agreement', 'Financing Bank', 'Business Register', 'Lien Assets',
    'Partial Invalidity', 'cash line', 'Cash line', 'revolving line', 'credit lines',
    'credit line', 'Domicile Election', 'election of domicile', 'Election of Domicile',
    'which intervenes as', 'who intervenes as', 'intervenes as',
    'by universal or singular title',
    'Deed of Establishment', 'Deed of Creation', 'deed of creation',
    'Deed of Constitution of Pledge', 'deed of constitution',
    'plants and works existing and future',
    'Description of Financing',
    'stipulated',
]

US_SPELLINGS = [
    (r'\bauthorize\b', 'authorise'), (r'\bauthorized\b', 'authorised'),
    (r'\bAuthorization\b', 'Authorisation'), (r'\bAUTHORIZATION\b', 'AUTHORISATION'),
    (r'\bauthorization\b', 'authorisation'),
    (r'\brecognize\b', 'recognise'), (r'\brecognized\b', 'recognised'),
    (r'\borganize\b', 'organise'), (r'\borganized\b', 'organised'),
    (r'\borganization\b', 'organisation'),
    (r'\bfavor\b', 'favour'), (r'\bhonor\b', 'honour'), (r'\bcenter\b', 'centre'),
    (r'\bdefense\b', 'defence'), (r'\bfulfill\b', 'fulfil'),
    (r'\bfulfillment\b', 'fulfilment'),
    (r'\bjudgment\b', 'judgement'), (r'\bjudgments\b', 'judgements'),
    (r'\bJudgment\b', 'Judgement'),
    (r'\backnowledgment\b', 'acknowledgement'),
    (r'\butilize\b', 'utilise'), (r'\butilized\b', 'utilised'),
    (r'\bcanceled\b', 'cancelled'), (r'\banalyze\b', 'analyse'),
]

LEGISLATION_KW = [
    'Civil Code', 'Legislative Decree', 'D.P.R.', 'Law No.', 'Law no.',
    'Royal Decree', 'Ministerial Decree', 'Regulation (EU)', 'Banking Act',
    'decreto legislativo', 'Codice Civile', 'D.Lgs.', 'D.L.',
    'T.U.B.', 'T.U.F.', 'Decree No.', 'Decree no.',
    'Consolidated Banking', 'Consolidated Financial', 'Presidential Decree',
]

# Italian words that should not appear (excluding OK-listed contexts)
ITALIAN_WORDS = [
    r'\bdella\b', r'\bdelle\b', r'\bdello\b', r'\bdegli\b',
    r'\bnella\b', r'\bnelle\b', r'\bnello\b', r'\bnegli\b', r'\bnel\b',
    r'\balla\b', r'\balle\b', r'\ballo\b', r'\bagli\b',
    r'\bsulla\b', r'\bsulle\b', r'\bsullo\b', r'\bsugli\b',
    r'\bche\b', r'\bogni\b', r'\bsuo\b', r'\bsua\b',
    r'\bciascun[oa]?\b', r'\bpresente\b', r'\bsecondo\b',
    r'\bai sensi\b', r'\bfermo restando\b',
    r'\bcontratto\b', r'\bsociet[aà]\b', r'\bgaranzia\b',
    r'\bcessione\b', r'\bipoteca\b', r'\bpegno\b',
    r'\bcrediti\b', r'\bconto\b', r'\bbanca\b',
    r'\bcinquanta per cento\b', r'\bcinquanta\b',
    r'\bprecedente\b', r'\bsuccessivo\b',
    r'\bParti\b', r'\bParte\b',
]

# Contexts that are OK even though they contain Italian-looking words
# NOTE: this constant is currently unused (live whitelist lives in
# source_language_markers.WHITESPACE_OK_CONTEXTS). Kept for reference;
# specific bank/institution names removed to avoid signalling.
OK_CONTEXTS = [
    'S.p.A.', 'S.r.l.', 'per cent', 'per annum', 'inter alia', 'pari passu',
    'pro rata', 'bona fide', 'Gazzetta Ufficiale',
    'D.P.R.', 'Codice Civile',
    'Decreto Legislativo', 'decreto legislativo',
    'Agenzia delle Entrate', 'Conservatoria', 'Camera di Commercio',
    'Comune di', 'Provincia di', 'Tribunale di', 'delle Imprese',
    'della Repubblica', 'del Registro', 'Registro delle Imprese',
    'Notaio', 'notaio', 'Repertorio', 'Raccolta',
    'Contratto di Finanziamento',  # sometimes kept in Italian as proper noun
    'the Parties', 'the Party', 'Counterparty', 'Counterparties',
    'Third Party', 'third party',
]

# Dangling endings that suggest truncation
TRUNCATION_ENDINGS = [
    r'\bthe\s*$', r'\bof\s*$', r'\band\s*$', r'\bin\s*$', r'\bto\s*$',
    r'\bfor\s*$', r'\bwith\s*$', r'\bby\s*$', r'\bfrom\s*$', r'\bor\s*$',
    r'\bas\s*$', r'\bat\s*$', r'\bon\s*$', r'\bthat\s*$', r'\bwhich\s*$',
    r'\bunder\s*$', r'\bpursuant\s*$', r'\bwithout\s*$',
    r'\bany\s*$', r'\beach\s*$', r'\bsuch\s*$', r'\bthis\s*$',
    r'\bshall\s*$', r'\bwill\s*$', r'\bmay\s*$',
    r'\ba\s*$', r'\ban\s*$',
]

# List-connective whitelist: "; and", ", and", "; or", ", or" are legal-English
# list connectives, NOT truncation. Short-circuits the truncation flag without
# weakening detection of genuine truncations (which lack the ;/, prefix).
LIST_CONNECTOR_RE = re.compile(r'(?:[;,]\s*)(?:and|or)\s*$', re.IGNORECASE)

# ======================================================================
# CHECK FUNCTIONS
# ======================================================================

def check_spacing(root, verbose):
    """Check 1: Missing spaces between adjacent w:t elements."""
    issues = []
    for p in root.iter(f'{{{W}}}p'):
        t_elems = [(t, t.text) for t in p.iter(f'{{{W}}}t') if t.text]
        for i in range(1, len(t_elems)):
            prev = t_elems[i-1][1]
            curr = t_elems[i][1]
            if not prev or not curr:
                continue
            pc, cc = prev[-1], curr[0]
            bad = False
            if pc.isalpha() and cc.isalpha(): bad = True
            elif pc.isalpha() and cc == '(': bad = True
            elif pc == ')' and cc.isalpha(): bad = True
            elif pc == ';' and cc.isalpha(): bad = True
            elif pc == ',' and cc.isalpha(): bad = True
            elif pc == ':' and cc.isalpha(): bad = True
            elif pc.isdigit() and cc.isupper(): bad = True
            elif pc == '.' and cc.isupper():
                if not re.search(r'\b[A-Z]\.$', prev) and not any(
                    prev.endswith(s) for s in ['No.', 'no.', 'etc.', 'S.p.A.', 'S.r.l.', '..', 'seq.']):
                    bad = True
            if bad:
                issues.append(f"'{prev[-20:]}|{curr[:20]}'")
    return issues

def check_definition_boundaries(root, verbose):
    """Check 2: Missing space before definition verbs (Xmeans, Xshall mean, etc.)."""
    issues = []
    for p in root.iter(f'{{{W}}}p'):
        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))
        for pat in [r'[A-Z\u201d"\)]means\b', r'[A-Z\u201d"\)]shall mean\b',
                    r'[A-Z\u201d"\)]has the meaning\b', r'[A-Z\u201d"\)]indicates\b']:
            for m in re.finditer(pat, full):
                issues.append(f"'{full[max(0,m.start()-10):m.end()+10]}'")
    return issues

def check_double_punctuation(root, verbose):
    """Check 3: Double colons, periods, commas, semicolons."""
    issues = []
    for t in root.iter(f'{{{W}}}t'):
        if t.text:
            if '::' in t.text: issues.append(f"'::' in '{t.text[:50]}'")
            if re.search(r'\.\.(?!\.)', t.text): issues.append(f"'..' in '{t.text[:50]}'")
            if ',,' in t.text: issues.append(f"',,' in '{t.text[:50]}'")
            if ';;' in t.text: issues.append(f"';;' in '{t.text[:50]}'")
    return issues

def check_terminology(root, verbose):
    """Check 4: Terminology/lexicon violations."""
    issues = []
    for t in root.iter(f'{{{W}}}t'):
        if t.text:
            for term in TERM_VIOLATIONS:
                if term in t.text:
                    issues.append(f"'{term}' in '{t.text[:60]}'")
    return issues

def check_standalone_financing(root, verbose):
    """Check 5: Standalone 'Financing' not part of 'Project Financing'."""
    issues = []
    for t in root.iter(f'{{{W}}}t'):
        if t.text and 'Financing' in t.text:
            cleaned = t.text.replace('Project Financing', '')
            if 'Financing' in cleaned:
                issues.append(f"Standalone 'Financing' in '{t.text[:60]}'")
    return issues

def check_duplicates(root, verbose):
    """Check 6: Duplicate words within and across elements."""
    issues = []
    # Within elements
    for t in root.iter(f'{{{W}}}t'):
        if t.text:
            for m in re.finditer(r'\b(\w{3,})\s+\1\b', t.text, re.IGNORECASE):
                if m.group(1).lower() not in ('that', 'had', 'very'):
                    issues.append(f"'{m.group(1)} {m.group(1)}' in '{t.text[:50]}'")
    # Across boundaries
    for p in root.iter(f'{{{W}}}p'):
        t_elems = [(t, t.text) for t in p.iter(f'{{{W}}}t') if t.text and t.text.strip()]
        for i in range(1, len(t_elems)):
            pw = t_elems[i-1][1].split()
            cw = t_elems[i][1].split()
            if pw and cw:
                p_clean = re.sub(r'[,;:."\'\)\]]+$', '', pw[-1])
                c_clean = re.sub(r'^["\'\(\[]+', '', cw[0])
                if (p_clean and c_clean and p_clean.lower() == c_clean.lower()
                        and len(p_clean) > 2 and p_clean.isalpha()):
                    issues.append(f"'{p_clean}' at boundary")
    return issues

def check_quotes(root, verbose):
    """Check 7: Missing/broken quotes on defined terms."""
    issues = []
    OPEN_Q = '\u201c'
    CLOSE_Q = '\u201d'
    for p in root.iter(f'{{{W}}}p'):
        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))
        if not any(v in full for v in ['means', 'shall mean', 'has the meaning', 'indicates']):
            continue
        # Check for unbalanced smart quotes
        opens = full.count(OPEN_Q) + full.count('\u201e')
        closes = full.count(CLOSE_Q)
        if opens > 0 and opens != closes:
            issues.append(f"Unbalanced quotes ({opens} open, {closes} close): '{full[:80]}'")
        # Check for "Term means" without closing quote
        for m in re.finditer(r'[\u201c"]\s*([^"\u201d\u201c]{2,60}?)\s+(means|shall mean|has the meaning|indicates)\b', full):
            term = m.group(1)
            if not term.rstrip().endswith(CLOSE_Q) and not term.rstrip().endswith('"'):
                issues.append(f"Missing close quote: '{full[m.start():m.end()+5]}'")
    return issues

def check_source_remnants(root, verbose, source_language=None):
    """Check 8: untranslated source-language words and paragraphs.

    Uses the shared `source_language_markers` module so the scanner is specific
    to the actual source language (Dutch, German, French, etc.) — not hardcoded
    to Italian. If `source_language` is None, the check is skipped silently.

    Scans BOTH <w:t> (accept-all view) AND <w:delText> (reject-all / markup
    view). The delText pass catches source-language remnants that live inside
    a tracked-change deletion — including the phantom <w:ins><w:del>SRC</w:del>
    </w:ins> shape that renders as empty under accept-all but is still visible
    with "Show Markup" on. The two views are reported under distinct labels so
    a reviewer knows where to look.
    """
    issues = []
    if not source_language:
        return issues
    lang = source_language.lower()
    if lang not in SUPPORTED_LANGUAGES:
        # Languages outside SUPPORTED_LANGUAGES skip remnant detection;
        # translator fidelity is the primary safeguard.
        return issues

    label = lang.capitalize()
    extra_filter_italian = (lang == 'italian')

    def _filtered_issues(full_text, view_tag):
        out = []
        for _marker, context in scan_remnants(full_text, lang):
            ctx_stripped = context.strip()
            # Italian-specific legacy filters kept for backwards compatibility.
            if extra_filter_italian:
                if re.search(r'\bcome\b|\bCome\b', ctx_stripped):
                    continue
                if re.search(r'non-\w', ctx_stripped):
                    continue
                if any(x in ctx_stripped for x in ('per cent', 'per annum', 'per se')):
                    continue
            out.append(f"{label} remnant ({view_tag}) in '{ctx_stripped[:100]}'")
        return out

    for p in root.iter(f'{{{W}}}p'):
        full_t = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))
        full_del = ''.join(dt.text or '' for dt in p.iter(f'{{{W}}}delText'))

        if full_t.strip() and len(full_t.split()) >= 3:
            issues.extend(_filtered_issues(full_t, 'accept-all'))
            # Full source-language paragraphs (high density of source function words)
            dense_hits = len(scan_remnants(full_t, lang))
            if dense_hits >= 3:
                issues.append(f"FULL {label.upper()} PARAGRAPH (accept-all): '{full_t[:100]}'")

        if full_del.strip() and len(full_del.split()) >= 1:
            # delText is almost always a short strike-through fragment, so the
            # 3-word minimum used for accept-all text would filter out most
            # legitimate remnants. Require only one word.
            issues.extend(_filtered_issues(full_del, 'reject-all / markup'))
            dense_hits_del = len(scan_remnants(full_del, lang))
            if dense_hits_del >= 3:
                issues.append(f"FULL {label.upper()} PARAGRAPH (reject-all / markup): '{full_del[:100]}'")

    return issues

def check_italian_remnants(root, verbose):
    """Legacy name kept for backward compatibility with callers that pass
    no source_language. Forwards to check_source_remnants with lang=None,
    which is a no-op. Prefer check_source_remnants(root, verbose, lang)."""
    return check_source_remnants(root, verbose, None)

def check_titles(root, verbose):
    """Check 9: Title/header issues."""
    issues = []
    bad_titles = [
        'Deed of Establishment of Special Lien', 'DEED OF ESTABLISHMENT OF SPECIAL LIEN',
        'Deed of Creation of Mortgage', 'DEED OF CREATION OF MORTGAGE',
        'Deed of Constitution of Pledge', 'DEED OF CONSTITUTION OF PLEDGE',
        'deed of creation of the Pledge', 'deed of creation of the pledge',
        'deed of constitution of the pledge',
    ]
    for t in root.iter(f'{{{W}}}t'):
        if t.text:
            for bt in bad_titles:
                if bt in t.text:
                    issues.append(f"'{bt}' in '{t.text[:60]}'")
    return issues

def check_word_order(root, verbose):
    """Check 10: Word order issues (adjective placement)."""
    issues = []
    pattern = re.compile(r'\b(\w+)\s+existing\s+and\s+future\b', re.IGNORECASE)
    for t in root.iter(f'{{{W}}}t'):
        if t.text:
            for m in pattern.finditer(t.text):
                noun = m.group(1).lower()
                if noun not in ('and', 'the', 'all', 'any', 'of'):
                    issues.append(f"'{m.group()}' should be 'existing and future {m.group(1)}'")
    return issues

def check_us_spelling(root, verbose):
    """Check 11a: US spelling violations (used under UK variant — the default)."""
    issues = []
    for t in root.iter(f'{{{W}}}t'):
        if t.text:
            for pattern, uk in US_SPELLINGS:
                m = re.search(pattern, t.text)
                if m:
                    issues.append(f"'{m.group()}' -> '{uk}'")
    return issues

# Inverse spelling table used ONLY when the caller passes --variant us,
# which itself should only happen when the user's original prompt explicitly
# asked for US English. UK is the hardcoded default variant of this skill.
UK_SPELLINGS_INV = [
    (r'\bauthorise\b', 'authorize'), (r'\bauthorised\b', 'authorized'),
    (r'\bAuthorisation\b', 'Authorization'), (r'\bAUTHORISATION\b', 'AUTHORIZATION'),
    (r'\bauthorisation\b', 'authorization'),
    (r'\brecognise\b', 'recognize'), (r'\brecognised\b', 'recognized'),
    (r'\borganise\b', 'organize'), (r'\borganised\b', 'organized'),
    (r'\borganisation\b', 'organization'),
    (r'\bfavour\b', 'favor'), (r'\bhonour\b', 'honor'), (r'\bcentre\b', 'center'),
    (r'\bdefence\b', 'defense'), (r'\bfulfil\b', 'fulfill'),
    (r'\bfulfilment\b', 'fulfillment'),
    (r'\bjudgement\b', 'judgment'), (r'\bjudgements\b', 'judgments'),
    (r'\bJudgement\b', 'Judgment'),
    (r'\backnowledgement\b', 'acknowledgment'),
    (r'\butilise\b', 'utilize'), (r'\butilised\b', 'utilized'),
    (r'\bcancelled\b', 'canceled'), (r'\banalyse\b', 'analyze'),
]

def check_uk_spelling(root, verbose):
    """Check 11b: UK spelling violations (used under US variant only)."""
    issues = []
    for t in root.iter(f'{{{W}}}t'):
        if t.text:
            for pattern, us in UK_SPELLINGS_INV:
                m = re.search(pattern, t.text)
                if m:
                    issues.append(f"'{m.group()}' -> '{us}'")
    return issues

def check_article_refs(root, verbose):
    """Check 12: Article for internal cross-refs (should be Clause)."""
    issues = []
    for p in root.iter(f'{{{W}}}p'):
        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))
        is_leg = any(kw in full for kw in LEGISLATION_KW)
        if not is_leg:
            for m in re.finditer(r'\bArticles?\s+\d{1,2}(?:\.\d+)*', full):
                issues.append(f"'{m.group()}' in '{full[:70]}'")
    return issues

def check_that_precedes(root, verbose):
    """Check 13: 'that precedes/precede/follows/follow' remnants."""
    issues = []
    for p in root.iter(f'{{{W}}}p'):
        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))
        # "that precede" / "that precedes"
        for m in re.finditer(r'\bthat precede[sd]?\b', full, re.IGNORECASE):
            issues.append(f"'{m.group()}' in '{full[:70]}'")
        # "that follow" / "that follows" (but not "that follows from" which is valid English)
        for m in re.finditer(r'\bthat follows?\b', full, re.IGNORECASE):
            if 'that follows from' not in full[m.start():m.start()+25].lower():
                issues.append(f"'{m.group()}' in '{full[:70]}'")
    return issues

def check_truncation(root, verbose, source_data=None):
    """Check 14: Truncated translations (sentences cut off mid-thought).

    Two methods:
    A) If source_data (paragraphs.json) is provided, compare English vs Italian length.
       Flag if English is less than 40% the length of Italian (suggests truncation).
    B) Always check for dangling endings (sentences ending with articles/prepositions).
    """
    issues = []

    # Method A: Length comparison with source
    if source_data:
        all_p = list(root.iter(f'{{{W}}}p'))
        for entry in source_data:
            idx = entry.get('idx', -1)
            src_text = entry.get('text', '')
            if not src_text.strip() or len(src_text) < 20:
                continue
            if idx < 0 or idx >= len(all_p):
                continue

            p = all_p[idx]
            en_text = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))

            if not en_text.strip():
                if len(src_text.strip()) > 30:
                    issues.append(f"EMPTY translation for non-empty source (idx={idx}): '{src_text[:60]}'")
                continue

            # Length ratio check (English is typically 0.8-1.2x Italian length for legal text)
            ratio = len(en_text) / len(src_text) if len(src_text) > 0 else 1
            if ratio < 0.4 and len(src_text) > 50:
                issues.append(f"TRUNCATED? ratio={ratio:.2f} (idx={idx}): EN='{en_text[:50]}' IT='{src_text[:50]}'")

    # Method B: Dangling endings. Skip drafter placeholder tokens
    # (faithful annotations preserved from source, not truncations).
    _PLACEHOLDER_PREFIXES = (
        'PM', '[PM]', 'TBD', '[TBD]', 'TBC', '[TBC]',
        '[...]', '[…]', '[●]', '[•]',
    )
    for p in root.iter(f'{{{W}}}p'):
        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))
        if not full.strip() or len(full) < 20:
            continue

        # Skip paragraphs that are drafter placeholder notes.
        stripped = full.strip()
        if any(stripped.startswith(pfx) for pfx in _PLACEHOLDER_PREFIXES):
            continue
        # Skip paragraphs that begin with a run of underscores (e.g. "____").
        if stripped and stripped[0] == '_' and stripped.lstrip('_') != stripped:
            continue

        # Rev34 list-connective whitelist (skip "; and", ", and", "; or", ", or").
        if LIST_CONNECTOR_RE.search(full):
            continue
        # Check if paragraph ends with a dangling preposition/article/auxiliary
        for pat in TRUNCATION_ENDINGS:
            if re.search(pat, full):
                # Don't flag if it's clearly a heading or short label
                if len(full.split()) < 5:
                    continue
                issues.append(f"Dangling ending '{full[-20:].strip()}' in '{full[:60]}'")
                break

    return issues

def check_formatting(root, verbose):
    """Check 15: Formatting issues (bold on definitions, spurious italic)."""
    issues = []

    for p in root.iter(f'{{{W}}}p'):
        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))

        # Check definition paragraphs have bold on the defined term
        if any(v in full for v in ['means', 'shall mean', 'has the meaning']) and \
           ('\u201c' in full or '"' in full):
            has_bold = False
            for r in p.iter(f'{{{W}}}r'):
                rpr = r.find(f'{{{W}}}rPr')
                t = r.find(f'{{{W}}}t')
                if rpr is not None and rpr.find(f'{{{W}}}b') is not None:
                    if t is not None and t.text and len(t.text.strip()) > 2:
                        has_bold = True
                        break
            if not has_bold:
                issues.append(f"No bold term in definition: '{full[:70]}'")

        # Check for line breaks in definition paragraphs (run before heading skip)
        if any(v in full for v in ['means', 'shall mean', 'has the meaning', 'indicates']) and \
           ('\u201c' in full or '"' in full):
            for r in p.iter(f'{{{W}}}r'):
                br = r.find(f'{{{W}}}br')
                if br is not None:
                    issues.append(f"Line break in definition: '{full[:70]}'")
                    break  # One report per paragraph

        # Check for spurious italic on body text — per-run detection
        # Skip headings (all caps + short) for italic check only
        is_heading = full.strip() == full.strip().upper() and len(full.split()) < 10
        if is_heading:
            continue

        # Skip if paragraph-level style sets italic intentionally
        # ST_OnOff falsy set extended to include 'off'.
        _ST_ONOFF_FALSE_QC = {'false', '0', 'off'}

        def _qc_is_off(v):
            return v is not None and v.strip().lower() in _ST_ONOFF_FALSE_QC

        ppr = p.find(f'{{{W}}}pPr')
        p_italic = False
        if ppr is not None:
            p_rpr = ppr.find(f'{{{W}}}rPr')
            if p_rpr is not None:
                i_elem = p_rpr.find(f'{{{W}}}i')
                if i_elem is not None and not _qc_is_off(i_elem.get(f'{{{W}}}val')):
                    p_italic = True

        if not p_italic:
            latin_terms = ['inter alia', 'mutatis mutandis', 'pari passu', 'pro rata',
                           'bona fide', 'de facto', 'de jure', 'prima facie']
            for r in p.iter(f'{{{W}}}r'):
                rpr = r.find(f'{{{W}}}rPr')
                if rpr is None:
                    continue
                i_elem = rpr.find(f'{{{W}}}i')
                if i_elem is None or _qc_is_off(i_elem.get(f'{{{W}}}val')):
                    continue
                t = r.find(f'{{{W}}}t')
                if t is None or not t.text:
                    continue
                text = t.text.strip()
                if not text:
                    continue
                # Allow italic in parentheses (cross-ref headings), Latin terms, numbering labels
                if text.startswith('(') and text.endswith(')'):
                    continue
                if any(lt in text.lower() for lt in latin_terms):
                    continue
                if len(text) <= 5 and re.match(r'^[\d\.\(\)a-z]+$', text):
                    continue
                if len(text.split()) > 2:
                    issues.append(f"Spurious italic run: '{text[:50]}' in para: '{full[:50]}'")

    return issues

def check_numbering(root, verbose):
    """Check 16: Numbering/structure validation.

    Detects:
    - Paragraphs with numId references that point to numbering definitions
      where the sequence appears broken (e.g., level 0 jumps from 1 to 3)
    - Orphaned sub-items (level 1+ without a preceding level 0 parent)
    """
    issues = []

    # Track numbering sequences by numId and ilvl
    # This is a heuristic check — we track the text-based numbering we see
    # and flag obvious gaps
    current_nums = {}  # numId -> last seen ilvl

    for p in root.iter(f'{{{W}}}p'):
        ppr = p.find(f'{{{W}}}pPr')
        if ppr is None:
            continue
        numpr = ppr.find(f'{{{W}}}numPr')
        if numpr is None:
            continue

        numid_elem = numpr.find(f'{{{W}}}numId')
        ilvl_elem = numpr.find(f'{{{W}}}ilvl')
        if numid_elem is None:
            continue

        numid = numid_elem.get(f'{{{W}}}val')
        ilvl = int(ilvl_elem.get(f'{{{W}}}val', '0')) if ilvl_elem is not None else 0

        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))

        if numid not in current_nums:
            current_nums[numid] = ilvl
            # First occurrence at level > 0 is suspicious (orphaned sub-item)
            if ilvl > 1:
                issues.append(f"Numbering starts at level {ilvl} (numId={numid}): '{full[:60]}'")
        else:
            prev = current_nums[numid]
            # Jumping down more than 1 level is suspicious
            if ilvl > prev + 1:
                issues.append(f"Numbering level jump {prev}->{ilvl} (numId={numid}): '{full[:60]}'")
            current_nums[numid] = ilvl

    return issues

def check_definition_order(root, verbose):
    """Check 17: Definitions are in alphabetical order by the English term.

    Groups consecutive definition paragraphs into blocks and checks each block
    independently. A definition paragraph is one containing a quoted term followed
    by "means"/"shall mean"/"has the meaning"/"indicates". A heading or a non-
    definition paragraph breaks the current block — so definitions in separate
    sections (e.g. "Interpretation" vs "Definitions") are checked independently.
    This prevents false positives when a document has definitions in multiple
    sections that are each internally sorted but not globally sorted.
    """
    issues = []

    # Collect consecutive definition blocks
    blocks = []
    current_block = []

    for p in root.iter(f'{{{W}}}p'):
        full = ''.join(t.text or '' for t in p.iter(f'{{{W}}}t'))

        # Check if this is a definition paragraph
        is_def = False
        term = None
        if any(v in full for v in ['means', 'shall mean', 'has the meaning', 'indicates']):
            m = re.search(r'[\u201c"]\s*(.+?)\s*[\u201d"]', full)
            if m:
                is_def = True
                term = m.group(1).strip()

        if is_def:
            current_block.append(term)
        else:
            # Non-definition paragraph breaks the block
            if len(current_block) >= 3:
                blocks.append(list(current_block))
            current_block = []

    # Don't forget the last block
    if len(current_block) >= 3:
        blocks.append(list(current_block))

    # Check each block independently
    for block in blocks:
        sorted_block = sorted(block, key=lambda t: t.lower())
        for i, (actual, expected) in enumerate(zip(block, sorted_block)):
            if actual != expected:
                issues.append(f"Definition out of order: '{actual}' (expected '{expected}' at position {i})")
                if len(issues) >= 5:
                    issues.append(f"... and potentially more.")
                    break

    return issues

# ======================================================================
# AUXILIARY-FILE SCANS # ======================================================================

def _scan_aux_xml_for_remnants(xml_path, source_language, label):
    """Parse an auxiliary OOXML file and run the source-language-remnant
    scan against every `<w:t>` element it contains. Returns a list of
    issue strings, prefixed with ``label`` (e.g. 'numbering.xml',
    'header1.xml')."""
    issues = []
    if not source_language:
        return issues
    lang = source_language.lower()
    if lang not in SUPPORTED_LANGUAGES:
        return issues
    try:
        tree = etree.parse(xml_path)
    except (OSError, etree.XMLSyntaxError):
        return issues
    root = tree.getroot()
    # numbering.xml uses <w:lvlText w:val="..."/> for level format strings.
    # header/footer/comments use <w:t> for text. Cover both.
    label_capped = source_language.capitalize()
    for t_elem in root.iter(f'{{{W}}}t'):
        text = t_elem.text or ''
        if not text.strip():
            continue
        for _marker, context in scan_remnants(text, lang):
            issues.append(
                f"{label_capped} remnant in {label}: '{context.strip()[:100]}'"
            )
    # Also scan w:lvlText for numbering format strings (scanned as plain
    # text — numbering format strings may legitimately reference
    # placeholder tokens like %1, %2 that scan_remnants ignores).
    for lvl_elem in root.iter(f'{{{W}}}lvlText'):
        val = lvl_elem.get(f'{{{W}}}val')
        if not val or not val.strip():
            continue
        for _marker, context in scan_remnants(val, lang):
            issues.append(
                f"{label_capped} remnant in {label} lvlText: "
                f"'{context.strip()[:100]}'"
            )
    return issues

def check_aux_files(aux_dir, source_language, verbose=False):
    """Scan every auxiliary XML part under ``aux_dir`` (typically the
    workdir's ``final/`` directory containing ``word/``) for source-
    language remnants. Returns a dict mapping aux-file basename to the
    list of issue strings.

    Auxiliary files covered:
      * word/numbering.xml
      * word/headerN.xml (all N)
      * word/footerN.xml (all N)
      * word/comments.xml
      * word/footnotes.xml
      * word/endnotes.xml

    The full quality_check rule set runs only on document.xml because
    most rules (italic, line breaks, definition formatting, truncation)
    are paragraph-shape rules that don't apply to numbering format
    strings or comments. This function adds the source-remnant scan to
    auxiliary files so calques and untranslated source-language text in
    headers / footers / numbering / comments are detected before
    repack rather than after."""
    results = {}
    word_dir = os.path.join(aux_dir, 'word')
    if not os.path.isdir(word_dir):
        # Allow callers to pass either the parent of word/ or word/
        # itself.
        if os.path.basename(aux_dir.rstrip(os.sep)) == 'word':
            word_dir = aux_dir
        else:
            return results
    candidates = [
        ('numbering.xml', 'word/numbering.xml'),
        ('comments.xml', 'word/comments.xml'),
        ('footnotes.xml', 'word/footnotes.xml'),
        ('endnotes.xml', 'word/endnotes.xml'),
    ]
    for label, rel in candidates:
        path = os.path.join(word_dir, os.path.basename(rel))
        if os.path.exists(path):
            issues = _scan_aux_xml_for_remnants(path, source_language, label)
            results[label] = issues
    # Headers and footers: pick up any headerN.xml / footerN.xml
    for fname in sorted(os.listdir(word_dir)):
        if (fname.startswith('header') or fname.startswith('footer')) \
                and fname.endswith('.xml'):
            path = os.path.join(word_dir, fname)
            issues = _scan_aux_xml_for_remnants(path, source_language, fname)
            results[fname] = issues
    return results

# ======================================================================
# MAIN
# ======================================================================

def check(xml_path, verbose=False, source_json=None, variant='uk',
          source_language=None, aux_dir=None):
    tree = etree.parse(xml_path)
    root = tree.getroot()

    source_data = None
    if source_json:
        with open(source_json, 'r', encoding='utf-8') as f:
            source_data = json.load(f)

    # Auto-detect source language from paragraphs.json if not provided.
    if not source_language and source_data:
        sample = ' '.join(
            (p.get('text') or '') for p in source_data[:60]
        )
        source_language = detect_language(sample)

    source_lang_label = (source_language or 'source').lower() + '_remnants'

    checks = [
        ('spacing', check_spacing),
        ('definition_boundaries', check_definition_boundaries),
        ('double_punctuation', check_double_punctuation),
        ('terminology', check_terminology),
        ('standalone_financing', check_standalone_financing),
        ('duplicates', check_duplicates),
        ('missing_quotes', check_quotes),
        (source_lang_label, lambda r, v: check_source_remnants(r, v, source_language)),
        ('titles_headers', check_titles),
        ('word_order', check_word_order),
        ('internal_article_refs', check_article_refs),
        ('that_precedes_follows', check_that_precedes),
        ('formatting', check_formatting),
        ('numbering', check_numbering),
        ('definition_order', check_definition_order),
    ]

    # Spelling check is variant-dependent (UK is the hardcoded default).
    if variant == 'us':
        checks.append(('uk_spelling', check_uk_spelling))
    else:
        checks.append(('us_spelling', check_us_spelling))

    results = {}
    total = 0
    for name, fn in checks:
        issues = fn(root, verbose)
        results[name] = issues
        total += len(issues)

    # Truncation check (needs different signature)
    trunc_issues = check_truncation(root, verbose, source_data)
    results['truncation'] = trunc_issues
    total += len(trunc_issues)

    # scan auxiliary XML files for source-language remnants if
    # --aux-dir was supplied. The full quality_check rule set runs only
    # on document.xml; this catches calques and untranslated source-
    # language text in headers/footers/numbering/comments that
    # previously slipped past quality_check entirely.
    aux_results = {}
    if aux_dir:
        aux_results = check_aux_files(aux_dir, source_language, verbose)
        for aux_label, aux_issues in aux_results.items():
            key = f'aux_{aux_label}'
            results[key] = aux_issues
            total += len(aux_issues)

    # Print summary
    print(f"\nQuality Check: {xml_path}")
    print(f"{'='*60}")
    for name, issues in results.items():
        status = 'CLEAN' if not issues else f'{len(issues)} issues'
        print(f"  {name:30s} {status}")
        if verbose and issues:
            for iss in issues[:5]:
                print(f"    -> {iss}")
            if len(issues) > 5:
                print(f"    ... and {len(issues)-5} more")
    print(f"{'='*60}")
    print(f"  {'TOTAL':30s} {total} issues")

    if total == 0:
        print("\n  *** PASSED: Document is ready for delivery ***")
    else:
        print(f"\n  *** FAILED: {total} issues must be resolved ***")

    return results

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(
        description='Quality check for a translated legal document.xml.',
        epilog=(
            "Note: --variant defaults to 'uk'. Only pass --variant us if the "
            "user's original prompt explicitly requested US English.\n"
            "Note: --language overrides auto-detection from paragraphs.json. "
            f"Supported: {', '.join(sorted(SUPPORTED_LANGUAGES))}"
        ),
    )
    ap.add_argument('xml_path', help='Path to the translated document.xml')
    ap.add_argument('--verbose', action='store_true',
                    help='Print the first few issues per check.')
    ap.add_argument('--with-source', dest='source_json', default=None,
                    help='paragraphs.json (enables truncation check by length comparison).')
    ap.add_argument('--variant', choices=('uk', 'us'), default='uk',
                    help='English variant for the spelling check (default: uk).')
    # --language is the canonical flag name across the skill. --source-language
    # is kept as a backward-compatible alias for older scripts and docs.
    ap.add_argument('--language', '--source-language', dest='source_language',
                    default=None,
                    help='Source language (overrides auto-detection from paragraphs.json).')
    ap.add_argument('--aux-dir', dest='aux_dir', default=None,
                    help='Rev12+: directory containing translated auxiliary XML '
                         '(numbering.xml, headerN.xml, footerN.xml, comments.xml, '
                         'footnotes.xml, endnotes.xml). Pass either the parent of '
                         'word/ or word/ itself. Auxiliary files are scanned for '
                         'source-language remnants. Strongly recommended.')
    args = ap.parse_args()

    source_language = args.source_language.lower() if args.source_language else None

    check(args.xml_path, verbose=args.verbose, source_json=args.source_json,
          variant=args.variant, source_language=source_language,
          aux_dir=args.aux_dir)


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
            "  Step 9 is MANDATORY — do not deliver while this script is\n"
            "  truncated. Either re-install or block delivery until\n"
            "  quality_check.py runs cleanly.\n"
            + "=" * 60 + "\n"
        )
        print(msg, file=sys.stderr)
        sys.exit(3)


# Run the integrity check at module-import time so callers (including
# auto-invokers) discover truncation before any work begins.
_check_self_integrity()

# === SKILL FILE COMPLETE ===
