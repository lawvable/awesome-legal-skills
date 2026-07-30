> **Pre-flight.** You should be entering this step having completed the previous step. **SKILL.md governs every step's discipline; if you have not read SKILL.md in full this session, STOP and `Read('SKILL.md')` before continuing.** Hard Rules from SKILL.md apply to this step too. **In Chat mode (no workspace folder, no auto-managed todo list) the same discipline applies — do not skim this step doc, do not bundle batches, do not skip the per-step Internal compliance check at the bottom.** **If this turn began from a compacted transcript, the compaction summary does NOT count as having read this step doc — `Read()` it now in full before any tool call.**

### Step 4: Translate ALL paragraphs

*[Internal compliance check — do not echo or paraphrase to the user. Re-read every rule in this step before executing. Do not deviate from any line of the skill. Do not bundle work, skip checks, or "interpret for efficiency" — every prior deviation has produced output below the quality the skill is designed to deliver. The skill's hard gates block deviations anyway; complying upfront is always faster than running into a gate and re-authoring paragraphs.json.]*

**The skill-wide Hard Rules apply to this step.** See SKILL.md for the full block. The rules that bite hardest in Step 4: ≤35 paragraphs per batch (enforced by `validate_translations.py`), every paragraph's complete `text` field must be in your context window during translation, and `en_runs` is mandatory for every definitions-section paragraph (enforced by `validate_en_runs.py` at the start of Step 5).

Translate **every non-empty paragraph** by filling in the `"en"` field in the JSON.

```json
{
  "idx": 42,
  "text": "\"Evento Rilevante Potenziale\" indica ciascun evento...",
  "runs": [
    {"start": 0, "end": 1, "text": "\"", "bold": false, "italic": false},
    {"start": 1, "end": 31, "text": "Evento Rilevante Potenziale", "bold": true},
    {"start": 31, "end": 95, "text": "\" indica ciascun evento...", "bold": false}
  ],
  "en": "\"Potential Event of Default\" means any event which...",
  "en_runs": [
    {"start": 0, "end": 1, "bold": false},
    {"start": 1, "end": 27, "bold": true},
    {"start": 27, "end": 80, "bold": false}
  ]
}
```

#### Translation rules

1. **Translate full paragraphs, not fragments.** You have full sentence context — use it.

2. **Preserve paragraph boundaries exactly.** One source paragraph = one English paragraph.
   Never merge or split paragraphs. Each paragraph inherits its formatting (style, numbering
   level, indentation) from the original. Splitting or merging breaks this alignment.

3. **Provide `en_runs` for any paragraph whose source `runs` array shows bold on text,
   AND for every paragraph in a definitions section or in a heading paragraph whose
   style provides bold .** The auto-detector inside
   `apply_translations_textmatch.py` only handles the classic `"X" means …` definition
   shape with explicit quotes. It will MISS bold on defined-term parentheticals in
   recitals (`(the "Agreement")`, `(hereinafter the "Substation")`), party-block defined
   terms, schedule listings, and any other body paragraph that *contains* a bold quoted
   span without being a textbook definition line. For all of those, populate `en_runs`
   explicitly — locate each bold quoted phrase in your `en` string and emit
   `{"start": …, "end": …, "bold": true}` for it.

   **Style-provided bold .** Definitions sections and clause/article headings
   often get their bold from the *paragraph style* (e.g. `FWBL1`, `ITScheduleL1`,
   bespoke template styles whose `<w:rPr>` in `styles.xml` carries `<w:b/>`), with
   the run-level `<w:rPr>` left empty. `extract_paragraphs.py` reads run-level
   formatting only, so `runs[i].bold` is **`false`** even though the rendered source
   is bold. If you supply only `en` for those paragraphs and leave `en_runs` null,
   `apply_translations_textmatch.py`'s default-off override (which exists to prevent
   style-bold leak from `basedOn` parents into body paragraphs) will *strip* the
   style's bold and the heading or definition will render plain. Identify these
   paragraphs by structural cues other than run-level bold:

   **Qualifier — run-level overrides that *defeat* the style.** Some authors apply
   direct run-level `<w:b w:val="0"/>` and/or `<w:i w:val="0"/>` overrides on every
   run of a heading paragraph specifically to suppress the style-inherited bold or
   italic for that one paragraph (typical pattern: a Heading3 style provides
   bold-italic, but the author wants this *particular* heading rendered plain, so
   they override at the run level). In that case, the rendered source is **plain**,
   not bold/italic, and emitting `en_runs:bold=true` would *over-bold* the
   translation — the inverse of the under-bold defect above.
   
   Decision rule, applied per paragraph:
   
   - If the paragraph is in a definitions section / has a heading style AND **at
     least one** run shows `runs[i].bold = true`: emit `en_runs` with `bold: true`
     (under-bold defence — the original rule).
   - If the paragraph is in a definitions section / has a heading style AND **every
     run** shows `runs[i].bold = false` (i.e. every run carries an explicit
     run-level override): emit `en_runs` with `bold: false`. The author has chosen
     to defeat the style's bold; respect that choice.
   - The same rule applies symmetrically for italic: emit `italic: true` only if
     at least one run shows `runs[i].italic = true`; emit `italic: false` if every
     run shows `runs[i].italic = false`.
   - Bold and italic are independent — a paragraph can be plain-bold (italic
     overridden off, bold inherited from style) or italic-only (bold overridden
     off, italic kept). Decide each property separately by the same per-property
     "any run true → true; all runs false → false" rule.
   
   Why this works: when every run has the explicit `false` override, the run-level
   property is what Word renders. When *no* run has any override (all `runs[i].bold`
   are `false` because the run-level `<w:rPr>` is silent), the style's inherited
   bold wins. Both cases produce `runs[i].bold = false` in `extract_paragraphs.py`'s
   output (the extract reads run-level only and cannot distinguish "silent" from
   "explicitly false"), so structural cues are still required to spot a definitions
   section in the silent case — but the *all-runs-bold-false* check uniquely
   identifies the explicit-override case and rules out a false bold emission.

   **Paragraph-mark override (`p_rpr_b` / `p_rpr_i`) — the strongest signal.**
   Some authors apply the bold/italic override at the *paragraph mark* (`<w:pPr>
   <w:rPr><w:b w:val="0"/><w:i w:val="0"/></w:rPr></w:pPr>`) rather than per-run.
   This pattern is common in Norwegian / Scandinavian drafts where Heading3 is
   rendered bold-italic by default but selected paragraphs are intentionally
   plain. Extract reads run-level only, so all such paragraphs look identical
   in the `runs` array. As of rev38, `extract_paragraphs.py` also captures the
   paragraph-mark setting as a tri-state field on the JSON entry:
   
   - `p_rpr_b == "false"` (or `p_rpr_i == "false"`) — author explicitly turned
     OFF style-inherited bold (or italic) for THIS paragraph. Emit
     `en_runs:[{...,"bold": false, ...}]` (or `italic: false`) regardless of
     whether the paragraph would otherwise have been treated as a heading.
   - `p_rpr_b == "true"` — author explicitly turned ON paragraph-mark bold.
     Emit `bold: true`. (Same for italic.)
   - field absent — no paragraph-mark setting; the pStyle cascade decides.
     Apply the heading rule and the all-runs-bold-false qualifier above.
   
   Decision priority for headings (apply in order, stop at first match):
   1. `p_rpr_b == "false"` ⇒ emit `bold: false` (paragraph mark wins)
   2. `p_rpr_b == "true"` ⇒ emit `bold: true` (paragraph mark wins)
   3. Any run shows `runs[i].bold == true` ⇒ emit `bold: true`
   4. Every text-bearing run shows `runs[i].bold == false` AND no `p_rpr_b`
      AND the paragraph is in a heading style ⇒ emit `bold: true` (style
      cascade wins; the silent-rPr case)
   5. Otherwise ⇒ emit `bold: false`
   
   The same five rules apply symmetrically and independently for italic
   using `p_rpr_i` and `runs[i].italic`. Bold and italic are decided
   separately — a paragraph can be plain-bold or italic-only or both/neither.

   - **Definitions sections** are typically labelled — a section heading paragraph
     reading `Definitions`, `Defined Terms`, `Definitions and Interpretation`,
     `Interpretation`, or prefixed by `Article 1`, `Clause 1`, `Section 1`, or a
     numbered annex labelled `Definitions`. Body paragraphs in such a section follow
     the predicate pattern `Term : means / shall mean / has the meaning given to it
     in / indicates / signifies`, with or without quotes around the term.
   - **Clause/article headings** are identifiable by their paragraph style (any
     `pStyle` value not in the standard `Normal` / `BodyText` / `Default` set —
     particularly bespoke template styles like `FWBL1`, `ITScheduleL1`, `Heading1`,
     `FWHeader`) or by their structural shape (short, all-caps or capitalised, no
     terminal period).

   When you encounter either pattern, populate `en_runs` for every paragraph in the
   section even if the source `runs` array shows no bold. For a definition with a
   bold-italic defined term, emit
   `[{"start": 0, "end": <term_end>, "bold": true, "italic": true},
   {"start": <term_end>, "end": <text_len>, "bold": false, "italic": false}]`.
   For a heading paragraph rendered bold by its style, emit
   `[{"start": 0, "end": <text_len>, "bold": true}]`.

   `en_runs` may be null only when the source `runs` array shows no bold AND the
   paragraph is not in a definitions section AND its `pStyle` is a body-text style.
   When in doubt, apply the qualifier above — check whether **every** run has
   `runs[i].bold = false` (and same for italic). If yes, emit
   `en_runs:[{...,"bold": false, "italic": false}]` to *defeat* a style-inherited
   bold/italic that the author explicitly suppressed. If at least one run shows
   bold or italic true, emit those properties true. The "supply en_runs by
   default" advice is correct in spirit (under-specification strips bold from
   genuinely-bold headings), but you must populate `en_runs` with the **right**
   bold/italic values per the qualifier — over-bolding a paragraph the author
   intentionally rendered plain is just as visible a defect as under-bolding a
   genuinely-bold heading.

4. **Use the domain-appropriate English legal lexicon** from the reference files.

5. **Keep defined terms consistent** — same translation every time.

6. **Natural English word order**: "all existing and future plants" not "plants existing
   and future".

7. **English legal cross-reference conventions**: "this Deed", "Clause 2" (not "Article 2"
   for internal refs), "above"/"below" (not "that precedes"/"that follows").

8. **English variant: UK by default.** US English only when the user's original prompt
   explicitly requested it. See "Target English variant" section below for the full
   anti-drift rule and the decision-point list — when in doubt, UK.

9. **For empty paragraphs** (whitespace only), set `en` to the same whitespace.

10. **For purely structural text** (party names, addresses, registration numbers), copy with
    minimal changes — translate descriptions but keep names/numbers intact.

11. **For page/section headers** like "SCHEDULE B" or "ALLEGATO 1", translate the header text.

12. **Keep titles and headers within page width.** Cover-page titles and section headings
    inherit fixed font sizes and indentation from the original. If the English translation
    is significantly longer than the source, it may overflow the page boundary and become
    invisible. Abbreviate or restructure to stay within comparable character length.

13. **Never abbreviate, summarise, or condense a paragraph.** The English translation must
    contain ALL substantive content from the source paragraph, including: all percentages
    and numerical values, all monetary amounts (in figures and words), all defined terms and
    their parenthetical definitions, all cap amounts and thresholds, all time periods and
    deadlines, and all cross-references. If the source paragraph specifies "1% per week up
    to a cap of 15%", the translation MUST state "1% per week up to a cap of 15%". If the
    source specifies a contract price in both figures and words, the translation MUST include
    both. Omitting commercial terms from a translation is a critical error that renders the
    document unusable.

14. **Always space digits and alpha words.** Legal English places a single space between a
    number and the word it modifies: write `Section 5` / `500 euros` / `12 months` / `3
    business days`, never `Section5` / `500euros` / `12months`. Three exceptions: English
    ordinals keep no space (`1st`, `2nd`, `3rd`, `4th`, `21st`); compact unit abbreviations
    of one or two letters may follow the digit directly (`5km`, `10kg`, `500ml`, `24h`); and
    well-known acronym-plus-digit tokens are written solid (`A4`, `MP3`, `H2O`, `B2B`, `3G`).
    Everything else takes the space. When in doubt, insert the space — the pre-apply linter
    (`validate_segment_shapes.py`) flags the most common violations but only as warnings;
    the primary defence against this class of defect is getting it right at translation time.

**Design stage terminology (critical for construction/EPC contracts):**

The three-stage design hierarchy must be translated correctly:

| Design stage | Correct English | Common errors to avoid |
|---|---|---|
| Stage 1 (conceptual) | Preliminary Design | — |
| Stage 2 (intermediate) | Detailed Design | "Preliminary Design" (wrong stage), "Definitive Project" (calque) |
| Stage 3 (construction-ready) | Construction Design | "Executive Project" (calque) |

Getting these wrong (especially confusing Stage 2 with Stage 1) is a material error.

#### Formatting rules for en_runs

- **Defined terms** (text between quotes in a definition paragraph): `bold: true`
- **Section headings**: inherit formatting from the paragraph style (usually bold via pPr)
- **Everything else**: `bold: false, italic: false`

If you don't provide `en_runs`, the apply script auto-detects defined terms and applies bold.
This works for simple definitions but may miss complex cases.

#### Working in batches — MANDATORY SIZE LIMIT (MAX 35 PARAGRAPHS)

**HARD LIMIT: Every batch MUST contain at most 35 paragraphs. No exceptions.**

This limit applies equally to batch 1, batch 5, and batch 15. A known failure mode is that
batch sizes creep upward as the translation progresses — the first few batches are 30–35,
then later batches silently grow to 50, 60, 80+ paragraphs as you try to "finish faster".
**This is not allowed.** The quality cost of large batches is invisible to you but real:
truncated clauses, skipped nuance in defined terms, inconsistent terminology, and
paraphrased instead of translated text. These errors compound and are very hard to catch
after the fact.

**Before starting each batch, state the paragraph range explicitly** (e.g. "Batch 4:
paragraphs 106–140, 35 paragraphs"). If the remaining paragraphs exceed 35, you MUST split
them into multiple batches — do NOT translate them all at once just because "there are only
50 left".

For every batch: translate, save the JSON as a checkpoint, then validate before moving on.

**CRITICAL: Never truncate paragraph text when viewing.** When displaying paragraphs for
translation, you MUST see the COMPLETE `text` field of every paragraph. Do not use Python
preview commands with character limits like `text[:200]` or `p['text'][:120]`. Always display
the full text. Paragraphs over 300 characters typically contain critical commercial terms —
rates, caps, amounts, defined terms in parentheses — that appear in the second half of the
paragraph and will be silently lost if truncated.

After each batch, run the validation script to catch truncated translations before proceeding:

```bash
python <skill-path>/scripts/validate_translations.py <workdir>/paragraphs.json
```

This checks character ratios between source and target for every paragraph. If any paragraph
is flagged as potentially truncated (ratio below 0.6 for paragraphs over 150 characters),
re-read the full source text and re-translate before moving to the next batch.

#### Appendix: Tracked-change documents only — skip if no paragraph has tracked changes

> **SKIP EVERYTHING BELOW (until Step 4b) if no paragraph in the document has tracked
> changes.** A document has tracked changes if `extract_paragraphs.py` reported any
> paragraphs with `has_track_changes: true` in `paragraphs.json` (or you saw `<w:ins>` /
> `<w:del>` elements in `word/document.xml`). If neither is true, jump to Step 4b — the
> remaining subsections of Step 4 do not apply.
>
> **READ EVERYTHING BELOW if any paragraph has tracked changes.** Every TC subsection
> below is mandatory for TC documents.

#### Tracked-change paragraphs — MANDATORY DUAL TRANSLATION

Paragraphs that contain tracked changes (`has_track_changes: true` in the JSON) need **two**
translations:

1. **`en`** — the translation of the `text` field (the "accepted" text: what the reader sees
   after accepting all changes). This is the normal translation you do for every paragraph.

2. **`en_deleted`** — the translation of the `deleted_text` field (the struck-through text
   shown in redline view). This text represents what the author deleted during editing.

Both translations are required because the apply script handles these two text streams
separately: `en` is distributed across `w:t` elements (current/visible runs), while
`en_deleted` is distributed across `w:delText` elements (deleted runs). If you only provide
`en` and leave `en_deleted` empty, the deleted text stays in the source language — which is
immediately visible to any reader viewing tracked changes and is a HIGH severity defect.

**How to translate TC paragraphs:**

When you encounter a paragraph with `has_track_changes: true`:

1. Read the `text` field — this is the accepted/visible text. Translate it normally into `en`.
2. Read the `deleted_text` field — this is the struck-through deleted text. Translate it into
   `en_deleted`. The deleted text is usually a phrase or clause that was replaced by the
   inserted text. Translate it in the same style and with the same terminology as the rest of
   the document.
3. **Check that the TC makes semantic sense.** After translating both parts, verify that the
   tracked change reads naturally: the deleted text (struck-through) should represent the old
   version, and the accepted text should represent the new version. If the English doesn't
   make sense as a tracked change (e.g. the deletion and insertion don't form a coherent edit),
   adjust both translations until the change reads naturally.

**Example:**

```json
{
  "idx": 45,
  "text": "The Developer shall be entitled to assign this Development Agreement",
  "deleted_text": "shall not be entitled to unilaterally",
  "has_track_changes": true,
  "en": "The Developer shall be entitled to assign this Development Agreement",
  "en_deleted": "shall not be entitled to unilaterally"
}
```

In Word, this renders as: "The Developer ~~shall not be entitled to unilaterally~~ shall be
entitled to assign this Development Agreement" — a coherent tracked change showing the
author's edit from a prohibition to a permission.

**Bold fix for TC paragraphs:** The apply script automatically applies `w:b val="0"` (bold
off) to all runs in non-heading TC paragraphs. This prevents a common defect where bold
formatting from `w:ins` runs (which inherit bold from tracked-insertion styling) leaks into
the translated body text. You do not need to do anything special for this — the fix is
automatic in the apply script.

**TC bold-off bypass (rev38) — when the override would over-strip.** The bold-off
override above keys on `pStyle` containing `heading`/`title`/`cmsor`/`titre`. Documents
drafted in plain Word default styles — common in Japanese contracts and some Scandinavian
templates where headings get bold purely from run-level `<w:b/>` rather than from a
Heading-N pStyle — present every heading as a non-heading to that detector. As of rev38,
two additional bypasses prevent the override from stripping intentional bold:

1. **Operator authored bold** — if you emit `en_runs` with at least one entry whose
   `bold: true`, the override is skipped for that paragraph. Authorial intent wins.
2. **Source paragraph is uniformly bold** — if every text-bearing source `runs[i]`
   carries `bold: true`, the source is genuinely bold throughout (a strong signal it
   IS a heading) and the override is skipped automatically.

For an unstyled-but-genuinely-bold heading carrying TC, you can rely on bypass 2
(do nothing — the override skips itself) or be explicit and emit
`en_runs: [{"start": 0, "end": <text_len>, "bold": true}]` to trigger bypass 1.
Either path preserves the heading's bold across the apply step.

#### Segment-aware TC translation — MANDATORY for TC paragraphs

The `extract_paragraphs.py` script extracts a `tc_segments` array for each TC paragraph.
This array breaks the paragraph into ordered segments by tracked-change type:

```json
{
  "idx": 45,
  "has_track_changes": true,
  "tc_segments": [
    {"type": "regular", "text": "A Fejlesztő jogosult"},
    {"type": "del", "text": "egyoldalúan nem jogosult"},
    {"type": "ins", "text": "jogosult engedményezni a jelen Fejlesztési Keretszerződést"}
  ]
}
```

**You MUST translate each segment independently** and provide the translations in a matching
`en_segments` array. Each entry must have the same `type` as the corresponding `tc_segments`
entry, plus an `en` field with the English translation:

```json
{
  "en_segments": [
    {"type": "regular", "en": "The Developer"},
    {"type": "del", "en": "shall not be entitled to unilaterally"},
    {"type": "ins", "en": "shall be entitled to assign this Development Agreement"}
  ]
}
```

**Why this matters:** Without segment-aware translation, the apply script distributes the
English text proportionally across ALL active `w:t` elements — ignoring TC boundaries.
This causes English words to land at wrong positions relative to `w:ins`/`w:del` boundaries,
producing tracked changes that read incoherently when the user accepts or rejects them.
With `en_segments`, each segment's translation is distributed only to its own runs, keeping
TC semantics intact.

**Rules for segment translation:**

1. The number and order of segments in `en_segments` must EXACTLY match `tc_segments`.
2. Each `en_segments[i].type` must equal `tc_segments[i].type`.
3. Translate each segment so that accepting all changes produces a coherent sentence, AND
   rejecting all changes (keeping only `regular` + `del` segments) also reads coherently.
4. Still provide `en` (full accepted text) and `en_deleted` as before — these serve as
   fallbacks if the segment types don't match at apply time.

**Reject-all grammar — where articles and prepositions belong (MANDATORY read)**

Rule 3 ("rejecting all changes also reads coherently") is easy to violate in
practice. The defect looks like a fluent accept-all reading plus an
ungrammatical reject-all reading, because an English word whose grammaticality
depends on whether the neighbouring TC is accepted or rejected ended up in the
wrong segment.

Worked example — a tracked-change `<w:del>` removes the word that translates
as "respective" from a clause where the English needs "the respective" before
two nouns. The WRONG split puts the definite article in both the regular
span AND the del:

```
WRONG
  regular: " to "
  del:     "the respective "
  regular: "the addressees, and"

  accept-all: " to the addressees, and"              ← reads well
  reject-all: " to the respective the addressees, and"  ← "the respective the"
```

The RIGHT split moves the article that must disappear under accept-all into
the del, and keeps the adjacent regular span starting with the bare noun
where reject-all needs no article:

```
RIGHT
  regular: " to "
  del:     "the respective "
  regular: "addressees, and"

  accept-all: " to addressees, and"                  ← ungrammatical

RIGHT (adjusted)
  regular: " to the "
  del:     "respective "
  regular: "addressees, and"

  accept-all: " to the addressees, and"              ← reads well
  reject-all: " to the respective addressees, and"   ← reads well
```

**General rule — articles, prepositions, and any word whose grammaticality
depends on whether the neighbouring tracked-change is accepted or rejected
must live INSIDE the del or ins, not in the regular span adjacent to it.**
The same rule applies to defined-term phrase boundaries: if two consecutive
noun phrases come from different segments, at least one of them must carry
its own leading article/comma/whitespace so that reinstating the deleted
phrase does not collide with the adjacent regular phrase.

**Mechanical enforcement.** Before calling `apply_translations_textmatch.py`,
run `validate_reject_all.py` on the filled `paragraphs.json`:

```bash
python scripts/validate_reject_all.py workdir/paragraphs.json
```

The script reconstructs the accept-all and reject-all views from
`en_segments` for every paragraph with a del/ins and scans both for double
articles (`the respective the`), repeated words, stranded prepositions,
punctuation-then-letter run-together, double spaces, empty brackets/quotes,
and a list of forbidden collocations. Fix every hit by rewriting the
offending segments so the article/preposition lives on the correct side of
the TC boundary, then re-run. A clean run is required before apply.

**Non-Latin script sources have additional segment-shape rules.** If the
source language uses a non-Latin script — Chinese, Japanese, Korean, Thai,
Lao, Khmer, Cyrillic (Russian, Bulgarian, Serbian, Ukrainian, etc.), Greek,
Arabic, Hebrew, Devanagari, or any other — read the **Non-Latin script
sources only** appendix at the end of Step 4 *before* writing `en_segments`.
Latin-script sources (Italian, Dutch, Spanish, French, German, Polish,
Hungarian, Finnish, Portuguese, Czech, Romanian, Vietnamese, Danish,
Swedish, Norwegian, English, etc.) inherit inter-segment whitespace from
the source and can skip that appendix entirely.

Run `validate_segment_shapes.py` on the filled `paragraphs.json` to
mechanically catch segment-shape violations before
`apply_translations_textmatch.py` runs (this step applies to every
TC document regardless of source language):

```bash
python scripts/validate_segment_shapes.py workdir/paragraphs.json
```

It complements `validate_reject_all.py`: the shape scanner warns about
*splits* that predict defects; the reject-all scanner catches *grammar*
defects in the reconstructed views. Both should run clean before apply.

**ins_then_del segments (phantom tracked changes).** If the source docx
contains a `<w:ins>` whose only content is a `<w:del>` (i.e. author A
inserted text, then author B deleted author A's insertion), the extract
step emits a segment with type `ins_then_del`. Both accept-all and
reject-all render the phantom as empty, so the segment contributes nothing
to the visible English — but "Show Markup" will display whatever English
you write as strike-through. Always fill these in; leaving the source
language there is the single most common silent remnant in tracked-change
documents.

#### Collapsing orthographic-only and typo-fix TC edits — MANDATORY

A common pattern in source-language concept drafts is tracked changes that fix the
**source language** only — orthography, abbreviation style, hyphenation, diacritics,
spelling reform, or simple typos. These edits have no semantic content in the target
language and therefore no meaningful translation: both the deleted and the inserted
text map to the **same English string**.

The rule applies to at least these categories, in any source language:

1. **Abbreviation style** — Dutch `mn` → `m.n.`, Italian `ecc` → `ecc.`, French `cf` → `cf.`
2. **Hyphenation** — Dutch `zonneenergie` → `zonne-energie`, Dutch `pro-actief` → `proactief`
3. **Diacritic restoration** — Dutch `coordinaat` → `coördinaat`, French `a` → `à`,
   Portuguese `nao` → `não`, Spanish `si` → `sí`
4. **Spelling reform** — Dutch `pro-actief` → `proactief` (2005), German `daß` → `dass`
   (1996), Portuguese `acção` → `ação` (2009)
5. **Soft-hyphen / end-of-line artefacts** — `voor-geschreven` → `voorgeschreven`
   where a line-break hyphen was baked into the text
6. **Typo correction** — any misspelling fixed to its correct form, where both forms
   translate to the **same English word**. E.g. Italian `contrato` → `contratto`
   (*contract*), Polish `umowe` → `umowę` (*agreement*), German `Vetrag` → `Vertrag`
   (*agreement*). Same principle as 1–5: a source-language edit that vanishes in English.

Real examples from a Dutch concept draft, showing the rule in action:

| Source del | Source ins | What the edit is | English del | English ins |
|---|---|---|---|---|
| `mn` | `m.n.` | Abbreviation for *met name* — full stops added | *in particular* | *in particular* |
| `pro-actief` | `proactief` | 2005 Dutch spelling reform | *proactive* | *proactive* |
| `zonneenergie` | `zonne-energie` | Dutch three-vowel collision — hyphen added | *solar energy* | *solar energy* |
| `coordinaat` | `coördinaat` | Missing diaeresis restored | *coordinate* | *coordinate* |
| `2` | `6` | Meaningful date-digit change ("22" → "26 July") — KEEP DISTINCT | *2* | *6* |
| `voor-geschreven` | `voorgeschreven` | Soft hyphen from end-of-line break | *required* | *required* |

**Rule:** when the deleted and inserted source segments translate to the **same
English string** — whether because of orthography, diacritic, abbreviation,
hyphenation, spelling reform, or a simple typo — give the `del` and the `ins`
English segments the **identical English translation**. Do not manufacture a fake
distinction (the Dutch-to-English translator who writes "proactive" ↔ "pro-active"
in a TC has turned a no-op Dutch fix into a visible but meaningless English redline).

This applies both to `en_segments` and to the fallback `en_deleted` / `en` fields:

```json
{
  "idx": 14,
  "tc_segments": [
    {"type": "regular", "text": "combinatie met "},
    {"type": "del", "text": "zonneenergie"},
    {"type": "ins", "text": "zonne-energie"}
  ],
  "en_segments": [
    {"type": "regular", "en": "combination with "},
    {"type": "del", "en": "solar energy"},
    {"type": "ins", "en": "solar energy"}
  ],
  "en": "… combination with solar energy.",
  "en_deleted": "solar energy"
}
```

The `w:ins` / `w:del` markers are still present in the output, so the TC marker count
is preserved and the reviewer can still see *where* the editor made a correction in the
Dutch. But accepting or rejecting the change produces the same English text — which is
correct, because in English there is no difference to accept or reject.

**When NOT to collapse.** If the source edit changes meaning, even trivially, translate
both sides with their real English. A typo-correcting number change like `2` → `6` in a
date IS a meaningful edit (the date changed), so translate `del: "2"` / `ins: "6"`
verbatim — the reviewer *does* want to see the numeric change in the English.

**Decision test — in two steps:**
1. Would a monolingual English lawyer, looking only at the English redline, learn
   anything by flipping between "accept" and "reject"?
2. If yes → translate del and ins distinctly. If no → give them the same English.

A corollary: digit-only edits to dates, amounts, percentages, counterparty names,
defined terms, or cross-reference numbers are **always meaningful** and must never be
collapsed.

#### Scrambled / character-fragmented whole-word edits — MANDATORY

A distinct pathology from orthographic collapse: a source-language editor changes a
**single word or ordinal** to a **different single word or ordinal**, but does it
letter by letter — producing a `tc_segments` array with many character-level splits
that cannot be cleanly translated segment by segment because English normally replaces
the whole word, not character ranges.

Canonical example (Spanish road-use draft, clause heading):

```
source edit:         "Duodécima" → "Decimotercera"   (12th → 13th)
tc_segments:         [regular "D"], [del "Duod"],
                     [ins "e"],     [del "é"],
                     [regular "cim"],
                     [ins "otercera"], [del "a"],
                     [regular ".- Legislación, Fuero y jurisdicción"]
accepted text:       "Decimotercera.- Legislación, Fuero y jurisdicción"
rejected text:       "Duodécima.- Legislación, Fuero y jurisdicción"
desired English:     accepted  = "Clause 13. Governing law, venue and jurisdiction"
                     rejected  = "Clause 12. Governing law, venue and jurisdiction"
```

There is no one-to-one mapping from those 7 character-level segments onto English
text: the English edit is `Clause 12` → `Clause 13`, a two-token replacement. Left
alone, whatever `en_segments` the translator invents, orphan source letters (`é`,
`cim`, `otercera`, `D`, `ecimo`, …) leak into the redline view and the result reads
as `"Clause 13~~Clause 12~~eé cim otercera. Governing law…"` — cosmetically wrong
even though Accept/Reject land the right clause number.

**Detection — do this in Step 3b before drafting `en_segments`.** A fragmented
whole-word cluster is a maximal run of contiguous `tc_segments` that:

1. contains at least 3 ins/del pieces with at least one of each;
2. has no whitespace inside any segment's text;
3. concatenates to a coherent single word / ordinal on each of the Accept and
   Reject sides (e.g. `Decimotercera` vs `Duodécima`).

**Fix — scaffold `en_segments` with the English on the first ins/del of the
cluster and empty strings on all other cluster segments.** Two options, in
order of preference:

**Option A (preferred): run `coalesce_fragmented_tcs.py`.**

```bash
python <skill-path>/scripts/coalesce_fragmented_tcs.py <workdir>/paragraphs.json
```

The script does NOT touch `tc_segments` — the XML structure still has every
character-level run. What it does is **write a pre-filled `en_segments`
skeleton** into each flagged paragraph, one entry for every `tc_segments`
entry, with a `<<TRANSLATE: …>>` placeholder on the first ins and first del
of each detected cluster and the empty string `""` on every other cluster
segment. The translator only fills in the placeholders and the non-cluster
slots; the empty strings inside the cluster are the deliberate "clear this
run" instructions for the apply step. Use `--dry-run` first to preview.

For the road-use idx 117 example above, the script writes this skeleton
(one entry per tc_segments entry, in the original order — 8 entries for 8
source segments):

```json
[
  {"type": "ins",     "en": "<<TRANSLATE: ins='Decimotercera' (accepted)>>"},
  {"type": "del",     "en": "<<TRANSLATE: del='Duodécima' (rejected)>>"},
  {"type": "ins",     "en": ""},
  {"type": "del",     "en": ""},
  {"type": "regular", "en": ""},
  {"type": "ins",     "en": ""},
  {"type": "del",     "en": ""},
  {"type": "regular", "en": ""}
]
```

The translator replaces the two placeholders with their final renderings and
fills the trailing non-cluster `regular` entry with the rest of the heading:

```json
[
  {"type": "ins",     "en": "Clause 13"},
  {"type": "del",     "en": "Clause 12"},
  {"type": "ins",     "en": ""},
  {"type": "del",     "en": ""},
  {"type": "regular", "en": ""},
  {"type": "ins",     "en": ""},
  {"type": "del",     "en": ""},
  {"type": "regular", "en": ". Governing law, venue and jurisdiction"}
]
```

On Accept: the first ins carries "Clause 13", the other ins runs are empty,
the regular runs contribute "" and ". Governing law…" — the paragraph reads
"Clause 13. Governing law, venue and jurisdiction". On Reject: the first del
carries "Clause 12", the other del runs are empty, the regular runs
contribute "" and ". Governing law…" — the paragraph reads
"Clause 12. Governing law, venue and jurisdiction". No orphan source letters
leak through.

**Option B (manual fallback).** If you skipped Option A, write the same shape
by hand: full English `del` phrase on the first `del` of the cluster, full
English `ins` phrase on the first `ins`, `"en": ""` on every other cluster
segment, normal translations on non-cluster segments. This relies on the
empty-string behaviour of `apply_translations_textmatch.py`: `"en": ""`
(key present, value empty) **clears** the matching runs; no `"en"` key at
all **preserves** the source. Use Option A — running the script — instead
whenever you can.

**Why not accept the garbling.** Orphan source-language letters scattered
through an English clause heading make the redline unreadable for the
reviewer.

**Adjacent defect class — short consecutive ins/del clusters at apply
time.** Two consecutive `<w:ins>` (or `<w:del>`) XML elements carrying
short alphanumeric fragments (e.g. `"P"` then `"S"`) would otherwise be
re-joined as `"P S"` by `post_process.fix_spacing`'s alpha+alpha rule.
This is handled automatically: `extract_paragraphs.py` flags such
clusters in `tc_cluster_hits` at extract time, and
`apply_translations_textmatch.py` injects a zero-width space (U+200B,
invisible to the reader, noise to `strip_noop_tracked_changes`) at every
wrapper boundary at apply time, defeating the alpha+alpha rule
structurally. No operator action required. If a residual defect slips
through, `validate_apply.py --report-clusters --apply-zwsp` re-injects
ZWSPs into cluster-flagged en strings as a belt-and-suspenders
fallback — rarely needed.

#### Sub-appendix: Non-Latin script sources only — for TC docs with non-Latin source script

> **SKIP if source is Latin-script** (Italian, Dutch, Spanish, French, German, Polish,
> Hungarian, Finnish, Portuguese, Czech, Romanian, Vietnamese, Danish, Swedish,
> Norwegian, English, etc.). Latin-script sources carry inter-word whitespace that
> survives extract and apply, so segments separate cleanly without the rules below.
>
> **READ if source is non-Latin script** — Chinese, Japanese, Korean, Thai, Lao, Khmer,
> Cyrillic (Russian, Bulgarian, Serbian, Ukrainian, etc.), Greek, Arabic, Hebrew,
> Devanagari, etc.

**TROUBLESHOOTING — read this first if `validate_segment_shapes.py` passes but
apply produces glued text at TC seams.** This is the single most common failure
mode for non-Latin source TC paragraphs and the answer is Rule 1 below — go
straight there. Do NOT iterate through any of the following: literal ASCII
space at boundaries, leading-only ASCII space, NBSP (U+00A0) at boundaries,
NBSP at every leading edge, ideographic space (U+3000), thin space (U+2009),
en-space (U+2002), em-space (U+2003). They all return `True` from
`str.isspace()`, so `validate_segment_shapes.py` accepts them at line 224
(the `_rule_alpha_collision_no_space` whitespace-present check); they all
get removed by `apply_translations_textmatch.py`'s `.strip()` call inside
the `en_segments` distribution path (Python's `str.strip()` removes every
character whose `.isspace()` returns `True`). For European-source paragraphs
this never surfaces because `distribute_text_across_elements` restores
boundary whitespace from the source `<w:t>` element, and source elements in
European languages naturally have spaces. Non-Latin source elements have no
inter-character whitespace, so nothing is restored — the rendered output
reads `"theInvestment"`, `"of500MW"`, `"Clause3Insurance"`. The documented
fix is the visible-space + ZWSP hybrid in Rule 1: `" ​"` after a
regular segment, `"​ "` before a regular segment that follows an
ins/del. The ZWSP (U+200B) is Unicode category `Cf` (Format), NOT whitespace
per `.isspace()`, so `.strip()` stops at the ZWSP and the adjacent literal
space survives. **Read Rule 1 in full before authoring the first non-Latin
TC paragraph; do not iterate through whitespace candidates.** The path of
trial-and-error costs ~6–8 tool calls per failure; reading Rule 1 once
costs none.

Non-Latin scripts either write without inter-word spaces at all (CJK, Thai, Lao, Khmer)
or carry character classes that `fix_spacing` handles less reliably (Cyrillic, Greek,
Arabic, Hebrew, Devanagari). Either way, the English translator must **manufacture**
the whitespace English needs at segment boundaries. If `en_segments` are
`{"regular": "the contract"}, {"ins": "provisions"}, {"regular": " apply to"}`,
the output reads `"the contractprovisions apply to"` — one view fine, the other
collides two words.

Four rules, applied to every `en_segments` array:

1. **Bookend every regular↔ins/del seam with the visible-space + ZWSP hybrid (this is the default — read carefully, both failure modes below have been observed in production).** At the
   *trailing* edge of a regular segment that abuts an ins/del, append `" ​"`
   (one literal space, then U+200B ZWSP). At the *leading* edge of a regular
   segment that follows an ins/del, prepend `"​ "` (ZWSP, then one literal
   space). The visible space gives the reader a real separator in the rendered
   docx; the ZWSP anchors the space through `apply_translations_textmatch.py`'s
   `.strip()` (which strips trailing/leading whitespace per `str.isspace()` but
   stops at the ZWSP since ZWSP is Unicode category `Cf`, not whitespace), and
   the ZWSP is also treated as a token boundary by `validate_apply` and
   filtered out by `strip_noop_tracked_changes`. There are exactly two failure
   modes that the hybrid avoids:

   - **Literal space alone** — apply `.strip()`s the trailing/leading
     whitespace and the seam ends up glued in BOTH the rendered view and
     the validator-token view (`"theInvestment"`, `"of500262.5MW on"`).
   - **Pure ZWSP alone** — survives `.strip()` (validator-token view is
     fine because the tokeniser splits on ZWSP), but ZWSP is zero-width,
     so the *rendered* docx still reads `"theInvestment"` / `"of500MW"`.
     Markdown / `pandoc` previews look correct because they collapse
     ZWSPs to whitespace, but Word does not. This is the failure mode
     reported on a Japanese sponsor-guarantee MOU run.

   For ins/del segments that contain only digits or other non-alpha content
   (e.g., `"500"`, `"262.5"`), no further bookend is needed inside the ins/del
   — the regular sides handle the separator. For ins/del segments containing
   alpha text that abut another ins/del directly (no regular between them,
   e.g., `ins("Loan")` immediately followed by `del("Investment")`),
   bookend the inner edges with `"​"` (ZWSP only) — there is no rendered
   reader between two consecutive ins/del segments, so the visible-space
   half is unnecessary, and adding it would produce a double space when both
   sides accept- or reject-render. The recipe in one line: **regular sides
   carry visible-space + ZWSP; ins↔ins or ins↔del seams carry ZWSP only.**

   Worked example (verified on a Japanese sponsor-guarantee MOU re-run,
   the case that produced "of500262.5MW on" before the hybrid was applied):
   ```json
   {"type": "regular", "en": "with installed capacity of ​"},
   {"type": "ins",     "en": "500"},
   {"type": "del",     "en": "262.5"},
   {"type": "regular", "en": "​ MW on the Commercial Operation Date"}
   ```

   Worked example for alpha ins/del abutting alpha regular:
   ```json
   {"type": "regular", "en": "the ​"},
   {"type": "ins",     "en": "​Investment​"},
   {"type": "regular", "en": "​ Insurance"}
   ```

   Pure ZWSP bookend (`"​"` only, no visible space) is acceptable
   only when at least one side already has natural punctuation — period,
   comma, semicolon, opening or closing paren, em-dash — so the rendered
   text has a real visual separator from the punctuation itself. For
   alpha-alpha or alpha-digit boundaries (the common case in legal English
   prose), use the hybrid above.
2. **Never end a segment with a digit.** A digit on a TC boundary plus an alpha on
   the other side produces `"2025the"` / `"Clause5"`. Keep digits in the middle of
   their segment.
3. **Articles live inside the ins/del that contains the noun.** Same rule as the
   "Reject-all grammar" subsection earlier; bites harder here without a whitespace
   buffer.
4. **Never end a regular segment with a preposition.** Stranded prepositions on
   reject-all. Keep preposition + object in the same segment.

`validate_segment_shapes.py` (universal, already runs on every TC document) catches
violations mechanically. These rules are the prompt-side companion that keep the linter
silent.

**Backstop:  `fix_spacing` covers ins↔del seams.** `post_process.py`'s
`fix_spacing` now iterates `<w:t>` and `<w:delText>` together in document order, so
alpha+alpha collisions between an inserted run and an adjacent deletion's struck-
through text get a space inserted automatically. Visible glue in the reject-all
view (`"theInvestment Insurance"` from a `del("Investment")` between
`regular("the")` and `regular(" Insurance")`) is fixed without operator
intervention. ZWSP is still the recommended bookend for the validator-token view —
the two layers are complementary, not redundant.

**Rev20: the hybrid is now the default in Rule 1 above (was  caveat).**
The wording presented the visible-space + ZWSP hybrid as a "when
readability matters" exception under a pure-ZWSP default, and operators
reading top-down picked up pure ZWSP first. Pure ZWSP renders glued in
Word for alpha-alpha boundaries (the common case), so the order of
presentation got flipped: hybrid is the default, pure ZWSP is the
narrower case. See Rule 1 above for the full recipe and worked examples.

**Rev18: do NOT use Symbol-other characters (○ □ △ ◯ ■ ●) as placeholders.**
Japanese, Chinese and Korean documents commonly use ``○`` (U+25CB) for blank
date/number cells (``○年○月○日`` = year/month/day blanks). These characters are
Unicode category ``So`` and `strip_noop_tracked_changes._is_noise_only` treats them
as noise — any `<w:ins>` or `<w:del>` wrapper whose only content is one of those
symbols is removed during Step 6, leaving holes in the redline and triggering
validate_apply drift errors at end-of-Step-6. **Use digit ``0``** (or ``X``, ``_``)
for placeholder cells; those survive `strip_noop` because they are alphanumeric.
The skill does not auto-substitute because some placeholders are content-bearing
(a real ``○`` mark on a checkbox), so the operator must choose at translation
time.

## Internal compliance check — 04-translate

Before moving to the next step, confirm:

- [ ] You translated every paragraph of the source (no skipping, no summarisation)
- [ ] You stayed within the ≤35 paragraphs per batch cap
- [ ] You ran `validate_translations.py` after each batch (Step 4b)
- [ ] You populated `en_runs` for every definitions-section paragraph
- [ ] You produced `en_segments` for every TC paragraph (no shortcuts)

If any check is uncertain, STOP. Re-read this file. Do not proceed.

**Next:** `skill-docs/04b-translate-gates.md`
