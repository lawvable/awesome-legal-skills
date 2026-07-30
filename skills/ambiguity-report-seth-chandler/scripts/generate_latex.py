#!/usr/bin/env python3
"""
generate_latex.py — Render an ambiguity-report spec.json into a self-contained .tex file.

Usage:
    python generate_latex.py --spec PATH --out FILE.tex

The output is a single LaTeX file (article class) ready to compile with
latexmk -pdf or pdflatex (twice for cross-references). All preamble is
inline. Custom colors from spec['design'] are substituted into the preamble.
"""

import argparse
import json
import re
from pathlib import Path

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
    "border_color":     "#e3dcca",
    "text_color":       "#1f1b16",
    "text_soft":        "#5b524a",
    "text_faint":       "#8a8276",
    "highlight":        "#fdf2c4",
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
    "statute":    "statute",
    "contract":   "contract",
    "regulation": "regulation",
    "opinion":    "opinion",
}

# -------------------------------------------------------------------------
# LaTeX escaping
# -------------------------------------------------------------------------

LATEX_SPECIAL = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}

def tex_escape(text):
    """Escape a plain-text string for LaTeX. Also converts <em>/<strong> tags."""
    if text is None:
        return ""
    # Convert HTML em/strong tags to LaTeX before escaping the rest
    # Use placeholders so the tag-internal text gets escaped too
    out = text
    # Process inside-tag content separately
    placeholders = []
    def stash_em(m):
        placeholders.append(("emph", m.group(1)))
        return f"@@PLACE{len(placeholders)-1}@@"
    def stash_strong(m):
        placeholders.append(("strong", m.group(1)))
        return f"@@PLACE{len(placeholders)-1}@@"
    out = re.sub(r"<em>(.*?)</em>", stash_em, out, flags=re.DOTALL)
    out = re.sub(r"<strong>(.*?)</strong>", stash_strong, out, flags=re.DOTALL)

    # Escape special chars
    for ch, repl in LATEX_SPECIAL.items():
        out = out.replace(ch, repl)
    # Smart quotes
    out = out.replace("—", "---").replace("–", "--").replace("…", r"\ldots{}")
    # Curly quotes
    out = out.replace("“", "``").replace("”", "''")
    out = out.replace("‘", "`").replace("’", "'")

    # Replace placeholders with the escaped content wrapped in LaTeX commands
    def restore(m):
        idx = int(m.group(1))
        kind, content = placeholders[idx]
        escaped_content = content
        for ch, repl in LATEX_SPECIAL.items():
            escaped_content = escaped_content.replace(ch, repl)
        escaped_content = escaped_content.replace("—", "---").replace("–", "--")
        escaped_content = escaped_content.replace("“", "``").replace("”", "''")
        escaped_content = escaped_content.replace("‘", "`").replace("’", "'")
        if kind == "emph":
            return r"\emph{" + escaped_content + "}"
        else:
            return r"\textbf{" + escaped_content + "}"
    out = re.sub(r"@@PLACE(\d+)@@", restore, out)
    return out

def hex_to_html_color(hex_str):
    return hex_str.lstrip("#").upper()

def merge_design(spec_design):
    out = dict(DEFAULT_DESIGN)
    out.update(spec_design or {})
    return out

# -------------------------------------------------------------------------
# Preamble
# -------------------------------------------------------------------------

def render_preamble(design):
    color_defs = "\n".join([
        f"\\definecolor{{accentColor}}{{HTML}}{{{hex_to_html_color(design['accent_color'])}}}",
        f"\\definecolor{{accentSoft}}{{HTML}}{{{hex_to_html_color(design['accent_soft'])}}}",
        f"\\definecolor{{accentDeep}}{{HTML}}{{{hex_to_html_color(design['accent_deep'])}}}",
        f"\\definecolor{{deptColor}}{{HTML}}{{{hex_to_html_color(design['dept_color'])}}}",
        f"\\definecolor{{deptBg}}{{HTML}}{{{hex_to_html_color(design['dept_bg'])}}}",
        f"\\definecolor{{advColor}}{{HTML}}{{{hex_to_html_color(design['adv_color'])}}}",
        f"\\definecolor{{advBg}}{{HTML}}{{{hex_to_html_color(design['adv_bg'])}}}",
        f"\\definecolor{{bgColor}}{{HTML}}{{{hex_to_html_color(design['background_color'])}}}",
        f"\\definecolor{{panelColor}}{{HTML}}{{{hex_to_html_color(design['panel_color'])}}}",
        f"\\definecolor{{cardColor}}{{HTML}}{{{hex_to_html_color(design['card_color'])}}}",
        f"\\definecolor{{textColor}}{{HTML}}{{{hex_to_html_color(design['text_color'])}}}",
        f"\\definecolor{{textSoft}}{{HTML}}{{{hex_to_html_color(design['text_soft'])}}}",
        f"\\definecolor{{textFaint}}{{HTML}}{{{hex_to_html_color(design['text_faint'])}}}",
        f"\\definecolor{{borderColor}}{{HTML}}{{{hex_to_html_color(design['border_color'])}}}",
        f"\\definecolor{{highlightColor}}{{HTML}}{{{hex_to_html_color(design['highlight'])}}}",
        "\\definecolor{redraftBg}{HTML}{F7F2E3}",
        "\\definecolor{redraftBorder}{HTML}{E8DFBE}",
    ])
    return r"""\documentclass[11pt,letterpaper]{article}
\usepackage[margin=1in]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{microtype}
\linespread{1.05}
\usepackage{xcolor}
""" + color_defs + r"""
\usepackage[most]{tcolorbox}
\tcbset{
  situationbox/.style={
    enhanced, colback=panelColor, colframe=accentSoft,
    boxrule=0pt, leftrule=2pt, arc=2pt,
    left=12pt, right=12pt, top=10pt, bottom=10pt,
  },
  positionA/.style={
    enhanced, colback=deptBg, colframe=deptColor,
    boxrule=0pt, toprule=2pt, arc=2pt,
    left=12pt, right=12pt, top=10pt, bottom=10pt,
  },
  positionB/.style={
    enhanced, colback=advBg, colframe=advColor,
    boxrule=0pt, toprule=2pt, arc=2pt,
    left=12pt, right=12pt, top=10pt, bottom=10pt,
  },
  redraftbox/.style={
    enhanced, colback=redraftBg, colframe=redraftBorder,
    boxrule=0.5pt, arc=2pt,
    left=12pt, right=12pt, top=10pt, bottom=10pt,
  },
  excerptbox/.style={
    enhanced, colback=cardColor, colframe=accentColor,
    boxrule=0pt, leftrule=3pt, arc=2pt,
    left=12pt, right=12pt, top=8pt, bottom=8pt,
  }
}
\usepackage[colorlinks=true,linkcolor=accentDeep,urlcolor=accentDeep]{hyperref}
\usepackage{titlesec}
\titleformat*{\section}{\Large\bfseries\color{textColor}}
\titleformat*{\subsection}{\large\bfseries\color{textColor}}
\titleformat*{\subsubsection}{\normalsize\bfseries\color{accentColor}}
\usepackage{enumitem}
\setlist[description]{style=nextline, leftmargin=*}
\pagecolor{bgColor}
\color{textColor}

\newcommand{\kicker}[1]{{\footnotesize\textsc{\color{accentColor}#1}}}
\newcommand{\anchorpill}[1]{\textcolor{accentColor}{\fbox{\footnotesize\textsf{\S\,#1}}}}
\newcommand{\familypill}[1]{{\footnotesize\textsf{\textcolor{textFaint}{[#1]}}}}
\newcommand{\actor}[1]{{\scshape\small\color{textFaint}#1}}
\newcommand{\redraftlabel}{{\footnotesize\textsc{\bfseries\color{accentColor}Proposed amendment}\par\medskip}}
\newcommand{\sidelabelA}[1]{{\footnotesize\textsf{\textbf{\color{deptColor}#1}}}}
\newcommand{\sidelabelB}[1]{{\footnotesize\textsf{\textbf{\color{advColor}#1}}}}
"""

# -------------------------------------------------------------------------
# Source rendering
# -------------------------------------------------------------------------

def collect_scenarios_by_anchor(scenarios):
    by_anchor = {}
    for s in scenarios:
        for a in s.get("anchors", []):
            by_anchor.setdefault(a, []).append(s["id"])
    return by_anchor

def render_em_inline(text, emphasize):
    if not emphasize or not text:
        return text or ""
    out = text
    for phrase in emphasize:
        pattern = re.compile(r"(?<!<em>)(" + re.escape(phrase) + r")(?!</em>)")
        out = pattern.sub(r"<em>\1</em>", out, count=1)
    return out

def render_provision_tex(prov, scenarios_by_anchor, level=0):
    pid = prov.get("id", "")
    label = prov.get("label", "")
    text = render_em_inline(prov.get("text", ""), prov.get("emphasize", []))
    subs = prov.get("subprovisions", []) or []
    sids = scenarios_by_anchor.get(pid, [])

    out = ""
    if text:
        indent = r"\quad" * level
        badges = " ".join(rf"\anchorpill{{S-{s}}}" for s in sids)
        line = f"{indent}\\textbf{{{tex_escape(label)}}} {tex_escape(text)} {badges}"
        out += f"\\noindent {line}\\par\\medskip\n"
        if pid:
            out += rf"\hypertarget{{prov:{pid}}}{{}}" + "\n"
    for sub in subs:
        out += render_provision_tex(sub, scenarios_by_anchor, level + 1)
    return out

def render_source_section_tex(spec):
    source = spec.get("source", {})
    scenarios = spec.get("scenarios", [])
    scenarios_by_anchor = collect_scenarios_by_anchor(scenarios)
    out = "\\section*{The " + PROFILE_SOURCE_NOUN.get(spec.get("meta", {}).get("profile", "statute"), "source") + "}\n"
    out += "\\addcontentsline{toc}{section}{The source}\n"
    out += f"\\noindent\\textit{{{tex_escape(source.get('name', ''))}}}\\par\\bigskip\n"
    for sec in source.get("sections", []):
        if sec.get("subhead"):
            out += f"\\noindent\\textsc{{\\small {tex_escape(sec['subhead'])}}}\\par\\smallskip\n"
        if sec.get("text"):
            out += render_provision_tex(sec, scenarios_by_anchor, 0)
        for sub in sec.get("subprovisions", []) or []:
            out += render_provision_tex(sub, scenarios_by_anchor, 0)
        out += "\\par\\medskip\n"
    return out

# -------------------------------------------------------------------------
# Scenario rendering
# -------------------------------------------------------------------------

def build_source_index(spec):
    idx = {}
    def walk(prov):
        if prov.get("id"):
            idx[prov["id"]] = {"label": prov.get("label", ""), "text": prov.get("text", "")}
        for sub in prov.get("subprovisions", []) or []:
            walk(sub)
    for sec in spec.get("source", {}).get("sections", []):
        walk(sec)
    return idx

def family_label(key, families_block):
    for f in (families_block or []):
        if f.get("key") == key:
            return f.get("label", DEFAULT_FAMILY_LABELS.get(key, key))
    return DEFAULT_FAMILY_LABELS.get(key, key)

def render_scenarios_section_tex(spec):
    scenarios = spec.get("scenarios", [])
    families_block = spec.get("families")
    source_index = build_source_index(spec)
    n = len(scenarios)
    profile = spec.get("meta", {}).get("profile", "statute")

    out = f"\\section*{{The {n} scenarios}}\n"
    out += "\\addcontentsline{toc}{section}{The scenarios}\n\n"

    for s in scenarios:
        sid = s["id"]
        out += rf"\subsection*{{S-{sid} {{\large\color{{textFaint}} ·}} {tex_escape(s.get('title', ''))}}}" + "\n"
        out += rf"\hypertarget{{scen:{sid}}}{{}}" + "\n"
        if s.get("tagline"):
            out += rf"\noindent\textit{{{tex_escape(s['tagline'])}}}\par\smallskip" + "\n"

        anchors_tex = " ".join(rf"\anchorpill{{{source_index.get(a, {}).get('label', a)}}}" for a in s.get("anchors", []))
        fams_tex = " ".join(rf"\familypill{{{family_label(k, families_block)}}}" for k in s.get("families", []))
        if anchors_tex or fams_tex:
            out += rf"\noindent {anchors_tex}\quad {fams_tex}\par\medskip" + "\n"

        out += r"\begin{tcolorbox}[situationbox]" + "\n"
        out += rf"{{\footnotesize\textsc{{\color{{textFaint}}\bfseries The situation}}}}\par\smallskip" + "\n"
        out += rf"\itshape {tex_escape(s.get('situation', ''))}" + "\n"
        out += r"\end{tcolorbox}" + "\n\n"

        # Two-sides — use tcbraster
        positions = s.get("positions", [])
        pos_a = positions[0] if len(positions) > 0 else {"label": "Position A", "actor": "", "argument": ""}
        pos_b = positions[1] if len(positions) > 1 else {"label": "Position B", "actor": "", "argument": ""}
        out += r"\begin{tcbraster}[raster columns=2, raster column skip=4mm, raster equal height]" + "\n"
        out += r"\begin{tcolorbox}[positionA]" + "\n"
        out += rf"\sidelabelA{{{tex_escape(pos_a.get('label', 'Position A'))}}} \quad \actor{{{tex_escape(pos_a.get('actor', ''))}}}\par\medskip" + "\n"
        out += tex_escape(pos_a.get("argument", "")) + "\n"
        out += r"\end{tcolorbox}" + "\n"
        out += r"\begin{tcolorbox}[positionB]" + "\n"
        out += rf"\sidelabelB{{{tex_escape(pos_b.get('label', 'Position B'))}}} \quad \actor{{{tex_escape(pos_b.get('actor', ''))}}}\par\medskip" + "\n"
        out += tex_escape(pos_b.get("argument", "")) + "\n"
        out += r"\end{tcolorbox}" + "\n"
        out += r"\end{tcbraster}" + "\n\n"

        if s.get("weak_point"):
            out += rf"\noindent\textbf{{Weak point.}}\quad {tex_escape(s['weak_point'])}\par\medskip" + "\n"
        if s.get("likely_outcome"):
            out += rf"\noindent\textbf{{Likely outcome.}}\quad {tex_escape(s['likely_outcome'])}\par\medskip" + "\n"

        if s.get("redraft"):
            out += r"\begin{tcolorbox}[redraftbox]" + "\n"
            out += r"\redraftlabel" + "\n"
            out += rf"\itshape {tex_escape(s['redraft'])}" + "\n"
            out += r"\end{tcolorbox}" + "\n\n"

        out += r"\medskip\hrule\bigskip" + "\n\n"

    return out

# -------------------------------------------------------------------------
# Redrafts section
# -------------------------------------------------------------------------

def render_redrafts_tex(spec):
    scenarios = spec.get("scenarios", [])
    source_index = build_source_index(spec)
    if not any(s.get("redraft") for s in scenarios):
        return ""
    out = "\\section*{Proposed amendments}\n"
    out += "\\addcontentsline{toc}{section}{Proposed amendments}\n\n"
    out += "\\noindent Each redraft below closes one ambiguity. A drafter who wants the opposite policy can usually flip the language and reuse the structure.\\par\\bigskip\n"
    for s in scenarios:
        if not s.get("redraft"):
            continue
        anchors = ", ".join(source_index.get(a, {}).get("label", a) for a in s.get("anchors", []))
        out += rf"\subsection*{{R-{s['id']} · {tex_escape(s.get('title', ''))}}}" + "\n"
        out += rf"\noindent\textit{{Amends {tex_escape(anchors)}}}\par\smallskip" + "\n"
        if s.get("weak_point"):
            out += rf"\noindent {tex_escape(s['weak_point'])}\par\medskip" + "\n"
        out += r"\begin{tcolorbox}[redraftbox]" + "\n"
        out += rf"\itshape {tex_escape(s['redraft'])}" + "\n"
        out += r"\end{tcolorbox}" + "\n"
        out += rf"\noindent\hyperlink{{scen:{s['id']}}}{{See scenario S-{s['id']}.}}\par\bigskip" + "\n\n"
    return out

# -------------------------------------------------------------------------
# Coverage + methodology
# -------------------------------------------------------------------------

def render_coverage_tex(spec):
    coverage = spec.get("coverage_list", [])
    if not coverage:
        return ""
    out = "\\section*{Additional ambiguities flagged}\n"
    out += "\\addcontentsline{toc}{section}{Additional ambiguities}\n\n"
    out += "\\noindent Items the scan surfaced that were not developed into full scenarios.\\par\\medskip\n"
    out += r"\begin{description}" + "\n"
    for c in coverage:
        out += rf"\item[{tex_escape(c.get('label', ''))}] {tex_escape(c.get('note', ''))}" + "\n"
    out += r"\end{description}" + "\n\n"
    return out

def render_methodology_tex(spec):
    m = spec.get("methodology", {})
    meta = spec.get("meta", {})
    if not m and not meta.get("audit_date"):
        return ""
    out = "\\section*{Methodology}\n"
    out += "\\addcontentsline{toc}{section}{Methodology}\n\n"

    def block(key, heading):
        paras = m.get(key, [])
        if not paras:
            return ""
        s = rf"\subsection*{{{heading}}}" + "\n"
        for p in paras:
            s += rf"\noindent {tex_escape(p)}\par\medskip" + "\n"
        return s

    out += block("workflow", "The workflow")
    out += block("filter", "The canon filter")
    out += block("profile", "Audit profile")
    out += block("scope", "What this audit does not do")
    out += block("research", "Research notes")

    prov = m.get("provenance", f"Generated by the ambiguity-report skill on {meta.get('audit_date', '')}, {meta.get('profile', 'statute')} profile, with the canon filter applied.")
    out += rf"\subsection*{{Provenance}}" + "\n"
    out += rf"\noindent\textit{{{tex_escape(prov)}}}\par" + "\n\n"
    return out

# -------------------------------------------------------------------------
# Front matter
# -------------------------------------------------------------------------

def render_frontmatter(spec):
    meta = spec.get("meta", {})
    out = r"\begin{document}" + "\n"
    out += r"\thispagestyle{empty}" + "\n\n"
    out += r"\vspace*{2cm}" + "\n"
    out += rf"\noindent\kicker{{{tex_escape(meta.get('kicker', 'Interpretive-Ambiguity Stress-Test'))}}}\par\bigskip" + "\n"
    out += rf"{{\Huge\bfseries {tex_escape(meta.get('title', ''))}}}\par\bigskip" + "\n"
    if meta.get("subtitle"):
        out += rf"{{\Large\itshape\color{{textSoft}} {tex_escape(meta['subtitle'])}}}\par\bigskip" + "\n"
    if meta.get("page_subtitle"):
        out += rf"\noindent\textit{{\large {tex_escape(meta['page_subtitle'])}}}\par\bigskip" + "\n"
    out += r"\vspace{1cm}" + "\n"
    out += rf"\noindent\textsf{{\footnotesize Audit run {tex_escape(meta.get('audit_date', ''))} \quad · \quad {tex_escape(meta.get('profile', 'statute'))} profile \quad · \quad canon filter applied}}\par" + "\n"
    out += r"\vspace{2cm}" + "\n"
    # Scenarios table of contents
    scenarios = spec.get("scenarios", [])
    if scenarios:
        out += rf"\noindent\textbf{{\large The {len(scenarios)} scenarios}}\par\smallskip" + "\n"
        out += r"\begin{description}" + "\n"
        for s in scenarios:
            out += rf"\item[\textsf{{S-{s['id']}}}] \hyperlink{{scen:{s['id']}}}{{{tex_escape(s.get('title', ''))}}}" + "\n"
        out += r"\end{description}" + "\n\n"
    out += r"\clearpage" + "\n\n"
    return out

# -------------------------------------------------------------------------
# Main
# -------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Render an ambiguity-report spec into a .tex file.")
    ap.add_argument("--spec", required=True, help="Path to spec.json")
    ap.add_argument("--out", required=True, help="Output .tex path")
    args = ap.parse_args()

    with open(args.spec) as f:
        spec = json.load(f)
    design = merge_design(spec.get("design"))

    parts = [
        render_preamble(design),
        render_frontmatter(spec),
        render_source_section_tex(spec),
        render_scenarios_section_tex(spec),
        render_redrafts_tex(spec),
        render_coverage_tex(spec),
        render_methodology_tex(spec),
        r"\end{document}" + "\n",
    ]

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(parts))
    print(f"LaTeX written to: {out_path}")
    print(f"Compile with: latexmk -pdf {out_path.name}")

if __name__ == "__main__":
    main()
