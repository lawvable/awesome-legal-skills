# HTML Deal Card Template

Complete implementation pattern for regulatory deal cards. Adapt section names, content, and colour scheme to the specific regulation and audience.

## Full template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Regulation Name] Deal Card</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    :root {
      --primary: #4a5568;
      --primary-accent: #3182ce;
      --surface: #ffffff;
      --surface-muted: #f8f9fa;
      --surface-dim: #f0f2f5;
      --border: #e2e8f0;
      --text: #1a202c;
      --text-muted: #4a5568;
      --text-dim: #718096;
      --risk-high: #e53e3e;
      --risk-high-bg: #fff5f5;
      --risk-medium: #dd6b20;
      --risk-medium-bg: #fffaf0;
      --risk-low: #38a169;
      --risk-low-bg: #f0fff4;
      --example: #3182ce;
      --example-bg: #ebf8ff;
      --implementation: #805ad5;
      --implementation-bg: #faf5ff;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.6;
      color: var(--text);
      background: var(--surface-muted);
    }

    /* Header */
    .header {
      background: var(--primary);
      color: white;
      padding: 2rem;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }
    .header h1 { font-size: 2.25rem; margin-bottom: 0.25rem; font-weight: 600; }
    .header .subtitle { opacity: 0.85; font-size: 1rem; font-weight: 300; }
    .header .verification-note {
      margin-top: 0.75rem;
      font-size: 0.85rem;
      opacity: 0.75;
      font-style: italic;
    }

    /* Navigation */
    .nav {
      background: var(--surface);
      padding: 1rem 2rem;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
      border-bottom: 1px solid var(--border);
    }
    .nav-item {
      padding: 0.5rem 1rem;
      background: var(--surface-dim);
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s;
      font-size: 0.9rem;
      color: var(--text-muted);
      user-select: none;
    }
    .nav-item:hover { background: var(--primary-accent); color: white; }
    .nav-item.active { background: var(--primary); color: white; }

    /* Panels */
    .panel {
      display: none;
      max-width: 1400px;
      margin: 2rem auto;
      background: var(--surface);
      border-radius: 8px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
      overflow: hidden;
    }
    .panel.active { display: block; }
    .panel-header {
      padding: 2rem;
      border-bottom: 2px solid var(--primary-accent);
      background: var(--surface-muted);
    }
    .panel-header h2 { font-size: 1.75rem; margin-bottom: 0.25rem; font-weight: 600; }
    .panel-subtitle { color: var(--text-dim); font-size: 1rem; }

    /* Table */
    .table-container { overflow-x: auto; padding: 1.5rem; }
    table { width: 100%; border-collapse: collapse; }
    th, td {
      padding: 1rem;
      text-align: left;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
    }
    th {
      background: var(--surface-dim);
      font-weight: 600;
      font-size: 0.875rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    tr:hover td { background: var(--surface-muted); }

    /* Requirement cell */
    .requirement-name { font-weight: 600; color: var(--text); display: block; margin-bottom: 0.25rem; }
    .requirement-article { font-size: 0.8rem; color: var(--text-dim); font-family: "SF Mono", Consolas, monospace; }

    /* Risk badges */
    .risk-badge {
      display: inline-block;
      padding: 0.2rem 0.6rem;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-top: 0.5rem;
    }
    .risk-badge.high { background: var(--risk-high-bg); color: var(--risk-high); border: 1px solid var(--risk-high); }
    .risk-badge.medium { background: var(--risk-medium-bg); color: var(--risk-medium); border: 1px solid var(--risk-medium); }
    .risk-badge.low { background: var(--risk-low-bg); color: var(--risk-low); border: 1px solid var(--risk-low); }

    /* Example and implementation boxes */
    .example-box, .implementation-box {
      padding: 0.75rem 1rem;
      border-radius: 6px;
      margin: 0.5rem 0;
      font-size: 0.9rem;
    }
    .example-box {
      background: var(--example-bg);
      border-left: 3px solid var(--example);
      color: var(--text);
    }
    .implementation-box {
      background: var(--implementation-bg);
      border-left: 3px solid var(--implementation);
      color: var(--text);
    }

    /* Negotiable list */
    .negotiable-list { list-style: none; padding: 0; }
    .negotiable-list li {
      padding: 0.4rem 0 0.4rem 1.25rem;
      position: relative;
      font-size: 0.9rem;
      color: var(--text-muted);
    }
    .negotiable-list li::before {
      content: "◇";
      position: absolute;
      left: 0;
      color: var(--primary-accent);
    }

    /* Collapsible sections */
    .collapsible {
      cursor: pointer;
      padding: 0.75rem 1rem;
      background: var(--surface-dim);
      border-left: 3px solid var(--primary-accent);
      margin: 0.75rem 0;
      border-radius: 4px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.9rem;
    }
    .collapsible:hover { background: var(--surface-muted); }
    .collapsible-content {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.3s ease;
    }
    .collapsible-content.active { max-height: 3000px; padding: 1rem; }

    /* Interactive term tooltips */
    .interactive-term {
      color: var(--primary-accent);
      border-bottom: 1px dotted var(--primary-accent);
      cursor: help;
      position: relative;
    }
    .interactive-term:hover::after {
      content: attr(data-term);
      position: absolute;
      bottom: 125%;
      left: 0;
      background: var(--text);
      color: white;
      padding: 0.5rem 0.75rem;
      border-radius: 4px;
      font-size: 0.8rem;
      white-space: normal;
      width: 260px;
      z-index: 1000;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    /* Disclaimer */
    .disclaimer {
      max-width: 1400px;
      margin: 2rem auto;
      padding: 1.25rem 2rem;
      background: var(--surface);
      border-left: 4px solid var(--risk-medium);
      border-radius: 4px;
      font-size: 0.85rem;
      color: var(--text-muted);
      font-style: italic;
    }

    /* Print */
    @media print {
      .nav { display: none; }
      .panel { display: block !important; box-shadow: none; page-break-after: always; }
      .collapsible-content { max-height: none !important; padding: 1rem !important; }
      body { background: white; }
    }

    /* Mobile */
    @media (max-width: 768px) {
      .header { padding: 1.5rem; }
      .header h1 { font-size: 1.75rem; }
      .nav { padding: 0.75rem; }
      .panel { margin: 1rem; }
      table { font-size: 0.85rem; }
      th, td { padding: 0.6rem; }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header class="header">
    <h1>[Regulation Name] Deal Card</h1>
    <div class="subtitle">[Official Citation] · Version of [Date] · Verified [YYYY-MM-DD]</div>
    <div class="verification-note">Verify current consolidated text before relying on this document.</div>
  </header>

  <!-- Navigation -->
  <nav class="nav">
    <div class="nav-item active" onclick="showPanel('panel-1', this)">1. Scope &amp; Definitions</div>
    <div class="nav-item" onclick="showPanel('panel-2', this)">2. Core Obligations</div>
    <div class="nav-item" onclick="showPanel('panel-3', this)">3. Reporting &amp; Notification</div>
    <!-- Add nav items as needed -->
  </nav>

  <!-- Panel 1 -->
  <section id="panel-1" class="panel active">
    <div class="panel-header">
      <h2>I. Scope &amp; Definitions</h2>
      <p class="panel-subtitle">Who the regulation applies to and how key terms are defined.</p>
    </div>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th style="width:20%;">Requirement</th>
            <th style="width:25%;">What is mandatory</th>
            <th style="width:25%;">What is negotiable</th>
            <th style="width:30%;">Example &amp; implementation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="requirement-name">[Requirement title]</span>
              <span class="requirement-article">Art. X(Y)</span>
              <div><span class="risk-badge high">High risk</span></div>
            </td>
            <td>
              [What the regulation compels, in plain language. Not paraphrased so loosely that it misrepresents the obligation.]
            </td>
            <td>
              <ul class="negotiable-list">
                <li>Implementation method</li>
                <li>Timing within the regulatory window</li>
                <li>Allocation of responsibility between parties</li>
                <li>Documentation format</li>
              </ul>
            </td>
            <td>
              <div class="example-box">
                <strong>Example.</strong> [Concrete worked example showing compliant behaviour.]
              </div>
              <div class="implementation-box">
                <strong>Implementation note.</strong> [Practical guidance on how to operationalize.]
              </div>
            </td>
          </tr>
          <!-- Add rows as needed -->
        </tbody>
      </table>
    </div>
  </section>

  <!-- Additional panels follow the same pattern -->

  <!-- Disclaimer -->
  <div class="disclaimer">
    This deal card is a negotiation and training aid. It is not legal advice and does not substitute for qualified counsel on specific matters. Regulations evolve; guidance and enforcement practice evolve faster. Verify current text before relying on this document for any binding decision.
  </div>

  <script>
    function showPanel(panelId, el) {
      document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
      document.getElementById(panelId).classList.add('active');
      if (el) el.classList.add('active');
    }

    document.querySelectorAll('.collapsible').forEach(item => {
      item.addEventListener('click', function() {
        this.classList.toggle('open');
        const content = this.nextElementSibling;
        if (content) content.classList.toggle('active');
      });
    });
  </script>
</body>
</html>
```

## Key component patterns

### Article reference format

```html
<span class="requirement-name">User data access</span>
<span class="requirement-article">Art. 4(1), Art. 3(2)</span>
```

Include annex references where the substance sits in an annex: `Art. 6(2); Annex III No. 5`.

### Mandatory vs. negotiable cell split

```html
<!-- Mandatory column -->
<td>
  Access must be provided without undue delay, in a structured, commonly used, and machine-readable format, free of charge to the user.
  <div><span class="risk-badge high">High risk</span></div>
</td>

<!-- Negotiable column -->
<td>
  <ul class="negotiable-list">
    <li>API design and access protocol</li>
    <li>Granularity of data provision (real-time vs. batch)</li>
    <li>Authentication mechanism</li>
    <li>Contractual allocation of implementation costs</li>
  </ul>
</td>
```

### Example box pattern

```html
<div class="example-box">
  <strong>Example.</strong> A connected home appliance manufacturer provides users with an authenticated API endpoint returning JSON payloads of device-generated data within 48 hours of request, at no cost to the user.
</div>
<div class="implementation-box">
  <strong>Implementation note.</strong> Budget for API development and ongoing maintenance. The "free of charge" provision does not prohibit recovering costs from third-party recipients the user authorizes, which is a distinct commercial negotiation.
</div>
```

### Interactive term (tooltip) pattern

```html
<span class="interactive-term" data-term="A natural or legal person who purchases, rents, or leases a connected product or receives a related service.">user</span>
```

### Collapsible detail section

```html
<div class="collapsible">
  <span>Implementation detail and edge cases</span>
  <span>▾</span>
</div>
<div class="collapsible-content">
  <p>Detailed content, sub-provisions, cross-references, or interpretive notes.</p>
</div>
```

## Colour scheme variants

Swap the CSS variables at the top of the stylesheet. Three pre-sets:

### Corporate (default in template above)
Professional greys and blues; suits client-facing deliverables.

### Legal (conservative)
```css
--primary: #1a365d;
--primary-accent: #2c5282;
--surface-dim: #edf2f7;
```

### High contrast
```css
--primary: #000000;
--primary-accent: #d69e2e;
--surface: #ffffff;
--surface-muted: #f7fafc;
--surface-dim: #edf2f7;
```

## Bilingual toggle pattern

Add at the top of the panel area:

```html
<div class="language-toggle">
  <button onclick="setLanguage('en')" class="lang-btn active">EN</button>
  <button onclick="setLanguage('de')" class="lang-btn">DE</button>
</div>
```

Structure content with language attributes:

```html
<div data-lang="en">English text goes here.</div>
<div data-lang="de" style="display:none;">Deutscher Text hier.</div>
```

JavaScript:

```javascript
function setLanguage(lang) {
  document.querySelectorAll('[data-lang]').forEach(el => {
    el.style.display = el.dataset.lang === lang ? '' : 'none';
  });
  document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
}
```

Do not use this pattern for machine-translated legal text. Both language versions must be independently accurate.

## Accessibility

- Semantic HTML5 throughout (`<header>`, `<nav>`, `<section>`, `<table>` with proper `<thead>`/`<tbody>`)
- `aria-label` on navigation items and interactive controls
- Keyboard navigation: all interactive elements must be reachable via Tab and activatable via Enter or Space
- Focus indicators visible (do not `outline: none` without a visible replacement)
- Colour is not the only signal for severity: risk badges include text, not just colour
- Contrast ratios meet WCAG AA at minimum

## Performance

- Keep everything inline in a single file. External dependencies defeat the purpose of a portable deal card.
- Minimize JavaScript complexity. The interactivity here is lightweight; no framework is needed.
- Test with realistic content volumes (regulations can produce 60+ rows per panel).
- Ensure initial render is fast on mobile devices.
