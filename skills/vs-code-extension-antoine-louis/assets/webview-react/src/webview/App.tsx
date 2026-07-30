import { useState, useCallback, useEffect } from 'react';

// VS Code API types
interface VsCodeApi {
  postMessage(message: any): void;
  getState(): any;
  setState(state: any): void;
}

declare function acquireVsCodeApi(): VsCodeApi;

const vscode = acquireVsCodeApi();

export function App() {
  const [count, setCount] = useState(() => {
    const state = vscode.getState();
    return state?.count ?? 0;
  });
  const [message, setMessage] = useState<string>('');

  // Save state when count changes
  useEffect(() => {
    vscode.setState({ count });
  }, [count]);

  // Listen for messages from extension
  useEffect(() => {
    const handler = (event: MessageEvent) => {
      const message = event.data;
      switch (message.type) {
        case 'data':
          setMessage(message.data.message);
          break;
      }
    };

    window.addEventListener('message', handler);
    return () => window.removeEventListener('message', handler);
  }, []);

  const handleIncrement = useCallback(() => {
    setCount(c => c + 1);
  }, []);

  const handleAlert = useCallback(() => {
    vscode.postMessage({ type: 'alert', text: `Current count: ${count}` });
  }, [count]);

  const handleGetData = useCallback(() => {
    vscode.postMessage({ type: 'getData' });
  }, []);

  return (
    <main className="container">
      <h1>VS Code Webview</h1>

      <section className="card">
        <h2>Counter</h2>
        <p className="count">{count}</p>
        <button onClick={handleIncrement}>Increment</button>
      </section>

      <section className="card">
        <h2>Communication</h2>
        <div className="button-group">
          <button onClick={handleAlert}>Show Alert in VS Code</button>
          <button onClick={handleGetData}>Get Data from Extension</button>
        </div>
        {message && <p className="message">Response: {message}</p>}
      </section>
    </main>
  );
}
