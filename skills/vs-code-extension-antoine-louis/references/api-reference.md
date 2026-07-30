# VS Code API Reference

Quick reference for commonly used VS Code APIs.

## Table of Contents

- [vscode.window](#vscodewindow) — Windows, editors, notifications, UI
- [vscode.workspace](#vscodeworkspace) — Files, configuration, events
- [vscode.commands](#vscodecommands) — Register and execute commands
- [ExtensionContext](#extensioncontext) — Activation context, storage, subscriptions
- [vscode.Uri](#vscodeuri) — File and resource URIs
- [vscode.env](#vscodeenv) — Environment info, clipboard, external links

---

## vscode.window

### Show Messages

```typescript
// Information (blue)
vscode.window.showInformationMessage('Operation completed');

// Warning (yellow)
vscode.window.showWarningMessage('This may take a while');

// Error (red)
vscode.window.showErrorMessage('Something went wrong');

// With action buttons
const result = await vscode.window.showInformationMessage(
  'Save changes?',
  'Save', 'Discard', 'Cancel'
);
if (result === 'Save') { /* ... */ }
```

### Input Boxes

```typescript
// Simple text input
const name = await vscode.window.showInputBox({
  prompt: 'Enter your name',
  placeHolder: 'John Doe',
  validateInput: (value) => value.length < 2 ? 'Too short' : null
});

// Password input
const password = await vscode.window.showInputBox({
  prompt: 'Enter password',
  password: true
});
```

### Quick Picks

```typescript
// Simple selection
const color = await vscode.window.showQuickPick(
  ['Red', 'Green', 'Blue'],
  { placeHolder: 'Select a color' }
);

// With descriptions
const item = await vscode.window.showQuickPick([
  { label: 'Option 1', description: 'First option', detail: 'More info' },
  { label: 'Option 2', description: 'Second option' }
]);

// Multi-select
const items = await vscode.window.showQuickPick(
  ['A', 'B', 'C'],
  { canPickMany: true }
);
```

### Progress Notifications

```typescript
await vscode.window.withProgress({
  location: vscode.ProgressLocation.Notification,
  title: 'Processing...',
  cancellable: true
}, async (progress, token) => {
  for (let i = 0; i < 100; i += 10) {
    if (token.isCancellationRequested) break;
    progress.report({ increment: 10, message: `${i}%` });
    await sleep(100);
  }
});
```

### Status Bar

```typescript
// Create status bar item
const statusBar = vscode.window.createStatusBarItem(
  vscode.StatusBarAlignment.Right, 100
);
statusBar.text = '$(sync~spin) Syncing...';
statusBar.tooltip = 'Click to cancel';
statusBar.command = 'myExt.cancelSync';
statusBar.show();

// Dispose when done
context.subscriptions.push(statusBar);
```

### Active Editor

```typescript
// Get active text editor
const editor = vscode.window.activeTextEditor;
if (editor) {
  const document = editor.document;
  const selection = editor.selection;
  const text = document.getText(selection);
}

// Listen for editor changes
vscode.window.onDidChangeActiveTextEditor(editor => {
  if (editor) {
    console.log('Switched to:', editor.document.fileName);
  }
});
```

### Output Channels

```typescript
// Create output channel
const output = vscode.window.createOutputChannel('My Extension');
output.appendLine('Starting...');
output.show(); // Reveal in Output panel

// Log channel (structured logging)
const log = vscode.window.createOutputChannel('My Extension', { log: true });
log.info('Information');
log.warn('Warning');
log.error('Error');
```

---

## vscode.workspace

### Read/Write Files

```typescript
// Read file
const uri = vscode.Uri.file('/path/to/file.txt');
const content = await vscode.workspace.fs.readFile(uri);
const text = new TextDecoder().decode(content);

// Write file
const data = new TextEncoder().encode('Hello World');
await vscode.workspace.fs.writeFile(uri, data);

// Delete file
await vscode.workspace.fs.delete(uri);

// Create directory
await vscode.workspace.fs.createDirectory(vscode.Uri.file('/path/to/dir'));

// Copy file
await vscode.workspace.fs.copy(sourceUri, targetUri, { overwrite: true });
```

### Open Documents

```typescript
// Open in editor
const doc = await vscode.workspace.openTextDocument(uri);
await vscode.window.showTextDocument(doc);

// Open untitled document
const doc = await vscode.workspace.openTextDocument({
  content: 'Initial content',
  language: 'javascript'
});

// Open text document by content
const doc = await vscode.workspace.openTextDocument({
  content: JSON.stringify(data, null, 2),
  language: 'json'
});
```

### Configuration

```typescript
// Read configuration
const config = vscode.workspace.getConfiguration('myExtension');
const value = config.get<string>('settingName', 'default');

// Update configuration
await config.update('settingName', 'newValue', vscode.ConfigurationTarget.Global);

// Watch for config changes
vscode.workspace.onDidChangeConfiguration(e => {
  if (e.affectsConfiguration('myExtension.settingName')) {
    // Reload setting
  }
});
```

### Workspace Folders

```typescript
// Get workspace folders
const folders = vscode.workspace.workspaceFolders;
if (folders) {
  const rootPath = folders[0].uri.fsPath;
}

// Find files
const files = await vscode.workspace.findFiles(
  '**/*.ts',           // include pattern
  '**/node_modules/**' // exclude pattern
);
```

### File System Watcher

```typescript
const watcher = vscode.workspace.createFileSystemWatcher('**/*.json');

watcher.onDidCreate(uri => console.log('Created:', uri.fsPath));
watcher.onDidChange(uri => console.log('Changed:', uri.fsPath));
watcher.onDidDelete(uri => console.log('Deleted:', uri.fsPath));

context.subscriptions.push(watcher);
```

---

## vscode.commands

### Register Commands

```typescript
// Simple command
const disposable = vscode.commands.registerCommand('myExt.hello', () => {
  vscode.window.showInformationMessage('Hello!');
});
context.subscriptions.push(disposable);

// Command with arguments
vscode.commands.registerCommand('myExt.openFile', (uri: vscode.Uri) => {
  vscode.window.showTextDocument(uri);
});

// Text editor command (has active editor)
vscode.commands.registerTextEditorCommand('myExt.format', (editor, edit) => {
  const text = editor.document.getText();
  edit.replace(editor.selection, text.toUpperCase());
});
```

### Execute Commands

```typescript
// Execute built-in command
await vscode.commands.executeCommand('vscode.open', uri);

// Execute with arguments
await vscode.commands.executeCommand('myExt.openFile', uri);

// Get command result
const result = await vscode.commands.executeCommand<string>('myExt.getValue');
```

### Built-in Commands

```typescript
// Open file
await vscode.commands.executeCommand('vscode.open', uri);

// Open folder
await vscode.commands.executeCommand('vscode.openFolder', uri);

// Open settings
await vscode.commands.executeCommand('workbench.action.openSettings');

// Show file in explorer
await vscode.commands.executeCommand('revealInExplorer', uri);

// Execute terminal command
await vscode.commands.executeCommand('workbench.action.terminal.sendSequence', {
  text: 'npm install\n'
});
```

---

## ExtensionContext

Passed to `activate()` function. Store subscriptions and state.

### Subscriptions

```typescript
export function activate(context: vscode.ExtensionContext) {
  // Register disposables for cleanup on deactivate
  context.subscriptions.push(
    vscode.commands.registerCommand('myExt.cmd', () => {}),
    vscode.window.createStatusBarItem(),
    fileWatcher
  );
}
```

### Storage

```typescript
// Global state (persists across workspaces)
await context.globalState.update('key', { data: 'value' });
const data = context.globalState.get<{ data: string }>('key');

// Workspace state (per workspace)
await context.workspaceState.update('key', 'value');

// Secrets (encrypted storage)
await context.secrets.store('apiKey', 'secret-value');
const apiKey = await context.secrets.get('apiKey');
```

### Extension Paths

```typescript
// Extension installation directory
const extensionPath = context.extensionPath;

// Global storage (persists, writable)
const storagePath = context.globalStorageUri.fsPath;

// Workspace storage (per workspace, writable)
const workspaceStorage = context.storageUri?.fsPath;

// Log output path
const logPath = context.logUri.fsPath;
```

### Extension URI

```typescript
// Get URI for bundled resource
const iconUri = vscode.Uri.joinPath(context.extensionUri, 'media', 'icon.png');

// For webview resources
const scriptUri = panel.webview.asWebviewUri(
  vscode.Uri.joinPath(context.extensionUri, 'dist', 'webview.js')
);
```

---

## vscode.Uri

### Create URIs

```typescript
// From file path
const uri = vscode.Uri.file('/path/to/file.txt');

// From string
const uri = vscode.Uri.parse('https://example.com/api');

// Join paths
const uri = vscode.Uri.joinPath(baseUri, 'subdir', 'file.txt');
```

### URI Properties

```typescript
const uri = vscode.Uri.file('/Users/me/project/file.ts');

uri.scheme;   // 'file'
uri.fsPath;   // '/Users/me/project/file.ts'
uri.path;     // '/Users/me/project/file.ts'
uri.toString(); // 'file:///Users/me/project/file.ts'
```

---

## vscode.env

### Environment Info

```typescript
// Machine ID (anonymous, stable)
const machineId = vscode.env.machineId;

// Session ID (changes each session)
const sessionId = vscode.env.sessionId;

// VS Code version
const version = vscode.version;

// Is running in development
const isDev = vscode.env.appHost === 'desktop';
```

### Clipboard

```typescript
// Read clipboard
const text = await vscode.env.clipboard.readText();

// Write clipboard
await vscode.env.clipboard.writeText('Copied text');
```

### External Links

```typescript
// Open URL in browser
await vscode.env.openExternal(vscode.Uri.parse('https://example.com'));
```

---

## Common Patterns

### Debounce Events

```typescript
let timeout: NodeJS.Timeout | undefined;

vscode.workspace.onDidChangeTextDocument(e => {
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    // Handle change after 300ms of no activity
    processDocument(e.document);
  }, 300);
});
```

### Disposable Pattern

```typescript
class MyFeature implements vscode.Disposable {
  private disposables: vscode.Disposable[] = [];

  constructor() {
    this.disposables.push(
      vscode.commands.registerCommand('myExt.cmd', this.handleCommand, this)
    );
  }

  private handleCommand() { /* ... */ }

  dispose() {
    this.disposables.forEach(d => d.dispose());
  }
}

// In activate()
context.subscriptions.push(new MyFeature());
```

### Error Handling

```typescript
try {
  await riskyOperation();
} catch (error) {
  if (error instanceof vscode.FileSystemError) {
    if (error.code === 'FileNotFound') {
      vscode.window.showErrorMessage('File not found');
    }
  } else {
    vscode.window.showErrorMessage(`Error: ${error}`);
  }
}
```
