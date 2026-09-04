# Record-Keeping and Logging (Art. 12 EU AI Act)

## Purpose

This reference explains what providers of high-risk AI systems need to implement for record-keeping and logging to satisfy **Article 12** of the EU AI Act, and how deployers should handle access and operational use of logs.

This is a practical implementation note, not legal advice.

---

## 1. What Art. 12 requires (plain language)

For high-risk AI systems, the provider must ensure the system is designed and developed with **automatic logging capabilities** that enable traceability of the system’s operation throughout its lifecycle.

In practice, logs should allow you to answer:
- What input was processed?
- What output was produced?
- What version/model/config was active?
- What human oversight actions happened (override, approval, stop)?
- What errors, anomalies, or security events occurred?

---

## 2. Recommended risk-based logging fields, not a universal Article 12 minimum

Article 12(1) and (2) require automatic logging of events relevant to the system's intended purpose and appropriate across its lifetime. The specific minimum fields in Article 12(3) apply only to Annex III point 1(a) remote biometric identification systems. For other high-risk systems, select proportionate fields based on purpose, risk, traceability needs, data minimisation, privacy, and security.

Consider the following where relevant:

### System identity
- System name
- Unique system ID
- Provider legal entity
- Deployment environment (prod/staging)

### Versioning
- Model/version identifier
- Prompt/template version (if applicable)
- Rules/config version
- Release/build identifier

### Runtime events
- Timestamp (UTC) + timezone context
- Request ID / session ID
- Component calling the model

### Inputs and outputs (risk-based)
- Input category and metadata
- Output category and metadata
- If storing raw content is high-risk (privacy/confidentiality), store hashes or structured summaries instead

### Human oversight
- Human reviewer present? (yes/no)
- Intervention: override, stop, escalate
- Decision and rationale (short)

### Safety and security
- Policy violations / blocked requests
- System errors
- anomaly detection signals
- authentication/authorization events

---

## 3. Retention and access

- Define a retention period consistent with:
  - security incident investigation needs
  - legal hold requirements
  - data minimization and privacy requirements
- Ensure logs are access-controlled.
- Deployers should be able to access the logs needed for operating the system safely, consistent with instructions for use.

---

## 4. Common pitfalls

- Logs exist but are not tied to a specific model/version.
- Human oversight decisions are not recorded.
- Logs are stored but not reviewable or queryable.
- Retention is undefined.
- Logs contain unnecessary personal data.

---

## 5. Output suggestions

When asked to implement Art. 12, produce:
- a logging requirements list tailored to the system type
- an example log schema (JSON)
- a retention + access policy snippet
- a checklist for go-live readiness
