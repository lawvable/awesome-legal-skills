# Canonical Spec Schema

Every renderer in this skill consumes the same JSON spec. This file documents the schema.

The spec has six top-level keys, all optional except `meta`, `source`, and `scenarios`:

```json
{
  "meta":        { ... },          // required
  "design":      { ... },          // optional — defaults supplied
  "source":      { ... },          // required
  "families":    [ ... ],          // optional — auto-derived from scenarios if omitted
  "scenarios":   [ ... ],          // required
  "coverage_list": [ ... ],        // optional
  "methodology": { ... }           // optional
}
```

Save the spec to `<output-dir>/spec.json` before invoking any renderer. The spec is the single source of truth and re-rendering it with tweaked design is fast.

## `meta` — required

Identifies the document being audited and supplies headline/footer copy.

```json
{
  "title": "Tex. Ins. Code § 101.051",
  "subtitle": "Conduct That Constitutes the Business of Insurance",
  "kicker": "Interpretive-Ambiguity Stress-Test",
  "page_subtitle": "Seven places in § 101.051 where the statute is unclear enough to produce litigation, with both sides' arguments and a likely outcome for each.",
  "audit_date": "27 May 2026",
  "profile": "statute",
  "brand_short": "Tex. Ins. § 101.051",
  "brand_sub": "Ambiguity Stress-Test"
}
```

- `title`: Short reference name of the document (used in titles, breadcrumbs).
- `subtitle`: One-line caption that says what the document is.
- `kicker`: Eyebrow text above the main title (small caps, accent color).
- `page_subtitle`: One-sentence pitch for the landing page / cover.
- `audit_date`: When the audit was run. Free-form string.
- `profile`: One of `contract`, `statute`, `regulation`, `opinion`. Determines some default copy.
- `brand_short`, `brand_sub`: Used in the nav bar / footer / cover slide.

## `design` — optional, defaults supplied

Visual tokens. All optional; sensible defaults are applied.

```json
{
  "accent_color": "#8b3a1f",
  "accent_soft": "#c47e5a",
  "accent_deep": "#6b2d18",
  "dept_color": "#2c4a6e",
  "dept_bg": "#eef3f9",
  "adv_color": "#8b3a1f",
  "adv_bg": "#fbf0ea",
  "background_color": "#fbf8f1",
  "card_color": "#ffffff",
  "panel_color": "#f3ede0",
  "text_color": "#1f1b16",
  "highlight_color": "#fdf2c4",
  "primary_font": "Fraunces",
  "body_font": "Inter",
  "serif_font": "Crimson Pro",
  "family_palette": {
    "scope":      { "bg": "#dceadb", "fg": "#2c5a2c" },
    "vague":      { "bg": "#fadeb9", "fg": "#7a4a14" },
    "def":        { "bg": "#e4d4ee", "fg": "#523072" },
    "mensrea":    { "bg": "#f6d3d3", "fg": "#862828" },
    "conflict":   { "bg": "#cee0e8", "fg": "#1c485a" },
    "conlaw":     { "bg": "#eed1e0", "fg": "#6a2249" },
    "discretion": { "bg": "#ddd9f1", "fg": "#38346e" }
  }
}
```

**Single-color shortcut.** If the user wants only to change the accent, set `accent_color` and leave the rest. The skill should compute `accent_soft` (e.g., 60% mix with white) and `accent_deep` (e.g., 80% mix with black) when the user didn't supply them, but a faithful default is to let the user provide them explicitly.

**Family palette extensions.** If scenarios use a defect family not in the default palette, add a new key under `family_palette` with `bg` and `fg`. Family palette colors should be light/dark pairs with WCAG-AA contrast.

## `source` — required

The text being audited, broken into addressable units.

```json
{
  "name": "Sec. 101.051. Conduct That Constitutes the Business of Insurance",
  "sections": [
    {
      "id": "a",
      "label": "(a)",
      "subhead": "Definition",
      "text": "In this section, \"medical expense\" includes ...",
      "emphasize": ["medical expense"],
      "subprovisions": []
    },
    {
      "id": "b",
      "subhead": "Acts that constitute the business of insurance in this state",
      "subprovisions": [
        { "id": "b1", "label": "(b)(1)", "text": "making or proposing to make ..." },
        { "id": "b2", "label": "(b)(2)", "text": "...", "emphasize": ["as a vocation"] }
      ]
    }
  ]
}
```

**Section model.** A section may be a top-level provision with text and an ID, or a header-only grouping with `subprovisions` listed underneath. Both shapes are valid. Subprovisions may themselves contain `subprovisions` (e.g., (b)(6) containing (b)(6)(A) … (b)(6)(I)) — the schema recurses.

**IDs.** Every addressable unit needs a unique ID. The scheme is up to the audit but should be stable — scenarios anchor to these IDs. Conventional choices:
- Statute: subdivision marker without parens — `a`, `b1`, `b6B`, `c`.
- Contract: section number with underscores — `s2_1`, `s2_1_a`.
- Regulation: paragraph number — `p_a`, `p_b_1`.
- Opinion: paragraph or holding fragment — `holding_1`, `p_3`, `dictum_2`.

**`emphasize` array.** Substrings within `text` that should render in italics. Use sparingly — only for the words at the heart of the ambiguity.

## `families` — optional

Defect families used by scenarios. If omitted, the skill derives families from scenario `families` arrays and uses default labels.

```json
[
  {
    "key": "scope",
    "label": "Scope / coverage",
    "description": "Does the statute reach this actor or this conduct at all? In public law, whether the text applies is often the whole fight.",
    "diagnostic": "Can I draw a colorable line excluding a real-world actor or activity from the statute's domain entirely?"
  }
]
```

Default labels by key (used when families is omitted):

| Key | Label |
|-----|-------|
| `scope` | Scope / coverage |
| `vague` | Vague term |
| `def` | Definitional boundary |
| `mensrea` | Mens rea gap |
| `conflict` | Cross-clause tension |
| `conlaw` | Constitutional avoidance |
| `discretion` | Standardless discretion |
| `contradiction` | Internal contradiction |
| `gap` | Gap / silence |

A scenario may list multiple families — render with all pills shown.

## `scenarios` — required

The core analysis. Each scenario is a structured record.

```json
{
  "id": 1,
  "title": "Health care sharing ministry as \"funding mechanism\"",
  "tagline": "A pooled-funds ministry collects monthly contributions from 50,000 Texas members. Is it insurance, or is it religious cost-sharing the statute was not aimed at?",
  "anchors": ["b7"],
  "families": ["scope"],
  "situation": "A nondenominational ministry headquartered in Tennessee enrolls 50,000 Texas members ...",
  "positions": [
    {
      "label": "Position A",
      "actor": "Texas Department of Insurance",
      "argument": "The ministry contracts to provide reimbursement for medical expenses ..."
    },
    {
      "label": "Position B",
      "actor": "Ministry",
      "argument": "No contract exists. Sharing is morally binding only ..."
    }
  ],
  "weak_point": "\"By another method\" supplies no limiting principle ...",
  "likely_outcome": "The Legislature's later Chapter 1681 carveout presupposes ...",
  "redraft": "Add: <strong>\"Contracting to provide,\" in this section, includes ...</strong>"
}
```

**Field meanings.**
- `id`: integer 1..N, monotonically increasing. Renders as "S-N" in headers.
- `title`: full descriptive title, can be longer than the tagline.
- `tagline`: ≤2 sentences, used on cards/cover/slide titles.
- `anchors`: array of source IDs the scenario attaches to. At least one.
- `families`: array of family keys. At least one.
- `situation`: 3–6 sentences setting up the dispute. Neutral, factual.
- `positions`: array of exactly two opposed positions. Each has `label` (default "Position A" / "Position B"), `actor` (the realistic entity holding that position), and `argument` (the steel-manned reading).
- `weak_point`: one sentence naming the textual flaw.
- `likely_outcome`: predicted resolution with the doctrine that drives it.
- `redraft`: the proposed amendment. May contain HTML `<strong>` and `<em>` tags; renderers strip or honor as appropriate.

**Inline HTML.** The fields `situation`, `weak_point`, `likely_outcome`, `redraft`, and `argument` within positions may contain `<em>` and `<strong>` tags. Renderers honor these in HTML and LaTeX, convert to italic/bold runs in docx, and apply text-formatting in pptx.

## `coverage_list` — optional

Additional flagged ambiguities that did not get developed into full scenarios. Renders as a small-card grid in the website and as bullets in the docx / LaTeX.

```json
[
  {
    "label": "(a) 'professional mental health'",
    "note": "Does 'professional' require state licensure? Ejusdem generis with the listed licensed professions favors a licensure reading; the text does not say."
  }
]
```

## `methodology` — optional

Audit methodology — how the analysis was generated, what was filtered out, what the audit does not do. Renders as the "Methods" page in the website, an appendix in docx and LaTeX, and a closing slide in pptx.

```json
{
  "workflow":   ["Para 1 of workflow description...", "Para 2..."],
  "filter":     ["Para 1 of canon-filter description..."],
  "profile":    ["Para describing which audit profile was used and why..."],
  "scope":      ["Para describing what the audit does and does not cover..."],
  "research":   ["Para describing assumed law, cite-checking, research notes..."],
  "provenance": "One-sentence provenance line"
}
```

Each key is an array of paragraph strings (except `provenance`, which is a single string). The renderer concatenates paragraphs within a section.

## Validation

Before invoking a renderer, sanity-check the spec:

- Every anchor in every scenario must match an ID in `source.sections` (recursively). Catch typos here.
- Every family key in every scenario must be defined in `families` OR be one of the default keys above.
- Scenarios should have IDs 1..N with no gaps and no duplicates.
- `positions` arrays must have exactly two entries.

If validation fails, fix the spec (don't render an invalid one). The renderers may not check, and a missing anchor will silently produce a broken link.

## Example: minimal spec

The smallest spec that produces a usable site:

```json
{
  "meta": {
    "title": "Sample Contract § 7",
    "subtitle": "Termination for Convenience",
    "audit_date": "May 2026",
    "profile": "contract"
  },
  "source": {
    "name": "Section 7. Termination for Convenience.",
    "sections": [
      { "id": "s7_1", "label": "7.1", "text": "Either party may terminate this agreement at any time with thirty (30) days' written notice." }
    ]
  },
  "scenarios": [
    {
      "id": 1,
      "title": "Pretextual termination during performance",
      "tagline": "When can 'at any time' be challenged as bad faith?",
      "anchors": ["s7_1"],
      "families": ["vague"],
      "situation": "Buyer terminates the supply agreement two weeks before a scheduled delivery for which Supplier has already incurred non-recoverable costs ...",
      "positions": [
        { "label": "Buyer", "actor": "Buyer", "argument": "The contract says 'at any time' — no qualifier, no good-faith requirement." },
        { "label": "Supplier", "actor": "Supplier", "argument": "Texas law implies a duty of good faith into every contract; 'at any time' cannot be read to authorize pretextual termination calculated to avoid post-performance obligations." }
      ],
      "weak_point": "The clause says 'at any time' but does not address whether the right is subject to the implied duty of good faith and fair dealing.",
      "likely_outcome": "Most jurisdictions read 'at any time' against the backdrop of UCC § 1-304 and implied good-faith duties, which means the bare textual reading does not survive — but courts split on what 'good faith' requires when the contract is silent.",
      "redraft": "Add to § 7.1: <strong>The party exercising the right of termination under this Section need not have cause; provided, however, that termination during a period in which the other party has incurred non-recoverable costs in good-faith performance shall entitle the other party to recover such costs.</strong>"
    }
  ]
}
```

Even with no `families` block, no `coverage_list`, and no `methodology`, the renderer produces a clean site or document. Optional sections add depth where present; their absence is graceful.
