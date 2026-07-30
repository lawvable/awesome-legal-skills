from __future__ import annotations

import re
from typing import Callable, Optional

from ..context import HarvestContext
from ..utils import condition_corrob_signals, deadline_text, extract_subject, heading_prior_signals, score_confidence

# W6 T4 Item B: FR closing-relative frames (pre_closing_deadline /
# post_closing_deadline) that lack a duration qualifier are bare covenant
# cross-references, not actionable deadlines.  A duration qualifier is one
# or more digits followed by a time unit (mois, jours, semaines, ans, heures).
_FR_DURATION_RE = re.compile(
    r"\b\d+\s+(?:mois|jours?(?:\s+ouvrables?)?|semaines?|ans?|heures?)\b",
    re.I,
)
# Frame names that require a duration qualifier in FR context.
_FR_CLOSING_RELATIVE_FRAMES = frozenset({"pre_closing_deadline", "post_closing_deadline"})

# ---------------------------------------------------------------------------
# Deadline timing phrase extractor (Work item 2 fix).
#
# When normalize_date and deadline_text both return None, m.group(0) alone is
# typically a partial phrase ("no later than", "fails to cure within", "cure
# period") with no temporal value.  Instead, extract the clause fragment
# starting from the match and running to the nearest clause boundary.
#
# Additionally: clamp description to the clause containing the match rather
# than the full joined paragraph sentence.
# ---------------------------------------------------------------------------

# Broader deadline phrase extractor: N business/calendar days <after|before|of|from>...
_DAYS_PERIOD_RE = re.compile(
    r"\b(?:within\s+)?\d+\s+(?:business\s+|calendar\s+|ouvrables?\s+)?days?"
    r"['\s]*(?:after|before|of|from|suivant|après|avant|de|prior\s+to)"
    r"(?:[^,;:.]{0,60})?",
    re.I,
)

# Hyphenated day-count forms: "15-business-day", "30-calendar-day", etc.
# Captured from sentences like "the 15-business-day cure period".
_HYPHEN_DAYS_RE = re.compile(
    r"\b(\d+)-(?:business|calendar|ouvrable)s?-days?\b[^,;:.]{0,50}",
    re.I,
)

# "N weeks/months <preposition>" phrase
_WEEKS_MONTHS_RE = re.compile(
    r"\b\d+\s+(?:weeks?|months?|semaines?|mois)\s+(?:after|before|following|prior\s+to|suivant|avant|après)\b[^,;:.\n]{0,60}",
    re.I,
)

# Guard for step 5: fragment must START with a temporal indicator to be useful.
# If the fragment starts with a verb or pronoun (trigger word, not time), skip it.
_TEMPORAL_FRAGMENT_START_RE = re.compile(
    r"^(?:within|no\s+later|not\s+later|on\s+or\s+before|at\s+or\s+before|prior\s+to"
    r"|before|after|following|upon|no\s+less|no\s+more|at\s+least|by\s+(?:the|closing|[A-Z])"
    r"|\d|january|february|march|april|may|june|july|august|september|october|november|december"
    r"|avant|après|dans\s+les|au\s+plus|moyennant|suite|suivant)",
    re.I,
)


def _extract_deadline_timing(
    sent: str,
    m: re.Match[str],
    bundle_normalize_date: Optional[Callable[[str], Optional[str]]],
) -> str:
    """Return the best deadline timing string for a matched sentence.

    Priority:
    1. bundle.normalize_date(sent) -- ISO date (FR) or verbatim EN date.
    2. deadline_text(sent) -- broader phrase like 'within 5 business days after'.
    3. _DAYS_PERIOD_RE broader extraction around match position.
    4. _WEEKS_MONTHS_RE broader extraction.
    5. Clause fragment starting from match position (up to 80 chars, capped at
       first clause boundary) so callers get a meaningful timing string even
       for 'cure period'-style matches.
    6. m.group(0) as absolute last resort.
    """
    # Step 1: normalize_date (callable on bundle)
    if bundle_normalize_date is not None:
        date_val = bundle_normalize_date(sent)
        if date_val:
            return date_val

    # Step 2: deadline_text
    dt = deadline_text(sent)
    if dt:
        return dt

    # Step 3: days-period phrase anywhere in sentence (also hyphenated forms).
    dp = _DAYS_PERIOD_RE.search(sent)
    if dp:
        return dp.group(0).strip().rstrip(",;: ")
    hd = _HYPHEN_DAYS_RE.search(sent)
    if hd:
        # Normalize: replace hyphens with spaces, then ensure plural "days" form
        # so "15-business-day cure period" → "15 business days cure period"
        normalized = hd.group(0).replace("-", " ").strip().rstrip(",;: ")
        normalized = re.sub(r"\bday\b", "days", normalized, count=1)
        return normalized

    # Step 4: weeks/months phrase
    wm = _WEEKS_MONTHS_RE.search(sent)
    if wm:
        return wm.group(0).strip().rstrip(",;: ")

    # Step 5: clause fragment from match position, capped at 80 chars.
    # Guard: skip if fragment does not start with a temporal indicator (e.g. when
    # the frame trigger is a verb phrase like "fails to cure within").
    start = m.start()
    tail = sent[start:]
    # Stop at first clause boundary (comma, semicolon, colon).
    ce = re.search(r"[,;:]", tail)
    if ce:
        fragment = tail[:ce.start()].strip()
    else:
        fragment = tail[:80].strip()
    if (fragment and len(fragment) > len(m.group(0))
            and _TEMPORAL_FRAGMENT_START_RE.match(fragment)):
        return fragment.rstrip(",;: ")

    # Step 6: raw match group
    return m.group(0)


# Procedural completion-reporting pattern: sentences whose primary purpose is
# reporting completion of another obligation (e.g. "report completion within N days").
# These are derivative deadlines, not primary ones; demote with two anti-signals.
_COMPLETION_REPORT_DEADLINE_RE = re.compile(
    r"\breport(?:ing)?\s+completion\b|\breport(?:ing)?\s+satisfaction\b",
    re.I,
)


def harvest_deadlines(ctx: HarvestContext, sent: str) -> None:
    for frame, rx, base in ctx.bundle.deadline_frames:
        m = rx.search(sent)
        if not m:
            continue
        signals = [frame, "deadline_signal", *heading_prior_signals(ctx.source_ref, "deadlines")]
        if condition_corrob_signals(sent):
            signals.append("trigger_signal")
        if ctx.bundle.legal_action_verbs.search(sent):
            signals.append("legal_action_object")
        anti = ctx.anti
        confidence = score_confidence(base, signals, anti)
        if re.search(r"\bpromptly\b", sent, re.I) and not re.search(r"\b(after|following|upon|receipt)\b", sent, re.I):
            confidence = min(confidence, 0.44)
            anti = [*anti, "promptly_without_trigger"]
        # Procedural completion-reporting: "report completion within N days" is a
        # derivative deadline (about reporting, not the primary obligation).
        # Add two anti-signals to demote below promote tier.
        if _COMPLETION_REPORT_DEADLINE_RE.search(sent):
            anti = [*anti, "completion_report", "derivative_deadline"]
            confidence = score_confidence(base, signals, anti)
        # W6 T4 Item B: FR closing-relative deadlines without a duration
        # qualifier are bare covenant cross-references (e.g. "avant la Clôture"
        # alone in an obligation clause), not standalone actionable deadlines.
        # Demote them to hint by capping confidence below PROMOTE_WITH_CORROBORATION.
        # A sentence with a duration (e.g. "dans les 18 mois suivant la Clôture")
        # passes through unchanged because deadline_text() will also match.
        if frame in _FR_CLOSING_RELATIVE_FRAMES and not _FR_DURATION_RE.search(sent):
            confidence = min(confidence, 0.44)
            anti = [*anti, "closing_relative_no_duration"]
        # W6 T4 Item B: EN hard_deadline with an explicit calendar date (e.g.
        # "on or before February 20, 2026") should not be demoted below
        # PROMOTE_WITH_CORROBORATION solely because of an incidental
        # "including" in the middle of the sentence.  Remove including_example
        # from anti when the frame is hard_deadline and a calendar date is present.
        if frame == "hard_deadline" and "including_example" in anti and ctx.bundle.normalize_date is not None:
            if ctx.bundle.normalize_date(sent):
                anti = [a for a in anti if a != "including_example"]
                confidence = score_confidence(base, signals, anti)
        timing = _extract_deadline_timing(sent, m, ctx.bundle.normalize_date)
        ctx.add_candidate("deadlines", frame, {"date_or_timing": timing, "description": sent, "party": extract_subject(sent) or None}, sent, ctx.source_ref, confidence, signals, anti)


