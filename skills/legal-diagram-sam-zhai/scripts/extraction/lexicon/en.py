"""English (EN) LexiconBundle: all language-bearing patterns for English documents.

Every regex string and pattern table is reproduced verbatim from the sources
listed beside each constant.

Circular-import note: utils.py imports SENTENCE_SPLIT from the lexicon package
(``from .lexicon import SENTENCE_SPLIT``), so en.py must NOT import from
``..utils``.  Instead, the SENTENCE_SPLIT pattern and ABBREVIATION_GUARDS_EN
tuple are defined here directly (verbatim from their original locations).
W2.4 / W3 finishes the relocation by removing the copies in utils.py and
pointing all callers to this module.
"""
from __future__ import annotations

import re
from typing import Optional

from .base import LexiconBundle


# ---------------------------------------------------------------------------
# sentence splitting  (verbatim from extraction/lexicon.py SENTENCE_SPLIT)
# W2.4 / W3 finishes relocation; utils.py copy removed then.
# ---------------------------------------------------------------------------
_SENTENCE_SPLIT = re.compile(r"(?<=[.;!?])\s+")

# ---------------------------------------------------------------------------
# abbreviation guards  (verbatim from extraction/utils.py ABBREVIATION_GUARDS_EN)
# W2.4 / W3 finishes relocation; utils.py copy removed then.
# ---------------------------------------------------------------------------
_ABBREVIATION_GUARDS_EN: tuple[str, ...] = (
    "Inc.",
    "Corp.",
    "Ltd.",
    "No.",
    "U.S.",
    "e.g.",
    "i.e.",
)


# ---------------------------------------------------------------------------
# date regex  (verbatim from extraction/lexicon.py DATE_RE)
# ---------------------------------------------------------------------------
_DATE_RE = re.compile(
    r"\b(?:\d{4}-\d{2}-\d{2}|"
    r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t)?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4}|"
    r"\d{1,2}\s+(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t)?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4})\b",
    re.I,
)

# ---------------------------------------------------------------------------
# legal action verbs  (verbatim from extraction/lexicon.py LEGAL_ACTION_VERBS)
# ---------------------------------------------------------------------------
_LEGAL_ACTION_VERBS = re.compile(
    r"\b(deliver|provide|furnish|make available|submit|file|send|notify|pay|reimburse|fund|deposit|remit|wire|transfer|"
    r"maintain|keep|preserve|retain|obtain|perform|comply|execute|cause|procure|ensure|approve|consent|waive|terminate|cure|remedy)\b",
    re.I,
)

# ---------------------------------------------------------------------------
# money regex  (verbatim from extraction/lexicon.py MONEY_RE)
# ---------------------------------------------------------------------------
_MONEY_RE = re.compile(r"\$\s?[\d,]+(?:\.\d{2})?|\bUSD\s?[\d,]+(?:\.\d{2})?\b", re.I)

# ---------------------------------------------------------------------------
# deadline frame table  (verbatim from extraction/harvesters/deadlines.py)
# ---------------------------------------------------------------------------
_DEADLINE_FRAMES: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("hard_deadline", re.compile(r"\b(no\s+later\s+than|on\s+or\s+before|not\s+later\s+than|at\s+least\s+\d+\s+(?:business\s+)?days?\s+before|by\s+(?:\d{4}-\d{2}-\d{2}|[A-Z][a-z]+\s+\d{1,2},?\s+\d{4}|\d{1,2}\s+[A-Z][a-z]+\s+\d{4}|(?:the\s+)?Closing(?:\s+Date)?))\b", re.I), 0.64),
    ("relative_deadline", re.compile(
        r"\b(within\s+\d+\s+(?:business\s+|calendar\s+)?days?\s+(?:after|of|from)"
        r"|\b(?:shall\s+have|have|has)\s+\d+\s+(?:business\s+|calendar\s+)?days?\s+(?:after|to|from|following)"
        r"|promptly\s+after|as\s+soon\s+as\s+practicable\s+after)\b", re.I), 0.58),
    ("pre_closing_deadline", re.compile(r"\b(prior\s+to\s+Closing|before\s+the\s+Closing\s+Date|at\s+or\s+before\s+Closing)\b", re.I), 0.62),
    # W6 T4 Item B: "the following closing deliveries" is a list-leader sentence,
    # not a post-closing temporal deadline.  Exclude 'the following <noun>' pattern
    # by requiring that 'following Closing' is NOT preceded by 'the' article.
    # post-Closing and after/from-and-after forms are unambiguous; left unchanged.
    ("post_closing_deadline", re.compile(r"\b(?<!the\s)(following\s+Closing)\b|\b(after\s+the\s+Closing\s+Date|post-Closing|from\s+and\s+after\s+Closing)\b", re.I), 0.62),
    ("notice_period", re.compile(r"\b(?:upon\s+)?\d+\s+(?:business\s+)?days?[']?\s+(?:prior\s+)?written\s+notice\b", re.I), 0.66),
    ("cure_period", re.compile(r"\b(cure\s+period|fails?\s+to\s+cure\s+within|remedied\s+within)\b", re.I), 0.66),
)

# ---------------------------------------------------------------------------
# obligation frame table  (verbatim from extraction/harvesters/obligations.py)
# ---------------------------------------------------------------------------
_OBLIGATION_PATTERNS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("negative_obligation", re.compile(r"\b(shall\s+not|will\s+not|agrees?\s+not\s+to|is\s+prohibited\s+from|may\s+not|must\s+not|no\s+party\s+shall)\b", re.I), 0.78),
    ("best_efforts_duty", re.compile(r"\b(use\s+commercially\s+reasonable\s+efforts|reasonable\s+best\s+efforts|best\s+efforts|good\s+faith\s+efforts)\b", re.I), 0.76),
    ("procurement_duty", re.compile(r"\b(shall\s+cause|shall\s+procure\s+that|shall\s+ensure\s+that|cause\s+its\s+affiliates\s+to)\b", re.I), 0.80),
    ("continuing_duty", re.compile(r"\b(continue\s+to|maintain|keep|preserve|retain|not\s+permit)\b", re.I), 0.68),
    ("positive_obligation", re.compile(r"\b(shall|must|agrees?\s+to|undertakes\s+to|covenants\s+to|will|(?:is|are)\s+obligated\s+to|(?:is|are)\s+responsible\s+for|(?:is|are)\s+required\s+to)\b", re.I), 0.70),
)

# Prohibition patterns: negative-obligation frames extracted as a separate
# table for callers that need to distinguish prohibitions from duties.
# The prohibition frames are the negative_obligation entries from _OBLIGATION_PATTERNS.
# Index 0 = "negative_obligation"; update this slice if _OBLIGATION_PATTERNS order changes.
_PROHIBITION_PATTERNS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    _OBLIGATION_PATTERNS[0],  # negative_obligation
)

# ---------------------------------------------------------------------------
# rep/warranty anti-signal frame table  (verbatim from extraction/harvesters/reps.py
# -- the qualifier_signal check is the only frame; base confidence is not used
# by reps.py directly but is stored here for structural uniformity)
# ---------------------------------------------------------------------------
_REP_WARRANTY_ANTI_SIGNALS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("qualifier_signal", re.compile(r"\b(true\s+and\s+correct|material\s+respects|knowledge\s+of|except\s+as\s+disclosed|set\s+forth\s+on\s+Schedule)\b", re.I), 0.65),
)

# ---------------------------------------------------------------------------
# occurrence verbs  (verbatim from extraction/harvesters/events.py _OCCURRENCE_VERBS)
# ---------------------------------------------------------------------------
_OCCURRENCE_VERBS = re.compile(
    r"\b("
    r"heard|filed|issued|entered\s+into|rendered|released|decided|dismissed|granted|allowed|denied|"
    r"dated|executed|signed|served|commenced|convened|adjourned|occurred|took\s+place|closed|"
    r"pronounced|sentenced|convicted|acquitted|registered|incorporated|amalgamated|notified|approved"
    r")\b",
    re.I,
)

# ---------------------------------------------------------------------------
# caption patterns  (verbatim from extraction/harvesters/parties.py)
# ---------------------------------------------------------------------------
_CAPTION_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"([A-Z][A-Za-z0-9.&' ]*?)"
        r"\s+(?:vs?\.?|vs)\s+"
        r"([A-Z][A-Za-z0-9.&' ]*?[A-Za-z0-9]\.?)"
        r"(?=\s+[a-z]|\s*,|\s*et\s+al|\s*$)",
        re.MULTILINE,
    ),
)

# corporate suffix patterns  (verbatim from extraction/harvesters/parties.py
# and extraction/utils.py extract_entity_like_names)
_CORPORATE_SUFFIXES: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b([A-Z][A-Za-z0-9&.,' -]+?\s+(?:Inc\.?|LLC|Ltd\.?|Corp(?:oration)?\.?|Company|LP|LLP|PLC|GmbH))\b"),
)

# defined party marker patterns  (verbatim from extraction/harvesters/parties.py)
_DEFINED_PARTY_MARKERS: tuple[re.Pattern[str], ...] = (
    re.compile(r"(?P<name>[A-Z][A-Za-z0-9&.,' -]+?\s+(?:Inc\.?|LLC|Ltd\.?|Corp(?:oration)?\.?|Company|LP|LLP|PLC|GmbH))\s*(?:,\s*(?:a|an)\s+[^()]{2,80})?\s*\(\s*(?:the\s+)?['\"](?P<role>[A-Za-z][A-Za-z ]{1,40})['\"]\s*\)", re.I),
    re.compile(r"(?P<name>[A-Z][A-Za-z0-9&.,' -]+?)\s+(?:is|are)\s+referred\s+to\s+herein\s+as\s+['\"](?P<role>[A-Za-z][A-Za-z ]{1,40})['\"]", re.I),
)

# ---------------------------------------------------------------------------
# heuristic NER pass (W4.2): one-capitalized-token pattern + role words
# titlecase_token_re matches a single capitalized token; the harvester chains
# 2+ of them into a candidate mention.  EN class is ASCII-only.
# ---------------------------------------------------------------------------
_TITLECASE_TOKEN_RE = re.compile(r"[A-Z][A-Za-z0-9.&'-]*")

# Role words that corroborate a freeform mention as a party reference.
_PARTY_ROLE_WORDS: tuple[str, ...] = (
    "plaintiff",
    "defendant",
    "vendor",
    "purchaser",
    "employee",
)

# ---------------------------------------------------------------------------
# citation patterns  (verbatim from extraction/harvesters/citations.py)
# ---------------------------------------------------------------------------
_CITATION_PATTERNS: tuple[re.Pattern[str], ...] = (
    # neutral citation
    re.compile(
        r"\b(19|20)\d{2}\s+"
        r"(SCC|FCA|FC|FCTD|TCC|ONSC|ONCA|ONCJ|BCSC|BCCA|ABQB|ABCA|QCCA|QCCS|SKQB|SKCA|MBQB|MBCA|NSCA|NSSC|NLCA|NBCA|PESC)"
        r"\s+\d+\b"
    ),
    # case citation ("X v. Y, YYYY")
    re.compile(
        r"\b([A-Z][A-Za-z0-9.&' -]+?)\s+v\.?\s+([A-Z][A-Za-z0-9.&' -]+?)"
        r"(?=[,\d]|$|\s+\d|\s*\.)"
        r"(?=.{0,30}[\[(]?(?:19|20)\d{2})",
        re.MULTILINE | re.DOTALL,
    ),
    # statutory section reference
    re.compile(
        r"\b(?:section|s\.)\s*\d+(?:\(\d+\))?(?:\([a-z]\))?(?:\(\d+\))?"
    ),
    # rule / article reference
    re.compile(r"\b(Rule|Article)\s+\d+\b"),
)

# ---------------------------------------------------------------------------
# notice patterns  (verbatim from extraction/harvesters/notices.py)
# ---------------------------------------------------------------------------
_NOTICE_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b(notify|give\s+notice|written\s+notice|notice\s+shall\s+be\s+sent|to\s+the\s+attention\s+of|with\s+a\s+copy\s+to|cc\b|email|overnight\s+courier|certified\s+mail|personal\s+delivery|deemed\s+(?:received|given)|effective\s+upon\s+receipt)\b", re.I),
)

# ---------------------------------------------------------------------------
# condition frame table  (verbatim from extraction/harvesters/conditions.py)
# ---------------------------------------------------------------------------
_CONDITION_PATTERNS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("condition_precedent", re.compile(r"\b(condition\s+precedent|subject\s+to\s+the\s+satisfaction\s+of|subject\s+to\s+waiver\s+of|unless\s+and\s+until|provided\s+that)\b", re.I), 0.66),
    ("trigger_condition", re.compile(r"\b(if|in\s+the\s+event\s+that|upon|following|after\s+receipt\s+of|once|where)\b", re.I), 0.42),
    ("exception_carveout", re.compile(r"\b(except\s+that|except\s+as|other\s+than|excluding|provided\s+however|notwithstanding|for\s+the\s+avoidance\s+of\s+doubt|nothing\s+herein\s+shall)\b", re.I), 0.48),
    ("dependency", re.compile(r"\b(conditioned\s+upon|dependent\s+on|contingent\s+upon|subject\s+to)\b", re.I), 0.44),
)

# ---------------------------------------------------------------------------
# consent/discretion frame table  (verbatim from extraction/harvesters/consent.py _PATTERNS)
# ---------------------------------------------------------------------------
_CONSENT_PATTERNS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("consent_given", re.compile(r"\b(consents?\s+to|expressly\s+consents?|hereby\s+consents?|consented\s+to)\b", re.I), 0.60),
    ("consent_required", re.compile(r"\b(requires?\s+consent|with\s+the\s+prior\s+written\s+consent\s+of|without\s+consent|subject\s+to\s+approval)\b", re.I), 0.64),
    ("approval_right", re.compile(r"\bapproval\s+shall\s+not\s+be\s+unreasonably\s+(?:withheld|conditioned|delayed)\b", re.I), 0.72),
    ("sole_discretion", re.compile(r"\b(in\s+its\s+sole\s+discretion|absolute\s+discretion|reasonable\s+discretion)\b", re.I), 0.58),
    ("veto_right", re.compile(r"\b(may\s+block|may\s+object|right\s+to\s+object|shall\s+not\s+proceed\s+without)\b", re.I), 0.66),
    ("waiver", re.compile(r"\b(may\s+waive|waiver\s+of|waived\s+by|failure\s+to\s+enforce\s+shall\s+not\s+constitute\s+waiver)\b", re.I), 0.64),
)

# ---------------------------------------------------------------------------
# control patterns  (verbatim from extraction/harvesters/controls.py)
# ---------------------------------------------------------------------------
_CONTROL_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b(verified\s+by|evidenced\s+by|control(?:led)?\s+by|audit(?:ed)?\s+(?:by|via)|reviewed\s+by|approved\s+by|sign-?off)\b", re.I),
    re.compile(r"\b(verified\s+by|evidenced\s+by|audit(?:ed)?)\b", re.I),
)

# ---------------------------------------------------------------------------
# ownership patterns  (verbatim from extraction/harvesters/ownership.py)
# ---------------------------------------------------------------------------
_OWNERSHIP_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"(?P<parent>[A-Z][A-Za-z .&]+?)\s+(?:owns?|holds?|beneficially\s+owns|is\s+the\s+record\s+owner\s+of)\s+(?P<pct>\d+(?:\.\d+)?)?%?\s*(?:of\s+)?(?P<child>[A-Z][A-Za-z .&]+)"),
    re.compile(r"\b(controls|controlled\s+by|under\s+common\s+control|power\s+to\s+direct|authorized\s+to|has\s+authority\s+to|power\s+and\s+authority|duly\s+authorized|may\s+not\s+assign|transfer|pledge|encumber|dispose\s+of|board\s+approval|manager\s+approval|shareholder\s+approval|consent\s+of\s+members)\b", re.I),
)

# ---------------------------------------------------------------------------
# payment verbs  (verbatim from extraction/utils.py has_payment_verb)
# ---------------------------------------------------------------------------
_PAYMENT_VERBS = re.compile(
    r"\b(pay|reimburse|fund|deposit|remit|wire|transfer|payable|due\s+and\s+payable)\b",
    re.I,
)

# ---------------------------------------------------------------------------
# remedy patterns  (verbatim from extraction/harvesters/remedies.py)
# ---------------------------------------------------------------------------
_REMEDY_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b(breach|default|event\s+of\s+default|failure\s+to\s+perform|non-compliance|cure|remedy|fails?\s+to\s+cure|may\s+terminate|right\s+to\s+terminate|termination\s+event|automatic\s+termination|specific\s+performance|injunctive\s+relief|damages|indemnification|setoff|survive\s+(?:Closing|termination)|remain\s+in\s+effect)\b", re.I),
)

# ---------------------------------------------------------------------------
# document patterns  (verbatim from extraction/harvesters/documents.py)
# ---------------------------------------------------------------------------
_DOCUMENT_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"\b(deliver|provide|furnish|make\s+available|submit|file|send"
        r"|officer's\s+certificate|secretary's\s+certificate|bring-down\s+certificate"
        r"|compliance\s+certificate|executed\s+counterpart|books\s+and\s+records"
        r"|inspection\s+rights"
        # W6 T4 Item D: schedule/exhibit/annex references in rep-warranty and
        # closing conditions should trigger document harvesting.
        r"|Schedule\s+No\.?\s*\d+|Schedule\s+[A-Z0-9]+|Exhibit\s+[A-Z0-9]+"
        r"|Annexe?\s+\d+|set\s+forth\s+on\s+Schedule|disclosed\s+on\s+Schedule)\b",
        re.I,
    ),
)


# ---------------------------------------------------------------------------
# date normalisation + amount parsing (W3.3 bundle callables)
#
# Design decision (W3.3): normalisation is bundle-carried so the EN/FR
# asymmetry lives in the lexicon layer.  helpers/ stay lexicon-free and keep
# their EN-format parsers; harvesters consult the bundle first and fall back
# to the helpers, which is a byte-identical no-op for EN.
# ---------------------------------------------------------------------------

def _normalize_date_en(text: str) -> Optional[str]:
    """EN canonical date surface = the matched text verbatim.

    EN goldens lock date_or_timing values to as-written dates, so the EN
    bundle never rewrites them; it returns the first _DATE_RE match unchanged
    (None when no date is present).  FR converts to ISO 8601 in fr.py.
    """
    m = _DATE_RE.search(text)
    return m.group(0) if m else None


def _parse_amount_en(text: Optional[str]) -> Optional[float]:
    """EN defers amount parsing to the pipeline default.

    EN amounts are parsed downstream at materialize time by
    helpers.money.amount_number, and the EN candidate payload must not gain a
    harvest-time "amount" key (goldens lock the payload shape), so the EN
    bundle always returns None here.
    """
    return None


# ---------------------------------------------------------------------------
# Bundle factory
# ---------------------------------------------------------------------------

def _build_en_bundle() -> LexiconBundle:
    return LexiconBundle(
        date_re=_DATE_RE,
        sentence_split_re=_SENTENCE_SPLIT,
        abbreviation_guards=_ABBREVIATION_GUARDS_EN,
        legal_action_verbs=_LEGAL_ACTION_VERBS,
        money_re=_MONEY_RE,
        deadline_frames=_DEADLINE_FRAMES,
        obligation_patterns=_OBLIGATION_PATTERNS,
        prohibition_patterns=_PROHIBITION_PATTERNS,
        rep_warranty_anti_signals=_REP_WARRANTY_ANTI_SIGNALS,
        occurrence_verbs=_OCCURRENCE_VERBS,
        caption_patterns=_CAPTION_PATTERNS,
        corporate_suffixes=_CORPORATE_SUFFIXES,
        defined_party_markers=_DEFINED_PARTY_MARKERS,
        titlecase_token_re=_TITLECASE_TOKEN_RE,
        party_role_words=_PARTY_ROLE_WORDS,
        citation_patterns=_CITATION_PATTERNS,
        notice_patterns=_NOTICE_PATTERNS,
        condition_patterns=_CONDITION_PATTERNS,
        consent_patterns=_CONSENT_PATTERNS,
        control_patterns=_CONTROL_PATTERNS,
        ownership_patterns=_OWNERSHIP_PATTERNS,
        payment_verbs=_PAYMENT_VERBS,
        remedy_patterns=_REMEDY_PATTERNS,
        document_patterns=_DOCUMENT_PATTERNS,
        normalize_date=_normalize_date_en,
        parse_amount=_parse_amount_en,
    )


# Module-level singleton; constructed once on first import.
_EN_BUNDLE: LexiconBundle = _build_en_bundle()
