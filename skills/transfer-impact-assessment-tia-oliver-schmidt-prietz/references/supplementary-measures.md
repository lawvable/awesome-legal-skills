# Supplementary Measures Catalog

Source: EDPB Recommendations 01/2020 Annex 2 — Examples of supplementary measures.

This catalog maps measures to the essential-guarantee gaps they address. Each measure includes honest "when effective" and "when NOT effective" guidance — the goal is not to paper over gaps, but to close them where possible and flag them honestly where not.

The OLG München judgment (21 U 3882/25 e, 2026) confirmed encryption + minimum-necessary data + transparency reporting as genuine supplementary measures accepted by a German court. This catalog reflects that practical acceptance.

---

## Technical Measures

### TM-1: Encryption in transit and at rest with exporter-held keys

**Addresses:** Bulk surveillance, data-at-rest access by authorities, importer-side breach.

**When effective:**
- Importer does NOT need access to plaintext (storage-only services, backup, archival)
- Key management is exclusively in the EEA, under the exporter's control
- Modern algorithms (AES-256, RSA-4096+) with no known weaknesses
- Keys cannot be compelled from the exporter under third-country law

**When NOT effective:**
- Importer must decrypt to process (cloud SaaS, analytics, content moderation, AI inference)
- Keys are escrowed with the importer or a third party in the recipient country
- The importer is a cloud provider hosting both data and keys (even with HSM separation, if the importer can be compelled)

### TM-2: Pseudonymisation

**Addresses:** Re-identification by authorities, partial data minimisation.

**When effective:**
- Mapping table / re-identification key stays in the EEA, under exporter control
- The pseudonymised data alone has limited utility for identifying individuals
- Robust pseudonymisation (hashing with secret salt, not just reversible tokenisation)

**When NOT effective:**
- Authorities can compel production of the mapping table (e.g., via the exporter under domestic process)
- The pseudonymisation is trivially reversible (e.g., simple ID swap)
- The importer can re-identify via auxiliary data already in their possession

### TM-3: Split / multi-party processing

**Addresses:** Single-point government access; no single party has the full picture.

**When effective:**
- Processing can be genuinely distributed across jurisdictions
- No single processor holds a complete dataset
- Outputs are aggregated only in the EEA (or via secure multi-party computation)

**When NOT effective:**
- Service architecture requires centralised processing
- One party effectively orchestrates and can be compelled to assemble the full picture

### TM-4: Transport-layer encryption (TLS / VPN)

**Addresses:** Interception in transit between exporter and importer.

**When effective:**
- Standard TLS 1.3 or higher with strong cipher suites
- Verified certificate chains
- For any transfer, this is baseline hygiene, not a Schrems II supplementary measure on its own

**When NOT effective:**
- Doesn't help against lawful disclosure requests targeting the importer (the data is decrypted at the endpoint)
- Doesn't help against importer-side breach

## Contractual Measures

### CM-1: Transparency obligation (notification of access requests)

**Addresses:** Lack of oversight; data subjects unaware of access.

**When effective:**
- Importer commits to notify the exporter of any government access request affecting the transferred data
- Importer commits to notify data subjects (where legally permitted)
- Combined with regular transparency reporting (aggregate statistics on requests received)

**When NOT effective:**
- Local law prohibits notification (US gag orders under FISA 702, NSL non-disclosure orders, etc.)
- Importer commits but lacks enforcement capacity
- Notification is to the exporter only, with no path to inform affected data subjects

### CM-2: Challenge / contest clause

**Addresses:** Weak remedies, automatic compliance with overbroad requests.

**When effective:**
- Importer commits to assess each request for legality, necessity, and proportionality
- Importer commits to challenge overbroad or unlawful requests through available legal channels
- Importer has standing and a realistic legal avenue to challenge

**When NOT effective:**
- No realistic legal challenge available under local law
- Importer faces severe penalties for non-compliance that outweigh contractual obligations
- Standing is restricted (e.g., importer cannot challenge on behalf of the data subject)

### CM-3: Enhanced audit rights

**Addresses:** Lack of oversight, importer compliance verification.

**When effective:**
- Exporter or independent auditor can meaningfully inspect importer's compliance
- Audit covers technical measures (encryption deployment, access controls) and procedural measures (request handling)
- Audit findings are actionable (corrective measures, termination)

**When NOT effective:**
- Audit is impractical at scale (e.g., audit of a hyperscale cloud provider's full operations)
- Audit access is limited by claims of national security / classified operations
- Audit findings have no enforcement mechanism

### CM-4: Data localisation commitment

**Addresses:** Jurisdictional overreach; data physically present in the third country.

**When effective:**
- Importer commits to keep data within the EEA (or another agreed jurisdiction) for storage and processing
- Architecture supports localisation (regional cloud regions, EU sovereign cloud variants)
- Sub-processor management ensures the localisation extends down the chain

**When NOT effective:**
- Service architecture requires the transfer (the whole point of the engagement)
- Localisation is commitment-only, not technically enforced
- Importer's parent company can compel cross-border access regardless of contractual commitments (the Example 12 problem from EDPB Guidelines 05/2021)

## Organisational Measures

### OM-1: Strict purpose limitation policies

**Addresses:** Function creep; data used beyond the transfer purpose.

**When effective:**
- Importer's internal policies bind processing to the transfer purpose
- Access controls enforce purpose limitation technically
- Regular policy compliance assessments

**When NOT effective:**
- Policy without technical enforcement
- No consequences for breach
- Authorities bypass internal policies via court order

### OM-2: Access control policies (minimum necessary access)

**Addresses:** Broad internal access by importer's personnel.

**When effective:**
- Role-based access controls limit data exposure to need-to-know personnel
- Privileged access reviews and revocation processes
- Logged and auditable access trails

**When NOT effective:**
- Authorities bypass internal controls via legal process
- Importer's administrators effectively have unrestricted access

### OM-3: Government request handling policy

**Addresses:** Ad hoc / inconsistent responses to government access requests.

**When effective:**
- Importer has a documented process: review for legality → minimum necessary → notify (if permitted) → challenge (if applicable)
- Trained personnel handle requests
- Public transparency reporting on requests received and handled

**When NOT effective:**
- Policy has no legal force against court orders / NSLs
- Local law mandates compliance without internal review
- No path to challenge

### OM-4: Certifications and codes of conduct

**Addresses:** Verified compliance posture; third-party assurance.

**When effective:**
- Recognised certifications (ISO 27001, ISO 27701, SOC 2 Type II, ENS, EU Cloud Code of Conduct)
- Certification covers the relevant processing scope
- Auditor independence and competence verified

**When NOT effective:**
- Certification is scope-limited to other processing
- Auditor is captive / lacks independence
- Certification body itself is subject to questionable government influence

---

## Auto-Suggest Logic

When Step 3 identifies gaps in specific essential guarantees, the skill matches measures to gaps using this mapping:

| Identified Gap (per Essential Guarantee) | Suggested Measures |
|---|---|
| Guarantee A (rules unclear) | OM-3 (request handling policy), CM-1 (transparency obligation) |
| Guarantee B (bulk surveillance / no proportionality) | TM-1 (encryption with exporter-held keys), TM-2 (pseudonymisation), CM-4 (data localisation) |
| Guarantee C (no independent oversight) | CM-1 (transparency), CM-3 (audit rights), OM-4 (certifications) |
| Guarantee D (no effective remedies) | CM-2 (challenge clause), CM-1 (transparency), OM-3 (request handling) |
| Importer must process plaintext | TM-2 (pseudonymisation), TM-3 (split processing), if neither viable → flag that the gap cannot be closed |

The skill presents matched suggestions, lets the user accept/reject/customise, then assesses overall effectiveness against the gaps. If effectiveness is insufficient, the skill honestly flags: this transfer cannot proceed as structured.
