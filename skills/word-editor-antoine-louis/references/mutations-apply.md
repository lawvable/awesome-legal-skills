# Critical Patterns

### mutations apply (batch / find-and-replace)

The most powerful command. Handles find-and-replace, multi-step edits, and atomic batches -- all declaratively. **Use this instead of individual replace/delete/format calls whenever possible.**

```bash
superdoc mutations apply --atomic true --change-mode tracked --steps-json '<JSON array>' 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--steps-json` | JSON array | yes | Array of mutation step objects |
| `--atomic` | boolean | no | Execute all steps in a single transaction (default: true) |
| `--change-mode` | string | no | `direct` or `tracked` |
| `--session` | string | no | Session ID |
| `--expected-revision` | number | no | Optimistic concurrency check |
| `--in-json` | JSON | no | Story scope (defaults to body) |
| `--out` | string | no | Output file path (stateless mode) |

### Step Format

Each step needs: `id`, `op`, `where`, `args`.

```json
{
  "id": "unique-step-id",
  "op": "<operation>",
  "where": { ... },
  "args": { ... }
}
```

Available `op` values: `text.rewrite`, `text.insert`, `text.delete`, `format.apply`, `assert`.

---

#### text.rewrite -- find and replace text

```json
{
  "id": "s1",
  "op": "text.rewrite",
  "where": {
    "by": "select",
    "select": { "type": "text", "pattern": "old text" },
    "require": "all"
  },
  "args": {
    "replacement": { "text": "new text" }
  }
}
```

**`require` values:**

| Value | Behavior |
|-------|----------|
| `"all"` | Replace every match (global find-and-replace). Fails if 0 matches. |
| `"first"` | Replace only the first match |
| `"exactlyOne"` | Fail if there is not exactly one match |

**`select` options:**

| Selector | Description |
|----------|-------------|
| `{"type": "text", "pattern": "..."}` | Substring match (default, case-insensitive) |
| `{"type": "text", "pattern": "...", "mode": "regex"}` | Regex match |
| `{"type": "text", "pattern": "...", "caseSensitive": true}` | Case-sensitive substring |
| `{"type": "node", "nodeType": "paragraph"}` | Match by node type |

**Optional: scope to a specific block with `within`:**

```json
"where": {
  "by": "select",
  "select": { "type": "text", "pattern": "old" },
  "within": { "kind": "block", "nodeType": "paragraph", "nodeId": "ABC123" },
  "require": "all"
}
```

**Optional: control replacement styling:**

```json
"args": {
  "replacement": { "text": "new text" },
  "style": {
    "inline": {
      "mode": "preserve",
      "setMarks": { "bold": "on", "italic": "clear" }
    }
  }
}
```

Style `mode`: `"preserve"` (keep original formatting), `"set"`, `"clear"`, `"merge"`.

---

#### text.insert -- insert text relative to a match

```json
{
  "id": "s2",
  "op": "text.insert",
  "where": {
    "by": "select",
    "select": { "type": "text", "pattern": "anchor text" },
    "require": "first"
  },
  "args": {
    "position": "after",
    "content": { "text": " inserted text" }
  }
}
```

`position`: `"before"` or `"after"` the matched text.

---

#### text.delete -- delete matched text

```json
{
  "id": "s3",
  "op": "text.delete",
  "where": {
    "by": "select",
    "select": { "type": "text", "pattern": "text to remove" },
    "require": "all"
  },
  "args": { "behavior": "selection" }
}
```

`behavior`: `"selection"` (default, deletes the matched text range) or `"exact"`.

---

#### format.apply -- format matched text

```json
{
  "id": "s4",
  "op": "format.apply",
  "where": {
    "by": "select",
    "select": { "type": "text", "pattern": "text to format" },
    "require": "all"
  },
  "args": {
    "inline": { "bold": true, "fontSize": 14, "fontFamily": "Arial" }
  }
}
```

All inline properties from `format apply` are available (bold, italic, underline, strike, fontSize, fontFamily, color, highlight, etc.). Set a property to `null` to clear it.

---

#### assert -- validate document state

```json
{
  "id": "s5",
  "op": "assert",
  "where": {
    "by": "select",
    "select": { "type": "text", "pattern": "expected text" }
  },
  "args": { "expectCount": 3 }
}
```

Fails the entire batch if the expected count does not match. Useful for precondition checks before mutations.

---

### Targeting with `where` -- the 3 modes

#### Mode 1: `by: "select"` (preferred for find-and-replace)

```json
"where": {
  "by": "select",
  "select": { "type": "text", "pattern": "search text" },
  "require": "all"
}
```

#### Mode 2: `by: "ref"` (from a previous query match result)

```json
"where": {
  "by": "ref",
  "ref": "text:v4:eyJ..."
}
```

Use the `.handle.ref` value from a `query match` response.

#### Mode 3: `by: "target"` (explicit SelectionTarget from query match)

```json
"where": {
  "by": "target",
  "target": {
    "kind": "selection",
    "start": { "kind": "text", "blockId": "ABC123", "offset": 0 },
    "end": { "kind": "text", "blockId": "ABC123", "offset": 8 }
  }
}
```

Use the `.target` value from a `query match` response.

---

### SelectionTarget Format

Used by `--target-json` across replace, delete, format apply, and `by: "target"` in mutations apply.

**Text-offset addressing (character-level):**

```json
{
  "kind": "selection",
  "start": { "kind": "text", "blockId": "ABC123", "offset": 0 },
  "end": { "kind": "text", "blockId": "ABC123", "offset": 8 }
}
```

**Block-edge addressing (whole-block operations):**

```json
{
  "kind": "selection",
  "start": { "kind": "nodeEdge", "node": { "kind": "block", "nodeType": "paragraph", "nodeId": "ABC123" }, "edge": "before" },
  "end": { "kind": "nodeEdge", "node": { "kind": "block", "nodeType": "paragraph", "nodeId": "ABC123" }, "edge": "after" }
}
```

**BlockNodeAddress (for structural replacements):**

```json
{
  "kind": "block",
  "nodeType": "paragraph",
  "nodeId": "ABC123"
}
```

Valid `nodeType` values: `paragraph`, `heading`, `listItem`, `table`, `tableRow`, `tableCell`, `tableOfContents`, `image`, `sdt`.

Valid `edge` values: `before`, `after`.

---

### Multiple Steps in One Batch

Steps execute in order within a single atomic transaction:

```json
[
  {"id":"s1","op":"text.rewrite","where":{"by":"select","select":{"type":"text","pattern":"ACME"},"require":"all"},"args":{"replacement":{"text":"NewCo"}}},
  {"id":"s2","op":"text.rewrite","where":{"by":"select","select":{"type":"text","pattern":"2024"},"require":"all"},"args":{"replacement":{"text":"2025"}}},
  {"id":"s3","op":"format.apply","where":{"by":"select","select":{"type":"text","pattern":"CONFIDENTIAL"},"require":"all"},"args":{"inline":{"bold":true,"color":"#FF0000"}}}
]
```
