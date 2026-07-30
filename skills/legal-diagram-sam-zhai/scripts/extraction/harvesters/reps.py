from __future__ import annotations

from ..context import HarvestContext
from ..utils import extract_subject, is_rep_warranty, score_confidence


def harvest_rep_warranty(ctx: HarvestContext, sent: str) -> None:
    if not is_rep_warranty(sent):
        return
    signals = ["rep_warranty_signal"]
    if ctx.is_known_subject(extract_subject(sent)):
        signals.append("known_party_subject")
    for frame, rx, _base in ctx.bundle.rep_warranty_anti_signals:
        if rx.search(sent):
            signals.append(frame)
            break
    anti = ctx.anti
    ctx.add_candidate("concepts", "representation_warranty", {"name": "Representation/Warranty", "concept_type": "representation", "description": sent}, sent, ctx.source_ref, score_confidence(0.65, signals, anti), signals, anti)
