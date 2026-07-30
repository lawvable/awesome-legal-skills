# DPIA Risk Scoring Methodology

5×5 semi-quantitative risk assessment matrix. Risks are assessed from the **data subject's perspective** per Recital 75 GDPR, EDPB Guidelines WP 248 rev.01, and the EDPB DPIA Template v1.0 (March 2026).

---

## Likelihood Scale

| Score | Level | Anchor Description |
|-------|-------|--------------------|
| 1 | **Negligible** | Theoretically possible but no realistic scenario under current conditions. Extensive, proven safeguards in place. No known precedent in similar contexts. Would require extraordinary and unlikely combination of failures. |
| 2 | **Limited** | Unlikely under normal operating conditions. Would require an unusual combination of failures or deliberate, sophisticated attack. Safeguards exist but are not foolproof. Rare precedent in the sector. |
| 3 | **Moderate** | Could occur in foreseeable circumstances. Some precedent exists in similar processing contexts. Safeguards reduce but do not eliminate the possibility. Requires attention but not an immediate concern. |
| 4 | **Significant** | Likely to occur without additional safeguards. Has occurred in comparable contexts or organizations. Current controls are insufficient. Active threat vectors exist. |
| 5 | **Maximum** | Almost certain to occur or is inherent in the processing design. Would require affirmative countermeasures to prevent. Known, active exploitation in the sector. |

### Factors increasing likelihood
- Processing at scale (larger attack surface)
- Internet-connected systems vs. air-gapped
- Multiple data recipients, complex processor chains
- Novel technology with unproven security posture
- Weak or absent access controls / encryption
- Inadequate staff training or awareness
- History of incidents in the sector or organization
- High attractiveness of data to malicious actors
- Regulatory enforcement trend in this area

### Factors reducing likelihood (through mitigations)
- Strong encryption at rest and in transit with sound key management
- Effective pseudonymization with technically separated keys (EDPB 2025 Guidelines)
- Edge/local processing instead of cloud transmission (EDPB 1/2020)
- Robust access controls (RBAC/ABAC, MFA, privileged access management)
- Regular security testing, penetration testing, red teaming
- Staff training and security awareness programs
- Incident detection and response capabilities (SIEM, SOC)
- Data minimization practiced in reality, not just in policy

---

## Severity Scale (Impact on Data Subject)

| Score | Level | Anchor Description |
|-------|-------|--------------------|
| 1 | **Negligible** | Minor inconvenience the data subject can easily overcome. No lasting effect. Example: receiving unwanted marketing email, minor administrative annoyance. |
| 2 | **Limited** | Temporary difficulties the data subject can overcome with some effort. No permanent damage. Example: need to re-register for a service, minor financial cost (< €100), temporary anxiety. |
| 3 | **Significant** | Serious difficulties that can be overcome but with real effort, time, or cost. Example: blacklisting requiring dispute, financial cost (€100–€10,000), health concern requiring medical attention, employment difficulty. |
| 4 | **High** | Serious consequences that may be irreversible or very difficult to overcome. Example: long-term financial damage, job loss, health deterioration, relationship breakdown, significant psychological harm. |
| 5 | **Maximum** | Devastating, potentially irreversible consequences. Example: endangerment of life or physical safety, permanent financial ruin, severe discrimination with lasting social exclusion, loss of liberty. |

### Factors increasing severity
- Sensitivity of data (Art. 9 > financial > behavioral > basic contact)
- Vulnerability of data subjects (children, employees, patients)
- Irreversibility of harm (genetic disclosure, reputational damage)
- Power imbalance between controller and data subject
- Essential nature of affected service (banking, healthcare, housing, employment)
- Number of individuals affected (wider impact = higher aggregate severity)
- Difficulty of remediation for the individual
- Cascading effects (one harm enabling further harms)

### Factors reducing severity (through mitigations)
- Data minimization limits scope of potential harm
- Pseudonymization reduces identifiability
- Transparency enables informed decisions and protective action
- Effective rights mechanisms enable remediation
- Rapid breach notification enables protective measures
- Human oversight of automated decisions reduces error persistence
- Compensation or insurance mechanisms for financial harm

---

## Risk Level Matrix

Risk Score = Likelihood × Severity

|  | **Sev. 1** | **Sev. 2** | **Sev. 3** | **Sev. 4** | **Sev. 5** |
|---|:---:|:---:|:---:|:---:|:---:|
| **Lik. 5** | 5 Med | 10 High | 15 VHigh | 20 VHigh | 25 VHigh |
| **Lik. 4** | 4 Med | 8 High | 12 High | 16 VHigh | 20 VHigh |
| **Lik. 3** | 3 Low | 6 Med | 9 High | 12 High | 15 VHigh |
| **Lik. 2** | 2 Low | 4 Med | 6 Med | 8 High | 10 High |
| **Lik. 1** | 1 Low | 2 Low | 3 Low | 4 Med | 5 Med |

### Risk Level Thresholds

| Score Range | Level | Implication |
|-------------|-------|-------------|
| **1–3** | **Low** | Acceptable. Document and monitor. No specific action required beyond existing safeguards. |
| **4–6** | **Medium** | Action recommended. Implement additional safeguards. Monitor effectiveness. |
| **7–12** | **High** | Action required. Significant mitigation needed before processing can proceed. Document justification if residual risk remains at this level. |
| **13–25** | **Very High** | Processing may not be permissible without fundamental redesign. Art. 36 prior consultation with the SA is likely required if residual risk remains at this level after all feasible mitigations. |

**Acceptability caveat (EDPB 2026, fn. 9):** A risk may be deemed non-acceptable even at low likelihood if the potential severity is very high. Extremely serious consequences for data subjects can make a risk unacceptable regardless of how rarely the event is expected to occur.

---

## Modulating Factors

Modulating factors are characteristics that increase or decrease the likelihood or severity of a risk **without being the primary source of the corresponding threat** (EDPB Template 2026, §37). They adjust the baseline L×S score to reflect real-world context.

**Mechanism:** A modulating factor can shift the final risk level ±1 tier from the raw L×S score. This is not a formula multiplier — it is a documented, justified contextual adjustment.

### Aggravating factors (upward)
- Very large number of affected data subjects
- High data sensitivity (Art. 9 categories, financial, biometric)
- Data subjects in dependency or vulnerability (children, patients, workers, migrants)
- High exposure to external adversaries (public-facing systems, high-value targets)
- Cross-border processing increasing jurisdictional complexity

### Mitigating factors (downward)
- Effective design choices from Section 2.3 measures (encryption, access controls, pseudonymization)
- Narrow scope limiting blast radius
- Strong operational controls with demonstrated effectiveness
- Low attractiveness of data to adversaries

### Application
For each risk in the register, document applicable modulating factors and whether they warrant an adjustment. Most risks will not be adjusted — modulating factors are the exception, not the rule. Always justify: "Adjusted from High to Very High because data subjects are children in a dependency relationship with the controller."

---

## Two Risk Tracks

The EDPB 2026 template distinguishes two categories of risk. Both are assessed using the same L×S + modulating factors methodology and appear together in the risk register.

### Track A — Inherent-by-Design Risks

Risks that exist **when everything works exactly as designed and all actors follow the rules**. These flow from the personal data processed, the purpose, and the nature/scope/context of the processing.

Sources: data types collected, retention periods, scope of profiling, breadth of sharing, use of unique identifiers, algorithmic design choices.

Examples: linking risk from combining datasets, identification risk from data granularity, profiling bias inherent to algorithm design, disclosure risk from data sharing arrangements, inaccuracy from processing scope.

Maps to: EDPB Template Section 3.1 and most entries in `risk-catalog.md`.

### Track B — Operational Risks

Risks from **non-default, accidental, unlawful, or abnormal events** — when something deviates from the intended, compliant state.

Must identify at minimum three standard threat vectors:
1. **Illegitimate access** — unauthorized disclosure, exfiltration, insider abuse
2. **Undesired modification** — data corruption, injection, accidental overwrite
3. **Data disappearance** — deletion, ransomware, system failure, retention expiry error

Sources: software bugs, misconfigurations, wrong access rights, operational errors (wrong recipient, wrong dataset, forgotten de-provisioning), unpatched vulnerabilities, insider abuse, external attacks (phishing, ransomware).

Maps to: EDPB Template Section 4.1.a and Track B entries in `risk-catalog.md`.

### Combined Assessment

Both tracks feed into a single inherent risk assessment table (EDPB Section 4.1.c). Track labels in the risk register enable reviewers to distinguish design-inherent concerns from security/operational ones.

---

## Risk Register Format

| Risk ID | Track | Description | Rights Category | L | S | Score | Modulating Factors | Adjusted Level | Status |
|---------|-------|-------------|-----------------|---|---|-------|--------------------|----------------|--------|

- **Track:** A (inherent-by-design) or B (operational)
- **Modulating Factors:** Brief note of applicable aggravating/mitigating factors, or "—" if none
- **Adjusted Level:** Final risk level after modulating factor adjustment (Low / Medium / High / Very High)
- **Status:** For the residual risk register: implementation status of the corresponding mitigation (Planned / Partially Implemented / Implemented)

---

## DPIA Verdict

Four outcomes per EDPB 2026 template (Section 6):

| Verdict | Meaning |
|---------|---------|
| **APPROVED** | All residual risks are acceptable. No Art. 36(5) consultation requirement. Processing may proceed. |
| **CONDITIONALLY APPROVED** | Processing may proceed only after specified conditions are met. List each condition with a cross-reference to the relevant mitigation in the action plan. |
| **CONSULT SA** | Residual risk remains high despite all feasible mitigations (Art. 36(1)), or national law requires SA consultation/prior authorization (Art. 36(5)). Processing must not begin until SA response is received or the statutory period has elapsed. |
| **REJECTED** | Processing must be abandoned. Risks are unacceptable, required tests cannot be passed, or the DPO/SA has advised against proceeding. |

---

## Scoring Discipline

1. **Always justify scores with reference to the anchor descriptions.** "Likelihood 3 because precedent exists in the sector (X incident at comparable organization) and current access controls are standard but not hardened."

2. **Score inherent risk first, then re-score as residual risk after additional mitigations.** This shows the effect of safeguards and makes the DPIA defensible. Inherent risk assumes the baseline set of planned measures; residual risk reflects the level after additional mitigations have been applied.

3. **Mitigations primarily reduce likelihood.** Encryption, access controls, and pseudonymization reduce the probability of the risk materializing. They rarely reduce severity — if the risk does materialize despite safeguards, the impact on the data subject is often unchanged. Note: mitigations that are already part of the baseline design are reflected in the inherent risk score; only *additional* mitigations (Section 4.2) affect the residual risk score.

4. **Severity is largely inherent to the data and context.** The sensitivity of data, vulnerability of subjects, and nature of the service determine severity. Mitigations can sometimes reduce severity (e.g., data minimization means less data exposed if breached), but the effect is smaller than on likelihood.

5. **Be honest about uncertainty.** If scoring is genuinely difficult, give a range and explain: "Likelihood is between 2 and 3 depending on whether the cloud provider's supplementary measures are effective against government access requests."

6. **Avoid the "medium-medium" trap.** Untrained assessors default to the center of the matrix. Use the anchor descriptions to force honest calibration. A 3×3 should be justified, not a default.
