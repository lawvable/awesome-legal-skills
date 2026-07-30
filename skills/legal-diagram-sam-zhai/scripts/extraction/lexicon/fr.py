"""French (FR) LexiconBundle: all language-bearing patterns for French documents.

Twin of en.py: same constant names, same section order, same frame names and
base confidences, so the two files read side by side.  Patterns match accented
text as written (no NFD stripping here; transliteration is a later task's
concern for node IDs only).

Name classes follow the W3 spec: ``[A-ZÀ-ÖØ-Þ]`` for the leading capital
(covers À É Î Ô Û etc.) and ``[\\w'’À-ÿ.&\\- ]`` for the body.

Circular-import note: same constraint as en.py -- fr.py must NOT import from
``..utils`` (utils.py imports from the lexicon package).
"""
from __future__ import annotations

import re
from typing import Optional

from .base import LexiconBundle


# ---------------------------------------------------------------------------
# sentence splitting  (same language-neutral boundary as EN)
# ---------------------------------------------------------------------------
_SENTENCE_SPLIT = re.compile(r"(?<=[.;!?])\s+")

# ---------------------------------------------------------------------------
# abbreviation guards (FR list per W3 spec; the guard MECHANISM lives in
# utils._guard_split).  "c." guards both citation chapters ("RLRQ c. X-1")
# and case captions ("Tremblay c. Daigle").
# ---------------------------------------------------------------------------
_ABBREVIATION_GUARDS_FR: tuple[str, ...] = (
    "art.",
    "al.",
    "par.",
    "no",
    "M.",
    "Mme",
    "Me",
    "c.",
)


# ---------------------------------------------------------------------------
# date regex: ISO dates and French long-form dates ("1er juin 2026",
# "le 2 juin 2026" -- the article is not part of the match).
# ---------------------------------------------------------------------------
_MONTHS_FR = (
    "janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|"
    "septembre|octobre|novembre|décembre|decembre"
)
_DATE_RE = re.compile(
    r"\b(?:\d{4}-\d{2}-\d{2}|"
    r"(?:1er|\d{1,2})\s+(?:" + _MONTHS_FR + r")\s+\d{4})\b",
    re.I,
)

_MONTH_NUMBERS_FR = {
    "janvier": 1,
    "février": 2,
    "fevrier": 2,
    "mars": 3,
    "avril": 4,
    "mai": 5,
    "juin": 6,
    "juillet": 7,
    "août": 8,
    "aout": 8,
    "septembre": 9,
    "octobre": 10,
    "novembre": 11,
    "décembre": 12,
    "decembre": 12,
}

# ---------------------------------------------------------------------------
# legal action verbs (FR equivalents within the EN field's frame: infinitive,
# third-person present, and past participle of the core action verbs)
# ---------------------------------------------------------------------------
_LEGAL_ACTION_VERBS = re.compile(
    r"\b(livrer|livre|fournir|fournit|fourni|remettre|remet|remis|"
    r"mettre\s+à\s+(?:la\s+)?disposition|soumettre|soumet|soumis|"
    r"déposer|dépose|déposé|envoyer|envoie|envoyé|transmettre|transmet|transmis|"
    r"aviser|avise|avisé|notifier|notifie|notifié|payer|paie|payé|"
    r"verser|verse|versé|rembourser|rembourse|remboursé|financer|finance|financé|"
    r"virer|vire|viré|transférer|transfère|transféré|"
    r"maintenir|maintient|maintenu|conserver|conserve|conservé|"
    r"préserver|préserve|préservé|obtenir|obtient|obtenu|"
    r"exécuter|exécute|exécuté|respecter|respecte|respecté|se\s+conformer|conformer|"
    r"faire\s+en\s+sorte|veiller\s+à|s['’]assurer\s+que|"
    r"approuver|approuve|approuvé|consentir|consent|consenti|"
    r"renoncer|renonce|renoncé|résilier|résilie|résilié|"
    r"remédier|remédie|remédié|corriger|corrige|corrigé)\b",
    re.I,
)

# ---------------------------------------------------------------------------
# money regex: Canadian-French formats with trailing currency symbol --
# "1 234 567,89 $" (space / U+00A0 / U+202F thousands separators, comma
# decimals) and "1,5 M$" (millions shorthand).  The numeric body is a shared
# source string, reused by the W3.3 amount parser below.
# ---------------------------------------------------------------------------
_THOUSANDS_SEP_CLASS = "[   ]"  # space / U+00A0 / U+202F
_AMOUNT_BODY = r"\d{1,3}(?:" + _THOUSANDS_SEP_CLASS + r"\d{3})*(?:,\d+)?"
_MONEY_RE = re.compile(_AMOUNT_BODY + r"\s?M?\$")

# ---------------------------------------------------------------------------
# deadline frame table (FR twins of the EN frames; same names and bases)
# ---------------------------------------------------------------------------
_DEADLINE_FRAMES: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("hard_deadline", re.compile(r"\b(au\s+plus\s+tard\s+(?:le|à)|au\s+moins\s+\d+\s+jours?\s+(?:ouvrables\s+)?avant|d['’]ici\s+le|avant\s+le\s+(?:\d{4}-\d{2}-\d{2}|(?:1er|\d{1,2})\s+[a-zà-ÿ]+\s+\d{4}))\b", re.I), 0.64),
    ("relative_deadline", re.compile(r"\b(dans\s+les?\s+\d+\s+(?:jours?\s+(?:ouvrables\s+)?|mois\s+|semaines?\s+)(?:suivant|après|de|suivant\s+la\s+(?:date\s+de\s+)?clôture|après\s+la\s+clôture)|promptement\s+après|dès\s+que\s+(?:possible|raisonnablement\s+possible)\s+après)\b", re.I), 0.58),
    ("pre_closing_deadline", re.compile(r"\b(avant\s+la\s+clôture|avant\s+la\s+date\s+de\s+clôture|à\s+la\s+clôture\s+ou\s+avant)\b", re.I), 0.62),
    ("post_closing_deadline", re.compile(r"\b(après\s+la\s+clôture|après\s+la\s+date\s+de\s+clôture|suivant\s+la\s+clôture|suivant\s+la\s+date\s+de\s+clôture|postérieurement\s+à\s+la\s+clôture)\b", re.I), 0.62),
    ("notice_period", re.compile(r"\b(?:moyennant\s+un\s+)?préavis\s+(?:écrit\s+)?de\s+\d+\s+jours?\b", re.I), 0.66),
    ("cure_period", re.compile(r"\b(délai\s+de\s+remédiation|omet\s+de\s+remédier\s+dans|défaut\s+de\s+remédier\s+dans|corrigée?\s+dans\s+un\s+délai\s+de)\b", re.I), 0.66),
)

# ---------------------------------------------------------------------------
# obligation frame table (FR twins; same frame names, order, and bases)
# ---------------------------------------------------------------------------
_OBLIGATION_PATTERNS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("negative_obligation", re.compile(r"\b(ne\s+(?:doit|doivent|devra|devront|peut|peuvent)\s+pas|s['’]engage(?:nt)?\s+à\s+ne\s+pas|il\s+est\s+interdit\s+de|s['’]abstien(?:t|nent)\s+de|s['’]abstenir\s+de|aucune\s+partie\s+ne\s+(?:doit|peut))\b", re.I), 0.78),
    ("best_efforts_duty", re.compile(r"\b(efforts\s+commercialement\s+raisonnables|meilleurs\s+efforts|efforts\s+raisonnables|de\s+bonne\s+foi)\b", re.I), 0.76),
    ("procurement_duty", re.compile(r"\b(fai(?:t|re|ra)\s+en\s+sorte\s+que|veille(?:nt|ra)?\s+à\s+ce\s+que|s['’]assure(?:nt)?\s+que)\b", re.I), 0.80),
    ("continuing_duty", re.compile(r"\b(continue(?:nt|ra)?\s+(?:à|de)|maintien(?:t|nent)|conserve(?:nt)?|préserve(?:nt)?|ne\s+permet(?:tent)?\s+pas)\b", re.I), 0.68),
    ("positive_obligation", re.compile(r"\b(doit|doivent|devra|devront|s['’]engage(?:nt)?\s+à|est\s+tenue?\s+de|sont\s+tenue?s\s+de|il\s+incombe\s+à|a\s+l['’]obligation\s+de|est\s+responsable\s+de|est\s+obligée?\s+de)\b", re.I), 0.70),
)

# Prohibition patterns: same extraction discipline as EN -- the negative
# frames from _OBLIGATION_PATTERNS, exposed as a separate table.
# Index 0 = "negative_obligation"; update this slice if _OBLIGATION_PATTERNS order changes.
_PROHIBITION_PATTERNS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    _OBLIGATION_PATTERNS[0],  # negative_obligation
)

# ---------------------------------------------------------------------------
# rep/warranty anti-signal frame table ("déclare et garantit" family,
# excluded from obligations, mirroring the EN rep/warranty discipline)
# ---------------------------------------------------------------------------
_REP_WARRANTY_ANTI_SIGNALS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("qualifier_signal", re.compile(r"\b(déclare(?:nt)?\s+et\s+garanti(?:t|ssent)|déclare(?:nt)?|atteste(?:nt)?|véridiques?\s+et\s+exactes?|à\s+tous\s+(?:les\s+)?égards\s+importants|à\s+la\s+connaissance\s+de|sauf\s+divulgation|énoncée?s?\s+à\s+l['’]annexe)\b", re.I), 0.65),
)

# ---------------------------------------------------------------------------
# occurrence verbs (past participles of FR procedural/factual verbs:
# "a déposé", "a rendu", "a signifié", "a conclu", "est survenu", "a entendu")
# ---------------------------------------------------------------------------
_OCCURRENCE_VERBS = re.compile(
    r"\b("
    r"entendue?|déposée?|rendue?|signifiée?|conclue?|survenue?|"
    r"publiée?|décidée?|rejetée?|accueillie?|accordée?|refusée?|"
    r"datée?|signée?|exécutée?|intentée?|introduite?|eu\s+lieu|"
    r"prononcée?|condamnée?|acquittée?|enregistrée?|constituée?|fusionnée?|"
    r"avisée?|approuvée?|clôturée?|entrée?\s+en\s+vigueur"
    r")\b",
    re.I,
)

# ---------------------------------------------------------------------------
# caption patterns ("Tremblay c. Daigle": FR captions use "c.", never "v.")
# ---------------------------------------------------------------------------
_CAPTION_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"([A-ZÀ-ÖØ-Þ][\w'’À-ÿ.& \-]*?)"
        r"\s+c\.\s+"
        r"([A-ZÀ-ÖØ-Þ][\w'’À-ÿ.& \-]*?[\wÀ-ÿ]\.?)"
        r"(?=\s+[a-zà-ÿ]|\s*,|\s*et\s+al|\s*$)",
        re.MULTILINE,
    ),
)

# corporate suffix patterns (Québec / French corporate forms; trailing dots
# optional so the boundary backtracks like the EN twin)
_CORPORATE_SUFFIXES: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b([A-ZÀ-ÖØ-Þ][\w'’À-ÿ.&, \-]+?\s+(?:Ltée|ltée|[Ii]nc\.?|S\.E\.N\.C\.?(?:R\.L\.?)?|s\.r\.l\.?|S\.A\.R\.L\.?|S\.A\.?|S\.E\.C\.?|Cie))\b"),
)

# defined party marker patterns («...», ci-après désigné(e), ci-après la «...»)
_DEFINED_PARTY_MARKERS: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"(?P<name>[A-ZÀ-ÖØ-Þ][\w'’À-ÿ.&, \-]+?)\s*"
        r"(?:,\s*(?:une?|la|le)\s+[^()«»]{2,80})?\s*"
        r"\(\s*ci-après\s+(?:désignée?\s+)?(?:la\s+|le\s+|les\s+|l['’]\s*)?"
        r"«\s*(?P<role>[^»]{1,40}?)\s*»\s*\)",
        re.I,
    ),
    re.compile(
        r"(?P<name>[A-ZÀ-ÖØ-Þ][\w'’À-ÿ.&, \-]+?),?\s+"
        r"ci-après\s+(?:désignée?\s+)?(?:la\s+|le\s+|les\s+|l['’]\s*)?"
        r"«\s*(?P<role>[^»]{1,40}?)\s*»",
        re.I,
    ),
)

# ---------------------------------------------------------------------------
# heuristic NER pass (W4.2): one-capitalized-token pattern + role words
# titlecase_token_re uses the same name classes as the FR caption pattern
# (leading [A-ZÀ-ÖØ-Þ], body [\w'’À-ÿ.&\-]) so accented tokens ("Société",
# "Générale", "Tremblay") match.  The harvester chains 2+ tokens.
# ---------------------------------------------------------------------------
_TITLECASE_TOKEN_RE = re.compile(r"[A-ZÀ-ÖØ-Þ][\w'’À-ÿ.&\-]*")

# Role words that corroborate a freeform mention as a party reference (FR
# twins of the EN list).  Lowercased; matched case-insensitively.
# Québec judgments routinely use the feminine forms ("la défenderesse"), which
# the masculine stems do not substring-match, so both genders are listed.
_PARTY_ROLE_WORDS: tuple[str, ...] = (
    "demandeur",
    "demanderesse",
    "défendeur",
    "défenderesse",
    "vendeur",
    "venderesse",
    "acheteur",
    "acheteuse",
    "employé",
)

# ---------------------------------------------------------------------------
# citation patterns
# Index contract: [0] neutral_citation, [1] case_citation, [2] statutory_ref,
# [3] rule_ref (same order as EN).
# ---------------------------------------------------------------------------
_CITATION_PATTERNS: tuple[re.Pattern[str], ...] = (
    # neutral citation ("[2026] CSC 12", "2026 QCCA 100") and RCS reporter
    # citations ("[1989] 2 RCS 530")
    re.compile(
        r"(?:\[(?:19|20)\d{2}\]|\b(?:19|20)\d{2})\s+"
        r"(?:CSC|CAF|CF|CCI|QCCA|QCCS|QCCQ|QCTDP|QCTAT|NBCA|ONCA)\s+\d+\b"
        r"|\[(?:19|20)\d{2}\]\s+(?:\d+\s+)?R\.?C\.?S\.?\s+\d+\b"
    ),
    # case citation ("X c. Y, YYYY")
    re.compile(
        r"\b([A-ZÀ-ÖØ-Þ][\w'’À-ÿ.& \-]+?)\s+c\.\s+([A-ZÀ-ÖØ-Þ][\w'’À-ÿ.& \-]+?)"
        r"(?=[,\d]|$|\s+\d|\s*\.)"
        r"(?=.{0,30}[\[(]?(?:19|20)\d{2})",
        re.MULTILINE | re.DOTALL,
    ),
    # statutory reference ("art. 1457 C.c.Q.", "RLRQ c. X-1", "L.R.C. (1985), ch. C-46")
    re.compile(
        r"\b(?:article|art\.)\s*\d+(?:\.\d+)*(?:\s*\(\d+\))?(?:\s*\([a-z]\))?(?:\s+C\.c\.Q\.?)?"
        r"|\bRLRQ,?\s+c\.\s+[A-Z][A-Za-z0-9.\-]*"
        r"|\bL\.R\.C\.\s*\(\d{4}\),?\s*ch\.\s*[A-Z0-9.\-]+"
    ),
    # rule / article reference
    re.compile(r"\b(Règle|Article)\s+\d+\b"),
)

# ---------------------------------------------------------------------------
# notice patterns (avis écrit, signification, mise en demeure)
# ---------------------------------------------------------------------------
_NOTICE_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b(aviser|avise(?:nt|ra)?|donner\s+(?:un\s+)?avis|avis\s+écrit|mise\s+en\s+demeure|signification|signifier|signifié(?:e)?|l['’]avis\s+(?:doit|sera)\s+(?:être\s+)?(?:envoyé|transmis)|à\s+l['’]attention\s+de|avec\s+copie\s+à|courriel|courrier\s+recommandé|messagerie\s+de\s+nuit|remise\s+en\s+mains?\s+propres|réputée?\s+(?:reçue?|donnée?)|prend\s+effet\s+(?:dès|à)\s+(?:la\s+)?réception)\b", re.I),
)

# ---------------------------------------------------------------------------
# condition frame table (sous réserve de, à condition que, pourvu que,
# advenant que; same frame names, order, and bases as EN)
# ---------------------------------------------------------------------------
_CONDITION_PATTERNS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("condition_precedent", re.compile(r"\b(condition\s+préalable|sous\s+réserve\s+de\s+la\s+(?:réalisation|satisfaction)\s+de|sous\s+réserve\s+de\s+la\s+renonciation\s+à|tant\s+que\s+.{0,40}n['’]a\s+pas|à\s+condition\s+que|pourvu\s+que)\b", re.I), 0.66),
    ("trigger_condition", re.compile(r"\b(si|advenant\s+que|dans\s+le\s+cas\s+où|en\s+cas\s+de|dès\s+(?:que|réception)|lorsque|lorsqu['’]|sur\s+réception\s+de|une\s+fois\s+que|où)\b", re.I), 0.42),
    ("exception_carveout", re.compile(r"\b(sauf\s+(?:que|si|disposition\s+contraire)|à\s+l['’]exception\s+de|à\s+l['’]exclusion\s+de|autre\s+que|excluant|nonobstant|malgré|pour\s+éviter\s+toute\s+ambiguïté|rien\s+dans\s+les\s+présentes)\b", re.I), 0.48),
    ("dependency", re.compile(r"\b(conditionnée?\s+(?:à|par)|dépend(?:ent)?\s+de|subordonnée?\s+à|sous\s+réserve\s+de)\b", re.I), 0.44),
)

# ---------------------------------------------------------------------------
# consent/discretion frame table (consentement préalable écrit,
# "ne peut ... sans le consentement"; same frame names, order, and bases)
# ---------------------------------------------------------------------------
_CONSENT_PATTERNS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("consent_given", re.compile(r"\b(consent(?:ent)?\s+(?:expressément\s+)?à|consent\s+par\s+les\s+présentes\s+à|a\s+consenti\s+à|donne(?:nt)?\s+(?:son|leur)\s+consentement\s+à)\b", re.I), 0.60),
    ("consent_required", re.compile(r"\b(exige\s+le\s+consentement|avec\s+le\s+consentement\s+préalable\s+écrit\s+de|consentement\s+préalable\s+écrit|sans\s+le\s+consentement|ne\s+peu(?:t|vent)\s+.{0,60}sans\s+le\s+consentement|sous\s+réserve\s+de\s+l['’]approbation)\b", re.I), 0.64),
    ("approval_right", re.compile(r"\bapprobation\s+ne\s+(?:peut|doit|sera|pourra)\s+(?:pas\s+)?être\s+(?:refusée|retenue|retardée|assortie\s+de\s+conditions)(?:\s+de\s+manière\s+déraisonnable|\s+déraisonnablement)?\b", re.I), 0.72),
    ("sole_discretion", re.compile(r"\b(à\s+sa\s+(?:seule|entière)\s+discrétion|discrétion\s+absolue|discrétion\s+raisonnable)\b", re.I), 0.58),
    ("veto_right", re.compile(r"\b(peu(?:t|vent)\s+bloquer|peu(?:t|vent)\s+s['’]opposer|droit\s+de\s+s['’]opposer|ne\s+procède(?:nt)?\s+pas\s+sans)\b", re.I), 0.66),
    ("waiver", re.compile(r"\b(peu(?:t|vent)\s+renoncer|renonciation\s+à|renoncée?\s+par|le\s+défaut\s+d['’]exercer\s+.{0,40}ne\s+constitue\s+pas\s+une\s+renonciation)\b", re.I), 0.64),
)

# ---------------------------------------------------------------------------
# control patterns (contrôle, mesure de protection, chiffrement, vérification)
# Index contract: [0] gate pattern, [1] evidence-signal pattern.
# ---------------------------------------------------------------------------
_CONTROL_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b(vérifiée?s?\s+par|attestée?s?\s+par|contrôlée?s?\s+par|sous\s+le\s+contrôle\s+de|auditée?s?\s+par|vérification\s+(?:par|de)|examinée?s?\s+par|approuvée?s?\s+par|mesure\s+de\s+protection|chiffrement|contrôle)\b", re.I),
    re.compile(r"\b(vérifiée?s?|attestée?s?|auditée?s?|vérification|chiffrement)\b", re.I),
)

# ---------------------------------------------------------------------------
# ownership patterns (détient N % de, filiale en propriété exclusive,
# actionnaire).  pct stays integer/dot-decimal so float() in ownership.py
# never receives a comma-decimal string.
# ---------------------------------------------------------------------------
_OWNERSHIP_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"(?P<parent>[A-ZÀ-ÖØ-Þ][\w'’À-ÿ.& ]+?)\s+(?:détient|possède|est\s+(?:le\s+)?propriétaire\s+(?:inscrit\s+)?de)\s+(?P<pct>\d+(?:\.\d+)?)?\s*%?\s*(?:de\s+la\s+|de\s+|du\s+|des\s+|d['’])?(?P<child>[A-ZÀ-ÖØ-Þ][\w'’À-ÿ.& ]+)"),
    re.compile(r"\b(contrôle|contrôlée?\s+par|sous\s+contrôle\s+commun|filiale\s+en\s+propriété\s+exclusive|actionnaires?|pouvoir\s+de\s+diriger|autorisée?\s+à|a\s+le\s+pouvoir\s+de|pouvoir\s+et\s+autorité|dûment\s+autorisée?|ne\s+peu(?:t|vent)\s+(?:pas\s+)?céder|transférer|nantir|grever|aliéner|approbation\s+du\s+conseil|approbation\s+des\s+actionnaires|consentement\s+des\s+membres)\b", re.I),
)

# ---------------------------------------------------------------------------
# payment verbs (verse, paie, rembourse, à titre de contrepartie)
# ---------------------------------------------------------------------------
_PAYMENT_VERBS = re.compile(
    r"\b(paie(?:nt|ra)?|payer|payée?|verse(?:nt|ra)?|verser|versée?|rembourse(?:nt|ra)?|rembourser|remboursée?|finance(?:nt|ra)?|financer|financée?|dépose(?:nt|ra)?|déposer|déposée?|remet(?:tent|tra)?|remettre|remise?|vire(?:nt|ra)?|virer|virée?|transfère(?:nt)?|transférer|transférée?|payable|exigible|à\s+titre\s+de\s+contrepartie)\b",
    re.I,
)

# ---------------------------------------------------------------------------
# remedy patterns (dommages-intérêts, injonction, résiliation, résolution,
# exécution en nature)
# ---------------------------------------------------------------------------
_REMEDY_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b(violation|manquement|défaut|cas\s+de\s+défaut|inexécution|non-conformité|remédier|remédiation|omet\s+de\s+remédier|peu(?:t|vent)\s+résilier|droit\s+de\s+résilier|résiliation|résolution|résiliation\s+automatique|exécution\s+en\s+nature|injonction|mesure\s+injonctive|dommages-intérêts|indemnisation|compensation|survi(?:t|vent)\s+à|demeure(?:nt)?\s+en\s+vigueur)\b", re.I),
)

# ---------------------------------------------------------------------------
# document patterns (pièce, annexe, convention, entente, jugement, requête)
# ---------------------------------------------------------------------------
_DOCUMENT_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b(livre(?:r|nt)?|fourni(?:r|t|ssent)?|remet(?:tre|tent)?|met(?:tre)?\s+à\s+(?:la\s+)?disposition|soumet(?:tre|tent)?|dépose(?:r|nt)?|transmet(?:tre|tent)?|pièce|annexe|convention|entente|jugement|requête|certificat\s+de\s+(?:dirigeant|conformité)|certificat\s+du\s+secrétaire|exemplaire\s+signé|livres\s+et\s+registres|droit\s+d['’]inspection)\b", re.I),
)


# ---------------------------------------------------------------------------
# date normalisation + amount parsing (W3.3 bundle callables)
#
# Design decision (W3.3): normalisation is bundle-carried so the EN/FR
# asymmetry lives in the lexicon layer.  FR converts dates to ISO 8601 and
# parses locale money formats at harvest time; EN keeps as-written dates and
# defers money parsing to helpers.money.amount_number (see en.py twins).
# ---------------------------------------------------------------------------

# Numeric body of an FR money amount: the shared _AMOUNT_BODY source
# (defined beside _MONEY_RE above) compiled standalone for parsing.
_AMOUNT_BODY_RE = re.compile(_AMOUNT_BODY)
# Thousands separators stripped before float() conversion.
_THOUSANDS_SEP_RE = re.compile(_THOUSANDS_SEP_CLASS)
# Millions shorthand ("1,5 M$" = 1 500 000 $).
_MILLIONS_RE = re.compile(r"M\s?\$")


def _normalize_date_fr(text: str) -> Optional[str]:
    """FR canonical date surface = ISO 8601 (YYYY-MM-DD).

    Returns the ISO rendering of the first _DATE_RE match in *text* ("1er
    juin 2026" -> "2026-06-01"; ISO matches pass through), or None when no
    date is present.
    """
    m = _DATE_RE.search(text)
    if not m:
        return None
    raw = m.group(0)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        return raw
    day_str, month_name, year_str = raw.split()
    day = 1 if day_str.lower() == "1er" else int(day_str)
    month = _MONTH_NUMBERS_FR[month_name.lower()]
    return f"{int(year_str):04d}-{month:02d}-{day:02d}"


def _parse_amount_fr(text: Optional[str]) -> Optional[float]:
    """Parse an FR money string to a float at harvest time.

    Strips space/U+00A0/U+202F thousands separators, converts the comma
    decimal to a dot, and applies the M$ millions multiplier.  Returns None
    when *text* carries no numeric amount.
    """
    if not text:
        return None
    m = _AMOUNT_BODY_RE.search(text)
    if not m:
        return None
    digits = _THOUSANDS_SEP_RE.sub("", m.group(0)).replace(",", ".")
    amount = float(digits)
    if _MILLIONS_RE.search(text):
        amount *= 1_000_000
    return amount


# ---------------------------------------------------------------------------
# Bundle factory
# ---------------------------------------------------------------------------

def _build_fr_bundle() -> LexiconBundle:
    return LexiconBundle(
        date_re=_DATE_RE,
        sentence_split_re=_SENTENCE_SPLIT,
        abbreviation_guards=_ABBREVIATION_GUARDS_FR,
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
        normalize_date=_normalize_date_fr,
        parse_amount=_parse_amount_fr,
    )


# Module-level singleton; constructed once on first import.
_FR_BUNDLE: LexiconBundle = _build_fr_bundle()
