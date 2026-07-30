# Citations and Authorities

## Citations

### Citation marks

| Command | Description |
|---------|-------------|
| `citations list` | List all citation marks in the document |
| `citations get` | Get detailed information about a specific citation mark |
| `citations insert` | Insert a new citation mark at a target location |
| `citations update` | Update an existing citation mark's source references |
| `citations remove` | Remove a citation mark from the document |

### Citation sources (document store)

| Command | Description |
|---------|-------------|
| `citations sources list` | List all citation sources in the document store |
| `citations sources get` | Get detailed information about a specific citation source |
| `citations sources insert` | Register a new citation source in the document store |
| `citations sources update` | Update the fields of an existing citation source |
| `citations sources remove` | Remove a citation source from the document store |

### Bibliography

| Command | Description |
|---------|-------------|
| `citations bibliography get` | Get information about the bibliography block |
| `citations bibliography insert` | Insert a bibliography block at a target location |
| `citations bibliography rebuild` | Rebuild the bibliography from current sources |
| `citations bibliography configure` | Configure the bibliography style |
| `citations bibliography remove` | Remove the bibliography block from the document |

## Authorities (Table of Authorities)

| Command | Description |
|---------|-------------|
| `authorities list` | List all table-of-authorities blocks in the document |
| `authorities get` | Get detailed information about a specific table-of-authorities block |
| `authorities insert` | Insert a new table-of-authorities block at a target location |
| `authorities configure` | Update the configuration of an existing table-of-authorities block |
| `authorities rebuild` | Rebuild a table-of-authorities block from its entries |
| `authorities remove` | Remove a table-of-authorities block from the document |
| `authorities entries list` | List all TA (authority entry) fields in the document |
| `authorities entries get` | Get detailed information about a specific TA authority entry |
| `authorities entries insert` | Insert a new TA authority entry field at a target location |
| `authorities entries update` | Update the properties of an existing TA authority entry |
| `authorities entries remove` | Remove a TA authority entry field from the document |

All mutating commands support `--dry-run`. Use `superdoc describe command "<name>"` for exact flags.
