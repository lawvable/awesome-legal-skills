"""entities.py: Harvest corporate entity candidates from structural frames.

Three harvesting frames (all require a corporate suffix for promotion):

  1. Ownership-statement participants -- both sides of "X owns N% of Y" and
     the holder in "held by Z" (reuses the ownership regex already parsed by
     ownership.py; extracts the participant names as entity candidates).

  2. Defined-entity list items -- "- **Name**: description" under a heading
     whose text matches an entities/structure keyword.

  3. Acquisition-target references -- "shares of X" / "actions de X" with a
     corp suffix, covering EN SPA and FR contract acquisition-target patterns.

Promotion discipline:
  - Every frame anchors to a structural signal (ownership_participant,
    entity_list_item, acquisition_target) which is listed in resolver
    has_corroboration(); this means base-confidence 0.68 + one structural
    signal clears the PROMOTE_WITH_CORROBORATION band (0.65).
  - Names without a corporate suffix are never emitted.
  - The value dict uses {"name": <company name>, "type": "entity"} so
    materialize's Entity builder fires correctly.
"""
from __future__ import annotations

import re

from ..context import HarvestContext
from ..utils import clean_entity, heading_prior_signals, score_confidence
from ._patterns import CORP_SUFFIX_ALT

# ---------------------------------------------------------------------------
# Corporate suffix guard: only names ending with a recognised suffix promote.
# This covers EN (Inc., Ltd., Corp., LLC, LP, LLP, PLC) and FR (Ltée, S.E.N.C.,
# s.r.l.) forms.  The regex anchors at a word boundary so partial matches
# (e.g. "Incorporated" without abbreviation) do not fire.
# ---------------------------------------------------------------------------
_CORP_SUFFIX_RE = re.compile(
    r"\b(?:" + CORP_SUFFIX_ALT + r")\s*$",
    re.I,
)

# "held by Z" pattern: captures the holder's name after "held by".
_HELD_BY_RE = re.compile(
    r"\bheld\s+by\s+(?P<holder>[A-Z][A-Za-zÀ-ÿ0-9.&'', \-]+?)(?:[,.]|\s+an?\s|\s*$)",
)

# Heading text patterns that indicate an entities/structure section.
_ENTITY_HEADING_RE = re.compile(
    r"\b(entit(?:y|ies)|structure|corporate\s+group|subsidiaries|membership|parties?\s+to)\b",
    re.I,
)

# List-item bold-name pattern: "- **Name**: description" OR "**Name**: description"
# (The Markdown adapter strips the leading "- " bullet, so both forms occur.)
_LIST_BOLD_ITEM_RE = re.compile(
    r"^(?:\s*[-*]\s+)?\*\*(?P<name>[^*]+)\*\*\s*:",
)

# Acquisition-target EN: "shares of X" / "all X shares" / "the shares of X"
_ACQUISITION_TARGET_EN_RE = re.compile(
    r"\b(?:shares?\s+of|all\s+(?:issued\s+and\s+outstanding\s+)?shares?\s+of|"
    r"the\s+(?:issued\s+and\s+outstanding\s+)?shares?\s+of)\s+"
    r"(?P<target>[A-Z][A-Za-z0-9.&'', \-]+?)(?=\s*[,()\"\']|\s*$|\s+free|\s+\()",
)

# Acquisition-target FR: "actions de X" / "actions émises ... de X Ltée"
_ACQUISITION_TARGET_FR_RE = re.compile(
    r"\b(?:actions\s+(?:émises\s+et\s+en\s+circulation\s+de|de|visées\s+de))\s+"
    r"(?P<target>[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÿ0-9.&'', \-]+?)(?=\s*[,()\«\»]|\s*$|\s+\()",
)


def _has_corp_suffix(name: str) -> bool:
    """Return True if *name* ends with a recognised corporate suffix."""
    return bool(_CORP_SUFFIX_RE.search(name.strip()))


def harvest_entities(ctx: HarvestContext, sent: str) -> None:
    """Harvest entity candidates from a sentence using structural frames."""
    anti = ctx.anti

    # ------------------------------------------------------------------
    # Frame 1a: Ownership-statement owner -- "X owns N% of Y"
    # The ownership regex is already on the bundle; we extract both sides.
    # ------------------------------------------------------------------
    own = ctx.bundle.ownership_patterns[0].search(sent)
    if own:
        for group_name in ("parent", "child"):
            raw = own.group(group_name) or ""
            name = clean_entity(raw)
            if name and _has_corp_suffix(name):
                signals = [
                    "ownership_participant",
                    *heading_prior_signals(ctx.source_ref, "relationships"),
                ]
                ctx.add_candidate(
                    "entities",
                    "ownership_participant",
                    {"name": name, "type": "entity"},
                    sent,
                    ctx.source_ref,
                    score_confidence(0.72, signals, anti),
                    signals,
                    anti,
                )

    # ------------------------------------------------------------------
    # Frame 1b: "held by Z" -- the minority holder name
    # ------------------------------------------------------------------
    held = _HELD_BY_RE.search(sent)
    if held:
        name = clean_entity(held.group("holder") or "")
        if name and _has_corp_suffix(name):
            signals = [
                "ownership_participant",
                *heading_prior_signals(ctx.source_ref, "relationships"),
            ]
            ctx.add_candidate(
                "entities",
                "ownership_participant",
                {"name": name, "type": "entity"},
                sent,
                ctx.source_ref,
                score_confidence(0.70, signals, anti),
                signals,
                anti,
            )

    # ------------------------------------------------------------------
    # Frame 2: Defined-entity list item "- **Name**: ..."
    # Only promotes when under an entities/structure heading.  Without a
    # structural heading no candidate is emitted (FP guard).
    # ------------------------------------------------------------------
    heading_text = " > ".join(ctx.source_ref.heading_path or [])
    under_entity_heading = bool(_ENTITY_HEADING_RE.search(heading_text))
    list_match = _LIST_BOLD_ITEM_RE.match(sent)
    if list_match:
        name = clean_entity(list_match.group("name") or "")
        if name and _has_corp_suffix(name):
            if under_entity_heading:
                signals = ["entity_list_item", "heading_prior"]
                ctx.add_candidate(
                    "entities",
                    "entity_list_item",
                    {"name": name, "type": "entity"},
                    sent,
                    ctx.source_ref,
                    score_confidence(0.72, signals, anti),
                    signals,
                    anti,
                )
            # No structural heading: emit nothing (FP guard).

    # ------------------------------------------------------------------
    # Frame 3a: Acquisition-target EN "shares of X"
    # ------------------------------------------------------------------
    acq_en = _ACQUISITION_TARGET_EN_RE.search(sent)
    if acq_en:
        name = clean_entity(acq_en.group("target") or "")
        if name and _has_corp_suffix(name):
            signals = ["acquisition_target"]
            ctx.add_candidate(
                "entities",
                "acquisition_target",
                {"name": name, "type": "entity"},
                sent,
                ctx.source_ref,
                score_confidence(0.72, signals, anti),
                signals,
                anti,
            )

    # ------------------------------------------------------------------
    # Frame 3b: Acquisition-target FR "actions de X Ltée"
    # ------------------------------------------------------------------
    acq_fr = _ACQUISITION_TARGET_FR_RE.search(sent)
    if acq_fr:
        name = clean_entity(acq_fr.group("target") or "")
        if name and _has_corp_suffix(name):
            signals = ["acquisition_target"]
            ctx.add_candidate(
                "entities",
                "acquisition_target",
                {"name": name, "type": "entity"},
                sent,
                ctx.source_ref,
                score_confidence(0.72, signals, anti),
                signals,
                anti,
            )
