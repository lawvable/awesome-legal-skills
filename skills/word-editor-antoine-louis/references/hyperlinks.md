# Hyperlinks

### hyperlinks list

List all hyperlinks in the document.

```bash
superdoc hyperlinks list 2>/dev/null
```

### hyperlinks get

Retrieve hyperlink details by inline address.

```bash
superdoc hyperlinks get --target-json '<target>' 2>/dev/null
```

### hyperlinks wrap

Wrap an existing text range with a hyperlink.

```bash
superdoc hyperlinks wrap \
  --target-json '{"kind":"text","blockId":"ABC","range":{"start":0,"end":10}}' \
  --link-json '{"destination":{"href":"https://example.com"},"tooltip":"Click here"}' \
  2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-json` | JSON | yes | `{"kind":"text","blockId":"...","range":{"start":N,"end":N}}` |
| `--link-json` | JSON | yes | `{"destination":{"href":"..."},"tooltip":"...","target":"...","rel":"..."}` |
| `--dry-run` | boolean | no | Preview |

The `destination` object supports: `href` (external URL), `anchor` (internal bookmark), `docLocation` (document location).

### hyperlinks insert

Insert new linked text at a target position.

```bash
superdoc hyperlinks insert \
  --target-json '{"kind":"text","blockId":"ABC","range":{"start":5,"end":5}}' \
  --text "Click here" \
  --link-json '{"destination":{"href":"https://example.com"}}' \
  2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--target-json` | JSON | no | Insertion position |
| `--text` | string | yes | Display text for the link |
| `--link-json` | JSON | yes | `{"destination":{"href":"..."}}` |
| `--dry-run` | boolean | no | Preview |

### hyperlinks patch

Update hyperlink metadata without changing display text.

```bash
superdoc hyperlinks patch --target-json '<target>' --link-json '{"destination":{"href":"https://new-url.com"}}' 2>/dev/null
```

### hyperlinks remove

Remove a hyperlink. Mode controls text preservation.

```bash
superdoc hyperlinks remove --target-json '<target>' --mode unwrap 2>/dev/null    # preserve text
superdoc hyperlinks remove --target-json '<target>' --mode deleteText 2>/dev/null # remove text too
```
