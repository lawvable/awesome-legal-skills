import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  console.log('Extension "my-extension" is now active');

  const disposable = vscode.commands.registerCommand(
    'myExtension.helloWorld',
    () => {
      vscode.window.showInformationMessage('Hello World from My Extension!');
    }
  );

  context.subscriptions.push(disposable);
}

export function deactivate() {}
