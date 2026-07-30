# Format — PowerPoint deck

The PowerPoint path produces a `.pptx` suitable for presenting the audit at a meeting, a CLE, a client briefing, or a legislative hearing. One scenario per slide; speaker notes carry the analytical depth that doesn't fit on a slide.

## Delegation to the pptx skill

This skill does not implement pptx generation directly. It delegates to the existing `pptx` skill (loaded via the Skill tool). That skill uses `python-pptx` and knows the patterns for layouts, masters, shapes, fonts, and speaker notes.

**Workflow.**
1. Read the spec.
2. Invoke the `pptx` skill (or read its SKILL.md if not directly invocable).
3. Build the deck by walking the spec, applying the slide structure below.
4. Save to `<output-dir>/deck.pptx`.
5. Deliver the file to the user by whatever mechanism the host provides; if none exists, state the output path.

## Slide structure

The deck is built for live presentation. Total slide count = ~6 + N scenarios + 2 closing slides.

**Slide 1 — Title.**
- Centered: `meta.title` (big, serif, primary color), `meta.subtitle` (smaller, secondary).
- Below: `meta.kicker` in small caps.
- Bottom: `meta.audit_date`, presenter name (leave blank for user to fill).
- Background: solid `design.background_color`, with a thin band of `design.accent_color` along the left edge.

**Slide 2 — What this audit is.**
- Title: "What this audit is"
- Bullets summarizing the deliverable:
  - "[N] places in {source} where the text is unclear enough to produce litigation"
  - "For each: the situation, both sides' arguments, the likely outcome, a proposed amendment"
  - "Methodology: {profile} profile, canon filter applied"
- Speaker notes: longer narrative version, drawn from `meta.page_subtitle`.

**Slide 3 — The source at a glance.**
- Title: `source.name`
- A condensed render of the section structure — heading-only or with short text. If the source is small, render in full; if long, render only top-level structure (e.g., "(a) Definitions / (b) Acts that constitute the business / (c) Extraterritorial reach"), and note which subdivisions are contested.
- Visual: provisions with anchored scenarios get small dot markers in `design.accent_color`.
- Speaker notes: brief summary of what the document does.

**Slide 4 — The N fights at a glance.**
- Title: "The {N} fights"
- 2- or 3-column layout: each scenario as a small card with S-N, short title, and the family pill colored according to `design.family_palette`.
- This is the visual table of contents.
- Speaker notes: "I'll walk through each in detail next."

**Slides 5 through 5+N — One per scenario.**
- Title: "S-N · {title}"
- A colored band along the top in the family color (use `families[0]` if multiple).
- Body layout: left half = situation (short paragraph), right half = two stacked boxes for Position A and Position B (actor name in small caps + 2-3 sentence argument).
- Bottom: anchor pills inline.
- Speaker notes carry:
  - The full situation text (if abbreviated on slide).
  - Weak point.
  - Likely outcome.
  - Reference to the redraft (without the redraft text — that gets its own slide later if redrafts slide is included).

**Slide 5+N+1 — Redrafts overview.**
- Title: "Proposed amendments"
- A list of R-1 through R-N with one-line description and the target provision.
- Visual: same family-color dots as the source-at-a-glance slide.
- Speaker notes: explain the package as a whole.

**Slides 5+N+2 through 5+2N+1 — One slide per redraft (optional).**
- Title: "R-N · {target provision}"
- Body: the problem in 2-3 lines, then the proposed amendment text in a callout box (yellow-tinted background).
- Speaker notes: rationale, cross-reference back to the scenario.

If time is tight (the user asks for a "short deck"), skip the per-redraft slides and keep only the overview.

**Slide N — Methodology.**
- Title: "Methodology"
- 3-4 short bullets covering: profile used, canon filter, what's excluded (validity/legality, current-law check).
- Speaker notes: the full text from `methodology.workflow` + `methodology.filter` + `methodology.scope`.

**Slide N+1 — Closing / Q&A.**
- "Thank you" or "Questions?"
- Audit metadata (date, profile) at the bottom.
- Presenter contact line — leave blank.

## Visual design

**Colors.**
- Title slide and section slides: solid background = `design.background_color`.
- Family-color band on scenario slides: 8px tall along the top, color from family palette.
- Position A box: thin top border in `design.dept_color`, light background.
- Position B box: thin top border in `design.adv_color`, light background.
- Redraft callout: yellow background (`#f7f2e3` default), italic body.

**Typography.**
- Titles: serif, ~32pt, semibold.
- Body: sans-serif, 14-16pt.
- Speaker notes: don't worry about formatting; just plain text.

**Imagery.** None by default. The deck should read as a clean text-and-color presentation, not a stock-photo deck. If the user explicitly wants a header image (a courthouse, a state seal, etc.), they can add it after.

**Slide masters.** Define one master with two layouts: Title-and-body (for content slides) and Title-only (for section dividers). Most slides use Title-and-body.

## Common asks

**"Shorter deck."** Combine the at-a-glance slides and skip per-redraft slides. Target 10 slides for a 15-minute briefing.

**"Longer deck with more analysis on each slide."** Move parts of the speaker notes onto the slide (weak point as a line on the scenario slide, likely outcome as a line on the redraft slide). Watch out for slide density — speakers reading dense slides is the death of a presentation.

**"Two-deck output."** A "client deck" (cleaner, no methodology, no per-redraft slides) and a "team deck" (full version). Generate both.

## What this format does well

PowerPoint forces compression: one scenario per slide, the speaker carries the analysis. Good for stakeholders who need the overview without the full audit.

## What this format does poorly

Slides aren't suited to detailed reading. If a stakeholder wants to *study* the audit, give them the Word doc or the website — not the deck.
