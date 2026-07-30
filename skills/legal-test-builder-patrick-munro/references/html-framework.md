# HTML Framework Reference

Complete implementation guide for the Legal Test Builder HTML output.
Read this before writing any HTML for a legal test artifact.

---

## Design system

### Philosophy

Dark, monochrome-adjacent palette with a single accent colour. Serif display font for question text
(conveys gravity and legality). Monospace for all metadata, labels, timers, and code. Sans-serif for
body prose. The aesthetic should feel like a serious professional tool, not a consumer app.

### CSS variables. Paste these into every test

```css
:root {
  --bg: #08090d;
  --surface: #111218;
  --surface2: #181920;
  --border: #24252e;
  --border2: #2e3040;
  --text: #e8e9f0;
  --text-muted: #6b6d80;
  --text-dim: #44465a;
  --accent: #c8b4ff;       /* primary highlight. Purple */
  --accent2: #7b6fbf;      /* dimmed accent */
  --red: #ff6b6b;          /* critical problems */
  --red-dim: #3d1a1a;
  --amber: #ffb347;        /* high problems / warnings */
  --amber-dim: #3d2a0a;
  --green: #5ddfb0;        /* model answers / fixes */
  --green-dim: #0d2e23;
  --blue: #60a5fa;         /* medium problems / info */
  --blue-dim: #0d1f3d;
  --mono: 'DM Mono', monospace;
  --serif: 'Fraunces', serif;
  --sans: 'DM Sans', sans-serif;
}
```

### Google Fonts import (always include)

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@300;400;500&family=Fraunces:ital,opsz,wght@0,9.144,300;0,9.144,400;0,9.144,600;1,9.144,300&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
```

---

## Components

### 1. Sticky header with timer

```html
<header class="header">
  <div class="header-left">
    <div class="header-label">Organisation · Role</div>
    <div class="header-title">Test Title</div>
  </div>
  <nav class="section-nav">
    <a href="#s1" class="nav-pill">§1 Contract</a>
    <a href="#s2" class="nav-pill">§2 Memo</a>
    <!-- add as needed -->
  </nav>
  <div class="timer-block">
    <div>
      <div class="header-label" style="text-align:center;margin-bottom:2px;">Time Remaining</div>
      <div class="timer-display" id="timer">3:00:00</div>
      <div class="progress-bar"><div class="progress-fill" id="timer-bar" style="width:100%"></div></div>
    </div>
    <div class="timer-controls">
      <button class="btn primary" id="start-btn" onclick="startTimer()">Start</button>
      <button class="btn" onclick="resetTimer()">Reset</button>
    </div>
  </div>
</header>
```

**Timer CSS:**
```css
.header {
  position: sticky; top: 0; z-index: 100;
  background: rgba(8,9,13,0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  padding: 12px 32px;
  display: flex; align-items: center; justify-content: space-between; gap: 24px;
}
.timer-display {
  font-family: var(--mono); font-size: 28px; color: var(--accent);
  letter-spacing: 0.05em; min-width: 120px; text-align: center;
  transition: color 0.3s;
}
.timer-display.warn { color: var(--amber); }
.timer-display.danger { color: var(--red); animation: pulse 1s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }
.progress-bar { height: 2px; background: var(--border); border-radius: 1px; margin-top: 8px; overflow: hidden; }
.progress-fill { height: 100%; background: linear-gradient(90deg, var(--accent2), var(--accent)); transition: width 1s linear; }
```

**Timer JS (place in `<script>` at bottom of body):**
```js
const TOTAL = 3 * 60 * 60; // adjust to test duration in seconds
let remaining = TOTAL;
let interval = null;
let running = false;

function startTimer() {
  if (running) {
    clearInterval(interval); running = false;
    document.getElementById('start-btn').textContent = 'Resume'; return;
  }
  running = true;
  document.getElementById('start-btn').textContent = 'Pause';
  interval = setInterval(() => {
    if (remaining <= 0) { clearInterval(interval); return; }
    remaining--;
    const h = Math.floor(remaining/3600);
    const m = Math.floor((remaining%3600)/60);
    const s = remaining%60;
    const el = document.getElementById('timer');
    el.textContent = `${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
    el.className = 'timer-display';
    if (remaining < 1800) el.classList.add('warn');
    if (remaining < 600) { el.classList.remove('warn'); el.classList.add('danger'); }
    document.getElementById('timer-bar').style.width = (remaining/TOTAL*100)+'%';
  }, 1000);
}
function resetTimer() {
  clearInterval(interval); running = false; remaining = TOTAL;
  document.getElementById('start-btn').textContent = 'Start';
  document.getElementById('timer').textContent = '3:00:00'; // match TOTAL
  document.getElementById('timer-bar').style.width = '100%';
}
```

---

### 2. Contract body with annotated problems

Problems are marked with `<span class="problem">` and `data-title` / `data-body` attributes.
A floating tooltip renders on hover via JS. The problem annotation is **invisible until hovered**: the clause reads as normal contract text, which is the point.

```html
<!-- Contract wrapper -->
<div class="contract-wrapper">
  <div class="contract-toolbar">
    <div class="toolbar-label">DRAFT. Agreement Name v1 (Party markup). Date</div>
    <span style="font-family:var(--mono);font-size:9px;color:var(--red);">● N embedded problems</span>
  </div>
  <div class="contract-body">

    <span class="cl">
      <span class="cl-title">1. Clause Title</span>
      Normal contract text here. <span class="problem" 
        data-id="P1" 
        data-title="Short problem title" 
        data-body="Full explanation of why this is a problem and what it means commercially. Be specific. Mention the commercial consequence, not just the legal defect.">The problematic language goes here and reads naturally within the clause.</span> More normal text.
    </span>

  </div>
</div>

<!-- Tooltip element. Place once, near top of body -->
<div id="tooltip">
  <div id="tooltip-title"></div>
  <div id="tooltip-body"></div>
</div>
```

**CSS for contract body:**
```css
.contract-wrapper { border: 1px solid var(--border2); border-radius: 8px; overflow: hidden; margin-bottom: 24px; }
.contract-toolbar { padding: 10px 16px; background: var(--surface2); border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 12px; }
.toolbar-label { font-family: var(--mono); font-size: 9px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-dim); flex: 1; }
.contract-body { padding: 32px; background: var(--surface); font-family: var(--mono); font-size: 12.5px; line-height: 1.9; color: #c8cad8; }
.cl { display: block; margin-bottom: 20px; }
.cl-title { font-weight: 500; color: var(--text); display: block; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em; font-size: 11px; border-bottom: 1px solid var(--border); padding-bottom: 4px; }
.problem { background: rgba(255,107,107,0.12); border-bottom: 1.5px solid var(--red); cursor: pointer; transition: background 0.15s; }
.problem:hover { background: rgba(255,107,107,0.22); }
#tooltip { position: fixed; z-index: 999; display: none; background: #1a0d0d; border: 1px solid var(--red); border-radius: 6px; padding: 10px 14px; font-family: var(--sans); font-size: 12px; color: var(--text); max-width: 320px; pointer-events: none; box-shadow: 0 8px 32px rgba(0,0,0,0.5); line-height: 1.5; }
#tooltip-title { font-family: var(--mono); font-size: 9px; letter-spacing: 0.1em; color: var(--red); margin-bottom: 5px; text-transform: uppercase; }
```

**Tooltip JS:**
```js
const tooltip = document.getElementById('tooltip');
document.querySelectorAll('.problem').forEach(el => {
  el.addEventListener('mouseenter', (e) => {
    document.getElementById('tooltip-title').textContent = el.dataset.title || '';
    document.getElementById('tooltip-body').textContent = el.dataset.body || '';
    tooltip.style.display = 'block';
    posTooltip(e);
  });
  el.addEventListener('mousemove', posTooltip);
  el.addEventListener('mouseleave', () => { tooltip.style.display = 'none'; });
});
function posTooltip(e) {
  const x = e.clientX + 16, y = e.clientY + 16;
  const tw = tooltip.offsetWidth || 320, th = tooltip.offsetHeight || 100;
  tooltip.style.left = Math.min(x, window.innerWidth-tw-20)+'px';
  tooltip.style.top = Math.min(y, window.innerHeight-th-20)+'px';
}
```

---

### 3. Problem row (below the contract)

One row per problem. Contains: ID badge, severity badge, title, candidate textarea, reveal block.

```html
<div class="problem-row">
  <div class="problem-row-header">
    <div class="problem-id">P1</div>
    <div class="problem-severity sev-critical">CRITICAL</div>  <!-- sev-critical | sev-high | sev-medium -->
    <div class="problem-title">Short description of the clause issue</div>
  </div>
  <div class="problem-detail">One sentence explaining what the candidate should address.</div>
  <textarea class="write-area" placeholder="Your analysis + proposed redline language.."></textarea>
  
  <!-- Reveal block goes here. See component 4 -->
</div>
```

**CSS:**
```css
.problem-row { padding: 16px; border: 1px solid var(--border); border-radius: 6px; margin-bottom: 10px; background: var(--surface); transition: all 0.15s; }
.problem-row:hover { border-color: var(--red); }
.problem-row-header { display: flex; align-items: center; gap: 12px; margin-bottom: 8px; }
.problem-id { font-family: var(--mono); font-size: 9px; letter-spacing: 0.1em; color: var(--red); padding: 2px 8px; border: 1px solid var(--red); border-radius: 3px; }
.problem-severity { font-family: var(--mono); font-size: 9px; letter-spacing: 0.08em; padding: 2px 8px; border-radius: 3px; }
.sev-critical { background: var(--red-dim); color: var(--red); border: 1px solid var(--red); }
.sev-high { background: var(--amber-dim); color: var(--amber); border: 1px solid var(--amber); }
.sev-medium { background: var(--blue-dim); color: var(--blue); border: 1px solid var(--blue); }
.problem-title { font-size: 13px; font-weight: 500; color: var(--text); flex: 1; }
.problem-detail { font-size: 12px; color: var(--text-muted); line-height: 1.65; margin-bottom: 10px; }
.write-area { width: 100%; min-height: 160px; background: var(--surface2); border: 1px solid var(--border2); border-radius: 6px; padding: 14px; color: var(--text); font-family: var(--mono); font-size: 12px; line-height: 1.8; resize: vertical; outline: none; transition: border-color 0.15s; }
.write-area:focus { border-color: var(--accent2); }
.write-area::placeholder { color: var(--text-dim); }
```

---

### 4. Reveal block (hidden model answer)

```html
<div class="reveal-block">
  <div class="reveal-header" onclick="toggle(this)">
    <span class="reveal-header-label model">▸ Model Answer. P1</span>
    <!-- label class options: model (green) | analysis (purple) | strategy (amber) -->
    <span class="reveal-chevron">▼</span>
  </div>
  <div class="reveal-body">
    <div class="answer-content">
      <h4>Section heading</h4>
      <p>Body text..</p>
      
      <!-- Redlined replacement text -->
      <p style="font-family:var(--mono);font-size:11px;color:var(--green);background:var(--green-dim);padding:12px;border-radius:4px;line-height:1.8;">
        <span style="text-decoration:line-through;color:var(--red);">Original bad text here.</span>
        [INSERT] Replacement text here.
      </p>
      
      <!-- Hook quote -->
      <div class="hook-box">One memorable sentence capturing the strategic point.</div>
      
      <!-- Trap warning -->
      <div class="trap-box">What the instinctive-but-wrong response is and why it fails.</div>
      
      <!-- Knowledge gap -->
      <div class="gap-box">Where the law is genuinely uncertain. Be honest about this.</div>
    </div>
  </div>
</div>
```

**CSS:**
```css
.reveal-block { margin-top: 12px; border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }
.reveal-header { padding: 14px 20px; background: var(--surface2); cursor: pointer; display: flex; align-items: center; justify-content: space-between; transition: background 0.15s; user-select: none; }
.reveal-header:hover { background: var(--surface); }
.reveal-header-label { font-family: var(--mono); font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; }
.reveal-header-label.model { color: var(--green); }
.reveal-header-label.analysis { color: var(--accent); }
.reveal-header-label.strategy { color: var(--amber); }
.reveal-chevron { font-family: var(--mono); font-size: 10px; color: var(--text-dim); transition: transform 0.2s; }
.reveal-header.open .reveal-chevron { transform: rotate(180deg); }
.reveal-body { display: none; padding: 24px; background: var(--surface); border-top: 1px solid var(--border); }
.reveal-body.open { display: block; }
.answer-content h4 { font-family: var(--mono); font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--accent); margin: 20px 0 8px; }
.answer-content h4:first-child { margin-top: 0; }
.answer-content p { font-size: 13px; color: var(--text-muted); margin-bottom: 12px; line-height: 1.75; }
.answer-content ul { list-style: none; margin-bottom: 16px; }
.answer-content ul li { font-size: 13px; color: var(--text-muted); padding: 6px 0 6px 20px; position: relative; border-bottom: 1px solid var(--border); line-height: 1.6; }
.answer-content ul li::before { content: '—'; position: absolute; left: 0; color: var(--text-dim); font-family: var(--mono); }
.hook-box { padding: 14px 18px; background: var(--green-dim); border-left: 3px solid var(--green); border-radius: 0 6px 6px 0; font-size: 13px; color: var(--green); font-style: italic; margin: 16px 0; }
.trap-box { padding: 14px 18px; background: var(--red-dim); border-left: 3px solid var(--red); border-radius: 0 6px 6px 0; font-size: 12px; color: var(--red); margin: 12px 0; }
.trap-box::before { content: '⚠ TRAP: '; font-family: var(--mono); font-size: 9px; letter-spacing: 0.1em; text-transform: uppercase; display: block; margin-bottom: 4px; opacity: 0.7; }
.gap-box { padding: 12px 16px; background: var(--amber-dim); border-left: 3px solid var(--amber); border-radius: 0 6px 6px 0; font-size: 12px; color: var(--amber); margin: 12px 0; }
.gap-box::before { content: '⚡ GAP: '; font-family: var(--mono); font-size: 9px; letter-spacing: 0.1em; text-transform: uppercase; display: block; margin-bottom: 4px; opacity: 0.7; }
```

**Reveal JS:**
```js
function toggle(el) {
  el.classList.toggle('open');
  const body = el.nextElementSibling;
  if (body) body.classList.toggle('open');
}
```

---

### 5. Section structure

```html
<section class="section" id="s1">
  <div class="section-header">
    <div class="section-num">TASK 01</div>
    <div class="section-meta">
      <h2 class="section-title">Task Title</h2>
      <div class="section-sub">Subtitle / document name</div>
    </div>
    <div class="section-time-badge">⏱ Target: 65 min</div>
  </div>
  <!-- task content here -->
</section>
```

```css
.section { margin-bottom: 80px; scroll-margin-top: 80px; }
.section-header { display: flex; align-items: flex-start; gap: 20px; margin-bottom: 32px; padding-bottom: 20px; border-bottom: 1px solid var(--border); }
.section-num { font-family: var(--mono); font-size: 11px; letter-spacing: 0.1em; color: var(--accent2); padding: 4px 10px; border: 1px solid var(--accent2); border-radius: 3px; white-space: nowrap; margin-top: 4px; }
.section-title { font-family: var(--serif); font-size: 22px; font-weight: 300; color: var(--text); margin-bottom: 4px; }
.section-sub { font-family: var(--mono); font-size: 10px; letter-spacing: 0.1em; color: var(--text-dim); }
.section-time-badge { font-family: var(--mono); font-size: 10px; padding: 4px 12px; border-radius: 20px; background: var(--surface2); border: 1px solid var(--border2); color: var(--text-muted); white-space: nowrap; }
```

---

### 6. Question card

Use for scenario / memo questions.

```html
<div class="q-card">
  <div class="q-eyebrow">Scenario label</div>
  <div class="q-text">"The scenario question text goes here, in italics."</div>
  <div class="q-context">
    <strong>Instructions / constraints:</strong> Additional facts the candidate needs.
  </div>
  <textarea class="write-area" style="min-height:200px;" placeholder="Your analysis.."></textarea>
  <!-- reveal block here -->
</div>
```

```css
.q-card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 24px; margin-bottom: 24px; }
.q-eyebrow { font-family: var(--mono); font-size: 9px; letter-spacing: 0.15em; text-transform: uppercase; color: var(--text-dim); margin-bottom: 10px; }
.q-text { font-family: var(--serif); font-size: 16px; font-weight: 300; color: var(--text); margin-bottom: 16px; line-height: 1.5; font-style: italic; }
.q-context { font-size: 13px; color: var(--text-muted); padding: 12px 16px; background: var(--surface2); border-radius: 6px; margin-bottom: 16px; border-left: 3px solid var(--border2); }
```

---

### 7. Checklist

```html
<div onclick="toggleCheck(this)" class="checklist-item">
  <div class="check-box"><span class="check-mark">✓</span></div>
  <div class="checklist-text">Item text describing what the candidate should have done.</div>
</div>
```

```css
.checklist-item { display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid var(--border); cursor: pointer; }
.check-box { width: 16px; height: 16px; border: 1px solid var(--border2); border-radius: 3px; flex-shrink: 0; margin-top: 1px; display: flex; align-items: center; justify-content: center; transition: all 0.15s; }
.checklist-item.done .check-box { background: var(--green); border-color: var(--green); }
.check-mark { font-size: 9px; color: #000; display: none; }
.checklist-item.done .check-mark { display: block; }
.checklist-item.done .checklist-text { text-decoration: line-through; color: var(--text-dim); }
.checklist-text { font-size: 13px; color: var(--text-muted); line-height: 1.5; }
```

```js
function toggleCheck(item) { item.classList.toggle('done'); }
```

---

## Full HTML scaffold

Use this as your starting point. Fill in content and adjust as needed.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[Organisation] : [Role] Practice Test</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@300;400;500&family=Fraunces:ital,opsz,wght@0,9.144,300;0,9.144,400;0,9.144,600;1,9.144,300&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
/* === PASTE FULL CSS HERE === */
/* Include: css variables, * reset, body, header, timer, nav, main, intro, section, contract, problem, reveal, q-card, checklist */
</style>
</head>
<body>

<div id="tooltip"><div id="tooltip-title"></div><div id="tooltip-body"></div></div>

<header class="header">
  <!-- timer header here -->
</header>

<main class="main">

  <!-- intro block -->
  
  <section class="section" id="s1">
    <!-- TASK 01: Contract Redline -->
  </section>

  <hr class="divider">

  <section class="section" id="s2">
    <!-- TASK 02: Legal Memo -->
  </section>

  <hr class="divider">

  <section class="section" id="s3">
    <!-- TASK 03: Short Analysis -->
  </section>

  <hr class="divider">

  <section class="section" id="s4">
    <!-- TASK 04: Strategy -->
  </section>

  <hr class="divider">

  <section class="section" id="s5">
    <!-- CHECKLIST -->
  </section>

</main>

<script>
// Timer functions: startTimer(), resetTimer()
// Reveal: toggle()
// Tooltip: posTooltip() + event listeners
// Checklist: toggleCheck()
// Smooth scroll for nav pills
</script>
</body>
</html>
```
