---
name: "irac-prompt-stephane-boghossian"
version: 0.1.0
description: |
  Restructure any rough build, research, or legal-drafting request into an IRAC-shaped prompt — Issue, Rule, Analysis, Conclusion — optimized for a frontier model. It's the bar-exam framework, repurposed as prompt engineering. The skill leads with the issue and ends with the conclusion (where models weight attention most), forces you to name your constraints and non-goals, and specifies what "good" looks like before a single token is generated. Use it before any non-trivial build, or whenever a vague ask deserves a precise brief.
triggers:
  - irac this
  - structure this prompt
  - make a proper prompt for X
  - brief the model
  - turn this into a memo prompt
  - prompt like a lawyer
metadata:
  author: "Stephane Boghossian"
  license: "agpl-3.0"
  version: "2026-06-05"
---

# IRAC Prompt

A lawyer doesn't hand an associate "go look into the housing thing." They write a memo: here's the **issue**, here are the **rules** that govern it, here's the **analysis** of how they apply, here's the **conclusion** I want. That same structure is the single biggest lever on frontier-model output quality. This skill turns a vague ask into that brief.

## When to use
- The user has a fuzzy build/research/drafting task and wants a good prompt, not a guess.
- Before kicking off a non-trivial vibecode task (pairs naturally before `/grill-me` and `/yalla`).
- Repackaging a task to hand to a sub-agent or to HAQQ's Justinian.

## The method

Take the user's raw ask and rewrite it into four labelled blocks. **Lead with the issue, end with the conclusion** — models weight the top and bottom of a prompt most.

### I — Issue (top)
One or two sentences: what exactly are we trying to do, and for whom. The single problem statement. If the user gave three problems, pick the one that matters or split into three prompts. *No problem, no solution, no value.*

### R — Rule (constraints)
The governing facts the model must respect:
- Hard constraints (stack, language, libraries, file paths, output format).
- Domain rules (for legal: the statute/clause/jurisdiction; for code: the API contract, existing patterns to match).
- Non-goals — what NOT to do. Lawyers specify what they don't want; do the same.
- Definition of done / what "good" looks like, ideally measurable.

### A — Analysis (the reasoning the model should do)
- Why this matters and who the real user is.
- The known hard part / where prior attempts or weaker models failed.
- The approach or first principles to apply (or explicitly: "figure out the approach, here are the inputs").
- Edge cases to handle: empty state, auth failure, network error, malformed input.

### C — Conclusion (the ask)
The concrete deliverable, restated crisply. What artifact, in what shape, verified how.

## Output contract
Emit the rewritten prompt inside a fenced block the user can copy verbatim, with the four headers (**Issue / Rule / Analysis / Conclusion**). Then, below the fence, a 2–3 line note on what you inferred or assumed, and any gap worth a `/grill-me` pass. Don't pad — if a block is genuinely empty (rare), say so rather than inventing constraints.

## Modifiers (the user can ask for any of these)

**`--adversarial`** — append a three-agent split so no agent grades its own homework (Mike's core trick: *"you don't ask the associate if they double-checked it; you give it to someone else"*):
> Run this as three roles. **Planner**: produce a step plan from the Issue/Rule, no code.
> **Executor**: implement the plan against the Rule constraints. **Tester**: adversarially
> verify the Executor's output against the definition-of-done and edge cases; report failures,
> do not fix. Loop Executor↔Tester until the Tester passes. (Maps to `/grill-me` + `/lecun-world-model`.)

**`--budget`** — prepend a context-budget directive (Mike: performance "drops off a cliff" as context fills):
> Treat the context window as a budget, not a dumpster. Keep this prompt lean. Use parallel
> sub-agents with narrow jobs and fresh context rather than one bloated agent. Compact or start
> a new conversation between phases. Load only the Skills/files each step needs.

**`--voice`** — the user dictated this; tolerate disfluency, infer structure, don't nitpick phrasing.

**`--legal`** — Issue/Rule/Analysis/Conclusion map literally to IRAC. Rule = the statute/clause + jurisdiction; Analysis = application to facts; flag anything JUDGMENT-BOUND (hand to `/law-as-code-audit`). Never assert a legal conclusion the source text doesn't support.

## Worked example

**Raw ask:** "make something that checks if building permits are gonna get rejected"

**Output:**
```
ISSUE
Build a tool that, given a set of ADU building-permit blueprints, flags the corrections a California city plan-reviewer will require — before submission — for the builder filing the permit.

RULE
- Inputs: multi-page blueprint PDFs, table-sized, with dense margin annotations.
- Constraint: OCR alone strips annotations from the wall/element they reference —
  preserve visual context (which wall a "thickness" note belongs to).
- Stack: Anthropic SDK, parallel sub-agents, Skills for the ruleset. No paralegal in the loop.
- Done = ≥70% agreement with the city's real correction letters on a held-out set.
- Non-goal: do not auto-submit or give legal advice; output is an action plan a human files.

ANALYSIS
Prior generation models can't do this — that's the point. The hard part is grounding each rule check in the right region of the blueprint. Chunk the blueprint, pass each chunk + the relevant rules, ask "what's wrong here," then aggregate. Handle: missing pages, illegible scans, blueprints with no annotations.

CONCLUSION
A pipeline that ingests blueprints and returns a precise, per-item correction action plan in <20 min, benchmarked hourly against the correction-letter set.
```
*Inferred: ADU + California + builder-side from "permits." Open question for /grill-me: builder-side only, or also the city reviewer side? (CrossBeam ended up doing both.)*

## Notes
- This skill writes a *prompt*, it doesn't execute the task.
- Inspired by Michael T. Brown's CrossBeam — the personal-injury lawyer who, never having written a line of code, beat 13,000 builders to win Anthropic's 2026 global hackathon by prompting the model the way he briefs an associate. Three modifiers: --adversarial (a plan→execute→test agent split so no agent grades its own homework), --budget (treat the context window as a budget, not a dumpster), and --legal (literal IRAC that flags judgment-bound clauses).
