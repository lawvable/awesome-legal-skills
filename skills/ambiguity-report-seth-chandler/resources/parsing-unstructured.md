# Parsing Unstructured Input

The cleanest case for this skill is the structured output of `ambiguity-stress-test` — markdown with labeled fields per scenario. Real users won't always supply that. This file describes how to handle the messier cases.

## Three input signatures

**Signature A — fully structured.** Markdown with `### S-N — Title` headers and labeled fields:
```
### S-1 — Title

*Narrative:* ...
*Anchors:* ...
*Family:* ...
*Weak point:* ...
*Likely outcome:* ...
*Redraft:* ...
```
Or the variant with **bold labels** instead of italic. Both are common. Map directly into the canonical spec fields:
- `Title` → `title`
- `Narrative` or `Situation` → `situation`
- `Anchors` → `anchors` (parse comma-separated IDs)
- `Family` or `Defect family` → `families` (split on slashes or "+")
- `Weak point` → `weak_point`
- `Likely outcome` → `likely_outcome`
- `Redraft` → `redraft`

The narrative may already contain the two positions inline — sentences like "The prosecution argues … the resident argues…". Extract them:
- Look for "The [actor] argues" / "The [actor] contends" / "[Actor] argues" / "[Actor] says".
- Split into two `positions` objects with `actor` and `argument`.
- Whatever sentences remain (typically the first 1–2 setting up the facts) become the `situation`.
- If the narrative is genuinely a single block with no explicit positions, ask the user to identify the two opposed actors.

**Signature B — semi-structured.** Numbered scenarios in prose, each a paragraph or two but without labeled fields. Sometimes a redraft or a "likely outcome" is mentioned but not labeled. Apply the extraction heuristics below.

**Signature C — raw prose.** A memo, brief, or transcript that mentions ambiguities without isolating them. The skill must do more work: identify candidate ambiguities, propose scenario structure, confirm with the user.

## Extraction heuristics for Signatures B and C

**Identifying scenarios.** Look for these structural cues:
- Numbered or labeled lists ("First, …", "Second, …", "Issue #1: …").
- Repeated paragraph openings ("Another ambiguity arises when…", "A second problem is…").
- Topic-shift signals (em-dashes, bullet points, transition phrases).

When in doubt, ask the user: "I see you've identified [N] separate ambiguities — should I treat each as its own scenario, or combine some?" Don't silently merge or split.

**Identifying anchors.** Look for citation patterns:
- For statutes: `§ 7.2`, `(b)(3)`, `subsection (a)`, `Section 7.1`.
- For contracts: `Section X`, `Clause Y`, `paragraph Z`.
- For regulations: `Rule X.Y`, `§ XXX.YY(a)`.
- For opinions: `holding`, `paragraph N`, `the rule of X v. Y`.
If the cited unit doesn't appear in `source.sections`, either add it (if it's in the source text but not yet parsed) or flag the mismatch.

**Identifying defect family.** Read the prose and classify:
- Talks about *what the words mean* → `vague` or `def`.
- Talks about *whether the rule reaches an actor* → `scope`.
- Talks about *whose intent matters* or about silence on mental state → `mensrea`.
- Talks about *two provisions pointing different ways* → `conflict`.
- Talks about *one reading raising constitutional doubt* → `conlaw`.
- Talks about *unilateral power with no standard* → `discretion`.

If the family is genuinely unclear, ask. If multiple apply, list all.

**Identifying positions.** Even in raw prose, real disputes have two sides. Look for:
- Adversarial framing ("The plaintiff would argue…the defendant would respond…").
- Hedged uncertainty ("On one reading…on another…").
- A government-vs.-citizen pattern, a buyer-vs.-seller pattern, a regulator-vs.-regulated pattern.

When the prose has only sketched one side, **construct the steel-manned other side** based on what the text plausibly supports. Then surface what you did to the user: "I sketched the [adversary]'s position based on the text you provided — please confirm or revise."

**Identifying weak point and likely outcome.** These are often left implicit in unstructured input. Be willing to infer:
- The "weak point" is one sentence describing what the text fails to say.
- The "likely outcome" is a hedged prediction about how the dispute resolves under the relevant canons of construction or common-law doctrines.

If the input genuinely supplies neither, the skill can still render the scenario with the situation and positions only — but the analysis layer will be visibly thin. Flag this to the user and offer to fill it in (or ask them to).

**Identifying redrafts.** A redraft is the textual cure. If the input doesn't propose one, the skill can:
- Propose one based on the weak point (default behavior).
- Leave the field blank and mark it as "Drafter to propose."
- Ask the user which they prefer.

Default to proposing a redraft. A drafter can override; an empty redraft is jarring in the rendered output.

## Source text parsing

The `source` block in the spec requires the audited text broken into addressable units. If the input includes the full source, parse it:

**For statutes.** Regex on subdivision markers — `Sec.`, `§`, `(a)`, `(b)(1)`, `(b)(1)(A)`. Build a tree: top-level provisions are children of the section header; subprovisions nest as `subprovisions`. Assign IDs by stripping parens and concatenating: `(b)(6)(B)` → `b6B`.

**For contracts.** Headings are usually numbered (1, 2, 2.1, 2.1(a)). Parse hierarchically. IDs: `s2_1_a`.

**For regulations.** Similar to statutes but watch for "Subpart" and "Part" groupings that the renderer should treat as headers.

**For opinions.** Paragraphs are addressable but unlabeled in most opinions. Either number paragraphs sequentially (`p1`, `p2`, …) or use the court's own enumeration if present. The "holding" is usually identifiable; mark it as a top-level section.

If parsing is uncertain — overlapping numbering schemes, ambiguous subdivisions — produce a draft tree and show it to the user for correction before building scenarios.

## What to do if the source isn't supplied

The scenarios reference anchor IDs that don't exist anywhere the renderer can see. The site/document will look broken: anchor pills with no target, statute pages reading "[source not provided]".

Two options:
1. **Ask for the source.** Almost always the right move. Even one paste of the relevant section is enough.
2. **Render in "scenarios-only" mode.** Skip the statute pane on the website; skip the statute block in the docx/LaTeX. The result is usable as a memo but lacks the spine the skill is designed for. Use only when the source genuinely isn't available.

## Surfacing what was inferred

After parsing, show the user a brief summary of what got extracted vs. what was inferred:

```
Parsed input:
  - Identified 4 scenarios.
  - Anchored to source sections (a), (b)(2), (b)(7), (c).
  - Inferred defect families for 3 of 4 scenarios; scenario 2 was explicit.
  - Constructed Position B for scenarios 1 and 3 (input had only Position A).
  - Proposed redrafts for all 4; user supplied redrafts for scenarios 2 and 4.

Want me to render this, or do you want to revise first?
```

This protects against silent over-inference. The user can correct before any output is produced.
