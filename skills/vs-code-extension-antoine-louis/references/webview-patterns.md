# Webview Patterns

Comprehensive guide for building webview UIs in VS Code extensions.

## Table of Contents

- [Creating Webviews](#creating-webviews)
- [Content Security Policy](#content-security-policy)
- [Resource Loading](#resource-loading)
- [Message Passing](#message-passing)
- [State Persistence](#state-persistence)
- [React Integration](#react-integration)
- [Vite Configuration](#vite-configuration)
- [Sidebar Webviews](#sidebar-webviews)

---

## Creating Webviews

### WebviewPanel (Editor Area)

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  context.subscriptions.push(
    vscode.commands.registerCommand('myExt.openPanel', () => {
      const panel = vscode.window.createWebviewPanel(
        'myWebview',           // viewType (unique ID)
        'My Panel',            // title
        vscode.ViewColumn.One, // editor column
        {
          enableScripts: true,                    // Allow JS
          retainContextWhenHidden: true,          // Keep state when hidden
          localResourceRoots: [                   // Allowed resource paths
            vscode.Uri.joinPath(context.extensionUri, 'dist')
          ]
        }
      );

      panel.webview.html = getWebviewContent(panel.webview, context.extensionUri);

      // Handle messages from webview
      panel.webview.onDidReceiveMessage(
        message => handleMessage(message, panel),
        undefined,
        context.subscriptions
      );

      // Handle panel disposal
      panel.onDidDispose(() => {
        // Cleanup resources
      });
    })
  );
}
```

### WebviewViewProvider (Sidebar)

```typescript
class MyWebviewProvider implements vscode.WebviewViewProvider {
  private _view?: vscode.WebviewView;

  constructor(private readonly extensionUri: vscode.Uri) {}

  resolveWebviewView(
    webviewView: vscode.WebviewView,
    _context: vscode.WebviewViewResolveContext,
    _token: vscode.CancellationToken
  ) {
    this._view = webviewView;

    webviewView.webview.options = {
      enableScripts: true,
      localResourceRoots: [this.extensionUri]
    };

    webviewView.webview.html = this.getHtml(webviewView.webview);

    webviewView.webview.onDidReceiveMessage(msg => {
      // Handle messages
    });
  }

  private getHtml(webview: vscode.Webview): string {
    // Return HTML content
  }

  public postMessage(message: any) {
    this._view?.webview.postMessage(message);
  }
}

// Register in activate()
const provider = new MyWebviewProvider(context.extensionUri);
context.subscriptions.push(
  vscode.window.registerWebviewViewProvider('myExt.sidebarView', provider)
);
```

---

## Content Security Policy

Always set a strict CSP to prevent XSS attacks.

```typescript
function getWebviewContent(webview: vscode.Webview, extensionUri: vscode.Uri): string {
  const scriptUri = webview.asWebviewUri(
    vscode.Uri.joinPath(extensionUri, 'dist', 'webview.js')
  );
  const styleUri = webview.asWebviewUri(
    vscode.Uri.joinPath(extensionUri, 'dist', 'webview.css')
  );

  // Generate nonce for inline scripts
  const nonce = getNonce();

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy" content="
    default-src 'none';
    style-src ${webview.cspSource} 'unsafe-inline';
    script-src 'nonce-${nonce}';
    font-src ${webview.cspSource};
    img-src ${webview.cspSource} https: data:;
  ">
  <link href="${styleUri}" rel="stylesheet">
  <title>My Webview</title>
</head>
<body>
  <div id="root"></div>
  <script nonce="${nonce}" src="${scriptUri}"></script>
</body>
</html>`;
}

function getNonce(): string {
  let text = '';
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  for (let i = 0; i < 32; i++) {
    text += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return text;
}
```

**CSP Directives:**

| Directive | Purpose |
|-----------|---------|
| `default-src 'none'` | Block all by default |
| `script-src 'nonce-xxx'` | Only allow scripts with matching nonce |
| `style-src ${webview.cspSource}` | Allow extension styles |
| `font-src ${webview.cspSource}` | Allow extension fonts |
| `img-src ${webview.cspSource} https:` | Allow extension and HTTPS images |

---

## Resource Loading

Convert local paths to webview URIs:

```typescript
// Extension code
const scriptUri = webview.asWebviewUri(
  vscode.Uri.joinPath(extensionUri, 'dist', 'webview', 'index.js')
);

const imageUri = webview.asWebviewUri(
  vscode.Uri.joinPath(extensionUri, 'media', 'icon.png')
);
```

**In HTML:**

```html
<script src="${scriptUri}"></script>
<img src="${imageUri}">
<link href="${styleUri}" rel="stylesheet">
```

---

## Message Passing

### Extension → Webview

```typescript
// Extension code
panel.webview.postMessage({
  type: 'update',
  data: { items: [...] }
});
```

### Webview → Extension

```typescript
// Extension code
panel.webview.onDidReceiveMessage(message => {
  switch (message.type) {
    case 'save':
      saveData(message.data);
      break;
    case 'alert':
      vscode.window.showInformationMessage(message.text);
      break;
    case 'openFile':
      vscode.commands.executeCommand('vscode.open', vscode.Uri.file(message.path));
      break;
  }
});
```

### Webview JavaScript

```typescript
// Webview code (runs in browser context)
declare function acquireVsCodeApi(): {
  postMessage(message: any): void;
  getState(): any;
  setState(state: any): void;
};

const vscode = acquireVsCodeApi();

// Send message to extension
function sendToExtension(type: string, data: any) {
  vscode.postMessage({ type, data });
}

// Receive messages from extension
window.addEventListener('message', event => {
  const message = event.data;
  switch (message.type) {
    case 'update':
      updateUI(message.data);
      break;
  }
});

// Example: button click
document.getElementById('saveBtn')?.addEventListener('click', () => {
  vscode.postMessage({ type: 'save', data: getData() });
});
```

---

## State Persistence

Webview state persists when the panel is hidden (if `retainContextWhenHidden: true`) or across VS Code restarts.

```typescript
// Webview code
const vscode = acquireVsCodeApi();

// Restore previous state
const previousState = vscode.getState();
if (previousState) {
  restoreUI(previousState);
}

// Save state when it changes
function updateState(newState: any) {
  vscode.setState(newState);
}

// Example: save form data
document.getElementById('input')?.addEventListener('input', (e) => {
  const value = (e.target as HTMLInputElement).value;
  vscode.setState({ ...vscode.getState(), inputValue: value });
});
```

### Serialization for Restart

```typescript
// Extension code
class MySerializer implements vscode.WebviewPanelSerializer {
  constructor(private readonly extensionUri: vscode.Uri) {}

  async deserializeWebviewPanel(panel: vscode.WebviewPanel, state: any) {
    panel.webview.options = { enableScripts: true };
    panel.webview.html = getWebviewContent(panel.webview, this.extensionUri);

    // Restore state
    if (state) {
      panel.webview.postMessage({ type: 'restore', data: state });
    }
  }
}

// Register in activate()
vscode.window.registerWebviewPanelSerializer('myWebview', new MySerializer(context.extensionUri));
```

---

## React Integration

### Project Structure

```
src/
├── extension.ts          # Extension entry
└── webview/
    ├── index.tsx         # React entry
    ├── App.tsx           # Main component
    ├── components/       # React components
    ├── hooks/
    │   └── useVsCode.ts  # VS Code API hook
    └── vite.config.ts    # Vite config
```

### VS Code Hook

```typescript
// src/webview/hooks/useVsCode.ts
import { useEffect, useRef, useState, useCallback } from 'react';

interface VsCodeApi {
  postMessage(message: any): void;
  getState(): any;
  setState(state: any): void;
}

declare function acquireVsCodeApi(): VsCodeApi;

const vscodeApi = acquireVsCodeApi();

export function useVsCode<T = any>() {
  const [state, setStateInternal] = useState<T | undefined>(vscodeApi.getState);

  const setState = useCallback((newState: T) => {
    vscodeApi.setState(newState);
    setStateInternal(newState);
  }, []);

  const postMessage = useCallback((message: any) => {
    vscodeApi.postMessage(message);
  }, []);

  return { state, setState, postMessage };
}

export function useMessage<T = any>(handler: (message: T) => void) {
  const handlerRef = useRef(handler);
  handlerRef.current = handler;

  useEffect(() => {
    const listener = (event: MessageEvent) => {
      handlerRef.current(event.data);
    };
    window.addEventListener('message', listener);
    return () => window.removeEventListener('message', listener);
  }, []);
}
```

### React App

```tsx
// src/webview/App.tsx
import { useState } from 'react';
import { useVsCode, useMessage } from './hooks/useVsCode';

interface AppState {
  items: string[];
}

interface Message {
  type: 'update' | 'clear';
  data?: any;
}

export function App() {
  const { state, setState, postMessage } = useVsCode<AppState>();
  const [items, setItems] = useState<string[]>(state?.items || []);

  useMessage<Message>((message) => {
    switch (message.type) {
      case 'update':
        setItems(message.data.items);
        setState({ items: message.data.items });
        break;
      case 'clear':
        setItems([]);
        setState({ items: [] });
        break;
    }
  });

  const handleAdd = () => {
    postMessage({ type: 'addItem' });
  };

  const handleSave = () => {
    postMessage({ type: 'save', data: { items } });
  };

  return (
    <div className="app">
      <button onClick={handleAdd}>Add Item</button>
      <button onClick={handleSave}>Save</button>
      <ul>
        {items.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>
    </div>
  );
}
```

### Entry Point

```tsx
// src/webview/index.tsx
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { App } from './App';
import './styles.css';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>
);
```

---

## Vite Configuration

```typescript
// src/webview/vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: resolve(__dirname, '../../dist/webview'),
    rollupOptions: {
      input: resolve(__dirname, 'index.html'),
      output: {
        entryFileNames: '[name].js',
        chunkFileNames: '[name].js',
        assetFileNames: '[name].[ext]'
      }
    },
    sourcemap: true,
    emptyOutDir: true
  },
  define: {
    'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV || 'production')
  }
});
```

### Webview HTML Template

```html
<!-- src/webview/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Webview</title>
</head>
<body>
  <div id="root"></div>
  <script type="module" src="./index.tsx"></script>
</body>
</html>
```

**Note:** The extension code replaces this with the CSP-secured version at runtime.

---

## Sidebar Webviews

Register in `package.json`:

```json
{
  "contributes": {
    "viewsContainers": {
      "activitybar": [
        {
          "id": "myExtContainer",
          "title": "My Extension",
          "icon": "resources/icon.svg"
        }
      ]
    },
    "views": {
      "myExtContainer": [
        {
          "id": "myExt.sidebarView",
          "name": "My View",
          "type": "webview"
        }
      ]
    }
  }
}
```

The `WebviewViewProvider` (shown earlier) handles the sidebar webview.

---

## VS Code Theme Integration

Use VS Code CSS variables for consistent theming:

```css
/* Webview CSS */
body {
  background-color: var(--vscode-editor-background);
  color: var(--vscode-editor-foreground);
  font-family: var(--vscode-font-family);
  font-size: var(--vscode-font-size);
}

button {
  background-color: var(--vscode-button-background);
  color: var(--vscode-button-foreground);
  border: none;
  padding: 6px 14px;
  cursor: pointer;
}

button:hover {
  background-color: var(--vscode-button-hoverBackground);
}

input, textarea {
  background-color: var(--vscode-input-background);
  color: var(--vscode-input-foreground);
  border: 1px solid var(--vscode-input-border);
  padding: 4px 8px;
}

a {
  color: var(--vscode-textLink-foreground);
}

.error {
  color: var(--vscode-errorForeground);
}

.warning {
  color: var(--vscode-editorWarning-foreground);
}
```

**Common Variables:**

| Variable | Purpose |
|----------|---------|
| `--vscode-editor-background` | Main background |
| `--vscode-editor-foreground` | Main text |
| `--vscode-button-background` | Button background |
| `--vscode-button-foreground` | Button text |
| `--vscode-input-background` | Input background |
| `--vscode-input-border` | Input border |
| `--vscode-focusBorder` | Focus outline |
| `--vscode-list-activeSelectionBackground` | Selected item |
