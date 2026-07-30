# AI Agent Integration

Patterns for integrating VS Code extensions with AI agents like Claude Code.

## Table of Contents

- [Overview](#overview)
- [File-Bridge IPC Pattern](#file-bridge-ipc-pattern)
- [Message Format](#message-format)
- [Implementation](#implementation)
- [Security Considerations](#security-considerations)
- [Alternative Approaches](#alternative-approaches)

---

## Overview

VS Code extensions don't natively communicate with AI agents running in the terminal. The **file-bridge pattern** enables this communication through watched files.

**How it works:**
1. Extension watches a commands directory for new JSON files
2. AI agent writes command files to trigger extension actions
3. Extension processes commands and writes results to a response file
4. AI agent reads the response

**Benefits:**
- No API keys needed in the extension
- Uses the agent's existing subscription
- Works with any AI agent (Claude Code, Codex, Gemini CLI)
- Simple, language-agnostic protocol

---

## File-Bridge IPC Pattern

### Directory Structure

```
.vscode/
└── ai-bridge/
    ├── commands/          # Agent writes here
    │   └── cmd-{timestamp}.json
    └── responses/         # Extension writes here
        └── resp-{timestamp}.json
```

### Communication Flow

```
┌─────────────┐                      ┌─────────────┐
│  AI Agent   │                      │  Extension  │
│(Claude Code)│                      │  (VS Code)  │
└──────┬──────┘                      └──────┬──────┘
       │                                    │
       │  1. Write command JSON             │
       │ ─────────────────────────────────> │
       │    commands/cmd-123.json           │
       │                                    │
       │                     2. Process     │
       │                        command     │
       │                                    │
       │  3. Read response JSON             │
       │ <───────────────────────────────── │
       │    responses/resp-123.json         │
       │                                    │
       │  4. Delete command file            │
       │ ─────────────────────────────────> │
       │                                    │
```

---

## Message Format

### Command File (Agent → Extension)

```json
{
  "id": "cmd-1706789012345",
  "action": "extractText",
  "params": {
    "filePath": "/path/to/document.docx",
    "options": {
      "includeMetadata": true
    }
  },
  "timestamp": 1706789012345
}
```

### Response File (Extension → Agent)

```json
{
  "id": "cmd-1706789012345",
  "status": "success",
  "result": {
    "text": "Document content here...",
    "metadata": {
      "author": "John Doe",
      "created": "2024-01-15"
    }
  },
  "timestamp": 1706789012567
}
```

### Error Response

```json
{
  "id": "cmd-1706789012345",
  "status": "error",
  "error": {
    "code": "FILE_NOT_FOUND",
    "message": "The specified file does not exist"
  },
  "timestamp": 1706789012567
}
```

---

## Implementation

### Extension Side

```typescript
import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';

interface Command {
  id: string;
  action: string;
  params: Record<string, any>;
  timestamp: number;
}

interface Response {
  id: string;
  status: 'success' | 'error';
  result?: any;
  error?: { code: string; message: string };
  timestamp: number;
}

export class FileBridge {
  private commandsDir: string;
  private responsesDir: string;
  private watcher: fs.FSWatcher | null = null;
  private handlers: Map<string, (params: any) => Promise<any>> = new Map();

  constructor(private workspaceRoot: string) {
    this.commandsDir = path.join(workspaceRoot, '.vscode', 'ai-bridge', 'commands');
    this.responsesDir = path.join(workspaceRoot, '.vscode', 'ai-bridge', 'responses');
  }

  async start() {
    // Ensure directories exist
    await fs.promises.mkdir(this.commandsDir, { recursive: true });
    await fs.promises.mkdir(this.responsesDir, { recursive: true });

    // Process existing commands
    await this.processExistingCommands();

    // Watch for new commands
    this.watcher = fs.watch(this.commandsDir, async (eventType, filename) => {
      if (eventType === 'rename' && filename?.endsWith('.json')) {
        const filePath = path.join(this.commandsDir, filename);
        // Small delay to ensure file is fully written
        setTimeout(() => this.processCommand(filePath), 50);
      }
    });
  }

  stop() {
    this.watcher?.close();
    this.watcher = null;
  }

  registerHandler(action: string, handler: (params: any) => Promise<any>) {
    this.handlers.set(action, handler);
  }

  private async processExistingCommands() {
    try {
      const files = await fs.promises.readdir(this.commandsDir);
      for (const file of files.filter(f => f.endsWith('.json'))) {
        await this.processCommand(path.join(this.commandsDir, file));
      }
    } catch (e) {
      // Directory might not exist yet
    }
  }

  private async processCommand(filePath: string) {
    try {
      // Check if file exists (might have been processed already)
      if (!fs.existsSync(filePath)) return;

      const content = await fs.promises.readFile(filePath, 'utf-8');
      const command: Command = JSON.parse(content);

      // Find handler
      const handler = this.handlers.get(command.action);
      let response: Response;

      if (!handler) {
        response = {
          id: command.id,
          status: 'error',
          error: {
            code: 'UNKNOWN_ACTION',
            message: `No handler for action: ${command.action}`
          },
          timestamp: Date.now()
        };
      } else {
        try {
          const result = await handler(command.params);
          response = {
            id: command.id,
            status: 'success',
            result,
            timestamp: Date.now()
          };
        } catch (e: any) {
          response = {
            id: command.id,
            status: 'error',
            error: {
              code: 'HANDLER_ERROR',
              message: e.message || String(e)
            },
            timestamp: Date.now()
          };
        }
      }

      // Write response
      const responsePath = path.join(this.responsesDir, `resp-${command.id}.json`);
      await fs.promises.writeFile(responsePath, JSON.stringify(response, null, 2));

      // Delete command file
      await fs.promises.unlink(filePath);

    } catch (e) {
      console.error('Error processing command:', e);
    }
  }
}

// Usage in extension
export function activate(context: vscode.ExtensionContext) {
  const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
  if (!workspaceRoot) return;

  const bridge = new FileBridge(workspaceRoot);

  // Register handlers
  bridge.registerHandler('extractText', async (params) => {
    const content = await vscode.workspace.fs.readFile(
      vscode.Uri.file(params.filePath)
    );
    return { text: new TextDecoder().decode(content) };
  });

  bridge.registerHandler('showMessage', async (params) => {
    await vscode.window.showInformationMessage(params.message);
    return { shown: true };
  });

  bridge.registerHandler('getOpenFiles', async () => {
    const editors = vscode.window.visibleTextEditors;
    return {
      files: editors.map(e => e.document.uri.fsPath)
    };
  });

  bridge.start();
  context.subscriptions.push({ dispose: () => bridge.stop() });
}
```

### Agent Side (Shell)

For AI agents using bash (Claude Code, etc.), use `until` to poll for the response:

```bash
# Write command and wait for response
BRIDGE_DIR=".vscode/ai-bridge"
CMD_ID="cmd-$(date +%s%3N)"

# Write command
echo '{
  "id": "'$CMD_ID'",
  "action": "extractText",
  "params": { "filePath": "/path/to/doc.docx" },
  "timestamp": '$(date +%s%3N)'
}' > "$BRIDGE_DIR/commands/$CMD_ID.json"

# Poll for response (fast commands return instantly, slow ones wait)
RESP_FILE="$BRIDGE_DIR/responses/resp-$CMD_ID.json"
until grep -q '"status"' "$RESP_FILE" 2>/dev/null; do
  sleep 0.1
done

# Read and display response
cat "$RESP_FILE"
rm "$RESP_FILE"
```

**One-liner version:**

```bash
echo '{"id":"cmd-1","action":"showMessage","params":{"message":"Hello"}}' > .vscode/ai-bridge/commands/cmd-1.json && until grep -q '"status"' .vscode/ai-bridge/responses/resp-cmd-1.json 2>/dev/null; do sleep 0.1; done && cat .vscode/ai-bridge/responses/resp-cmd-1.json
```

### Agent Side (Python)

```python
# For AI agents to use when interacting with the extension
import json
import time
from pathlib import Path

def send_command(workspace: str, action: str, params: dict, timeout: float = 30.0) -> dict:
    """Send a command to the VS Code extension and wait for response."""
    bridge_dir = Path(workspace) / '.vscode' / 'ai-bridge'
    commands_dir = bridge_dir / 'commands'
    responses_dir = bridge_dir / 'responses'

    # Create command
    cmd_id = f"cmd-{int(time.time() * 1000)}"
    command = {
        "id": cmd_id,
        "action": action,
        "params": params,
        "timestamp": int(time.time() * 1000)
    }

    # Write command file
    cmd_file = commands_dir / f"{cmd_id}.json"
    cmd_file.write_text(json.dumps(command, indent=2))

    # Poll for response (fast commands return instantly)
    resp_file = responses_dir / f"resp-{cmd_id}.json"
    start = time.time()
    while time.time() - start < timeout:
        if resp_file.exists():
            response = json.loads(resp_file.read_text())
            resp_file.unlink()  # Clean up
            return response
        time.sleep(0.1)

    raise TimeoutError(f"No response received within {timeout}s")

# Example usage
result = send_command(
    workspace="/path/to/project",
    action="extractText",
    params={"filePath": "/path/to/document.docx"}
)
print(result)
```

---

## Security Considerations

### Validate Commands

```typescript
bridge.registerHandler('executeCommand', async (params) => {
  // Whitelist allowed commands
  const allowedCommands = [
    'myExt.formatDocument',
    'myExt.extractText',
    'myExt.showPreview'
  ];

  if (!allowedCommands.includes(params.command)) {
    throw new Error(`Command not allowed: ${params.command}`);
  }

  return await vscode.commands.executeCommand(params.command, ...params.args);
});
```

### Sanitize File Paths

```typescript
bridge.registerHandler('readFile', async (params) => {
  const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
  if (!workspaceRoot) throw new Error('No workspace');

  // Ensure path is within workspace
  const resolvedPath = path.resolve(workspaceRoot, params.filePath);
  if (!resolvedPath.startsWith(workspaceRoot)) {
    throw new Error('Path outside workspace');
  }

  const content = await vscode.workspace.fs.readFile(
    vscode.Uri.file(resolvedPath)
  );
  return { content: new TextDecoder().decode(content) };
});
```

### Rate Limiting

```typescript
class RateLimiter {
  private requests: number[] = [];
  private maxRequests: number;
  private windowMs: number;

  constructor(maxRequests = 100, windowMs = 60000) {
    this.maxRequests = maxRequests;
    this.windowMs = windowMs;
  }

  check(): boolean {
    const now = Date.now();
    this.requests = this.requests.filter(t => now - t < this.windowMs);
    if (this.requests.length >= this.maxRequests) {
      return false;
    }
    this.requests.push(now);
    return true;
  }
}

const limiter = new RateLimiter();

private async processCommand(filePath: string) {
  if (!limiter.check()) {
    // Write rate limit error response
    return;
  }
  // ... process command
}
```

---

## Alternative Approaches

### VS Code Language Model Tools API

For extensions that want to expose tools to VS Code's built-in AI features:

```typescript
// Register a tool for Copilot/language models
const tool = vscode.lm.registerTool('myExt.searchFiles', {
  displayName: 'Search Files',
  description: 'Search for files in the workspace',
  inputSchema: {
    type: 'object',
    properties: {
      query: { type: 'string', description: 'Search query' }
    },
    required: ['query']
  }
});

tool.onDidReceiveInput(async (input) => {
  const files = await vscode.workspace.findFiles(`**/*${input.query}*`);
  return { files: files.map(f => f.fsPath) };
});
```

### MCP (Model Context Protocol)

For advanced AI integrations, consider implementing an MCP server:

```typescript
// MCP server in extension
import { Server } from '@modelcontextprotocol/sdk/server';

const mcpServer = new Server({
  name: 'vscode-extension',
  version: '1.0.0'
});

mcpServer.setRequestHandler('tools/call', async (request) => {
  // Handle MCP tool calls
});
```

### Extension-to-Extension API

If building multiple extensions that need to communicate:

```typescript
// Extension A: Export API
export function activate(context: vscode.ExtensionContext) {
  return {
    extractText: async (path: string) => { /* ... */ },
    formatDocument: async (uri: vscode.Uri) => { /* ... */ }
  };
}

// Extension B: Use API
const extA = vscode.extensions.getExtension('publisher.extension-a');
const api = await extA?.activate();
const text = await api?.extractText('/path/to/file');
```
