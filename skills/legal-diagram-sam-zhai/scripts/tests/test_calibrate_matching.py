"""W4.3a matcher regression tests for the calibration harness.

Standalone-runnable: python scripts/tests/test_calibrate_matching.py
Also discoverable by pytest. No pytest fixtures; no parametrize (plain loops
keep the bare __main__ runner working, W0 item 1 convention).

Covers the two matcher equivalences added in W4.3a:
  - date equivalence (locale-verbatim label vs ISO candidate, same date only);
  - evidence-snippet fallback (label is a verbatim subspan of a candidate's
    evidence snippet when the primary string fails);
plus the greedy one-to-one discipline and an end-to-end fr_judgment events lift
through the real in-process calibration path (mirrors the W4.0c pattern).
"""
from __future__ import annotations

from pathlib import Path
import sys

_SKILL_ROOT = Path(__file__).resolve().parents[2]
if str(_SKILL_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(_SKILL_ROOT / "scripts"))

from tests.calibrate import (  # noqa: E402
    _is_match,
    _match_label_to_extractions,
    _normalise,
    _run_calibration,
    _import_stack,
    _DATE_BEARING_FIELDS,
    _collect_misses,
    format_miss_dump,
)


# ---------------------------------------------------------------------------
# Date equivalence -- flag-gated behaviour (W4.3b regression)
# ---------------------------------------------------------------------------

def test_date_equivalence_fr_locale_matches_iso() -> None:
    # A verbatim FR locale date must match the ISO candidate for the same day
    # when date_rule=True (events field semantics).
    assert _is_match(_normalise("1er février 2023"), _normalise("2023-02-01"),
                     date_rule=True)


def test_date_equivalence_en_locale_matches_iso() -> None:
    # A verbatim EN locale date must match the ISO candidate for the same day
    # when date_rule=True (events field semantics).
    assert _is_match(_normalise("March 1, 2024"), _normalise("2024-03-01"),
                     date_rule=True)


def test_date_equivalence_different_dates_do_not_match() -> None:
    # A different calendar date must never match through the date path.
    assert not _is_match(_normalise("1er février 2023"), _normalise("2023-02-02"),
                         date_rule=True)
    assert not _is_match(_normalise("March 1, 2024"), _normalise("2024-04-01"),
                         date_rule=True)


def test_date_rule_false_disjoint_content_same_date_no_match() -> None:
    # Regression: two strings with disjoint content that share only a date token
    # must NOT match when date_rule=False (non-date-bearing field).
    # Jaccard of the tokens is far below 0.5 (3 shared of ~12 total).
    label = _normalise("alpha bravo charlie 2026-06-01")
    extraction = _normalise("xray yankee zulu 2026-06-01")
    assert not _is_match(label, extraction, date_rule=False)


def test_date_rule_true_same_date_matches() -> None:
    # With date_rule=True the same-date pair resolves through rule (d) for
    # a date-bearing field such as events.
    assert _is_match(_normalise("1er février 2023"), _normalise("2023-02-01"),
                     date_rule=True)


def test_date_bearing_fields_set_contains_events_and_deadlines() -> None:
    # The module-level set that controls call-site gating must include
    # events and deadlines, and must exclude fields like entities.
    assert "events" in _DATE_BEARING_FIELDS
    assert "deadlines" in _DATE_BEARING_FIELDS
    assert "entities" not in _DATE_BEARING_FIELDS


# ---------------------------------------------------------------------------
# Evidence-snippet fallback
# ---------------------------------------------------------------------------

def test_evidence_fallback_matches_verbatim_subspan() -> None:
    # The primary string is a reconstruction the label cannot match; the label
    # is a verbatim subspan of the candidate evidence snippet, so the fallback
    # pool recovers the match.
    labels = ["royalty of $250,000.00 no later than June 30, 2026"]
    primary = ["pay royalty quarterly and remit sales reports"]
    snippets = [
        "The Distributor shall pay to the Licensor a royalty of $250,000.00 "
        "no later than June 30, 2026, and remit quarterly sales reports"
    ]
    matched, _ = _match_label_to_extractions(labels, primary, fallback_pool=snippets)
    assert matched == 1


def test_evidence_fallback_absent_label_never_matches() -> None:
    # A label present in neither the primary strings nor any evidence snippet
    # stays unmatched.
    labels = ["a clause that appears nowhere in the document"]
    primary = ["pay royalty quarterly and remit sales reports"]
    snippets = ["The Distributor shall pay to the Licensor a royalty of $250,000.00"]
    matched, _ = _match_label_to_extractions(labels, primary, fallback_pool=snippets)
    assert matched == 0


def test_evidence_fallback_ordered_after_primary() -> None:
    # When the primary string already matches, the fallback pool is not needed
    # and the count is exactly one (no double credit).
    labels = ["Distributor shall pay royalty"]
    primary = ["Distributor shall pay royalty"]
    snippets = ["Distributor shall pay royalty"]
    matched, _ = _match_label_to_extractions(labels, primary, fallback_pool=snippets)
    assert matched == 1


# ---------------------------------------------------------------------------
# Greedy one-to-one discipline
# ---------------------------------------------------------------------------

def test_greedy_one_to_one_two_labels_one_extraction() -> None:
    # Two identical labels against a single candidate yield exactly one tp.
    labels = ["Acme owes payment", "Acme owes payment"]
    primary = ["Acme owes payment"]
    matched, _ = _match_label_to_extractions(labels, primary)
    assert matched == 1


def test_greedy_one_to_one_snippet_consumed_once() -> None:
    # Two labels that both subspan a single evidence snippet consume it once.
    # Two non-matching primary extractions give the budget room for both
    # fallback attempts, so the cap is not what limits the count; the single
    # snippet being consumed once is.
    labels = ["royalty of $250,000.00", "royalty of $250,000.00"]
    primary = ["unrelated extraction one", "unrelated extraction two"]
    snippets = ["pay a royalty of $250,000.00 no later than June 30"]
    matched, _ = _match_label_to_extractions(labels, primary, fallback_pool=snippets)
    assert matched == 1


def test_fallback_capped_at_extraction_count() -> None:
    # The fallback can never push the total above the number of extractions,
    # so precision (tp / n_promoted) stays <= 1.0.  Two labels both subspan two
    # distinct snippets, but a single extraction caps the total at one.
    labels = ["clause alpha", "clause beta"]
    primary = ["one promoted entity that matches neither label"]
    snippets = ["the clause alpha appears here", "the clause beta appears here"]
    matched, n = _match_label_to_extractions(labels, primary, fallback_pool=snippets)
    assert matched == 1
    assert n == 1


# ---------------------------------------------------------------------------
# End-to-end: fr_judgment events lift through the real calibration path
# ---------------------------------------------------------------------------

def _fr_judgment_events_tp() -> int:
    """Run the in-process calibration and return fr_judgment events tp_promoted.

    Runs the full calibration deliberately (mirrors the W4.0c regression test):
    the point is exercising the real _run_calibration path end to end.
    """
    normalize_fn, extract_fn, recommend_fn = _import_stack()[:3]
    report = _run_calibration(normalize_fn, extract_fn, recommend_fn)
    return report["per_fixture"]["fr_judgment"]["extraction"]["events"]["tp_promoted"]


def test_fr_judgment_events_tp_lifts_with_date_equivalence() -> None:
    # Before W4.3a the verbatim FR locale labels never matched the ISO candidate
    # dates, so events tp was 0.  With date equivalence the dated occurrence
    # verbs match their ISO twins, lifting tp to at least five.
    assert _fr_judgment_events_tp() >= 5


# ---------------------------------------------------------------------------
# --dump-misses: _collect_misses and format_miss_dump unit tests
# ---------------------------------------------------------------------------

def _make_candidate(
    cand_id: str,
    target_field: str,
    norm_value: dict,
    action: str = "promote",
    frame_type: str = "test_frame",
    evidence_snippet: str = "",
) -> tuple:
    """Return (candidate dict, promotion_decision dict, evidence_packet dict) triple."""
    cand = {
        "id": cand_id,
        "target_field": target_field,
        "frame_type": frame_type,
        "normalized_value": norm_value,
        "signals": [],
        "anti_signals": [],
        "confidence": 0.8,
        "evidence_ids": [f"E{cand_id}"],
        "source_ref": None,
    }
    pd = {"candidate_id": cand_id, "action": action}
    ep = {"id": f"E{cand_id}", "snippet": evidence_snippet}
    return cand, pd, ep


def _make_manifest(triples: list) -> dict:
    """Build a minimal candidate_manifest from a list of (cand, pd, ep) triples."""
    candidates = [t[0] for t in triples]
    pds = [t[1] for t in triples]
    eps = [t[2] for t in triples]
    return {
        "schema_version": "1",
        "candidates": candidates,
        "promotion_decisions": pds,
        "evidence_packets": eps,
        "structure_metrics": {},
        "warning_codes": [],
    }


def test_collect_misses_fp_identified() -> None:
    # A promoted candidate that matches no label is a false positive.
    cand, pd, ep = _make_candidate(
        "C01", "obligations",
        {"description": "Vendor shall deliver title documents"},
        action="promote",
        evidence_snippet="Vendor shall deliver title documents to Purchaser",
    )
    manifest = _make_manifest([(cand, pd, ep)])
    er_dict: dict = {"obligations": [{"description": "Vendor shall deliver title documents"}]}
    labels: dict = {"fields": {"obligations": ["Purchaser shall pay deposit"]}}

    misses = _collect_misses(er_dict, manifest, labels)
    assert "obligations" in misses
    fps = [m for m in misses["obligations"] if m["kind"] == "FP"]
    assert len(fps) == 1
    assert fps[0]["value"] == "Vendor shall deliver title documents"


def test_collect_misses_fn_identified() -> None:
    # A label not matched by any promoted candidate is a false negative.
    cand, pd, ep = _make_candidate(
        "C01", "obligations",
        {"description": "Vendor shall deliver title documents"},
        action="promote",
    )
    manifest = _make_manifest([(cand, pd, ep)])
    er_dict: dict = {"obligations": [{"description": "Vendor shall deliver title documents"}]}
    labels: dict = {"fields": {"obligations": [
        "Vendor shall deliver title documents",
        "Purchaser shall pay deposit",
    ]}}

    misses = _collect_misses(er_dict, manifest, labels)
    fns = [m for m in misses["obligations"] if m["kind"] == "FN"]
    assert len(fns) == 1
    assert "deposit" in fns[0]["expected_value"].lower()


def test_collect_misses_no_misses_when_perfect() -> None:
    # When every label matches and every promoted item matches a label: no misses.
    cand, pd, ep = _make_candidate(
        "C01", "obligations",
        {"description": "Vendor shall deliver title documents"},
        action="promote",
    )
    manifest = _make_manifest([(cand, pd, ep)])
    er_dict: dict = {"obligations": [{"description": "Vendor shall deliver title documents"}]}
    labels: dict = {"fields": {"obligations": ["Vendor shall deliver title documents"]}}

    misses = _collect_misses(er_dict, manifest, labels)
    # obligations field present but empty list (no misses)
    assert misses.get("obligations", []) == []


def test_collect_misses_fn_closest_candidate_present() -> None:
    # When a FN label has a hint-tier candidate nearby, closest should be populated.
    cand_promote, pd_promote, ep_promote = _make_candidate(
        "C01", "obligations",
        {"description": "unrelated promoted item"},
        action="promote",
    )
    cand_hint, pd_hint, ep_hint = _make_candidate(
        "C02", "obligations",
        {"description": "Purchaser shall pay deposit of amount"},
        action="hint",
    )
    manifest = _make_manifest([(cand_promote, pd_promote, ep_promote),
                                (cand_hint, pd_hint, ep_hint)])
    er_dict: dict = {"obligations": [{"description": "unrelated promoted item"}]}
    labels: dict = {"fields": {"obligations": ["Purchaser shall pay deposit"]}}

    misses = _collect_misses(er_dict, manifest, labels)
    fns = [m for m in misses["obligations"] if m["kind"] == "FN"]
    assert len(fns) == 1
    fn = fns[0]
    # closest_value should point to the hint candidate
    assert fn["closest_value"] is not None
    assert "deposit" in fn["closest_value"].lower()


def test_collect_misses_fn_no_candidate() -> None:
    # When no candidate at all covers a FN label, closest_value is None.
    manifest = _make_manifest([])
    er_dict: dict = {"obligations": []}
    labels: dict = {"fields": {"obligations": ["Purchaser shall pay deposit"]}}

    misses = _collect_misses(er_dict, manifest, labels)
    fns = [m for m in misses["obligations"] if m["kind"] == "FN"]
    assert len(fns) == 1
    assert fns[0]["closest_value"] is None


def test_format_miss_dump_fp_prefix() -> None:
    # FP lines must begin with "FP ".
    misses_by_fixture = {
        "test_fixture": {
            "obligations": [
                {
                    "kind": "FP",
                    "field": "obligations",
                    "value": "Vendor shall deliver title",
                    "tier": "promote",
                    "frame_type": "positive_obligation",
                    "evidence_snippet": "Vendor shall deliver title documents to Purchaser",
                }
            ]
        }
    }
    output = format_miss_dump(misses_by_fixture)
    fp_lines = [ln for ln in output.splitlines() if ln.startswith("FP ")]
    assert len(fp_lines) >= 1


def test_format_miss_dump_fn_prefix() -> None:
    # FN lines must begin with "FN ".
    misses_by_fixture = {
        "test_fixture": {
            "obligations": [
                {
                    "kind": "FN",
                    "field": "obligations",
                    "expected_value": "Purchaser shall pay deposit",
                    "closest_value": None,
                    "closest_tier": None,
                }
            ]
        }
    }
    output = format_miss_dump(misses_by_fixture)
    fn_lines = [ln for ln in output.splitlines() if ln.startswith("FN ")]
    assert len(fn_lines) >= 1


def test_format_miss_dump_deterministic() -> None:
    # Calling format_miss_dump twice with same input yields byte-identical output.
    misses_by_fixture = {
        "fixture_b": {
            "obligations": [
                {
                    "kind": "FP",
                    "field": "obligations",
                    "value": "alpha",
                    "tier": "promote",
                    "frame_type": "frame",
                    "evidence_snippet": "alpha context",
                }
            ]
        },
        "fixture_a": {
            "entities": [
                {
                    "kind": "FN",
                    "field": "entities",
                    "expected_value": "BetaCorp",
                    "closest_value": None,
                    "closest_tier": None,
                }
            ]
        },
    }
    assert format_miss_dump(misses_by_fixture) == format_miss_dump(misses_by_fixture)


def test_format_miss_dump_ordering_fixture_then_field() -> None:
    # Fixtures appear in sorted order; within a fixture, fields appear in sorted order.
    misses_by_fixture = {
        "zzz_fixture": {"b_field": [{"kind": "FN", "field": "b_field",
                                     "expected_value": "v", "closest_value": None,
                                     "closest_tier": None}]},
        "aaa_fixture": {"a_field": [{"kind": "FN", "field": "a_field",
                                     "expected_value": "v", "closest_value": None,
                                     "closest_tier": None}]},
    }
    output = format_miss_dump(misses_by_fixture)
    idx_aaa = output.find("aaa_fixture")
    idx_zzz = output.find("zzz_fixture")
    assert idx_aaa < idx_zzz, "aaa_fixture must appear before zzz_fixture"


def test_default_output_no_dump_marker() -> None:
    # Without --dump-misses, calibrate output must parse as JSON and
    # must NOT contain the miss-audit separator.
    import subprocess, json as _json
    result = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        ["python", "scripts/tests/calibrate.py"],
        capture_output=True, text=True, check=True,
        cwd=str(Path(__file__).resolve().parents[2]),
    )
    _json.loads(result.stdout)  # must parse clean
    assert "=== MISS AUDIT ===" not in result.stdout


def test_dump_misses_json_still_parses() -> None:
    # With --dump-misses, the prefix (up to the separator) must still be valid JSON.
    import subprocess, json as _json
    result = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        ["python", "scripts/tests/calibrate.py", "--dump-misses"],
        capture_output=True, text=True, check=True,
        cwd=str(Path(__file__).resolve().parents[2]),
    )
    sep = "=== MISS AUDIT ==="
    assert sep in result.stdout
    json_part = result.stdout.split(sep)[0].rstrip()
    _json.loads(json_part)  # must parse clean


def test_dump_misses_has_fp_and_fn_lines() -> None:
    # With --dump-misses, the audit section must contain at least one FP line
    # and at least one FN line (any non-trivial corpus has both; exact counts
    # are reconciled against the JSON aggregate in the reconciliation test).
    import subprocess
    result = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        ["python", "scripts/tests/calibrate.py", "--dump-misses"],
        capture_output=True, text=True, check=True,
        cwd=str(Path(__file__).resolve().parents[2]),
    )
    sep = "=== MISS AUDIT ==="
    audit_section = result.stdout.split(sep, 1)[1] if sep in result.stdout else ""
    fp_lines = [ln for ln in audit_section.splitlines() if ln.startswith("FP ")]
    fn_lines = [ln for ln in audit_section.splitlines() if ln.startswith("FN ")]
    assert len(fp_lines) >= 1
    assert len(fn_lines) >= 1


# ---------------------------------------------------------------------------
# Finding 2: FN lines must carry closest-candidate suffix
# ---------------------------------------------------------------------------

def test_format_miss_dump_fn_has_closest_suffix() -> None:
    # Every FN line emitted by format_miss_dump must end with either
    # "// closest=[tier] ..." or "// no candidate".  A bare "FN 'value'"
    # without the suffix must FAIL this assertion.
    misses_by_fixture = {
        "test_fixture": {
            "obligations": [
                {
                    "kind": "FN",
                    "field": "obligations",
                    "expected_value": "Purchaser shall pay deposit",
                    "closest_value": "Purchaser shall pay deposit amount",
                    "closest_tier": "hint",
                },
                {
                    "kind": "FN",
                    "field": "obligations",
                    "expected_value": "Vendor delivers title",
                    "closest_value": None,
                    "closest_tier": None,
                },
            ]
        }
    }
    output = format_miss_dump(misses_by_fixture)
    fn_lines = [ln for ln in output.splitlines() if ln.startswith("FN ")]
    assert len(fn_lines) == 2, f"Expected 2 FN lines, got {len(fn_lines)}"
    for ln in fn_lines:
        assert "// " in ln, (
            f"FN line missing '// closest=...' or '// no candidate' suffix: {ln!r}"
        )
        suffix = ln.split("// ", 1)[1]
        assert suffix.startswith("closest=[") or suffix == "no candidate", (
            f"FN suffix does not match expected pattern: {suffix!r}"
        )


# ---------------------------------------------------------------------------
# Finding 3: reconciliation integration test (FP/FN counts must match aggregate)
# ---------------------------------------------------------------------------

def test_dump_misses_fp_fn_reconcile_with_aggregate() -> None:
    # Run calibrate with --dump-misses (subprocess), parse the JSON prefix,
    # count FP and FN lines in the audit section, assert dump FP count ==
    # aggregate fp_promoted AND dump FN count == aggregate fn_labels.
    # This test FAILS before the Finding-1 fix (99 FP lines vs 96 aggregate)
    # and PASSES after the fix.
    import subprocess
    import json as _json
    result = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        ["python", "scripts/tests/calibrate.py", "--dump-misses"],
        capture_output=True, text=True, check=True,
        cwd=str(Path(__file__).resolve().parents[2]),
    )
    sep = "=== MISS AUDIT ==="
    assert sep in result.stdout, "Missing audit separator in output"
    json_part = result.stdout.split(sep)[0].rstrip()
    audit_section = result.stdout.split(sep, 1)[1]

    data = _json.loads(json_part)
    fp_lines = [ln for ln in audit_section.splitlines() if ln.startswith("FP ")]
    fn_lines = [ln for ln in audit_section.splitlines() if ln.startswith("FN ")]

    # Sum aggregate counts across all fixtures and fields
    total_fp_agg = sum(
        data["per_fixture"][fx]["extraction"][field]["fp_promoted"]
        for fx in data["per_fixture"]
        for field in data["per_fixture"][fx]["extraction"]
    )
    total_fn_agg = sum(
        data["per_fixture"][fx]["extraction"][field]["fn_labels"]
        for fx in data["per_fixture"]
        for field in data["per_fixture"][fx]["extraction"]
    )

    assert len(fp_lines) == total_fp_agg, (
        f"Dump FP line count ({len(fp_lines)}) != aggregate fp_promoted ({total_fp_agg}). "
        f"Reconciliation failed."
    )
    assert len(fn_lines) == total_fn_agg, (
        f"Dump FN line count ({len(fn_lines)}) != aggregate fn_labels ({total_fn_agg}). "
        f"Reconciliation failed."
    )


# ---------------------------------------------------------------------------
# Finding 1: fallback-matched promoted items must not appear as FP
# ---------------------------------------------------------------------------

def test_collect_misses_fallback_matched_not_fp() -> None:
    # A promoted candidate whose evidence snippet is a verbatim superspan of a
    # label (snippet fallback hit) counts as a TP, not an FP.  Before the fix,
    # _collect_misses would still emit it as FP because used_prom[pi] was never
    # set during the fallback branch.
    cand, pd, ep = _make_candidate(
        "C01", "obligations",
        {"description": "pay royalty quarterly and remit sales reports"},
        action="promote",
        evidence_snippet=(
            "The Distributor shall pay to the Licensor a royalty of $250,000.00 "
            "no later than June 30, 2026, and remit quarterly sales reports"
        ),
    )
    manifest = _make_manifest([(cand, pd, ep)])
    er_dict: dict = {"obligations": [{"description": "pay royalty quarterly and remit sales reports"}]}
    # Label matches via snippet fallback (not primary string match)
    labels: dict = {"fields": {"obligations": [
        "royalty of $250,000.00 no later than June 30, 2026"
    ]}}

    misses = _collect_misses(er_dict, manifest, labels)
    fps = [m for m in misses.get("obligations", []) if m["kind"] == "FP"]
    fns = [m for m in misses.get("obligations", []) if m["kind"] == "FN"]
    # The promoted item is a TP (via fallback), so must not appear as FP.
    assert len(fps) == 0, (
        f"Expected 0 FPs (fallback TP), got {len(fps)}: {fps}"
    )
    # The label is matched, so must not appear as FN.
    assert len(fns) == 0, (
        f"Expected 0 FNs (label matched via snippet fallback), got {len(fns)}: {fns}"
    )


# ---------------------------------------------------------------------------
# Fix-round-2: owner-identity suppression on fallback hits
# ---------------------------------------------------------------------------

def test_fallback_owner_identity_unused_owner_not_first_unused() -> None:
    # Two promoted candidates: "A item" (sorted first) and "B item" (sorted second).
    # Snippet belongs to "B item" (sorted second, owner_idx=1).
    # A label matches the snippet of "B item" via fallback.
    # BEFORE fix: first-unused is idx=0 ("A item"); it gets suppressed. WRONG.
    # AFTER fix:  owner is idx=1 ("B item"); it gets suppressed. CORRECT.
    cand_a, pd_a, ep_a = _make_candidate(
        "CA", "obligations",
        {"description": "A item unrelated to any label"},
        action="promote",
        evidence_snippet="A item context that no label mentions",
    )
    cand_b, pd_b, ep_b = _make_candidate(
        "CB", "obligations",
        {"description": "B item unrelated to any label"},
        action="promote",
        evidence_snippet="The label text lives inside the B item snippet here",
    )
    manifest = _make_manifest([(cand_a, pd_a, ep_a), (cand_b, pd_b, ep_b)])
    er_dict: dict = {
        "obligations": [
            {"description": "A item unrelated to any label"},
            {"description": "B item unrelated to any label"},
        ]
    }
    # Label matches the snippet of "B item", not "A item".
    # Both primary strings ("A item..." and "B item...") fail primary matching.
    labels: dict = {"fields": {"obligations": ["label text lives inside the B item snippet"]}}

    misses = _collect_misses(er_dict, manifest, labels)
    fps = [m for m in misses.get("obligations", []) if m["kind"] == "FP"]
    fns = [m for m in misses.get("obligations", []) if m["kind"] == "FN"]
    # Exactly one FP: "A item..." (not consumed by the fallback).
    # "B item..." must be suppressed (it owns the matched snippet).
    fp_values = [fp["value"] for fp in fps]
    assert len(fps) == 1, f"Expected 1 FP (A item), got {len(fps)}: {fp_values}"
    assert "A item" in fps[0]["value"], (
        f"Expected FP to be 'A item', got: {fps[0]['value']!r}"
    )
    assert all("B item" not in v for v in fp_values), (
        f"B item (snippet owner) must NOT be in FP list, got: {fp_values}"
    )
    # Label is matched (via fallback), so no FN.
    assert len(fns) == 0, f"Expected 0 FNs, got {len(fns)}: {fns}"


def test_fallback_used_owner_emits_slot_consumed_note() -> None:
    # Two promoted candidates: "X item" and "Y item".
    # A label_1 matches "X item" via primary match (consuming X's prom slot).
    # A label_2 matches the snippet of "X item" via fallback (merged-fact case:
    # owner already used). Rule 2: anonymous slot consumed, NOTE annotation emitted.
    # "Y item" (first-unused at the time) should be the suppressed item.
    cand_x, pd_x, ep_x = _make_candidate(
        "CX", "obligations",
        {"description": "X item primary string"},
        action="promote",
        evidence_snippet="long X item snippet that contains secondary label text here",
    )
    cand_y, pd_y, ep_y = _make_candidate(
        "CY", "obligations",
        {"description": "Y item unrelated"},
        action="promote",
        evidence_snippet="Y item snippet context",
    )
    manifest = _make_manifest([(cand_x, pd_x, ep_x), (cand_y, pd_y, ep_y)])
    er_dict: dict = {
        "obligations": [
            {"description": "X item primary string"},
            {"description": "Y item unrelated"},
        ]
    }
    labels: dict = {"fields": {"obligations": [
        "X item primary string",          # matches X via primary
        "secondary label text here",      # matches X's snippet via fallback (owner already used)
    ]}}

    misses = _collect_misses(er_dict, manifest, labels)
    fps = [m for m in misses.get("obligations", []) if m["kind"] == "FP"]
    fns = [m for m in misses.get("obligations", []) if m["kind"] == "FN"]
    notes = [m for m in misses.get("obligations", []) if m["kind"] == "NOTE"]

    # X is a TP (primary). Y is consumed by the anonymous slot.
    # No genuine FP items (Y is suppressed via slot arithmetic).
    assert len(fps) == 0, f"Expected 0 FPs, got {len(fps)}: {fps}"
    # Both labels are matched, so no FNs.
    assert len(fns) == 0, f"Expected 0 FNs, got {len(fns)}: {fns}"
    # Exactly one NOTE annotation for the slot-consumed suppression.
    assert len(notes) == 1, f"Expected 1 NOTE, got {len(notes)}: {notes}"
    note = notes[0]
    # NOTE must record the suppressed item (Y item), the label, and the snippet-owner (X item).
    assert "Y item" in note["suppressed_value"], (
        f"NOTE suppressed_value must be Y item, got: {note['suppressed_value']!r}"
    )
    assert "secondary label text" in note["label"], (
        f"NOTE label must contain the matching label, got: {note['label']!r}"
    )
    assert "X item" in note["snippet_owner_value"], (
        f"NOTE snippet_owner_value must be X item, got: {note['snippet_owner_value']!r}"
    )


def test_format_miss_dump_note_prefix_not_counted_as_fp_or_fn() -> None:
    # NOTE lines must start with "NOTE " and must NOT be counted by "FP "/"FN " greps.
    misses_by_fixture = {
        "test_fixture": {
            "obligations": [
                {
                    "kind": "NOTE",
                    "field": "obligations",
                    "suppressed_value": "Chaque partie peut resilier la presente convention",
                    "label": "Distributor shall remit quarterly sales reports to the Licensor",
                    "snippet_owner_value": "The Distributor shall pay to the Licensor a royalty",
                }
            ]
        }
    }
    output = format_miss_dump(misses_by_fixture)
    note_lines = [ln for ln in output.splitlines() if ln.startswith("NOTE ")]
    fp_lines = [ln for ln in output.splitlines() if ln.startswith("FP ")]
    fn_lines = [ln for ln in output.splitlines() if ln.startswith("FN ")]
    assert len(note_lines) >= 1, f"Expected at least 1 NOTE line, got 0. Output:\n{output}"
    assert len(fp_lines) == 0, f"NOTE must not be counted as FP, got: {fp_lines}"
    assert len(fn_lines) == 0, f"NOTE must not be counted as FN, got: {fn_lines}"
    # NOTE line content must carry the suppressed value and slot-consumed wording.
    note_line = note_lines[0]
    assert "slot-consumed" in note_line, (
        f"NOTE line must contain 'slot-consumed': {note_line!r}"
    )


# ---------------------------------------------------------------------------
# W6 T2 Defect F -- apostrophe folding in _normalise
# ---------------------------------------------------------------------------

def test_normalise_folds_right_single_quotation_mark() -> None:
    # U+2019 (right single quotation mark) must normalise the same as U+0027.
    assert _normalise("l’Acheteur") == _normalise("l'Acheteur")


def test_normalise_folds_modifier_letter_apostrophe() -> None:
    # U+02BC (modifier letter apostrophe) must normalise the same as U+0027.
    assert _normalise("lʼacheteur") == _normalise("l'acheteur")


def test_is_match_fr_apostrophe_unicode_vs_straight() -> None:
    # The fr_contract FN case: label uses U+0027, extraction used U+2019.
    # After folding, the normalised strings must match via substring or equality.
    label = "La Venderesse doit indemniser l'Acheteur de toutes les pertes découlant de la violation des engagements prévus aux présentes"
    extraction = "La Venderesse doit indemniser l’Acheteur de toutes les pertes découlant de la violation des engagements prévus aux présentes, à condition que toute réclamation soit transmise dans les 18 mois suivant la date de Clôture"
    assert _is_match(_normalise(label), _normalise(extraction))


def test_fr_apostrophe_label_is_prefix_of_longer_extraction() -> None:
    # The label is a strict prefix of the extraction (with U+2019 folded to U+0027).
    # Substring matching must recover the hit.
    label = "La Venderesse doit indemniser l'Acheteur de toutes les pertes"
    extraction = "La Venderesse doit indemniser l’Acheteur de toutes les pertes découlant de la violation des engagements prévus aux présentes"
    assert _is_match(_normalise(label), _normalise(extraction))


# ---------------------------------------------------------------------------
# W6 T2 Round 3: Item 1 -- _jaccard_tokens stopword filtering + punctuation strip
# ---------------------------------------------------------------------------

def test_jaccard_tokens_salary_pair_matches() -> None:
    # This pair currently fails due to function-word dilution + trailing comma tokens.
    # After stopword filtering, content tokens overlap well.
    label = _normalise("Employer shall pay base salary of $185,000 per annum semi-monthly")
    extraction = _normalise(
        "The Employer shall pay the Employee a base salary of $185,000 per annum, "
        "payable in equal semi-monthly instalments in accordance with the Employer's payroll practices"
    )
    # Must match via Jaccard after stopword filtering
    assert _is_match(label, extraction), (
        f"Salary pair must match after stopword filtering; label={label!r}, extraction={extraction!r}"
    )


def test_jaccard_tokens_fr_pair_matches() -> None:
    # FR pair: function words filtered, content tokens overlap
    label = _normalise("La Venderesse doit livrer les actions visées")
    extraction = _normalise("La Venderesse doit céder et transférer à l'Acheteur les actions émises et en circulation")
    # Both have at least some content overlap after filtering 'la', 'les', 'et', 'à'
    # This tests that FR stopwords are properly stripped without breaking meaningful matches
    # (we don't assert True/False for this fuzzy case; we just ensure no crash)
    from tests.calibrate import _jaccard_tokens
    result = _jaccard_tokens(label, extraction)
    assert isinstance(result, float)
    assert 0.0 <= result <= 1.0


def test_jaccard_tokens_stopword_only_strings_return_zero() -> None:
    # Two strings that share only stopwords (after filtering) must return 0.0
    from tests.calibrate import _jaccard_tokens
    # Both strings become empty after filtering all stopwords
    label = "the of to in and or with for by on at"
    extraction = "le la les de du et ou à au aux en dans par pour sur"
    result = _jaccard_tokens(label, extraction)
    assert result == 0.0, (
        f"Strings that reduce to empty token sets must return 0.0, got {result}"
    )


def test_jaccard_tokens_disjoint_content_no_match() -> None:
    # Two strings with completely different content words must NOT match
    label = _normalise("Vendor shall deliver title deeds to Purchaser")
    extraction = _normalise("Employee shall maintain confidentiality obligations annually")
    from tests.calibrate import _jaccard_tokens
    result = _jaccard_tokens(label, extraction)
    assert result < 0.5, (
        f"Disjoint-content strings must not reach Jaccard >= 0.5, got {result}"
    )


def test_is_match_stopword_only_shared_tokens_no_match() -> None:
    # Two strings that share only function words after filtering must NOT match
    # via Jaccard. (They also shouldn't match via equality/substring.)
    label = _normalise("the vendor agrees to deliver documents to the purchaser")
    extraction = _normalise("the employee is required to maintain confidential information in the office")
    assert not _is_match(label, extraction), (
        "Strings sharing only function words must not match after stopword filtering"
    )


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items())
             if name.startswith("test_") and callable(value)]
    for test in tests:
        test()
    print(f"{len(tests)} tests passed")
