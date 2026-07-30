#!/usr/bin/env python3
"""Detect character-fragmented tracked-change clusters in paragraphs.json and
scaffold the en_segments array for the translator.

Problem
-------
Civil-law concept drafts sometimes edit a single word or ordinal letter by
letter, producing a tc_segments array with many character-level splits that
map to one conceptual edit in English. Because English normally replaces the
whole word (not character ranges), the segment-aware translator cannot cleanly
map source character segments onto English without orphan letters leaking into
the redline view.

Canonical example (Spanish road-use draft):
  Source clause heading changed from "Duodécima" to "Decimotercera".
  OOXML stores 7 interleaved runs for that one edit:
    [ins "D"], [del "Duod"], [ins "e"], [del "é"],
    [regular "cim"], [ins "otercera"], [del "a"],
    [regular ".- Legislación, Fuero y jurisdicción"]
  The intended English edit is a simple 2-token replacement:
    del = "Clause 12"   ins = "Clause 13"
  plus the untouched trailing ".- Legislación…" → ". Governing law…"

What this script does
---------------------
For each paragraph with `has_track_changes: true`, it scans `tc_segments`
looking for contiguous clusters of ins/del/regular entries that (a) contain at
least 3 ins+del pieces and at least one of each, (b) have no whitespace in any
piece, and (c) reassemble on each of the Accept and Reject sides into a
coherent single word (different on each side).

When a cluster is found, the script writes a pre-filled `en_segments` skeleton
into the paragraph, matching the original tc_segments type pattern 1-for-1
(because the XML still has those runs). Inside the detected cluster it places:

  - on the **first `ins` segment**: a placeholder like
        `<<TRANSLATE: ins='Decimotercera' (accepted)>>`
  - on the **first `del` segment**: a placeholder like
        `<<TRANSLATE: del='Duodécima' (rejected)>>`
  - on **every other cluster segment**: the empty string `""`.

Outside the cluster, the script leaves `en` fields empty (so the translator
still writes them) — but each tc_segment that carries non-cluster text is
exposed in the skeleton so the translator sees the whole paragraph at once.

The translator then replaces the `<<TRANSLATE: …>>` placeholders with the
final English (`"Clause 13"` / `"Clause 12"`) and fills the remaining empty
`en` fields for non-cluster segments. The empty strings inside the cluster
carry through to apply time, where `apply_translations_textmatch.py` clears
the matching XML runs (v2024+ empty-string behaviour), producing a clean
Accept/Reject redline.

Structural fields that the script does NOT touch: `text`, `deleted_text`,
`tc_segments`, `has_track_changes`. Any existing `en_segments` is overwritten
only if the script actually detects a cluster; paragraphs without clusters
are untouched entirely.

Usage
-----
    python coalesce_fragmented_tcs.py <paragraphs.json> [--dry-run]
                                                        [--min-pieces N]

Run AFTER extract_paragraphs.py (Step 2) and BEFORE translation (Step 4).
Idempotent; re-running replaces the scaffolding on the same clusters and is a
no-op on paragraphs that have no fragmented clusters.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import os

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



PLACEHOLDER_PREFIX = "<<TRANSLATE: "

def _is_wordlike(s: str) -> bool:
    """True if s is a single 'word-like' token: no internal whitespace, at
    least one alphabetic character, plausibly a single edited token."""
    if not s or len(s) > 80:
        return False
    stripped = s.strip()
    if not stripped or re.search(r"\s", stripped):
        return False
    if not re.search(r"[^\W\d_]", stripped, flags=re.UNICODE):
        return False
    return True

def _find_clusters(tc_segments: list[dict], min_pieces: int) -> list[tuple[int, int]]:
    """Return (start_idx, end_idx_inclusive) ranges of fragmented clusters.

    A cluster is a maximal run of adjacent segments whose individual texts
    have no whitespace, and whose concatenations by side (Accept = non-del,
    Reject = non-ins) both read as coherent single words — different from
    each other — and which contains at least `min_pieces` ins+del entries
    with at least one ins and one del."""
    clusters: list[tuple[int, int]] = []
    n = len(tc_segments)
    i = 0
    while i < n:
        seg = tc_segments[i]
        text = seg.get("text", "") or ""
        if re.search(r"\s", text) or len(text) > 60:
            i += 1
            continue
        j = i
        ins_count = del_count = 0
        while j < n:
            s = tc_segments[j]
            t = s.get("text", "") or ""
            if re.search(r"\s", t) or len(t) > 60:
                break
            if s.get("type") == "ins":
                ins_count += 1
            elif s.get("type") == "del":
                del_count += 1
            j += 1
        if (
            j - i >= 2
            and ins_count + del_count >= min_pieces
            and ins_count >= 1
            and del_count >= 1
        ):
            accepted = "".join((s.get("text") or "") for s in tc_segments[i:j]
                               if s.get("type") != "del")
            rejected = "".join((s.get("text") or "") for s in tc_segments[i:j]
                               if s.get("type") != "ins")
            if (_is_wordlike(accepted) and _is_wordlike(rejected)
                    and accepted != rejected):
                clusters.append((i, j - 1))
                i = j
                continue
        i = j if j > i else i + 1
    return clusters

def _build_en_segments_skeleton(tc_segments: list[dict],
                                clusters: list[tuple[int, int]],
                                direct_ins_en: str | None = None,
                                direct_del_en: str | None = None) -> list[dict]:
    """Generate an en_segments array of the SAME length and type pattern as
    tc_segments, populated with:
      - '' (empty) for cluster segments other than the first ins / first del
      - on the first ins / first del of each cluster: either a TRANSLATE
        placeholder (default) or, if direct_ins_en/direct_del_en are given
        AND there is exactly ONE cluster, the final English text directly.
      - '' (empty) for non-cluster segments (translator fills these)
    """
    en_segs: list[dict] = [
        {"type": s.get("type"), "en": ""} for s in tc_segments
    ]

    direct_fill = (
        direct_ins_en is not None
        and direct_del_en is not None
        and len(clusters) == 1
    )

    for start, end in clusters:
        accepted = "".join((tc_segments[k].get("text") or "")
                           for k in range(start, end + 1)
                           if tc_segments[k].get("type") != "del")
        rejected = "".join((tc_segments[k].get("text") or "")
                           for k in range(start, end + 1)
                           if tc_segments[k].get("type") != "ins")
        first_ins = next(
            (k for k in range(start, end + 1)
             if tc_segments[k].get("type") == "ins"),
            None,
        )
        first_del = next(
            (k for k in range(start, end + 1)
             if tc_segments[k].get("type") == "del"),
            None,
        )
        if first_ins is not None:
            if direct_fill:
                en_segs[first_ins]["en"] = direct_ins_en
            else:
                en_segs[first_ins]["en"] = (
                    f"{PLACEHOLDER_PREFIX}ins='{accepted}' (accepted)>>"
                )
        if first_del is not None:
            if direct_fill:
                en_segs[first_del]["en"] = direct_del_en
            else:
                en_segs[first_del]["en"] = (
                    f"{PLACEHOLDER_PREFIX}del='{rejected}' (rejected)>>"
                )
        # All other cluster segments keep en='' so apply will clear the
        # corresponding runs. This is the whole point.

    return en_segs

def process_paragraph(p: dict, min_pieces: int,
                      report: list[str],
                      direct_ins_en: str | None = None,
                      direct_del_en: str | None = None) -> bool:
    if not p.get("has_track_changes"):
        return False
    tcs = p.get("tc_segments")
    if not tcs or not isinstance(tcs, list):
        return False
    clusters = _find_clusters(tcs, min_pieces)
    if not clusters:
        return False
    skeleton = _build_en_segments_skeleton(
        tcs, clusters,
        direct_ins_en=direct_ins_en,
        direct_del_en=direct_del_en,
    )
    p["en_segments"] = skeleton
    for (start, end) in clusters:
        accepted = "".join((tcs[k].get("text") or "")
                           for k in range(start, end + 1)
                           if tcs[k].get("type") != "del")
        rejected = "".join((tcs[k].get("text") or "")
                           for k in range(start, end + 1)
                           if tcs[k].get("type") != "ins")
        report.append(
            f"  idx={p.get('idx')}: fragmented cluster segments[{start}..{end}] "
            f"=> rejected='{rejected}' / accepted='{accepted}'"
        )
    return True

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        description="Detect character-fragmented TC clusters and scaffold en_segments."
    )
    ap.add_argument("paragraphs_json")
    ap.add_argument("--dry-run", action="store_true",
                    help="Report without modifying the file.")
    ap.add_argument("--min-pieces", type=int, default=3,
                    help="Minimum ins+del count per cluster (default: 3).")
    # Direct-fill shortcut for whole-word clusters (the only scenario observed
    # in practice: clause renumbering like "Duodécima" → "Decimotercera").
    # When --idx/--ins-en/--del-en are all passed, the script writes the final
    # English directly into the scaffold instead of a TRANSLATE placeholder.
    # Requires --idx so the fill only touches a single, unambiguous cluster.
    ap.add_argument("--idx", type=int, default=None,
                    help="Paragraph idx to target for direct --ins-en/--del-en fill. "
                         "Required when --ins-en or --del-en is used.")
    ap.add_argument("--ins-en", default=None,
                    help="English text for the accepted (ins) side of a whole-word "
                         "cluster. Requires --idx and --del-en.")
    ap.add_argument("--del-en", default=None,
                    help="English text for the rejected (del) side of a whole-word "
                         "cluster. Requires --idx and --ins-en.")
    args = ap.parse_args(argv)

    # Validate direct-fill usage.
    _direct_flags = [args.ins_en, args.del_en]
    if any(f is not None for f in _direct_flags):
        if args.idx is None:
            ap.error("--ins-en/--del-en require --idx <paragraph_idx>.")
        if any(f is None for f in _direct_flags):
            ap.error("--ins-en and --del-en must be used together.")

    try:
        with open(args.paragraphs_json, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR reading {args.paragraphs_json}: {e}", file=sys.stderr)
        return 2

    report: list[str] = []
    touched = 0
    direct_applied = False
    for p in data:
        # Route direct-fill args only to the targeted paragraph idx. Every
        # other paragraph still gets the placeholder scaffold.
        if (args.idx is not None and args.ins_en is not None
                and p.get("idx") == args.idx):
            tcs = p.get("tc_segments") or []
            clusters = _find_clusters(tcs, args.min_pieces)
            if len(clusters) != 1:
                print(
                    f"ERROR: --idx={args.idx} has {len(clusters)} fragmented "
                    f"cluster(s); --ins-en/--del-en only supports paragraphs with "
                    f"exactly one cluster. Use placeholder mode (omit --ins-en/--del-en).",
                    file=sys.stderr,
                )
                return 2
            if process_paragraph(p, args.min_pieces, report,
                                 direct_ins_en=args.ins_en,
                                 direct_del_en=args.del_en):
                touched += 1
                direct_applied = True
            continue
        if process_paragraph(p, args.min_pieces, report):
            touched += 1

    if args.idx is not None and args.ins_en is not None and not direct_applied:
        print(
            f"ERROR: --idx={args.idx} did not match any fragmented-cluster "
            "paragraph (no ins/del cluster detected at that idx).",
            file=sys.stderr,
        )
        return 2

    if not report:
        print("No character-fragmented TC clusters detected. Nothing to do.")
        return 0

    print(f"Detected fragmented clusters in {touched} paragraph(s):")
    for line in report:
        print(line)

    print()
    print("Scaffolded en_segments on each flagged paragraph. At translation time:")
    print(f"  1. Replace each '{PLACEHOLDER_PREFIX}…>>' placeholder with the final English")
    print("     (e.g. 'Clause 13' on the ins side, 'Clause 12' on the del side).")
    print("  2. Fill the remaining empty 'en' fields for non-cluster segments with")
    print("     normal English translations — but do NOT populate the empty-string")
    print("     slots inside the cluster; those must stay as '' so apply_translations_")
    print("     textmatch.py can clear the matching source runs.")

    if args.dry_run:
        print()
        print("(--dry-run: no file written)")
        return 0

    with open(args.paragraphs_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print()
    print(f"Wrote scaffolded JSON to {args.paragraphs_json}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# === SKILL FILE COMPLETE ===
