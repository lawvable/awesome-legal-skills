"""Tests for patch_gate.py and extraction/patching.py.

Covers V1-V9 validation rules plus end-to-end golden manifest test and CLI exit codes.

Standalone-runnable: python scripts/tests/test_patch_gate.py
Also discoverable by pytest.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

PATCH_GATE = ROOT / "patch_gate.py"
GOLDEN_DIR = Path(__file__).resolve().parent / "golden"
SPA_MANIFEST = GOLDEN_DIR / "en_spa_contract.manifest.json"

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _run_gate(manifest_data: dict, patch_data: list, apply: bool = False) -> tuple[int, dict]:
    """Run patch_gate CLI via subprocess; return (returncode, parsed_stdout_dict)."""
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory() as tmp:
        mpath = Path(tmp) / "manifest.json"
        ppath = Path(tmp) / "patch.json"
        mpath.write_text(json.dumps(manifest_data), encoding="utf-8")
        ppath.write_text(json.dumps(patch_data), encoding="utf-8")
        args = [sys.executable, str(PATCH_GATE), "--manifest", str(mpath), "--patch", str(ppath)]
        if apply:
            args.append("--apply")
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            args,
            text=True,
            capture_output=True,
            env=env,
            timeout=30,
        )
    out = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, out


def _minimal_manifest(extraction_result: dict | None = None) -> dict:
    """Return a minimal manifest skeleton for unit tests."""
    er = extraction_result or {}
    return {
        "extraction_result": er,
        "extraction_hints": [],
        "coverage": {},
        "matter_type_evidence": {},
        "candidate_manifest": {"evidence_packets": [], "candidates": [], "promotion_decisions": []},
        "llm_enrichment": {"evidence_packets": [], "directives": []},
        "profile_signals": {},
    }


def _manifest_with_evidence(ev_id: str = "E0001") -> dict:
    """Manifest with one candidate evidence packet whose id is ev_id."""
    m = _minimal_manifest()
    m["candidate_manifest"]["evidence_packets"] = [{
        "id": ev_id,
        "snippet": "test snippet",
        "source_ref": {"source": "test.md"},
        "heading_path": [],
        "candidate_fields": ["conditions"],
        "confidence": 0.8,
        "neighboring_context_ids": [],
    }]
    return m


# ---------------------------------------------------------------------------
# V1 op-shape
# ---------------------------------------------------------------------------

def test_v1_passes_valid_ops() -> None:
    m = _minimal_manifest()
    patch = [{"op": "add", "path": "/conditions/-", "value": {"id": "COND-X", "evidence_id": "H0", "source_ref": {}}}]
    rc, out = _run_gate(m, patch)
    assert rc == 1  # V4 fires (no directive for conditions); V1 itself is clean
    errors = [f for f in out.get("findings", []) if f["rule"] == "V1" and f["severity"] == "error"]
    assert not errors, errors


def test_v1_fails_not_array() -> None:
    m = _minimal_manifest()
    rc, out = _run_gate(m, {"op": "add", "path": "/conditions/-", "value": {}})  # type: ignore[arg-type]
    assert rc == 1
    assert any(f["rule"] == "V1" for f in out.get("findings", []))


def test_v1_fails_disallowed_op() -> None:
    m = _minimal_manifest()
    patch = [{"op": "move", "from": "/conditions/0", "path": "/events/-"}]
    rc, out = _run_gate(m, patch)
    assert rc == 1
    assert any(f["rule"] == "V1" for f in out.get("findings", []))


def test_v1_fails_missing_path() -> None:
    m = _minimal_manifest()
    patch = [{"op": "add", "value": "x"}]
    rc, out = _run_gate(m, patch)
    assert rc == 1
    assert any(f["rule"] == "V1" for f in out.get("findings", []))


def test_v1_fails_missing_value_for_add() -> None:
    m = _minimal_manifest()
    patch = [{"op": "add", "path": "/conditions/-"}]
    rc, out = _run_gate(m, patch)
    assert rc == 1
    assert any(f["rule"] == "V1" for f in out.get("findings", []))


def test_v1_error_suppresses_downstream_rules() -> None:
    """A patch with a V1-broken op (disallowed 'move') must yield ONLY V1 findings.

    Before fix, V8 ('Cannot add at root pointer') and V4 (tier errors) fired as
    spurious secondary findings because the bail logic only short-circuited on
    non-list input, not on V1 errors within a list.
    """
    m = _minimal_manifest()
    patch = [{"op": "move", "from": "/conditions/0", "path": "/events/-"}]
    rc, out = _run_gate(m, patch)
    assert rc == 1
    findings = out.get("findings", [])
    # Must have at least one V1 finding
    assert any(f["rule"] == "V1" for f in findings), f"No V1 finding in {findings}"
    # No V4 or V8 findings (spurious secondary findings)
    non_v1 = [f for f in findings if f["rule"] in ("V4", "V8")]
    assert not non_v1, f"Spurious downstream findings present: {non_v1}"


# ---------------------------------------------------------------------------
# V2 evidence-presence
# ---------------------------------------------------------------------------

def test_v2_passes_entity_add_with_evidence() -> None:
    m = _manifest_with_evidence("E0001")
    patch = [{
        "op": "add",
        "path": "/conditions/-",
        "value": {
            "id": "COND-NEW",
            "description": "test",
            "evidence_id": "E0001",
            "source_ref": {"source": "test.md"},
        },
    }]
    rc, out = _run_gate(m, patch)
    assert rc == 1  # V4 fires (no directive for conditions); V2 itself is clean
    errors = [f for f in out.get("findings", []) if f["rule"] == "V2"]
    assert not errors, errors


def test_v2_fails_entity_add_missing_evidence() -> None:
    m = _minimal_manifest()
    patch = [{
        "op": "add",
        "path": "/conditions/-",
        "value": {"id": "COND-NEW", "description": "test"},
    }]
    rc, out = _run_gate(m, patch)
    assert rc == 1
    assert any(f["rule"] == "V2" and f["severity"] == "error" for f in out.get("findings", []))


def test_v2_scalar_subfield_exempt() -> None:
    """risk_level replace on existing obligation is exempt from V2 (sub-field scalar replace)."""
    m = _minimal_manifest({"obligations": [{"id": "OBL-001", "risk_level": None}]})
    m["llm_enrichment"]["directives"] = [{"field": "obligations[].risk_level"}]
    patch = [{"op": "replace", "path": "/obligations/0/risk_level", "value": "high"}]
    rc, out = _run_gate(m, patch)
    assert rc == 0
    errors = [f for f in out.get("findings", []) if f["rule"] == "V2"]
    assert not errors, errors


def test_v2_hierarchy_exempt() -> None:
    """Hierarchy add is exempt from V2."""
    m = _minimal_manifest()
    m["llm_enrichment"]["directives"] = [{"field": "hierarchy"}]
    patch = [{
        "op": "add",
        "path": "/hierarchy/-",
        "value": {"id": "H-new", "label": "New Section", "parent": None, "depth": 0, "source": "llm"},
    }]
    rc, out = _run_gate(m, patch)
    assert rc == 1  # V8 fires (no hierarchy array in extraction_result); V2 itself is clean
    errors = [f for f in out.get("findings", []) if f["rule"] == "V2"]
    assert not errors, errors


def test_v2_matter_type_exempt() -> None:
    """matter_type replace is exempt from V2."""
    m = _minimal_manifest({"matter_type": None})
    m["llm_enrichment"]["directives"] = [{"field": "matter_type"}]
    patch = [{"op": "replace", "path": "/matter_type", "value": "deal"}]
    rc, out = _run_gate(m, patch)
    assert rc == 0
    errors = [f for f in out.get("findings", []) if f["rule"] == "V2"]
    assert not errors, errors


# ---------------------------------------------------------------------------
# V3 evidence-resolves
# ---------------------------------------------------------------------------

def test_v3_passes_known_evidence_id() -> None:
    m = _manifest_with_evidence("E0001")
    patch = [{
        "op": "add",
        "path": "/conditions/-",
        "value": {"id": "COND-X", "evidence_id": "E0001", "source_ref": {}},
    }]
    rc, out = _run_gate(m, patch)
    assert rc == 1  # V4 fires (no directive for conditions); V3 itself is clean
    errors = [f for f in out.get("findings", []) if f["rule"] == "V3"]
    assert not errors, errors


def test_v3_passes_hint_evidence_id() -> None:
    m = _minimal_manifest()
    m["extraction_hints"] = [{"id": "H0", "suggested_field": "conditions"}]
    patch = [{
        "op": "add",
        "path": "/conditions/-",
        "value": {"id": "COND-X", "evidence_id": "H0", "source_ref": {}},
    }]
    rc, out = _run_gate(m, patch)
    assert rc == 1  # V8 fires (no conditions array in extraction_result); V3 itself is clean
    errors = [f for f in out.get("findings", []) if f["rule"] == "V3"]
    assert not errors, errors


def test_v3_fails_unknown_evidence_id() -> None:
    m = _minimal_manifest()
    patch = [{
        "op": "add",
        "path": "/conditions/-",
        "value": {"id": "COND-X", "evidence_id": "EXXXX", "source_ref": {}},
    }]
    rc, out = _run_gate(m, patch)
    assert rc == 1
    assert any(f["rule"] == "V3" and f["severity"] == "error" for f in out.get("findings", []))


def test_v3_passes_llm_evidence_id() -> None:
    m = _minimal_manifest()
    m["llm_enrichment"]["evidence_packets"] = [{"id": "E0100", "snippet": "x"}]
    patch = [{
        "op": "add",
        "path": "/conditions/-",
        "value": {"id": "COND-X", "evidence_id": "E0100", "source_ref": {}},
    }]
    rc, out = _run_gate(m, patch)
    assert rc == 1  # V4 fires (no directive for conditions); V3 itself is clean
    errors = [f for f in out.get("findings", []) if f["rule"] == "V3"]
    assert not errors, errors


# ---------------------------------------------------------------------------
# V4 tier-guard
# ---------------------------------------------------------------------------

def test_v4_passes_allowed_field() -> None:
    m = _minimal_manifest()
    m["llm_enrichment"]["directives"] = [{"field": "conditions"}]
    patch = [{
        "op": "add",
        "path": "/conditions/-",
        "value": {"id": "COND-X", "evidence_id": "H0", "source_ref": {}},
    }]
    _, out = _run_gate(m, patch)
    errors = [f for f in out.get("findings", []) if f["rule"] == "V4"]
    assert not errors, errors


def test_v4_passes_hierarchy_always_allowed() -> None:
    m = _minimal_manifest()
    patch = [{
        "op": "add",
        "path": "/hierarchy/-",
        "value": {"id": "H-x", "label": "X", "parent": None, "depth": 0, "source": "llm"},
    }]
    _, out = _run_gate(m, patch)
    errors = [f for f in out.get("findings", []) if f["rule"] == "V4"]
    assert not errors, errors


def test_v4_fails_disallowed_field() -> None:
    m = _minimal_manifest()
    # no directive for 'parties'; no suggestion; not in LLM_ONLY or NULL_FIELDS
    m["llm_enrichment"]["directives"] = []
    m["extraction_hints"] = []
    patch = [{"op": "add", "path": "/parties/-", "value": {"id": "P-X", "evidence_id": "H0", "source_ref": {}}}]
    _, out = _run_gate(m, patch)
    assert any(f["rule"] == "V4" and f["severity"] == "error" for f in out.get("findings", []))


def test_v4_passes_llm_only_field() -> None:
    """decision_points is in LLM_ONLY; always tier-allowed."""
    m = _minimal_manifest()
    m["candidate_manifest"]["evidence_packets"] = [{"id": "E0001"}]
    m["llm_enrichment"]["evidence_packets"] = [{"id": "E0001"}]
    patch = [{
        "op": "add",
        "path": "/decision_points/-",
        "value": {"id": "DP-1", "evidence_id": "E0001", "source_ref": {}},
    }]
    _, out = _run_gate(m, patch)
    errors = [f for f in out.get("findings", []) if f["rule"] == "V4"]
    assert not errors, errors


# ---------------------------------------------------------------------------
# V5 immutability
# ---------------------------------------------------------------------------

def test_v5_passes_append_to_existing_array() -> None:
    m = _manifest_with_evidence("E0001")
    m["extraction_result"] = {"conditions": [{"id": "COND-001"}]}
    m["llm_enrichment"]["directives"] = [{"field": "conditions"}]
    patch = [{
        "op": "add",
        "path": "/conditions/-",
        "value": {"id": "COND-NEW", "evidence_id": "E0001", "source_ref": {}},
    }]
    _, out = _run_gate(m, patch)
    errors = [f for f in out.get("findings", []) if f["rule"] == "V5"]
    assert not errors, errors


def test_v5_fails_replace_existing_entity() -> None:
    m = _minimal_manifest({"conditions": [{"id": "COND-001", "description": "original"}]})
    m["llm_enrichment"]["directives"] = [{"field": "conditions"}]
    patch = [{"op": "replace", "path": "/conditions/0", "value": {"id": "COND-001", "description": "changed"}}]
    _, out = _run_gate(m, patch)
    assert any(f["rule"] == "V5" and f["severity"] == "error" for f in out.get("findings", []))


def test_v5_passes_risk_level_subfield_replace() -> None:
    m = _minimal_manifest({"obligations": [{"id": "OBL-001", "risk_level": None}]})
    m["llm_enrichment"]["directives"] = [{"field": "obligations[].risk_level"}]
    patch = [{"op": "replace", "path": "/obligations/0/risk_level", "value": "high"}]
    _, out = _run_gate(m, patch)
    errors = [f for f in out.get("findings", []) if f["rule"] == "V5"]
    assert not errors, errors


def test_v5_passes_obligation_id_subfield_replace() -> None:
    """obligation_id replace on existing control is exempt from V5 (cross-linking exemption)."""
    m = _minimal_manifest({"controls": [{"id": "CTRL-001", "obligation_id": None}]})
    m["llm_enrichment"]["directives"] = [{"field": "controls[].obligation_id"}]
    patch = [{"op": "replace", "path": "/controls/0/obligation_id", "value": "OBL-001"}]
    rc, out = _run_gate(m, patch)
    assert rc == 0
    errors = [f for f in out.get("findings", []) if f["rule"] == "V5"]
    assert not errors, errors


def test_v5_passes_matter_type_when_null() -> None:
    m = _minimal_manifest({"matter_type": None})
    m["llm_enrichment"]["directives"] = [{"field": "matter_type"}]
    patch = [{"op": "replace", "path": "/matter_type", "value": "deal"}]
    _, out = _run_gate(m, patch)
    errors = [f for f in out.get("findings", []) if f["rule"] == "V5"]
    assert not errors, errors


def test_v5_fails_matter_type_when_set() -> None:
    m = _minimal_manifest({"matter_type": "deal"})
    m["llm_enrichment"]["directives"] = [{"field": "matter_type"}]
    patch = [{"op": "replace", "path": "/matter_type", "value": "litigation"}]
    _, out = _run_gate(m, patch)
    assert any(f["rule"] == "V5" and f["severity"] == "error" for f in out.get("findings", []))


# ---------------------------------------------------------------------------
# V6 remove-scope
# ---------------------------------------------------------------------------

def test_v6_passes_remove_from_hierarchy() -> None:
    m = _minimal_manifest({"hierarchy": [{"id": "H-x", "label": "X", "parent": None, "depth": 0, "source": "deterministic"}]})
    patch = [{"op": "remove", "path": "/hierarchy/0"}]
    _, out = _run_gate(m, patch)
    errors = [f for f in out.get("findings", []) if f["rule"] == "V6"]
    assert not errors, errors


def test_v6_fails_remove_from_conditions() -> None:
    m = _minimal_manifest({"conditions": [{"id": "COND-001"}]})
    patch = [{"op": "remove", "path": "/conditions/0"}]
    _, out = _run_gate(m, patch)
    assert any(f["rule"] == "V6" and f["severity"] == "error" for f in out.get("findings", []))


def test_v6_fails_remove_from_obligations() -> None:
    m = _minimal_manifest({"obligations": [{"id": "OBL-001"}]})
    patch = [{"op": "remove", "path": "/obligations/0"}]
    _, out = _run_gate(m, patch)
    assert any(f["rule"] == "V6" and f["severity"] == "error" for f in out.get("findings", []))


# ---------------------------------------------------------------------------
# V7 hierarchy-integrity
# ---------------------------------------------------------------------------

def test_v7_passes_valid_hierarchy_add() -> None:
    m = _minimal_manifest({"hierarchy": [{"id": "ROOT", "label": "Root", "parent": None, "depth": 0, "source": "deterministic"}]})
    m["llm_enrichment"]["directives"] = [{"field": "hierarchy"}]
    patch = [{
        "op": "add",
        "path": "/hierarchy/-",
        "value": {"id": "CHILD", "label": "Child", "parent": "ROOT", "depth": 1, "source": "llm"},
    }]
    _, out = _run_gate(m, patch)
    errors = [f for f in out.get("findings", []) if f["rule"] == "V7"]
    assert not errors, errors


def test_v7_fails_orphan_llm_node() -> None:
    """LLM node with parent that does not exist as another node's id."""
    m = _minimal_manifest({"hierarchy": []})
    m["llm_enrichment"]["directives"] = [{"field": "hierarchy"}]
    patch = [{
        "op": "add",
        "path": "/hierarchy/-",
        "value": {"id": "ORPHAN", "label": "Orphan", "parent": "NONEXISTENT", "depth": 1, "source": "llm"},
    }]
    _, out = _run_gate(m, patch)
    assert any(f["rule"] == "V7" and f["severity"] == "error" for f in out.get("findings", []))


def test_v7_fails_depth_exceeds_2() -> None:
    m = _minimal_manifest({"hierarchy": [
        {"id": "R", "label": "Root", "parent": None, "depth": 0, "source": "deterministic"},
        {"id": "C", "label": "Child", "parent": "R", "depth": 1, "source": "deterministic"},
    ]})
    m["llm_enrichment"]["directives"] = [{"field": "hierarchy"}]
    patch = [{
        "op": "add",
        "path": "/hierarchy/-",
        "value": {"id": "GC", "label": "Grand-child", "parent": "C", "depth": 3, "source": "llm"},
    }]
    _, out = _run_gate(m, patch)
    assert any(f["rule"] == "V7" and f["severity"] == "error" for f in out.get("findings", []))


def test_v7_passes_llm_root_node_null_parent() -> None:
    """LLM node with null/empty parent at depth-0 is a valid root."""
    m = _minimal_manifest()
    m["llm_enrichment"]["directives"] = [{"field": "hierarchy"}]
    patch = [{
        "op": "add",
        "path": "/hierarchy/-",
        "value": {"id": "LLM-ROOT", "label": "New Section", "parent": None, "depth": 0, "source": "llm"},
    }]
    _, out = _run_gate(m, patch)
    errors = [f for f in out.get("findings", []) if f["rule"] == "V7"]
    assert not errors, errors


def test_v7_fails_invalid_source_value() -> None:
    """A hierarchy node with source='garbage' (present after trial-apply) triggers a V7 error."""
    m = _minimal_manifest({"hierarchy": [
        {"id": "ROOT", "label": "Root", "parent": None, "depth": 0, "source": "deterministic"},
    ]})
    m["llm_enrichment"]["directives"] = [{"field": "hierarchy"}]
    # Add a node whose source is not 'deterministic' or 'llm'
    patch = [{
        "op": "add",
        "path": "/hierarchy/-",
        "value": {"id": "BAD-SOURCE", "label": "Bad", "parent": None, "depth": 0, "source": "garbage"},
    }]
    _, out = _run_gate(m, patch)
    errors = [f for f in out.get("findings", []) if f["rule"] == "V7" and f["severity"] == "error"]
    assert errors, f"Expected V7 error for invalid source; got: {out.get('findings', [])}"


# ---------------------------------------------------------------------------
# V8 applies-cleanly
# ---------------------------------------------------------------------------

def test_v8_passes_clean_apply() -> None:
    m = _manifest_with_evidence("E0001")
    m["extraction_result"] = {"conditions": []}
    m["llm_enrichment"]["directives"] = [{"field": "conditions"}]
    patch = [{
        "op": "add",
        "path": "/conditions/-",
        "value": {"id": "COND-X", "evidence_id": "E0001", "source_ref": {}},
    }]
    _, out = _run_gate(m, patch)
    errors = [f for f in out.get("findings", []) if f["rule"] == "V8"]
    assert not errors, errors


def test_v8_fails_bad_array_index() -> None:
    m = _minimal_manifest({"conditions": []})
    m["llm_enrichment"]["directives"] = [{"field": "conditions"}]
    patch = [{"op": "replace", "path": "/conditions/99", "value": {"id": "X"}}]
    _, out = _run_gate(m, patch)
    assert any(f["rule"] == "V8" and f["severity"] == "error" for f in out.get("findings", []))


def test_v8_fails_missing_key() -> None:
    m = _minimal_manifest({"conditions": []})
    m["llm_enrichment"]["directives"] = [{"field": "conditions"}]
    patch = [{"op": "replace", "path": "/nonexistent_field", "value": "x"}]
    _, out = _run_gate(m, patch)
    assert any(f["rule"] == "V8" and f["severity"] == "error" for f in out.get("findings", []))


# ---------------------------------------------------------------------------
# V9 no-op restate (warn)
# ---------------------------------------------------------------------------

def test_v9_passes_real_change() -> None:
    m = _minimal_manifest({"matter_type": None})
    m["llm_enrichment"]["directives"] = [{"field": "matter_type"}]
    patch = [{"op": "replace", "path": "/matter_type", "value": "deal"}]
    _, out = _run_gate(m, patch)
    warns = [f for f in out.get("findings", []) if f["rule"] == "V9"]
    assert not warns, warns


def test_v9_warns_no_op_replace() -> None:
    m = _minimal_manifest({"matter_type": "deal"})
    m["llm_enrichment"]["directives"] = [{"field": "matter_type"}]
    # Bypassing V5 immutability for testing V9: use extraction_warnings (always patchable)
    m["extraction_result"] = {"extraction_warnings": ["existing warning"]}
    patch = [{"op": "replace", "path": "/extraction_warnings/0", "value": "existing warning"}]
    _, out = _run_gate(m, patch)
    warns = [f for f in out.get("findings", []) if f["rule"] == "V9"]
    assert warns, "Expected V9 warn for no-op replace"
    assert warns[0]["severity"] == "warn"


def test_v9_warn_only_is_still_ok() -> None:
    """A patch with only V9 warn must yield rc=0 and ok=true."""
    m = _minimal_manifest()
    m["extraction_result"] = {"extraction_warnings": ["existing warning"]}
    patch = [{"op": "replace", "path": "/extraction_warnings/0", "value": "existing warning"}]
    rc, out = _run_gate(m, patch)
    assert rc == 0
    assert out.get("ok") is True


# ---------------------------------------------------------------------------
# End-to-end: golden manifest + --apply
# ---------------------------------------------------------------------------

def test_e2e_golden_spa_append_condition() -> None:
    """Load the real golden spa manifest, append a condition with valid evidence, run with --apply."""
    with open(SPA_MANIFEST, encoding="utf-8") as f:
        manifest = json.load(f)

    # Pick a known llm evidence_packet id from the manifest.
    le_eps = manifest.get("llm_enrichment", {}).get("evidence_packets", [])
    assert le_eps, "Expected llm evidence_packets in spa manifest"
    ev_id = le_eps[0]["id"]

    patch = [{
        "op": "add",
        "path": "/conditions/-",
        "value": {
            "id": "COND-TEST-E2E",
            "description": "Test end-to-end gate condition added by test.",
            "responsible_party": "Purchaser",
            "evidence_id": ev_id,
            "source_ref": {"source": "en_spa_contract.md"},
        },
    }]

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory() as tmp:
        mpath = Path(tmp) / "manifest.json"
        ppath = Path(tmp) / "patch.json"
        mpath.write_text(json.dumps(manifest), encoding="utf-8")
        ppath.write_text(json.dumps(patch), encoding="utf-8")
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, str(PATCH_GATE), "--manifest", str(mpath), "--patch", str(ppath), "--apply"],
            text=True,
            capture_output=True,
            env=env,
            timeout=60,
        )
    assert proc.returncode == 0, f"Expected exit 0; got {proc.returncode}. stderr: {proc.stderr}"
    out = json.loads(proc.stdout)
    assert out.get("ok") is True, f"Expected ok=true; findings: {out.get('findings')}"
    assert "enriched_extraction_result" in out, "Expected enriched_extraction_result in output"
    cond_ids = [c.get("id") for c in out["enriched_extraction_result"].get("conditions", [])]
    assert "COND-TEST-E2E" in cond_ids, f"Appended condition not found. conditions: {cond_ids}"


# ---------------------------------------------------------------------------
# CLI exit code 2 (parse error)
# ---------------------------------------------------------------------------

def test_cli_exit_2_missing_manifest_file() -> None:
    """Passing a nonexistent manifest path must exit 2."""
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory() as tmp:
        ppath = Path(tmp) / "patch.json"
        ppath.write_text("[]", encoding="utf-8")
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, str(PATCH_GATE), "--manifest", "/nonexistent/path/manifest.json", "--patch", str(ppath)],
            text=True,
            capture_output=True,
            env=env,
            timeout=15,
        )
    assert proc.returncode == 2, f"Expected exit 2 for missing file; got {proc.returncode}"


def test_cli_exit_2_malformed_json_patch() -> None:
    """Passing a malformed JSON patch must exit 2."""
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory() as tmp:
        mpath = Path(tmp) / "manifest.json"
        ppath = Path(tmp) / "patch.json"
        mpath.write_text(json.dumps(_minimal_manifest()), encoding="utf-8")
        ppath.write_text("not valid json{{", encoding="utf-8")
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, str(PATCH_GATE), "--manifest", str(mpath), "--patch", str(ppath)],
            text=True,
            capture_output=True,
            env=env,
            timeout=15,
        )
    assert proc.returncode == 2, f"Expected exit 2 for malformed JSON; got {proc.returncode}"


def test_cli_apply_not_present_when_errors() -> None:
    """enriched_extraction_result must be absent when ok=false, even with --apply."""
    m = _minimal_manifest()
    patch = [{"op": "move", "from": "/x", "path": "/y"}]  # V1 failure
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory() as tmp:
        mpath = Path(tmp) / "manifest.json"
        ppath = Path(tmp) / "patch.json"
        mpath.write_text(json.dumps(m), encoding="utf-8")
        ppath.write_text(json.dumps(patch), encoding="utf-8")
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, str(PATCH_GATE), "--manifest", str(mpath), "--patch", str(ppath), "--apply"],
            text=True,
            capture_output=True,
            env=env,
            timeout=15,
        )
    out = json.loads(proc.stdout)
    assert proc.returncode == 1
    assert "enriched_extraction_result" not in out


# ---------------------------------------------------------------------------
# standalone runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    tests = [(name, fn) for name, fn in sorted(globals().items()) if name.startswith("test_") and callable(fn)]
    passed = failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
            passed += 1
        except Exception:
            print(f"  FAIL  {name}")
            traceback.print_exc()
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
    if failed:
        sys.exit(1)
