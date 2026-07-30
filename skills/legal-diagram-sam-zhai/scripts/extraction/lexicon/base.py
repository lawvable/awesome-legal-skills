"""LexiconBundle: frozen dataclass contract for language-bearing pattern tables.

All fields are required (no Optional).  The EN bundle is built in en.py and
the FR bundle in fr.py (W3); both must populate every field (enforced by
scripts/tests/test_lexicon_contract.py).  Harvesters receive the bundle via
the HarvestContext threaded by the dispatcher, which selects it per block
from block.lang.
"""
from __future__ import annotations

import dataclasses
import re
from typing import Callable, Optional, Tuple


# Type aliases for the pattern table field types.
# A frame entry is (frame_name, compiled_pattern, base_confidence).
_FrameTable = Tuple[Tuple[str, re.Pattern[str], float], ...]


@dataclasses.dataclass(frozen=True)
class LexiconBundle:
    """All language-bearing regex patterns and pattern tables for one locale.

    Fields mirror the field-to-harvester mapping defined in the W2.1 spec.
    Every field must be non-empty in a valid bundle, in every language
    (enforced by scripts/tests/test_lexicon_contract.py).

    Canonical sentence_split_re and abbreviation_guards definitions live in
    en.py and fr.py (relocated out of utils.py by W2.4 / W3); utils.py only
    re-exports the EN names for backward compatibility.
    """

    # --- date / time ---
    # Compiled pattern matching ISO dates and English long-form dates.
    date_re: re.Pattern[str]

    # --- sentence splitting ---
    # Compiled pattern consumed by _guard_split in utils.py.  Canonical
    # definition lives in en.py (_SENTENCE_SPLIT); utils.py re-exports it.
    # The _guard_split MECHANISM stays in utils.py (language-neutral).
    sentence_split_re: re.Pattern[str]

    # --- abbreviation guards ---
    # Tuple of literal strings that must not trigger a sentence split.
    # Canonical definitions live in en.py (_ABBREVIATION_GUARDS_EN) and fr.py
    # (_ABBREVIATION_GUARDS_FR); utils.py re-exports the EN name for
    # compatibility and the dispatcher passes the per-block bundle's guards
    # to sentences_with_offsets (W3).
    abbreviation_guards: tuple[str, ...]

    # --- legal action verbs (from lexicon.py LEGAL_ACTION_VERBS) ---
    legal_action_verbs: re.Pattern[str]

    # --- money regex (from lexicon.py MONEY_RE) ---
    money_re: re.Pattern[str]

    # --- deadlines.py patterns ---
    deadline_frames: _FrameTable

    # --- obligations.py patterns (positive and negative obligations) ---
    obligation_patterns: _FrameTable

    # --- obligations.py prohibition patterns ---
    # Negative obligations are a subset of obligation_patterns; this field
    # exposes them separately so callers can reference prohibition patterns
    # directly.  The actual table entries live in obligation_patterns; this
    # field holds the same compiled patterns filtered to negative frames.
    prohibition_patterns: _FrameTable

    # --- reps.py anti-signal patterns ---
    rep_warranty_anti_signals: _FrameTable

    # --- events.py occurrence verbs ---
    occurrence_verbs: re.Pattern[str]

    # --- parties.py caption / corporate / defined-party patterns ---
    # Each caption entry is one caption style (EN: single "X v. Y" pattern;
    # FR may add entries, e.g. "X c. Y").  Corporate suffixes and defined-party
    # markers are separate fields, never folded into caption_patterns.
    caption_patterns: tuple[re.Pattern[str], ...]
    corporate_suffixes: tuple[re.Pattern[str], ...]
    defined_party_markers: tuple[re.Pattern[str], ...]

    # --- party_mentions.py heuristic NER pass (W4.2) ---
    # Compiled pattern matching ONE capitalized token built from the
    # per-language title-case character class, so accented FR tokens
    # ("Société", "Générale", "Tremblay") match under the FR bundle.  The NER
    # harvester anchors a run of 2+ such tokens with this pattern; the EN class
    # is ASCII-only and the FR class adds the accented ranges used elsewhere in
    # this bundle (see _CAPTION_PATTERNS).  Used for detection only; the
    # harvester caps its candidates at hint tier (the resolver enforces the
    # ceiling structurally for the freeform_mention frame).
    titlecase_token_re: re.Pattern[str]

    # Role words that corroborate a freeform mention as a party reference
    # (EN: plaintiff/defendant/vendor/purchaser/employee; FR twins:
    # demandeur/défendeur/vendeur/acheteur/employé).  Lowercased; the harvester
    # matches them case-insensitively within the mention's sentence.
    party_role_words: tuple[str, ...]

    # --- citations.py citation patterns ---
    # Index contract: [0] neutral_citation, [1] case_citation, [2] statutory_ref,
    # [3] rule_ref.  Every language bundle must keep this order.
    citation_patterns: tuple[re.Pattern[str], ...]

    # --- notices.py notice patterns ---
    notice_patterns: tuple[re.Pattern[str], ...]

    # --- conditions.py condition patterns ---
    condition_patterns: _FrameTable

    # --- consent.py consent/discretion patterns ---
    consent_patterns: _FrameTable

    # --- controls.py control patterns ---
    # Index contract: [0] gate pattern (mandatory entry check), [1] evidence-signal
    # pattern.  Every language bundle must keep this order.
    control_patterns: tuple[re.Pattern[str], ...]

    # --- ownership.py ownership patterns ---
    ownership_patterns: tuple[re.Pattern[str], ...]

    # --- payments.py payment verbs and money ---
    payment_verbs: re.Pattern[str]

    # --- remedies.py remedy patterns ---
    remedy_patterns: tuple[re.Pattern[str], ...]

    # --- documents.py document patterns ---
    document_patterns: tuple[re.Pattern[str], ...]

    # --- date normalisation (W3.3) ---
    # Callable: text -> canonical date string for the FIRST date_re match in
    # the text, or None when no date is present.  The canonical surface form
    # is per-language: EN returns the matched text verbatim (EN goldens lock
    # date_or_timing to as-written dates); FR returns ISO 8601 (YYYY-MM-DD).
    # Harvesters call this through the bundle so the language asymmetry stays
    # in the lexicon layer and helpers/ remain lexicon-free (W2 invariant).
    normalize_date: Callable[[str], Optional[str]]

    # --- amount parsing (W3.3) ---
    # Callable: money text -> float amount, or None when the bundle defers to
    # the pipeline's default parser (helpers.money.amount_number, applied at
    # materialize time).  EN always defers (returns None) so the EN candidate
    # payload stays golden-locked; FR parses locale formats at harvest time
    # ("1 234 567,89 $" with space/U+00A0/U+202F thousands separators, comma
    # decimals, "1,5 M$" millions) and payments.py stores the result under
    # value["amount"], which materialize prefers over re-parsing amount_text.
    parse_amount: Callable[[Optional[str]], Optional[float]]
