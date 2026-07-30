"""Tests for render_html._inject_classdef — TDD red-green for classDef injection fix."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from render_html import _inject_classdef, _inject_container_styles


# ── supported diagram types ───────────────────────────────────────────────────

def test_flowchart_party_injects_classdef():
    block = 'flowchart TD\n    SAM["Sam"]\n    ALICE["Alice"]'
    sem = {"nodes": {"SAM": "sem-party", "ALICE": "sem-party"}}
    result = _inject_classdef(block, sem)
    assert "classDef semParty fill:#C9D6E3" in result
    assert "class ALICE,SAM semParty" in result  # sorted alphabetically


def test_flowchart_risk_high_modifier_produces_high_variant():
    block = 'flowchart TD\n    NOIP["No IP"]'
    sem = {"nodes": {"NOIP": "sem-process sem-risk-high"}}
    result = _inject_classdef(block, sem)
    assert "classDef semProcessHigh" in result
    assert "#8B4444" in result
    assert "stroke-width:2.5px" in result
    assert "class NOIP semProcessHigh" in result
    assert "classDef semProcess " not in result  # no plain variant emitted


def test_flowchart_mixed_classes_all_injected():
    block = 'flowchart TD\n    A["a"]\n    B{"b"}\n    C["c"]'
    sem = {"nodes": {"A": "sem-party", "B": "sem-risk", "C": "sem-outcome"}}
    result = _inject_classdef(block, sem)
    assert "classDef semParty" in result
    assert "classDef semRisk" in result
    assert "classDef semOutcome" in result
    assert "class A semParty" in result
    assert "class B semRisk" in result
    assert "class C semOutcome" in result


def test_flowchart_high_and_normal_same_primary():
    """Two nodes with sem-process: one plain, one with risk-high — two classDef variants emitted."""
    block = 'flowchart TD\n    A["a"]\n    B["b"]'
    sem = {"nodes": {"A": "sem-process", "B": "sem-process sem-risk-high"}}
    result = _inject_classdef(block, sem)
    assert "classDef semProcess " in result
    assert "classDef semProcessHigh" in result
    assert "class A semProcess" in result
    assert "class B semProcessHigh" in result


def test_statediagram_v2_injects_classdef():
    block = 'stateDiagram-v2\n    [*] --> Active'
    sem = {"nodes": {"Active": "sem-process"}}
    result = _inject_classdef(block, sem)
    assert "classDef semProcess" in result
    assert "class Active semProcess" in result


# ── unsupported diagram types — block unchanged ───────────────────────────────

def test_sequence_diagram_no_injection():
    block = "sequenceDiagram\n    Alice->>Bob: Hello"
    sem = {"nodes": {"Alice": "sem-party"}}
    result = _inject_classdef(block, sem)
    assert result == block


def test_er_diagram_no_injection():
    block = "erDiagram\n    PARTY ||--o{ SHARE : holds"
    sem = {"nodes": {"PARTY": "sem-party"}}
    result = _inject_classdef(block, sem)
    assert result == block


def test_gantt_no_injection():
    block = "gantt\n    title Schedule\n    dateFormat YYYY-MM-DD"
    sem = {"nodes": {"Task1": "sem-process"}}
    result = _inject_classdef(block, sem)
    assert result == block


# ── edge cases ────────────────────────────────────────────────────────────────

def test_empty_nodes_dict_unchanged():
    block = 'flowchart TD\n    A["test"]'
    result = _inject_classdef(block, {})
    assert result == block


def test_nodes_key_missing_unchanged():
    block = 'flowchart TD\n    A["test"]'
    result = _inject_classdef(block, {"meta": {"diagram_type": "flowchart"}})
    assert result == block


def test_unknown_sem_class_skipped():
    block = 'flowchart TD\n    A["test"]'
    sem = {"nodes": {"A": "sem-nonexistent"}}
    result = _inject_classdef(block, sem)
    assert result == block
    assert "classDef" not in result


def test_only_risk_high_no_primary_skipped():
    """sem-risk-high alone (no primary class) must be skipped gracefully."""
    block = 'flowchart TD\n    A["test"]'
    sem = {"nodes": {"A": "sem-risk-high"}}
    result = _inject_classdef(block, sem)
    assert result == block


def test_original_block_preserved_as_prefix():
    """Injected classDef/class lines must be appended, not replace, existing content."""
    block = 'flowchart TD\n    SAM["Sam"]'
    sem = {"nodes": {"SAM": "sem-party"}}
    result = _inject_classdef(block, sem)
    assert result.startswith(block)


def test_all_fourteen_sem_classes_supported():
    """Every sem-* class in the palette must produce its named classDef."""
    from render_html import _SEM_TO_CLASSDEF
    sem_classes = list(_SEM_TO_CLASSDEF.keys())
    block = "flowchart TD\n" + "\n".join(f'    N{i}["node"]' for i in range(len(sem_classes)))
    sem = {"nodes": {f"N{i}": cls for i, cls in enumerate(sem_classes)}}
    result = _inject_classdef(block, sem)
    for cls in sem_classes:
        name, _, _ = _SEM_TO_CLASSDEF[cls]
        assert f"classDef {name} " in result, f"classDef {name} missing for {cls}"
    assert result.count("classDef") == len(sem_classes)


# ── container tier shading ────────────────────────────────────────────────────

def test_flowchart_containers_inject_tier_styles():
    block = 'flowchart TB\n    subgraph Era1\n        A["a"]\n    end\n    subgraph Era2\n        B["b"]\n    end'
    sem = {"nodes": {"A": "sem-process", "B": "sem-process"}, "containers": {"Era1": 0, "Era2": 1}}
    result = _inject_container_styles(block, sem)
    assert "style Era1 fill:#F7F7F5" in result
    assert "style Era2 fill:#ECECE6" in result


def test_containers_skip_non_flowchart():
    block = "sequenceDiagram\n    Alice->>Bob: hi"
    sem = {"containers": {"Box1": 0}}
    assert _inject_container_styles(block, sem) == block


def test_containers_missing_or_empty_unchanged():
    block = 'flowchart TB\n    A["a"]'
    assert _inject_container_styles(block, {}) == block
    assert _inject_container_styles(block, {"containers": {}}) == block


def test_container_tier_clamps_beyond_palette():
    block = 'flowchart TB\n    subgraph Deep\n        A["a"]\n    end'
    sem = {"containers": {"Deep": 9}}
    result = _inject_container_styles(block, sem)
    assert "style Deep fill:#E0E0D8" in result


def test_containers_coexist_with_classdef():
    block = 'flowchart TB\n    subgraph Era1\n        A["a"]\n    end'
    sem = {"nodes": {"A": "sem-party"}, "containers": {"Era1": 0}}
    out = _inject_container_styles(_inject_classdef(block, sem), sem)
    assert "class A semParty" in out
    assert "style Era1 fill:#F7F7F5" in out
