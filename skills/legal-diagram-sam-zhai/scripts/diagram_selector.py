import argparse, heapq, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from extraction.domain import ExtractionResult, ENTITY_FIELDS
from extraction.utils import strip_diacritics

STATE_DIAGRAM = "stateDiagram-" + "v" + "2"

# Simple pairwise edge fields: (field_attr, src_attr, dst_attr).
# These five all follow the identical pattern: iterate items, add one directed edge.
# Kept beside ENTITY_FIELDS / RULES so the field registry stays a single source.
SIMPLE_EDGE_FIELDS = [
    ("relationships",   "from_entity", "to_entity"),
    ("ownership_links", "parent",      "child"),
    ("transitions",     "from_state",  "to_state"),
    ("communications",  "from_party",  "to_party"),
    ("transfers",       "from_party",  "to_party"),
]

RULES = [
    ("events",             ["timeline", "gantt"],                2.0),
    ("deadlines",          ["gantt", "timeline"],                2.0),
    ("phases",             ["gantt", "timeline"],                2.5),
    ("tasks",              ["gantt"],                            2.5),
    ("ownership_links",    ["erDiagram", "flowchart"],           3.0),
    ("relationships",      ["erDiagram", "flowchart"],           1.5),
    ("entities",           ["erDiagram", "flowchart"],           1.5),
    ("documents",          ["flowchart", "requirementDiagram"],  1.0),
    ("obligations",        ["requirementDiagram", "flowchart"],  2.5),
    ("controls",           ["requirementDiagram"],               1.5),
    ("conditions",         ["flowchart", "requirementDiagram"],  2.0),
    ("states",             [STATE_DIAGRAM, "flowchart"],     2.5),
    ("transitions",        [STATE_DIAGRAM],                  2.0),
    ("decision_points",    ["flowchart"],                        2.5),
    ("process_steps",      ["flowchart", STATE_DIAGRAM],     2.5),
    ("investigation_steps",["timeline", "flowchart"],            2.0),
    ("risk_items",         ["quadrantChart"],                    3.0),
    ("negotiation_issues", ["quadrantChart"],                    3.0),
    ("transfers",          ["sequenceDiagram", "flowchart"],     2.0),
    ("claim_classes",      ["flowchart", "timeline"],            2.5),
    ("communications",     ["sequenceDiagram"],                  3.0),
    ("concepts",           ["mindmap", "flowchart"],             2.5),
    ("data_flows",         ["flowchart", "sequenceDiagram"],     2.5),
    ("witnesses",          ["mindmap"],                          2.0),
    ("legal_authorities",  ["mindmap", "flowchart"],             1.5),
    ("ip_assets",          [STATE_DIAGRAM, "timeline"],      2.0),
    ("parties",            ["sequenceDiagram", "flowchart"],     0.5),
]

# INTENT_MAP: keyword -> (target types, specificity).
#
# specificity ranks how diagram-defining a keyword is.  Shape-naming nouns
# ("chronology", "flows", "phases", "ownership structure") score 2; generic
# legal modifiers that appear across many document kinds ("compliance",
# "obligations", "deadlines", "notice periods") score 1.  Matching collects ALL
# substring hits, then the single highest-specificity hit (longest keyword breaks
# ties) becomes the dominant signal; the rest are secondary (see _score).  This is
# the longest-/most-specific-match precedence that replaces first-substring-wins.
# Structure stays data-driven so W3 can append FR keywords with their own
# specificity.  Every keyword here is a plausible generic user phrase.
INTENT_MAP: dict[str, tuple[list[str], int]] = {
    "chronology": (["timeline", "gantt"], 2), "timeline": (["timeline", "gantt"], 2),
    "entity structure": (["erDiagram", "flowchart"], 2),
    "ownership structure": (["erDiagram"], 2), "ownership": (["erDiagram", "flowchart"], 2),
    "compliance": (["requirementDiagram", "flowchart"], 1), "obligations": (["requirementDiagram"], 1),
    "workflow": (["flowchart", STATE_DIAGRAM], 2), "process": (["flowchart"], 2),
    "state": ([STATE_DIAGRAM], 2),
    "funds flow": (["sequenceDiagram", "flowchart"], 2), "deal timeline": (["gantt"], 2),
    "risk": (["quadrantChart"], 2),
    "research": (["mindmap"], 2), "issue tree": (["mindmap", "flowchart"], 2),
    "strategy": (["quadrantChart", "mindmap"], 2),
    "witness": (["mindmap"], 2), "sequence": (["sequenceDiagram"], 2),
    "client explanation": (["journey"], 2), "client guide": (["journey"], 2),
    "counseling": (["journey"], 2), "explain to client": (["journey"], 2),
    "communications": (["sequenceDiagram"], 2), "tax structure": (["erDiagram"], 2),
    "ip": ([STATE_DIAGRAM], 2),
    "bankruptcy": (["flowchart", "timeline"], 2), "waterfall": (["flowchart", "timeline"], 2),
    # Added so each diagram type is reachable by a natural generic phrase.
    "data flow": (["flowchart", "sequenceDiagram"], 2),
    "data flows": (["flowchart", "sequenceDiagram"], 2),
    "privacy flows": (["flowchart"], 2), "flows": (["flowchart"], 2),
    "phases": (["gantt", "timeline"], 2), "schedule": (["gantt", "timeline"], 2),
    "deadlines": (["gantt", "timeline"], 1),
    "compliance checklist": (["requirementDiagram"], 2),
    "checklist": (["requirementDiagram"], 2),
    "notice periods": (["requirementDiagram"], 1),
    # W3.5 FR keywords: each mirrors the (types, specificity) of its EN twin
    # concept.  Keys keep their accents; matching folds both sides (NFD-strip +
    # casefold, see _fold), so unaccented spellings such as "echeancier" match too.
    "chronologie": (["timeline", "gantt"], 2),
    "échéancier": (["gantt", "timeline"], 2),
    "organigramme": (["erDiagram", "flowchart"], 2),
    "arbre de décision": (["flowchart"], 2),
    "schéma": (["flowchart"], 2),
    "liste d'obligations": (["requirementDiagram"], 2),
    "qui-fait-quoi-quand": (["sequenceDiagram"], 2),
    "carte mentale": (["mindmap"], 2),
    "grille de priorités": (["quadrantChart"], 2),
    "carte d'expérience": (["journey"], 2),
}

# Intent boost magnitudes.  The dominant (most-specific) keyword hit decisively
# nudges its types so a clearly stated user intent can win against a diffuse
# fallback pileup; remaining hits add a smaller secondary nudge.
DOMINANT_INTENT_BOOST = 8.0
SECONDARY_INTENT_BOOST = 2.0

# Non-primary types inside one RULES entry are fallbacks; they earn this fraction
# of the rule weight.  Without it, a catch-all fallback (flowchart appears as a
# secondary type in many rules) sponges full weight from every signal and drowns
# the document's true primary shape (defect-1 structural cause).
SECONDARY_TYPE_FACTOR = 0.6

MATTER_BOOSTS = {
    "litigation": {"timeline": 1.0, "flowchart": 0.5}, "corporate": {"erDiagram": 1.0, "gantt": 0.5},
    "compliance": {"requirementDiagram": 1.5}, "employment": {"timeline": 1.0, "flowchart": 0.5},
    "ip": {STATE_DIAGRAM: 1.5}, "bankruptcy": {"timeline": 1.0, "flowchart": 0.5}, "tax": {"erDiagram": 1.0},
    "privacy":     {"flowchart": 1.0, "sequenceDiagram": 0.5},
    "real_estate": {"gantt": 1.0, "flowchart": 0.5},
    "arbitration": {"timeline": 1.0, "sequenceDiagram": 0.5},
    # "deal" favours gantt strongly: a deal matter wants a closing schedule, and the
    # former flowchart secondary boost fought any schedule-naming intent (W1 calibration).
    "deal":        {"gantt": 3.0},
    "tech":        {"requirementDiagram": 1.5},
}


def _intent_types(keyword: str) -> list[str]:
    """Return the target diagram types for an INTENT_MAP keyword."""
    return INTENT_MAP[keyword][0]


def _fold(text: str) -> str:
    """Accent-insensitive comparison key: NFD-strip diacritics, then casefold.

    EN keywords contain no accents, so folding them is the identity transform and
    EN matching behaviour is unchanged (for ASCII, casefold == lower).
    Curly apostrophe (U+2019) folds to ASCII so intents typed with smart quotes
    still match keys like "liste d'obligations".
    """
    return strip_diacritics(text).replace("’", "'").casefold()


def _intent_hits(intent: str) -> list[tuple[str, list[str], int]]:
    """Collect every INTENT_MAP keyword that occurs in the intent string.

    Case- and accent-insensitive substring match: both the intent text and each
    keyword are folded via _fold, so "echeancier" matches "échéancier".  Returned
    ordered by specificity (desc), then keyword length (desc), then keyword
    alphabetically (asc) so same-specificity same-length collisions break
    deterministically by spelling, never by INTENT_MAP insertion order.  The sort
    key operates on the original keyword strings, so adding FR keys cannot perturb
    EN tie-breaks.  The first hit becomes the dominant signal.
    """
    il = _fold(intent)
    hits = [(kw, types, spec) for kw, (types, spec) in INTENT_MAP.items() if _fold(kw) in il]
    hits.sort(key=lambda h: (-h[2], -len(h[0]), h[0]))
    return hits


def _event_text(e):
    if isinstance(e, dict):
        return e.get("description") or ""
    return getattr(e, "description", "") or ""


def _build_edge_graph(r):
    """Derive a directed graph from all typed edge-bearing fields in r.

    Returns (nodes: set[str], adjacency: dict[str, list[str]]) where adjacency
    maps each node to its list of successor nodes.  Every field is optional and
    guarded with getattr so sparse ExtractionResult objects never raise.

    Single place geometry derives topology (high cohesion).
    """
    nodes: set = set()
    # Use sets internally to deduplicate parallel edges from redundant fields
    # (e.g. concept.children and child.parent_id both encode the same edge).
    adj_sets: dict = {}

    def _add_edge(src, dst):
        if src is None or dst is None:
            return
        src, dst = str(src), str(dst)
        nodes.add(src)
        nodes.add(dst)
        adj_sets.setdefault(src, set()).add(dst)
        adj_sets.setdefault(dst, set())  # ensure dst has an entry

    def _ensure_node(x):
        # Retains isolated source nodes that may have zero edges.
        s = str(x)
        nodes.add(s)
        adj_sets.setdefault(s, set())

    # Simple pairwise fields: driven by SIMPLE_EDGE_FIELDS table.
    for attr, s_field, d_field in SIMPLE_EDGE_FIELDS:
        for item in (getattr(r, attr, None) or []):
            _add_edge(getattr(item, s_field, None), getattr(item, d_field, None))

    # process_steps: step.id -> each entry in step.next_steps
    for ps in (getattr(r, "process_steps", None) or []):
        src = getattr(ps, "id", None)
        if src is not None:
            _ensure_node(src)  # preserve isolated steps with no next_steps
            for nxt in (getattr(ps, "next_steps", None) or []):
                _add_edge(src, nxt)

    # decision_points: question -> yes_path, question -> no_path
    for dp in (getattr(r, "decision_points", None) or []):
        q = getattr(dp, "question", None)
        _add_edge(q, getattr(dp, "yes_path", None))
        _add_edge(q, getattr(dp, "no_path", None))

    # concepts: parent_id -> child id; concept id -> each child in children list
    for con in (getattr(r, "concepts", None) or []):
        cid = getattr(con, "id", None)
        if cid is not None:
            _ensure_node(cid)  # preserve isolated concepts with no edges
        parent_id = getattr(con, "parent_id", None)
        if parent_id is not None and cid is not None:
            _add_edge(parent_id, cid)
        for child in (getattr(con, "children", None) or []):
            _add_edge(cid, child)

    # hierarchy entries contribute subgraph breadth (parent -> node)
    for h in (getattr(r, "hierarchy", None) or []):
        if isinstance(h, dict):
            parent = h.get("parent")
            child = h.get("id") or h.get("name")
            if parent and child:
                _add_edge(parent, child)

    # Convert sets to sorted lists for deterministic downstream iteration
    adj = {k: sorted(v) for k, v in adj_sets.items()}
    return nodes, adj


def _longest_path_layered(adj, nodes):
    """Compute longest path length and per-layer widths via topological layering.

    Uses Kahn's algorithm for topological sort then assigns each node the layer
    of max(layer(predecessors)) + 1.  Handles cycles gracefully by skipping
    nodes that were not processed (in-degree never reached 0).

    Returns (longest_path: int, layer_widths: list[int]).
    """
    if not nodes:
        return 0, []

    # Build in-degree and predecessor maps from adjacency
    in_degree: dict = {n: 0 for n in nodes}
    for src, dsts in adj.items():
        for dst in dsts:
            if dst in in_degree:
                in_degree[dst] = in_degree.get(dst, 0) + 1

    layer: dict = {}
    queue = [n for n in nodes if in_degree.get(n, 0) == 0]
    for n in queue:
        layer[n] = 0
    heapq.heapify(queue)  # min-heap for O((V+E) log V) deterministic processing

    processed = []
    while queue:
        n = heapq.heappop(queue)
        processed.append(n)
        for dst in adj.get(n, []):  # adj already sorted at construction
            if dst not in nodes:
                continue
            in_degree[dst] -= 1
            new_layer = layer[n] + 1
            if layer.get(dst, -1) < new_layer:
                layer[dst] = new_layer
            if in_degree[dst] == 0:
                heapq.heappush(queue, dst)

    if not layer:
        return 0, []

    max_layer = max(layer.values())
    widths = [0] * (max_layer + 1)
    for n, lv in layer.items():
        widths[lv] += 1

    return max_layer, widths


def _graph_metrics(r) -> dict:
    """Compute topology-only metrics from an ExtractionResult.

    All returned values are independent of recommended diagram type.
    Expensive work (graph build, topo layering, CC scan) runs once here;
    callers that need to reclassify for a different type call _classify_geometry
    with the cached result rather than rebuilding from scratch.
    """
    nodes, adj = _build_edge_graph(r)
    N = len(nodes)
    E = sum(len(v) for v in adj.values())
    max_out_degree = max((len(v) for v in adj.values()), default=0)

    longest_path, layer_widths = _longest_path_layered(adj, nodes)
    est_max_rank_width = max(layer_widths) if layer_widths else 0

    # Subgraph count: weakly-connected components
    visited: set = set()
    subgraph_count = 0
    undirected: dict = {}
    for src, dsts in adj.items():
        undirected.setdefault(src, set())
        for dst in dsts:
            undirected[src].add(dst)
            undirected.setdefault(dst, set()).add(src)
    for n in nodes:
        undirected.setdefault(n, set())
    for start in nodes:
        if start not in visited:
            subgraph_count += 1
            stack = [start]
            while stack:
                cur = stack.pop()
                if cur in visited:
                    continue
                visited.add(cur)
                stack.extend(undirected.get(cur, set()) - visited)

    # Max siblings per subgraph: max out-degree within concept hierarchy or adj
    max_siblings_per_subgraph = max_out_degree

    # Also inspect concept children lists directly for mindmap breadth
    concept_children_counts = []
    for con in (getattr(r, "concepts", None) or []):
        children = getattr(con, "children", None) or []
        concept_children_counts.append(len(children))
    if concept_children_counts:
        max_siblings_per_subgraph = max(max_siblings_per_subgraph, max(concept_children_counts))

    return {
        "N": N, "E": E,
        "max_out_degree": max_out_degree,
        "longest_path": longest_path,
        "est_max_rank_width": est_max_rank_width,
        "subgraph_count": subgraph_count,
        "max_siblings_per_subgraph": max_siblings_per_subgraph,
        # Preserve raw field references for _classify_geometry's ER/sequence branches.
        "_r": r,
    }


def _classify_geometry(metrics: dict, recommended_type: str) -> dict:
    """Classify pre-computed topology metrics against a diagram type's thresholds.

    Accepts the dict returned by _graph_metrics and the target type; returns the
    full geometry dict (same shape as legacy _geometry).  Separated from
    _graph_metrics so that recommend() can build the graph once and reclassify
    cheaply when a grouping override changes the recommended type.
    """
    r = metrics["_r"]
    N = metrics["N"]
    E = metrics["E"]
    max_out_degree = metrics["max_out_degree"]
    longest_path = metrics["longest_path"]
    est_max_rank_width = metrics["est_max_rank_width"]
    subgraph_count = metrics["subgraph_count"]
    max_siblings_per_subgraph = metrics["max_siblings_per_subgraph"]

    triggers: list = []
    band = "green"
    action = "ship"
    split_axis_suggestion = None
    primary_metric = "est_max_rank_width"

    dtype = (recommended_type or "").lower()

    # -----------------------------------------------------------------------
    # Flowchart / graph / stateDiagram (breadth-primary)
    # -----------------------------------------------------------------------
    if dtype in ("flowchart", "graph", "statediagram-v2", "statediagram"):
        primary_metric = "est_max_rank_width"
        if est_max_rank_width >= 8 or max_out_degree >= 13:
            band = "split"
            action = "split"
            if est_max_rank_width >= 8:
                triggers.append(f"est_max_rank_width={est_max_rank_width} >= 8 (legibility floor)")
            if max_out_degree >= 13:
                triggers.append(f"max_out_degree={max_out_degree} >= 13")
            split_axis_suggestion = "type"
        elif subgraph_count > 0 and max_siblings_per_subgraph >= 12:
            band = "split"
            action = "split"
            triggers.append(f"max_siblings_per_subgraph={max_siblings_per_subgraph} >= 12")
            split_axis_suggestion = "type"
        elif est_max_rank_width == 7 or (7 <= max_out_degree <= 12):
            band = "warn"
            action = "caveat"
            if est_max_rank_width == 7:
                triggers.append(f"est_max_rank_width={est_max_rank_width} == 7 (approaching limit)")
            if 7 <= max_out_degree <= 12:
                triggers.append(f"max_out_degree={max_out_degree} in warn range 7-12")
        # Soft navigability warn (does not override green/warn from above)
        if N >= 60 and band == "green":
            triggers.append(f"node_count={N} >= 60 (navigability soft-warn)")

    # -----------------------------------------------------------------------
    # erDiagram / classDiagram (entity + edge-density)
    # -----------------------------------------------------------------------
    elif dtype in ("erdiagram", "classdiagram"):
        primary_metric = "entity_count"
        # Entity count: use r.entities + r.parties as proxies for ER nodes
        entity_count = len(getattr(r, "entities", None) or [])
        if entity_count == 0:
            entity_count = N  # fallback to graph nodes
        ratio = E / entity_count if entity_count else 0.0
        if entity_count >= 21 or ratio >= 4.0:
            band = "split"
            action = "split"
            if entity_count >= 21:
                triggers.append(f"entity_count={entity_count} >= 21")
            if ratio >= 4.0:
                triggers.append(f"edge/entity ratio={ratio:.1f} >= 4.0")
            split_axis_suggestion = "type"
        elif 13 <= entity_count <= 20 or 2.6 <= ratio <= 4.0:
            band = "warn"
            action = "caveat"
            if 13 <= entity_count <= 20:
                triggers.append(f"entity_count={entity_count} in warn range 13-20")
            if 2.6 <= ratio <= 4.0:
                triggers.append(f"edge/entity ratio={ratio:.1f} in warn range 2.6-4.0")

    # -----------------------------------------------------------------------
    # sequenceDiagram (participants)
    # -----------------------------------------------------------------------
    elif dtype == "sequencediagram":
        primary_metric = "participant_count"
        participant_count = len(getattr(r, "parties", None) or [])
        if participant_count == 0:
            # derive unique participants from communications
            comms = getattr(r, "communications", None) or []
            participants_set: set = set()
            for comm in comms:
                fp = getattr(comm, "from_party", None)
                tp = getattr(comm, "to_party", None)
                if fp:
                    participants_set.add(fp)
                if tp:
                    participants_set.add(tp)
            participant_count = len(participants_set)

        message_count = len(getattr(r, "communications", None) or [])

        if participant_count >= 13:
            band = "split"
            action = "split"
            triggers.append(f"participant_count={participant_count} >= 13")
            split_axis_suggestion = "party"
        elif 9 <= participant_count <= 12:
            band = "warn"
            action = "caveat"
            triggers.append(f"participant_count={participant_count} in warn range 9-12")
        if message_count >= 50 and band == "green":
            triggers.append(f"message_count={message_count} >= 50 (soft-warn)")

    # -----------------------------------------------------------------------
    # timeline / gantt (scroll-tolerated)
    # -----------------------------------------------------------------------
    elif dtype in ("timeline", "gantt"):
        primary_metric = "event_count"
        event_count = len(getattr(r, "events", None) or [])
        task_count = len(getattr(r, "tasks", None) or [])

        if dtype == "gantt":
            # gantt split: rows in one section >= 20
            # Use task_count as proxy for rows; sections approximated by subgraph_count
            if task_count >= 20:
                band = "split"
                action = "split"
                triggers.append(f"task_count={task_count} >= 20 (gantt section rows)")
                split_axis_suggestion = "date"
            elif event_count >= 25 or task_count >= 15:
                band = "warn"
                action = "caveat"
                if event_count >= 25:
                    triggers.append(f"event_count={event_count} >= 25")
                if task_count >= 15:
                    triggers.append(f"task_count={task_count} >= 15 (warn)")
        else:
            # timeline
            if event_count >= 25:
                band = "warn"
                action = "caveat"
                triggers.append(f"event_count={event_count} >= 25")

    # -----------------------------------------------------------------------
    # mindmap (tree breadth)
    # -----------------------------------------------------------------------
    elif dtype == "mindmap":
        primary_metric = "max_siblings"
        # max siblings = max children under one parent node
        max_sib = max_siblings_per_subgraph

        depth = longest_path  # longest path from root approximates depth

        if max_sib >= 16:
            band = "split"
            action = "split"
            triggers.append(f"max_siblings={max_sib} >= 16")
            split_axis_suggestion = "type"
        elif 9 <= max_sib <= 15:
            band = "warn"
            action = "caveat"
            triggers.append(f"max_siblings={max_sib} in warn range 9-15")
        if depth > 4 and band == "green":
            triggers.append(f"depth={depth} > 4 (soft-warn)")

    # -----------------------------------------------------------------------
    # unknown / other: green default, soft N>=60 warn
    # -----------------------------------------------------------------------
    else:
        primary_metric = "node_count"
        if N >= 60:
            triggers.append(f"node_count={N} >= 60 (navigability soft-warn)")

    return {
        "type": recommended_type,
        "primary_metric": primary_metric,
        "node_count": N,
        "edge_count": E,
        "max_out_degree": max_out_degree,
        "longest_path": longest_path,
        "est_max_rank_width": est_max_rank_width,
        "subgraph_count": subgraph_count,
        "max_siblings_per_subgraph": max_siblings_per_subgraph,
        "band": band,
        "action": action,
        "split_axis_suggestion": split_axis_suggestion,
        "triggers": triggers,
    }


def _geometry(r, recommended_type: str) -> dict:
    """Compute geometry metrics and classify into green|warn|split band.

    Thin wrapper that builds topology once via _graph_metrics and classifies via
    _classify_geometry.  Kept for call-site compatibility; prefer calling
    _graph_metrics + _classify_geometry directly when reclassification is needed.

    Primary metric is BREADTH (max nodes per rank / max out-degree) for graph
    types, not raw node count.  Raw node count is a soft navigability signal only.
    """
    return _classify_geometry(_graph_metrics(r), recommended_type)


def _grouping_decision(r, top, intent_exempt=False, geometry=None):
    """Phase 1 single-layer grouping: dense-timeline path and geometry-split path.

    Returns (new_top, grouping_axis, rationale_override|None). grouping_suggested
    is derived from grouping_axis being non-null at the call site.

    intent_exempt: when the user's intent explicitly names timeline (an INTENT_MAP
    keyword resolved to timeline), the dense-timeline override is suppressed so the
    stated intent is honoured.  The no-intent path passes intent_exempt=False, so its
    10-event / 50-char boundaries are unchanged (defect-2 fix).

    geometry: optional pre-computed geometry dict.  When geometry band == 'split',
    the grouping override also fires (generalising the dense-timeline override),
    using split_axis_suggestion as the grouping_axis.  Existing dense-timeline
    behaviour is preserved so selector tests stay green.
    """
    if top == "timeline" and not intent_exempt:
        events = r.events or []
        n = len(events)
        if n > 10 or (n and sum(len(_event_text(e)) for e in events) / n > 50):
            return ("flowchart", "era",
                    f"Timeline overridden to a grouped flowchart: {n} events exceed the density "
                    f"threshold. Rendering as a vertical flowchart with era subgraphs.")

    # Geometry split override: fires when geometry verdict is 'split'
    if geometry is not None and geometry.get("band") == "split":
        axis = geometry.get("split_axis_suggestion") or "type"
        return (top, axis, None)

    return (top, None, None)


def _score(r, intent):
    """Score every diagram type from structural signals, intent, and matter boosts.

    Returns the score dict.  The intent contribution uses most-specific-match
    precedence: the single dominant hit boosts its types by DOMINANT_INTENT_BOOST,
    every other hit by SECONDARY_INTENT_BOOST; a type is boosted only once.
    """
    return _score_with_intent_types(r, intent)[0]


def _score_with_intent_types(r, intent):
    """Like _score, but also return the set of intent-boosted types.

    The returned set lets recommend() decide grouping-override exemption without
    re-running keyword matching.
    """
    scores: dict[str, float] = {}
    for fld, types, weight in RULES:
        items = getattr(r, fld, [])
        if items:
            boost = min(len(items) / 3.0, 2.0)
            for idx, t in enumerate(types):
                factor = 1.0 if idx == 0 else SECONDARY_TYPE_FACTOR
                scores[t] = scores.get(t, 0) + weight * boost * factor
    matched_types: set[str] = set()
    for rank, (_kw, types, _spec) in enumerate(_intent_hits(intent)):
        amount = DOMINANT_INTENT_BOOST if rank == 0 else SECONDARY_INTENT_BOOST
        for t in types:
            if t not in matched_types:
                scores[t] = scores.get(t, 0) + amount
                matched_types.add(t)
    for t, b in MATTER_BOOSTS.get((r.matter_type or "").lower(), {}).items():
        scores[t] = scores.get(t, 0) + b
    return scores, matched_types


def _confidence(scores, top):
    """Margin-based confidence in [0, 1].

    conf = 0.9 * (top / (top + second)) + 0.1 * (top / total).

    The dominant term is the head-to-head margin between the winner and the runner-up,
    so a clear winner reports high confidence even when many other types carry small
    residual scores (the old top/total formula diluted clear winners to ~0.32-0.42 and
    would have tripped the 0.50 interrupt almost always).  The small share-of-total term
    breaks genuine ambiguity downward: when several types are near-tied the residual mass
    pulls confidence below 0.50 so the interrupt fires.  A perfect uncontested winner
    approaches 1.0; an exact two-way tie sits at 0.50; multi-way ambiguity lands below it.
    """
    ranked = sorted(scores, key=lambda t: scores[t], reverse=True)
    second = scores[ranked[1]] if len(ranked) > 1 else 0.0
    total = sum(scores.values())
    margin = scores[top] / (scores[top] + second) if (scores[top] + second) else 0.0
    share = scores[top] / total if total else 0.0
    return round(min(0.9 * margin + 0.1 * share, 1.0), 2)


# _DENSITY_BANDS: band name -> (inclusion_low, inclusion_high) fractions.
# Band names must stay in sync with workflows/generation.md § Step 3.4.
_DENSITY_BANDS = {
    "comprehensive": (0.85, 0.95),
    "detailed":      (0.60, 0.75),
    "overview":      (0.30, 0.45),
}

# Floor fields: only these three are scanned for risk_level == 'high'
_FLOOR_FIELDS = ("risk_items", "obligations", "deadlines")

# Per-band keywords for case-insensitive substring classification of intent strings.
_DENSITY_BAND_KEYWORDS: dict[str, tuple[str, ...]] = {
    "comprehensive": ("comprehensive", "exhaustive", "everything", "all"),
    "detailed":      ("detailed", "detail", "thorough"),
    "overview":      ("overview", "at a glance", "at-a-glance", "high level", "high-level", "summary", "simple"),
}


def _classify_band(intent: str) -> str:
    """Classify an intent string into a density band name.

    Case-insensitive substring match against three exclusive keyword groups.
    When exactly one group matches, that band is returned.
    When zero or multiple groups match (conflict), default is 'comprehensive'
    (guards against under-detailing -- the stated failure mode this signal fixes).
    """
    il = intent.casefold()
    matched = [b for b, kws in _DENSITY_BAND_KEYWORDS.items() if any(kw in il for kw in kws)]
    return matched[0] if len(matched) == 1 else "comprehensive"


def _density(r, intent: str) -> dict:
    """Compute a density advisory signal for the diagram generation step.

    Returns a dict with keys:
      salient_count  -- total entity count across all ENTITY_FIELDS
      band           -- 'comprehensive' | 'detailed' | 'overview'
      inclusion_low  -- lower fraction of the band (float)
      inclusion_high -- upper fraction of the band (float)
      target_low     -- round(salient_count * inclusion_low), clamped by floor
      target_high    -- round(salient_count * inclusion_high)
      floor          -- count of high-risk entities that must not be dropped

    When salient_count == 0 all targets are 0 but the band is still classified
    so callers without entities do not break.
    """
    salient_count = sum(len(getattr(r, field) or []) for field in ENTITY_FIELDS)
    band = _classify_band(intent)
    low_frac, high_frac = _DENSITY_BANDS[band]

    # Floor: count items whose risk_level == 'high' across the three floor fields
    floor = 0
    for field in _FLOOR_FIELDS:
        for item in (getattr(r, field) or []):
            if getattr(item, "risk_level", None) == "high":
                floor += 1

    # Compute floor clamped to salient_count; targets are 0 when salient_count == 0.
    effective_floor = min(floor, salient_count)
    target_low = max(round(salient_count * low_frac), effective_floor) if salient_count else 0
    target_high = round(salient_count * high_frac) if salient_count else 0

    return {
        "salient_count": salient_count,
        "band": band,
        "inclusion_low": low_frac,
        "inclusion_high": high_frac,
        "target_low": target_low,
        "target_high": target_high,
        "floor": floor,
    }


def recommend(r, intent):
    scores, intent_types = _score_with_intent_types(r, intent)
    # Build topology once; reclassify cheaply if grouping override changes the type.
    topo = _graph_metrics(r)
    if not scores:
        geo = _classify_geometry(topo, "flowchart")
        return {"recommended_type": "flowchart", "rationale": "No signals; flowchart is the versatile default.",
                "alternatives": ["mindmap", "timeline"], "confidence": 0.3,
                "grouping_suggested": False, "grouping_axis": None,
                "density": _density(r, intent), "geometry": geo}
    ranked = sorted(scores, key=lambda t: scores[t], reverse=True)
    top = ranked[0]
    conf = _confidence(scores, top)
    drivers = [f.replace("_", " ") for f, types, _ in RULES if top in types and getattr(r, f)]
    base_rationale = f"{top} selected based on: {', '.join(drivers) or 'intent match'}."
    geo = _classify_geometry(topo, top)
    new_top, grouping_axis, rationale_override = _grouping_decision(
        r, top, intent_exempt=top in intent_types, geometry=geo)
    # Reclassify against new_top using the already-built topology (no graph rebuild).
    if geo["type"] != new_top:
        geo = _classify_geometry(topo, new_top)
    return {"recommended_type": new_top,
            "rationale": rationale_override or base_rationale,
            "alternatives": ranked[1:3], "confidence": conf,
            "grouping_suggested": grouping_axis is not None, "grouping_axis": grouping_axis,
            "density": _density(r, intent), "geometry": geo}

def main():
    p = argparse.ArgumentParser(); p.add_argument("--extraction-json", required=True)
    args = p.parse_args()
    try:
        payload = json.loads(args.extraction_json)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON: {e}", file=sys.stderr); sys.exit(1)
    if "extraction_result" not in payload and "extraction" not in payload:
        print("Error: payload must contain 'extraction_result' key", file=sys.stderr)
        sys.exit(1)
    extraction_payload = payload.get("extraction_result") or payload.get("extraction") or {}
    r = ExtractionResult.from_dict(extraction_payload)
    print(json.dumps(recommend(r, payload.get("intent", "general"))))

if __name__ == "__main__":
    main()
