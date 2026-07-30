import * as vscode from 'vscode';
import { JsonEditorProvider } from './editorProvider';

export function activate(context: vscode.ExtensionContext) {
  console.log('Extension "my-custom-editor-extension" is now active');

  context.subscriptions.push(
    JsonEditorProvider.register(context)
  );
}

export function deactivate() {}
