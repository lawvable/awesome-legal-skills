# Track Changes

> **Namespace is `track-changes` (with hyphen).** Not `tracked-changes`, not `changes`.

### track-changes list

List all tracked changes in the document.

```bash
superdoc track-changes list [flags] 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | string | no | Filter: `insert`, `delete`, or `format` |
| `--limit` | number | no | Max results |
| `--offset` | number | no | Skip first N |

### track-changes get

Retrieve a single tracked change by ID.

```bash
superdoc track-changes get --id <changeId> 2>/dev/null
```

### track-changes accept

Accept a tracked change by ID.

```bash
superdoc track-changes accept --id <changeId> 2>/dev/null
```

Shorthand for `track-changes decide --decision accept --target-json '{"id":"<changeId>"}'`.

### track-changes reject

Reject a tracked change by ID.

```bash
superdoc track-changes reject --id <changeId> 2>/dev/null
```

Shorthand for `track-changes decide --decision reject --target-json '{"id":"<changeId>"}'`.

### track-changes accept-all

Accept all tracked changes in the document.

```bash
superdoc track-changes accept-all 2>/dev/null
```

### track-changes reject-all

Reject all tracked changes in the document.

```bash
superdoc track-changes reject-all 2>/dev/null
```

### track-changes decide

Accept or reject a tracked change by ID or by scope.

```bash
superdoc track-changes decide --decision accept --target-json '{"id":"<changeId>"}' 2>/dev/null
superdoc track-changes decide --decision reject --target-json '{"scope":"all"}' 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--decision` | string | yes | `accept` or `reject` |
| `--target-json` | JSON | yes | `{"id":"<changeId>"}` or `{"scope":"all"}` |
