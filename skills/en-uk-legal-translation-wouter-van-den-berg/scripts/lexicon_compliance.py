#!/usr/bin/env python3
"""
lexicon_compliance.py — scan a translation JSON or document.xml for forbidden
calque phrases and hard-rule terminology violations drawn from the reference
lexicons' "Avoid" columns and the language sub-lexicons.

Exits with code 0 if the input is clean, non-zero (and prints each offending
location) if any forbidden phrase is found.

Usage:
    # Scan paragraphs.json BEFORE applying translations (Step 4d)
    python scripts/lexicon_compliance.py paragraphs.json --stage pre-apply

    # Scan the translated document.xml AFTER post-processing (Step 8d, pre-repack)
    python scripts/lexicon_compliance.py final/word/document.xml --stage pre-repack

    # Disable source-language hints (use only the language-agnostic ruleset)
    python scripts/lexicon_compliance.py paragraphs.json --language none

    # Restrict to a specific source language (narrows language-specific rules)
    python scripts/lexicon_compliance.py paragraphs.json --language dutch

The script is intentionally conservative: it only flags phrases that are
explicitly listed in a reference lexicon's "Avoid" column, or that have been
documented (with a real example) as a calque by previous translations produced
by this skill. False positives on bona fide correct usages are kept rare by
using word-boundary-aware regex and, where needed, negative look-behind /
context checks.

Exit codes:
    0 — clean
    1 — violations found (script prints each, then exits 1)
    2 — I/O error or bad invocation
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

def _check_self_integrity():
    """Detect install-time truncation. Whole-file scan tolerates null-padding."""
    try:
        with open(os.path.abspath(__file__), 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError:
        return
    if '\n# === SKILL FILE COMPLETE ===' not in content:
        msg = (
            "\n" + "=" * 60 + "\n"
            "[skill] FILE INTEGRITY CHECK FAILED — script truncated.\n"
            f"  File: {os.path.abspath(__file__)}\n"
            f"  Size: {len(content):,} bytes (sentinel marker missing).\n"
            "  Re-install the skill from the .skill / .zip archive.\n"
            + "=" * 60 + "\n"
        )
        print(msg, file=sys.stderr)
        sys.exit(3)


_check_self_integrity()



# --------------------------------------------------------------------------
# Rule table
# --------------------------------------------------------------------------
#
# Each rule is:
#   (severity, pattern, message, applies_to_languages)
#
# severity: "BLOCK" (exit 1) or "WARN" (printed but does not fail).
# pattern:  Python regex. Case-insensitive by default; escape \b for word
#           boundaries. Keep patterns *narrow* — the Avoid column of the
#           lexicon is authoritative.
# message:  Short human-readable explanation including the correct rendering.
# applies_to_languages:
#           List of source languages for which this rule applies, OR
#           ["*"] for language-agnostic rules derived from the English
#           reference lexicons.
#
# Adding a new rule: it must be traceable to a specific lexicon line
# (English reference or language sub-lexicon Avoid column). Do not add
# rules based on personal preference — only documented guidance.

Rule = Tuple[str, "re.Pattern[str]", str, List[str]]

def _c(pat: str) -> "re.Pattern[str]":
    return re.compile(pat, re.IGNORECASE)

RULES: List[Rule] = [
    # ------ Language-agnostic (from references/general-legal.md) ------
    ("BLOCK", _c(r"\bthe present (?:agreement|contract|deed)\b"),
     "'the present agreement/contract/deed' is a civil-law calque. Use 'this Agreement' / 'this Contract' / 'this Deed' (general-legal.md).",
     ["*"]),
    ("BLOCK", _c(r"\bthis present (?:agreement|contract|deed)\b"),
     "'this present agreement' is a calque (often from NL 'deze onderhavige overeenkomst'). Use 'this Agreement' (general-legal.md; dutch-general-legal.md).",
     ["*"]),
    ("BLOCK", _c(r"\bauthenticating signature\b"),
     "'authenticating signature' is a calque (HU 'hitelesítő aláírás'). Use 'signature' or 'authorised signatory' (general-legal.md).",
     ["*"]),
    ("BLOCK", _c(r"\brepresentative acting on behalf of the\b"),
     "Verbose calque. Use 'authorised representative' (general-legal.md).",
     ["*"]),
    ("BLOCK", _c(r"\bduly invested with (?:the )?(?:necessary )?powers?\b"),
     "'duly invested with powers' is a civil-law calque. Use 'duly authorised' (general-legal.md).",
     ["*"]),
    ("BLOCK", _c(r"\bendowed with (?:the )?necessary powers?\b"),
     "Civil-law calque. Use 'duly authorised' (general-legal.md).",
     ["*"]),
    ("BLOCK", _c(r"\bon the basis of and pursuant to\b"),
     "Redundant stacking. Use 'pursuant to' (general-legal.md).",
     ["*"]),
    ("BLOCK", _c(r"\bbearing the date of\b"),
     "Verbose calque. Use '[Title], dated [date]' (general-legal.md).",
     ["*"]),
    ("BLOCK", _c(r"\bin the name and on behalf of\b"),
     "Stacked calque. Use 'on behalf of' unless the 'in the name of' distinction is intentional (general-legal.md).",
     ["*"]),
    ("BLOCK", _c(r"\b(?:plants|receivables|assets) existing and future\b"),
     "Civil-law adjective-after-noun word order. Use 'existing and future plants/receivables/assets' (general-legal.md).",
     ["*"]),
    ("BLOCK", _c(r"\bapplicant organisation:\s*$"),
     "Verbose on a cover page. Drop 'organisation' when the entity name makes it obvious (general-legal.md).",
     ["*"]),
    ("BLOCK", _c(r"\bfor the grant application entitled\b"),
     "Vague indirect phrasing on cover pages. Use 'Application under Call [ref]' (general-legal.md).",
     ["*"]),

    # UK signature-block label — this is a HARD RULE in general-legal.md
    # so we flag the alternatives. We only match them *when they look like
    # a signature-block label* (colon at end-of-line or followed by capitalised name).
    ("BLOCK", _c(r"(?m)^\s*(?:Position|Function|Capacity|Role)\s*:\s*[A-Z]"),
     "English signature-block label is 'Title:', never 'Position/Function/Capacity/Role:'. Re-label (general-legal.md).",
     ["*"]),

    # Headings — internal refs must be 'Clause', 'Article' is for legislation
    # Too easy to false-positive; only warn.
    # Flag 'Article N' only when it clearly is NOT a statutory/regulatory
    # reference: statutory refs include colons (civil-code style 'Article 2:24b'),
    # or are followed by 'of the ...', 'of Book', 'BW', 'of Directive', etc.
    ("WARN", _c(r"\bArticle\s+\d+(?:\.\d+)*\b"
                r"(?![\:\.]\d)"
                r"(?!\s*(?:of the|of Book|BW|of Directive|of Regulation|of the EU|of the European|of Law))"),
     "'Article N' for an internal reference is non-standard in UK legal drafting — prefer 'Clause N' unless this is a reference to legislation (general-legal.md).",
     ["*"]),

    # Date format under UK variant — we do not hard-block here (US output is supported).

    # ------ Dutch-specific (from sub-lexicons/dutch-*.md) ------
    ("BLOCK", _c(r"\bframework conditions?\b"),
     "'framework conditions' is a Eurospeak calque (NL 'randvoorwaarden'). Use 'conditions' or 'parameters' (dutch-general-legal.md; dutch-corporate-ma-jv.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bin more concrete terms\b"),
     "'in more concrete terms' is a calque (NL 'concretiseren'). Use 'set out' / 'specify' / 'flesh out' (dutch-general-legal.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\benvirons fund\b"),
     "'environs fund' is a calque (NL 'omgevingsfonds'). Use 'community fund' or 'local-impact fund' (dutch-energy-infrastructure.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bacceptance by the environs\b"),
     "'acceptance by the environs' is a calque (NL 'acceptatie door de omgeving'). Use 'acceptance by the local community' (dutch-energy-infrastructure.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bwind park\b"),
     "'Wind Park' is a calque (NL 'Windpark'). UK English is 'Wind Farm' (dutch-energy-infrastructure.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bsun park\b"),
     "Literal calque. Use 'Solar Farm' or 'PV plant' (dutch-energy-infrastructure.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bground rights\b"),
     "'ground rights' is a calque (NL 'grondrechten' in project context). Use 'land rights' (dutch-energy-infrastructure.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bground owners?\b"),
     "'ground owners' is a calque (NL 'grondeigenaren'). Use 'landowners' (dutch-energy-infrastructure.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bnet connection\b"),
     "'net connection' is a calque (NL 'netaansluiting'). Use 'grid connection' (dutch-energy-infrastructure.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bbehaviour code\b"),
     "'behaviour code' is a calque (NL 'gedragscode'). Use 'code of conduct' (dutch-energy-infrastructure.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bstriking shadow\b"),
     "'striking shadow' is a calque (NL 'slagschaduw'). Use 'shadow flicker' or 'flicker' (dutch-energy-infrastructure.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bsupport base\b"),
     "'support base' is a calque (NL 'draagvlak'). Use 'support' or 'public support' (dutch-energy-infrastructure.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\blandscape insertion\b"),
     "'landscape insertion' is a calque (NL 'landschappelijke inpassing'). Use 'landscape integration' (dutch-energy-infrastructure.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bgroup society\b"),
     "'group society' is a calque (NL 'groepsmaatschappij'). Use 'group company' (dutch-corporate-ma-jv.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\b(?:statutorily|legally) (?:established|domiciled) at\b"),
     "Calque. Use 'having its registered office at' (dutch-general-legal.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\blegally validly represented\b"),
     "Calque (NL 'ten deze rechtsgeldig vertegenwoordigd'). Use 'duly represented' (dutch-general-legal.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bputting in default\b"),
     "Calque (NL 'ingebrekestelling'). Use 'notice of default' (dutch-general-legal.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bsuspensive conditions?\b"),
     "Civil-law calque (NL 'opschortende voorwaarden'). Use 'conditions precedent' (dutch-general-legal.md; general-legal.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bresolutive conditions?\b"),
     "Civil-law calque (NL 'ontbindende voorwaarden'). Use 'conditions subsequent' (dutch-general-legal.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bsolidarily liable\b"),
     "Civil-law calque (NL 'hoofdelijk aansprakelijk'). Use 'jointly and severally liable' (dutch-general-legal.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bintent or gross fault\b"),
     "Calque (NL 'opzet of grove schuld'). Use 'wilful misconduct or gross negligence' (dutch-general-legal.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bequivalent partner\b"),
     "Calque (NL 'gelijkwaardige partner'). Use 'equal partner' (dutch-corporate-ma-jv.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bconcurrent activities\b"),
     "False-friend calque (NL 'concurrerende activiteiten' = competing). Use 'competing activities' (dutch-corporate-ma-jv.md).",
     ["dutch"]),
    ("BLOCK", _c(r"\bapproach plan\b"),
     "Calque (NL 'Plan van Aanpak'). Use 'Plan of Action' / 'Action Plan' (dutch-corporate-ma-jv.md).",
     ["dutch"]),
    ("WARN", _c(r"\bcooperation on an equal footing\b"),
     "Acceptable UK rendering of 'samenwerking op basis van gelijkwaardigheid' — this is a positive marker, not a violation. Retained here only so that reviewers can confirm the term is used consistently.",
     ["dutch"]),

    # ------ Italian-specific placeholders (for future work) ------
    ("BLOCK", _c(r"\blegislative changes\b(?!\s+(?:and|or))"),
     "Likely calque (IT 'Mutamenti Legislativi'). Use 'Change in Law' (FIDIC/PF standard) (italian-*.md).",
     ["italian"]),
    ("BLOCK", _c(r"\bfinancing institutions?\b"),
     "Literal calque (IT 'Istituti Finanziatori'). Use 'Finance Parties' (PF standard) (italian-*.md).",
     ["italian"]),
    ("BLOCK", _c(r"\bpenalties for delay\b"),
     "Calque (IT 'penali per ritardo'). Use 'delay damages' / 'liquidated damages for delay' (energy-infrastructure.md).",
     ["italian"]),
    ("BLOCK", _c(r"\bdefinitive project\b"),
     "Calque (IT 'progetto definitivo'). Use 'detailed design' (Stage 2) (energy-infrastructure.md).",
     ["italian"]),
    ("BLOCK", _c(r"\bexecutive project\b"),
     "Calque (IT 'progetto esecutivo'). Use 'construction design' (Stage 3) (energy-infrastructure.md).",
     ["italian"]),

    # ------ Spanish-specific (from sub-lexicons/spanish-*.md) ------
    # The sub-lexicon already prescribes "Notices" for Comunicación / Notificaciones
    # section headings; this rule enforces that explicitly on clause-heading lines.
    ("BLOCK", _c(r"(?m)^\s*(?:Clause\s+\d+\.?\s+)?Notification\s*$"),
     "Clause heading 'Notification' must be 'Notices' per spanish-general-legal.md (Section Headings / Universal Legal Terms: 'ALWAYS Notices; never Notification, never Communication').",
     ["spanish"]),
    ("BLOCK", _c(r"(?m)^\s*(?:Clause\s+\d+\.?\s+)?Communication\s*$"),
     "Clause heading 'Communication' must be 'Notices' per spanish-general-legal.md.",
     ["spanish"]),

    # Ley Común Española — classic false friend. Spain is a civil-law jurisdiction;
    # "common law" in English denotes the English common-law tradition.
    ("BLOCK", _c(r"\bSpanish\s+common\s+law\b"),
     "False friend for 'Ley Común Española'. Use 'Spanish general law' or 'Spanish law' — Spain is civil-law, not common-law (spanish-general-legal.md: False Friends).",
     ["spanish"]),

    # EXPONEN — standard English heading is RECITALS, not RECITE.
    ("BLOCK", _c(r"(?m)^\s*RECITE\s*$"),
     "Spanish 'EXPONEN' as a section heading should be 'RECITALS', not 'RECITE' (spanish-general-legal.md: Section Headings).",
     ["spanish"]),

    # Closing-formula calque.
    ("BLOCK", _c(r"\bfor\s+a\s+single\s+effect\b"),
     "Calque of 'a un solo efecto'. Use 'as a single instrument' or 'in [N] original counterparts' (spanish-general-legal.md: Closing Formulae).",
     ["spanish"]),

    # Passive-stack calque — warn only, since a narrow active-voice variant may appear.
    ("WARN", _c(r"\bshall\s+be\s+endeavoured\s+to\s+be\b"),
     "Awkward passive stack. Prefer active voice — 'the Parties shall seek to' / 'shall endeavour to' (spanish-general-legal.md: Dispute-Resolution Formulae).",
     ["spanish"]),
]

# --------------------------------------------------------------------------
# I/O helpers
# --------------------------------------------------------------------------

_WT = re.compile(r"<w:t(?:\s[^>]*)?>([^<]*)</w:t>")
_WDT = re.compile(r"<w:delText(?:\s[^>]*)?>([^<]*)</w:delText>")

def _extract_from_json(path: str) -> List[Tuple[str, int, str]]:
    """Return list of (field_label, idx, text) from a paragraphs.json."""
    out: List[Tuple[str, int, str]] = []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON array in {path}")
    for p in data:
        idx = p.get("idx", -1)
        en = p.get("en")
        if en:
            out.append(("en", idx, en))
        en_del = p.get("en_deleted")
        if en_del:
            out.append(("en_deleted", idx, en_del))
        for i, seg in enumerate(p.get("en_segments") or []):
            t = seg.get("en") if isinstance(seg, dict) else None
            if t:
                out.append((f"en_segments[{i}]:{seg.get('type','?')}", idx, t))
    return out

def _extract_from_xml(path: str) -> List[Tuple[str, int, str]]:
    """Return list of (field_label, seq, text) from a document.xml — treats
    w:t and w:delText content as separate streams so that a calque in
    deleted text is still surfaced."""
    with open(path, "r", encoding="utf-8") as f:
        xml = f.read()
    out: List[Tuple[str, int, str]] = []
    for seq, m in enumerate(_WT.finditer(xml)):
        t = m.group(1)
        if t.strip():
            out.append(("w:t", seq, t))
    for seq, m in enumerate(_WDT.finditer(xml)):
        t = m.group(1)
        if t.strip():
            out.append(("w:delText", seq, t))
    return out

def _extract(path: str) -> List[Tuple[str, int, str]]:
    if path.endswith(".json"):
        return _extract_from_json(path)
    if path.endswith(".xml"):
        return _extract_from_xml(path)
    # Allow docx too, for convenience
    if path.endswith(".docx"):
        import zipfile
        with zipfile.ZipFile(path) as z:
            with z.open("word/document.xml") as f:
                xml = f.read().decode("utf-8")
        out: List[Tuple[str, int, str]] = []
        for seq, m in enumerate(_WT.finditer(xml)):
            if m.group(1).strip():
                out.append(("w:t", seq, m.group(1)))
        for seq, m in enumerate(_WDT.finditer(xml)):
            if m.group(1).strip():
                out.append(("w:delText", seq, m.group(1)))
        return out
    raise ValueError(f"Unsupported input extension: {path}")

# --------------------------------------------------------------------------
# Scan
# --------------------------------------------------------------------------

def scan(entries: List[Tuple[str, int, str]], language: str) -> Tuple[List[str], List[str]]:
    """Return (blocking_messages, warning_messages)."""
    blocks: List[str] = []
    warns: List[str] = []
    lang = (language or "*").lower()
    for sev, pat, msg, langs in RULES:
        if "*" not in langs and lang not in langs and lang != "*":
            continue
        for field, idx, text in entries:
            m = pat.search(text)
            if not m:
                continue
            snippet = _ctx(text, m.start(), m.end())
            line = f"[{sev}] {field} idx={idx}: {msg}\n        …{snippet}…"
            if sev == "BLOCK":
                blocks.append(line)
            else:
                warns.append(line)
    return blocks, warns

def _ctx(text: str, a: int, b: int, radius: int = 40) -> str:
    s = max(0, a - radius)
    e = min(len(text), b + radius)
    chunk = text[s:e].replace("\n", " ")
    return chunk

# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="paragraphs.json, document.xml, or .docx to scan")
    ap.add_argument("--language", default="auto",
                    help="Source language (dutch, italian, etc.) — drives language-specific rules. "
                         "Default: 'auto' tries to read a language hint from the input; "
                         "'none' disables language-specific rules.")
    ap.add_argument("--stage", default="pre-repack",
                    choices=["pre-apply", "pre-repack"],
                    help="Advisory label printed in output; does not change rule selection.")
    ap.add_argument("--warnings-are-errors", action="store_true",
                    help="Treat WARN severity as BLOCK and fail on them too.")
    args = ap.parse_args(argv)

    path = args.path
    if not os.path.exists(path):
        print(f"lexicon_compliance: file not found: {path}", file=sys.stderr)
        return 2

    try:
        entries = _extract(path)
    except Exception as e:
        print(f"lexicon_compliance: failed to read {path}: {e}", file=sys.stderr)
        return 2

    # Language detection: if 'auto' and the path is a JSON, peek at a few source
    # paragraphs to guess. Very cheap — look for common Dutch/Italian markers.
    language = args.language
    if language == "auto":
        language = _guess_language(path)

    blocks, warns = scan(entries, language)
    if args.warnings_are_errors:
        blocks.extend(warns)
        warns = []

    print(f"Lexicon compliance scan — stage={args.stage}, language={language}, input={path}")
    print(f"  entries scanned: {len(entries)}")
    print(f"  blocking violations: {len(blocks)}")
    print(f"  warnings:            {len(warns)}")
    if warns:
        print("")
        print("Warnings:")
        for w in warns:
            print(f"  {w}")
    if blocks:
        print("")
        print("Blocking violations:")
        for b in blocks:
            print(f"  {b}")
        print("")
        print("  *** BLOCKED: resolve all BLOCK-severity findings before proceeding. ***")
        return 1
    print("  PASSED: no lexicon violations detected.")
    return 0

def _guess_language(path: str) -> str:
    """Best-effort source-language detection from a paragraphs.json or document.xml.

    The detector deliberately uses source-language markers that do NOT overlap
    with common English legal drafting vocabulary. Earlier versions of this
    function matched on bare " clause " / " article " for French — which
    collided with post-translation English output (every English clause
    contract contains "clause"/"article") and mis-tagged English XMLs as French.

    For JSON, the detector only looks at the `text` field (always the source
    language). For XML, it looks at all w:t content.
    """
    try:
        if path.endswith(".json"):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            sample = " ".join((p.get("text") or "")[:400] for p in data[:40] if isinstance(p, dict))
        elif path.endswith(".xml"):
            with open(path, "r", encoding="utf-8") as f:
                xml = f.read(40000)
            sample = " ".join(m.group(1) for m in _WT.finditer(xml))
        else:
            return "*"
        low = sample.lower()
        # Diacritic-based fingerprint first — cheap and strong signal for
        # Finnish, Hungarian, Polish, Portuguese, Spanish, German, French.
        # Count occurrences of language-unique characters.
        counts = {
            "finnish": sum(low.count(c) for c in "äöå"),
            "hungarian": sum(low.count(c) for c in "őűáéíóú"),
            "polish": sum(low.count(c) for c in "ąćęłńóśźż"),
            "portuguese": sum(low.count(c) for c in "ãõçâêôáéíóú"),
            "spanish": sum(low.count(c) for c in "ñ¿¡áéíóú"),
            "german": sum(low.count(c) for c in "äöüß"),
            "french": low.count("ç") + low.count("œ"),
        }
        # Chinese / Japanese — by codepoint range.
        has_cjk = any(0x4E00 <= ord(c) <= 0x9FFF for c in sample[:2000])
        has_hiragana = any(0x3040 <= ord(c) <= 0x309F for c in sample[:2000])
        has_katakana = any(0x30A0 <= ord(c) <= 0x30FF for c in sample[:2000])
        if has_hiragana or has_katakana:
            return "japanese"
        if has_cjk:
            return "chinese"

        # Source-language token markers that do NOT overlap with English legal
        # vocabulary. Each list intentionally excludes bare words like "clause",
        # "article", "agreement" that collide with English output.
        if any(k in low for k in [" overeenkomst", " bijlage", " partijen",
                                    " nederland", " stuurgroep", " coöperatie",
                                    " onderhavige", " wederpartij", " zijnde"]):
            return "dutch"
        if any(k in low for k in [" l'articolo", " fra le parti", " il presente",
                                    " contratto", " comunicazione di avvio",
                                    " ai sensi", " fermo restando", " nonché"]):
            return "italian"
        if any(k in low for k in [" yhtiö", " yhtiön", " sopimus", " sopimuksen",
                                    " tiekunta", " tiekunnan", " tuulivoima",
                                    " kiinteistö", " sekä ", " tämän ", " tässä ",
                                    " ehdossa", " mukaisesti"]):
            return "finnish"
        if any(k in low for k in [" der vertrag", " vertragspartner", " hiermit",
                                    " gesellschaft", " verpflichtet", " anlage"]):
            return "german"
        if any(k in low for k in [" la présente", " entre les parties",
                                    " société ", " le présent contrat",
                                    " nonobstant", " dénommé"]):
            return "french"
        if any(k in low for k in [" presente contrato", " conforme ",
                                    " nos termos ", " cláusula ", " sociedade "]):
            return "portuguese"
        if any(k in low for k in [" umowa", " umowy", " strona umowy",
                                    " zgodnie z", " niniejszą ", " spółka"]):
            return "polish"
        if any(k in low for k in [" jelen szerződés", " szerződő fél", " társaság",
                                    " képviseli", " kötelezett", " jogosult"]):
            return "hungarian"
        if any(k in low for k in [" el presente contrato", " las partes",
                                    " sociedad ", " en virtud de", " mediante"]):
            return "spanish"
        # Diacritic fallback — if nothing matched but we see a strong diacritic
        # signal, use that. Threshold = 5 to avoid single-loanword false hits.
        top = max(counts, key=counts.get)
        if counts[top] >= 5:
            return top
        return "*"
    except Exception:
        return "*"

if __name__ == "__main__":
    sys.exit(main())

# === SKILL FILE COMPLETE ===
