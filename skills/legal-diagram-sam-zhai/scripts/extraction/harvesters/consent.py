from __future__ import annotations

import re
from typing import Optional

from ..lexicon import get_bundle
from ..schema import Candidate, SourceRef
from ..utils import anti_signals, clamp, extract_subject, score_confidence


def harvest_consent_discretion(
    sent: str,
    candidates: list[Candidate],
    heading_path: Optional[list[str]] = None,
    lang: str = "en",
) -> None:
    """Standalone consent/discretion harvester.

    Matches consent, approval, discretion, veto, and waiver patterns in *sent*
    and appends :class:`~extraction.schema.Candidate` objects directly to
    *candidates*.  No harvester orchestrator is required.

    Patterns are bundle-sourced per *lang* (W3); the "en" default preserves
    the pre-W3 behaviour exactly for callers without language information.

    Args:
        sent: The sentence text to analyse.
        candidates: Mutable list; matched candidates are appended in place.
        heading_path: Optional heading context for the candidate source ref.
        lang: Language code for pattern selection ("en"/"fr"; default "en").
    """
    if heading_path is None:
        heading_path = []
    bundle = get_bundle(lang)
    anti = anti_signals(sent)
    source_ref = SourceRef(heading_path=list(heading_path))
    for frame, rx, base in bundle.consent_patterns:
        if not rx.search(sent):
            continue
        subject = extract_subject(sent)
        signals = [frame]
        if bundle.legal_action_verbs.search(sent):
            signals.append("legal_action_object")
        confidence = score_confidence(base, signals, anti)
        if re.search(r"\bmay\b", sent, re.I) and "legal_action_object" not in signals:
            confidence = min(confidence, 0.44)
        confidence = clamp(confidence)
        cid = f"C{len(candidates):04d}"
        candidates.append(
            Candidate(
                id=cid,
                target_field="decision_points",
                frame_type=frame,
                normalized_value={
                    "question": sent,
                    "subject": subject,
                    "yes_path": "permitted/approved",
                    "no_path": "blocked/not approved",
                },
                signals=signals,
                anti_signals=anti,
                confidence=confidence,
                evidence_ids=[],
                source_ref=source_ref,
            )
        )
