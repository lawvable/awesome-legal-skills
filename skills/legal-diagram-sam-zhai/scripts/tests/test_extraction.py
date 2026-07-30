from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

EXTRACT = ROOT / "extract_entities.py"
SELECTOR = ROOT / "diagram_selector.py"


def _run_extract(text: str) -> dict:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(EXTRACT), "--stdin"],
        input=text,
        text=True,
        capture_output=True,
        env=env,
        timeout=30,
    )
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


def _run_extract_file(path: Path, extra_args: list[str] | None = None) -> dict:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(EXTRACT), "--input", str(path), *(extra_args or [])],
        text=True,
        capture_output=True,
        env=env,
        timeout=30,
    )
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


def _decisions(sidecar: dict) -> dict[str, str]:
    return {d["candidate_id"]: d["action"] for d in sidecar.get("promotion_decisions", [])}


def _candidates(sidecar: dict, field: str | None = None, frame: str | None = None) -> list[dict]:
    rows = sidecar.get("candidates", [])
    if field is not None:
        rows = [c for c in rows if c.get("target_field") == field]
    if frame is not None:
        rows = [c for c in rows if c.get("frame_type") == frame]
    return rows


def _promoted(sidecar: dict, field: str, frame: str) -> list[dict]:
    decisions = _decisions(sidecar)
    return [c for c in _candidates(sidecar, field, frame) if decisions.get(c["id"]) == "promote"]


def test_extractor_is_canonical_and_keeps_manifest_shape() -> None:
    data = _run_extract(
        '''# Closing Deliveries

Parties: Acme Holdings Inc. ("Buyer"), Beta LLC ("Seller")

Seller shall cause its Affiliates to deliver the officer's certificate no later than June 1, 2026.
Buyer may not assign this Agreement without the prior written consent of Seller.
If Seller fails to cure within 10 business days after written notice, Buyer may terminate.
Buyer shall pay $500,000 to Seller at Closing.
Seller represents and warrants that the statements are true and correct as of Closing.
'''
    )
    for key in ["extraction_result", "extraction_hints", "coverage", "matter_type_evidence", "candidate_manifest", "llm_enrichment"]:
        assert key in data
    sidecar = data["candidate_manifest"]
    extraction = data["extraction_result"]
    assert sidecar["schema_version"] == "legal-diagram-candidates"
    assert _promoted(sidecar, "obligations", "procurement_duty")
    assert _promoted(sidecar, "relationships", "procurement_edge")
    assert _promoted(sidecar, "transfers", "payment_flow")
    assert _promoted(sidecar, "deadlines", "hard_deadline")
    assert extraction["obligations"]
    assert extraction["relationships"]
    assert extraction["transfers"]
    assert extraction["deadlines"]
    assert extraction["concepts"]
    assert not _promoted(sidecar, "communications", "notice_communication")
    assert all("represents and warrants" not in item["description"].lower() for item in extraction["obligations"])


def test_table_row_binding_promotes_canonical_row_entities() -> None:
    data = _run_extract(
        '''# Compliance Matrix

| Responsible Party | Obligation | Due Date | Control | Document |
| --- | --- | --- | --- | --- |
| Seller | Deliver certificate | June 1, 2026 | Legal review | Officer certificate |
'''
    )
    sidecar = data["candidate_manifest"]
    extraction = data["extraction_result"]
    assert sidecar["structure_metrics"]["tables"] == 1
    assert sidecar["structure_metrics"]["table_rows"] == 1
    for field, frame in [
        ("parties", "table_party"),
        ("obligations", "table_obligation"),
        ("deadlines", "table_deadline"),
        ("controls", "table_control"),
        ("documents", "table_document"),
    ]:
        rows = _promoted(sidecar, field, frame)
        assert rows, (field, frame)
        assert "table_row_binding" in rows[0]["signals"]
        assert extraction[field], field


def test_old_runtime_directory_is_removed() -> None:
    assert not (ROOT / "det" "ectors").exists()


def test_noisy_standalone_phrases_do_not_promote() -> None:
    data = _run_extract("This section may include affiliates. Subject to the foregoing. Promptly comply.")
    sidecar = data["candidate_manifest"]
    decisions = _decisions(sidecar)
    assert all(decisions.get(c["id"]) != "promote" for c in sidecar.get("candidates", []))
    assert not any(data["extraction_result"][field] for field in ["conditions", "obligations", "relationships"])


def test_one_span_can_produce_condition_and_control_without_false_deadline() -> None:
    data = _run_extract(
        "If Seller fails to deliver documents, remediation is verified by an audit report and evidenced by a board certificate."
    )
    sidecar = data["candidate_manifest"]
    assert _candidates(sidecar, "conditions", "trigger_condition")
    assert _candidates(sidecar, "controls", "evidence_control")
    assert not _candidates(sidecar, "deadlines", "hard_deadline")


def test_materialization_downgrades_missing_required_fields() -> None:
    from extraction.materialize import materialize_result
    from extraction.schema import Candidate, EvidencePacket, PromotionDecision, SourceRef

    ref = SourceRef(block_id="1", anchor="a1")
    cand = Candidate(id="C0", target_field="relationships", frame_type="bad_relationship", normalized_value={"from_entity": "A"}, confidence=0.99, evidence_ids=["E0"], source_ref=ref)
    evidence = EvidencePacket(id="E0", snippet="A controls.", source_ref=ref, confidence=0.99)
    decision = PromotionDecision("C0", "promote", "test")
    result, decisions = materialize_result([cand], [decision], [evidence])
    assert not result.relationships
    assert result.extraction_hints
    assert decisions[0].action == "hint"
    assert "missing_required_fields" in decisions[0].reason


def test_generated_ids_are_stable() -> None:
    data1 = _run_extract("Seller shall deliver the officer's certificate no later than June 1, 2026.")
    data2 = _run_extract("Seller shall deliver the officer's certificate no later than June 1, 2026.")
    assert data1["extraction_result"]["obligations"][0]["id"] == data2["extraction_result"]["obligations"][0]["id"] == "OBL-0001"


def test_semantic_dedupe_merges_evidence_and_keeps_highest_confidence() -> None:
    from extraction.resolver import dedupe_candidates
    from extraction.schema import Candidate

    a = Candidate(id="C1", target_field="documents", frame_type="deliverable_document", normalized_value={"name": "Certificate"}, confidence=0.5, evidence_ids=["E1"], signals=["a"])
    b = Candidate(id="C2", target_field="documents", frame_type="deliverable_document", normalized_value={"name": "Certificate"}, confidence=0.9, evidence_ids=["E2"], signals=["b"])
    out = dedupe_candidates([a, b])
    assert len(out) == 1
    assert out[0].confidence == 0.9
    assert out[0].evidence_ids == ["E1", "E2"]
    assert out[0].signals == ["a", "b"]


def test_selector_accepts_extraction_result_payload() -> None:
    payload = json.dumps({"extraction_result": {"events": [{"date": "2026-06-01", "description": "closing"}]}})
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(SELECTOR), "--extraction-json", payload],
        text=True,
        capture_output=True,
        env=env,
        timeout=30,
    )
    assert proc.returncode == 0, proc.stderr
    result = json.loads(proc.stdout)
    assert result["recommended_type"] == "timeline"


def test_html_renderer_mermaid_version_in_cdn_url(monkeypatch, tmp_path) -> None:
    """CDN URL must reference the pinned MERMAID_VERSION constant, not a hardcoded string."""
    import render_html
    # Stub vendor path to a guaranteed-nonexistent file so loader yields cdn (not vendored),
    # regardless of whether assets/vendor/mermaid.min.js exists in the real tree.
    monkeypatch.setattr(render_html, "_vendored_mermaid_path", lambda: tmp_path / "no-vendor.js")

    from render_html import render, MERMAID_VERSION

    cdn_out = tmp_path / "version-check.html"
    render("flowchart TD\nA-->B", {"title": "VersionCheck"}, str(cdn_out), allow_cdn=True)
    cdn_html = cdn_out.read_text(encoding="utf-8")
    assert f"mermaid@{MERMAID_VERSION}" in cdn_html, (
        f"CDN URL must contain mermaid@{MERMAID_VERSION}; got:\n{cdn_html[:500]}"
    )


def test_html_renderer_escapes_untrusted_fields_and_requires_explicit_cdn(monkeypatch, tmp_path) -> None:
    import render_html
    # Stub vendor path to a guaranteed-nonexistent file so loader yields source-only (no flag)
    # or cdn (allow_cdn=True), regardless of whether assets/vendor/mermaid.min.js exists.
    monkeypatch.setattr(render_html, "_vendored_mermaid_path", lambda: tmp_path / "no-vendor.js")

    from render_html import render, MERMAID_VERSION

    desc = {
        "title": 'Matter </title><script>alert(1)</script>',
        "matter_context": '<img src=x onerror=alert(1)>',
        "caption": 'Caption <script>alert(1)</script>',
        "overview": 'Overview <b onclick=alert(1)>unsafe</b>',
        "how_to_read": 'Read </p><script>alert(1)</script>',
        "observations": ['<img src=x onerror=alert(1)>'],
        "caveats": ['</li><script>alert(1)</script>'],
    }
    semantic_map = json.dumps({"nodes": {"A": "sem-party"}, "meta": {"label": "</script><script>alert(1)</script>"}})
    mermaid = 'flowchart TD\nA["</pre><script>alert(1)</script>"]'

    out = tmp_path / "figure.html"
    render(mermaid, desc, str(out), semantic_map=semantic_map)
    html = out.read_text(encoding="utf-8")
    assert "<script>alert(1)</script>" not in html
    assert "</pre><script" not in html
    assert "<img src=x onerror=alert(1)>" not in html
    assert 'id="sourceOnlyPanel"' in html  # source-only fallback panel rendered
    assert "cdn.jsdelivr.net" not in html
    assert "securityLevel: 'strict'" in html

    cdn_out = tmp_path / "figure-cdn.html"
    render("flowchart TD\nA-->B", {"title": "Safe"}, str(cdn_out), allow_cdn=True)
    cdn_html = cdn_out.read_text(encoding="utf-8")
    assert f"https://cdn.jsdelivr.net/npm/mermaid@{MERMAID_VERSION}/dist/mermaid.min.js" in cdn_html


def test_html_renderer_rejects_invalid_semantic_map() -> None:
    from render_html import render

    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "bad.html"
        try:
            render("flowchart TD\nA-->B", {"title": "Bad"}, str(out), semantic_map="[]")
        except ValueError as exc:
            assert "root must be an object" in str(exc)
        else:
            raise AssertionError("expected invalid semantic map to fail")


def test_file_input_uses_basename_unless_full_path_opted_in() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "Client Matter.md"
        path.write_text("Seller shall deliver the officer's certificate no later than June 1, 2026.", encoding="utf-8")

        data = _run_extract_file(path)
        extraction = data["extraction_result"]
        assert extraction["input_source"] == path.name
        assert extraction["matter_name"] == "Client Matter"
        assert str(path) not in json.dumps(data)

        full_path_data = _run_extract_file(path, ["--include-source-path"])
        assert full_path_data["extraction_result"]["input_source"] == str(path)


def test_file_size_limit_blocks_untrusted_oversized_input() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "large.md"
        path.write_text("Seller shall deliver documents.", encoding="utf-8")
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, str(EXTRACT), "--input", str(path), "--max-file-bytes", "1"],
            text=True,
            capture_output=True,
            timeout=30,
        )
        assert proc.returncode != 0
        assert "max_file_bytes" in proc.stderr


def test_specific_limit_warnings_are_included_with_source_truncated() -> None:
    from extraction.handoff import warning_codes
    from normalize import NormalizedDoc, mark_truncated

    doc = NormalizedDoc(source_format="xlsx")
    mark_truncated(doc, "XLSX_ROW_LIMIT_REACHED")
    warnings = warning_codes(doc, [])
    assert "XLSX_ROW_LIMIT_REACHED" in warnings
    assert "SOURCE_TRUNCATED" in warnings


def test_sentence_harvesters_registry_is_iterable() -> None:
    from extraction.harvesters.base import SENTENCE_HARVESTERS

    expected_names = {
        "harvest_party_alias",
        "harvest_privacy_parties",
        "harvest_rep_warranty",
        "harvest_obligation",
        "harvest_conditions",
        "harvest_controls",
        "harvest_deadlines",
        "harvest_consent_discretion",
        "harvest_deliverables",
        "harvest_payments",
        "harvest_default_remedy",
        "harvest_notice",
        "harvest_ownership_control",
        "harvest_entities",
        "harvest_event",
        "harvest_citation",
    }
    assert isinstance(SENTENCE_HARVESTERS, list)
    assert all(callable(fn) for fn in SENTENCE_HARVESTERS)
    actual_names = {fn.__name__ for fn in SENTENCE_HARVESTERS}
    assert expected_names == actual_names


def test_neutral_citation_promotes_authority() -> None:
    data = _run_extract("See Smith v. Jones, 2024 ONSC 1234.")
    assert data["extraction_result"]["legal_authorities"], "expected at least one promoted legal authority"
    assert any(
        "2024 ONSC 1234" in (auth.get("citation") or "")
        for auth in data["extraction_result"]["legal_authorities"]
    ), "expected an authority whose citation contains '2024 ONSC 1234'"


def test_paragraph_reference_is_not_an_authority() -> None:
    data = _run_extract("As noted at para. 42, the limitation test applies.")
    assert not data["extraction_result"]["legal_authorities"], (
        "bare paragraph reference must not produce a legal_authorities entry"
    )


def test_judgment_excerpt_yields_party_authority_event() -> None:
    data = _run_extract(
        "Smith v. Jones, 2024 ONSC 1234. "
        "The motion was heard on March 12, 2024. "
        "The motion is dismissed."
    )
    sidecar = data["candidate_manifest"]
    ext = data["extraction_result"]
    assert _candidates(sidecar, "parties", "litigation_caption"), (
        "expected litigation_caption party candidates"
    )
    assert ext["legal_authorities"], "expected at least one promoted legal authority"
    assert ext["events"], "expected at least one promoted event"


def test_litigation_caption_yields_party_candidates() -> None:
    data = _run_extract("Smith v. Jones is the leading authority.")
    sidecar = data["candidate_manifest"]
    caps = _candidates(sidecar, "parties", "litigation_caption")
    assert len(caps) >= 2
    names = [c["normalized_value"]["name"] for c in caps]
    assert any("Smith" in n for n in names)
    assert any("Jones" in n for n in names)


def test_litigation_role_words_present() -> None:
    from extraction.lexicon import KNOWN_ROLE_WORDS

    required = {"appellant", "respondent", "plaintiff", "defendant"}
    assert required <= KNOWN_ROLE_WORDS


def test_dated_procedural_event_promotes() -> None:
    data = _run_extract("The motion was heard on March 12, 2024.")
    sidecar = data["candidate_manifest"]
    extraction = data["extraction_result"]
    assert _candidates(sidecar, "events"), "expected at least one events candidate"
    assert extraction["events"], "expected at least one promoted event"
    assert any("March 12, 2024" in (evt.get("date") or "") for evt in extraction["events"]), (
        "expected event with date containing 'March 12, 2024'"
    )


def test_bare_date_without_event_verb_does_not_promote() -> None:
    data = _run_extract("The amount is calculated as of June 1, 2026 per the schedule.")
    extraction = data["extraction_result"]
    assert not extraction["events"], "bare date with no occurrence verb must not produce a promoted event"


def test_privacy_profile_emits_directed_inference() -> None:
    data = _run_extract(
        "The vendor collects personal data and transfers it to its processor."
        " The main risk is unauthorized access. Encryption mitigates the risk."
    )
    assert data["profile_signals"]["privacy"] >= 0.34
    fields = {d["field"] for d in data["llm_enrichment"]["directives"] if d["type"] == "directed_inference"}
    assert "data_flows" in fields


def test_governance_profile_emits_directed_inference() -> None:
    data = _run_extract(
        "The board approved the transaction subject to audit committee review."
        " The shareholder resolution passed by quorum."
    )
    assert data["profile_signals"]["governance"] >= 0.34
    fields = {d["field"] for d in data["llm_enrichment"]["directives"] if d["type"] == "directed_inference"}
    assert fields & {"process_steps", "decision_points"}


def test_plain_clause_emits_no_directed_inference() -> None:
    data = _run_extract(
        "Seller shall deliver the officer's certificate no later than June 1, 2026."
    )
    assert not any(d["type"] == "directed_inference" for d in data["llm_enrichment"]["directives"])


def test_caption_simple_still_works() -> None:
    """Simple unpunctuated caption must still produce both sides."""
    data = _run_extract("Smith v. Jones is the leading authority.")
    names = [c["normalized_value"].get("name", "") for c in _candidates(data["candidate_manifest"], "parties", "litigation_caption")]
    assert any(n == "Smith" for n in names), f"expected 'Smith' in {names}"
    assert any(n == "Jones" for n in names), f"expected 'Jones' in {names}"


def test_caption_corporate_suffix() -> None:
    """Corporate-suffix parties (Ltd./Corp.) before a comma must match, and the
    leading stop word 'In' must not appear in any extracted party name."""
    data = _run_extract("In Acme Corp. v. Beta Ltd., 2023 FCA 45 governed the appeal.")
    names = [c["normalized_value"].get("name", "") for c in _candidates(data["candidate_manifest"], "parties", "litigation_caption")]
    assert any("Acme" in n and "Corp" in n for n in names), f"expected a name containing 'Acme' and 'Corp' in {names}"
    assert any("Beta" in n and "Ltd" in n for n in names), f"expected a name containing 'Beta' and 'Ltd' in {names}"
    assert all(not n.startswith("In ") for n in names), f"a name starts with 'In ': {names}"


def test_caption_with_neutral_citation_comma() -> None:
    """Caption followed by neutral citation (comma then year) must still extract both sides."""
    data = _run_extract("Smith v. Jones, 2024 ONSC 1234.")
    names = [c["normalized_value"].get("name", "") for c in _candidates(data["candidate_manifest"], "parties", "litigation_caption")]
    assert any("Smith" in n for n in names), f"expected 'Smith' in {names}"
    assert any("Jones" in n for n in names), f"expected 'Jones' in {names}"


# ---------------------------------------------------------------------------
# Fix A -- statutory subsections captured in citation text
# ---------------------------------------------------------------------------

def test_statutory_reference_captures_subsection() -> None:
    """_STATUTORY_REF must include subsection text such as (1)(a) in the citation."""
    data = _run_extract("Pursuant to section 12(1)(a), the rule applies.")
    authorities = data["extraction_result"]["legal_authorities"]
    assert authorities, "expected at least one promoted legal authority"
    assert any(
        "12(1)(a)" in (auth.get("citation") or "")
        for auth in authorities
    ), f"expected an authority whose citation contains '12(1)(a)', got: {[a.get('citation') for a in authorities]}"


# ---------------------------------------------------------------------------
# Fix B -- future/conditional statements do not promote as events
# ---------------------------------------------------------------------------

def test_future_conditional_not_promoted_as_event() -> None:
    """A sentence with 'if' + occurrence verb must not produce a promoted event."""
    data = _run_extract("If the request is approved by March 1, 2024, the funds release.")
    assert not data["extraction_result"]["events"], (
        "future/conditional sentence must not produce a promoted event"
    )


def test_future_shall_not_promoted_as_event() -> None:
    """A sentence with 'shall' + occurrence verb must not produce a promoted event."""
    data = _run_extract("The loan shall be approved no later than 31 December 2024.")
    assert not data["extraction_result"]["events"], (
        "future 'shall' sentence must not produce a promoted event"
    )


# ---------------------------------------------------------------------------
# Fix C -- case_citation requires a year to follow the case name
# ---------------------------------------------------------------------------

def test_case_citation_requires_year_context() -> None:
    """'Option A v Option B' with no following year must not produce a legal_authorities entry."""
    data = _run_extract("We compared Option A v Option B today.")
    assert not data["extraction_result"]["legal_authorities"], (
        "prose 'v' without a following year must not produce a legal_authorities entry"
    )


# ---------------------------------------------------------------------------
# Fix D -- profile keyword matching respects word boundaries
# ---------------------------------------------------------------------------

def test_profile_keywords_respect_word_boundaries() -> None:
    """Substring-only matches (brisket=risk, berating=rating, asterisk=risk) must not activate risk_assessment.

    Under the old substring matching this scored {risk, rating} = 0.67 and falsely
    activated the profile; with word boundaries it scores 0.0.
    """
    data = _run_extract("The brisket was tasty and the berating frisky cat slept near the asterisk.")
    assert data["profile_signals"]["risk_assessment"] < 0.34, (
        f"risk_assessment must not be active from substrings alone, got {data['profile_signals']['risk_assessment']}"
    )


# === TESTS: Task 1 (domain relocation) ===
def test_t1_domain_importable_from_extraction_package():
    from extraction.domain import ExtractionResult, ENTITY_FIELDS
    assert ExtractionResult is not None
    assert isinstance(ENTITY_FIELDS, dict)

def test_t1_materialize_no_extraction_schema_import():
    import inspect
    import extraction.materialize as m
    src = inspect.getsource(m)
    assert "from extraction_schema" not in src
    assert 'import extraction_schema' not in src
    assert '__import__("extraction_schema")' not in src  # audit-ok: dangerous-python: assertion guards against dynamic import, string literal only

def test_t1_diagram_selector_no_extraction_schema_import():
    import inspect, sys
    scripts_dir = str(__import__("pathlib").Path(__file__).parent.parent)  # audit-ok: dangerous-python: fixed stdlib pathlib literal
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import diagram_selector as ds
    src = inspect.getsource(ds)
    assert "from extraction_schema" not in src

def test_t1_manifest_no_extraction_schema_import():
    import inspect
    import extraction.manifest as m
    src = inspect.getsource(m)
    assert "from extraction_schema" not in src


# === TESTS: Task 2 (manifest relocation) ===
def test_t2_manifest_importable_from_extraction_package():
    from extraction.manifest import build_manifest
    assert callable(build_manifest)

def test_t2_extraction_init_exports_build_manifest():
    import extraction
    assert hasattr(extraction, "build_manifest")
    assert callable(extraction.build_manifest)

def test_t2_extract_entities_imports_manifest_from_package():
    import inspect, sys
    scripts_dir = str(__import__("pathlib").Path(__file__).parent.parent)  # audit-ok: dangerous-python: fixed stdlib pathlib literal
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import extract_entities
    src = inspect.getsource(extract_entities)
    assert "from manifest import" not in src
    assert "import manifest\n" not in src

def test_t2_manifest_build_returns_expected_keys():
    from extraction.manifest import build_manifest
    from extraction.domain import ExtractionResult
    result = build_manifest(
        doc=None,
        extraction_result=ExtractionResult(),
        candidates=[],
        decisions=[],
        evidence_packets=[],
    )
    assert isinstance(result, dict)
    assert "extraction_result" in result
    _dropped_key = "enrichment" "_directives"  # audit-ok: split-literal: avoids grep false-positive on retired key name
    assert _dropped_key not in result
    directives = result.get("llm_enrichment", {}).get("directives", None)
    assert isinstance(directives, list)


# === TESTS: Task 3 (consent harvester extraction) ===
def test_t3_consent_harvester_in_own_module():
    from extraction.harvesters.consent import harvest_consent_discretion
    assert callable(harvest_consent_discretion)

def test_t3_consent_not_defined_in_base():
    import inspect
    import extraction.harvesters.base as b
    src = inspect.getsource(b)
    assert "def harvest_consent_discretion" not in src

def test_t3_consent_harvester_reachable_via_base():
    from extraction.harvesters.base import harvest_consent_discretion
    assert callable(harvest_consent_discretion)

def test_t3_consent_harvester_produces_candidate_for_consent_sentence():
    from extraction.harvesters.consent import harvest_consent_discretion
    from extraction.schema import Candidate
    candidates: list[Candidate] = []
    harvest_consent_discretion(
        "Client expressly consents to disclosure of all records.",
        candidates,
        heading_path=[],
    )
    assert len(candidates) >= 1
    assert all(0.0 <= c.confidence <= 1.0 for c in candidates)


# === TESTS: Task 4 (handoff + engine cleanup) ===
def test_t4_structure_metrics_reads_stored_value():
    from extraction.handoff import structure_metrics
    class FakeDoc:
        blocks: list = []
        tables: list = []
        structure_metrics = {"headings": 5, "paragraphs": 10, "lists": 2, "tables": 1, "blocks": 13}
    result = structure_metrics(FakeDoc(), synthetic_table_blocks=3)
    assert result["headings"] == 5
    assert result["paragraphs"] == 10
    assert result["table_rows"] == 3

def test_t4_structure_metrics_fallback_when_not_stored():
    from extraction.handoff import structure_metrics
    class FakeBlock:
        block_type: str
        def __init__(self, t: str):
            self.block_type = t
    class FakeDoc:
        blocks = [FakeBlock("heading"), FakeBlock("paragraph"), FakeBlock("paragraph")]
        tables: list = []
        structure_metrics = None  # type: ignore
    result = structure_metrics(FakeDoc())
    assert result["headings"] == 1
    assert result["paragraphs"] == 2

def test_t4_no_duplicate_source_unparseable_warning():
    from extraction.handoff import warning_codes
    class FakeDoc:
        warning_codes = ["SOURCE_UNPARSEABLE_OR_EMPTY"]
        blocks = None
        tables = None
    result = warning_codes(FakeDoc(), [])
    assert result.count("SOURCE_UNPARSEABLE_OR_EMPTY") == 1

def test_t4_engine_build_candidate_manifest_removed():
    import extraction
    assert not hasattr(extraction, "build_candidate_manifest")


# === TESTS: Task 5 (score_confidence helper) ===
def test_t5_score_confidence_helper_exists():
    from extraction.utils import score_confidence
    assert callable(score_confidence)

def test_t5_score_confidence_matches_formula():
    from extraction.utils import score_confidence, score_boost, anti_penalty
    base = 0.55
    signals = ["obligation_verb", "known_party_subject"]
    anti = ["boilerplate"]
    expected = base + score_boost(signals) - anti_penalty(anti)
    assert score_confidence(base, signals, anti) == expected

def test_t5_obligations_no_inline_formula():
    import inspect
    import extraction.harvesters.obligations as o
    src = inspect.getsource(o)
    assert "score_boost(signals) - anti_penalty" not in src
    assert "score_confidence(" in src


# === TESTS: Task 6-B5 ===
def test_t6_b5_cli_loop_registers_all_default_limits():
    result = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(EXTRACT), "--help"],
        capture_output=True,
        text=True,
    )
    from normalize import DEFAULT_LIMITS
    for key in DEFAULT_LIMITS:
        flag = f"--{key.replace('_', '-')}"
        assert flag in result.stdout, f"Missing flag: {flag}"
    assert 'add_argument("--max-pdf-pages"' not in EXTRACT.read_text()


# === TESTS: Task 6-B6 ===
def test_t6_b6_missing_required_uses_explicit_sentinel():
    import inspect
    import extraction.materialize as m
    src = inspect.getsource(m)
    assert "dataclasses.MISSING" in src or "_MISSING" in src
    assert "field.default is not field.default_factory" not in src


# === TESTS: Task 6-B8 ===
def test_t6_b8_no_count_assertion_in_harvester_test():
    src = Path(__file__).read_text()
    count_assert = "len(SENTENCE_HARVES" "TERS) == 14"
    assert count_assert not in src


# === TESTS: Task 7 ===
def test_t7_docx_adapter_has_heading_stack():
    import inspect
    import normalize.docx_adapter as da
    src = inspect.getsource(da)
    assert "heading_stack" in src
    assert "heading_path" in src


def test_t7_pdf_adapter_has_heading_path():
    import inspect
    import normalize.pdf_adapter as pa
    src = inspect.getsource(pa)
    assert "heading_path" in src


def test_t7_pptx_adapter_has_heading_path():
    import inspect
    import normalize.pptx_adapter as pp
    src = inspect.getsource(pp)
    assert "heading_path" in src


# === TESTS: Task 8 ===
def test_t8_c1_entities_field_drives_erdiagram():
    from diagram_selector import RULES
    field_names = [r[0] for r in RULES]
    assert "entities" in field_names

def test_t8_c1_documents_field_in_rules():
    from diagram_selector import RULES
    field_names = [r[0] for r in RULES]
    assert "documents" in field_names

def test_t8_c2_journey_reachable_from_counseling_intent():
    from diagram_selector import _score
    from extraction.domain import ExtractionResult
    er = ExtractionResult()
    payload = {"extraction_result": er.__dict__, "intent": "client explanation walkthrough"}
    scores = _score(er, payload["intent"])
    assert scores.get("journey", 0) > 0

def test_t8_c3_matter_boosts_five_added():
    from diagram_selector import MATTER_BOOSTS
    for mt in ["privacy", "real_estate", "arbitration", "deal", "tech"]:
        assert mt in MATTER_BOOSTS, f"Missing: {mt}"

def test_t8_c4_compound_intent_matches_multiple_keywords():
    from diagram_selector import _score
    from extraction.domain import Event, ExtractionResult
    er = ExtractionResult()
    er.events = [Event(date="2026-01-01", description="filed") for _ in range(3)]
    payload = {"extraction_result": er.__dict__, "intent": "timeline sequence of events"}
    scores = _score(er, payload["intent"])
    assert scores.get("timeline", 0) > 0
    assert scores.get("sequenceDiagram", 0) > 0

def test_t8_c5_missing_payload_key_exits_nonzero():
    payload = json.dumps({"bad_key": {}, "intent": "general"})
    r = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(SELECTOR), "--extraction-json", payload],
        capture_output=True,
        text=True,
    )
    assert r.returncode != 0
    assert "extraction_result" in r.stderr

def test_t8_c4_no_break_in_intent_loop():
    import inspect
    import diagram_selector as ds
    src = inspect.getsource(ds._score)
    assert "break" not in src


# ---------------------------------------------------------------------------
# TESTS: render_html digest_table + source_path
# ---------------------------------------------------------------------------

def test_render_html_accepts_digest_table():
    import inspect, sys as _sys
    _sys.path.insert(0, str(ROOT))
    import render_html
    sig = inspect.signature(render_html.render)
    assert 'digest_table' in sig.parameters


def test_render_html_accepts_source_path():
    import inspect, sys as _sys
    _sys.path.insert(0, str(ROOT))
    import render_html
    sig = inspect.signature(render_html.render)
    assert 'source_path' in sig.parameters


def test_render_html_digest_table_appears_in_output(tmp_path):
    import sys as _sys
    _sys.path.insert(0, str(ROOT))
    import render_html
    rows = [{'row_num': 1, 'category': 'Obligation', 'finding': 'Seller must deliver docs',
             'party': 'Seller', 'verbatim': 'Seller shall deliver to Buyer, no later than June 30, 2026',
             'anchor': '§1 ¶2', 'page': None, 'slide': None, 'unverified': False}]
    out = tmp_path / 'out.html'
    render_html.render('flowchart TD\n  A-->B', {'title': 'Test'}, str(out), digest_table=rows)
    html = out.read_text()
    assert 'verification-table' in html
    assert 'Seller must deliver docs' in html
    assert 'Seller shall deliver to Buyer' in html


def test_render_html_pdf_source_link_includes_page(tmp_path):
    import sys as _sys
    _sys.path.insert(0, str(ROOT))
    import render_html
    rows = [{'row_num': 1, 'category': 'Deadline', 'finding': 'June 30 deadline',
             'party': 'Seller', 'verbatim': 'no later than June 30, 2026',
             'anchor': '§1 ¶2', 'page': 3, 'slide': None, 'unverified': False}]
    out = tmp_path / 'out.html'
    render_html.render('flowchart TD\n  A-->B', {'title': 'T'}, str(out),
                       digest_table=rows, source_path='/fake/doc.pdf')
    html = out.read_text()
    assert '#page=3' in html


def test_render_html_docx_source_link_no_fragment(tmp_path):
    import sys as _sys
    _sys.path.insert(0, str(ROOT))
    import render_html
    rows = [{'row_num': 1, 'category': 'Obligation', 'finding': 'Deliver docs',
             'party': 'Seller', 'verbatim': 'Seller shall deliver',
             'anchor': '§1', 'page': None, 'slide': None, 'unverified': False}]
    out = tmp_path / 'out.html'
    render_html.render('flowchart TD\n  A-->B', {'title': 'T'}, str(out),
                       digest_table=rows, source_path='/fake/contract.docx')
    html = out.read_text()
    assert 'contract.docx' in html
    assert '#page' not in html


def test_render_html_unverified_row_marked(tmp_path):
    import sys as _sys
    _sys.path.insert(0, str(ROOT))
    import render_html
    rows = [{'row_num': 1, 'category': 'Decision', 'finding': 'Financing satisfactory?',
             'party': 'Purchaser', 'verbatim': 'in its sole discretion',
             'anchor': '§3 ¶1', 'page': None, 'slide': None, 'unverified': True}]
    out = tmp_path / 'out.html'
    render_html.render('flowchart TD\n  A-->B', {'title': 'T'}, str(out), digest_table=rows)
    html = out.read_text()
    assert 'unverified' in html.lower() or '⚠' in html


def test_render_html_no_digest_table_backward_compat(tmp_path):
    import sys as _sys
    _sys.path.insert(0, str(ROOT))
    import render_html
    out = tmp_path / 'out.html'
    render_html.render('flowchart TD\n  A-->B', {'title': 'T'}, str(out))
    html = out.read_text()
    assert 'verification-table' not in html


def test_cli_digest_table_flag(tmp_path):
    import subprocess, sys as _sys, json
    rows = json.dumps([{'row_num': 1, 'category': 'Obligation', 'finding': 'Seller deliver',
                        'party': 'Seller', 'verbatim': 'Seller shall deliver to Buyer',
                        'anchor': '§1', 'page': None, 'slide': None, 'unverified': False}])
    out = tmp_path / 'out.html'
    r = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [_sys.executable, 'render_html.py',
         '--mermaid-block', 'flowchart TD\n  A-->B',
         '--figure-desc', '{"title": "T"}',
         '--output-path', str(out),
         '--digest-table', rows],
        capture_output=True, text=True, cwd=str(ROOT)
    )
    assert r.returncode == 0, r.stderr
    result = json.loads(r.stdout)
    assert result['ok'] is True
    html = out.read_text()
    assert 'Seller deliver' in html


def _run_selector(payload: dict) -> dict:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(SELECTOR), "--extraction-json", json.dumps(payload)],
        text=True, capture_output=True, env=env, timeout=30,
    )
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


def test_selector_flags_grouping_on_dense_timeline() -> None:
    # No timeline-naming intent: the dense-timeline grouping override fires and flips
    # timeline to a grouped flowchart.  (A timeline-naming intent such as "chronology"
    # now exempts timeline from this override; that exemption is covered in test_selector.py.)
    events = [{"date": f"2026-06-{d:02d}", "description": f"event {d}"} for d in range(1, 13)]
    result = _run_selector({"extraction_result": {"events": events, "matter_type": "litigation"},
                            "intent": "general"})
    assert result["recommended_type"] == "flowchart"
    assert result["grouping_suggested"] is True
    assert result["grouping_axis"] == "era"


def test_selector_no_grouping_on_sparse_timeline() -> None:
    events = [{"date": "2026-06-01", "description": "closing"},
              {"date": "2026-06-05", "description": "filing"}]
    result = _run_selector({"extraction_result": {"events": events, "matter_type": "litigation"},
                            "intent": "chronology"})
    assert result["recommended_type"] == "timeline"
    assert result["grouping_suggested"] is False
    assert result["grouping_axis"] is None


def test_selector_grouping_fields_present_on_empty_signals() -> None:
    result = _run_selector({"extraction_result": {}})
    assert result["grouping_suggested"] is False
    assert result["grouping_axis"] is None


def test_extraction_result_hierarchy_field_roundtrips():
    from extraction.domain import ExtractionResult
    r = ExtractionResult()
    assert r.hierarchy == []
    node = {"id": "H-a", "label": "A", "parent": None, "depth": 0, "source": "deterministic"}
    r2 = ExtractionResult.from_dict({"hierarchy": [node]})
    assert r2.hierarchy[0]["id"] == "H-a"
    assert "hierarchy" in r2.to_dict()


def test_materialize_builds_deterministic_hierarchy_from_headings():
    from extraction.schema import Candidate, SourceRef, PromotionDecision
    from extraction.materialize import materialize_result
    cand = Candidate(id="c1", target_field="events", frame_type="event",
                     normalized_value={"date": "2026-01-01", "description": "filed"},
                     source_ref=SourceRef(heading_path=["Background", "Procedural History"]))
    dec = PromotionDecision(candidate_id="c1", action="promote", reason="ok")
    result, _ = materialize_result([cand], [dec], [])
    tops = [n for n in result.hierarchy if n["depth"] == 0]
    kids = [n for n in result.hierarchy if n["depth"] == 1]
    assert tops and tops[0]["label"] == "Background" and tops[0]["parent"] is None
    assert kids and kids[0]["label"] == "Procedural History"
    assert kids[0]["parent"] == tops[0]["id"]


def test_materialize_hierarchy_caps_depth_at_two():
    from extraction.schema import Candidate, SourceRef, PromotionDecision
    from extraction.materialize import materialize_result
    cand = Candidate(id="c1", target_field="events", frame_type="event",
                     normalized_value={"date": "2026-01-01", "description": "x"},
                     source_ref=SourceRef(heading_path=["L0", "L1", "L2", "L3", "L4"]))
    dec = PromotionDecision(candidate_id="c1", action="promote", reason="ok")
    result, _ = materialize_result([cand], [dec], [])
    assert result.hierarchy
    assert max(n["depth"] for n in result.hierarchy) <= 2


# ---------------------------------------------------------------------------
# TESTS: W0.6 -- sentence-split abbreviation guards
# ---------------------------------------------------------------------------

def test_w0_6_abbreviation_guards_exported() -> None:
    """ABBREVIATION_GUARDS_EN must be importable from extraction.utils and be a tuple."""
    from extraction.utils import ABBREVIATION_GUARDS_EN
    assert isinstance(ABBREVIATION_GUARDS_EN, tuple)


def test_w0_6_seeded_abbreviations_exact() -> None:
    """Guard list must be exactly the seven seeded EN abbreviations (no more, no fewer)."""
    from extraction.utils import ABBREVIATION_GUARDS_EN
    required = {"Inc.", "Corp.", "Ltd.", "No.", "U.S.", "e.g.", "i.e."}
    assert required == set(ABBREVIATION_GUARDS_EN), (
        f"Guard set mismatch -- extra: {set(ABBREVIATION_GUARDS_EN) - required}, "
        f"missing: {required - set(ABBREVIATION_GUARDS_EN)}"
    )


def test_w0_6_inc_does_not_split() -> None:
    """'Acme Inc. shall pay the Vendor.' must remain a single sentence."""
    from extraction.utils import sentences_with_offsets
    result = list(sentences_with_offsets("Acme Inc. shall pay the Vendor."))
    assert len(result) == 1, f"expected 1 sentence, got {len(result)}: {[s for s, *_ in result]}"


def test_w0_6_corp_does_not_split() -> None:
    from extraction.utils import sentences_with_offsets
    result = list(sentences_with_offsets("Acme Corp. shall deliver the certificate."))
    assert len(result) == 1, f"expected 1 sentence, got {len(result)}: {[s for s, *_ in result]}"


def test_w0_6_ltd_does_not_split() -> None:
    from extraction.utils import sentences_with_offsets
    result = list(sentences_with_offsets("Beta Ltd. will transfer the funds."))
    assert len(result) == 1, f"expected 1 sentence, got {len(result)}: {[s for s, *_ in result]}"


def test_w0_6_no_does_not_split() -> None:
    """'See Schedule No. 4 before closing.' must stay as one sentence."""
    from extraction.utils import sentences_with_offsets
    result = list(sentences_with_offsets("See Schedule No. 4 before closing."))
    assert len(result) == 1, f"expected 1 sentence, got {len(result)}: {[s for s, *_ in result]}"


def test_w0_6_us_does_not_split() -> None:
    from extraction.utils import sentences_with_offsets
    result = list(sentences_with_offsets("The U.S. regulations apply here."))
    assert len(result) == 1, f"expected 1 sentence, got {len(result)}: {[s for s, *_ in result]}"


def test_w0_6_eg_does_not_split() -> None:
    from extraction.utils import sentences_with_offsets
    result = list(sentences_with_offsets("Permitted uses include e.g. subleasing or assignment."))
    assert len(result) == 1, f"expected 1 sentence, got {len(result)}: {[s for s, *_ in result]}"


def test_w0_6_ie_does_not_split() -> None:
    from extraction.utils import sentences_with_offsets
    result = list(sentences_with_offsets("The closing date i.e. the Transfer Date is June 1."))
    assert len(result) == 1, f"expected 1 sentence, got {len(result)}: {[s for s, *_ in result]}"


def test_w0_6_normal_boundaries_still_split() -> None:
    """Ordinary sentence boundary must still produce two sentences."""
    from extraction.utils import sentences_with_offsets
    result = list(sentences_with_offsets("First sentence. Second sentence."))
    assert len(result) == 2, f"expected 2 sentences, got {len(result)}: {[s for s, *_ in result]}"


def test_w0_6_abbreviation_at_true_sentence_end() -> None:
    """An abbreviation at the true end of a document (terminal period) must produce
    exactly one sentence; the guard must not suppress the terminal boundary.
    Chosen behaviour: single sentence returned, text preserved verbatim (stripped)."""
    from extraction.utils import sentences_with_offsets
    result = list(sentences_with_offsets("Buyer is incorporated in the U.S."))
    assert len(result) == 1, f"expected 1 sentence, got {len(result)}: {[s for s, *_ in result]}"
    assert result[0][0] == "Buyer is incorporated in the U.S."


def test_w0_6_guards_are_case_sensitive() -> None:
    """Guards are literal strings; lowercase 'inc.' must not trigger the guard.
    Lowercase 'inc.' allows a split, so two sentences must be produced."""
    from extraction.utils import sentences_with_offsets
    result = list(sentences_with_offsets("The acme inc. shall pay. Second sentence."))
    assert len(result) > 1, (
        f"expected lowercase 'inc.' to allow a split (got {len(result)} sentence(s)): "
        f"{[s for s, *_ in result]}"
    )


def test_w0_6_offsets_are_correct_after_guard() -> None:
    """start/end offsets must still locate the substring in the original text."""
    from extraction.utils import sentences_with_offsets
    text = "Acme Inc. shall pay. Beta Corp. shall deliver."
    for sent, start, end in sentences_with_offsets(text):
        assert text[start:end] == sent, (
            f"offset mismatch: text[{start}:{end}]={text[start:end]!r} != {sent!r}"
        )


def test_w0_6_multi_abbreviation_in_one_sentence() -> None:
    """Sentence containing both Inc. and e.g. must remain unsplit."""
    from extraction.utils import sentences_with_offsets
    result = list(sentences_with_offsets("Acme Inc. may assign this e.g. by written notice."))
    assert len(result) == 1, f"expected 1 sentence, got {len(result)}: {[s for s, *_ in result]}"


def test_w0_6_tab_after_guard_round_trips_to_correct_offset() -> None:
    """A tab character after a guarded abbreviation must not corrupt offsets.

    PDF extraction routinely emits tabs between tokens.  The guard mechanism
    must preserve the original whitespace verbatim so text[start:end] == sent.
    """
    from extraction.utils import sentences_with_offsets
    text = "Acme Inc.\tshall pay the Vendor."
    results = list(sentences_with_offsets(text))
    assert len(results) == 1, (
        f"expected 1 sentence (tab after Inc.), got {len(results)}: {[s for s, *_ in results]}"
    )
    sent, start, end = results[0]
    assert text[start:end] == sent, (
        f"offset mismatch with tab: text[{start}:{end}]={text[start:end]!r} != {sent!r}"
    )


def test_w0_6_double_space_after_guard_round_trips_to_correct_offset() -> None:
    """A double-space after a guarded abbreviation must not corrupt offsets.

    PDFs commonly emit two spaces between tokens.  Round-trip requirement:
    text[start:end] must equal the yielded sentence string exactly.
    """
    from extraction.utils import sentences_with_offsets
    text = "Acme Inc.  shall pay the Vendor."
    results = list(sentences_with_offsets(text))
    assert len(results) == 1, (
        f"expected 1 sentence (double-space after Inc.), got {len(results)}: {[s for s, *_ in results]}"
    )
    sent, start, end = results[0]
    assert text[start:end] == sent, (
        f"offset mismatch with double-space: text[{start}:{end}]={text[start:end]!r} != {sent!r}"
    )


def test_w0_6_embedded_nul_in_source_does_not_corrupt_output() -> None:
    """NUL-bearing input must yield exact offsets: text[start:end] == sent for every triple.

    PyMuPDF and pdfplumber emit \\x00 for unmapped glyphs.  The guard mechanism
    must never mutate input characters, so every yielded sentence must be
    identical to the slice of the original text at the reported offsets.
    NUL-adjacent 'Inc.' may legitimately split (guards are bypassed for NUL
    input); the test asserts offset exactness, not guard suppression.
    """
    from extraction.utils import sentences_with_offsets
    text = "Acme Inc.\x00shall pay the Vendor. Second sentence here."
    results = list(sentences_with_offsets(text))
    assert results, "expected at least one sentence from NUL-bearing input"
    for sent, start, end in results:
        # Primary invariant: offset must locate the exact substring in the original text.
        assert text[start:end] == sent, (
            f"offset mismatch: text[{start}:{end}]={text[start:end]!r} != {sent!r}"
        )
        # Verbatim evidence: no character may differ from the original text slice.
        assert list(text[start:end]) == list(sent), (
            f"character-level mismatch at [{start}:{end}]: {text[start:end]!r} vs {sent!r}"
        )


# ---------------------------------------------------------------------------
# TESTS: W1.3 -- calibrate.py Group A (pyright) and Group B (ownership aggregate)
# ---------------------------------------------------------------------------

def test_w1_3_score_fixture_no_fixture_stem_param() -> None:
    """_score_fixture must not have a fixture_stem parameter (pyright A2)."""
    import inspect
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "_calibrate",
        Path(__file__).parent / "calibrate.py",
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    sig = inspect.signature(mod._score_fixture)
    assert "fixture_stem" not in sig.parameters, (
        "_score_fixture must not have fixture_stem parameter"
    )


def test_w1_3_score_selector_no_fixture_stem_param() -> None:
    """_score_selector must not have a fixture_stem parameter (pyright A2)."""
    import inspect
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "_calibrate2",
        Path(__file__).parent / "calibrate.py",
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    sig = inspect.signature(mod._score_selector)
    assert "fixture_stem" not in sig.parameters, (
        "_score_selector must not have fixture_stem parameter"
    )


def test_w1_3_field_ownership_table_exists() -> None:
    """FIELD_OWNERSHIP must be a module-level dict mapping field names to 'script' or 'llm'."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "_calibrate3",
        Path(__file__).parent / "calibrate.py",
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    assert hasattr(mod, "FIELD_OWNERSHIP"), "calibrate must export FIELD_OWNERSHIP"
    fo = mod.FIELD_OWNERSHIP
    assert isinstance(fo, dict), "FIELD_OWNERSHIP must be a dict"
    assert all(v in ("script", "llm") for v in fo.values()), (
        "FIELD_OWNERSHIP values must be 'script' or 'llm'"
    )
    # Mandatory llm fields per task spec
    for llm_field in ("data_flows", "relationships", "conditions"):
        assert fo.get(llm_field) == "llm", (
            f"FIELD_OWNERSHIP['{llm_field}'] must be 'llm'"
        )
    # parties is unambiguously script-direct
    assert fo.get("parties") == "script", "FIELD_OWNERSHIP['parties'] must be 'script'"


_CALIBRATE_SCRIPT = Path(__file__).resolve().parent / "calibrate.py"
_SKILL_ROOT_FOR_CALIBRATE = Path(__file__).resolve().parents[2]


def test_w1_3_calibrate_json_five_top_level_keys() -> None:
    """calibrate.py stdout must parse as JSON with exactly 5 top-level keys."""
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(_CALIBRATE_SCRIPT)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(_SKILL_ROOT_FOR_CALIBRATE),
    )
    assert proc.returncode == 0, proc.stderr[:500]
    data = json.loads(proc.stdout)
    assert len(data) == 5, (
        f"expected 5 top-level keys, got {len(data)}: {list(data.keys())}"
    )
    assert "aggregate_script_scope" in data, (
        "aggregate_script_scope key must be present"
    )


def test_w1_3_per_field_has_ownership_key() -> None:
    """Every entry in per_field must have an 'ownership' key equal to 'script' or 'llm'."""
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(_CALIBRATE_SCRIPT)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(_SKILL_ROOT_FOR_CALIBRATE),
    )
    assert proc.returncode == 0, proc.stderr[:500]
    data = json.loads(proc.stdout)
    for field, stats in data["per_field"].items():
        assert "ownership" in stats, f"per_field['{field}'] missing 'ownership' key"
        assert stats["ownership"] in ("script", "llm"), (
            f"per_field['{field}']['ownership'] must be 'script' or 'llm'"
        )


def test_w1_3_aggregate_script_scope_has_metrics() -> None:
    """aggregate_script_scope must contain precision, recall_promoted, recall_combined, f1, and raw counts."""
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(_CALIBRATE_SCRIPT)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(_SKILL_ROOT_FOR_CALIBRATE),
    )
    assert proc.returncode == 0, proc.stderr[:500]
    data = json.loads(proc.stdout)
    scope = data["aggregate_script_scope"]
    for key in ("precision", "recall_promoted", "recall_combined", "f1",
                "tp_promoted", "fp_promoted", "fn_labels", "n_labels", "n_promoted"):
        assert key in scope, f"aggregate_script_scope missing '{key}'"


def test_w1_3_existing_aggregate_unchanged() -> None:
    """The 'aggregate' key must still be present and have the same structure as before."""
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(_CALIBRATE_SCRIPT)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(_SKILL_ROOT_FOR_CALIBRATE),
    )
    assert proc.returncode == 0, proc.stderr[:500]
    data = json.loads(proc.stdout)
    agg = data["aggregate"]
    for key in ("precision", "recall_promoted", "recall_combined", "f1",
                "tp_promoted", "fp_promoted", "fn_labels"):
        assert key in agg, f"aggregate missing '{key}'"


def test_w1_3_calibrate_byte_identical() -> None:
    """Two consecutive runs of calibrate.py must produce byte-identical output."""
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    out1 = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(_CALIBRATE_SCRIPT)],
        capture_output=True,
        env=env,
        timeout=120,
        cwd=str(_SKILL_ROOT_FOR_CALIBRATE),
    ).stdout

    out2 = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(_CALIBRATE_SCRIPT)],
        capture_output=True,
        env=env,
        timeout=120,
        cwd=str(_SKILL_ROOT_FOR_CALIBRATE),
    ).stdout

    assert out1 == out2, "calibrate.py is not deterministic: two runs produced different output"


# ---------------------------------------------------------------------------
# TESTS: W2.1 -- lexicon package contract
# ---------------------------------------------------------------------------

def test_w2_1_get_bundle_en_populates_all_fields() -> None:
    """get_bundle('en') must return a LexiconBundle with every field non-empty."""
    from extraction.lexicon import get_bundle, LexiconBundle
    import dataclasses

    bundle = get_bundle("en")
    assert isinstance(bundle, LexiconBundle)
    for field in dataclasses.fields(bundle):
        value = getattr(bundle, field.name)
        assert value, (
            f"LexiconBundle.{field.name} must be non-empty for the EN bundle, got: {value!r}"
        )


def test_w2_1_get_bundle_unknown_lang_returns_en() -> None:
    """get_bundle with an unknown language code must return the EN bundle (W3 fallback contract)."""
    from extraction.lexicon import get_bundle

    en_bundle = get_bundle("en")
    xx_bundle = get_bundle("xx")
    assert en_bundle is xx_bundle, (
        "get_bundle('xx') must return the same EN bundle instance as get_bundle('en')"
    )


# ---------------------------------------------------------------------------
# TESTS: W2.2 -- HarvestContext and dispatcher rewire
# ---------------------------------------------------------------------------

def test_w2_2_harvest_context_deadlines_end_to_end() -> None:
    """HarvestContext wires the EN bundle + recording sink; harvest_deadlines
    appends a candidate with the expected frame (proves the ctx path without
    the orchestrator).
    """
    from extraction.context import HarvestContext
    from extraction.harvesters.deadlines import harvest_deadlines
    from extraction.schema import Candidate, SourceRef

    candidates: list[Candidate] = []
    source_ref = SourceRef(block_id="b0", heading_path=["Closing"])

    def _add_candidate(target_field, frame_type, value, snippet_text, source_ref, confidence, signals, anti_signals=None):
        eid = f"E{len(candidates):04d}"
        cid = f"C{len(candidates):04d}"
        candidates.append(
            Candidate(
                id=cid,
                target_field=target_field,
                frame_type=frame_type,
                normalized_value=value,
                confidence=confidence,
                evidence_ids=[eid],
                source_ref=source_ref,
                signals=signals,
                anti_signals=anti_signals or [],
            )
        )

    from extraction.lexicon import get_bundle
    ctx = HarvestContext(
        bundle=get_bundle("en"),
        add_candidate=_add_candidate,
        source_ref=source_ref,
        anti=[],
    )

    sent = "Seller shall deliver the officer's certificate no later than June 1, 2026."
    harvest_deadlines(ctx, sent)

    assert candidates, "harvest_deadlines must append at least one candidate via ctx"
    frames = {c.frame_type for c in candidates}
    assert "hard_deadline" in frames, (
        f"expected 'hard_deadline' frame, got: {frames}"
    )


# ---------------------------------------------------------------------------
# TESTS: W2.3 -- domain package split by entity concern
# ---------------------------------------------------------------------------

def test_w2_3_domain_is_package() -> None:
    """extraction.domain must be a package (directory), not a single module file."""
    import importlib
    import importlib.util
    spec = importlib.util.find_spec("extraction.domain")
    assert spec is not None, "extraction.domain must be importable"
    # A package has a submodule_search_locations attribute set
    assert spec.submodule_search_locations is not None, (
        "extraction.domain must be a package (directory with __init__.py), not a .py file"
    )


def test_w2_3_core_submodule_importable() -> None:
    """extraction.domain.core must be importable and export Party, Event, Obligation."""
    from extraction.domain.core import Party, Event, Obligation, Deadline, Communication, Document
    assert all(c is not None for c in [Party, Event, Obligation, Deadline, Communication, Document])


def test_w2_3_litigation_submodule_importable() -> None:
    """extraction.domain.litigation must export ClaimClass, WitnessMap, LegalAuthority."""
    from extraction.domain.litigation import ClaimClass, WitnessMap, LegalAuthority
    assert all(c is not None for c in [ClaimClass, WitnessMap, LegalAuthority])


def test_w2_3_corporate_submodule_importable() -> None:
    """extraction.domain.corporate must export OwnershipLink, ConditionPrecedent."""
    from extraction.domain.corporate import OwnershipLink, ConditionPrecedent
    assert all(c is not None for c in [OwnershipLink, ConditionPrecedent])


def test_w2_3_compliance_submodule_importable() -> None:
    """extraction.domain.compliance must export Control, DataFlow."""
    from extraction.domain.compliance import Control, DataFlow
    assert all(c is not None for c in [Control, DataFlow])


def test_w2_3_result_submodule_importable() -> None:
    """extraction.domain.result must export ExtractionResult and ENTITY_FIELDS."""
    from extraction.domain.result import ExtractionResult, ENTITY_FIELDS
    assert ExtractionResult is not None
    assert isinstance(ENTITY_FIELDS, dict)


def test_w2_3_init_reexports_all_public_names() -> None:
    """extraction.domain.__init__ must re-export every public name from old domain.py."""
    import extraction.domain as dm
    required_names = [
        "Party", "Entity", "Event", "Deadline", "Phase", "Task", "Obligation",
        "Control", "ConditionPrecedent", "Relationship", "OwnershipLink",
        "State", "Transition", "DecisionPoint", "ProcessStep", "InvestigationStep",
        "Communication", "Concept", "RiskItem", "NegotiationIssue", "Transfer",
        "ClaimClass", "DataFlow", "WitnessMap", "LegalAuthority", "IPAsset",
        "Document", "ExtractionHint", "EnrichmentDirective", "CoverageMap",
        "ExtractionResult", "ENTITY_FIELDS",
    ]
    for name in required_names:
        assert hasattr(dm, name), f"extraction.domain must export {name!r}"


def test_w2_3_flat_imports_still_work() -> None:
    """from extraction.domain import X must keep working for all historically used names."""
    from extraction.domain import (
        ExtractionResult, ENTITY_FIELDS, Party, Event, ClaimClass,
        WitnessMap, LegalAuthority, OwnershipLink, ConditionPrecedent,
        Control, DataFlow, Communication, Document, Obligation,
        Deadline, Entity, Relationship,
    )
    assert ExtractionResult is not None
    assert isinstance(ENTITY_FIELDS, dict)


def test_w2_3_extraction_result_from_dict_roundtrip() -> None:
    """ExtractionResult.from_dict must survive the split (uses ENTITY_FIELDS internally)."""
    from extraction.domain import ExtractionResult
    data = {
        "parties": [{"name": "Acme", "role": "buyer", "type": "corporation"}],
        "events": [{"date": "2026-01-01", "description": "signed"}],
        "legal_authorities": [{"citation": "2024 ONSC 1", "authority_type": "case_citation"}],
        "claim_classes": [{"priority_rank": 1, "name": "Secured"}],
        "witnesses": [{"witness_name": "A. Smith", "topics": ["delay"]}],
        "controls": [{"id": "C1", "description": "audit", "obligation_id": "OBL-0001"}],
        "data_flows": [{"from_system": "S1", "to_system": "S2"}],
        "conditions": [{"id": "CP1", "description": "financing"}],
        "ownership_links": [{"parent": "Parent Co", "child": "Sub Co"}],
    }
    result = ExtractionResult.from_dict(data)
    assert result.parties[0].name == "Acme"
    assert result.events[0].date == "2026-01-01"
    assert result.legal_authorities[0].citation == "2024 ONSC 1"
    assert result.claim_classes[0].priority_rank == 1
    assert result.witnesses[0].witness_name == "A. Smith"
    assert result.controls[0].id == "C1"
    assert result.data_flows[0].from_system == "S1"
    assert result.conditions[0].description == "financing"
    assert result.ownership_links[0].parent == "Parent Co"


def test_w2_3_classes_in_declared_module() -> None:
    """Each class must live in its declared submodule (not just re-exported from __init__)."""
    from extraction.domain import core, litigation, corporate, compliance, result as result_mod

    # core
    assert core.Party.__module__ == "extraction.domain.core"
    assert core.Event.__module__ == "extraction.domain.core"
    assert core.Obligation.__module__ == "extraction.domain.core"
    assert core.Communication.__module__ == "extraction.domain.core"
    assert core.Document.__module__ == "extraction.domain.core"

    # litigation
    assert litigation.ClaimClass.__module__ == "extraction.domain.litigation"
    assert litigation.WitnessMap.__module__ == "extraction.domain.litigation"
    assert litigation.LegalAuthority.__module__ == "extraction.domain.litigation"

    # corporate
    assert corporate.OwnershipLink.__module__ == "extraction.domain.corporate"
    assert corporate.ConditionPrecedent.__module__ == "extraction.domain.corporate"

    # compliance
    assert compliance.Control.__module__ == "extraction.domain.compliance"
    assert compliance.DataFlow.__module__ == "extraction.domain.compliance"

    # result
    assert result_mod.ExtractionResult.__module__ == "extraction.domain.result"


# ---------------------------------------------------------------------------
# TESTS: W2.4 -- helpers package split + utils compat re-exports
# ---------------------------------------------------------------------------

_W2_4_HELPERS_NAMES = [
    # money.py
    "money_text",
    "amount_number",
    "extract_payment_parties",
    "has_payment_verb",
    # dates.py
    "deadline_text",
    "has_deadline_signal",
    # subjects.py
    "extract_subject",
    "clean_party",
    "clean_entity",
    "extract_entity_like_names",
    # scoring.py
    "score_confidence",
    "score_boost",
    "anti_penalty",
]


def test_w2_4_helpers_package_exports() -> None:
    """helpers package must export every named public symbol.

    Plain loop, not pytest.mark.parametrize: every test in this file must stay
    standalone-runnable via the bare __main__ runner (W0 item 1 convention).
    """
    import extraction.helpers as helpers
    for name in _W2_4_HELPERS_NAMES:
        assert hasattr(helpers, name), (
            f"extraction.helpers must export {name!r}"
        )
        assert callable(getattr(helpers, name)) or isinstance(getattr(helpers, name), type), (
            f"extraction.helpers.{name} must be callable"
        )


def test_w2_4_utils_compat_reexports() -> None:
    """extraction.utils must still export every helpers name for backward compat."""
    import extraction.utils as utils
    for name in _W2_4_HELPERS_NAMES:
        assert hasattr(utils, name), (
            f"extraction.utils must still export {name!r} for compat"
        )


def test_w2_4_guard_split_reads_guards_from_lexicon() -> None:
    """_guard_split must read abbreviation guards from the EN lexicon bundle,
    not from a hard-coded constant in utils.py (single source of truth).
    """
    from extraction.lexicon import get_bundle
    from extraction.utils import ABBREVIATION_GUARDS_EN
    bundle = get_bundle("en")
    # After W2.4, utils' ABBREVIATION_GUARDS_EN must point to the lexicon value.
    assert ABBREVIATION_GUARDS_EN is bundle.abbreviation_guards or set(ABBREVIATION_GUARDS_EN) == set(bundle.abbreviation_guards), (
        "utils.ABBREVIATION_GUARDS_EN must equal lexicon EN bundle's abbreviation_guards"
    )


# ---------------------------------------------------------------------------
# TESTS: W3.4 -- NFD transliteration for Mermaid node IDs
# ---------------------------------------------------------------------------


def test_w3_4_strip_diacritics_exported() -> None:
    """strip_diacritics must be importable from extraction.utils and callable."""
    from extraction.utils import strip_diacritics
    assert callable(strip_diacritics)


def test_w3_4_strip_diacritics_french_accents() -> None:
    """Each common FR accented character must transliterate to its ASCII base.

    Plain loop, not parametrize (standalone __main__ runner convention).
    """
    from extraction.utils import strip_diacritics
    cases = {
        "é": "e", "è": "e", "ê": "e", "à": "a", "ç": "c",
        "î": "i", "ô": "o", "û": "u", "Œ": "OE", "œ": "oe",
    }
    for accented, expected in cases.items():
        assert strip_diacritics(accented) == expected, (
            f"strip_diacritics({accented!r}) must be {expected!r}, "
            f"got {strip_diacritics(accented)!r}"
        )


def test_w3_4_strip_diacritics_ascii_idempotent() -> None:
    """ASCII input must pass through strip_diacritics unchanged."""
    from extraction.utils import strip_diacritics
    for text in ("Operating Sub A", "PRIV-001", "", "plain ascii 123"):
        assert strip_diacritics(text) == text


def test_w3_4_slug_transliterates_accented_entity() -> None:
    """_slug must produce a stable ASCII-only ID for an accented FR entity name."""
    from extraction.materialize import _slug
    slug = _slug("Société Générale Ltée")
    assert slug == "societegeneraleltee", f"got {slug!r}"
    assert slug.isascii()


def test_w3_4_slug_ascii_behaviour_unchanged() -> None:
    """Existing ASCII slug behaviour (lowercase, alnum-only, 'x' fallback) is untouched."""
    from extraction.materialize import _slug
    assert _slug("Operating Sub A") == "operatingsuba"
    assert _slug("") == "x"
    assert _slug("!!!") == "x"


def test_w3_4_hierarchy_node_id_ascii_label_keeps_accents() -> None:
    """Hierarchy node IDs transliterate; the display label keeps accents verbatim."""
    from extraction.schema import Candidate, SourceRef, PromotionDecision
    from extraction.materialize import materialize_result
    cand = Candidate(id="c1", target_field="events", frame_type="event",
                     normalized_value={"date": "2026-01-01", "description": "déposé"},
                     source_ref=SourceRef(heading_path=["Conditions générales"]))
    dec = PromotionDecision(candidate_id="c1", action="promote", reason="ok")
    result, _ = materialize_result([cand], [dec], [])
    node = result.hierarchy[0]
    assert node["id"] == "H-conditionsgenerales", f"got {node['id']!r}"
    assert node["id"].isascii()
    assert node["label"] == "Conditions générales"


# ---------------------------------------------------------------------------
# TESTS: W4.0a -- _guard_split word-boundary-aware abbreviation guards
# ---------------------------------------------------------------------------

def test_w4_0a_fr_collision_sentence_final_quebec_splits() -> None:
    """FR: 'Québec.' ends with 'c.' but must not suppress the following sentence split."""
    from extraction.utils import sentences_with_offsets
    from extraction.lexicon import get_bundle

    bundle = get_bundle("fr")
    text = "Le tribunal est situé au Québec. La décision est rendue."
    results = list(sentences_with_offsets(text, bundle.abbreviation_guards))
    assert len(results) == 2, (
        f"FR: 'Québec.' must not suppress sentence split (got {len(results)} sentence(s)): "
        f"{[s for s, *_ in results]}"
    )


def test_w4_0a_fr_genuine_guard_still_protects() -> None:
    """FR: genuine 'art.' guard keeps 'art. 1457' as one sentence."""
    from extraction.utils import sentences_with_offsets
    from extraction.lexicon import get_bundle

    bundle = get_bundle("fr")
    text = "La règle prévue à l'art. 1457 s'applique ici."
    results = list(sentences_with_offsets(text, bundle.abbreviation_guards))
    assert len(results) == 1, (
        f"FR: 'art.' guard must protect 'art. 1457' from splitting "
        f"(got {len(results)} sentence(s)): {[s for s, *_ in results]}"
    )


def test_w4_0a_en_word_ending_in_guard_splits() -> None:
    """EN: compound name 'FinCorp.' must not suppress the split via guard 'Corp.' as its tail."""
    from extraction.utils import sentences_with_offsets
    from extraction.lexicon import get_bundle

    bundle = get_bundle("en")
    text = "This was filed by FinCorp. The next sentence follows."
    results = list(sentences_with_offsets(text, bundle.abbreviation_guards))
    assert len(results) == 2, (
        f"EN: 'FinCorp.' must not suppress sentence split via 'Corp.' substring "
        f"(got {len(results)} sentence(s)): {[s for s, *_ in results]}"
    )


def test_w4_0a_en_genuine_guard_still_protects() -> None:
    """EN: genuine 'i.e.' abbreviation still protected after fix."""
    from extraction.utils import sentences_with_offsets
    from extraction.lexicon import get_bundle

    bundle = get_bundle("en")
    text = "The closing date i.e. the Transfer Date is June 1."
    results = list(sentences_with_offsets(text, bundle.abbreviation_guards))
    assert len(results) == 1, (
        f"EN: 'i.e.' guard must protect from splitting "
        f"(got {len(results)} sentence(s)): {[s for s, *_ in results]}"
    )


def test_w4_0a_offset_invariant_fr_collision() -> None:
    """Offset invariant: text[start:end] == sent for every triple, including FR collision case."""
    from extraction.utils import sentences_with_offsets
    from extraction.lexicon import get_bundle

    bundle = get_bundle("fr")
    text = "Le tribunal est situé au Québec. La décision est rendue."
    for sent, start, end in sentences_with_offsets(text, bundle.abbreviation_guards):
        assert text[start:end] == sent, (
            f"offset mismatch: text[{start}:{end}]={text[start:end]!r} != {sent!r}"
        )


# ---------------------------------------------------------------------------
# W6 T2 Defect A -- hard-wrapped paragraph line-joining in md_adapter
# ---------------------------------------------------------------------------

def test_w6_defect_a_hardwrap_salary_full_sentence_promoted() -> None:
    # A sentence that hard-wraps mid-clause (no blank line) must produce a
    # complete obligation, not a truncated fragment.
    data = _run_extract(
        "## Compensation\n\n"
        "The Employer shall pay the Employee a base salary of $185,000 per annum, payable in equal\n"
        "semi-monthly instalments in accordance with the Employer's payroll practices.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    assert obligations, "expected at least one obligation"
    full = any("semi-monthly" in (o.get("description") or "") for o in obligations)
    truncated = any(
        (o.get("description") or "").endswith("payable in equal")
        for o in obligations
    )
    assert full, "obligation must include 'semi-monthly' from the wrapped continuation"
    assert not truncated, "obligation must not be truncated at line break"


def test_w6_defect_a_blank_line_still_separates_paragraphs() -> None:
    # A blank line between two clauses must keep them as separate blocks
    # (standard Markdown paragraph semantics).
    data = _run_extract(
        "The Employer shall pay $100.\n\n"
        "The Employee shall deliver the report.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    assert len(obligations) >= 2, (
        f"blank-line-separated clauses must produce separate obligations, got {len(obligations)}"
    )


def test_w6_defect_a_hardwrap_notify_full_sentence_promoted() -> None:
    # 'The Employee must immediately notify the Employer ... upon becoming aware of any
    # actual or suspected unauthorized disclosure' wraps at line 88 in en_employment.
    # After the fix it should promote the full sentence, not just the first line.
    data = _run_extract(
        "The Employee must immediately notify the Employer in writing upon becoming aware of any\n"
        "actual or suspected unauthorized disclosure of Confidential Information.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    assert obligations, "expected at least one obligation"
    full = any("unauthorized disclosure" in (o.get("description") or "") for o in obligations)
    assert full, "notification obligation must include continuation text from wrapped line"


# ---------------------------------------------------------------------------
# W6 T2 Defect C -- junk promotion demotion (governing-law, term, conditions precedent)
# ---------------------------------------------------------------------------

def test_w6_defect_c_governing_law_does_not_promote() -> None:
    # "This Agreement shall be governed by and construed in accordance with the laws of..."
    # is governing-law boilerplate and must not be promoted as an obligation.
    data = _run_extract(
        "This Agreement shall be governed by and construed in accordance with the laws of the Province of Ontario."
    )
    obligations = data["extraction_result"]["obligations"]
    governed_by = [
        o for o in obligations
        if re.search(r"shall\s+be\s+governed\s+by", o.get("description") or "", re.I)
    ]
    assert not governed_by, f"governing-law boilerplate must not promote: {governed_by}"


def test_w6_defect_c_term_clause_does_not_promote() -> None:
    # "This Agreement shall commence on April 1, 2026, and shall continue until terminated"
    # is a term clause (not a duty) and must not be promoted.
    data = _run_extract(
        "This Agreement shall commence on April 1, 2026, and shall continue until terminated in accordance with its terms."
    )
    obligations = data["extraction_result"]["obligations"]
    term_promo = [
        o for o in obligations
        if re.search(r"shall\s+commence", o.get("description") or "", re.I)
    ]
    assert not term_promo, f"term/commence clause must not promote: {term_promo}"


def test_w6_defect_c_condition_precedent_shall_have_does_not_promote() -> None:
    # "The Vendor shall have delivered all closing documents" uses 'shall have <participle>'
    # which is a condition precedent frame, not an affirmative duty.
    data = _run_extract(
        "The Vendor shall have delivered all closing documents required under Article 5."
    )
    obligations = data["extraction_result"]["obligations"]
    cond_prec = [
        o for o in obligations
        if re.search(r"shall\s+have\s+delivered", o.get("description") or "", re.I)
    ]
    assert not cond_prec, f"'shall have <participle>' condition precedent must not promote: {cond_prec}"


def test_w6_defect_c_purpose_list_item_without_party_does_not_promote() -> None:
    # "To create and maintain user accounts and authenticate access" is a purpose-list
    # item without a modal + identifiable party subject. Must not promote.
    data = _run_extract(
        "We collect personal information for the following purposes:\n"
        "- To create and maintain user accounts and authenticate access.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    purpose_items = [
        o for o in obligations
        if re.search(r"To\s+create\s+and\s+maintain", o.get("description") or "", re.I)
    ]
    assert not purpose_items, f"purpose-list item must not promote: {purpose_items}"


# ---------------------------------------------------------------------------
# W6 T2 Defect D -- table obligations materialize with party + deadline
# ---------------------------------------------------------------------------

def test_w6_defect_d_table_obligation_includes_party_and_deadline() -> None:
    # A table row with Responsible Party + Obligation + Due Date should materialize
    # the description as "Party shall <obligation> by <deadline>" (or similar).
    data = _run_extract(
        "| Responsible Party | Obligation | Due Date |\n"
        "| --- | --- | --- |\n"
        "| Company | Renew operating licence with FINTRAC | March 31, 2026 |\n"
    )
    obligations = data["extraction_result"]["obligations"]
    assert obligations, "expected at least one obligation from table row"
    desc = (obligations[0].get("description") or "").lower()
    has_party = "company" in desc
    has_deadline = "march 31" in desc or "2026" in desc
    assert has_party, f"table obligation description must include party 'Company', got: {desc!r}"
    assert has_deadline, f"table obligation description must include deadline '2026', got: {desc!r}"


def test_w6_defect_d_table_obligation_two_rows_two_obligations() -> None:
    # Two rows with the same obligation but different due dates (quarterly) must
    # produce two separate obligations.
    data = _run_extract(
        "| Responsible Party | Obligation | Due Date |\n"
        "| --- | --- | --- |\n"
        "| Company | Submit quarterly compliance certificate to the board of directors | June 30, 2026 |\n"
        "| Company | Submit quarterly compliance certificate to the board of directors | September 30, 2026 |\n"
    )
    obligations = data["extraction_result"]["obligations"]
    june = [o for o in obligations if "june" in (o.get("description") or "").lower() or "2026-06" in (o.get("description") or "")]
    sept = [o for o in obligations if "september" in (o.get("description") or "").lower() or "2026-09" in (o.get("description") or "")]
    assert june, "expected an obligation for the June 30 deadline"
    assert sept, "expected an obligation for the September 30 deadline"


# ---------------------------------------------------------------------------
# W6 T2 Defect E -- first-person corporate obligations
# ---------------------------------------------------------------------------

def test_w6_defect_e_we_maintain_obligation_promotes() -> None:
    # "We maintain an incident response plan requiring notification to the OPC within 72 hours"
    # must promote as an obligation for the organization.
    data = _run_extract(
        "**Organization:** Example Digital Services Inc.\n\n"
        "We maintain an incident response plan requiring notification to the Office of the Privacy\n"
        "Commissioner of Canada within 72 hours of discovery of a reportable breach.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    oir = [o for o in obligations if "72 hours" in (o.get("description") or "") or "incident response" in (o.get("description") or "").lower()]
    assert oir, "first-person 'We maintain... 72 hours' obligation must promote"


def test_w6_defect_e_employees_must_obligation_promotes() -> None:
    # "Employees with access are required to complete privacy training annually"
    # must promote as an obligation.
    data = _run_extract(
        "Employees with access to personal information are required to complete privacy training\n"
        "annually and are subject to confidentiality agreements.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    emp = [o for o in obligations if "training" in (o.get("description") or "").lower() or "employees" in (o.get("description") or "").lower()]
    assert emp, "'Employees ... are required to complete ... training' must promote as obligation"


# ---------------------------------------------------------------------------
# TESTS: W6 FIX ROUND -- Defect B, compound/list obligation splitting
# ---------------------------------------------------------------------------

def test_w6b_en_judgment_list_under_colon_splits_to_items() -> None:
    """A lead-in obligation sentence ending in ':' followed by list items must
    produce one obligation per item (lead-in + item), NOT the bare lead-in.

    Mirrors en_judgment: 'The Defendant shall pay to the Plaintiff:' + 4 items.
    """
    data = _run_extract(
        "## Order\n\n"
        "The Defendant shall pay to the Plaintiff:\n\n"
        "1. General damages of $485,000 for unpaid fees.\n"
        "2. Damages for wrongful termination of $190,000.\n"
        "3. Pre-judgment interest from September 15, 2024.\n"
        "4. Costs on a partial indemnity basis.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    descriptions = [o.get("description", "") for o in obligations]
    # Each item must be promoted with the lead-in subject carried through.
    assert any("485,000" in d for d in descriptions), (
        "obligation with '$485,000' (item 1) must be promoted"
    )
    assert any("190,000" in d for d in descriptions), (
        "obligation with '$190,000' (item 2) must be promoted"
    )
    assert any("interest" in d.lower() for d in descriptions), (
        "obligation for pre-judgment interest (item 3) must be promoted"
    )
    assert any("costs" in d.lower() for d in descriptions), (
        "obligation for costs (item 4) must be promoted"
    )
    # The bare lead-in must NOT appear as a standalone obligation.
    bare_lead_in = [
        d for d in descriptions
        if d.strip().rstrip(":").strip() in {
            "The Defendant shall pay to the Plaintiff",
            "The Defendant shall pay to the Plaintiff:",
        }
    ]
    assert not bare_lead_in, (
        f"bare lead-in must not promote as a standalone obligation: {bare_lead_in}"
    )


def test_w6b_fr_contract_list_under_colon_splits_to_items() -> None:
    """FR lead-in obligation 'L'Acheteur doit payer ... comme suit :' + 2 list items
    must produce one obligation per item, not the bare lead-in.
    """
    data = _run_extract(
        "## Achat et vente\n\n"
        "L’Acheteur doit payer le Prix d’achat comme suit :\n\n"
        "- un acompte de 1 234 567,89 $ payable au plus tard le 1er juin 2026 ;\n"
        "- le solde de 11 111 111,01 $ payable à la clôture par virement de fonds immédiatement disponibles.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    descriptions = [o.get("description", "") for o in obligations]
    assert any("acompte" in d or "1 234 567" in d or "1 234 567" in d for d in descriptions), (
        "obligation for acompte (first list item) must be promoted"
    )
    assert any("solde" in d or "11 111 111" in d or "11 111 111" in d for d in descriptions), (
        "obligation for solde (second list item) must be promoted"
    )
    bare = [d for d in descriptions if d.strip().rstrip(":").strip() in {
        "L’Acheteur doit payer le Prix d’achat comme suit",
        "L’Acheteur doit payer le Prix d’achat comme suit :",
    }]
    assert not bare, f"bare lead-in must not promote as standalone obligation: {bare}"


def test_w6b_en_spa_coordinated_conjunct_splits() -> None:
    """Coordinated conjunct 'The Vendor agrees to sell, and the Purchaser agrees to purchase...'
    must emit two obligations: one for Vendor, one for Purchaser.
    """
    data = _run_extract(
        "## Purchase and Sale\n\n"
        "The Vendor agrees to sell, and the Purchaser agrees to purchase, all issued and outstanding\n"
        "shares of Maplewood Technologies Ltd. (the \"Target Shares\"), free and clear of all\n"
        "encumbrances, for an aggregate purchase price of $12,500,000.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    descriptions = [o.get("description", "") for o in obligations]
    vendor_obls = [d for d in descriptions if "vendor" in d.lower() and ("sell" in d.lower() or "transfer" in d.lower())]
    purchaser_obls = [d for d in descriptions if "purchaser" in d.lower() and "purchase" in d.lower()]
    assert vendor_obls, "Vendor agrees-to-sell obligation must be promoted"
    assert purchaser_obls, "Purchaser agrees-to-purchase obligation must be promoted"


def test_w6b_fr_judgment_ainsi_que_splits_second_item() -> None:
    """FR 'La défenderesse doit verser ... 180 000,00 $..., ainsi que des dommages-intérêts
    de 60 000,00 $...' must produce two obligations: one for each monetary item.
    """
    data = _run_extract(
        "## Dispositif\n\n"
        "La défenderesse doit verser au demandeur la somme de 180 000,00 $ "
        "à titre de factures impayées, ainsi que des dommages-intérêts "
        "de 60 000,00 $ pour la résiliation fautive du contrat.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    descriptions = [o.get("description", "") for o in obligations]
    assert any("180" in d for d in descriptions), (
        "obligation for 180 000 $ must be promoted"
    )
    assert any("60" in d and "dommages" in d for d in descriptions), (
        "obligation for 60 000 $ dommages-intérêts must be promoted as separate obligation"
    )


# ---------------------------------------------------------------------------
# TESTS: W6 FIX ROUND -- Work item 2, deadlines description clamping
# ---------------------------------------------------------------------------

def test_w6_deadline_description_clamped_to_sentence() -> None:
    """Deadline candidate description must be the sentence containing the deadline
    phrase, not the joined paragraph.

    Regression: after paragraph-joining, the 'description' field was set to the
    whole joined paragraph.  It must be the sentence (or clause) holding the
    deadline expression only.
    """
    data = _run_extract(
        "The Distributor shall pay to the Licensor a royalty of $250,000.00 "
        "no later than June 30, 2026, and the Distributor shall remit quarterly sales reports.\n"
    )
    deadlines = data["extraction_result"]["deadlines"]
    assert deadlines, "at least one deadline must be promoted"
    desc = deadlines[0].get("description") or deadlines[0].get("date") or ""
    # The description must NOT start with 'June 30, 2026 The Distributor shall...'
    # (the paragraph-joined monster string) -- it should contain the deadline phrase only.
    assert not desc.startswith("June 30, 2026 The Distributor"), (
        f"description must not be a monster paragraph-joined string: {desc!r}"
    )


def test_w6_deadline_phrase_captures_date_correctly() -> None:
    """Deadline 'date_or_timing' must be the captured date/phrase, not a fragment.

    Regression: 'no later than' was captured as the phrase with no date, or
    'fails to cure within' became the phrase with no period.
    """
    data = _run_extract(
        "The Employee shall be eligible to receive a bonus payable no later than "
        "March 31 of each calendar year following the performance year.\n"
    )
    deadlines = data["extraction_result"]["deadlines"]
    assert deadlines, "deadline must be promoted"
    timing = deadlines[0].get("date") or deadlines[0].get("date_or_timing") or ""
    # Must NOT be just 'no later than' with no date
    assert timing != "no later than", (
        f"date_or_timing must capture the full phrase including the date, got: {timing!r}"
    )
    assert "March" in timing or "31" in timing or "no later than" in timing, (
        f"date_or_timing must contain the date, got: {timing!r}"
    )


def test_w6_deadline_cure_period_phrase_not_truncated() -> None:
    """Cure-period deadline must capture the period phrase, not sentence-initial fragment."""
    data = _run_extract(
        "If the Employee fails to cure within the 15-business-day cure period, "
        "the Employer may terminate for cause.\n"
    )
    deadlines = data["extraction_result"]["deadlines"]
    assert deadlines, "cure period deadline must be promoted"
    timing = deadlines[0].get("date") or deadlines[0].get("date_or_timing") or ""
    # 'fails to cure within' alone is not a valid timing phrase -- it must anchor to the period
    assert timing != "fails to cure within", (
        f"date_or_timing must not be a sentence-initial fragment, got: {timing!r}"
    )


# ---------------------------------------------------------------------------
# TESTS: W6 FIX ROUND -- Work item 3, parties description clamping
# ---------------------------------------------------------------------------

def test_w6_parties_defined_alias_captures_name_only() -> None:
    """defined_party_alias must capture the corporate name span, not sentence prefix.

    Regression: 'This Share Purchase Agreement is entered into by and among Northgate
    Acquisitions Corp' was promoted as the party 'name', which is a sentence fragment.
    """
    data = _run_extract(
        "This Share Purchase Agreement is entered into by and among Northgate Acquisitions Corp., "
        "a corporation incorporated under the laws of Ontario (\"Purchaser\"), "
        "Riverview Holdings Ltd., a corporation incorporated under the laws of British Columbia "
        "(\"Vendor\"), effective as of January 15, 2026.\n"
    )
    parties = data["extraction_result"]["parties"]
    names = [p.get("name", "") for p in parties]
    # Must NOT contain sentence-prefix fragments
    bad = [n for n in names if n.startswith("This ") or n.startswith("This Share")]
    assert not bad, f"party name must not be a sentence prefix: {bad}"
    # The actual corporate names must be present
    assert any("Northgate" in n for n in names), "Northgate Acquisitions Corp. must be a party"
    assert any("Riverview" in n for n in names), "Riverview Holdings Ltd. must be a party"


def test_w6_parties_no_duplicates() -> None:
    """Identical party names must not appear twice in the promoted parties list."""
    data = _run_extract(
        "This Share Purchase Agreement is entered into by and among Northgate Acquisitions Corp., "
        "a corporation incorporated under the laws of Ontario (\"Purchaser\"), "
        "Riverview Holdings Ltd., a corporation incorporated under the laws of British Columbia "
        "(\"Vendor\"), effective as of January 15, 2026.\n"
    )
    parties = data["extraction_result"]["parties"]
    names = [p.get("name", "").strip() for p in parties]
    seen: set[str] = set()
    for n in names:
        assert n not in seen, f"duplicate party name promoted: {n!r}"
        seen.add(n)


def test_w6_parties_agreement_intro_captures_name_not_sentence() -> None:
    """agreement_intro_party must extract a proper name token run, not a sentence fragment."""
    data = _run_extract(
        "This Employment Agreement is entered into between Sandbourne Industries Inc., "
        "a corporation incorporated under the laws of Alberta (\"Employer\"), "
        "and Jordan Fairweather (\"Employee\").\n"
    )
    parties = data["extraction_result"]["parties"]
    names = [p.get("name", "") for p in parties]
    bad = [n for n in names if n.startswith("This ")]
    assert not bad, f"party name must not start with sentence opener 'This': {bad}"


# ---------------------------------------------------------------------------
# TESTS: W6 T2 Round 3 -- Items 2-7
# ---------------------------------------------------------------------------

# Item 2a: MANGLED conjunct splice fix
def test_w6r3_conjunct_first_conjunct_carries_shared_object() -> None:
    """First conjunct after coordinate split must carry the shared object tail intact."""
    data = _run_extract(
        "The Vendor agrees to sell, and the Purchaser agrees to purchase, "
        "all issued and outstanding shares of Maplewood Technologies Ltd., free and clear "
        "of all encumbrances, for an aggregate purchase price of $12,500,000."
    )
    obligations = data["extraction_result"]["obligations"]
    descs = [o.get("description", "") for o in obligations]
    # First conjunct must say "Vendor agrees to sell all issued..."
    # NOT "The Vendor agrees to sell, purchase, all issued..."
    bad = [d for d in descs if ", purchase," in d]
    assert not bad, (
        f"First conjunct must not contain ', purchase,' (mangled splice): {bad}"
    )
    # The shared object tail must be present in a Vendor obligation
    vendor_descs = [d for d in descs if "Vendor" in d and "sell" in d.lower()]
    assert vendor_descs, f"Expected at least one Vendor/sell obligation, got: {descs}"
    assert any("Maplewood" in d or "shares" in d.lower() for d in vendor_descs), (
        f"Vendor conjunct must carry shared object tail (Maplewood/shares): {vendor_descs}"
    )


# Item 2b: TRIPLE DUPLICATE prevention
def test_w6r3_list_promoted_obligations_deduplicated() -> None:
    """Obligations promoted from a lead-in + list must not emit the same description 3x."""
    data = _run_extract(
        "Northgate Acquisitions Corp. shall deliver to the Vendor, at or before Closing, "
        "the following closing deliveries:\n\n"
        "1. A certified resolution of the board of directors.\n"
        "2. An executed officer's certificate.\n"
        "3. Evidence of financing.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    descs = [o.get("description", "") for o in obligations]
    # Normalize and check for duplicates
    norm_descs = [" ".join(d.lower().split()) for d in descs]
    seen: dict[str, int] = {}
    for nd in norm_descs:
        seen[nd] = seen.get(nd, 0) + 1
    triples = {nd: cnt for nd, cnt in seen.items() if cnt >= 3}
    assert not triples, (
        f"Obligations promoted 3+ times (triple duplicate): {triples}"
    )


# Item 2c: lead-in connector phrase stripping
def test_w6r3_lead_in_connector_stripped_from_composed_description() -> None:
    """Lead-in 'as follows' connector + colon must be stripped before composing item description."""
    data = _run_extract(
        "The Purchaser shall pay the Purchase Price as follows:\n\n"
        "- A deposit of $1,250,000 shall be paid to the Vendor's solicitors in trust.\n"
        "- The balance of $11,250,000 shall be paid at Closing by wire transfer.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    descs = [o.get("description", "") for o in obligations]
    # The description must not contain "as follows A deposit" (unstripped connector)
    bad = [d for d in descs if "as follows" in d.lower() and "$1,250,000" in d]
    assert not bad, (
        f"Lead-in connector 'as follows' must be stripped before composing description: {bad}"
    )


# Item 3: junk demotion for exclusive-jurisdiction, survival, condition-precedent, closing-logistics, procedural-channel
def test_w6r3_exclusive_jurisdiction_demoted() -> None:
    """Exclusive-jurisdiction clauses must be demoted to hint, not promoted as obligations."""
    data = _run_extract(
        "Any disputes arising from this Agreement shall be subject to the exclusive "
        "jurisdiction of the courts of the Province of Alberta."
    )
    obligations = data["extraction_result"]["obligations"]
    assert not obligations, (
        f"Exclusive-jurisdiction clause must not be promoted as obligation: {obligations}"
    )


def test_w6r3_survival_clause_demoted() -> None:
    """Survival clauses must be demoted to hint, not promoted as obligations."""
    data = _run_extract(
        "The obligation of confidentiality shall survive termination of this Agreement "
        "indefinitely with respect to trade secrets and for 5 years with respect to other "
        "Confidential Information."
    )
    obligations = data["extraction_result"]["obligations"]
    assert not obligations, (
        f"Survival clause must not be promoted as obligation: {obligations}"
    )


def test_w6r3_condition_precedent_sentence_demoted() -> None:
    """Condition-precedent sentences must be demoted to hint, not promoted as obligations."""
    data = _run_extract(
        "The obligations of the Vendor to complete the Closing are subject to the condition "
        "that the Purchaser shall have paid the deposit described in Section 3.1 prior to Closing."
    )
    obligations = data["extraction_result"]["obligations"]
    assert not obligations, (
        f"Condition-precedent sentence must not be promoted as obligation: {obligations}"
    )


def test_w6r3_closing_logistics_demoted() -> None:
    """Closing-logistics sentences must be demoted to hint, not promoted as obligations."""
    data = _run_extract(
        "The closing of the transactions contemplated herein (the \"Closing\") shall occur "
        "at 10:00 a.m. on February 28, 2026."
    )
    obligations = data["extraction_result"]["obligations"]
    assert not obligations, (
        f"Closing-logistics sentence must not be promoted as obligation: {obligations}"
    )


def test_w6r3_procedural_channel_sentence_demoted() -> None:
    """Procedural-channel sentences (requests must be submitted to...) must not be promoted as obligations."""
    data = _run_extract(
        "Requests must be submitted in writing to privacy@example.org."
    )
    obligations = data["extraction_result"]["obligations"]
    assert not obligations, (
        f"Procedural-channel sentence must not be promoted as obligation: {obligations}"
    )


def test_w6r3_genuine_obligation_not_demoted_by_junk_filter() -> None:
    """A genuine obligation must still be promoted even when junk patterns are active."""
    data = _run_extract(
        "The Employer shall pay the Employee a base salary of $185,000 per annum, "
        "payable in equal semi-monthly instalments."
    )
    obligations = data["extraction_result"]["obligations"]
    assert obligations, "Genuine pay obligation must still be promoted after junk filter expansion"


# Item 4: citation fragment not promoted as obligation
def test_w6r3_citation_fragment_not_promoted_as_obligation() -> None:
    """A sentence fragment starting mid-citation must not be promoted as an obligation."""
    # This is a fragment that starts after a case citation split inside a sentence.
    # It should either not be segmented as a sentence, or the harvester should reject it.
    data = _run_extract(
        "In Maple Leaf Foods Inc. v. Schneiders Corp., 1995 CanLII 3773 (ON CA), "
        "the court held that lost profits must be calculated on the balance of the contract term."
    )
    obligations = data["extraction_result"]["obligations"]
    # No obligation should start with a lowercase word or a preposition
    bad = [o for o in obligations
           if o.get("description", "")[:1].islower()
           or o.get("description", "").startswith("of ")]
    assert not bad, (
        f"Citation fragment obligations promoted (start with lowercase/preposition): {bad}"
    )


# Item 5: description tail-trimming
def test_w6r3_description_tail_trimmed_in_accordance_with() -> None:
    """Trailing ', in accordance with X' must be stripped from obligation description."""
    from extraction.harvesters.obligations import _trim_obligation_description
    sent = "The Employer shall pay the Employee a base salary of $185,000 per annum, payable in equal semi-monthly instalments in accordance with the Employer's payroll practices."
    trimmed = _trim_obligation_description(sent)
    assert "in accordance with" not in trimmed, (
        f"Trailing 'in accordance with' must be stripped: {trimmed!r}"
    )
    # Must still contain the monetary amount
    assert "$185,000" in trimmed, (
        f"Monetary amount must be preserved after trimming: {trimmed!r}"
    )


def test_w6r3_description_tail_trimmed_to_reasonable_satisfaction() -> None:
    """Trailing ', to the reasonable satisfaction of X' must be stripped."""
    from extraction.harvesters.obligations import _trim_obligation_description
    sent = "The Employee shall have 15 business days after receipt of such written notice to cure the deficiency to the reasonable satisfaction of the Employer."
    trimmed = _trim_obligation_description(sent)
    assert "to the reasonable satisfaction" not in trimmed, (
        f"Trailing 'to the reasonable satisfaction of' must be stripped: {trimmed!r}"
    )


def test_w6r3_description_tail_not_trimmed_when_monetary() -> None:
    """A tail containing a monetary amount must NOT be trimmed."""
    from extraction.harvesters.obligations import _trim_obligation_description
    sent = "The Vendor shall pay the balance of $11,250,000 in accordance with Section 3.1."
    trimmed = _trim_obligation_description(sent)
    # The tail contains a monetary amount -> must NOT be trimmed
    assert "$11,250,000" in trimmed, (
        f"Tail with monetary amount must not be trimmed: {trimmed!r}"
    )


def test_w6r3_description_tail_not_trimmed_when_date_present() -> None:
    """A tail containing a deadline expression must NOT be trimmed."""
    from extraction.harvesters.obligations import _trim_obligation_description
    sent = "The Employee shall be eligible for the bonus payable no later than March 31 of each calendar year."
    trimmed = _trim_obligation_description(sent)
    # Contains a date expression -> must NOT trim anything that removes the date
    assert "March 31" in trimmed, (
        f"Date expression must be preserved after trimming: {trimmed!r}"
    )


# Item 6: first-person corporate subject resolution
def test_w6r3_we_subject_resolved_to_operator_in_description() -> None:
    """'We maintain...' with a single unambiguous operator must resolve 'We' in description."""
    data = _run_extract(
        "Example Digital Services Inc. (\"Company\") is the operator of this platform.\n"
        "We maintain an incident response plan requiring notification to the Office of the "
        "Privacy Commissioner of Canada within 72 hours of discovery of a reportable breach."
    )
    obligations = data["extraction_result"]["obligations"]
    # At least one obligation should reference "Example Digital" (not "We") in description
    descs = [o.get("description", "") for o in obligations]
    resolved = [d for d in descs if "Example Digital" in d and "incident response" in d.lower()]
    assert resolved, (
        f"'We maintain...' obligation must resolve 'We' to 'Example Digital Services Inc.' "
        f"in description; got: {descs}"
    )


def test_w6r3_we_resolution_skipped_when_multiple_operators() -> None:
    """When multiple operators exist, 'We' resolution must be skipped (ambiguous)."""
    data = _run_extract(
        "Alpha Corp. and Beta Inc. are both operators.\n"
        "We maintain records as required by law."
    )
    obligations = data["extraction_result"]["obligations"]
    descs = [o.get("description", "") for o in obligations]
    # With two candidates, 'We' must NOT be replaced by either party name
    ambiguous_resolved = [d for d in descs
                          if ("Alpha Corp" in d or "Beta Inc" in d) and "maintain" in d.lower()]
    assert not ambiguous_resolved, (
        f"With multiple operators, 'We' must not be resolved; got: {ambiguous_resolved}"
    )


# Item 7: deadline FP fix - junk deadline descriptions rejected
def test_w6r3_deadline_junk_fp_not_promoted() -> None:
    """Deadline candidates whose description starts with the timing phrase (not a sentence) must not be promoted."""
    data = _run_extract(
        "The Employee shall provide the Employer with no less than 30 days prior written "
        "notice of the Employee's intention to resign."
    )
    deadlines = data["extraction_result"]["deadlines"]
    # No deadline description should start with '30 days prior written notice The Employee...'
    # (that is the junk pattern from old broken capture)
    bad = [d for d in deadlines
           if d.get("description", "").startswith("30 days") or
           d.get("date_or_timing", "").startswith("30 days prior written notice The")]
    assert not bad, (
        f"Deadline must not have timing phrase as prefix of full description: {bad}"
    )


def test_w6r3_hyphen_cure_period_timing_not_starts_with_fails() -> None:
    """Cure-period deadline from '15-business-day' hyphenated sentence must not emit timing starting with 'fails'."""
    data = _run_extract(
        "The Employee shall have 15 business days after receipt of such written notice to cure the deficiency. "
        "If the Employee fails to cure within the 15-business-day cure period, the Employer may terminate for cause."
    )
    deadlines = data["extraction_result"]["deadlines"]
    timing_values = [d.get("date") or d.get("date_or_timing", "") for d in deadlines]
    bad = [t for t in timing_values if t.lower().startswith("fails")]
    assert not bad, (
        f"Cure-period timing must not start with 'fails'; got timing values: {timing_values}"
    )


def test_w6r3_no_later_than_timing_does_not_embed_sentence() -> None:
    """'no later than March 31 of each calendar year' timing must not include the following sentence body."""
    data = _run_extract(
        "The Employee shall be eligible to participate in the annual performance bonus plan, "
        "with a target bonus of 20% of base salary, payable no later than March 31 of each "
        "calendar year following the performance year, subject to the Employee remaining employed."
    )
    deadlines = data["extraction_result"]["deadlines"]
    timing_values = [d.get("date") or d.get("date_or_timing", "") for d in deadlines]
    # Timing must not embed the full sentence text; 'The Employee shall' is sentence marker
    bad = [t for t in timing_values if "The Employee shall" in t or "the Employer" in t]
    assert not bad, (
        f"Timing value must not embed full sentence; got: {timing_values}"
    )


# ---------------------------------------------------------------------------
# TESTS: W6 T2 Round 4 -- Bugs 1-9
# ---------------------------------------------------------------------------

# Bug 1: Dedup on punctuation-normalized description
def test_w6r4_dedup_punct_normalized_description() -> None:
    """Obligations whose descriptions differ only in punctuation variants must be deduplicated."""
    from extraction.resolver import dedupe_candidates, semantic_key
    from extraction.schema import Candidate, SourceRef

    ref = SourceRef(block_id="1", anchor="a1")
    # Two candidates with descriptions that differ only in curly vs straight quotes.
    desc_a = "Northgate Acquisitions Corp. shall deliver the officer’s certificate"
    desc_b = "Northgate Acquisitions Corp. shall deliver the officer's certificate"
    cand_a = Candidate(id="C1", target_field="obligations", frame_type="positive_obligation",
                       normalized_value={"party": "Northgate", "description": desc_a},
                       confidence=0.80, evidence_ids=["E1"], source_ref=ref)
    cand_b = Candidate(id="C2", target_field="obligations", frame_type="positive_obligation",
                       normalized_value={"party": "Northgate", "description": desc_b},
                       confidence=0.75, evidence_ids=["E2"], source_ref=ref)
    out = dedupe_candidates([cand_a, cand_b])
    assert len(out) == 1, (
        f"Obligations differing only in quote-char variants must be deduplicated to 1, got {len(out)}"
    )
    assert out[0].confidence == 0.80, "keep-first by highest confidence"


# Bug 2: Conjunct splitter preserves verb in second conjunct
def test_w6r4_conjunct_second_conjunct_carries_verb() -> None:
    """Second conjunct must include the verb from 'agrees to purchase'."""
    data = _run_extract(
        "The Vendor agrees to sell, and the Purchaser agrees to purchase, "
        "all issued and outstanding shares of Maplewood Technologies Ltd."
    )
    obligations = data["extraction_result"]["obligations"]
    descs = [o.get("description", "") for o in obligations]
    purchaser_descs = [d for d in descs if "purchaser" in d.lower() or "Purchaser" in d]
    assert purchaser_descs, f"Purchaser obligation must be promoted; got: {descs}"
    # The purchaser obligation must contain 'purchase' (verb), not just 'agrees to all issued...'
    bad = [d for d in purchaser_descs
           if "purchase" not in d.lower()
           and "all issued" in d.lower()]
    assert not bad, (
        f"Second conjunct missing verb 'purchase': {purchaser_descs}"
    )


# Bug 3: Citation fragment rejected (starts lowercase or dangling preposition)
def test_w6r4_citation_fragment_starts_lowercase_rejected() -> None:
    """A sentence fragment starting with 'of Canada, ...' must not be promoted as obligation."""
    data = _run_extract(
        "In Transamerica Life Insurance Co. of Canada, 2006 SCC 30, "
        "lost profits must be calculated on the balance of the contract term."
    )
    obligations = data["extraction_result"]["obligations"]
    bad = [o for o in obligations
           if o.get("description", "").startswith("of ")
           or (o.get("description", "") and o["description"][0].islower())]
    assert not bad, (
        f"Citation fragment starting with lowercase/preposition promoted: {[o['description'] for o in bad]}"
    )


def test_w6r4_obligation_sentence_starting_lowercase_rejected() -> None:
    """A sentence starting with a lowercase letter must not be promoted as an obligation."""
    from extraction.harvesters.obligations import harvest_obligation
    from extraction.context import HarvestContext
    from extraction.schema import Candidate, SourceRef
    from extraction.lexicon import get_bundle

    candidates: list[Candidate] = []
    ref = SourceRef(block_id="1", anchor="a1")

    def _add(target_field, frame_type, value, snippet_text, source_ref,
             confidence, signals, anti_signals=None):
        candidates.append(Candidate(id=f"C{len(candidates)}", target_field=target_field,
                                    frame_type=frame_type, normalized_value=value,
                                    confidence=confidence, evidence_ids=[],
                                    source_ref=source_ref, signals=signals))

    ctx = HarvestContext(bundle=get_bundle("en"), add_candidate=_add,
                         source_ref=ref, anti=[])
    # Fragment starting with lowercase preposition 'of'
    harvest_obligation(ctx, "of Canada, 2006 SCC 30, lost profits must be calculated on the balance")
    assert not candidates, (
        f"Fragment starting with lowercase/preposition 'of' must not emit obligation candidate; got: {candidates}"
    )


# Bug 4: FR tail-trim must not fire mid-sentence before the main verb
def test_w6r4_fr_tail_trim_not_fires_before_main_verb() -> None:
    """FR 'en vertu de' mid-sentence must not trim to fragment when modal follows."""
    from extraction.harvesters.obligations import _trim_obligation_description
    sent = (
        "Tout avis requis en vertu de la présente Convention "
        "doit être transmis par courrier recommandé ou par courriel"
    )
    trimmed = _trim_obligation_description(sent)
    # Must keep 'doit' and the content after 'Convention' -- must NOT truncate to 'Tout avis requis'
    assert "doit" in trimmed, (
        f"FR tail-trim must not remove main verb 'doit'; got: {trimmed!r}"
    )
    assert len(trimmed.split()) >= 5, (
        f"Trimmed description must have >= 5 content tokens; got: {trimmed!r}"
    )


def test_w6r4_fr_trim_only_after_main_verb() -> None:
    """FR trim markers occurring after the main modal must still fire."""
    from extraction.harvesters.obligations import _trim_obligation_description
    sent = (
        "Tout avis requis en vertu de la présente Convention "
        "doit être transmis par courrier recommandé ou par courriel "
        "à l'attention des représentants désignés des parties"
    )
    trimmed = _trim_obligation_description(sent)
    # 'doit être transmis par courrier recommandé' should be preserved
    assert "doit" in trimmed, f"Main verb must be present: {trimmed!r}"
    assert "courrier" in trimmed, f"Delivery method must be present: {trimmed!r}"


# Bug 5a: 'at the rate prescribed under' trailing marker must fire
def test_w6r4_trim_at_rate_prescribed_under_fires() -> None:
    """', at the rate prescribed under X' is a trailing statutory reference and must be trimmed."""
    from extraction.harvesters.obligations import _trim_obligation_description
    sent = (
        "The Defendant shall pay to the Plaintiff Pre-judgment interest "
        "from September 15, 2024, at the rate prescribed under the Courts of Justice Act"
    )
    trimmed = _trim_obligation_description(sent)
    assert "at the rate prescribed under" not in trimmed, (
        f"Trailing 'at the rate prescribed under' must be trimmed; got: {trimmed!r}"
    )
    # Must preserve the date
    assert "September 15, 2024" in trimmed or "2024" in trimmed, (
        f"Date must be preserved after trim: {trimmed!r}"
    )


# Bug 5b: ', including X' trailing marker with no date/amount must fire
def test_w6r4_trim_including_clause_fires() -> None:
    """', including extended health, dental, and life insurance, in accordance with...' tail must trim."""
    from extraction.harvesters.obligations import _trim_obligation_description
    sent = (
        "The Employer shall provide the Employee with group benefits coverage, "
        "including extended health, dental, and life insurance, "
        "in accordance with Sandbourne Industries group policy terms"
    )
    trimmed = _trim_obligation_description(sent)
    # The trim must shorten the description - 'in accordance with' should be gone
    assert "in accordance with" not in trimmed, (
        f"', in accordance with...' must be trimmed from tail; got: {trimmed!r}"
    )
    # The core must still be present
    assert "group benefits coverage" in trimmed or "benefits" in trimmed, (
        f"Core description must be preserved: {trimmed!r}"
    )


def test_w6r4_trim_including_with_date_not_trimmed() -> None:
    """', including...' tail containing a date must NOT be trimmed."""
    from extraction.harvesters.obligations import _trim_obligation_description
    sent = (
        "The Employer shall provide the Employee with group benefits coverage, "
        "including a bonus payable no later than March 31 of each year"
    )
    trimmed = _trim_obligation_description(sent)
    # Guard fires because tail has date expression
    assert "March 31" in trimmed, (
        f"Date in including-tail must prevent trim; got: {trimmed!r}"
    )


# Bug 6: Markdown emphasis stripped from description
def test_w6r4_markdown_bold_prefix_stripped_from_description() -> None:
    """'**Label**: sentence...' bold-prefix must be stripped; obligation starts at sentence."""
    data = _run_extract(
        "**Consent**: Users must expressly consent to the collection and use of their "
        "personal information for marketing communications by checking an opt-in box."
    )
    obligations = data["extraction_result"]["obligations"]
    assert obligations, "obligation must be promoted from bold-prefixed sentence"
    descs = [o.get("description", "") for o in obligations]
    bad = [d for d in descs if d.startswith("**")]
    assert not bad, (
        f"Obligation description must not start with markdown bold markers: {bad}"
    )
    # Must start with 'Users' (the sentence subject)
    good = [d for d in descs if d.startswith("Users") or "Users" in d[:10]]
    assert good, f"Description must start with the sentence subject; got: {descs}"


def test_w6r4_markdown_bold_stripped_from_trim_unit() -> None:
    """_trim_obligation_description must strip leading '**X**: ' bold-prefix."""
    from extraction.harvesters.obligations import _trim_obligation_description
    sent = "**Consent**: Users must expressly consent to the collection."
    trimmed = _trim_obligation_description(sent)
    assert not trimmed.startswith("**"), (
        f"Leading markdown bold prefix must be stripped; got: {trimmed!r}"
    )


# Bug 7: Lead-in with own amount promotes lead-in alone
def test_w6r4_lead_in_with_amount_also_promoted() -> None:
    """When lead-in carries its own monetary amount, it must also be promoted as a standalone obligation."""
    data = _run_extract(
        "The Purchaser shall pay the Purchase Price of $12,500,000 as follows:\n\n"
        "- A deposit of $1,250,000 shall be paid no later than January 22, 2026.\n"
        "- The balance of $11,250,000 shall be paid at Closing by wire transfer.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    descs = [o.get("description", "") for o in obligations]
    # Lead-in alone must be promoted (with $12,500,000)
    lead_in_promoted = [d for d in descs if "$12,500,000" in d and "as follows" not in d.lower()]
    assert lead_in_promoted, (
        f"Lead-in with own amount '$12,500,000' must be promoted standalone; got descs: {descs}"
    )


def test_w6r4_composed_item_uses_core_not_full_lead_in() -> None:
    """Composed list items must join core (subject+modal+verb), not the full lead-in text."""
    data = _run_extract(
        "The Purchaser shall pay the Purchase Price of $12,500,000 as follows:\n\n"
        "- A deposit of $1,250,000 shall be paid no later than January 22, 2026.\n"
    )
    obligations = data["extraction_result"]["obligations"]
    descs = [o.get("description", "") for o in obligations]
    # No description should contain both 'Purchase Price' AND 'A deposit' as "shall pay Purchase Price A deposit"
    bad = [d for d in descs if "Purchase Price" in d and "A deposit" in d and "$12,500,000" not in d]
    assert not bad, (
        f"Composed item must not embed full lead-in text: {bad}"
    )


# Bug 8: Party alias role substitution in description subject
def test_w6r4_legal_name_substituted_with_role_alias() -> None:
    """When a party's legal name equals the obligation subject and has a role alias, substitute role."""
    data = _run_extract(
        "This Agreement is between Northgate Acquisitions Corp. (\"Purchaser\") "
        "and Riverview Holdings Ltd. (\"Vendor\").\n\n"
        "Northgate Acquisitions Corp. shall deliver closing documents to the Vendor at or before Closing."
    )
    obligations = data["extraction_result"]["obligations"]
    descs = [o.get("description", "") for o in obligations]
    # The obligation subject should use 'Purchaser' not 'Northgate Acquisitions Corp.'
    good = [d for d in descs if d.startswith("Purchaser") and "deliver" in d.lower()]
    assert good, (
        f"Legal name 'Northgate Acquisitions Corp.' must be substituted with role 'Purchaser' in description; "
        f"got: {descs}"
    )


# Bug 9: No-party-subject junk rule
def test_w6r4_passive_non_party_subject_demoted() -> None:
    """Obligation whose grammatical subject is not a party (passive/impersonal) must not promote."""
    data = _run_extract(
        "The register shall be made available to the board of directors upon request."
    )
    obligations = data["extraction_result"]["obligations"]
    bad = [o for o in obligations if "register" in o.get("description", "").lower()[:20]]
    assert not bad, (
        f"Passive/impersonal obligation with non-party subject must not promote: {bad}"
    )


def test_w6r4_fr_impersonal_ne_doit_survenir_demoted() -> None:
    """FR impersonal 'aucun changement défavorable ... ne doit survenir' must not promote."""
    data = _run_extract(
        "aucun changement défavorable important ne doit survenir "
        "relativement aux activités de Technologies Malouin Ltée avant la Clôture"
    )
    obligations = data["extraction_result"]["obligations"]
    bad = [o for o in obligations if "changement" in o.get("description", "").lower()[:30]]
    assert not bad, (
        f"FR impersonal MAC clause must not be promoted: {bad}"
    )


def test_w6r4_party_passive_subject_still_promotes() -> None:
    """An obligation with a party-like subject in passive voice must still promote."""
    data = _run_extract(
        "Sandbourne Industries Inc. (\"Employer\").\n\n"
        "The Employer shall provide the Employee with group benefits coverage."
    )
    obligations = data["extraction_result"]["obligations"]
    assert obligations, "Party-subject obligation must still promote"


# ---------------------------------------------------------------------------
# W6 Fix: composed list-item obligations evidence must be verbatim source text
# ---------------------------------------------------------------------------

def test_w6_list_item_evidence_is_verbatim_source_block() -> None:
    """Each obligation emitted from a lead-in+list block must have evidence_text
    that is a verbatim substring of one of the source blocks (lead-in or item block),
    never a synthesized composite string.

    The bug: previously evidence_text = f"{lead_in_core} {item}" -- a string that
    does not appear anywhere in the source -- violating the project invariant that
    evidence snippets must be verbatim source spans.
    """
    lead_in = "Vendor shall deliver to the Purchaser, at or before Closing, the following:"
    item_a = "A certified resolution of the board of directors approving the transaction."
    item_b = "An executed officer's certificate confirming representations are true."
    doc_text = f"{lead_in}\n\n- {item_a}\n- {item_b}\n"

    data = _run_extract(doc_text)
    sidecar = data["candidate_manifest"]

    # Collect all source blocks from the input document for verbatim check.
    source_blocks = [lead_in, item_a, item_b]

    # Gather evidence snippets for obligation candidates marked list_split.
    list_split_obligations = [
        c for c in sidecar.get("candidates", [])
        if c.get("target_field") == "obligations" and "list_split" in c.get("signals", [])
    ]
    assert list_split_obligations, (
        "Expected at least one obligation candidate with 'list_split' signal"
    )

    # Build evidence lookup by id.
    evidence_by_id = {e["id"]: e for e in sidecar.get("evidence_packets", [])}

    bad: list[str] = []
    for cand in list_split_obligations:
        for eid in cand.get("evidence_ids", []):
            ep = evidence_by_id.get(eid)
            if ep is None:
                continue
            snippet = ep.get("snippet", "")
            # Check: snippet must be a verbatim substring of at least one source block.
            if not any(snippet in blk or blk.startswith(snippet) for blk in source_blocks):
                bad.append(snippet)

    assert not bad, (
        f"Obligation evidence snippets must be verbatim source spans; "
        f"non-verbatim snippets found: {bad}"
    )


def test_w6_list_item_evidence_verbatim_integration_en_spa_contract() -> None:
    """Integration: all obligation candidates from en_spa_contract that carry
    'list_split' signal must have evidence_text verbatim in the source document
    (after the same whitespace normalisation applied by the snippet() helper).

    The snippet() function collapses whitespace and strips leading/trailing punctuation
    before storing, so the check uses that same normalised form of the source text.
    """
    import re as _re

    fixture = Path(__file__).parent / "fixtures" / "en_spa_contract.md"
    assert fixture.exists(), f"Fixture missing: {fixture}"
    doc_text = fixture.read_text(encoding="utf-8")
    # Normalise source the same way snippet() does: collapse whitespace, strip edges.
    doc_normalised = _re.sub(r"\s+", " ", doc_text).strip(" .,;:")

    data = _run_extract_file(fixture)
    sidecar = data["candidate_manifest"]

    list_split_obligations = [
        c for c in sidecar.get("candidates", [])
        if c.get("target_field") == "obligations" and "list_split" in c.get("signals", [])
    ]
    assert list_split_obligations, (
        "en_spa_contract must produce at least one list_split obligation candidate"
    )

    evidence_by_id = {e["id"]: e for e in sidecar.get("evidence_packets", [])}

    bad: list[str] = []
    for cand in list_split_obligations:
        for eid in cand.get("evidence_ids", []):
            ep = evidence_by_id.get(eid)
            if ep is None:
                continue
            snip = ep.get("snippet", "")
            if snip and snip not in doc_normalised:
                bad.append(snip)

    assert not bad, (
        f"en_spa_contract: {len(bad)} obligation evidence snippet(s) are not verbatim "
        f"in the normalised source document:\n" + "\n".join(f"  - {s!r}" for s in bad)
    )


# ---------------------------------------------------------------------------
# W6 T2 Defect F -- md_adapter edge defects: list absorption and fence joining
# ---------------------------------------------------------------------------

def test_w6_defect_f_flush_left_line_after_list_starts_new_paragraph() -> None:
    """A flush-left non-list line immediately after a list item (no blank line) must
    NOT be absorbed into the list_item block; it must become a separate paragraph.

    Defect: the old continuation loop accepted any non-structural, non-blank line
    as list continuation, so 'This is a paragraph.' was swallowed into the item.
    Fix: only indented lines (or lines with leading whitespace) may continue a
    list item; a flush-left line starts a new block.
    """
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from normalize.md_adapter import parse_text

    doc = parse_text("- Item two\nThis is a paragraph.\n")
    block_types = [b.block_type for b in doc.blocks]
    block_texts = [b.text for b in doc.blocks]

    assert len(doc.blocks) == 2, (
        f"Expected 2 blocks (list_item + paragraph), got {len(doc.blocks)}: {list(zip(block_types, block_texts))}"
    )
    assert block_types[0] == "list_item", (
        f"First block must be list_item, got: {block_types[0]!r}"
    )
    assert block_texts[0] == "Item two", (
        f"list_item text must be 'Item two' (not absorbed), got: {block_texts[0]!r}"
    )
    assert block_types[1] == "paragraph", (
        f"Second block must be paragraph, got: {block_types[1]!r}"
    )
    assert block_texts[1] == "This is a paragraph.", (
        f"Paragraph text must be 'This is a paragraph.', got: {block_texts[1]!r}"
    )


def test_w6_defect_f_indented_continuation_still_joins() -> None:
    """An indented continuation line after a list item must still be joined into
    the list_item block (CommonMark indented continuation is accepted here).

    Design: lines with one or more leading spaces/tabs are treated as list
    continuation; flush-left lines are not.
    """
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from normalize.md_adapter import parse_text

    doc = parse_text("- Item\n  indented continuation\n")
    assert len(doc.blocks) == 1, (
        f"Expected 1 block (list_item with continuation), got {len(doc.blocks)}: "
        f"{[(b.block_type, b.text) for b in doc.blocks]}"
    )
    assert doc.blocks[0].block_type == "list_item", (
        f"Block must be list_item, got: {doc.blocks[0].block_type!r}"
    )
    assert "continuation" in doc.blocks[0].text, (
        f"Indented continuation must be joined; text: {doc.blocks[0].text!r}"
    )


def test_w6_defect_f_fenced_code_not_joined_into_paragraph() -> None:
    """Fenced code blocks (``` fences) must not be joined into surrounding paragraphs.

    Design choice: fence-open and fence-close lines are treated as block
    boundaries; the fence content is consumed as a 'code_fence' block (or at
    minimum the fence lines break any surrounding paragraph join).  The
    paragraph before the fence and the paragraph after must be emitted as
    separate blocks; fence content must not appear inside a paragraph block.
    """
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from normalize.md_adapter import parse_text

    doc = parse_text("Para.\n```\nx=1\n```\n\nAfter.\n")
    block_types = [b.block_type for b in doc.blocks]
    block_texts = [b.text for b in doc.blocks]

    # 1. No paragraph block may contain backtick fence markers.
    para_blocks_with_fence = [
        (bt, txt) for bt, txt in zip(block_types, block_texts)
        if bt == "paragraph" and "```" in txt
    ]
    assert not para_blocks_with_fence, (
        f"Paragraph blocks must not contain fence markers; got: {para_blocks_with_fence}"
    )

    # 2. The paragraph 'Para.' and paragraph 'After.' must both be present.
    para_texts = [txt for bt, txt in zip(block_types, block_texts) if bt == "paragraph"]
    assert any("Para." in t for t in para_texts), (
        f"'Para.' paragraph must be emitted; paragraph blocks: {para_texts}"
    )
    assert any("After." in t for t in para_texts), (
        f"'After.' paragraph must be emitted; paragraph blocks: {para_texts}"
    )

    # 3. No paragraph block may contain the fence content 'x=1'.
    para_with_content = [t for t in para_texts if "x=1" in t]
    assert not para_with_content, (
        f"Fence content 'x=1' must not appear in a paragraph block; got: {para_with_content}"
    )


if __name__ == "__main__":
    import inspect
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_") and callable(value)]
    for test in tests:
        if "tmp_path" in inspect.signature(test).parameters:
            with tempfile.TemporaryDirectory() as _d:
                test(Path(_d))
        else:
            test()
    print(f"{len(tests)} tests passed")
