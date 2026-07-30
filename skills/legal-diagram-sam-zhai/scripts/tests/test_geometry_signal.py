"""Tests for the geometry (overcrowding) gate added to diagram_selector.

TDD suite written before implementation (P2-geometry-signal).

Import pattern mirrors test_density_signal.py: sys.path.insert ROOT, then import
diagram_selector and extraction.domain.

Empirical grounding (Mermaid 11.15.0 headless render):
  BREADTH (max nodes per rank), not raw node count, drives the squeeze.
  Effective font crosses below ~9px legibility floor between 7 and 8 nodes/rank
  at 800px frame.  A 90-node deep-narrow chain is legible; a 30-node graph with
  18 in one rank is not.  max_rank_width is the primary flowchart metric.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from extraction.domain import ExtractionResult
from extraction.domain.core import (
    Concept,
    Communication,
    DecisionPoint,
    Event,
    Obligation,
    Party,
    ProcessStep,
    Relationship,
    Transfer,
    Transition,
    State,
)
from extraction.domain.corporate import OwnershipLink


# ---------------------------------------------------------------------------
# Helpers: build ExtractionResult fixtures
# ---------------------------------------------------------------------------

def _make_result(**kwargs) -> ExtractionResult:
    """Build ExtractionResult with keyword-supplied list overrides."""
    r = ExtractionResult()
    for k, v in kwargs.items():
        setattr(r, k, v)
    return r


def _make_relationship(from_e: str, to_e: str) -> Relationship:
    return Relationship(from_entity=from_e, to_entity=to_e, type="related")


def _make_transition(from_s: str, to_s: str) -> Transition:
    return Transition(from_state=from_s, to_state=to_s)


def _make_process_step(step_id: str, next_steps=None) -> ProcessStep:
    return ProcessStep(id=step_id, name=f"Step {step_id}", next_steps=next_steps or [])


def _make_concept(cid: str, parent_id=None, children=None) -> Concept:
    return Concept(id=cid, name=f"Concept {cid}", parent_id=parent_id, children=children or [])


def _make_communication(from_p: str, to_p: str) -> Communication:
    return Communication(from_party=from_p, to_party=to_p)


def _make_transfer(from_p: str, to_p: str) -> Transfer:
    return Transfer(from_party=from_p, to_party=to_p, description="payment")


def _make_ownership_link(parent: str, child: str) -> OwnershipLink:
    return OwnershipLink(parent=parent, child=child)


def _make_decision_point(q: str, yes: str, no: str) -> DecisionPoint:
    return DecisionPoint(question=q, yes_path=yes, no_path=no)


# ---------------------------------------------------------------------------
# (1) Breadth dominates over raw node count for flowchart
# ---------------------------------------------------------------------------

class TestBreadthDominates:
    """Deep-narrow graph => green; shallow-wide graph => split."""

    def test_deep_narrow_flowchart_is_green(self):
        """20-node chain (1 node/rank at each level) must be green."""
        from diagram_selector import _geometry
        # Build a linear chain: step_0 -> step_1 -> ... -> step_19
        steps = []
        for i in range(20):
            nxt = [f"s{i+1}"] if i < 19 else []
            steps.append(_make_process_step(f"s{i}", nxt))
        r = _make_result(process_steps=steps)
        geo = _geometry(r, "flowchart")
        assert geo["band"] == "green", (
            f"deep-narrow chain should be green, got {geo['band']}; "
            f"est_max_rank_width={geo['est_max_rank_width']}"
        )

    def test_shallow_wide_flowchart_is_split(self):
        """30-node star (18 children of one root) must be split."""
        from diagram_selector import _geometry
        # Root -> 18 children (all 18 in one rank = width 18 >= 8 threshold)
        steps = [_make_process_step("root", [f"c{i}" for i in range(18)])]
        for i in range(18):
            # remaining 12 nodes are leaves hanging off some children to reach 30 total
            if i < 12:
                steps.append(_make_process_step(f"c{i}", [f"leaf{i}"]))
                steps.append(_make_process_step(f"leaf{i}", []))
            else:
                steps.append(_make_process_step(f"c{i}", []))
        r = _make_result(process_steps=steps)
        geo = _geometry(r, "flowchart")
        assert geo["band"] == "split", (
            f"shallow-wide star should be split, got {geo['band']}; "
            f"est_max_rank_width={geo['est_max_rank_width']}"
        )


# ---------------------------------------------------------------------------
# (2) Per-type band thresholds
# ---------------------------------------------------------------------------

class TestFlowchartBands:
    """flowchart/graph: green <=6 width AND <=6 out_degree; warn at 7; split >=8."""

    def test_flowchart_green(self):
        from diagram_selector import _geometry
        # Linear chain of 6 nodes; max_rank_width=1, max_out_degree=1
        steps = [_make_process_step(f"s{i}", [f"s{i+1}"] if i < 5 else []) for i in range(6)]
        r = _make_result(process_steps=steps)
        geo = _geometry(r, "flowchart")
        assert geo["band"] == "green"
        assert geo["action"] == "ship"

    def test_flowchart_warn_at_7_width(self):
        from diagram_selector import _geometry
        # Root with exactly 7 children -> max_rank_width = 7 -> warn
        steps = [_make_process_step("root", [f"c{i}" for i in range(7)])]
        for i in range(7):
            steps.append(_make_process_step(f"c{i}", []))
        r = _make_result(process_steps=steps)
        geo = _geometry(r, "flowchart")
        assert geo["band"] == "warn"
        assert geo["action"] == "caveat"

    def test_flowchart_split_at_8_width(self):
        from diagram_selector import _geometry
        # Root with 8 children -> split
        steps = [_make_process_step("root", [f"c{i}" for i in range(8)])]
        for i in range(8):
            steps.append(_make_process_step(f"c{i}", []))
        r = _make_result(process_steps=steps)
        geo = _geometry(r, "flowchart")
        assert geo["band"] == "split"
        assert geo["action"] == "split"


class TestErDiagramBands:
    """erDiagram/classDiagram: green <=12 entities AND ratio<=2.5; warn 13-20; split >=21."""

    def test_er_green(self):
        from diagram_selector import _geometry
        from extraction.domain.core import Entity
        entities = [Entity(name=f"E{i}", type="company") for i in range(10)]
        rels = [_make_relationship(f"E{i}", f"E{i+1}") for i in range(4)]
        r = _make_result(entities=entities, relationships=rels)
        geo = _geometry(r, "erDiagram")
        assert geo["band"] == "green"

    def test_er_warn_at_15_entities(self):
        from diagram_selector import _geometry
        from extraction.domain.core import Entity
        entities = [Entity(name=f"E{i}", type="company") for i in range(15)]
        rels = [_make_relationship(f"E{i}", f"E{i+1}") for i in range(10)]
        r = _make_result(entities=entities, relationships=rels)
        geo = _geometry(r, "erDiagram")
        assert geo["band"] == "warn"

    def test_er_split_at_21_entities(self):
        from diagram_selector import _geometry
        from extraction.domain.core import Entity
        entities = [Entity(name=f"E{i}", type="company") for i in range(21)]
        rels = [_make_relationship(f"E{i}", f"E{i+1}") for i in range(20)]
        r = _make_result(entities=entities, relationships=rels)
        geo = _geometry(r, "erDiagram")
        assert geo["band"] == "split"


class TestSequenceDiagramBands:
    """sequenceDiagram: green <=8 participants; warn 9-12; split >=13."""

    def _make_comms(self, n_parties: int, n_comms: int):
        """Build n_comms communications cycling through n_parties."""
        parties = [f"P{i}" for i in range(n_parties)]
        comms = []
        for i in range(n_comms):
            comms.append(_make_communication(parties[i % n_parties], parties[(i + 1) % n_parties]))
        return parties, comms

    def test_sequence_green(self):
        from diagram_selector import _geometry
        parties_names, comms = self._make_comms(6, 12)
        parties = [Party(name=p, role="party", type="org") for p in parties_names]
        r = _make_result(parties=parties, communications=comms)
        geo = _geometry(r, "sequenceDiagram")
        assert geo["band"] == "green"

    def test_sequence_warn_at_10(self):
        from diagram_selector import _geometry
        parties_names, comms = self._make_comms(10, 20)
        parties = [Party(name=p, role="party", type="org") for p in parties_names]
        r = _make_result(parties=parties, communications=comms)
        geo = _geometry(r, "sequenceDiagram")
        assert geo["band"] == "warn"

    def test_sequence_split_at_13(self):
        from diagram_selector import _geometry
        parties_names, comms = self._make_comms(13, 26)
        parties = [Party(name=p, role="party", type="org") for p in parties_names]
        r = _make_result(parties=parties, communications=comms)
        geo = _geometry(r, "sequenceDiagram")
        assert geo["band"] == "split"


class TestTimelineBands:
    """timeline/gantt: green default; warn events>=25; gantt split rows-in-one-section>=20."""

    def test_timeline_green_below_25(self):
        from diagram_selector import _geometry
        events = [Event(date="2026-01-01", description="ev") for _ in range(15)]
        r = _make_result(events=events)
        geo = _geometry(r, "timeline")
        assert geo["band"] == "green"

    def test_timeline_warn_at_25(self):
        from diagram_selector import _geometry
        events = [Event(date="2026-01-01", description="ev") for _ in range(25)]
        r = _make_result(events=events)
        geo = _geometry(r, "timeline")
        assert geo["band"] == "warn"

    def test_timeline_warn_at_30(self):
        from diagram_selector import _geometry
        events = [Event(date="2026-01-01", description="ev") for _ in range(30)]
        r = _make_result(events=events)
        geo = _geometry(r, "timeline")
        assert geo["band"] == "warn"


class TestMindmapBands:
    """mindmap: green max_siblings<=8; warn 9-15; split>=16; warn depth>4."""

    def _make_mindmap_result(self, n_siblings: int):
        """Root concept with n_siblings children."""
        root = _make_concept("root", children=[f"c{i}" for i in range(n_siblings)])
        children = [_make_concept(f"c{i}", parent_id="root") for i in range(n_siblings)]
        r = _make_result(concepts=[root] + children)
        return r

    def test_mindmap_green(self):
        from diagram_selector import _geometry
        r = self._make_mindmap_result(6)
        geo = _geometry(r, "mindmap")
        assert geo["band"] == "green"

    def test_mindmap_warn_at_10(self):
        from diagram_selector import _geometry
        r = self._make_mindmap_result(10)
        geo = _geometry(r, "mindmap")
        assert geo["band"] == "warn"

    def test_mindmap_split_at_16(self):
        from diagram_selector import _geometry
        r = self._make_mindmap_result(16)
        geo = _geometry(r, "mindmap")
        assert geo["band"] == "split"


# ---------------------------------------------------------------------------
# (3) Split verdict sets grouping_suggested + supplies grouping_axis
# ---------------------------------------------------------------------------

class TestSplitSetsGrouping:
    """When geometry band == 'split', recommend() must set grouping_suggested
    and provide a non-null grouping_axis derived from split_axis_suggestion."""

    def test_split_flowchart_sets_grouping_suggested(self):
        from diagram_selector import recommend
        # Wide star -> split -> grouping_suggested True
        steps = [_make_process_step("root", [f"c{i}" for i in range(10)])]
        for i in range(10):
            steps.append(_make_process_step(f"c{i}", []))
        r = _make_result(process_steps=steps)
        result = recommend(r, "process")
        geo = result["geometry"]
        if geo["band"] == "split":
            assert result["grouping_suggested"] is True
            assert result["grouping_axis"] is not None

    def test_split_geometry_has_split_axis_suggestion(self):
        from diagram_selector import _geometry
        steps = [_make_process_step("root", [f"c{i}" for i in range(10)])]
        for i in range(10):
            steps.append(_make_process_step(f"c{i}", []))
        r = _make_result(process_steps=steps)
        geo = _geometry(r, "flowchart")
        if geo["band"] == "split":
            # split_axis_suggestion must be a string or None (never missing key)
            assert "split_axis_suggestion" in geo
            # triggers must be non-empty for a split
            assert len(geo["triggers"]) > 0

    def test_split_sequence_sets_grouping_suggested(self):
        from diagram_selector import recommend
        # 14 parties -> sequence split
        parties_names = [f"Party{i}" for i in range(14)]
        parties = [Party(name=p, role="actor", type="org") for p in parties_names]
        comms = [_make_communication(parties_names[i % 14], parties_names[(i + 1) % 14])
                 for i in range(30)]
        r = _make_result(parties=parties, communications=comms)
        result = recommend(r, "communications")
        geo = result["geometry"]
        if geo["band"] == "split":
            assert result["grouping_suggested"] is True
            assert result["grouping_axis"] is not None


# ---------------------------------------------------------------------------
# (4) density dict is unchanged in shape/values
# ---------------------------------------------------------------------------

class TestDensityUnchanged:
    """geometry addition must not alter density shape or values."""

    def test_density_keys_intact_no_signal_branch(self):
        from diagram_selector import recommend
        r = ExtractionResult()
        result = recommend(r, "general")
        d = result["density"]
        required = {"salient_count", "band", "inclusion_low", "inclusion_high",
                    "target_low", "target_high", "floor"}
        assert required <= set(d.keys()), f"missing density keys: {required - set(d.keys())}"

    def test_density_keys_intact_main_branch(self):
        from diagram_selector import recommend
        obls = [Obligation(id="O1", description="Do X", party="A") for _ in range(5)]
        r = _make_result(obligations=obls)
        result = recommend(r, "comprehensive")
        d = result["density"]
        required = {"salient_count", "band", "inclusion_low", "inclusion_high",
                    "target_low", "target_high", "floor"}
        assert required <= set(d.keys()), f"missing density keys: {required - set(d.keys())}"

    def test_density_values_unchanged_by_geometry(self):
        """density dict values must match direct _density() call."""
        from diagram_selector import recommend, _density
        obls = [Obligation(id="O1", description="Do X", party="A") for _ in range(8)]
        r = _make_result(obligations=obls)
        result = recommend(r, "detailed")
        d_via_recommend = result["density"]
        d_direct = _density(r, "detailed")
        assert d_via_recommend == d_direct, "density dict values changed by geometry addition"

    def test_density_no_new_keys_injected(self):
        """geometry must not inject extra keys into the density dict."""
        from diagram_selector import recommend
        r = ExtractionResult()
        result = recommend(r, "general")
        d = result["density"]
        allowed = {"salient_count", "band", "inclusion_low", "inclusion_high",
                   "target_low", "target_high", "floor"}
        extra = set(d.keys()) - allowed
        assert not extra, f"unexpected extra keys in density dict: {extra}"


# ---------------------------------------------------------------------------
# (5) Sparse/empty ExtractionResult yields valid green geometry without raising
# ---------------------------------------------------------------------------

class TestEmptyExtractionResult:
    """_geometry() on a fully empty ExtractionResult must not raise and must
    return a dict with band == 'green' and all required keys."""

    REQUIRED_GEO_KEYS = {
        "type", "primary_metric", "node_count", "edge_count", "max_out_degree",
        "longest_path", "est_max_rank_width", "subgraph_count",
        "max_siblings_per_subgraph", "band", "action", "split_axis_suggestion",
        "triggers",
    }

    def test_empty_result_flowchart_no_raise(self):
        from diagram_selector import _geometry
        r = ExtractionResult()
        geo = _geometry(r, "flowchart")
        assert isinstance(geo, dict)

    def test_empty_result_has_all_keys(self):
        from diagram_selector import _geometry
        r = ExtractionResult()
        geo = _geometry(r, "flowchart")
        missing = self.REQUIRED_GEO_KEYS - set(geo.keys())
        assert not missing, f"missing geometry keys: {missing}"

    def test_empty_result_is_green(self):
        from diagram_selector import _geometry
        r = ExtractionResult()
        geo = _geometry(r, "flowchart")
        assert geo["band"] == "green"
        assert geo["action"] == "ship"

    def test_empty_result_er_is_green(self):
        from diagram_selector import _geometry
        r = ExtractionResult()
        geo = _geometry(r, "erDiagram")
        assert geo["band"] == "green"

    def test_empty_result_sequence_is_green(self):
        from diagram_selector import _geometry
        r = ExtractionResult()
        geo = _geometry(r, "sequenceDiagram")
        assert geo["band"] == "green"

    def test_empty_result_timeline_is_green(self):
        from diagram_selector import _geometry
        r = ExtractionResult()
        geo = _geometry(r, "timeline")
        assert geo["band"] == "green"

    def test_empty_result_mindmap_is_green(self):
        from diagram_selector import _geometry
        r = ExtractionResult()
        geo = _geometry(r, "mindmap")
        assert geo["band"] == "green"

    def test_empty_result_triggers_is_list(self):
        from diagram_selector import _geometry
        r = ExtractionResult()
        geo = _geometry(r, "flowchart")
        assert isinstance(geo["triggers"], list)

    def test_empty_result_split_axis_suggestion_is_none(self):
        from diagram_selector import _geometry
        r = ExtractionResult()
        geo = _geometry(r, "flowchart")
        assert geo["split_axis_suggestion"] is None


# ---------------------------------------------------------------------------
# (6) recommend() returns both 'density' and 'geometry' keys in BOTH branches
# ---------------------------------------------------------------------------

class TestRecommendReturnsBothKeys:
    """Both density and geometry must appear in recommend() output in both branches."""

    REQUIRED_GEO_KEYS = {
        "type", "primary_metric", "node_count", "edge_count", "max_out_degree",
        "longest_path", "est_max_rank_width", "subgraph_count",
        "max_siblings_per_subgraph", "band", "action", "split_axis_suggestion",
        "triggers",
    }

    def test_no_signal_branch_has_both_keys(self):
        from diagram_selector import recommend
        r = ExtractionResult()
        result = recommend(r, "general")
        assert "density" in result, "density key missing from no-signal branch"
        assert "geometry" in result, "geometry key missing from no-signal branch"

    def test_main_branch_has_both_keys(self):
        from diagram_selector import recommend
        obls = [Obligation(id="O1", description="Do X", party="A") for _ in range(5)]
        r = _make_result(obligations=obls)
        result = recommend(r, "comprehensive")
        assert "density" in result, "density key missing from main branch"
        assert "geometry" in result, "geometry key missing from main branch"

    def test_no_signal_geometry_has_all_required_keys(self):
        from diagram_selector import recommend
        r = ExtractionResult()
        result = recommend(r, "general")
        geo = result["geometry"]
        missing = self.REQUIRED_GEO_KEYS - set(geo.keys())
        assert not missing, f"geometry missing keys in no-signal branch: {missing}"

    def test_main_geometry_has_all_required_keys(self):
        from diagram_selector import recommend
        obls = [Obligation(id="O1", description="Do X", party="A") for _ in range(5)]
        r = _make_result(obligations=obls)
        result = recommend(r, "comprehensive")
        geo = result["geometry"]
        missing = self.REQUIRED_GEO_KEYS - set(geo.keys())
        assert not missing, f"geometry missing keys in main branch: {missing}"

    def test_no_signal_geometry_type_is_flowchart(self):
        """no-signal branch uses recommended_type='flowchart', so geometry.type='flowchart'."""
        from diagram_selector import recommend
        r = ExtractionResult()
        result = recommend(r, "general")
        assert result["geometry"]["type"] == "flowchart"

    def test_main_branch_geometry_type_matches_recommended(self):
        """geometry.type must match recommended_type in the main branch."""
        from diagram_selector import recommend
        obls = [Obligation(id="O1", description="Do X", party="A") for _ in range(5)]
        r = _make_result(obligations=obls)
        result = recommend(r, "comprehensive")
        assert result["geometry"]["type"] == result["recommended_type"]

    def test_existing_keys_not_removed(self):
        """geometry addition must not remove any pre-existing keys."""
        from diagram_selector import recommend
        obls = [Obligation(id="O1", description="Do X", party="A") for _ in range(5)]
        r = _make_result(obligations=obls)
        result = recommend(r, "comprehensive")
        for key in ("recommended_type", "rationale", "alternatives", "confidence",
                    "grouping_suggested", "grouping_axis", "density"):
            assert key in result, f"existing key '{key}' missing after geometry addition"
