"""Tests for the density signal added to diagram_selector.recommend().

TDD suite written before implementation (P2-B4-density-signal).

Import pattern mirrors test_extraction.py: sys.path.insert ROOT, then import
diagram_selector and extraction.domain.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from extraction.domain import ExtractionResult
from extraction.domain.core import Obligation, RiskItem, Deadline, Event


# ---------------------------------------------------------------------------
# Helper: build an ExtractionResult quickly
# ---------------------------------------------------------------------------

def _make_result(**kwargs) -> ExtractionResult:
    """Build ExtractionResult with keyword-supplied list overrides."""
    r = ExtractionResult()
    for k, v in kwargs.items():
        setattr(r, k, v)
    return r


def _make_obligation(risk_level: str | None = None) -> Obligation:
    return Obligation(id="OBL-0001", description="Deliver docs", party="Seller", risk_level=risk_level)


def _make_deadline(risk_level: str | None = None) -> Deadline:
    return Deadline(date="2026-06-01", description="Closing", party="Buyer")


def _make_risk_item(risk_level: str | None = None) -> RiskItem:
    # RiskItem has no risk_level field; getattr returns None safely
    return RiskItem(label="Unauthorized access", x_score=0.8, y_score=0.9)


# ---------------------------------------------------------------------------
# (a) Band classification
# ---------------------------------------------------------------------------

class TestBandClassification:
    def _band(self, intent: str) -> str:
        from diagram_selector import _density
        r = ExtractionResult()
        return _density(r, intent)["band"]

    def test_comprehensive_keyword(self):
        assert self._band("comprehensive overview") == "comprehensive"

    def test_detailed_keyword(self):
        assert self._band("detailed analysis") == "detailed"

    def test_overview_keyword(self):
        assert self._band("overview of the matter") == "overview"

    def test_high_level_hyphenated(self):
        assert self._band("high-level summary") == "overview"

    def test_at_a_glance(self):
        assert self._band("at a glance") == "overview"

    def test_at_a_glance_hyphenated(self):
        assert self._band("at-a-glance view") == "overview"

    def test_summary_keyword(self):
        # "a high level summary" alone -> overview; but "everything" also triggers
        # comprehensive. Conflict -> default comprehensive per spec.
        assert self._band("a high level summary") == "overview"

    def test_simple_keyword(self):
        assert self._band("simple diagram") == "overview"

    def test_empty_string_defaults_comprehensive(self):
        assert self._band("") == "comprehensive"

    def test_no_match_defaults_comprehensive(self):
        assert self._band("flowchart of the workflow") == "comprehensive"

    def test_exhaustive_keyword(self):
        assert self._band("exhaustive breakdown") == "comprehensive"

    def test_everything_keyword(self):
        assert self._band("flowchart of everything") == "comprehensive"

    def test_all_keyword(self):
        assert self._band("show all entities") == "comprehensive"

    def test_thorough_keyword(self):
        assert self._band("thorough walkthrough") == "detailed"

    def test_detail_keyword(self):
        assert self._band("detail of each step") == "detailed"

    def test_case_insensitive_comprehensive(self):
        assert self._band("COMPREHENSIVE breakdown") == "comprehensive"

    def test_case_insensitive_detailed(self):
        assert self._band("Detailed plan") == "detailed"

    def test_case_insensitive_overview(self):
        assert self._band("High Level summary") == "overview"


# ---------------------------------------------------------------------------
# (b) Target math
# ---------------------------------------------------------------------------

class TestTargetMath:
    def test_comprehensive_band_targets(self):
        """salient_count=10 obligations -> comprehensive -> low=round(10*0.85)=9, high=round(10*0.95)=10."""
        from diagram_selector import _density
        obls = [_make_obligation() for _ in range(10)]
        r = _make_result(obligations=obls)
        d = _density(r, "comprehensive")
        assert d["salient_count"] == 10
        assert d["band"] == "comprehensive"
        assert d["inclusion_low"] == 0.85
        assert d["inclusion_high"] == 0.95
        assert d["target_low"] == round(10 * 0.85)
        assert d["target_high"] == round(10 * 0.95)

    def test_detailed_band_targets(self):
        """salient_count=20 -> detailed -> low=round(20*0.60)=12, high=round(20*0.75)=15."""
        from diagram_selector import _density
        obls = [_make_obligation() for _ in range(20)]
        r = _make_result(obligations=obls)
        d = _density(r, "detailed review")
        assert d["target_low"] == round(20 * 0.60)
        assert d["target_high"] == round(20 * 0.75)

    def test_overview_band_targets(self):
        """salient_count=30 -> overview -> low=round(30*0.30)=9, high=round(30*0.45)=14 (rounded)."""
        from diagram_selector import _density
        events = [Event(date="2026-01-01", description="event") for _ in range(30)]
        r = _make_result(events=events)
        d = _density(r, "high-level overview")
        assert d["target_low"] == round(30 * 0.30)
        assert d["target_high"] == round(30 * 0.45)

    def test_calibration_example_85_entities_comprehensive(self):
        """Calibration: salient_count=85, comprehensive -> target_low=72, target_high=81."""
        from diagram_selector import _density

        # Build an ExtractionResult with 85 total salient entities spread
        # across obligations (50) and events (35).
        obls = [_make_obligation() for _ in range(50)]
        events = [Event(date="2026-01-01", description="ev") for _ in range(35)]
        r = _make_result(obligations=obls, events=events)
        d = _density(r, "comprehensive")
        assert d["salient_count"] == 85
        assert d["target_low"] == round(85 * 0.85)   # 72
        assert d["target_high"] == round(85 * 0.95)  # 81

    def test_salient_count_sums_all_entity_fields(self):
        """salient_count must equal sum across ALL ENTITY_FIELDS, not just obligations."""
        from diagram_selector import _density
        r = _make_result(
            obligations=[_make_obligation() for _ in range(3)],
            events=[Event(date="2026-01-01", description="ev") for _ in range(2)],
            parties=[],   # empty lists count as 0
        )
        d = _density(r, "")
        # 3 obligations + 2 events = 5
        assert d["salient_count"] == 5


# ---------------------------------------------------------------------------
# (c) Floor clamping
# ---------------------------------------------------------------------------

class TestFloor:
    def test_floor_forces_target_low_up(self):
        """K high-risk obligations forces target_low >= K."""
        from diagram_selector import _density
        # 5 high-risk obligations out of 6 total
        high_risk = [_make_obligation(risk_level="high") for _ in range(5)]
        normal = [_make_obligation(risk_level="low") for _ in range(1)]
        r = _make_result(obligations=high_risk + normal)
        d = _density(r, "overview")  # overview band would normally give a low target
        # With only 6 salient entities and overview band: target_low = round(6*0.30) = 2
        # floor = 5, so effective target_low must be 5
        assert d["floor"] == 5
        assert d["target_low"] >= 5

    def test_floor_counts_high_risk_deadlines(self):
        """Deadlines do not have risk_level; getattr returns None; they do NOT count toward floor."""
        from diagram_selector import _density
        # Deadlines lack risk_level; none should add to floor
        deadlines = [_make_deadline() for _ in range(10)]
        r = _make_result(deadlines=deadlines)
        d = _density(r, "comprehensive")
        assert d["floor"] == 0

    def test_floor_counts_high_risk_risk_items(self):
        """RiskItem has no risk_level attribute; getattr returns None; they don't add to floor."""
        from diagram_selector import _density
        risk_items = [_make_risk_item() for _ in range(5)]
        r = _make_result(risk_items=risk_items)
        d = _density(r, "comprehensive")
        assert d["floor"] == 0

    def test_floor_not_exceed_salient_count(self):
        """target_low clamped to <= salient_count."""
        from diagram_selector import _density
        # All 3 are high-risk obligations
        obls = [_make_obligation(risk_level="high") for _ in range(3)]
        r = _make_result(obligations=obls)
        d = _density(r, "overview")
        assert d["target_low"] <= d["salient_count"]

    def test_floor_zero_when_no_high_risk(self):
        """No high-risk items -> floor == 0."""
        from diagram_selector import _density
        obls = [_make_obligation(risk_level="low") for _ in range(5)]
        r = _make_result(obligations=obls)
        d = _density(r, "comprehensive")
        assert d["floor"] == 0

    def test_floor_mixed_fields(self):
        """Floor counts high-risk obligations only (risk_items and deadlines have no risk_level)."""
        from diagram_selector import _density
        obls = [_make_obligation(risk_level="high") for _ in range(3)]
        risk_items = [_make_risk_item() for _ in range(5)]
        deadlines = [_make_deadline() for _ in range(2)]
        r = _make_result(obligations=obls, risk_items=risk_items, deadlines=deadlines)
        d = _density(r, "overview")
        assert d["floor"] == 3


# ---------------------------------------------------------------------------
# (d) Zero salient_count returns safe default
# ---------------------------------------------------------------------------

class TestZeroDefault:
    def test_zero_salient_count_returns_without_error(self):
        from diagram_selector import _density
        r = ExtractionResult()  # all lists empty
        d = _density(r, "comprehensive")
        assert d["salient_count"] == 0
        assert d["target_low"] == 0
        assert d["target_high"] == 0
        assert d["floor"] == 0

    def test_zero_band_still_classified(self):
        from diagram_selector import _density
        # "detailed overview" matches both detailed and overview keywords;
        # conflict -> default comprehensive per spec.
        d = _density(ExtractionResult(), "detailed overview")
        assert d["band"] == "comprehensive"

    def test_zero_default_has_all_keys(self):
        from diagram_selector import _density
        d = _density(ExtractionResult(), "")
        required_keys = {"salient_count", "band", "inclusion_low", "inclusion_high",
                         "target_low", "target_high", "floor"}
        assert required_keys <= set(d.keys())


# ---------------------------------------------------------------------------
# (e) density key present in BOTH recommend() return branches
# ---------------------------------------------------------------------------

class TestRecommendDensityKey:
    def test_no_signal_branch_has_density_key(self):
        """Empty extraction -> no-signal branch -> density key must be present."""
        from diagram_selector import recommend
        r = ExtractionResult()
        result = recommend(r, "general")
        assert "density" in result, "density key missing from no-signal branch"
        d = result["density"]
        assert isinstance(d, dict)
        required = {"salient_count", "band", "inclusion_low", "inclusion_high",
                    "target_low", "target_high", "floor"}
        assert required <= set(d.keys())

    def test_main_branch_has_density_key(self):
        """Non-empty extraction -> main branch -> density key must be present."""
        from diagram_selector import recommend
        obls = [_make_obligation() for _ in range(5)]
        r = _make_result(obligations=obls)
        result = recommend(r, "comprehensive")
        assert "density" in result, "density key missing from main branch"
        d = result["density"]
        assert isinstance(d, dict)
        assert d["salient_count"] == 5

    def test_recommend_existing_keys_preserved_no_signal(self):
        """Existing keys must not be removed or renamed in the no-signal branch."""
        from diagram_selector import recommend
        r = ExtractionResult()
        result = recommend(r, "general")
        for key in ("recommended_type", "rationale", "alternatives", "confidence",
                    "grouping_suggested", "grouping_axis"):
            assert key in result, f"existing key '{key}' missing from no-signal branch"

    def test_recommend_existing_keys_preserved_main(self):
        """Existing keys must not be removed or renamed in the main branch."""
        from diagram_selector import recommend
        obls = [_make_obligation() for _ in range(5)]
        r = _make_result(obligations=obls)
        result = recommend(r, "comprehensive")
        for key in ("recommended_type", "rationale", "alternatives", "confidence",
                    "grouping_suggested", "grouping_axis"):
            assert key in result, f"existing key '{key}' missing from main branch"

    def test_density_inclusion_fractions_match_band(self):
        """inclusion_low/high must match the resolved band's documented fractions."""
        from diagram_selector import recommend
        obls = [_make_obligation() for _ in range(10)]
        r = _make_result(obligations=obls)
        result = recommend(r, "overview")
        d = result["density"]
        assert d["inclusion_low"] == 0.30
        assert d["inclusion_high"] == 0.45
