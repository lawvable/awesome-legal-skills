# USA (non-DPF) — TIA Country Profile

Last verified: 2026-05-31

For DPF-certified US importers, use `us-dpf.md` instead. This profile covers transfers to US importers that are NOT certified under the EU-US Data Privacy Framework.

## Adequacy Status

**Adequacy:** Yes, for DPF-certified organisations only (Implementing Decision (EU) 2023/1795 of 10 July 2023). For non-DPF importers, no adequacy applies — Art. 46 + TIA required.

**Political fragility:** The DPF rests on Executive Order 14086 and the Data Protection Review Court. Both are executive-branch constructs that a future administration could rescind or restructure, and a Schrems III-style challenge to the adequacy decision is foreseeable. Treat the durability of the DPF basis as a live, forward-looking risk rather than a settled fact.

## Data Protection Framework

**General law:** No comprehensive federal data protection law. Sectoral laws: HIPAA (health), GLBA (financial), COPPA (children), FCRA (credit), CCPA/CPRA (California), VCDPA (Virginia), CPA (Colorado), CTDPA (Connecticut), and ~15 other state laws.

**Supervisory authority:** FTC under "unfair or deceptive practices" (Section 5 FTC Act). State Attorneys General. No EU-style single DPA.

**Data subject rights:** Patchwork. Access, deletion, opt-out exist in state laws but coverage is uneven. No general right to object or rectification at federal level.

**Effective remedies:** Private rights of action are state-law-specific and limited. FTC enforcement is consent-decree-based.

## Surveillance & Government Access Laws

### Section 702 FISA (50 U.S.C. § 1881a)

**Scope:** Permits targeted collection of communications of non-US persons reasonably believed to be located outside the US. Compels US-based electronic communication service providers (ECSPs) to assist.

**Powers:** Bulk collection through PRISM (downstream from US providers) and UPSTREAM (cable taps). The Reforming Intelligence and Securing America Act (RISAA, signed 20 April 2024) reauthorised Section 702 for two years — sunset 20 April 2026 — and broadened the definition of electronic communication service provider. **Status as at 2026-05-31:** the RISAA two-year reauthorisation lapsed at the 20 April 2026 sunset, and Section 702 is now operating on short-term extensions — a clean 45-day extension runs to ~12 June 2026, with no long-term reauthorisation agreed and the warrant-requirement reform unresolved. Section 702 therefore **remains operative**; re-verify at each extension cliff (next ~12 June 2026) and carry it as a standing Step 6 monitoring trigger.

**Guarantee A — Clear, precise, accessible rules:** **Insufficient.** FISA Court orders and procedures are classified. Section 702 procedures are partially declassified but the "About" collection rule and minimisation procedures remain opaque.

**Guarantee B — Necessary and proportionate:** **Insufficient.** Bulk collection by design. CJEU in Schrems II concluded Section 702 surveillance "is not limited to what is strictly necessary."

**Guarantee C — Independent oversight:** **Concerns identified — and degrading since the 2023 adequacy assessment.** FISA Court provides judicial oversight but operates ex parte (no adversary). The PCLOB — relied on in the EO 14086 oversight architecture — lost its quorum in January 2025 (three members removed; a district court ordered reinstatement, but the order was stayed on appeal and the matter deferred pending the Supreme Court), leaving it unable to start new oversight. Separately, *Trump v. Slaughter* (US Supreme Court, argued 8 December 2025, decision expected ~June 2026) may remove for-cause removal protection for FTC and PCLOB members — a structural-independence pillar the adequacy decision relied on. Both developments post-date the 2023 snapshot the EU General Court endorsed in Latombe.

**Guarantee D — Effective remedies:** **Concerns identified (post-EO 14086).** EO 14086 created the Data Protection Review Court (DPRC), and the EU/EEA was designated a "qualifying state" on 30 June 2023 — so the redress mechanism **is** available to EU data subjects for non-DPF transfers too, not only in the DPF context. Its *effectiveness* as an Article 47 Charter remedy is, however, contested: the DPRC is an executive-branch body (not a court in the EU sense), its proceedings are non-adversarial and classified, and it has not been tested by the CJEU. Treat redress as legally available but of uncertain effectiveness pending a future CJEU ruling.

### Executive Order 12333

**Scope:** Authorises foreign intelligence collection outside the US by NSA/CIA. Covers cable taps abroad, satellite intercepts, hacking of foreign systems.

**Powers:** Effectively unbounded for non-US persons abroad.

**Guarantees A-D:** **Insufficient across all four.** Operates entirely outside the FISA framework. No judicial oversight, no individual redress.

### CLOUD Act (18 U.S.C. § 2713)

**Scope:** Requires US-based providers to produce data in their "possession, custody, or control" regardless of where stored. Extraterritorial reach to data of EU subjects held by US providers' subsidiaries abroad.

**Powers:** Subpoena, court order, or warrant compelling production. Provider may move to quash if foreign law would be violated. The CLOUD Act also created the executive-agreement framework (18 U.S.C. § 2523), under which a UK-US agreement is in force.

**Guarantee A — Clear, precise, accessible rules:** **Adequate.** Defined process under existing US criminal procedure.

**Guarantee B — Necessary and proportionate:** **Concerns.** Standard varies by process type (subpoena lowest, warrant highest).

**Guarantee C — Independent oversight:** **Concerns.** Warrants reviewed by judges; subpoenas not subject to prior judicial review.

**Guarantee D — Effective remedies:** **Concerns.** Provider can challenge; data subject typically cannot.

### Executive Order 14086 (October 2022)

**Effect:** Established binding signals-intelligence limitations on necessity and proportionality. Created the Data Protection Review Court for individual redress.

**Status:** Foundation of the DPF adequacy decision. The signals-intelligence safeguards and the DPRC redress mechanism are formally available to all EU/EEA data subjects whose data is collected (the EU was designated a "qualifying state" on 30 June 2023), regardless of whether the importer is DPF-certified.

**Political fragility:** EO can be rescinded by future administrations.

## Practical Risk Factors

- **Transparency reporting:** Major US providers (Google, Microsoft, Meta, Apple, Amazon) publish biannual transparency reports showing government requests and compliance rates. Use as evidence of importer's exposure.
- **Sectoral targeting:** Section 702 is intelligence-focused — businesses outside intelligence-relevant sectors face lower realistic risk.
- **Importer size:** Hyperscale cloud providers are higher-risk targets than small B2B SaaS.
- **Data type:** Communications metadata and content are higher-risk than e.g. payroll records.

## Recommended Supplementary Measures

Default suggestions for US non-DPF transfers:

- **TM-1** (encryption with exporter-held keys) — critical for any data the importer doesn't need to read
- **TM-2** (pseudonymisation) — where service can function without identifiers
- **CM-1** (transparency obligation) — importer commits to notify and publish transparency reports
- **CM-2** (challenge clause) — importer commits to challenge overbroad requests via available US legal process
- **OM-3** (government request handling policy) — formal request review process

**Where supplementary measures are likely insufficient:**
- Importer must process plaintext (cloud SaaS where decryption is required for service function)
- Hyperscale provider where the realistic probability of FISA 702 targeting is non-trivial
- Communications content (subject to Section 702 PRISM/UPSTREAM)

In those cases, the skill flags: consider non-US alternatives, on-premises deployment, or EU sovereign cloud.

## Key Sources

- 50 U.S.C. § 1881a (FISA Section 702)
- Executive Order 12333
- 18 U.S.C. § 2713 and § 2523 (CLOUD Act — extraterritorial disclosure + executive-agreement framework)
- Executive Order 14086 (October 2022)
- Implementing Decision (EU) 2023/1795 (DPF adequacy)
- Schrems II, C-311/18 (CJEU, 16 July 2020) — paragraphs on Section 702 / EO 12333
- PCLOB Section 702 reports
- Major US provider transparency reports (Google, Microsoft, Meta, Apple, Amazon)
- Rosenthal "Lawful Access" FAQ (May 2025) — Sections D, E on US law
