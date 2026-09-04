---
name: footnote-relegator
description: >-
  Condense a scholarly legal article by moving nonessential detail from the body into
  substantive footnotes while preserving every word and keeping the argument self-sufficient.
  Handles Markdown and Word (.docx), integrates moved material with existing notes, measures a
  user-specified relegation fraction (25% by default), and delivers a move-by-move memo. Use when
  asked to "push detail into footnotes," "relegate to footnotes," "footnote the caveats," "move
  the digressions down," or tighten a dense draft without deleting content. Word output requires
  file access plus document-conversion and rendering support; when those capabilities are
  unavailable, deliver Markdown and the memo or ask for a convertible source.
metadata:
  author: "Seth J. Chandler"
  author_link: "https://legaled.ai"
  license: "Apache-2.0"
  version: "2026-08-10"
  jurisdiction: "International"
  language: "English"
  category: "legal-drafting"
  requires: "File access; Python 3 for bundled checks; document conversion and rendering for Word output"
---

# Footnote Relegator

Take a scholarly article and make it two-tiered: a leaner main text that carries
the argument, and substantive footnotes that carry the detail. Nothing is
deleted — text is *moved*, near-verbatim, from body to notes.

## The governing principle

**The body must remain self-sufficient.** A reader who never glances at a
footnote should follow every step of the argument and lose nothing essential.
Footnotes carry enrichment, qualification, and apparatus — never a load-bearing
move. Every candidate demotion must pass this test in both directions:

- If removing the passage breaks the argument's chain, it stays in the body.
- If the passage would survive removal without any reader noticing a gap in
  reasoning, it is a demotion candidate.

The complementary test for the footnote side: each note must stand alone. A
reader who *does* drop down should find a self-contained mini-discussion, not a
fragment that only makes sense mid-paragraph.

## Inputs

1. **The article** — Markdown or .docx. (Other formats: convert to Markdown
   first with pandoc, then treat as Markdown; deliver back in the original
   format only if a faithful conversion exists.)
2. **The relegation fraction** — the share of original body-text words to move
   into footnotes. If the user gives a number ("relegate a third", "20%"), use
   it. **If the user says nothing, use 25%.** Body words means words in the
   main text excluding existing footnote/endnote content, headings kept as-is,
   and excluding tables, figures, and block quotes of primary sources (those
   are neither demoted nor counted).

### Capability preflight

Before promising output formats, check what the host can actually do.

1. If the user names a conversion or document-processing method, use it. If it is
   unavailable, say so and ask before substituting another method.
2. Otherwise use any connected or built-in document capability that can faithfully read,
   edit, render, and verify the source while keeping it local to the authorized workspace.
3. Otherwise use available local tools such as pandoc for conversion, Python 3 for the
   bundled scripts, and a Word-compatible renderer for visual checks.
4. If no faithful Word conversion and verification path exists, do not promise `.docx` or
   tracked changes. Offer Markdown plus the relegation memo; if the only input is `.docx`,
   ask the user for Markdown or another source the host can read faithfully.

For Markdown input, `scripts/ledger.py` is optional but preferred. If Python 3 is not
available, perform its conservation, word-count, and note-reference checks manually and
say that the automated check did not run.

## Hard rules (these define the skill — do not relax them)

1. **Move, never delete.** Every word that leaves the body lands in a
   footnote. If something seems worthless, it still moves; flagging it for the
   author's own deletion belongs in the memo, not in your edit.
2. **Near-verbatim.** Demoted text keeps its wording. Permitted edits are only
   those a passage needs to stand alone as a note: resolving pronouns whose
   referent stayed in the body, adjusting an opening connective ("Moreover,"
   → dropped or replaced), converting a sentence fragment into a sentence.
   Do not compress, paraphrase, or improve the author's prose.
3. **The body reads seamlessly.** After each removal, repair the seam:
   transitions, pronoun references, list continuity ("three reasons" → check
   all three still appear in the body or adjust the framing sentence — by
   moving framing too, not rewriting the claim).
4. **Citations travel with their sentences.** An inline citation or an
   existing footnote reference inside demoted text goes down with it (see
   integration rules). Never strand a citation from the claim it supports,
   and never lose one.

## Workflow

### Step 1 — Intake and measure

- Markdown: work on the file directly.
- .docx: extract with `pandoc article.docx -t markdown -o article.md`
  (footnotes arrive as `[^n]` — verify they did). Keep the original .docx
  untouched; you will need it for output.
- Count body words (see definition above) and compute the target:
  `target_words = fraction × body_words`. Land within about two percentage
  points of the requested fraction — this is a commitment the user gave a
  number for, not a vibe. `scripts/ledger.py` measures this for you; run it
  at the end, but you can also run it mid-edit to check progress.

### Step 2 — Classify

Walk the text sentence by sentence. Mark each unit **protected** or
**relegable** using `resources/demotion-rubric.md`. Read that file before
classifying — the protected list (thesis moves, chain-of-reasoning steps,
definitions used later, primary evidence, topic sentences) and the relegable
taxonomy (qualifications, compressed history, literature placement, source
criticism, counterexamples, secondary examples, methodological asides) with
worked micro-examples live there.

### Step 3 — Select to target

Build a **demotion ledger** before touching the text — a table of candidate
units: the text (or its first words), word count, rubric category, destination
(new note vs. merge into existing note N), and anchor sentence. Select
candidates until the ledger sums to the target, preferring:

- whole sentences and 2–3 sentence clusters over clause surgery;
- demotions spread across the article over gutting one section;
- the clearest rubric fits first — if you must reach for marginal candidates
  to hit the target, take the least load-bearing ones and say so in the memo.

If the article simply lacks enough relegable material to hit the fraction
without breaking the body (rare, but real for very lean texts), stop short,
and report the achieved fraction and the reason rather than demoting
load-bearing prose.

### Step 4 — Execute and repair

For each ledger entry, in document order:

1. Remove the unit from the body; place the note anchor at the end of the
   surviving sentence it enriches (after closing punctuation).
2. Write the footnote: the demoted text near-verbatim, standing alone.
3. Repair the seam in the body prose.
4. Check for orphaned back-references: "as noted above," "this exception,"
   "the second objection" — anything in the body that now points at text that
   moved. Fix by re-anchoring the reference or moving the referring phrase too.

### Step 5 — Integrate with existing footnotes

Read `resources/integration-rules.md` before this step. In brief: demoted
prose joins an existing citation-only note at the same anchor rather than
stacking a second flag on one sentence; same-subject textual notes merge;
footnote references inside demoted text fold into the destination note (no
notes-on-notes); numbering renumbers automatically in both Markdown and Word.

### Step 6 — Verify

Run the ledger script:

```
python scripts/ledger.py original.md revised.md --fraction 0.25
```

It reports achieved fraction vs. target, body/note word deltas, and — most
important — a **lost-text check**: any sentence that left the body and cannot
be found (near-verbatim) in a footnote is flagged. A flagged sentence means
you deleted instead of moved; fix it. Then re-read the revised *body only*,
start to finish, for flow — the machine checks conservation, only reading
checks seamlessness.

### Step 7 — Deliver

- **Markdown in → Markdown out**: revised `.md` with `[^n]` notes, plus the
  relegation memo.
- **.docx in → both of**: (a) a clean `.docx` with real auto-numbered Word
  footnotes, and (b) a tracked-changes redline of the original. See
  `resources/word-redline.md` for the full pipeline; the redline uses
  `scripts/docx_redline.py` against the unpacked original.
- **The relegation memo** (always): a short Markdown file listing every move —
  anchor location, first words of demoted text, word count, rubric reason —
  plus anything flagged as deserving the author's own attention (filler,
  candidates you declined and why, fraction shortfall if any). The memo is
  what lets the author veto individual moves; keep each entry scannable.

Name outputs after the source: `article-relegated.md` / `.docx`,
`article-redline.docx`, `article-relegation-memo.md`.

## Word documents: what to know before starting

After the capability preflight succeeds, the clean .docx can come from pandoc using the original as a style reference,
then a typography pass — pandoc's footnote style references are often
undefined in real-world documents, leaving full-size baseline note calls:

```
pandoc revised.md -o article-draft.docx --reference-doc=article.docx
python scripts/polish_footnotes.py article-draft.docx article-relegated.docx
```

The redline is real Word tracked changes produced by editing the original
document's XML — deletions wrapped in `<w:del>`, inserted note references in
`<w:ins>`, notes added to `word/footnotes.xml`. This preserves the author's
formatting exactly and lets them accept/reject each demotion in Word.
`resources/word-redline.md` has the step-by-step pipeline including a
host-capability fallback when dedicated Word verification tools are unavailable. Warn the user up front if the document contains pre-existing
tracked changes, comments, or cross-reference fields: pre-existing tracked
changes must be accepted (by the user) before relegation; fields referring to
moved text will need manual attention.

## Bundled resources

- `resources/demotion-rubric.md` — protected vs. relegable taxonomy with
  examples. Read before Step 2.
- `resources/integration-rules.md` — how demoted text merges with existing
  citation and textual footnotes. Read before Step 5.
- `resources/word-redline.md` — the .docx redline pipeline and its verification
  fallback. Read before
  producing Word output.
- `resources/worked-example.md` — a short before/after with its ledger and
  memo entries. Read if calibration feels uncertain, or the user asks what
  the output will look like.
- `scripts/ledger.py` — standard-library Markdown word accounting, conservation,
  and footnote-reference checks. Run in Step 6 when Python 3 is available.
- `scripts/docx_redline.py` — standard-library OOXML tracked-change editor. Read
  `resources/word-redline.md`, then run only for Word redline output.
- `scripts/polish_footnotes.py` — standard-library `.docx` typography pass for
  a pandoc-produced clean copy. Run only for Word clean-copy output.

## Relationship to tentacle-footnote-finder

If the user also has the `tentacle-footnote-finder` skill, the two compose:
that skill finds body sentences that deserve *expansion* footnotes; this one
*moves existing body text down*. The rubric here deliberately shares its
vocabulary (qualification, literature placement, source criticism, …). Do not
confuse the tasks: this skill writes footnotes only out of the author's own
existing words.

This companion is optional. Its absence does not change this skill's workflow or outputs.

## Jurisdiction

The demotion method is jurisdiction-neutral: it preserves an author's doctrine, citations,
and terminology rather than resolving legal questions. Citation forms, court rules, and
substantive propositions remain the author's and must be checked under the source's actual
jurisdiction. For that reason, catalogue jurisdiction is International.

## License and attribution

Copyright 2026 Seth J. Chandler. This original work is released under the Apache License
2.0. See `LICENSE` for the full terms and `NOTICE` for origin, code, and disclaimer details.

## Limitations and risks

- Relegation is an editorial judgment. A model can misclassify a necessary premise as a
  digression, weaken emphasis, or choose an awkward anchor even when no words are lost.
  The author must review the clean copy, redline, and memo before publication or filing.
- The conservation script uses approximate sentence splitting and fuzzy matching. A clean
  report does not prove that citations, defined terms, cross-references, bookmarks, fields,
  or note antecedents remain correct; perform the specified manual sweep.
- Word output depends on the host's ability to convert, render, and inspect OOXML. The
  bundled editor fails loudly on ambiguous text matches, but it does not replace opening
  both accepted and rejected views in a Word-compatible application.
- Drafts may contain privileged, confidential, personal, or embargoed material. Keep them
  within systems the user has authorized and do not upload them to a third-party service
  without informed approval.
- This skill supplies editorial assistance, not legal advice or citation validation. It
  does not determine whether the revised article is legally correct or ready to file.

The package contains three Python scripts. They use only the standard library, make no
network calls, spawn no subprocesses, and perform no dynamic evaluation. `ledger.py` is
read-only; `docx_redline.py` writes only inside the caller-named unpacked document directory;
and `polish_footnotes.py` uses a temporary directory and writes or replaces only the
caller-named output file.
