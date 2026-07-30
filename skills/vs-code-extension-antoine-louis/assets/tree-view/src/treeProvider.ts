import * as vscode from 'vscode';

interface ItemData {
  id: string;
  name: string;
  children?: ItemData[];
}

export class MyTreeProvider implements vscode.TreeDataProvider<MyTreeItem> {
  private _onDidChangeTreeData = new vscode.EventEmitter<MyTreeItem | undefined | void>();
  readonly onDidChangeTreeData = this._onDidChangeTreeData.event;

  private items: ItemData[] = [
    {
      id: '1',
      name: 'Category A',
      children: [
        { id: '1-1', name: 'Item A1' },
        { id: '1-2', name: 'Item A2' }
      ]
    },
    {
      id: '2',
      name: 'Category B',
      children: [
        { id: '2-1', name: 'Item B1' }
      ]
    },
    {
      id: '3',
      name: 'Item C'
    }
  ];

  refresh(): void {
    this._onDidChangeTreeData.fire();
  }

  addItem(name: string): void {
    const id = Date.now().toString();
    this.items.push({ id, name });
    this.refresh();
  }

  deleteItem(item: MyTreeItem): void {
    this.items = this.removeItemById(this.items, item.id);
    this.refresh();
  }

  private removeItemById(items: ItemData[], id: string): ItemData[] {
    return items
      .filter(item => item.id !== id)
      .map(item => ({
        ...item,
        children: item.children ? this.removeItemById(item.children, id) : undefined
      }));
  }

  getTreeItem(element: MyTreeItem): vscode.TreeItem {
    return element;
  }

  getChildren(element?: MyTreeItem): MyTreeItem[] {
    if (!element) {
      // Root items
      return this.items.map(item => this.createTreeItem(item));
    }

    // Children of element
    const itemData = this.findItemById(this.items, element.id);
    if (itemData?.children) {
      return itemData.children.map(child => this.createTreeItem(child));
    }

    return [];
  }

  getParent(element: MyTreeItem): MyTreeItem | undefined {
    const parent = this.findParentById(this.items, element.id);
    return parent ? this.createTreeItem(parent) : undefined;
  }

  private createTreeItem(data: ItemData): MyTreeItem {
    const hasChildren = data.children && data.children.length > 0;
    return new MyTreeItem(
      data.id,
      data.name,
      hasChildren
        ? vscode.TreeItemCollapsibleState.Collapsed
        : vscode.TreeItemCollapsibleState.None
    );
  }

  private findItemById(items: ItemData[], id: string): ItemData | undefined {
    for (const item of items) {
      if (item.id === id) return item;
      if (item.children) {
        const found = this.findItemById(item.children, id);
        if (found) return found;
      }
    }
    return undefined;
  }

  private findParentById(items: ItemData[], id: string, parent?: ItemData): ItemData | undefined {
    for (const item of items) {
      if (item.id === id) return parent;
      if (item.children) {
        const found = this.findParentById(item.children, id, item);
        if (found) return found;
      }
    }
    return undefined;
  }
}

export class MyTreeItem extends vscode.TreeItem {
  constructor(
    public readonly id: string,
    public readonly label: string,
    public readonly collapsibleState: vscode.TreeItemCollapsibleState
  ) {
    super(label, collapsibleState);

    this.tooltip = `${this.label} (${this.id})`;

    // Set icon based on whether it has children
    if (collapsibleState !== vscode.TreeItemCollapsibleState.None) {
      this.iconPath = new vscode.ThemeIcon('folder');
    } else {
      this.iconPath = new vscode.ThemeIcon('file');
    }

    // Context value for menu filtering
    this.contextValue = 'myItem';
  }
}
