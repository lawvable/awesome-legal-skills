"""Tests for eval_pass2.py and extraction/evaluation.py.

Covers: expectation kinds (field_filled, value_matches, entity_added, unchanged),
forbidden kinds (no_entity_added, path_untouched), gate-error short-circuit,
labels-stale warning, vacuous grading, CLI exit 2 on malformed JSON, and
an e2e CLI test on the real en_spa_contract frozen manifest.

Standalone-runnable: python scripts/tests/test_eval_pass2.py
Also discoverable by pytest.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

EVAL_CLI = ROOT / "eval_pass2.py"
FROZEN_DIR = Path(__file__).resolve().parent / "eval" / "manifests"
LABELS_DIR = Path(__file__).resolve().parent / "eval" / "labels"
SPA_FROZEN = FROZEN_DIR / "en_spa_contract.frozen.json"
SPA_LABELS = LABELS_DIR / "en_spa_contract.pass2-labels.json"


# ---------------------------------------------------------------------------
# helpers: manifest builders
# ---------------------------------------------------------------------------

def _minimal_manifest(extraction_result: dict | None = None) -> dict:
    """Return a minimal gate-valid manifest skeleton."""
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


def _sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _run_eval(
    manifest_data: dict,
    patch_data: list,
    labels_data: dict,
) -> tuple[int, dict]:
    """Run eval_pass2 CLI via subprocess; return (returncode, parsed_stdout_dict)."""
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory() as tmp:
        mpath = Path(tmp) / "manifest.json"
        ppath = Path(tmp) / "patch.json"
        lpath = Path(tmp) / "labels.json"
        mpath.write_text(json.dumps(manifest_data), encoding="utf-8")
        ppath.write_text(json.dumps(patch_data), encoding="utf-8")
        lpath.write_text(json.dumps(labels_data), encoding="utf-8")
        args = [
            sys.executable, str(EVAL_CLI),
            "--manifest", str(mpath),
            "--patch", str(ppath),
            "--labels", str(lpath),
        ]
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            args,
            text=True,
            capture_output=True,
            env=env,
            timeout=30,
        )
    out = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, out


def _make_labels(
    fixture: str,
    sha: str,
    labelled: bool = True,
    expectations: list | None = None,
    forbidden: list | None = None,
) -> dict:
    return {
        "schema_version": "legal-diagram-pass2-labels-v1",
        "fixture": fixture,
        "frozen_manifest_sha256": sha,
        "labelled": labelled,
        "expectations": expectations or [],
        "forbidden": forbidden or [],
    }


# ---------------------------------------------------------------------------
# vacuous grading (labelled=false skeleton)
# ---------------------------------------------------------------------------

def test_vacuous_grading_unlabelled_skeleton() -> None:
    """Unlabelled skeleton with labelled=false yields vacuous=true and required_total=0."""
    manifest = _minimal_manifest({"matter_type": None, "extraction_warnings": []})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)

    labels = _make_labels("test_fixture", sha, labelled=False)

    with tempfile.TemporaryDirectory() as tmp:
        mpath = Path(tmp) / "manifest.json"
        ppath = Path(tmp) / "patch.json"
        lpath = Path(tmp) / "labels.json"
        mpath.write_bytes(manifest_bytes)
        ppath.write_text("[]", encoding="utf-8")
        lpath.write_text(json.dumps(labels), encoding="utf-8")
        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, str(EVAL_CLI), "--manifest", str(mpath), "--patch", str(ppath), "--labels", str(lpath)],
            text=True,
            capture_output=True,
            env=env,
            timeout=30,
        )
    assert proc.returncode == 0, f"Expected exit 0; got {proc.returncode}. stderr: {proc.stderr}"
    out = json.loads(proc.stdout)
    assert out.get("ok") is True, out
    assert out.get("vacuous") is True, f"Expected vacuous=true; got {out}"
    assert out["score"]["required_total"] == 0, out["score"]


# ---------------------------------------------------------------------------
# labels-stale warning
# ---------------------------------------------------------------------------

def test_labels_stale_sha_mismatch_warns_but_grades() -> None:
    """When frozen_manifest_sha256 does not match the actual manifest bytes, a warn is emitted but grading still runs."""
    manifest = _minimal_manifest({"matter_type": None})
    labels = _make_labels("test_fixture", "deadbeef" * 8, labelled=True)

    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, f"Expected exit 0; got {rc}. out: {out}"
    assert out.get("ok") is True, out
    stale_findings = [f for f in out.get("gate_findings", []) if f.get("rule") == "labels_stale"]
    assert stale_findings, f"Expected labels_stale warn in gate_findings; got {out.get('gate_findings')}"
    assert stale_findings[0]["severity"] == "warn", stale_findings[0]


# ---------------------------------------------------------------------------
# gate-error short-circuit (illegal patch -> exit 1, ok false, empty results)
# ---------------------------------------------------------------------------

def test_gate_error_blocks_grading() -> None:
    """A patch with an illegal op (unknown op type) causes gate error: exit 1, ok=false, results empty."""
    manifest = _minimal_manifest()
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("test_fixture", sha, labelled=True)

    # 'move' is not in allowed ops (V1 error)
    bad_patch = [{"op": "move", "from": "/x", "path": "/y"}]

    rc, out = _run_eval(manifest, bad_patch, labels)
    assert rc == 1, f"Expected exit 1; got {rc}"
    assert out.get("ok") is False, out
    assert out.get("results") == [], f"Expected empty results; got {out.get('results')}"
    assert out.get("forbidden_violations") == [], f"Expected empty forbidden_violations; got {out.get('forbidden_violations')}"
    # gate_findings should have at least one error
    errors = [f for f in out.get("gate_findings", []) if f.get("severity") == "error"]
    assert errors, f"Expected gate error findings; got {out.get('gate_findings')}"


# ---------------------------------------------------------------------------
# CLI exit 2 on malformed JSON
# ---------------------------------------------------------------------------

def test_cli_exit_2_malformed_manifest() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory() as tmp:
        mpath = Path(tmp) / "manifest.json"
        ppath = Path(tmp) / "patch.json"
        lpath = Path(tmp) / "labels.json"
        mpath.write_text("not valid json{{", encoding="utf-8")
        ppath.write_text("[]", encoding="utf-8")
        lpath.write_text("{}", encoding="utf-8")
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, str(EVAL_CLI), "--manifest", str(mpath), "--patch", str(ppath), "--labels", str(lpath)],
            text=True,
            capture_output=True,
            env=env,
            timeout=15,
        )
    assert proc.returncode == 2, f"Expected exit 2 for malformed manifest; got {proc.returncode}"


def test_cli_exit_2_malformed_patch() -> None:
    manifest = _minimal_manifest()
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory() as tmp:
        mpath = Path(tmp) / "manifest.json"
        ppath = Path(tmp) / "patch.json"
        lpath = Path(tmp) / "labels.json"
        mpath.write_text(json.dumps(manifest), encoding="utf-8")
        ppath.write_text("{not json}", encoding="utf-8")
        lpath.write_text("{}", encoding="utf-8")
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, str(EVAL_CLI), "--manifest", str(mpath), "--patch", str(ppath), "--labels", str(lpath)],
            text=True,
            capture_output=True,
            env=env,
            timeout=15,
        )
    assert proc.returncode == 2, f"Expected exit 2 for malformed patch; got {proc.returncode}"


def test_cli_exit_2_malformed_labels() -> None:
    manifest = _minimal_manifest()
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory() as tmp:
        mpath = Path(tmp) / "manifest.json"
        ppath = Path(tmp) / "patch.json"
        lpath = Path(tmp) / "labels.json"
        mpath.write_text(json.dumps(manifest), encoding="utf-8")
        ppath.write_text("[]", encoding="utf-8")
        lpath.write_text("{bad json", encoding="utf-8")
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, str(EVAL_CLI), "--manifest", str(mpath), "--patch", str(ppath), "--labels", str(lpath)],
            text=True,
            capture_output=True,
            env=env,
            timeout=15,
        )
    assert proc.returncode == 2, f"Expected exit 2 for malformed labels; got {proc.returncode}"


# ---------------------------------------------------------------------------
# expectation kind: field_filled -- pass case
# ---------------------------------------------------------------------------

def test_field_filled_pass_value_present() -> None:
    """field_filled expectation passes when value at path is non-null and non-empty."""
    manifest = _minimal_manifest({"matter_type": "deal"})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "field_filled", "path": "/matter_type", "predicate": {}, "note": ""},
    ])

    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    results = out.get("results", [])
    e1 = next((r for r in results if r["id"] == "E1"), None)
    assert e1 is not None, f"E1 not found in results {results}"
    assert e1["pass"] is True, f"Expected E1 pass=true; got {e1}"


# ---------------------------------------------------------------------------
# expectation kind: field_filled -- fail case
# ---------------------------------------------------------------------------

def test_field_filled_fail_null_value() -> None:
    """field_filled expectation fails when value at path is null."""
    manifest = _minimal_manifest({"matter_type": None})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "field_filled", "path": "/matter_type", "predicate": {}, "note": ""},
    ])

    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    results = out.get("results", [])
    e1 = next((r for r in results if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is False, f"Expected E1 pass=false; got {e1}"


def test_field_filled_fail_empty_string() -> None:
    manifest = _minimal_manifest({"matter_type": ""})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "field_filled", "path": "/matter_type", "predicate": {}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is False, e1


def test_field_filled_fail_empty_list() -> None:
    manifest = _minimal_manifest({"extraction_warnings": []})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "field_filled", "path": "/extraction_warnings", "predicate": {}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is False, e1


# ---------------------------------------------------------------------------
# expectation kind: value_matches (equals) -- pass and fail
# ---------------------------------------------------------------------------

def test_value_matches_equals_pass() -> None:
    """value_matches with equals predicate passes on exact match."""
    manifest = _minimal_manifest({"matter_type": "deal"})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "value_matches", "path": "/matter_type",
         "predicate": {"equals": "deal"}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is True, e1


def test_value_matches_equals_fail() -> None:
    manifest = _minimal_manifest({"matter_type": "litigation"})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "value_matches", "path": "/matter_type",
         "predicate": {"equals": "deal"}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is False, e1


# ---------------------------------------------------------------------------
# value_matches -- one_of predicate
# ---------------------------------------------------------------------------

def test_value_matches_one_of_pass() -> None:
    manifest = _minimal_manifest({"matter_type": "deal"})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "value_matches", "path": "/matter_type",
         "predicate": {"one_of": ["deal", "corporate"]}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is True, e1


def test_value_matches_one_of_fail() -> None:
    manifest = _minimal_manifest({"matter_type": "litigation"})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "value_matches", "path": "/matter_type",
         "predicate": {"one_of": ["deal", "corporate"]}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is False, e1


# ---------------------------------------------------------------------------
# value_matches -- regex predicate
# ---------------------------------------------------------------------------

def test_value_matches_regex_pass() -> None:
    manifest = _minimal_manifest({"matter_type": "deal_2026"})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "value_matches", "path": "/matter_type",
         "predicate": {"regex": "deal.*"}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is True, e1


def test_value_matches_regex_fail() -> None:
    manifest = _minimal_manifest({"matter_type": "litigation"})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "value_matches", "path": "/matter_type",
         "predicate": {"regex": "^deal$"}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is False, e1


def test_value_matches_bad_predicate_exits_2() -> None:
    """value_matches with zero predicate keys (empty dict) must exit 2."""
    manifest = _minimal_manifest({"matter_type": "deal"})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "value_matches", "path": "/matter_type",
         "predicate": {}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 2, f"Expected exit 2 for bad predicate; got {rc}. out: {out}"


def test_value_matches_two_predicate_keys_exits_2() -> None:
    """value_matches with two predicate keys must exit 2."""
    manifest = _minimal_manifest({"matter_type": "deal"})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "value_matches", "path": "/matter_type",
         "predicate": {"equals": "deal", "one_of": ["deal"]}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 2, f"Expected exit 2 for ambiguous predicate; got {rc}. out: {out}"


# ---------------------------------------------------------------------------
# expectation kind: entity_added -- pass and fail
# ---------------------------------------------------------------------------

def _make_entity_manifest_with_obligation() -> tuple[dict, str, bytes]:
    """Manifest with obligations array containing OBL-001; returns (manifest, ev_id, raw_bytes)."""
    ev_id = "E0001"
    manifest = _minimal_manifest({
        "obligations": [{"id": "OBL-001", "description": "existing", "risk_level": None}],
    })
    manifest["llm_enrichment"]["evidence_packets"] = [{"id": ev_id, "snippet": "s"}]
    manifest["llm_enrichment"]["directives"] = [{"field": "obligations[].risk_level"}]
    raw = json.dumps(manifest).encode("utf-8")
    return manifest, ev_id, raw


def test_entity_added_pass_entity_exists_after_patch() -> None:
    """entity_added passes when the named entity is present in the enriched result."""
    manifest, ev_id, raw = _make_entity_manifest_with_obligation()
    sha = _sha256_of(raw)

    # Patch adds OBL-002
    patch = [{
        "op": "add",
        "path": "/obligations/-",
        "value": {"id": "OBL-002", "description": "new obligation", "risk_level": "high",
                  "evidence_id": ev_id, "source_ref": {"source": "test.md"}},
    }]
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "entity_added",
         "path": "", "predicate": {"array": "obligations", "match": {"id": "OBL-002"}}, "note": ""},
    ])
    rc, out = _run_eval(manifest, patch, labels)
    assert rc == 0, f"rc={rc}; out={out}"
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is True, e1


def test_entity_added_fail_entity_not_in_enriched() -> None:
    """entity_added fails when the entity is not present after the patch."""
    manifest, _, raw = _make_entity_manifest_with_obligation()
    sha = _sha256_of(raw)

    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "entity_added",
         "path": "", "predicate": {"array": "obligations", "match": {"id": "OBL-GHOST"}}, "note": ""},
    ])
    # Empty patch -- OBL-GHOST never added
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is False, e1


def test_entity_added_fail_entity_already_existed_in_frozen() -> None:
    """entity_added fails when the matching entity already existed in the frozen manifest (not truly added)."""
    manifest, _, raw = _make_entity_manifest_with_obligation()
    sha = _sha256_of(raw)

    # OBL-001 already exists in frozen extraction_result; entity_added should fail
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "entity_added",
         "path": "", "predicate": {"array": "obligations", "match": {"id": "OBL-001"}}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is False, f"entity_added should fail for pre-existing entity; got {e1}"


# ---------------------------------------------------------------------------
# expectation kind: unchanged -- pass and fail
# ---------------------------------------------------------------------------

def test_unchanged_pass_value_same_after_patch() -> None:
    """unchanged passes when the value at path is the same in frozen and enriched result."""
    manifest = _minimal_manifest({"matter_type": "deal"})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "unchanged", "path": "/matter_type",
         "predicate": {}, "note": ""},
    ])
    # Empty patch keeps matter_type unchanged
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is True, e1


def test_unchanged_fail_value_changed_by_patch() -> None:
    """unchanged fails when a patch replaces the value at path."""
    manifest = _minimal_manifest({"matter_type": None})
    manifest["llm_enrichment"]["directives"] = [{"field": "matter_type"}]
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=True, expectations=[
        {"id": "E1", "credit": "required", "kind": "unchanged", "path": "/matter_type",
         "predicate": {}, "note": ""},
    ])
    # Patch replaces matter_type: null -> "deal"
    patch = [{"op": "replace", "path": "/matter_type", "value": "deal"}]
    rc, out = _run_eval(manifest, patch, labels)
    assert rc == 0, out
    e1 = next((r for r in out["results"] if r["id"] == "E1"), None)
    assert e1 is not None
    assert e1["pass"] is False, e1


# ---------------------------------------------------------------------------
# forbidden kind: no_entity_added -- clean and violation
# ---------------------------------------------------------------------------

def test_no_entity_added_clean_no_new_entities() -> None:
    """no_entity_added is not violated when the patch does not add a matching entity."""
    manifest, _, raw = _make_entity_manifest_with_obligation()
    sha = _sha256_of(raw)

    labels = _make_labels("t", sha, labelled=True, forbidden=[
        {"id": "F1", "kind": "no_entity_added", "array": "obligations",
         "match": {"id": "OBL-999"}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    assert out.get("forbidden_violations") == [], f"Expected no violations; got {out.get('forbidden_violations')}"


def test_no_entity_added_violation_entity_was_added() -> None:
    """no_entity_added is violated when the patch adds an entity matching the match dict."""
    manifest, ev_id, raw = _make_entity_manifest_with_obligation()
    sha = _sha256_of(raw)

    patch = [{
        "op": "add",
        "path": "/obligations/-",
        "value": {"id": "OBL-FORBIDDEN", "description": "forbidden",
                  "evidence_id": ev_id, "source_ref": {"source": "test.md"}},
    }]
    labels = _make_labels("t", sha, labelled=True, forbidden=[
        {"id": "F1", "kind": "no_entity_added", "array": "obligations",
         "match": {"id": "OBL-FORBIDDEN"}, "note": ""},
    ])
    rc, out = _run_eval(manifest, patch, labels)
    assert rc == 0, f"Forbidden violations are reported, not blocking; expected exit 0; got {rc}"
    violations = out.get("forbidden_violations", [])
    assert any(v["id"] == "F1" for v in violations), f"Expected F1 in violations; got {violations}"


# ---------------------------------------------------------------------------
# forbidden kind: path_untouched -- clean and violation
# ---------------------------------------------------------------------------

def test_path_untouched_clean_path_was_changed() -> None:
    """path_untouched is not violated when the patch changes the value at path."""
    manifest = _minimal_manifest({"matter_type": None})
    manifest["llm_enrichment"]["directives"] = [{"field": "matter_type"}]
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)

    patch = [{"op": "replace", "path": "/matter_type", "value": "deal"}]
    labels = _make_labels("t", sha, labelled=True, forbidden=[
        {"id": "F1", "kind": "path_untouched", "path": "/matter_type", "note": ""},
    ])
    rc, out = _run_eval(manifest, patch, labels)
    assert rc == 0, out
    assert out.get("forbidden_violations") == [], f"Expected no violations; got {out.get('forbidden_violations')}"


def test_path_untouched_violation_path_unchanged() -> None:
    """path_untouched is violated when the patch does not change the value at the given path."""
    manifest = _minimal_manifest({"matter_type": "deal"})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)

    labels = _make_labels("t", sha, labelled=True, forbidden=[
        {"id": "F1", "kind": "path_untouched", "path": "/matter_type", "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    violations = out.get("forbidden_violations", [])
    assert any(v["id"] == "F1" for v in violations), f"Expected F1 in violations; got {violations}"


def test_path_untouched_violation_path_removed() -> None:
    """path_untouched is violated when the patch removes the value at the given path.

    Context: a hierarchy node exists in the frozen manifest; the patch removes it (allowed by V6).
    path_untouched must detect that the node no longer exists and report a violation.
    """
    manifest = _minimal_manifest({
        "hierarchy": [
            {"id": "ROOT", "label": "Root", "parent": None, "depth": 0, "source": "deterministic"},
            {"id": "CHILD", "label": "Child", "parent": "ROOT", "depth": 1, "source": "llm"},
        ],
    })
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)

    # Patch removes the CHILD node (index 1), which passes V6 (remove allowed under /hierarchy)
    patch = [{"op": "remove", "path": "/hierarchy/1"}]
    labels = _make_labels("t", sha, labelled=True, forbidden=[
        {"id": "F1", "kind": "path_untouched", "path": "/hierarchy/1", "note": ""},
    ])
    rc, out = _run_eval(manifest, patch, labels)
    assert rc == 0, f"Expected exit 0; got {rc}. out={out}"
    violations = out.get("forbidden_violations", [])
    f1_violations = [v for v in violations if v["id"] == "F1"]
    assert f1_violations, f"Expected F1 violation for removed path; got {violations}"
    assert any("removed" in v.get("detail", "").lower() for v in f1_violations), \
        f"Expected 'removed' in detail; got {f1_violations}"


# ---------------------------------------------------------------------------
# score structure checks
# ---------------------------------------------------------------------------

def test_score_counts_required_and_bonus() -> None:
    """Score counts required vs bonus expectations correctly."""
    manifest = _minimal_manifest({"matter_type": "deal", "extraction_warnings": []})
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)

    labels = _make_labels("t", sha, labelled=True, expectations=[
        # required: pass
        {"id": "E1", "credit": "required", "kind": "field_filled", "path": "/matter_type",
         "predicate": {}, "note": ""},
        # required: fail (empty list)
        {"id": "E2", "credit": "required", "kind": "field_filled", "path": "/extraction_warnings",
         "predicate": {}, "note": ""},
        # bonus: pass
        {"id": "E3", "credit": "bonus", "kind": "value_matches", "path": "/matter_type",
         "predicate": {"equals": "deal"}, "note": ""},
    ])
    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    score = out.get("score", {})
    assert score.get("required_total") == 2, score
    assert score.get("required_pass") == 1, score
    assert score.get("bonus_total") == 1, score
    assert score.get("bonus_pass") == 1, score


# ---------------------------------------------------------------------------
# output structure checks
# ---------------------------------------------------------------------------

def test_output_structure_has_all_keys() -> None:
    """Output object carries all required top-level keys."""
    manifest = _minimal_manifest()
    manifest_bytes = json.dumps(manifest).encode("utf-8")
    sha = _sha256_of(manifest_bytes)
    labels = _make_labels("t", sha, labelled=False)

    rc, out = _run_eval(manifest, [], labels)
    assert rc == 0, out
    for key in ("ok", "fixture", "labelled", "gate_findings", "results", "forbidden_violations", "score"):
        assert key in out, f"Missing key {key!r} in output: {out.keys()}"


# ---------------------------------------------------------------------------
# e2e via CLI subprocess: real en_spa_contract frozen manifest + skeleton labels + minimal patch
# ---------------------------------------------------------------------------

def test_e2e_spa_contract_vacuous_grading() -> None:
    """E2E test: frozen en_spa_contract + its real skeleton labels + legal patch that passes gate.

    The labels skeleton has labelled=false; grading is vacuous.
    Exit must be 0, ok=true, vacuous=true.
    """
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    # The hint patch: replace obligations/0/risk_level with 'high' passes the gate
    patch = [{"op": "replace", "path": "/obligations/0/risk_level", "value": "high"}]

    with tempfile.TemporaryDirectory() as tmp:
        ppath = Path(tmp) / "patch.json"
        ppath.write_text(json.dumps(patch), encoding="utf-8")
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [
                sys.executable, str(EVAL_CLI),
                "--manifest", str(SPA_FROZEN),
                "--patch", str(ppath),
                "--labels", str(SPA_LABELS),
            ],
            text=True,
            capture_output=True,
            env=env,
            timeout=30,
        )
    assert proc.returncode == 0, (
        f"Expected exit 0; got {proc.returncode}. stderr: {proc.stderr!r}. stdout: {proc.stdout!r}"
    )
    out = json.loads(proc.stdout)
    assert out.get("ok") is True, f"Expected ok=true; findings: {out.get('gate_findings')}"
    assert out.get("vacuous") is True, f"Expected vacuous=true; out: {out}"


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
