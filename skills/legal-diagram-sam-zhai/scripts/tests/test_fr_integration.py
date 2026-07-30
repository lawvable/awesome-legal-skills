"""W3.6 integration tests: FR/bilingual fixtures end-to-end through the CLI.

Standalone-runnable: python scripts/tests/test_fr_integration.py
Also discoverable by pytest. No pytest fixtures; no parametrize (plain loops
keep the bare __main__ runner working, W0 item 1 convention).

Assertions stay on the promoted tier (extraction_result) plus the manifest
language_profile, mirroring the promoted-tier assertions in test_extraction.py,
so they are robust to candidate-tier noise.  Expected values are derived from
the three W3.6 fixtures under scripts/tests/fixtures/.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

EXTRACT = ROOT / "extract_entities.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

# Per-fixture matter_type, mirroring FIXTURE_MATTER_TYPE in run_golden.py so
# the integration runs exercise the same CLI invocation as the goldens.
_MATTER_TYPES = {
    "fr_contract.md": "deal",
    "fr_judgment.md": "litigation",
    "bilingual_contract.md": "deal",
}

# One extraction run per (fixture, extra-args) combination; the manifest is
# deterministic for a fixed fixture so tests share the parsed result.
_CACHE: dict[tuple[str, tuple[str, ...]], dict] = {}


def _run_extract_fixture(name: str, extra_args: list[str] | None = None) -> dict:
    key = (name, tuple(extra_args or []))
    if key in _CACHE:
        return _CACHE[key]
    args = list(extra_args or [])
    matter_type = _MATTER_TYPES.get(name)
    if matter_type and "--matter_type" not in args:
        args = ["--matter_type", matter_type, *args]
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(EXTRACT), "--input", str(FIXTURES / name), *args],
        text=True,
        capture_output=True,
        env=env,
        timeout=60,
    )
    assert proc.returncode == 0, proc.stderr
    data = json.loads(proc.stdout)
    _CACHE[key] = data
    return data


def _party_names(data: dict) -> list[str]:
    return [p["name"] for p in data["extraction_result"]["parties"]]


# ---------------------------------------------------------------------------
# fr_contract.md
# ---------------------------------------------------------------------------

def test_fr_contract_promotes_canonical_parties() -> None:
    data = _run_extract_fixture("fr_contract.md")
    names = _party_names(data)
    for expected in ["Placements Beauchemin Ltée", "Groupe Faucher", "Financière Dorval Ltée"]:
        assert expected in names, (expected, names)


def test_fr_contract_obligations_capture_fr_triggers() -> None:
    data = _run_extract_fixture("fr_contract.md")
    descriptions = [o["description"] for o in data["extraction_result"]["obligations"]]
    assert descriptions, "expected promoted obligations from the FR contract"
    # Positive and negative FR obligation triggers must both survive promotion,
    # with accents intact in the evidence text (never transliterated).
    for trigger in ["doit", "ne doit pas", "s’engage à", "devra"]:
        assert any(trigger in d for d in descriptions), (trigger, descriptions)
    deadline_descriptions = [d["description"] for d in data["extraction_result"]["deadlines"]]
    termination_texts = descriptions + deadline_descriptions
    assert any("résilier" in t or "préavis" in t for t in termination_texts), termination_texts


def test_fr_contract_deadlines_iso_normalised() -> None:
    data = _run_extract_fixture("fr_contract.md")
    deadlines = data["extraction_result"]["deadlines"]
    assert deadlines, "expected promoted deadlines from the FR contract"
    dates = [d["date"] for d in deadlines]
    # Long-form FR dates normalise to ISO 8601 per fr.py normalize_date.
    assert "2026-06-01" in dates, dates   # "au plus tard le 1er juin 2026"
    assert "2026-06-20" in dates, dates   # "au plus tard le 20 juin 2026"
    descriptions = [d["description"] for d in deadlines]
    assert any("préavis écrit de 60 jours" in d for d in descriptions), descriptions
    assert any("dans les" in d and "jours" in d for d in descriptions), descriptions


def test_fr_contract_payments_parse_fr_money() -> None:
    data = _run_extract_fixture("fr_contract.md")
    transfers = data["extraction_result"]["transfers"]
    assert transfers, "expected promoted transfers from the FR contract"
    amounts = [t["amount"] for t in transfers]
    # Space-thousands + comma-decimal amounts parse at harvest time (W3.3).
    assert 1234567.89 in amounts, amounts
    assert 11111111.01 in amounts, amounts
    # W6 T4: the conditional indemnity clause ('Advenant un manquement..., jusqu'à
    # concurrence de 1,5 M$') is demoted to hint tier because it is a conditional
    # cap, not a direct payment obligation.  The 1,5 M$ shorthand parse capability
    # (W3.3 millions shorthand) is preserved at the unit level.
    #
    # (a) Unit assertion: FR money parser must convert '1,5 M$' -> 1 500 000.0.
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from extraction.lexicon import get_bundle as _get_bundle
    _parse_amount_fr = _get_bundle("fr").parse_amount
    assert _parse_amount_fr("1,5 M$") == 1500000.0, (
        "FR money parser must convert '1,5 M$' to 1 500 000.0"
    )
    # (b) Hint-tier assertion: the demoted transfer candidate still carries the
    # parsed 1 500 000.0 amount in an extraction_hints entry whose suggested
    # field is 'transfers'.
    hints = data.get("extraction_hints", [])
    transfer_hints = [h for h in hints if h.get("suggested_field") == "transfers"]
    hint_amounts = [
        _parse_amount_fr(h.get("snippet", ""))
        for h in transfer_hints
    ]
    assert 1500000.0 in hint_amounts, (
        "demoted conditional-indemnity candidate (1,5 M$) must survive "
        "as a hint-tier transfer entry; hint amounts: " + repr(hint_amounts)
    )


def test_fr_contract_conditions_and_consent() -> None:
    data = _run_extract_fixture("fr_contract.md")
    conditions = [c["description"] for c in data["extraction_result"]["conditions"]]
    assert any("sous réserve de la satisfaction" in c for c in conditions), conditions
    assert any("à condition que" in c for c in conditions), conditions
    decision_points = [d["question"] for d in data["extraction_result"]["decision_points"]]
    assert any("consentement préalable écrit" in q for q in decision_points), decision_points


def test_fr_contract_language_profile_dominant_fr() -> None:
    data = _run_extract_fixture("fr_contract.md")
    profile = data["language_profile"]
    assert profile["dominant"] == "fr"
    assert profile["override"] is None
    assert profile["blocks"]["fr"] > 0
    assert profile["char_share"]["fr"] > 0.9


# ---------------------------------------------------------------------------
# fr_judgment.md
# ---------------------------------------------------------------------------

def test_fr_judgment_promotes_canonical_parties() -> None:
    data = _run_extract_fixture("fr_judgment.md")
    names = _party_names(data)
    for expected in ["Marc Tremblay", "Gagnon Transport Ltée"]:
        assert expected in names, (expected, names)


def test_fr_judgment_events_from_occurrence_verbs() -> None:
    data = _run_extract_fixture("fr_judgment.md")
    events = data["extraction_result"]["events"]
    # The fixture carries at least four dated occurrence-verb sentences
    # (a conclu, a signifié, a déposé, a rendu, prononcée).
    assert len(events) >= 4, events
    dates = {e["date"] for e in events}
    for expected in ["2023-02-01", "2024-03-05", "2024-06-12", "2026-01-10"]:
        assert expected in dates, (expected, dates)
    descriptions = [e["description"] for e in events]
    assert any("a rendu" in d for d in descriptions), descriptions


def test_fr_judgment_citations_captured() -> None:
    data = _run_extract_fixture("fr_judgment.md")
    citations = [a["citation"] for a in data["extraction_result"]["legal_authorities"]]
    assert citations, "expected promoted legal authorities from the FR judgment"
    # C.c.Q. article citations must be present with article number and code name.
    assert any("1457" in c and "C.c.Q" in c for c in citations), citations
    assert any("1458" in c and "C.c.Q" in c for c in citations), citations
    # W6 T4: case authorities must be promoted using the composed case-name +
    # neutral-citation form that appears in the relied-upon authority sentences,
    # not as bare citation fragments.
    assert "Lavergne c. Transport Boisclair Ltée, [1994] 2 RCS 415" in citations, citations
    assert "Morin c. Entreprises Casgrain, 2026 QCCA 217" in citations, citations
    # W6 T4 own-citation demotion regression guard: the judgment's own reference
    # line ('Référence : Tremblay c. Gagnon Transport Ltée, 2026 QCCS 1234') is
    # not a relied-upon authority and must NOT appear in promoted citations.
    assert "2026 QCCS 1234" not in citations, (
        "own-citation '2026 QCCS 1234' must be demoted (W6 T4); found in: "
        + repr(citations)
    )


def test_fr_judgment_obligations_and_remedies_present() -> None:
    data = _run_extract_fixture("fr_judgment.md")
    obligations = [o["description"] for o in data["extraction_result"]["obligations"]]
    assert any("doit verser" in o for o in obligations), obligations
    transfers = data["extraction_result"]["transfers"]
    amounts = [t["amount"] for t in transfers]
    assert 180000.0 in amounts, amounts


def test_fr_judgment_language_profile_dominant_fr() -> None:
    data = _run_extract_fixture("fr_judgment.md")
    profile = data["language_profile"]
    assert profile["dominant"] == "fr"
    assert profile["override"] is None
    assert profile["blocks"]["fr"] > 0
    assert profile["char_share"]["fr"] > 0.9


# ---------------------------------------------------------------------------
# bilingual_contract.md
# ---------------------------------------------------------------------------

def test_bilingual_party_dedup_across_languages() -> None:
    data = _run_extract_fixture("bilingual_contract.md")
    names = _party_names(data)
    # The same canonical parties are introduced in the EN clause and its FR
    # twin; the resolver dedups them into a single promoted entry each, with
    # no duplicates differing only by language artifacts.
    for expected in ["Aurora Software Inc", "Boreal Distribution Ltd"]:
        assert names.count(expected) == 1, (expected, names)


def test_bilingual_obligations_from_both_languages() -> None:
    data = _run_extract_fixture("bilingual_contract.md")
    descriptions = [o["description"] for o in data["extraction_result"]["obligations"]]
    assert any("shall" in d for d in descriptions), descriptions
    assert any("doit" in d for d in descriptions), descriptions
    assert any("ne doit pas céder" in d for d in descriptions), descriptions
    assert any("shall not assign" in d for d in descriptions), descriptions


def test_bilingual_deadlines_keep_language_conventions() -> None:
    data = _run_extract_fixture("bilingual_contract.md")
    dates = [d["date"] for d in data["extraction_result"]["deadlines"]]
    # FR blocks normalise to ISO; EN blocks keep the as-written date.
    assert "2026-06-30" in dates, dates
    assert "June 30, 2026" in dates, dates


def test_bilingual_transfers_match_across_languages() -> None:
    data = _run_extract_fixture("bilingual_contract.md")
    amounts = [t["amount"] for t in data["extraction_result"]["transfers"]]
    # The royalty appears once per language with the same parsed value.
    assert amounts.count(250000.0) >= 2, amounts


def test_bilingual_language_profile_counts_both() -> None:
    data = _run_extract_fixture("bilingual_contract.md")
    profile = data["language_profile"]
    assert profile["override"] is None
    assert profile["blocks"]["en"] > 0, profile
    assert profile["blocks"]["fr"] > 0, profile
    assert profile["char_share"]["en"] > 0.2, profile
    assert profile["char_share"]["fr"] > 0.2, profile


# ---------------------------------------------------------------------------
# EN regression guard: forced --lang fr on an EN fixture stays graceful
# ---------------------------------------------------------------------------

def test_en_fixture_forced_fr_is_graceful() -> None:
    # Graceful low-yield is acceptable; the CLI must exit 0 (asserted inside
    # the helper) with a valid manifest that records the forced override.
    data = _run_extract_fixture("en_spa_contract.md", ["--matter_type", "deal", "--lang", "fr"])
    assert data["language_profile"]["override"] == "fr"
    assert data["language_profile"]["dominant"] == "en"
    assert "extraction_result" in data


# ---------------------------------------------------------------------------
# W4.0c regression: calibrate in-process path must annotate blocks before
# extraction so FR fixtures yield correct promoted counts.
# Without the fix, annotate_blocks is never called and every FR block carries
# the default lang, causing the FR harvesters to find nothing.
# ---------------------------------------------------------------------------

def _calibrate_fr_contract_promoted() -> dict[str, int]:
    """Run calibrate's in-process extraction path on fr_contract and return promoted counts.

    Runs the full calibration (all nine fixtures) deliberately: the point of the
    regression test is exercising the real _run_calibration path, so the cost is
    intentional; do not swap in a cheaper single-fixture seam.
    """
    # Import path mirrors calibrate.py's own sys.path setup so the internal
    # _run_calibration function can import its deps without duplication.
    _SKILL_ROOT = Path(__file__).resolve().parents[2]
    if str(_SKILL_ROOT / "scripts") not in sys.path:
        sys.path.insert(0, str(_SKILL_ROOT / "scripts"))
    from tests.calibrate import _run_calibration, _import_stack
    normalize_fn, extract_fn, recommend_fn = _import_stack()[:3]
    report = _run_calibration(normalize_fn, extract_fn, recommend_fn)
    fc_extraction = report["per_fixture"]["fr_contract"]["extraction"]
    return {field: stats["n_promoted"] for field, stats in fc_extraction.items()}


def test_fr_contract_calibrate_path_annotates_blocks() -> None:
    # Regression for W4.0c: calibrate must call annotate_blocks on doc.blocks
    # before extract_fn so FR language harvesters activate on FR fixtures.
    # Before the fix: parties=0, obligations=0 (EN bundle harvests nothing).
    # After the fix: parties>=3, obligations>=11 (matches golden manifest).
    promoted = _calibrate_fr_contract_promoted()
    assert promoted.get("parties", 0) >= 3, (
        f"calibrate fr_contract: expected parties>=3, got {promoted.get('parties', 0)}; "
        "annotate_blocks likely not called before extraction"
    )
    assert promoted.get("obligations", 0) >= 11, (
        f"calibrate fr_contract: expected obligations>=11, got {promoted.get('obligations', 0)}; "
        "annotate_blocks likely not called before extraction"
    )


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_") and callable(value)]
    for test in tests:
        test()
    print(f"{len(tests)} tests passed")
