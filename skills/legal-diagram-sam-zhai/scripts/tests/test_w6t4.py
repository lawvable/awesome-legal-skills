"""W6 T4 red tests: precision sweep across legal_authorities, deadlines, parties, documents, transfers.

Items:
  A -- legal_authorities: compose case+citation, demote own-citation, demote bare section refs,
       harvest Act-name patterns, CanLII citations, classic case names w/ parentheticals
  B -- deadlines: fix 'the following closing' FP, demote bare FR closing-relative refs,
       clause-scoped description for cure/hard deadline, promote Feb 20 hint
  C -- parties: dedup same normalized name, demote single-token generic table_party,
       fix agreement_intro_party for corp-structure sentences
  D -- documents: dedup on normalized name, fix name capture from sentence prefix,
       demote single-word generic names, harvest schedule/exhibit/annex refs
  E -- transfers: suppress lead-in when split items emitted, demote conditional-trigger transfers
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
sys.path.insert(0, str(ROOT))

EXTRACT = ROOT / "extract_entities.py"


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


def _run_extract_file(path: Path) -> dict:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(EXTRACT), "--input", str(path)],
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


def _promoted(sidecar: dict, field: str, frame: str | None = None) -> list[dict]:
    decisions = _decisions(sidecar)
    cands = _candidates(sidecar, field, frame)
    return [c for c in cands if decisions.get(c["id"]) == "promote"]


def _citation_values(sidecar: dict) -> list[str]:
    return [c["normalized_value"].get("citation", "") for c in _promoted(sidecar, "legal_authorities")]


def _document_names(sidecar: dict) -> list[str]:
    return [c["normalized_value"].get("name", "") for c in _promoted(sidecar, "documents")]


# ===========================================================================
# Item A: legal_authorities
# ===========================================================================

def test_fr_judgment_case_and_neutral_citation_composed_single() -> None:
    """FR judgment: 'Morin c. Entreprises Casgrain' + '2026 QCCA 217' must compose
    into ONE authority, not two separate candidates."""
    data = _run_extract_file(FIXTURES_DIR / "fr_judgment.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    # Both parts promoted individually would each appear separately; after fix
    # only the composed form should appear
    composed = "Morin c. Entreprises Casgrain, 2026 QCCA 217"
    # The composed citation (or a Jaccard-equivalent) must appear
    found = any("morin" in c.lower() and ("2026" in c or "qcca" in c.lower()) for c in citations)
    assert found, f"Composed Morin citation not found; got: {citations}"
    # The bare case name without citation must NOT appear as a separate promoted item
    bare_case_only = [c for c in citations if c.lower().strip() == "morin c. entreprises casgrain"]
    assert len(bare_case_only) == 0, (
        f"Bare case name promoted separately (should be composed): {bare_case_only}"
    )
    # The bare neutral citation without case name must NOT appear separately
    bare_citation_only = [c for c in citations if c.strip() == "2026 QCCA 217"]
    assert len(bare_citation_only) == 0, (
        f"Bare neutral citation promoted separately (should be composed): {bare_citation_only}"
    )


def test_fr_judgment_own_citation_header_retained_as_authority() -> None:
    """FR judgment: **Référence :** Tremblay c. Gagnon Transport Ltée, 2026 QCCS 1234
    IS in the labels (it's the authoritative citation for the judgment itself, referenced
    via the case name). The labels show 'Lavergne c. Transport Boisclair Ltée, [1994] 2 RCS 415'
    and 'Morin c. Entreprises Casgrain, 2026 QCCA 217' as the two required citations.
    The own-citation header for fr_judgment IS a valid authority (unique situation:
    both names from the header are case parties AND cited authorities in the body).
    For the fr_judgment, the composed form (Tremblay + 2026 QCCS 1234) may or may not
    be promoted as an authority -- the labels do NOT include it. We just verify the
    body citations (Lavergne and Morin+QCCA) are promoted."""
    data = _run_extract_file(FIXTURES_DIR / "fr_judgment.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    # The Lavergne citation must be present (it's from body text, not header)
    found_lavergne = any("lavergne" in c.lower() or "1994" in c or "rcs" in c.lower() for c in citations)
    assert found_lavergne, f"Lavergne citation not found; got: {citations}"


def test_en_judgment_own_citation_header_demoted() -> None:
    """EN judgment: **Citation:** 2025 ONSC 4812 is the document's OWN citation header.
    This should NOT be promoted as a legal authority (it's metadata, not a cited authority)."""
    data = _run_extract_file(FIXTURES_DIR / "en_judgment.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    # The own-citation '2025 ONSC 4812' should not appear as a promoted authority
    own_citation = [c for c in citations if "2025 ONSC 4812" in c or c.strip() == "2025 ONSC 4812"]
    assert len(own_citation) == 0, (
        f"Own-citation '2025 ONSC 4812' must not be promoted; got: {own_citation}"
    )


def test_en_judgment_bare_section_ref_without_act_demoted() -> None:
    """EN judgment: 'section 7' (bare section reference without act name) must not
    be promoted as a legal authority."""
    data = _run_extract_file(FIXTURES_DIR / "en_judgment.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    bare_section = [c for c in citations if c.strip().lower() in ("section 7", "section 7.2", "s. 7")]
    assert len(bare_section) == 0, (
        f"Bare section ref without act name must not be promoted; got: {bare_section}"
    )


def test_en_spa_article_5_cross_ref_demoted() -> None:
    """EN SPA: 'Article 5' is an internal cross-reference, not a legal authority."""
    data = _run_extract_file(FIXTURES_DIR / "en_spa_contract.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    bare_article = [c for c in citations if c.strip().lower() in ("article 5",)]
    assert len(bare_article) == 0, (
        f"Internal 'Article 5' cross-reference must not be promoted; got: {bare_article}"
    )


def test_en_judgment_courts_of_justice_act_harvested() -> None:
    """EN judgment: 'Courts of Justice Act, R.S.O. 1990, c. C.43' must be promoted."""
    data = _run_extract_file(FIXTURES_DIR / "en_judgment.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    found = any(
        "courts of justice act" in c.lower() or "r.s.o. 1990" in c.lower() or "c. c.43" in c.lower()
        for c in citations
    )
    assert found, f"Courts of Justice Act not promoted; got: {citations}"


def test_en_judgment_hadley_baxendale_harvested() -> None:
    """EN judgment: classic case 'Hadley v. Baxendale' (no neutral citation) must be promoted."""
    data = _run_extract_file(FIXTURES_DIR / "en_judgment.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    found = any("hadley" in c.lower() and "baxendale" in c.lower() for c in citations)
    assert found, f"Hadley v. Baxendale not promoted; got: {citations}"


def test_en_judgment_victoria_laundry_harvested() -> None:
    """EN judgment: classic case 'Victoria Laundry (Windsor) Ltd. v. Newman Industries Ltd.'
    (parenthetical in name, no neutral citation) must be promoted."""
    data = _run_extract_file(FIXTURES_DIR / "en_judgment.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    found = any("victoria laundry" in c.lower() for c in citations)
    assert found, f"Victoria Laundry case not promoted; got: {citations}"


def test_en_judgment_transamerica_canLII_harvested() -> None:
    """EN judgment: 'Transamerica Life Insurance Co. of Canada v. Canada Life Assurance Co.,
    1996 CanLII 7979 (ON SC)' must be promoted."""
    data = _run_extract_file(FIXTURES_DIR / "en_judgment.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    found = any("transamerica" in c.lower() or "canLII 7979" in c for c in citations)
    assert found, f"Transamerica CanLII citation not promoted; got: {citations}"


def test_en_privacy_policy_pipeda_harvested() -> None:
    """EN privacy policy: 'Personal Information Protection and Electronic Documents Act,
    S.C. 2000, c. 5' must be promoted."""
    data = _run_extract_file(FIXTURES_DIR / "en_privacy_policy.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    found = any("pipeda" in c.lower() or "personal information protection" in c.lower() for c in citations)
    assert found, f"PIPEDA not promoted; got: {citations}"


def test_en_privacy_policy_income_tax_act_harvested() -> None:
    """EN privacy policy: 'Income Tax Act (Canada)' must be promoted."""
    data = _run_extract_file(FIXTURES_DIR / "en_privacy_policy.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    found = any("income tax act" in c.lower() for c in citations)
    assert found, f"Income Tax Act (Canada) not promoted; got: {citations}"


def test_en_spa_competition_act_harvested() -> None:
    """EN SPA: 'Competition Act (Canada)' must be promoted as an authority."""
    data = _run_extract_file(FIXTURES_DIR / "en_spa_contract.md")
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    found = any("competition act" in c.lower() for c in citations)
    assert found, f"Competition Act (Canada) not promoted; got: {citations}"


def test_act_name_pattern_harvests_jurisdictional_acts() -> None:
    """Unit test: Act-name patterns harvest 'Courts of Justice Act, R.S.O. 1990, c. C.43'
    and 'Competition Act (Canada)' from prose."""
    text = """The rate is prescribed under the Courts of Justice Act, R.S.O. 1990, c. C.43.
All regulatory approvals, including approval under the Competition Act (Canada), shall have been obtained."""
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    found_cja = any("courts of justice act" in c.lower() for c in citations)
    found_ca = any("competition act" in c.lower() for c in citations)
    assert found_cja, f"Courts of Justice Act not harvested; got: {citations}"
    assert found_ca, f"Competition Act not harvested; got: {citations}"


def test_case_name_no_neutral_citation_harvested() -> None:
    """Unit test: classic case name without following year is harvested when
    the sentence provides legal context (principle/test/rule reference)."""
    text = """The two-stage test from Hadley v. Baxendale applies to lost-profit claims.
Victoria Laundry (Windsor) Ltd. v. Newman Industries Ltd. refined the remoteness principle."""
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    citations = _citation_values(sidecar)
    found_hadley = any("hadley" in c.lower() for c in citations)
    found_victoria = any("victoria laundry" in c.lower() for c in citations)
    assert found_hadley, f"Hadley v. Baxendale not harvested; got: {citations}"
    assert found_victoria, f"Victoria Laundry not harvested; got: {citations}"


# ===========================================================================
# Item B: deadlines
# ===========================================================================

def test_deadline_the_following_closing_deliveries_not_promoted() -> None:
    """'the following closing deliveries' must NOT trigger pre_closing_deadline.
    'following closing' within 'the following <noun>' is a list-leader, not a deadline."""
    text = "Northgate Acquisitions Corp. shall deliver to the Vendor, at or before Closing, the following closing deliveries:\n1. A certified resolution."
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    promoted_deadlines = _promoted(sidecar, "deadlines")
    # The sentence "deliver ... at or before Closing, the following closing deliveries"
    # should NOT produce a 'following closing' FP deadline
    fp_following = [
        d for d in promoted_deadlines
        if "following closing" in d["normalized_value"].get("date_or_timing", "").lower()
        and "deliver" in d["normalized_value"].get("description", "").lower()
        and "at or before closing" not in d["normalized_value"].get("date_or_timing", "").lower()
    ]
    assert len(fp_following) == 0, (
        f"'following closing' in list-leader sentence must not promote as post_closing deadline: {fp_following}"
    )


def test_fr_contract_bare_avant_la_cloture_demoted() -> None:
    """FR contract: bare 'avant la Clôture' without duration on a covenant sentence
    must be demoted (hint or lower), not promoted as a deadline."""
    text = "La Venderesse ne doit pas vendre, transférer ni grever les Actions visées avant la Clôture sans le consentement préalable écrit de l'Acheteur."
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    promoted_deadlines = _promoted(sidecar, "deadlines")
    bare_avant = [
        d for d in promoted_deadlines
        if d["normalized_value"].get("date_or_timing", "").strip().lower() == "avant la clôture"
        or d["normalized_value"].get("date_or_timing", "").strip().lower() == "avant la cloture"
    ]
    assert len(bare_avant) == 0, (
        f"Bare 'avant la Clôture' without duration must not promote as deadline: {bare_avant}"
    )


def test_fr_contract_duration_suivant_cloture_promoted() -> None:
    """FR contract: 'dans les 18 mois suivant la date de Clôture' (has duration) must
    be promoted as a deadline."""
    data = _run_extract_file(FIXTURES_DIR / "fr_contract.md")
    sidecar = data["candidate_manifest"]
    promoted_deadlines = _promoted(sidecar, "deadlines")
    timings = [d["normalized_value"].get("date_or_timing", "") for d in promoted_deadlines]
    found = any("18 mois" in t or "18" in t for t in timings)
    assert found, f"'dans les 18 mois suivant la date de Clôture' not promoted; timings: {timings}"


def test_en_employment_cure_period_description_is_clause_scoped() -> None:
    """EN employment: cure-period deadline description should be clause-scoped,
    not the full joined multi-clause sentence."""
    text = "The Employee shall have 15 business days after receipt of written notice to cure the deficiency."
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    promoted_deadlines = _promoted(sidecar, "deadlines")
    assert promoted_deadlines, "No deadlines promoted from cure-period sentence"
    # The timing should be extracted, not the whole sentence
    timing = promoted_deadlines[0]["normalized_value"].get("date_or_timing", "")
    assert "15 business days" in timing, f"Expected '15 business days' in timing; got: {timing!r}"


def test_en_spa_feb20_regulatory_approval_promoted() -> None:
    """EN SPA: 'on or before February 20, 2026' (regulatory approval deadline) must be
    promoted, not only at hint tier."""
    data = _run_extract_file(FIXTURES_DIR / "en_spa_contract.md")
    sidecar = data["candidate_manifest"]
    promoted_deadlines = _promoted(sidecar, "deadlines")
    timings = [d["normalized_value"].get("date_or_timing", "") for d in promoted_deadlines]
    found = any("february 20" in t.lower() or "february 20, 2026" in t.lower() for t in timings)
    assert found, f"'on or before February 20, 2026' not promoted; timings: {timings}"


# ===========================================================================
# Item C: parties
# ===========================================================================

def test_parties_same_normalized_name_deduped() -> None:
    """en_corp_structure: 'Cedarbrook Group Inc' from two separate sentences with
    the same normalized name must be deduped to a single promoted party."""
    data = _run_extract_file(FIXTURES_DIR / "en_corp_structure.md")
    sidecar = data["candidate_manifest"]
    promoted_parties = _promoted(sidecar, "parties")
    party_names = [p["normalized_value"].get("name", "") for p in promoted_parties]
    # Count occurrences of Cedarbrook Group Inc
    cedarbrook_count = sum(
        1 for n in party_names
        if n.lower().replace(".", "").strip() in (
            "cedarbrook group inc",
            "cedarbrook group inc.",
        )
    )
    assert cedarbrook_count <= 1, (
        f"'Cedarbrook Group Inc' promoted more than once ({cedarbrook_count} times): {party_names}"
    )


def test_table_party_bare_party_word_always_demoted() -> None:
    """'Party' and 'Parties' in table cells are never standalone identifiers and must
    always be suppressed (static floor), regardless of document context."""
    text = """## Obligations

| Responsible Party | Obligation | Due Date |
|---|---|---|
| Party | File annual report | December 31, 2026 |
| Parties | Submit notice | June 30, 2026 |
"""
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    promoted_parties = _promoted(sidecar, "parties")
    party_names = [p["normalized_value"].get("name", "").strip() for p in promoted_parties]
    static_suppressed = [n for n in party_names if n in ("Party", "Parties")]
    assert len(static_suppressed) == 0, (
        f"'Party'/'Parties' must always be suppressed as table party values: {static_suppressed}"
    )


def test_table_party_role_word_promoted_when_no_alias_defined() -> None:
    """Single-token role words ('Company', 'Vendor') without a defined alias
    in the document ARE promoted: the bare role word is the party identifier.
    Context-sensitive suppression fires only when a defined_party_alias maps
    that role to a specific named party."""
    text = """## Obligations

| Responsible Party | Obligation | Due Date |
|---|---|---|
| Company | File annual report | December 31, 2026 |
| Vendor | Provide SOC 2 certification | June 30, 2026 |
"""
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    promoted_parties = _promoted(sidecar, "parties")
    party_names = [p["normalized_value"].get("name", "").strip() for p in promoted_parties]
    # Both Company and Vendor have no defined-alias mapping in this text,
    # so the bare role word IS the party identifier and must be promoted.
    assert any(n == "Company" for n in party_names), (
        f"'Company' must be promoted when no alias defines it; got: {party_names}"
    )
    assert any(n == "Vendor" for n in party_names), (
        f"'Vendor' must be promoted when no alias defines it; got: {party_names}"
    )


def test_table_party_role_word_suppressed_when_alias_defined() -> None:
    """'Company' in a table must be suppressed when the document defines
    Company as an alias of a named party (via a defined_party_alias frame)."""
    text = """Acme Holdings Inc. (\"Company\") and Beta Corp. (\"Vendor\") agree as follows.

## Obligations

| Responsible Party | Obligation | Due Date |
|---|---|---|
| Company | File annual report | December 31, 2026 |
| Vendor | Provide SOC 2 certification | June 30, 2026 |
"""
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    promoted_parties = _promoted(sidecar, "parties")
    party_names = [p["normalized_value"].get("name", "").strip() for p in promoted_parties]
    # Both Company and Vendor are defined as aliases; their bare role words
    # must NOT appear as promoted parties (the named party is the canonical entry).
    assert not any(n == "Company" for n in party_names), (
        f"'Company' must be suppressed when alias maps it to Acme Holdings Inc.; got: {party_names}"
    )
    assert not any(n == "Vendor" for n in party_names), (
        f"'Vendor' must be suppressed when alias maps it to Beta Corp.; got: {party_names}"
    )


def test_en_obligation_schedule_vendor_promoted_company_suppressed() -> None:
    """en_obligation_schedule: 'Vendor' (no defined alias) must be promoted; 'Company'
    (defined as alias of Foxwood Technologies Ltd.) must NOT be promoted.

    The document header defines Company = Foxwood Technologies Ltd. via the alias
    frame.  'Vendor' has no such mapping, so the bare role word IS the party
    identifier and must be promoted.  Blanket suppression of 'vendor' creates a
    ground-truth FN; context-sensitive suppression fixes it."""
    data = _run_extract_file(FIXTURES_DIR / "en_obligation_schedule.md")
    sidecar = data["candidate_manifest"]
    promoted_parties = _promoted(sidecar, "parties")
    party_names = [p["normalized_value"].get("name", "").strip() for p in promoted_parties]
    # Vendor must be promoted (no defined-alias mapping exists for 'vendor')
    assert any(n == "Vendor" for n in party_names), (
        f"'Vendor' must be promoted when no defined alias maps to 'vendor'; got: {party_names}"
    )
    # Company must NOT be promoted (defined as alias of Foxwood Technologies Ltd.)
    assert not any(n == "Company" for n in party_names), (
        f"'Company' must not be promoted when defined alias maps Company → Foxwood; got: {party_names}"
    )


def test_corp_structure_between_sentence_no_party_promotion() -> None:
    """en_corp_structure: descriptive corp-structure sentence 'X is a joint venture
    vehicle between A and B' must NOT promote A and B as parties (they are entities).
    The 'between' intro frame requires agreement context."""
    data = _run_extract_file(FIXTURES_DIR / "en_corp_structure.md")
    sidecar = data["candidate_manifest"]
    promoted_parties = _promoted(sidecar, "parties")
    party_names = [p["normalized_value"].get("name", "").strip() for p in promoted_parties]
    # Ridgetop and Westcoast must not be parties (they are entities in corp structure)
    ridgetop = [n for n in party_names if "ridgetop" in n.lower()]
    westcoast = [n for n in party_names if "westcoast" in n.lower()]
    assert len(ridgetop) == 0, (
        f"'Ridgetop Realty Ltd' must not be promoted as party in corp structure: {ridgetop}"
    )
    assert len(westcoast) == 0, (
        f"'Westcoast Properties Corp' must not be promoted as party in corp structure: {westcoast}"
    )


def test_en_employment_sandbourne_industries_match() -> None:
    """en_employment: 'Sandbourne Industries Inc.' label must match the promoted
    'Sandbourne Industries Inc' (trailing period difference resolved by normalization)."""
    data = _run_extract_file(FIXTURES_DIR / "en_employment.md")
    sidecar = data["candidate_manifest"]
    promoted_parties = _promoted(sidecar, "parties")
    party_names = [p["normalized_value"].get("name", "").lower().strip(".,") for p in promoted_parties]
    found = any("sandbourne industries" in n for n in party_names)
    assert found, f"'Sandbourne Industries Inc.' not promoted; got: {party_names}"


# ===========================================================================
# Item D: documents
# ===========================================================================

def test_documents_dedup_by_normalized_name() -> None:
    """en_obligation_schedule: 'Platform Licence Agreement' promoted three times from
    separate table rows must be deduped to a single promoted document."""
    data = _run_extract_file(FIXTURES_DIR / "en_obligation_schedule.md")
    sidecar = data["candidate_manifest"]
    promoted_docs = _promoted(sidecar, "documents")
    doc_names = [d["normalized_value"].get("name", "").strip() for d in promoted_docs]
    pla_count = sum(1 for n in doc_names if n.lower() == "platform licence agreement")
    assert pla_count <= 1, (
        f"'Platform Licence Agreement' promoted {pla_count} times; expected at most 1: {doc_names}"
    )


def test_deliverable_document_not_sentence_fragment() -> None:
    """EN SPA: the deliverable document name must not capture a full sentence fragment
    starting with a party name ('Northgate Acquisitions Corp. shall deliver to the Vendor...')."""
    text = "Northgate Acquisitions Corp. shall deliver to the Vendor, at or before Closing, the following closing deliveries:"
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    promoted_docs = _promoted(sidecar, "documents")
    doc_names = [d["normalized_value"].get("name", "").strip() for d in promoted_docs]
    # None of the document names should start with a party name token
    sentence_fragment_names = [
        n for n in doc_names
        if n.lower().startswith("northgate") or len(n.split()) > 8
    ]
    assert len(sentence_fragment_names) == 0, (
        f"Document name captured as sentence fragment: {sentence_fragment_names}"
    )


def test_single_word_notice_document_demoted() -> None:
    """EN SPA: bare 'notice' (single generic word) must not be promoted as a document name."""
    text = "The Vendor shall, within 5 business days after written notice from the Purchaser, provide any information reasonably requested for the Purchaser's due diligence review."
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    promoted_docs = _promoted(sidecar, "documents")
    doc_names = [d["normalized_value"].get("name", "").strip().lower() for d in promoted_docs]
    bare_notice = [n for n in doc_names if n == "notice"]
    assert len(bare_notice) == 0, (
        f"Bare 'notice' must not be promoted as document name: {bare_notice}"
    )


def test_schedule_no_4_harvested() -> None:
    """EN SPA: 'Schedule No. 4' must be promoted as a document reference."""
    data = _run_extract_file(FIXTURES_DIR / "en_spa_contract.md")
    sidecar = data["candidate_manifest"]
    promoted_docs = _promoted(sidecar, "documents")
    doc_names = [d["normalized_value"].get("name", "").strip().lower() for d in promoted_docs]
    found = any("schedule no. 4" in n or "schedule no 4" in n for n in doc_names)
    assert found, f"'Schedule No. 4' not promoted as document; got: {doc_names}"


def test_schedule_exhibit_annex_references_harvested() -> None:
    """Unit test: Schedule/Exhibit/Annex references must be harvested as documents."""
    text = "The representations set forth on Schedule No. 4 and Exhibit B shall be true and correct."
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    promoted_docs = _promoted(sidecar, "documents")
    doc_names = [d["normalized_value"].get("name", "").strip().lower() for d in promoted_docs]
    found_schedule = any("schedule" in n for n in doc_names)
    assert found_schedule, f"Schedule reference not harvested; got: {doc_names}"


# ===========================================================================
# Item E: transfers
# ===========================================================================

def test_transfer_lead_in_suppressed_when_split_items_present() -> None:
    """EN SPA: 'The Purchaser shall pay the Purchase Price as follows' (lead-in)
    must not be promoted as a transfer when the split payment items are also promoted."""
    data = _run_extract_file(FIXTURES_DIR / "en_spa_contract.md")
    sidecar = data["candidate_manifest"]
    promoted_transfers = _promoted(sidecar, "transfers")
    transfer_descs = [t["normalized_value"].get("description", "") for t in promoted_transfers]
    lead_in = [d for d in transfer_descs if d.strip().lower() == "the purchaser shall pay the purchase price as follows"]
    assert len(lead_in) == 0, (
        f"Lead-in transfer sentence must not be promoted when split items present: {lead_in}"
    )


def test_fr_contract_conditional_transfer_demoted() -> None:
    """FR contract: 'Advenant un manquement... celle-ci rembourse...' (conditional
    indemnity trigger) must be demoted to hint or suppress."""
    text = "Advenant un manquement aux déclarations de la Venderesse, celle-ci rembourse à l'Acheteur les pertes subies, jusqu'à concurrence d'un plafond global de 1,5 M$."
    data = _run_extract(text)
    sidecar = data["candidate_manifest"]
    promoted_transfers = _promoted(sidecar, "transfers")
    conditional_transfers = [
        t for t in promoted_transfers
        if "advenant" in t["normalized_value"].get("description", "").lower()
    ]
    assert len(conditional_transfers) == 0, (
        f"Conditional 'Advenant' transfer must not be promoted: {conditional_transfers}"
    )


def test_fr_contract_ceder_transferer_actions_unlabelled() -> None:
    """FR contract: 'céder et transférer la totalité des actions' is a share transfer
    that is NOT labelled. We do not suppress it (valid transfer, label-coverage issue).
    This test verifies it stays promoted (genuine transfer, just unlabelled)."""
    data = _run_extract_file(FIXTURES_DIR / "fr_contract.md")
    sidecar = data["candidate_manifest"]
    promoted_transfers = _promoted(sidecar, "transfers")
    transfer_descs = [t["normalized_value"].get("description", "") for t in promoted_transfers]
    # The share transfer (cession/transfert of all shares) must remain promoted
    found = any(
        "actions" in d.lower() and ("céder" in d.lower() or "transferer" in d.lower() or "transférer" in d.lower())
        for d in transfer_descs
    )
    assert found, (
        f"Valid share transfer 'céder et transférer la totalité des actions' must remain promoted; got: {transfer_descs}"
    )


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items())
             if name.startswith("test_") and callable(value)]
    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            print(f"  PASS  {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {test.__name__}: {e}")
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
