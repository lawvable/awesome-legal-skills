import * as vscode from 'vscode';

export class JsonEditorProvider implements vscode.CustomTextEditorProvider {
  public static readonly viewType = 'myExtension.jsonEditor';

  public static register(context: vscode.ExtensionContext): vscode.Disposable {
    return vscode.window.registerCustomEditorProvider(
      JsonEditorProvider.viewType,
      new JsonEditorProvider(context),
      {
        webviewOptions: { retainContextWhenHidden: true },
        supportsMultipleEditorsPerDocument: false
      }
    );
  }

  constructor(private readonly context: vscode.ExtensionContext) {}

  async resolveCustomTextEditor(
    document: vscode.TextDocument,
    webviewPanel: vscode.WebviewPanel,
    _token: vscode.CancellationToken
  ): Promise<void> {
    webviewPanel.webview.options = {
      enableScripts: true,
      localResourceRoots: [this.context.extensionUri]
    };

    webviewPanel.webview.html = this.getHtmlForWebview(webviewPanel.webview);

    // Sync document → webview
    const updateWebview = () => {
      try {
        const data = JSON.parse(document.getText());
        webviewPanel.webview.postMessage({
          type: 'update',
          data
        });
      } catch {
        webviewPanel.webview.postMessage({
          type: 'error',
          message: 'Invalid JSON'
        });
      }
    };

    // Listen for document changes
    const changeDocumentSubscription = vscode.workspace.onDidChangeTextDocument(e => {
      if (e.document.uri.toString() === document.uri.toString()) {
        updateWebview();
      }
    });

    // Listen for webview messages
    webviewPanel.webview.onDidReceiveMessage(message => {
      switch (message.type) {
        case 'edit':
          this.applyEdit(document, message.data);
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

  private applyEdit(document: vscode.TextDocument, data: any) {
    const edit = new vscode.WorkspaceEdit();
    const newContent = JSON.stringify(data, null, 2);

    edit.replace(
      document.uri,
      new vscode.Range(0, 0, document.lineCount, 0),
      newContent
    );

    vscode.workspace.applyEdit(edit);
  }

  private getHtmlForWebview(webview: vscode.Webview): string {
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
  ">
  <title>JSON Editor</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      background-color: var(--vscode-editor-background);
      color: var(--vscode-editor-foreground);
      font-family: var(--vscode-font-family);
      font-size: var(--vscode-font-size);
      padding: 20px;
    }
    h1 {
      margin-bottom: 20px;
      font-size: 18px;
    }
    .error {
      color: var(--vscode-errorForeground);
      padding: 10px;
      margin-bottom: 20px;
      background: var(--vscode-inputValidation-errorBackground);
      border: 1px solid var(--vscode-inputValidation-errorBorder);
      border-radius: 4px;
    }
    .form-group {
      margin-bottom: 16px;
    }
    label {
      display: block;
      margin-bottom: 4px;
      font-weight: 500;
    }
    input, textarea {
      width: 100%;
      padding: 8px;
      background-color: var(--vscode-input-background);
      color: var(--vscode-input-foreground);
      border: 1px solid var(--vscode-input-border);
      border-radius: 4px;
    }
    input:focus, textarea:focus {
      outline: 1px solid var(--vscode-focusBorder);
    }
    textarea {
      min-height: 100px;
      resize: vertical;
    }
    .field-row {
      display: flex;
      gap: 16px;
      margin-bottom: 16px;
    }
    .field-row > div {
      flex: 1;
    }
  </style>
</head>
<body>
  <h1>JSON Visual Editor</h1>
  <div id="error" class="error" style="display: none;"></div>
  <div id="form"></div>

  <script nonce="${nonce}">
    const vscode = acquireVsCodeApi();
    let currentData = {};

    window.addEventListener('message', event => {
      const message = event.data;
      switch (message.type) {
        case 'update':
          currentData = message.data;
          renderForm(currentData);
          document.getElementById('error').style.display = 'none';
          break;
        case 'error':
          document.getElementById('error').textContent = message.message;
          document.getElementById('error').style.display = 'block';
          break;
      }
    });

    function renderForm(data) {
      const form = document.getElementById('form');
      form.innerHTML = '';

      for (const [key, value] of Object.entries(data)) {
        const group = document.createElement('div');
        group.className = 'form-group';

        const label = document.createElement('label');
        label.textContent = key;
        label.htmlFor = 'field-' + key;
        group.appendChild(label);

        let input;
        if (typeof value === 'object' && value !== null) {
          input = document.createElement('textarea');
          input.value = JSON.stringify(value, null, 2);
        } else if (typeof value === 'boolean') {
          input = document.createElement('input');
          input.type = 'checkbox';
          input.checked = value;
          input.style.width = 'auto';
        } else if (typeof value === 'number') {
          input = document.createElement('input');
          input.type = 'number';
          input.value = value;
        } else {
          input = document.createElement('input');
          input.type = 'text';
          input.value = value || '';
        }

        input.id = 'field-' + key;
        input.addEventListener('change', () => handleChange(key, input));
        group.appendChild(input);

        form.appendChild(group);
      }
    }

    function handleChange(key, input) {
      let value;
      if (input.type === 'checkbox') {
        value = input.checked;
      } else if (input.type === 'number') {
        value = parseFloat(input.value);
      } else if (input.tagName === 'TEXTAREA') {
        try {
          value = JSON.parse(input.value);
        } catch {
          value = input.value;
        }
      } else {
        value = input.value;
      }

      currentData[key] = value;

      vscode.postMessage({
        type: 'edit',
        data: currentData
      });
    }
  </script>
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
