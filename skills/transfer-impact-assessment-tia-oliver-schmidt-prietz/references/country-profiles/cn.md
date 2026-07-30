# China — TIA Country Profile

Last verified: 2026-05-29

## Adequacy Status

**Adequacy:** None. Art. 46 + TIA required. EU adequacy is not on the foreseeable agenda.

## Data Protection Framework

**General law:** Personal Information Protection Law (PIPL, effective 1 November 2021). Substantively similar to GDPR in structure (legal bases, data subject rights, processor obligations).

**Other relevant laws:**
- Cybersecurity Law 2017
- Data Security Law 2021
- Cryptography Law 2019
- E-commerce Law 2019

**Supervisory authority:** Cyberspace Administration of China (CAC) — primary regulator. NOT independent from the executive.

**Data subject rights:** PIPL grants access, correction, deletion, portability, automated decision objection. Practical exercise constrained where national security implicated.

**Effective remedies:** Administrative complaints to CAC; civil claims in People's Courts. Practical effectiveness against state actors is limited.

## Surveillance & Government Access Laws

### National Intelligence Law 2017

**Scope:** Article 7: "Any organization and citizen shall, in accordance with law, support, assist, and cooperate with national intelligence efforts, and guard the secrecy of any national intelligence work they are aware of." Article 14: Intelligence agencies may request assistance from any organisation. Article 16: Intelligence officers may enter restricted areas and access documents/materials.

**Powers:** Broad — extends to any organisation operating in China, including foreign subsidiaries.

**Guarantee A — Clear, precise, accessible rules:** **Insufficient.** "Intelligence work" undefined; assistance obligations unbounded.

**Guarantee B — Necessary and proportionate:** **Insufficient.** No statutory necessity/proportionality test; no scope limitations on intelligence collection.

**Guarantee C — Independent oversight:** **Insufficient.** No independent oversight body. State Security ministries are executive-internal.

**Guarantee D — Effective remedies:** **Insufficient.** No mechanism for data subjects to challenge intelligence access. The NIL Art. 7 secrecy duty (above) requires anyone aware of national intelligence work to keep it secret, barring an importer from disclosing that it was compelled to cooperate.

### National Security Law 2015

**Scope:** Broad "national security" framework. Permits state to demand cooperation, access, and confidentiality.

**Profile:** Same insufficiency across all four guarantees as the NIL.

### Cybersecurity Law 2017

**Scope:** Network operators must provide technical support and assistance to public security and state security organs for safeguarding national security.

**Data localisation:** Critical Information Infrastructure Operators (CIIO) must store personal data and important data in China.

**Powers:** Extends to cooperation with security inspections, content removal, identity verification.

### Data Security Law 2021

**Scope:** Art. 35 permits public-security and state-security organs to demand data from organisations for national-security or criminal investigations. Art. 36 prohibits providing data stored in China to foreign judicial or law-enforcement authorities without Chinese government approval (parallel to PIPL Art. 41).

**Profile:** Reinforces the NIL/NSL access regime — same insufficiency across all four guarantees; the Art. 36 approval gate can also trap an importer between EU and Chinese legal demands.

### PIPL, Article 41

**Scope:** Foreign judicial or law enforcement requests for data stored in China require CAC approval before disclosure. Mirror-image of the CLOUD Act problem from China's perspective.

## Practical Risk Factors

- The legal regime imposes structural conflicts with EU essential equivalence
- Major Chinese providers (Alibaba, Tencent, Baidu, Huawei) operate under these laws
- Many EU-China transfers are inbound (China to EU); outbound EU-to-China raises the highest TIA difficulty
- Sectoral data localisation: financial data, automotive, health, "important data" categories

## Recommended Supplementary Measures

For most EU-to-China transfers, supplementary measures are unlikely to close the essential guarantee gaps. Realistic options:

- **TM-1** (encryption with exporter-held keys) — only effective if importer doesn't need plaintext, AND if keys are never compelled. NIL Article 7 raises compulsion risk.
- **TM-2** (pseudonymisation) — partial protection; mapping table must stay in EEA, but onward identification by importer's auxiliary data is a concern
- **Avoid central deployment** — split processing, minimum data sets, no plaintext access

**Honest verdict:** For most use cases involving sensitive personal data, supplementary measures cannot close the gap. The skill should flag: consider whether the transfer is necessary at all. Alternatives — on-premises EU deployment, EU sovereign cloud, suspension — may be the appropriate verdict.

## TIA Output

For China transfers:
- Section 3 Block A: PIPL provides framework but state actors exempted
- Section 3 Block B: all four guarantees insufficient for NIL and NSL
- Section 3 Block C: realistic risk is high for any data of interest to Chinese state
- Section 3 conclusion: typically (2) with insufficient measures → suspend OR restructure
- Some narrow cases (purely operational data, no personal data dimension worth Chinese state interest) may yield option (3), but documentation requirements are high

## Key Sources

- Personal Information Protection Law 2021 (PIPL)
- National Intelligence Law 2017
- National Security Law 2015
- Cybersecurity Law 2017
- Data Security Law 2021
- CAC implementing regulations (Standard Contract, Security Assessment, Certification)
- Rosenthal "Lawful Access" FAQ — Chinese Law sample case
- EDPB / EDPS work on third-country surveillance (where Chinese provisions discussed)
