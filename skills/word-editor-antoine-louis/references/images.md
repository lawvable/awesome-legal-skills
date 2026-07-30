# Images

### Key Image Commands

| Command | Description | Key flags |
|---------|-------------|-----------|
| `create image` | Insert a new image | `--at-json`, `--src`, `--dry-run` |
| `images list` | List all images | (none) |
| `images get` | Get image details by ID | `--id` |
| `images delete` | Delete an image | `--id`, `--dry-run` |
| `images move` | Move image to new location | `--id`, `--at-json`, `--dry-run` |
| `images set-size` | Set width/height | `--id`, `--width`, `--height`, `--dry-run` |
| `images scale` | Scale by factor | `--id`, `--factor`, `--dry-run` |
| `images rotate` | Set rotation angle | `--id`, `--angle`, `--dry-run` |
| `images flip` | Flip horizontal/vertical | `--id`, `--horizontal`, `--vertical`, `--dry-run` |
| `images crop` | Apply rectangular crop | `--id`, `--dry-run` |
| `images reset-crop` | Remove all cropping | `--id`, `--dry-run` |
| `images replace-source` | Replace image source | `--id`, `--src`, `--dry-run` |
| `images set-alt-text` | Set alt text | `--id`, `--text`, `--dry-run` |
| `images set-decorative` | Mark as decorative | `--id`, `--decorative`, `--dry-run` |
| `images set-name` | Set object name | `--id`, `--name`, `--dry-run` |
| `images set-hyperlink` | Set/remove hyperlink | `--id`, `--href`, `--dry-run` |
| `images convert-to-inline` | Float to inline | `--id`, `--dry-run` |
| `images convert-to-floating` | Inline to float | `--id`, `--dry-run` |
| `images set-wrap-type` | Set text wrapping | `--id`, `--dry-run` |
| `images set-wrap-side` | Set wrap side | `--id`, `--dry-run` |
| `images set-wrap-distances` | Set wrap margins | `--id`, `--dry-run` |
| `images set-position` | Set anchor position | `--id`, `--dry-run` |
| `images set-anchor-options` | Set anchor behavior | `--id`, `--dry-run` |
| `images set-z-order` | Set z-order | `--id`, `--dry-run` |
| `images set-lock-aspect-ratio` | Lock/unlock aspect ratio | `--id`, `--dry-run` |
| `images insert-caption` | Insert caption below | `--id`, `--dry-run` |
| `images update-caption` | Update caption text | `--id`, `--dry-run` |
| `images remove-caption` | Remove caption | `--id`, `--dry-run` |

### Standalone Captions (not tied to a specific image)

| Command | Description |
|---------|-------------|
| `captions list` | List all caption paragraphs in the document |
| `captions get` | Get detailed information about a specific caption paragraph |
| `captions insert` | Insert a new caption paragraph adjacent to a target block |
| `captions update` | Update the text of an existing caption paragraph |
| `captions remove` | Remove a caption paragraph from the document |
| `captions configure` | Configure numbering format for a caption label |
