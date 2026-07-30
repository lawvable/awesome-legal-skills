# Format — Website (multi-page or single-page)

The website renderer is the default format. It produces a complete static site that can be opened locally or uploaded to Netlify, Vercel, GitHub Pages, or any static host.

## Two modes

**Multi-page (default).** A folder of linked HTML pages plus a shared `style.css`. Each scenario has its own citeable URL. Good for a reference site readers will come back to, share by link, or print one page at a time.

```
site/
├── index.html              # Overview + scenario grid
├── statute.html            # Annotated source text
├── scenario-1.html ... scenario-N.html
├── families.html           # Pedagogical defect-family page
├── redrafts.html           # Amendment package
├── methods.html            # Methodology
├── style.css
└── netlify.toml            # Static publish config
```

**Single-page.** One self-contained HTML file with everything cross-linked via JavaScript. Sticky statute pane on the left, scenarios on the right, click-to-filter, anchor-pill jump-to-statute. Good for a dashboard view or a single shareable file.

```
site/
├── index.html              # Self-contained, all-in-one
└── netlify.toml
```

## Invocation

```bash
python scripts/generate_site.py \
  --spec <output-dir>/spec.json \
  --out <output-dir>/site \
  --mode multi
```

Flags:
- `--spec`: path to the canonical spec JSON.
- `--out`: target directory for the generated site. The script creates it if needed.
- `--mode`: `multi` (default) or `single`.
- `--no-netlify-toml`: skip the netlify.toml stub if the user is deploying somewhere else.

The script is pure Python, no external dependencies. Run it with system Python.

## Design

The default palette is warm cream + burnt sienna accent. Two adversary panels are slate blue (Position A) and burnt sienna (Position B). Defect families have a fixed pastel palette. All are overridable via the `design` block in the spec — see `data-format.md`.

Fonts are loaded from Google Fonts: Fraunces (display), Inter (UI), Crimson Pro (serif prose). If the deployment target blocks external fonts, the user can swap these via `design.primary_font`, `design.body_font`, `design.serif_font` and provide their own font stack.

## What the multi-page site contains

**`index.html`** — overview. Hero with title and subtitle, a brief lede, a grid of scenario cards (each showing num + title + tagline + anchor pills + family pills), and tile links to the major sections.

**`statute.html`** — the source text rendered as the primary artifact. Each addressable unit is a styled block; provisions that are anchored by scenarios get numbered badges linking to those scenarios. A right-rail "table of contents" lists all scenarios.

**`scenario-N.html`** — one per scenario. Breadcrumb, hero (num + title + tagline + meta pills), the situation block, two-sides panel (Position A vs Position B with actor names), an analysis card (weak point + likely outcome), the redraft callout, an "anchored in the source" excerpt block, a "related scenarios" list (other scenarios sharing a family or anchor), and prev/next nav.

**`families.html`** — pedagogical taxonomy. Each defect family present in scenarios gets its own block with the description, the diagnostic test, and the scenarios that use it.

**`redrafts.html`** — every proposed amendment collected as a legislative-amendment artifact. Each redraft block shows the problem statement, the proposal text in italic statutory voice, and a link back to its originating scenario.

**`methods.html`** — methodology, canon filter, scope notes, the coverage list of additional flagged ambiguities.

## What the single-page site contains

Same content, different chrome. The statute pane is sticky on wide screens. Scenarios are stacked cards. A filter bar at the top toggles defect families. Anchor pills and badge buttons cross-link by scroll-and-highlight rather than navigation.

JavaScript is inline and self-contained — no external libraries beyond fonts.

## Deployment to Netlify

Two paths:

1. **Drag-and-drop (Netlify Drop).** Open `https://app.netlify.com/drop` and drag the `site/` folder onto it. Netlify creates a free site at a random subdomain. This works for both multi-page and single-page modes.
2. **Git-backed deploy.** Push the `site/` folder to a GitHub repo, link Netlify to the repo. The included `netlify.toml` declares the publish directory as `.` so Netlify finds the HTML directly.

The generated `netlify.toml` is minimal:

```toml
[build]
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "SAMEORIGIN"
    X-Content-Type-Options = "nosniff"
```

If the user wants a custom domain, they configure that in Netlify after deploy.

## Common customizations

**Branding override.** "Use our firm's colors":
- Set `design.accent_color` to the brand red/blue/green.
- Set `design.dept_color` to a complementary slate.
- Leave `design.background_color` cream OR set to white if the firm prefers a colder feel.

**Section names.** If the audit is for a contract (not a statute), the user may want to rename sections in the nav:
- "The Statute" → "The Contract" (just change the page link text)
- "The Seven Fights" → "The N Issues" or "Disputes" or whatever fits

These are not currently controlled by the spec (the labels live in the renderer). Future work: expose nav labels in `meta`.

**Font swap.** A user uploading to a site without external font CDN access can replace Fraunces / Inter / Crimson Pro with system fonts. Add to spec:
```json
"design": {
  "primary_font": "Georgia",
  "body_font": "-apple-system, system-ui, sans-serif",
  "serif_font": "Charter, Georgia"
}
```

The script generates a font-face declaration only if the font names look like Google-Fonts candidates (CamelCase single names); otherwise it relies on system font availability.

## Tone calibration

The default lede copy on the index, families, redrafts, and methods pages is practical rather than ornamental. If the user wants more literary copy ("seams," "fights," "load-bearing") the `meta.page_subtitle` can be set to that register and the renderer honors it. For an academic audience, consider tightening to flatter, drier prose; the renderer does not enforce a register.

## Testing the output locally

After generation:

```bash
cd <output-dir>/site
python -m http.server 8000
# open http://localhost:8000
```

This serves the site locally and ensures all relative links resolve. Open the dev tools network tab to confirm no 404s.
