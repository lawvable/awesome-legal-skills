# Diff

### diff capture

Capture the current document's diffable state as a versioned snapshot. Covers body, comments, styles, and numbering. Header/footer content is not included.

```bash
superdoc diff capture 2>/dev/null
```

Returns a snapshot object to store and pass to `diff compare` later.

### diff compare

Compare the current document (base) against a previously captured target snapshot. Returns a versioned diff payload.

```bash
superdoc diff compare --target-snapshot-json '<snapshot>' 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-snapshot-json` | JSON | yes | Snapshot from a previous `diff capture` |

The snapshot must include: `version`, `engine`, `fingerprint`, `coverage`, `payload`.

Returns a diff payload with `baseFingerprint`, `targetFingerprint`, `summary`, and `payload`.

### diff apply

Apply a previously computed diff payload to the current document. The document fingerprint must match the diff base fingerprint.

```bash
superdoc diff apply --diff-json '<diff_payload>' --change-mode tracked 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--diff-json` | JSON | yes | Diff payload from `diff compare` |
| `--change-mode` | string | no | `direct` or `tracked` (tracked applies body changes as tracked) |

Note: Tracked mode governs body content only; styles, numbering, and comments are always applied directly.

### Typical Diff Workflow

```bash
# 1. Capture snapshot of original document
SNAPSHOT=$(superdoc diff capture 2>/dev/null)

# 2. Make changes to the document...
superdoc replace --block-id ABC --start 0 --end 5 --text "Updated" 2>/dev/null

# 3. Capture snapshot of modified document
TARGET_SNAPSHOT=$(superdoc diff capture 2>/dev/null)

# 4. Compare (on a different session with the original doc)
DIFF=$(superdoc diff compare --target-snapshot-json "$TARGET_SNAPSHOT" 2>/dev/null)

# 5. Apply diff (optionally as tracked changes)
superdoc diff apply --diff-json "$DIFF" --change-mode tracked 2>/dev/null
```
