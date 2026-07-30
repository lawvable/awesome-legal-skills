---
name: "dpdpa-gdpr-review-parth-desai"
description: "Performs structured compliance review, clause redlining, and drafting suggestions for legal documents (privacy policies, data processing agreements, vendor and SaaS contracts) against India's DPDPA 2023 and the EU GDPR. Flags clauses as compliant, at-risk, or non-compliant with reasoning, and proposes ready-to-use model replacement language."
metadata:
  author: "Parth Desai"
  license: "agpl-3.0"
  version: "2026-05-20"
---

# DPDPA & GDPR Legal Review Skill

Performs structured compliance review, redlining, and drafting suggestions on legal documents
against **DPDPA 2023** (India) and **GDPR** (EU/EEA). Produces annotated output with:
- ✅ Compliant clauses
- ⚠️ Suspect / at-risk clauses (with reasoning)
- 🔴 Non-compliant / missing clauses
- 📝 Redline suggestions (proposed replacement language)

---

## Step 1 — Identify Scope

On receiving a document, determine:
1. **Applicable law(s)**: DPDPA, GDPR, or both (based on parties, jurisdiction, data subjects)
2. **Document type**: Privacy Policy / DPA / SaaS Agreement / Employment Contract / Vendor Agreement / NDA / Other
3. **Data types mentioned**: personal data, sensitive personal data (SPD), children's data, health, financial

> If jurisdiction or parties are ambiguous, state your assumption clearly before proceeding.

---

## Step 2 — Clause Extraction & Mapping

Parse the document into logical clause groups. Map each to the relevant legal obligation:

| Clause Group | DPDPA Reference | GDPR Reference |
|---|---|---|
| Purpose of processing | §6 – Notice | Art. 13/14 – Transparency |
| Lawful basis / consent | §6–§9 | Art. 6 / Art. 7 |
| Data fiduciary / controller identity | §8 | Art. 13(1)(a) |
| Data principal / subject rights | §11–§14 | Art. 15–22 |
| Data retention / erasure | §8(7), §13 | Art. 5(1)(e), Art. 17 |
| Cross-border transfer | §16 | Art. 44–49 |
| Children's data / parental consent | §9 | Art. 8 |
| Grievance / DPO contact | §8(10), §13(5) | Art. 37–39 |
| Security obligations | §8(5) | Art. 32 |
| Breach notification | §8(6) | Art. 33/34 |
| Data processor obligations | §8(2)–(3) | Art. 28 |
| Sub-processor / consent manager | §3(5), §8(2) | Art. 28(2) |

---

## Step 3 — Compliance Analysis

For each clause group, apply checks from `references/dpdpa-checklist.md` and `references/gdpr-checklist.md`.

### Redline Format

When flagging or rewriting a clause, use this format:

```
──────────────────────────────────────────
CLAUSE: [Clause title / section number]
STATUS: ⚠️ SUSPECT | 🔴 NON-COMPLIANT | ✅ COMPLIANT
LAW: DPDPA §__ | GDPR Art. __
ISSUE: [Plain-language explanation of risk]
ORIGINAL TEXT:
  "[paste original clause]"
REDLINE SUGGESTION:
  "[Proposed replacement or addition]"
RISK LEVEL: HIGH | MEDIUM | LOW
──────────────────────────────────────────
```

---

## Step 4 — Summary Report

After full analysis, output a **Compliance Summary** table:

```
## Compliance Summary

| Area | DPDPA Status | GDPR Status | Risk |
|------|-------------|------------|------|
| Consent mechanism | ⚠️ Weak | ✅ OK | Medium |
| Data retention | 🔴 Missing | 🔴 Missing | High |
| Children's data | N/A | ⚠️ Unclear | Medium |
| Cross-border transfer | ⚠️ Unaddressed | ✅ SCCs present | High |
| Breach notification | ✅ Present | ✅ Present | Low |
...

Overall Risk: HIGH / MEDIUM / LOW
Recommended Actions: [numbered list]
```

---

## Step 5 — Drafting Suggestions

For every `🔴 NON-COMPLIANT` or `⚠️ SUSPECT` finding, provide:
1. **Why it's risky** (legal exposure, penalty risk under DPDPA or GDPR)
2. **Model clause** (ready-to-use replacement language)
3. **Optional: Alternative formulation** if context is ambiguous

Reference `references/model-clauses.md` for standard clause templates.

---

## Behaviour Rules

- **Never give definitive legal advice.** Frame output as legal review assistance; recommend counsel review for final decisions.
- **Be specific**: cite exact DPDPA section or GDPR article for every finding.
- **Flag children's data immediately** — highest risk tier under both laws.
- **Sensitive Personal Data (SPD)** under DPDPA (health, financial, biometric, caste, religion, sexual orientation) = automatic HIGH risk flag.
- **Special category data** under GDPR Art. 9 = automatic HIGH risk flag.
- If document is in mixed language (e.g., English + Hindi), analyse both portions.
- Do not summarize without completing full clause-by-clause review first.

---

## Reference Files

| File | When to Read |
|------|-------------|
| `references/dpdpa-checklist.md` | DPDPA-specific clause checks |
| `references/gdpr-checklist.md` | GDPR-specific clause checks |
| `references/model-clauses.md` | Ready-to-use replacement clause language |

Load the relevant reference(s) before beginning analysis.
