# Build Configuration

Complete build configurations for VS Code extensions.

## Table of Contents

- [esbuild (Extension)](#esbuild-extension)
- [Vite (Webview)](#vite-webview)
- [TypeScript Configuration](#typescript-configuration)
- [Package Scripts](#package-scripts)
- [Development Workflow](#development-workflow)

---

## esbuild (Extension)

Use esbuild for the extension code (Node.js runtime).

### esbuild.js

```javascript
const esbuild = require('esbuild');
const { resolve } = require('path');

const isWatch = process.argv.includes('--watch');
const isProduction = process.argv.includes('--production');

/** @type {esbuild.BuildOptions} */
const buildOptions = {
  entryPoints: ['src/extension.ts'],
  bundle: true,
  outfile: 'dist/extension.js',
  external: [
    'vscode',  // VS Code API provided at runtime
    // Add other externals if needed (native modules, etc.)
  ],
  format: 'cjs',
  platform: 'node',
  target: 'node18',
  sourcemap: !isProduction,
  minify: isProduction,
  treeShaking: true,
  logLevel: 'info',

  // Handle __dirname in bundled code
  define: {
    'process.env.NODE_ENV': isProduction ? '"production"' : '"development"'
  },

  // Copy static assets
  loader: {
    '.node': 'copy',  // Native modules
  },

  // Plugins (optional)
  plugins: []
};

async function build() {
  if (isWatch) {
    const ctx = await esbuild.context(buildOptions);
    await ctx.watch();
    console.log('Watching for changes...');
  } else {
    await esbuild.build(buildOptions);
    console.log('Build complete');
  }
}

build().catch(() => process.exit(1));
```

### Multi-Entry Build

For extensions with multiple entry points:

```javascript
const buildOptions = {
  entryPoints: {
    extension: 'src/extension.ts',
    server: 'src/server.ts',  // Language server, etc.
  },
  outdir: 'dist',
  // ... rest of config
};
```

---

## Vite (Webview)

Use Vite for webview code (browser runtime).

### vite.config.ts

```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

export default defineConfig({
  plugins: [react()],

  root: resolve(__dirname),

  build: {
    outDir: resolve(__dirname, '../../dist/webview'),
    emptyOutDir: true,
    sourcemap: true,

    rollupOptions: {
      input: resolve(__dirname, 'index.html'),
      output: {
        // Consistent filenames (no hashes) for CSP
        entryFileNames: '[name].js',
        chunkFileNames: '[name].js',
        assetFileNames: '[name].[ext]'
      }
    },

    // Don't split chunks (simpler for extension)
    cssCodeSplit: false,

    // Inline small assets
    assetsInlineLimit: 4096,
  },

  // Resolve aliases
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },

  // Define globals
  define: {
    'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV || 'production')
  },

  // Dev server (for standalone testing)
  server: {
    port: 3000,
    strictPort: true
  }
});
```

### Webview HTML Template

```html
<!-- src/webview/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Webview</title>
</head>
<body>
  <div id="root"></div>
  <script type="module" src="./index.tsx"></script>
</body>
</html>
```

---

## TypeScript Configuration

### tsconfig.json (Extension)

```json
{
  "compilerOptions": {
    "module": "commonjs",
    "target": "ES2022",
    "lib": ["ES2022"],
    "outDir": "dist",
    "rootDir": "src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,

    // Path aliases (optional)
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "src/webview"]
}
```

### tsconfig.json (Webview)

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,

    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

---

## Package Scripts

### package.json

```json
{
  "scripts": {
    "vscode:prepublish": "npm run build",

    "build": "npm run build:extension && npm run build:webview",
    "build:extension": "node esbuild.js --production",
    "build:webview": "cd src/webview && vite build",

    "watch": "npm-run-all --parallel watch:*",
    "watch:extension": "node esbuild.js --watch",
    "watch:webview": "cd src/webview && vite build --watch",

    "compile": "npm run build:extension && npm run build:webview",

    "lint": "eslint src --ext ts,tsx",
    "lint:fix": "eslint src --ext ts,tsx --fix",

    "typecheck": "tsc --noEmit",
    "typecheck:webview": "cd src/webview && tsc --noEmit",

    "package": "vsce package",
    "publish": "vsce publish"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "@types/vscode": "^1.85.0",
    "@vitejs/plugin-react": "^4.2.0",
    "esbuild": "^0.20.0",
    "npm-run-all": "^4.1.5",
    "typescript": "^5.3.0",
    "vite": "^5.0.0",
    "@vscode/vsce": "^2.22.0"
  }
}
```

---

## Development Workflow

### Launch Configuration

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Run Extension",
      "type": "extensionHost",
      "request": "launch",
      "args": [
        "--extensionDevelopmentPath=${workspaceFolder}"
      ],
      "outFiles": ["${workspaceFolder}/dist/**/*.js"],
      "preLaunchTask": "npm: watch"
    },
    {
      "name": "Run Extension (Production)",
      "type": "extensionHost",
      "request": "launch",
      "args": [
        "--extensionDevelopmentPath=${workspaceFolder}"
      ],
      "outFiles": ["${workspaceFolder}/dist/**/*.js"],
      "preLaunchTask": "npm: build"
    }
  ]
}
```

### Tasks Configuration

Create `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "npm: watch",
      "type": "npm",
      "script": "watch",
      "isBackground": true,
      "problemMatcher": [
        "$tsc-watch",
        "$esbuild-watch"
      ],
      "presentation": {
        "reveal": "never",
        "panel": "dedicated"
      }
    },
    {
      "label": "npm: build",
      "type": "npm",
      "script": "build",
      "problemMatcher": ["$tsc", "$esbuild"]
    }
  ]
}
```

### Problem Matchers

Add to `.vscode/settings.json` for esbuild errors:

```json
{
  "typescript.tsc.autoDetect": "off"
}
```

### Development Steps

1. Open extension folder in VS Code
2. Run `npm install`
3. Press F5 to launch Extension Development Host
4. Make changes → extension reloads automatically (with watch)
5. Open Output panel → "Extension Host" for logs

### Debug Webview

1. In Extension Development Host, open Command Palette
2. Run "Developer: Toggle Developer Tools"
3. Switch to "Console" tab to see webview logs

Or use "Developer: Open Webview Developer Tools" when focused on a webview.

---

## .vscodeignore

Exclude unnecessary files from the packaged extension:

```
# Source files (compiled to dist/)
src/**
**/*.ts
tsconfig*.json

# Build tools
esbuild.js
vite.config.ts
.eslintrc*
.prettierrc*

# Dev files
.vscode/**
.github/**
node_modules/**

# Test files
**/*.test.ts
**/__tests__/**
coverage/**

# Documentation (optional)
docs/**
*.md
!README.md
!CHANGELOG.md
!LICENSE.md

# Git
.git/**
.gitignore

# Misc
**/*.map
.DS_Store
*.vsix
```

---

## Production Optimizations

### Minification

Already enabled in esbuild with `--production` flag.

### Tree Shaking

esbuild handles this automatically. Ensure:
- Use ES modules where possible
- Avoid `require()` for tree-shakeable imports
- Mark side-effect-free packages in package.json

### Bundle Analysis

```javascript
// Add to esbuild.js
const buildOptions = {
  // ...
  metafile: true,
};

const result = await esbuild.build(buildOptions);
const analysis = await esbuild.analyzeMetafile(result.metafile);
console.log(analysis);
```

### Source Maps in Production

For debugging published extensions:

```javascript
// esbuild.js
const buildOptions = {
  sourcemap: 'external',  // Separate .map files
  // or
  sourcemap: true,  // Inline (larger bundle)
};
```

Keep source maps but exclude from package:

```
# .vscodeignore
**/*.map
```
