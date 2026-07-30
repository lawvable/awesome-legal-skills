> **Pre-flight.** You should be entering this step having completed the previous step. **SKILL.md governs every step's discipline; if you have not read SKILL.md in full this session, STOP and `Read('SKILL.md')` before continuing.** Hard Rules from SKILL.md apply to this step too. **In Chat mode (no workspace folder, no auto-managed todo list) the same discipline applies — do not skim this step doc, do not bundle batches, do not skip the per-step Internal compliance check at the bottom.** **If this turn began from a compacted transcript, the compaction summary does NOT count as having read this step doc — `Read()` it now in full before any tool call.**

### Step 1: Set up and unpack

*[Internal compliance check — do not echo or paraphrase to the user. Re-read every rule in this step before executing. Do not deviate from any line of the skill. Do not bundle work, skip checks, or "interpret for efficiency" — every prior deviation has produced output below the quality the skill is designed to deliver. The skill's hard gates block deviations anyway; complying upfront is always faster than running into a gate and re-authoring paragraphs.json.]*

#### Step 1a — Chat-mode user warning (rev41) — MANDATORY

**Detect your host environment** before doing anything else:
- **Cowork mode** if any of these hold: your `<application_details>` system block names "Cowork mode"; an `mcp__cowork__*` MCP tool is available (e.g. `mcp__cowork__create_artifact`, `mcp__cowork__request_cowork_directory`); or `<env>` reports a selected workspace folder.
- **Chat mode** if none of the above hold.

**If you are in Chat mode, post the following warning to the user verbatim before any tool call.** Adjust `this document` / `these N documents` based on how many documents the user has presented for translation in this session (1 → "this document"; ≥2 → "these N documents", e.g. "these 3 documents"):

> Please be aware that you are now using Claude Chat to translate this document. The risk of me deviating and drifting from the skill is higher in Chat and might impact the quality of the translation. I recommend to always use Cowork when translating documents using the legal-translation skill.

(Plural form when ≥2 documents in scope: replace `to translate this document` with `to translate these N documents`. Keep everything else verbatim.)

Post the warning **once per session**, not once per document. After posting, proceed with Step 1. At Step 11a (diligence audit) pass `--mode chat` so the audit can append a Cowork recommendation to its report if drift is detected.

**If you are in Cowork mode** (or `mcp__cowork__*` tools are present), **do NOT post any message about Step 1a, the warning, or the Chat/Cowork detection.** Do not announce that you are skipping the warning. Do not mention that you detected Cowork. Do not say "I'm in Cowork mode, so I'll skip the Chat-mode warning." Simply proceed silently to Step 1b — the user does not need to know this check happened. Step 1a is a no-op in Cowork; treat the entire subsection as if it doesn't exist when narrating progress to the user.

#### Step 1b — Set up workdir and convert source

**If a script fails with `SyntaxError`, `NameError`, or prints a `FILE INTEGRITY CHECK FAILED — script truncated` banner, the install copy was truncated during marketplace transfer.** The packaged `.skill` / `.zip` archive is intact; only the local install was cut. Re-install the skill from the archive. The integrity check runs at every CLI invocation of apply / extract / validate scripts, so truncation is caught at the start of any step rather than failing mysteriously partway through. Do not work around an integrity-check failure by editing the script — re-install the archive instead.

```bash
mkdir -p <workdir>
```

If the input is `.doc`, convert first:
```bash
python <docx-skill-path>/scripts/office/soffice.py <input>.doc --format docx
```

The docx skill path is at `mnt/.claude/skills/docx/scripts/office/`.

**After `.doc` → `.docx` conversion:** LibreOffice may introduce revision markup (`<w:ins>`,
`<w:del>` elements) that was not visible in the original `.doc`. These conversion artifacts
will appear as tracked changes in the translated output. Run the conversion cleanup script
to accept any such artifacts:

```bash
python <skill-path>/scripts/clean_conversion_artifacts.py <converted>.docx
```

This accepts insertions (unwraps `<w:ins>`, keeping content), removes deletions (strips
`<w:del>` entirely), and removes move markers — but ONLY if the original is expected to be
a clean document without intentional track changes. If the original intentionally contains
tracked changes (e.g., a redline), skip this step to preserve them in the translation.

**Do not** strip revision markup during the apply step (Step 5) — that would destroy
intentional tracked changes in documents that have them.

### Step 2: Extract paragraphs with formatting metadata

*[Internal compliance check — do not echo or paraphrase to the user. Re-read every rule in this step before executing. Do not deviate from any line of the skill. Do not bundle work, skip checks, or "interpret for efficiency" — every prior deviation has produced output below the quality the skill is designed to deliver. The skill's hard gates block deviations anyway; complying upfront is always faster than running into a gate and re-authoring paragraphs.json.]*

```bash
python <skill-path>/scripts/extract_paragraphs.py <original>.docx <workdir>/paragraphs.json
```

Note: this script reads directly from the .docx ZIP — no need to unpack separately.

**Critical: multi-w:t runs.** In .doc→.docx conversions, LibreOffice often produces runs
where a clause number and its body text share a single `<w:r>` element, separated by a
`<w:tab/>`: e.g. `<w:t>11.3.1</w:t><w:tab/><w:t>Il 10% del Corrispettivo...</w:t>`.
The extraction script MUST collect text from ALL `w:t` children of each run (not just
the first). Using `r.find('{W}t')` silently drops all text after the first `w:t` —
a data-loss bug that can leave entire commercial clauses (payment milestones, finance
party consent rights) invisible to the translator. The patched script iterates over
all child elements of each `w:r`, collecting text from every `w:t` while skipping
`w:tab` and `w:br` elements (which are preserved in the XML during the apply step).
Do NOT insert tab or newline characters for `w:tab`/`w:br` in the extracted text —
the apply script's `get_paragraph_text()` joins `w:t` texts without separators, so
inserting separators would cause text-match failures.

This creates a JSON array where each entry contains:
- `idx` — paragraph index at time of extraction
- `text` — full paragraph text in the source language (from `w:t` elements — i.e. accepted/visible text, including text inside `w:ins` wrappers but excluding text inside `w:del` wrappers)
- `runs` — array of character ranges with formatting (bold, italic, font, size)
- `style` — paragraph style name
- `en` — to be filled with the English translation
- `en_runs` — optional: explicit formatting instructions for the English text
- `deleted_text` — (TC paragraphs only) the struck-through text from `w:delText` elements inside `w:del` wrappers. Present only when the paragraph contains tracked changes.
- `has_track_changes` — (TC paragraphs only) `true` if the paragraph contains `w:ins`, `w:del`, `w:moveFrom`, or `w:moveTo` markup
- `en_deleted` — to be filled with the English translation of `deleted_text` (see "Tracked-change paragraphs" below)

The `idx` field is assigned during extraction and may not perfectly match the original
document.xml paragraph indices. This is expected and harmless — the apply step matches
by text content, not by index.

#### Footnotes, endnotes, and comments — MANDATORY

A .docx stores footnotes, endnotes, and comments in **separate XML files** alongside
`word/document.xml`:

- `word/footnotes.xml` — footnote content (referenced by `<w:footnoteReference>` in body)
- `word/endnotes.xml` — endnote content
- `word/comments.xml` — comment content (margin annotations)

**These files contain translatable text that the main extraction script does NOT cover.**
If you only extract and translate `document.xml`, footnotes/endnotes/comments will remain
in the source language in the output — a HIGH severity defect.

After extracting the main body paragraphs, check whether the source .docx contains any of
these files:

```python
import zipfile
with zipfile.ZipFile('<original>.docx') as z:
    for name in ['word/footnotes.xml', 'word/endnotes.xml', 'word/comments.xml']:
        if name in z.namelist():
            print(f'FOUND: {name} — must extract and translate')
```

For each file that exists and contains substantive text (footnote IDs -1 and 0 are standard
empty separator/continuation entries — skip those), extract paragraphs using the same
approach as for `document.xml`: find all `<w:p>` elements, collect `<w:t>` text from all
runs. Store them in a separate JSON file per XML (e.g. `footnotes.json`, `endnotes.json`,
`comments.json`) with the same structure as `paragraphs.json`.

**Translate these alongside the main body** — they count toward your batch totals and are
subject to the same 35-paragraph batch limit. Include them in validation runs.

## Internal compliance check — 01-setup-and-extract

Before moving to the next step, confirm:

- [ ] You converted .doc → .docx (if needed) using soffice, NOT pandoc
- [ ] You inspected `clean_conversion_artifacts.py`'s author/ratio output and did not run it on a redline
- [ ] You produced `paragraphs.json` with `extract_paragraphs.py`
- [ ] You did NOT manually edit document.xml or skip Step 1's integrity check
- [ ] **If this is your second or later document this session:** you re-`Read('SKILL.md')` and you will re-`Read()` each step file as you arrive at it; you did NOT skip the per-document refresh on the assumption that the previous document's reads are still active

If any check is uncertain, STOP. Re-read this file. Do not proceed.

**Next:** `skill-docs/03-lexicons-and-segments.md`
