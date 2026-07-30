# Table of Contents, Index, Fields

## Table of Contents (toc)

| Command | Description |
|---------|-------------|
| `toc list` | List all tables of contents in the document |
| `toc get` | Retrieve details of a specific table of contents |
| `toc configure` | Update the configuration switches of a table of contents |
| `toc update` | Rebuild or refresh the materialized content of a table of contents |
| `toc remove` | Remove a table of contents from the document |
| `toc mark-entry` | Insert a TC (table of contents entry) field at the target paragraph |
| `toc unmark-entry` | Remove a TC (table of contents entry) field from the document |
| `toc list-entries` | List all TC (table of contents entry) fields in the document body |
| `toc get-entry` | Retrieve details of a specific TC entry field |
| `toc edit-entry` | Update the properties of a TC entry field |

To create a table of contents, use `create table-of-contents` (see [create.md](create.md)).

## Index

| Command | Description |
|---------|-------------|
| `index list` | List all index blocks in the document |
| `index get` | Get detailed information about a specific index block |
| `index insert` | Insert a new index block at a target location |
| `index configure` | Update the configuration of an existing index block |
| `index rebuild` | Rebuild (regenerate) an index block from its entries |
| `index remove` | Remove an index block from the document |
| `index entries list` | List all XE (index entry) fields in the document |
| `index entries get` | Get detailed information about a specific XE index entry |
| `index entries insert` | Insert a new XE index entry field at a target location |
| `index entries update` | Update the properties of an existing XE index entry |
| `index entries remove` | Remove an XE index entry field from the document |

## Fields

Generic Word field operations. ToC, Index, cross-references, and citations all use fields internally.

| Command | Description |
|---------|-------------|
| `fields list` | List all fields in the document |
| `fields get` | Get detailed information about a specific field |
| `fields insert` | Insert a raw field code at a target location |
| `fields rebuild` | Rebuild (recalculate) a field |
| `fields remove` | Remove a field from the document |

All mutating commands support `--dry-run`. Use `superdoc describe command "<name>"` for exact flags.
