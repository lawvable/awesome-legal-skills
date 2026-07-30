# Changelog — ICC skill

All notable changes to the `icc/` skill. Versions follow the suite-level
versioning indicated in the top-level `README.md`.

## v1.1.2 — 2026-06-02

Substantive correction following an expert verification pass.

- **Corrected the Article 28 numbering throughout the skill.** The Rome
  Statute's Article 28 uses lettered subparagraphs — `28(a)` (military
  commanders) and `28(b)` (other superiors), each with roman-numeral
  sub-elements — and has no numbered paragraphs. Earlier versions wrongly
  presented `Article 28(1)/(2)` as the Statute's numbering and `28(a)/(b)`
  as practitioner shorthand; this was inverted. Updated
  `references/citation-format.md`, `SKILL.md`,
  `references/verification-workflow.md`, and both examples to use `28(a)`
  (the *Bemba* military regime) and `28(b)` (the civilian / other-superior
  regime). The top-level `CLAUDE.md` constraint was corrected to match.

## v1.1.1 — 2026-05-30

Editorial consistency pass (suite-wide review); no substantive changes.

- Corrected the content-file count in the v1.0 and v1.1 notes (six files, not seven).
- Replaced tick and cross check-mark symbols in `verification-workflow.md` and the examples with plain-text markers, to match the suite's no-symbol house style.

## v1.1 — 2026-05-27

Reorganisation into the standard skill layout.

- Moved the six existing ICC content files from the repository root into
  `icc/references/` and `icc/examples/`.
- Added `icc/SKILL.md` as the skill entry point, gathering the core
  discipline, when-to-use guidance, workflow summary, pointers to the
  reference and example materials, and the five hard rules.
- Added this changelog.

No substantive changes to the content of the reference or example files in
this revision.

## v1.0 — initial

Initial content of the ICC skill, authored as six Markdown files:

- `authoritative-sources.md` — source hierarchy and icc-cpi.int fallback
  ladder.
- `citation-format.md` — citation formats for the foundational instruments
  and ICC documents; Article 28 shorthand discussion.
- `verification-workflow.md` — operational procedure and three-level
  verification gradient.
- `foundational-texts.md` — the four foundational ICC texts and what is
  not foundational.
- `example-verification.md` — worked verification examples (Bemba,
  Ntaganda).
- `example-audit.md` — working-draft audit and Court-record audit modes.
