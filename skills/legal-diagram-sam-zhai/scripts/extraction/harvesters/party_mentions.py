"""W4.2 heuristic NER party pass.

A whole-document harvester (not a sentence harvester) because its corroboration
signal is document frequency: a freeform mention must appear in 2+ distinct
blocks.

Stop-list seam (deliberate choice): the harvester does NOT consult
h.known_aliases to drop mentions that duplicate a defined term.  Doing so would
suppress the very mentions that corroborate a BELOW-threshold defined party
(e.g. a bare litigation caption at 0.60 that the spec wants NER to lift), and
promotion is unknown at harvest time.  Instead the harvester emits a hint for
every repeated, role-corroborated mention, and the resolver does the
defined-term reconciliation: a freeform_mention whose name matches a
defined-party / table-row candidate raises THAT candidate's confidence
(resolver._apply_ner_corroboration), while the hint itself stays a hint.  The
harvester therefore stays pure of resolution state: it reads only h.doc.blocks
and emits via h._add_candidate.

Tier ceiling: every candidate is a "freeform_mention" frame emitted at a fixed
sub-promotion confidence.  The hard cap is enforced STRUCTURALLY in the
resolver (resolve_candidates demotes any freeform_mention to a hint regardless
of score), never by this harvester's confidence value alone.  Canonical party
entities therefore never originate from NER.

Detection: runs of 2+ capitalized tokens (bundle.titlecase_token_re, so FR
accents work), filtered against a stop list (sentence-initial sequences and
month names), corroborated by a role word from the bundle and by document
frequency (2+ distinct blocks).
"""
from __future__ import annotations

from ..lexicon import get_bundle
from ..lexicon.base import LexiconBundle
from ..schema import SourceRef
from ..utils import norm, sentences_with_offsets

# Fixed sub-promotion confidence for every freeform mention.  Below
# PROMOTE_WITH_CORROBORATION (0.65) and HINT_MIN-clear so the candidate lands
# in the hint band; the resolver caps the frame structurally regardless.
_MENTION_CONFIDENCE = 0.50

# Minimum distinct blocks a mention must appear in (document-frequency floor).
_MIN_DISTINCT_BLOCKS = 2


class _Mention:
    """Accumulator for one candidate mention across the document."""

    __slots__ = ("text", "blocks", "has_role_word", "snippet", "source_ref")

    def __init__(self, text: str, snippet: str, source_ref: SourceRef) -> None:
        self.text = text
        self.blocks: set[str] = set()
        self.has_role_word = False
        # First-seen verbatim snippet + provenance; stable for determinism.
        self.snippet = snippet
        self.source_ref = source_ref


def _is_month_token(token: str, bundle: LexiconBundle) -> bool:
    """True when *token* is a month name in this language.

    Reuses the bundle's date_re month vocabulary (no constant duplication):
    a bare month name completes a date only when wrapped as "1 <token> 2000".
    Couples month detection to date_re accepting the "D Month YYYY" form; if
    that form is ever dropped from date_re, month stop-listing silently regresses.
    """
    return bool(bundle.date_re.search(f"1 {token} 2000"))


def _capitalized_runs(sentence: str, bundle: LexiconBundle) -> list[tuple[str, bool]]:
    """Return (run_text, is_sentence_initial) for each run of 2+ title-case tokens.

    A run is a maximal sequence of consecutive capitalized tokens separated by
    single spaces.  is_sentence_initial marks a run whose first token is the
    first token of the sentence (positional stop-list signal).
    """
    matches = list(bundle.titlecase_token_re.finditer(sentence))
    runs: list[tuple[str, bool]] = []
    i = 0
    while i < len(matches):
        j = i
        # Extend the run while the next token is adjacent (separated only by a
        # single space) and also title-case.
        while j + 1 < len(matches) and sentence[matches[j].end():matches[j + 1].start()] == " ":
            j += 1
        if j > i:  # 2+ tokens
            run_start = matches[i].start()
            run_text = sentence[run_start:matches[j].end()]
            is_initial = run_start == 0
            runs.append((run_text, is_initial))
        i = j + 1
    return runs


def harvest_party_mentions(h) -> None:
    """Emit freeform_mention hints for repeated, role-corroborated party mentions."""
    mentions: dict[str, _Mention] = {}
    order: list[str] = []  # first-seen key order for deterministic emission

    for blk in list(getattr(h.doc, "blocks", []) or []):
        text = str(getattr(blk, "text", "") or "").strip()
        if not text:
            continue
        if (getattr(blk, "block_type", "") or "") == "heading":
            continue
        bundle = get_bundle(str(getattr(blk, "lang", "") or ""))
        block_id = str(getattr(blk, "idx", ""))
        for sent, start, end in sentences_with_offsets(text, bundle.abbreviation_guards):
            if not sent:
                continue
            role_in_sentence = any(rw in sent.lower() for rw in bundle.party_role_words)
            for run_text, is_initial in _capitalized_runs(sent, bundle):
                if is_initial:
                    continue  # sentence-initial capitalized sequence: stop-listed
                tokens = run_text.split()
                if any(_is_month_token(tok, bundle) for tok in tokens):
                    continue  # month names: stop-listed
                key = norm(run_text)
                if not key:
                    continue
                mention = mentions.get(key)
                if mention is None:
                    source_ref = h._block_source_ref(blk, char_span=(start, end))
                    mention = _Mention(run_text, sent, source_ref)
                    mentions[key] = mention
                    order.append(key)
                mention.blocks.add(block_id)
                if role_in_sentence:
                    mention.has_role_word = True

    for key in order:
        mention = mentions[key]
        if len(mention.blocks) < _MIN_DISTINCT_BLOCKS:
            continue
        if not mention.has_role_word:
            continue
        signals = ["ner_mention", "ner_role_word", "ner_doc_frequency"]
        h._add_candidate(
            "parties",
            "freeform_mention",
            {"mention": mention.text, "snippet": mention.snippet, "type": "party"},
            mention.snippet,
            mention.source_ref,
            _MENTION_CONFIDENCE,
            signals,
        )
