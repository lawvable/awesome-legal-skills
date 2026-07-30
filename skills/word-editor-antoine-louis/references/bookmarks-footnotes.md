# Bookmarks, Footnotes, Cross-references

### Bookmarks

| Command | Description | Key flags |
|---------|-------------|-----------|
| `bookmarks list` | List all bookmarks | (none) |
| `bookmarks get` | Get bookmark details | `--name` or `--id` |
| `bookmarks insert` | Insert a named bookmark | `--name`, `--at-json` (see below), `--dry-run` |
| `bookmarks rename` | Rename a bookmark | `--id`, `--name`, `--dry-run` |
| `bookmarks remove` | Remove a bookmark | `--id` or `--name`, `--dry-run` |

**bookmarks insert `--at-json` format:**

```json
{
  "kind": "text",
  "segments": [
    { "blockId": "ABC123", "range": { "start": 0, "end": 10 } }
  ]
}
```

### Footnotes and Endnotes

| Command | Description | Key flags |
|---------|-------------|-----------|
| `footnotes list` | List all footnotes and endnotes | (none) |
| `footnotes get` | Get footnote/endnote details | `--id` |
| `footnotes insert` | Insert footnote or endnote | `--type` (footnote/endnote), `--content`, `--at-json`, `--dry-run` |
| `footnotes update` | Update footnote content | `--id`, `--content`, `--dry-run` |
| `footnotes remove` | Remove footnote/endnote | `--id`, `--dry-run` |
| `footnotes configure` | Configure numbering/placement | `--type`, `--dry-run` |

**footnotes insert `--at-json` format** (same as bookmarks):

```json
{
  "kind": "text",
  "segments": [
    { "blockId": "ABC123", "range": { "start": 5, "end": 5 } }
  ]
}
```

**footnotes insert** full flags:

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--at-json` | JSON | yes | Anchor location (see format above) |
| `--type` | string | yes | `footnote` or `endnote` |
| `--content` | string | yes | Note content text |
| `--dry-run` | boolean | no | Preview |

### Cross-references

| Command | Description | Key flags |
|---------|-------------|-----------|
| `cross-refs list` | List all cross-reference fields | (none) |
| `cross-refs get` | Get cross-reference details | `--id` |
| `cross-refs insert` | Insert a cross-reference | `--at-json`, `--dry-run` |
| `cross-refs rebuild` | Rebuild a cross-reference | `--id`, `--dry-run` |
| `cross-refs remove` | Remove a cross-reference | `--id`, `--dry-run` |
