---
name: "Word Editor"
description: "Edit, query, and transform Word documents (.docx) with the SuperDoc CLI. Use when the user asks to read, search, modify, format, comment, track changes, or review changes in .docx files. Triggers on any task involving Word documents — text replacement, redlining, contract markup, template filling, bulk edits, content extraction, or document review."
metadata:
  author: "Dr. Antoine Louis"
  license: "agpl-3.0"
  version: "2026-04-10"
---

# SuperDoc CLI (v1)

Use SuperDoc CLI for DOCX work. Use v1 commands (canonical operations and their helper wrappers).
Do not default to legacy commands unless explicitly needed for v0-style bulk workflows.

Use `superdoc` if installed, or `npx @superdoc-dev/cli@latest` as a fallback.

## Auto-Open in VS Code

Before starting any edit workflow, check if running inside VS Code by testing `VSCODE_PID`. If set, open the target document so the user sees changes live:

```bash
if [ -n "$VSCODE_PID" ]; then
  for cmd in code code-insiders cursor; do
    if command -v "$cmd" > /dev/null 2>&1; then "$cmd" "$DOC_PATH"; break; fi
  done
fi
```

- `VSCODE_PID` is set by VS Code itself — works for any agent extension (Claude Code, Codex, Cline, etc.) and the integrated terminal.
- Skip silently if not set. Idempotent: re-opening focuses the existing tab.

## Edit Identity: Ask Before Starting

Before opening a document for editing, ask the user under which name tracked changes should be attributed:
1. Their own name (e.g., the lawyer reviewing the document)
2. The AI agent's name as default (e.g., "Claude", "Codex", "Gemini")

Use the chosen name in `--user-name` on `open`. Convention for email: `<name>@lawvable.com`.

## Default Edit Mode: Tracked Changes

**Always use `--tracked` on every mutating command** unless the user explicitly asks for direct edits.

- `--tracked` is shorthand for `--change-mode tracked`.
- If a command returns `TRACK_CHANGE_COMMAND_UNAVAILABLE`, fall back to direct edit for that command only.

## Save After Every Mutation

The CLI and the VS Code SuperDoc extension run separate engines — the only sync point is the file on disk.

**Call `superdoc save` after every mutation** so changes appear live.

- Single mutation → `save` immediately.
- Tight group of 2-3 related mutations (e.g., replace + format) → `save` once after the group.
- Never defer `save` to end of session.

## Command Reference

**Read [references/index.md](references/index.md)** first — it lists all reference files by topic. Then read only the relevant file for your task (e.g., `references/track-changes.md` for accepting/rejecting changes, `references/mutations-apply.md` for batch find-and-replace).

Do NOT read all reference files at once — pick only what you need.

For commands not covered in any reference file, use `superdoc describe command "<name>"` as fallback.

## Common Patterns

### Global find & replace (most common)

Use `mutations apply` with `text.rewrite` + `require: "all"`. **Do NOT manually find → parse → build steps.**

```bash
superdoc open ./contract.docx --user-name "Claude" --user-email "claude@lawvable.com"

superdoc mutations apply --atomic true --change-mode tracked --steps-json '[
  {"id":"s1","op":"text.rewrite",
   "where":{"by":"select","select":{"type":"text","pattern":"Lawvable"},"require":"all"},
   "args":{"replacement":{"text":"Google"}}}
]'
superdoc save
superdoc close
```

- `require: "all"` → every match. `"first"` → first only. `"exactlyOne"` → fails if != 1.
- Batch multiple replacements in the same `steps` array (see [references/commands.md](references/commands.md)).

### Targeted single edit

Use `query match` (not `find`) to locate a target, then `replace`:

```bash
superdoc open ./contract.docx --user-name "Claude" --user-email "claude@lawvable.com"

superdoc query match --select-json '{"type":"text","pattern":"termination"}' --require exactlyOne
superdoc replace --tracked --target-json '{"kind":"text","blockId":"p1","range":{"start":0,"end":11}}' --text "expiration"
superdoc save

superdoc close
```

- `query match` returns exact addresses with cardinality guarantees. `find` does not — use it only for exploration.
- After `open`, commands run against the active session when `<doc>` is omitted.

### Tight group of related mutations

```bash
superdoc open ./contract.docx --user-name "Claude" --user-email "claude@lawvable.com"

superdoc query match --select-json '{"type":"text","pattern":"ACME Corp"}' --require exactlyOne
superdoc replace --tracked --target-json '{"kind":"text","blockId":"p2","range":{"start":0,"end":9}}' --text "NewCo Inc."
superdoc format bold --tracked --block-id p2 --start 0 --end 10
superdoc save

superdoc close
```

### Stateless reads (no session needed)

```bash
superdoc get-text ./proposal.docx
superdoc get-markdown ./proposal.docx
superdoc info ./proposal.docx
```

### Stateless mutation

```bash
superdoc replace --tracked ./proposal.docx \
  --target-json '{"kind":"text","blockId":"p1","range":{"start":0,"end":5}}' \
  --text "Updated" --out ./proposal.updated.docx
```

Stateless mutating commands require `--out` unless using `--dry-run`.

### Safety

- `--dry-run` to preview any mutation without applying.
- `--expected-revision <n>` for optimistic concurrency checks.

## Important Notes

- **Telemetry on stdout**: The CLI may print `[super-editor] Telemetry: enabled`. Use `2>/dev/null` when piping JSON. Prefer declarative selectors (`mutations apply`) over `find | parse` pipelines.
- **Legacy commands** (`search`, `replace-legacy`, `read`) exist for v0 compatibility. Use only for multi-file glob workflows.
- **Session cleanup**: `close` on dirty state requires `--discard` or a prior `save`.
