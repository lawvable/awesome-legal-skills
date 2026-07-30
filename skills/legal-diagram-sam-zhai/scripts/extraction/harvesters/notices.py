from __future__ import annotations

from ..context import HarvestContext
from ..utils import delivery_method, extract_notice_parties, heading_prior_signals, score_confidence


def harvest_notice(ctx: HarvestContext, sent: str) -> None:
    if not ctx.bundle.notice_patterns[0].search(sent):
        return
    sender, recipient = extract_notice_parties(sent)
    method = delivery_method(sent)
    anti = ctx.anti
    signals = ["notice_signal", *heading_prior_signals(ctx.source_ref, "communications")]
    if sender and sender != "unspecified":
        signals.append("sender_signal")
    if recipient and recipient != "unspecified":
        signals.append("recipient_signal")
    if method:
        signals.append("delivery_method_signal")
    confidence = score_confidence(0.62, signals, anti)
    if not method and not recipient and not (sender and sender != "unspecified"):
        confidence = min(confidence, 0.44)
        anti = [*anti, "notice_without_sender_recipient_or_method"]
    ctx.add_candidate("communications", "notice_communication", {"from_party": sender or "unspecified", "to_party": recipient or "unspecified", "comm_type": "notice", "description": sent, "delivery_method": method}, sent, ctx.source_ref, confidence, signals, anti)
