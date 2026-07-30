> **Pre-flight.** You should be entering this step having completed the previous step. **SKILL.md governs every step's discipline; if you have not read SKILL.md in full this session, STOP and `Read('SKILL.md')` before continuing.** Hard Rules from SKILL.md apply to this step too. **In Chat mode (no workspace folder, no auto-managed todo list) the same discipline applies — do not skim this step doc, do not bundle batches, do not skip the per-step Internal compliance check at the bottom.** **If this turn began from a compacted transcript, the compaction summary does NOT count as having read this step doc — `Read()` it now in full before any tool call.**

### Step 8: Translate auxiliary XML files — MANDATORY

*[Internal compliance check — do not echo or paraphrase to the user. Re-read every rule in this step before executing. Do not deviate from any line of the skill. Do not bundle work, skip checks, or "interpret for efficiency" — every prior deviation has produced output below the quality the skill is designed to deliver. The skill's hard gates block deviations anyway; complying upfront is always faster than running into a gate and re-authoring paragraphs.json.]*

OOXML stores list numbering, headers, footers, comments, footnotes, and endnotes in
separate XML files outside `word/document.xml`. The main translation pipeline (Steps
2-7) only touches `document.xml` — every auxiliary file must be translated separately
in this step. Run all applicable sub-steps before Step 9 (quality check) so the QC
pass scans the auxiliary files too.

> **Never round-trip an auxiliary XML part (`comments.xml`, `footnotes.xml`,
> `endnotes.xml`, `headerN.xml`, `footerN.xml`, `numbering.xml`) through Python's
> `xml.etree.ElementTree`. Not with header-grafting, not with namespace
> registration, not at all.** Use one of the bundled namespace-safe scripts, or
> `lxml` (which preserves prefixes), or a pure-regex approach that only replaces
> text between `<w:t>` / `<w:delText>` tags. See the pitfall "Auxiliary XML
> corrupted by ElementTree" below for the explanation.

#### Step 8a: Translate numbering format strings — MANDATORY (if numbering.xml exists)

```bash
python <skill-path>/scripts/translate_numbering.py \
  <original_source_language>.docx \
  <workdir>/final/word/numbering.xml \
  --language <source-language>
```

`word/numbering.xml` defines list and heading numbering. Each level has a `w:lvlText`
whose `w:val` attribute is the rendered prefix string. If those strings contain
source-language words (Hungarian `%1. sz. Melléklet` = "Schedule %1"), the output
shows mixed-language numbering on schedule headers, appendix titles, and chapter
headings.

The script auto-detects the source language from the format strings and applies a
built-in translation map (Hungarian, Italian, German, French, Spanish, Portuguese,
Dutch, Polish, Finnish). Pass `--language` if auto-detect fails.

**Do not skip.** Mixed-language numbering ("1. sz. Melléklet" instead of "Schedule 1")
is immediately visible. If the script reports "No word/numbering.xml found" or "No
translatable format strings found", the document doesn't need this — exit cleanly.

#### Step 8b: Translate headers and footers — MANDATORY (if any source-language text)

OOXML stores page headers/footers in separate `word/header1.xml`, `word/footer2.xml`,
etc. They typically mix standard boilerplate (signature blocks, watermarks, role
labels) with free-text content (agreement titles like `Samenwerkingsovereenkomst`,
version labels like `Versie DRAFT 1 – juli 2021`, initialling-box labels like
`Parafen`, month names, watermarks). Use the scaffold + apply round-trip.

**8b.1 — Extract.**

```bash
python <skill-path>/scripts/translate_headers_footers.py \
  <original_source_language>.docx \
  --extract <workdir>/headers_footers.json
```

Writes one JSON entry per non-empty header/footer paragraph with source text, run
metadata, and an empty `en` field. Pure page-numbers and tab-only lines are skipped.
Prints an English-passthrough reminder: copy English source verbatim into `en`, no
rewrites.

**8b.2 — Translate the JSON.** Fill `en` for every entry using the same lexicons and
judgment as body paragraphs:

- **Translate every source-language token by default.** Agreement titles
  (`Samenwerkingsovereenkomst → Cooperation Agreement`), document-attribute labels
  (`Versie → Version`, `Pagina → Page`), month names (`juli → July`,
  `styczeń → January`), draft/confidentiality watermarks
  (`CONCEPT/BOZZA/ENTWURF/PROJET/BORRADOR/MINUTA/TERVEZET/PROJEKT/LUONNOS → DRAFT`;
  `VERTROUWELIJK/RISERVATO/VERTRAULICH/CONFIDENTIEL/CONFIDENCIAL/POUFNE/BIZALMAS/
  LUOTTAMUKSELLINEN → CONFIDENTIAL`), initialling-box labels
  (`Parafen/Parafy/Paraphes/Paraphen/Sigle/Rúbricas/Parafę → Initials`), role labels
  in signature bands.
- **Preserve only proper nouns and codes.** Project names, entity strings
  (`Acme Energy Europe B.V.`, `Acme s.r.l.`), reference codes (`RRF-6.5.1-23`),
  acronyms (`EUR`, `HUF`, `RRF`), dates, page numbers. For a preserved entry, set
  `en == text` or leave it `null`.
- **English source passes through unchanged.** Same rule as Step 4.
- Entries with `en == null` or `en == ""` are preserved verbatim at apply time.

**8b.2a — Field placeholders (`<<PAGE>>`, `<<NUMPAGES>>`, …) — MANDATORY.**

Some header/footer paragraphs contain Word *field codes* — runtime-evaluated
placeholders like `PAGE` (current page number), `NUMPAGES` (total pages), `DATE`
(today's date), `TIME`, `FILENAME`, `AUTHOR`, etc. In OOXML, a field is encoded
as a sequence of runs:

```
<w:fldChar fldCharType="begin"/>  ... <w:instrText> PAGE </w:instrText>
... <w:fldChar fldCharType="separate"/>  <w:t>2</w:t>   <-- cached result
... <w:fldChar fldCharType="end"/>
```

The cached result (`2` in the example above) is what Word *currently displays*,
re-evaluated each time the user opens the file. Treating that cached digit as
static text and overwriting it with translated English breaks the field — the
new English lands in the wrong run, and at render time Word recomputes the
field and produces visible garbage like `Page 2 of 27` (where `27` is the
correct total but the layout is broken because the static "of" was dropped).

The extract step (`translate_headers_footers.py --extract`) detects fields and
emits each cached result as a placeholder token in the `text` field — for
example, a Norwegian footer reading `Side 2 av 2` (with `2` and `2` both being
cached field results) is extracted as:

```
"text": "Side <<PAGE>> av <<NUMPAGES>>"
```

**The placeholders MUST be preserved verbatim in the `en` field.** Translate
the static surround, leave the `<<...>>` tokens unchanged:

```
"en": "Page <<PAGE>> of <<NUMPAGES>>"
```

The apply step substitutes each `<<TYPE>>` back with the original field
structure (`begin / instrText / separate / cached_result / end`), so Word
re-evaluates the field at open time and renders the correct live page number.
If you accidentally translate a placeholder (e.g. write
`Side 2 av 2 → Page 2 of 2` with literal digits), the apply step writes
literal `2` and `2` into static runs, the field structure is empty, and the
rendered footer shows the *literal* digits forever — never updating with the
real page count. The corresponding field-cached runs become orphan empty
text, producing the visible garbage described above.

Recognised placeholder types include `<<PAGE>>`, `<<NUMPAGES>>`, `<<SECTIONPAGES>>`,
`<<DATE>>`, `<<TIME>>`, `<<CREATEDATE>>`, `<<SAVEDATE>>`, `<<PRINTDATE>>`,
`<<FILENAME>>`, `<<AUTHOR>>`, `<<TITLE>>`, `<<SUBJECT>>`, `<<HYPERLINK>>`,
`<<REF>>`, `<<PAGEREF>>`. If you see a `<<...>>` token in `text`, copy it
into `en` exactly — never expand, translate, or reorder its internal letters.

**8b.3 — Apply.**

```bash
python <skill-path>/scripts/translate_headers_footers.py \
  <original_source_language>.docx \
  <workdir>/final \
  --apply <workdir>/headers_footers.json
```

Writes translated `word/header*.xml` / `word/footer*.xml` under `<workdir>/final/word/`,
preserving run-level properties (`w:sz`, `w:rFonts`, `w:color`, `w:b`, `w:i`, field
codes, tab stops, line breaks) byte-for-byte. Step 10 (repack) picks these up via
`--headers-footers-dir`.

**Legacy dictionary-only fallback.** For watermark-only docs the older mode
`--language <lang>` is retained — fast but can only translate tokens in its built-in
dictionaries. Prefer the scaffold round-trip.

#### Step 8c: Translate comments — MANDATORY (if word/comments.xml exists)

```bash
# 1. List source comments so you can draft translations
python <skill-path>/scripts/translate_comments.py <original>.docx --list

# 2. Save translations to a JSON file keyed by comment ID:
#    {
#      "19": "To be named as \"the Plots\"?",
#      "29": "To be discussed with Acme",
#      ...
#    }

# 3. Produce the translated comments.xml
python <skill-path>/scripts/translate_comments.py \
    <original>.docx <workdir>/final \
    --translations <workdir>/comments_translations.json
```

`word/comments.xml` holds Word's margin annotations. Highly visible, frequently left
untranslated. The script uses pure regex so no namespace prefix is touched. Same
English-passthrough reminder as 8b.1: if a comment is already in English, copy the
source verbatim. Step 10 (repack) picks up the translated `comments.xml` via
`--comments`.

#### Step 8d: Translate footnotes / endnotes — MANDATORY (if present)

There is no bundled script (footnotes/endnotes are rare in legal drafts), but the
same regex-only rule applies: do not use ElementTree. Use pure-regex text
substitution inside `<w:t>` / `<w:delText>` elements, or `lxml`. Minimal template:

```python
import re, zipfile

_WT = re.compile(r'(<w:t(?:\s[^>]*)?>)([^<]*)(</w:t>)')
_WDT = re.compile(r'(<w:delText(?:\s[^>]*)?>)([^<]*)(</w:delText>)')

with zipfile.ZipFile('<original>.docx') as z:
    xml = z.read('word/footnotes.xml').decode('utf-8')

# translations: dict mapping exact source w:t text -> English
def rewrite(m):
    op, txt, cl = m.group(1), m.group(2), m.group(3)
    return op + translations.get(txt, txt) + cl

xml = _WT.sub(rewrite, xml)
xml = _WDT.sub(rewrite, xml)

with open('<workdir>/final/word/footnotes.xml', 'w', encoding='utf-8') as f:
    f.write(xml)
```

Replaces text content only; every namespace declaration, prefix, rsid, and paragraph
ID passes through byte-for-byte.

**Do not skip auxiliary translation steps.** Source-language text in numbering,
headers, footers, comments, footnotes, or endnotes is a HIGH-severity defect — it is
visible on every page (numbering, headers, footers) or contains substantive legal
content (comments, footnotes). Grading: Step 8 outputs are penalised under Criterion 5
(Completeness), capping at 7 if any source-language token survives. Comments inside
`w:delText` are penalised under Criterion 13 (Track Changes Fidelity).

### Step 9: Run quality check — MANDATORY

*[Internal compliance check — do not echo or paraphrase to the user. Re-read every rule in this step before executing. Do not deviate from any line of the skill. Do not bundle work, skip checks, or "interpret for efficiency" — every prior deviation has produced output below the quality the skill is designed to deliver. The skill's hard gates block deviations anyway; complying upfront is always faster than running into a gate and re-authoring paragraphs.json.]*

```bash
python <skill-path>/scripts/quality_check.py <workdir>/final/word/document.xml \
  --verbose --with-source <workdir>/paragraphs.json --variant uk \
  --aux-dir <workdir>/final
```

**`--aux-dir` is and strongly recommended.** It points at the directory
containing translated `word/numbering.xml`, `word/headerN.xml`, `word/footerN.xml`,
and `word/comments.xml` (typically `<workdir>/final`). With this flag, quality_check
also scans every auxiliary file produced by Step 8 for source-language remnants. Without
it, calques and untranslated text in headers / footers / numbering / comments slip past
quality_check entirely (only the post-repack scan inside `repack_docx.py` would catch
them, and that scan covers fewer rule classes).

**Variant flag — use the same variant as Step 6.** `--variant uk` is the hardcoded
default. Only pass `--variant us` if Step 6 was run with `--variant us`, which itself
requires that the user's original prompt explicitly requested US English. Mismatched
variants between Step 6 and Step 9 produce false-positive "spelling violations".

Review the output. Key checks:
- `<source_language>_remnants` — source-language text in `document.xml`?
- `aux_<filename>` — source-language text in auxiliary file ?
- `numbering`, `truncation`, `formatting`, `definition_order` — structural defects in
  `document.xml`.

**The check should report 0 issues before Step 10 (repack).** If issues are reported,
go back to the relevant prior step (paragraphs.json for body issues; the auxiliary
JSON / source for aux-file issues), fix, then re-run Steps 5-9 in order.

**Do NOT silently strip semantic content to satisfy a QC heuristic.** When a QC pattern
flags a paragraph that is in fact a faithful translation of the source — most commonly a
list connective like `; and` / `, and` (faithful translation of the Italian `; e`) — the
correct response is to inspect the flag against the source, **not** to alter the translation
to silence the script. As of rev34 the truncation check has a built-in whitelist that
suppresses the `; and` / `, and` / `; or` / `, or` false positive automatically. If a future
QC flag turns out to be a similar false positive (the source supports the translation as
written), keep the faithful translation, note the false positive in delivery notes, and
proceed. Reaching 0 issues is desirable but never at the cost of fidelity. See SKILL.md
Common Pitfalls — "Translator alters source-faithful translation to satisfy a QC linter."

### Step 9 is MANDATORY — never skip it

`quality_check.py` is **not optional**. It runs at Step 9 of every document, including each document in a multi-document session. If the script fails to run for any reason — including suspected install-pipeline truncation — **do not skip Step 9 and deliver anyway**. Instead:

1. Run `python <skill-path>/scripts/quality_check.py --help` to see if the integrity check fires (rev35 added a `_check_self_integrity()` guard with sentinel `# === SKILL FILE COMPLETE ===`). If it reports `FILE INTEGRITY CHECK FAILED — script truncated`, the local install is corrupt — re-install the skill from the .skill / .zip archive and retry.
2. If the script runs but errors mid-execution, fix the error (paragraphs.json malformed, document.xml not found, etc.) and re-run.
3. **Do NOT deliver a translation while Step 9 has been skipped** because the script is broken. Block delivery until QC runs cleanly. The auto-invoked gates inside apply.py and repack.py do not substitute for QC — they catch a different class of defects.

## Internal compliance check — 08-aux-and-quality

Before moving to the next step, confirm:

- [ ] You translated every auxiliary XML file (headers, footers, comments, footnotes, endnotes) flagged in Step 8
- [ ] You ran `quality_check.py` and it ran cleanly (no integrity-check failure, no Python error). If it didn't run cleanly, you did NOT proceed to delivery — you re-installed or fixed the input.
- [ ] You acted on any source-language remnants `quality_check.py` flagged
- [ ] You did NOT decide an aux file was "trivial" and skip translating it
- [ ] If QC flagged a paragraph and you "fixed" it, the fix preserves source fidelity (you did NOT silently strip a connective, preposition, defined term, or other semantic content to satisfy the linter)

If any check is uncertain, STOP. Re-read this file. Do not proceed.

**Next:** `skill-docs/10-repack-and-validate.md`
