# Core Mutation Commands

### replace

Replace content at a contiguous document selection. Text path accepts a SelectionTarget or ref plus replacement text. Structural path replaces whole blocks with SDFragment content.

```bash
superdoc replace --tracked --block-id <id> --start <n> --end <n> --text "new text" 2>/dev/null
superdoc replace --tracked --target-json '<SelectionTarget>' --text "new text" 2>/dev/null
superdoc replace --tracked --ref-json '"text:v4:eyJ..."' --text "new text" 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--text` | string | no* | Replacement text (text path) |
| `--target-json` | JSON | no* | SelectionTarget from `query match` |
| `--ref-json` | JSON | no* | Ref string from `query match` handle |
| `--block-id` | string | no* | Target block ID (flat flag alternative) |
| `--start` | number | no* | Start offset within block |
| `--end` | number | no* | End offset within block |
| `--content-json` | JSON | no* | SDFragment for structural replacement |
| `--in-json` | JSON | no | Story scope |
| `--nesting-policy-json` | JSON | no | `{"tables":"allow"}` to permit nested tables |
| `--tracked` | boolean | no | Apply as tracked change |
| `--change-mode` | string | no | `direct` or `tracked` |
| `--dry-run` | boolean | no | Preview without applying |
| `--expected-revision` | number | no | Optimistic concurrency check |

*Must provide either `--text` or `--content-json`, and one of: `--target-json`, `--ref-json`, or `--block-id`+`--start`+`--end`.

### insert

Insert content into the document. Text mode inserts inline content at a position. Structural mode inserts blocks.

```bash
superdoc insert --tracked --value "text to insert" 2>/dev/null                              # append to end
superdoc insert --tracked --block-id <id> --offset <n> --value "text" 2>/dev/null           # insert at position
superdoc insert --tracked --type markdown --value "## New Heading" 2>/dev/null               # insert markdown
superdoc insert --tracked --type html --value "<p>Paragraph</p>" 2>/dev/null                 # insert html
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--value` | string | no* | Text/markdown/html content |
| `--type` | string | no | `text` (default), `markdown`, `html` |
| `--target-json` | JSON | no | SelectionTarget or BlockNodeAddress for positioning |
| `--ref` | string | no | Ref string for positioning |
| `--block-id` | string | no | Block ID for inline insertion |
| `--offset` | number | no | Character offset within block |
| `--start` | number | no | Start offset (alias for text-based positioning) |
| `--end` | number | no | End offset |
| `--placement` | string | no | `before`, `after`, `insideStart`, `insideEnd` (structural inserts) |
| `--content-json` | JSON | no* | SDFragment for structural insertion |
| `--in-json` | JSON | no | Story scope |
| `--nesting-policy-json` | JSON | no | `{"tables":"allow"}` to permit nested tables |
| `--tracked` | boolean | no | Apply as tracked change |
| `--change-mode` | string | no | `direct` or `tracked` |
| `--dry-run` | boolean | no | Preview without applying |

*Provide either `--value` or `--content-json`. When both target and value are omitted, content appends at document end.

### delete

Delete content at a contiguous document selection. Supports cross-block deletion.

```bash
superdoc delete --tracked --block-id <id> --start <n> --end <n> 2>/dev/null
superdoc delete --tracked --target-json '<SelectionTarget>' 2>/dev/null
superdoc delete --tracked --ref "text:v4:eyJ..." 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-json` | JSON | no* | SelectionTarget |
| `--ref` | string | no* | Ref string from query match |
| `--block-id` | string | no* | Target block ID |
| `--start` | number | no* | Start offset |
| `--end` | number | no* | End offset |
| `--behavior` | string | no | `selection` (default) or `exact` |
| `--in-json` | JSON | no | Story scope |
| `--tracked` | boolean | no | Apply as tracked change |
| `--change-mode` | string | no | `direct` or `tracked` |
| `--dry-run` | boolean | no | Preview without applying |

*Provide one of: `--target-json`, `--ref`, or `--block-id`+`--start`+`--end`.

### clear-content

Clear all document body content, leaving a single empty paragraph.

```bash
superdoc clear-content 2>/dev/null
```

### blocks delete

Delete an entire block node by address.

```bash
superdoc blocks delete --target-json '{"kind":"block","nodeType":"paragraph","nodeId":"ABC"}' --dry-run 2>/dev/null
```

### blocks delete-range

Delete a contiguous range of top-level blocks between two endpoints (inclusive).

```bash
superdoc blocks delete-range --start-json '<BlockNodeAddress>' --end-json '<BlockNodeAddress>' 2>/dev/null
```
