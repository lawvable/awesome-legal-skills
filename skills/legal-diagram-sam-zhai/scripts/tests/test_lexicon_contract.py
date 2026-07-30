"""Tests for W3.2/W3.3: LexiconBundle contract (EN + FR) and FR normalisation.

Contract test: every LexiconBundle field must be populated in BOTH the EN and
FR bundles.  Field discovery iterates dataclasses.fields, so adding a field to
base.py without populating it in both en.py and fr.py FAILS here.

Standalone-runnable: python scripts/tests/test_lexicon_contract.py
Also discoverable by pytest. No pytest fixtures; no parametrize (plain loops
keep the bare __main__ runner working, W0 item 1 convention).
"""
from __future__ import annotations

import dataclasses
import re
import sys
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from extraction.lexicon import LexiconBundle, get_bundle  # noqa: E402

LANGS = ("en", "fr")


# ---------------------------------------------------------------------------
# Bundle contract: every field populated, correctly typed, in both languages
# ---------------------------------------------------------------------------

def _assert_field_populated(lang: str, name: str, value: object) -> None:
    """Assert one bundle field is populated per its runtime type.

    Regex fields: compiled with a non-empty pattern.  Tuple fields: non-empty;
    elements are compiled regexes, non-empty strings, or frame-table entries
    (name, compiled regex, base confidence).  Callable fields: callable.
    Unknown field types fail loudly so a new field shape must be added here.
    """
    label = f"{lang} bundle field {name!r}"
    assert value is not None, f"{label} is None"
    if isinstance(value, re.Pattern):
        assert value.pattern.strip(), f"{label} compiled from an empty pattern"
        return
    if isinstance(value, tuple):
        assert len(value) > 0, f"{label} is an empty tuple"
        for i, element in enumerate(value):
            element_label = f"{label}[{i}]"
            if isinstance(element, re.Pattern):
                assert element.pattern.strip(), f"{element_label} empty pattern"
            elif isinstance(element, str):
                assert element.strip(), f"{element_label} empty string"
            elif isinstance(element, tuple):
                assert len(element) == 3, f"{element_label} frame entry must be (name, regex, base)"
                frame, rx, base = element
                assert isinstance(frame, str) and frame.strip(), f"{element_label} frame name empty"
                assert isinstance(rx, re.Pattern) and rx.pattern.strip(), f"{element_label} regex empty"
                assert isinstance(base, float) and 0.0 < base <= 1.0, f"{element_label} base confidence invalid"
            else:
                raise AssertionError(f"{element_label} has unhandled element type {type(element)!r}")
        return
    if callable(value):
        return
    raise AssertionError(f"{label} has unhandled field type {type(value)!r}; extend this contract test")


def test_bundle_contract_all_fields_populated_both_languages() -> None:
    for lang in LANGS:
        bundle = get_bundle(lang)
        assert isinstance(bundle, LexiconBundle)
        for field in dataclasses.fields(bundle):
            _assert_field_populated(lang, field.name, getattr(bundle, field.name))


def test_bundle_index_contracts_both_languages() -> None:
    """Documented index contracts harvesters rely on, per language."""
    for lang in LANGS:
        bundle = get_bundle(lang)
        # citations.py: [0] neutral, [1] case, [2] statutory, [3] rule.
        assert len(bundle.citation_patterns) == 4, f"{lang}: citation_patterns must have exactly 4 entries"
        # controls.py: [0] gate pattern, [1] evidence-signal pattern.
        assert len(bundle.control_patterns) >= 2, f"{lang}: control_patterns needs gate + evidence entries"
        # parties.py: caption pattern exposes two positional groups (left, right).
        assert bundle.caption_patterns[0].groups >= 2, f"{lang}: caption pattern needs 2 groups"
        # parties.py: defined-party markers expose named groups name/role.
        for rx in bundle.defined_party_markers:
            assert {"name", "role"} <= set(rx.groupindex), f"{lang}: defined_party_markers need name/role groups"
        # ownership.py: [0] exposes named groups parent/pct/child.
        assert {"parent", "pct", "child"} <= set(bundle.ownership_patterns[0].groupindex), (
            f"{lang}: ownership_patterns[0] needs parent/pct/child groups"
        )
        # obligations.py: prohibition frames are a subset of the obligation table.
        obligation_frames = {frame for frame, _rx, _base in bundle.obligation_patterns}
        for frame, _rx, _base in bundle.prohibition_patterns:
            assert frame in obligation_frames, f"{lang}: prohibition frame {frame!r} missing from obligation_patterns"
        # party_mentions.py (W4.2): titlecase token + role words.
        assert bundle.titlecase_token_re.match("Aurora"), f"{lang}: titlecase_token_re must match a capitalized token"
        assert len(bundle.party_role_words) >= 5, f"{lang}: party_role_words needs the documented role set"
        assert all(w == w.lower() for w in bundle.party_role_words), f"{lang}: party_role_words must be lowercased"


def test_fr_titlecase_token_matches_accented_tokens() -> None:
    # Regression guard: the FR title-case token class must cover accented
    # leading capitals and accented bodies so "Société"/"Générale"/"Ltée"
    # survive the heuristic NER pass under the FR bundle.
    fr = get_bundle("fr")
    for token in ("Société", "Générale", "Ltée", "Tremblay", "Île"):
        m = fr.titlecase_token_re.match(token)
        assert m is not None and m.group(0) == token, f"FR titlecase_token_re must match {token!r}"


def test_party_role_words_cover_spec_vocabulary() -> None:
    en = get_bundle("en")
    fr = get_bundle("fr")
    for word in ("plaintiff", "defendant", "vendor", "purchaser", "employee"):
        assert word in en.party_role_words, f"EN party_role_words missing {word!r}"
    for word in ("demandeur", "défendeur", "vendeur", "acheteur", "employé"):
        assert word in fr.party_role_words, f"FR party_role_words missing {word!r}"
    # Québec feminine forms: real FR judgments say "la défenderesse"; the
    # masculine stems do not substring-match these, so both genders ship.
    for word in ("demanderesse", "défenderesse", "venderesse", "acheteuse"):
        assert word in fr.party_role_words, f"FR party_role_words missing feminine form {word!r}"


def test_get_bundle_fr_branch_and_en_fallback() -> None:
    en = get_bundle("en")
    fr = get_bundle("fr")
    assert fr is not en, "get_bundle('fr') must return a distinct FR bundle"
    assert get_bundle("fr") is fr, "FR bundle must be a module-level singleton"
    assert get_bundle("xx") is en, "unknown language codes must still fall back to EN"
    assert get_bundle("") is en, "empty language code must fall back to EN"


# ---------------------------------------------------------------------------
# FR date -> ISO normalisation; EN normalize_date keeps as-written surface
# ---------------------------------------------------------------------------

def test_fr_date_normalises_to_iso() -> None:
    fr = get_bundle("fr")
    cases = [
        ("1er juin 2026", "2026-06-01"),
        ("le 2 juin 2026", "2026-06-02"),
        ("2026-06-01", "2026-06-01"),
        ("Le jugement a été rendu le 15 décembre 2025.", "2025-12-15"),
        ("au plus tard le 3 août 2026", "2026-08-03"),
        ("aucune date ici", None),
    ]
    for text, expected in cases:
        assert fr.normalize_date(text) == expected, f"normalize_date({text!r})"
        if expected is not None:
            assert fr.date_re.search(text), f"fr date_re must match {text!r}"


def test_en_normalize_date_returns_matched_text_verbatim() -> None:
    """EN canonical date surface is the as-written match (EN goldens lock it)."""
    en = get_bundle("en")
    cases = [
        ("no later than June 1, 2026", "June 1, 2026"),
        ("by 2026-06-01", "2026-06-01"),
        ("no date here", None),
    ]
    for text, expected in cases:
        assert en.normalize_date(text) == expected, f"normalize_date({text!r})"


# ---------------------------------------------------------------------------
# FR money: pattern match + amount parse; EN parse_amount defers to helpers
# ---------------------------------------------------------------------------

def test_fr_money_re_matches_locale_formats() -> None:
    fr = get_bundle("fr")
    samples = [
        "1 234 567,89 $",
        "100 000 $",
        "1,5 M$",
        "1 234 567,89 $",  # narrow no-break space thousands separator
        "1 234 567,89 $",  # no-break space thousands separator
    ]
    for sample in samples:
        assert fr.money_re.search(sample), f"fr money_re must match {sample!r}"


def test_fr_parse_amount() -> None:
    fr = get_bundle("fr")
    cases = [
        ("1 234 567,89 $", 1234567.89),
        ("1 234 567,89 $", 1234567.89),
        ("100 000 $", 100000.0),
        ("1,5 M$", 1500000.0),
        ("2 M$", 2000000.0),
        (None, None),
        ("aucun montant", None),
    ]
    for text, expected in cases:
        assert fr.parse_amount(text) == expected, f"parse_amount({text!r})"


def test_en_parse_amount_defers_to_pipeline_default() -> None:
    """EN bundle contributes no harvest-time amount: EN candidate payloads are
    golden-locked, and EN amounts parse downstream via helpers.money.amount_number."""
    en = get_bundle("en")
    for text in [None, "$1,000,000", "USD 250.00"]:
        assert en.parse_amount(text) is None, f"EN parse_amount({text!r}) must defer (None)"


# ---------------------------------------------------------------------------
# FR caption style ("Tremblay c. Daigle")
# ---------------------------------------------------------------------------

def test_fr_caption_pattern_matches_c_style() -> None:
    fr = get_bundle("fr")
    m = fr.caption_patterns[0].search("Tremblay c. Daigle")
    assert m is not None, "FR caption pattern must match 'Tremblay c. Daigle'"
    assert m.group(1).strip() == "Tremblay"
    assert m.group(2).strip() == "Daigle"
    # EN caption style must not be required for FR: 'v.' captions stay EN-only.
    assert fr.caption_patterns[0].search("Smith v. Jones") is None


def test_fr_corporate_suffixes_match_catalogue_forms() -> None:
    # Regression guard: 'S.E.N.C.' once had a mandatory final dot before \b,
    # making the branch unmatchable in real text (spec-review catch).
    fr = get_bundle("fr")
    for sample in (
        "Conseil S.E.N.C.",
        "Conseil S.E.N.C. est partie",
        "Gagnon S.E.N.C.R.L.",
        "Tremblay Ltée",
        "Aubin inc.",
        "Dion s.r.l.",
        "Roy S.A.",
    ):
        assert any(p.search(sample) for p in fr.corporate_suffixes), (
            f"FR corporate suffix must match {sample!r}"
        )


# ---------------------------------------------------------------------------
# FR abbreviation guards: no sentence split at "art. 1457" / "M. Tremblay"
# ---------------------------------------------------------------------------

def test_fr_abbreviation_guards_protect_sentence_split() -> None:
    from extraction.utils import sentences_with_offsets

    fr = get_bundle("fr")
    text = "M. Tremblay invoque l'art. 1457 du Code civil. La cour rejette la requête."
    sentences = [sent for sent, _start, _end in sentences_with_offsets(text, fr.abbreviation_guards)]
    assert len(sentences) == 2, f"expected 2 sentences, got {sentences!r}"
    assert "art. 1457" in sentences[0], f"'art. 1457' split apart: {sentences!r}"
    assert sentences[0].startswith("M. Tremblay"), f"'M. Tremblay' split apart: {sentences!r}"
    # Offsets must stay exact under guard substitution (W0 invariant).
    for sent, start, end in sentences_with_offsets(text, fr.abbreviation_guards):
        assert text[start:end] == sent


# ---------------------------------------------------------------------------
# Dispatcher: bundle selected per block from block.lang
# ---------------------------------------------------------------------------

def test_dispatcher_selects_bundle_from_block_lang() -> None:
    from extraction.harvesters import CandidateHarvester

    def _block(idx: int, text: str, lang: str) -> SimpleNamespace:
        return SimpleNamespace(idx=idx, text=text, lang=lang, block_type="paragraph", anchor="", heading_path=[], parent_heading=None)

    doc = SimpleNamespace(
        source="test.md",
        blocks=[
            _block(0, "Smith v. Jones, 2026 SCC 12 was heard on June 1, 2026.", "en"),
            _block(1, "Tremblay c. Daigle, 2026 CSC 12 a été entendu le 1er juin 2026.", "fr"),
        ],
        tables=[],
        truncated=False,
    )
    harvester = CandidateHarvester(doc)
    candidates = harvester.run()
    caption_names = {
        c.normalized_value.get("name")
        for c in candidates
        if c.frame_type == "litigation_caption"
    }
    assert {"Smith", "Jones"} <= caption_names, f"EN caption missing: {caption_names!r}"
    assert {"Tremblay", "Daigle"} <= caption_names, f"FR caption missing (FR bundle not selected): {caption_names!r}"


def test_fr_payment_amount_override_and_en_payload_unchanged() -> None:
    from extraction.context import HarvestContext
    from extraction.harvesters.payments import harvest_payments
    from extraction.schema import SourceRef

    recorded: list[dict] = []

    def _sink(target_field, frame_type, value, snippet_text, source_ref, confidence, signals, anti_signals=None):
        recorded.append({"target_field": target_field, "frame_type": frame_type, "value": value})

    source_ref = SourceRef(block_id="b0", heading_path=[])

    # FR: bundle-matched money parses at harvest time; date normalises to ISO.
    fr_ctx = HarvestContext(bundle=get_bundle("fr"), add_candidate=_sink, source_ref=source_ref, anti=[])
    harvest_payments(fr_ctx, "L'Acheteur verse 1 234 567,89 $ au Vendeur au plus tard le 1er juin 2026.")
    fr_payments = [r for r in recorded if r["frame_type"] == "payment_flow"]
    assert len(fr_payments) == 1, f"FR payment sentence must harvest: {recorded!r}"
    assert fr_payments[0]["value"]["amount"] == 1234567.89
    assert fr_payments[0]["value"]["amount_text"] == "1 234 567,89 $"
    assert fr_payments[0]["value"]["timing"] == "2026-06-01"

    # EN: payload shape unchanged (no harvest-time "amount" key; goldens lock it).
    recorded.clear()
    en_ctx = HarvestContext(bundle=get_bundle("en"), add_candidate=_sink, source_ref=source_ref, anti=[])
    harvest_payments(en_ctx, "Buyer shall pay $1,000,000 to Seller no later than June 1, 2026.")
    en_payments = [r for r in recorded if r["frame_type"] == "payment_flow"]
    assert len(en_payments) == 1, f"EN payment sentence must harvest: {recorded!r}"
    assert "amount" not in en_payments[0]["value"], "EN payment payload must not gain an 'amount' key"
    assert en_payments[0]["value"]["amount_text"] == "$1,000,000"
    assert en_payments[0]["value"]["timing"] == "June 1, 2026"


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_") and callable(value)]
    for test in tests:
        test()
    print(f"{len(tests)} tests passed")
