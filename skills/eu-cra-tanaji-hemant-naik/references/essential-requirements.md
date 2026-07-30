# EU CRA — Essential Requirements & Obligations Reference

## Table of Contents
1. [Annex I Part I — Security Properties of PDEs](#annex-i-part-i--security-properties)
2. [Annex I Part II — Vulnerability Handling](#annex-i-part-ii--vulnerability-handling)
3. [Product Categories — Annex III (Class I)](#annex-iii--class-i-products)
4. [Product Categories — Annex IV (Class II)](#annex-iv--class-ii-products)
5. [Support Period Obligations](#support-period-obligations)
6. [SBOM Requirements](#sbom-requirements)
7. [Vulnerability and Incident Reporting](#vulnerability-and-incident-reporting)
8. [Manufacturer Obligations Summary (Article 13)](#manufacturer-obligations-article-13)
9. [Importer Obligations (Article 19)](#importer-obligations-article-19)
10. [Distributor Obligations (Article 20)](#distributor-obligations-article-20)
11. [Open-Source Software Stewards](#open-source-software-stewards)

---

## Annex I Part I — Security Properties

Products with digital elements must be **designed, developed, and produced** to meet these essential requirements:

1. **No known exploitable vulnerabilities:** Products must be placed on the market without known exploitable vulnerabilities. Manufacturers must exercise due diligence in tracking and addressing vulnerabilities before release.

2. **Secure by default configuration:**
   - Minimal attack surface — functions and ports not required for the intended purpose must be disabled by default
   - Secure default settings — passwords, cryptographic keys, and authentication must not use factory defaults that are easily guessable or common across products
   - Users must be able to reset the product to a secure factory state

3. **Protection against unauthorised access:**
   - Appropriate authentication and access control mechanisms
   - Identity and access management based on the principle of least privilege
   - Where feasible: multi-factor authentication, cryptographic credentials

4. **Confidentiality — data protection:**
   - Personal and other sensitive data protected at rest and in transit using state-of-the-art encryption
   - Cryptographic best practices (no deprecated algorithms)

5. **Integrity — data and software protection:**
   - Unauthorised modification of data, firmware, or software detected and mitigated
   - Software and firmware updates must be cryptographically signed and the signature verified before installation
   - Secure boot mechanisms where applicable

6. **Data minimisation:**
   - Only personal data and other data necessary for intended function is processed
   - Privacy-by-design principles applied (GDPR Art. 25 alignment)

7. **Availability — resilience against DoS:**
   - Products must be designed to maintain availability of essential functions under denial-of-service attacks
   - Resilience and graceful degradation

8. **Limited negative impact on other devices or networks:**
   - Products must not be usable as attack vectors against other devices or networks
   - Network traffic generation must be limited to what is necessary

9. **Exploit mitigation mechanisms:**
   - State-of-the-art exploit mitigations (ASLR, stack canaries, NX/DEP, control-flow integrity) where feasible
   - Memory-safe programming practices or compensating controls

10. **Security information transparency:**
    - Users must receive adequate information about the product's security features, settings, and limitations
    - Contact details for vulnerability reporting published

---

## Annex I Part II — Vulnerability Handling

Manufacturers must put in place and document a **vulnerability handling policy and process** covering:

1. **Vulnerability identification:**
   - Maintain an inventory of software components in the product (SBOM basis)
   - Proactively monitor for new CVEs and security advisories affecting integrated components
   - Apply automated vulnerability scanning in the build pipeline

2. **Vulnerability remediation:**
   - Vulnerabilities addressed without undue delay
   - Security updates released promptly and free of charge
   - Document the remediation process and evidence of fix verification

3. **Coordinated Vulnerability Disclosure (CVD) policy:**
   - Publish a CVD/VDP policy that is publicly accessible
   - Specify: expected response time, acknowledgement process, scope, responsible disclosure expectations
   - Provide a named point of contact (email, security advisory page, or bug bounty platform)

4. **CERT/CSIRT information sharing:**
   - Share information about identified vulnerabilities and mitigations with EU CERT/CSIRT networks as appropriate

5. **SBOM provision:**
   - Provide a machine-readable SBOM on request to national authorities
   - Minimum content: top-level dependencies (name, version, supplier, licence)
   - Recommended formats: SPDX (ISO/IEC 5962:2021), CycloneDX
   - SBOM must be kept current throughout the support period

6. **Security updates — free of charge:**
   - Security updates must not be bundled exclusively with feature updates (security patches must be available independently)
   - Update delivery mechanism must be secure (signed updates, integrity verification)
   - Users must be notified of available security updates

7. **ENISA/CSIRT reporting — actively exploited vulnerabilities:**
   - Within **24 hours** of becoming aware: early warning to ENISA and relevant national CSIRT
   - Within **72 hours** of becoming aware: full vulnerability notification (nature of vulnerability, affected products, remediation status)
   - Final report within **14 days** of fix availability
   - Notify affected users as soon as practicable

8. **Security incident reporting (severe incidents):**
   - Severe incidents impacting product security → notify ENISA and national CSIRT within 24 hours (early warning)
   - Full incident report within 72 hours
   - Final post-incident report within 1 month

9. **End-of-life notification:**
   - Notify users of end of security support at least **1 year** before the end-of-support date
   - Provide final cumulative security update where technically feasible
   - Document that the product is no longer receiving security updates

---

## Annex III — Class I Products

Class I products require **enhanced conformity assessment** (manufacturer may choose self-assessment or Notified Body). These 35 categories include:

**Identity and access:**
- Identity management software and hardware (identity providers, SSO systems)
- Password managers
- Biometric readers and biometric data management software
- Privileged access management (PAM) software

**Network security and monitoring:**
- Network traffic monitoring and analysis tools
- Network monitoring systems
- Web application firewalls
- Network filters (DNS filtering, email filtering)
- Micro-segmentation tools
- VPNs (virtual private networks)
- Security information and event management (SIEM) systems

**Endpoint security:**
- Endpoint detection and response (EDR) tools
- Antivirus and anti-malware software
- Security update management software (patch management)

**Cryptography:**
- Certificate management software
- PKI components
- Digital signature software

**Hardware:**
- Microprocessors, microcontrollers (sold for integration in PDEs)
- General-purpose processors
- Routers, modems, and network switches intended for home use
- Smart meters and energy management systems

**Development tools:**
- Application security testing tools (SAST, DAST, IAST)
- Code integrity tools
- Compilers and build tools (where used for safety-critical software)

**Other Class I examples:**
- Mobile applications providing secure communications
- Industrial automation/monitoring systems (non-critical infrastructure)
- Remote access software (RDP, SSH clients/servers)
- Smart home hubs and controllers

---

## Annex IV — Class II Products

Class II products require **mandatory Notified Body assessment**. These 12 categories include:

1. **Hypervisors and container runtime environments** (Type 1 hypervisors, Docker, Kubernetes, etc.)
2. **Trusted Execution Environments (TEEs)** and hardware security enclaves
3. **Trusted Platform Modules (TPMs)**
4. **Hardware Security Modules (HSMs)**
5. **Microprocessors with security functions** (secure elements, cryptographic processors)
6. **Smart card readers and smart cards** (including NFC-enabled devices)
7. **Industrial firewalls, intrusion detection/prevention systems (IDS/IPS)** intended for use in critical infrastructure or OT environments
8. **Industrial control systems (ICS) and SCADA systems** — including PLCs, RTUs, DCS components intended for critical infrastructure sectors (energy, water, transport)
9. **Industrial robots and robotic control systems**
10. **Safety-critical automotive components** with network connectivity (ECUs, V2X modules — to the extent not excluded by type-approval)
11. **Medical-grade network-connected devices** (where not excluded by MDR/IVDR)
12. **Advanced metering infrastructure (AMI) systems** and grid-connected energy management systems

---

## Support Period Obligations

### Minimum support period
- **At least 5 years** from the date the product is placed on the market, or the expected product lifetime if shorter than 5 years
- The support period must be **clearly communicated** to users before purchase (in product description, packaging, or documentation)

### During the support period
- Provide free security updates in a timely manner
- Security updates must not reduce or degrade product functionality or security posture
- Maintain and update the SBOM

### End of support
- Notify users at least **1 year before end of security support**
- Provide a final cumulative security update where technically feasible
- Cease making the product available on the EU market if unable to fulfil support obligations (or provide an adequate alternative)
- Document the end-of-support decision in the technical file

### Multi-component products
- If the product integrates a software component with a shorter support lifecycle, the product's support period is limited accordingly, OR the manufacturer must provide alternative components or patches independently

---

## SBOM Requirements

### What is required
- A **machine-readable SBOM** must be available on request to national market surveillance authorities
- Minimum content:
  - Product name and version
  - For each component: component name, version, supplier/author, licence
  - Dependency relationship (top-level dependencies at minimum)
- The SBOM must be kept **current** throughout the support period

### Recommended formats
- **SPDX** (ISO/IEC 5962:2021) — widely used, standardised
- **CycloneDX** — security-focused, supports VEX (Vulnerability Exploitability eXchange)
- JSON or XML formats preferred for machine readability

### VEX (Vulnerability Exploitability eXchange)
- Not mandated but strongly recommended as a complement to SBOM
- VEX documents allow manufacturers to communicate whether a specific CVE affects a specific product version
- Reduces false positives for customers and authorities scanning the SBOM against vulnerability databases

### SBOM governance
- Assign ownership of SBOM maintenance to a named team
- Integrate SBOM generation into the CI/CD pipeline (automated tooling: SPDX tools, Syft, Trivy, etc.)
- Review and update SBOM with each release and when third-party components are updated

---

## Vulnerability and Incident Reporting

### Reporting recipients
- **ENISA** (EU Agency for Cybersecurity) — central reporting point; ENISA forwards to national CSIRTs
- **National CSIRT** — member state's designated CSIRT (e.g., BSI/CERT-Bund in Germany, ANSSI in France, NCSC in Netherlands/UK-equivalent)
- **Affected users** — direct notification where feasible

### Actively exploited vulnerability
| Timeframe | Action |
|---|---|
| T+24 hours | Early warning to ENISA: vulnerability identifier, affected product versions, brief description |
| T+72 hours | Full notification: nature of vulnerability, CVSS/severity, affected versions, workarounds, remediation status |
| T+14 days after fix | Final report: fix details, patch release notes, lessons learned |

### Severe security incident
| Timeframe | Action |
|---|---|
| T+24 hours | Early warning to ENISA and national CSIRT |
| T+72 hours | Full incident notification |
| T+1 month | Post-incident report |

### What triggers reporting
- **Actively exploited vulnerability:** A vulnerability in the product that the manufacturer becomes aware is being actively exploited in the wild (confirmed or credible intelligence)
- **Severe incident:** A security incident that has, or could have, significant impact on the product's security or availability at scale (e.g., supply chain compromise, cryptographic key exposure, large-scale unauthorised access)

---

## Manufacturer Obligations (Article 13)

Manufacturers must:
1. Design, develop, and produce PDEs in accordance with Annex I essential requirements
2. Conduct a cybersecurity risk assessment before placing on market
3. Prepare technical documentation (Annex VII) and retain for 10 years
4. Conduct conformity assessment (Module A self-assessment or Notified Body)
5. Draw up EU Declaration of Conformity (Annex V) and retain for 10 years
6. Affix CE marking
7. Register Class I and Class II products in the EU database before placing on market
8. Apply vulnerability handling obligations continuously throughout the support period
9. Report actively exploited vulnerabilities and severe incidents to ENISA/CSIRTs
10. Ensure products distributed in the EU have a point of contact address
11. Cooperate with market surveillance authorities
12. Take corrective action if product is non-compliant; issue recall if necessary

---

## Importer Obligations (Article 19)

Importers must:
1. Only place on the EU market products accompanied by a valid DoC and technical documentation
2. Verify CE marking is affixed and legible
3. Verify the manufacturer is identified on the product
4. Add their own name, registered trade name or mark, and postal/electronic address
5. Ensure the product has vulnerability reporting contact information in a Union language
6. Not place on market products known to be non-compliant
7. Notify the manufacturer and market surveillance authority if a product poses a risk
8. Retain copies of DoC and technical documentation for 10 years
9. Cooperate with market surveillance authorities

---

## Distributor Obligations (Article 20)

Distributors must:
1. Verify CE marking, DoC availability, and instructions/information in a Union language
2. Not make available products known to be non-compliant
3. Notify the manufacturer and market surveillance authority of risks
4. Cooperate with market surveillance authorities on request

---

## Open-Source Software Stewards

**Definition:** Entities that provide sustained support for open-source software components that are incorporated into PDEs on a commercial basis (e.g., foundations, companies maintaining widely-used open-source libraries).

**Light-touch obligations (compared to manufacturers):**
- Publish and maintain a **cybersecurity policy** covering vulnerability handling and coordinated disclosure
- Cooperate with market surveillance authorities when requested
- Forward security vulnerability information to affected downstream users
- **Not required** to conduct full conformity assessment or affix CE marking
- Must provide technical documentation to authorities on request

**Note:** Individual open-source contributors who do not monetise or commercially support their software are **not** covered by CRA.
