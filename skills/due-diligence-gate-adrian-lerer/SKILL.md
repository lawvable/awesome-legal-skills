---
name: "lawve-public-due-diligence-gate-ignacio-adrian-lerer"
description: "Use for due diligence, legal-financial risk review, investment or business transaction checklists, and preliminary screening where facts, documents, assumptions, legal uncertainty, debt/equity, assets/liabilities, contracts, tax, regulatory, compliance, technology/product, and financial-model issues must be separated clearly."
metadata:
  author: "Ignacio Adrián Lerer"
  license: "agpl-3.0"
  version: "2026-06-14"
---

# Lawve Public Due Diligence Gate

Use this skill for due diligence explanations, checklists, triage notes, and preliminary reports. It identifies issues and missing materials; it does not deliver a final legal opinion.

This file is self-contained for loaders that read only `SKILL.md`. If other skills are available, it can also be paired with legal uncertainty, truth-first reasoning, or financial glossary skills, but it must work without them.

## Core Rule

Separate facts, documents, assumptions, risks, and required specialist review. Do not convert missing evidence into confident conclusions.

## Reasoning Standard

- Verify before validating a claim.
- Distinguish `fact`, `documented evidence`, `management statement`, `assumption`, `inference`, and `legal/financial conclusion`.
- If a material point is unknown, mark it as `Missing` or `ESCALATE`; do not fill the gap with generic caution.
- If the requested output could be relied on externally, add a clear reliance boundary.

## Public Scope

Safe public outputs may include:

- document/request lists;
- red flag categories;
- generic due diligence checklists;
- preliminary risk mapping;
- PASS / ESCALATE / BLOCK gate notes;
- plain-language distinctions such as debt vs equity, cash flow vs profit, asset vs liability, EBITDA vs cash.

Do not include:

- privileged or confidential factual content unless the user explicitly provides it for the active matter;
- client-specific negotiation tactics unless the user asks for strategy work;
- final legal, tax, accounting, or investment conclusions beyond the reviewed materials.

## Intake Contract

Before relying on an answer, identify:

- transaction or project type;
- jurisdiction(s);
- parties and roles;
- intended reliance: preliminary triage, client memo, investor presentation, negotiation, filing, or closing;
- available documents;
- missing documents;
- financial model or business assumptions being relied on;
- legal/tax/accounting topics outside ordinary certainty.

## Due Diligence Buckets

Check these buckets and mark each as `OK`, `Issue`, `Missing`, or `ESCALATE`:

- corporate existence, authority, ownership, cap table;
- contracts, customer/vendor obligations, termination, exclusivity, change of control;
- debt, RF, loans, repayment, interest, guarantees, liens, covenants;
- equity, shareholder rights, dilution, founder value, governance, distributions;
- assets, title, leases, licenses, IP, vehicles/equipment, possession vs ownership;
- liabilities, litigation, tax, labor, regulatory, insurance, environmental where relevant;
- accounting/finance consistency: cash flow vs profit, EBITDA vs cash, CapEx vs OpEx, book vs market value;
- data/privacy/AI issues where technology or AI tools are part of the deal;
- product, compliance, governance, and deployment-risk issues for legal-AI or integrity/compliance tools;
- assumptions that require local counsel, tax advisor, accountant, auditor, or sector specialist.

## Financial Concept Checks

Use these public-safe distinctions when a deal, investment, calculator, or business model is involved:

- `Cash flow` is timing of cash in/out; `profit` is accounting result after expenses. Positive profit does not guarantee liquidity.
- `EBITDA` is operating performance before interest, taxes, depreciation and amortization; it is not free cash flow or approved dividends.
- `CapEx` buys long-term assets; `OpEx` supports current operations.
- `Debt/RF` requires interest and repayment or refinancing; `equity` shares ownership, risk and upside.
- `Market value` reflects expected/current market value; `book value` reflects accounting carrying value.
- `Assets` may generate value; `liabilities` require settlement.
- `ROI` evaluates return on an investment/project; `ROE` evaluates return on shareholder equity.

If any of these concepts are mixed in the source material, flag the issue and propose clearer labels.

## Output Gate

Use this compact structure:

```text
State: PASS | ESCALATE | BLOCK
Purpose:
Materials reviewed:
Key assumptions:
Confirmed points:
Open issues:
Missing documents:
Risks by bucket:
Required next step:
Safe for external reliance: yes/no
```

## Decision Rules

- `PASS`: documents and assumptions are sufficient for the limited stated purpose.
- `ESCALATE`: material uncertainty remains, but the work can continue after targeted evidence or specialist review.
- `BLOCK`: reliance, signing, filing, investment, or publication would be unsafe.

## Public Wording Standard

Use cautious but concrete language:

- "Based on the materials reviewed..." rather than "it is certain".
- "Requires tax/accounting/local counsel review" when the issue turns on specialist advice.
- "The model assumes..." when a financial output depends on unverified inputs.
- "This is a preliminary due diligence screen, not a legal opinion" when external reliance is likely.
