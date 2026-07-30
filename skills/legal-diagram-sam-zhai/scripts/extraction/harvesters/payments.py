from __future__ import annotations

import re
from typing import Any

from ..context import HarvestContext
from ..utils import deadline_text, extract_payment_parties, has_deadline_signal, heading_prior_signals, money_text, rank_from_text, score_confidence

# W6 T4 Item E: conditional-trigger patterns that indicate the transfer is
# contingent on an event (indemnity, breach, insolvency) rather than a direct
# scheduled payment.  These should be demoted to hint tier, not promoted.
_CONDITIONAL_TRIGGER_RE = re.compile(
    r"^(?:advenant\b|in\s+the\s+event\s+(?:of|that)\b|en\s+cas\s+de\b|"
    r"si\s+(?:une\s+partie|la\s+société|le\s+vendeur|l'acheteur|l'acquéreur)\b|"
    r"upon\s+(?:a\s+breach|default|insolvency|failure)\b)",
    re.I,
)

# W6 T4 Item E: lead-in pattern for transfers -- "X shall pay Y as follows"
# introduces a list; the lead-in sentence itself should not be a separate
# transfer candidate when split items follow.
_TRANSFER_LEAD_IN_RE = re.compile(
    r"\b(?:shall|must|will)\s+(?:pay|remit|transfer)\b.{0,80}\bas\s+follows\s*:",
    re.I,
)


def harvest_payments(ctx: HarvestContext, sent: str) -> None:
    anti = ctx.anti
    # Money and payment verbs are bundle-sourced (W3) with the EN helpers as
    # fallback: the EN bundle patterns are verbatim the helper patterns, so
    # the EN path is byte-identical; money_text() stays broader than money_re
    # alone because it also matches bare money nouns ("purchase price", "fee").
    money_match = ctx.bundle.money_re.search(sent)
    amount_text = money_match.group(0) if money_match else money_text(sent)
    if not (ctx.bundle.payment_verbs.search(sent) and amount_text is not None):
        if re.search(r"\b(first|second|then|thereafter|pro\s+rata|pari\s+passu|true-up|setoff|deduct|net\s+of)\b", sent, re.I) and heading_prior_signals(ctx.source_ref, "transfers"):
            ctx.add_candidate("claim_classes", "waterfall_sequence", {"name": sent, "priority_rank": rank_from_text(sent), "claim_type": "waterfall"}, sent, ctx.source_ref, 0.58, ["waterfall_signal", "heading_prior"], anti)
        return
    # W6 T4 Item E: lead-in sentences ("X shall pay the Purchase Price as follows:")
    # introduce a payment list; the sentence itself is not a discrete transfer
    # candidate.  Suppress it by refusing to emit a candidate (split items from
    # the list will be the actual candidates).
    if _TRANSFER_LEAD_IN_RE.search(sent):
        return
    # W6 T4 Item E: conditional-trigger sentences (starting with "Advenant",
    # "In the event of", "En cas de") describe contingent indemnity obligations,
    # not direct transfers.  Demote by capping confidence below promote thresholds.
    _cond_trigger = _CONDITIONAL_TRIGGER_RE.search(sent)
    payer, payee = extract_payment_parties(sent)
    signals = ["payment_signal", *heading_prior_signals(ctx.source_ref, "transfers")]
    if payer:
        signals.append("known_party_subject" if ctx.is_known_subject(payer) else "payer_signal")
    if payee:
        signals.append("payee_signal")
    if has_deadline_signal(sent):
        signals.append("deadline_signal")
    if _cond_trigger:
        anti = [*anti, "conditional_transfer_trigger"]
    confidence = score_confidence(0.66, signals, anti)
    if _cond_trigger:
        # Hard cap below PROMOTE_WITH_CORROBORATION (0.65) to ensure hint tier.
        confidence = min(confidence, 0.50)
    value: dict[str, Any] = {"from_party": payer or "unspecified", "to_party": payee or "unspecified", "amount_text": amount_text, "description": sent, "timing": ctx.bundle.normalize_date(sent) or deadline_text(sent)}
    # Harvest-time amount parse (W3.3): the EN bundle defers (returns None) so
    # the EN payload never gains an "amount" key (goldens lock the shape); the
    # FR bundle parses locale formats here and materialize prefers value["amount"].
    amount = ctx.bundle.parse_amount(amount_text)
    if amount is not None:
        value["amount"] = amount
    ctx.add_candidate("transfers", "payment_flow", value, sent, ctx.source_ref, confidence, signals, anti)
