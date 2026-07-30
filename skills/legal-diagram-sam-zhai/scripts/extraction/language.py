"""W3.1 language detection: function-word frequency scoring (pure stdlib, deterministic).

detect_language(text) classifies a span as "en", "fr", or "und" by counting
token hits against two fixed high-frequency function-word marker sets.  The
sets are disjoint by construction; ambiguous tokens that read as words in
both languages (a, on, as, or, but, en, de, plus, son) are deliberately
excluded from both sets, which also keeps English legal phrases such as
"de facto" and "en banc" from scoring as French.

annotate_blocks() runs the block-level pass: raw detection per block, document
dominance by character count, short-block / und inheritance, optional forced
override, and the manifest language_profile payload.  Blocks are duck-typed
(any object with a .text attribute); the effective language is written to
block.lang in place and stays internal to the pipeline.
"""
from __future__ import annotations

import re
from typing import Any, Iterable

# Blocks shorter than this inherit the document-dominant language.
SHORT_BLOCK_CHARS = 80
# Fewer total marker hits than this -> "und".
_MIN_TOTAL_HITS = 3

# Tokens: lowercase letters incl. Latin-1 accents and oe ligature; internal
# hyphens kept so multi-part markers like "ci-après" survive tokenisation.
_TOKEN_RE = re.compile(r"[a-zà-öø-ÿœ]+(?:-[a-zà-öø-ÿœ]+)*")

EN_MARKERS = frozenset({
    "the", "of", "to", "and", "that", "this", "these", "those", "with",
    "from", "by", "not", "is", "are", "was", "were", "be", "been", "has",
    "have", "had", "shall", "will", "may", "must", "would", "should",
    "hereby", "herein", "thereof", "hereunder", "whereas", "upon", "under",
    "between", "any", "each", "such", "which", "including",
})

FR_MARKERS = frozenset({
    "le", "la", "les", "des", "du", "au", "aux", "une", "et", "ou", "à",
    "que", "qui", "ne", "pas", "est", "sont", "être", "été", "doit",
    "doivent", "peut", "peuvent", "sera", "seront", "dans", "par", "pour",
    "sur", "avec", "sans", "sous", "entre", "dont", "cette", "ces", "leurs",
    "tout", "toute", "tous", "toutes", "conformément", "ci-après",
    "lorsque", "selon", "notamment", "afin", "ainsi",
})


def detect_language(text: str) -> tuple[str, float]:
    """Classify text as ("en" | "fr" | "und", confidence).

    Score = marker-token hit count per set over the tokenised lowercase text.
    Fewer than 3 total hits, or a zero margin (tie), -> ("und", 0.0).
    Confidence = winner hits / total hits.
    """
    tokens = _TOKEN_RE.findall((text or "").lower())
    en_hits = sum(1 for t in tokens if t in EN_MARKERS)
    fr_hits = sum(1 for t in tokens if t in FR_MARKERS)
    total = en_hits + fr_hits
    if total < _MIN_TOTAL_HITS or en_hits == fr_hits:
        return ("und", 0.0)
    winner, hits = ("en", en_hits) if en_hits > fr_hits else ("fr", fr_hits)
    return (winner, hits / total)


def annotate_blocks(blocks: Iterable[Any], override: str | None = None) -> dict[str, Any]:
    """Assign an effective .lang to every block in place; return language_profile.

    Raw detection runs per block (always, even when forced, for reporting).
    Dominant = majority by character count over classified (en/fr) blocks;
    tie or no classified block -> "en".  Effective lang: the override when
    forced to en/fr; else the dominant for "und" blocks and blocks under
    SHORT_BLOCK_CHARS characters; else the raw detection.

    language_profile: {"dominant", "override", "blocks" (raw detector counts,
    so "und" can appear), "char_share" (share over classified blocks, 2 dp)}.
    """
    block_list = list(blocks)
    raw_langs: list[str] = []
    counts = {"en": 0, "fr": 0, "und": 0}
    chars = {"en": 0, "fr": 0}
    for block in block_list:
        text = str(getattr(block, "text", "") or "")
        lang, _ = detect_language(text)
        raw_langs.append(lang)
        counts[lang] += 1
        if lang in chars:
            chars[lang] += len(text)

    dominant = "fr" if chars["fr"] > chars["en"] else "en"
    total_chars = chars["en"] + chars["fr"]
    if total_chars:
        char_share = {
            "en": round(chars["en"] / total_chars, 2),
            "fr": round(chars["fr"] / total_chars, 2),
        }
    else:
        char_share = {"en": 0.0, "fr": 0.0}

    forced = override if override in ("en", "fr") else None
    for block, raw in zip(block_list, raw_langs):
        text = str(getattr(block, "text", "") or "")
        if forced:
            block.lang = forced
        elif raw == "und" or len(text) < SHORT_BLOCK_CHARS:
            block.lang = dominant
        else:
            block.lang = raw

    return {
        "dominant": dominant,
        "override": forced,
        "blocks": counts,
        "char_share": char_share,
    }
