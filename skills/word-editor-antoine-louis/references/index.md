# SuperDoc CLI -- Command Reference Index

> 410 commands. Read the relevant file below for exact flags and examples.
> For commands not covered here: `superdoc describe command "<name>" 2>/dev/null`
>
> **Telemetry:** `[super-editor] Telemetry: enabled` may appear on stderr. Use `2>/dev/null`.

## Global Conventions

- **`--tracked`** is shorthand for `--change-mode tracked`. All mutating commands with `trackedMode` capability support it.
- **`--dry-run`** previews a mutation without applying. All mutating commands with `dryRun` capability support it.
- **`--target-json`** has NO `--target-file` counterpart. Use flat flags (`--block-id`, `--start`, `--end`) as the alternative.
- **`--session`** specifies a session ID. If omitted, uses the default session.
- **`--in-json`** specifies a story scope (body, header/footer, footnote, endnote). Defaults to document body when omitted.
- **`--out`** writes to a different file instead of in-place (stateless mode).
- **`--expected-revision`** enables optimistic concurrency check.

## Reference Files

| File | Covers | Key commands |
|------|--------|--------------|
| [mutations-apply.md](mutations-apply.md) | Batch mutations, find-and-replace, SelectionTarget format | `mutations apply`, `text.rewrite`, `text.insert`, `text.delete`, `format.apply`, `assert` |
| [session.md](session.md) | Session lifecycle, history | `open`, `save`, `close`, `status`, `session list`, `history undo/redo` |
| [reading.md](reading.md) | Core reading: extract text, search, query | `get-text`, `get-markdown`, `get-html`, `info`, `find`, `query match`, `get-node`, `blocks list` |
| [mutations.md](mutations.md) | Core mutations: replace, insert, delete | `replace`, `insert`, `delete`, `clear-content`, `blocks delete`, `blocks delete-range` |
| [format.md](format.md) | Inline formatting, paragraph formatting, styles | `format apply`, `format bold/italic/underline/...`, `format paragraph set-alignment/set-spacing/...`, `styles apply` |
| [create.md](create.md) | Create new blocks | `create paragraph`, `create heading`, `create table`, `create image`, `create section-break`, `create content-control` |
| [lists.md](lists.md) | List operations | `lists insert`, `lists create`, `lists attach/detach`, `lists indent/outdent`, `lists set-level`, `lists set-type` |
| [tables.md](tables.md) | Table structure and formatting | `tables get`, `tables get-cells`, `tables insert-row/delete-row`, `tables insert-column/delete-column`, `tables merge-cells` |
| [comments.md](comments.md) | Comment threads | `comments list`, `comments add`, `comments reply`, `comments resolve`, `comments delete`, `comments edit` |
| [track-changes.md](track-changes.md) | Tracked change review | `track-changes list`, `track-changes accept/reject`, `track-changes accept-all/reject-all`, `track-changes decide` |
| [images.md](images.md) | Images and captions | `create image`, `images list/get/delete`, `images set-size`, `images replace-source`, `captions list/insert/remove` |
| [hyperlinks.md](hyperlinks.md) | Hyperlink operations | `hyperlinks list`, `hyperlinks wrap`, `hyperlinks insert`, `hyperlinks patch`, `hyperlinks remove` |
| [content-controls.md](content-controls.md) | Structured Document Tags (SDTs) / form fields | `content-controls list/get/get-content/replace-content`, `content-controls checkbox/date/text/choice-list` |
| [sections.md](sections.md) | Section layout and page setup | `sections list/get`, `sections set-page-margins`, `sections set-page-setup`, `sections set-columns` |
| [headers-footers.md](headers-footers.md) | Header/footer slots and story scopes | `header-footers list/get/resolve`, `header-footers refs set/clear`, `--in-json` story scope |
| [bookmarks-footnotes.md](bookmarks-footnotes.md) | Bookmarks, footnotes, endnotes, cross-references | `bookmarks list/insert/remove`, `footnotes list/insert/update/remove`, `cross-refs list/insert/remove` |
| [diff.md](diff.md) | Snapshot-based diffing and patching | `diff capture`, `diff compare`, `diff apply` |
| [protection.md](protection.md) | Document protection and permission ranges | `protection get/set-editing-restriction/clear-editing-restriction`, `permission-ranges list/create/remove` |
| [toc.md](toc.md) | Table of contents, index blocks, fields | `toc list/configure/update`, `index insert/rebuild`, `fields list/insert/rebuild` |
| [citations.md](citations.md) | Citations, bibliography, table of authorities | `citations insert/update/sources`, `citations bibliography insert/rebuild`, `authorities insert/rebuild` |

## Fallback

For any command not listed in these reference files:

```bash
superdoc describe command "<command name>" 2>/dev/null
```

To list all available commands:

```bash
superdoc describe 2>/dev/null
```

### Additional Command Categories Not Fully Documented Above

| Category | Commands | Description |
|----------|----------|-------------|
| `toc` | list, get, configure, update, remove, mark-entry, unmark-entry, list-entries, get-entry, edit-entry | Table of Contents |
| `index` | list, get, insert, configure, rebuild, remove, entries list/get/insert/update/remove | Index blocks and XE entries |
| `captions` | list, get, insert, update, remove, configure | Caption paragraphs |
| `fields` | list, get, insert, rebuild, remove | Generic Word fields |
| `citations` | list, get, insert, update, remove, sources list/get/insert/update/remove, bibliography get/insert/rebuild/configure/remove | Citations and bibliography |
| `authorities` | list, get, insert, configure, rebuild, remove, entries list/get/insert/update/remove | Table of authorities |
| `insert tab` | Insert a real Word tab node | `--target-json` or `--ref` |
| `insert line-break` | Insert a real Word line-break node | `--target-json` or `--ref` |
| `ranges resolve` | Resolve two anchors into a contiguous range | Returns SelectionTarget |
| `mutations preview` | Dry-run a mutation plan | Same as `mutations apply` but read-only |
| `capabilities` | Query runtime capabilities | (none) |
| `markdown-to-fragment` | Convert Markdown to SDFragment | `--markdown` |
