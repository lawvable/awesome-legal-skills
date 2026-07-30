from __future__ import annotations

import re

from .lexicon import HINT_MIN, PROMOTE_AUTO, PROMOTE_WITH_CORROBORATION
from .schema import Candidate, PromotionDecision
from .utils import clamp, norm, strip_diacritics, uniq

# Punctuation normalization for dedup: strip all non-alphanumeric, non-space
# characters so quote-char variants (" vs ') do not produce separate keys.
_PUNCT_STRIP_RE = re.compile(r"[^\w\s]")

# W4.2: the frame an NER hint carries.  A candidate of this frame never
# promotes (the cap is structural, enforced here, not via its confidence).
_NER_FRAME = "freeform_mention"

# W4.2: party candidate frames an NER hint may corroborate (defined-party and
# table-row parties).  Matching one raises its confidence; the hint stays a hint.
_CORROBORATABLE_PARTY_FRAMES = frozenset({
    "defined_party_alias",
    "agreement_intro_party",
    "table_party",
    "litigation_caption",
})

# Confidence delta applied to a defined-party candidate corroborated by an NER
# hint.  Pushes a bare caption (0.60) past PROMOTE_WITH_CORROBORATION (0.65).
_CORROBORATION_BOOST = 0.10

# W6 T4 Item C (resolver stage): table_party candidates whose single-token
# name normalises to a role word must be suppressed when a defined_party_alias
# candidate in the same run maps that role to a specific named party.
# Words that are never standalone identifiers are pre-suppressed in tables.py
# (_GENERIC_ROLE_WORDS).  This set defines additional single-token role words
# that are eligible for context-sensitive suppression only.
_CONTEXT_SENSITIVE_ROLE_WORDS: frozenset[str] = frozenset({
    "company", "vendor", "purchaser", "seller", "buyer",
    "licensor", "licensee", "borrower", "lender", "lessor", "lessee",
    "franchisor", "franchisee", "employer", "employee", "contractor",
    "subcontractor", "customer", "client", "supplier", "agent",
    "principal", "guarantor", "indemnitor", "indemnified",
})


def _build_defined_role_set(candidates: list[Candidate]) -> frozenset[str]:
    """Return the set of normalised role words that defined_party_alias candidates map to.

    A defined_party_alias candidate with a non-empty 'role' field registers that
    norm(role) as a word that should suppress a matching single-token table_party.
    Only roles that match a known context-sensitive role word are registered to
    avoid suppressing genuinely named parties (e.g. a table cell "Acme Corp"
    normalising to an unexpected role).
    """
    defined_roles: set[str] = set()
    for cand in candidates:
        if cand.frame_type != "defined_party_alias":
            continue
        role_raw = cand.normalized_value.get("role", "") or ""
        role_norm = norm(role_raw)
        if role_norm in _CONTEXT_SENSITIVE_ROLE_WORDS:
            defined_roles.add(role_norm)
    return frozenset(defined_roles)


def _suppress_defined_role_table_parties(candidates: list[Candidate]) -> frozenset[str]:
    """Return the set of candidate IDs that must be suppressed.

    A table_party candidate is suppressed when its single-token name normalises
    to a role word that is already mapped to a specific named party via a
    defined_party_alias candidate.  The logic preserves candidates whose role
    word has no such mapping (those bare role words are the party identifier).
    """
    defined_roles = _build_defined_role_set(candidates)
    if not defined_roles:
        return frozenset()
    suppress_ids: set[str] = set()
    for cand in candidates:
        if cand.frame_type != "table_party":
            continue
        name = cand.normalized_value.get("name", "") or ""
        tokens = name.strip().split()
        if len(tokens) != 1:
            continue
        if norm(tokens[0]) in defined_roles:
            suppress_ids.add(cand.id)
    return frozenset(suppress_ids)


def resolve_candidates(candidates: list[Candidate], *, sparse: bool = True) -> list[PromotionDecision]:
    # W4.2: NER corroboration runs first so the confidence bump it lands on a
    # paired defined-party candidate is visible to the tier decision below.
    _apply_ner_corroboration(candidates)
    # W6 T4 Item C (resolver stage): suppress table_party candidates whose
    # single-token role-word name is already mapped to a named party via a
    # defined_party_alias candidate.  This runs after NER corroboration so the
    # corroboration boost is in place before suppression is evaluated.
    suppress_ids = _suppress_defined_role_table_parties(candidates)
    decisions: list[PromotionDecision] = []
    for cand in candidates:
        # W6 T4 Item C: defined-role suppression overrides any confidence tier.
        if cand.id in suppress_ids:
            decisions.append(PromotionDecision(cand.id, "suppress", "table_party role word mapped to defined named party", None))
            continue
        # W4.2 structural ceiling: a freeform_mention never promotes, even at
        # max confidence.  Canonical parties never originate from NER alone.
        if cand.frame_type == _NER_FRAME:
            action = "hint" if cand.confidence >= HINT_MIN or (sparse and cand.confidence >= 0.35) else "suppress"
            decisions.append(PromotionDecision(cand.id, action, "NER freeform mention capped at hint tier", None))
        elif cand.confidence >= PROMOTE_AUTO:
            decisions.append(PromotionDecision(cand.id, "promote", "confidence >= 0.85", f"candidate:{cand.id}"))
        elif cand.confidence >= PROMOTE_WITH_CORROBORATION and has_corroboration(cand):
            decisions.append(PromotionDecision(cand.id, "promote", "medium confidence with corroborating signals", f"candidate:{cand.id}"))
        elif cand.confidence >= HINT_MIN:
            decisions.append(PromotionDecision(cand.id, "hint", "below promotion threshold; send compact evidence to LLM", None))
        elif sparse and cand.confidence >= 0.35:
            decisions.append(PromotionDecision(cand.id, "hint", "sparse extraction fallback", None))
        else:
            decisions.append(PromotionDecision(cand.id, "suppress", "low confidence or noisy uncorroborated signal", None))
    return decisions


def _apply_ner_corroboration(candidates: list[Candidate]) -> None:
    """Raise a defined-party candidate's confidence when an NER hint names it.

    An NER hint (freeform_mention) whose mention matches an existing
    defined-party or table-row party candidate (case/diacritic-insensitive)
    appends a ner_corroboration signal to THAT candidate and bumps its
    confidence.  The hint itself is untouched and stays a hint; there is no
    new promotion channel.  Matching is keyed on strip_diacritics so accented
    FR mentions corroborate their defined-party twins.
    """
    mention_keys = {
        _corroboration_key(cand.normalized_value.get("mention", ""))
        for cand in candidates
        if cand.frame_type == _NER_FRAME
    }
    mention_keys.discard("")
    if not mention_keys:
        return
    for cand in candidates:
        if cand.frame_type not in _CORROBORATABLE_PARTY_FRAMES:
            continue
        if _corroboration_key(cand.normalized_value.get("name", "")) not in mention_keys:
            continue
        if "ner_corroboration" not in cand.signals:
            cand.signals = uniq([*cand.signals, "ner_corroboration"])
            cand.confidence = clamp(cand.confidence + _CORROBORATION_BOOST)


def _corroboration_key(name: str) -> str:
    return norm(strip_diacritics(str(name or "")))


def has_corroboration(cand: Candidate) -> bool:
    corroborators = {
        "table_row_binding", "known_party_subject", "heading_prior", "deadline_signal", "alias_match",
        "legal_action_object", "defined_term", "sender_signal", "recipient_signal", "payment_signal",
        "document_header", "control_header", "party_header", "obligation_header", "qualifier_signal", "rep_warranty_signal",
        "date_signal", "event_verb", "citation_signal", "ner_corroboration",
        # W6 T2 Defect E: explicit positive modal ("shall", "must", "are required to", etc.)
        # self-corroborates a positive_obligation candidate whose subject is a collective
        # noun or first-person pronoun not in known_aliases.
        "explicit_modal",
        # W6 T3: entity structural frames -- ownership participants, list items, acquisition
        # targets are structurally corroborated by their source frame.
        "ownership_participant", "entity_list_item", "acquisition_target",
        # W6 T3: privacy party frames -- operator declaration and service-provider enumeration.
        "privacy_operator", "service_provider",
        # W6 T3: privacy controls frames -- technical and organisational security measures.
        "privacy_control",
        # W6 T3: litigation action context -- promotes hint-tier dated events.
        "litigation_action_context",
    }
    return bool(corroborators.intersection(cand.signals)) or cand.source_ref.table_coords is not None


def dedupe_candidates(candidates: list[Candidate]) -> list[Candidate]:
    by_key: dict[str, Candidate] = {}
    for cand in candidates:
        key = semantic_key(cand)
        existing = by_key.get(key)
        if existing is None or cand.confidence > existing.confidence:
            if existing is not None:
                cand.evidence_ids = uniq([*existing.evidence_ids, *cand.evidence_ids])
                cand.signals = uniq([*existing.signals, *cand.signals])
                cand.anti_signals = uniq([*existing.anti_signals, *cand.anti_signals])
                cand.confidence = max(existing.confidence, cand.confidence)
            by_key[key] = cand
        elif existing is not None:
            existing.evidence_ids = uniq([*existing.evidence_ids, *cand.evidence_ids])
            existing.signals = uniq([*existing.signals, *cand.signals])
            existing.anti_signals = uniq([*existing.anti_signals, *cand.anti_signals])
    return list(by_key.values())


def semantic_key(cand: Candidate) -> str:
    value = cand.normalized_value
    # For entity candidates the canonical identity is (field, name): two frames
    # discovering the same corporate name (e.g. ownership_participant vs
    # entity_list_item) must produce the same dedup key so only one is kept.
    if cand.target_field == "entities":
        name_raw = value.get("name", "")
        return f"entities|{_norm_for_dedup(str(name_raw))}"
    # W6 T4 Item C: parties dedup on (field, normalized_name) like entities so
    # the same party name from two different sentence frames (e.g. both
    # defined_party_alias) collapses to a single entry.  Frame type is NOT
    # part of the key; cross-frame dedup produces the highest-confidence entry.
    if cand.target_field == "parties":
        name_raw = value.get("name", "")
        return f"parties|{_norm_for_dedup(str(name_raw))}"
    # W6 T4 Item D: documents dedup on (field, normalized_name) so the same
    # document title captured from multiple table rows or sentences does not
    # produce duplicate promoted entries.
    if cand.target_field == "documents":
        name_raw = value.get("name", "")
        return f"documents|{_norm_for_dedup(str(name_raw))}"
    pieces = [cand.target_field, cand.frame_type]
    for key in ("party", "name", "description", "date_or_timing", "from_party", "to_party", "parent", "child", "question"):
        raw = value.get(key)
        if raw:
            pieces.append(_norm_for_dedup(str(raw)))
    if len(pieces) == 2:
        pieces.append(_norm_for_dedup(str(value)))
    return "|".join(pieces)


def _norm_for_dedup(text: str) -> str:
    """Normalise text for dedup: casefold, strip all punctuation, collapse whitespace.

    Quote-char variants (" vs '), curly vs straight apostrophes, and other
    punctuation differences must not produce distinct keys.
    """
    s = norm(text)                          # casefold + whitespace-collapse
    s = _PUNCT_STRIP_RE.sub(" ", s)        # remove all non-alphanumeric
    return re.sub(r"\s+", " ", s).strip()
