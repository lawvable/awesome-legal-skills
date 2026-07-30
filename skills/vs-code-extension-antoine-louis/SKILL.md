---
name: vscode-extension-builder-lawvable
description: Build VS Code extensions from scratch or convert existing JS/React/Vue apps. Supports commands, webviews (React/Vue), custom editors, tree views, and AI agent integration via file-bridge IPC. Use when user wants to create a VS Code extension, convert a web app to an extension, add webviews or custom UIs to VS Code, implement tree views, build custom file editors, integrate with AI agents, or package/publish extensions (.vsix).
metadata:
  author: Antoine Louis (Lawvable)
  license: AGPL-3.0
  version: 2026.02.04
---

# VS Code Extension

Build VS Code extensions from scratch or convert existing web apps into portable, shareable extensions.

## Architecture

VS Code extensions run in two contexts:

1. **Extension Host (Node.js)** — Backend logic, file access, VS Code APIs
2. **Webviews (browser sandbox)** — Custom UIs with HTML/CSS/JS (React, Vue, vanilla)

Build stack: **TypeScript + esbuild** (extension) + **Vite** (webviews)

## Quick Start

1. Choose a template from `assets/` based on your needs (see decision tree below)
2. Copy the template to your project directory
3. Update `package.json`: name, displayName, publisher, description
4. Run `npm install` then `npm run build`
5. Press F5 in VS Code to launch Extension Development Host

## Template Decision Tree

| Need | Template |
|------|----------|
| Simple command/action | `assets/basic-command/` |
| Custom UI panel (React) | `assets/webview-react/` |
| Sidebar file tree | `assets/tree-view/` |
| Custom file editor | `assets/custom-editor/` |
| AI agent integration | `assets/file-bridge/` |

## Extension Types

### Commands

Register actions triggered via Command Palette, keyboard shortcuts, or menus.

```typescript
vscode.commands.registerCommand('myExt.doSomething', () => {
  vscode.window.showInformationMessage('Done!');
});
```

See [references/api-reference.md](references/api-reference.md) for common APIs.

### Webviews

Full HTML/CSS/JS UIs in panels or sidebar. Use React for complex interfaces.

```typescript
const panel = vscode.window.createWebviewPanel(
  'myView', 'My Panel', vscode.ViewColumn.One,
  { enableScripts: true }
);
panel.webview.html = getWebviewContent();
```

See [references/webview-patterns.md](references/webview-patterns.md) for React setup, messaging, and CSP.

### Tree Views

Hierarchical data in the sidebar (file explorers, outlines, lists).

```typescript
vscode.window.registerTreeDataProvider('myTreeView', new MyTreeProvider());
```

See [references/tree-view-patterns.md](references/tree-view-patterns.md) for TreeDataProvider patterns.

### Custom Editors

Replace the default editor for specific file types.

```typescript
vscode.window.registerCustomEditorProvider('myExt.myEditor', new MyEditorProvider());
```

See [references/custom-editor-patterns.md](references/custom-editor-patterns.md) for document sync and undo/redo.

## Converting Existing Apps

To convert a JS/React/Vue app into an extension:

1. **Assess** — What does the app do? What VS Code features does it need?
2. **Map APIs** — Replace web APIs with VS Code equivalents
3. **Restructure** — Move UI into webview, logic into extension host
4. **Connect** — Wire up postMessage communication

| Web API | VS Code Equivalent |
|---------|-------------------|
| `localStorage` | `context.globalState` / `context.workspaceState` |
| `fetch()` | `vscode.workspace.fs` or keep `fetch` for external APIs |
| Router | Multiple webview panels or sidebar views |
| `alert()` | `vscode.window.showInformationMessage()` |
| `prompt()` | `vscode.window.showInputBox()` |
| `confirm()` | `vscode.window.showWarningMessage()` with options |

See [references/conversion-guide.md](references/conversion-guide.md) for detailed step-by-step process.

## Build System

**Extension code** — Use esbuild (fast, simple):

```javascript
// esbuild.js
esbuild.build({
  entryPoints: ['src/extension.ts'],
  bundle: true,
  outfile: 'dist/extension.js',
  external: ['vscode'],
  format: 'cjs',
  platform: 'node',
});
```

**Webview code** — Use Vite (HMR, React support):

```javascript
// vite.config.ts
export default defineConfig({
  build: {
    outDir: '../dist/webview',
    rollupOptions: { output: { entryFileNames: '[name].js' } }
  }
});
```

See [references/build-config.md](references/build-config.md) for complete configurations.

## package.json Manifest

Essential fields:

```json
{
  "name": "my-extension",
  "displayName": "My Extension",
  "publisher": "your-publisher-id",
  "version": "0.0.1",
  "engines": { "vscode": "^1.85.0" },
  "main": "./dist/extension.js",
  "activationEvents": [],
  "contributes": {
    "commands": [{ "command": "myExt.hello", "title": "Hello" }]
  }
}
```

The `contributes` section defines commands, menus, views, settings, keybindings, and more.

See [references/contribution-points.md](references/contribution-points.md) for all contribution types.

## IPC Patterns

### Extension ↔ Webview

Use `postMessage` for bidirectional communication:

```typescript
// Extension → Webview
panel.webview.postMessage({ type: 'update', data: {...} });

// Webview → Extension
panel.webview.onDidReceiveMessage(msg => {
  if (msg.type === 'save') { /* handle */ }
});
```

### Extension ↔ External Tools (AI Agents)

Use file-based IPC for communication with Claude Code or other agents:

```typescript
// Watch for command files
fs.watch(commandDir, (event, filename) => {
  if (filename.endsWith('.json')) {
    const command = JSON.parse(fs.readFileSync(path.join(commandDir, filename)));
    processCommand(command);
  }
});
```

See [references/ai-integration.md](references/ai-integration.md) for the file-bridge pattern.

## Packaging & Distribution

### Package as .vsix

```bash
npm install -g @vscode/vsce
vsce package
```

This creates `my-extension-0.0.1.vsix`.

### .vscodeignore

Exclude unnecessary files:

```
.vscode/**
node_modules/**
src/**
*.ts
tsconfig.json
esbuild.js
vite.config.ts
```

### Distribution Options

1. **Direct sharing** — Send .vsix file, install via `code --install-extension file.vsix`
2. **VS Marketplace** — Publish with `vsce publish` (requires Microsoft account)
3. **Open VSX** — Alternative registry for open-source extensions

### Platform-Specific Builds

For extensions with native dependencies:

```bash
vsce package --target win32-x64
vsce package --target darwin-arm64
vsce package --target linux-x64
```

## Reference Files

| File | When to Read |
|------|--------------|
| [api-reference.md](references/api-reference.md) | Implementing extension features |
| [contribution-points.md](references/contribution-points.md) | Configuring package.json contributes |
| [webview-patterns.md](references/webview-patterns.md) | Building React webviews |
| [tree-view-patterns.md](references/tree-view-patterns.md) | Implementing tree views |
| [custom-editor-patterns.md](references/custom-editor-patterns.md) | Building custom file editors |
| [build-config.md](references/build-config.md) | Configuring esbuild/Vite |
| [conversion-guide.md](references/conversion-guide.md) | Converting web apps |
| [ai-integration.md](references/ai-integration.md) | Integrating with AI agents |

## Asset Templates

| Template | Description |
|----------|-------------|
| [basic-command/](assets/basic-command/) | Minimal extension with one command |
| [webview-react/](assets/webview-react/) | React webview panel with messaging |
| [tree-view/](assets/tree-view/) | Sidebar tree view with provider |
| [custom-editor/](assets/custom-editor/) | Custom editor for specific file types |
| [file-bridge/](assets/file-bridge/) | File-based IPC for AI agents |
