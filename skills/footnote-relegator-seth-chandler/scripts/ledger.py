#!/usr/bin/env python3
"""Verify a footnote relegation: word accounting + lost-text check.

Usage:
    python ledger.py original.md revised.md [--fraction 0.25] [--json]

Both files are pandoc-style Markdown where footnotes are defined as

    [^label]: note text
        possibly continued on indented lines

Reports:
  * body words before/after, note words before/after
  * achieved relegation fraction vs. target (words moved / original body words)
  * LOST TEXT: original body sentences absent from the revised body that
    cannot be found (near-verbatim, fuzzy-matched) in any revised footnote
  * footnote references without definitions and vice versa

Exit code 1 if text was lost or the fraction misses target by more than
2 percentage points; 0 otherwise.
"""

import argparse
import difflib
import json
import re
import sys

FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:[ \t]?(.*)$")
FOOTNOTE_REF = re.compile(r"\[\^([^\]]+)\]")
HEADING = re.compile(r"^#{1,6}\s")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")


def split_body_and_notes(text):
    """Return (body_text, {label: note_text})."""
    lines = text.splitlines()
    body, notes = [], {}
    current = None
    for line in lines:
        m = FOOTNOTE_DEF.match(line)
        if m:
            current = m.group(1)
            notes[current] = m.group(2)
            continue
        if current is not None and (line.startswith(("    ", "\t")) or line.strip() == ""):
            # continuation of a note (blank lines inside notes are ambiguous;
            # treat a blank followed by an indented line as continuation)
            if line.strip() == "":
                notes[current] += "\n"
            else:
                notes[current] += "\n" + line.strip()
            continue
        current = None
        body.append(line)
    return "\n".join(body), notes


def strip_markup(text):
    text = FOOTNOTE_REF.sub("", text)
    text = re.sub(r"[*_`>#\[\]()|]", " ", text)
    return text


def prose_lines(body):
    """Body minus headings, tables, and block quotes."""
    kept = []
    for line in body.splitlines():
        if HEADING.match(line) or TABLE_ROW.match(line) or line.lstrip().startswith(">"):
            continue
        kept.append(line)
    return "\n".join(kept)


def countable_body_words(body):
    return len(strip_markup(prose_lines(body)).split())


def note_words(notes):
    return sum(len(strip_markup(t).split()) for t in notes.values())


def sentences(text):
    """Crude sentence split, good enough for matching."""
    text = strip_markup(text)
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(])", text)
    return [p.strip() for p in parts if len(p.split()) >= 5]


def normalize(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s.lower())).strip()


def fuzzy_in(needle, haystacks, threshold=0.75):
    n = normalize(needle)
    if not n:
        return True
    for h in haystacks:
        hn = normalize(h)
        if n in hn:
            return True
        # windowed ratio: compare against the note as a whole
        if difflib.SequenceMatcher(None, n, hn).ratio() >= threshold:
            return True
        # also compare sentence-by-sentence within the note
        for hs in sentences(h):
            if difflib.SequenceMatcher(None, n, normalize(hs)).ratio() >= threshold:
                return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("original")
    ap.add_argument("revised")
    ap.add_argument("--fraction", type=float, default=0.25)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    orig = open(args.original, encoding="utf-8").read()
    rev = open(args.revised, encoding="utf-8").read()

    obody, onotes = split_body_and_notes(orig)
    rbody, rnotes = split_body_and_notes(rev)

    ob, rb = countable_body_words(obody), countable_body_words(rbody)
    on, rn = note_words(onotes), note_words(rnotes)
    moved = ob - rb
    achieved = moved / ob if ob else 0.0

    # lost-text check: original body sentences missing from revised body
    rbody_norm = normalize(strip_markup(prose_lines(rbody)))
    rev_note_texts = list(rnotes.values())
    rbody_sents = sentences(prose_lines(rbody))
    lost, split_moves, repaired, moved_ok = [], [], [], 0
    for s in sentences(prose_lines(obody)):
        if normalize(s) in rbody_norm:
            continue
        # still in body but reworded (seam repair)?
        if any(difflib.SequenceMatcher(None, normalize(s), normalize(rs)).ratio() >= 0.8
               for rs in rbody_sents):
            repaired.append(s)
            continue
        # sentence left the body — is it (near-verbatim) in some note?
        if fuzzy_in(s, rev_note_texts):
            moved_ok += 1
            continue
        # clause-level split? check fragments against body + notes together
        frags = [
            re.sub(r"^(and|but|or|yet|though|while|whereas)\s+", "", f, flags=re.I)
            for f in re.split(r",\s+|;\s+|:\s+", s)
        ]
        frags = [f for f in frags if len(f.split()) >= 4]
        if frags and all(
            normalize(f) in rbody_norm or fuzzy_in(f, rev_note_texts)
            for f in frags
        ):
            split_moves.append(s)
        else:
            lost.append(s)

    # reference/definition consistency in revised doc
    refs = set(FOOTNOTE_REF.findall(rbody)) | {
        r for t in rnotes.values() for r in FOOTNOTE_REF.findall(t)
    }
    defs = set(rnotes)
    dangling = sorted(refs - defs)
    orphaned = sorted(defs - set(FOOTNOTE_REF.findall(rbody)))
    nested = sorted(r for t in rnotes.values() for r in FOOTNOTE_REF.findall(t))

    report = {
        "body_words": {"original": ob, "revised": rb, "moved": moved},
        "note_words": {"original": on, "revised": rn, "added": rn - on},
        "fraction": {"target": args.fraction, "achieved": round(achieved, 4)},
        "fraction_ok": abs(achieved - args.fraction) <= 0.02,
        "sentences_moved_and_found": moved_ok,
        "split_moves_verify_manually": split_moves,
        "seam_repaired_in_body": repaired,
        "lost_sentences": lost,
        "dangling_refs": dangling,
        "unreferenced_notes": orphaned,
        "refs_inside_notes": nested,
    }

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        f = report["fraction"]
        print(f"Body words: {ob} -> {rb}  (moved {moved})")
        print(f"Note words: {on} -> {rn}  (added {rn - on})")
        print(f"Fraction:   achieved {achieved:.1%} vs target {f['target']:.1%}"
              f"  [{'OK' if report['fraction_ok'] else 'MISS'}]")
        print(f"Moved sentences found in notes: {moved_ok}")
        if repaired:
            print(f"\nSeam-repaired body sentences (confirm each was intended): {len(repaired)}")
            for s in repaired:
                print(f"  ~ {s[:120]}")
        if split_moves:
            print(f"\nSplit moves (clause-level; verify each by eye): {len(split_moves)}")
            for s in split_moves:
                print(f"  ~ {s[:120]}")
        if lost:
            print(f"\nLOST TEXT — {len(lost)} sentence(s) left the body and "
                  f"were not found in any footnote:")
            for s in lost:
                print(f"  - {s[:120]}")
        if dangling:
            print(f"\nDangling footnote refs (no definition): {dangling}")
        if orphaned:
            print(f"Unreferenced footnote definitions: {orphaned}")
        if nested:
            print(f"Footnote refs inside notes (notes-on-notes): {nested}")
        if not (lost or dangling):
            print("\nConservation check passed: nothing deleted, all refs defined.")

    sys.exit(1 if (lost or not report["fraction_ok"]) else 0)


if __name__ == "__main__":
    main()
