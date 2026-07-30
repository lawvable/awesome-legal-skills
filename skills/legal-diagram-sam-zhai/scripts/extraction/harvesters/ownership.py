from __future__ import annotations

import re

from ..context import HarvestContext
from ..utils import clean_entity, extract_object_entity, extract_subject, heading_prior_signals, score_confidence


def harvest_ownership_control(ctx: HarvestContext, sent: str) -> None:
    # ownership_patterns[0] = ownership regex; ownership_patterns[1] = control-authority pattern
    anti = ctx.anti
    own = ctx.bundle.ownership_patterns[0].search(sent)
    if own:
        signals = ["ownership_signal", *heading_prior_signals(ctx.source_ref, "relationships")]
        pct = own.group("pct")
        ctx.add_candidate("ownership_links", "ownership", {"parent": clean_entity(own.group("parent")), "child": clean_entity(own.group("child")), "percentage": float(pct) if pct else None}, sent, ctx.source_ref, score_confidence(0.78, signals, anti), signals, anti)
    if ctx.bundle.ownership_patterns[1].search(sent):
        signals = ["control_authority_signal", *heading_prior_signals(ctx.source_ref, "relationships")]
        if re.search(r"\b(ownership|voting|affiliate|governance|authority|approval)\b", sent, re.I):
            signals.append("legal_action_object")
        ctx.add_candidate("relationships", "control_authority", {"from_entity": extract_subject(sent) or "unspecified", "to_entity": extract_object_entity(sent) or "unspecified", "type": "control_or_authority", "description": sent}, sent, ctx.source_ref, score_confidence(0.58, signals, anti), signals, anti)
