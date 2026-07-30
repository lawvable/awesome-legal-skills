# HTML export workflow

Optional. Builds a standalone scientific-paper-figure HTML from Mermaid block and FigureDescription via `render_html.py`. Called by `direct.md` and `tutorial.md`.

## Step 1 — Opt-in

Caller passed `html_export=true` -> skip prompt. Otherwise present a structured choice when the host supports one, or a numbered list in plain text: **HTML report** (recommended) / **No, just the diagram**. Stop and wait for the reply. A path in the user's reply captures the output path.

## Step 2 — Collect inputs

Collect `semantic_map_json` from caller (passed from `workflows/generation.md` § Step 3.5). If absent or empty, default to `'{}'` — coloring JS no-ops gracefully and legend hidden.

Determine Mermaid asset mode. Prefer vendored file at assets/vendor/mermaid.min.js (skill-root relative, not committed; auto-fetched on demand via `python scripts/fetch_mermaid.py`, or `render_html.py --fetch-engine`). If absent, do not load network JavaScript unless user or caller explicitly accepts CDN fallback; CLI flag `--allow-cdn`, pinned to the version in `render_html.py` `MERMAID_VERSION` (Mermaid 11.x).

## Step 2a — Build the FigureDescription

Fields and per-type content from `shared/figure-description-schema.md`.
- `title`: `<matter_name> — <category_label>`; fallback `<category_label> — <YYYY-MM-DD>`.
- `matter_context`: matter_type + jurisdiction (if any) + one-line parties summary.
- `caption`: per-type one-line pattern.
- `overview`: 3 sentences (what it shows, why it matters to matter type, what decision it supports).
- `how_to_read`: per-type legend.
- `observations`: scan Mermaid block's structure, produce 3-5 plain-language bullets.
- `caveats`: matter-type base set + diagram-type addendum + date-validity note.

## Step 3 — Output path

User-specified path validated, else `./diagrams/` (created if absent; otherwise current directory). Filename `<matter_slug>_<diagram_type>_<YYYYMMDD>.html`. Collision appends `_2`, `_3`.

## Step 4 — Detect runtime and render

**Detect context first.** Check `render_html.py` reachable: run `python scripts/check_setup.py` or test `python --version`. Two paths:

**Render check (Tier-0, best-effort).** Before rendering, confirm the fenced Mermaid block previewed without a "Syntax error" (see `workflows/generation.md` § Step 3.4). On the web app this is the artifact preview; on the CLI it is the same pinned engine the export uses.

### 4a — CLI / local Python available

Forward everything `workflows/generation.md` handed over, not a stripped subset:

`python scripts/render_html.py --mermaid-block <block> --figure-desc <JSON> --output-path <path> --semantic-map '<semantic_map_json>' --digest-table '<digest_rows_json>' --source-path '<source_path>' --ui-lang <en|fr>`

- `--digest-table` / `--source-path`: required whenever Step 3.6 built `digest_rows`. Omitting them silently drops the Source Docs verification table, the evidence trail. Add `--relative-links` when the report ships beside its source files.
- `--ui-lang`: derive from the matter language (`language_profile` from extraction, else the prompt language). Use `fr` for a dominant-French matter, else `en`. Omitting it forces English chrome and `html lang=en` on a French matter, breaking the localization SKILL.md promises.
- `--allow-cdn`: append only after explicit approval for network-loaded Mermaid.

Script returns `{ok, output_path, file_size_kb}`. `PermissionError` → suggest alternative path, offer retry. Script-not-found or jinja2 missing → surface message, fall through to 4b.

### 4b — Web app / no local Python

Do NOT freehand the page. A freehand build reproduces almost none of the template's hardening (transparent black canvas, no pan/zoom, no contrast toggle, parser-fragile source) — exactly the reviewer-breaking export. Use `assets/html_template.html` as the literal scaffold and substitute only data:

1. **Copy VERBATIM from the template:** the `<head>` (including `<meta name="color-scheme" content="light">`), the entire `<style>` block, all control/tab/legend markup, and the entire `<script>` block (pan/zoom, semantic colouring, `enforceLabelsOnTop`, high-contrast, flip, fullscreen, editor, PNG/SVG export). Never re-author CSS, JS, or the Mermaid theme by hand.
2. **Substitute ONLY these slots:** `html lang`; `matter_title`, `matter_context`, `caption`, `overview`, `how_to_read`, each observation and caveat, each digest cell; the Mermaid source in BOTH the `<pre class="mermaid">` (HTML-escaped) AND `<script id="mermaid-source" type="application/json">` (JSON-encoded — the JS reads this stash, not the `<pre>`); `<script id="semantic-map" type="application/json">` (JSON-encoded); the Mermaid engine `<script>`; and the `ui.*` chrome strings.
3. **Escaping checklist** (do by hand what the template's Jinja `autoescape` + `tojson` do): HTML-escape `& < > " '` in every text slot above; JSON-encode (escape `< > &`) the two `application/json` stashes so a `</script>` or quote in content cannot break out; the ONLY raw-HTML slot is the fixed disclaimer constant, never matter text.
4. **Language:** pick the `ui.*` string set matching the matter language and set `<html lang>` to match (`fr` for a dominant-French matter, else `en`).
5. **Engine:** embed vendored Mermaid if available; the pinned CDN script (`https://cdn.jsdelivr.net/npm/mermaid@<MERMAID_VERSION>/dist/mermaid.min.js`, same version as `render_html.py` `MERMAID_VERSION`, Mermaid 11.x) only after explicit approval. Never hardcode an older version; never switch to an ESM/`+esm` URL (the scaffold loads a classic `<script>`).

One diagram per file (see § Multiple diagrams). Emit as an HTML artifact; the panel lets the user copy, open, or download.

## Step 4.5 — Render-verify (Tier-1, optional)

**Purpose.** Tier-0 (the preview step in `workflows/generation.md` § Step 3.4) catches parse failures before generation. Tier-1 is a post-export gate that re-checks the rendered HTML file for Mermaid parse errors, guarding against version-specific edge cases that static lint misses.

This step is **capability-detected and fully optional.** Never block the workflow on its absence; always emit an explicit notice instead of a silent pass.

### When mmdc (mermaid-cli) is available on the CLI

Run:

```
python scripts/verify_render.py <output.html>
```

- Exit 0 (`clean` or `unverified`) — proceed to Step 5.
- Exit 2 (`syntax_error`) — surface the error message, offer to refine the diagram source, and do **not** ship silently.

### When the host provides a headless browser but no mmdc

If the host exposes a headless browser or browser-automation driver (Playwright, Puppeteer, or a host-provided wrapper), verify by loading the file and checking for the Mermaid error text. Many such wrappers are shell-only, so run the check from your shell, not a Python subprocess (a subprocess can deadlock). The two steps: navigate to `file://<abs-path-to-output.html>`, then read whether `document.getElementById('diagramInner').textContent` contains `Syntax error`.

```bash
# Example shape (substitute your driver). In Claude Code the bundled agent-browser
# wrapper provides navigate/eval verbs; other hosts use their own driver.
<driver> navigate "file://<abs-path-to-output.html>"
<driver> eval "document.getElementById('diagramInner').textContent.includes('Syntax error')"
```

If the eval returns `true`, a Mermaid parse error is present — surface it and do not ship silently.

### When no renderer is available

Emit an explicit note: "Diagram not render-verified — install `@mermaid-js/mermaid-cli` (`npm i -g @mermaid-js/mermaid-cli`) and re-run `python scripts/verify_render.py <output.html>` to confirm the diagram renders cleanly."

Never treat absence of a renderer as a silent pass.

### Web app path (4b)

Rely on the Tier-0 artifact preview in `workflows/generation.md` § Step 3.4. No server-side renderer is available, so Tier-1 is skipped. Tier-0 must have confirmed a clean render before export.

---

## Multiple diagrams

One matter often needs several diagrams. The template is one-diagram-per-file by design: its IDs (`#diagramInner`, `#mermaid-source`, `#semantic-map`, `#editor`) are singular, so stacking blocks into one page wires only the first and breaks pan/zoom, colouring, edit, and export for the rest.

- Render each diagram as its OWN file: loop Step 4 once per diagram, filename suffix `_1`, `_2`, … Each file carries the full frame, controls, contrast, and zoom.
- Never freehand-bundle multiple `pre.mermaid` blocks into one page (the reviewer's 5-in-1 failure). A single composed multi-section page would need a template rewrite to per-section scoped IDs; that is out of scope here.
- A geometry `split` verdict (`workflows/generation.md` § Step 3.4) yields N diagrams; export them as N files by this rule, joined by the shared Source Docs digest table.

## Step 5 — Confirm

**CLI path:** Print "HTML exported to: `<path>`."
**Web app path:** Print "HTML figure ready in the artifact panel — open, copy, or download from there."

HTML embeds escaped diagram source, figure description, ARIA tab panels, labelled pill controls (Zoom in, Zoom out, Reset, High contrast, Flip, Full screen), a Save / Export menu (PNG, SVG, HTML), and an Advanced editor disclosure for tweaking the Mermaid source. Fully self-contained when a vendored mermaid.min.js (assets/vendor/ under skill root) is embedded into export; otherwise shows the source-only explainer panel unless `--allow-cdn` used. Description static once generated.
