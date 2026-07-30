# Diagram type map (shared)

30 legal categories mapped to Mermaid types. Source taxonomy: legal-diagram discovery doc. Used by `direct.md` Step 2 and `extract.md` Step 5.

**How to read.** When user names a legal category → map to its **primary** type. If row marked **ambiguous** → do not map directly; call `diagram_selector.py` with enriched extraction so entity counts break the tie. **Driving field** = the `ExtractionResult` field dominating selection.

|#|Category|Primary|Alternatives|Driving field(s)|Ambiguous|Quirk|
|---|---|---|---|---|---|---|
|1|Legal process maps|flowchart|state diagram|process_steps, decision_points|no|flowchart|
|2|Legal decision trees|flowchart||decision_points|no|flowchart|
|3|Issue / claim-defense maps|flowchart|erDiagram|concepts, relationships|yes|flowchart|
|4|Chronologies / timelines|timeline|gantt|events|yes|timeline|
|5|Litigation deadline planning|gantt|timeline|tasks, deadlines, phases|no|gantt|
|6|Parties / entity relationships|erDiagram|flowchart, classDiagram|ownership_links, relationships, entities|yes|erDiagram|
|7|Contract architecture|flowchart|mindmap, requirementDiagram|relationships, concepts, documents|yes|flowchart|
|8|Negotiation / position maps|quadrantChart|flowchart, mindmap|negotiation_issues, risk_items|no|quadrantChart|
|9|Compliance obligation maps|requirementDiagram|flowchart, state diagram|obligations, controls|no|requirementDiagram|
|10|Data privacy / data flow|flowchart|sequenceDiagram, erDiagram|data_flows|yes|flowchart|
|11|E-discovery workflows|state diagram|flowchart, gantt|states, transitions, process_steps|yes|state diagram|
|12|Privilege / confidentiality|state diagram|flowchart|decision_points, states, transitions|yes|state diagram|
|13|Regulatory investigation|sequenceDiagram|flowchart, timeline, gantt|communications, events|yes|sequenceDiagram|
|14|Deal / transaction execution|gantt|flowchart, sequenceDiagram, erDiagram|phases, tasks, conditions|yes|gantt|
|15|Funds flow / money movement|sequenceDiagram|flowchart|transfers, communications|yes|sequenceDiagram|
|16|Corporate governance / approvals|state diagram|flowchart, sequenceDiagram|process_steps, conditions|yes|state diagram|
|17|Legal intake / triage|state diagram|flowchart|states, transitions|yes|state diagram|
|18|Legal ops / knowledge mgmt|quadrantChart|flowchart, mindmap|risk_items|yes|quadrantChart|
|19|Client counseling / explanation|journey|flowchart, timeline|process_steps|yes|journey|
|20|Legal research maps|mindmap|flowchart, classDiagram|concepts, legal_authorities|yes|mindmap|
|21|Statutory / regulatory structure|requirementDiagram|flowchart, mindmap|obligations, concepts|yes|requirementDiagram|
|22|Litigation strategy / case theory|quadrantChart|mindmap, flowchart, timeline|risk_items, concepts|yes|quadrantChart|
|23|Depositions / witness prep|mindmap|flowchart, timeline|witnesses|yes|mindmap|
|24|Arbitration / dispute resolution|timeline|gantt, flowchart, sequenceDiagram|events, phases, transitions|yes|timeline|
|25|IP strategy / prosecution|state diagram|flowchart, timeline, mindmap|states, transitions, ip_assets|yes|state diagram|
|26|Employment / HR workflows|timeline|flowchart, state diagram|events, investigation_steps, transitions|yes|timeline|
|27|Real estate / construction|gantt|timeline, flowchart, erDiagram|phases, tasks|yes|gantt|
|28|Bankruptcy / restructuring|timeline|flowchart, erDiagram|claim_classes, transfers|yes|timeline|
|29|Tax planning / controversy|erDiagram|flowchart, timeline|entities, relationships, transfers|yes|erDiagram|
|30|AI / cyber / tech law|requirementDiagram|flowchart, sequenceDiagram, state diagram|obligations, controls, data_flows|yes|requirementDiagram|

**Renderer note.** `Sankey`, `architecture`, `kanban`, `classDiagram` render unevenly. Selector never returns them; substitutes listed primary (e.g. flowchart for Sankey funds flow, erDiagram for classDiagram entity models). Quirk column → row in `shared/parser-guards.md`.

## Mindmap scope rule

Mindmap = **brainstorming and orientation only.** Tree structure: every node has exactly one parent; edges carry no labels; cross-links impossible. Use only when hierarchy is the entire point and relationship precision is not required.

**Mindmap is banned when matter involves any of the following:**

- Arguments, claims, or defenses (directed support/contradiction between nodes)
- Evidence chains (one fact supporting multiple claims, or undermining a defense)
- Obligations, compliance, or regulatory requirements
- Directed causality (X leads to Y leads to Z)
- Parties, entities, or relationships requiring labeled edges or cardinality
- Any intent phrased as "map the arguments", "show how X supports Y", "trace the reasoning"

For all above, use **flowchart** (directed graph with labeled edges). Flowchart expresses everything a mindmap can, plus directed logic, multiple parents, and edge labels. Selector must prefer flowchart over mindmap whenever any precision field is populated in extraction.

**Precision guard (called from `workflows/generation.md` Step 1).** When fixed type is `mindmap`, check enriched extraction for any non-empty precision field: `obligations`, `parties`, `ownership_links`, `relationships`, `risk_level`, `decision_points`, `process_steps`, `communications`, `transfers`, `risk_items`, `legal_authorities`. If any populated, flag mismatch once before proceeding:

> "Mind maps are trees: no labeled edges, no directed logic, no cross-links. Your matter has [populated field(s)], which need directed relationships. A **flowchart** would preserve that precision. Proceed with the mind map, switch to a flowchart, or pick an alternative?"

Wait for user's answer. This counts as the one allowed interruption. After user confirms, honour their choice with no further challenge.

## Plain-language names (user-facing)

In all text user reads, name diagrams with these plain words, never the Mermaid type. Technical name stays internal (scripts, workflows). Accept plain-word requests from user and map back to the type the same way. FR prompts use the FR column both ways (accept and speak).

|Mermaid type|Say to the user|En français|
|---|---|---|
|`timeline`|timeline|chronologie|
|`gantt`|schedule (timeline with durations)|échéancier|
|`flowchart`|flowchart, or "decision tree" when it walks a yes/no test|schéma, ou « arbre de décision »|
|`state diagram`|status flow (how something moves through stages)|flux de statuts|
|`erDiagram`|org chart, or relationship map|organigramme|
|`requirementDiagram`|obligation checklist (compliance map)|liste d'obligations|
|`sequenceDiagram`|who-does-what-when (back-and-forth diagram)|qui-fait-quoi-quand|
|`mindmap`|mind map|carte mentale|
|`quadrantChart`|priority grid (a 2x2)|grille de priorités|
|`journey`|experience map|carte d'expérience|

Example delivery: "I drew a **timeline**. This matter would also work as an **org chart** or an **obligation checklist** — want either?" Not: "recommended_type: timeline, alternatives: erDiagram, requirementDiagram."

