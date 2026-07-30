"""Tests for W3.1: language detection + manifest language_profile.

Standalone-runnable: python scripts/tests/test_language.py
Also discoverable by pytest. No pytest fixtures beyond tmp_path; no parametrize
(plain loops keep the bare __main__ runner working, W0 item 1 convention).
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from extraction.language import SHORT_BLOCK_CHARS, annotate_blocks, detect_language  # noqa: E402

EXTRACT = ROOT / "extract_entities.py"

FR_LONG = (
    "Le présent contrat est conclu entre les parties conformément aux dispositions "
    "applicables et toutes les obligations doivent être respectées par les parties."
)
EN_LONG = (
    "The buyer shall deliver the certificate to the seller and each party must comply "
    "with all of the obligations under this agreement, including any notice requirements."
)


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


def _block(text: str) -> SimpleNamespace:
    return SimpleNamespace(text=text)


# ---------------------------------------------------------------------------
# detect_language unit tests
# ---------------------------------------------------------------------------

def test_detect_language_french() -> None:
    lang, confidence = detect_language(FR_LONG)
    assert lang == "fr"
    assert confidence > 0.5


def test_detect_language_english() -> None:
    lang, confidence = detect_language(EN_LONG)
    assert lang == "en"
    assert confidence > 0.5


def test_detect_language_low_signal_und() -> None:
    # Fewer than 3 total marker hits across both sets -> und.
    samples = [
        "",
        "Quantum 9000 chassis bolt torque 45 Nm",
        "12345 67890",
        "the certificate",  # only 1 hit
    ]
    for text in samples:
        lang, confidence = detect_language(text)
        assert lang == "und", text
        assert confidence == 0.0, text


def test_detect_language_tie_is_und() -> None:
    # Equal hits in both sets: no margin, no winner.
    lang, confidence = detect_language("the of shall le la les")
    assert lang == "und"
    assert confidence == 0.0


# ---------------------------------------------------------------------------
# annotate_blocks unit tests
# ---------------------------------------------------------------------------

def test_annotate_blocks_assigns_lang_and_profile() -> None:
    blocks = [_block(FR_LONG), _block(EN_LONG)]
    profile = annotate_blocks(blocks)
    assert blocks[0].lang == "fr"
    assert blocks[1].lang == "en"
    assert set(profile) == {"dominant", "override", "blocks", "char_share"}
    assert profile["override"] is None
    assert profile["blocks"] == {"en": 1, "fr": 1, "und": 0}
    assert abs(profile["char_share"]["en"] + profile["char_share"]["fr"] - 1.0) < 0.011


def test_annotate_blocks_short_block_inherits_dominant() -> None:
    short_en = "The buyer shall deliver the documents to the seller."
    assert len(short_en) < SHORT_BLOCK_CHARS  # fixture premise: block must be short
    blocks = [_block(FR_LONG), _block(FR_LONG), _block(short_en)]
    profile = annotate_blocks(blocks)
    assert profile["dominant"] == "fr"
    # Raw detector counts keep the short block as en...
    assert profile["blocks"] == {"en": 1, "fr": 2, "und": 0}
    # ...but the effective lang inherits the document-dominant language.
    assert blocks[2].lang == "fr"


def test_annotate_blocks_und_block_inherits_dominant() -> None:
    blocks = [_block(EN_LONG), _block("12345 67890")]
    profile = annotate_blocks(blocks)
    assert profile["dominant"] == "en"
    assert profile["blocks"]["und"] == 1
    assert blocks[1].lang == "en"


def test_annotate_blocks_char_count_tie_dominant_en() -> None:
    # Pad the shorter text with spaces so classified char counts tie exactly.
    width = max(len(FR_LONG), len(EN_LONG))
    blocks = [_block(FR_LONG.ljust(width)), _block(EN_LONG.ljust(width))]
    profile = annotate_blocks(blocks)
    assert profile["dominant"] == "en"
    assert profile["char_share"] == {"en": 0.5, "fr": 0.5}


def test_annotate_blocks_no_classified_blocks_dominant_en() -> None:
    blocks = [_block("12345"), _block("Quantum chassis torque")]
    profile = annotate_blocks(blocks)
    assert profile["dominant"] == "en"
    assert profile["blocks"] == {"en": 0, "fr": 0, "und": 2}
    assert profile["char_share"] == {"en": 0.0, "fr": 0.0}
    for b in blocks:
        assert b.lang == "en"


def test_annotate_blocks_override_forces_every_block() -> None:
    blocks = [_block(FR_LONG), _block(FR_LONG), _block(EN_LONG), _block("12345")]
    profile = annotate_blocks(blocks, override="en")
    assert profile["override"] == "en"
    # Detection still runs for reporting when forced.
    assert profile["dominant"] == "fr"
    assert profile["blocks"] == {"en": 1, "fr": 2, "und": 1}
    for b in blocks:
        assert b.lang == "en"


# ---------------------------------------------------------------------------
# CLI integration: --lang flag and manifest language_profile
# ---------------------------------------------------------------------------

FR_DOC = """# Contrat de services

Le présent contrat est conclu entre les parties conformément aux dispositions applicables et toutes les obligations doivent être respectées.

Le prestataire doit livrer les documents au client dans les trente jours et les parties doivent respecter toutes les obligations prévues par le présent contrat.
"""


def test_cli_language_profile_shape_and_auto_default(tmp_path: Path) -> None:
    doc = tmp_path / "contrat.md"
    doc.write_text(FR_DOC, encoding="utf-8")
    data = _run_extract_file(doc)
    profile = data["language_profile"]
    assert list(profile) == ["dominant", "override", "blocks", "char_share"]
    assert profile["dominant"] == "fr"
    assert profile["override"] is None
    assert list(profile["blocks"]) == ["en", "fr", "und"]
    assert list(profile["char_share"]) == ["en", "fr"]
    assert profile["blocks"]["fr"] >= 2
    assert profile["char_share"]["fr"] > 0.8
    # Per-block lang stays internal: no per-block lang emitted in the manifest.
    assert "blocks" not in data  # NormalizedDoc blocks never serialised top-level
    # --lang auto is the default; explicit auto must match.
    data_auto = _run_extract_file(doc, ["--lang", "auto"])
    assert data_auto["language_profile"] == profile


def test_cli_lang_override_reports_override_and_keeps_detection(tmp_path: Path) -> None:
    doc = tmp_path / "contrat.md"
    doc.write_text(FR_DOC, encoding="utf-8")
    for forced in ["en", "fr"]:
        data = _run_extract_file(doc, ["--lang", forced])
        profile = data["language_profile"]
        assert profile["override"] == forced
        # Detection still runs for reporting when forced.
        assert profile["dominant"] == "fr"
        assert profile["blocks"]["fr"] >= 2


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
