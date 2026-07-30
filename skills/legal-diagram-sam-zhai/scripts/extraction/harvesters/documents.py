from __future__ import annotations

import re

from ..context import HarvestContext
from ..utils import document_name, extract_subject, heading_prior_signals, is_rep_warranty, score_confidence

# Schedule/exhibit/annex reference pattern: fires when the sentence references
# a named schedule or exhibit.  Used to add rep_warranty_signal corroboration
# so the document candidate reaches the promotion threshold.
_SCHEDULE_REF_RE = re.compile(
    r"\b(?:Schedule(?:\s+No\.?)?\s*[A-Z0-9]+|Exhibit\s+[A-Z0-9]+|Annexe?\s*\d+"
    r"|set\s+forth\s+on\s+Schedule|disclosed\s+on\s+Schedule)\b",
    re.I,
)


def harvest_deliverables(ctx: HarvestContext, sent: str) -> None:
    if not ctx.bundle.document_patterns[0].search(sent):
        return
    anti = ctx.anti
    signals = ["deliverable_signal", *heading_prior_signals(ctx.source_ref, "documents")]
    if ctx.bundle.legal_action_verbs.search(sent):
        signals.append("legal_action_object")
    subject = extract_subject(sent)
    if ctx.is_known_subject(subject):
        signals.append("known_party_subject")
    # W6 T4 Item D: schedule/exhibit/annex references in rep-warranty or
    # condition sentences are structurally corroborated by the schedule mention
    # itself.  Use a higher base confidence and add qualifier_signal so the
    # candidate reaches the promotion threshold.
    base = 0.58
    if _SCHEDULE_REF_RE.search(sent):
        signals.append("qualifier_signal")
        if is_rep_warranty(sent):
            signals.append("rep_warranty_signal")
        # Schedule/exhibit references are concrete named documents; raise base
        # so they can reach PROMOTE_WITH_CORROBORATION (0.65).
        base = 0.66
    confidence = score_confidence(base, signals, anti)
    # W6 T4 Item D: document_name() returns "" when no specific document name
    # is found (bare generic words or full-sentence snippets are not useful
    # document names).  Skip emission to avoid promoting noise candidates.
    name = document_name(sent)
    if not name:
        return
    ctx.add_candidate("documents", "deliverable_document", {"name": name, "type": "deliverable", "parties": [subject] if subject else [], "description": sent}, sent, ctx.source_ref, confidence, signals, anti)
