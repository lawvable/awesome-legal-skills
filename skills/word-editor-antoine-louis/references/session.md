# Session Lifecycle

### open

Open a document and create a persistent editing session.

```bash
superdoc open <doc> [flags] 2>/dev/null
```

| Flag | Type | Description |
|------|------|-------------|
| `<doc>` | string (positional) | Path to the .docx file |
| `--user-name` | string | Author name for tracked changes and comments |
| `--user-email` | string | Author email |
| `--content-override` | string | Seed body from markdown/html/text |
| `--override-type` | string | `markdown`, `html`, or `text` |
| `--password` | string | Document password |
| `--session` | string | Custom session ID |
| `--collaboration-json` | JSON | Collaboration provider config |
| `--collab-url` | string | WebSocket server URL (shorthand) |
| `--collab-document-id` | string | Room/document identifier (shorthand) |

Examples:

```bash
superdoc open my-doc.docx 2>/dev/null
superdoc open my-doc.docx --user-name "AI Agent" --user-email "agent@example.com" 2>/dev/null
superdoc open template.docx --content-override "# Title" --override-type markdown 2>/dev/null
```

### save

Save the current session to the original file or a new path.

```bash
superdoc save [flags] 2>/dev/null
```

| Flag | Type | Description |
|------|------|-------------|
| `--out` | string | Save to a different file path |
| `--force` | boolean | Overwrite if output file exists |
| `--in-place` | boolean | Save in-place (default behavior) |
| `--session` | string | Session ID |

Examples:

```bash
superdoc save 2>/dev/null                  # save in-place
superdoc save --out ./new.docx 2>/dev/null # save to a different file
```

### close

Close the active editing session and clean up resources.

```bash
superdoc close [flags] 2>/dev/null
```

| Flag | Type | Description |
|------|------|-------------|
| `--discard` | boolean | Close and discard unsaved changes |
| `--session` | string | Session ID |

Examples:

```bash
superdoc close 2>/dev/null             # close (must save first)
superdoc close --discard 2>/dev/null   # close and discard unsaved changes
```

### status

Show the current session status and document metadata.

```bash
superdoc status 2>/dev/null
```

### Session Management

| Command | Description |
|---------|-------------|
| `session list` | List all active editing sessions |
| `session save` | Persist the current session state |
| `session close --session <id>` | Close a specific session by ID |
| `session set-default --session <id>` | Set the default session for subsequent commands |

---

## History

| Command | Description |
|---------|-------------|
| `history get` | Query the current undo/redo history state |
| `history undo` | Undo the most recent history-safe mutation |
| `history redo` | Redo the most recently undone action |
