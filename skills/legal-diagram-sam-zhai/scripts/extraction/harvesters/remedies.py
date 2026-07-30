from __future__ import annotations

import re

from ..context import HarvestContext
from ..utils import extract_subject, score_confidence


def harvest_default_remedy(ctx: HarvestContext, sent: str) -> None:
    if not ctx.bundle.remedy_patterns[0].search(sent):
        return
    anti = ctx.anti
    signals = ["default_remedy_signal"]
    if re.search(r"\b(obligation|representation|warranty|covenant|remedy|terminate|cure)\b", sent, re.I):
        signals.append("legal_action_object")
    if ctx.is_known_subject(extract_subject(sent)):
        signals.append("known_party_subject")
    confidence = score_confidence(0.58, signals, anti)
    ctx.add_candidate("conditions", "default_remedy", {"description": sent, "responsible_party": extract_subject(sent) or None}, sent, ctx.source_ref, confidence, signals, anti)
