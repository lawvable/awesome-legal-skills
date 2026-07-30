---
name: legal-translation
metadata:
  author: "Wouter van den Berg - wouter@monteclima.com - linkedin.com/in/wjvandenberg"
  license: "mit"
  version: "2026-05-12"
description: >
  Translate legal documents from any language into English while preserving .docx formatting
  and translating track changes and headers/footers. Use this skill whenever the user asks to
  translate a legal document, contract, deed, agreement, or any formal legal text into English.
  Also trigger when the user mentions translating .docx files that contain legal content, or
  asks for a "format-preserving translation" of a legal document. This skill covers all legal
  domains: finance, M&A, corporate, IP, real estate, regulatory, consumer, taxes, litigation,
  SaaS and more. Even if the user just says "translate this contract" or "translate this into
  English", use this skill if the document is legal in nature.
---

# Legal Document Translation Skill

Translate legal documents from any language into publication-quality English while preserving
all original .docx formatting (fonts, styles, headers, tables, numbering, etc.).

## Pre-step checkpoint — read this whole file before doing anything

This skill's discipline depends on you actually reading SKILL.md, not just having it loaded in context. Before performing any step (Step 1 through Step 11), post a single short confirmation line in chat: **"Understanding of skill discipline is confirmed, now initiating translation process."** (use this exact wording). Do NOT print the technical details (Hard Rules location, validator names, step files) — the user does not want a wall of internal-state text. The act of writing the confirmation line is what proves you are at the right place; keep it terse.

If, while you are about to type the line, you realise you cannot from memory name (a) where the Hard Rules block lives, (b) which validators auto-invoke from `apply_translations_textmatch.py` (there are four), or (c) the file containing the step you are about to perform — **STOP**, `Read('SKILL.md')` again slowly, then post the one-line confirmation. Internal verification is required; user-facing display of that verification is not.

### Compaction-resume trigger — treat as session start

If this turn began from a **compacted transcript** (signs: a system message describing prior work, a "summary" preface, a "This session is being continued from a previous conversation that ran out of context" header, or any context indicating that work has progressed without you having `Read('SKILL.md')` in *this* turn), you MUST treat the resume as session start. **Compaction summaries are NOT a substitute for the actual rules.** A summary may compress a 100-line rule into one line, drop the qualifier that bites in the case at hand, or omit the appendix that contains the answer to the failure mode you are about to hit.

Concretely, on every compaction-resume, before any tool call:

1. `Read('SKILL.md')` in full.
2. `Read()` the active step doc you are about to operate on.
3. `Read()` any lexicon / sub-lexicon you were using before compaction.
4. Post the one-line "Understanding of skill discipline is confirmed, now initiating translation process." before resuming work.

This is **not** "re-reading what you already read"; it is reading what you have NOT read in this turn. The Mandatory Reading Order applies on every compaction-resume, identically to first session start. **Never trust a compaction summary's paraphrase of a rule** — if the summary names a rule, go to the file and read the rule's exact text before applying it.

## Do not ask the user — these are absolute defaults

The following are **non-negotiable defaults**. Do NOT pause to ask the user about them. Proceed silently with the default; only switch if the user has already given an explicit instruction in their original request. If you find yourself drafting a clarifying question about any of these, stop — the question is the wrong move:

1. **UK English is the standard.** Always translate into UK English. The only switch to US English is if the user already said so explicitly in their request (phrases like "translate into US English", "use American English"). Do not ask whether to use UK or US. Do not pre-emptively confirm. Just translate into UK English and, if you want, mention in the delivery message that US English is available on request.
2. **Sequential, single-context translation is the only mode.** When translating one document, or multiple documents in one session, just proceed sequentially in the main context window. Do NOT ask "shall I proceed sequentially?" or "the skill mandates sequential — how would you like me to proceed?" — sequential is the only mode. Only ask the user if THEY explicitly request sub-agents / parallelism, in which case warn them about quality risk and recommend sequential.
3. **All 11 steps for one document, then start the next.** When translating multiple documents, complete the full pipeline (Steps 1 through 11, including final repack and validation) for Document 1 before beginning Step 1 of Document 2. Do NOT translate two documents in parallel batches, do NOT defer Document 1's repack to "do them together." Each document is its own sequential run.
4. **35-paragraph batch cap is mandatory** (enforced by `validate_translations.py`). Do not ask whether to use a larger batch.
5. **`en_runs` on every definitions-section paragraph is mandatory** (enforced by `validate_en_runs.py`). Do not ask.
6. **Auto-invoked validators always run.** Do not ask whether to skip a gate. Do not pass override flags unless the user has explicitly approved (e.g. `--allow-bold-loss` for known-acceptable bold loss).
7. **Per-document refresh is mandatory.** When starting a new document in the same session, re-`Read('SKILL.md')`, re-`Read()` each step file as you arrive at it, and re-`Read()` the relevant lexicons and sub-lexicons. Do not ask.

8. **Compaction-resume re-read is mandatory.** If the turn began from a compacted transcript, `Read('SKILL.md')` and the active step doc before any tool call. Compaction summaries are NOT a substitute for the actual rules (see "Compaction-resume trigger" subsection above). Do not ask.

9. **Chat-mode does not relax discipline.** In Chat mode (no workspace folder, no auto-managed todo list), the same 11 steps, the same `paragraphs.json` checkpoint, the same per-batch validator, and the same Mandatory Reading Order all apply identically (see "Chat-mode discipline" in Anti-drift safeguards). Do not ask whether shortcuts are acceptable in Chat — they are not.

If the user explicitly overrides any of these, follow the user — but never invent a clarifying question.

## Multi-document workflow

If you translate **more than one document in the same Claude session**, treat each document as a fresh workflow start. Even when the documents are similar (same project, same parties, same domain), the per-document refresh is non-negotiable:

1. **Complete all 11 steps for Document 1 before starting Document 2.** Do NOT batch the translations across documents (translate Doc 1 + Doc 2 in interleaved batches), do NOT defer the repack of Document 1 to "do them together later," and do NOT split verification or the final delivery between documents. Each document is its own sequential run from Step 1 (setup) through Step 11 (validate). Only after Document 1 is delivered as a finished .docx does Step 1 of Document 2 begin.
2. **Re-`Read('SKILL.md')`** at the start of each new document, in full. Do not assume the previous document's reading is still active in your working memory.
3. **Re-`Read()` every step file** when arriving at the corresponding step of the new document. Pre-flight banners apply per-document.
4. **Re-`Read()` every applicable per-language sub-lexicon and English reference lexicon** at Step 3 of each new document. Sub-lexicon Avoid-column entries that were the right answer for Document 1 may not be the right answer for Document 2 if the domain shifts. Calque drift is the predictable failure mode here.
5. **Treat the per-batch validator state file (`.validate-state.json`) as document-scoped.** Each document gets its own workdir; the state file lives there.

Sub-lexicon and step-file rereads are part of the **document setup**, not the **session setup**. Skipping them because "I just read this for the previous document" is exactly the drift this skill is designed to prevent.

**Do not ask the user how to proceed when multiple documents are in scope.** Sequential, complete-document-first is the only mode (see "Do not ask" catalogue above). Just begin Document 1 from Step 1.

## IMPORTANT: Single-document workflow — no agent parallelisation

This skill is designed for **one document at a time**, translated by Claude in its main context window. Sequential single-context translation is the **default and only mode** of operation. **Do not ask the user "shall I proceed sequentially?"** — sequential is what the skill does. Just start Document 1, finish all 11 steps, then start Document 2 if there is one.

The only situation that requires the user's input is when **the user explicitly asks for sub-agents or parallelisation**. In that case:

1. **Stop and ask the user** before deploying any agents — do they really want this? They probably don't.
2. **Warn clearly** that agent-based parallel translation is likely to reduce quality: agents lack the full-document context needed for consistent terminology, defined-term tracking, and cross-reference handling. Inconsistencies between agent outputs are difficult to detect and fix.
3. **Recommend** translating documents sequentially in the main context window.

If the user did not explicitly request agents, the question never arises — silently proceed sequentially.

## The golden rule: original-as-base with text matching

The formatting of a .docx lives in paragraph properties (styles, numbering, indentation, spacing)
set on each `<w:p>` element in `word/document.xml`. These properties are fragile — any
re-serialisation through Python's XML parsers can corrupt them in ways that look fine in XML but
render wrong in Word (scrambled numbering, wrong heading levels, lost indentation).

The approach that works reliably: **use the original source-language .docx as the formatting base
and only replace the text runs (w:r elements) inside each paragraph.** The paragraph structure,
styles, numbering, spacing, indentation — everything stays untouched from the original. Only the
words change.

Crucially, the replacement must be done by **matching paragraphs by their source-language text
content**, not by index position. Paragraph extraction can introduce small index offsets (empty
paragraphs counted differently, field codes, nested content). Text matching handles any offset
automatically, and has been verified to produce **zero** style/numbering mismatches across all
tested documents.

**Table and container paragraphs are first-class citizens.** Legal documents routinely contain
paragraphs nested inside tables (`w:tbl/w:tr/w:tc/w:p`), text boxes, and structured document
tags — signature blocks, form fields, schedules with tabular data, and party detail tables all
use these. Both extraction and application MUST use recursive paragraph search (not just direct
children of `w:body`) to find and translate these paragraphs. Failing to do so leaves signature
blocks, schedule tables, and form fields in the source language.

## Architecture overview

```
Original .docx (source language)
        │
        ├──▶ Extract paragraphs → paragraphs.json (text + formatting metadata)
        │                              │
        │                              ▼
        │                     Translate all paragraphs (fill in "en" field)
        │                              │
        │                              ▼
        │                     Validate translations (character-ratio check)
        │                              │
        │                              ▼
        └──▶ Apply translations ◀──────┘
             (text-match onto original document.xml,
              replacing only w:r elements,
              scanning for source-language remnants,
              then post-process in-place)
                    │
                    ▼
              Final .docx (English, identical formatting to original)
```

There is no intermediate "translated document.xml" step. Translations go directly from
the JSON onto the original. This eliminates the paragraph count mismatch problem that
caused cascading formatting corruption in earlier approaches.

## Hard rules. Non-negotiable. Enforced by the skill's gates.

These five rules apply to every step of the pipeline, not just Step 4. Each step file ends with an Internal compliance check that asks you to confirm you have respected these rules. Deviating triggers gates that will block your work; complying upfront is always faster than running into a gate.

**Hard rules. Non-negotiable. Enforced by the skill's gates.**

1. **One document at a time.** Complete the entire pipeline (Steps 1 through 11) for one document before starting the next. Never bundle translations across documents into one paragraphs.json, and never run two translation pipelines in parallel "for efficiency". Translation quality is per-paragraph attention; the workflow is structured around it.

2. **≤35 paragraphs per batch (hard cap, enforced by `validate_translations.py`).** Translate at most 35 paragraphs, then run `validate_translations.py paragraphs.json` BEFORE writing the next batch. Skipping batches is exactly the failure mode the skill is designed against — when the task feels laborious, the instinct is to bundle, and the result is output with errors that early validation would have caught. The validator's state file enforces a hard cap of 35 newly-translated paragraphs per invocation; bulk validation of more than 35 paragraphs blocks unless `--accept-large-batch` is passed.

3. **Step 5 (apply) verifies complete validation coverage.** Apply blocks if any paragraph with non-empty `en` has not been validated by `validate_translations.py`. There is no way to skip Step 4b's per-batch validation and still get past Step 5.

4. **Read every paragraph's complete `text` field.** Do not use summarisation, sampling, or "translate the gist" shortcuts — every word must be in your context window during translation.

5. **Populate `en_runs` for every definitions section paragraph.** Apply blocks if any paragraph in a detected definitions section lacks `en_runs`. See rule 3 below for the structural cues that identify definitions sections and how to populate `en_runs`.

## Mandatory reading order

This skill's discipline depends on you reading the right file at the right step. The full procedural detail for each step lives in `skill-docs/`, organised as eight files. Before performing each step, you MUST `Read('skill-docs/0X-...md')` *in full*. **You MUST not skim. You MUST not skip a step file. You MUST not paraphrase a step from memory.**

Each step file ends with a per-step *Internal compliance check*; you MUST complete that check before moving on. **If at any point you find yourself executing a step without having Read the corresponding step file in this session, STOP — Read the file now, then continue.**

The reading order is:

1. `skill-docs/01-setup-and-extract.md` — Steps 1+2: convert + extract paragraphs
2. `skill-docs/03-lexicons-and-segments.md` — Steps 3+3b: identify document type, read lexicons, scaffold en_segments for TC
3. `skill-docs/04-translate.md` — Step 4: translate every paragraph (the heaviest step)
4. `skill-docs/04b-translate-gates.md` — Steps 4b+4c+4d: per-batch validation, cross-references, lexicon compliance
5. `skill-docs/05-apply.md` — Step 5: apply translations onto the original
6. `skill-docs/06-postprocess-and-reorder.md` — Steps 6+7: post-process and reorder definitions
7. `skill-docs/08-aux-and-quality.md` — Steps 8+9: auxiliary XML files and quality check
8. `skill-docs/10-repack-and-validate.md` — Pre-repack hooks + Steps 10+11: repack into .docx and final validate

Each file should be `Read()`d when you arrive at the corresponding step in the workflow. They are not appendices.

## Lexicon priority — cross-language reference wins on cross-language conventions

The skill's lexicons fall into two layers and they do NOT have equal authority. You MUST read both at Step 3, but on questions of *cross-language English convention* the cross-language reference always wins:

- **`sub-lexicons/<language>-<domain>.md`** — language-specific term mappings. Authoritative on **how a source-language term renders in English in its native context**. Example: the Japanese sub-lexicon maps `条 → "Article (Art.)"` correctly for legislative citations such as `民法第30条 → "Article 30 of the Civil Code"`. The mapping is correct *in its scope*.
- **`references/<domain>.md`** (`general-legal.md`, `finance-banking.md`, `energy-infrastructure.md`, `trading-capital-markets.md`, etc.) — cross-language English conventions. Authoritative on **how English legal writing handles a convention regardless of source language**: Clause vs Article for internal cross-references, defined-term capitalisation, "et al." vs "etc.", date and currency formats, comma usage in lists, abbreviation style, and so on.

**When the two appear to disagree, the cross-language reference wins.** The Japanese sub-lexicon's `条 → "Article"` is a *citation* mapping; `references/general-legal.md` says internal cross-references in a contract take "Clause" (e.g. `本契約第3条 → "Clause 3 of this Agreement"`, NOT `"Article 3 of this Agreement"`). The reference rule scopes the sub-lexicon mapping to legislative citations only — it does not contradict the sub-lexicon, it tells you when the sub-lexicon's mapping does and does not apply. The same logic applies for every cross-language convention: when a quality-check finding flags an "Article 3" inside an internal reference and the sub-lexicon offers the `Article` mapping, the QC finding is correct, not a false positive — read `references/general-legal.md` before treating it as one.

Always read the relevant `references/*.md` before relying on a sub-lexicon mapping for a cross-language convention. If you only consulted the sub-lexicon, you have only half the answer.

## Pipeline overview

High-level summary of what each step does. Detail in the step files.

| # | Step | Action | File |
|---|------|--------|------|
| 1 | Set up | Convert .doc→.docx if needed, unpack to a workdir | `skill-docs/01-setup-and-extract.md` |
| 2 | Extract | `extract_paragraphs.py` produces paragraphs.json with formatting metadata | `skill-docs/01-setup-and-extract.md` |
| 3 | Lexicons | Identify document domain, load English references and per-language sub-lexicons | `skill-docs/03-lexicons-and-segments.md` |
| 3b | Scaffold | (TC documents only) Build `en_segments` skeleton for fragmented TC | `skill-docs/03-lexicons-and-segments.md` |
| 4 | Translate | Fill `en` and `en_runs` for every paragraph, ≤35 per batch | `skill-docs/04-translate.md` |
| 4b | Per-batch validate | `validate_translations.py` after each batch | `skill-docs/04b-translate-gates.md` |
| 4c | Cross-refs | Resolve broken cross-references in translated text | `skill-docs/04b-translate-gates.md` |
| 4d | Lexicon compliance | `lexicon_compliance.py` pre-apply scan | `skill-docs/04b-translate-gates.md` |
| 5 | Apply | `apply_translations_textmatch.py` (auto-invokes 4 validators) | `skill-docs/05-apply.md` |
| 6 | Post-process | `post_process.py` (terminology, spacing, UK English, etc.) | `skill-docs/06-postprocess-and-reorder.md` |
| 7 | Reorder | `reorder_definitions.py` for documents with definitions | `skill-docs/06-postprocess-and-reorder.md` |
| 8 | Aux files | Translate headers/footers/comments/footnotes/endnotes | `skill-docs/08-aux-and-quality.md` |
| 9 | Quality check | `quality_check.py` for source-language remnants | `skill-docs/08-aux-and-quality.md` |
| 10 | Repack | `repack_docx.py` (auto-invokes validate_apply --strict) | `skill-docs/10-repack-and-validate.md` |
| 11 | Validate | Final integrity check on the .docx | `skill-docs/10-repack-and-validate.md` |

## Anti-drift safeguards

The discipline this skill enforces is the result of repeated post-mortems. Drift is the failure mode where you (the operator) start a translation with the skill loaded, then over the course of a long job begin paraphrasing rules from memory, skipping per-batch validation, or deciding a step "doesn't apply this time." The end state is output that looks plausible but has subtly wrong terminology, lost tracked changes, or missed definitions formatting.

The defences are layered and they are non-optional:

1. **Mandatory step-file reads.** Each of the 8 `skill-docs/0X-...md` files must be Read in full at the step it covers. Each ends with an Internal compliance check the operator must complete.

2. **Hard Rules apply skill-wide.** The 5 Hard Rules above are not just for Step 4. Every step's compliance check asks you to re-confirm them.

3. **Auto-invoked gates.** `apply_translations_textmatch.py` auto-runs four pre-apply validators (`validate_en_runs`, `validate_segment_shapes`, `validate_reject_all`, then `validate_apply --strict` after applying). `repack_docx.py` auto-runs `validate_apply --strict` again. `post_process.py` auto-runs `strip_noop_tracked_changes.py`. None of these can be skipped from the CLI.

4. **Per-batch validation.** `validate_translations.py` enforces a hard cap of 35 newly-translated paragraphs per invocation. The state file `.validate-state.json` makes batch coverage auditable.

5. **Skill-gate semantics.** A gate firing produces a `SKILL GATE FIRED — INTENTIONAL BLOCK, NOT A SCRIPT ERROR` banner. This is the script doing its job, not the script breaking. **Do NOT work around a gate by patching the script or skipping the validator** — fix the input (usually paragraphs.json) and re-run.

6. **Script-integrity errors.** Any script that exits with a `FILE INTEGRITY CHECK FAILED — script truncated` banner indicates a corrupted local install of that script. **STOP** — re-install the skill from the .skill / .zip archive before re-running the affected step. Do NOT work around the failure by skipping the step, calling the script through a wrapper, or treating the result as "optional." Every script in the skill carries the integrity check; a failure on any one of them is a hard install-side problem that can only be fixed by re-installation.

7. **Chat-mode discipline.** This skill is designed assuming a working folder (e.g. Cowork mode) where `paragraphs.json`, `final/word/document.xml`, and the `.validate-state.json` checkpoint are real files persisted between steps. **In Chat mode (no working folder, no auto-managed todo list), the discipline must be self-enforced** — and the temptation to skim or compress is materially higher. **At session start, you MUST detect Chat-mode (see `skill-docs/01-setup-and-extract.md` Step 1a) and post the user-facing Chat-mode warning verbatim** — once per session, with `this document` vs `these N documents` phrasing matching the document count. **At Step 11a, pass `--mode chat` to `verify_diligence.py`** so the diligence report can append a Cowork recommendation if drift is detected. Specifically:
   - `paragraphs.json` is still mandatory. If you do not have a workspace folder, write it to `/tmp/<workdir>/paragraphs.json` (or any persistent path your environment offers) and pass that path to every script. Do NOT translate "in-context" without writing a real file — `validate_translations.py` reads the file and writes a state file; both must exist as real files for the per-batch validator to enforce the 35-cap.
   - The 35-paragraph batch cap applies in Chat mode identically to Cowork. Do NOT bundle batches "to save context," "because the document is small," or "because the user is waiting." The validator's state-file check still fires; bypassing it is exactly the rationalisation flagged in this section.
   - The Mandatory Reading Order applies in Chat mode identically. If you arrive at Step 4 without having `Read('skill-docs/04-translate.md')` in this turn, STOP and read it. The smaller per-step file structure (one ~700-line step doc rather than a single 2500-line SKILL.md) makes skimming more tempting; resist. Each step doc was written to be read in full before the operator reaches the corresponding tool call.
   - Each step doc's Internal compliance check at the bottom is mandatory in Chat mode. Walk through the checklist explicitly before moving to the next step. Do not paraphrase or skip items.
   - Auto-invoked validators inside `apply_translations_textmatch.py` and `repack_docx.py` are not negotiable in Chat mode. If a validator fires, fix the input — do not pass override flags ("just this once") and do not run scripts through a Python wrapper to bypass the integrity check.

   The Chat-mode failure mode is the same as the Cowork-mode failure mode (drift, skim, paraphrase from memory) but with one extra failure surface: the operator can rationalise away the file-persistence requirements ("I have the JSON in context, I don't need to write it"). The validators are designed to catch defects the operator would not otherwise see; they only run on real files. Write the files.

If you find yourself rationalising a deviation ("just this once," "the document is small," "I'll catch this in post-processing," "I'm in Chat so I can hold this in context"), STOP. The failure mode is exactly that rationalisation.

## Why text matching matters

When extracting paragraphs from a .docx, the extraction script assigns sequential idx values.
But .docx documents can contain elements that the extraction counts differently from the raw
XML paragraph list: field codes, structured document tags, nested tables, and other structural
elements can cause the idx values to drift relative to the actual XML paragraph indices.

In real-world testing, one document showed 577 JSON entries for 564 XML paragraphs — a drift
of 6-13 positions. Index-based matching put English text onto the wrong original paragraphs,
causing cascading formatting corruption: clause headings rendered as body text, body text got
auto-numbering, Schedule content appeared with wrong indentation, and the last ~60 paragraphs
stayed in the source language.

Text-based matching eliminates this entire class of error. Each translation finds its correct
target paragraph regardless of index drift, producing zero style/numbering mismatches.

## Table-nested paragraphs (signature blocks, schedules, form fields)

Legal documents frequently contain paragraphs inside tables: signature blocks, schedule tables
with account details, party information grids, and form fields. These paragraphs are nested as
`w:tbl > w:tr > w:tc > w:p` rather than being direct children of `w:body`.

Both scripts must handle these consistently:

- **Extraction** (`extract_paragraphs.py`) uses `root.iter('{W}p')` — fully recursive, finds
  all paragraphs regardless of nesting depth.
- **Application** (`apply_translations_textmatch.py`) must use `findall('.//{W}p')` (recursive),
  NOT `findall('{W}p')` (direct children only).

Using direct-child search in the apply step while recursive search was used in extraction causes
the apply step to search a smaller paragraph set (e.g. 564 vs 577), making it impossible to
match table-nested paragraphs. The result: signature blocks, schedule tables, and form fields
remain untranslated.

In testing across 6 legal documents, 3 had table-nested paragraphs (13, 14, and 26 respectively).
All were signature blocks, schedule tables, and party information forms that would have remained
in the source language without recursive search.

## Target English variant: UK English (do NOT ask the user)

This skill translates into **UK English**. UK is the hardcoded standard. **Do NOT ask the user "UK or US English?"** — UK is the answer. The only situation in which US English applies is when the user has *already* given an explicit instruction in their original prompt (phrases like "translate into US English", "use American English"). If they haven't, proceed silently in UK; you can mention "US English available on request" in the delivery message rather than interrupting the translation to ask.

**Anti-drift rule — read this before every variant choice.** Before you make any decision
that depends on the English variant (what to put on the page, what flag to pass to
`post_process.py --variant`, what flag to pass to `quality_check.py --variant`, how to
spell a word in the delivery message), do this:

1. Go back to the user's **original prompt** for this translation.
2. Search it for an unambiguous US-English indicator: "US English", "American English",
   "American spelling", "US spelling", or a plainly equivalent phrase.
3. If and only if you find one, use US English.
4. Otherwise — including when the user mentioned a US party, a US counterparty, a US-based
   addressee, or any other context that feels American — use UK English.

Do not infer "US English" from context, from the client's nationality, from the document's
governing law, from the file name, or from any intermediate message. Only an explicit
instruction from the user's original prompt flips the variant. If there is any doubt at all,
choose UK. This re-check must happen at each of the following decision points; do not cache
a decision from earlier in the session:

- when drafting translations that contain variant-sensitive spelling or vocabulary;
- when invoking `post_process.py` (passes `--variant uk` by default);
- when invoking `quality_check.py` (passes `--variant uk` by default);
- when writing the delivery message to the user.

**How the user switches to US English:** the user must include a direct instruction in their
request — phrases like "translate into US English", "use American English", "American
spelling". When they do, apply US English for that translation, and pass `--variant us` to
both post-processing and quality-check scripts. If they didn't say it explicitly, UK wins —
and you can mention in the delivery message that US English is available on request rather
than interrupting the translation to ask.

**What the variant governs:**

- **Spelling**: organise/organize, authorise/authorize, favour/favor, defence/defense,
  fulfil/fulfill, programme/program, judgement/judgment (UK legal), analyse/analyze.
- **Date format**: "15 April 2026" (UK) vs "April 15, 2026" (US). Apply consistently in dates
  introduced by the translation; leave original-language dates in source documents alone
  beyond translating the month name.
- **Quotation conventions**: single quotes for primary quotations with double inside, commas
  and full stops outside the closing quote when not part of the quoted material (UK); double
  quotes with punctuation inside the closing quote (US). Note: legal drafting practice
  frequently uses double quotes for defined terms in both variants — keep double quotes for
  defined-term markers regardless of variant.
- **Generic legal vocabulary**: claimant/plaintiff, counsel/attorney (where the source is a
  generic word, not a jurisdiction-specific title), post/mail, flat/apartment, and similar
  everyday register choices.

**What the variant does NOT govern:**

- **Jurisdiction-specific legal terms.** When the source document refers to institutions,
  statutes, office-holders, or procedural concepts of a specific legal system, translate
  those by their correct English rendering for that system — do not anglicise them to US
  equivalents just because the reader prefers US English, and do not Americanise them to UK
  equivalents. An Italian *avvocato* stays an *avvocato* (or "lawyer" as a generic), not a
  "solicitor" or an "attorney"; a German *Rechtsanwalt* stays a *Rechtsanwalt* (or "lawyer");
  a US *attorney-at-law* stays an *attorney* in a UK-English translation; a UK *solicitor*
  stays a *solicitor* in a US-English translation. The same applies to statute names,
  court names, procedural stages, and office titles — the variant preference governs register
  and spelling around the term, not the term itself.
- **Statute and institution names as given in the source.** Translate them per the
  established English rendering in the sub-lexicons and reference files, regardless of
  variant.

If you are uncertain whether a specific term is "generic legal vocabulary" (governed by the
variant) or "jurisdiction-specific" (not governed), treat it as jurisdiction-specific and
preserve the established English rendering. Over-anglicising or over-Americanising
jurisdiction-specific terms is a more serious error than leaving register slightly off.

## Scripts reference

| Script | Purpose |
|---|---|
| `extract_paragraphs.py` | Extract paragraphs with formatting metadata to JSON (incl. TC deleted text) |
| `coalesce_fragmented_tcs.py` | **MANDATORY if source has TCs** — Detect character-level TC fragments (e.g. Spanish "Duodécima" → "Decimotercera" edited letter by letter) and scaffold `en_segments` with placeholders on the first ins/del and empty strings on intermediate runs; leaves `tc_segments` untouched |
| `validate_translations.py` | Check translation completeness (character ratios). **Per-batch invocation in Step 4 is manual; the final pre-apply pass auto-runs from inside `apply_translations_textmatch.py`.** |
| `validate_segment_shapes.py` | **MANDATORY if source has TCs** — Pre-apply shape linter: scans `en_segments` pair-wise for XML-boundary risk shapes (article collision, alpha-collision across a boundary with no whitespace — non-Latin script gotcha, digit-at-TC-boundary, double space straddling a boundary, bare-article TC segment, internal camelCase collision). **Auto-runs from `apply_translations_textmatch.py` on TC documents.** |
| `validate_reject_all.py` | **MANDATORY if source has TCs** — Reconstruct accept-all and reject-all views from `en_segments` and scan for readability defects (double article, repeated word, stranded preposition, run-together words, double space, empty brackets, forbidden collocations). **Auto-runs from `apply_translations_textmatch.py` on TC documents.** |
| `lexicon_compliance.py` | **MANDATORY (pre-apply AND pre-repack)** — Scan JSON or document.xml for calques and hard-rule violations drawn from lexicon Avoid columns. Pre-apply run is manual (Step 4d); pre-repack run **auto-fires from inside `repack_docx.py`** before bundling. |
| `apply_translations_textmatch.py` | **PRIMARY** — Apply translations by text matching onto original. Auto-runs `validate_translations.py` (BLOCK code 2 only), plus `validate_segment_shapes.py` and `validate_reject_all.py` on TC docs, all pre-apply, plus `validate_apply.py --strict` post-apply. |
| `repack_docx.py` | **MANDATORY** — Repack translated XML back into .docx (replaces shell zip). Auto-runs `lexicon_compliance.py --stage pre-repack` and (when `--paragraphs` supplied) `validate_apply.py --strict` before bundling. |
| `translate_numbering.py` | Translate numbering format strings in word/numbering.xml |
| `translate_headers_footers.py` | Translate text in word/headerN.xml and word/footerN.xml |
| `translate_comments.py` | **MANDATORY if the document has comments** — namespace-safe translation of word/comments.xml |
| `clean_conversion_artifacts.py` | Accept tracked changes introduced by `.doc` → `.docx` conversion |
| `post_process.py` | Automated terminology, spelling, spacing fixes. **Auto-invokes `strip_noop_tracked_changes.py` at the end on TC documents.** |
| `strip_noop_tracked_changes.py` | **MANDATORY if source has TCs** — remove del/ins pairs where both sides collapse to identical English (orthographic-only source edits). Bracket-aware: preserves bracket-only ins/del wrappers that flank a content-bearing insertion (e.g. placeholder dates like `[1 May 2020]`). **Auto-runs from `post_process.py` on TC documents.** |
| `validate_apply.py` | **MANDATORY pre-apply (post-write check inside apply) AND pre-repack** — Compare declared translations in paragraphs.json against the applied document.xml; catches the "dropped date" class of defect where character-fragmented bracket-plus-date ins clusters lose their date tokens. Use `--strict` to block on any miss. Auto-runs from `apply_translations_textmatch.py` (post-write) AND from `repack_docx.py` (pre-bundle, when `--paragraphs` supplied). Also supports `--report-clusters` mode that inspects `tc_cluster_hits` flags without requiring document.xml, and `--apply-zwsp` which injects ZWSPs into cluster-flagged en strings as belt-and-suspenders protection behind the apply-time auto-ZWSP. |
| `quality_check.py` | Comprehensive quality audit (target: zero issues) |
| `reorder_definitions.py` | Sort definitions alphabetically by English term |
| `verify_diligence.py` | **MANDATORY at Step 11a** — End-of-pipeline diligence audit. Verifies the 11 steps actually ran end-to-end by checking artifact-level evidence: paragraphs.json + .validate-state.json coverage, max batch ≤35, final document.xml exists, every source-side aux file has a translated copy, quality_check re-runs clean, final .docx exists and is a valid ZIP. Reports a single PASS/WARN/FAIL summary. Catches *skipped-step* failures (e.g. Step 8 aux translation skipped) that the per-step validators do not surface as a single end-of-pipeline report. |

## Common pitfalls and how to avoid them

### Python XML parsers corrupt .docx formatting
ElementTree and lxml strip namespace declarations (xmlns:o, xmlns:v, etc.) when re-serialising.
This causes "unreadable content" errors. The textmatch script handles this in two layers:
first by grafting the original XML header back onto the output, then by **validating** that
all namespace prefixes actually used in the document body are present in the root element
(injecting any missing ones). This two-layer approach catches both parser-induced stripping
and cases where the original file itself had incomplete declarations.

### Table-nested paragraphs left untranslated
If the apply script uses `findall('{W}p')` (direct children only) instead of `findall('.//{W}p')`
(recursive), paragraphs inside tables are invisible. Signature blocks, schedule tables, and form
fields stay in the source language. Always use recursive search in both extraction and application.

### Calque drift — "I read the lexicon but still used the forbidden phrase"
The most insidious quality issue. The drafter opens `references/general-legal.md`, scrolls
through the tables, notes the "Avoid" column exists, starts translating, and then — because
the Dutch source has *deze onderhavige overeenkomst* 30 paragraphs in — renders it as
*"this present agreement"*. The lexicon explicitly lists *"the present agreement"* in its
Avoid column, but the drafter's attention had drifted to the translation task by the time
the phrase came up, and the lexicon rule was forgotten.

Real examples that have slipped through this way (all from a single Dutch SOK):
- *"this present agreement"* (NL *deze onderhavige overeenkomst*) — fix: "this Agreement"
- *"framework conditions"* (NL *randvoorwaarden*) — fix: "conditions" / "parameters"
- *"in more concrete terms"* (NL *concretiseren*) — fix: "set out" / "specify"
- *"environs fund"* (NL *omgevingsfonds*) — fix: "community fund" / "local-impact fund"
- *"acceptance by the environs"* (NL *acceptatie door de omgeving*) — fix: "acceptance
  by the local community"

**Why reading the lexicon "once" is not enough.** Memory of a 250-line terminology table
decays within a few translation batches. The Avoid column is a blocklist — the only
reliable way to enforce it is to (a) re-open the sub-lexicon at each fresh batch and
re-scan the relevant sections for the phrases you're about to translate, and (b) run
`scripts/lexicon_compliance.py` at Step 4d (pre-apply) — the pre-repack run auto-fires
inside Step 10 (`repack_docx.py`). The compliance script is cheap (< 1 s) and catches
every documented calque by regex. There is no excuse for letting a listed Avoid-column
phrase reach a final output.

**How to respond when the compliance scan flags a calque.** Do not fight the finding. The
Avoid column is authoritative. Open the cited sub-lexicon, go to the row, pick the
preferred rendering, patch `paragraphs.json`, re-apply, re-scan, repeat until exit 0.

### Sub-lexicon over-applied where cross-language reference governs (lexicon priority misread)

A failure mode adjacent to calque drift but with a different mechanism. The translator
reads the per-language sub-lexicon in full, finds the source term mapped (e.g. Japanese
`条 → "Article (Art.)"`), and applies the mapping uniformly — including in contexts the
mapping was never meant to govern. The cross-language `references/general-legal.md`
rule says internal contract cross-references take "Clause" not "Article" (e.g.
`本契約第3条 → "Clause 3 of this Agreement"`), but the translator had only consulted the
sub-lexicon, treated its mapping as authoritative for all uses, and produced "Article 3"
throughout. When `quality_check.py` later flagged "Article N" in internal references, the
translator misread the QC finding as a false positive and bulk-replaced "Article" with
"Clause" via regex to make the gate pass — solving the symptom without consulting the
authoritative source.

**Root cause.** Reading the sub-lexicon without reading the matching `references/<domain>.md`.
Sub-lexicon mappings are correct in scope (Japanese `条` IS "Article" for legislative
citations like `民法第30条`); the cross-language reference scopes the mapping by usage
(internal contract refs take "Clause"). The two layers are complementary, not redundant.

**Fix.** At Step 3, read both layers. The cross-language `references/*.md` is mandatory
reading at every Step 3, identically to the sub-lexicon. Sub-lexicons go first to find
the term mapping; cross-language references go second to confirm the mapping applies in
the current usage. When in doubt, the cross-language reference wins (see "Lexicon
priority — cross-language reference wins on cross-language conventions" earlier in this
file). When `quality_check.py` flags a cross-language convention violation, treat it as
a real finding by default — `references/*.md` is the source of truth, the sub-lexicon
is the source of mapping.

### Footnotes, endnotes, and comments left in source language
A .docx stores footnote/endnote/comment content in separate XML files (`word/footnotes.xml`,
`word/endnotes.xml`, `word/comments.xml`) — NOT inside `word/document.xml`. If you only
extract, translate, and apply to `document.xml`, all footnotes, endnotes, and comments will
silently remain in the source language. This is a HIGH severity defect. Always check for
these files in Step 2, translate them alongside the body text, and include them in the
Step 10 repack.

### Auxiliary XML corrupted by ElementTree (causes "unreadable content")
**Symptom**: the translated .docx refuses to open in Word with an "unreadable content"
or "file is corrupt" error. A PDF render via LibreOffice may still succeed, which makes
the bug easy to miss.

**Cause**: `xml.etree.ElementTree` renames namespace prefixes when it re-serialises XML.
If the input uses `w14:paraId`, `mc:Ignorable`, `w16cid:*`, etc., ElementTree rewrites
these in the output as `ns1:paraId`, `ns2:Ignorable`, `ns3:*`. The root element also
loses most of its `xmlns:*` declarations. The result is XML that declares `w:` at the top
but uses `ns1:`, `ns2:`, etc. deep in the body — unbound prefixes that Word cannot parse.

**Where this bites**: `word/comments.xml`, `word/footnotes.xml`, `word/endnotes.xml`,
`word/headerN.xml`, `word/footerN.xml`. The main `document.xml` pipeline avoids this
problem because `apply_translations_textmatch.py` uses lxml and grafts the original root
tag back; but the auxiliary files are usually translated with ad-hoc inline Python, which
is where ElementTree sneaks in.

**Why header-grafting alone is insufficient**: earlier versions of this skill recommended
capturing the original `<w:comments ...>` opening tag and regex-substituting it back after
ElementTree finished writing. This restores the root element's namespace *declarations*,
but the body attributes (`ns2:paraId`, `ns1:Ignorable`, …) are still mangled. Word
enforces prefix binding per element, so grafting the root is not enough.

**Correct fix — any ONE of these three approaches**:
1. **(Preferred for comments)** Use the bundled `translate_comments.py` script. It replaces
   text purely via regex, without parsing the XML tree, so no prefix is ever renamed.
2. **(Preferred for headers/footers/numbering)** Use the bundled `translate_headers_footers.py`
   / `translate_numbering.py` scripts. They use lxml, which preserves prefixes correctly.
3. **(For footnotes/endnotes or any other aux file)** Use pure-regex text substitution
   inside `<w:t>` / `<w:delText>` elements, keeping every other byte of the original XML
   verbatim. Example pattern is in Step 8d.

**Do not**: use `xml.etree.ElementTree` on any aux XML file, even with header-grafting,
even with `ET.register_namespace`. It is not safe for files that use `w14:`, `w15:`,
`w16:*`, `mc:`, or any namespace declared on the root but referenced deep in the body.

### Batch size creep (critical quality risk)
A consistently observed failure mode: batch sizes start at 30–35 but silently grow to 50,
60, or 80+ as the translation progresses and you feel pressure to finish. This ALWAYS
degrades quality — later batches end up with truncated clauses, paraphrased text, missed
defined terms, and inconsistent terminology. The damage is invisible during translation but
obvious in review. **Every batch must be max 35 paragraphs.** State the range before each
batch. If fewer than 35 paragraphs remain, translate them as a final batch — do not merge
them into the previous one.

### Paragraph count mismatch between extraction and original
Extraction may produce more or fewer JSON entries than actual XML paragraphs. Text matching
makes this irrelevant — extra entries are skipped, missing entries leave text in the source
language.

### Style-changing scripts destroy numbering
Never use scripts that change paragraph styles (e.g., LeganceTitle2 → FWBL2) to "fix"
numbering. Styles interact with numbering definitions in complex ways. The text-match
approach never touches styles.

### `reorder_definitions.py` extracted more or fewer terms than expected (LibreOffice ST_OnOff)

**Symptom**: refuses to reorder, listing one or more "suspicious" extracted terms
that contain quotation marks, the word *means* / *indica* / *shall mean*, or end with a
colon. Or `--expected-defs N` says the count is wrong.

**Cause**: bold-run detection has misread an off-bold run as on-bold. The most common
reason is `<w:b w:val="0"/>`, which LibreOffice emits when converting `.odt` → `.docx` to
explicitly turn bold off. ECMA-376 ST_OnOff allows the lexical values `true | false | 1 |
0 | on | off` (case-insensitive). Rev11 fixed `reorder_definitions.py` and the other
property-readers to honour the full falsy set, so this should be rare — but if a future
input hits a different OOXML quirk, the term-sanity guard still catches the symptom.

**Fix**:

1. Re-run with `--dry-run` to inspect what the script extracted:
   ```bash
   python <skill-path>/scripts/reorder_definitions.py \
       --doc <workdir>/final/word/document.xml \
       --dry-run --expected-defs <N>
   ```
2. If a single bold-detection variation is the culprit, extend `is_on()` /
   `_ST_ONOFF_FALSE` in the relevant script.
3. If the cause is unclear, ship in source order. The reorder is a high-value but
   non-mandatory pass — definitions in source order are still legible. `quality_check.py`
   will emit `definition_order` warnings; document them as known false positives in the
   delivery notes.

**Do not** patch the script ad-hoc to "force" a sort. The  invariant check would
abort anyway. If the reorder won't run cleanly, source-order delivery is the supported
fallback.

### Splitting or merging paragraphs
If a translation splits one source paragraph into two, the text-match will fail to find a
match for the fabricated paragraph. Always: one source paragraph = one English paragraph.

### Multi-w:t runs silently truncate paragraph text during extraction
In .doc→.docx conversions, LibreOffice often places a clause number and its body text
in a single `<w:r>` element separated by `<w:tab/>`:
```xml
<w:r><w:t>11.3.1</w:t><w:tab/><w:t>Il 10% del Corrispettivo...</w:t></w:r>
```
Using `r.find('{W}t')` returns only the first `w:t` ("11.3.1"), silently dropping the
entire body text. In one tested document, this affected 45 paragraphs and 1,547 characters
— including payment milestone clauses and finance-party consent provisions.

**Symptom**: The extracted `paragraphs.json` contains entries with suspiciously short text
(just a clause number like "11.3.1" or a sub-reference like "(i)") where the original
document clearly has more content. The translator treats these as numbering-only paragraphs
and translates them as-is, leaving the substantive text untranslated in the output.

**Fix**: The extraction script must iterate over ALL child elements of each `w:r`, collecting
text from every `w:t` element. See the patched `extract_paragraphs.py`.

### Nonsensical redlines from orthographic-only source edits
Source-language drafts routinely contain tracked changes that fix *only* source-language
orthography — abbreviation punctuation (Dutch `mn` → `m.n.`), spelling reform (Dutch
`pro-actief` → `proactief`, German `daß` → `dass`), hyphenation (Dutch `zonneenergie` →
`zonne-energie`), diacritic restoration (`coordinaat` → `coördinaat`), or soft-hyphen
artefacts introduced by end-of-line breaks. When translated, both sides collapse to the
**same English text**: `mn` and `m.n.` both become "in particular,"; `zonneenergie` and
`zonne-energie` both become "solar energy"; `coordinaat` and `coördinaat` both become
"coordinate". The corresponding redline in the English output looks nonsensical —
"in particular" struck through with "in particular" inserted — and confuses any reviewer
who cannot see the source Dutch/German/French/etc.

**Symptom**: the translated document has tracked-change markers that do nothing. The
reviewer sees phrases like "in particular ↔ in particular" or "proactive ↔ proactive" in
the redline view.

**Fix (two steps)**:
1. At translation time: give both `del` and `ins` segments the SAME English text when the
   source edit is orthographic-only. See "Collapsing orthographic-only TC edits —
   MANDATORY" in Step 4 for the full rule and decision test.
2. After `apply_translations_textmatch.py` and `post_process.py`: run
   `strip_noop_tracked_changes.py`. It finds adjacent del/ins pairs whose text content
   normalises to the same string, removes the del, and unwraps the ins. It also strips
   empty/punctuation-only wrappers that survive translation. Meaningful edits (date digits,
   term substitutions, real content changes) are preserved untouched.

### Orphan source characters in English redlines from character-fragmented source edits

Separate from orthographic-collapse pathology (where both del and ins mean the same
thing in English), some source drafts contain TC edits where a **single word** is
replaced by a **different single word** but edited letter by letter — producing 5–10
character-level `ins` / `del` segments for a single conceptual edit. The segment-aware
translator has no way to map this cleanly onto English because English replaces the
whole word, not character ranges.

**Symptom**: an English clause heading in the redline view reads as something like
`"Clause 13~~Clause 12~~eé cim otercera. Governing law…"` or
`"D ecimo Clause 14~~Clause 13~~. General provisions"` — the correct accepted clause
number lands in the right place, but orphan source-language characters leak into the
heading from the intermediate segments.

**Fix (two steps)**:
1. At Step 3b (before translation): run `coalesce_fragmented_tcs.py` on
   `paragraphs.json`. The script detects contiguous character-level ins/del
   clusters that reassemble to coherent single words on each side and writes a
   pre-filled `en_segments` skeleton into each flagged paragraph, with
   `<<TRANSLATE: …>>` placeholders on the first ins/del of the cluster and the
   empty string `""` on every other cluster segment. It does NOT modify
   `tc_segments`. See Step 3b and the
   "Scrambled / character-fragmented whole-word edits" subsection of Step 4.
2. The translator replaces the placeholders with the final English and leaves
   the empty-string slots as `""`. The apply step then uses the v2026+
   behaviour of `apply_translations_textmatch.py` — a segment with
   `"en": ""` (key present, value empty) **clears** the matching runs, a
   segment with no `"en"` key at all **preserves** the source — to produce a
   clean Accept/Reject redline with no orphan source characters.

### Tracked-change deleted text left in source language
When a paragraph contains tracked changes (`w:ins`/`w:del` markup), the visible "accepted"
text lives in `w:t` elements but the struck-through deleted text lives in `w:delText`
elements — a different element type. If the apply script only iterates `w:t`, the `w:delText`
content is never touched and stays in the source language. This is immediately visible to
anyone viewing tracked changes.

**Fix**: The extraction script now captures `deleted_text` from `w:delText` elements. The
translator must provide `en_deleted` alongside `en`. The apply script distributes `en` across
active `w:t` elements and `en_deleted` across `w:delText` elements separately. See
"Tracked-change paragraphs — MANDATORY DUAL TRANSLATION" in Step 4.

### Bold leak in tracked-change paragraphs
Runs inside `<w:ins>` wrappers carry the formatting from the original tracked insertion,
which often includes bold (inherited from the paragraph style via `basedOn` chains like
Cmsor2 → Cmsor1). The old apply approach preserved the original rPr on every run, causing
bold to leak into translated body text. The user sees random words bolded in the party
section, defined-term paragraphs, or any paragraph with tracked changes.

**Fix**: The apply script now applies `<w:b w:val="0"/>` (explicit bold-off) to all runs in
non-heading TC paragraphs. This matches what `make_run_et()` does for non-TC paragraphs and
prevents style-inherited bold from leaking into translated body text.

### Translator alters source-faithful translation to satisfy a QC linter
The `quality_check.py` truncation patterns are heuristics. When a heuristic flags a paragraph that is in fact a faithful translation of the source — most commonly a list connective like `; and` / `, and` (translation of the Italian `; e`) — the correct response is **not** to trim the connective to silence the linter. Doing so silently strips semantic content that the source author drafted on purpose, and the result is a translation that no longer matches the source.

**Symptoms.** A paragraph in `paragraphs.json` was changed between QC fail and QC pass without the source change being reflected. The paragraph now ends with bare `;` (or some other punctuation rewrite) instead of the connective the source had.

**Mitigation.** When QC flags a paragraph, inspect the issue against the source first. If the source connective (`; e`, `; o`, `, e`, `, o`) is present and the translation faithfully reflects it (`; and`, `; or`, `, and`, `, or`), the QC flag is a false positive — keep the faithful translation, document the false positive in delivery notes, and proceed. **Reaching 0 QC issues is desirable but never at the cost of fidelity.** As of rev34 the truncation check has a list-connector whitelist that suppresses this specific false positive automatically; the rule above still applies to any other class of false-positive that crops up in the future.

## Maintainer discipline

Future revs need to keep the discipline coverage at least as strong as today's. Three rules for anyone editing this skill:

1. **If you change a Hard Rule**, update both this file (Hard Rules section) and the affected step file's Internal compliance check. The two MUST stay in sync.

2. **If you add a step**, update Mandatory Reading Order, Pipeline Overview, and the previous step file's "Next:" pointer. Add a new `skill-docs/0X-...md` following the established template (Pre-flight banner at top, Internal compliance check at bottom).

3. **Step-specific procedural detail belongs in `skill-docs/`, not here.** Cross-cutting discipline (rules, anti-drift, conventions, common pitfalls) belongs in this file. If unsure, prefer this file — always-loaded content over conditionally-loaded content.

## Begin the workflow

Once you have read SKILL.md in full, proceed to `skill-docs/01-setup-and-extract.md` to begin Step 1.
