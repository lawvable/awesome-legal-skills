# Corrective Measures and Investigation Duties

This reference covers what providers and deployers should do once a serious incident is suspected or confirmed.

## 1. Provider Duties Under Article 73(6)

After reporting a serious incident, the provider must, **without delay**:

- perform the necessary investigations
- assess the risks related to the incident and system
- take corrective action
- cooperate with the competent authorities
- where relevant, cooperate with the notified body

The provider must also avoid altering the AI system in a way that may affect subsequent evaluation of the causes of the incident before informing the competent authorities.

## 2. Immediate Provider Actions

### Containment
- suspend affected deployment where appropriate
- disable risky functionality
- tighten thresholds / require mandatory human review
- issue customer/deployer safety notice
- stop new rollouts if the issue may be systemic

### Evidence preservation
- preserve logs
- preserve prompts, outputs, settings, weights/version references where relevant
- preserve model card / instructions for use / technical documentation snapshots
- preserve incident tickets, customer reports, and communications

### Investigation set-up
- appoint a single incident lead
- document the known timeline
- open a legal privilege strategy where appropriate
- identify whether third-party vendors or integrators are involved

## 3. Good Investigation Questions

- What exactly failed: model, rules, data, UX, threshold, integration, or human oversight?
- Was the incident foreseeable from existing complaints or monitoring signals?
- Did instructions for use sufficiently warn deployers?
- Did the deployer use the system in accordance with instructions?
- Was the incident isolated or indicative of a broader field issue?
- Does the same failure mode exist in other customers, languages, markets, or versions?
- Do we need a correction, recall, withdrawal, or temporary stop-use notice?

## 4. Deployer Duties Under Article 26(5)

Deployers must monitor the operation of the high-risk AI system based on the instructions for use.

If they have reason to consider the system may present a risk:

- inform the provider or distributor and relevant market surveillance authority without undue delay
- suspend use of the system

If they identify a **serious incident**:

- immediately inform **first the provider**
- then the importer or distributor and the relevant market surveillance authority
- if unable to reach the provider, apply Article 73 mutatis mutandis

### Log retention
Under **Article 26(6)**, deployers must keep automatically generated logs under their control for an appropriate period of at least six months, unless other law provides otherwise.

## 5. Internal Escalation Matrix

### Legal / Compliance
- qualification under Article 73
- authority routing
- privilege and documentation discipline
- overlap with GDPR / NIS2 / MDR / contract notice

### Product / Engineering
- technical root-cause analysis
- rollback / patch / feature flag / kill switch
- version mapping
- population impact analysis

### Security / IT
- evidence preservation
- access and integrity checks
- possible cyber incident qualification
- logging completeness

### Customer / Operations
- deployer outreach
- user advisories
- script for inbound customer questions
- training or temporary operating restrictions

### HR / Labour / Works Council
- employee-impact analysis
- workplace information duties
- works-council communications where relevant

## 6. Typical Corrective Measures

- software patch or model update
- rollback to earlier validated version
- revised instructions for use
- narrower intended use / deployment restriction
- stronger human-oversight controls
- training for deployers/users
- disabling of unsafe integration paths
- temporary suspension pending re-validation

## 7. What Not to Do

- do not wait for perfect certainty before preserving evidence
- do not quietly hotfix a possibly reportable incident without a documented legal decision
- do not let sales/customer-success teams make ad hoc causation statements to customers
- do not assume deployer misuse ends the analysis
- do not overwrite logs or lose model/version traceability

## 8. Output Phrases for Action Plans

- **Suspend use pending investigation**
- **Preserve logs and deployment state immediately**
- **Issue deployer advisory today**
- **Prepare initial incomplete report now; supplement after root-cause analysis**
- **Assess field-wide corrective action across all comparable deployments**
