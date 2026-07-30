> **Pre-flight.** You should be entering this step having completed the previous step. **SKILL.md governs every step's discipline; if you have not read SKILL.md in full this session, STOP and `Read('SKILL.md')` before continuing.** Hard Rules from SKILL.md apply to this step too. **In Chat mode (no workspace folder, no auto-managed todo list) the same discipline applies — do not skim this step doc, do not bundle batches, do not skip the per-step Internal compliance check at the bottom.** **If this turn began from a compacted transcript, the compaction summary does NOT count as having read this step doc — `Read()` it now in full before any tool call.**

### Step 4b: Validate translations between batches

`validate_translations.py` runs after **every batch** in Step 4 to catch truncated
translations before the operator moves on. The final pre-apply pass that used to live
here is now auto-invoked inside Step 5 (`apply_translations_textmatch.py`), so there is
no separate Step 4b command after the last batch — Step 5 fires it automatically.

Per-batch invocation (still required after every batch in Step 4):

```bash
python <skill-path>/scripts/validate_translations.py <workdir>/paragraphs.json
```

The script reports:
- **PASS**: ratios acceptable — continue.
- **WARN** (exit 1): some paragraphs have low ratios — review and re-translate if genuinely
  incomplete; continuing is allowed.
- **BLOCK** (exit 2): one or more paragraphs are critically short — re-translate before
  proceeding.

**Pre-apply gates (TC documents) and post-apply token check run automatically inside
Step 5.** `apply_translations_textmatch.py` auto-invokes `validate_en_runs.py`
(definitions-section bold-italic gate) + `validate_segment_shapes.py`
+ `validate_reject_all.py` (TC docs only) at the start, and `validate_apply.py
--strict` at the end. The operator runs ONE command (Step 5) and gets all five gates
for free — there is no separate command for them and no flag to skip them.

For a manual pre-flight check before Step 5 (optional — the gates fire
automatically):

```bash
python <skill-path>/scripts/validate_segment_shapes.py <workdir>/paragraphs.json
python <skill-path>/scripts/validate_reject_all.py <workdir>/paragraphs.json
```

What each gate catches:

* **`validate_segment_shapes.py`** scans `en_segments` pair-wise and
  per-segment for XML-boundary risk shapes — an article or preposition
  in the wrong segment, a digit sitting exactly on a TC boundary, two
  alpha characters colliding across a boundary with no whitespace
  (Non-Latin script gotcha), a double-space straddling a boundary, an
  ins/del containing only a bare article, an internal camelCase
  collision. Each hit names the rule, points at the offending boundary,
  and suggests the rewrite.
* **`validate_reject_all.py`** reconstructs the accept-all and
  reject-all views from `en_segments` and scans both for mechanical
  readability defects — double articles (`the respective the`),
  repeated words, stranded prepositions, punctuation-then-letter
  run-together collisions, double spaces, empty brackets/quotes, and a
  list of forbidden collocations. Hits indicate an article /
  preposition / whitespace character sits on the wrong side of a TC
  boundary; see the "Reject-all grammar" subsection under Step 4 for
  the rewrite rule.

### Step 4c: Resolve broken cross-references

Source `.doc` files often contain broken field codes that render as "Error: Reference
source not found" in Word and survive into the translation if not addressed. Scan
`paragraphs.json` for any `text` field containing this string (or its source-language
equivalent). For each occurrence:

1. **Identify the intended target from context.** In definition paragraphs the pattern
   is "`[Defined Term]` has the meaning set out in Clause Error: Reference source not
   found" — the target clause is usually inferable from the term itself (e.g. "FAC" →
   the Final Acceptance clause, "Liquidated Damages" → the delay damages clause).
2. **Replace in the `en` field only** with the correct clause number (e.g. "Clause 8.1").
   Do NOT modify the `text` field — text matching depends on it staying intact.
3. **If the target is genuinely ambiguous**, render the error marker as
   "[cross-reference to be confirmed]" rather than carrying forward the raw error text.

### Step 4d: Lexicon compliance scan (pre-apply) — MANDATORY

Run the automated lexicon-compliance scan against `paragraphs.json` before
applying translations onto the document XML. The scan enforces the "Avoid"
columns of the reference lexicons and the language sub-lexicons, flagging any
calques or hard-rule violations that slipped into the `en` / `en_deleted` /
`en_segments` fields during drafting.

```bash
python <skill-path>/scripts/lexicon_compliance.py <workdir>/paragraphs.json --stage pre-apply
```

The script auto-detects the source language from the JSON; override with
`--language <name>` if needed, or `--language none` to apply only the
language-agnostic rules. Exit code 0 = clean, 1 = blocking violations, 2 = I/O
error.

**Do not proceed to Step 5 while the script exits 1.** For every blocking
finding:

1. Re-open the sub-lexicon file cited in the finding.
2. Locate the Avoid row.
3. Pick the correct rendering from the same row and patch the `en` (and
   `en_segments` if applicable) in `paragraphs.json`.
4. Re-run the compliance scan until it exits 0.

Warnings are printed but do not block — review them for context-dependent
false positives (e.g. an intentional reference to a statute using "Article N").

### State file (`.validate-state.json`) note
`validate_translations.py` writes a state file in the workdir to enforce
the per-batch cap and to audit batch coverage. Two operational notes:

1. **Do NOT `rm` the state file** to "reset" the validator. The sandbox
   may refuse the deletion with `Operation not permitted` because the file
   was created by the validator with restricted permissions. If you need
   to start a fresh validation pass, it's enough to leave the state file
   in place — the validator updates it. If you genuinely need to reset,
   use `python -c "import os; os.remove('.validate-state.json')"` from
   inside the workdir, which works in the sandbox where shell `rm` does
   not.
2. **The state file is document-scoped.** Each document gets its own
   workdir; the state file lives there. When you start a new document,
   the new workdir gets a new state file. Do not copy the state file
   from one document's workdir to another.

## Internal compliance check — 04b-translate-gates

Before moving to the next step, confirm:

- [ ] You ran `validate_translations.py` after each batch (mandatory)
- [ ] You resolved any cross-references flagged by Step 4c
- [ ] You ran the lexicon-compliance scan (Step 4d) and acted on any hits
- [ ] You did NOT skip a gate by passing override flags

If any check is uncertain, STOP. Re-read this file. Do not proceed.

**Next:** `skill-docs/05-apply.md`
