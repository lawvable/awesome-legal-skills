# DACH-Specific Considerations — GPAI Compliance

Additional regulatory considerations for GPAI model providers and deployers operating in Germany, Austria, and Switzerland.

**Context:** The GPAI Code of Practice is an EU-level instrument. This reference file covers national-level overlaps, designated authorities, and practical considerations specific to the DACH region.

---

## Table of Contents

1. [Germany](#germany)
2. [Austria](#austria)
3. [Switzerland](#switzerland)
4. [Cross-Border Considerations](#cross-border-considerations)

---

## Germany

### Market Surveillance Authority: BNetzA

The **Bundesnetzagentur (BNetzA)** is designated as the market surveillance authority for AI in Germany, including GPAI model oversight.

#### Practical implications:
- BNetzA will be the first point of contact for German GPAI model providers
- The AI Office (EU level) remains the primary enforcer for GPAI obligations, but works through national authorities
- BNetzA may issue national guidance, priorities, or supplementary requirements
- German companies should monitor BNetzA publications for enforcement approach signals
- BNetzA has existing expertise from telecom and energy regulation — expect structured, process-oriented oversight

#### What to expect:
- Requests for information channelled through BNetzA
- BNetzA may request AI Office to investigate specific providers
- National competent authority role means BNetzA can request documentation via the AI Office (Article 53(1)(a))

### BSI (Bundesamt für Sicherheit in der Informationstechnik)

For systemic risk models, the **cybersecurity requirements** (Article 55(1)(d), Code Commitment 6) intersect with BSI standards:

#### IT-Grundschutz alignment:
- BSI IT-Grundschutz provides a structured cybersecurity framework widely used in Germany
- Organisations already certified to IT-Grundschutz have a strong foundation for meeting Commitment 6
- Map existing IT-Grundschutz controls to Code of Practice security mitigation requirements
- Gap analysis: IT-Grundschutz may not cover model-specific security (extraction attacks, adversarial robustness) — supplement accordingly

#### KRITIS (Critical Infrastructure):
- If GPAI models are deployed in critical infrastructure sectors, additional KRITIS obligations apply
- The 2-day serious incident reporting deadline (Code Commitment 9) aligns with KRITIS incident reporting timelines
- Double reporting may be required: AI Office + BSI (for KRITIS incidents)

### Works Council (BetrVG)

Internal deployment of GPAI models within German companies triggers works council considerations:

#### BetrVG §87(1) No. 6 — Co-determination:
- Applies when GPAI models are used to monitor employee performance or behaviour
- Works council has **mandatory co-determination rights** on introduction and use
- This applies even if the GPAI model provider is external — the deployer (employer) must involve the works council

#### Practical steps:
1. Assess whether any internal GPAI model use falls under §87(1) No. 6
2. Engage works council early — before deployment, not after
3. Draft a Betriebsvereinbarung (works agreement) covering:
   - Purpose and scope of GPAI model use
   - Data collected and processed
   - Employee access to information about AI-assisted decisions
   - Human oversight mechanisms
   - Complaint and escalation procedures
4. Document the assessment even if you conclude §87(1) No. 6 does not apply

#### Common pitfalls:
- Assuming "we're just using an API" exempts you from works council involvement — it does not
- Internal chatbots and productivity tools using GPAI models can trigger co-determination if they log usage data, generate performance insights, or monitor workflow patterns
- AI-assisted HR tools (summarisation, analysis) are high-risk for works council scrutiny
- "We don't monitor employees" — but does the GPAI tool's telemetry create a monitoring capability? If technically possible, §87(1) No. 6 may apply regardless of intent

#### Example: GPAI deployment triggering co-determination

A German company deploys an internal Copilot-style tool (built on GPT-4 or similar GPAI model) for its legal team. The tool logs prompts, generates usage analytics, and can identify who uses it how often. Even though the employer has no intention to use this data for performance evaluation, the **technical capability** to monitor employee behaviour triggers §87(1) No. 6. The works council must be involved before deployment. A Betriebsvereinbarung should cover: data minimisation for telemetry, prohibition of individual performance profiling, access controls on usage data, and a review clause.

### BaFin (Financial Services)

For GPAI models used in financial services:

#### MaRisk (Mindestanforderungen an das Risikomanagement):
- Model risk management requirements apply to AI/ML models used in risk, compliance, and decision-making
- GPAI models used for credit scoring, fraud detection, or risk assessment must be integrated into the existing model risk framework
- BAIT/VAIT overlay for IT governance and outsourcing

#### Explainability expectations:
- BaFin expects explainability for models affecting customer outcomes
- GPAI models (often opaque) may need additional wrapper/explanation layers
- Document the explainability approach as part of compliance

### BDSG and GDPR Overlay

- **BDSG §22** — processing of special categories of data has stricter requirements
- Automated individual decision-making (GDPR Art. 22) intersects with GPAI model outputs
- Data protection impact assessment (DPIA) may be required for GPAI model deployment
- Coordination with DPO recommended, especially for models processing personal data

---

## Austria

### Regulatory Landscape

#### Market surveillance:
- **RTR (Rundfunk und Telekom Regulierungs-GmbH)** expected to play a significant role
- Exact designation and scope still being finalised
- Austrian providers should monitor Federal Chancellery (BKA) and RTR communications

#### ArbVG §96a — Works Council:
- Austrian equivalent of German BetrVG co-determination
- Applies to systems that affect human dignity or monitor employees
- GPAI model deployments in the workplace likely trigger ArbVG consultation requirements
- Works council agreement required before deployment

#### DSB (Datenschutzbehörde):
- Austrian data protection authority
- GDPR enforcement, including AI-related processing
- Active on DPIA requirements for AI systems

### Practical differences from Germany:
- Smaller regulatory ecosystem — fewer specialised authorities
- Closer alignment with EU-level instruments (less national gold-plating)
- Austrian companies may have more direct engagement with AI Office rather than through national authorities initially

---

## Switzerland

### Territorial Scope

Switzerland is **not an EU/EEA member state** and the AI Act does not directly apply on Swiss territory. However:

#### When Swiss companies ARE subject to GPAI obligations:
- **Placing GPAI models on the EU market** — if a Swiss company makes a GPAI model available in the EU (via API, downloads, or through EU-based intermediaries), the AI Act applies to that model
- **EU-based users** — if the model's output is intended for use in the EU
- Swiss companies in this situation need an **authorised representative** in the EU (Article 54)

#### When Swiss companies are NOT subject:
- Models developed and used exclusively within Switzerland
- Research and development activities not resulting in EU market placement
- Models used solely by Swiss entities for Swiss operations

### Swiss Regulatory Framework

#### FINMA (Financial Market Supervisory Authority):
- May issue supplementary guidance for AI/ML models in financial services
- Swiss financial institutions using GPAI models for EU-facing services should consider both FINMA and EU AI Act requirements

#### nDSG (Neues Datenschutzgesetz):
- Swiss data protection law (effective September 2023)
- Independent from GDPR but substantially aligned
- Privacy impact assessments for high-risk processing (including AI)
- GPAI model providers processing Swiss personal data must comply with nDSG regardless of AI Act applicability

#### Sector-specific considerations:
- Swiss pharmaceutical companies using GPAI models may face Swissmedic + EU MDR dual oversight
- Swiss banks operating in the EU face FINMA + BaFin/other NCA requirements

### Practical guidance for Swiss companies:
1. **Map EU market exposure** — determine which models/services are EU-facing
2. **Appoint authorised representative** if placing models on EU market
3. **Comply with EU requirements** for EU-facing activities while maintaining Swiss compliance for domestic operations
4. **Monitor bilateral developments** — Switzerland and EU may negotiate AI-related agreements

---

## Cross-Border Considerations

### Multi-jurisdictional DACH deployments:

| Scenario | Applicable framework |
|----------|---------------------|
| German company, GPAI model on EU market | AI Act + Code of Practice + BNetzA oversight |
| Austrian company, GPAI model on EU market | AI Act + Code of Practice + RTR/TBD oversight |
| Swiss company, GPAI model on EU market | AI Act + Code of Practice + Authorised representative required |
| German company deploying US-built GPAI model internally | Works council (BetrVG), BDSG/GDPR, deployer obligations |
| DACH company fine-tuning a GPAI model | Provider status if modification is "significant" (>1/3 compute) |

### Common patterns in DACH:
- Many DACH companies are **deployers** (not providers) of GPAI models from US companies
- Deployer obligations differ from provider obligations but still exist
- Internal deployment triggers works council / employee representative body obligations
- Data protection overlay applies regardless of AI Act classification
- Sector-specific regulators (BaFin, BNetzA, BSI) may impose additional requirements beyond the AI Act

### Documentation language:
- AI Office communications are in English
- BNetzA may require German-language documentation for national proceedings
- Practical recommendation: maintain documentation in English with German translations available for key documents

---

*Source: Regulation (EU) 2024/1689; GPAI Code of Practice (Final Version, July 2025); BetrVG, ArbVG, UrhG, BDSG, nDSG, MaRisk.*
