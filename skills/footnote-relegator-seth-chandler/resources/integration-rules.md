# Integrating Demoted Text with Existing Footnotes

Scholarly drafts arrive with footnotes already in place — citation-only notes,
textual notes, or mixtures. Demotion must weave into that apparatus, not pile
on top of it. The rules, in order of application:

## 1. One anchor, one note

Never leave a sentence carrying two footnote flags because a demotion landed
next to an existing note. If the anchor sentence already has a note, the
demoted text **joins that note** rather than creating a neighbor.

- **Existing citation-only note** (a bare cite): the citation stays first,
  exactly as written; the demoted prose follows as a new sentence or
  paragraph within the same note. A cite followed by discussion is a normal
  scholarly note shape. Do not rewrite the citation, and do not interleave
  prose into the middle of a citation string.
- **Existing textual note on the same subject**: merge — place the demoted
  text where it reads naturally within the existing note (usually at the
  end), with a seam repair if needed. Both texts stay near-verbatim.
- **Existing textual note on a different subject**: this is the one case
  where a second note is acceptable — but first try anchoring the demotion to
  a different surviving sentence nearby (often the demoted text enriches more
  than one). If no honest alternative anchor exists, add the new note anchored
  at a different point in the sentence (e.g., after the specific clause it
  qualifies) so each flag sits next to what it annotates.

## 2. Citations travel with their sentences

Inline citations inside demoted text move down inside it, untouched. A
citation left in the body whose supporting sentence moved down is an error;
so is a demoted claim whose citation stayed up. After each move, check both
directions.

Bluebook nicety: a citation that used *Id.* or *supra* may break when its
antecedent moves or when notes reorder. After all moves are done, sweep every
*Id.*, *supra*, and *infra* in the document and repair antecedents. This is
mechanical but easy to forget; the memo should state that the sweep was done.

## 3. No notes-on-notes

If demoted text itself contains a footnote reference, fold that footnote's
content into the destination note (the cite or text lands where the reference
sat, in parentheses or as a following sentence — whichever reads as normal
note prose). The old note is then empty and is removed; numbering closes up
automatically.

## 4. Numbering

Do not hand-manage numbers. In Markdown, `[^id]` labels can be arbitrary
strings — when inserting many notes, use fresh labels (`[^r1]`, `[^r2]`, …)
rather than renumbering existing ones; renderers number by order of
appearance. In Word, footnotes are auto-numbered by position. What you must
actively maintain is **anchor order**: a note's reference mark should appear
in the body in the same order as any text that discusses it.

## 5. Placement of the anchor

Default: end of the surviving sentence the demoted text most enriches, after
closing punctuation. Exceptions: anchor mid-sentence (after a clause or a
quoted term) only when the note speaks to that clause specifically and the
sentence also carries an end-of-sentence note. Never anchor on a heading.

## 6. Endnotes

If the source uses endnotes rather than footnotes (common in some book
manuscripts), keep the source's convention — pandoc and Word both treat the
distinction as a rendering setting. Everything above applies unchanged.
