---
name: "financial-comparison-glossary-ignacio-adrian-lerer"
description: "Use when a calculator, financial model, investor memo, due diligence report, risk review, dashboard, or client-facing explanation needs clear distinctions between accounting and finance concepts such as cash flow vs profit, EBIT vs EBITDA, CapEx vs OpEx, debt vs equity, market value vs book value, ROI vs ROE, assets vs liabilities, and accounting vs finance."
metadata:
  author: "Ignacio Adrián Lerer"
  license: "agpl-3.0"
  version: "2026-06-14"
---

# Financial Comparison Glossary

Use this skill to prevent conceptual confusion in financial tools, due diligence reports, risk screens, calculators, and client explanations. It is a public/portable glossary layer, not a substitute for a full financial model audit.

This file is self-contained for loaders that read only `SKILL.md`. If calculator/model integrity skills are available, use them too when building or verifying numbers; otherwise apply the checks below directly.

## Core Rule

Do not let a polished interface or memo blur financial categories. If two concepts are different, label them differently and make the model/report show the difference.

## Concepts To Distinguish

- `Cash flow` vs `Profit`: cash flow is timing of cash in/out; profit is accounting result after expenses. A profitable model can have cash stress; positive cash flow is not automatically approved dividends.
- `EBIT` vs `EBITDA`: EBIT includes depreciation/amortization impact; EBITDA excludes interest, taxes, depreciation, and amortization. EBITDA is not free cash flow.
- `CapEx` vs `OpEx`: CapEx purchases long-term assets and affects cash at purchase; OpEx supports ongoing operations and affects current-period operating result.
- `Debt` vs `Equity`: debt has repayment/interest obligations; equity shares ownership/risk/upside and usually has no fixed repayment obligation.
- `Market value` vs `Book value`: market value reflects perceived/current value; book value reflects accounting carrying value.
- `Assets` vs `Liabilities`: assets generate or preserve value; liabilities require future settlement.
- `ROI` vs `ROE`: ROI measures return on an investment/project; ROE measures return generated on shareholder equity.
- `Accounting` vs `Finance`: accounting records and reports past/current transactions; finance models decisions, risk, capital allocation, and future value.

## Calculator And Dashboard Checks

When reviewing a model or dashboard, ask:

- Is EBITDA being presented as cash available, dividends, or value without bridge? If yes, relabel or add bridge.
- Is RF/debt being treated like equity proceeds? If yes, show interest, maturity, repayment/provision, and risk.
- Are CapEx/assets treated as expenses without useful life or exit? If yes, define purchase, operating start, and exit/residual.
- Are dividends/distributions shown before legal, tax, debt, reserve, and cash constraints? If yes, label as economic simulation, not approved dividend.
- Are nominal values mixed with discounted values? If yes, show both and label WACC/discount rate.
- Are gross third-party revenues shown as company revenue when only commission/take-rate belongs to the company? If yes, correct to net commission.
- Are accounting provisions, reserves, and actual cash payments conflated? If yes, separate retained/reserved cash, accounting provision, and cash outflow.

## Client-Facing Explanation Pattern

Use this structure:

1. Define the term in one sentence.
2. State what it is not.
3. Explain why the distinction matters for the decision.
4. Point to the model row/control where it appears.

Example:

```text
EBITDA is operating performance before interest, taxes, depreciation and amortization. It is not cash available for distribution, because debt service, reserves, reinvestment and taxes may still reduce cash. In this calculator, EBITDA is an operating metric; cash available and distributions are separate outputs.
```

## Reliance Boundary

This skill is safe for public explanations and generic client deliverables. It must not include confidential facts, client-specific negotiation strategy, or final accounting, tax, legal, or investment advice.
