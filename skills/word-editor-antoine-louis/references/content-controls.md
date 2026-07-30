# Content Controls

Content controls (SDTs -- Structured Document Tags) are the Word equivalent of form fields. They have types (plainText, richText, comboBox, dropDownList, date, checkbox, repeatingSection, group, etc.).

### content-controls list

List all content controls with optional filtering.

```bash
superdoc content-controls list [flags] 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--control-type` | string | no | Filter by SDT type |
| `--tag` | string | no | Filter by tag value |
| `--limit` | number | no | Max results |
| `--offset` | number | no | Skip first N |

### content-controls get

Retrieve a single content control by target.

```bash
superdoc content-controls get --target-json '{"kind":"block","nodeType":"sdt","nodeId":"ABC"}' 2>/dev/null
```

### content-controls get-content

Get the text content of a content control.

```bash
superdoc content-controls get-content --target-json '{"kind":"block","nodeType":"sdt","nodeId":"ABC"}' 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-json` | JSON | yes | `{"kind":"block"|"inline","nodeType":"sdt","nodeId":"..."}` |

### content-controls replace-content

Replace the entire content of a content control.

```bash
superdoc content-controls replace-content --target-json '{"kind":"block","nodeType":"sdt","nodeId":"ABC"}' --content "New text" 2>/dev/null
superdoc content-controls replace-content --target-json '{"kind":"block","nodeType":"sdt","nodeId":"ABC"}' --content "<p>HTML</p>" --format html 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-json` | JSON | yes | `{"kind":"block"|"inline","nodeType":"sdt","nodeId":"..."}` |
| `--content` | string | yes | Replacement content |
| `--format` | string | no | `text` (default) or `html` |
| `--dry-run` | boolean | no | Preview |

### All Content Control Commands

| Command | Description | Key flags |
|---------|-------------|-----------|
| `content-controls list` | List all SDTs | `--control-type`, `--tag`, `--limit` |
| `content-controls get` | Get SDT details | `--target-json` |
| `content-controls get-content` | Get SDT text | `--target-json` |
| `content-controls replace-content` | Replace SDT content | `--target-json`, `--content`, `--format` |
| `content-controls clear-content` | Clear SDT content | `--target-json`, `--dry-run` |
| `content-controls append-content` | Append to SDT | `--target-json`, `--dry-run` |
| `content-controls prepend-content` | Prepend to SDT | `--target-json`, `--dry-run` |
| `content-controls insert-before` | Insert before SDT | `--target-json`, `--dry-run` |
| `content-controls insert-after` | Insert after SDT | `--target-json`, `--dry-run` |
| `content-controls select-by-tag` | Select SDTs by tag | `--tag` |
| `content-controls select-by-title` | Select SDTs by title | `--title` |
| `content-controls list-in-range` | SDTs within a block range | `--start-json`, `--end-json` |
| `content-controls list-children` | List nested SDTs | `--target-json` |
| `content-controls get-parent` | Get parent SDT | `--target-json` |
| `content-controls wrap` | Wrap content in new SDT | `--target-json`, `--dry-run` |
| `content-controls unwrap` | Remove SDT wrapper | `--target-json`, `--dry-run` |
| `content-controls delete` | Delete SDT and content | `--target-json`, `--dry-run` |
| `content-controls copy` | Copy SDT to destination | `--target-json`, `--dry-run` |
| `content-controls move` | Move SDT to new position | `--target-json`, `--dry-run` |
| `content-controls patch` | Patch metadata (tag, alias, etc.) | `--target-json`, `--dry-run` |
| `content-controls set-lock-mode` | Set lock mode | `--target-json`, `--dry-run` |
| `content-controls set-type` | Change SDT type | `--target-json`, `--dry-run` |
| `content-controls get-binding` | Get data binding | `--target-json` |
| `content-controls set-binding` | Set data binding | `--target-json`, `--dry-run` |
| `content-controls clear-binding` | Remove data binding | `--target-json`, `--dry-run` |
| `content-controls get-raw-properties` | Get raw sdtPr | `--target-json` |
| `content-controls patch-raw-properties` | Patch raw sdtPr | `--target-json`, `--dry-run` |
| `content-controls validate-word-compatibility` | Validate for Word compat | `--target-json` |
| `content-controls normalize-word-compatibility` | Fix Word compat issues | `--target-json`, `--dry-run` |
| `content-controls normalize-tag-payload` | Normalize tag format | `--target-json`, `--dry-run` |

**Type-specific commands:**

| Command | Description |
|---------|-------------|
| `content-controls text set-value` | Set plain-text SDT value |
| `content-controls text clear-value` | Clear plain-text SDT value |
| `content-controls text set-multiline` | Set multiline attribute |
| `content-controls date set-value` | Set date SDT value |
| `content-controls date clear-value` | Clear date SDT value |
| `content-controls date set-display-format` | Set date display format |
| `content-controls date set-display-locale` | Set date locale |
| `content-controls date set-storage-format` | Set date XML storage format |
| `content-controls date set-calendar` | Set calendar type |
| `content-controls checkbox get-state` | Get checkbox state |
| `content-controls checkbox set-state` | Set checkbox state |
| `content-controls checkbox toggle` | Toggle checkbox |
| `content-controls checkbox set-symbol-pair` | Set check/uncheck glyphs |
| `content-controls choice-list get-items` | Get comboBox/dropdown items |
| `content-controls choice-list set-items` | Replace items |
| `content-controls choice-list set-selected` | Set selected value |
| `content-controls repeating-section list-items` | List section items |
| `content-controls repeating-section insert-item-before` | Insert item before |
| `content-controls repeating-section insert-item-after` | Insert item after |
| `content-controls repeating-section clone-item` | Clone an item |
| `content-controls repeating-section delete-item` | Delete an item |
| `content-controls repeating-section set-allow-insert-delete` | Set insert/delete flag |
| `content-controls group wrap` | Wrap in group SDT |
| `content-controls group ungroup` | Remove group designation |
