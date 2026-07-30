# India — TIA Country Profile

Last verified: 2026-05-29

## Adequacy Status

**Adequacy:** None. Art. 46 + TIA required for transfers to India.

**Reform trajectory:** India enacted the Digital Personal Data Protection Act 2023 (DPDP Act). Rules and enforcement implementation are still phasing in. EU Commission has not opened formal adequacy talks as of 2026-05.

## Data Protection Framework

**General law:** Digital Personal Data Protection Act 2023 (DPDP Act). Effective from a date appointed by the central government; substantive provisions phasing in.

**Supervisory authority:** Data Protection Board of India (DPB). Established under the DPDP Act. Independence from executive contested in early commentary.

**Data subject rights:** Right to information, correction, erasure, grievance redressal, nomination. Narrower than EU GDPR (no right to data portability or object as currently drafted).

**Effective remedies:** DPB grievance mechanism + appeal to Telecom Disputes Settlement and Appellate Tribunal (TDSAT). Penalties up to INR 250 crore (~€28M) per breach.

## Surveillance & Government Access Laws

### Information Technology Act 2000, Section 69

**Scope:** Permits Central or State Government to intercept, monitor, or decrypt information transmitted, stored, or generated in any computer resource.

**Powers:** On the order of competent authority; grounds include sovereignty, integrity, defence, state security, foreign relations, public order, preventing incitement.

**Guarantee A — Clear, precise, accessible rules:** **Concerns.** Statutory grounds are broad ("public order", "incitement"); not all procedural rules are public.

**Guarantee B — Necessary and proportionate:** **Concerns.** Pegasus controversy (2021) highlighted use beyond statutory grounds; Supreme Court of India empanelled a committee in response.

**Guarantee C — Independent oversight:** **Concerns.** Review committee under MHA (executive-internal); judicial oversight is available only after the fact via a writ petition under Art. 32 / Art. 226 of the Constitution for breach of the Puttaswamy (2017) privacy right — not habeas corpus, which lies only for unlawful detention.

**Guarantee D — Effective remedies:** **Concerns.** Puttaswamy established fundamental right to privacy. Remedies via writ jurisdiction in High Courts / Supreme Court. Practical effectiveness varies.

### Indian Telegraph Act 1885, Section 5(2)

**Scope:** Older interception statute. Used for telephone and electronic communication intercepts.

**Powers:** On the order of the Central / State Government on stated grounds.

**Guarantees A–D:** Similar profile to IT Act s.69.

### National Investigation Agency Act 2008 + others

**Scope:** Special agency powers for terrorism, organised crime. Broad investigative powers.

### DPDP Act, Section 17(2)(a)

**Scope:** Carve-out for processing by state instrumentalities in the interests of sovereignty, integrity, defence, security, foreign relations, public order, friendly relations with foreign states. DPB jurisdiction effectively excluded.

## Practical Risk Factors

- India is a major BPO/outsourcing destination — practitioner familiarity is high
- DPDP Act enforcement is nascent; the Pegasus episode shows extralegal access can occur
- Government access requests are common in some sectors (telecoms, social media, payments)
- India has cybersecurity-related data localisation rules (RBI for payments, telecom sector)

## Recommended Supplementary Measures

Default suggestions for India:

- **TM-1** (encryption with exporter-held keys) — high priority, especially for non-payment data
- **TM-2** (pseudonymisation) — where service can function without identifiers
- **CM-1** (transparency obligation) — importer commits to notify exporter of access requests
- **CM-2** (challenge clause) — importer commits to challenge overbroad requests
- **CM-3** (enhanced audit rights)
- **OM-2** (access controls) and **OM-3** (request handling policy)

**Sectoral caveats:**
- Payment data: cannot localise outside India under RBI rules — different architecture needed
- Telecom data: subject to localisation under telecom licence conditions
- Other sectors: localisation NOT required, supplementary measures can compensate

**When these measures do NOT work for India:**
IT Act s.69(3) compels any person in charge of a computer resource to assist with interception, monitoring, and **decryption**, and s.69(4) punishes failure to assist with up to **7 years' imprisonment** plus fine. Consequently:
- **TM-1 (encryption)** helps only where the keys are held *outside India* by the exporter and the Indian importer has no technical ability to reach plaintext — otherwise decryption assistance can be compelled under penalty.
- **CM-1 (transparency)** and **CM-2 (challenge)** can be neutered by confidentiality/non-disclosure conditions attached to an s.69 direction.
Where the importer must process plaintext and the data is of state interest, the honest outcome is restructure-or-suspend, not measures.

## TIA Output

For India transfers:
- Section 3 Block A: DPDP Act provides a framework, but enforcement is phasing in AND s.17(2)(a) exempts State instrumentalities from DPB oversight for sovereignty/security/public-order processing — so the domestic framework gives little constraint on the Block B government-access risk
- Section 3 Block B: IT Act s.69 and Telegraph Act s.5(2) raise concerns on all four guarantees
- Section 3 Block C: practical risk depends on sector and importer profile
- Section 3 conclusion: typically option (2) — proceed with supplementary measures
- For small-scale, non-sensitive transfers: option (3) may be defensible with documentation

## Key Sources

- Digital Personal Data Protection Act 2023
- Information Technology Act 2000, Section 69 + the IT (Procedure and Safeguards for Interception, Monitoring and Decryption of Information) Rules 2009
- Indian Telegraph Act 1885, Section 5(2)
- Puttaswamy v. Union of India (2017) — Right to Privacy as fundamental right
- DPB notifications (when published)
- Major Indian provider transparency reports (where available)
- Rosenthal "Lawful Access" FAQ — Indian Law sample case
