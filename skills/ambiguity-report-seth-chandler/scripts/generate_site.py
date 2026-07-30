#!/usr/bin/env python3
"""
generate_site.py — Render an ambiguity-report spec.json into a static website.

Usage:
    python generate_site.py --spec PATH --out DIR [--mode multi|single] [--no-netlify-toml]

The script is pure Python (3.8+), no external dependencies. It reads the
canonical spec, applies design tokens, and emits a complete static site.
"""

import argparse
import html as htmllib
import json
import os
import re
import shutil
import sys
from pathlib import Path

# -------------------------------------------------------------------------
# Default design tokens (overridable via spec['design'])
# -------------------------------------------------------------------------

DEFAULT_DESIGN = {
    "accent_color":     "#8b3a1f",
    "accent_soft":      "#c47e5a",
    "accent_deep":      "#6b2d18",
    "dept_color":       "#2c4a6e",
    "dept_bg":          "#eef3f9",
    "adv_color":        "#8b3a1f",
    "adv_bg":           "#fbf0ea",
    "background_color": "#fbf8f1",
    "card_color":       "#ffffff",
    "panel_color":      "#f3ede0",
    "soft_panel_color": "#f7f3e8",
    "border_color":     "#e3dcca",
    "border_strong":    "#cdc4ad",
    "text_color":       "#1f1b16",
    "text_soft":        "#5b524a",
    "text_faint":       "#8a8276",
    "highlight":        "#fdf2c4",
    "highlight_strong": "#f4d35e",
    "primary_font":     "Fraunces",
    "body_font":        "Inter",
    "serif_font":       "Crimson Pro",
}

DEFAULT_FAMILY_PALETTE = {
    "scope":      {"bg": "#dceadb", "fg": "#2c5a2c"},
    "vague":      {"bg": "#fadeb9", "fg": "#7a4a14"},
    "def":        {"bg": "#e4d4ee", "fg": "#523072"},
    "mensrea":    {"bg": "#f6d3d3", "fg": "#862828"},
    "conflict":   {"bg": "#cee0e8", "fg": "#1c485a"},
    "conlaw":     {"bg": "#eed1e0", "fg": "#6a2249"},
    "discretion": {"bg": "#ddd9f1", "fg": "#38346e"},
    "contradiction": {"bg": "#f6d3d3", "fg": "#862828"},
    "gap":        {"bg": "#e0e0e0", "fg": "#3a3a3a"},
}

DEFAULT_FAMILY_LABELS = {
    "scope":      "Scope / coverage",
    "vague":      "Vague term",
    "def":        "Definitional boundary",
    "mensrea":    "Mens rea gap",
    "conflict":   "Cross-clause tension",
    "conlaw":     "Constitutional avoidance",
    "discretion": "Standardless discretion",
    "contradiction": "Internal contradiction",
    "gap":        "Gap / silence",
}

PROFILE_SOURCE_NOUN = {
    "statute":    "Statute",
    "contract":   "Contract",
    "regulation": "Regulation",
    "opinion":    "Opinion",
}

# -------------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------------

def merge_design(spec_design):
    out = dict(DEFAULT_DESIGN)
    out.update(spec_design or {})
    return out

def merge_family_palette(spec_palette):
    out = {k: dict(v) for k, v in DEFAULT_FAMILY_PALETTE.items()}
    for k, v in (spec_palette or {}).items():
        out[k] = dict(v)
    return out

def family_label(key, families_block):
    for f in (families_block or []):
        if f.get("key") == key:
            return f.get("label", DEFAULT_FAMILY_LABELS.get(key, key))
    return DEFAULT_FAMILY_LABELS.get(key, key)

def all_family_keys(spec):
    keys = []
    for s in spec.get("scenarios", []):
        for k in s.get("families", []):
            if k not in keys:
                keys.append(k)
    return keys

def google_font_url(design):
    fonts = []
    for name in [design.get("primary_font"), design.get("body_font"), design.get("serif_font")]:
        if name and re.match(r"^[A-Z][A-Za-z]+(\s[A-Z][A-Za-z]+)*$", name):
            fonts.append(name.replace(" ", "+") + ":ital,wght@0,400;0,500;0,600;0,700;1,400")
    if not fonts:
        return ""
    return ("<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n"
            "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n"
            f"<link href=\"https://fonts.googleapis.com/css2?family={'&family='.join(fonts)}&display=swap\" rel=\"stylesheet\">")

def patched_css(css_source, design, family_palette):
    """Replace the :root block in the CSS with values from the spec."""
    root_vars = []
    root_vars.append(f"  --bg: {design['background_color']};")
    root_vars.append(f"  --bg-card: {design['card_color']};")
    root_vars.append(f"  --bg-panel: {design['panel_color']};")
    root_vars.append(f"  --bg-soft: {design['soft_panel_color']};")
    root_vars.append(f"  --border: {design['border_color']};")
    root_vars.append(f"  --border-strong: {design['border_strong']};")
    root_vars.append(f"  --text: {design['text_color']};")
    root_vars.append(f"  --text-soft: {design['text_soft']};")
    root_vars.append(f"  --text-faint: {design['text_faint']};")
    root_vars.append(f"  --accent: {design['accent_color']};")
    root_vars.append(f"  --accent-soft: {design['accent_soft']};")
    root_vars.append(f"  --accent-deep: {design['accent_deep']};")
    root_vars.append(f"  --dept: {design['dept_color']};")
    root_vars.append(f"  --dept-bg: {design['dept_bg']};")
    root_vars.append(f"  --adv: {design['adv_color']};")
    root_vars.append(f"  --adv-bg: {design['adv_bg']};")
    root_vars.append(f"  --highlight: {design['highlight']};")
    root_vars.append(f"  --highlight-strong: {design['highlight_strong']};")
    for key, pal in family_palette.items():
        root_vars.append(f"  --fam-{key}-bg: {pal['bg']};")
        root_vars.append(f"  --fam-{key}-fg: {pal['fg']};")

    new_root = ":root {\n" + "\n".join(root_vars) + "\n}"
    patched = re.sub(r":root\s*\{[^}]*\}", new_root, css_source, count=1, flags=re.DOTALL)
    return patched

def esc(s):
    """HTML-escape a string. Preserves <em> and <strong> tags from spec content."""
    if s is None:
        return ""
    # We allow <em> and <strong> in spec content. Don't escape those.
    return s

def page_chrome(title, design, active_nav=None, profile="statute", brand_short="", brand_sub="", body_class=""):
    nav_items = [
        ("index.html", "Overview", "overview"),
        ("statute.html", f"The {PROFILE_SOURCE_NOUN.get(profile, 'Source')}", "statute"),
        ("scenario-1.html", "The Scenarios", "scenarios"),
        ("families.html", "Defect Families", "families"),
        ("redrafts.html", "Redrafts", "redrafts"),
        ("methods.html", "Methods", "methods"),
    ]
    nav_html = "".join(
        f'      <a href="{href}"' + (' class="active"' if key == active_nav else "") + f'>{label}</a>\n'
        for href, label, key in nav_items
    )
    body_attr = f' class="{body_class}"' if body_class else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{htmllib.escape(title)}</title>
{google_font_url(design)}
<link rel="stylesheet" href="style.css">
</head>
<body{body_attr}>

<nav class="site-nav">
  <div class="site-nav-inner">
    <a class="brand" href="index.html">
      <span class="brand-mark">{htmllib.escape(brand_short)}</span>
      <span class="brand-sub">{htmllib.escape(brand_sub)}</span>
    </a>
    <div class="nav-links">
{nav_html}    </div>
  </div>
</nav>

'''

def page_footer(meta):
    return f'''
<footer class="site-footer">
  <div class="site-footer-inner">
    <div class="site-footer-meta">
      <div>{htmllib.escape(meta.get("kicker", "Interpretive-Ambiguity Stress-Test"))}</div>
      <div>{htmllib.escape(meta.get("title", ""))} · Audit run {htmllib.escape(meta.get("audit_date", ""))}</div>
    </div>
    <div class="site-footer-meta" style="text-align:right;">
      <div><a href="methods.html">Methods</a> · <a href="statute.html">{PROFILE_SOURCE_NOUN.get(meta.get("profile","statute"), "Source")}</a> · <a href="redrafts.html">Redrafts</a></div>
      <div style="opacity:0.6;">{htmllib.escape(meta.get("profile", "statute"))} profile · canon filter applied</div>
    </div>
  </div>
</footer>

</body>
</html>'''

# -------------------------------------------------------------------------
# Statute (source) rendering
# -------------------------------------------------------------------------

def collect_scenarios_by_anchor(scenarios):
    by_anchor = {}
    for s in scenarios:
        for a in s.get("anchors", []):
            by_anchor.setdefault(a, []).append(s["id"])
    return by_anchor

def render_em(text, emphasize):
    """Wrap each substring in `emphasize` with <em> tags in `text`."""
    if not emphasize or not text:
        return text or ""
    out = text
    for phrase in emphasize:
        # Word-bounded replace, case-sensitive
        pattern = re.compile(r"(?<!<em>)(" + re.escape(phrase) + r")(?!</em>)")
        out = pattern.sub(r"<em>\1</em>", out, count=1)
    return out

def render_badges(scenario_ids, scenarios_by_id, link_mode="multi"):
    """Render small numbered badges linking to scenarios."""
    if not scenario_ids:
        return ""
    parts = []
    for sid in scenario_ids:
        scen = scenarios_by_id.get(sid)
        title = scen.get("title", "") if scen else ""
        if link_mode == "multi":
            href = f'scenario-{sid}.html'
        else:
            href = f'#scenario-{sid}'
        parts.append(
            f'<a class="scenario-badge" href="{href}" title="S-{sid} · {htmllib.escape(title)}">{sid}</a>'
        )
    return '<span class="scenario-badges">' + "".join(parts) + '</span>'

def render_provision(prov, scenarios_by_anchor, scenarios_by_id, link_mode="multi", level=0):
    """Render a single provision and any subprovisions recursively."""
    pid = prov.get("id", "")
    label = prov.get("label", "")
    text = render_em(prov.get("text", ""), prov.get("emphasize", []))
    has_issues = pid in scenarios_by_anchor
    subs = prov.get("subprovisions", []) or []
    badges = render_badges(scenarios_by_anchor.get(pid, []), scenarios_by_id, link_mode)
    cls_prefix = "prov" if level == 0 else "subprov"
    cls = f'{cls_prefix} has-issues' if has_issues else cls_prefix
    out = f'<div class="{cls}" id="prov-{pid}">'
    if label:
        lblcls = "prov-label" if level == 0 else "subprov-label"
        out += f'<span class="{lblcls}">{label}</span>'
    if text:
        out += text
    out += badges
    for sub in subs:
        out += render_provision(sub, scenarios_by_anchor, scenarios_by_id, link_mode, level + 1)
    out += '</div>'
    return out

def render_statute_html(spec, link_mode="multi"):
    source = spec.get("source", {})
    scenarios = spec.get("scenarios", [])
    scenarios_by_anchor = collect_scenarios_by_anchor(scenarios)
    scenarios_by_id = {s["id"]: s for s in scenarios}

    out = '<article class="statute-text">'
    out += f'<div class="stat-section">{htmllib.escape(source.get("name", "Source text"))}</div>'

    for sec in source.get("sections", []):
        if sec.get("subhead"):
            out += f'<div class="stat-subhead">{htmllib.escape(sec["subhead"])}</div>'
        # Top-level provision may have its own text + ID OR be header-only with subprovisions
        if sec.get("text") is not None or sec.get("id"):
            # Render as a provision itself (only if it has text)
            if sec.get("text"):
                out += render_provision(sec, scenarios_by_anchor, scenarios_by_id, link_mode, 0)
        # Render subprovisions
        for sub in sec.get("subprovisions", []) or []:
            out += render_provision(sub, scenarios_by_anchor, scenarios_by_id, link_mode, 0)
    out += '</article>'
    return out

# -------------------------------------------------------------------------
# Scenario rendering helpers
# -------------------------------------------------------------------------

def render_anchor_pills(anchors, source_index, link_mode="multi"):
    """Render anchor pills linking to source provisions."""
    parts = []
    for a in anchors:
        label = source_index.get(a, {}).get("label", a)
        if link_mode == "multi":
            href = f'statute.html#prov-{a}'
        else:
            href = f'#prov-{a}'
        # Strip outer parens from label for display since CSS adds §
        display = label.strip("()")
        if display.startswith(")") or display.endswith("("):
            display = label  # Don't strip if it would mangle
        parts.append(f'<a class="anchor-pill" href="{href}">{label}</a>')
    return " ".join(parts)

def render_family_pills(family_keys, families_block, link_mode="multi"):
    parts = []
    for k in family_keys:
        label = family_label(k, families_block)
        if link_mode == "multi":
            href = f'families.html#fam-{k}'
        else:
            href = f'#fam-{k}'
        parts.append(f'<a class="family-pill" data-fam="{k}" href="{href}">{htmllib.escape(label)}</a>')
    return " ".join(parts)

def build_source_index(spec):
    """Flat index: id -> {label, text}"""
    idx = {}
    def walk(prov):
        if prov.get("id"):
            idx[prov["id"]] = {"label": prov.get("label", ""), "text": prov.get("text", "")}
        for sub in prov.get("subprovisions", []) or []:
            walk(sub)
    for sec in spec.get("source", {}).get("sections", []):
        walk(sec)
    return idx

# -------------------------------------------------------------------------
# Multi-page renderers
# -------------------------------------------------------------------------

def render_index_html(spec, design):
    meta = spec.get("meta", {})
    scenarios = spec.get("scenarios", [])
    families_block = spec.get("families")
    source_index = build_source_index(spec)
    profile = meta.get("profile", "statute")

    cards = []
    for s in scenarios:
        anchors_html = " ".join(f'<span class="anchor-pill">{source_index.get(a, {}).get("label", a)}</span>' for a in s.get("anchors", []))
        fams_html = " ".join(f'<span class="family-pill" data-fam="{k}">{htmllib.escape(family_label(k, families_block))}</span>' for k in s.get("families", []))
        cards.append(f'''
    <a class="scenario-card" href="scenario-{s["id"]}.html">
      <div class="scenario-card-num">SCENARIO {s["id"]}</div>
      <h3 class="scenario-card-title">{htmllib.escape(s.get("title", ""))}</h3>
      <p class="scenario-card-summary">{esc(s.get("tagline", ""))}</p>
      <div class="scenario-card-foot">{anchors_html} {fams_html}</div>
    </a>''')

    n = len(scenarios)
    head = page_chrome(
        title=f'{meta.get("title", "Ambiguity Report")} — Overview',
        design=design,
        active_nav="overview",
        profile=profile,
        brand_short=meta.get("brand_short", meta.get("title", "")),
        brand_sub=meta.get("brand_sub", meta.get("kicker", "Ambiguity Report")),
    )
    source_noun = PROFILE_SOURCE_NOUN.get(profile, "Source")
    body = f'''<div class="wrap">

  <div class="kicker">{htmllib.escape(meta.get("kicker", "Ambiguity audit"))}</div>
  <h1 class="page-title">{htmllib.escape(meta.get("title", ""))}</h1>
  <p class="page-subtitle">{esc(meta.get("page_subtitle", ""))}</p>
  <div class="page-meta">
    <span>{htmllib.escape(meta.get("subtitle", ""))}</span>
    <span>Audit run {htmllib.escape(meta.get("audit_date", ""))}</span>
    <span>{htmllib.escape(profile)} profile · canon filter applied</span>
  </div>

  <div class="lede">
    {n} place{"s" if n != 1 else ""} in {htmllib.escape(meta.get("title", "the source"))} where the text is unclear enough to produce litigation, with both sides' arguments and a likely outcome for each. Each scenario page lays out the situation, both sides' arguments, the likely outcome, and a proposed amendment. The full {source_noun.lower()} is at <a href="statute.html" style="color:var(--accent)">the {source_noun.lower()} page</a>; all proposed amendments are collected at <a href="redrafts.html" style="color:var(--accent)">redrafts</a>; the audit method is at <a href="methods.html" style="color:var(--accent)">methods</a>.
  </div>

  <h2 style="font-family:'{design["primary_font"]}',Georgia,serif; font-weight:500; font-size:28px; margin:48px 0 8px; letter-spacing:-0.005em;">The {n} scenarios</h2>

  <div class="scenario-grid">
{"".join(cards)}
  </div>

</div>
'''
    return head + body + page_footer(meta)

def render_statute_page(spec, design):
    meta = spec.get("meta", {})
    scenarios = spec.get("scenarios", [])
    profile = meta.get("profile", "statute")
    source_noun = PROFILE_SOURCE_NOUN.get(profile, "Source")

    sidebar_items = "".join(
        f'<li style="padding:10px 0; border-bottom:1px solid var(--border);">'
        f'<a href="scenario-{s["id"]}.html" style="text-decoration:none; color:var(--text); font-family:\'{design["serif_font"]}\',Georgia,serif; font-size:15px; display:flex; gap:10px; align-items:baseline;">'
        f'<span style="font-family:\'{design["body_font"]}\',sans-serif; font-weight:700; color:var(--accent); font-size:13px;">S-{s["id"]}</span>'
        f'<span>{htmllib.escape(s.get("title", ""))}</span></a></li>'
        for s in scenarios
    )

    head = page_chrome(
        title=f'The {source_noun} · {meta.get("title", "")}',
        design=design,
        active_nav="statute",
        profile=profile,
        brand_short=meta.get("brand_short", meta.get("title", "")),
        brand_sub=meta.get("brand_sub", ""),
    )
    body = f'''<div class="wrap">
  <div class="breadcrumb"><a href="index.html">Overview</a><span class="sep">›</span><span>The {source_noun}</span></div>
  <div class="kicker">Source text</div>
  <h1 class="page-title">{htmllib.escape(meta.get("subtitle", meta.get("title", "")))}</h1>
  <p class="page-subtitle">{htmllib.escape(meta.get("title", ""))}. Numbered badges next to a provision link to the scenarios that attack it; hover for the scenario title.</p>

  <div style="display:grid; grid-template-columns: minmax(0, 2.2fr) minmax(0, 1fr); gap:32px; margin-top:36px; align-items:start;">
    {render_statute_html(spec, link_mode="multi")}

    <aside style="position:sticky; top:24px;">
      <div style="background:var(--bg-card); border:1px solid var(--border); border-radius:10px; padding:22px 24px;">
        <div style="font-family:'{design["body_font"]}',sans-serif; font-size:11px; text-transform:uppercase; letter-spacing:0.14em; color:var(--text-faint); font-weight:700; margin-bottom:12px;">The {len(scenarios)} scenarios</div>
        <ol style="list-style:none; padding:0; margin:0;">{sidebar_items}</ol>
      </div>
    </aside>
  </div>
</div>
'''
    return head + body + page_footer(meta)

def render_scenario_page(scen, spec, design):
    meta = spec.get("meta", {})
    scenarios = spec.get("scenarios", [])
    families_block = spec.get("families")
    source_index = build_source_index(spec)
    profile = meta.get("profile", "statute")
    sid = scen["id"]

    # Anchored excerpts
    excerpts = ""
    for a in scen.get("anchors", []):
        info = source_index.get(a, {})
        excerpts += (
            f'<div class="excerpt-card">'
            f'<span class="prov-label">{info.get("label", a)}</span>{render_em(info.get("text", ""), [])}'
            f'<a class="read-more" href="statute.html#prov-{a}">Read in context →</a></div>'
        )

    # Related scenarios (sharing anchor or family)
    rel_items = []
    for other in scenarios:
        if other["id"] == sid:
            continue
        shared_anchors = set(scen.get("anchors", [])) & set(other.get("anchors", []))
        shared_fams = set(scen.get("families", [])) & set(other.get("families", []))
        if shared_anchors or shared_fams:
            tags = [source_index.get(a, {}).get("label", a) for a in shared_anchors]
            tags += [family_label(f, families_block) for f in shared_fams]
            rel_items.append(
                f'<a href="scenario-{other["id"]}.html">S-{other["id"]} · {htmllib.escape(other.get("title", ""))}'
                f' <span style="color:var(--text-faint); font-size:12px;">— shared: {" · ".join(tags)}</span></a>'
            )
    rel_html = ""
    if rel_items:
        rel_html = '<div class="related"><h3>Related scenarios</h3><div class="related-list">' + "".join(rel_items) + '</div></div>'

    # Prev/next
    prev_s = next((s for s in scenarios if s["id"] == sid - 1), None)
    next_s = next((s for s in scenarios if s["id"] == sid + 1), None)
    prev_html = (f'<a class="prevnext-card prev" href="scenario-{prev_s["id"]}.html"><div class="prevnext-dir">← Previous</div><div class="prevnext-title">S-{prev_s["id"]} · {htmllib.escape(prev_s.get("title", ""))}</div></a>'
                 if prev_s else '<div class="prevnext-card prev disabled"><div class="prevnext-dir">← Previous</div><div class="prevnext-title">— first scenario —</div></div>')
    next_html = (f'<a class="prevnext-card next" href="scenario-{next_s["id"]}.html"><div class="prevnext-dir">Next →</div><div class="prevnext-title">S-{next_s["id"]} · {htmllib.escape(next_s.get("title", ""))}</div></a>'
                 if next_s else '<div class="prevnext-card next disabled"><div class="prevnext-dir">Next →</div><div class="prevnext-title">— last scenario —</div></div>')

    positions = scen.get("positions", [])
    pos_a = positions[0] if len(positions) > 0 else {"label": "Position A", "actor": "", "argument": ""}
    pos_b = positions[1] if len(positions) > 1 else {"label": "Position B", "actor": "", "argument": ""}

    head = page_chrome(
        title=f'S-{sid} · {scen.get("title", "")} — {meta.get("title", "")}',
        design=design,
        active_nav="scenarios",
        profile=profile,
        brand_short=meta.get("brand_short", meta.get("title", "")),
        brand_sub=meta.get("brand_sub", ""),
    )
    body = f'''<div class="wrap-narrow">
  <div class="breadcrumb"><a href="index.html">Overview</a><span class="sep">›</span><a href="index.html">Scenarios</a><span class="sep">›</span><span>S-{sid}</span></div>
  <div class="kicker">Scenario {sid} of {len(scenarios)}</div>
  <h1 class="page-title">{htmllib.escape(scen.get("title", ""))}</h1>
  <p class="page-subtitle">{esc(scen.get("tagline", ""))}</p>
  <div class="pill-row" style="margin-top:18px;">
    {render_anchor_pills(scen.get("anchors", []), source_index, link_mode="multi")}
    {render_family_pills(scen.get("families", []), families_block, link_mode="multi")}
  </div>

  <div class="situation">
    <span class="situation-label">The situation</span>
    {esc(scen.get("situation", ""))}
  </div>

  <div class="sides">
    <div class="side side-dept">
      <div class="side-header">{htmllib.escape(pos_a.get("label", "Position A"))} <span class="side-actor">— {htmllib.escape(pos_a.get("actor", ""))}</span></div>
      {esc(pos_a.get("argument", ""))}
    </div>
    <div class="side side-adv">
      <div class="side-header">{htmllib.escape(pos_b.get("label", "Position B"))} <span class="side-actor">— {htmllib.escape(pos_b.get("actor", ""))}</span></div>
      {esc(pos_b.get("argument", ""))}
    </div>
  </div>

  <div class="analysis">
    <div class="analysis-row">
      <div class="analysis-label">Weak point</div>
      <div class="analysis-body">{esc(scen.get("weak_point", ""))}</div>
    </div>
    <div class="analysis-row">
      <div class="analysis-label">Likely outcome</div>
      <div class="analysis-body">{esc(scen.get("likely_outcome", ""))}</div>
    </div>
  </div>

  <div class="redraft">
    <div class="redraft-label">Proposed amendment</div>
    <div class="redraft-body">{esc(scen.get("redraft", ""))}</div>
  </div>

  <div class="anchored-excerpt">
    <h3>Anchored in the {PROFILE_SOURCE_NOUN.get(profile, "source").lower()}</h3>
    {excerpts}
  </div>

  {rel_html}

  <div class="prevnext">{prev_html}{next_html}</div>
</div>
'''
    return head + body + page_footer(meta)

def render_families_page(spec, design):
    meta = spec.get("meta", {})
    scenarios = spec.get("scenarios", [])
    families_block = spec.get("families")
    used_keys = all_family_keys(spec)
    profile = meta.get("profile", "statute")

    blocks = []
    for k in used_keys:
        # find description
        desc = ""
        diagnostic = ""
        for f in (families_block or []):
            if f.get("key") == k:
                desc = f.get("description", "")
                diagnostic = f.get("diagnostic", "")
                break
        label = family_label(k, families_block)
        scen_in = [s for s in scenarios if k in s.get("families", [])]
        lst = "".join(
            f'<li><a href="scenario-{s["id"]}.html"><span class="num">S-{s["id"]}</span>{htmllib.escape(s.get("title", ""))}</a></li>'
            for s in scen_in
        )
        diag_html = f'<div class="family-test"><strong>Diagnostic:</strong> {esc(diagnostic)}</div>' if diagnostic else ""
        desc_html = f'<p class="family-intro">{esc(desc)}</p>' if desc else ""
        blocks.append(f'''
  <section class="family-block" data-fam="{k}" id="fam-{k}">
    <h2>{htmllib.escape(label)}</h2>
    {desc_html}
    {diag_html}
    <ul class="scenario-list">{lst}</ul>
  </section>''')

    head = page_chrome(
        title=f'Defect Families · {meta.get("title", "")}',
        design=design,
        active_nav="families",
        profile=profile,
        brand_short=meta.get("brand_short", meta.get("title", "")),
        brand_sub=meta.get("brand_sub", ""),
    )
    body = f'''<div class="wrap-narrow">
  <div class="breadcrumb"><a href="index.html">Overview</a><span class="sep">›</span><span>Defect Families</span></div>
  <div class="kicker">The taxonomy</div>
  <h1 class="page-title">Defect families that show up here</h1>
  <p class="page-subtitle">Each family groups scenarios of the same kind — what the dispute will look like and what kind of fix will close it.</p>
{"".join(blocks)}
</div>
'''
    return head + body + page_footer(meta)

def render_redrafts_page(spec, design):
    meta = spec.get("meta", {})
    scenarios = spec.get("scenarios", [])
    source_index = build_source_index(spec)
    profile = meta.get("profile", "statute")

    blocks = []
    for s in scenarios:
        if not s.get("redraft"):
            continue
        anchors_str = ", ".join(source_index.get(a, {}).get("label", a) for a in s.get("anchors", []))
        blocks.append(f'''
  <section class="redraft-block" id="r{s["id"]}">
    <div class="redraft-block-header">
      <h2>R-{s["id"]} · {htmllib.escape(s.get("title", ""))}</h2>
      <span class="target-prov">Amends {anchors_str}</span>
    </div>
    <p class="problem">{esc(s.get("weak_point", ""))}</p>
    <div class="proposal">{esc(s.get("redraft", ""))}</div>
    <div class="source-link"><a href="scenario-{s["id"]}.html">Originating scenario: S-{s["id"]} →</a></div>
  </section>''')

    head = page_chrome(
        title=f'Redrafts · {meta.get("title", "")}',
        design=design,
        active_nav="redrafts",
        profile=profile,
        brand_short=meta.get("brand_short", meta.get("title", "")),
        brand_sub=meta.get("brand_sub", ""),
    )
    body = f'''<div class="wrap-narrow">
  <div class="breadcrumb"><a href="index.html">Overview</a><span class="sep">›</span><span>Redrafts</span></div>
  <div class="kicker">Amendment package</div>
  <h1 class="page-title">Proposed amendments</h1>
  <p class="page-subtitle">Each scenario produced a textual cure — collected here as a single amendment package.</p>

  <div class="lede" style="margin-top:32px;">
    Each redraft closes an ambiguity by picking a direction. A drafter who wants the opposite policy can usually flip the language and reuse the structure. Read the problem statement first, then the proposal. The link at the bottom of each block returns to the originating scenario for the full analysis.
  </div>
{"".join(blocks)}
</div>
'''
    return head + body + page_footer(meta)

def render_methods_page(spec, design):
    meta = spec.get("meta", {})
    methodology = spec.get("methodology", {})
    coverage = spec.get("coverage_list", [])
    profile = meta.get("profile", "statute")

    def para_block(key, heading):
        paras = methodology.get(key, [])
        if not paras:
            return ""
        para_html = "".join(f"<p>{esc(p)}</p>" for p in paras)
        return f'<h2>{htmllib.escape(heading)}</h2>{para_html}'

    coverage_html = ""
    if coverage:
        items = "".join(
            f'<li><strong>{htmllib.escape(c.get("label", ""))}</strong>{esc(c.get("note", ""))}</li>'
            for c in coverage
        )
        coverage_html = f'''
    <h2 id="coverage">Coverage list — additional flagged ambiguities</h2>
    <p>Items the scan surfaced that were not developed into full scenarios.</p>
    <ul class="coverage-grid">{items}</ul>'''

    prov = methodology.get("provenance", f"Generated by the ambiguity-report skill on {meta.get('audit_date', '')}, {profile} profile, with the canon filter applied.")

    head = page_chrome(
        title=f'Methodology · {meta.get("title", "")}',
        design=design,
        active_nav="methods",
        profile=profile,
        brand_short=meta.get("brand_short", meta.get("title", "")),
        brand_sub=meta.get("brand_sub", ""),
    )
    body = f'''<div class="wrap-narrow">
  <div class="breadcrumb"><a href="index.html">Overview</a><span class="sep">›</span><span>Methodology</span></div>
  <div class="kicker">How this audit was run</div>
  <h1 class="page-title">Methodology</h1>
  <p class="page-subtitle">How the scenarios were generated, what got filtered out, and what the audit does not do.</p>

  <div class="prose">
{para_block("workflow", "The workflow")}
{para_block("filter", "The canon filter")}
{para_block("profile", "Audit profile")}
{para_block("scope", "What this audit does not do")}
{coverage_html}
{para_block("research", "Research notes")}
    <h2>Provenance</h2>
    <p>{esc(prov)}</p>
  </div>
</div>
'''
    return head + body + page_footer(meta)

# -------------------------------------------------------------------------
# Single-page renderer
# -------------------------------------------------------------------------

def render_single_page(spec, design):
    meta = spec.get("meta", {})
    scenarios = spec.get("scenarios", [])
    families_block = spec.get("families")
    used_keys = all_family_keys(spec)
    source_index = build_source_index(spec)
    profile = meta.get("profile", "statute")

    # Filter chips
    chips = ['<button class="sp-chip active" data-family="all">All</button>']
    for k in used_keys:
        chips.append(f'<button class="sp-chip" data-family="{k}"><span class="sp-chip-dot" style="background:var(--fam-{k}-fg);"></span>{htmllib.escape(family_label(k, families_block))}</button>')

    # Scenario cards
    cards = []
    for s in scenarios:
        positions = s.get("positions", [])
        pos_a = positions[0] if len(positions) > 0 else {"label": "Position A", "actor": "", "argument": ""}
        pos_b = positions[1] if len(positions) > 1 else {"label": "Position B", "actor": "", "argument": ""}
        cards.append(f'''
    <article class="sp-scenario scenario" id="scenario-{s["id"]}" data-families="{",".join(s.get("families", []))}" data-anchors="{",".join(s.get("anchors", []))}">
      <div class="sp-scenario-header">
        <div class="sp-scenario-num">S-{s["id"]}</div>
        <div class="sp-scenario-title-block">
          <h3 class="sp-scenario-title">{htmllib.escape(s.get("title", ""))}</h3>
          <div class="pill-row">
            {render_anchor_pills(s.get("anchors", []), source_index, link_mode="single")}
            {render_family_pills(s.get("families", []), families_block, link_mode="single")}
          </div>
        </div>
      </div>
      <div class="situation">
        <span class="situation-label">The situation</span>
        {esc(s.get("situation", ""))}
      </div>
      <div class="sides">
        <div class="side side-dept">
          <div class="side-header">{htmllib.escape(pos_a.get("label", "Position A"))} <span class="side-actor">— {htmllib.escape(pos_a.get("actor", ""))}</span></div>
          {esc(pos_a.get("argument", ""))}
        </div>
        <div class="side side-adv">
          <div class="side-header">{htmllib.escape(pos_b.get("label", "Position B"))} <span class="side-actor">— {htmllib.escape(pos_b.get("actor", ""))}</span></div>
          {esc(pos_b.get("argument", ""))}
        </div>
      </div>
      <div class="analysis">
        <div class="analysis-row">
          <div class="analysis-label">Weak point</div>
          <div class="analysis-body">{esc(s.get("weak_point", ""))}</div>
        </div>
        <div class="analysis-row">
          <div class="analysis-label">Likely outcome</div>
          <div class="analysis-body">{esc(s.get("likely_outcome", ""))}</div>
        </div>
      </div>
      <div class="redraft">
        <div class="redraft-label">Proposed amendment</div>
        <div class="redraft-body">{esc(s.get("redraft", ""))}</div>
      </div>
    </article>''')

    n = len(scenarios)
    source_noun = PROFILE_SOURCE_NOUN.get(profile, "Source")

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{htmllib.escape(meta.get("title", "Ambiguity Report"))}</title>
{google_font_url(design)}
<link rel="stylesheet" href="style.css">
</head>
<body>

<div class="wrap">

  <header class="masthead" style="border-bottom:1px solid var(--border); padding-bottom:32px; margin-bottom:32px;">
    <div class="kicker">{htmllib.escape(meta.get("kicker", ""))}</div>
    <h1 class="page-title">{htmllib.escape(meta.get("title", ""))}</h1>
    <p class="page-subtitle">{esc(meta.get("page_subtitle", ""))}</p>
    <div class="page-meta">
      <span>{htmllib.escape(meta.get("subtitle", ""))}</span>
      <span>Audit run {htmllib.escape(meta.get("audit_date", ""))}</span>
      <span>{htmllib.escape(profile)} profile · canon filter applied</span>
    </div>
  </header>

  <div class="sp-filter-row">
    <span class="sp-filter-label">Filter:</span>
    {"".join(chips)}
  </div>

  <div class="sp-layout">
    <aside class="sp-statute-pane">
      <h2 style="font-family:'{design["primary_font"]}',Georgia,serif; font-weight:500; font-size:20px; margin:0 0 12px;">The {source_noun}</h2>
      {render_statute_html(spec, link_mode="single")}
    </aside>
    <section>
      <h2 style="font-family:'{design["primary_font"]}',Georgia,serif; font-weight:500; font-size:22px; margin:0 0 16px;">The {n} scenarios</h2>
      {"".join(cards)}
    </section>
  </div>

</div>

<script>
document.querySelectorAll(".sp-chip").forEach(chip => {{
  chip.addEventListener("click", () => {{
    document.querySelectorAll(".sp-chip").forEach(c => c.classList.remove("active"));
    chip.classList.add("active");
    const fam = chip.dataset.family;
    document.querySelectorAll(".sp-scenario").forEach(card => {{
      if (fam === "all") {{ card.classList.remove("dim"); return; }}
      const fams = (card.dataset.families || "").split(",");
      card.classList.toggle("dim", !fams.includes(fam));
    }});
  }});
}});
document.querySelectorAll(".anchor-pill").forEach(p => {{
  p.addEventListener("click", e => {{
    const target = p.getAttribute("href");
    if (target && target.startsWith("#prov-")) {{
      const el = document.querySelector(target);
      if (el) {{
        document.querySelectorAll(".prov, .subprov").forEach(x => x.classList.remove("highlighted"));
        el.classList.add("highlighted");
      }}
    }}
  }});
}});
document.querySelectorAll(".scenario-badge").forEach(b => {{
  b.addEventListener("click", e => {{
    const target = b.getAttribute("href");
    if (target && target.startsWith("#scenario-")) {{
      const el = document.querySelector(target);
      if (el) {{
        el.scrollIntoView({{behavior: "smooth", block: "center"}});
        el.style.boxShadow = "0 0 0 3px var(--highlight-strong)";
        setTimeout(() => el.style.boxShadow = "", 1600);
      }}
    }}
  }});
}});
</script>

</body>
</html>'''

# -------------------------------------------------------------------------
# Netlify config
# -------------------------------------------------------------------------

NETLIFY_TOML = '''[build]
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "SAMEORIGIN"
    X-Content-Type-Options = "nosniff"
'''

# -------------------------------------------------------------------------
# Main
# -------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Render an ambiguity-report spec into a website.")
    ap.add_argument("--spec", required=True, help="Path to spec.json")
    ap.add_argument("--out", required=True, help="Output directory")
    ap.add_argument("--mode", choices=["multi", "single"], default="multi", help="Site mode")
    ap.add_argument("--no-netlify-toml", action="store_true", help="Skip writing netlify.toml")
    args = ap.parse_args()

    with open(args.spec) as f:
        spec = json.load(f)

    design = merge_design(spec.get("design"))
    family_palette = merge_family_palette((spec.get("design") or {}).get("family_palette"))

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    # CSS
    script_dir = Path(__file__).resolve().parent
    css_path = script_dir.parent / "assets" / "site-style.css"
    css_source = css_path.read_text()
    patched = patched_css(css_source, design, family_palette)
    (out_dir / "style.css").write_text(patched)

    if args.mode == "single":
        (out_dir / "index.html").write_text(render_single_page(spec, design))
    else:
        (out_dir / "index.html").write_text(render_index_html(spec, design))
        (out_dir / "statute.html").write_text(render_statute_page(spec, design))
        for s in spec.get("scenarios", []):
            (out_dir / f"scenario-{s['id']}.html").write_text(render_scenario_page(s, spec, design))
        (out_dir / "families.html").write_text(render_families_page(spec, design))
        (out_dir / "redrafts.html").write_text(render_redrafts_page(spec, design))
        (out_dir / "methods.html").write_text(render_methods_page(spec, design))

    if not args.no_netlify_toml:
        (out_dir / "netlify.toml").write_text(NETLIFY_TOML)

    print(f"Site written to: {out_dir}")
    print(f"Mode: {args.mode}")
    files = sorted(p.name for p in out_dir.iterdir())
    print(f"Files: {len(files)}")
    for fname in files:
        print(f"  {fname}")

if __name__ == "__main__":
    main()
