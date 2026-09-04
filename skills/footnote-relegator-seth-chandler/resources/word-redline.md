# Word Output: Clean Copy and Tracked-Changes Redline

.docx input produces two documents plus the memo only after the capability
preflight in SKILL.md succeeds. Do the editorial work in Markdown first
(Steps 1–6 of SKILL.md); this file covers only production.

## A. The clean copy

```
pandoc revised.md -o article-draft.docx --reference-doc=article.docx
python scripts/polish_footnotes.py article-draft.docx article-relegated.docx
```

`--reference-doc` carries the original's styles — but many documents format
footnotes with direct run properties and define no footnote styles at all.
Pandoc's output *references* `FootnoteReference`/`FootnoteText` regardless, so
against such a reference doc the calls render full-size on the baseline and
the notes at body size. `polish_footnotes.py` fixes this unconditionally:
it injects proper style definitions (superscript reference marks, note text
at `--size` half-points, default 9pt), gives each note number an explicit
superscript+size so Word and LibreOffice agree, and adds a period after the
note number ("27. See ..."; suppress with `--no-period`). Run it on every
pandoc-produced clean copy. If local rendering tools are available, render and
eyeball:

```
soffice --headless --convert-to pdf article-relegated.docx
pdftoppm -jpeg -r 100 article-relegated.pdf page && ls page-*.jpg
```

Read at least the first page and one page with dense footnotes. If the host
provides a dedicated Word-document verification workflow, follow its guidance.
Otherwise open the `.docx` in a Word-compatible application and inspect those
pages manually. Do not claim visual verification when neither route exists.

## B. The redline

The redline is the *original* document with each demotion recorded as Word
tracked changes: body text wrapped in `<w:del>`, a footnote reference inserted
under `<w:ins>`, and the note text added to `word/footnotes.xml` (itself
ins-marked so Word shows the note as inserted). The author accepts or rejects
each move in Word; rejecting restores the original exactly.

### Pipeline

```
unzip -q article.docx -d unpacked/
find unpacked -type l -delete                      # strip symlinks (untrusted docx)
```

The bundled redline script finds text across consecutive runs within one
paragraph, so no companion skill is required. It stops on spans interrupted by
non-text elements such as an existing footnote reference; handle those cases
manually only if the host can safely edit and verify OOXML. Otherwise omit the
redline, deliver the clean copy and memo, and explain the limitation.

Write a **plan JSON** directly from your demotion ledger:

```json
{
  "author": "footnote-relegator",
  "moves": [
    {
      "delete": "exact body text to demote, as it appears in the document",
      "anchor_after": "tail of the surviving sentence, ending at its final period",
      "note": "the footnote text, near-verbatim"
    },
    {
      "delete": "text whose destination is an EXISTING footnote",
      "merge_note_contains": "substring uniquely identifying that footnote",
      "note": "text appended to that note (no new reference is created)"
    },
    {
      "replace_find": "body text needing a seam repair",
      "replace_with": "the repaired text (tracked as del + ins)"
    }
  ]
}
```

Use the merge form for every demotion whose ledger destination is an existing
note — the anchor sentence already carries the reference, so the demoted prose
is appended to the note itself as a tracked insertion. Use the replace form
for the small referential body repairs the demotions force ("It also
emphasizes…" → naming the source whose introduction moved down).

Rules for plan strings: `delete` and `anchor_after` must match the document
text exactly and uniquely — extend a string with more
context if it matches twice. `anchor_after` should end exactly at the
character the reference mark follows (normally the sentence's closing
punctuation).

Then:

```
python scripts/docx_redline.py unpacked/ plan.json
(cd unpacked && rm -f ../article-redline.docx && zip -Xr ../article-redline.docx .)
```

Use any host-provided tracked-changes validator to compare the redline against
the original and require revision author `footnote-relegator`. This check
confirms every textual change is inside tracked markup — an untracked edit is
invisible in Word's accepted view and would silently corrupt the author's
document. Fix anything it reports before delivering.

If no such validator exists, use the manual fallback below. If the host cannot
open both tracked-change views, do not deliver the redline as verified; offer
the clean copy and memo instead.

### What the script does and does not do

`docx_redline.py` normalizes multi-child runs, finds plan text even when it
spans several runs of one paragraph (differing formatting, page-break markers),
splits boundary runs, wraps deletions, inserts ins-marked references, appends
ins-marked note text (to new or existing notes), creates `word/footnotes.xml`
(with relationship and content-type entries) if absent, and preserves the
document's namespace declarations on write. It **fails loudly, per move**,
when: text is not found, matches twice, or the span is interrupted by a
non-text run such as an existing footnote reference. Failed moves are listed
at the end — apply those by hand in the XML only when the host provides a safe
OOXML-editing and verification path, then re-validate.
The commonest hand case is demoting a sentence that itself carries a footnote
reference (fold: delete text + reference together, append the note's citation
text to the destination note, and mark the emptied paragraph's mark deleted
if the whole paragraph moved).

Deletions that span whole paragraphs: the script handles text within one
paragraph. To demote multiple paragraphs, use one move per paragraph; a move
cannot cross a paragraph boundary. Mark the paragraph mark itself deleted by
hand only if the empty paragraph would disturb layout
(usually accepting the deletion in Word cleans this up; leave a note in the
memo either way).

### Verify the redline

Use a host-provided tracked-changes validator when available. Then render or
open-check both views:

1. Confirm the archive is structurally readable (`python -m zipfile -t
   article-redline.docx`) and opens without repair warnings.
2. In the rejected-changes view, compare the body and notes with the original;
   they must match. Any difference indicates an untracked edit.
3. In the accepted-changes view, compare the body and notes with `revised.md`;
   they should match apart from whitespace and note-numbering noise.
4. In the reviewing pane, confirm each plan entry appears under author
   `footnote-relegator` and that no unrelated change appears.
5. Render or inspect at least the first page and one page with dense footnotes.

If the host offers an accept/reject simulation utility, it may automate steps 2
and 3. The outcome requirements above control; no particular companion tool is
required.

### Pre-existing complications — check before starting

- **Existing tracked changes**: stop and ask the user to accept/reject them
  first. Layering revisions on revisions is ambiguous for the reviewer.
- **Comments**: safe to leave; do not anchor demotions inside a comment range
  if avoidable.
- **Fields** (cross-references, auto-TOC): a field referring to moved text
  keeps working only if its bookmark survives; flag any bookmarks inside
  demoted spans in the memo.
- **Endnotes**: same pipeline, `word/endnotes.xml`, `w:endnoteReference`;
  the script's `--endnotes` flag switches part names and element names.
