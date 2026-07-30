# General-Purpose AI Code of Practice — Detailed Overview

Detailed overview of the GPAI Code of Practice structure, measures, and implementation guidance.

| Aspect | Detail |
|--------|--------|
| Institution | EU Artificial Intelligence Act (artificialintelligenceact.eu) |
| Date | 2025 |
| Source URL | https://artificialintelligenceact.eu/code-of-practice/ |
| NotebookLM Source ID | 9eacb0a4-... |

*German: Verhaltenskodex für KI-Modelle mit allgemeinem Verwendungszweck — Detaillierte Übersicht*

---

## Overview

The Code of Practice offers a clear framework to help developers of General Purpose AI (GPAI) models meet the requirements of the EU AI Act. While providers can choose to follow the Code, they are also free to demonstrate compliance through other appropriate methods.

The GPAI rules take effect on August 2, 2025, meaning all new models released from that date must comply. However, the Commission's enforcement actions -- such as requests for information, access to models, or model recalls -- will only begin a year later, on August 2, 2026. This grace period gives providers time to work with the AI Office to ensure they meet the standards.

For models released before August 2, 2025, providers have until August 2, 2027 to bring them into compliance.

## Executive Summary

### Transparency Chapter

Signatories commit to maintaining up-to-date, comprehensive documentation for every GPAI model distributed within the EU, except for models that are free, open-source, and pose no systemic risk. This documentation must follow a standardized Model Documentation Form, detailing licensing, technical specs, use cases, datasets, compute and energy usage, and more. It should be securely stored for at least ten years and made available, upon request, to the AI Office and downstream users. Public release of this information is encouraged to promote transparency.

### Copyright Chapter

This chapter ensures alignment with EU copyright law, especially the requirement for prior authorization unless specific exceptions apply (such as text and data mining). Signatories are required to develop and regularly update a robust copyright policy that clearly defines internal responsibilities and complies with legal standards. They must ensure that data collected via web crawling is lawfully accessible, respect machine-readable rights signals like robots.txt, and avoid accessing websites flagged for copyright infringement. Technical safeguards should minimize the generation of infringing content, and terms of service must clearly prohibit unauthorized use. A designated contact point must be provided for copyright holders to submit complaints, with efficient and fair processes for handling them.

### Safety and Security Chapter

This chapter sets out comprehensive obligations for developers of GPAI models with systemic risk to identify, assess, mitigate, and transparently report safety and security risks throughout the model's lifecycle. It establishes a risk governance framework focused on pre-market assessments, ongoing monitoring, and continuous oversight.

Signatories must develop a cutting-edge Safety and Security Framework before model release, outlining evaluation triggers, risk categories, mitigation strategies, forecasting methods, and organizational responsibilities. This framework should be regularly updated in response to new risks, incidents, or significant changes in the model or its environment.

Systemic risks are identified through structured processes such as inventories, scenario analysis, and consultation with internal and external experts. These risks are then analysed using rigorous evaluation methods including simulations, adversarial testing, and post-market surveillance.

Before progressing with development or deployment, signatories must evaluate whether identified risks are acceptable, applying defined risk-tier frameworks with built-in safety margins. If risks are deemed unacceptable, immediate corrective actions are required.

To maintain acceptable risk levels, safety measures must be integrated throughout the model's lifecycle, including filtering, continuous monitoring, refusal training, phased access controls, downstream tool safeguards, and secure deployment environments. Parallel security controls must prevent unauthorized access or misuse, employing strong digital and physical protections until the model is either publicly released or decommissioned.

A mandatory Safety and Security Model Report must be submitted prior to release and updated as risks evolve. This report should include detailed documentation on risk identification, analysis, mitigation efforts, model behaviour, external evaluations, and any material changes in the risk landscape.

Organizational accountability is key. Signatories must clearly assign oversight, ownership, monitoring, and assurance roles within their governance structures and ensure adequate resources, a strong risk culture, and protections for whistleblowers.

Serious incidents must be promptly tracked, documented, and reported to regulators according to severity and tight deadlines (for example, within 2 days for incidents affecting critical infrastructure). Reports must be regularly updated and kept for at least five years.

Finally, signatories are required to retain detailed records of safety and risk management activities for a minimum of ten years. High-level summaries of their safety frameworks and model reports should be published when needed to reduce risks, unless the model meets specific criteria qualifying it as "similarly safe or safer."

---

## Transparency Chapter (Detailed)

This chapter establishes clear expectations for how Signatories should meet their transparency duties under Article 53(1)(a)-(b) and Annexes XI and XII of the AI Act. The primary goal is to ensure critical information flows effectively to both downstream providers and the AI Office while preserving appropriate levels of confidentiality.

### Commitment 1: Documentation

Signatories pledge to:

- Keep comprehensive, current documentation for every model (Measure 1.1)
- Facilitate information sharing with the AI Office and downstream providers (Measure 1.2)
- Safeguard the accuracy, completeness, and protection of all documentation (Measure 1.3)

These commitments do not apply to free and open-source models, unless they are classified as a GPAI model with systemic risk.

#### Measure 1.1: Drawing up and keeping up-to-date model documentation

Before placing a GPAI model on the EU market, Signatories must prepare comprehensive documentation addressing all elements specified in the Model Documentation Form.

This documentation must remain current, reflecting any material changes, and be preserved for a minimum of 10 years after the model's initial release.

#### Measure 1.2: Providing relevant information

- Signatories must publicly provide contact details that allow the AI Office and downstream providers to request documentation access.
- When requested, they must deliver the latest documentation version to the AI Office within the designated timeframe.
- Downstream providers must receive necessary documentation -- along with any required clarifications -- within 14 days, barring legitimate reasons for delay.
- Public release of documentation is recommended as a means of enhancing overall transparency.

#### Measure 1.3: Ensuring quality, integrity, and security of information

Signatories bear responsibility for maintaining documentation that is precise, protected from unauthorized modification, and stored securely to demonstrate regulatory compliance.

### The Model Documentation Form

The form covers the following categories for regulatory and downstream use:

- Licensing and distribution
- Model identification (name, version, release date, entity)
- Technical specifications (architecture, size, I/O formats)
- Intended and approved use cases
- Integration dependencies (platforms, software/hardware)
- Training methodology and design rationale
- Dataset details (source, type, scope, volume, curation, bias mitigation)
- Energy and compute usage (training and inference)

---

## Copyright Chapter (Detailed)

This chapter facilitates adherence to Article 53(1)(c) of the AI Act, which mandates that providers establish copyright policies consistent with EU copyright and related rights legislation. While following these guidelines supports regulatory compliance efforts, it does not constitute a guarantee of full legal compliance, which ultimately depends on interpretations by national courts and the Court of Justice of the EU (CJEU).

European Union copyright law operates on the foundational principle that prior authorization is required for use of protected works, except where specific exceptions apply -- such as text and data mining (TDM) provisions under Article 4(1) of Directive (EU) 2019/790 -- and rights holders have not expressly reserved their rights.

### Commitment 1: Copyright Policy

Signatories undertake to establish, maintain, and execute a comprehensive copyright policy that applies to all GPAI models distributed within the EU. This policy must align with the standards outlined in this chapter.

However, adherence to these chapter requirements does not substitute for the fundamental obligation to comply with Union and national copyright legislation. Signatories retain full responsibility for ensuring their operations conform to applicable legal frameworks, including Article 4(3) of Directive (EU) 2019/790, prior to undertaking any copyright-relevant activities.

#### Measure 1.1: Draw up, keep up-to-date and implement a copyright policy

Signatories must develop and maintain a unified, regularly updated copyright policy that demonstrates compliance with this chapter's requirements and clearly defines internal accountability structures.

Publication of a policy summary is encouraged to enhance transparency and public understanding.

#### Measure 1.2: Reproduce and extract only lawfully accessible copyright-protected content when crawling the World Wide Web

- Web crawling systems deployed for training purposes must limit access to legally available content only.
- Circumventing technical barriers (such as paywalls or access restriction mechanisms) is forbidden.
- Providers must exclude websites that EU/EEA authorities have identified as persistent copyright violators, based on a publicly maintained EU-hosted registry.

#### Measure 1.3: Identify and comply with rights reservations when crawling the World Wide Web

- Crawling systems must possess the capability to recognize and honor machine-readable rights reservations, including robots.txt files, consistent with RFC 9309 standards.
- Providers must adhere to other broadly recognized and technically practical standards approved through EU-level consultations.
- Signatories are encouraged to actively participate in developing such technical protocols.
- They must provide transparency regarding their crawler operations, their approach to handling rights-reserved content, and offer automated notification systems for rights holders.
- Search engine operators must ensure that respecting rights reservations does not compromise their indexing capabilities.

#### Measure 1.4: Mitigate the risk of copyright-infringing outputs

- Providers must deploy technical protective measures designed to minimize the likelihood that AI models produce copyright-infringing content.
- They must explicitly prohibit infringing uses within their terms of service or documentation, including for open-source model distributions.
- These protective measures must remain effective whether the model is used directly or through third-party implementations.

#### Measure 1.5: Designate a point of contact and enable the lodging of complaints

- Signatories must establish a dedicated contact point for rights holders and implement a system for receiving substantiated electronic complaints.
- All complaints must receive fair consideration and timely responses, except those that are manifestly groundless or repetitive in nature.
- This complaint mechanism operates without prejudice to other legal remedies available to rights holders for protecting their interests.

---

## Safety and Security Chapter (Detailed)

### Commitment 1: Safety and Security Framework

Signatories pledge to establish a state-of-the-art Safety and Security Framework that defines comprehensive systemic risk management procedures and measures designed to maintain acceptable levels of systemic risk. This encompasses developing, implementing, and regularly updating the Framework while keeping the AI Office informed of all developments.

#### Measure 1.1: Creating the Framework

Signatories shall develop a Framework that documents both existing and planned processes for assessing and mitigating systemic risks. The Framework must encompass:

- Justified trigger points that determine when lighter-touch model evaluations should occur throughout the model lifecycle.
- For systemic risk acceptance (Commitment 4):
  - Clear criteria and rationale for establishing systemic risk categories and their practical application.
  - Comprehensive high-level mitigation strategies corresponding to each risk category.
  - Projected timelines indicating when models are anticipated to surpass the current highest risk tier, supported by detailed justification, underlying assumptions, and utilization of forecasting methodologies, expert surveys, or professional estimates.
- Clear description of how external guidance (including governmental input) influences development and deployment choices.
- Clear assignment of systemic risk management responsibilities (Commitment 8).
- Procedures for Framework updates and revisions.

Signatories must confirm the Framework within four weeks of notifying the Commission that their GPAI model meets the threshold to be classified as a GPAI model with systemic risk, and at minimum two weeks prior to market launch.

#### Measure 1.2: Implementing the Framework

Signatories shall maintain continuous systemic risk assessment through:

- Executing streamlined model evaluations (such as automated evaluations) at designated trigger points (established based on timeframes, computational training resources, development milestones, user accessibility, inference computing capacity, and/or affordances).
- Ongoing post-market monitoring.
- Incorporating intelligence from serious incident reports.
- Expanding assessment scope and intensity as circumstances warrant, or executing comprehensive systemic risk assessment and mitigation protocols based on evaluation results, post-market monitoring data, and serious incident intelligence.

They shall continuously deploy systemic risk mitigation measures that reflect the outcomes of assessments (model evaluations, post-market monitoring, and serious incident analysis).

They shall execute comprehensive systemic risk assessment and mitigation protocols involving:

1. Systematic identification of systemic risks.
2. Thorough analysis of each identified systemic risk.
3. Determination of systemic risk acceptability levels.
4. Implementation of mitigation measures and reassessment when risks prove unacceptable, followed by deployment of safety and/or security countermeasures, with the process cycling back to risk identification.

This process must be completed prior to market introduction. It must be repeated when:

- The reasonably predictable circumstances supporting the justification for acceptable systemic risk levels, including built-in safety margins, would cease to be valid.
- The model's application or integration within AI systems has experienced, or is projected to experience, substantial modification.

Signatories must provide comprehensive reporting of all measures and processes to the AI Office.

#### Measure 1.3: Updating the Framework

Signatories shall revise the Framework as necessary -- promptly following any assessment -- to ensure it remains current and maintains state-of-the-art standards. All updates must include comprehensive change documentation detailing the rationale, version identification, and implementation date.

Framework evaluations shall be conducted:

- At minimum annually following the model's market introduction; or
- Earlier, when reasonable evidence suggests that adequacy or compliance has been significantly compromised.

Triggering conditions include:

- Material changes that could foreseeably result in unacceptable systemic risks.
- Serious incidents or near-misses that demonstrate materialized systemic risks.
- Notable shifts in systemic risk profiles (including model capability evolution or declining mitigation effectiveness).

Evaluations examine:

- **Adequacy:** Whether Framework procedures and measures effectively address systemic risks.
- **Adherence:** Compliance with Framework requirements, explanations for any non-compliance, corrective actions taken, and -- where future non-compliance appears possible -- detailed remediation strategies.

#### Measure 1.4: Framework notifications

Signatories shall grant the AI Office complete, unredacted access to their Framework and all subsequent updates within five business days of final confirmation.

### Commitment 2: Systemic Risk Identification

Signatories pledge to identify systemic risks through a systematic methodology, including the creation of risk scenarios that inform systemic risk analysis and acceptance decisions.

#### Measure 2.1: Systemic risk identification process

Signatories shall identify systemic risks through:

- Creating a comprehensive inventory of potential risks (Appendix 1.1), drawing from model-agnostic sources, model-specific information (including post-market data and incident reports), and guidance from the AI Office, Scientific Panel, or International Network of AI Safety Institutes (where officially endorsed).
- Examining pertinent characteristics (Appendix 1.2) and sources (Appendix 1.3).
- Identifying systemic risks from this comprehensive analysis.
- Identifying risks catalogued in Appendix 1.4.

#### Measure 2.2: Systemic risk scenarios

Signatories shall construct detailed systemic risk scenarios, establishing the optimal quantity and granularity level for each identified systemic risk.

### Commitment 3: Systemic Risk Analysis

Signatories pledge to thoroughly examine each identified systemic risk to inform systemic risk acceptance decisions, encompassing the collection of model-independent information, execution of model evaluations, risk modelling, estimation activities, and ongoing monitoring of systemic risks.

#### Measure 3.1: Model-independent information

Signatories shall collect pertinent model-independent information through approaches including comprehensive literature reviews, market and training data analysis, incident pattern studies, trend projection, expert consultation, and public opinion research.

#### Measure 3.2: Model evaluations

Signatories shall execute cutting-edge evaluations across all relevant modalities to examine model capabilities, behavioural tendencies, operational features, and real-world impacts (Appendix 3).

Evaluations shall employ suitable methodologies, incorporate open-ended testing for emerging properties, and be guided by model-independent information. Approaches include: structured questioning, task-oriented assessment, standardized benchmarks, adversarial testing, human enhancement studies, model organism research, simulation exercises, and proxy evaluations for restricted content areas.

#### Measure 3.3: Systemic risk modelling

Signatories shall perform advanced systemic risk modelling, grounded in risk scenarios and informed by identified risks and comprehensive analysis.

#### Measure 3.4: Systemic risk estimation

Signatories shall calculate the likelihood and severity of potential harm using state-of-the-art methodologies. Estimations may be quantitative, semi-quantitative, or qualitative in nature, encompassing risk scoring systems, risk matrices, or probability distributions, and must incorporate identified risks, analytical findings, and serious incident data.

#### Measure 3.5: Post-market monitoring

Signatories shall establish comprehensive post-market surveillance systems to inform systemic risk determinations, Model Report updates, and timeline projections.

Monitoring activities shall evaluate model capabilities, propensities, affordances, and effects through methods including:

- End-user feedback collection, dedicated reporting channels, bug bounty programs, community-driven evaluations.
- Monitoring of code repositories and social media platforms, research support initiatives.
- Privacy-preserving data logging (including watermarking and provenance tracking).
- Monitoring violations of usage restrictions and resulting incidents.
- Tracking opaque model characteristics relevant to systemic risk assessment.

Signatories operating AI systems that incorporate their GPAI models must implement corresponding monitoring protocols for those systems.

To facilitate effective monitoring, Signatories shall provide sufficient numbers of independent external evaluators with complimentary access to the model's most advanced versions, including variants with minimal safety constraints, unless equivalently safe models are made available. Access mechanisms include API interfaces, on-premise installations, dedicated hardware provision, or public model distribution.

Signatories shall publish transparent evaluator selection standards and utilize evaluation outcomes solely for systemic risk assessment purposes. Evaluator inputs and outputs shall not be incorporated into model training processes without explicit consent.

Signatories shall refrain from legal or technical retaliation against evaluators conducting good-faith testing and publication activities, provided they:

- Maintain model availability without disruption.
- Handle sensitive data responsibly.
- Avoid creating public safety hazards.
- Refrain from coercive application of findings.
- Adhere to responsible disclosure protocols.

Such disclosure policies shall permit publication within 30 business days unless extended delays are warranted due to elevated systemic risk concerns.

Small and medium enterprises (SMEs) and small midcaps (SMCs) may seek AI Office assistance for monitoring activities.

### Commitment 4: Systemic Risk Acceptance Determination

Signatories pledge to establish clear systemic risk acceptance standards and determine whether systemic risks are acceptable prior to advancing with development activities, market introduction, or operational deployment.

#### Measure 4.1: Systemic risk acceptance criteria and acceptance determination

Signatories shall articulate and justify systemic risk acceptance criteria within their Framework documentation.

Criteria must include quantifiable risk tiers -- encompassing at least one category not yet achieved -- based on capabilities assessment, behavioural propensities, risk calculations, or alternative metrics.

They shall implement these categories with suitable safety margins to evaluate the acceptability of individual and aggregate systemic risks, considering risk identification and analysis outcomes.

Safety margins must account for:

- Uncertainties in systemic risk sources (such as post-assessment capability emergence).
- Assessment methodology limitations (including under-elicitation issues).
- Mitigation effectiveness vulnerabilities (such as circumvention risks).

#### Measure 4.2: Proceeding or not proceeding based on systemic risk acceptance determination

Signatories shall proceed with development and deployment only when systemic risks are determined to be acceptable.

When risks are or may imminently become unacceptable, they must implement suitable corrective actions, including usage restrictions, market withdrawal, enhanced mitigations, and comprehensive re-evaluation.

### Commitment 5: Safety Mitigations

Signatories pledge to deploy suitable safety mitigations throughout the model lifecycle to preserve acceptable systemic risk levels.

#### Measure 5.1: Appropriate safety mitigations

Mitigations must demonstrate resilience against adversarial attacks and align with the model's distribution strategy.

Implementation examples include:

- Comprehensive training data filtration.
- Real-time input and output monitoring.
- Behavioural modifications (including refusal training protocols).
- Phased model access deployment.
- Mitigation tools for downstream users.
- Quantitative safety guarantees.
- Secure agent ecosystems (including model identification, specialized protocols, incident response tools).
- Transparency enhancement tools (including chain-of-thought accessibility, mitigation durability assessment).

### Commitment 6: Security Mitigations

Signatories pledge to maintain robust cybersecurity measures throughout the model lifecycle to prevent risks arising from unauthorized release, access, or theft. Excludes models with capabilities lower than at least one model with parameters available for public download. Security measures remain in effect until model parameters are made publicly available or securely deleted.

#### Measure 6.1: Security Goal

Signatories shall establish a comprehensive Security Goal that identifies threat actors their mitigations are intended to protect against, informed by current and projected model capabilities.

#### Measure 6.2: Appropriate security mitigations

Signatories shall deploy security measures that align with their established Security Goal, incorporating those specified in Appendix 4.

Any departures from Appendix 4.1-4.5(a) must demonstrate equivalent protective outcomes. Implementation may be phased to correspond with model capability advancement.

### Commitment 7: Safety and Security Model Reports

Signatories pledge to prepare comprehensive Safety and Security Model Reports prior to market introduction, ensure they are updated, and provide timely notification to the AI Office. Reports may reference previous submissions and may encompass multiple models when appropriate. Small and medium enterprises (SMEs) and small midcaps (SMCs) may provide reduced detail levels.

#### Measure 7.1: Model description and behaviour

The Model Report must contain:

- A high-level description of the model's architecture, capabilities, propensities, affordances, and development methodology (including training approaches and data sources).
- Current and intended applications of the model.
- Available model variants and versions.
- Model specifications (including governing principles, principle hierarchy, refusal categories, system prompts).

#### Measure 7.2: Reasons for proceeding

The report must provide clear justification for why systemic risks are deemed acceptable, encompassing:

- Comprehensive rationale and incorporated safety margins.
- Reasonably foreseeable circumstances under which the justification might become invalid.
- Decision-making process details (including governmental input where applicable).

#### Measure 7.3: Documentation of systemic risk identification, analysis, and mitigation

The report must comprehensively document:

- Systemic risk identification and analysis outcomes, including:
  - Description of the systemic risk identification process.
  - Explanation of the uncertainties and assumptions on model usage and integration into AI systems.
  - Systemic risk modelling results summary.
  - Detailed description of systemic risks posed by the model, including evaluation procedures, tests and tasks performed during evaluations, scoring methods, capability elicitation process, evaluation score comparisons with human baselines, across model versions and evaluation settings.
  - Five randomly selected samples of inputs and outputs from each relevant model evaluation to support independent interpretation of evaluation results and systemic risk assessment. Trajectories that play a significant role in explaining systemic risk must be included. Additional random samples must be provided upon request by the AI Office.
  - Description of resources and access provided to internal model evaluation teams and independent external evaluators.
  - Where applicable, justification that the "safe reference model" and "similarly safe or safer model" criteria have been met.
- Description of all safety mitigations implemented; how they meet standards set out by Measure 5.1; and mitigation limitations.
- Description of the Security Goal (Measure 6.1); all security mitigations implemented; how they achieve the Security Goal, including alignment with international standards; and justification of how alternative approaches achieve the intended security objective if any security mitigations in Appendices 4.1-4.5(a) were not followed.
- High-level description of planned techniques and resources for model development over the next six months, including use of other AI systems; expected differences in capabilities and behaviour in future models; and planned new or significantly updated safety and security mitigations.

#### Measure 7.4: External reports

The report must incorporate:

- Hyperlinks or citations to reports from independent external evaluators (Appendix 3.5) and independent security reviewers (Appendix 4.5), while respecting confidentiality requirements and evaluator oversight.
- Justification when no external evaluator was engaged (per Appendix 3.5).
- Explanation of evaluator selection based on demonstrated qualifications.

#### Measure 7.5: Material changes to the systemic risk landscape

The report must describe significant alterations in the systemic risk environment resulting from model development or deployment, such as:

- Novel scaling relationships.
- Breakthrough architectural innovations.
- Enhanced or diminished mitigation effectiveness.
- New training methodologies that improve distributed training viability.

#### Measure 7.6: Model Report updates

Reports require updating when systemic risk acceptability justifications are materially undermined, including:

- Activation of specified trigger conditions (capability shifts, new integrations, serious incidents).
- Material changes in capabilities, propensities, or affordances due to additional post-training, integration with new tools, or increased inference compute.
- A material change in how the model is used or integrated into AI systems.
- Serious incidents or near misses involving the model or a similar model.
- Developments that either materially undermine the external validity of previously conducted model evaluations, significantly improve the state of the art in model evaluation, or otherwise indicate that the original systemic risk assessment is materially inaccurate.

Updates should be completed within a reasonable timeframe. Updates due to deliberate changes must be completed before the change is made available on the market.

For the most capable models currently on the market, the Signatory must provide the AI Office with an updated Model Report at least every six months, unless:

- There has been no material change in the model's capabilities, propensities, or affordances since the last report;
- The Signatory intends to release a more capable model within one month; or
- The model qualifies as "similarly safe or safer" under Appendix 2.2 for each systemic risk identified in accordance with Measure 2.1.

The updated Model Report must include updated content as specified in Measures 7.1 to 7.5, based on the most recent full systemic risk assessment and mitigation process, and a changelog describing what was updated, why the changes were made, the new version number, and the date of the update.

#### Measure 7.7: Model Report notifications

Reports must be delivered (unredacted except where restricted by national security legislation) by the time of market introduction.

Updates must be submitted within 5 business days of confirmation. A 15-day extension is permitted when:

- The AI Office determines the Signatory is operating in good faith; and
- An interim report is submitted without delay, containing justification for proceeding (Measure 7.2), and changes in systemic risk landscape (Measure 7.5).

### Commitment 8: Systemic Risk Responsibility Allocation

Signatories pledge to clearly assign responsibilities for managing systemic risks associated with their models across all levels of the organisation; allocate appropriate resources to the individuals or teams tasked with managing systemic risks; and foster a sound risk culture within the organisation.

#### Measure 8.1: Definition of clear responsibilities

- **Systemic risk oversight:** Oversight of systemic risk assessment and mitigation processes.
- **Systemic risk ownership:** Day-to-day management of systemic risks, including assessments, mitigation, and incident response.
- **Systemic risk support and monitoring:** Ongoing support for and monitoring of systemic risk processes.
- **Systemic risk assurance:** Providing internal and/or external assurance on the adequacy of risk management to the supervisory management body or equivalent independent body.

Responsibilities must be allocated appropriately to the Signatory's governance structure and complexity, including:

- Supervisory function of the management body (e.g. board, risk/audit committee);
- Executive function of the management body;
- Operational teams;
- Internal assurance providers (e.g. internal audit), if available;
- External assurance providers (e.g. third-party auditors), if available.

The Measure is presumed to be met if, proportionate to the model's systemic risks:

- Oversight is handled by a dedicated committee or independent body (e.g. risk/audit committee). For SMEs/SMCs, an individual in the supervisory function may suffice.
- Ownership is assigned to suitable executive-level individuals (e.g. Head of Research/Product), with cascading responsibility to operational managers.
- Support and Monitoring is assigned to executive members not directly involved in risk-generating business (e.g. CRO or VP of Safety). SMEs/SMCs must have at least one executive member responsible for this function.
- Assurance is led by a designated individual or function (e.g. Head of Internal Audit), with support from internal/external audits. For SMEs/SMCs, periodic supervisory assessment is required.

#### Measure 8.2: Allocation of appropriate resources

Signatories' management bodies must oversee and ensure the allocation of resources sufficient to support those assigned systemic risk responsibilities (per Measure 8.1), relative to the level of systemic risk. Types of resources include human resources, financial resources, access to information and knowledge, and computational resources.

#### Measure 8.3: Promotion of a healthy risk culture

- **Leadership tone:** Senior leadership communicates systemic risk frameworks clearly.
- **Open communication:** Staff can raise and challenge systemic risk decisions.
- **Independence and incentives:** Risk personnel are independent and incentivised to avoid under- or over-estimation of risk.
- **Staff awareness:** Surveys confirm awareness of risks and channels to raise concerns.
- **Effective reporting channels:** Reporting mechanisms are used and appropriately acted upon.
- **Whistleblower policy:** Workers are informed annually, and policies are publicly accessible.
- **Non-retaliation:** No adverse actions are taken against those who report systemic risks to authorities in good faith.

### Commitment 9: Serious Incident Reporting

Signatories pledge to systematically track, document, and report serious incidents involving their models to the AI Office and national competent authorities without unnecessary delay. Reports must include corrective measures and be proportionate to incident severity.

#### Measure 9.1: Methods for serious incident identification

To identify serious incidents, Signatories must:

- Apply the methods set out in Measure 3.5, including systematic post-market monitoring.
- Consult external sources, including police and media reports, social media content, academic research, and incident databases.
- Enable third-party reporting, by informing downstream providers, users, and other stakeholders of available direct reporting channels, and facilitating reporting to either the Signatory or directly to the AI Office and/or national authorities.

#### Measure 9.2: Relevant information for serious incident tracking, documentation, and reporting

Signatories must track, document, and report to the AI Office and, where applicable, to national competent authorities, at minimum and to the best of their knowledge, the following information (appropriately redacted to comply with Union data protection and other applicable laws):

1. Start and end dates (or best approximations) of the incident.
2. Description of resulting harm and the affected individuals or groups.
3. The causal chain of events.
4. Identification of the model involved.
5. Evidence of the model's involvement.
6. Measures taken or intended by the Signatory.
7. Recommendations for action by the AI Office or competent authorities.
8. Root cause analysis, including:
   - The model outputs that caused or contributed to the incident.
   - Inputs used.
   - Systemic mitigation failures or circumventions.
   - Patterns from post-market monitoring reasonably linked to the incident (e.g. near misses, anomaly trends).

If certain information is unavailable at the time of reporting, the report must record this explicitly. The level of detail must reflect the severity of the incident.

#### Measure 9.3: Reporting timelines

**Initial report** must include information in points (1)-(7) of Measure 9.2, submitted as follows:

- Disruption to critical infrastructure: within 2 days from awareness
- Serious cybersecurity breach (e.g. exfiltration, cyberattack): within 5 days from awareness
- Death of a person: within 10 days from awareness
- Serious harm to health, fundamental rights, property, or environment: within 15 days from awareness

Awareness includes both established and reasonably suspected involvement of the Signatory's model.

**Intermediate report:** Where an incident remains unresolved, Signatories must provide updated information, including additional details from Measure 9.2, at least every 4 weeks following submission of the initial report.

**Final report:** To be submitted no later than 60 days after the incident is resolved and must contain the full set of information required under Measure 9.2.

**Consolidated reporting:** If multiple similar serious incidents occur within a reporting window, they may be included in the same report as the first incident, provided individual reporting timelines are respected for that initial case.

#### Measure 9.4: Retention period

All documentation and relevant information gathered under this Measure must be retained for a minimum of five (5) years from the later of the date of documentation, or the date of the serious incident -- without prejudice to any applicable EU legal obligations regarding information retention.

### Commitment 10: Additional Documentation and Transparency

Signatories pledge to document their implementation of the Safety and Security Chapter and publish summarized versions of their Framework and Model Reports when necessary for systemic risk mitigation.

#### Measure 10.1: Additional documentation

**Core documentation to be maintained and provided upon request:**

Signatories must prepare and maintain the following records for provision to the AI Office upon request, ensuring that these documents remain up to date:

- A detailed description of the model's architecture.
- A detailed explanation of how the model is integrated into AI systems, including how software components build on or feed into each other, and their integration into the overall processing pipeline, insofar as known to the Signatory.
- A detailed account of model evaluations conducted under this Chapter, including evaluation strategies and evaluation results.
- A detailed description of safety mitigations implemented in accordance with Commitment 5.

This documentation must be retained for a minimum of ten (10) years after the relevant model is placed on the market.

**Additional records to support compliance with systemic risk measures:**

To evidence adherence to this Chapter upon request by the AI Office, Signatories are further required to track and maintain the following, where not already included in the above documentation:

- Processes, measures, and key decisions forming part of the Signatory's systemic risk assessment and mitigation efforts.
- Justifications for the selection of any particular best practice, state-of-the-art process or measure, or other innovative process or measure, if relied upon to demonstrate compliance with this Chapter.

The above information need not be compiled or stored in a single repository. It must, however, be retrievable and made available upon request by the AI Office.

#### Measure 10.2: Public transparency

Where necessary to assess and/or mitigate systemic risks, Signatories must publish (e.g., via their website) a summarised version of their framework (pursuant to Commitment 1) and Model Report(s) (pursuant to Commitment 7), including any updates thereof.

The published version must include high-level summaries of systemic risk assessment results, and high-level descriptions of safety and security mitigations implemented.

Any publication must exclude or redact information that would undermine the effectiveness of safety and/or security mitigations or compromise sensitive commercial information.

Publication is not required for:

- Frameworks -- if all models of the Signatory qualify as "similarly safe or safer models" under Appendix 2.2.
- Model Reports -- if the model in question qualifies as a "similarly safe or safer model" under Appendix 2.2.

---

## Appendix 1: Systemic Risks and Other Considerations

### Appendix 1.1: Types of Risks

To determine whether a systemic risk exists (as per Article 3(65) AI Act), risks are classified under five primary types, which may overlap:

1. Risks to public health
2. Risks to safety
3. Risks to public security
4. Risks to fundamental rights
5. Risks to society as a whole

Examples include threats to critical infrastructure, public mental health, freedom of expression, data privacy, economic security, the environment, and democracy. Specific risks such as disinformation, non-consensual intimate imagery (NCII), and child sexual abuse material (CSAM) are also covered.

### Appendix 1.2: Nature of Systemic Risks

#### Essential Characteristics

A risk is systemic when it:

- Is specific to high-impact AI capabilities,
- Has significant effects across the EU market, and
- Can scale through the AI value chain.

#### Contributing Characteristics

- **Capability- or reach-dependence:** Risk grows with model power or use.
- **High velocity:** Rapid onset, outpacing mitigations.
- **Cascading impact:** Triggers chain reactions.
- **Irreversibility:** Persistent or permanent harm.
- **Asymmetry:** Few actors can cause large-scale effects.

### Appendix 1.3: Sources of Systemic Risks

#### Model Capabilities

Risk may arise from functionalities such as:

- Offensive cyber or CBRN capabilities,
- Persuasive or deceptive interaction,
- Autonomy, self-replication, or planning,
- Tool use and control of physical systems,
- Self-reasoning and evasion of oversight.

#### Model Propensities

These refer to tendencies such as:

- Misalignment with human intent or values,
- Discriminatory bias, hallucinations, or lawlessness,
- Goal persistence or power-seeking,
- Collusion or conflict with other systems.

#### Model Affordances and Other Systemic Risk Sources

Systemic risk may also stem from:

- Access to powerful tools or infrastructure,
- Weak security, poor oversight, or misuse,
- Wide-scale deployment or user base,
- Vulnerabilities in release strategies,
- Inadequate explainability or transparency.

### Appendix 1.4: Specified Systemic Risks

The following are treated as specified systemic risks for the purpose of risk identification (Measure 2.1, point 2):

- **CBRN risk:** AI lowering barriers or increasing the impact of chemical, biological, radiological, or nuclear attacks.
- **Loss of control:** Human inability to modify or shut down models due to misalignment, autonomy, or resistance.
- **Cyber offence:** AI enabling advanced cyber-attacks, especially on critical infrastructure.
- **Harmful manipulation:** Strategic persuasion or deception targeting populations or decision-makers, potentially undermining democratic processes or fundamental rights.

---

## Appendix 2: Similarly Safe or Safer Models

### Appendix 2.1: Safe Reference Models

A model qualifies as a safe reference model in relation to a specific systemic risk if all of the following conditions are met:

- **Regulatory status:** The model was placed on the market before this Chapter's publication; or it has completed the full systemic risk assessment and mitigation process, and the AI Office has received its Model Report, with risks deemed acceptable.
- **Sufficient visibility:** The Signatory has full insight into the model's architecture, capabilities, tendencies, affordances, and mitigations. This is assumed for the Signatory's own models or where full technical access is granted (including model parameters).
- **No contrary evidence:** There are no other reasonable grounds to believe the model's systemic risks are not acceptable.

### Appendix 2.2: Similarly Safe or Safer Models

A model may be classified as similarly safe or safer in relation to a specific systemic risk when:

- **Risk comparison:** Following systemic risk identification, the Signatory does not reasonably foresee any materially different risk scenario compared to the safe reference model.
- **Benchmarking:** The model performs at or below the reference model on all relevant state-of-the-art, light-weight benchmarks, with only minor capability increases that do not materially elevate risk. Benchmarks must be conducted in accordance with established procedures (Measure 3.2).
- **Technical equivalence:** There are no known architectural or behavioural differences that would reasonably result in increased systemic risk. There are also no other reasonable grounds to believe risk is materially higher than the reference model.

Assessments in Appendix 2.2 points (2) and (3) and Appendix 2.1 point (2) must include appropriate safety margins to account for uncertainty, such as incomplete information or measurement error.

If a model previously used as a safe reference loses that status, the Signatory must act within six months to either identify a new safe reference model, or apply full regulatory obligations to the related model, including completion of all previously exempted or reduced elements of the systemic risk assessment process.

---

## Appendix 3: Model Evaluations

### Appendix 3.1: Rigorous Model Evaluations

All model evaluations must be carried out with a high level of scientific and technical rigour, ensuring:

- **Internal validity** (the results accurately reflect the tested scenario),
- **External validity** (results are generalisable to real-world use), and
- **Reproducibility** (independent replication is possible).

### Appendix 3.2: Model Elicitation

Evaluations must elicit the full capabilities, tendencies, and potential effects of the model using state-of-the-art techniques, designed to:

- Minimise under-elicitation (missing relevant behaviours),
- Prevent deception by the model during tests (e.g. sandbagging).

Techniques may include changes to compute access, prompt design, scaffolding, and fine-tuning.

Signatories must:

- Match the elicitation capabilities of potential misuse actors, and
- Reflect the expected context of use, including tools and integrations that are planned or already used for similar models.

### Appendix 3.3: Assessing Mitigation Effectiveness

Evaluations must test how well safety mitigations perform, especially when systemic risk acceptance depends on them. This includes:

- Whether mitigations work as intended,
- Whether they can be circumvented or subverted (e.g. by jailbreaking),
- Whether their effectiveness may degrade over time.

Testing must use state-of-the-art adversarial techniques to probe for vulnerabilities.

### Appendix 3.4: Qualified Evaluation Teams and Resources

Evaluations must be conducted by multi-disciplinary teams with both technical and domain expertise related to the specific systemic risk. Indicative qualifications include:

- A relevant PhD or peer-reviewed work,
- Experience in developing model evaluation methods,
- At least 3 years of relevant work or research experience.

Teams must be provided with:

- Sufficient access to the model, including internal components (e.g. logits, activations) and unmitigated versions where appropriate,
- Model information, including specifications and training data,
- Time (e.g. at least 20 business days for most tasks), and
- Resources, including compute, engineering support, and staffing.

Security concerns must be accounted for when granting access to sensitive model components.

### Appendix 3.5: Independent External Model Evaluations

In addition to internal reviews, Signatories must appoint qualified, independent external evaluators unless:

- The model is already deemed "similarly safe or safer" (Appendix 2.2), or
- Despite a good-faith effort (e.g. a 20-day public call), no suitable external evaluators can be identified.

Independent evaluators must:

- Have relevant domain and technical expertise,
- Follow strict security protocols, and
- Agree to protect commercially sensitive information.

They must be granted sufficient access, information, time, and resources, as outlined in Appendix 3.4. Signatories must not interfere with the integrity of external tests (e.g. by logging test data without permission).

Small and Medium Enterprises (SMEs/SMCs) may seek support from the AI Office to meet these requirements.

---

## Appendix 4: Security Mitigation Objectives and Measures

### Appendix 4.1: General Security Mitigations

Signatories must adopt baseline cybersecurity measures to protect against common threats. These include:

- **Network access control:** Identity and access management (e.g. MFA, strong passwords, zero trust architecture, wireless security equal to wired, guest network isolation).
- **Social engineering protection:** Email filtering to detect phishing and suspicious attachments.
- **Malware and removable media:** Policies restricting the use of USBs and similar devices.
- **Software security:** Regular software updates and patch management to prevent exploits.

### Appendix 4.2: Protection of Unreleased Model Parameters

To safeguard sensitive model data, Signatories must:

- **Track all stored copies:** Maintain a secure registry of devices/locations holding model parameters.
- **Restrict copying to unmanaged devices:** Enforce access controls and monitor for unauthorized data transfer.
- **Encrypt parameters in transit and at rest:** Use 256-bit encryption and secure key storage (e.g. TPM).
- **Secure temporary storage:** Decrypt parameters only in non-persistent memory for legitimate use.
- **Secure parameters in use:** Deploy confidential computing techniques such as attested trusted execution environments.
- **Control physical access:** Limit access to sensitive environments (e.g. data centres) and perform inspections for unauthorised presence or devices.

### Appendix 4.3: Hardening Interface-Access to Unreleased Model Parameters

Signatories must harden all interfaces that access unreleased model parameters:

- **Limit interface access:** Restrict access to authorised users/software with MFA and review permissions at least every 6 months.
- **Secure interface code:** Perform in-depth manual or automated security reviews of code linked to model parameter access.
- **Prevent exfiltration:** Apply methods such as output rate limiting on interfaces.
- **Minimise insider access:** Limit who can access non-hardened interfaces with model parameters.

### Appendix 4.4: Insider Threats

To protect against sabotage or internal theft (including by or through models):

- **Personnel vetting:** Conduct background checks on those with access to sensitive model data/systems.
- **Insider threat awareness:** Train staff to recognise and report insider threats.
- **Prevent self-exfiltration by models:** Use sandboxing and code execution isolation.
- **Safeguard model training:** Inspect training data for tampering or sabotage.

### Appendix 4.5: Security Assurance

To verify that security measures are effective, Signatories must:

- Use independent external reviews if internal capacity is insufficient.
- Conduct red-teaming to identify security gaps in networks and facilities.
- Run bug bounty programs for public-facing endpoints where appropriate.
- Test insider mitigation protocols, including personnel integrity assessments.
- Facilitate issue reporting through secure third-party communication channels.
- Monitor systems actively with Endpoint Detection and Response (EDR) or Intrusion Detection Systems (IDS).
- Respond rapidly to threats using trained security teams for incident handling and recovery.
