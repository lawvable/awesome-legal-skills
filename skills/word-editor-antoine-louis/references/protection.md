# Protection

| Command | Description | Key flags |
|---------|-------------|-----------|
| `protection get` | Read current document protection state | (none) |
| `protection set-editing-restriction` | Enable Word-style editing restriction (readOnly mode) | `--dry-run` |
| `protection clear-editing-restriction` | Disable editing restriction | `--dry-run` |

### Permission Ranges

| Command | Description | Key flags |
|---------|-------------|-----------|
| `permission-ranges list` | List all permission ranges | (none) |
| `permission-ranges get` | Get permission range by ID | `--id` |
| `permission-ranges create` | Create a permission range exception | `--dry-run` |
| `permission-ranges remove` | Remove a permission range | `--id`, `--dry-run` |
| `permission-ranges update-principal` | Change who can edit a range | `--id`, `--dry-run` |
