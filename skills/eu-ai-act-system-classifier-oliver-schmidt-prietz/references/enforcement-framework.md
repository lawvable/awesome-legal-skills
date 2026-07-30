# AI Act Penalty & Enforcement Framework

This reference provides the penalty structure, enforcement architecture, enforcement powers, and practical enforcement risk assessment under the EU AI Act (Regulation (EU) 2024/1689).

---

## 1. Penalty Tiers

### 1.1 Tiered Penalty Structure (Art. 99)

| Tier | Violation Type | Article | Maximum Fine | Maximum % Turnover | Applies To |
|------|---------------|---------|-------------|-------------------|------------|
| **Tier 1 (highest)** | Prohibited practices (Art. 5) | Art. 99(3) | EUR 35,000,000 | 7% global annual turnover | All actors |
| **Tier 2** | Non-compliance with high-risk requirements (Art. 8-17, Art. 25-27, Art. 50) + most other obligations | Art. 99(4) | EUR 15,000,000 | 3% global annual turnover | Providers, deployers, importers, distributors |
| **Tier 3** | Incorrect, incomplete, or misleading information to authorities | Art. 99(5) | EUR 7,500,000 | 1% global annual turnover | All actors |

**Calculation rule:** The **higher** of the fixed amount or the percentage of turnover applies (Art. 99(3)-(5)).

**Turnover basis:** Total worldwide annual turnover in the **preceding financial year** — not limited to EU revenue.

### 1.2 GPAI-Specific Penalties (Art. 101)

| Violation | Maximum Fine | Maximum % Turnover |
|-----------|-------------|-------------------|
| Non-compliance with GPAI obligations (Art. 53, 55) | EUR 15,000,000 | 3% global annual turnover |
| Incorrect or misleading information to AI Office | EUR 7,500,000 | 1% global annual turnover |
| Non-compliance with AI Office information requests | EUR 7,500,000 | 1% global annual turnover |

**Exclusive competence:** GPAI model penalties are imposed by the **AI Office** directly (not national authorities).

### 1.3 SME and Startup Proportionality (Art. 99(6))

| Organization Type | Proportionality Rule |
|-------------------|---------------------|
| SME (< 250 employees) | Fine must be proportionate to size, economic viability, and nature/gravity of infringement |
| Micro enterprise (< 10 employees) | Same proportionality, plus: if the percentage-based cap is lower than the fixed amount, the **lower** (percentage-based) amount applies |
| Startup | Same as micro enterprise — percentage cap applies when lower |

**Practical impact:** For a micro-enterprise with EUR 500,000 turnover:
- Tier 1: Max 7% = EUR 35,000 (vs. EUR 35M fixed → percentage cap applies)
- Tier 2: Max 3% = EUR 15,000 (vs. EUR 15M fixed → percentage cap applies)
- Tier 3: Max 1% = EUR 5,000 (vs. EUR 7.5M fixed → percentage cap applies)

### 1.4 EU Institutions and Bodies (Art. 100)

EDPS (European Data Protection Supervisor) has competence to impose penalties on EU institutions, bodies, offices, and agencies that violate the AI Act. Same penalty tiers apply up to EUR 1,500,000 (Art. 100(1)).

---

## 2. Enforcement Architecture

### 2.1 Multi-Level Enforcement Structure

```
┌─────────────────────────────────────────────────────┐
│                  EU LEVEL                             │
│                                                       │
│  AI Office (Art. 64)                                 │
│  ├── Exclusive: GPAI model enforcement               │
│  ├── Cross-border coordination                       │
│  ├── Systemic risk response                          │
│  └── Guidance and standards                          │
│                                                       │
│  AI Board (Art. 65)                                  │
│  └── Coordination of national authorities             │
└───────────────────────┬─────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────┐
│              MEMBER STATE LEVEL                       │
│                                                       │
│  Market Surveillance Authority (Art. 74)             │
│  ├── High-risk AI system enforcement                 │
│  ├── Market monitoring and product checks            │
│  ├── Corrective actions and penalties                │
│  └── EU database monitoring                          │
│                                                       │
│  Notifying Authority (Art. 28)                       │
│  └── Accreditation of conformity assessment bodies   │
│                                                       │
│  Sector Regulators (where applicable)                │
│  ├── Financial (BaFin, ACPR, DNB, etc.)             │
│  ├── Health (medical device authorities)             │
│  └── Transport, energy, telecom, etc.                │
│                                                       │
│  Data Protection Authorities                         │
│  └── GDPR enforcement overlapping with AI Act        │
└─────────────────────────────────────────────────────┘
```

### 2.2 Competence Distribution

| Actor/System | Primary Enforcement Authority | Secondary |
|-------------|------------------------------|-----------|
| GPAI model provider | AI Office (exclusive) | — |
| Provider of high-risk AI (Annex III) | National market surveillance authority | Sector regulator |
| Provider of high-risk AI (Annex I) | Sector-specific product safety authority | National market surveillance |
| Deployer of high-risk AI | National market surveillance authority | Labor inspectorate (for employment AI) |
| Importer/distributor | National market surveillance authority | — |
| Any actor violating Art. 5 | National market surveillance authority | AI Office (cross-border coordination) |
| Any actor processing personal data | National DPA (GDPR aspects) | National market surveillance (AI Act aspects) |

### 2.3 Relationship to GDPR Enforcement

**Dual enforcement reality:** Organizations deploying AI that processes personal data face potential enforcement from both AI Act authorities and data protection authorities.

| Aspect | AI Act Enforcement | GDPR Enforcement | Coordination |
|--------|-------------------|------------------|-------------|
| Authority | Market surveillance authority | Data protection authority | Art. 74(8) requires coordination |
| Focus | AI system compliance (safety, transparency, risk management) | Personal data processing (lawfulness, minimization, rights) | Overlapping areas: Art. 10 data governance, Art. 26(9) DPIA |
| Penalty | Up to EUR 35M / 7% | Up to EUR 20M / 4% (GDPR Art. 83) | No explicit ne bis in idem rule in AI Act |
| Right of complaint | Art. 85 | GDPR Art. 77 | Affected persons may complain to either or both |

**Double jeopardy consideration:** The AI Act does not contain an explicit prohibition on cumulative sanctions for the same conduct under both GDPR and AI Act. However, the general EU law principle of ne bis in idem and proportionality should prevent disproportionate double penalization. Art. 99(7) requires Member States to take GDPR penalties into account when setting AI Act penalties for the same infringement.

---

## 3. Enforcement Powers

### 3.1 Market Surveillance Tools (Art. 74-82)

| Power | Article | Description |
|-------|---------|-------------|
| **Information requests** | Art. 74(5) | Request documentation, data, information from any actor in the AI value chain |
| **Access to premises** | Art. 74(6) | Physical inspection of AI systems, source code, training data, testing environments |
| **Access to source code** | Art. 74(6) | When necessary to verify compliance — particularly for high-risk and prohibited practice investigations |
| **Testing and evaluation** | Art. 74(7) | Conduct tests on AI systems, including in real-world conditions |
| **Product sample** | Art. 74(8) | Acquire samples of AI systems for testing |
| **Mystery shopping** | Art. 74(10) | Test AI systems without disclosing authority status |

### 3.2 Corrective Actions

| Action | Article | Trigger |
|--------|---------|---------|
| **Compliance order** | Art. 79(1) | Non-compliance identified |
| **Product recall** | Art. 79(5) | Serious risk to health, safety, or fundamental rights |
| **Market withdrawal** | Art. 79(5) | Serious risk; system must be removed from EU market |
| **Prohibition** | Art. 79(6) | System cannot be made compliant; must be prohibited from market |
| **Public warning** | Art. 79(3) | Inform public about non-compliant AI system |
| **EU-wide action** | Art. 80-81 | Coordinated cross-border enforcement |

### 3.3 Systemic Risk Response (Art. 81-82)

For GPAI models with systemic risk:
- AI Office can require risk mitigation measures
- AI Office can restrict or suspend model availability
- Member States can take emergency measures for imminent serious risk
- Scientific Panel can issue qualified alerts

### 3.4 Right of Complaint and Redress (Art. 85)

| Right | Who | Against Whom |
|-------|-----|-------------|
| Complaint to market surveillance authority | Any natural or legal person | Any operator violating AI Act |
| Right to explanation for individual decisions | Affected persons | Deployers of high-risk AI (Art. 86) |
| Right to effective judicial remedy | Affected persons | Competent authorities (for inaction) |

---

## 4. Practical Enforcement Risk Assessment

### 4.1 Likelihood Factors

Factors that increase the likelihood of enforcement action:

| Factor | Risk Level | Reasoning |
|--------|-----------|-----------|
| **Sector visibility** | High risk: healthcare, financial services, law enforcement, employment | These sectors have active regulators already familiar with AI risks; complaints are more likely |
| **Consumer/citizen-facing system** | Higher risk than B2B-only systems | Direct interaction with natural persons generates complaints and visibility |
| **Complaint volume** | Each complaint creates a duty to investigate | Market surveillance authorities must respond to complaints (Art. 74(11)) |
| **Cross-border operation** | Increases likelihood of multi-authority attention | AI Office coordinates cross-border cases; multiple national authorities may investigate |
| **Media attention** | Significantly increases enforcement priority | Public interest cases receive prioritized investigation |
| **Data protection overlap** | DPA investigation may trigger parallel AI Act investigation | Coordination between DPA and market surveillance authority |
| **Existing regulatory relationship** | Regulated entities (banks, insurers) face higher scrutiny | Sector regulators already monitor these entities; AI adds additional compliance expectations |

### 4.2 Mitigating Factors

Factors that may reduce penalty severity:

| Factor | Impact | Legal Basis |
|--------|--------|------------|
| **Voluntary remediation** | Significant mitigation | Art. 99(8)(e): cooperation and remediation reduce penalty |
| **Compliance program** | Moderate mitigation | Demonstrates good faith effort; Art. 99(8)(d) considers organizational measures taken |
| **Cooperation with authorities** | Significant mitigation | Art. 99(8)(e): active cooperation explicitly considered |
| **Self-reporting** | Strong mitigation | Discovering and reporting own non-compliance before authority detection |
| **AI Pact participation** | Moderate mitigation (currently) | Demonstrates proactive commitment; no formal legal effect but practical persuasion value |
| **Codes of practice adoption** | Moderate mitigation | Art. 56: compliance with code of practice contributes to demonstrating compliance |
| **SME/startup status** | Proportionality applies | Art. 99(6): penalties must be proportionate to size and economic viability |
| **First offense** | May reduce severity | Art. 99(8)(c): previous infringements considered |
| **No actual harm** | May reduce severity | Art. 99(8)(b): nature, gravity, and duration of infringement |

### 4.3 Aggravating Factors

| Factor | Impact | Legal Basis |
|--------|--------|------------|
| **Intentional violation** | Maximum severity | Art. 99(8)(a): intentional or negligent character |
| **Repeat offense** | Increased severity | Art. 99(8)(c): previous infringements |
| **Failure to cooperate** | Increased severity + separate penalty | Art. 99(5): providing misleading information; Art. 99(8)(e) |
| **Vulnerable persons affected** | Increased severity | Art. 99(8)(b): gravity of infringement increased |
| **Large scale of impact** | Increased severity | Art. 99(8)(b): number of affected persons |
| **Continued non-compliance** | Ongoing penalty risk | Each day of non-compliance may constitute continued infringement |

### 4.4 Enforcement Risk Matrix

```
ENFORCEMENT RISK ASSESSMENT

                        Low Sector        High Sector
                        Visibility        Visibility
                    ┌─────────────────┬─────────────────┐
Consumer-facing     │    MEDIUM       │     HIGH        │
(B2C / citizens)    │ Standard        │ Priority        │
                    │ monitoring      │ enforcement     │
                    ├─────────────────┼─────────────────┤
Enterprise-only     │    LOW          │    MEDIUM       │
(B2B)               │ Reactive        │ Sector-driven   │
                    │ (complaint-     │ enforcement     │
                    │  driven)        │                 │
                    └─────────────────┴─────────────────┘

Cross-border operation: +1 risk level
Media attention: +1 risk level
Personal data processing: +1 risk level (DPA parallel)
```

### 4.5 Expected Enforcement Timeline

| Period | Expected Enforcement Focus |
|--------|--------------------------|
| **Now (2025-2027)** | Art. 5 prohibited practices (already enforceable); GPAI model compliance (enforceable since Aug 2025); AI literacy (Art. 4) |
| **Dec 2027-2028** | Phase 3 high-risk obligations (Annex III, Omnibus-postponed from Aug 2026): market surveillance ramp-up, first compliance checks, EU database completeness (per AI Omnibus 2026 postponement — verify current status via web search, as the Omnibus is legislative-in-progress) |
| **2028 onward** | Full enforcement across all tiers; product safety AI (Phase 4, Annex I, Omnibus-postponed to 2 Aug 2028); established case law from initial enforcement actions |
| **Ongoing** | GDPR-AI Act parallel enforcement; sector regulator coordination; cross-border coordination through AI Board |

**Early enforcement signals:** The AI Office has already demonstrated willingness to act on GPAI obligations. National DPA enforcement actions against AI systems (Clearview AI, ChatGPT) indicate aggressive enforcement appetite. Market surveillance authorities are building AI-specific expertise and capacity.
