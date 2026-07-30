# Format: Single-File HTML

One self-contained `.html` file, written directly from the spec. No script runs, nothing is imported, and the result opens by double-click on any machine.

This is the **universal fallback** — the only format with no host requirement at all — and it is also the right first choice whenever the deliverable has to be emailed, attached to a matter file, or opened by someone who will not unzip a folder.

## When to use it

- The host cannot run Python or write a directory tree. This is the only format that still works.
- The audience is one or two people who need to read it, not a team who will return to it.
- The deliverable must travel as an attachment.
- The user wants something now and the multi-page site is more machinery than the job needs.

Prefer the script-generated multi-page site where it is available and the audience will come back to it — per-scenario URLs are worth having, and this format has none.

## Construction

Write the file directly. Do not invoke `scripts/generate_site.py`; do not attempt to reproduce its output structure.

**Self-containment is the whole point.** Everything goes in one file:

- All CSS inside a single `<style>` block in the head. Take the design from `assets/site-style.css` — read it and adapt what this layout needs rather than inventing a new visual language, so the single-file output is recognisably the same product as the site.
- Any JavaScript inline, and keep it minimal. Smooth-scrolling anchors and a collapse toggle are worth having; nothing else is.
- No external stylesheets, no external scripts, no linked images.
- **No web fonts.** The multi-page site loads Fraunces, Inter and Crimson Pro from Google Fonts. This format must not: a file that phones out when opened is wrong for an emailed audit, and it will render badly offline. Use a system font stack — a serif stack for prose, a sans stack for UI — and map `design.primary_font`, `design.body_font` and `design.serif_font` onto it if the user set them.
- Honour the design tokens from the spec — `accent_color`, `accent_soft`, `dept_color`, `adv_color`, `background_color`, `family_palette`. Declare them as CSS custom properties at the top of the style block so a later tweak is a one-line edit.

## Document structure

Mirror the multi-page site's information architecture, flattened into one scrolling page with an anchor index at the top.

1. **Header** — title, source instrument, date, brand label if supplied.
2. **Contents** — a linked list of the scenarios, each with its defect family shown as a coloured pill. This is what replaces per-scenario URLs; make it good.
3. **Executive summary** — scenario count, families represented, and the one or two seams that matter most.
4. **The source text** — the instrument or the audited excerpt, in a bounded scrolling block, with provision IDs as anchor targets so a scenario's anchors can link into it.
5. **Scenarios** — one section each, in spec order, carrying every field: title, narrative, anchors linking back to the source block, defect family, weak point, likely outcome, and redraft or argument pair. Position A and Position B take the two side-panel colours, as on the site.
6. **Redrafts appendix** — every proposed cure collected as one amendment package, so a drafter can work from a single list.
7. **Methodology** — what produced the analysis, what the research step used or could not check, and the disclaimer that predicted outcomes are predictions.

## Scale

Single-file HTML holds a normal audit comfortably. Past roughly forty scenarios the page becomes unwieldy to navigate and the contents list stops carrying it — say so and recommend the multi-page site if the host can produce one.

## Delivery

One file, `report.html`. Deliver it by whatever mechanism the host provides, or state the path. It needs no zip, no folder, and no static host: opening it locally is the intended use, and uploading it anywhere also works.
