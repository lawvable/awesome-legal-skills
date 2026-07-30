# EDPB DPIA Template Explainer — Methodology Reference

> Source: EDPB "Template for Data Protection Impact Assessment ('DPIA') — Explainer", Version 1.0, adopted 10 March 2026, for public consultation.

This reference distills the EDPB's guidance on completing the DPIA template into practical methodology notes for DPIA Sentinel.

---

## 1. Template Purpose and Scope

The EDPB template is a **data-entry and reporting tool**, not a DPIA methodology. Key design principles:

- **Methodology-agnostic.** "Controllers can conduct their risk analysis and management processes as they prefer, using the DPIA methodology of their choice" (intro). The template records "a minimum amount of information that should always be documented" in a format "easily accepted by all SAs."
- **Pre-defined fields prompt complete responses.** Designed for ease of use — minimises errors, saves time, and ensures all necessary information is captured.
- **Intentional redundancy.** "Certain redundancy between the DPIA template sections ensures that each mandatory element is addressed explicitly and in a traceable manner, while enabling cross-referencing. Furthermore, the same fact serves different functions across sections" (intro). Controllers must establish links between sections and provide consistent information across tables.
- **Adopted for public consultation.** This is Version 1.0 (10 March 2026). Check for the final adopted version before treating guidance as definitive.

---

## 2. Two Risk Categories

This is the most important methodological contribution of the template. The EDPB explicitly separates risks into two distinct tracks, each assessed in a different template section.

### Track A — Inherent-by-Design Risks (Section 3.1)

Risks that exist "even if everything works exactly as designed and all actors follow the rules" (para 32).

**Core principle:** "Design choices themselves create risks for data subjects' rights and freedoms, even where there is no failure or attack" (para 32).

**Risk sources:** Flow mainly from:

- The processed personal data itself (Section 1.1.1)
- The very purpose of the processing (Section 1.1.2)
- The nature, scope, and context of the processing (Section 1.1.4)

**Key definitions (para 32):**

| Concept | Definition |
|---|---|
| **Threat** | "Any circumstance or event with the potential to adversely impact data subject's rights and freedoms (for example, linking, identifying, inaccuracy or data disclosure)" — may cause physical, material, or non-material damage |
| **Risk source** | "The origin or underlying cause from which a threat can materialise" — e.g., the processing's purpose, wrong design and weaknesses, exposures, use of unique identifiers, long retention periods |
| **Impact** | Consequences of threat materialisation, "always considering data subject's rights and freedoms (see recital 75 GDPR)" |

**Examples of inherent-by-design threats:**

- Linking risk (combining datasets enables re-identification)
- Identification risk (data scope allows singling out individuals)
- Inaccuracy (inherent to the data scope or collection method)
- Profiling bias (embedded in the processing design)
- Data disclosure (sharing by design with third parties)

### Track B — Operational Risks (Section 4.1.a)

Risks from "non-default, accidental, unlawful, or abnormal events" (para 35).

**Core principle:** "Something does not go as intended in the design, implementation, configuration or operation, or when there are malicious actors" (para 35). "The root cause is a deviation from the intended, compliant state" (para 35).

**Minimum threat vectors to identify:**

1. **Illegitimate access** to personal data
2. **Undesired modification** of personal data
3. **Disappearance of data** (loss of availability)

**Risk source examples (para 35):**

| Category | Examples |
|---|---|
| Technical defects | Software bugs, misconfigurations, wrong access rights |
| Operational errors | Sending data to the wrong recipient, wrong dataset used, forgotten de-provisioning |
| Maintenance failures | Unpatched vulnerabilities, outdated components |
| Insider threats | Staff exceeding their authorised use |
| External attacks | Phishing, ransomware |

---

## 3. Risk Assessment Methodology

### Scales

"Often a 2 to 5 levels scale is used" (para 36). The EDPB does **not** mandate a specific scale. Controllers must define:

- Likelihood levels and their meanings
- Severity levels and their meanings
- Risk metrics and how risks are prioritised
- Risk acceptance levels

DPIA Sentinel uses a 5x5 matrix (1-5 for likelihood, 1-5 for severity). This is fully EDPB-compatible.

### Risk Formula

"Risk level expresses the extent to which data subjects are affected by the corresponding threat and typically a function of: (i) the likelihood of the threat materialisation; and (ii) the magnitude of the adverse impacts that would arise if the threat materialises (severity)" (para 37).

**Standard calculation:** Risk = likelihood x severity, "typically using qualitative scales to derive a level (for example, low/medium/high)" (para 37).

### Modulating Factors (paras 37-38)

"Characteristics that increase or decrease the likelihood or severity of a risk (without being the primary source of the corresponding threat)" (para 37).

| Direction | Factor type | Examples |
|---|---|---|
| **Aggravating** (upward) | Scale | Very large number of data subjects |
| | Sensitivity | High data sensitivity |
| | Vulnerability | Data subjects in a situation of dependency or vulnerability (children, patients, workers, migrants) |
| | Exposure | High exposure to external adversaries |
| **Mitigating** (downward) | Controls | Design choices and measures (from Section 2.3) |

**Application:** "Modulating factors, not always present, may help in adjusting the baseline risk (likelihood x severity) up or down to reflect real-world nuances for this specific processing and its context" (para 37). These are **not** a formula multiplier — they represent contextual adjustment with documented justification.

### Inherent Risk (para 37)

"For a specific data processing, inherent risk is the risk level the controller assigns to the planned processing assuming the baseline or initial set of planned measures" (para 37).

- Combines **both** Track A (Section 3.1) and Track B (Section 4.1.a) risks
- Assessed **before** additional mitigations from the action plan (Section 4.2)

### Residual Risk (para 42)

"The risk that still remains after the controller has reflected on the unacceptable or excessively high risks, has decided to add additional mitigating measures, and has assessed how far those new measures actually reduce the inherent (initial or baseline) risk" (para 42).

- Assessed **after** additional mitigations from Section 4.2.a

### Risk Acceptability (footnote 9)

Two critical principles on acceptability:

- "A risk in data protection may be deemed non-acceptable if the potential severity of its impact is very high, even when its likelihood of occurring is low" (fn 9)
- "If the consequences for data subjects could be extremely serious, the risk may be considered unacceptable, regardless of how rarely the event is expected to occur" (fn 9)

This means high-severity / low-likelihood risks **cannot** be dismissed based on probability alone.

---

## 4. Asset-Based Risk Analysis

### Definition

"An 'asset' typically refers to any resource, tangible or intangible, that is used to process personal data" (para 20). "Assets represent vectors for both value and risk in the context of data protection" (para 20).

### Asset Types

| Category | Examples |
|---|---|
| Hardware, infrastructure, network | Servers, laptops, mobile devices, storage media, scanners, VPN gateways |
| Software | Database engines, business applications |
| APIs and models | Interfaces, AI/ML models |
| Personnel | Users, administrators, developers, operators, support staff, decision-makers |
| Sites and premises | Data centres, archives |
| Organisational | Policies, procedures, contracts with processors and sub-processors |

### Scoping Principles

- Include only **risk-relevant** assets: "whose compromise would plausibly impact rights and freedoms in a non-trivial way" (para 20)
- Examples of risk-relevant assets: those directly storing or processing personal data, those that control access or protect data, exposed or high-impact components (public-facing portals, APIs, data-sharing interfaces to third parties)
- "Very small, generic, or easily substitutable elements usually do not need individual listing" (para 20)

### Grouping

- Group by: logical module, technical layer, or function
- "Balance completeness and manageability" (para 20)
- Detailed per-device / per-service inventory goes in separate technical documentation
- The DPIA template captures the architecture closely related to risk assessment and management

---

## 5. Data Lifecycle Phases

The template prescribes five explicit lifecycle phases (para 19):

| Phase | Description |
|---|---|
| **1. Collection** | What data is collected and how, including sources and information provided to data subjects |
| **2. Use** | Operations performed on the data, technologies used, automated decision-making or profiling involved, whether data is combined with other datasets |
| **3. Storage** | Where and how data is stored (physical, cloud, third-party), and who has access |
| **4. Sharing and Transfer** | Data sharing to third parties or transfers outside the EU, legal mechanisms or tools used (e.g., SCCs, adequacy decisions) |
| **5. Deletion and Destruction** | Criteria and procedures for securely deleting data when no longer needed, including methods for permanent erasure |

---

## 6. Implementation Status Model

Three tiers required for every compliance measure (para 27):

| Status | Definition |
|---|---|
| **Planned** | "The safeguard is only at the intention or design stage, it has been identified as necessary, but is not yet deployed in production" |
| **Partially implemented** | "Some elements of the measure are in place, but important aspects are missing or incomplete" |
| **Implemented** | "The measure exists, is deployed, and is effectively operating in the live environment, not just on paper, there is evidence that the control works as intended" |

---

## 7. Necessity and Proportionality as Upstream Gates

Section 3 is assessed **before** risk mitigation (Section 4). These are sequential gates.

### Necessity (para 33)

- Evaluate whether the processing is **effective** and the **least intrusive** for data subjects' rights and freedoms
- Analyse whether the processing "demonstrably works as intended, at least to the appropriate or required level"
- Must provide **evidence** — specifically "concerning the different considered alternatives and their effectiveness in achieving the purpose"
- References: EDPS "Assessing the necessity of measures that limit the fundamental right to the protection of personal data: A Toolkit"

### Proportionality (para 34)

- "Necessity is a pre-condition for proportionality" (para 34)
- Discuss importance of the processing and its potential benefits for: the data subject, the organisation, and collectively
- Core question: "Is the processing envisaged to fulfil the purpose a proportionate response to the need you have, given the limitations to the data protection and privacy rights?" (para 34)
- The advantages resulting from the processing should not be outweighed by the disadvantages with respect to fundamental rights and freedoms
- Must use results from Section 3.1 (inherent-by-design risks) to reflect on the advantage/disadvantage balance
- References: EDPS "Guidelines on assessing the proportionality of measures that limit the fundamental rights to privacy and to the protection"

---

## 8. Four-Outcome Decision Model

Section 6 prescribes four outcomes (para 49):

| Outcome | Code | When to use |
|---|---|---|
| **REJECTED** | (a) | Processing must be abandoned — risks are unacceptable, required tests cannot be passed, advised by the DPO, data subjects, or Supervisory Authority |
| **CONSULTATION** | (b) | Consult the SA — either (i) residual risks remain high after all feasible measures, or (ii) national law requires consultation per Art. 36(5) GDPR |
| **APPROVED** | (c) | Processing may proceed as planned — residual risks are acceptable; no Art. 36(5) requirement applies |
| **CONDITIONALLY APPROVED** | (d) | Processing proceeds only after specified conditions are met — must link conditions to Section 4.2 measures (e.g., "by modifying the data processing design to better address identified risks") |

---

## 9. Relationship to WP 248 rev.01

The EDPB explicitly references WP 248 rev.01 (Guidelines on Data Protection Impact Assessment) as the foundational DPIA methodology guideline (footnotes 2 and 3).

### What the template PRESERVES from WP 248

- Two-stage risk assessment (inherent risk then residual risk)
- Nine-criteria threshold analysis for determining DPIA obligation
- Art. 35(3) mandatory triggers for conducting a DPIA

### What the template ADDS beyond WP 248

- **Modulating factors** as an explicit concept in risk assessment
- **Asset inventory** as a structured element of the DPIA
- **Five-phase data lifecycle** (collection, use, storage, sharing/transfer, deletion/destruction)
- **Implementation status tiers** (planned / partially implemented / implemented)
- **Four-outcome conclusion model** (rejected / consultation / approved / conditionally approved)
- **RACI suggestion** for DPIA team roles and responsibilities

### What the template ELABORATES on WP 248

- Necessity and proportionality as distinct, sequenced assessments
- Inherent-by-design risks vs. operational risks as separate tracks
- Cross-referencing between template sections for traceability

---

## 10. Annex: National SA DPIA Guidelines

The EDPB template Annex 1 provides a consolidated list of national Supervisory Authority DPIA guidelines. DPIA Sentinel's jurisdiction files should cross-reference these.

> See also: EDPB data protection guide for small business — https://www.edpb.europa.eu/sme-data-protection-guide/home_en

| # | Supervisory Authority | Link(s) |
|---|---|---|
| 1 | Austria (AT) | https://dsb.gv.at/faqs/verpflichtungen-fuer-unternehmen |
| 2 | Belgium (BE) | — |
| 3 | Bulgaria (BG) | https://cpdp.bg/ (lists of processing operations requiring DPIA) |
| 4 | Croatia (HR) | https://azop.hr/procjena-ucinka-na-zastitu-podataka-eng-data-protection-impact-assessment-dpia/ ; https://olivia-gdpr-arc.eu/hr/topic/show/9 |
| 5 | Cyprus (CY) | — |
| 6 | Czech Republic (CZ) | https://uoou.gov.cz/media/profesional/metodika-obecneho-posouzeni-vlivu-na-ochranu-osobnich-udaju.pdf |
| 7 | Denmark (DK) | https://www.datatilsynet.dk/regler-og-vejledning/behandlingssikkerhed/konsekvensanalyse |
| 8 | EDPS | — |
| 9 | Estonia (EE) | https://www.aki.ee/uudised/mis-asi-mojuhinnang |
| 10 | Finland (FI) | FI: https://tietosuoja.fi/vaikutustenarviointi ; EN: https://tietosuoja.fi/en/impact-assessments |
| 11 | France (FR) | FR: https://www.cnil.fr/fr/guides-aipd ; EN: https://www.cnil.fr/en/privacy-impact-assessment-pia |
| 12 | Germany (DE) | https://www.datenschutz-mv.de/datenschutz/datenschutzmodell/ |
| 13 | Greece (EL) | EL: https://www.dpa.gr/el/foreis/ektimisi_adiktipou_kai_diavouleush ; EN: https://www.dpa.gr/en/Organisations/Impact_Assessment ; https://www.dpa.gr/en/by-design/risk-assessment-dpia ; https://www.dpa.gr/en/by-design/ict-organizational-gdpr-roles-dpia |
| 14 | Hungary (HU) | — |
| 15 | Iceland (IS) | — |
| 16 | Ireland (IE) | https://www.dataprotection.ie/en/dpc-guidance/guide-data-protection-impact-assessments |
| 17 | Italy (IT) | — |
| 18 | Latvia (LV) | https://www.dvi.gov.lv/lv/novertejums-par-ietekmi-uz-datu-aizsardzibu-nida |
| 19 | Liechtenstein | — |
| 20 | Lithuania (LT) | — |
| 21 | Luxembourg (LU) | — |
| 22 | Malta (MT) | https://idpc.org.mt/for-organisations/data-protection-impact-assessment/ |
| 23 | Netherlands (NL) | NL: https://autoriteitpersoonsgegevens.nl/themas/basis-avg/praktisch-avg/data-protection-impact-assessment-dpia ; EN: https://autoriteitpersoonsgegevens.nl/en/themes/basic-gdpr/gdpr-in-practice/data-protection-impact-assessment-dpia |
| 24 | Norway (NO) | — |
| 25 | Poland (PL) | PL: https://uodo.gov.pl/pl/598/3617 ; EN: https://uodo.gov.pl/en/553/1882 ; https://monitorpolski.gov.pl/MP/2019/666 ; https://uodo.gov.pl/500 ; https://uodo.gov.pl/pl/138/605 |
| 26 | Portugal (PT) | — |
| 27 | Romania (RO) | — |
| 28 | Slovakia (SK) | — |
| 29 | Slovenia (SI) | https://www.ip-rs.si/fileadmin/user_upload/Pdf/Ocene_ucinkov/Smernice_o_ocenah_ucinka_DPIA_julij2018.pdf |
| 30 | Spain (ES) | ES: https://www.aepd.es/guias/gestion-riesgo-y-evaluacion-impacto-en-tratamientos-datos-personales.pdf ; EN: https://www.aepd.es/guides/risk-management-and-impact-assessment-in-processing-personal-data.pdf |
| 31 | Sweden (SE) | — |
