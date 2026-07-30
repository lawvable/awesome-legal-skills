# Custom Editor Patterns

Guide for implementing custom editors that replace VS Code's default file editors.

## Table of Contents

- [Overview](#overview)
- [CustomTextEditorProvider](#customtexteditorprovider)
- [CustomEditorProvider](#customeditorprovider)
- [Document Synchronization](#document-synchronization)
- [Undo/Redo Support](#undoredo-support)
- [Save Handling](#save-handling)

---

## Overview

Custom editors let you provide a custom UI for editing specific file types.

**Two types:**

| Type | Use Case | Document Model |
|------|----------|----------------|
| `CustomTextEditorProvider` | Text-based files (JSON, XML, YAML) | Uses VS Code's `TextDocument` |
| `CustomEditorProvider` | Binary files (images, custom formats) | Your own document model |

**Choose `CustomTextEditorProvider` when:**
- File is text-based
- Want VS Code's built-in dirty tracking
- Want Search/Replace to work
- Want other extensions to access the document

**Choose `CustomEditorProvider` when:**
- File is binary
- Need full control over document model
- Default text model doesn't fit

---

## CustomTextEditorProvider

Best for text files with a custom visual editor (JSON editors, diagram tools, etc.).

### Implementation

```typescript
import * as vscode from 'vscode';

class MyTextEditorProvider implements vscode.CustomTextEditorProvider {
  public static readonly viewType = 'myExt.myEditor';

  constructor(private readonly context: vscode.ExtensionContext) {}

  async resolveCustomTextEditor(
    document: vscode.TextDocument,
    webviewPanel: vscode.WebviewPanel,
    _token: vscode.CancellationToken
  ): Promise<void> {
    // Setup webview
    webviewPanel.webview.options = {
      enableScripts: true,
      localResourceRoots: [this.context.extensionUri]
    };

    // Set initial HTML
    webviewPanel.webview.html = this.getHtmlForWebview(webviewPanel.webview);

    // Sync document → webview
    const updateWebview = () => {
      webviewPanel.webview.postMessage({
        type: 'update',
        content: document.getText()
      });
    };

    // Listen for document changes (from other editors, search/replace, etc.)
    const changeDocumentSubscription = vscode.workspace.onDidChangeTextDocument(e => {
      if (e.document.uri.toString() === document.uri.toString()) {
        updateWebview();
      }
    });

    // Listen for webview messages
    webviewPanel.webview.onDidReceiveMessage(message => {
      switch (message.type) {
        case 'edit':
          this.applyEdit(document, message.content);
          break;
      }
    });

    // Cleanup
    webviewPanel.onDidDispose(() => {
      changeDocumentSubscription.dispose();
    });

    // Initial sync
    updateWebview();
  }

  private applyEdit(document: vscode.TextDocument, newContent: string) {
    const edit = new vscode.WorkspaceEdit();
    edit.replace(
      document.uri,
      new vscode.Range(0, 0, document.lineCount, 0),
      newContent
    );
    vscode.workspace.applyEdit(edit);
  }

  private getHtmlForWebview(webview: vscode.Webview): string {
    const scriptUri = webview.asWebviewUri(
      vscode.Uri.joinPath(this.context.extensionUri, 'dist', 'editor.js')
    );

    const nonce = getNonce();

    return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Content-Security-Policy" content="
    default-src 'none';
    script-src 'nonce-${nonce}';
    style-src ${webview.cspSource} 'unsafe-inline';
  ">
  <title>My Editor</title>
</head>
<body>
  <div id="editor"></div>
  <script nonce="${nonce}" src="${scriptUri}"></script>
</body>
</html>`;
  }
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

### Registration

```typescript
// In activate()
context.subscriptions.push(
  vscode.window.registerCustomEditorProvider(
    MyTextEditorProvider.viewType,
    new MyTextEditorProvider(context),
    {
      webviewOptions: { retainContextWhenHidden: true },
      supportsMultipleEditorsPerDocument: false
    }
  )
);
```

### package.json

```json
{
  "contributes": {
    "customEditors": [
      {
        "viewType": "myExt.myEditor",
        "displayName": "My Editor",
        "selector": [
          { "filenamePattern": "*.myext" }
        ],
        "priority": "default"
      }
    ]
  }
}
```

---

## CustomEditorProvider

For binary files or when you need full control over the document model.

### Document Model

```typescript
class MyDocument implements vscode.CustomDocument {
  uri: vscode.Uri;
  private _data: Uint8Array;
  private _edits: Edit[] = [];
  private _savedEdits: Edit[] = [];

  private readonly _onDidDispose = new vscode.EventEmitter<void>();
  public readonly onDidDispose = this._onDidDispose.event;

  private readonly _onDidChange = new vscode.EventEmitter<void>();
  public readonly onDidChange = this._onDidChange.event;

  constructor(uri: vscode.Uri, data: Uint8Array) {
    this.uri = uri;
    this._data = data;
  }

  get data(): Uint8Array {
    return this._data;
  }

  applyEdit(edit: Edit) {
    this._edits.push(edit);
    this._data = applyEditToData(this._data, edit);
    this._onDidChange.fire();
  }

  get isDirty(): boolean {
    return !arraysEqual(this._edits, this._savedEdits);
  }

  async save(): Promise<void> {
    await vscode.workspace.fs.writeFile(this.uri, this._data);
    this._savedEdits = [...this._edits];
  }

  async saveAs(targetUri: vscode.Uri): Promise<void> {
    await vscode.workspace.fs.writeFile(targetUri, this._data);
    this._savedEdits = [...this._edits];
  }

  async revert(): Promise<void> {
    const data = await vscode.workspace.fs.readFile(this.uri);
    this._data = data;
    this._edits = [...this._savedEdits];
    this._onDidChange.fire();
  }

  dispose(): void {
    this._onDidDispose.fire();
    this._onDidDispose.dispose();
    this._onDidChange.dispose();
  }
}
```

### Provider Implementation

```typescript
class MyBinaryEditorProvider implements vscode.CustomEditorProvider<MyDocument> {
  public static readonly viewType = 'myExt.binaryEditor';

  private readonly _onDidChangeCustomDocument = new vscode.EventEmitter<vscode.CustomDocumentEditEvent<MyDocument>>();
  public readonly onDidChangeCustomDocument = this._onDidChangeCustomDocument.event;

  constructor(private readonly context: vscode.ExtensionContext) {}

  // Open document
  async openCustomDocument(
    uri: vscode.Uri,
    openContext: vscode.CustomDocumentOpenContext,
    _token: vscode.CancellationToken
  ): Promise<MyDocument> {
    const data = openContext.backupId
      ? await vscode.workspace.fs.readFile(vscode.Uri.parse(openContext.backupId))
      : await vscode.workspace.fs.readFile(uri);

    return new MyDocument(uri, data);
  }

  // Create webview for document
  async resolveCustomEditor(
    document: MyDocument,
    webviewPanel: vscode.WebviewPanel,
    _token: vscode.CancellationToken
  ): Promise<void> {
    webviewPanel.webview.options = { enableScripts: true };
    webviewPanel.webview.html = this.getHtml(webviewPanel.webview, document);

    // Sync document changes to webview
    const changeSubscription = document.onDidChange(() => {
      webviewPanel.webview.postMessage({
        type: 'update',
        data: Array.from(document.data)
      });
    });

    // Handle webview edits
    webviewPanel.webview.onDidReceiveMessage(message => {
      if (message.type === 'edit') {
        const edit: Edit = message.edit;
        document.applyEdit(edit);

        // Fire change event for VS Code
        this._onDidChangeCustomDocument.fire({
          document,
          undo: () => document.undo(edit),
          redo: () => document.redo(edit)
        });
      }
    });

    webviewPanel.onDidDispose(() => {
      changeSubscription.dispose();
    });
  }

  // Save
  async saveCustomDocument(document: MyDocument, _token: vscode.CancellationToken): Promise<void> {
    await document.save();
  }

  // Save As
  async saveCustomDocumentAs(
    document: MyDocument,
    destination: vscode.Uri,
    _token: vscode.CancellationToken
  ): Promise<void> {
    await document.saveAs(destination);
  }

  // Revert
  async revertCustomDocument(document: MyDocument, _token: vscode.CancellationToken): Promise<void> {
    await document.revert();
  }

  // Backup (for hot exit)
  async backupCustomDocument(
    document: MyDocument,
    context: vscode.CustomDocumentBackupContext,
    _token: vscode.CancellationToken
  ): Promise<vscode.CustomDocumentBackup> {
    await vscode.workspace.fs.writeFile(context.destination, document.data);
    return {
      id: context.destination.toString(),
      delete: () => vscode.workspace.fs.delete(context.destination)
    };
  }
}
```

---

## Document Synchronization

### Handling External Changes

```typescript
// In resolveCustomTextEditor
const fileWatcher = vscode.workspace.createFileSystemWatcher(document.uri.fsPath);

fileWatcher.onDidChange(() => {
  // File changed externally, ask user
  vscode.window.showInformationMessage(
    'File changed on disk. Reload?',
    'Reload', 'Ignore'
  ).then(choice => {
    if (choice === 'Reload') {
      // Trigger document reload
      vscode.commands.executeCommand('workbench.action.files.revert');
    }
  });
});

webviewPanel.onDidDispose(() => {
  fileWatcher.dispose();
});
```

### Debouncing Updates

```typescript
let updateTimeout: NodeJS.Timeout | undefined;

function scheduleUpdate() {
  clearTimeout(updateTimeout);
  updateTimeout = setTimeout(() => {
    webviewPanel.webview.postMessage({
      type: 'update',
      content: document.getText()
    });
  }, 100);
}

vscode.workspace.onDidChangeTextDocument(e => {
  if (e.document.uri.toString() === document.uri.toString()) {
    scheduleUpdate();
  }
});
```

---

## Undo/Redo Support

### For CustomTextEditorProvider

VS Code handles undo/redo automatically via `TextDocument`.

### For CustomEditorProvider

Implement edit tracking:

```typescript
interface Edit {
  type: string;
  data: any;
  inverse: Edit; // The edit that undoes this one
}

class MyDocument {
  private edits: Edit[] = [];
  private undoneEdits: Edit[] = [];

  applyEdit(edit: Edit) {
    this.edits.push(edit);
    this.undoneEdits = []; // Clear redo stack
    this.applyToData(edit);
  }

  undo(edit: Edit) {
    const index = this.edits.indexOf(edit);
    if (index !== -1) {
      this.edits.splice(index, 1);
      this.undoneEdits.push(edit);
      this.applyToData(edit.inverse);
    }
  }

  redo(edit: Edit) {
    const index = this.undoneEdits.indexOf(edit);
    if (index !== -1) {
      this.undoneEdits.splice(index, 1);
      this.edits.push(edit);
      this.applyToData(edit);
    }
  }
}

// In provider
webviewPanel.webview.onDidReceiveMessage(message => {
  if (message.type === 'edit') {
    document.applyEdit(message.edit);

    this._onDidChangeCustomDocument.fire({
      document,
      undo: async () => document.undo(message.edit),
      redo: async () => document.redo(message.edit)
    });
  }
});
```

---

## Save Handling

### Auto-Save Support

CustomTextEditorProvider gets auto-save automatically.

For CustomEditorProvider, implement properly:

```typescript
async saveCustomDocument(
  document: MyDocument,
  cancellation: vscode.CancellationToken
): Promise<void> {
  // Check for cancellation during long saves
  if (cancellation.isCancellationRequested) {
    throw new vscode.CancellationError();
  }

  await document.save();
}
```

### Dirty Indicator

For CustomEditorProvider, fire `onDidChangeCustomDocument` to mark dirty:

```typescript
// Document is dirty when this fires
this._onDidChangeCustomDocument.fire({
  document,
  undo: async () => { /* ... */ },
  redo: async () => { /* ... */ }
});

// Or for non-undoable changes
this._onDidChangeCustomDocument.fire({
  document
});
```

### Prompt Save on Close

VS Code automatically prompts to save dirty documents.

For CustomEditorProvider, `isDirty` is determined by whether any edits exist since the last save (tracked internally by your document model).

---

## Webview Editor Script

```typescript
// editor.ts (webview code)
declare function acquireVsCodeApi(): {
  postMessage(message: any): void;
  getState(): any;
  setState(state: any): void;
};

const vscode = acquireVsCodeApi();

let currentContent: string;

// Receive updates from extension
window.addEventListener('message', event => {
  const message = event.data;
  switch (message.type) {
    case 'update':
      currentContent = message.content;
      renderContent(currentContent);
      break;
  }
});

// Send edit to extension
function makeEdit(newContent: string) {
  vscode.postMessage({
    type: 'edit',
    content: newContent
  });
}

// Render content in editor
function renderContent(content: string) {
  // Update your editor UI
}

// Example: JSON editor with form
function handleFormChange(field: string, value: any) {
  try {
    const data = JSON.parse(currentContent);
    data[field] = value;
    makeEdit(JSON.stringify(data, null, 2));
  } catch (e) {
    console.error('Invalid JSON');
  }
}
```
