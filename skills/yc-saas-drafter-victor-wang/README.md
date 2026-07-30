# YC SaaS Drafting Skill

A Claude skill that drafts a customized **Customer Agreement** starting from the Y Combinator standard form SaaS template. Runs a structured intake, applies 18 always-on defaults that turn the raw YC form into a professional starting point, handles 12 conditional decisions based on the deal, and outputs a clean `.docx` plus a lawyer-facing memo explaining every change.

Built for startup founders and their counsel who want YC's template as a baseline but without the drafting annotations, optional scaffolding, and rough edges.

## What it does

- Renames "SaaS Services Agreement" to "Customer Agreement" throughout
- Adds a proper data privacy section (§2.5)
- Restructures warranties into exclusive remedy / customer warranty / beta disclaimer
- Consolidates SLA and support into a single Exhibit B
- Strips every `[OPTIONAL]`, `*[Note: ...]*`, and drafting annotation
- Substitutes deal variables (company, customer, fees, governing law, etc.)
- Flags attorney-review items (DPA need, ML training rights, IP ownership in services, etc.)

Produces:
1. `[Company]_[Customer]_Customer_Agreement_DRAFT.docx`
2. `[Company]_[Customer]_Customer_Agreement_Memo.md` — every change documented

## How to use

This is a Claude Agent skill. To use it:

1. Drop this folder into your Claude skills directory (e.g., `~/.claude/skills/` for Claude Code / Cowork, or the skills folder of whichever Claude product you use).
2. Start a conversation with a trigger phrase like:
   - "Draft a YC SaaS agreement"
   - "I need a Customer Agreement starting from the YC form"
   - "New SaaS deal with [customer]"
3. Answer the intake questions. Claude will confirm your selections, produce the draft, and deliver the memo.

## What's in this repo

```
yc-saas-drafting-skill/
├── SKILL.md                              # Entry point — workflow and rules
├── assets/
│   └── YC_Form_SaaS_Agreement.docx       # YC's published standard form
└── references/
    ├── intake-questions.md               # 15 question groups with branching
    ├── decision-matrix.md                # Maps answers to template actions
    └── supplementary-language.md         # Verbatim clause text by anchor ID
```

The decision matrix tells Claude **what** to change. The supplementary language gives the **exact text** to insert. The skill does not improvise contract language.

## Attribution

The `assets/YC_Form_SaaS_Agreement.docx` is Y Combinator's standard form SaaS Agreement, published by YC for startup use. Y Combinator is not affiliated with this skill.

## Not a substitute for a lawyer

This skill produces a drafting starting point. Every output includes a memo with flagged items that require attorney review — DPA need, ML training rights, IP ownership in implementation services, derivative data ownership, and data retention. Do not send a draft without counsel review on those points.

## License

[MIT](./LICENSE) — Copyright (c) 2026 Victor @ stokebuilder
