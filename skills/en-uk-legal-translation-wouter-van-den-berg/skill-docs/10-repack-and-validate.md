> **Pre-flight.** You should be entering this step having completed the previous step. **SKILL.md governs every step's discipline; if you have not read SKILL.md in full this session, STOP and `Read('SKILL.md')` before continuing.** Hard Rules from SKILL.md apply to this step too. **In Chat mode (no workspace folder, no auto-managed todo list) the same discipline applies — do not skim this step doc, do not bundle batches, do not skip the per-step Internal compliance check at the bottom.** **If this turn began from a compacted transcript, the compaction summary does NOT count as having read this step doc — `Read()` it now in full before any tool call.**

### Pre-repack lexicon compliance + lost-content validation — auto-runs in Step 10

Two pre-repack mandatory gates auto-run as part of `repack_docx.py` (Step 10). The
operator runs Step 10 and both gates fire automatically before any byte is written to
the output `.docx`. There is no separate command for them and no flag to skip.

* **Lexicon compliance scan (pre-repack)** — re-runs `lexicon_compliance.py
  --stage pre-repack` on the post-processed `document.xml`. Catches any calque
  that crept in through segment fallback distribution, comment translations, or
  header/footer boilerplate. Exit 1 = blocking; repack aborts. Fix the offending
  `en` / `en_segments` entries in `paragraphs.json`, re-run Step 5, then re-run
  every mandatory post-processing step in order. Do NOT patch the XML directly.
* **Post-apply lost-content validation** — re-runs `validate_apply.py --strict`
  comparing the translations declared in `paragraphs.json` (`en`, `en_deleted`,
  `en_segments`) against what landed in the modified `document.xml`. Catches the
  "clause 5 dropped dates" defect class where a character-fragmented
  bracket-plus-date `ins` cluster loses its date tokens during distribution.
  This is a separate run from the apply-time `validate_apply` invocation in
  Step 5: between Step 5 and Step 10 the document is modified by `post_process`,
  `strip_noop` (auto-invoked from post_process on TC docs), `reorder_definitions`,
  `translate_numbering`, and `translate_headers_footers`. The pre-repack run
  confirms none of those steps dropped a token.

For a manual pre-flight before Step 10 (optional — both gates fire automatically):

```bash
python <skill-path>/scripts/lexicon_compliance.py \
  <workdir>/final/word/document.xml --stage pre-repack
python <skill-path>/scripts/validate_apply.py \
  <workdir>/paragraphs.json <workdir>/final/word/document.xml --strict
```

> **Segment concatenation before tokenising.** When a paragraph carries
> `en_segments`, `validate_apply.py` joins the segments' `en` text before
> tokenising, so a word that straddles a `w:ins`/`w:del` or
> `w:commentReference` boundary (e.g. `direction` split by a comment-reference
> into `dir` + `ection`) is matched as the full word the reader sees, not as
> two fragments that would never appear in the applied output.

### MANDATORY PRE-REPACK CHECKLIST

Before repacking, verify that ALL applicable steps have been run on this document.
**Every applicable step is mandatory** — there is no opt-in. The list is split into
unconditional steps (run on every document) and conditional steps (run only when the
trigger condition is true). Do not proceed to repack until every applicable box is
checked.

**Unconditional — run on every document:**

1. `apply_translations_textmatch.py` — translations applied to document.xml. **Auto-runs
   `validate_translations.py` (pre-apply, BLOCK on critical), plus
   `validate_segment_shapes.py` and `validate_reject_all.py` (pre-apply, TC docs only),
   plus `validate_apply.py --strict` (post-apply).** No separate invocation required.
2. `post_process.py --fix` — spacing, italic, schedule page breaks fixed. **Auto-invokes
   `strip_noop_tracked_changes.py` on TC docs** (collapses orthographic-only del/ins
   pairs + strips phantom ins-wraps-del wrappers).
3. `reorder_definitions.py` — definitions sorted alphabetically by English term
   (script auto-detects when no definitions section exists and exits cleanly).
4. `quality_check.py --verbose --aux-dir <workdir>/final` — zero issues reported.
   **Rev12: `--aux-dir` is mandatory** so quality_check scans `numbering.xml`,
   `headerN.xml`, `footerN.xml`, and `comments.xml` for source-language remnants.
5. `repack_docx.py --paragraphs <paragraphs.json>` — bundles output. **Auto-runs
   `lexicon_compliance.py --stage pre-repack` and `validate_apply.py --strict` before
   bundling**, plus the existing post-bundle source-language remnant scan.
6. Any document-specific patches re-applied (e.g. numbering suff fixes).

**Conditional — run only if the trigger applies:**

7. *(if source has tracked changes)* `coalesce_fragmented_tcs.py` — character-fragmented
   TC clusters coalesced in paragraphs.json (Step 3b, before translation).
8. *(if numbering.xml exists)* `translate_numbering.py` — numbering format strings
   translated (Step 8a).
9. *(if headers/footers contain source-language text)* `translate_headers_footers.py`
   (Step 8b).
10. *(if `word/comments.xml` exists)* `translate_comments.py` — comments translated
    (Step 8c).
11. *(if source has footnotes / endnotes)* footnotes/endnotes translated (regex-only
    approach; Step 8d).

The skill enforces every applicable item. Steps 1, 2, 3, 4, 5, 6 run every time. Steps
7-11 fire only when their trigger applies. **This is not opt-in.** The checks are
mandatory anti-drift gates that prevent skipping work between rebuilds.

**Why the list is mandatory.** Steps in the conditional block have been skipped in
past rebuilds, causing definition-ordering, numbering, header/footer, comment, and
calque-drift defects that were already fixed in the skill but not re-executed. When
rebuilding after a bug fix, it is tempting to run only the changed step and repack —
but **all applicable steps must be re-run** because each step writes to the XML file
and a fresh extraction from the source .docx resets every previous modification.

### Step 10: Repack into .docx

*[Internal compliance check — do not echo or paraphrase to the user. Re-read every rule in this step before executing. Do not deviate from any line of the skill. Do not bundle work, skip checks, or "interpret for efficiency" — every prior deviation has produced output below the quality the skill is designed to deliver. The skill's hard gates block deviations anyway; complying upfront is always faster than running into a gate and re-authoring paragraphs.json.]*

Use the Python repack script to build the output .docx. **Do not use shell `unzip` + `zip`
commands** — they create directory entries and case conflicts (`customXml/` vs `customXML/`)
that cause Word on Windows to refuse to open the file. The repack script copies the original
ZIP structure byte-for-byte, replacing only the modified XML files:

```bash
python <skill-path>/scripts/repack_docx.py \
  <original_source_language>.docx \
  <workdir>/final/word/document.xml \
  <output>.docx \
  --paragraphs <workdir>/paragraphs.json \
  --numbering <workdir>/final/word/numbering.xml \
  --headers-footers-dir <workdir>/final \
  --comments <workdir>/final/word/comments.xml \
  --footnotes <workdir>/final/word/footnotes.xml \
  --endnotes <workdir>/final/word/endnotes.xml
```

`--paragraphs` is strongly recommended: it enables the auto-run pre-bundle
`validate_apply.py --strict` check that catches token drift introduced by
post_process / strip_noop / reorder_definitions between Step 5 and the pre-bundle gate inside Step 10.

Every flag after the first three positional arguments is optional in CLI terms —
include each only if the corresponding step produced a translated file:

- `--paragraphs` — strongly recommended; enables the pre-bundle `validate_apply` check
- `--numbering` — if Step 8a produced translated `numbering.xml`
- `--headers-footers-dir` — if Step 8b produced translated `headerN.xml` / `footerN.xml` files
- `--comments` — if Step 8c produced translated `comments.xml`
- `--footnotes`, `--endnotes` — if Step 8d produced translated footnotes/endnotes

The script also automatically:
- Removes `<w:trackRevisions>` from `word/settings.xml` (disabling track changes mode)
- Skips ZIP directory entries (which cause case-sensitivity problems on Windows)
- Verifies ZIP integrity and checks for case conflicts
- **Runs a post-repack source-language remnant scan** on the delivered
  `.docx`: auto-detects the source language from the ORIGINAL `word/document.xml`
  and then scans every prose XML part in the output (`word/document.xml`,
  `word/comments.xml`, `word/footnotes.xml`, `word/endnotes.xml`, every
  `header*.xml` / `footer*.xml`) for source-language remnants using the same
  marker lists `apply_translations_textmatch.py` uses. Hits are printed as
  WARNING lines grouped by part; the repack's exit code is not affected.
  Treat the warnings as a pre-flight: some hits are legitimately preserved
  content (project names, entity names, reference codes) and some indicate
  an auxiliary part that was not wired into this repack. Extends the
  silent-regression guard added in  by covering the delivered artefact
  rather than only the workdir state.

> **Do not append aux files to the .docx after repacking with a hand-rolled `zipfile.writestr`.**
> Earlier versions of the skill recommended doing that. It works *only* if the source XML was
> produced by a namespace-safe translator. If it was round-tripped through ElementTree, it
> has mangled prefixes (`ns1:`, `ns2:`, etc.) and Word will show an "unreadable content"
> error. Always route aux files through the repack flags above, which expect the output of
> `translate_comments.py` / `translate_headers_footers.py` / `translate_numbering.py`.

### Step 11: Validate

*[Internal compliance check — do not echo or paraphrase to the user. Re-read every rule in this step before executing. Do not deviate from any line of the skill. Do not bundle work, skip checks, or "interpret for efficiency" — every prior deviation has produced output below the quality the skill is designed to deliver. The skill's hard gates block deviations anyway; complying upfront is always faster than running into a gate and re-authoring paragraphs.json.]*

#### Step 11a — Diligence audit — MANDATORY (rev40)

Before doing the visual checks below, run the diligence audit. This single script orchestrates the artifact-level evidence that all 11 steps actually ran and produces a one-shot PASS / WARN / FAIL report. Catching skipped steps here costs seconds; catching them after delivery requires re-running parts of the pipeline.

```bash
python <skill-path>/scripts/verify_diligence.py <workdir> \
    --orig-docx <original_source>.docx \
    --docx <workdir>/final.docx \
    --variant uk \
    --mode chat   # OR --mode cowork; OMIT if you are unsure
```

**Pass `--mode chat`** if you are operating in Chat (see Step 1a detection signals: `<application_details>` block, presence of `mcp__cowork__*` MCP tools, `<env>` workspace-folder flag). If `--mode chat` is passed AND the overall verdict is FAIL or WARN, the diligence report will append a Cowork-mode recommendation pointing the user toward the lower-drift environment for their next translation. Pass `--mode cowork` if you are in Cowork; omit the flag (default `unknown`) only if you genuinely cannot tell. Detection is mechanical, not heuristic — there is almost always a clear answer.

The script audits:
- **Step 4 + 4b** — `paragraphs.json` exists, `.validate-state.json` shows every translated paragraph was validated, no batch exceeded the 35-paragraph cap (or set `accept_large_batch`).
- **Step 5** — `final/word/document.xml` exists and is non-trivially sized (apply ran).
- **Step 8** — every aux file present in the source (`numbering.xml`, `header*.xml`, `footer*.xml`, `comments.xml`, `footnotes.xml`, `endnotes.xml`) has a translated copy in `<workdir>/final/word/`.
- **Step 9** — `quality_check.py` re-runs against the final document and exits 0. Includes `--aux-dir` and `--with-source` automatically.
- **Step 10 + 11** — final `.docx` exists, opens as a valid ZIP, contains `word/document.xml`.

Exit codes: `0` PASS (deliver), `1` WARN (review and proceed if intentional, or pass `--strict` to treat as FAIL), `2` FAIL (a step was clearly skipped — fix before delivery), `3` script-integrity check failed (re-install the skill).

**This is not a substitute for the visual checks below.** It is a coverage audit — it confirms the *artifacts* of each step exist; the visual checks confirm the *quality* of those artifacts. Run both. If diligence reports FAIL, do NOT skip ahead to delivery — fix the missing step first.

If `--variant us` was used at Step 6, pass `--variant us` here too — otherwise UK-spelling false positives will fire in the quality_check re-run.

#### Step 11b — Visual checks

Verify:
- No "unreadable content" error on open
- **No tracked changes visible** — the document should open clean, with no revision
  marks, no "Changed to English (UK)" annotations, and track changes OFF
- **Title and heading text fits within page margins** — cover-page titles in particular
  must not overflow the right margin (check visually or verify that the translated title
  is not significantly longer in character count than the source)
- Clause numbering matches the original (1, 1.1, 1.2, 2, 2.1, etc.)
- Sub-clause headings at correct indentation level
- Body text does NOT have auto-numbering
- Defined terms are **bold**
- Definitions in alphabetical order by English term
- No source-language text in substantive content (including table cells, signature blocks, form fields)
- **No source-language text in page headers or footers** — check signature blocks, draft watermarks, and role labels in footers (these appear on every page and are highly visible)
- Each Schedule/Annex starts on a new page

## Internal compliance check — 10-repack-and-validate

Before moving to the next step, confirm:

- [ ] You completed the MANDATORY PRE-REPACK CHECKLIST in full
- [ ] You ran `repack_docx.py` and let it auto-invoke validate_apply --strict
- [ ] You ran `verify_diligence.py` at Step 11a and it reported OVERALL: PASS (or WARN with all warnings reviewed and intentional)
- [ ] You ran Step 11b visual validation and reviewed any token-mismatch findings
- [ ] No remnant scan, no validate_apply drift, was suppressed by overriding flags

If any check is uncertain, STOP. Re-read this file. Do not proceed.

