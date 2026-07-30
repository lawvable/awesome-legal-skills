import * as vscode from 'vscode';
import { MyTreeProvider, MyTreeItem } from './treeProvider';

export function activate(context: vscode.ExtensionContext) {
  console.log('Extension "my-tree-view-extension" is now active');

  const treeProvider = new MyTreeProvider();

  // Register tree data provider
  const treeView = vscode.window.createTreeView('myTreeView', {
    treeDataProvider: treeProvider,
    showCollapseAll: true
  });

  // Register commands
  context.subscriptions.push(
    treeView,

    vscode.commands.registerCommand('myExtension.refresh', () => {
      treeProvider.refresh();
    }),

    vscode.commands.registerCommand('myExtension.addItem', async () => {
      const name = await vscode.window.showInputBox({
        prompt: 'Enter item name',
        placeHolder: 'New Item'
      });

      if (name) {
        treeProvider.addItem(name);
        vscode.window.showInformationMessage(`Added: ${name}`);
      }
    }),

    vscode.commands.registerCommand('myExtension.deleteItem', (item: MyTreeItem) => {
      treeProvider.deleteItem(item);
      vscode.window.showInformationMessage(`Deleted: ${item.label}`);
    })
  );
}

export function deactivate() {}
