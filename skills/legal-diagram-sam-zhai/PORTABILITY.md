# Portability

Classification: standalone

This skill is self-contained. The whole folder, copied alone into any AI assistant's skills folder on a fresh machine, works without sibling skills, a vault, or machine-local paths. Extraction, type selection, and HTML rendering are pure Python over the filesystem; no external skill or document tool is invoked. Optional helpers (offline Mermaid engine, headless-browser render verification) degrade gracefully when absent.

## Portable Surface

- `SKILL.md`, `PORTABILITY.md`, `legal-diagram-readme.md`, `LICENSE`
- `requirements.txt`, `constraints.txt`
- `workflows/`, `references/`, `shared/`, `assets/`
- `scripts/` including `extraction/`, `normalize/`, and `tests/` (with synthetic fixtures and golden snapshots)

## Required When Copying

1. Copy the entire skill folder into the host assistant's skills folder. In Claude Code that is `~/.claude/skills/legal-diagram/`; other hosts use their own skills location.
2. Install Python dependencies once: `pip install -r requirements.txt -c constraints.txt` (release-verified versions), or omit `-c constraints.txt` for broad-compatibility testing.

## Required Runtime Dependencies

- Python 3.9+ on any OS.
- Markdown, plain text, pasted text, conversation context, and the Mermaid block output need only the Python standard library. `check_setup.py` reports which optional libraries are missing and which input formats remain available.

## Optional Dependencies

- `python-docx`, `PyMuPDF`, `openpyxl`, `python-pptx`: binary-format extraction. Absent, those formats are unavailable; Markdown, text, pasted input, and conversation context still work.
- `jinja2`: HTML export. Absent, the skill still emits the fenced Mermaid block.
- **Offline Mermaid engine.** HTML export prefers a vendored bundle at `assets/vendor/mermaid.min.js` (not shipped). Vendor it on demand while online with `python scripts/fetch_mermaid.py` (or `render_html.py --fetch-engine`), pinned to `MERMAID_VERSION` in `render_html.py` (Mermaid 11.x). `check_setup.py` and `first_run.py` only report whether the bundle is present; they never fetch over the network. Absent the bundle, output is source-only unless the caller enables the pinned CDN fallback with `--allow-cdn`.
- **Headless-browser render verification (Tier-1).** `scripts/verify_render.py` confirms the exported HTML renders without a Mermaid error. It is environment-agnostic via a `--browser-adapter`; supply your own driver (Playwright, Puppeteer, or a host-provided browser wrapper). Omit it and rely on the in-host preview (Tier-0).
- **mmdc golden render check (Tier-2).** A maintainer/CI check behind a pytest marker; skipped automatically when `mmdc` is absent.

## No Vault Or Personal Path Dependencies

No private vault, note system, or machine-local path is required. Chat output stays in the assistant; HTML reports write only to a user-selected path or the neutral default `./diagrams/`. File provenance records basenames by default; full source paths require the explicit `--include-source-path` opt-in.

## Adapter Notes

- **Structured-choice UI.** The skill uses user-decision gates (tutorial offer, build mode, multi-file scope, HTML report). Present them as a structured choice if the host supports one; otherwise as a numbered list in plain text, then wait for the reply. Every gate is a hard stop: never inferred from wording, never skipped, never pre-answered except by a literal flag the user typed.
- **First-run state.** `scripts/first_run.py` records whether the tutorial has been offered. State path resolves `$LEGAL_DIAGRAM_STATE`, then `~/.legal-diagram/state.json`. On a read-only or ephemeral filesystem the detector returns `unknown`; the skill then offers the tutorial rather than suppressing it, suppressing only on a confirmed `returning`. State lives outside the skill folder, so the package stays standalone. Override the path with `$LEGAL_DIAGRAM_STATE` to relocate or share it.
- **Headless-browser check.** Render verification is a documented shell step, not a Python subprocess shelled from inside the renderer (some browser wrappers are shell-only and a Python subprocess can deadlock). Run the verifier from your shell or host driver.
- **OS assumptions.** Pure Python, cross-platform. Doc commands use forward-slash paths; adapt to your shell. No reliance on a specific OS, shell, or editor.

## Public Defaults

- `input_source` is basename-only by default; `--include-source-path` is an explicit trusted-local opt-in.
- File parsing has default caps for file size, PDF pages, DOCX paragraphs/tables/table rows, PPTX slides/text shapes, and XLSX sheets/rows/cells. Limit hits set `truncated=true` and emit warning codes in the manifest where a partial parse is possible.
- HTML export writes to `./diagrams/` unless the user provides a path. Vendored Mermaid and render verification are optional and degrade to source-only or `unverified` with explicit notices.