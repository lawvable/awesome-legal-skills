# Format Commands

### format apply

Apply inline run-property patch changes to the target range with explicit set/clear semantics.

```bash
superdoc format apply --tracked --block-id <id> --start <n> --end <n> --inline-json '<props>' 2>/dev/null
superdoc format apply --tracked --target-json '<SelectionTarget>' --inline-json '<props>' 2>/dev/null
superdoc format apply --tracked --ref "text:v4:eyJ..." --inline-json '<props>' 2>/dev/null
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--inline-json` | JSON | no | Inline formatting properties (see below) |
| `--target-json` | JSON | no* | SelectionTarget |
| `--ref` | string | no* | Ref string from query match |
| `--block-id` | string | no* | Target block ID |
| `--start` | number | no* | Start offset |
| `--end` | number | no* | End offset |
| `--in-json` | JSON | no | Story scope |
| `--tracked` | boolean | no | Apply as tracked change |
| `--change-mode` | string | no | `direct` or `tracked` |
| `--dry-run` | boolean | no | Preview without applying |

**Common inline properties for `--inline-json`:**

```json
{
  "bold": true,
  "italic": true,
  "underline": true,
  "strike": true,
  "fontSize": 12,
  "fontFamily": "Arial",
  "color": "#FF0000",
  "highlight": "yellow",
  "vertAlign": "superscript",
  "smallCaps": true,
  "caps": true,
  "dstrike": true
}
```

Set a property to `null` to clear it (e.g., `{"bold": null}` removes bold).

**Full list of inline properties:** `bold`, `italic`, `strike`, `underline`, `highlight`, `color`, `fontSize`, `fontFamily`, `letterSpacing`, `vertAlign` (superscript/subscript/baseline), `position`, `dstrike`, `smallCaps`, `caps`, `shading`, `border`, `outline`, `shadow`, `emboss`, `imprint`, `charScale`, `kerning`, `vanish`, `webHidden`, `specVanish`, `rtl`, `cs`, `bCs`, `iCs`, `eastAsianLayout`, `em`, `fitText`, `snapToGrid`, `lang`, `oMath`, `rStyle`, `rFonts`, `fontSizeCs`, `ligatures`, `numForm`, `numSpacing`, `stylisticSets`, `contextualAlternates`.

### Format Shortcuts

All format shortcuts accept the same targeting flags (`--block-id`+`--start`+`--end`, `--target-json`, or `--ref`) plus `--tracked` and `--dry-run`.

| Command | Description | Key value flag |
|---------|-------------|----------------|
| `format bold` | Set or clear bold | `--value true/false` |
| `format italic` | Set or clear italic | `--value true/false` |
| `format underline` | Set or clear underline | `--value true/false` |
| `format strike` | Set or clear strikethrough | `--value true/false` |
| `format strikethrough` | Apply strikethrough (alias) | `--value true/false` |
| `format highlight` | Set or clear highlight | `--value <color>` |
| `format color` | Set or clear text color | `--value <hex>` |
| `format font-size` | Set or clear font size | `--value <number>` |
| `format font-family` | Set or clear font family | `--value <string>` |
| `format letter-spacing` | Set or clear letter spacing | `--value <number>` |
| `format vert-align` | Set vertical alignment | `--value superscript/subscript/baseline` |
| `format position` | Set or clear position | `--value <number>` |
| `format dstrike` | Double strikethrough | `--value true/false` |
| `format small-caps` | Small caps | `--value true/false` |
| `format caps` | All caps | `--value true/false` |
| `format shading` | Run shading | `--value-json <object>` |
| `format border` | Run border | `--value-json <object>` |
| `format outline` | Outline effect | `--value true/false` |
| `format shadow` | Shadow effect | `--value true/false` |
| `format emboss` | Emboss effect | `--value true/false` |
| `format imprint` | Imprint effect | `--value true/false` |
| `format char-scale` | Character scale | `--value <number>` |
| `format kerning` | Kerning | `--value <number>` |
| `format vanish` | Hidden text | `--value true/false` |
| `format web-hidden` | Web hidden | `--value true/false` |
| `format rtl` | Right-to-left | `--value true/false` |
| `format r-style` | Run style reference | `--value <styleName>` |
| `format r-fonts` | Run fonts | `--value-json <object>` |
| `format font-size-cs` | Complex script font size | `--value <number>` |
| `format lang` | Language | `--value-json <object>` |
| `format em` | Emphasis mark | `--value <string>` |
| `format b-cs` | Complex script bold | `--value true/false` |
| `format i-cs` | Complex script italic | `--value true/false` |
| `format cs` | Complex script flag | `--value true/false` |
| `format spec-vanish` | Special vanish | `--value true/false` |
| `format o-math` | Math mode | `--value true/false` |
| `format snap-to-grid` | Snap to grid | `--value true/false` |
| `format east-asian-layout` | East Asian layout | `--value-json <object>` |
| `format fit-text` | Fit text | `--value-json <object>` |
| `format ligatures` | OpenType ligatures | `--value <string>` |
| `format num-form` | Number form | `--value <string>` |
| `format num-spacing` | Number spacing | `--value <string>` |
| `format stylistic-sets` | OpenType stylistic sets | `--value-json <array>` |
| `format contextual-alternates` | Contextual alternates | `--value true/false` |

Note: `format strikethrough` exists in addition to `format strike` -- both work.

### Paragraph Formatting

| Command | Description | Key flags |
|---------|-------------|-----------|
| `styles paragraph set-style` | Apply a paragraph style | `--target-json`, `--style` |
| `styles paragraph clear-style` | Remove paragraph style | `--target-json` |
| `format paragraph set-alignment` | Set alignment (left/center/right/both) | `--target-json`, `--alignment` |
| `format paragraph clear-alignment` | Remove direct alignment | `--target-json` |
| `format paragraph set-indentation` | Set indent (twips) | `--target-json`, `--left`, `--right`, `--first-line`, `--hanging` |
| `format paragraph clear-indentation` | Remove direct indent | `--target-json` |
| `format paragraph set-spacing` | Set spacing (twips) | `--target-json`, `--before`, `--after`, `--line`, `--line-rule` |
| `format paragraph clear-spacing` | Remove direct spacing | `--target-json` |
| `format paragraph set-keep-options` | Keep-with-next, widow/orphan | `--target-json`, flags |
| `format paragraph set-outline-level` | Set outline level (0-9) | `--target-json`, `--level` |
| `format paragraph set-flow-options` | Page-break-before, contextual spacing | `--target-json`, flags |
| `format paragraph set-tab-stop` | Add/replace tab stop | `--target-json`, `--position`, `--alignment`, `--leader` |
| `format paragraph clear-tab-stop` | Remove a tab stop | `--target-json`, `--position` |
| `format paragraph clear-all-tab-stops` | Remove all tab stops | `--target-json` |
| `format paragraph set-border` | Set paragraph border | `--target-json`, `--side`, config |
| `format paragraph clear-border` | Remove paragraph border | `--target-json`, `--side` |
| `format paragraph set-shading` | Set paragraph background | `--target-json`, `--fill` |
| `format paragraph clear-shading` | Remove paragraph shading | `--target-json` |
| `format paragraph set-direction` | Set LTR/RTL | `--target-json`, `--direction` |
| `format paragraph clear-direction` | Remove explicit direction | `--target-json` |
| `format paragraph reset-direct-formatting` | Strip all direct formatting | `--target-json` |

### Document-Level Styles

```bash
superdoc styles apply --patch-json '<stylesPatch>' --dry-run 2>/dev/null
```

Applies document-level default style changes to the stylesheet (word/styles.xml).
