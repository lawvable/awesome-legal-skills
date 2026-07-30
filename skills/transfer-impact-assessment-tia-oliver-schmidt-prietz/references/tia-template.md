# TIA Document Template

This file defines the structure of the formal TIA document produced by the skill. The skill emits Markdown (preview) and `.docx` (formal) versions of the same structure.

Use the CNIL TIA Guide tables as the visual model for the assessment sections.

---

## Cover Page

| Field | Content |
|---|---|
| Document title | Transfer Impact Assessment — [Importer Name] |
| TIA reference | `TIA-<DEST-CC>-<YYYY>-<seq>` (e.g. `TIA-US-2026-001`) |
| Version | 1.0 (initial) |
| Date of assessment | YYYY-MM-DD |
| Next review date | YYYY-MM-DD |
| Exporter | Name, role, EEA establishment |
| Importer | Name, role, country |
| Assessor | Name, role |
| Approved by (DPO) | Name, date |

## Section 1: Transfer Description (EDPB Step 1)

Structured intake table:

| Field | Value |
|---|---|
| Exporter | |
| Exporter role | Controller / Joint controller / Processor |
| Importer | |
| Importer role | Controller / Processor / Sub-processor |
| Importer country | |
| Importer sector | |
| Data categories | (list, with Art. 9 categories flagged) |
| Data subjects | (employees, customers, patients, …) |
| Purpose | |
| Volume | |
| Frequency | One-off / Periodic / Continuous |
| Data format in transit | Plaintext / TLS-encrypted / E2E-encrypted |
| Data format at rest | Plaintext / Encrypted (importer keys) / Encrypted (exporter keys) / Pseudonymised |
| Onward transfers | Yes (list) / No |

## Section 2: Transfer Tool (EDPB Step 2)

| Field | Value |
|---|---|
| Primary mechanism | Adequacy / SCCs / BCRs / Ad hoc / Code / Cert / Art. 49 |
| Mechanism details | (SCC module + execution date / BCR ref / decision ref) |
| Fallback mechanism (if any) | (e.g. Art. 49(1)(b) noted alongside SCCs) |
| Documentation evidence | (signed copies, decision references) |

## Section 3: Third-Country Assessment (EDPB Step 3)

### Block A — Data protection framework

(CNIL-style table)

| Question | Finding |
|---|---|
| General data protection law? | Yes / No — name, scope |
| Independent SA? | Yes / No — name, independence assessment |
| Data subject rights? | Access, rectification, deletion, objection — gaps noted |
| Effective remedies and sanctions? | Yes / Partial / No — justification |

### Block B — Surveillance / government access laws

For each relevant law (from country profile):

| Law | Scope | Powers | Guarantee A | Guarantee B | Guarantee C | Guarantee D |
|---|---|---|---|---|---|---|

(adequate / concerns / insufficient for each guarantee)

### Block C — Practical risk assessment

| Question | Finding |
|---|---|
| Importer history of government access requests? | (cite transparency reports) |
| Realistic targeting basis? | (sector, data type, scale) |
| Importer technical access to plaintext? | Yes / No |
| Realistic authority interest in this data? | (justify) |

### Step 3 Conclusion

Choose ONE:
- ☐ (1) Transfer tool effective — proceed without supplementary measures
- ☐ (2) Transfer tool not effective — supplementary measures needed
- ☐ (3) Transfer tool not effective on paper, but no realistic basis to believe problematic law will apply — proceed with thorough documentation

**Justification:** (mandatory for all three; option 3 requires substantive — not boilerplate — reasoning)

## Section 4: Supplementary Measures (EDPB Step 4)

(only if Step 3 conclusion = 2)

| Measure | Type | Addresses Gap | Implementation Status | Effectiveness Assessment |
|---|---|---|---|---|

(Technical / Contractual / Organisational; Planned / In progress / Implemented; Effective / Partial / Insufficient)

**Overall effectiveness:** ☐ Sufficient → proceed ☐ Insufficient → restructure or suspend

## Section 5: Implementation Action Plan (EDPB Step 5)

| Action | Owner | Due | Status |
|---|---|---|---|

## Section 6: Monitoring (EDPB Step 6)

| Trigger Type | Trigger | Action |
|---|---|---|
| Standing | Adequacy decision review date | Re-verify status |
| Standing | DPF political risk monitoring | Quarterly check |
| Event-driven | New surveillance law in country | Re-assess Block B |
| Event-driven | SA enforcement action | Review applicability |
| Event-driven | Importer receives government request | Re-assess Block C |
| Periodic | Annual review | Full re-assessment |

**Next periodic review date:** YYYY-MM-DD

## Annex A: Country Profile Summary

Embed or reference the country profile used for the assessment.

## Annex B: Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Assessor | | | |
| DPO | | | |
| Legal review (if applicable) | | | |
