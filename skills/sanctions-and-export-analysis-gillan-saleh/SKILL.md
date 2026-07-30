---
name: "sanctions-screening-legal-analysis-skill-english-gillan-saleh"
description: "Sanctions and export control analysis tool for Claude Desktop. Real-time individual screening across 30+ official lists (UN, EU, OFAC, OFSI, French DGT...), sectoral analysis, dual-use goods (EU Reg. 2021/821), US/China extraterritorial regimes (EAR, ITAR, FDPR, ECL), USD/SWIFT risk and jurisdictional mapping across 30+ countries. All results sourced and verified in real time — no memory-based answers. Responds in French, English, German, Spanish, Russian and Chinese. Updated 19 May 2026 (EU 20th package, UK SEUC, Cuba EO). Indicative guidance only — not legal advice."
metadata:
  author: "Gillan Saleh"
  license: "agpl-3.0"
  version: "2026-05-21"
---

# Sanctions Screening & Legal Analysis Skill

> **Last updated: 19 May 2026** — EU 20th package · UK SEUC · Cuba EO 14404 · GL 131E Lukoil

## Scope

This skill covers exclusively the field of **international economic sanctions and export controls**,
in all their dimensions:
- Individual designations (asset freeze, travel ban)
- Sectoral sanctions (energy, finance, technology, transport...)
- Dual-use goods and technologies
- Payment systems (SWIFT, USD, EUR) as sanctions vectors
- Extraterritorial regimes (EAR/ITAR/FDPR US, China ECL, EU no re-export clause)
- Financial institutions' obligations under sanctions

---

---

## ABSOLUTE RULE — Prohibition of hallucinations and invented data

**These rules apply without exception to every response produced by this skill. They take precedence over all other instructions.**

### 1. Absolute prohibition on answering from memory regarding designation lists

Sanctions lists (OFAC SDN, EU FSF, UN list, French DGT, UK FCDO, etc.) are updated daily. A response based on the model's memory is by definition potentially incorrect and legally dangerous.

**Rule**: any statement about the presence or absence of a person or entity on a sanctions list **must be preceded by a real-time web search** on the corresponding official source. If the search is impossible (source unavailable, failed connection), state this explicitly — never fill the gap with an assertion.

### 2. Mandatory source citation

Every piece of information produced under this skill must be accompanied by its source:
- **Name of the list or text** (e.g.: "OFAC SDN List", "EU FSF — Reg. 269/2014", "UN Committee 1988")
- **URL or precise reference** (e.g.: sanctionssearch.ofac.treas.gov, webgate.ec.europa.eu/fsd/fsf)
- **Date of the search** (e.g.: "verified on [date]")

If no source could be consulted for a statement, do not produce it.

### 3. Mandatory alerts — inconclusive results

In the following situations, an explicit alert is mandatory **before any conclusion**:

| Situation | Alerte à produire |
|-----------|------------------|
| Common / ambiguous name (e.g.: Mohamed Ali) | ⚠️ "Very common name — inconclusive result without additional identifiers (DOB, nationality, passport)" |
| Official source inaccessible during search | ⚠️ "Source [name] inaccessible at time of search — result must be verified directly at [URL]" |
| Partial match / low score on OpenSanctions | ⚠️ "Partial match detected — verification on official source [list] mandatory before any conclusion" |
| Variable transliteration (Arabic, Cyrillic, Chinese) | ⚠️ "Variable spelling possible — also search: [variants]" |
| "No match" result without confirmed search | ⚠️ "Absence of match not confirmed by real-time search — do not conclude absence of designation" |

### 4. Prohibition on extrapolating the state of the law without a verified source

Sanctions law evolves very rapidly (new EU packages, OFAC updates, individual designations). 

**Rule**: if a rule, an entry into force date, or a designation cannot be confirmed by a source consulted in the session, flag it as **"to be verified — not confirmed in this session"** rather than asserting it as certain.

Never produce a designation date, regulation number, or legal reference without having verified it in the session or in the skill's reference files.

### 5. Mandatory citation format in results

Each result block must explicitly mention:

```
Sources consulted: [list of sources with URLs]
Date of verification: [date]
Limits of this analysis: [missing identifiers / inaccessible sources / partial results]
⚠️ This result is indicative. Verify against official sources before any decision.
```

### 6. Prohibition on compensating uncertainty with a reassuring statement

It is prohibited to produce a reassuring conclusion ("no risk identified", "transaction freely feasible") when the search is incomplete, the name is ambiguous, or a source is inaccessible. In such cases, the conclusion must reflect the actual level of certainty:

- ✅ Result confirmed by official source consulted in the session
- 🟡 Partial result — to be completed by direct verification
- ⚠️ Inconclusive — insufficient identifiers or inaccessible source
- ❌ Cannot conclude — do not produce a conclusion

---

## Step 0 — Language and user profile

### Supported languages — mandatory multilingual rule

Detect the user's language at the very first message and respond **exclusively in that language** throughout the entire conversation — including all result blocks, alerts and recommendations.

**Supported languages:**

| Language | Respond in | Key terminology |
|--------|-------------|-----------------|
| **Français** | French | Reference language of the skill |
| **English** | English | Default fallback for any unsupported language |
| **Deutsch** | Deutsch | Vermögenssperrung · Ausfuhrkontrolle · Güter mit doppeltem Verwendungszweck · Sanktionsliste |
| **Español** | Español | Congelación de activos · Control de exportaciones · Bienes de doble uso · Lista de sanciones |
| **Русский** | Русский | Заморозка активов · Экспортный контроль · Товары двойного назначения · Санкционный список |
| **中文** | 中文（简体） | 资产冻结 · 出口管制 · 两用物项 · 制裁名单 |

**Rules:**
- Never mix languages within a single response
- If the user switches language mid-conversation, switch immediately and maintain the new language
- For any other language: respond in English and note that the tool is optimised for the 6 languages listed above
- Regulatory references (DGT, SBDU, ACPR, CMF) are French/EU obligations — when responding in Russian or Chinese, clarify that these are the applicable French/EU legal frameworks, not the user's domestic law

### User profile
- **Non-expert**: plain language, traffic-light indicators 🔴/🟡/✅, define all acronyms, explicit "what to do next"
- **Legal/compliance professional**: precise regulatory references, concise, full extraterritorial analysis

---

## Step 1 — Request analysis

Identify which modules to activate:

| Signal | Module |
|--------|--------|
| Individual's name | **A** — Individual screening |
| Sector / transaction / country | **B** — Sectoral sanctions + payments |
| Good / technology / software / component | **C** — Dual-use goods |
| "US goods", "US component", "FDPR", "EAR", "ITAR" | **C2** — Extraterritorial regimes US/China |
| Third country involved in transaction | **D** — Jurisdictional risk |

**Combined triggers — examples:**
- "Gillan Saleh + pétrole + Russie" → A + B + D
- "Machine américaine + extraction pétrolière + Irak + paiement USD" → B + C + C2 + D
- "Logiciel de cryptographie + Iran" → B + C + C2 + D
- "Est-ce que X est sanctionné ?" → A seul

Collect before launching:
- **A**: full name + nationality/residence (required); DOB, aliases (useful)
- **B**: sector, nature of transaction, countries
- **C/C2**: description of good/technology, destination, declared use, origin (US? Chinese?)
- **D**: jurisdictions involved, payment currency

---

## MODULE A — Individual screening

### A1 — Universal baseline (always run)
1. **ONU** → `"[nom]" UN Security Council consolidated sanctions list`
2. **UE** → `"[nom]" EU financial sanctions consolidated list`
3. **OpenSanctions** → `"[nom]" site:opensanctions.org` — filet 100+ listes
   - Hit not found in baseline → identify source → targeted official source search
   - Never cite OpenSanctions as authoritative source

### A2 — Geographic tier (based on nationality)

**EU national**: baseline sufficient + French DGT if French entity involved

**Aligned autonomous European countries (NO/IS/LI/CH)**: baseline + SECO (Switzerland). Treat as near-EU.

**EU candidate countries (RS/ME/AL/MK/MD/UA/BA/GE)**: baseline. Declared alignment, less robust legal basis.

**Turkey**: UN only on autonomous sanctions. Different regime from EU/US Russia sanctions.

**UK national / UK link**: UK Sanctions List (FCDO) → `"[name]" site:gov.uk UK sanctions list`
Note: since 28 Jan 2026, single FCDO list — OFSI Consolidated List merged.

**US national / US link**: OFAC SDN + Non-SDN + SSI + GLOMAG → `"[name]" site:ofac.treas.gov`

**Russian / Belarusian**: EU (Reg. 269/2014) + OFAC + UK Sanctions List + SECO as priority.

**Iranian**: UN (snapback 28 Sept 2025, Res. 2231) + OFAC Iran programme + EU (Reg. 267/2012). Watch USD secondary sanctions risk.

**DPRK (North Korea)**: UN (near-total embargo) + OFAC + EU. Watch DPRK workers abroad.

**Syrian**: UN + EU (Reg. 36/2012) + OFAC. Post-Dec 2024: situation evolving — verify current status.

**Gulf / Middle East**: baseline + national list if available (Qatar NCTC / UAE ECON / Saudi Arabia PSS). See `references/regimes.md`.

**African**: baseline generally sufficient. South Africa: + FIC. See `references/regimes.md`.

**CA/AU/JP/SG**: baseline + own list (Global Affairs Canada / DFAT / METI-MOFA / MAS). Lists ≠ EU list.

### A3 — Screening result
```
═══════════════════════════════════════════
SANCTIONS SCREENING — [NAME]     [DATE]
═══════════════════════════════════════════
🔴 MATCH / 🟡 AMBIGUOUS / ✅ NO MATCH / ⚠️ INCONCLUSIVE
Lists checked: [exhaustive]
Match on: [list + reference + grounds if applicable]
⚠️ Indicative. Verify against official sources. Not legal advice.
═══════════════════════════════════════════
```
**If ⚠️ AMBIGUOUS NAME**: request DOB, nationality, passport number, aliases. Minimum 2 concordant identifiers.

---

## MODULE B — Sectoral sanctions and payment systems

### B1 — Sectoral sanctions by regime

**Russie (UE Reg. 833/2014 + 20 paquets successifs — 20ème paquet : Reg. UE 2026/506, 2026/511, 2026/509 du 23 avr. 2026) :**
- Energy: ban on purchase/import of Russian crude oil and refined petroleum products; restrictions on gas, coal
- Finance: ban on access to EU capital markets for designated banks; restrictions on deposits, loans
- Transport: ban on EU airspace overflight, access to ports and airports
- Technology: ban on export of semiconductors, advanced electronics, dual-use goods (Russia removed from EU general authorisations EU001-EU008 since Reg. 2022/699)
- Luxury: ban on export of luxury goods >€300/item
- Services: ban on legal advisory, accounting, PR, cloud, IT consulting to Russian entities
- Gold, steel, wood, chemicals, paper: import restrictions
- Oil price cap G7 : plafonnement 60$/baril pétrole transporté par opérateurs G7
- **Russian LNG embargo (19th package)**: effective 25 April 2026 (short-term contracts concluded before 17 June 2025) / 1 January 2027 (long-term contracts >1 year)
- **Extension of transaction ban to Mir and SBP** (Russian fast payment system) since 25 January 2026 (19th package)
- **Russian crypto-assets ban**: stablecoin A7A5 prohibited since 25 November 2025; extension of transaction ban to crypto-asset and payment service providers (Annex XLV)
- **Commercial space-based services** (Earth observation, satellite navigation): prohibited to Russia and Belarus since the 19th package
- **Désignation OFAC Rosneft et Lukoil** (22 oct. 2025) : les deux plus grandes compagnies pétrolières russes désormais sur la SDN List sous EO 14024 — toutes transactions US-nexus interdites ; secondaires sanctions risk pour entités non-américaines ; wind-down GL 131E prolongée jusqu'au 30 mai 2026 (OFAC, 29 avr. 2026) — pour cession Lukoil International GmbH uniquement ; aucun transfert vers la Russie autorisé
- **20th EU package (23 Apr. 2026) — key new measures:**
  - **Transaction ban extended to 20 additional Russian banks** (effective 14 May 2026) — total now 70 banks; + 4 banks in Kyrgyzstan, Laos and Azerbaijan for circumvention facilitation
  - **Full sectoral ban on Russian crypto-asset service providers and decentralised platforms** (effective 24 May 2026) — categorical ban, no individual listing required; digital rouble and RUBx stablecoin prohibited
  - **Managed security services** (cybersecurity risk management, penetration testing, security audits) prohibited to Russian government and Russia-established entities (effective 25 May 2026)
  - **Kyrgyzstan**: first-ever activation of EU anti-circumvention tool (Art. 12f) — specific trade restrictions extended due to systematic re-export risk to Russia (imports of controlled EU goods +800%, re-exports to Russia +1,200%)
  - **LNG terminal services** ban for Russian entities; prohibition on maintenance services for Russian LNG tankers and icebreakers
  - **Shadow fleet**: 46 additional vessels listed (total: 632); Murmansk and Tuapse ports sanctioned; Karimun Oil Terminal (Indonesia) — first third-country port sanctioned
  - **Payment agents** (non-financial intermediaries offering netting/set-off/settlement services to route Russian transactions around sanctions) newly restricted — entities listed in Annex XLV Part D (Arneis, Asia Import Group, GPAgent, Platejka), effective 14 May 2026
  - **Future maritime services ban** on Russian oil/petroleum: legal framework established, entry into force to be decided by the Council in coordination with G7
  - **Protections for EU operators**: new anti-suit injunction mechanism (Art. 11ca Reg. 833/2014) allowing EU companies to seek court orders against abusive Russian proceedings
  - **Export bans** (goods >€365M: chemicals, rubber, steel, tools, industrial tractors); **import bans** (metals, chemicals, minerals >€530M)
- "No re-export to Russia" clause (Art. 12g Reg. 833/2014, 12th package Dec 2023, effective March 2024): EU exporters must insert a clause prohibiting re-export to Russia in all contracts with third-country partners — **unless the third country is in Annex VIII**: US, JP, UK, CA, AU, NZ, NO, CH, LI, IS, South Korea

**Iran (UN + EU Reg. 267/2012 + OFAC):**
- Oil/gas: EU embargo; US near-total prohibitions
- Finance: restrictions on transactions with designated Iranian banks
- Nuclear/missiles/IRGC: broad UN + EU + OFAC prohibitions
- **Snapback ONU (28 sept. 2025)** : réimposition sanctions ONU suite activation mécanisme Res. 2231 par E3 le 28 août 2025

**DPRK (UN near-total embargo):**
- Coal, steel, iron, lead, seafood: UN import bans
- Oil: export cap to DPRK
- DPRK workers abroad: employment ban (UNSC Res. 2397)

**Syrie** : sanctions économiques larges **levées** (UE 28 mai 2025, US 1er juillet 2025, UK avril 2025). Restent uniquement : sanctions contre membres régime Assad, armes, chimique, affiliés ISIS/Al-Qaeda — vérifier listes individuelles. Voir `references/regimes.md` section 2.4.

**Myanmar / Belarus / Venezuela :** voir `references/regimes.md`

### B2 — Payment systems as sanctions vectors

**SWIFT — statut juridique et exclusions :**
SWIFT is incorporated under Belgian law → directly subject to EU law → obligation to disconnect entities designated by EU regulation.

Timeline of Russian exclusions:
- **12 mars 2022** (Reg. 2022/345) : 7 banques — VTB, Bank Otkritie, Novikombank, Promsvyazbank, Rossiya Bank, Sovcombank, VEB
- **May 2022**: + Sberbank, Credit Bank of Moscow, Russian Agricultural Bank
- **2022–2025** : extension progressive à d'autres banques russes et biélorusses
- **July 2025** (Reg. EU 2025/1494): **major development** — conversion to full transaction ban. Any EU operator is prohibited from any direct or indirect transaction with the 50+ designated Russian banks, 4 Belarusian banks, 5 third-country financial operators.
- **June 2024**: prohibition on use of SPFS (Russian alternative financial messaging system) by EU operators

**USD risk (OFAC / correspondent banking):**
Any USD payment transiting through the US banking system is subject to OFAC, regardless of the parties' nationality. US correspondent banks screen every transaction. If any element of the chain touches a designated person or entity → automatic blocking.

**Alternatives to SWIFT/USD payments toward Russia:**
- SPFS (Russian): prohibited for EU operators since June 2024
- CIPS (Chinese — Cross-Border Interbank Payment System): not prohibited under EU law but risk of exposure to US secondary sanctions for entities with US links

**EUR payments toward sanctioned areas:**
- EUR payments transiting through EU banks: subject to EU sanctions regime
- Ban on provision of euro banknotes to Russia (Reg. 2022/345) with limited exceptions (personal use by travellers, diplomatic missions)
- Immobilisation of Russian Central Bank reserves held in the EU (since March 2022) — extraordinary revenues used to support Ukraine since May 2024

### B3 — Financial institutions' obligations under sanctions

**France / EU — result obligation (not best-efforts):**
Asset freezing is a **result obligation** — unlike AML/CFT which is risk-based. The financial institution cannot invoke a proportionate approach to justify a failure. If a designated person holds funds: immediate freeze, without discretionary assessment (principle consistently upheld by the ACPR sanctions commission).

Key regulatory obligations (France):
- **Decree of 6 January 2021**: mandatory internal controls for asset freezing
- **Joint DGT/ACPR guidelines** on implementation of asset freeze measures (updated 2024)
- **EBA Guidelines 2024/14 and 2024/15** (14 Nov 2024): internal policies, procedures and controls for restrictive measures
- **EU Directive 2024/1226**: EU harmonisation of criminal offences for sanctions violations
- **AMLA** (EU Regulation 2024/1620): new EU AML/CFT Authority — first supervisory reviews of ~40 financial institutions from mid-2025
- **EU Directive 2024/1640**: to be transposed by 10 July 2027 at the latest
- ACPR Decision 2024-02 (19 June 2025): Banque Delubac sanctioned for asset freeze failures
- ACPR sanctions 2024: ~€5 million in fines — main findings: internal control failures, insufficient transaction monitoring, gaps in detection of designated persons

**UK (OFSI):**
- **Strict liability** regime since SAMLA 2018 — civil penalties even without knowledge of the violation
- £160,000 fine on Bank of Scotland (Lloyds subsidiary) in January 2026 for Russia sanctions breach
- Since 28 Jan 2026: single FCDO list — any contractual reference to the OFSI Consolidated List must be updated

**US (OFAC):**
- No general legal obligation to establish a compliance programme — but the **OFAC Compliance Framework (2019)** creates strong normative pressure
- Robust compliance programme = significant mitigating factor; absence = aggravating factor
- In practice: all US banks and their correspondents have structured compliance programmes

**Japan (FEFTA):**
- Since **April 2024**: legal obligation for financial institutions to establish internal systems for compliance with asset freeze measures
- Since **December 2024**: mandatory prior reporting for transfers of key technologies (15 items: MLCC, carbon fibres, semiconductors...)
- Since **October 2025**: revised catch-all export controls — high-risk dual-use items classified as "core items"

**China:**
- No obligation to comply with foreign sanctions
- Anti-sanctions Law 2021 + Blocking Statute 2021 may create **inverse obligations** for entities in China — duty not to comply with foreign sanctions targeting Chinese entities

### B4 — Sectoral / payments result
```
═══════════════════════════════════════════
SECTORAL ANALYSIS — [SECTOR/PAYMENT] / [COUNTRY]
═══════════════════════════════════════════
🔴 RESTRICTIONS / ✅ PAS DE RESTRICTION IDENTIFIÉE
Applicable regime: [regulation/resolution]
Nature: [total ban / licence required / cap / SWIFT restriction]
Who is bound: [EU entities / US persons / financial institutions]
Derogations: [yes/no — which ones]
USD risk: [yes/no — OFAC correspondent banking]
SWIFT risk: [designated bank? transaction ban since July 2025?]
═══════════════════════════════════════════
```

---

## MODULE C — Dual-use goods — EU regime

### C1 — EU legal basis
- **Regulation (EU) 2021/821** of 20 May 2021 (recast) — in force since 9 Sept 2021, replaces Reg. 428/2009
- **Reg. délégué (UE) 2022/699** : Russie retirée des autorisations générales EU001-EU008
- **France**: SBDU (Service des Biens à Double Usage) — DGE, Ministry of the Economy — EGIDE platform
- Annual update of Annex I via Commission delegated regulations

### C2 — The 10 dual-use categories (Annex I Reg. 2021/821)

Nomenclature structure: `[Category][Type][Regime][Number]` e.g. `3A225`
- **Type**: A=equipment/components · B=test/production equipment · C=materials · D=software · E=technology

| Cat. | Intitulé | Exemples de codes |
|------|----------|------------------|
| **0** | Nuclear | `0A001` (reactors), `0B001` (enrichment equipment), `0C001` (fissile materials) |
| **1** | Special materials | `1C010` (composite fibres), `1C011` (metals/alloys) |
| **2** | Materials processing | `2B001` (CNC machine tools), `2B004` (high-temperature furnaces) |
| **3** | Electronics | `3A001` (electronic components), `3A225` (frequency converters), `3E001` (semicond. tech.) |
| **4** | Computers | `4A001` (high-performance computing), `4D001` (software) |
| **5** | Telecom & info security | `5A002` (encryption), `5D002` (cryptographic software), `5E002` (encryption tech.) |
| **6** | Sensors and lasers | `6A002` (optical detectors), `6A008` (radars), `6C005` (lasers) |
| **7** | Navigation and avionics | `7A003` (gyroscopes), `7A005` (GPS), `7E004` (aerospace tech.) |
| **8** | Marine | `8A001` (submersibles), `8A002` (naval equipment) |
| **9** | Aerospace and propulsion | `9A004` (space launchers), `9A012` (UAVs), `9C110` (propellants) |

> **Important**: no automatic direct link between dual-use code and customs tariff code (CN/HS). An annual CN–dual-use correlation table is published by the EU (EUR-Lex).

### C3 — International control regimes (basis of the dual-use list)

| Régime | Objet | Membres |
|--------|-------|---------|
| **Wassenaar Arrangement** (1996) | Conventional arms + dual-use | 42 states |
| **Australia Group** | Chemical and biological precursors | 43 states |
| **NSG** (Nuclear Suppliers Group) | Nuclear materials and technology | 48 states |
| **MTCR** | Missile technology and delivery systems | 35 states |

### C4 — Types of authorisation (EU/France)

| Type | Référence | Conditions |
|------|-----------|------------|
| EU General Export Authorisations | EU001–EU008 | Approved destinations — **Russia EXCLUDED (Reg. 2022/699)** |
| Individual authorisation | SBDU/EGIDE | 1 exporter, 1 good, 1 recipient — max. 2 years |
| Global authorisation | SBDU/EGIDE | 1 exporter, multiple operations — max. 2 years |
| National general authorisation | SBDU | Complementary to EU authorisations |

### C5 — Dual-use result
```
═══════════════════════════════════════════
DUAL-USE ANALYSIS — [GOOD] / [DESTINATION]
═══════════════════════════════════════════
🔴 LICENCE REQUISE / 🟡 À VÉRIFIER / ✅ PAS DE CONTRÔLE BDU
Potential classification: [dual-use code]
Category: [0-9 + description]
Source regime: [Wassenaar / NSG / Australia Group / MTCR]
Authorisation required: [general / individual / global]
French authority: SBDU — EGIDE platform
Legal basis: Reg. (EU) 2021/821, Annex I
═══════════════════════════════════════════
```

---

## MODULE C2 — Extraterritorial export control regimes

### C2.1 — US EAR/BIS

**Legal basis**: Export Administration Regulations (EAR) — 15 CFR Parts 730-774 — Bureau of Industry and Security (BIS), US Department of Commerce.

**Commerce Control List (CCL)**: US equivalent of EU Annex I — coded in ECCN (Export Control Classification Numbers), format `3A991`, `5E002`, etc.

**De minimis rule**: if US EAR-controlled components represent more than **25%** of the final product's value (10% for strictly embargoed destinations: Iran, DPRK, Cuba, Syria), the entire product is subject to the EAR even if manufactured outside the US.

**Foreign Direct Product Rule (FDPR)** — 15 CFR § 734.9: foreign-made products are subject to the EAR if they are the "direct product" of specified US-origin technology or software, or produced by a plant itself made from US technology. **Massive extraterritorial reach.**

**Russia/Belarus FDP Rule (since Feb 2022)**: extension of the FDPR — any item produced anywhere in the world from US tooling or technology is subject to the EAR for export to Russia/Belarus.

**BIS lists distinct from OFAC SDN List:**
- **Entity List**: entities to which any export of EAR-controlled items requires a licence — often reviewed under denial policy. "Footnote 3" = Russia-MEU FDP rule applies automatically
- **Denied Persons List**: total export prohibition to these persons
- **Unverified List**: entities whose end-use cannot be verified → enhanced due diligence required
- **Military End-User (MEU) List**: Russian and Chinese military entities — enhanced restrictions

**BIS Affiliates Rule (BIS 50% Rule) — status as of 19 May 2026**: BIS adopted on 29 September 2025 a rule extending Entity List restrictions to subsidiaries owned 50%+. This rule was **suspended for one year** as of 10 November 2025 under US-China trade negotiations (Trump-Xi Busan agreement). The rule is scheduled for reactivation on 10 November 2026 unless extended. During suspension: not operative — but BIS recommends maintaining capacity to analyse ownership chains.

**End-use controls**: even if an item is not on the CCL or if the destination is not embargoed, a BIS licence may be required if the final use is military, WMD-related, or for certain designated end-users.

**BIS Affiliates Rule (BIS 50% Rule) — suspended:**
- Adopted 29 September 2025: extension of Entity List restrictions to subsidiaries owned 50%+ (analogous to OFAC 50% rule but for export controls)
- **Suspended for one year** since 10 November 2025 (Trump-Xi agreement — in exchange for China suspending rare earth export controls)
- **Reactivation scheduled 10 November 2026** unless extended — maintain capacity to analyse ownership chains in anticipation
- During suspension: the BIS 50% Rule is **not operative** — but Entity List obligations for named entities remain in full force

**AI semiconductors / China — revised policy (January 2026):**
- Biden AI Diffusion Rule (January 2025) **rescinded** by the Trump administration
- New BIS policy effective **15 January 2026**: AI chips below certain thresholds (TPP < 21,000; DRAM bandwidth < 6,500 GB/s — H200/MI325X level) can now be evaluated **case by case** for export to China, instead of the previous systematic denial
- Conditions: proof that the export does not reduce production capacity available to US customers; KYC procedures on the Chinese buyer; independent third-party testing on US territory

**EU "no re-export to Russia" clause (Art. 12g Reg. 833/2014)**: obligation for all EU exporters to insert in contracts with third-country partners a clause prohibiting re-export to Russia — **unless the third country is in Annex VIII** (US, JP, UK, CA, AU, NZ, NO, CH, LI, IS, South Korea). Effective since March 2024. Declaration to national competent authorities required for contracts with foreign public authorities or international organisations.

### C2.2 — ITAR

**Legal basis**: 22 CFR Parts 120-130 — Directorate of Defense Trade Controls (DDTC), US Department of State.

**Distinct from EAR**: more restrictive, covers items on the **US Munitions List (USML)** — 21 categories covering weapons, ammunition, military aircraft, military electronics, missiles, chemical/biological weapons, etc.

**If a product component falls under ITAR**: no EAR licence suffices — this is a separate regime requiring a DDTC licence. Extraterritorial reach: any transfer of ITAR articles or technical data to a foreign national (including on US territory) is subject to ITAR.

**"Once ITAR, always ITAR" rule**: a product incorporating an ITAR component remains ITAR-controlled even if the component represents a tiny fraction of the final product.

**For French/EU entities**: if the US machine contains military or potentially military-use components, ITAR may apply in addition to or instead of the EAR → specialist legal advice essential.

### C2.3 — China Export Control Law (ECL)

**Base légale** : Loi sur le contrôle des exportations (Export Control Law — ECL) — entrée en vigueur le 1er décembre 2020. Complétée par le Règlement sur le contrôle des exportations de biens à double usage (2024).

**Extraterritorial reach** (Article 44 ECL + Article 49 Regulations 2024): foreign entities transferring products outside China that contain specific Chinese dual-use components may be subject to the 2024 Regulations. **Chinese equivalent of the US FDPR** — still developing, selective application.

**Terres rares et semiconducteurs (2025)** : mesures extraterritoriales spécifiques introduites en 2025 sur les terres rares, batteries lithium et matériaux superhard — avec une règle des 50% propre à la Chine pour les entités sur sa Control List.

**Unreliable Entity List (UEL)**: Chinese list of foreign entities having taken discriminatory measures against Chinese entities — may result in market access restrictions.

**Parallel anti-sanctions regime**:
- Anti-Foreign Sanctions Law 2021 (反外国制裁法): prohibits entities in China from complying with foreign unilateral sanctions targeting Chinese nationals/entities; right to claim damages
- Blocking Statute 2021: against extraterritorial application of foreign laws
- Law on Foreign Relations 2023: codifies and strengthens these mechanisms

**Practical note**: China's Control List and UEL are not publicly accessible in the same way as the OFAC SDN List or EU list — greater opacity.

### C2.4 — Other national export control regimes

**UK**: Export Control Order 2008 + UK Strategic Export Controls Lists — post-Brexit alignment with Wassenaar/NSG/MTCR/Australia Group; own regime distinct from the EU since 31 Dec 2020. **Sanctions End-Use Controls (SEUC — effective 13 May 2026)**: complementary mechanism to existing export controls — applicable to goods not on strategic lists but presenting diversion risk to a sanctioned destination. Triggered by written notification from OTSI to the exporter. Check systematically for any UK export toward third countries with re-export risk (Turkey, UAE, Kyrgyzstan, China, India...).

**Canada**: Export and Import Permits Act (EIPA) + Export Control List — Wassenaar alignment + specific Russia/Belarus measures post-2022.

**Australia**: Defence Export Controls (DEC) + Defence and Strategic Goods List (DSGL) — Wassenaar/NSG/MTCR/Australia Group alignment.

**Japan (FEFTA)**: no own FDPR; no secondary sanctions. BIS US controls apply in practice for Japanese exporters of products containing EAR items. Catch-all revised October 2025 with "core items" classification. Prior reporting for key technologies since December 2024.

**Russia**: no extraterritorial export control regime comparable to EAR/ECL. However, counter-measures targeting "unfriendly states":
- Decrees 95 and 254 (March/May 2022): restrictions on dividend transfers — payments only in roubles on type "C" accounts
- Decree 618 (Sept 2022): government approval required for any transaction by a national of an "unfriendly state" on participations in Russian companies
- Decree 302 (April 2023): authorisation to seize Russian assets held by nationals of "unfriendly states" (Rosimushchestvo)

### C2.5 — Analysis questions for Module C2

When a US-origin good or machine is mentioned:
1. Is the good on the CCL (ECCN)? → check BIS
2. Does the final product contain US EAR-controlled components exceeding 25% (or 10% for embargoed destinations)? → de minimis rule
3. Was the product manufactured using US tools or technology? → potential FDPR
4. Do any components fall under the USML (ITAR)? → separate, stricter regime
5. Is the destination subject to an extended FDP Rule (Russia/Belarus)?
6. Does the transaction involve an entity on the BIS Entity List, Denied Persons List or MEU List?
7. Does the good contain Chinese dual-use components? → potential ECL 2024 Art. 49
8. Is payment in USD? → OFAC risk via correspondent banking

### C2.6 — Module C2 result
```
═══════════════════════════════════════════════════════════
EXTRATERRITORIAL REGIMES ANALYSIS — [GOOD] / [ORIGIN] / [DESTINATION]
═══════════════════════════════════════════════════════════
EAR/BIS (US) :
  🔴 BIS LICENCE REQUIRED / 🟡 TO VERIFY / ✅ NO EAR CONTROL
  Potential ECCN: [code if identifiable]
  De minimis rule: [applicable? threshold?]
  FDPR : [applicable ?]
  BIS lists: [Entity List / Denied Persons / MEU / Unverified]

ITAR (US) :
  🔴 APPLICABLE — USML CATEGORY [X] / ✅ NOT ON USML
  If applicable: DDTC licence mandatory — EAR licence insufficient

ECL CHINE :
  🟡 TO ASSESS if Chinese components / ✅ NO CHINESE COMPONENT IDENTIFIED

RISQUE USD :
  🔴 USD PAYMENT → OFAC SCREENING MANDATORY / ✅ NO USD PAYMENT

CLAUSE NO RE-EXPORT (UE Art. 12g) :
  🔴 APPLICABLE — third country not in Annex VIII / ✅ THIRD COUNTRY IN ANNEX VIII
═══════════════════════════════════════════════════════════
```

---

## MODULE D — Jurisdictional risk management

> **Principle**: States exercise full sovereignty over their sanctions policy. A regime different from the EU/France regime implies no judgment on the legitimacy of that State's policy. The analysis covers only the obligations of the user under their own legal regime.

### D1 — Geographic mapping (summary — read `references/regimes.md` for detail)

**EU 27**: CFSP regulations directly applicable — automatic obligation.

**Aligned autonomous (NO/IS/LI)**: near-EU. Switzerland (SECO): strong EU convergence, separate verification.

**EU candidates**: declared alignment, less robust legal basis — residual risk per transaction.

**Turkey**: UN only; different regime on Russia.

**UK**: strong G7 alignment; distinct FCDO list; OFSI strict liability since Jan 2026. **New — SEUC (Sanctions End-Use Controls, effective 13 May 2026)**: new licensing requirement for exports toward non-sanctioned third countries where OTSI has notified diversion risk — Sanctions (EU Exit) (Miscellaneous Amendments) Regulations 2026 (S.I. 2026/443).

**US**: largest + most extraterritorial regime (secondary sanctions, USD). EU Blocking Statute Reg. 2018/1100 applicable in principle for Cuba/Iran. **New — EO 14404 Cuba (1 May 2026)**: new Executive Order extending US sanctions on Cuba (energy, defence, metals, mining, financial services sectors) with threat of secondary sanctions on foreign financial institutions dealing with blocked Cuban entities — increased risk for non-US entities.

**CA/AU/JP**: strong G7 alignment; distinct lists — separate systematic verification.

**Singapore**: UN + terrorism; indirect OFAC exposure via USD.

**UAE**: UN + terrorism (ECON); different regime on Russia; exposed to OFAC designations Iran/Russia.

**Qatar**: NCTC terrorism list (best structured in the region). No broad autonomous sanctions.

**Saudi Arabia**: formal UN framework (automatic freeze upon UNSC 1267 designation); PSS list poorly structured; different regime on Western unilateral sanctions.

**South Africa**: only sub-Saharan autonomous public list (FIC).

**Rest of Africa**: no public autonomous lists; variable UN obligation; individual designations via UN/EU/OFAC only. AU/ECOWAS: regional regimes under construction.

**China**: selective UN (abstentions on Russia 2022); anti-sanctions law 2021; inverted regime for entities in China.

**India**: UN; different regime on Russia; India-Russia bilateral trade rising since 2022.

**Russia**: own counter-sanctions targeting "unfriendly states" — inverted context for French/EU entities operating in Russia.

### D2 — Residual risk questions

Even if Module A = ✅ and Module B = ✅:
1. USD payment? → OFAC risk via correspondent banking even without direct US link
2. Entity owned 50%+ by a designated person? → OFAC 50% rule + EU indirect control rule
3. Intermediaries in jurisdictions with different regimes? → analyze the full transaction chain
4. Sector itself under sanctions even if counterparty not individually designated?
5. Does the financial institution involved fall under the July 2025 transaction ban (70 Russian banks as of May 2026)?
6. Bien contient-il des composants US ou chinois déclenchant EAR/ECL ?

---

## Step 4 — Cross-jurisdictional legal qualification and synthesis

Read `references/qualification-juridique.md` for the full grid.

```
═══════════════════════════════════════════════════════════
SYNTHESIS — COMPLETE TRANSACTION ANALYSIS
═══════════════════════════════════════════════════════════
PERSON            : [Module A result]
TRANSACTION       : [Module B result — sectoral + SWIFT/USD]
GOOD/TECH EU      : [Module C result]
EXTRAT. REGIMES   : [Module C2 result — EAR/ITAR/FDPR/ECL]
JURISDICTION      : [Module D result]

CONCLUSION :
⛔ TRANSACTION NOT FEASIBLE AS STRUCTURED
⚠️ FEASIBLE UNDER CONDITIONS: [specify — BIS/SBDU licence / DGT authorisation...]
✅ NO RESTRICTION IDENTIFIED

IMMEDIATE OBLIGATIONS: [if applicable]
AUTHORITIES TO CONTACT: [DGT / SBDU / TRACFIN / ACPR / BIS / DDTC]
═══════════════════════════════════════════════════════════
```

---

## Step 5 — Practical guidance

**Non-expert**: traffic-light indicator on each dimension + "what this means for you" in plain language + explicit "what to do next" (contact SBDU, specialist lawyer, DGT...). Never leave without a clear next step.

**Expert (legal/compliance)**:
- Precise regulatory references (regulation numbers, articles, CFR)
- US extraterritoriality analysis (secondary sanctions, FDPR, EU Blocking Statute Reg. 2018/1100)
- China ECL analysis if Chinese components involved
- Residual jurisdictional risk (USD correspondent banking, transaction chain)
- Reporting obligations with legal basis (CMF L. 562-1 et seq., penalties L. 562-5)
- ACPR/AMF if financial sector; SBDU if dual-use; DDTC if ITAR

---

## MCP Tools — Automatic integration

When MCP tools are available in the session, use them **systematically and as priority** over general web search. MCPs provide access to official consolidated texts — more reliable and precise than web search.

### OpenLegi (Légifrance) — use if available

Use OpenLegi automatically for any French law verification within this skill:

**Mandatory use cases:**
- Verify the current consolidated version of CMF articles on asset freezing: **L. 562-1 to L. 562-10, R. 562-1 et seq.**
- Search for autonomous national sanctions decrees published in the JORF (Prime Minister decrees under CMF art. L. 562-2)
- Verify decrees applicable to financial institutions for asset freezing (e.g. Decree of 6 January 2021)
- Consult ACPR sanctions commission case law on asset freezing
- Verify any French legislative or regulatory reference cited in the analysis

**Typical OpenLegi queries:**
- `CMF L. 562-1` → consolidated text of the article
- `gel des avoirs décret [year]` → national sanctions decrees JORF
- `arrêté 6 janvier 2021 gel avoirs` → text applicable to financial institutions

**If OpenLegi is not available**: use `web_fetch` on legifrance.gouv.fr targeting the relevant article URL.

### EUR-Lex — via web_fetch (no dedicated MCP)

Il n'existe pas de MCP EUR-Lex natif — utiliser `web_fetch` directement sur EUR-Lex :

**Mandatory use cases:**
- Verify the consolidated version of any cited EU regulation (e.g. Reg. 833/2014 and its 20+ amendments)
- Consult Annex I of Reg. (EU) 2021/821 (dual-use list) in its current version
- Verify Annex VIII of Reg. 833/2014 (no re-export clause exempt countries)
- Verify Annex VII of Reg. 833/2014 (goods subject to the no re-export clause)
- Confirm the entry into force date of a sanctions package

**Direct EUR-Lex URLs — web_fetch:**
- Reg. 833/2014 consolidé : `https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02014R0833-20250224`
- Reg. 269/2014 consolidé : `https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02014R0269-20250224`
- Reg. 2021/821 consolidé (BDU) : `https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02021R0821-20241108`
- Liste consolidée sanctions financières UE (FSF) : `https://webgate.ec.europa.eu/fsd/fsf`

**Rule**: always use the most recent consolidated version — never cite a base regulation without checking its successive amendments via EUR-Lex.

### Tool prioritisation

| Task | Priority tool | Fallback |
|-------|------------------|---------|
| French CMF texts / JORF / decrees | **OpenLegi MCP** | web_fetch legifrance.gouv.fr |
| Consolidated EU regulations | web_fetch EUR-Lex (CELEX) | web_search + verification |
| Individual designation lists | web_search on official sources | OpenSanctions |
| ACPR case law | **OpenLegi MCP** | web_search site:acpr.banque-france.fr |
| BIS Entity List / OFAC SDN | web_search site:bis.doc.gov / site:ofac.treas.gov | opensanctions.org |

---

## Disclaimer

**EN**: *Indicative legal guidance only. Last updated: 19 May 2026 (EU 20th sanctions package, UK SEUC, Cuba EO 14404). Results must be verified against official sources before any decision. Does not constitute legal advice. When in doubt: specialist in sanctions and export controls / DGT (asset freeze, France) / SBDU (dual-use goods, France) / BIS (EAR) / DDTC (ITAR).*

**EN** : *Indicative legal guidance only. Verify against official sources before any decision. Not legal advice. When in doubt: sanctions and export control specialist / DGT (asset freeze) / SBDU (dual-use) / BIS (EAR) / DDTC (ITAR).*

---

## Reference files

- `references/sources-officielles.md` — Official URLs + search strategies by jurisdiction
- `references/regimes.md` — Complete regime cartography by zone + jurisdictional risk matrix
- `references/qualification-juridique.md` — Cross-qualification grid + reporting obligations + criminal penalties