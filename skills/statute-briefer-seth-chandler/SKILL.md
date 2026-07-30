---
name: statute-briefer
description: >
  Brief statutes and legislative Acts using the MAPS + RULES framework. Use when
  briefing statutes, analyzing legislative text, mapping statutory structure,
  extracting rule-modules from provisions, applying statutes to scenarios, or any
  statutory analysis task. Triggers include "brief this statute," "analyze this Act,"
  "map the statute," "apply [statute] to [scenario]," "what are the elements of
  [provision]," "statutory analysis," or references to codified sections (such as
  42 U.S.C. sections or Texas Health & Safety Code). Supports two modes -
  (A) text-only briefing for structural analysis, and (B) scenario-driven briefing
  that applies statutory provisions to specific facts.
---

# Statute Briefer (MAPS + RULES)

Produce structured statute/Act briefs that (a) map the architecture of the entire statute/Act and (b) express operative provisions as rule-modules. Optionally apply provisions to scenarios with verbatim quotations.

## Input Modes

**Mode A: Text-only briefing**
- Required: Statutory text (or delimited excerpt)
- Optional: Citation info, version type (enacted/codified/amendment), length constraint (short/standard/long)

**Mode B: Scenario-driven briefing**
- Required: Statutory text + scenario description
- Optional: Decision posture (advice/compliance/litigation), length constraint

If citation/version missing, label brief as "text-as-provided" without recency claims.

## Output Structure

Every brief produces two layers. In Mode B, prepend the Scenario Module.

### Scenario Module (Mode B only)

See [references/scenario-template.md](references/scenario-template.md) for detailed template.

Six components:
1. **Scenario synopsis** – Legally salient facts only
2. **Issues framed as statutory questions** – Frame disputes as statutory interpretation questions
3. **Relevant excerpts (verbatim)** – Block-quoted text with pinpoint cites; include adjacent definitions/exceptions
4. **Application map (statute-to-facts)** – For each issue: elements met, unclear, or disputed; identify missing facts
5. **Context map (where excerpts live)** – Title/Chapter/Section path for each excerpt
6. **Not used but structurally important** – Major Act components not triggered by scenario

### MAPS (System-Level Map)

Five components:
1. **Citation and text status** – Citation block or "citation not provided"; note if partial text
2. **Purpose** – Quote express purpose/findings if present (with cite); otherwise label as inference
3. **Structure map (entire Act)** – Hierarchical outline with functional labels ("definitions," "prohibition," "enforcement," etc.); for large statutes, provide major-divisions overview plus zoomed detail
4. **Scope and coverage** – Covered actors, conduct, geography, time, jurisdictional hooks, explicit exclusions
5. **Definitions and interpretive rules** – Defined terms index; interpretive provisions; cross-references

### RULES (Operational Modules)

For each major operative provision (or scenario-relevant provisions), produce a rule-module.

See [references/rule-module-template.md](references/rule-module-template.md) for detailed template.

**Rule-Module required fields:**
1. **Provision** – Pinpoint cite
2. **Trigger conditions (elements)** – What activates the provision
3. **Legal effect** – Command / permission / prohibition / entitlement
4. **Exceptions / defenses / safe harbors** – Carve-outs from the rule
5. **Procedure / decision-maker** – Deadlines, notice, standards
6. **Consequences** – Penalties, remedies, invalidity, loss of benefits
7. **Forum / enforcer** – Agency, court, private plaintiff
8. **Interaction rules** – Preemption/savings, severability, effective date, cross-references

## Mandatory Constraints

### Verbatim Discipline
- Never invent statutory language
- Mark all quotations explicitly with pinpoint cites
- If text is missing, say so and proceed with what is provided

### Cross-Reference Discipline
- When statute defines a term used in operative provision, incorporate that definition
- Flag external cross-references: "cross-reference not included in provided materials"

### Separation of Layers
- Keep "Quoted Text" separate from "Explanation/Translation"
- Use block quotes or clear markers

### No Premature Narrowing
- Even in scenario mode, include MAPS structure map at major-division level

## Selection Rules

**Mode A (no scenario):** Major operative provisions = primary prohibitions/requirements/entitlements + enforcement/remedies + key definitions + preemption/savings/severability/venue

**Mode B (with scenario):** Prioritize provisions governing scenario issues + conditioning definitions/enforcement/exceptions. Still include full structure map.

## Length Control

| Constraint | Structure Map | Rule-Modules | Definitions |
|------------|---------------|--------------|-------------|
| Short | Spine outline only | Most relevant only | Key scope terms only |
| Standard | Major divisions complete | Core operative provisions | Terms affecting scope |
| Long | Full detail | All operative provisions | Comprehensive index |

## Uncertainty Handling

- Insufficient facts → Label "Fact needed: [specific missing fact]"
- Partial statute → Label "based on provided excerpt only"
- Never fill in absent provisions

## Exact Headings (for parsing)

```
Scenario Module
  Scenario synopsis
  Issues framed as statutory questions
  Relevant excerpts (verbatim)
  Application map (statute-to-facts)
  Context map (where excerpts live)
  Not used but structurally important

MAPS
  Citation and text status
  Purpose
  Structure map (entire Act)
  Scope and coverage
  Definitions and interpretive rules

RULES
  Rule-Module: [Provision cite]
```

## Boundaries

- Briefs statutes and legislative Acts only
- No policy commentary unless asked
- No grading or pedagogy commentary
- No generating new statutory text
- No case citations unless explicitly requested; may note "interpretive pressure points" as ambiguity flags
