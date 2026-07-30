# Sectoral lex specialis gate

This gate is warn-only. The Data Act is horizontal: it applies across sectors. Many sectors have their own Union law instruments that overlay the Data Act with sector-specific obligations, access rights, or carve-outs. The skill recognises when a scenario falls within a sectoral overlay, names the relevant instruments, gives the horizontal Data Act answer, and directs the user to specialist counsel or Commission sectoral guidance for the sectoral piece.

The gate does not produce sectoral analysis. Doing so would require deep knowledge of sectoral law that this skill does not have. A general Data Act skill that opines on, for example, type-approval data access under Regulation (EU) 2018/858 or DORA's third-party risk requirements without sectoral expertise produces wrong answers. The gate's job is to detect, flag, and redirect.

---

## When the gate applies

The gate runs whenever the scenario involves any of:

- A regulated product (vehicle, medical device, financial service, energy product, AI system, cybersecurity-relevant product)
- A regulated activity (banking, insurance, market infrastructure, critical infrastructure operation, public-sector procurement)
- A regulated sector (automotive, healthcare, financial services, energy, agriculture, telecommunications, aviation, maritime, rail)
- A regulated entity (NIS2 essential or important entity, DORA financial entity, CRA manufacturer of products with digital elements, AI Act provider or deployer of high-risk AI)

When in doubt, the skill runs the gate. The cost of a missed sectoral overlay is high (wrong analysis); the cost of a redundant flag is low (one extra paragraph in the output).

---

## How the skill runs the gate

Operational steps:

1. **Detect the sector.** Identify whether the connected product, related service, data processing service, or covered activity falls within a sectoral instrument. Use the catalogue below as the trigger list.

2. **Name the relevant instrument(s).** Cite the Union law instrument by full reference on first mention. Sectoral instruments are typically Regulations or Directives; identify which.

3. **Run the horizontal Data Act analysis.** Produce the Data Act answer using the seven-step method. The horizontal rules apply regardless of the sectoral overlay; the sectoral instrument typically adds requirements or carve-outs, it does not replace the Data Act analysis.

4. **Flag the sectoral overlay in the output.** State that the sector has specific Union law that may impose additional obligations, grant additional access rights, or carve out specific data categories. Do not opine on what the sectoral overlay requires.

5. **Recommend the next step.** This is typically one of: consult specialist counsel for the sector; consult the Commission's sectoral guidance (e.g. Commission Vehicle Data Guidance, EBA/ESMA/EIOPA technical standards under DORA); or check the sector's competent authority for sectoral interpretations.

6. **Where the user has already provided sectoral facts, integrate them but do not extend.** If the user states "the data is subject to Article 61 of Regulation (EU) 2018/858", the skill notes this and works with it, but does not analyse Article 61 itself unless the user has provided the analysis. The skill respects the boundary of its competence.

---

## What the skill does not do

The skill does not:

- Analyse type-approval data access rights under Regulation (EU) 2018/858 or Regulation (EU) 2019/2144
- Apply MDR or IVDR data access provisions, post-market surveillance obligations, or UDI database rules
- Apply DORA third-party risk management, incident reporting, or critical-services classification
- Apply NIS2 covered-entity obligations, incident reporting, or cooperation group requirements
- Apply CRA vulnerability handling, conformity assessment, or post-market obligations
- Apply AI Act high-risk classification, technical documentation, or transparency requirements
- Apply eIDAS qualified trust services or Digital Identity Wallet rules
- Apply Clean Energy Package smart meter data rules or energy network code requirements
- Apply CAP-derived agricultural data sharing rules or the Code of Conduct on agricultural data sharing

In each case, the gate identifies the overlay and directs the user onward. The Data Act analysis stops at the boundary.

---

## Sector catalogue

The catalogue lists the sectors and instruments the skill recognises. It is not exhaustive; new sectoral instruments are adopted regularly. The skill flags any sector that has dedicated Union law on data access, processing, or product safety, even if not enumerated here.

### Automotive

- **Regulation (EU) 2018/858** on the approval and market surveillance of motor vehicles, their trailers and systems, components and separate technical units. Establishes type-approval framework, vehicle identification, and certain access rights for repairers and independent operators (vehicle on-board diagnostic information, repair and maintenance information).
- **Regulation (EU) 2019/2144** on type-approval requirements for the general safety of motor vehicles. Includes event data recorder requirements, driver monitoring, and other safety-relevant data systems.
- **Commission Guidance on Vehicle Data accompanying the Data Act.** Sectoral interpretive guidance on how the Data Act applies to vehicle data. Pointer at `sources/vehicle-data-guidance-pointer.md`.

The vehicle-data debate has been active for over a decade (Extended Vehicle data, in-vehicle access, repairer/independent-operator access). The horizontal Data Act answer rarely captures the full sectoral picture. The skill always recommends specialist automotive counsel for any deliverable that will reach a vehicle data-sharing decision or contract.

### Medical devices and in-vitro diagnostics

- **Regulation (EU) 2017/745** on medical devices (MDR). Establishes the Medical Devices Coordination Group, UDI database (EUDAMED), post-market surveillance, and vigilance reporting obligations.
- **Regulation (EU) 2017/746** on in-vitro diagnostic medical devices (IVDR). Parallel regime for IVDs.

Connected medical devices generate data that may fall within both Data Act Ch II (user access) and MDR/IVDR (post-market surveillance, vigilance). The interaction between user data access rights under the Data Act and patient safety obligations under MDR/IVDR is not fully settled. The skill flags the MDR/IVDR overlay for any medical device scenario and recommends specialist medical devices counsel.

### Financial services

- **Regulation (EU) 2022/2554** on digital operational resilience for the financial sector (DORA). Governs ICT third-party risk management, incident reporting, digital operational resilience testing, and oversight of critical ICT third-party service providers. Applicable to financial entities (credit institutions, investment firms, payment institutions, insurance undertakings, etc.).
- **Regulation (EU) 2016/679** governs personal data of financial customers (no sectoral lex specialis here, but worth noting that financial services have layered confidentiality regimes under national law and the Capital Requirements Regulation).
- **Payment Services Directive 2 (PSD2)** and the proposed Payment Services Regulation (PSR) plus Financial Data Access (FIDA) framework. Sector-specific data access rights for payment account data and certain other financial data.

The interaction between Data Act Ch VI (cloud switching) and DORA's ICT third-party risk requirements is particularly important: financial entities switching cloud providers must comply with both regimes simultaneously. The skill flags the DORA overlay for any financial-services cloud switching scenario.

### Cybersecurity

- **Directive (EU) 2022/2555** (NIS2). Establishes covered entity categories (essential and important entities), incident reporting requirements, and risk management measures across critical sectors. Sectors include energy, transport, banking, financial market infrastructure, health, drinking water, wastewater, digital infrastructure, ICT service management, public administration, space, postal and courier services, waste management, manufacture/production/distribution of chemicals, food, manufacturing, digital providers, and research.
- **Regulation (EU) 2024/2847** (Cyber Resilience Act, CRA). Governs cybersecurity requirements for products with digital elements, including vulnerability handling, conformity assessment, and post-market obligations.

NIS2 overlay matters for any covered entity's data processing activities and incident reporting. CRA overlay matters for any manufacturer of products with digital elements, including most connected products. The skill flags both for cybersecurity-relevant scenarios.

### AI systems

- **Regulation (EU) 2024/1689** (AI Act). Governs prohibited AI practices, high-risk AI systems, general-purpose AI models, and AI literacy. Applicable to providers, deployers, importers, and distributors of AI systems. Phased application: prohibited practices from 2 February 2025; general-purpose AI rules from 2 August 2025; high-risk AI rules from 2 August 2026 (or 2 August 2027 for certain categories).

AI systems often process data that also falls within the Data Act (e.g. data from connected products fed into an AI model). The AI Act adds requirements on data quality, training data documentation, technical documentation, and transparency. The skill flags the AI Act overlay for any scenario involving AI systems and recommends specialist AI counsel.

### Digital identity

- **Regulation (EU) 910/2014** (eIDAS) as amended by Regulation (EU) 2024/1183. Governs qualified trust services and, after the 2024 amendment, the European Digital Identity Wallet.

eIDAS becomes relevant for Data Act scenarios where user identification is performed via the EU Digital Identity Wallet, or where data access requires qualified electronic signatures or seals. Recital 30 of the Data Act mentions the Wallet as a possible solution for user identification.

### Energy

- **Clean Energy Package** (multiple instruments). Includes Directive (EU) 2019/944 on common rules for the internal market for electricity, Regulation (EU) 2019/943 on the internal market for electricity, Directive (EU) 2018/2001 on the promotion of the use of energy from renewable sources, and others.
- **Smart meter data** is governed by national implementing rules under the Clean Energy Package, with EU-level guidance on data access for energy services.
- **Network codes and guidelines** under Regulation (EU) 2019/943 establish specific data exchange and access rules for the electricity sector.

Energy sector data scenarios (smart meter data access, demand response, distributed generation) involve dense sector-specific rules. The skill flags the energy overlay and recommends specialist energy counsel.

### Agriculture

- **Common Agricultural Policy regulations** (Regulation (EU) 2021/2115 and related instruments). Govern agricultural data collection, monitoring, and IACS (Integrated Administration and Control System).
- **EU Code of Conduct on agricultural data sharing by contractual agreement.** Industry self-regulatory instrument referenced in Data Act Recital 27. Not binding but the dominant practice norm in the sector.

Agriculture has been a particular focus of the Data Act's drafters (Recital 27 explicitly addresses agricultural data). The horizontal Data Act applies, but the Code of Conduct and CAP regulations layer significant sectoral practice on top.

### Other sectoral hotspots

The catalogue is open-ended. Sectors that have or are developing sector-specific data access rules include:

- **Aviation.** Regulation (EU) 2018/1139 (EASA Regulation) and related implementing rules on aircraft operational data, flight data recorders.
- **Maritime.** Various instruments under the IMO and EU maritime safety framework on vessel data.
- **Rail.** Regulation (EU) 2016/796 on the European Union Agency for Railways and related interoperability requirements for rail data.
- **Telecommunications.** Directive (EU) 2018/1972 (European Electronic Communications Code) and related instruments on traffic data, location data, and confidentiality of communications.

When a scenario touches any of these, the skill flags the sectoral overlay and recommends specialist counsel.

---

## What the skill produces in the output

When the gate is run, the output includes a dedicated "Sectoral overlay" section or paragraph. Minimum content:

- The sector identified.
- The relevant Union law instrument(s), cited in full.
- A statement that the sectoral overlay may impose additional obligations, grant additional access rights, or carve out specific data categories that the horizontal Data Act analysis does not capture.
- A clear redirection: consult specialist counsel for the sector, or consult Commission sectoral guidance where available.
- The horizontal Data Act conclusion stands, but is qualified by the sectoral overlay.

Sample phrasing the skill may use:

> Sectoral overlay: this matter falls within the scope of [instrument], which establishes [general nature of obligation]. The Data Act analysis above gives the horizontal position. The sectoral instrument may impose additional or different requirements, including in respect of [specific area]. The user should consult specialist [sector] counsel before relying on this analysis for a contract, deliverable, or product decision.

The phrasing is calibrated. The skill does not say "the sectoral overlay does not apply" unless it has actively confirmed that. The skill does not say "the sectoral overlay overrides the Data Act" unless it can cite the specific lex specialis rule that does so.

---

## Article 44 framing

Art. 44(1) provides that data-sharing obligations contained in Union legal acts that entered into force on or before 11 January 2024 (the Data Act's entry into force) remain unaffected. This is the regulation's own lex specialis acknowledgement. Sectoral data-sharing rules that pre-date 11 January 2024 prevail.

Art. 44(2) permits sector-specific legislation to complement the Data Act with practical and technical modalities or specific limits on data-holder access rights. The interaction is intended to be additive (sectoral law adds requirements) rather than displacive (sectoral law replaces the Data Act).

FAQ Q3 elaborates: between 11 January 2024 and 12 September 2025, "best efforts should be made to ensure alignment, but there is no legal obligation to do so." After 12 September 2025, Art. 44(2) governs the relationship. Sectoral legislation introduced after 12 September 2025 should be consistent with Data Act principles "to the greatest extent possible".

The skill cites Art. 44 when explaining the relationship between the Data Act and a sectoral instrument. The relationship is structural; it is not a matter of "which one wins."

---

## Cross-references

- `references/gotchas.md` does not currently have a sectoral-specific entry. The skill checks sectoral overlay through this gate rather than through the gotcha catalogue.
- `sources/vehicle-data-guidance-pointer.md` is the dedicated pointer for the automotive sector. Future sectoral guidance from the Commission should be added as parallel pointer files.
- `sources/regulation-2023-2854.md` Art. 44 (relationship with other Union legal acts), Recital 115 (sectoral rules without prejudice).
- `sources/faq-v1-4.md` FAQ Q3 (interaction with other EU legislation).
- The Commission's Data Act Legal Helpdesk (https://digital-strategy.ec.europa.eu/en/policies/data-act-legal-helpdesk) is the channel for sector-specific Commission interpretations that go beyond the FAQ. The skill may recommend the Helpdesk for edge cases.
