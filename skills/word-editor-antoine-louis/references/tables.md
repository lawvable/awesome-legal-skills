# Tables

### Key Table Commands with Flags

#### tables get

Retrieve table structure and dimensions by locator.

```bash
superdoc tables get --target-json '{"kind":"block","nodeType":"table","nodeId":"ABC"}' 2>/dev/null
superdoc tables get --node-id "ABC" 2>/dev/null
```

#### tables get-cells

Retrieve cell information, optionally filtered by row or column.

```bash
superdoc tables get-cells --target-json '{"kind":"block","nodeType":"table","nodeId":"ABC"}' 2>/dev/null
```

#### tables insert-row

Insert a new row into the target table.

```bash
superdoc tables insert-row --target-json '{"kind":"block","nodeType":"table","nodeId":"ABC"}' --row-index 2 --position below --tracked 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-json` | JSON | no | Table or row target |
| `--node-id` | string | no | Flat flag alternative |
| `--row-index` | number | no | Row index for positioning |
| `--position` | string | yes | `above` or `below` |
| `--count` | number | no | Number of rows to insert (default: 1) |
| `--tracked` | boolean | no | Apply as tracked change |
| `--dry-run` | boolean | no | Preview |

#### tables delete-row

Delete a row from the target table.

```bash
superdoc tables delete-row --target-json '{"kind":"block","nodeType":"table","nodeId":"ABC"}' --row-index 2 --tracked 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-json` | JSON | no | Table or row target |
| `--node-id` | string | no | Flat flag alternative |
| `--row-index` | number | no | Row index to delete |
| `--tracked` | boolean | no | Apply as tracked change |
| `--dry-run` | boolean | no | Preview |

#### tables insert-column

Insert a new column into the target table.

```bash
superdoc tables insert-column --target-json '{"kind":"block","nodeType":"table","nodeId":"ABC"}' --column-index 1 --position right --tracked 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-json` | JSON | no | Table target |
| `--node-id` | string | no | Flat flag alternative |
| `--column-index` | number | yes | Column index for positioning |
| `--position` | string | yes | `left` or `right` |
| `--count` | number | no | Number of columns to insert (default: 1) |
| `--tracked` | boolean | no | Apply as tracked change |
| `--dry-run` | boolean | no | Preview |

#### tables delete-column

Delete a column from the target table.

```bash
superdoc tables delete-column --target-json '{"kind":"block","nodeType":"table","nodeId":"ABC"}' --column-index 2 --tracked 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-json` | JSON | no | Table target |
| `--node-id` | string | no | Flat flag alternative |
| `--column-index` | number | yes | Column index to delete |
| `--tracked` | boolean | no | Apply as tracked change |
| `--dry-run` | boolean | no | Preview |

#### tables merge-cells

Merge a range of table cells into one.

```bash
superdoc tables merge-cells --target-json '{"kind":"block","nodeType":"table","nodeId":"ABC"}' --start-json '{"rowIndex":0,"columnIndex":0}' --end-json '{"rowIndex":1,"columnIndex":2}' 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-json` | JSON | no | Table target |
| `--node-id` | string | no | Flat flag alternative |
| `--start-json` | JSON | yes | `{"rowIndex":<n>,"columnIndex":<n>}` |
| `--end-json` | JSON | yes | `{"rowIndex":<n>,"columnIndex":<n>}` |
| `--dry-run` | boolean | no | Preview |

### All Table Commands

| Command | Description | Key flags |
|---------|-------------|-----------|
| `tables get` | Get table structure | `--target-json`, `--node-id` |
| `tables get-cells` | Get cell info | `--target-json`, `--node-id` |
| `tables get-properties` | Get layout/style props | `--target-json`, `--node-id` |
| `tables get-styles` | List all table styles | (none) |
| `tables insert-row` | Insert row | `--target-json`, `--row-index`, `--position`, `--tracked` |
| `tables delete-row` | Delete row | `--target-json`, `--row-index`, `--tracked` |
| `tables insert-column` | Insert column | `--target-json`, `--column-index`, `--position`, `--tracked` |
| `tables delete-column` | Delete column | `--target-json`, `--column-index`, `--tracked` |
| `tables insert-cell` | Insert cell | `--target-json`, `--dry-run` |
| `tables delete-cell` | Delete cell | `--target-json`, `--dry-run` |
| `tables merge-cells` | Merge cells | `--target-json`, `--start-json`, `--end-json`, `--dry-run` |
| `tables unmerge-cells` | Unmerge cells | `--target-json`, `--dry-run` |
| `tables split-cell` | Split a cell | `--target-json`, `--dry-run` |
| `tables delete` | Delete entire table | `--target-json`, `--tracked` |
| `tables clear-contents` | Clear table contents | `--target-json`, `--dry-run` |
| `tables move` | Move table to new position | `--target-json`, `--at-json`, `--dry-run` |
| `tables split` | Split table at a row | `--target-json`, `--dry-run` |
| `tables sort` | Sort rows by column | `--target-json`, `--dry-run` |
| `tables convert-from-text` | Text to table | `--target-json`, `--dry-run` |
| `tables convert-to-text` | Table to text | `--target-json`, `--dry-run` |
| `tables set-layout` | Set layout mode | `--target-json`, `--layout`, `--dry-run` |
| `tables set-row-height` | Set row height | `--target-json`, `--dry-run` |
| `tables distribute-rows` | Even row heights | `--target-json`, `--dry-run` |
| `tables set-row-options` | Header repeat, page break | `--target-json`, `--dry-run` |
| `tables set-column-width` | Set column width | `--target-json`, `--dry-run` |
| `tables distribute-columns` | Even column widths | `--target-json`, `--dry-run` |
| `tables set-cell-properties` | Vertical align, text dir | `--target-json`, `--dry-run` |
| `tables set-alt-text` | Table alt text | `--target-json`, `--text`, `--dry-run` |
| `tables set-style` | Apply named table style | `--target-json`, `--style`, `--dry-run` |
| `tables clear-style` | Remove table style | `--target-json`, `--dry-run` |
| `tables set-style-option` | Toggle banded rows, etc. | `--target-json`, `--dry-run` |
| `tables set-border` | Set border | `--target-json`, `--dry-run` |
| `tables clear-border` | Remove border | `--target-json`, `--dry-run` |
| `tables apply-border-preset` | Apply border preset | `--target-json`, `--dry-run` |
| `tables set-shading` | Set background color | `--target-json`, `--dry-run` |
| `tables clear-shading` | Remove shading | `--target-json`, `--dry-run` |
| `tables set-table-padding` | Set default cell padding | `--target-json`, `--dry-run` |
| `tables set-cell-padding` | Set cell padding | `--target-json`, `--dry-run` |
| `tables set-cell-spacing` | Set cell spacing | `--target-json`, `--dry-run` |
| `tables clear-cell-spacing` | Remove cell spacing | `--target-json`, `--dry-run` |
| `tables apply-style` | Apply style + options | `--target-json`, `--dry-run` |
| `tables set-borders` | Set borders per-edge | `--target-json`, `--dry-run` |
| `tables set-table-options` | Set default margins/spacing | `--target-json`, `--dry-run` |
| `tables set-default-style` | Set document default table style | `--dry-run` |
| `tables clear-default-style` | Remove default table style | `--dry-run` |
