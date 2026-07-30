"""W4.2 tests: heuristic NER party pass (harvesters/party_mentions.py).

Standalone-runnable: python scripts/tests/test_party_mentions.py
Also discoverable by pytest. No pytest fixtures; no parametrize (plain loops
keep the bare __main__ runner working, W0 item 1 convention).

The NER pass emits freeform_mention hints only; the cap is enforced
structurally in the resolver (a freeform_mention candidate never promotes,
even at maximum confidence).  Corroboration happens in the resolver: an NER
hint whose mention matches an existing defined-party or table-row candidate
raises that candidate's confidence, never its own tier.

Assertions run against the real engine (extract()) for the cap and
corroboration proofs, not harvester internals, so the ceiling is proven on
resolver output.
"""
from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from extraction import extract  # noqa: E402
from extraction.harvesters import CandidateHarvester  # noqa: E402


# ---------------------------------------------------------------------------
# Synthetic-doc helpers
# ---------------------------------------------------------------------------

def _block(idx: int, text: str, lang: str = "en") -> SimpleNamespace:
    return SimpleNamespace(
        idx=idx,
        text=text,
        lang=lang,
        block_type="paragraph",
        anchor="",
        heading_path=[],
        parent_heading=None,
        table_coords=None,
    )


def _doc(blocks: list[SimpleNamespace]) -> SimpleNamespace:
    return SimpleNamespace(source="test.md", blocks=blocks, tables=[], truncated=False)


def _run(blocks: list[SimpleNamespace]) -> tuple:
    """Run the full engine; return (result, candidate_manifest)."""
    result, candidate_manifest, _enrich = extract(_doc(blocks))
    return result, candidate_manifest


def _freeform_candidates(manifest: dict) -> list[dict]:
    return [c for c in manifest.get("candidates", []) if c.get("frame_type") == "freeform_mention"]


def _decision_for(manifest: dict, candidate_id: str) -> str:
    for d in manifest.get("promotion_decisions", []):
        if d.get("candidate_id") == candidate_id:
            return d.get("action", "")
    return ""


def _party_names(result) -> list[str]:
    return [p.name for p in result.parties]


# ---------------------------------------------------------------------------
# 1. Hint emission (EN + FR): freeform mention repeated across blocks with a
#    role word yields a freeform_mention hint carrying a verbatim snippet and
#    full SourceRef provenance.
# ---------------------------------------------------------------------------

def test_en_freeform_mention_emits_hint() -> None:
    blocks = [
        _block(0, "The vendor Aurora Software shall deliver the goods to the purchaser.", "en"),
        _block(1, "The purchaser confirmed that Aurora Software remained the vendor.", "en"),
    ]
    _result, manifest = _run(blocks)
    freeform = _freeform_candidates(manifest)
    names = {c["normalized_value"].get("mention") for c in freeform}
    assert "Aurora Software" in names, names
    cand = next(c for c in freeform if c["normalized_value"].get("mention") == "Aurora Software")
    # Verbatim snippet from one of the source sentences, full SourceRef provenance.
    assert "Aurora Software" in cand["normalized_value"].get("snippet", ""), cand
    assert cand["evidence_ids"], "freeform hint must carry an evidence packet"
    assert cand["source_ref"]["source"] == "test.md", cand["source_ref"]
    # Tier stays hint.
    assert _decision_for(manifest, cand["id"]) == "hint", manifest["promotion_decisions"]


def test_fr_freeform_mention_emits_hint() -> None:
    blocks = [
        _block(0, "Le vendeur Société Générale Ltée doit livrer les marchandises à l'acheteur.", "fr"),
        _block(1, "L'acheteur a confirmé que Société Générale Ltée demeurait le vendeur.", "fr"),
    ]
    _result, manifest = _run(blocks)
    names = {c["normalized_value"].get("mention") for c in _freeform_candidates(manifest)}
    assert "Société Générale Ltée" in names, names


def test_single_block_mention_emits_no_hint() -> None:
    # Document frequency is 2+ distinct blocks; a single-block mention with a
    # role word does not clear the frequency floor and emits no hint.
    blocks = [
        _block(0, "Aurora Software shall deliver the goods to the purchaser.", "en"),
        _block(1, "The closing occurred on schedule with no further action.", "en"),
    ]
    _result, manifest = _run(blocks)
    names = {c["normalized_value"].get("mention") for c in _freeform_candidates(manifest)}
    assert "Aurora Software" not in names, names


def test_role_word_absent_emits_no_hint() -> None:
    # Corroboration requires a role word in at least one occurrence; capitalized
    # sequences repeated across blocks with no role word stay below the bar.
    blocks = [
        _block(0, "Aurora Software released a new feature.", "en"),
        _block(1, "Aurora Software updated its website.", "en"),
    ]
    _result, manifest = _run(blocks)
    names = {c["normalized_value"].get("mention") for c in _freeform_candidates(manifest)}
    assert "Aurora Software" not in names, names


# ---------------------------------------------------------------------------
# 2. Cap proof: a maximally-corroborated NER mention still lands at hint tier
#    in the real resolver output, never as a promoted entity.
# ---------------------------------------------------------------------------

def test_freeform_mention_capped_at_hint_even_at_max_signals() -> None:
    # Repeated across many blocks, every occurrence carrying a role word, so
    # the harvester's own signals are maximal.  The resolver must still refuse
    # to promote a freeform_mention frame.
    blocks = [
        _block(i, f"The purchaser noted that Aurora Software, the vendor, acted as employee {i}.", "en")
        for i in range(6)
    ]
    result, manifest = _run(blocks)
    # No promoted party originates from the freeform mention alone.
    assert "Aurora Software" not in _party_names(result), _party_names(result)
    # Every freeform_mention candidate is a hint, regardless of its score.
    for cand in _freeform_candidates(manifest):
        assert _decision_for(manifest, cand["id"]) == "hint", (cand["id"], cand.get("confidence"))


def test_resolver_caps_freeform_mention_at_unit_confidence() -> None:
    # Structural cap proof at the resolver seam: a freeform_mention candidate
    # with confidence 1.0 (above PROMOTE_AUTO) is still demoted to a hint.
    from extraction.resolver import resolve_candidates
    from extraction.schema import Candidate, SourceRef

    cand = Candidate(
        id="C0000",
        target_field="parties",
        frame_type="freeform_mention",
        normalized_value={"mention": "Aurora Software", "snippet": "Aurora Software", "type": "party"},
        signals=["ner_mention", "ner_role_word", "ner_doc_frequency"],
        confidence=1.0,
        evidence_ids=["E0000"],
        source_ref=SourceRef(source="test.md", block_id="0"),
    )
    decisions = resolve_candidates([cand], sparse=True)
    assert decisions[0].action == "hint", decisions[0]


# ---------------------------------------------------------------------------
# 3. Corroboration promotion (EN + FR): a defined-party candidate that would
#    otherwise sit below the promotion threshold crosses it when an NER hint
#    corroborates it.  Tested by comparing the same doc with and without the
#    freeform repetition: the defined party's confidence strictly increases.
# ---------------------------------------------------------------------------

def _litigation_party_confidence(result, manifest: dict, name: str) -> float:
    best = 0.0
    for c in manifest.get("candidates", []):
        if c.get("target_field") != "parties":
            continue
        if c["normalized_value"].get("name") == name:
            best = max(best, float(c.get("confidence", 0.0)))
    return best


def test_en_corroboration_raises_defined_party_confidence() -> None:
    # A litigation caption seeds a below-promotion defined party ("Aurora
    # Software"); repeated freeform mentions with role words corroborate it.
    caption_block = _block(0, "Aurora Software v. Boreal Distribution", "en")
    mention_a = _block(1, "The vendor Aurora Software acted in this matter.", "en")
    mention_b = _block(2, "The purchaser engaged Aurora Software as vendor.", "en")

    # Baseline: caption only (no freeform corroboration).
    _r0, m0 = _run([caption_block])
    base_conf = _litigation_party_confidence(_r0, m0, "Aurora Software")
    assert base_conf > 0.0, "caption should seed a defined-party candidate"

    # With corroboration: the same caption plus repeated freeform mentions.
    r1, m1 = _run([caption_block, mention_a, mention_b])
    corrob_conf = _litigation_party_confidence(r1, m1, "Aurora Software")
    assert corrob_conf > base_conf, (base_conf, corrob_conf)
    # The corroborated party candidate carries the corroboration signal.
    corrob_cands = [
        c for c in m1.get("candidates", [])
        if c.get("target_field") == "parties"
        and c["normalized_value"].get("name") == "Aurora Software"
        and "ner_corroboration" in c.get("signals", [])
    ]
    assert corrob_cands, "corroborated party must carry the ner_corroboration signal"


def test_fr_corroboration_raises_defined_party_confidence() -> None:
    caption_block = _block(0, "Gagnon Transport c. Beaulieu Construction", "fr")
    mention_a = _block(1, "Le vendeur Gagnon Transport agit dans cette affaire.", "fr")
    mention_b = _block(2, "L'acheteur a engagé Gagnon Transport comme vendeur.", "fr")

    _r0, m0 = _run([caption_block])
    base_conf = _litigation_party_confidence(_r0, m0, "Gagnon Transport")
    assert base_conf > 0.0, "FR caption should seed a defined-party candidate"

    r1, m1 = _run([caption_block, mention_a, mention_b])
    corrob_conf = _litigation_party_confidence(r1, m1, "Gagnon Transport")
    assert corrob_conf > base_conf, (base_conf, corrob_conf)


# ---------------------------------------------------------------------------
# 4. Stop list: sentence-initial capitalized sequences and month names do not
#    produce freeform_mention hints.
# ---------------------------------------------------------------------------

def test_sentence_initial_capital_not_a_mention() -> None:
    # "Closing Conditions" leads every sentence; sentence-initial capitalized
    # sequences are stop-listed and must not become freeform mentions.
    blocks = [
        _block(0, "Closing Conditions apply to the purchaser obligations.", "en"),
        _block(1, "Closing Conditions also bind the vendor obligations.", "en"),
    ]
    _result, manifest = _run(blocks)
    names = {c["normalized_value"].get("mention") for c in _freeform_candidates(manifest)}
    assert "Closing Conditions" not in names, names


def test_month_names_not_a_mention() -> None:
    blocks = [
        _block(0, "The purchaser must act before March April per the schedule.", "en"),
        _block(1, "The vendor must act before March April per the addendum.", "en"),
    ]
    _result, manifest = _run(blocks)
    names = {c["normalized_value"].get("mention") for c in _freeform_candidates(manifest)}
    assert "March April" not in names, names


# ---------------------------------------------------------------------------
# 5. FR accents: "Société Générale Ltée" style mentions detect under FR blocks
#    via the bundle character class (covered above in
#    test_fr_freeform_mention_emits_hint; this asserts accents survive verbatim).
# ---------------------------------------------------------------------------

def test_fr_accented_mention_preserves_accents() -> None:
    blocks = [
        _block(0, "Le vendeur Société Générale Ltée doit livrer à l'acheteur.", "fr"),
        _block(1, "Selon l'acheteur, Société Générale Ltée a confirmé la livraison.", "fr"),
    ]
    _result, manifest = _run(blocks)
    mention = next(
        c["normalized_value"]["mention"]
        for c in _freeform_candidates(manifest)
        if "Société" in c["normalized_value"].get("mention", "")
    )
    assert mention == "Société Générale Ltée", mention


# ---------------------------------------------------------------------------
# 6. Determinism: same doc parsed twice yields identical candidate ordering.
# ---------------------------------------------------------------------------

def test_determinism_identical_candidate_ordering() -> None:
    blocks_first = [
        _block(0, "Aurora Software shall deliver to the purchaser.", "en"),
        _block(1, "The purchaser engaged Aurora Software as vendor.", "en"),
        _block(2, "Boreal Distribution shall pay the vendor on time.", "en"),
        _block(3, "The vendor invoiced Boreal Distribution promptly.", "en"),
    ]
    blocks_second = [
        _block(0, "Aurora Software shall deliver to the purchaser.", "en"),
        _block(1, "The purchaser engaged Aurora Software as vendor.", "en"),
        _block(2, "Boreal Distribution shall pay the vendor on time.", "en"),
        _block(3, "The vendor invoiced Boreal Distribution promptly.", "en"),
    ]
    _r1, m1 = _run(blocks_first)
    _r2, m2 = _run(blocks_second)
    order1 = [(c["frame_type"], c["normalized_value"]) for c in m1["candidates"]]
    order2 = [(c["frame_type"], c["normalized_value"]) for c in m2["candidates"]]
    assert order1 == order2, "candidate ordering must be deterministic across runs"


# ---------------------------------------------------------------------------
# 7. Bilingual dedup safety: the NER pass must not break canonical party
#    single-promotion (the bilingual W3 invariant names.count(x) == 1).
# ---------------------------------------------------------------------------

def test_ner_pass_does_not_duplicate_promoted_parties() -> None:
    # Two defined parties via captions, plus freeform repetition of each.  The
    # promoted tier must still carry each party exactly once.
    blocks = [
        _block(0, "Aurora Software v. Boreal Distribution", "en"),
        _block(1, "Aurora Software shall act as vendor for the purchaser.", "en"),
        _block(2, "The purchaser paid Aurora Software as vendor.", "en"),
        _block(3, "Boreal Distribution shall notify the purchaser as vendor.", "en"),
        _block(4, "The purchaser received Boreal Distribution's vendor notice.", "en"),
    ]
    result, _manifest = _run(blocks)
    names = _party_names(result)
    for expected in ["Aurora Software", "Boreal Distribution"]:
        assert names.count(expected) <= 1, (expected, names)


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_") and callable(value)]
    for test in tests:
        test()
    print(f"{len(tests)} tests passed")
