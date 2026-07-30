---
name: "law-expertise-to-skill-ignacio-adrian-lerer"
description: "Turn a lawyer's bounded expertise, workflow, review standard, or legal judgment pattern into a safe, inspectable legal AI skill. Use when a user provides legal memos, comments, checklists, negotiation notes, review habits, compliance playbooks, or professional feedback and wants a reusable Lawve-style skill. Do not impersonate the lawyer or claim to reproduce a person; distill only authorized, source-bounded capability."
metadata:
  author: "Ignacio Adrián Lerer"
  license: "agpl-3.0"
  version: "2026-06-01"
---

# Law Expertise To Skill

Use this skill to convert legal professional know-how into a simple, safe skill package.

## Inputs

Accept:

- Legal workflow notes, memos, comments, checklists, templates, negotiation positions, audit criteria, or review standards.
- A short description of the target legal task.
- User feedback about what the skill should or should not do.

Do not use private client material, confidential firm know-how, privileged communications, or personal traces unless the user confirms authority to use them.

## Workflow

1. Define the legal capability: what the skill helps with, for whom, and under which legal system or practice area.
2. Define source boundaries: what materials were used, what was excluded, and whether the evidence is first-hand, public, generated, or user-described.
3. Extract only reusable capability:
   - issue-spotting criteria;
   - review sequence;
   - risk taxonomy;
   - drafting or negotiation heuristics;
   - escalation thresholds;
   - required disclaimers or source checks.
4. Separate capability from voice:
   - Capability is allowed.
   - Professional tone guidance is allowed.
   - Persona simulation or identity replacement is not allowed.
5. Add safety boundaries:
   - no legal advice beyond the skill scope;
   - no unsupported jurisdictional claims;
   - no hidden source inference;
   - no confidential-data reuse;
   - human lawyer review required for material decisions.
6. Produce a compact skill with:
   - clear trigger;
   - negative scope;
   - step-by-step method;
   - output format;
   - verification checklist.

## Output

Return:

- `What this skill does`: short marketplace description.
- `How to use`: user-facing instructions.
- `SKILL.md`: portable skill text.
- `Source boundaries`: what evidence was used and what was not.
- `Human review points`: decisions that need a lawyer.

## Refusal / Escalation

Refuse or request clarification when the user asks to:

- impersonate a real lawyer without consent;
- use private traces from another person without authority;
- hide source limitations;
- remove human-review requirements from high-stakes legal work;
- present the skill as the actual person or as guaranteed legal advice.
