from __future__ import annotations

from ..context import HarvestContext
from ..utils import condition_corrob_signals, extract_subject, heading_prior_signals, score_confidence


def harvest_conditions(ctx: HarvestContext, sent: str) -> None:
    for frame, rx, base in ctx.bundle.condition_patterns:
        if not rx.search(sent):
            continue
        anti = ctx.anti
        signals = [frame, *condition_corrob_signals(sent), *heading_prior_signals(ctx.source_ref, "conditions")]
        confidence = score_confidence(base, signals, anti)
        ctx.add_candidate("conditions", frame, {"description": sent, "responsible_party": extract_subject(sent) or None}, sent, ctx.source_ref, confidence, signals, anti)
