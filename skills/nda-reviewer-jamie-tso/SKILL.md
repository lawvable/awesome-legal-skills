---
name: nda-review-jamie-tso
description: Guide to review incoming one-way (unilateral) commercial NDAs in a jurisdiction-agnostic way, from either a Recipient or Discloser perspective (user-selected), producing a clause-by-clause issue log with preferred redlines, fallbacks, rationales, owners, and deadlines.
metadata:
  author: Jamie Tso
  license: AGPL-3.0
  version: 2025.12.30
---

# NDA Review Playbook (Commercial, Jurisdiction-Agnostic)

## Overview

| What this skill does | What it does not do |
|---|---|
| Reviews an NDA and outputs issues, risks, and suggested redlines | Provide jurisdiction-specific legal conclusions |
| Supports *Recipient* or *Discloser* perspectives (user-chosen) | Guarantee enforceability |
| Produces an executive summary + clause-by-clause markup guidance | Replace counsel for complex deals |

**Scope limitation (important):** this playbook supports **one-way (unilateral) commercial NDAs only**.

If the NDA is **mutual**, stop: this playbook is **out of scope** and you should escalate to counsel or use a separate mutual-NDA review approach.

> **Variation callouts** appear throughout:
> - **M&A / Due diligence**
> - **Employment / contractor**
> - **Investor / VC**

## LEGAL DISCLAIMER

**THIS IS NOT LEGAL ADVICE.** This skill is provided for informational and educational purposes only. Laws vary by jurisdiction and individual circumstances, and only a licensed attorney can provide advice tailored to your specific situation. When the NDA is high-risk, high-value, cross-border, or otherwise sensitive, escalate to qualified counsel.

**Remember:** All outputs from this skill must be reviewed by a qualified legal professional before being used for any legal purposes.

---

## Inputs to collect (ask before reviewing)

### A. Role and deal context (required)
- [ ] Are we reviewing as **Recipient** (we receive confidential info) or **Discloser** (we disclose confidential info)?
- [ ] Confirm the NDA is **one-way (unilateral)**. If it is **mutual**, stop: this playbook cannot be used.
- [ ] What is the **purpose** / permitted use (e.g., evaluation of partnership, vendor RFP, diligence)?
- [ ] What are the **parties** (legal names) and any **affiliates** that should be covered?
- [ ] What information types are expected (tech, pricing, customer data, product roadmap, source code)?
- [ ] Desired **timeline**: when do we need to sign?

### B. Practical constraints (recommended)
- [ ] Do we need to share with **affiliates**, advisors, contractors, auditors, or potential acquirers?
- [ ] Will we need to **export** data across borders or store in cloud tools?
- [ ] Will any **personal data** be shared? If yes, are there separate data-processing terms?

> **Jurisdiction-agnostic note:** avoid asserting “this clause is invalid” without the governing law details; focus on *commercial risk*, *operational feasibility*, and *market norms*.

## Deliverables (output format)

### Quick start (default output template)

ALWAYS output:
1) **Executive summary**
2) **Clause-by-clause issue log** (single table)

### A. Executive summary (1 page)
- [ ] Party role (Recipient or Discloser) and confirmation it is one-way (unilateral)
- [ ] Top 5 negotiation points (ranked)
- [ ] “Sign as-is” / “Sign with changes” / “Escalate” recommendation

### B. Clause-by-clause issue log (lawyer-style, thorough)
Use a single table so counsel and business owners can track issues, owners, and deadlines.

| Clause | Issue (1 line) | Risk (H/M/L) | Preferred redline | Fallback | Rationale (1–2 sentences) | Owner | Deadline |
|---|---|---:|---|---|---|---|---|
| Definition | Overbroad; includes unmarked info with no reasonableness |  |  |  |  |  |  |
| Term & survival | Perpetual confidentiality for all information |  |  |  |  |  |  |
| Use restriction | Purpose too broad; blocks internal evaluation |  |  |  |  |  |  |
| Disclosures | Representatives undefined; strict liability |  |  |  |  |  |  |
| Return/destruction | No backup carve-out |  |  |  |  |  |  |
| Remedies | One-way fees + automatic injunction |  |  |  |  |  |  |
| Liability | Indemnity + unlimited consequential damages |  |  |  |  |  |  |
| Boilerplate | Assignment prohibits change of control |  |  |  |  |  |  |

### Example (compact)

**Executive summary (example skeleton):**
- Role: Recipient (one-way NDA)
- Recommendation: Sign with changes
- Top 5 points: definition scope; term/survival; representatives; backup carve-out; remedies/fees

**Issue log (example rows):**

| Clause | Issue (1 line) | Risk (H/M/L) | Preferred redline | Fallback | Rationale (1–2 sentences) | Owner | Deadline |
|---|---|---:|---|---|---|---|---|
| Term & survival | Perpetual confidentiality for all information | H | Add 2–5 year survival; trade secret carve-out only | 5-year survival for all | Reduces indefinite operational burden while protecting truly sensitive info | Legal | Before signature |
| Return/destruction | No backup carve-out | M | Add backup/legal hold exception + continued confidentiality | Allow retention in immutable backups only | Required for standard IT operations; avoids impossible compliance | Security + Legal | Before signature |

## 5-step workflow

### Step 1 — Identify stance (Recipient vs Discloser)
- [ ] Confirm which side we are on for *this specific NDA* (titles are often misleading).
- [ ] Confirm the NDA is **one-way (unilateral)**. If it is mutual, stop (out of scope).

**Quick heuristic:**
- If we are being asked to keep their info secret → we are **Recipient**.
- If we are sharing our sensitive info → we are **Discloser** (if the NDA is mutual, stop: out of scope).

### Step 2 — Triage the NDA (fast risk scan)
Flag these immediately:
- [ ] **Perpetual** confidentiality for *all* information (no trade secret distinction)
- [ ] **Residuals clause** allowing use of “memory” or generalized knowledge
- [ ] **Injunctive relief** + **attorneys’ fees** one-way against Recipient
- [ ] **Indemnity** for breach or broad third-party claims
- [ ] **No carve-outs** for compelled disclosure or prior knowledge
- [ ] **Overbroad definition**: “all information, whether marked or not” with no reasonableness
- [ ] **Affiliate coverage** missing when we must share internally

> If any are present and the NDA matters, proceed with full review and consider escalation.

### Step 3 — Clause-by-clause review (use the reference modules)
Use these references while reviewing:
- [Key clauses](references/KEY_CLAUSES.md)
- [Party obligations](references/PARTY_OBLIGATIONS.md)
- [Duration & scope](references/DURATION_SCOPE.md)
- [Remedies & liability](references/REMEDIES_LIABILITY.md)
- [Standard exceptions](references/STANDARD_EXCEPTIONS.md)

### Step 4 — Draft redlines and negotiation positions
For each issue, produce:
- **Preferred redline** (best risk outcome)
- **Fallback position** (acceptable compromise)
- **Rationale** (1–2 sentences: business + operational feasibility)
- **Owner** (who needs to approve / negotiate: Legal, Sales, Security, Product)
- **Deadline** (by when the counterparty needs the change)

**Negotiation discipline:** do not propose 20 changes. Focus on the 5–10 that materially change risk.

### Step 5 — Finalize the package
- [ ] Ensure consistency (definitions used the same way everywhere)
- [ ] Confirm operational feasibility (can we actually comply?)
- [ ] Re-scan the Step 2 triage list and ensure each flagged item is represented in the issue log
- [ ] Provide a short “what we changed and why” summary

## Perspective-specific checklists

### A. Recipient checklist (incoming NDA — typical case)

| Topic | Red flags | Typical ask |
|---|---|---|
| Definition of Confidential Information | Overbroad; includes independently developed info; no marking/identification standard | Add reasonableness + identification standard; add exclusions |
| Purpose / Permitted Use | Any use restriction beyond evaluation; bans on internal sharing | Tie to stated purpose; allow internal need-to-know |
| Representatives | We are liable for any representative breach without control | Limit to those under written confidentiality; commercially reasonable care |
| Term & survival | Perpetual for everything; unclear start date | Fixed term; longer only for trade secrets |
| Return / destruction | Requires deletion of backups immediately | Add practical backup carve-out |
| Remedies | One-way fees + broad injunction language | Mutuality or reasonableness; clarify equitable relief scope |
| Liability / indemnity | Indemnity; unlimited damages; consequential damages | Cap or exclude categories; remove indemnity |
| Residuals | Allows use of “retained in memory” | Delete or narrow heavily |

> **M&A / Due diligence:** ensure diligence sharing (advisors, financing, affiliates) is permitted and that data room exports/notes are covered.

### B. Discloser checklist (when we are sharing sensitive info)

| Topic | Red flags | Typical ask |
|---|---|---|
| Definition | Too narrow; requires marking only; excludes oral disclosures | Add oral confirmation mechanism; broaden categories reasonably |
| Security standard | Only “reasonable” with no baseline | Add minimum safeguards, or align with internal policy |
| Exclusions | Too broad (e.g., “independently developed” with no proof) | Require written evidence of prior knowledge/independent development |
| Term & survival | Too short | Extend for sensitive categories; trade secret survival |
| Remedies | No equitable relief, no fees | Add equitable relief and/or fees (carefully) |

> **Investor / VC:** watch for standstill, solicitation, and “no contact” provisions—these are not standard in plain NDAs and may need separate agreement.

## Risk rating guide

| Rating | Meaning | Example |
|---:|---|---|
| High | Creates material, uncapped, or operationally impossible risk | Broad indemnity + unlimited damages for any breach |
| Medium | Risk is real but manageable with process controls | Strict notice deadlines for compelled disclosure |
| Low | Mostly cosmetic or market-standard | Minor notice method issues |

## Common pitfalls (issue → risk → fix)

| Issue | Risk | Suggested fix |
|---|---|---|
| “All information is confidential forever” | Operational burden; unfair risk allocation | Add fixed term + trade secret carve-out |
| No compelled disclosure carve-out | Breach if subpoenaed | Add “required by law” disclosure path |
| Return/destruction requires purge of backups | Impossible to comply | Add backup and system integrity exception |
| Recipient indemnifies discloser | Open-ended exposure | Remove indemnity; use direct damages only |
| Residuals clause | Allows de facto use of confidential info | Delete or restrict to non-trade-secret, non-source-code |

## Review prompts (copy/paste)

### A. Minimal prompt (fast)
- Role: Recipient/Discloser
- NDA type: one-way (unilateral)
- Purpose: …
- Please produce (1) exec summary, (2) clause-by-clause issue log table with: Clause, Issue, Risk, Preferred redline, Fallback, Rationale, Owner, Deadline, (3) top 5 negotiation points.

### B. Deep prompt (recommended)
- Add constraints: affiliates, advisors, contractors, cross-border sharing, personal data, cloud tools.
- Ask for: preferred redline + fallback + rationale per issue.

## Ownership & timing defaults (if the user does not specify)

Use these defaults to populate **Owner** and **Deadline** in the issue log:

| Topic | Default owner | Default deadline |
|---|---|---|
| Confidentiality scope/definition, exceptions, term/survival | Legal | Before signature |
| Security standards / audit rights | Security + Legal | Before signature |
| Return/destruction and backups | Security + IT + Legal | Before signature |
| Liability cap / damages / indemnity / fees | Legal + Finance | Before signature |
| Operational constraints (representatives, affiliates, tooling) | Legal + Business owner | Before signature |
