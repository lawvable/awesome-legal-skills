# Core Reading Commands

### get-text

Extract the plain-text content of the document.

```bash
superdoc get-text <doc> 2>/dev/null
superdoc get-text 2>/dev/null                # with active session
```

| Flag | Type | Description |
|------|------|-------------|
| `<doc>` | string | Path to .docx (stateless mode) |
| `--session` | string | Session ID |
| `--in-json` | JSON | Story scope (body, header/footer, footnote, endnote) |

### get-markdown

Extract the document content as a Markdown string.

```bash
superdoc get-markdown <doc> 2>/dev/null
superdoc get-markdown 2>/dev/null            # with active session
```

| Flag | Type | Description |
|------|------|-------------|
| `<doc>` | string | Path to .docx (stateless mode) |
| `--session` | string | Session ID |
| `--in-json` | JSON | Story scope |

### get-html

Extract the document content as an HTML string.

```bash
superdoc get-html <doc> 2>/dev/null
```

| Flag | Type | Description |
|------|------|-------------|
| `<doc>` | string | Path to .docx (stateless mode) |
| `--session` | string | Session ID |
| `--in-json` | JSON | Story scope |

### info

Return document summary info including word, character, paragraph, heading, table, image, comment, tracked-change, SDT-field, list, and page counts, plus outline and capabilities.

```bash
superdoc info <doc> 2>/dev/null
superdoc info 2>/dev/null                    # with active session
```

| Flag | Type | Description |
|------|------|-------------|
| `<doc>` | string | Path to .docx (stateless mode) |
| `--session` | string | Session ID |

### find

Search the document for text or node matches using SDM/1 selectors. Returns discovery-grade results. **For mutation targeting, use `query match` instead.**

```bash
superdoc find --select-json '<selector>' [flags] 2>/dev/null
```

| Flag | Type | Description |
|------|------|-------------|
| `--select-json` | JSON | Selector: `{"type":"text","pattern":"..."}` or `{"type":"node","nodeType":"paragraph"}` |
| `--within-json` | JSON | Scope to a block: `{"kind":"block","nodeType":"paragraph","nodeId":"..."}` |
| `--limit` | number | Max results |
| `--offset` | number | Skip first N results |
| `--in-json` | JSON | Story scope |
| `--options-json` | JSON | `{"includeResolved":bool, "includeProvenance":bool, "includeContext":bool}` |
| `--pattern` | string | Flat flag alternative for text pattern |
| `--type` | string | Flat flag: `text` or `node` |
| `--node-type` | string | Flat flag for node type |
| `--mode` | string | `contains` (default) or `regex` |
| `--case-sensitive` | boolean | Case-sensitive matching |

### query match

Deterministic selector-based search returning mutation-grade addresses and text ranges. **Always use this instead of `find` when preparing mutations.**

```bash
superdoc query match --select-json '<selector>' --require <cardinality> [flags] 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--select-json` | JSON | yes | `{"type":"text","pattern":"..."}` or `{"type":"node","nodeType":"paragraph"}` |
| `--require` | string | no | `any`, `first`, `exactlyOne`, `all` |
| `--within-json` | JSON | no | Scope: `{"kind":"block","nodeType":"paragraph","nodeId":"..."}` |
| `--mode` | string | no | `strict` (default) or `candidates` (scored fuzzy matches) |
| `--limit` | number | no | Max results |
| `--offset` | number | no | Skip first N |
| `--include-nodes` | boolean | no | Include full node data in results |
| `--in-json` | JSON | no | Story scope |

**Select types:**

| Type | Description | Example |
|------|-------------|---------|
| Text (substring) | Case-insensitive substring match | `{"type":"text","pattern":"Introduction"}` |
| Text (regex) | Regular expression match | `{"type":"text","pattern":"Section \\d+","mode":"regex"}` |
| Text (case-sensitive) | Exact case matching | `{"type":"text","pattern":"ACME","caseSensitive":true}` |
| Node (block) | Match by block node type | `{"type":"node","nodeType":"paragraph"}` |
| Node (inline) | Match by inline node type | `{"type":"node","nodeType":"hyperlink","kind":"inline"}` |

**Require cardinalities:**

| Value | Behavior |
|-------|----------|
| `any` | Return all matches (no failure) |
| `first` | Return only the first match |
| `exactlyOne` | Fail if count != 1 |
| `all` | Return all matches, fail if 0 |

**Response shape** -- each match includes `.target` (SelectionTarget) and `.handle.ref` (ref string), both usable directly in `replace`, `delete`, `format apply`, or `mutations apply` steps.

### get-node

Retrieve a single node by target position.

```bash
superdoc get-node --target-json '<target>' 2>/dev/null
```

### get-node-by-id

Retrieve a single node by its unique ID.

```bash
superdoc get-node-by-id --id <nodeId> 2>/dev/null
```

### blocks list

List top-level blocks in document order with IDs, types, and text previews. Supports pagination.

```bash
superdoc blocks list [flags] 2>/dev/null
```

| Flag | Type | Description |
|------|------|-------------|
| `--offset` | number | Skip first N blocks |
| `--limit` | number | Max blocks to return |
| `--node-types-json` | JSON array | Filter: `["paragraph","heading"]` |
| `--session` | string | Session ID |

Valid node types for filtering: `paragraph`, `heading`, `listItem`, `table`, `tableRow`, `tableCell`, `tableOfContents`, `image`, `sdt`.
