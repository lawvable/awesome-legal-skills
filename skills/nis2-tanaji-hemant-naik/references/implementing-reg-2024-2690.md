# Commission Implementing Regulation (EU) 2024/2690: Technical & Methodological Requirements

The detailed, audit-level specification of the NIS2 Art. 21(2) cybersecurity risk-management measures. Where the Directive states ten high-level measures, this implementing regulation turns them into 13 numbered Annex sections with concrete sub-requirements, and defines the significant-incident thresholds.

Heading structure below is taken verbatim from the Annex as published in the Official Journal (EUR-Lex, OJ L, 2024/2690).

## What it is

- **Full title:** Commission Implementing Regulation (EU) 2024/2690 of 17 October 2024 laying down rules for the application of Directive (EU) 2022/2555 as regards technical and methodological requirements of cybersecurity risk-management measures and further specification of the cases in which an incident is considered to be significant.
- **Adopted:** 17 October 2024. **In force:** 20 days after OJ publication.
- **Two functions:** (1) the **Annex** details the technical/methodological requirements for the Art. 21(2) measures; (2) **Articles 3 to 14** specify when an incident is "significant".

## Scope: binds a SUBSET of NIS2 entities only

This regulation does **NOT** apply to every NIS2 entity. Per Article 1 it binds only these relevant entity types:

> DNS service providers, TLD name registries, cloud computing service providers, data centre service providers, content delivery network providers, managed service providers (MSP), managed security service providers (MSSP), providers of online marketplaces, online search engines and social networking services platforms, and trust service providers.

For other NIS2 sectors (energy, health, transport, manufacturing, etc.) the Annex is highly persuasive best practice and the de-facto technical benchmark, but the binding detail comes from national transposition plus sector guidance, not directly from 2024/2690. When advising, state this distinction. Do not tell a manufacturing or energy client that 2024/2690 is legally binding on them.

## Significant-incident thresholds (Articles 3 to 14)

- **Horizontal baseline (Art. 3(1)(a)):** direct financial loss exceeding **EUR 500 000 or 5 % of the entity's total annual turnover** in the preceding financial year, whichever is **lower**.
- **Entity-specific thresholds (Arts. 5 to 14)** layer on top, e.g.:
  - DNS providers: complete unavailability of 30 minutes or more.
  - Cloud providers: impact on 5 % of users or more, or 1 million users or more, whichever is smaller.
- These feed the Art. 23 reporting clock (24h early warning / 72h notification / 1-month final report): the implementing reg defines *when the clock starts* for a relevant entity.

## Annex structure: 13 sections, mapped to Art. 21(2) points

Top-level section number and title (verbatim), with the Art. 21(2) Directive point each maps to, and the named sub-points beneath it.

**1. Policy on the security of network and information systems** [Art. 21(2)(a)]
- 1.1 Policy on the security of network and information systems
- 1.2 Roles, responsibilities and authorities

**2. Risk management policy** [Art. 21(2)(a)]
- 2.1 Risk management framework
- 2.2 Compliance monitoring
- 2.3 Independent review of information and network security

**3. Incident handling** [Art. 21(2)(b)]
- 3.1 Incident handling policy
- 3.2 Monitoring and logging
- 3.3 Event reporting
- 3.4 Event assessment and classification
- 3.5 Incident response
- 3.6 Post-incident reviews

**4. Business continuity and crisis management** [Art. 21(2)(c)]
- 4.1 Business continuity and disaster recovery plan
- 4.2 Backup and redundancy management
- 4.3 Crisis management

**5. Supply chain security** [Art. 21(2)(d)]
- 5.1 Supply chain security policy
- 5.2 Directory of suppliers and service providers

**6. Security in network and information systems acquisition, development and maintenance** [Art. 21(2)(e)]
- 6.1 Security in acquisition of ICT services or ICT products
- 6.2 Secure development life cycle
- 6.3 Configuration management
- 6.4 Change management, repairs and maintenance
- 6.5 Security testing
- 6.6 Security patch management
- 6.7 Network security
- 6.8 Network segmentation
- 6.9 Protection against malicious and unauthorised software
- 6.10 Vulnerability handling and disclosure

**7. Policies and procedures to assess the effectiveness of cybersecurity risk-management measures** [Art. 21(2)(f)]
- (substantive requirements only, no named sub-points)

**8. Basic cyber hygiene practices and security training** [Art. 21(2)(g)]
- 8.1 Awareness raising and basic cyber hygiene practices
- 8.2 Security training

**9. Cryptography** [Art. 21(2)(h)]
- (substantive requirements only, no named sub-points)

**10. Human resources security** [Art. 21(2)(i)]
- 10.1 Human resources security
- 10.2 Verification of background
- 10.3 Termination or change of employment procedures
- 10.4 Disciplinary process

**11. Access control** [Art. 21(2)(i) and (j)]
- 11.1 Access control policy
- 11.2 Management of access rights
- 11.3 Privileged accounts and system administration accounts
- 11.4 Administration systems
- 11.5 Identification
- 11.6 Authentication
- 11.7 Multi-factor authentication

**12. Asset management** [Art. 21(2)(i)]
- 12.1 Asset classification
- 12.2 Handling of assets
- 12.3 Removable media policy
- 12.4 Asset inventory

**13. Environmental and physical security** [Art. 21(2)(c) and (e)]
- 13.1 Supporting utilities
- 13.2 Protection against physical and environmental threats
- 13.3 Perimeter and physical access control

> Mapping note: the Directive packs HR security, access control, and asset management into a single measure 21(2)(i). The Annex splits them across sections 10, 11, and 12, and adds section 13 (physical/environmental). Expect a one-to-many relationship between Directive letters and Annex sections.

## How to use this in advisory work

- For a **relevant entity** (the Art. 1 list), treat the Annex sub-points as the binding control checklist.
- For **other sectors**, use it as the benchmark and qualify that it is persuasive, not directly binding.
- For **gap assessments**, map controls to the X.Y sub-point level, not just the ten Directive measures. Real gaps surface there.
- The EUR 500 000 / 5 %-turnover threshold is the fastest test for "is this incident reportable?" for a relevant entity.
