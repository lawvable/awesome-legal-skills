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

type Handler = (params: any) => Promise<any>;

export class FileBridge {
  private commandsDir: string;
  private responsesDir: string;
  private watcher: fs.FSWatcher | null = null;
  private handlers: Map<string, Handler> = new Map();
  private processedCommands: Set<string> = new Set();

  constructor(private workspaceRoot: string) {
    this.commandsDir = path.join(workspaceRoot, '.vscode', 'ai-bridge', 'commands');
    this.responsesDir = path.join(workspaceRoot, '.vscode', 'ai-bridge', 'responses');
  }

  async start() {
    // Ensure directories exist
    await fs.promises.mkdir(this.commandsDir, { recursive: true });
    await fs.promises.mkdir(this.responsesDir, { recursive: true });

    // Process any existing commands
    await this.processExistingCommands();

    // Watch for new commands
    this.watcher = fs.watch(this.commandsDir, async (eventType, filename) => {
      if (filename?.endsWith('.json')) {
        const filePath = path.join(this.commandsDir, filename);
        // Small delay to ensure file is fully written
        setTimeout(() => this.processCommand(filePath), 50);
      }
    });

    console.log(`FileBridge started. Watching: ${this.commandsDir}`);
  }

  stop() {
    if (this.watcher) {
      this.watcher.close();
      this.watcher = null;
    }
    console.log('FileBridge stopped.');
  }

  registerHandler(action: string, handler: Handler) {
    this.handlers.set(action, handler);
    console.log(`Registered handler for action: ${action}`);
  }

  private async processExistingCommands() {
    try {
      const files = await fs.promises.readdir(this.commandsDir);
      for (const file of files.filter(f => f.endsWith('.json'))) {
        await this.processCommand(path.join(this.commandsDir, file));
      }
    } catch (e) {
      // Directory might not exist yet, that's ok
    }
  }

  private async processCommand(filePath: string) {
    const filename = path.basename(filePath);

    // Prevent processing the same command twice
    if (this.processedCommands.has(filename)) {
      return;
    }

    try {
      // Check if file exists
      if (!fs.existsSync(filePath)) {
        return;
      }

      this.processedCommands.add(filename);

      const content = await fs.promises.readFile(filePath, 'utf-8');
      const command: Command = JSON.parse(content);

      console.log(`Processing command: ${command.action} (${command.id})`);

      // Find handler
      const handler = this.handlers.get(command.action);
      let response: Response;

      if (!handler) {
        response = {
          id: command.id,
          status: 'error',
          error: {
            code: 'UNKNOWN_ACTION',
            message: `No handler registered for action: ${command.action}`
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

      console.log(`Wrote response: ${responsePath}`);

      // Delete command file
      await fs.promises.unlink(filePath);

      // Clean up processed set after a delay (prevent memory leak)
      setTimeout(() => {
        this.processedCommands.delete(filename);
      }, 60000);

    } catch (e) {
      console.error('Error processing command:', e);
      this.processedCommands.delete(filename);
    }
  }
}
