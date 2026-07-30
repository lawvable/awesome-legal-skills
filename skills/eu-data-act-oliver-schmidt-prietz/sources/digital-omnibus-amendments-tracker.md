# Digital Omnibus Data Act amendments tracker

**Status:** Proposal stage as of 15 May 2026. NOT law. Current text of Regulation (EU) 2023/2854 remains in force unchanged.

**Source:** European Commission proposal for the Digital Omnibus Regulation, COM(2025) 833 final, presented 19 November 2025. The proposal amends multiple instruments including the Data Act, GDPR, ePrivacy Directive, NIS2 Directive, and others.

**Critical rule for skill output:**

Every deliverable that touches a provision affected by the proposed amendments must:

1. Apply the **current law** (Reg. 2023/2854 as published, OJ 22.12.2023) as the operative regulatory text.
2. Flag that a Commission proposal would modify the relevant provision if adopted, with a one-sentence summary of the proposed change.
3. Note that the proposal is in co-legislator negotiations and may be amended substantially before adoption.
4. Not blend proposed text into the operative analysis. Pending amendments inform watch-list strategy, not current compliance.

## Affected Data Act provisions in the proposal

The following items are flagged for cross-reference from scenario cards. Substantive amendment text is in the Commission proposal; this tracker is a navigation aid only.

### Chapter II IoT data access (Arts. 4 and 5)

**Trade-secret refusal grounds (Arts. 4(8), 5(11)).** The proposal would introduce an additional refusal ground where there is a substantial risk that the trade-secret data could be unlawfully acquired, used, or disclosed to entities in third countries operating under legal regimes offering weaker protection than the EU. Case-by-case assessment on objective factors remains required.

**Current law for now:** Art. 4(8) and Art. 5(11) refusal is exceptional, requires demonstration of likely serious and irreparable economic loss on objective elements, on a case-by-case basis. The third-country-misuse-risk ground is NOT yet part of the operative regulation.

### Chapter V B2G (Arts. 14-22)

**Narrowed circumstances for public-sector data requests.** The proposal would narrow the conditions under which public authorities can demand data from businesses in non-emergency situations.

**Current law for now:** Art. 15(1)(b) cumulative conditions and Art. 17 procedural conditions apply as drafted.

### Chapter VI DPS switching (Arts. 23-31)

**Custom-built DPS carve-out expanded (Art. 31).** The proposal would expand Art. 31(1) exemptions for custom-made DPS but limit the expansion to contracts concluded before or on 12 September 2025.

**SME/small-mid-cap exemption.** The proposal would create exemptions for SMEs and small mid-caps providing non-IaaS services under pre-12-Sept-2025 contracts.

**Early termination penalties clarified.** The proposal clarifies that providers may include early termination penalties in fixed-term contracts. This was already discussed in the existing text (Recital 89; standard service fees and early termination penalties are not switching charges), but the Omnibus would put it in operative form.

**Current law for now:** Art. 31 carve-outs apply to custom-built (the majority of main features custom-built for an individual customer) and non-production test/beta services. SME exemptions outside Art. 31 currently flow only from general scope (Art. 7) which does not apply to Chapter VI.

### Chapter VIII Interoperability (Art. 36 smart contracts)

**Smart-contract essential requirements relaxed.** The proposal would remove the "essential requirements" compliance regime for smart contract vendors and instead link compliance to harmonised standards via Commission standard-setting powers.

**Current law for now:** Art. 36 essential requirements (robustness, safe termination, archiving, access control, consistency) apply to smart contract vendors and EU declaration of conformity is required.

### Consolidation: incorporation of other instruments into the Data Act

The proposal would repeal and absorb into the Data Act the following instruments, restructuring much of the EU data acquis into a single regulation:

- Regulation (EU) 2022/868 (Data Governance Act) → new Data Act Chapter VIIa (per Commission proposal structure)
- Directive (EU) 2019/1024 (Open Data Directive) → new Chapter VIIb
- Regulation (EU) 2018/1807 (Free Flow of Non-Personal Data Regulation) → new Chapter VIIc
- Regulation (EU) 2019/1150 (Platform-to-Business Regulation) → repealed (substance covered by DMA/DSA per Commission)

**Critical implication for the skill.** If the Omnibus is adopted, the Data Act becomes the consolidated home for the bulk of the EU data acquis. Scenarios currently routed via the DGA, ODD, or FFD will fold back into Data Act chapters. The skill structure should accommodate this without rebuilding from scratch when the time comes.

**Current law for now:** DGA, ODD, FFD, and P2B Regulation apply as standalone instruments. The skill flags interaction points (Chapter V mentions DGA where relevant) but does not analyse those instruments substantively.

## Legislative status snapshot (15 May 2026)

- 19 November 2025: Commission tabled proposal.
- January 2026 onward: EP committee referrals, rapporteur nominations, amendment tabling.
- Q1-Q2 2026: Council technical talks toward general approach.
- Trilogue not yet concluded for the general Digital Omnibus (the parallel Digital Omnibus on AI reached political agreement May 2026 on a separate track; that track does not amend the Data Act).

Realistic adoption window for the general Digital Omnibus is mid-to-late 2026 at earliest. Substantive amendment during co-legislator negotiation is likely.

## Skill maintenance trigger

When the Digital Omnibus is adopted and published in the OJ:

1. Replace this file with a definitive crosswalk old-text vs new-text.
2. Update `sources/_versions.json` to reflect the amending regulation's CELEX.
3. Fetch the Commission's consolidated version of Reg. 2023/2854 from EUR-Lex and replace `regulation-2023-2854.md`.
4. Archive the pre-Omnibus snapshot under `sources/_archive/{YYYY-MM-DD-pre-omnibus}/`.
5. Update affected scenario cards.
6. Update affected templates (notably the Art. 4(8) refusal letter, the Art. 31 disclosure, and any Chapter V templates).
7. Bump major version.
