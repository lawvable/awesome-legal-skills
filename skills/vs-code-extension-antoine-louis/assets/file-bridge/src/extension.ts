import * as vscode from 'vscode';
import { FileBridge } from './fileBridge';

let bridge: FileBridge | undefined;
let statusBarItem: vscode.StatusBarItem;

export async function activate(context: vscode.ExtensionContext) {
  console.log('Extension "my-file-bridge-extension" is now active');

  // Create status bar item
  statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
  statusBarItem.command = 'myExtension.showBridgeStatus';
  context.subscriptions.push(statusBarItem);

  // Register commands
  context.subscriptions.push(
    vscode.commands.registerCommand('myExtension.initBridge', async () => {
      await initializeBridge(context);
    }),

    vscode.commands.registerCommand('myExtension.showBridgeStatus', () => {
      if (bridge) {
        vscode.window.showInformationMessage('AI Bridge is active and listening for commands.');
      } else {
        vscode.window.showWarningMessage('AI Bridge is not initialized. Run "Initialize AI Bridge" command.');
      }
    })
  );

  // Auto-initialize if bridge directory exists
  const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
  if (workspaceRoot) {
    const bridgeDir = vscode.Uri.joinPath(
      vscode.Uri.file(workspaceRoot),
      '.vscode',
      'ai-bridge'
    );

    try {
      await vscode.workspace.fs.stat(bridgeDir);
      await initializeBridge(context);
    } catch {
      // Bridge directory doesn't exist, wait for manual init
    }
  }
}

async function initializeBridge(context: vscode.ExtensionContext) {
  const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
  if (!workspaceRoot) {
    vscode.window.showErrorMessage('No workspace folder open.');
    return;
  }

  if (bridge) {
    bridge.stop();
  }

  bridge = new FileBridge(workspaceRoot);

  // Register command handlers
  registerHandlers(bridge, context);

  await bridge.start();

  statusBarItem.text = '$(plug) AI Bridge';
  statusBarItem.tooltip = 'AI Bridge is active';
  statusBarItem.show();

  vscode.window.showInformationMessage('AI Bridge initialized and listening for commands.');
}

function registerHandlers(bridge: FileBridge, context: vscode.ExtensionContext) {
  // Handler: Show message
  bridge.registerHandler('showMessage', async (params) => {
    const type = params.type || 'info';
    const message = params.message;

    switch (type) {
      case 'error':
        vscode.window.showErrorMessage(message);
        break;
      case 'warning':
        vscode.window.showWarningMessage(message);
        break;
      default:
        vscode.window.showInformationMessage(message);
    }

    return { shown: true };
  });

  // Handler: Read file
  bridge.registerHandler('readFile', async (params) => {
    const uri = vscode.Uri.file(params.filePath);
    const content = await vscode.workspace.fs.readFile(uri);
    return { content: new TextDecoder().decode(content) };
  });

  // Handler: Write file
  bridge.registerHandler('writeFile', async (params) => {
    const uri = vscode.Uri.file(params.filePath);
    const content = new TextEncoder().encode(params.content);
    await vscode.workspace.fs.writeFile(uri, content);
    return { written: true };
  });

  // Handler: Get open files
  bridge.registerHandler('getOpenFiles', async () => {
    const editors = vscode.window.visibleTextEditors;
    return {
      files: editors.map(e => ({
        path: e.document.uri.fsPath,
        languageId: e.document.languageId,
        isDirty: e.document.isDirty
      }))
    };
  });

  // Handler: Execute VS Code command
  bridge.registerHandler('executeCommand', async (params) => {
    // Whitelist of allowed commands for security
    const allowedCommands = [
      'editor.action.formatDocument',
      'workbench.action.files.save',
      'workbench.action.files.saveAll'
    ];

    if (!allowedCommands.includes(params.command)) {
      throw new Error(`Command not allowed: ${params.command}`);
    }

    const result = await vscode.commands.executeCommand(params.command, ...(params.args || []));
    return { result };
  });

  // Handler: Get workspace info
  bridge.registerHandler('getWorkspaceInfo', async () => {
    const folders = vscode.workspace.workspaceFolders || [];
    return {
      folders: folders.map(f => ({
        name: f.name,
        path: f.uri.fsPath
      })),
      name: vscode.workspace.name
    };
  });

  // Handler: Show input box
  bridge.registerHandler('showInputBox', async (params) => {
    const result = await vscode.window.showInputBox({
      prompt: params.prompt,
      placeHolder: params.placeHolder,
      value: params.value
    });
    return { value: result };
  });

  // Handler: Show quick pick
  bridge.registerHandler('showQuickPick', async (params) => {
    const result = await vscode.window.showQuickPick(params.items, {
      placeHolder: params.placeHolder,
      canPickMany: params.canPickMany
    });
    return { selected: result };
  });
}

export function deactivate() {
  if (bridge) {
    bridge.stop();
    bridge = undefined;
  }
}
