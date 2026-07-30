import argparse, json, os, sys
from pathlib import Path

MERMAID_VERSION = "11.15.0"

# ── UI chrome strings (W3.5 scaffolding; W5 owns the full UX pass) ────────────

# Per-language chrome strings injected into assets/html_template.html.  The
# table swaps labels only; matter text (diagram, figure description, digest
# rows) stays verbatim source language.  disclaimer_html is raw inner HTML
# (rendered with | safe), so the EN banner keeps its existing markup verbatim.
UI_STRINGS: dict[str, dict[str, str]] = {
    "en": {
        "tab_overview": "Overview",
        "tab_how_to_read": "How to Read",
        "tab_observations": "Observations",
        "tab_limitations": "⚠ Limitations",
        "tab_source_docs": "Source Docs",
        "panel_overview": "Overview",
        "panel_how_to_read": "How to Read",
        "panel_observations": "Key Observations",
        "panel_limitations": "Limitations",
        "panel_source_docs": "Source Docs",
        "ctrl_zoom_in": "Zoom in",
        "ctrl_zoom_out": "Zoom out",
        "ctrl_reset": "Reset",
        "ctrl_contrast": "High contrast",
        "ctrl_flip": "Flip",
        "ctrl_fullscreen": "Full screen",
        "ctrl_exit_fullscreen": "Exit fullscreen (Esc)",
        "ctrl_exit_fullscreen_label": "✕ Exit",
        "export_svg": "Sharp vector (SVG), best for printing and slides",
        "export_png": "Picture (PNG), best for email and Word",
        "export_html": "This whole page (HTML)",
        "export_title": "Save / Export",
        "edit_source": "✎ Edit Source",
        "edit_title": "Edit",
        # W5.3 editor strings
        "editor_summary": "Advanced: edit the diagram's drawing instructions",
        "editor_warning": "Changes here affect the picture only, not your documents.",
        "rerender": "Re-draw",
        "cancel": "Cancel",
        "disclaimer_html": (
            '🤖 GenAI Output &nbsp;·&nbsp; Visual aid only. '
            '<span class="not-advice">Not legal advice.</span> '
            'Verify all facts against source documents. &nbsp;🤖'
        ),
        # W5.1 UX strings
        "source_only_message": (
            "This file was exported without its drawing engine, "
            "so the diagram is shown as text instructions."
        ),
        "source_only_disclosure_label": "Show diagram source",
        "source_only_action": (
            "Ask the person who sent you this file for the rendered version."
        ),
        "alert_no_renderer": (
            "The drawing engine did not load for this file. "
            "Try reopening the file or refreshing the page."
        ),
        "alert_rerender_error": (
            "The diagram could not be redrawn. "
            "Your change may have a typo; press Cancel to restore the original."
        ),
        "alert_svg_not_ready": (
            "The diagram is not ready yet. Please wait a moment and try again."
        ),
        "alert_png_failed": (
            "The image could not be saved. Try downloading the SVG version instead."
        ),
        # W5.2 guidance strings
        "hint_chip": "Drag to move · scroll or pinch to zoom · buttons below right",
        "hint_pulse": "More detail in these tabs",
        "hint_got_it": "Got it",
        "fab_save_label": "Save",
        "fab_edit_label": "Edit",
    },
    "fr": {
        "tab_overview": "Aperçu",
        "tab_how_to_read": "Comment lire",
        "tab_observations": "Observations",
        "tab_limitations": "⚠ Limites",
        "tab_source_docs": "Documents sources",
        "panel_overview": "Aperçu",
        "panel_how_to_read": "Comment lire",
        "panel_observations": "Observations clés",
        "panel_limitations": "Limites",
        "panel_source_docs": "Documents sources",
        "ctrl_zoom_in": "Zoom avant",
        "ctrl_zoom_out": "Zoom arrière",
        "ctrl_reset": "Réinitialiser",
        "ctrl_contrast": "Contraste élevé",
        "ctrl_flip": "Basculer",
        "ctrl_fullscreen": "Plein écran",
        "ctrl_exit_fullscreen": "Quitter le plein écran (Échap)",
        "ctrl_exit_fullscreen_label": "✕ Quitter",
        "export_svg": "Vecteur haute qualité (SVG), idéal pour l'impression et les présentations",
        "export_png": "Image (PNG), idéale pour les courriels et Word",
        "export_html": "Cette page complète (HTML)",
        "export_title": "Enregistrer / Exporter",
        "edit_source": "✎ Modifier la source",
        "edit_title": "Modifier",
        # W5.3 editor strings
        "editor_summary": "Avancé : modifier les instructions de dessin du diagramme",
        "editor_warning": "Ces modifications affectent uniquement l'image, pas vos documents.",
        "rerender": "Redessiner",
        "cancel": "Annuler",
        "disclaimer_html": (
            "Sortie d'IA générative · Aide visuelle seulement. Ne constitue pas "
            "un avis juridique. Vérifiez tous les faits contre les documents sources."
        ),
        # W5.1 UX strings
        "source_only_message": (
            "Ce fichier a été exporté sans son moteur de rendu, "
            "alors le diagramme est affiché sous forme d'instructions textuelles."
        ),
        "source_only_disclosure_label": "Afficher la source du diagramme",
        "source_only_action": (
            "Demandez à la personne qui vous a envoyé ce fichier la version avec le diagramme rendu."
        ),
        "alert_no_renderer": (
            "Le moteur de dessin de ce fichier n'a pas pu se charger. "
            "Essayez de rouvrir le fichier ou de rafraîchir la page."
        ),
        "alert_rerender_error": (
            "Le diagramme n'a pas pu être redessiné. "
            "Votre modification contient peut-être une erreur; appuyez sur Annuler pour restaurer l'original."
        ),
        "alert_svg_not_ready": (
            "Le diagramme n'est pas encore prêt. Veuillez patienter un moment et réessayer."
        ),
        "alert_png_failed": (
            "L'image n'a pas pu être enregistrée. Essayez plutôt de télécharger la version SVG."
        ),
        # W5.2 guidance strings
        "hint_chip": "Glisser pour déplacer · défiler ou pincer pour zoomer · boutons en bas à droite",
        "hint_pulse": "Plus de détails dans ces onglets",
        "hint_got_it": "Compris",
        "fab_save_label": "Enregistrer",
        "fab_edit_label": "Modifier",
    },
}

# ── classDef injection ────────────────────────────────────────────────────────

# "graph" is a Mermaid alias for flowchart and also supports classDef.
_CLASSDEF_SUPPORTED_TYPES = {"flowchart", "graph", "statediagram-v2", "statediagram"}

_RISK_HIGH_STROKE = "#8B4444"
_RISK_HIGH_WIDTH = "2.5px"


def _sem_table() -> dict[str, tuple[str, str, str]]:
    """Build sem-* → (camelName, baseStyle, highStyle) lookup. Called once at import."""
    _BASE = [
        ("sem-party",     "semParty",     "#C9D6E3", "#8FA8BE"),
        ("sem-authority", "semAuthority", "#CAD2C5", "#8A9E84"),
        ("sem-risk",      "semRisk",      "#D6B8B8", "#A87878"),
        ("sem-outcome",   "semOutcome",   "#CFCFCF", "#909090"),
        ("sem-process",   "semProcess",   "#F5F3EE", "#B0A898"),
        ("sem-evidence",  "semEvidence",  "#D8D3E8", "#9888B8"),
        ("sem-claim",     "semClaim",     "#DDD2C2", "#A89878"),
        ("sem-ownership", "semOwnership", "#D3DDE8", "#7898B8"),
        ("sem-financial", "semFinancial", "#E6D3A3", "#B89840"),
        ("sem-control",   "semControl",   "#D4E8D3", "#78A878"),
        ("sem-gap",       "semGap",       "#E8D6B8", "#B89860"),
        ("sem-dataflow",  "semDataflow",  "#D8E8E3", "#78A898"),
        ("sem-finding",   "semFinding",   "#E3D8E8", "#9878A8"),
        ("sem-ip-asset",  "semIpAsset",   "#D8E3D8", "#789878"),
    ]
    return {
        sem: (
            name,
            f"fill:{fill},stroke:{stroke},stroke-width:1.5px,color:#1a1a1a",
            f"fill:{fill},stroke:{_RISK_HIGH_STROKE},stroke-width:{_RISK_HIGH_WIDTH},color:#1a1a1a",
        )
        for sem, name, fill, stroke in _BASE
    }


_SEM_TO_CLASSDEF: dict[str, tuple[str, str, str]] = _sem_table()


def _first_token(mermaid_block: str) -> str:
    """Lowercased first token of the diagram declaration line."""
    return next(
        (line.strip().split()[0].lower() for line in mermaid_block.splitlines() if line.strip()),
        "",
    )


def _inject_classdef(mermaid_block: str, semantic_map: dict) -> str:
    """Append Mermaid classDef + class lines derived from semantic_map.nodes.

    Only injects for diagram types that support classDef (flowchart, stateDiagram).
    Returns mermaid_block unchanged for unsupported types or empty node maps.
    sem-risk-high modifier produces a *High variant with a red stroke override.
    """
    nodes: dict[str, str] = semantic_map.get("nodes", {})
    if not nodes:
        return mermaid_block

    if _first_token(mermaid_block) not in _CLASSDEF_SUPPORTED_TYPES:
        return mermaid_block

    groups: dict[str, tuple[str, list[str]]] = {}  # cname → (style, node_ids)
    for node_id, sem_classes_str in nodes.items():
        parts = sem_classes_str.split()
        primary = next((p for p in parts if p in _SEM_TO_CLASSDEF), None)
        if primary is None:
            continue
        name, base_style, high_style = _SEM_TO_CLASSDEF[primary]
        has_high = "sem-risk-high" in parts
        cname = name + "High" if has_high else name
        style = high_style if has_high else base_style
        if cname not in groups:
            groups[cname] = (style, [])
        groups[cname][1].append(node_id)

    if not groups:
        return mermaid_block

    sorted_names = sorted(groups)
    lines = (
        [""]
        + [f"    classDef {c} {groups[c][0]}" for c in sorted_names]
        + [""]
        + [f"    class {','.join(sorted(groups[c][1]))} {c}" for c in sorted_names]
    )
    return mermaid_block + "\n".join(lines)


# ── container tier shading ─────────────────────────────────────────────────────

_CONTAINER_SUPPORTED_TYPES = {"flowchart", "graph"}

# Light -> dark neutral ramp; deliberately greyscale so it never collides with
# the coloured node sem-* fills.
_CONTAINER_TIERS = [
    ("#F7F7F5", "#D8D8D2"),
    ("#ECECE6", "#C8C8C0"),
    ("#E0E0D8", "#B8B8AE"),
]


def _inject_container_styles(mermaid_block: str, semantic_map: dict) -> str:
    """Append Mermaid `style <SubgraphId> fill:...` lines per container depth tier.

    Only injects for flowchart/graph. Reads semantic_map['containers'] =
    {subgraph_id: tier_int}; the tier index clamps into the palette range.
    Returns the block unchanged for unsupported types or empty container maps.
    """
    containers: dict = semantic_map.get("containers", {})
    if not containers:
        return mermaid_block
    if _first_token(mermaid_block) not in _CONTAINER_SUPPORTED_TYPES:
        return mermaid_block
    lines = [""]
    for sub_id, tier in sorted(containers.items()):
        try:
            idx = max(0, min(int(tier), len(_CONTAINER_TIERS) - 1))
        except (TypeError, ValueError):
            idx = 0
        fill, stroke = _CONTAINER_TIERS[idx]
        lines.append(f"    style {sub_id} fill:{fill},stroke:{stroke},stroke-width:1px")
    return mermaid_block + "\n".join(lines)


def _template_path() -> Path:
    return Path(__file__).parent.parent / "assets" / "html_template.html"

def _vendored_mermaid_path() -> Path:
    return Path(__file__).parent.parent / "assets" / "vendor" / "mermaid.min.js"

def cdn_url(version: str = MERMAID_VERSION) -> str:
    return f"https://cdn.jsdelivr.net/npm/mermaid@{version}/dist/mermaid.min.js"

def _mermaid_loader(allow_cdn: bool) -> dict:
    vendored = _vendored_mermaid_path()
    if vendored.exists():
        return {
            "mode": "vendored",
            "script_body": vendored.read_text(encoding="utf-8"),
            "script_url": "",
        }
    if allow_cdn:
        return {
            "mode": "cdn",
            "script_body": "",
            "script_url": cdn_url(),
        }
    return {"mode": "source-only", "script_body": "", "script_url": ""}

def _semantic_map(value: str) -> dict:
    try:
        parsed = json.loads(value or "{}")
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid semantic map JSON: {exc}") from exc
    if not isinstance(parsed, dict):
        raise ValueError("Invalid semantic map JSON: root must be an object")
    return parsed

def _string_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [str(item) for item in value]
    return [str(value)]

def _as_file_uri(p: Path) -> str:
    """file:// URI for p; resolve relative paths first (Py3.14 as_uri() rejects them)."""
    try:
        return p.as_uri()
    except ValueError:
        return p.resolve().as_uri()


def _source_link(source_path: str | None, page: int | None,
                 relative_links: bool, output_path: str) -> str | None:
    if not source_path:
        return None
    p = Path(source_path)
    if relative_links:
        try:
            rel = p.relative_to(Path(output_path).parent)
            uri = str(rel).replace("\\", "/")
        except ValueError:
            uri = _as_file_uri(p)
    else:
        uri = _as_file_uri(p)
    fragment = ""
    if p.suffix.lower() == ".pdf" and page:
        fragment = f"#page={page}"
    return f"{uri}{fragment}"


def render(mermaid_block: str, figure_desc: dict, output_path: str,
           semantic_map: str = "{}", allow_cdn: bool = False,
           digest_table: list[dict] | None = None,
           source_path: str | None = None,
           relative_links: bool = False,
           ui_lang: str = "en",
           fetch_engine: bool = False) -> dict:
    from jinja2 import Environment, BaseLoader
    src = _template_path().read_text(encoding="utf-8")
    env = Environment(loader=BaseLoader(), autoescape=True)
    if fetch_engine:
        try:
            import fetch_mermaid as _fm
            _fm.ensure_vendored()
        except Exception:
            pass  # best-effort; missing module or network failure does not break render
    loader = _mermaid_loader(allow_cdn=allow_cdn)

    digest_rows: list[dict] | None = None
    has_unverified = False
    if digest_table:
        digest_rows = []
        for row in digest_table:
            enriched = dict(row)
            row_source = row.get("source_path") or source_path
            enriched["source_link"] = _source_link(
                row_source, row.get("page"), relative_links, output_path
            )
            digest_rows.append(enriched)
        has_unverified = any(r.get("unverified") for r in digest_table)

    parsed_sem_map = _semantic_map(semantic_map)
    injected_block = _inject_classdef(mermaid_block, parsed_sem_map)
    injected_block = _inject_container_styles(injected_block, parsed_sem_map)

    if ui_lang not in UI_STRINGS:
        ui_lang = "en"

    html = env.from_string(src).render(
        ui=UI_STRINGS[ui_lang],
        ui_lang=ui_lang,
        matter_title=figure_desc.get("title", "Legal Diagram"),
        matter_context=figure_desc.get("matter_context", ""),
        mermaid_block=injected_block, figure_caption=figure_desc.get("caption", ""),
        overview=figure_desc.get("overview", ""), how_to_read=figure_desc.get("how_to_read", ""),
        observations=_string_list(figure_desc.get("observations", [])),
        caveats=_string_list(figure_desc.get("caveats", [])),
        semantic_map=parsed_sem_map,
        mermaid_loader=loader,
        digest_rows=digest_rows,
        has_unverified=has_unverified)
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    return {"ok": True, "output_path": os.path.abspath(output_path),
            "file_size_kb": round(os.path.getsize(output_path) / 1024, 1)}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mermaid-block", required=True)
    p.add_argument("--figure-desc", required=True)
    p.add_argument("--output-path", required=True)
    p.add_argument("--semantic-map", default="{}")
    p.add_argument("--allow-cdn", action="store_true",
                   help="Allow pinned Mermaid CDN fallback when assets/vendor/mermaid.min.js is absent.")
    p.add_argument("--fetch-engine", action="store_true",
                   help="Opt-in: download mermaid.min.js into assets/vendor/ before rendering (offline support).")
    p.add_argument("--digest-table", default="[]",
                   help="JSON array of digest row dicts to render as verification table.")
    p.add_argument("--source-path", default="",
                   help="Absolute path to source document for source links in digest table.")
    p.add_argument("--relative-links", action="store_true",
                   help="Emit relative file:// links for source_path instead of absolute.")
    p.add_argument("--ui-lang", choices=("en", "fr"), default="en",
                   help="Chrome language for tabs, controls, export labels, and the "
                        "disclaimer banner. Diagram and matter text stay verbatim.")
    args = p.parse_args()
    try:
        desc = json.loads(args.figure_desc)
    except json.JSONDecodeError as e:
        print(json.dumps({"ok": False, "error": f"Invalid JSON: {e}"})); sys.exit(1)
    try:
        digest_table = json.loads(args.digest_table)
    except json.JSONDecodeError as e:
        print(json.dumps({"ok": False, "error": f"Invalid digest-table JSON: {e}"})); sys.exit(1)
    try:
        print(json.dumps(render(args.mermaid_block, desc, args.output_path,
                                semantic_map=args.semantic_map,
                                allow_cdn=args.allow_cdn,
                                digest_table=digest_table or None,
                                source_path=args.source_path or None,
                                relative_links=args.relative_links,
                                ui_lang=args.ui_lang,
                                fetch_engine=args.fetch_engine)))
    except Exception as e:
        print(json.dumps({"ok": False, "error": str(e)})); sys.exit(1)

if __name__ == "__main__":
    main()
