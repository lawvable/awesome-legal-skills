# Changelog

## 0.2.0 — 2026-05-11

Scope lock: US law only (federal / state / local), with explicit multi-jurisdiction handling for the 50 states + DC + territories and federal/state/local interactions.

- Added `jurisdiction: US (federal, state, local)` to frontmatter
- Rewrote `description` to flag US-only scope and name federal preemption / multi-state comparison as triggers
- Title and intro updated to "US Law" with explicit decline rule for non-US sources
- Added **non-US flag** to Input Requirements: halt and decline if EU/UK/foreign source detected
- Replaced "Cross-Jurisdictional Analysis" section with "Multi-Jurisdiction Handling (Within the US)" covering federal / state / local levels, federal preemption (always escalation), multi-state comparison patterns, and home-rule vs. Dillon's Rule interactions
- Added "Out-of-scope foreign law" failure mode
- Refined "Jurisdiction mismatch" failure mode to call out US-internal patterns (preemption, home-rule)
- Escalation triggers updated: non-US source detected, federal/state/local preemption, ordinance-vs-state conflict, state-vs-federal conflict
- Output Template now splits jurisdiction line into Level + Which, adds federal-preemption-status and inter-state-conflict fields (both flagged for attorney, not declared)
- Out of Scope section explicitly enumerates non-US law as the first excluded category

## 0.1.0 — 2026-05-11

Second pass: skill-creator alignment.

- Rewrote `description` frontmatter to name explicit trigger contexts (combats under-triggering per skill-creator guidance)
- Trimmed inline canons table to summary; pointed to `references/canons_of_construction.md` for depth
- Added a worked Input/Output example alongside the abstract Output Template
- Softened rigid MUSTs by adding "why" rationale where the reasoning could carry the weight
- Collapsed three-section Quick Reference Checklist into a single Pre-Flight Checklist
- Folded the "Consistency and Common Sense" section into one paragraph
- Added "Read when:" guidance for each file in `references/index.md`
- Moved changelog noise from `SKILL.md` into this file

## 0.1.0 — 2026-05-11 (first pass)

Production-hardening pass per QA report dated 2026-05-11. Added:

- Audience section (junior associates / compliance / paralegals; attorney review required)
- Work Shape declaration (Accretive Judgment)
- Out of Scope section (case law, constitutional, treaty, choice-of-law, drafting, lobbying, final opinions)
- Input Requirements with five minima and a halt-and-ask rule
- Delegation Threshold & Accountability section (Draft header, named-attorney requirement)
- Confidence Bands (High / Medium / Low)
- Escalation Logic with seven mandatory halt-and-route triggers
- Failure Modes (advice drift, privilege leakage, accountability gap, cite-staleness, jurisdiction mismatch)
- Structured Output Template
- `version` and `author` in frontmatter

Resolved jurisdiction frontmatter mismatch (was `jurisdiction: US` while examples used GDPR-style language) by making the framework explicitly jurisdiction-agnostic, applied one jurisdiction per analysis.
