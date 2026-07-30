from __future__ import annotations

import re

from ..context import HarvestContext
from ..utils import anti_penalty, extract_subject, score_confidence

# Future/hypothetical markers: when present in the occurrence-verb branch the
# candidate confidence is capped at 0.44 so it never promotes.
# W6 T3: also used to suppress the litigation-action promotion branch so that
# prospective sentences ("the trial was scheduled to proceed on X") stay below
# the promotion threshold.
#
# "may" is the modal verb (permission/possibility), not the month.  Month "May"
# is always followed by a digit or a comma, whereas modal "may" is followed by
# a verb infinitive.  We use a negative lookahead on digits to exclude the month.
# "to be" is a genuine future marker only when it is not embedded in a past
# factual statement like "remained to be tried" -- we exclude it when preceded
# by a past-tense verb ("remained", "found", "ordered", etc.) to avoid false
# caps on judgment sentences that describe what was left undecided.
_FUTURE_HYPOTHETICAL = re.compile(
    r"\b(shall|will|must|should|if|in the event|subject to|provided that|once|when)\b"
    r"|(?<!\w)may(?!\s+\d)(?!\s*,)(?!\s+(?:Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|June|July|August|September|October|November|December))\b"
    r"|\bto\s+be\b(?!\s+(?:tried|determined|assessed|heard|argued|decided))",
    re.I,
)

# Metadata-header sentinel: lines of the form "**Label :** value" or "**Label:** value"
# are document header fields (date, court, citation), not event sentences.
# The colon may appear INSIDE the bold markers ("**Date du jugement :**") or
# OUTSIDE ("**Label:**").
# Harvesting events from these lines produces FPs because the same date is
# also captured by the substantive prose sentence that references the event.
_METADATA_HEADER_RE = re.compile(
    r"^\*\*[^*]+:?\s*\*\*\s*:?",  # "**Label:**" or "**Label :**" (colon inside or outside)
    re.I,
)

# Frame families keyed by representative verb patterns.
_HEARING_RE = re.compile(r"\b(heard|convened|adjourned)\b", re.I)
_FILING_RE = re.compile(r"\b(filed|served|registered)\b", re.I)
_ORDER_RE = re.compile(
    r"\b(issued|rendered|released|decided|dismissed|granted|allowed|denied|pronounced|sentenced|convicted|acquitted)\b",
    re.I,
)
_TRANSACTION_RE = re.compile(
    r"\b(executed|signed|entered\s+into|closed|incorporated|amalgamated)\b",
    re.I,
)

# ---------------------------------------------------------------------------
# W6 T3: Litigation-action context signals for date-only event candidates.
#
# These are factual past-tense actions that appear in judgment procedural
# histories but do not use the "occurrence verbs" vocabulary (sent, wrote,
# engaged, held, was heard, conference was held, etc.).
# The pattern fires on sentences that carry a date AND a past-action verb;
# when it fires the hint-tier event is bumped to promotion band (0.66).
# Precision guard: the sentence must NOT match _FUTURE_HYPOTHETICAL so
# that prospective sentences ("the trial was scheduled to proceed on X")
# stay below the promotion threshold.
# ---------------------------------------------------------------------------
_LITIGATION_ACTION_RE = re.compile(
    r"\b("
    # Communication / correspondence verbs
    r"sent|wrote|notified|responded|replied|informed|advised|disputed|demanded|"
    # Engagement / action verbs
    r"engaged|retained|appointed|commenced|terminated|purported|"
    # Court-hearing constructs (not in _OCCURRENCE_VERBS)
    r"(?:was\s+)?held\s+on|(?:was\s+)?convened\s+on|(?:conference\s+was\s+held)|"
    r"(?:motion\s+was\s+dismissed)|(?:motion\s+was\s+heard)|"
    r"(?:was\s+dismissed)|(?:was\s+heard)|"
    # Date-of-judgment / court date headers
    r"date\s+of\s+(?:judgment|hearing|trial|decision|order)|"
    r"judgment\s+dated|hearing\s+date|trial\s+date|order\s+dated|"
    # FR equivalents
    r"a\s+envoyé|a\s+écrit|a\s+notifié|a\s+contesté|a\s+demandé|a\s+retenu|"
    r"a\s+nommé|a\s+rejeté|a\s+été\s+entendu|"
    r"date\s+du\s+jugement|date\s+de\s+l['']audience"
    r")\b",
    re.I,
)


def _frame_type(sent: str) -> str:
    """Return the frame type based on the occurrence verb family present in the sentence."""
    if _HEARING_RE.search(sent):
        return "hearing_event"
    if _FILING_RE.search(sent):
        return "filing_event"
    if _ORDER_RE.search(sent):
        return "order_event"
    if _TRANSACTION_RE.search(sent):
        return "transaction_event"
    return "dated_event"


def harvest_event(ctx: HarvestContext, sent: str) -> None:
    """Harvest factual/procedural dated events from a sentence.

    Fires only when a full date is present. With an occurrence verb the candidate
    is emitted at base confidence 0.66 (promotes at the 0.65 corroborated band).
    Without an occurrence verb the candidate is emitted at 0.42 (hint only),
    unless the sentence carries a litigation-action verb (W6 T3), in which case
    confidence is bumped to 0.66 (corroboration-promotion band).
    """
    date_match = ctx.bundle.date_re.search(sent)
    if not date_match:
        return

    # Bundle date normalisation (W3.3): EN returns the first date_re match
    # verbatim (identical to date_match.group(0)); FR returns ISO 8601.
    date_text = ctx.bundle.normalize_date(sent) or date_match.group(0)
    anti = ctx.anti

    if ctx.bundle.occurrence_verbs.search(sent):
        frame = _frame_type(sent)
        signals = [frame, "date_signal", "event_verb"]
        confidence = score_confidence(0.66, signals, anti)
        # Guard: future/hypothetical markers indicate the verb describes a
        # potential or required action, not a confirmed factual past event.
        # Cap confidence below the promotion threshold and add an anti-signal.
        if _FUTURE_HYPOTHETICAL.search(sent):
            confidence = min(confidence, 0.44)
            signals = signals + ["future_or_hypothetical"]
        value = {
            "date_or_timing": date_text,
            "description": sent,
            "actor": extract_subject(sent) or None,
        }
        ctx.add_candidate("events", frame, value, sent, ctx.source_ref, confidence, signals, anti)
    else:
        # Date present but no occurrence verb.
        # W6 T3: if the sentence carries a litigation-action verb context and
        # no future/hypothetical marker, bump to corroboration-promotion band.
        # Exclude metadata-header lines ("**Date du jugement :** value") from the
        # litigation-action promotion: these are header fields, not event sentences.
        # They still emit as hints (0.42) so combined recall is preserved when
        # the same date does not appear in any prose sentence.
        # Otherwise emit a low-confidence hint only.
        signals = ["date_signal"]
        if (
            _LITIGATION_ACTION_RE.search(sent)
            and not _FUTURE_HYPOTHETICAL.search(sent)
            and not _METADATA_HEADER_RE.match(sent)
        ):
            signals = [*signals, "litigation_action_context", "event_verb"]
            confidence = score_confidence(0.66, signals, anti)
        else:
            confidence = 0.42 - anti_penalty(anti)
        value = {
            "date_or_timing": date_text,
            "description": sent,
        }
        ctx.add_candidate("events", "dated_event", value, sent, ctx.source_ref, confidence, signals, anti)
