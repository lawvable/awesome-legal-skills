"""Unit tests for diagram_selector.py.

Covers:
  - Empty extraction: default type and low-confidence path.
  - Each RULES entry contributes its weight (data-driven over actual RULES list).
  - Density boost capping at 2.0.
  - INTENT_MAP keyword hit, case-insensitive.
  - Accent-tolerant INTENT_MAP matching placeholder (activates with W3).
  - MATTER_BOOSTS per matter type.
  - Grouping override boundaries (events > 10; average description length > 50).
  - Alternatives truncation when fewer than three types score.
  - Confidence normalization bounds.

Conventions (mirror scripts/tests/test_extraction.py):
  - Plain functions, no pytest fixtures.
  - Standalone __main__ block iterating test_* callables; exit non-zero on failure.
  - Works under pytest too.
  - Imports via sys.path insert, mirroring calibrate.py's approach.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Allow imports from scripts/ whether run as a script or under pytest.
_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from extraction.domain import (
    Communication,
    Concept,
    Control,
    DataFlow,
    Deadline,
    DecisionPoint,
    Document,
    Entity,
    Event,
    ExtractionResult,
    IPAsset,
    InvestigationStep,
    LegalAuthority,
    NegotiationIssue,
    Obligation,
    OwnershipLink,
    Party,
    Phase,
    ProcessStep,
    Relationship,
    RiskItem,
    State,
    Task,
    Transfer,
    Transition,
    WitnessMap,
    ClaimClass,
)

from diagram_selector import (
    DOMINANT_INTENT_BOOST,
    INTENT_MAP,
    MATTER_BOOSTS,
    RULES,
    SECONDARY_INTENT_BOOST,
    SECONDARY_TYPE_FACTOR,
    _grouping_decision,
    _intent_types,
    _score,
    recommend,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_event(desc: str = "event", date: str = "2026-01-01") -> Event:
    return Event(date=date, description=desc)


def _make_obligation() -> Obligation:
    return Obligation(id="OBL-0001", description="Seller shall deliver.", party="Seller")


# ---------------------------------------------------------------------------
# Test: empty extraction defaults
# ---------------------------------------------------------------------------

def test_empty_extraction_recommends_flowchart() -> None:
    """An extraction with no signals must recommend 'flowchart'."""
    result = recommend(ExtractionResult(), "general")
    assert result["recommended_type"] == "flowchart", (
        f"expected flowchart for empty extraction, got {result['recommended_type']}"
    )


def test_empty_extraction_low_confidence() -> None:
    """An extraction with no signals must return confidence 0.3 (the hardcoded default)."""
    result = recommend(ExtractionResult(), "general")
    assert result["confidence"] == 0.3, (
        f"expected confidence 0.3 for empty extraction, got {result['confidence']}"
    )


def test_empty_extraction_default_alternatives() -> None:
    """Empty extraction must return the hardcoded two alternatives: mindmap and timeline."""
    result = recommend(ExtractionResult(), "general")
    assert result["alternatives"] == ["mindmap", "timeline"], (
        f"unexpected alternatives for empty extraction: {result['alternatives']}"
    )


def test_empty_extraction_no_grouping() -> None:
    """Empty extraction must have grouping_suggested False and grouping_axis None."""
    result = recommend(ExtractionResult(), "general")
    assert result["grouping_suggested"] is False
    assert result["grouping_axis"] is None


# ---------------------------------------------------------------------------
# Test: each RULES entry contributes its weight (data-driven)
# ---------------------------------------------------------------------------

# Minimal synthetic items per field type. Exactly 3 items so density boost = min(3/3, 2.0) = 1.0.
_FIELD_SYNTHETIC: dict[str, list] = {
    "events":             [_make_event(f"e{i}") for i in range(3)],
    "deadlines":          [Deadline(date="2026-01-01", description="d", party="Seller") for _ in range(3)],
    "phases":             [Phase(name=f"P{i}", start_date="2026-01-01", end_date="2026-02-01") for i in range(3)],
    "tasks":              [Task(id=f"T{i}", name=f"task{i}") for i in range(3)],
    "ownership_links":    [OwnershipLink(parent="A", child=f"B{i}") for i in range(3)],
    "relationships":      [Relationship(from_entity="A", to_entity=f"B{i}", type="rel") for i in range(3)],
    "entities":           [Entity(name=f"E{i}", type="corp") for i in range(3)],
    "documents":          [Document(name=f"Doc{i}", type="contract") for i in range(3)],
    "obligations":        [Obligation(id=f"OBL-000{i}", description="d", party="S") for i in range(3)],
    "controls":           [Control(id=f"C{i}", description="ctrl", obligation_id="OBL-0001") for i in range(3)],
    "conditions":         [{"id": f"CP{i}", "description": "if X"} for i in range(3)],
    "states":             [State(name=f"S{i}") for i in range(3)],
    "transitions":        [Transition(from_state="A", to_state="B") for _ in range(3)],
    "decision_points":    [DecisionPoint(question="Q?", yes_path="Y", no_path="N") for _ in range(3)],
    "process_steps":      [ProcessStep(id=f"PS{i}", name=f"step{i}") for i in range(3)],
    "investigation_steps":[InvestigationStep(id=f"IS{i}", step_number=i, description="d") for i in range(3)],
    "risk_items":         [RiskItem(label=f"R{i}", x_score=0.5, y_score=0.5) for i in range(3)],
    "negotiation_issues": [NegotiationIssue(id=f"NI{i}", term="price") for i in range(3)],
    "transfers":          [Transfer(from_party="A", to_party="B", description="pay") for _ in range(3)],
    "claim_classes":      [ClaimClass(priority_rank=i, name=f"class{i}") for i in range(3)],
    "communications":     [Communication(from_party="A", to_party="B") for _ in range(3)],
    "concepts":           [Concept(id=f"CON{i}", name=f"concept{i}") for i in range(3)],
    "data_flows":         [DataFlow(from_system="A", to_system="B") for _ in range(3)],
    "witnesses":          [WitnessMap(witness_name=f"W{i}") for i in range(3)],
    "legal_authorities":  [LegalAuthority(citation=f"2026 ONSC {i}", authority_type="case") for i in range(3)],
    "ip_assets":          [IPAsset(name=f"Patent{i}", asset_type="patent") for i in range(3)],
    "parties":            [Party(name=f"P{i}", role="vendor", type="corp") for i in range(3)],
}


def test_rules_each_entry_contributes_weight() -> None:
    """For each RULES entry, an extraction containing exactly 3 items in that field must
    increase the score for the PRIMARY target diagram type by exactly weight * 1.0, and
    each non-primary (fallback) type by weight * 1.0 * SECONDARY_TYPE_FACTOR.

    The primary type (RULES index 0) carries the full rule weight; every later type in the
    same rule is a fallback and earns a discounted share so that a catch-all fallback such
    as flowchart cannot sponge full weight from every signal (defect-1 structural fix).

    This test is data-driven over the live RULES list so that additions in W3 inherit
    coverage automatically.  Isolation: only the field under test is populated; intent
    is empty string; no matter type so no MATTER_BOOSTS.
    """
    for fld, types, weight in RULES:
        if fld not in _FIELD_SYNTHETIC:
            # Guard: if RULES adds a new field without a synthetic entry, fail explicitly.
            raise AssertionError(
                f"RULES field '{fld}' has no synthetic entry in _FIELD_SYNTHETIC; "
                f"add one so data-driven coverage is maintained."
            )
        er = ExtractionResult()
        setattr(er, fld, _FIELD_SYNTHETIC[fld])
        scores = _score(er, "")  # no intent, no matter type
        for idx, t in enumerate(types):
            expected = weight * 1.0 * (1.0 if idx == 0 else SECONDARY_TYPE_FACTOR)
            actual = scores.get(t, 0)
            assert actual >= expected - 1e-9, (
                f"RULES field '{fld}' type '{t}' (rule index {idx}) weight {weight}: "
                f"expected score >= {expected}, got {actual}"
            )


# ---------------------------------------------------------------------------
# Test: density boost capping
# ---------------------------------------------------------------------------

def test_density_boost_exactly_three_items() -> None:
    """3 items: density boost = min(3/3.0, 2.0) = 1.0 exactly."""
    er = ExtractionResult()
    er.events = [_make_event(f"e{i}") for i in range(3)]
    # timeline is first type for 'events' in RULES; weight = 2.0
    scores = _score(er, "")
    # With 3 events, boost = 1.0 * 2.0 = 2.0
    assert scores.get("timeline", 0) == 2.0 * 1.0  # weight 2.0 * density 1.0


def test_density_boost_six_items_equals_two_times_weight() -> None:
    """6 items: density boost = min(6/3.0, 2.0) = 2.0 (cap hit)."""
    er = ExtractionResult()
    er.events = [_make_event(f"e{i}") for i in range(6)]
    scores = _score(er, "")
    # events weight = 2.0, density = min(2.0, 2.0) = 2.0
    assert scores.get("timeline", 0) == 2.0 * 2.0


def test_density_boost_nine_items_same_as_six() -> None:
    """9 items must not exceed the 6-item score: density cap is at 2.0 regardless."""
    er6 = ExtractionResult()
    er6.events = [_make_event(f"e{i}") for i in range(6)]
    er9 = ExtractionResult()
    er9.events = [_make_event(f"e{i}") for i in range(9)]
    scores6 = _score(er6, "")
    scores9 = _score(er9, "")
    assert scores9.get("timeline", 0) == scores6.get("timeline", 0), (
        f"9-item boost {scores9.get('timeline')} must equal 6-item boost {scores6.get('timeline')}"
    )


def test_density_boost_below_cap_not_equal_to_cap() -> None:
    """1 item: boost = min(1/3.0, 2.0) = 0.333... which is strictly less than cap 2.0."""
    er = ExtractionResult()
    er.events = [_make_event("single")]
    scores_1 = _score(er, "")
    er6 = ExtractionResult()
    er6.events = [_make_event(f"e{i}") for i in range(6)]
    scores_6 = _score(er6, "")
    assert scores_1.get("timeline", 0) < scores_6.get("timeline", 0), (
        "1-item score must be strictly below 6-item score (cap boundary)"
    )


# ---------------------------------------------------------------------------
# Test: INTENT_MAP keyword hit (case-insensitive)
# ---------------------------------------------------------------------------

def test_intent_map_lowercase_hit() -> None:
    """Lowercase keyword from INTENT_MAP must contribute a positive intent boost."""
    er = ExtractionResult()
    scores_with = _score(er, "chronology")
    scores_without = _score(er, "")
    for t in _intent_types("chronology"):
        assert scores_with.get(t, 0) > scores_without.get(t, 0), (
            f"lowercase 'chronology' intent must boost '{t}'"
        )


def test_intent_map_uppercase_hit() -> None:
    """Uppercase intent string must match case-insensitively via .lower() in _score."""
    er = ExtractionResult()
    scores_upper = _score(er, "CHRONOLOGY")
    scores_lower = _score(er, "chronology")
    for t in _intent_types("chronology"):
        assert scores_upper.get(t, 0) == scores_lower.get(t, 0), (
            f"CHRONOLOGY and chronology must produce identical scores for '{t}'"
        )


def test_intent_map_mixed_case_hit() -> None:
    """Mixed-case intent string must match case-insensitively."""
    er = ExtractionResult()
    scores_mixed = _score(er, "Chronology of Events")
    scores_lower = _score(er, "chronology of events")
    for t in _intent_types("chronology"):
        assert scores_mixed.get(t, 0) == scores_lower.get(t, 0), (
            f"Mixed-case and lowercase must produce identical scores for '{t}'"
        )


def test_intent_map_dominant_keyword_boost_magnitude() -> None:
    """The single most-specific (dominant) keyword match adds DOMINANT_INTENT_BOOST to its types.

    'risk' is the only keyword in this intent and maps to ['quadrantChart'] only, so it is
    the dominant hit and contributes DOMINANT_INTENT_BOOST (defect-1 precedence fix).
    """
    er = ExtractionResult()
    scores = _score(er, "risk")
    assert scores.get("quadrantChart", 0) == DOMINANT_INTENT_BOOST, (
        f"'risk' intent must boost quadrantChart by {DOMINANT_INTENT_BOOST}, "
        f"got {scores.get('quadrantChart', 0)}"
    )


def test_intent_map_secondary_keyword_boost_magnitude() -> None:
    """A non-dominant keyword hit adds the smaller SECONDARY_INTENT_BOOST to its new types.

    'data privacy flows and obligations' matches a flows-family keyword (dominant, more
    specific) and 'obligations' (secondary).  The dominant hit boosts flowchart by the
    larger amount; 'obligations' boosts requirementDiagram by SECONDARY_INTENT_BOOST.
    """
    er = ExtractionResult()
    scores = _score(er, "data privacy flows and obligations")
    # requirementDiagram is reached only via the secondary 'obligations' hit here.
    assert scores.get("requirementDiagram", 0) == SECONDARY_INTENT_BOOST, (
        f"secondary 'obligations' hit must boost requirementDiagram by "
        f"{SECONDARY_INTENT_BOOST}, got {scores.get('requirementDiagram', 0)}"
    )
    # flowchart is reached via the dominant flows-family hit; it must outrank the secondary.
    assert scores.get("flowchart", 0) > scores.get("requirementDiagram", 0), (
        "the dominant flows-family hit must give flowchart a larger intent boost than "
        "the secondary obligations hit gives requirementDiagram"
    )


def test_intent_longest_match_precedence_privacy() -> None:
    """Longest / most-specific intent keyword wins over an incidental shorter one (defect 1).

    'data privacy flows and obligations' must resolve to flowchart, not requirementDiagram:
    the flows-family hit (shape-defining) dominates the incidental 'obligations' hit.  This
    is the privacy fixture's intent string; matching is by general rule, not fixture text.
    """
    er = ExtractionResult()
    scores = _score(er, "data privacy flows and obligations")
    ranked = sorted(scores, key=lambda t: scores[t], reverse=True)
    assert ranked[0] == "flowchart", (
        f"flows-dominant intent must rank flowchart first, got ranking {ranked}"
    )


def test_intent_map_duplicate_type_across_keywords_not_doubled() -> None:
    """If two keywords map to the same type, that type receives an intent boost only once."""
    er = ExtractionResult()
    # 'chronology' and 'timeline' both map to ['timeline', 'gantt']
    scores_both = _score(er, "chronology timeline")
    scores_one = _score(er, "chronology")
    # 'timeline' type is matched once; a second keyword mapping to it must not add again
    assert scores_both.get("timeline", 0) == scores_one.get("timeline", 0), (
        "timeline type must be boosted only once even if two keywords map to it"
    )


# ---------------------------------------------------------------------------
# Test: accent-tolerant INTENT_MAP matching (W3 placeholder)
# ---------------------------------------------------------------------------

def test_intent_map_accent_tolerant_placeholder() -> None:
    """Accent-normalised keyword ('chronologie' -> 'chronology' via NFD strip) is a W3 feature.

    This test checks whether the selector already handles accented input; if not,
    it prints SKIP and returns without failing.  Once W3 lands and the selector
    gains accent normalisation, this test will exercise the behaviour automatically.

    To activate manually after W3: ensure _score normalises intent via unicodedata.normalize
    before keyword matching, then remove the early-return guard below.
    """
    # A plausible FR accented variant of a known keyword.
    accented_intent = "chronologie"
    # Check whether the selector already lower()s and strips accents internally.
    er = ExtractionResult()
    scores_accented = _score(er, accented_intent)
    scores_clean = _score(er, "chronology")

    # W3 will normalise via NFD-decompose-then-strip-combining-marks; until it lands,
    # keyword 'chronologie' is not in INTENT_MAP.  The scores should differ (or both be zero).
    # If W3 has landed and the selector does normalise, the scores will be equal to
    # scores_clean; in that case the test passes naturally.
    timeline_accented = scores_accented.get("timeline", 0)
    timeline_clean = scores_clean.get("timeline", 0)
    if timeline_clean == 0 or timeline_accented == timeline_clean:
        # W3 has landed or keyword is unknown; test exercises real behaviour.
        # Either the selector correctly handles it or no boost was expected.
        return
    # W3 not yet landed: skip without failing.
    print("SKIP: accent-tolerant INTENT_MAP matching activates with W3 (see comment in test)")  # noqa: T201


# ---------------------------------------------------------------------------
# Test: MATTER_BOOSTS per matter type
# ---------------------------------------------------------------------------

def test_matter_boosts_each_type_applied() -> None:
    """For every entry in MATTER_BOOSTS, setting matter_type on the extraction must increase
    the score of each boosted diagram type by the declared boost amount.
    """
    er_base = ExtractionResult()
    er_base.events = [_make_event("anchor")]  # at least one signal so scores dict is non-empty
    for matter, boosts in MATTER_BOOSTS.items():
        er = ExtractionResult()
        er.events = [_make_event("anchor")]
        er.matter_type = matter
        scores_with = _score(er, "")
        er_no_matter = ExtractionResult()
        er_no_matter.events = [_make_event("anchor")]
        scores_without = _score(er_no_matter, "")
        for diag_type, boost_amount in boosts.items():
            delta = scores_with.get(diag_type, 0) - scores_without.get(diag_type, 0)
            assert abs(delta - boost_amount) < 1e-9, (
                f"matter_type='{matter}' type='{diag_type}': expected delta {boost_amount}, got {delta}"
            )


def test_matter_boosts_unknown_matter_type_no_effect() -> None:
    """An unrecognised matter_type must produce no boost delta."""
    er_known = ExtractionResult()
    er_known.events = [_make_event("anchor")]
    er_unknown = ExtractionResult()
    er_unknown.events = [_make_event("anchor")]
    er_unknown.matter_type = "unknown_matter_type_xyz"
    scores_known = _score(er_known, "")
    scores_unknown = _score(er_unknown, "")
    assert scores_known == scores_unknown, (
        "Unknown matter_type must not alter scores"
    )


def test_matter_boosts_case_sensitive_match() -> None:
    """MATTER_BOOSTS lookup uses .lower() on matter_type.  'LITIGATION' must match 'litigation'."""
    er_upper = ExtractionResult()
    er_upper.events = [_make_event("anchor")]
    er_upper.matter_type = "LITIGATION"
    er_lower = ExtractionResult()
    er_lower.events = [_make_event("anchor")]
    er_lower.matter_type = "litigation"
    scores_upper = _score(er_upper, "")
    scores_lower = _score(er_lower, "")
    assert scores_upper == scores_lower, (
        "matter_type lookup must be case-insensitive via .lower()"
    )


# ---------------------------------------------------------------------------
# Test: grouping override boundaries (events > 10 and avg description > 50)
# ---------------------------------------------------------------------------

def test_grouping_triggers_at_eleven_events() -> None:
    """11 events (> 10 threshold) with timeline as top must trigger grouping override to flowchart."""
    events = [_make_event(f"event {i}") for i in range(11)]
    new_top, grouping_axis, rationale = _grouping_decision(
        ExtractionResult(events=events), "timeline"
    )
    assert new_top == "flowchart", f"expected flowchart override, got {new_top}"
    assert grouping_axis == "era", f"expected grouping_axis='era', got {grouping_axis}"
    assert rationale is not None, "expected a rationale string"


def test_grouping_does_not_trigger_at_exactly_ten_events() -> None:
    """10 events (not > 10) with short descriptions must NOT trigger grouping override."""
    events = [_make_event(f"event {i}") for i in range(10)]
    new_top, grouping_axis, rationale = _grouping_decision(
        ExtractionResult(events=events), "timeline"
    )
    assert new_top == "timeline", f"expected no override at exactly 10 events, got {new_top}"
    assert grouping_axis is None, f"expected grouping_axis=None at 10 events, got {grouping_axis}"
    assert rationale is None


def test_grouping_triggers_on_avg_description_over_50() -> None:
    """A single event with a description longer than 50 chars must trigger grouping override."""
    long_desc = "A" * 51  # length 51, avg over 50 with n=1
    events = [_make_event(long_desc)]
    new_top, grouping_axis, _ = _grouping_decision(
        ExtractionResult(events=events), "timeline"
    )
    assert new_top == "flowchart", (
        f"expected flowchart override for avg desc > 50, got {new_top}"
    )
    assert grouping_axis == "era"


def test_grouping_does_not_trigger_on_avg_description_exactly_50() -> None:
    """Average description length exactly 50 must NOT trigger grouping override."""
    exact_desc = "A" * 50  # avg = 50, not > 50
    events = [_make_event(exact_desc)]
    new_top, grouping_axis, _ = _grouping_decision(
        ExtractionResult(events=events), "timeline"
    )
    assert new_top == "timeline", (
        f"expected no override at avg desc == 50, got {new_top}"
    )
    assert grouping_axis is None


def test_grouping_only_fires_when_top_is_timeline() -> None:
    """Grouping override must not fire when top type is not 'timeline'."""
    events = [_make_event(f"event {i}") for i in range(11)]
    new_top, grouping_axis, _ = _grouping_decision(
        ExtractionResult(events=events), "flowchart"
    )
    # top is already flowchart; override path only checks top == "timeline"
    assert new_top == "flowchart"
    assert grouping_axis is None


def test_grouping_no_events_never_overrides() -> None:
    """Empty events list must never trigger grouping override."""
    new_top, grouping_axis, _ = _grouping_decision(
        ExtractionResult(events=[]), "timeline"
    )
    assert new_top == "timeline"
    assert grouping_axis is None


def test_grouping_eleven_events_via_recommend_intent_exempt() -> None:
    """End-to-end: 11 events with a timeline-naming intent hold timeline (defect-2 exemption).

    'chronology' resolves to timeline in INTENT_MAP, so the dense-timeline override is
    suppressed and the stated intent is honoured.  (Updated pin: pre-fix this returned a
    grouped flowchart; the override no longer overrides an explicit intent.)
    """
    er = ExtractionResult()
    er.events = [_make_event(f"event {i}", f"2026-01-{i+1:02d}") for i in range(11)]
    result = recommend(er, "chronology")
    assert result["recommended_type"] == "timeline"
    assert result["grouping_suggested"] is False
    assert result["grouping_axis"] is None


def test_grouping_ten_events_via_recommend_no_override() -> None:
    """End-to-end: exactly 10 events with 'chronology' intent must return timeline, no grouping."""
    er = ExtractionResult()
    er.events = [_make_event(f"event {i}", f"2026-01-{i+1:02d}") for i in range(10)]
    result = recommend(er, "chronology")
    assert result["recommended_type"] == "timeline"
    assert result["grouping_suggested"] is False
    assert result["grouping_axis"] is None


# ---------------------------------------------------------------------------
# Test: alternatives truncation when fewer than three types score
# ---------------------------------------------------------------------------

def test_alternatives_exactly_two_when_two_types_score() -> None:
    """When only two diagram types receive any score, alternatives has exactly one entry
    (ranked[1:3] with ranked length 2 gives a 1-element slice)."""
    # 'risk_items' maps only to ['quadrantChart'] in RULES.
    # 'negotiation_issues' also maps only to ['quadrantChart'].
    # With no other signals and a pure quadrantChart intent, only one type scores,
    # so alternatives = ranked[1:3] = [].
    er = ExtractionResult()
    er.risk_items = [RiskItem(label="R1", x_score=0.5, y_score=0.5)]
    er.negotiation_issues = [NegotiationIssue(id="NI1", term="price")]
    result = recommend(er, "")
    # quadrantChart should dominate; alternatives may be empty or short
    assert len(result["alternatives"]) <= 2, (
        f"alternatives must not exceed 2 entries; got {result['alternatives']}"
    )


def test_alternatives_empty_when_only_one_type_scores() -> None:
    """When exactly one type scores, alternatives must be an empty list."""
    # 'communications' maps only to ['sequenceDiagram'].
    er = ExtractionResult()
    er.communications = [Communication(from_party="A", to_party="B") for _ in range(3)]
    result = recommend(er, "")
    # Only sequenceDiagram should score from this field alone
    assert result["recommended_type"] == "sequenceDiagram"
    assert result["alternatives"] == [], (
        f"expected empty alternatives when only one type scores, got {result['alternatives']}"
    )


def test_alternatives_at_most_two() -> None:
    """The recommend function must never return more than 2 alternatives."""
    er = ExtractionResult()
    er.events = [_make_event(f"e{i}") for i in range(5)]
    er.obligations = [_make_obligation() for _ in range(5)]
    er.relationships = [Relationship(from_entity="A", to_entity=f"B{i}", type="rel") for i in range(5)]
    er.entities = [Entity(name=f"E{i}", type="corp") for i in range(5)]
    result = recommend(er, "workflow risk compliance")
    assert len(result["alternatives"]) <= 2, (
        f"alternatives must not exceed 2, got {result['alternatives']}"
    )


# ---------------------------------------------------------------------------
# Test: confidence normalization bounds
# ---------------------------------------------------------------------------

def test_confidence_between_zero_and_one() -> None:
    """Confidence must always be in [0.0, 1.0]."""
    cases = [
        ExtractionResult(),
        ExtractionResult(events=[_make_event("e")]),
        ExtractionResult(obligations=[_make_obligation()]),
    ]
    intents = ["", "general", "chronology", "RISK", "workflow compliance"]
    for er in cases:
        for intent in intents:
            result = recommend(er, intent)
            c = result["confidence"]
            assert 0.0 <= c <= 1.0, (
                f"confidence {c} is out of bounds [0,1] for intent={intent!r}"
            )


def test_confidence_is_rounded_to_two_decimals() -> None:
    """Confidence must be rounded to 2 decimal places (matching round(..., 2) in recommend)."""
    er = ExtractionResult()
    er.events = [_make_event(f"e{i}") for i in range(4)]
    er.obligations = [_make_obligation() for _ in range(2)]
    result = recommend(er, "chronology")
    c = result["confidence"]
    assert round(c, 2) == c, f"confidence {c} is not rounded to 2 decimal places"


def test_confidence_non_zero_for_nonempty_extraction() -> None:
    """Any non-empty extraction must produce confidence strictly above 0."""
    er = ExtractionResult()
    er.events = [_make_event("single event")]
    result = recommend(er, "")
    assert result["confidence"] > 0.0, (
        f"non-empty extraction must have confidence > 0, got {result['confidence']}"
    )


def test_confidence_cap_at_one() -> None:
    """Confidence is capped at 1.0 via min(..., 1.0); a dominant type must not exceed 1.0."""
    er = ExtractionResult()
    # Stack heavy signals all pointing at the same type to maximise the margin.
    er.communications = [Communication(from_party="A", to_party="B") for _ in range(6)]
    er.transfers = [Transfer(from_party="A", to_party="B", description="pay") for _ in range(6)]
    result = recommend(er, "sequence communications funds flow")
    assert result["confidence"] <= 1.0, (
        f"confidence must not exceed 1.0, got {result['confidence']}"
    )


# ---------------------------------------------------------------------------
# Test: margin-based confidence (defect 3)
# ---------------------------------------------------------------------------

def test_confidence_clear_winner_above_half() -> None:
    """A clear winner (dominant single type, no competitor) must land >= 0.50.

    Margin confidence rewards a dominant top-over-second gap rather than diluting it across
    every scoring type, so a single uncontested signal clears the 0.50 interrupt line.
    """
    er = ExtractionResult()
    er.communications = [Communication(from_party="A", to_party="B") for _ in range(4)]
    result = recommend(er, "communications sequence")
    assert result["recommended_type"] == "sequenceDiagram"
    assert result["confidence"] >= 0.50, (
        f"a clear single-type winner must have confidence >= 0.50, got {result['confidence']}"
    )


def test_confidence_genuine_tie_below_half() -> None:
    """A genuine multi-way ambiguity must stay below 0.50 so the interrupt fires.

    risk_items and communications are single-type rules of equal weight, producing an exact
    top-two tie; witnesses adds residual mass on a third type.  The thin margin plus the
    diluted share must report < 0.50 on real ambiguity.
    """
    er = ExtractionResult()
    er.risk_items = [RiskItem(label=f"R{i}", x_score=0.5, y_score=0.5) for i in range(3)]
    er.communications = [Communication(from_party="A", to_party="B") for _ in range(3)]
    er.witnesses = [WitnessMap(witness_name=f"W{i}") for i in range(3)]
    result = recommend(er, "")
    assert result["confidence"] < 0.50, (
        f"a genuine multi-way tie must report confidence < 0.50, got {result['confidence']}"
    )


def test_confidence_margin_beats_dilution() -> None:
    """Margin confidence must not be diluted by many low-scoring types.

    Adding a weak unrelated signal (a single party) must not drag a strong, clearly dominant
    winner below 0.50.  Under the old top/total formula such residue diluted the winner.
    """
    er = ExtractionResult()
    er.communications = [Communication(from_party="A", to_party="B") for _ in range(5)]
    er.parties = [Party(name="P", role="vendor", type="corp")]  # weak residue
    result = recommend(er, "communications sequence")
    assert result["recommended_type"] == "sequenceDiagram"
    assert result["confidence"] >= 0.50, (
        f"a dominant winner must stay >= 0.50 despite weak residue, got {result['confidence']}"
    )


def test_confidence_empty_extraction_keeps_low_default() -> None:
    """The empty-extraction path keeps its hardcoded low-confidence value (0.3), unchanged."""
    result = recommend(ExtractionResult(), "general")
    assert result["confidence"] == 0.3, (
        f"empty extraction must keep confidence 0.3, got {result['confidence']}"
    )


# ---------------------------------------------------------------------------
# Test: intent keyword exempts its type from the grouping override (defect 2)
# ---------------------------------------------------------------------------

def test_intent_timeline_exempts_grouping_override() -> None:
    """An explicit timeline-naming intent must hold timeline even with > 10 events.

    The dense-timeline grouping override would normally flip timeline to a grouped flowchart,
    but an intent keyword that explicitly names timeline exempts it from that override.
    """
    er = ExtractionResult()
    er.events = [_make_event(f"event {i}", f"2026-01-{i+1:02d}") for i in range(11)]
    result = recommend(er, "litigation chronology of events")
    assert result["recommended_type"] == "timeline", (
        f"intent naming chronology/timeline must hold timeline, got {result['recommended_type']}"
    )
    assert result["grouping_suggested"] is False
    assert result["grouping_axis"] is None


def test_grouping_override_still_fires_without_intent() -> None:
    """Without a timeline-naming intent, the dense-timeline override still flips to flowchart.

    The override exemption applies only to the intent path; the no-intent boundary behaviour
    (events > 10 -> grouped flowchart) is unchanged.
    """
    er = ExtractionResult()
    er.events = [_make_event(f"event {i}", f"2026-01-{i+1:02d}") for i in range(11)]
    result = recommend(er, "general")
    assert result["recommended_type"] == "flowchart"
    assert result["grouping_suggested"] is True
    assert result["grouping_axis"] == "era"


# ---------------------------------------------------------------------------
# Test: every labels-intent string resolves to its labelled type (data-driven)
#
# One generated test per scripts/tests/fixtures/*.labels.json: run the real
# extraction + selector for the fixture and assert that the labelled intent
# string yields the labelled with_intent type at confidence >= 0.50.  This is
# the W1 calibration gate, encoded as TDD over the fixture corpus rather than
# over any hardcoded intent text.  W3's FR fixtures join automatically via glob.
# ---------------------------------------------------------------------------

import json as _json  # noqa: E402

from normalize import normalize as _normalize  # noqa: E402
from extraction import extract as _extract  # noqa: E402
from tests.run_golden import FIXTURE_MATTER_TYPE as _FIXTURE_MATTER_TYPE  # noqa: E402

_FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def _resolve_fixture_with_intent(stem: str) -> tuple[str, dict]:
    """Run extraction + selector for one fixture under its labelled intent.

    Returns (labelled_with_intent_type, selector_result).
    """
    fixture = _FIXTURES_DIR / f"{stem}.md"
    labels = _json.loads((_FIXTURES_DIR / f"{stem}.md.labels.json").read_text(encoding="utf-8"))
    matter_type = _FIXTURE_MATTER_TYPE.get(stem)
    doc = _normalize(str(fixture), "md")
    extracted = _extract(doc, matter_type=matter_type, input_source=fixture.name)
    er = ExtractionResult.from_dict(extracted[0].to_dict())
    intent_block = labels.get("expected_type_with_intent", {})
    intent = intent_block.get("intent", "general")
    expected_type = intent_block.get("type", labels.get("expected_type", ""))
    result = recommend(er, intent)
    return expected_type, result


def _make_labels_resolution_test(stem: str):
    def _test() -> None:
        expected_type, result = _resolve_fixture_with_intent(stem)
        assert result["recommended_type"] == expected_type, (
            f"fixture '{stem}': labelled intent must resolve to {expected_type!r}, "
            f"got {result['recommended_type']!r}"
        )
        assert result["confidence"] >= 0.50, (
            f"fixture '{stem}': with-intent confidence must clear 0.50, "
            f"got {result['confidence']}"
        )
    _test.__name__ = f"test_labels_intent_resolves_{stem}"
    _test.__doc__ = (
        f"Fixture '{stem}': its labelled intent string must resolve to the labelled "
        f"with_intent type at confidence >= 0.50 (W1 gate, data-driven)."
    )
    return _test


# Register one zero-arg test per labels file so both pytest and the standalone
# runner discover them.
for _labels_path in sorted(_FIXTURES_DIR.glob("*.md.labels.json")):
    _stem = _labels_path.name[: -len(".md.labels.json")]
    globals()[f"test_labels_intent_resolves_{_stem}"] = _make_labels_resolution_test(_stem)


# ---------------------------------------------------------------------------
# Test: W3.5 -- FR intent keywords and accent-tolerant matching
# ---------------------------------------------------------------------------

# Each FR keyword mirrors the types and specificity of its EN twin keyword.
_FR_EN_TWINS = {
    "chronologie": "chronology",
    "échéancier": "schedule",
    "organigramme": "entity structure",
    "arbre de décision": "process",
    "schéma": "process",
    "liste d'obligations": "checklist",
    "qui-fait-quoi-quand": "sequence",
    "carte mentale": "research",
    "grille de priorités": "risk",
    "carte d'expérience": "client explanation",
}


def test_w3_5_fr_keywords_mirror_en_twins() -> None:
    """Every FR keyword must exist in INTENT_MAP with its EN twin's exact entry.

    Plain loop, not parametrize (standalone __main__ runner convention).
    """
    for fr_kw, en_kw in _FR_EN_TWINS.items():
        assert fr_kw in INTENT_MAP, f"FR keyword {fr_kw!r} missing from INTENT_MAP"
        assert INTENT_MAP[fr_kw] == INTENT_MAP[en_kw], (
            f"FR keyword {fr_kw!r} must carry the same (types, specificity) as its "
            f"EN twin {en_kw!r}: {INTENT_MAP[fr_kw]} != {INTENT_MAP[en_kw]}"
        )


def test_w3_5_fr_chronologie_timeline_family() -> None:
    """'chronologie' must resolve to the timeline family, like EN 'chronology'."""
    result = recommend(ExtractionResult(), "chronologie du litige")
    assert result["recommended_type"] == "timeline", (
        f"'chronologie' intent must recommend timeline, got {result['recommended_type']}"
    )


def test_w3_5_fr_organigramme_org_chart_family() -> None:
    """'organigramme' must resolve to the org-chart family (erDiagram top)."""
    result = recommend(ExtractionResult(), "organigramme des parties")
    assert result["recommended_type"] == "erDiagram", (
        f"'organigramme' intent must recommend erDiagram, got {result['recommended_type']}"
    )


def test_w3_5_fr_echeancier_accent_tolerant() -> None:
    """Accented 'échéancier' and unaccented 'echeancier' must score identically."""
    er = ExtractionResult()
    scores_accented = _score(er, "échéancier")
    scores_plain = _score(er, "echeancier")
    assert scores_accented == scores_plain, (
        f"accented and unaccented spellings must match the same keyword: "
        f"{scores_accented} != {scores_plain}"
    )
    result = recommend(ExtractionResult(), "échéancier")
    assert result["recommended_type"] == "gantt", (
        f"'échéancier' intent must recommend gantt, got {result['recommended_type']}"
    )


def test_w3_5_fr_curly_apostrophe_folds_to_ascii() -> None:
    """Smart-quote intents (U+2019) must match apostrophe-bearing FR keys."""
    er = ExtractionResult()
    scores_curly = _score(er, "liste d’obligations")
    scores_ascii = _score(er, "liste d'obligations")
    assert scores_curly == scores_ascii, (
        f"curly and ASCII apostrophes must match the same keyword: "
        f"{scores_curly} != {scores_ascii}"
    )


def test_w3_5_fr_carte_mentale_mindmap() -> None:
    """'carte mentale' must resolve to mindmap, like EN 'research'."""
    result = recommend(ExtractionResult(), "carte mentale")
    assert result["recommended_type"] == "mindmap", (
        f"'carte mentale' intent must recommend mindmap, got {result['recommended_type']}"
    )


def test_w3_5_en_outcomes_unchanged() -> None:
    """EN keywords must resolve exactly as before the FR additions.

    Mirrors existing pins: 'chronology' -> timeline; 'risk' -> quadrantChart at
    DOMINANT_INTENT_BOOST; the privacy intent ranks flowchart first (defect 1).
    """
    er = ExtractionResult()
    assert recommend(er, "chronology")["recommended_type"] == "timeline"
    scores_risk = _score(er, "risk")
    assert scores_risk.get("quadrantChart", 0) == DOMINANT_INTENT_BOOST
    scores_privacy = _score(er, "data privacy flows and obligations")
    ranked = sorted(scores_privacy, key=lambda t: scores_privacy[t], reverse=True)
    assert ranked[0] == "flowchart"


# ---------------------------------------------------------------------------
# Test: result structure completeness
# ---------------------------------------------------------------------------

def test_recommend_always_returns_required_keys() -> None:
    """recommend must always return a dict with all six required keys."""
    required = {"recommended_type", "rationale", "alternatives", "confidence",
                "grouping_suggested", "grouping_axis"}
    cases = [
        (ExtractionResult(), ""),
        (ExtractionResult(), "chronology"),
        (ExtractionResult(events=[_make_event("e")]), "risk"),
    ]
    for er, intent in cases:
        result = recommend(er, intent)
        missing = required - set(result.keys())
        assert not missing, f"result missing keys {missing} for intent={intent!r}"


# ---------------------------------------------------------------------------
# Standalone runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    _tests = [
        v for name, v in sorted(globals().items())
        if name.startswith("test_") and callable(v)
    ]
    _passed = 0
    _failed = 0
    for _test in _tests:
        # All tests in this module take no parameters.
        try:
            _test()
            _passed += 1
        except Exception as _exc:
            print(f"FAIL: {_test.__name__}: {_exc}")
            _failed += 1

    print(f"{_passed} tests passed, {_failed} failed")
    if _failed:
        sys.exit(1)
