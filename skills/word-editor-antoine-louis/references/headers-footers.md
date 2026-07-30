# Headers and Footers

| Command | Description | Key flags |
|---------|-------------|-----------|
| `header-footers list` | List header/footer slot entries across sections | (none) |
| `header-footers get` | Get a single slot entry by address | `--address-json` |
| `header-footers resolve` | Resolve effective header/footer (walks inheritance) | `--address-json` |
| `header-footers refs set` | Set header/footer reference on a section slot | `--target-json`, `--dry-run` |
| `header-footers refs clear` | Clear header/footer reference | `--target-json`, `--dry-run` |
| `header-footers refs set-linked-to-previous` | Link/unlink to previous section | `--target-json`, `--dry-run` |
| `header-footers parts list` | List unique header/footer parts | (none) |
| `header-footers parts create` | Create new header/footer part | `--dry-run` |
| `header-footers parts delete` | Delete header/footer part | `--dry-run` |

**Story scope for reading/writing in headers/footers:**

```json
{
  "kind": "story",
  "storyType": "headerFooterSlot",
  "section": { "kind": "section", "sectionId": "<id>" },
  "headerFooterKind": "header",
  "variant": "default"
}
```

Variants: `default`, `first`, `even`. Kinds: `header`, `footer`.

Use `--in-json` with this story scope on commands like `get-text`, `get-markdown`, `insert`, `replace`, `blocks list`, etc. to operate within header/footer content.
