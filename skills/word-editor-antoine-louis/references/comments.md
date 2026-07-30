# Comments

> **Namespace is `comments` (not `comment`).** `comments add` is an alias for `comments create`. `comments remove` is an alias for `comments delete`.

### comments list

List all comment threads in the document.

```bash
superdoc comments list [flags] 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--include-resolved` | boolean | no | Include resolved comments |
| `--limit` | number | no | Max results |
| `--offset` | number | no | Skip first N |

### comments get

Retrieve a single comment thread by ID.

```bash
superdoc comments get --id <commentId> 2>/dev/null
```

### comments add (alias: comments create)

Add a new comment thread anchored to a text range.

```bash
superdoc comments add --block-id <id> --start <n> --end <n> --text "Review this" 2>/dev/null
superdoc comments add --target-json '{"kind":"text","blockId":"ABC","range":{"start":0,"end":10}}' --text "Check this" 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--text` | string | no | Comment body |
| `--target-json` | JSON | no | `{"kind":"text","blockId":"...","range":{"start":N,"end":N}}` |
| `--block-id` | string | no | Target block ID (flat flag) |
| `--start` | number | no | Start offset (flat flag) |
| `--end` | number | no | End offset (flat flag) |
| `--parent-id` | string | no | Reply to existing comment thread |

### comments reply

Reply to an existing comment thread.

```bash
superdoc comments reply --parent-id <commentId> --text "I agree" 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--parent-id` | string | yes | Parent comment thread ID |
| `--text` | string | no | Reply body |

### All Comment Commands

| Command | Description | Key flags |
|---------|-------------|-----------|
| `comments list` | List all comment threads | `--include-resolved`, `--limit`, `--offset` |
| `comments get` | Get a specific comment | `--id` |
| `comments add` | Add comment (alias: `create`) | `--text`, `--target-json` or `--block-id`+`--start`+`--end` |
| `comments reply` | Reply to a comment thread | `--parent-id`, `--text` |
| `comments edit` | Edit comment content | `--id`, `--text` |
| `comments resolve` | Resolve a comment thread | `--id` |
| `comments delete` | Delete a comment (alias: `remove`) | `--id` |
| `comments remove` | Remove a comment (alias: `delete`) | `--id` |
| `comments move` | Move comment to new anchor | `--id`, `--target-json` |
| `comments set-internal` | Toggle internal/private flag | `--id`, `--is-internal` |
| `comments patch` | Patch fields on a comment | `--id`, various |
