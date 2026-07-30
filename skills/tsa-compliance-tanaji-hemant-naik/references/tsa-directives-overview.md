# TSA Cybersecurity Security Directives — Overview and Revision History

Source: Transportation Security Administration (TSA); Federal Register; DHS publications
https://www.tsa.gov/sd-and-ea

Note: TSA Security Directives are classified as Sensitive Security Information (SSI). Full directive text is not publicly available. This reference is based on publicly disclosed summaries, Federal Register notices, and TSA press releases.

---

## Overview

Following the May 2021 Colonial Pipeline ransomware attack, TSA issued mandatory cybersecurity Security Directives requiring critical transportation infrastructure owners and operators to implement baseline cybersecurity measures. These directives have been updated through multiple revisions and now cover pipelines, freight rail, passenger rail, public transit, and (via NPRM) bus operators.

Directives are renewed annually and carry the force of law under 49 U.S.C. § 114. Non-compliance can result in civil penalties. Each directive identifies specific "covered entities" by name — not all operators in a sector are automatically covered.

---

## Pipeline Security Directives

### SD Pipeline-2021-01 Series — Immediate Measures
**Purpose**: Established minimum immediate cybersecurity requirements for pipeline operators following the Colonial Pipeline incident.

**Current revision**: Pipeline-2021-01G (effective January 2026)

| Revision | Issued | Key Changes |
|----------|--------|-------------|
| Pipeline-2021-01 | May 2021 | Initial directive: incident reporting, coordinator, practices review |
| Pipeline-2021-01A | July 2021 | Minor clarifications |
| Pipeline-2021-01B/C | 2022–2023 | Renewed with refinements |
| Pipeline-2021-01D | May 2024 | Extended; clarified applicability and reporting requirements |
| Pipeline-2021-01E | 2025 | Extended; additional clarifications |
| Pipeline-2021-01G | January 2026 | Current revision |

**Core requirements of SD Pipeline-2021-01 series**:
1. Report cybersecurity incidents to CISA within 24 hours
2. Designate a Cybersecurity Coordinator (24/7 availability; backup designee)
3. Review current cybersecurity practices and identify gaps relative to TSA/CISA guidance
4. Develop and implement remediation measures to address identified gaps

**Covered entities**: Owners and operators of TSA-designated critical hazardous liquid and natural gas pipelines and LNG facilities.

---

### SD Pipeline-2021-02 Series — Comprehensive CRMP
**Purpose**: Established comprehensive Cyber Risk Management Program requirements for pipeline operators.

**Current revision**: Pipeline-2021-02F (latest)

| Revision | Issued | Key Changes |
|----------|--------|-------------|
| Pipeline-2021-02 | July 2021 | Initial comprehensive CRMP requirements |
| Pipeline-2021-02A/B | 2022 | Performance-based approach introduced; replaced prescriptive controls |
| Pipeline-2021-02C/D | 2023 | Further refinements; feedback incorporated from operators |
| Pipeline-2021-02E | July 2024 | Extended; strengthened; additional clarity on OT/IT requirements |
| Pipeline-2021-02F | 2025/2026 | Current revision |

**Core requirements of SD Pipeline-2021-02 series**:
1. **Cybersecurity Implementation Plan (CIP)**: Submit to TSA for review and approval
2. **Cybersecurity Incident Response Plan (IRP/CIRP)**: Document + test two objectives annually
3. **Architecture Design Review (ADR)**: Annual review of IT/OT network architecture
4. **Cybersecurity Assessment Plan (CAP)**: Annual assessment + results reported to TSA
5. **Four technical domains**: Network segmentation, access controls, continuous monitoring, patch management
6. **Accountable Executive**: C-suite individual with authority for cybersecurity decisions

**Sensitive Security Information (SSI)**: The full text of SD Pipeline-2021-02 and its revisions is SSI. Covered entities receive the directive directly from TSA.

---

## Freight Rail Security Directives

### SD 1580-21-01 Series — Freight Rail Cybersecurity
**Purpose**: Requires freight railroad carriers and related entities to implement cybersecurity measures equivalent in scope to the pipeline directives.

**Current revision**: SD 1580-21-01E (effective January 15, 2026)

| Revision | Issued | Key Changes |
|----------|--------|-------------|
| SD 1580-21-01 | 2021 | Initial rail cybersecurity: incident reporting, coordinator |
| SD 1580-21-01A/B/C | 2022–2023 | CRMP requirements added; performance-based updates |
| SD 1580-21-01D | October 2024 | Updated; aligned with pipeline directive structure |
| SD 1580-21-01E | January 15, 2026 | Current revision |

**Core requirements of SD 1580-21-01 series**:
1. Report cybersecurity incidents to CISA within 24 hours
2. Designate a Cybersecurity Coordinator (24/7)
3. Implement CRMP including CIP, IRP (annual testing), ADR, CAP
4. Four technical domains: segmentation, access controls, monitoring, patching
5. Specific attention to ICS/SCADA systems controlling rail operations (switches, signals, dispatch)

**Covered entities**: TSA-designated freight railroad owners and operators with higher cybersecurity risk profiles. Includes Class I railroads and potentially higher-risk Class II/III operations.

---

## Public Transportation and Passenger Rail Security Directives

### SD 1582-21-01 Series — Transit and Passenger Rail Cybersecurity
**Purpose**: Requires public transportation agencies and passenger railroad operators to implement cybersecurity measures.

**Current revision**: SD 1582-21-01E (effective January 15, 2026)

| Revision | Issued | Key Changes |
|----------|--------|-------------|
| SD 1582-21-01 | 2021 | Initial transit cybersecurity requirements |
| SD 1582-21-01A/B/C | 2022–2023 | CRMP additions; performance-based approach |
| SD 1582-21-01D | October 2024 | Updated requirements |
| SD 1582-21-01E | January 15, 2026 | Current revision |

**Core requirements of SD 1582-21-01 series**: Same structure as freight rail — incident reporting, coordinator, CRMP (CIP, IRP, ADR, CAP), four technical domains.

**Covered entities**: TSA-designated public transportation agencies (metro, light rail, commuter rail, bus rapid transit) and passenger railroad operators (Amtrak and designated commuter rail agencies).

**OT focus for transit**: Automatic Train Control (ATC) systems, SCADA for traction power and ventilation, Communications-Based Train Control (CBTC), Electronic Ticketing Systems (where they interface with operational systems), CCTV/access control integration.

---

## Aviation Cybersecurity

Aviation cybersecurity directives are issued separately by TSA to airport operators and aircraft operators. These are largely SSI and address:
- Incident reporting to CISA within 24 hours
- Cybersecurity Coordinator designation
- Access controls for aviation systems
- Network segmentation between passenger and operational networks
- Passenger screening system security

The aviation sector also operates under FAA cybersecurity requirements for aircraft systems, which are distinct from TSA directives.

---

## November 2024 NPRM — Proposed Permanent Rule

**Title**: "Enhancing Surface Transportation Cybersecurity"
**Published**: Federal Register, November 2024
**Comment period**: Closed February 5, 2025

### What the NPRM proposes:
The NPRM would formalise current Security Directive requirements into permanent federal regulations under 49 CFR, making them enforceable as regulation rather than directive.

**Proposed covered entities**:
| Sector | Coverage |
|--------|---------|
| Pipelines | Same as current directives; higher-risk designated operators |
| Freight railroad | Higher-risk Class I and designated Class II/III |
| Passenger rail/transit | Higher-risk passenger rail and transit agencies |
| Bus operators | Incident reporting requirements only (less prescriptive) |

**Three core proposed requirements**:
1. **Annual Cybersecurity Evaluation**: Enterprise-wide evaluation comparing current profile vs target profile (explicitly using NIST CSF 2.0 as the framework)
2. **Cybersecurity Operational Implementation Plan (COIP)**: TSA-approved plan (equivalent to current CIP) with accountable executive, CCS inventory, network architecture description, and measures for all four domains
3. **Cybersecurity Assessment Plan (CAP)**: Annual assessment schedule and reporting to TSA

**Framework alignment**:
- **NIST CSF 2.0**: Primary framework for the annual profile-based evaluation
- **CISA Cross-Sector Cybersecurity Performance Goals (CPGs)**: Baseline performance measures referenced in the NPRM
- CPGs are grouped into IT and OT goals and map closely to NIST CSF subcategories

**Status as of 2026**: Comment period closed; final rule not yet published. Current Security Directives remain in force.

---

## Relationship to Other Frameworks

| Framework | Relationship to TSA Directives |
|-----------|-------------------------------|
| **NIST CSF 2.0** | Referenced in 2024 NPRM for annual profile evaluation; GV/ID/PR/DE/RS/RC maps to TSA domains |
| **CISA CPGs** | Baseline goals for critical infrastructure; TSA directives align with IT and OT CPGs |
| **NIST SP 800-82** | Guide to ICS/OT security; informative reference for implementing TSA's OT requirements |
| **NERC CIP** | Electric sector parallel; some operators subject to both TSA and NERC CIP |
| **IEC 62443** | OT/ICS security standard; applicable for implementing TSA's Domain 1–4 requirements |
| **NIST SP 800-53** | Federal controls; FedRAMP-covered systems within covered entities may have dual obligations |

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **Critical Cyber System (CCS)** | IT or OT system whose compromise could disrupt operations, safety, or security |
| **Cybersecurity Coordinator** | 24/7 designated contact person for TSA and CISA |
| **CIP / COIP** | Cybersecurity Implementation Plan / Cybersecurity Operational Implementation Plan |
| **IRP / CIRP** | (Cybersecurity) Incident Response Plan |
| **ADR** | Architecture Design Review — annual IT/OT network architecture assessment |
| **CAP** | Cybersecurity Assessment Plan — annual CRMP effectiveness assessment |
| **CRMP** | Cyber Risk Management Program — the collective set of CIP, IRP, ADR, CAP requirements |
| **SSI** | Sensitive Security Information — information protected under 49 CFR Part 1520 |
| **OT** | Operational Technology — hardware/software controlling physical industrial processes |
| **ICS** | Industrial Control System — subset of OT |
| **SCADA** | Supervisory Control and Data Acquisition — OT system for monitoring/controlling distributed assets |
