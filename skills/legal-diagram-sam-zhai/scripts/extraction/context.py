"""HarvestContext: extraction context threaded through sentence harvesters.

W2.2 replaces the (h, sent, source_ref, anti) calling convention with
(ctx, sent) where *ctx* carries the bundle, sink, source ref, and
anti-signal accumulator.

Design note: the dispatcher builds one fresh HarvestContext per sentence
because source_ref and anti vary per sentence; construction is a cheap
dataclass allocation and exactly mirrors the previous per-sentence argument
passing.  The bundle and known_aliases are shared by reference across all
sentences of a block (W3 selects the bundle from block.lang).
"""
from __future__ import annotations

import dataclasses
from typing import Any, Optional, Protocol

from .lexicon.base import LexiconBundle
from .schema import SourceRef
from .utils import norm


class AddCandidateFn(Protocol):
    """Typing contract for the candidate-sink callable stored on HarvestContext.

    Mirrors the parameter list of ``CandidateHarvester._add_candidate``
    (without *self*).  Any callable whose ``__call__`` does not match this
    signature will produce a pyright error when assigned to
    ``HarvestContext.add_candidate``.
    """

    def __call__(
        self,
        target_field: str,
        frame_type: str,
        value: dict[str, Any],
        snippet_text: str,
        source_ref: SourceRef,
        confidence: float,
        signals: list[str],
        anti_signals: Optional[list[str]] = None,
    ) -> None: ...


@dataclasses.dataclass
class HarvestContext:
    """Per-block extraction context threaded into every sentence harvester.

    Attributes:
        bundle: Language-bearing pattern tables for the current block.
        add_candidate: Sink function with the same parameter shape as
            CandidateHarvester._add_candidate.
        source_ref: Current per-sentence source reference; updated by the
            dispatcher before each harvester call.
        anti: Current per-sentence anti-signal list; updated by the dispatcher
            before each harvester call.  Harvesters may extend it locally
            (e.g. ``anti = [*ctx.anti, "extra"]``) without mutating ctx.anti.
        known_aliases: Set of normalised party/role aliases accumulated across
            the document; updated by harvest_party_alias.
    """

    bundle: LexiconBundle
    add_candidate: AddCandidateFn
    source_ref: SourceRef
    anti: list[str]
    known_aliases: set[str] = dataclasses.field(default_factory=set)
    # Item 6: original-cased corporate party names (populated by harvest_party_alias).
    # Used by _resolve_first_person so 'We'/'Our' resolves with correct capitalisation.
    corporate_names: set[str] = dataclasses.field(default_factory=set)
    # Bug 8: mapping from normalised legal name → normalised role alias, populated
    # by harvest_party_alias.  Used by harvest_obligation to substitute the legal
    # name with the defined role in the description subject so that "Northgate
    # Acquisitions Corp. shall deliver..." becomes "Purchaser shall deliver...".
    party_role_map: dict[str, str] = dataclasses.field(default_factory=dict)

    def is_known_subject(self, subject: str) -> bool:
        """Return True if *subject* matches a known party alias."""
        normalised = norm(subject)
        if not normalised:
            return False
        if normalised in self.known_aliases:
            return True
        return any(
            normalised == alias
            or normalised.endswith(" " + alias)
            or alias.endswith(" " + normalised)
            for alias in self.known_aliases
            if alias
        )
