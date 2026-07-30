> **Pre-flight.** You should be entering this step having completed the previous step. **SKILL.md governs every step's discipline; if you have not read SKILL.md in full this session, STOP and `Read('SKILL.md')` before continuing.** Hard Rules from SKILL.md apply to this step too. **In Chat mode (no workspace folder, no auto-managed todo list) the same discipline applies — do not skim this step doc, do not bundle batches, do not skip the per-step Internal compliance check at the bottom.** **If this turn began from a compacted transcript, the compaction summary does NOT count as having read this step doc — `Read()` it now in full before any tool call.**

### Step 5: Apply translations directly onto original

*[Internal compliance check — do not echo or paraphrase to the user. Re-read every rule in this step before executing. Do not deviate from any line of the skill. Do not bundle work, skip checks, or "interpret for efficiency" — every prior deviation has produced output below the quality the skill is designed to deliver. The skill's hard gates block deviations anyway; complying upfront is always faster than running into a gate and re-authoring paragraphs.json.]*

**Distinguishing skill gates from script errors.** If `apply_translations_textmatch.py` exits with code 2, raises `RuntimeError` mentioning `BLOCK`, or prints a banner reading `SKILL GATE FIRED — INTENTIONAL BLOCK, NOT A SCRIPT ERROR`, that is a gate firing intentionally. The scripts are not crashing, not truncated, and not buggy. Read the BLOCK message printed immediately above the exit/raise — it tells you exactly which gate fired (en_runs missing on a definitions section, per-batch cap exceeded, validate_apply token mismatch, post-strip drift, etc.) and how to fix `paragraphs.json`. **Do NOT work around a gate by calling `textmatch_apply()` from a wrapper that bypasses the auto-invoked validators, by suppressing `--strict` flags, or by patching the script to return success.** The gates exist because every prior occasion the operator went around them shipped output below the quality the skill is designed to deliver. Fix the underlying issue and re-run apply; it is always faster than the workaround.

```bash
python <skill-path>/scripts/apply_translations_textmatch.py \
  <original_source_language>.docx \
  <workdir>/paragraphs.json \
  <workdir>/final/word/document.xml
```

This is the single most important step. It does everything at once:

1. Reads the original document.xml directly from the source .docx ZIP
2. For each translated entry in paragraphs.json, **matches the source-language text** to find
   the correct original paragraph (handles any index offset automatically)
3. Replaces only the w:r (text run) elements with new English runs
4. Preserves all paragraph properties (styles, numbering, indentation, spacing)
5. Restores original namespace declarations (prevents "unreadable content" errors in Word)
6. **Validates namespace completeness** — scans the document body for any namespace prefixes
   used but not declared in the root element, and injects missing declarations. This catches
   cases where the original .docx (especially .doc→.docx conversions) uses namespaces like
   `a:` or `pic:` on embedded elements without declaring them in the root. Without this,
   Word will refuse to open the file with a 422/unreadable-content error.
7. **Strips language tags** (`w:lang` elements) from both run-level and paragraph-level
   properties. The source document carries `w:lang val="it-IT"` (or similar) on every run;
   if these survive into the English output, Word shows "Changed to English (UK)" tracked
   changes on every single paragraph. Removing `w:lang` lets Word auto-detect the language.
8. **Strips revision tracking attributes** (`w:rsidR`, `w:rsidRDefault`, `w:rsidRPr`,
   `w:rsidP`, etc.) from all elements. These cause Word to display formatting changes as
   tracked changes in the output.
9. **Scans for source-language remnants** — after applying all replacements, scans the
   entire output XML for common source-language words and reports any found with their
   surrounding context. This catches text in split-run paragraphs, structured document
   tags, or nested elements that the paragraph-level replacement missed.

The script prints a summary showing exact vs offset matches and any unmatched entries. Target:
zero style/numbering mismatches.

**Auxiliary XML files (numbering, headers/footers, comments, footnotes, endnotes) are
translated separately in Step 8 — see Step 8 below.** Step 5 only modifies
`document.xml`. Step 6 post-processes `document.xml`. Step 7 reorders definitions
in `document.xml`. All other XML parts wait until Step 8.

## Internal compliance check — 05-apply

Before moving to the next step, confirm:

- [ ] You ran `apply_translations_textmatch.py` and let it auto-invoke ALL pre-apply gates
- [ ] You did NOT pass `--allow-bold-loss` unless bold loss is genuinely acceptable
- [ ] You read every gate output (segment_shapes, reject_all, validate_en_runs, validate_apply)
- [ ] No gate exit code 2 was suppressed or worked around

If any check is uncertain, STOP. Re-read this file. Do not proceed.

**Next:** `skill-docs/06-postprocess-and-reorder.md`
