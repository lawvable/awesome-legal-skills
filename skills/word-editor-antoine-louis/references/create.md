# Create Commands

### create paragraph

Create a standalone paragraph at the target position.

```bash
superdoc create paragraph --text "New paragraph" --at-json '{"kind":"documentEnd"}' --tracked 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--text` | string | no | Paragraph text content |
| `--input-json` | JSON | no | Structured input (alternative to --text) |
| `--at-json` | JSON | no | Position (see below) |
| `--in-json` | JSON | no | Story scope |
| `--tracked` | boolean | no | Apply as tracked change |
| `--dry-run` | boolean | no | Preview |

**Position (`--at-json`) options:**

```json
{"kind": "documentEnd"}                                                           // append at end
{"kind": "documentStart"}                                                         // prepend at start
{"kind": "before", "target": {"kind": "block", "nodeType": "paragraph", "nodeId": "ABC"}}  // before a block
{"kind": "after", "target": {"kind": "block", "nodeType": "paragraph", "nodeId": "ABC"}}   // after a block
```

Note: To add a list item, use `lists insert` instead.

### create heading

Create a new heading at the target position.

```bash
superdoc create heading --text "Section Title" --level 2 --at-json '{"kind":"documentEnd"}' --tracked 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--text` | string | no | Heading text content |
| `--level` | number | no | Heading level (1-9) |
| `--at-json` | JSON | no | Position (same format as create paragraph) |
| `--in-json` | JSON | no | Story scope |
| `--tracked` | boolean | no | Apply as tracked change |
| `--dry-run` | boolean | no | Preview |

### create table

Create a new table at the target position.

```bash
superdoc create table --rows 3 --columns 4 --at-json '{"kind":"documentEnd"}' --tracked 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--rows` | number | yes | Number of rows |
| `--columns` | number | yes | Number of columns |
| `--at-json` | JSON | no | Position |
| `--tracked` | boolean | no | Apply as tracked change |
| `--dry-run` | boolean | no | Preview |

### Other Create Commands

| Command | Description | Key flags |
|---------|-------------|-----------|
| `create image` | Insert a new image | `--at-json`, `--src`, `--dry-run` |
| `create section-break` | Create a section break | `--at-json`, `--break-type`, `--dry-run` |
| `create content-control` | Create a new SDT | `--at-json`, `--type`, `--tag`, `--dry-run` |
| `create table-of-contents` | Insert a TOC | `--at-json`, `--dry-run` |
