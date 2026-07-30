---
name: yc-saas-drafter
description: |
  Drafts a customized Customer Agreement starting from the Y Combinator
  standard form SaaS template. Tailors the agreement through structured intake
  questions covering fee structure, data handling, ML rights, implementation
  services, and more. Applies 18 always-on defaults that transform the raw YC
  form into a professional starting point (renamed to "Customer Agreement",
  data privacy section added, warranty restructured, consolidated SLA/support
  exhibit, etc.). Produces a clean .docx and a lawyer-facing memo explaining
  every change from the YC standard. Use when user says "draft a SaaS
  agreement", "YC SaaS", "startup SaaS contract", "customer agreement",
  "SaaS subscription agreement", or "I need a SaaS agreement starting from
  the YC form". Also trigger when the user is a startup founder discussing
  SaaS contracting, even if they don't mention YC specifically.
metadata:
  author: "Victor Wang"
  license: "mit"
  version: "2026-05-12"
---

## Output Requirements

The final .docx must read like a lawyer drafted it. The output must contain:

- **Zero** YC drafting annotations (`*[Note:...]*`, `*[OPTIONAL:...]*`)
- **Zero** placeholder scaffolding (`[OPTIONAL]` markers, option guides)
- **Zero** unfilled template brackets — except deliberate `[TBD — description]`
  markers for values the user couldn't provide, documented in the memo

The agreement title is "Customer Agreement" — NOT "SaaS Services Agreement".

If any annotation, note, or non-TBD bracket appears in the output, the draft
is not ready. Fix it before delivering.

---

## Workflow

### Step 1: Load References

Before asking any questions, read all three reference files:

- `references/intake-questions.md` — 15 question groups with branching and defaults
- `references/decision-matrix.md` — maps answers to YC template actions (18 always-apply defaults, 12 conditional decisions, variable substitutions, raise-with-lawyer flags)
- `references/supplementary-language.md` — pre-written clause text anchored by ID (always-apply blocks and conditional blocks)

The decision matrix tells you WHAT to change. The supplementary language gives
you the EXACT TEXT to insert. Do not improvise contract language — if the
matrix says to insert `#DATA-PRIVACY`, use the verbatim text from
supplementary-language.md. The ONE exception is Order Form Service Fees,
where the LLM composes from fee pattern examples.

### Step 2: Run Intake

Follow the questions in `references/intake-questions.md` in order. Apply
branching logic (e.g., skip implementation fee if no implementation, skip
pilot details if no pilot, skip service capacity if flat pricing).

Key principles:
- Offer defaults but let the user override
- Use `[TBD — description]` for any value the user can't provide yet
- Confirm all decisions in a summary before proceeding (template at the
  end of intake-questions.md)
- Do NOT proceed to document assembly without user confirmation

### Step 3: Produce the Agreement

Read the YC template from `assets/YC_Form_SaaS_Agreement.docx`.

Apply modifications in this order:

**First — Always-apply defaults** (decision-matrix.md Section A, items A1-A18):
1. Rename Order Form title → "Order Form Number One"
2. Rename "SaaS Services Agreement" → "Customer Agreement" throughout
3. Update preamble date year
4. Section 1.1 SLA reference — remove [OPTIONAL], always on
5. Section 1.2 — change "Exhibit C" to "Exhibit B"
6. Section 2.2 — strip export controls note (keep the language)
7. Section 2.3 — delete customer indemnity clause + note entirely
8. Section 2.5 — insert `#DATA-PRIVACY` (new section)
9. Section 3.3 — remove optional framing (keep analytics language)
10. Section 6 — restructure into 6.1/6.2/6.3: insert `#WARRANTY-REMEDY`,
    `#CUSTOMER-WARRANTY`, `#BETA-DISCLAIMER`
11. Section 7 — remove optional note, remove "United States" from patent scope
12. Section 8 — strip negotiation note
13. Section 9 — replace YC press release language with `#MARKETING-DEFAULT`
14. Exhibits — replace B + C with `#EXHIBIT-B-CONSOLIDATED`, delete Exhibit C
15. Strip ALL remaining annotations and notes

**Second — Conditional decisions** (decision-matrix.md Section B, items B1-B12):
Walk through each conditional decision. For each, look up the intake answer
and apply the specified action. When the matrix references supplementary
language (e.g., `#NO-AUTO-RENEWAL`), use the verbatim text.

**Third — Variable substitutions** (decision-matrix.md Section C):
Replace all YC placeholders with intake values. Any field not collected →
`[TBD — description]`.

**Fourth — Cleanup:**
- Remove any surviving annotations, brackets, or drafting guidance
- Remove empty paragraphs left by deleted sections
- Verify section numbering is sequential (especially after §2.5 addition
  and §6 restructure into 6.1/6.2/6.3)
- Verify no non-TBD brackets remain

**DocX formatting notes:**
- Exhibit B credit table MUST be a proper Word table, not inline text
- Exhibit B communication channels MUST be a proper Word table
- Section 6 subsections (6.1, 6.2, 6.3) need proper heading formatting
- Section 6.3 (Beta Products) must be ALL CAPS

Produce the output as a .docx file:
`[CompanyName]_[CustomerName]_Customer_Agreement_DRAFT.docx`

Use available document creation tools (native DocX skill, python-docx, or
equivalent) to produce a professionally formatted Word document.

### Step 4: Produce the Lawyer Memo

Create a markdown memo alongside the agreement:
`[CompanyName]_[CustomerName]_Customer_Agreement_Memo.md`

The memo must include:

**1. Deal Summary** — One paragraph: who, what, fee structure, term.

**2. Template Base** — "This agreement is based on the Y Combinator standard
form SaaS Agreement with the following modifications."

**3. Always-Applied Defaults** — Itemized list of every always-apply change
(A1-A18), with brief rationale for each. Example:
- "Renamed to 'Customer Agreement' (professional standard)"
- "Removed 'United States' from IP indemnity patent scope (standard redline)"
- "Added Section 2.5 data privacy and security provisions (essential for modern SaaS)"
- "Added Section 6.2 customer warranty and Section 6.3 beta products disclaimer"

**4. Intake-Driven Decisions** — Each conditional decision and what was
selected. Example:
- "Section 3.2: Customer owns derivative data (bracketed language retained)"
- "Section 5.1: Auto-renewal with 60-day notice"

**5. Items Requiring Attorney Review** — This is critical. For each
raise-with-lawyer flag (decision-matrix.md Section D), include the flag
text verbatim. These are:
- DPA recommendation (almost always needed)
- Implementation services IP ownership (if applicable)
- Derivative data ownership (if company retains)
- ML training on customer content (if applicable)
- Data retention timeline confirmation

**6. TBD Items** — Every `[TBD — description]` in the document, listed so
the founder knows what to fill in before sending.

### Step 5: Deliver

Provide the user with:
1. The clean .docx Customer Agreement
2. The lawyer memo
3. Brief summary: key decisions, TBD count, attorney review items

---

## Decision Points Quick Reference

| # | Location | What's Decided |
|---|----------|---------------|
| B1 | Order Form | Services description (from product intake) |
| B2 | Order Form | Fee structure + service capacity (8 fee types) |
| B3 | Order Form + Exhibit A | Implementation services: include or remove |
| B4 | Order Form | Pilot period: include or remove |
| B5 | §2.1 | Distributed software license: include or remove |
| B6 | §3.2 | Derivative data: customer owns or company retains |
| B7 | §5.1 | Auto-renewal: yes (30/60/90 day notice) or no |
| B8 | §5.2 | Data retention period on termination |
| B9 | §9 | Governing law: state selection |
| B10 | §9 | Marketing formulation: default, more, or less |
| B11 | Exhibit B | SLA availability: 99.9% / 99.95% / 99.99% |
| B12 | Exhibit B | Support details: email, phone, hours, tool |

---

## Supplementary Language Reference

| Anchor | Clause | Type |
|--------|--------|------|
| #DATA-PRIVACY | §2.5 Data privacy & security | Always |
| #WARRANTY-REMEDY | §6.1 Exclusive warranty remedy | Always |
| #CUSTOMER-WARRANTY | §6.2 Customer warranty | Always |
| #BETA-DISCLAIMER | §6.3 Beta products (ALL CAPS) | Always |
| #MARKETING-DEFAULT | §9 Marketing language | Always |
| #EXHIBIT-B-CONSOLIDATED | Exhibit B: SLA + Support | Always |
| #NO-AUTO-RENEWAL | §5.1 Manual renewal replacement | Conditional |
| #FEE-EXAMPLES | Order Form fee patterns (8 types) | Conditional |
| #EXPANDED-DATA-RESTRICTIONS | Sensitive data protections | Conditional |
| #ML-TRAINING | ML model training rights | Conditional |
| #ML-FEDERATED | Federated learning carve-out | Conditional |

---

## What This Skill Does NOT Do

- **Does not draft DPAs.** Flags DPA need in memo; use dpa-drafter separately.
- **Does not handle professional services agreements.** If the deal has
  significant services beyond implementation, use msa-drafter.
- **Does not review or redline incoming contracts.** This drafts from a
  template. For review, use a review skill.
- **Does not invent clause language.** Every modification is a deletion,
  variable substitution, or verbatim insertion from supplementary-language.md.
  Exception: Order Form Service Fees, composed from fee pattern examples.
- **Does not resolve attorney review items.** Flags them in the memo for
  counsel to address.
