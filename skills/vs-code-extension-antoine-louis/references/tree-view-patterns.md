# Tree View Patterns

Guide for implementing tree views in VS Code extensions.

## Table of Contents

- [Basic TreeDataProvider](#basic-treedataprovider)
- [TreeItem Configuration](#treeitem-configuration)
- [Refresh Patterns](#refresh-patterns)
- [Lazy Loading](#lazy-loading)
- [Commands and Context Menus](#commands-and-context-menus)
- [Drag and Drop](#drag-and-drop)
- [Decorations](#decorations)

---

## Basic TreeDataProvider

### Minimal Implementation

```typescript
import * as vscode from 'vscode';

class MyTreeProvider implements vscode.TreeDataProvider<MyItem> {
  getTreeItem(element: MyItem): vscode.TreeItem {
    return element;
  }

  getChildren(element?: MyItem): MyItem[] {
    if (!element) {
      // Root items
      return [
        new MyItem('Item 1', vscode.TreeItemCollapsibleState.None),
        new MyItem('Item 2', vscode.TreeItemCollapsibleState.Collapsed),
      ];
    }
    // Children of element
    return [
      new MyItem('Child 1', vscode.TreeItemCollapsibleState.None),
      new MyItem('Child 2', vscode.TreeItemCollapsibleState.None),
    ];
  }
}

class MyItem extends vscode.TreeItem {
  constructor(
    public readonly label: string,
    public readonly collapsibleState: vscode.TreeItemCollapsibleState
  ) {
    super(label, collapsibleState);
  }
}

// Register in activate()
const provider = new MyTreeProvider();
vscode.window.registerTreeDataProvider('myTreeView', provider);
```

### package.json Configuration

```json
{
  "contributes": {
    "views": {
      "explorer": [
        {
          "id": "myTreeView",
          "name": "My Tree View"
        }
      ]
    }
  }
}
```

---

## TreeItem Configuration

### Full TreeItem Example

```typescript
class FileItem extends vscode.TreeItem {
  constructor(
    public readonly label: string,
    public readonly filePath: string,
    public readonly isDirectory: boolean
  ) {
    super(
      label,
      isDirectory
        ? vscode.TreeItemCollapsibleState.Collapsed
        : vscode.TreeItemCollapsibleState.None
    );

    // Tooltip on hover
    this.tooltip = filePath;

    // Description (shown after label in gray)
    this.description = isDirectory ? 'folder' : path.extname(filePath);

    // Icon
    this.iconPath = isDirectory
      ? new vscode.ThemeIcon('folder')
      : vscode.ThemeIcon.File;

    // Or custom icon
    // this.iconPath = {
    //   light: vscode.Uri.joinPath(extensionUri, 'resources', 'light', 'icon.svg'),
    //   dark: vscode.Uri.joinPath(extensionUri, 'resources', 'dark', 'icon.svg')
    // };

    // Command executed on click
    if (!isDirectory) {
      this.command = {
        command: 'vscode.open',
        title: 'Open File',
        arguments: [vscode.Uri.file(filePath)]
      };
    }

    // Resource URI (enables file decorations)
    this.resourceUri = vscode.Uri.file(filePath);

    // Context value for menu filtering
    this.contextValue = isDirectory ? 'folder' : 'file';

    // Unique ID (for getParent, reveal)
    this.id = filePath;
  }
}
```

### Theme Icons

Use built-in icons with `ThemeIcon`:

```typescript
// Common icons
new vscode.ThemeIcon('file')
new vscode.ThemeIcon('folder')
new vscode.ThemeIcon('folder-opened')
new vscode.ThemeIcon('symbol-class')
new vscode.ThemeIcon('symbol-method')
new vscode.ThemeIcon('symbol-property')
new vscode.ThemeIcon('gear')
new vscode.ThemeIcon('refresh')
new vscode.ThemeIcon('add')
new vscode.ThemeIcon('edit')
new vscode.ThemeIcon('trash')
new vscode.ThemeIcon('check')
new vscode.ThemeIcon('error')
new vscode.ThemeIcon('warning')
new vscode.ThemeIcon('info')

// With color
new vscode.ThemeIcon('circle-filled', new vscode.ThemeColor('charts.green'))
```

---

## Refresh Patterns

### Event-Based Refresh

```typescript
class MyTreeProvider implements vscode.TreeDataProvider<MyItem> {
  private _onDidChangeTreeData = new vscode.EventEmitter<MyItem | undefined | void>();
  readonly onDidChangeTreeData = this._onDidChangeTreeData.event;

  // Refresh entire tree
  refresh(): void {
    this._onDidChangeTreeData.fire();
  }

  // Refresh specific item and its children
  refreshItem(item: MyItem): void {
    this._onDidChangeTreeData.fire(item);
  }

  getTreeItem(element: MyItem): vscode.TreeItem {
    return element;
  }

  getChildren(element?: MyItem): MyItem[] {
    // Return items...
  }
}

// Usage
const provider = new MyTreeProvider();
vscode.window.registerTreeDataProvider('myTreeView', provider);

// Refresh command
vscode.commands.registerCommand('myExt.refresh', () => provider.refresh());
```

### Toolbar Refresh Button

```json
{
  "contributes": {
    "commands": [
      {
        "command": "myExt.refresh",
        "title": "Refresh",
        "icon": "$(refresh)"
      }
    ],
    "menus": {
      "view/title": [
        {
          "command": "myExt.refresh",
          "when": "view == myTreeView",
          "group": "navigation"
        }
      ]
    }
  }
}
```

---

## Lazy Loading

Load children asynchronously:

```typescript
class LazyTreeProvider implements vscode.TreeDataProvider<LazyItem> {
  getTreeItem(element: LazyItem): vscode.TreeItem {
    return element;
  }

  async getChildren(element?: LazyItem): Promise<LazyItem[]> {
    if (!element) {
      return this.getRootItems();
    }

    // Fetch children asynchronously
    const children = await this.fetchChildren(element.id);
    return children.map(c => new LazyItem(c.name, c.id, c.hasChildren));
  }

  private async fetchChildren(parentId: string): Promise<ChildData[]> {
    // API call, file system read, etc.
    const response = await fetch(`/api/items/${parentId}/children`);
    return response.json();
  }
}

class LazyItem extends vscode.TreeItem {
  constructor(
    label: string,
    public readonly id: string,
    hasChildren: boolean
  ) {
    super(
      label,
      hasChildren
        ? vscode.TreeItemCollapsibleState.Collapsed
        : vscode.TreeItemCollapsibleState.None
    );
  }
}
```

---

## Commands and Context Menus

### Register Commands

```typescript
// In activate()
context.subscriptions.push(
  vscode.commands.registerCommand('myExt.addItem', () => {
    // Add new item
    provider.addItem();
  }),

  vscode.commands.registerCommand('myExt.editItem', (item: MyItem) => {
    // Edit clicked item
    provider.editItem(item);
  }),

  vscode.commands.registerCommand('myExt.deleteItem', (item: MyItem) => {
    // Delete clicked item
    provider.deleteItem(item);
  })
);
```

### Context Menu Configuration

```json
{
  "contributes": {
    "commands": [
      { "command": "myExt.addItem", "title": "Add Item", "icon": "$(add)" },
      { "command": "myExt.editItem", "title": "Edit", "icon": "$(edit)" },
      { "command": "myExt.deleteItem", "title": "Delete", "icon": "$(trash)" }
    ],
    "menus": {
      "view/title": [
        {
          "command": "myExt.addItem",
          "when": "view == myTreeView",
          "group": "navigation"
        }
      ],
      "view/item/context": [
        {
          "command": "myExt.editItem",
          "when": "view == myTreeView && viewItem == editable",
          "group": "inline"
        },
        {
          "command": "myExt.deleteItem",
          "when": "view == myTreeView && viewItem == deletable",
          "group": "inline"
        },
        {
          "command": "myExt.editItem",
          "when": "view == myTreeView",
          "group": "1_edit"
        },
        {
          "command": "myExt.deleteItem",
          "when": "view == myTreeView",
          "group": "2_delete"
        }
      ]
    }
  }
}
```

Set `contextValue` on TreeItem to filter menus:

```typescript
class MyItem extends vscode.TreeItem {
  constructor(label: string, canEdit: boolean, canDelete: boolean) {
    super(label);

    const contexts: string[] = [];
    if (canEdit) contexts.push('editable');
    if (canDelete) contexts.push('deletable');
    this.contextValue = contexts.join(',');
  }
}
```

---

## Drag and Drop

### Enable Drag and Drop

```typescript
class DragDropProvider implements vscode.TreeDataProvider<MyItem>, vscode.TreeDragAndDropController<MyItem> {

  // Supported MIME types
  dropMimeTypes = ['application/vnd.code.tree.myTreeView'];
  dragMimeTypes = ['application/vnd.code.tree.myTreeView'];

  // Handle drag start
  handleDrag(source: readonly MyItem[], dataTransfer: vscode.DataTransfer): void {
    dataTransfer.set(
      'application/vnd.code.tree.myTreeView',
      new vscode.DataTransferItem(source.map(s => s.id))
    );
  }

  // Handle drop
  async handleDrop(
    target: MyItem | undefined,
    dataTransfer: vscode.DataTransfer,
    token: vscode.CancellationToken
  ): Promise<void> {
    const transferItem = dataTransfer.get('application/vnd.code.tree.myTreeView');
    if (!transferItem) return;

    const sourceIds: string[] = transferItem.value;
    // Move items to new location
    await this.moveItems(sourceIds, target?.id);
    this.refresh();
  }

  // ... other TreeDataProvider methods
}

// Register with drag and drop
const treeView = vscode.window.createTreeView('myTreeView', {
  treeDataProvider: provider,
  dragAndDropController: provider,
  canSelectMany: true  // Enable multi-select
});
```

---

## Decorations

Add badges and colors to tree items:

```typescript
class DecorationProvider implements vscode.FileDecorationProvider {
  private _onDidChangeFileDecorations = new vscode.EventEmitter<vscode.Uri | vscode.Uri[]>();
  readonly onDidChangeFileDecorations = this._onDidChangeFileDecorations.event;

  provideFileDecoration(uri: vscode.Uri): vscode.FileDecoration | undefined {
    // Only decorate items with our scheme
    if (uri.scheme !== 'myext') return;

    const status = this.getItemStatus(uri.path);

    if (status === 'error') {
      return {
        badge: '!',
        color: new vscode.ThemeColor('charts.red'),
        tooltip: 'Error'
      };
    }

    if (status === 'modified') {
      return {
        badge: 'M',
        color: new vscode.ThemeColor('gitDecoration.modifiedResourceForeground'),
        tooltip: 'Modified'
      };
    }

    if (status === 'new') {
      return {
        badge: '+',
        color: new vscode.ThemeColor('gitDecoration.addedResourceForeground'),
        tooltip: 'New'
      };
    }

    return undefined;
  }

  refresh(uris: vscode.Uri[]) {
    this._onDidChangeFileDecorations.fire(uris);
  }
}

// Register
context.subscriptions.push(
  vscode.window.registerFileDecorationProvider(new DecorationProvider())
);
```

Set `resourceUri` on TreeItem to enable decorations:

```typescript
class MyItem extends vscode.TreeItem {
  constructor(label: string, id: string) {
    super(label);
    // Use custom scheme to identify our items
    this.resourceUri = vscode.Uri.parse(`myext:/${id}`);
  }
}
```

---

## TreeView API

Get more control with `createTreeView`:

```typescript
const treeView = vscode.window.createTreeView('myTreeView', {
  treeDataProvider: provider,
  showCollapseAll: true,       // Add "Collapse All" button
  canSelectMany: true          // Enable multi-select
});

// Reveal item
treeView.reveal(item, { select: true, focus: true, expand: true });

// Get selection
treeView.selection; // readonly MyItem[]

// Listen to selection changes
treeView.onDidChangeSelection(e => {
  console.log('Selected:', e.selection);
});

// Listen to visibility changes
treeView.onDidChangeVisibility(e => {
  if (e.visible) {
    // Tree view became visible
  }
});

// Set title
treeView.title = 'My Items (5)';

// Set description
treeView.description = 'filtered';

// Set message (shown when tree is empty)
treeView.message = 'No items found. Click + to add.';

// Dispose
context.subscriptions.push(treeView);
```

### getParent for Reveal

Implement `getParent` to enable `reveal()`:

```typescript
class MyTreeProvider implements vscode.TreeDataProvider<MyItem> {
  private itemMap = new Map<string, MyItem>();
  private parentMap = new Map<string, MyItem>();

  getParent(element: MyItem): MyItem | undefined {
    return this.parentMap.get(element.id);
  }

  getChildren(element?: MyItem): MyItem[] {
    const children = this.fetchChildren(element?.id);

    // Track parent relationships
    for (const child of children) {
      this.itemMap.set(child.id, child);
      if (element) {
        this.parentMap.set(child.id, element);
      }
    }

    return children;
  }
}
```
