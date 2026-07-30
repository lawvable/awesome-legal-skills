# Lists

### Key List Commands

#### lists insert

Insert a new list item before or after an existing list item. Inherits the target list context.

```bash
superdoc lists insert --target-json '{"kind":"block","nodeType":"listItem","nodeId":"ABC"}' --position after --text "New item" --tracked 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-json` | JSON | no | `{"kind":"block","nodeType":"listItem","nodeId":"..."}` |
| `--node-id` | string | no | Flat flag alternative for target |
| `--position` | string | yes | `before` or `after` |
| `--text` | string | no | Item text |
| `--input-json` | JSON | no | Structured input |
| `--tracked` | boolean | no | Apply as tracked change |
| `--dry-run` | boolean | no | Preview |

### All List Commands

| Command | Description | Key flags |
|---------|-------------|-----------|
| `lists list` | List all list nodes | `--limit`, `--offset` |
| `lists get` | Get a specific list node | `--target-json` |
| `lists insert` | Insert a new list item | `--target-json`, `--position`, `--text`, `--tracked` |
| `lists create` | Create a new list from paragraphs | `--target-json`, `--preset`, `--dry-run` |
| `lists attach` | Convert paragraphs to list items | `--target-json`, `--dry-run` |
| `lists detach` | Convert list items to plain paragraphs | `--target-json`, `--dry-run` |
| `lists exit` | Alias for `lists detach` | `--target-json`, `--dry-run` |
| `lists indent` | Increase indentation level | `--target-json`, `--dry-run` |
| `lists outdent` | Decrease indentation level | `--target-json`, `--dry-run` |
| `lists set-level` | Set absolute nesting level (0-8) | `--target-json`, `--level`, `--dry-run` |
| `lists set-value` | Set explicit numbering value | `--target-json`, `--value`, `--dry-run` |
| `lists join` | Merge two adjacent list sequences | `--target-json`, `--dry-run` |
| `lists can-join` | Check if two lists can join | `--target-json` |
| `lists separate` | Split a list at a target item | `--target-json`, `--dry-run` |
| `lists continue-previous` | Continue numbering from previous list | `--target-json`, `--dry-run` |
| `lists can-continue-previous` | Check if continuation is possible | `--target-json` |
| `lists set-type` | Convert to ordered or bullet | `--target-json`, `--list-type`, `--dry-run` |
| `lists convert-to-text` | Convert items to plain paragraphs | `--target-json`, `--dry-run` |
| `lists restart-at` | Restart numbering at a specific value | `--target-json`, `--value`, `--dry-run` |
| `lists apply-preset` | Apply a built-in list preset | `--target-json`, `--preset`, `--dry-run` |
| `lists apply-template` | Apply a captured template | `--target-json`, `--template-json`, `--dry-run` |
| `lists apply-style` | Apply a reusable list style | `--target-json`, `--style-json`, `--dry-run` |
| `lists capture-template` | Capture formatting from a list | `--target-json` |
| `lists get-style` | Read the effective reusable style | `--target-json` |
| `lists set-level-restart` | Set restart behavior for a level | `--target-json`, `--level`, `--dry-run` |
| `lists set-level-numbering` | Set format/pattern/start for a level | `--target-json`, `--level`, `--dry-run` |
| `lists set-level-bullet` | Set bullet marker text | `--target-json`, `--level`, `--text`, `--dry-run` |
| `lists set-level-number-style` | Set numbering style (decimal, etc.) | `--target-json`, `--level`, `--style`, `--dry-run` |
| `lists set-level-text` | Set level text pattern | `--target-json`, `--level`, `--text`, `--dry-run` |
| `lists set-level-start` | Set start value for a level | `--target-json`, `--level`, `--start`, `--dry-run` |
| `lists set-level-alignment` | Set marker alignment | `--target-json`, `--level`, `--alignment`, `--dry-run` |
| `lists set-level-indents` | Set indent values for a level | `--target-json`, `--level`, `--dry-run` |
| `lists set-level-trailing-character` | Set trailing character (tab/space) | `--target-json`, `--level`, `--dry-run` |
| `lists set-level-marker-font` | Set marker font family | `--target-json`, `--level`, `--dry-run` |
| `lists set-level-layout` | Set full layout for a level | `--target-json`, `--level`, `--dry-run` |
| `lists set-level-picture-bullet` | Set picture bullet | `--target-json`, `--level`, `--dry-run` |
| `lists clear-level-overrides` | Remove instance-level overrides | `--target-json`, `--level`, `--dry-run` |
