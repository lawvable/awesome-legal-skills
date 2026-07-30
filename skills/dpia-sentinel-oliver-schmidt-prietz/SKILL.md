---
name: dpia-sentinel-oliver-schmidt-prietz
description: |
  GDPR Data Protection Impact Assessment (DPIA) guidance under Article 35 GDPR, EDPB Guidelines WP 248 rev.01, EDPB Opinion 28/2024 (AI), and national SA blacklists/whitelists. Triggers: "DPIA", "DSFA", "Datenschutz-Folgenabschätzung", "impact assessment", "Art. 35", "do I need a DPIA", descriptions of new high-risk processing (profiling, AI, biometrics, large-scale monitoring, special category data), Art. 36 prior consultation questions, national blacklist/whitelist queries.
metadata:
  author: Oliver Schmidt-Prietz
  license: AGPL-3.0
  version: 2026.06.05
---


# DPIA Sentinel

## Disclaimer (show at session start, do not block)

> **Important:** This skill provides structured GDPR Article 35 guidance based on EDPB Guidelines and national SA requirements. It is not legal advice. Involve your DPO (Art. 35(2)) and qualified counsel for final decisions.

## Routing

Determine what the user needs and load references accordingly:

| User Need | Load These References | Action |
|-----------|----------------------|--------|
| "Do I need a DPIA?" / threshold question | `references/edpb-criteria.md` + relevant jurisdiction file(s) | Run threshold assessment |
| Full DPIA | `edpb-criteria.md` + jurisdiction(s) + `references/risk-catalog.md` + `scoring.md` | Walk through assessment phases |
| Document generation (.docx) — custom format | `references/dpia-custom-population.md` + `references/templates.md` + docx skill | Populate custom template .docx (unpack → fill tables → repack) |
| Document generation (.docx) — EDPB 2026 format | `references/edpb-2026-population.md` + `references/edpb-2026-template.md` + docx skill | Populate official EDPB template .docx (unpack → fill tables → repack) |
| Specific legal question | Load relevant reference only | Answer directly |

**Jurisdiction selection:** Ask two questions: (1) Where is the controller's main establishment? (2) Where are the data subjects located? Load **all** jurisdiction files that are relevant — this may be multiple files for multi-jurisdictional processing. See `references/edpb-criteria.md` → "Multi-Jurisdictional DPIA Analysis" for the full decision framework.

Available jurisdiction files:
- `references/jurisdictions/de-dsk.md` — Germany
- `references/jurisdictions/fr-cnil.md` — France
- `references/jurisdictions/ie-dpc.md` — Ireland
- `references/jurisdictions/be-apd.md` — Belgium
- `references/jurisdictions/nl-ap.md` — Netherlands
- `references/jurisdictions/it-garante.md` — Italy
- `references/jurisdictions/pl-uodo.md` — Poland
- `references/jurisdictions/whitelists.md` — France, Czech Republic, Spain, Austria

For jurisdictions not covered by a dedicated file, rely on the EDPB nine-criteria analysis in `references/edpb-criteria.md` and note that the user should check their national SA's Art. 35(4) list directly.

## Assessment Flow

**Threshold → Description → Asset Inventory → Necessity → Proportionality → Inherent Risks (Track A+B) → Mitigations → Residual Risk → Art. 36 Check → Documentation**

This is the logical sequence, not a rigid script. Adapt to the user: if they provide rich context upfront, skip intake questions. If they're experienced, move faster. If they're new to DPIAs, explain more.

**Asset Inventory** (per EDPB Template 2026, Section 1.3): Collect risk-relevant assets — hardware, software, APIs/models, personnel, sites/premises, organisational assets. Group by logical module or technical layer. Include only assets whose compromise would plausibly impact data subjects' rights and freedoms.

**Necessity and Proportionality** are separate upstream gates (EDPB Template 2026, Section 3). Necessity: is the processing effective and least intrusive? Proportionality: do the benefits justify the impacts? These must be assessed *before* the risk mitigation phase.

**Two risk tracks** (per EDPB Template 2026): Track A identifies inherent-by-design risks (from processing working as intended). Track B identifies operational risks (from accidental/unlawful/abnormal events). Both are scored using the same L×S + modulating factors methodology in `references/scoring.md`.

The assessment is **iterative**: if mitigations in later stages change the processing design, revisit earlier analysis and flag this to the user.

## Legal Precision Points

These are areas where Claude's training knowledge may be imprecise. Always apply these rules:

1. **Art. 35(3) triggers are absolute.** If any of the three mandatory cases apply (systematic extensive automated evaluation with legal/significant effect; large-scale special category/criminal data; systematic monitoring of publicly accessible areas on large scale), a DPIA is required — no balancing, no judgment call.

2. **The two-criteria rule is a presumption, not a mandate.** Meeting 2+ of the 9 EDPB criteria creates a strong presumption a DPIA is needed. But a DPIA *may* be needed with only 1 criterion, and *may* be justified as unnecessary with 2 — if thoroughly documented. See WP 248 rev.01, p. 11.

3. **Art. 9 is cumulative with Art. 6.** Special category data always needs BOTH a legal basis under Art. 6 AND an exception under Art. 9(2). These are separate legal hurdles.

4. **"Large scale" has no fixed number.** The EDPB uses four factors: number of subjects, data volume, duration, geographic extent. An individual doctor is not large scale; a regional hospital is. Never cite a specific numerical threshold.

5. **National blacklists are additive, not exhaustive.** Processing not on a blacklist may still require a DPIA. A blacklist entry in the relevant jurisdiction overrides whitelist exemptions from other jurisdictions.

6. **Multi-jurisdictional processing requires checking ALL relevant blacklists.** Art. 35(4) lists are territorial — the DPIA obligation is triggered if the processing matches a blacklist in ANY jurisdiction where the controller is established OR where data subjects are located. The one-stop-shop mechanism (Art. 56) governs enforcement jurisdiction, but it does NOT limit which Art. 35(4) lists apply to the DPIA obligation itself. A single DPIA can address multiple jurisdictions, but the threshold analysis must run against each applicable national list. See `references/edpb-criteria.md` → "Multi-Jurisdictional DPIA Analysis" for details.

7. **DPIA must happen before processing begins** (Art. 35(1)). It is a pre-processing obligation, not a retroactive compliance exercise. If processing has already started, the DPIA should still be done but note this as a compliance gap.

8. **AI requires dual-phase analysis** (EDPB Opinion 28/2024). Training and deployment are separate processing activities with distinct risk profiles. A deployer cannot simply rely on the model provider's DPIA.

9. **Art. 36 prior consultation is sequential to the DPIA, not part of it.** The DPIA identifies residual risk; if that risk remains high after all feasible mitigations, Art. 36 requires consulting the SA before processing begins. The SA has 8 weeks (extendable by 6).

10. **Pseudonymization as risk reducer** (EDPB Guidelines 01/2025 on Pseudonymisation, adopted 17 January 2025): Effective pseudonymization with technically separated additional information can meaningfully reduce likelihood scores in risk assessment. But it must be genuine — if re-identification is trivial, it doesn't reduce risk.

11. **Risk assessment is from the data subject's perspective.** A DPIA assesses risks to rights and freedoms of natural persons (Recital 75), not corporate/business risks. Identity theft risk to the individual, not reputational risk to the company.

12. **AI Act FRIA is distinct from DPIA.** For high-risk AI systems under the AI Act, a Fundamental Rights Impact Assessment (FRIA) may also be required. DPIA (data protection risks) and FRIA (broader fundamental rights) are complementary — one does not replace the other.

13. **EDPB DPIA Template (v1.0, March 2026)** provides a harmonised EU-wide DPIA structure but does not mandate a specific risk scoring methodology. Controllers may use any established methodology (CNIL PIA, DSK SDM, etc.); the template records the minimum required information in a standardised format. National SA requirements and methodologies remain valid complements. Note: the template was adopted for public consultation — check for final version updates.

## Output Formats

**Threshold result:** Present a clear verdict (DPIA Required / Recommended / Not Required) with the reasoning showing Art. 35(3) check, criteria analysis, and national list check.

**Risk register:** Table with Risk ID, Track (A/B), Description, Rights Category, Likelihood (1-5), Severity (1-5), Score, Modulating Factors, Adjusted Level. Use the scoring methodology in `references/scoring.md`.

**Residual risk overview:** Summary showing total risks by level before and after additional mitigation, plus overall verdict (APPROVED / CONDITIONALLY APPROVED / CONSULT SA / REJECTED).

**Documents:** Both formats use template population (unpack → fill → repack) for consistent styling. Read the docx skill first, then the relevant population guide:
- **EDPB 2026 format:** Populate `references/edpb-2026-template-v1.docx` using `references/edpb-2026-population.md`. Official format recognized by all EU SAs.
- **Custom 12-section format:** Populate `references/dpia-custom-template-v1.docx` using `references/dpia-custom-population.md`. Includes threshold analysis, jurisdictional blacklist detail, risk heat maps, and annexes.

> **If the `.docx` template files are not present** (some hosts, including lawve.ai, store text files only): build the Word document **from scratch with the docx skill following the matching population guide** — the population guides above fully specify every section, table, and field. The pre-styled `.docx` templates are available in the GitHub repo linked at the top of this skill if you want the exact corporate styling.

Ask the user which format they prefer.

## Related GDPR skills

This skill works standalone, but pairs well with my other EU data-protection skills — install any on its own or combine them:

- **GDPR Breach Sentinel** — Art. 33/34 breach response & notification
- **Privacy Notice Generator** — Art. 13/14 privacy notices
- **Transfer Impact Assessment (TIA)** — Chapter V transfer assessments
- **DPA Art. 28** — controller–processor agreements (AVV)
- **Legitimate Interest** — Art. 6(1)(f) LIA / balancing test
