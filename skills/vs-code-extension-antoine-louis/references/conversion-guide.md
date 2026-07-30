# Web App Conversion Guide

Step-by-step guide for converting existing JS/React/Vue apps into VS Code extensions.

## Table of Contents

- [Assessment](#assessment)
- [Architecture Mapping](#architecture-mapping)
- [API Mapping](#api-mapping)
- [Step-by-Step Conversion](#step-by-step-conversion)
- [Common Patterns](#common-patterns)
- [Limitations](#limitations)

---

## Assessment

Before converting, assess your app:

### Questions to Answer

1. **What does the app do?**
   - Data visualization → Webview panel
   - File editing → Custom editor
   - Project navigation → Tree view
   - Background tasks → Extension commands

2. **What web APIs does it use?**
   - DOM manipulation → Webview (works as-is)
   - localStorage → VS Code state API
   - fetch() → Keep for external APIs, or use VS Code fs for files
   - File System Access API → VS Code workspace.fs

3. **Does it need a server?**
   - Static app → Convert directly
   - API server → Keep external or embed in extension

4. **What framework?**
   - React/Vue/Svelte → Webview with Vite
   - Vanilla JS → Webview (simplest)
   - Next.js/Nuxt → Extract client-side code only

### Conversion Difficulty

| App Type | Difficulty | Notes |
|----------|------------|-------|
| Static React/Vue SPA | Easy | Direct webview conversion |
| Form-based app | Easy | Map inputs to VS Code APIs |
| File viewer/editor | Medium | Use custom editor pattern |
| App with routing | Medium | Map routes to panels/views |
| Real-time/WebSocket | Medium | Keep external connection |
| Full-stack app | Hard | Extract frontend, keep backend external |
| SSR app (Next.js) | Hard | Extract client code, lose SSR |

---

## Architecture Mapping

### Web App → Extension Structure

```
Web App                          VS Code Extension
─────────────────────────────────────────────────────────
index.html          →            Webview HTML (generated)
src/App.tsx         →            src/webview/App.tsx
src/components/     →            src/webview/components/
src/hooks/          →            src/webview/hooks/
src/api/            →            src/extension.ts (or keep external)
public/assets/      →            media/ or dist/webview/
package.json        →            package.json (merged)
```

### State Management

| Web Pattern | VS Code Pattern |
|-------------|-----------------|
| React useState | Same (webview) |
| Redux/Zustand | Same (webview) + sync to extension |
| localStorage | `context.globalState` / `context.workspaceState` |
| IndexedDB | `context.globalStorageUri` (file-based) |
| URL params | Command arguments or `context.workspaceState` |

### Routing

| Web Pattern | VS Code Pattern |
|-------------|-----------------|
| Single route | Single webview panel |
| Multiple routes | Multiple panels or tabs in webview |
| Nested routes | Sidebar (tree) + panel combination |
| Modal routes | VS Code quick pick or webview modal |

---

## API Mapping

### Browser APIs → VS Code APIs

```typescript
// localStorage
// Before:
localStorage.setItem('key', JSON.stringify(data));
const data = JSON.parse(localStorage.getItem('key') || '{}');

// After:
await context.globalState.update('key', data);
const data = context.globalState.get('key', {});
```

```typescript
// alert/confirm/prompt
// Before:
alert('Done!');
const confirmed = confirm('Are you sure?');
const name = prompt('Enter name:');

// After:
vscode.window.showInformationMessage('Done!');
const confirmed = await vscode.window.showWarningMessage('Are you sure?', 'Yes', 'No') === 'Yes';
const name = await vscode.window.showInputBox({ prompt: 'Enter name:' });
```

```typescript
// File reading
// Before:
const response = await fetch('/data/config.json');
const config = await response.json();

// After (workspace file):
const uri = vscode.Uri.joinPath(vscode.workspace.workspaceFolders![0].uri, 'config.json');
const content = await vscode.workspace.fs.readFile(uri);
const config = JSON.parse(new TextDecoder().decode(content));
```

```typescript
// File writing
// Before:
const blob = new Blob([content], { type: 'text/plain' });
const url = URL.createObjectURL(blob);
// ... download link

// After:
const uri = await vscode.window.showSaveDialog({ filters: { 'Text': ['txt'] } });
if (uri) {
  await vscode.workspace.fs.writeFile(uri, new TextEncoder().encode(content));
}
```

```typescript
// Clipboard
// Before:
await navigator.clipboard.writeText(text);

// After:
await vscode.env.clipboard.writeText(text);
```

```typescript
// Open external URL
// Before:
window.open('https://example.com', '_blank');

// After:
await vscode.env.openExternal(vscode.Uri.parse('https://example.com'));
```

### Keep These As-Is

These work unchanged in webviews:
- `fetch()` for external APIs
- `setTimeout`, `setInterval`
- `console.log` (appears in webview devtools)
- DOM APIs (`document.querySelector`, etc.)
- Canvas API
- Web Workers (with some setup)

---

## Step-by-Step Conversion

### Step 1: Set Up Extension Structure

```bash
# Create extension from template
cp -r assets/webview-react my-converted-app
cd my-converted-app
npm install
```

### Step 2: Copy App Code

```bash
# Copy your React components
cp -r ../my-web-app/src/components src/webview/
cp -r ../my-web-app/src/hooks src/webview/
cp ../my-web-app/src/App.tsx src/webview/
```

### Step 3: Create VS Code Bridge Hook

```typescript
// src/webview/hooks/useVsCodeBridge.ts
import { useCallback, useEffect, useState } from 'react';

declare function acquireVsCodeApi(): {
  postMessage(message: any): void;
  getState(): any;
  setState(state: any): void;
};

const vscode = acquireVsCodeApi();

export function useVsCodeState<T>(key: string, defaultValue: T) {
  const [value, setValue] = useState<T>(() => {
    const state = vscode.getState() || {};
    return state[key] ?? defaultValue;
  });

  const updateValue = useCallback((newValue: T) => {
    setValue(newValue);
    const state = vscode.getState() || {};
    vscode.setState({ ...state, [key]: newValue });
  }, [key]);

  return [value, updateValue] as const;
}

export function useExtensionCommand() {
  return useCallback((command: string, args?: any) => {
    vscode.postMessage({ type: 'command', command, args });
  }, []);
}

export function useExtensionMessage<T>(handler: (data: T) => void) {
  useEffect(() => {
    const listener = (event: MessageEvent) => handler(event.data);
    window.addEventListener('message', listener);
    return () => window.removeEventListener('message', listener);
  }, [handler]);
}
```

### Step 4: Update App to Use Bridge

```typescript
// src/webview/App.tsx
import { useVsCodeState, useExtensionCommand } from './hooks/useVsCodeBridge';

export function App() {
  // Replace localStorage with VS Code state
  const [settings, setSettings] = useVsCodeState('settings', { theme: 'dark' });

  // Replace direct file operations with commands
  const sendCommand = useExtensionCommand();

  const handleSave = () => {
    sendCommand('save', { data: settings });
  };

  const handleOpenFile = () => {
    sendCommand('openFile');
  };

  return (
    // Your existing JSX
  );
}
```

### Step 5: Handle Commands in Extension

```typescript
// src/extension.ts
panel.webview.onDidReceiveMessage(async (message) => {
  switch (message.type) {
    case 'command':
      switch (message.command) {
        case 'save':
          await saveData(message.args.data);
          break;
        case 'openFile':
          const uri = await vscode.window.showOpenDialog({});
          if (uri?.[0]) {
            const content = await vscode.workspace.fs.readFile(uri[0]);
            panel.webview.postMessage({
              type: 'fileContent',
              content: new TextDecoder().decode(content)
            });
          }
          break;
      }
      break;
  }
});
```

### Step 6: Update Imports and Dependencies

```json
// package.json - merge dependencies
{
  "dependencies": {
    // Keep your app's dependencies
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
    // Remove server-side deps (express, etc.)
  },
  "devDependencies": {
    "@types/vscode": "^1.85.0",
    // ... extension dev deps
  }
}
```

### Step 7: Update Build Configuration

Ensure Vite builds your webview code. See [build-config.md](build-config.md).

### Step 8: Test and Iterate

1. Press F5 to launch Extension Development Host
2. Open Command Palette → Your Extension Command
3. Test functionality, fix issues
4. Check browser console (Developer Tools) for webview errors

---

## Common Patterns

### Converting a Form App

```typescript
// Before (web)
function ContactForm() {
  const [name, setName] = useState(localStorage.getItem('name') || '');

  const handleSubmit = async () => {
    await fetch('/api/submit', { method: 'POST', body: JSON.stringify({ name }) });
    alert('Submitted!');
  };
}

// After (extension webview)
function ContactForm() {
  const [name, setName] = useVsCodeState('name', '');
  const sendCommand = useExtensionCommand();

  const handleSubmit = () => {
    sendCommand('submit', { name });
  };
}

// Extension handles the command
panel.webview.onDidReceiveMessage(async (msg) => {
  if (msg.command === 'submit') {
    await fetch('https://api.example.com/submit', {
      method: 'POST',
      body: JSON.stringify(msg.args)
    });
    vscode.window.showInformationMessage('Submitted!');
  }
});
```

### Converting a Dashboard

```typescript
// Before: Multiple pages with router
// After: Tabs within single webview

function Dashboard() {
  const [activeTab, setActiveTab] = useVsCodeState('activeTab', 'overview');

  return (
    <div>
      <nav>
        <button onClick={() => setActiveTab('overview')}>Overview</button>
        <button onClick={() => setActiveTab('analytics')}>Analytics</button>
        <button onClick={() => setActiveTab('settings')}>Settings</button>
      </nav>
      {activeTab === 'overview' && <Overview />}
      {activeTab === 'analytics' && <Analytics />}
      {activeTab === 'settings' && <Settings />}
    </div>
  );
}
```

---

## Limitations

### What Won't Work

1. **Server-Side Rendering** — Webviews are client-only
2. **Server API routes** — Use external API or VS Code commands
3. **Real-time databases (Firebase Realtime, Supabase)** — May work but test carefully
4. **OAuth redirects** — Use VS Code's authentication API instead
5. **Service Workers** — Not supported in webviews
6. **Web Push Notifications** — Use VS Code notifications instead

### Workarounds

| Web Feature | VS Code Alternative |
|-------------|---------------------|
| OAuth login | `vscode.authentication.getSession()` |
| Push notifications | `vscode.window.showInformationMessage()` |
| Background sync | Extension background tasks |
| PWA install | Publish to VS Marketplace |
| SEO | Not applicable |

### Performance Considerations

- Webviews are Chromium instances (memory overhead)
- Consider `retainContextWhenHidden: true` for frequently used panels
- Large datasets: process in extension, send summary to webview
- Heavy computation: use Web Workers in webview or process in extension
