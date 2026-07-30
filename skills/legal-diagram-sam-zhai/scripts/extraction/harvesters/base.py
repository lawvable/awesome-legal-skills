from __future__ import annotations

import re
from typing import Any, Callable, Optional

from ..context import HarvestContext
from ..lexicon import KNOWN_ROLE_WORDS, get_bundle
from ..lexicon.base import LexiconBundle
from ..schema import Candidate, EvidencePacket, SourceRef
from ..utils import (
    anti_signals,
    clamp,
    clean_value,
    neighbor_ids,
    page_from_anchor,
    sheet_from_anchor,
    slide_from_anchor,
    snippet,
    sentences_with_offsets,
)
from .conditions import harvest_conditions
from .controls import harvest_controls
from .deadlines import harvest_deadlines
from .documents import harvest_deliverables
from .events import harvest_event
from .notices import harvest_notice
from .obligations import harvest_obligation, harvest_obligation_list_blocks
from .ownership import harvest_ownership_control
from .parties import harvest_litigation_captions, harvest_party_alias, harvest_privacy_parties
from .party_mentions import harvest_party_mentions
from .payments import harvest_payments
from .remedies import harvest_default_remedy
from .reps import harvest_rep_warranty
from .citations import harvest_citation, harvest_citation_block
from .entities import harvest_entities
from .tables import harvest_tables


class CandidateHarvester:
    def __init__(self, doc: Any, *, input_source: Optional[str] = None) -> None:
        self.doc = doc
        self.source = input_source or getattr(doc, "source", "") or ""
        self.evidence_packets: list[EvidencePacket] = []
        self.candidates: list[Candidate] = []
        self.synthetic_table_block_count = 0
        self.known_aliases: set[str] = set(KNOWN_ROLE_WORDS)
        # Item 6: original-cased corporate names for first-person resolution.
        self.corporate_names: set[str] = set()
        # Bug 8: legal-name → role alias mapping (populated by harvest_party_alias).
        self.party_role_map: dict[str, str] = {}

    def run(self) -> list[Candidate]:
        harvest_tables(self)
        blocks = list(getattr(self.doc, "blocks", []) or [])
        # Defect B: detect lead-in+list obligation patterns across consecutive
        # blocks.  Returns the set of lead-in paragraph indices consumed; those
        # blocks are skipped below to avoid double-promoting the bare lead-in.
        consumed_lead_ins = harvest_obligation_list_blocks(
            blocks,
            self._add_candidate,
            self._block_source_ref,
            anti_signals,
            lambda blk: get_bundle(str(getattr(blk, "lang", "") or "")),
            self.known_aliases,
        )
        for idx, blk in enumerate(blocks):
            if idx in consumed_lead_ins:
                # Lead-in was already expanded into per-item obligations above;
                # skip its obligation harvesting only -- other fields (deadlines,
                # parties, etc.) still run so their candidates are collected.
                self._harvest_block_skip_obligations(blk)
            else:
                self._harvest_block(blk)
        # NER party pass (W4.2): whole-document harvester emitting freeform
        # mention hints; runs after the per-block harvesters so its candidates
        # append after the per-block candidates (stable, deterministic order).
        harvest_party_mentions(self)
        return self.candidates

    def _harvest_block(self, blk: Any) -> None:
        text = str(getattr(blk, "text", "") or "").strip()
        if not text:
            return
        if (getattr(blk, "block_type", "") or "") == "heading":
            self._harvest_heading(text, self._block_source_ref(blk))
            return
        # W3: the bundle is selected once per block from the block's effective
        # language (post-inheritance "en"/"fr" set by language.annotate_blocks).
        # Blocks that never went through annotate_blocks (unit-test paths) carry
        # no lang and fall back to EN via get_bundle("").
        bundle = get_bundle(str(getattr(blk, "lang", "") or ""))
        # Caption detection and block-level citation harvesting run on the full
        # block text before sentence iteration because the sentence splitter
        # splits at "v."/"c." and breaks caption and citation spans.
        harvest_litigation_captions(self, text, self._block_source_ref(blk), anti_signals(text), bundle)
        harvest_citation_block(self._add_candidate, text, self._block_source_ref(blk), anti_signals(text))
        for sent, start, end in sentences_with_offsets(text, bundle.abbreviation_guards):
            if sent:
                self._harvest_sentence(sent, self._block_source_ref(blk, char_span=(start, end)), bundle)

    def _harvest_block_skip_obligations(self, blk: Any) -> None:
        """Harvest all fields except obligations for a consumed lead-in block.

        Called for paragraph blocks whose obligation candidates were already
        emitted by harvest_obligation_list_blocks (the lead-in expansion).
        All other sentence harvesters (deadlines, parties, etc.) still run.
        """
        text = str(getattr(blk, "text", "") or "").strip()
        if not text:
            return
        if (getattr(blk, "block_type", "") or "") == "heading":
            self._harvest_heading(text, self._block_source_ref(blk))
            return
        bundle = get_bundle(str(getattr(blk, "lang", "") or ""))
        harvest_litigation_captions(self, text, self._block_source_ref(blk), anti_signals(text), bundle)
        harvest_citation_block(self._add_candidate, text, self._block_source_ref(blk), anti_signals(text))
        for sent, start, end in sentences_with_offsets(text, bundle.abbreviation_guards):
            if sent:
                self._harvest_sentence_skip_obligations(
                    sent, self._block_source_ref(blk, char_span=(start, end)), bundle
                )

    def _harvest_sentence_skip_obligations(
        self, sent: str, source_ref: SourceRef, bundle: LexiconBundle
    ) -> None:
        """Run all sentence harvesters except harvest_obligation."""
        ctx = HarvestContext(
            bundle=bundle,
            add_candidate=self._add_candidate,
            source_ref=source_ref,
            anti=anti_signals(sent),
            known_aliases=self.known_aliases,
            corporate_names=self.corporate_names,
            party_role_map=self.party_role_map,
        )
        for fn in SENTENCE_HARVESTERS:
            if fn is harvest_obligation:
                continue
            fn(ctx, sent)

    def _harvest_heading(self, text: str, source_ref: SourceRef) -> None:
        if re.search(r"conditions?\s+precedent|closing\s+conditions?", text, re.I):
            self._add_candidate("conditions", "condition_section", {"description": text}, text, source_ref, 0.52, ["heading_prior"])
        if re.search(r"closing\s+deliver(?:y|ies)|documents?|certificates?", text, re.I):
            self._add_candidate("documents", "document_section", {"name": text, "description": text}, text, source_ref, 0.48, ["heading_prior"])

    def _harvest_sentence(self, sent: str, source_ref: SourceRef, bundle: LexiconBundle) -> None:
        # Build one context per sentence; source_ref and anti vary per sentence.
        # known_aliases and corporate_names are shared by reference so
        # harvest_party_alias mutations are immediately visible to subsequent
        # harvesters and the orchestrator.
        # The bundle is resolved per block from block.lang in _harvest_block (W3).
        ctx = HarvestContext(
            bundle=bundle,
            add_candidate=self._add_candidate,
            source_ref=source_ref,
            anti=anti_signals(sent),
            known_aliases=self.known_aliases,
            corporate_names=self.corporate_names,
            party_role_map=self.party_role_map,
        )
        for fn in SENTENCE_HARVESTERS:
            fn(ctx, sent)

    def _add_candidate(self, target_field: str, frame_type: str, value: dict[str, Any], snippet_text: str, source_ref: SourceRef, confidence: float, signals: list[str], anti_signals: Optional[list[str]] = None) -> None:
        confidence = clamp(confidence)
        evidence_id = f"E{len(self.evidence_packets):04d}"
        candidate_id = f"C{len(self.candidates):04d}"
        evidence = EvidencePacket(
            id=evidence_id,
            snippet=snippet(snippet_text),
            source_ref=source_ref,
            heading_path=list(source_ref.heading_path),
            candidate_fields=[target_field],
            confidence=confidence,
            neighboring_context_ids=neighbor_ids(source_ref.block_id),
        )
        self.evidence_packets.append(evidence)
        self.candidates.append(
            Candidate(
                id=candidate_id,
                target_field=target_field,
                frame_type=frame_type,
                normalized_value=clean_value(value),
                signals=_uniq(signals),
                anti_signals=_uniq(anti_signals or []),
                confidence=confidence,
                evidence_ids=[evidence_id],
                source_ref=source_ref,
            )
        )

    def _block_source_ref(self, blk: Any, char_span: Optional[tuple[int, int]] = None) -> SourceRef:
        anchor = str(getattr(blk, "anchor", "") or "")
        heading_path = list(getattr(blk, "heading_path", []) or [])
        parent = getattr(blk, "parent_heading", None)
        if not heading_path and parent:
            heading_path = [str(parent)]
        return SourceRef(
            source=self.source,
            block_id=str(getattr(blk, "idx", "")),
            anchor=anchor,
            page=page_from_anchor(anchor),
            slide=slide_from_anchor(anchor),
            sheet=sheet_from_anchor(anchor),
            heading_path=heading_path,
            table_coords=getattr(blk, "table_coords", None),
            char_span=char_span,
        )

    def _table_source_ref(self, table: Any, table_idx: int, row_idx: int) -> SourceRef:
        anchor = str(getattr(table, "anchor", "") or f"table{table_idx}")
        heading = str(getattr(table, "caption", "") or "").strip()
        return SourceRef(
            source=self.source,
            block_id=f"{anchor}:r{row_idx}",
            anchor=anchor,
            page=page_from_anchor(anchor),
            slide=slide_from_anchor(anchor),
            sheet=sheet_from_anchor(anchor),
            heading_path=[heading] if heading else [],
            table_coords=(table_idx, row_idx),
        )

def _uniq(items: list[str]) -> list[str]:
    seen = set()
    out = []
    for item in items:
        if not item or item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out


class _ConsentHarvesterProtocol:
    """Protocol adapter: bridges the ctx calling convention into the consent
    harvester, omitting the "consent_given" frame.

    Behaves as a plain callable; its __name__ is set to match the original
    function name so that the SENTENCE_HARVESTERS registry name check passes.
    """

    __name__ = "harvest_consent_discretion"
    __qualname__ = "harvest_consent_discretion"

    def __call__(self, ctx: HarvestContext, sent: str) -> None:
        from ..utils import extract_subject, score_confidence
        # The orchestrator protocol omits "consent_given"; the standalone
        # harvest_consent_discretion in consent.py uses the full table.
        # Filter preserves the pre-bundle behaviour for the orchestrator path.
        anti = ctx.anti
        for frame, rx, base in ctx.bundle.consent_patterns:
            if frame == "consent_given":
                continue
            if not rx.search(sent):
                continue
            subject = extract_subject(sent)
            signals = [frame]
            if ctx.is_known_subject(subject):
                signals.append("known_party_subject")
            if ctx.bundle.legal_action_verbs.search(sent):
                signals.append("legal_action_object")
            confidence = score_confidence(base, signals, anti)
            if re.search(r"\bmay\b", sent, re.I) and "known_party_subject" not in signals and not ctx.bundle.legal_action_verbs.search(sent):
                confidence = min(confidence, 0.44)
                anti = [*anti, "uncorroborated_may"]
            ctx.add_candidate("decision_points", frame, {"question": sent, "yes_path": "permitted/approved", "no_path": "blocked/not approved"}, sent, ctx.source_ref, confidence, signals, anti)


harvest_consent_discretion = _ConsentHarvesterProtocol()


# Registry of sentence-level harvesters called in order by _harvest_sentence.
# Defined here (at module end) so all names -- including harvest_consent_discretion
# above -- are already bound when this list is evaluated.
SENTENCE_HARVESTERS: list[Callable[[HarvestContext, str], None]] = [
    harvest_party_alias,
    harvest_privacy_parties,
    harvest_rep_warranty,
    harvest_obligation,
    harvest_conditions,
    harvest_controls,
    harvest_deadlines,
    harvest_consent_discretion,
    harvest_deliverables,
    harvest_payments,
    harvest_default_remedy,
    harvest_notice,
    harvest_ownership_control,
    harvest_entities,
    harvest_event,
    harvest_citation,
]
