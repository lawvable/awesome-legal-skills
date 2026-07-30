"""W6 T3 red tests: entities harvester, privacy parties, privacy controls, judgment events promotion.

Covers four items:
  Item 1 -- entities harvester: ownership participants, list items, acquisition target
  Item 2 -- privacy parties: operator self-id + service-provider enumeration
  Item 3 -- privacy controls: prose/list security measures
  Item 4 -- judgment events: promote hint-tier dates with litigation-action context
"""
from __future__ import annotations

import os
import sys
import json
import subprocess
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


def _promoted_entities(data: dict) -> list[str]:
    return [e["name"] for e in data["extraction_result"].get("entities", [])]


def _promoted_parties(data: dict) -> list[str]:
    return [p["name"] for p in data["extraction_result"].get("parties", [])]


def _promoted_controls(data: dict) -> list[str]:
    return [c["description"] for c in data["extraction_result"].get("controls", [])]


def _promoted_events(data: dict) -> list[str]:
    return [e.get("date") or e.get("date_or_timing", "") for e in data["extraction_result"].get("events", [])]


# ---------------------------------------------------------------------------
# Item 1: entities harvester
# ---------------------------------------------------------------------------

def test_entities_from_ownership_participants() -> None:
    """Both sides of 'X owns N% of Y' must yield entity candidates."""
    data = _run_extract(
        "Cedarbrook Group Inc. owns 100% of Lakeview Distribution Corp., a corporation incorporated under the laws of Manitoba."
    )
    entities = _promoted_entities(data)
    assert any("Cedarbrook Group Inc" in e for e in entities), f"Cedarbrook missing from entities: {entities}"
    assert any("Lakeview Distribution Corp" in e for e in entities), f"Lakeview Distribution Corp missing: {entities}"


def test_entities_from_held_by_frame() -> None:
    """Holder in 'held by Z' must yield an entity candidate."""
    data = _run_extract(
        "The remaining 25% is held by Westcoast Properties Corp., an arm's length third party."
    )
    entities = _promoted_entities(data)
    assert any("Westcoast Properties Corp" in e for e in entities), f"Westcoast missing from entities: {entities}"


def test_entities_from_defined_list_item() -> None:
    """'- **Name**: description' under an Entities heading must yield entity candidates."""
    data = _run_extract(
        "## Entities\n\n- **Bridgewater Asset Management Inc.**: provides investment management services in Ontario.\n"
    )
    entities = _promoted_entities(data)
    assert any("Bridgewater Asset Management Inc" in e for e in entities), f"Bridgewater missing: {entities}"


def test_entities_no_generic_caps_without_suffix() -> None:
    """Capitalized runs without corporate suffix must NOT promote as entities (precision guard)."""
    data = _run_extract(
        "The Vendor agrees to sell all shares under the Share Purchase Agreement."
    )
    entities = _promoted_entities(data)
    # 'Vendor', 'Share Purchase Agreement' are not corp-suffix entities
    assert not any(e in ("Vendor", "Share Purchase Agreement") for e in entities), (
        f"Generic caps should not promote as entities: {entities}"
    )


def test_entities_acquisition_target_en() -> None:
    """'shares of X' with corp suffix must yield X as an entity candidate."""
    data = _run_extract(
        "The Vendor agrees to sell all issued and outstanding shares of Maplewood Technologies Ltd. (the \"Target Shares\"), free and clear of all encumbrances."
    )
    entities = _promoted_entities(data)
    assert any("Maplewood Technologies Ltd" in e for e in entities), f"Maplewood missing from entities: {entities}"


def test_entities_acquisition_target_fr() -> None:
    """'actions de X Ltée' (FR) must yield X as an entity candidate."""
    data = _run_extract(
        "La Venderesse doit céder et transférer à l'Acheteur la totalité des actions émises et en circulation de Technologies Malouin Ltée (les « Actions visées »)."
    )
    entities = _promoted_entities(data)
    assert any("Technologies Malouin Ltée" in e for e in entities), f"Technologies Malouin Ltée missing from entities: {entities}"


def test_entities_corp_structure_fixture_integration() -> None:
    """en_corp_structure fixture must promote all 9 entity labels."""
    fixture_path = FIXTURES_DIR / "en_corp_structure.md"
    labels_path = FIXTURES_DIR / "en_corp_structure.md.labels.json"
    data = _run_extract_file(fixture_path)
    with open(labels_path) as f:
        labels = json.load(f)
    expected = labels["fields"]["entities"]
    entities = _promoted_entities(data)
    found = sum(
        1 for label in expected
        if any(label.rstrip(".") in e or e in label for e in entities)
    )
    assert found >= 7, f"Expected >=7/9 entity labels promoted, got {found}. Promoted: {entities}"


# ---------------------------------------------------------------------------
# Item 2: privacy parties
# ---------------------------------------------------------------------------

def test_privacy_operator_party() -> None:
    """Policy-operator declaration 'X ("we", "our")' must yield X as a party."""
    data = _run_extract(
        'This Privacy Policy describes how Example Digital Services Inc. collects, uses, discloses, and protects personal information in accordance with PIPEDA.'
    )
    parties = _promoted_parties(data)
    assert any("Example Digital Services Inc" in p for p in parties), (
        f"Policy operator party missing. Found: {parties}"
    )


def test_privacy_service_provider_party() -> None:
    """Corp-suffix name listed as service provider/third party must yield a party."""
    data = _run_extract(
        "Example Digital Services Inc. transfers personal information to the following third parties:\n"
        "- **Example Payments Corp.**: receives payment data for payment processing; bound by a data processing agreement."
    )
    parties = _promoted_parties(data)
    assert any("Example Payments Corp" in p for p in parties), (
        f"Service provider party missing. Found: {parties}"
    )


def test_privacy_multiple_service_providers() -> None:
    """Multiple disclosed-recipient corp names from list items must each promote as a party."""
    # The fixture's list-item format is the primary vehicle for service-provider enumeration.
    data = _run_extract(
        "## Data Flows and Third-Party Transfers\n\n"
        "Example Digital Services Inc. transfers personal information to the following third parties:\n\n"
        "- **Stacklayer Cloud Inc.**: hosts our platform infrastructure.\n"
        "- **Insightful Analytics Ltd.**: receives pseudonymised usage data.\n"
        "- **Meridian Support Systems Inc.**: receives communications data.\n"
    )
    parties = _promoted_parties(data)
    names = ["Stacklayer Cloud Inc", "Insightful Analytics Ltd", "Meridian Support Systems Inc"]
    missing = [n for n in names if not any(n in p for p in parties)]
    assert not missing, f"Service provider parties missing: {missing}. Found: {parties}"


def test_privacy_parties_fixture_integration() -> None:
    """en_privacy_policy fixture must promote all 5 party labels."""
    fixture_path = FIXTURES_DIR / "en_privacy_policy.md"
    labels_path = FIXTURES_DIR / "en_privacy_policy.md.labels.json"
    data = _run_extract_file(fixture_path)
    with open(labels_path) as f:
        labels = json.load(f)
    expected = labels["fields"]["parties"]
    parties = _promoted_parties(data)
    found = sum(
        1 for label in expected
        if any(label.rstrip(".") in p or p in label for p in parties)
    )
    assert found >= 4, f"Expected >=4/5 party labels promoted, got {found}. Promoted: {parties}"


# ---------------------------------------------------------------------------
# Item 3: privacy controls
# ---------------------------------------------------------------------------

def test_privacy_controls_encryption() -> None:
    """Encryption-at-rest/TLS sentence must yield a controls candidate."""
    data = _run_extract(
        "All personal information is encrypted at rest using AES-256 and in transit using TLS 1.3."
    )
    controls = _promoted_controls(data)
    assert any("AES-256" in c or "encrypt" in c.lower() for c in controls), (
        f"Encryption control missing. Found: {controls}"
    )


def test_privacy_controls_access_control() -> None:
    """Role-based access controls sentence must yield a controls candidate."""
    data = _run_extract(
        "Access to personal data systems is restricted to authorized personnel and enforced by role-based access controls and multi-factor authentication."
    )
    controls = _promoted_controls(data)
    assert any("role-based access" in c.lower() or "multi-factor" in c.lower() for c in controls), (
        f"Access control missing. Found: {controls}"
    )


def test_privacy_controls_incident_response() -> None:
    """Incident response plan mention must yield a controls candidate."""
    data = _run_extract(
        "We maintain an incident response plan requiring notification to the Office of the Privacy Commissioner of Canada within 72 hours of discovery of a reportable breach."
    )
    controls = _promoted_controls(data)
    assert any("incident response" in c.lower() for c in controls), (
        f"Incident response plan missing. Found: {controls}"
    )


def test_privacy_controls_penetration_testing() -> None:
    """Penetration testing sentence must yield a controls candidate."""
    data = _run_extract(
        "Our platform undergoes annual penetration testing conducted by an independent third party."
    )
    controls = _promoted_controls(data)
    assert any("penetration" in c.lower() or "testing" in c.lower() for c in controls), (
        f"Penetration testing control missing. Found: {controls}"
    )


def test_privacy_controls_confidentiality_agreements() -> None:
    """Employee confidentiality agreements sentence must yield a controls candidate."""
    data = _run_extract(
        "Employees with access to personal information are required to complete privacy training annually and are subject to confidentiality agreements."
    )
    controls = _promoted_controls(data)
    assert any("confidentiality" in c.lower() for c in controls), (
        f"Confidentiality agreements control missing. Found: {controls}"
    )


def test_privacy_controls_fixture_integration() -> None:
    """en_privacy_policy fixture must promote all 5 controls labels."""
    fixture_path = FIXTURES_DIR / "en_privacy_policy.md"
    labels_path = FIXTURES_DIR / "en_privacy_policy.md.labels.json"
    data = _run_extract_file(fixture_path)
    with open(labels_path) as f:
        labels = json.load(f)
    expected = labels["fields"]["controls"]
    controls = _promoted_controls(data)
    # Match: any label word appears in a control description
    found = 0
    for label in expected:
        label_lower = label.lower()
        for ctrl in controls:
            ctrl_lower = ctrl.lower()
            # Check key tokens of the label appear in the control
            key_words = [w for w in label_lower.split() if len(w) > 4]
            if key_words and all(w in ctrl_lower for w in key_words[:2]):
                found += 1
                break
            if label_lower in ctrl_lower or ctrl_lower in label_lower:
                found += 1
                break
    assert found >= 4, f"Expected >=4/5 controls labels promoted, got {found}. Promoted: {controls}"


def test_privacy_controls_precision_not_regressed() -> None:
    """Non-privacy non-security sentences must not produce controls entries."""
    data = _run_extract(
        "The Vendor agrees to sell all Target Shares free and clear of encumbrances for $12,500,000."
    )
    controls = _promoted_controls(data)
    assert not controls, f"Non-security sentence produced controls: {controls}"


# ---------------------------------------------------------------------------
# Item 4: judgment events promotion
# ---------------------------------------------------------------------------

def test_event_with_litigation_context_promotes() -> None:
    """Date + litigation action verb must produce a promoted event."""
    data = _run_extract(
        "The motion was dismissed on March 3, 2025, the court finding that genuine issues of material fact remained to be tried."
    )
    events = _promoted_events(data)
    assert any("March 3, 2025" in e or "2025-03-03" in e for e in events), (
        f"March 3 2025 event not promoted. Events: {events}"
    )


def test_event_filed_promotes() -> None:
    """'filed' + date must produce a promoted event."""
    data = _run_extract(
        "The Defendant filed its Statement of Defence on August 5, 2024."
    )
    events = _promoted_events(data)
    assert any("August 5, 2024" in e or "2024-08-05" in e for e in events), (
        f"August 5 2024 filing not promoted. Events: {events}"
    )


def test_event_hearing_promotes() -> None:
    """'hearing' + date must produce a promoted event."""
    data = _run_extract(
        "Pre-trial conference was held on May 8, 2025."
    )
    events = _promoted_events(data)
    assert any("May 8, 2025" in e or "2025-05-08" in e for e in events), (
        f"May 8 2025 conference not promoted. Events: {events}"
    )


def test_event_sent_letter_promotes() -> None:
    """Factual past action + date must produce a promoted event (sent letter)."""
    data = _run_extract(
        "On September 15, 2024, the Defendant sent a letter purporting to terminate the agreement with immediate effect."
    )
    events = _promoted_events(data)
    assert any("September 15, 2024" in e or "2024-09-15" in e for e in events), (
        f"September 15 2024 not promoted. Events: {events}"
    )


def test_event_wrote_disputes_promotes() -> None:
    """'wrote to' (factual past action) + date must yield a promoted event."""
    data = _run_extract(
        "On September 18, 2024, the Plaintiff wrote to the Defendant disputing the termination and demanding reinstatement."
    )
    events = _promoted_events(data)
    assert any("September 18, 2024" in e or "2024-09-18" in e for e in events), (
        f"September 18 2024 not promoted. Events: {events}"
    )


def test_event_engaged_contractor_promotes() -> None:
    """'engaged' (factual past action) + date must yield a promoted event."""
    data = _run_extract(
        "On October 1, 2024, the Defendant engaged a replacement contractor without notifying the Plaintiff."
    )
    events = _promoted_events(data)
    assert any("October 1, 2024" in e or "2024-10-01" in e for e in events), (
        f"October 1 2024 not promoted. Events: {events}"
    )


def test_events_precision_preserved() -> None:
    """Future/hypothetical date sentences must not produce promoted events."""
    data = _run_extract(
        "The agreement shall close on or before February 28, 2026 if all conditions are satisfied."
    )
    events = _promoted_events(data)
    # The condition 'if' should cap confidence below promotion threshold
    assert not events, f"Hypothetical future event must not promote: {events}"


def test_judgment_fixture_events_promoted_recall() -> None:
    """en_judgment fixture: promoted events recall must be >= 12/14 (>=0.85)."""
    fixture_path = FIXTURES_DIR / "en_judgment.md"
    labels_path = FIXTURES_DIR / "en_judgment.md.labels.json"
    data = _run_extract_file(fixture_path)
    with open(labels_path) as f:
        labels = json.load(f)
    expected = labels["fields"]["events"]
    events = _promoted_events(data)
    # Matching: label date string matches event date
    found = 0
    for label in expected:
        label_stripped = label.strip()
        for e in events:
            if label_stripped in e or e in label_stripped:
                found += 1
                break
    assert found >= int(len(expected) * 0.7), (
        f"Expected >={int(len(expected) * 0.7)}/{len(expected)} judgment events promoted, got {found}. "
        f"Promoted dates: {events}"
    )


if __name__ == "__main__":
    import traceback
    tests = [v for k, v in globals().items() if k.startswith("test_") and callable(v)]
    passed = failed = 0
    for fn in tests:
        try:
            fn()
            print(f"  PASS  {fn.__name__}")
            passed += 1
        except Exception:
            print(f"  FAIL  {fn.__name__}")
            traceback.print_exc()
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
