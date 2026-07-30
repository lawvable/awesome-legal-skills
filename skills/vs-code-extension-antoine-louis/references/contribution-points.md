# Contribution Points Reference

Complete reference for `package.json` contributes section. These define how your extension integrates with VS Code.

## Table of Contents

- [commands](#commands) — Command definitions
- [menus](#menus) — Context menus, command palette
- [keybindings](#keybindings) — Keyboard shortcuts
- [configuration](#configuration) — Extension settings
- [views](#views) — Tree views in sidebar
- [viewsContainers](#viewscontainers) — Custom sidebar containers
- [customEditors](#customeditors) — Custom file editors
- [languages](#languages) — Language support
- [icons](#icons) — Custom icons
- [walkthroughs](#walkthroughs) — Getting started guides

---

## commands

Define commands that users can execute.

```json
{
  "contributes": {
    "commands": [
      {
        "command": "myExt.helloWorld",
        "title": "Hello World",
        "category": "My Extension",
        "icon": "$(sparkle)"
      },
      {
        "command": "myExt.openFile",
        "title": "Open File",
        "category": "My Extension",
        "enablement": "resourceScheme == file"
      }
    ]
  }
}
```

**Properties:**

| Property | Description |
|----------|-------------|
| `command` | Unique command ID (required) |
| `title` | Display name in Command Palette (required) |
| `category` | Groups commands (shown as "Category: Title") |
| `icon` | Icon for toolbar buttons (`$(icon-name)` or `{ "light": "...", "dark": "..." }`) |
| `enablement` | When clause to enable/disable command |
| `shortTitle` | Shorter title for menus |

---

## menus

Place commands in menus and toolbars.

```json
{
  "contributes": {
    "menus": {
      "commandPalette": [
        {
          "command": "myExt.helloWorld",
          "when": "editorHasSelection"
        }
      ],
      "editor/context": [
        {
          "command": "myExt.formatSelection",
          "when": "editorHasSelection",
          "group": "1_modification"
        }
      ],
      "editor/title": [
        {
          "command": "myExt.refresh",
          "when": "resourceLangId == json",
          "group": "navigation"
        }
      ],
      "explorer/context": [
        {
          "command": "myExt.openFile",
          "when": "resourceExtname == .json",
          "group": "navigation"
        }
      ],
      "view/title": [
        {
          "command": "myExt.refreshTree",
          "when": "view == myTreeView",
          "group": "navigation"
        }
      ],
      "view/item/context": [
        {
          "command": "myExt.deleteItem",
          "when": "view == myTreeView && viewItem == deletable",
          "group": "inline"
        }
      ]
    }
  }
}
```

**Menu Locations:**

| Menu | Location |
|------|----------|
| `commandPalette` | Command Palette (Ctrl+Shift+P) |
| `editor/context` | Right-click in editor |
| `editor/title` | Editor tab toolbar |
| `editor/title/context` | Right-click editor tab |
| `explorer/context` | Right-click in file explorer |
| `view/title` | Tree view title bar |
| `view/item/context` | Right-click tree view item |
| `scm/title` | Source control title bar |
| `terminal/context` | Right-click in terminal |

**Groups (determine order):**

- `navigation` — Top section
- `1_modification` — Edit actions
- `9_cutcopypaste` — Clipboard actions
- `z_commands` — Bottom section
- `inline` — Inline buttons (icons only)

---

## keybindings

Define keyboard shortcuts.

```json
{
  "contributes": {
    "keybindings": [
      {
        "command": "myExt.helloWorld",
        "key": "ctrl+shift+h",
        "mac": "cmd+shift+h",
        "when": "editorTextFocus"
      },
      {
        "command": "myExt.save",
        "key": "ctrl+s",
        "when": "editorTextFocus && resourceExtname == .myext"
      }
    ]
  }
}
```

**Key Modifiers:**

- Windows/Linux: `ctrl`, `shift`, `alt`
- Mac: `cmd`, `ctrl`, `shift`, `alt`

**Special Keys:** `enter`, `escape`, `tab`, `space`, `backspace`, `delete`, `up`, `down`, `left`, `right`, `home`, `end`, `pageup`, `pagedown`, `f1`-`f19`

---

## configuration

Define extension settings.

```json
{
  "contributes": {
    "configuration": {
      "title": "My Extension",
      "properties": {
        "myExt.enabled": {
          "type": "boolean",
          "default": true,
          "description": "Enable the extension"
        },
        "myExt.maxItems": {
          "type": "number",
          "default": 100,
          "minimum": 1,
          "maximum": 1000,
          "description": "Maximum number of items to display"
        },
        "myExt.mode": {
          "type": "string",
          "default": "auto",
          "enum": ["auto", "manual", "disabled"],
          "enumDescriptions": [
            "Automatically detect mode",
            "Manual mode",
            "Disable feature"
          ],
          "description": "Operation mode"
        },
        "myExt.paths": {
          "type": "array",
          "items": { "type": "string" },
          "default": [],
          "description": "List of paths to include"
        },
        "myExt.settings": {
          "type": "object",
          "default": {},
          "description": "Advanced settings"
        }
      }
    }
  }
}
```

**Types:** `boolean`, `number`, `string`, `array`, `object`, `null`

**Scopes:**

```json
{
  "myExt.setting": {
    "scope": "resource",
    "type": "boolean"
  }
}
```

- `application` — User settings only
- `machine` — User settings, not synced
- `window` — User or workspace settings
- `resource` — Can be different per folder/file (most flexible)

---

## views

Define tree views in sidebar.

```json
{
  "contributes": {
    "views": {
      "explorer": [
        {
          "id": "myTreeView",
          "name": "My View",
          "when": "workspaceFolderCount > 0",
          "icon": "$(list-tree)",
          "contextualTitle": "My Extension"
        }
      ],
      "myContainer": [
        {
          "id": "mySecondView",
          "name": "Second View",
          "type": "webview"
        }
      ]
    }
  }
}
```

**Built-in Containers:**

- `explorer` — File explorer sidebar
- `scm` — Source control sidebar
- `debug` — Debug sidebar
- `test` — Testing sidebar

**View Types:**

- Default (tree view) — Uses `TreeDataProvider`
- `"type": "webview"` — Full HTML/CSS/JS UI

---

## viewsContainers

Create custom sidebar containers.

```json
{
  "contributes": {
    "viewsContainers": {
      "activitybar": [
        {
          "id": "myContainer",
          "title": "My Extension",
          "icon": "resources/icon.svg"
        }
      ],
      "panel": [
        {
          "id": "myPanel",
          "title": "My Panel",
          "icon": "$(output)"
        }
      ]
    }
  }
}
```

**Locations:**

- `activitybar` — Left sidebar (icons)
- `panel` — Bottom panel (tabs)

---

## customEditors

Register custom editors for file types.

```json
{
  "contributes": {
    "customEditors": [
      {
        "viewType": "myExt.myEditor",
        "displayName": "My Editor",
        "selector": [
          { "filenamePattern": "*.myext" },
          { "filenamePattern": "*.custom" }
        ],
        "priority": "default"
      }
    ]
  }
}
```

**Priority:**

- `default` — Opens by default for matching files
- `option` — Available in "Open With..." menu

---

## languages

Register language support.

```json
{
  "contributes": {
    "languages": [
      {
        "id": "mylang",
        "aliases": ["My Language", "mylang"],
        "extensions": [".mylang", ".ml"],
        "configuration": "./language-configuration.json",
        "icon": {
          "light": "./icons/mylang-light.svg",
          "dark": "./icons/mylang-dark.svg"
        }
      }
    ],
    "grammars": [
      {
        "language": "mylang",
        "scopeName": "source.mylang",
        "path": "./syntaxes/mylang.tmLanguage.json"
      }
    ]
  }
}
```

---

## icons

Register custom icons for use in the UI.

```json
{
  "contributes": {
    "icons": {
      "myext-logo": {
        "description": "My Extension Logo",
        "default": {
          "fontPath": "./icons/myext-icons.woff",
          "fontCharacter": "\\E001"
        }
      }
    }
  }
}
```

Use with `$(myext-logo)` in commands and UI elements.

---

## walkthroughs

Create interactive getting started guides.

```json
{
  "contributes": {
    "walkthroughs": [
      {
        "id": "myExt.gettingStarted",
        "title": "Getting Started with My Extension",
        "description": "Learn how to use My Extension",
        "steps": [
          {
            "id": "installDependencies",
            "title": "Install Dependencies",
            "description": "Run the setup command.\n\n[Run Setup](command:myExt.setup)",
            "media": {
              "image": "media/setup.png",
              "altText": "Setup screenshot"
            },
            "completionEvents": ["onCommand:myExt.setup"]
          },
          {
            "id": "openFile",
            "title": "Open a File",
            "description": "Open any .myext file to get started.",
            "completionEvents": ["onLanguage:mylang"]
          }
        ]
      }
    ]
  }
}
```

---

## Activation Events

Define when your extension activates.

```json
{
  "activationEvents": [
    "onCommand:myExt.helloWorld",
    "onLanguage:javascript",
    "onView:myTreeView",
    "workspaceContains:**/.myextrc",
    "onFileSystem:myfs",
    "onCustomEditor:myExt.myEditor",
    "onUri",
    "*"
  ]
}
```

**Common Events:**

| Event | Activates When |
|-------|----------------|
| `onCommand:commandId` | Command is executed |
| `onLanguage:langId` | File of that language opens |
| `onView:viewId` | View is expanded |
| `workspaceContains:glob` | Workspace contains matching file |
| `onFileSystem:scheme` | File with URI scheme is accessed |
| `onCustomEditor:viewType` | Custom editor opens |
| `onUri` | Extension URI is opened |
| `*` | VS Code starts (avoid if possible) |

**Note:** As of VS Code 1.74, many activation events are implicit. Commands, views, and custom editors auto-activate.

---

## When Clause Contexts

Use in `when` properties for conditional visibility.

**Editor Contexts:**

| Context | Description |
|---------|-------------|
| `editorFocus` | Editor has focus |
| `editorTextFocus` | Editor text area has focus |
| `editorHasSelection` | Text is selected |
| `editorReadonly` | Editor is read-only |
| `editorLangId` | Editor language ID |

**Resource Contexts:**

| Context | Description |
|---------|-------------|
| `resourceScheme` | URI scheme (file, untitled, etc.) |
| `resourceExtname` | File extension (.js, .ts, etc.) |
| `resourceFilename` | File name |
| `resourcePath` | Full file path |
| `resourceLangId` | Language ID of file |

**Workspace Contexts:**

| Context | Description |
|---------|-------------|
| `workspaceFolderCount` | Number of workspace folders |
| `workbenchState` | `empty`, `folder`, or `workspace` |

**View Contexts:**

| Context | Description |
|---------|-------------|
| `view` | Current view ID |
| `viewItem` | Context value of tree item |
| `focusedView` | ID of focused view |

**Operators:** `==`, `!=`, `<`, `>`, `<=`, `>=`, `=~` (regex), `&&`, `||`, `!`, `in`

```json
{
  "when": "editorLangId == javascript && !editorReadonly",
  "when": "resourceExtname =~ /\\.(js|ts)$/",
  "when": "view == myTreeView && viewItem == folder"
}
```
