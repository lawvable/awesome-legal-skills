# Consent Notice / Cookie Banner Template

## Legal Basis
Art. 7 (conditions for consent), Art. 4(11) (definition of consent), Recitals 32, 42–43.
ePrivacy Directive Art. 5(3) additionally applies to cookies/device storage.

---

## Consent Requirements Checklist (Art. 7)
- [ ] **Freely given**: No bundling with service terms; genuine choice with no detriment (Art. 7(4))
- [ ] **Specific**: Separate consent for each distinct purpose (Recital 43)
- [ ] **Informed**: Clear plain-language explanation before consent given
- [ ] **Unambiguous**: Affirmative act required — no pre-ticked boxes (Recital 32)
- [ ] **Withdrawable**: "As easy to withdraw as to give" (Art. 7(3)); withdrawal does not affect prior processing
- [ ] **Documented**: Record of when, how, and what consented to (Art. 7(1))
- [ ] **Age verified**: Under-16 requires parental consent (Art. 8; check Member State derogation 13–16)

---

## Cookie Banner — Required Elements

### Layer 1 (Initial Banner)
```
We use cookies to [improve your experience / personalise content / analyse traffic].
[ACCEPT ALL]   [REJECT ALL]   [MANAGE PREFERENCES]

[Link to Cookie Policy]
```

**Critical**: "Accept" and "Reject" must be equally prominent. Dark patterns (hiding reject,
pre-selected toggles) violate Art. 7 and Art. 5(1)(a) (fairness).

### Layer 2 (Preference Centre)
Group cookies by purpose; each requires a separate opt-in toggle defaulting to OFF:
| Category | Description | Default |
|----------|-------------|---------|
| Strictly Necessary | Required for site function — no consent needed | Always ON |
| Analytics | [Provider, purpose] | OFF |
| Marketing | [Provider, purpose] | OFF |
| Personalisation | [Provider, purpose] | OFF |

### Consent Record to Store
```json
{
  "userId": "...",
  "consentTimestamp": "ISO-8601",
  "consentVersion": "v1.2",
  "purposes": {
    "analytics": true,
    "marketing": false
  },
  "method": "explicit-click",
  "ipAddress": "[pseudonymised or omit]"
}
```

---
---

# DPIA Template (Data Protection Impact Assessment)

## Legal Basis
Art. 35 GDPR — mandatory when processing is "likely to result in a high risk" to individuals.
Art. 35(3) lists mandatory triggers; supervisory authorities publish lists (Art. 35(4)).

## When Required (Art. 35(3) + WP29/EDPB guidance — any 2+ of these factors)
- Systematic and extensive profiling
- Large-scale special category data (Art. 9)
- Systematic monitoring of public areas
- New technologies
- Automated decision-making with legal/significant effects (Art. 22)
- Children's data at scale
- Data matching / combining datasets

---

## DPIA Structure

### 1. Description of Processing (Art. 35(7)(a))
- **System / project name**: [NAME]
- **Controller**: [NAME + DPO if applicable]
- **Nature of processing**: [What operations are performed on the data]
- **Scope**: [Volume, frequency, geographic reach]
- **Context**: [Who are the data subjects; their vulnerability level]
- **Purpose**: [What is the legitimate aim]
- **Lawful basis**: Art. 6(1)[X]; Art. 9(2)[X] if special category

### 2. Necessity and Proportionality Assessment (Art. 35(7)(b))
Assess whether processing is:
- **Necessary** for the purpose — could the purpose be achieved with less/no personal data?
- **Proportionate** — do the benefits outweigh the risks to individuals?
- **Compliant** with data minimisation (Art. 5(1)(c)), purpose limitation (Art. 5(1)(b))

### 3. Risk Assessment (Art. 35(7)(c))
For each identified risk:
| Risk | Likelihood (1–3) | Severity (1–3) | Risk Score | Mitigation |
|------|-----------------|---------------|-----------|------------|
| Unauthorised access | 2 | 3 | High | Encryption, access controls |
| Function creep | 1 | 2 | Medium | Purpose limitation controls |
| Re-identification | 2 | 3 | High | Pseudonymisation |

### 4. Measures to Address Risks (Art. 35(7)(d))
For each High/Medium risk:
- Technical measure: [DESCRIBE]
- Organisational measure: [DESCRIBE]
- Residual risk after mitigation: [Low/Medium/High]

### 5. DPO / Stakeholder Sign-off (Art. 35(2))
- DPO consulted: Yes / No — DPO opinion: [ATTACH]
- Data subjects consulted (where appropriate): Yes / No
- Outcome: ✅ Proceed | ⚠️ Proceed with conditions | 🔴 Prior consultation with SA required (Art. 36)

---
---

# Data Retention Policy Template

## Legal Basis
Art. 5(1)(e) — storage limitation: data kept no longer than necessary for purpose.
Art. 17 — right to erasure triggers where retention period expired.

---

## Retention Schedule

| Data Category | Business Purpose | Retention Period | Lawful Basis | Deletion Method |
|--------------|-----------------|-----------------|--------------|----------------|
| Customer account data | Service provision | Duration of contract + 2 years | Contract (Art. 6(1)(b)) | Secure deletion |
| Marketing preferences | Direct marketing | Until withdrawal of consent | Consent (Art. 6(1)(a)) | Anonymisation |
| Transaction records | Financial/legal obligations | 7 years | Legal obligation (Art. 6(1)(c)) | Secure archival then deletion |
| Employee records | Employment law | Duration + 6 years | Legal obligation | Secure deletion |
| CCTV footage | Security | 30 days | Legitimate interests (Art. 6(1)(f)) | Automatic overwrite |
| Server/access logs | Security monitoring | 90 days | Legitimate interests | Automated purge |
| Consent records | Compliance evidence | 3 years after withdrawal | Legal obligation | Retain in audit log |

---

## Operational Requirements
- Automated deletion jobs should run [FREQUENCY] against retention schedule
- Backups must be included in retention policy — purge from backups within [X] days of primary deletion
- Exceptions process: legal hold procedure for litigation/investigation (suspend deletion)
- Retention schedule reviewed: annually or upon material change to processing

---
---

# Data Subject Rights Procedure

## Legal Basis
Arts. 15–22 (individual rights), Art. 12 (modalities — response within 1 month, extendable by 2 months).

---

## Rights Summary

| Right | Article | When Applicable | Response Time |
|-------|---------|----------------|--------------|
| Access (SAR) | Art. 15 | Always (with exceptions) | 1 month (Art. 12(3)) |
| Rectification | Art. 16 | Inaccurate/incomplete data | 1 month |
| Erasure | Art. 17 | Consent withdrawn; no longer necessary; unlawful processing | 1 month |
| Restriction | Art. 18 | Accuracy contested; objection pending; unlawful but subject wants restriction | 1 month |
| Portability | Art. 20 | Consent or contract basis; automated processing only | 1 month |
| Object | Art. 21 | Legitimate interests or public task basis; direct marketing (absolute) | Immediately for direct marketing |
| No automated decisions | Art. 22 | Solely automated decisions with legal/significant effect | 1 month |

---

## Request Handling Process

1. **Receive**: Accept requests via [EMAIL / WEB FORM / POST]. Identity verification required — proportionate to risk; do not request excessive info (Art. 12(6)).
2. **Verify identity**: [METHOD — e.g., match against account details; 2FA confirmation]
3. **Log**: Record date received, type of request, handler assigned.
4. **Assess**: Determine if exemptions apply (e.g., Art. 17(3) — overriding legal obligation prevents erasure).
5. **Respond**: Within **one calendar month** of receipt (Art. 12(3)). If extending, notify requester within first month with reason (Art. 12(3)).
6. **Response must be**: Free of charge (Art. 12(5)); in concise, plain language (Art. 12(1)); in writing or by electronic means where requested.
7. **Refusal**: If request is refused, inform subject of reasons and right to complain to SA and seek judicial remedy (Art. 12(4)).

## Exemptions to Document
- Legal claims (Art. 17(3)(e))
- Freedom of expression (Art. 17(3)(a))
- Public interest archiving (Art. 17(3)(d))
- Manifestly unfounded or excessive requests — can charge fee or refuse (Art. 12(5))

---

## SLA & Escalation
- Day 0: Request received and logged
- Day 3: Identity verified; request categorised
- Day 20: Draft response reviewed by DPO/legal
- Day 28: Response sent (allowing 2 days buffer before Day 30 deadline)
- Day 30: Statutory deadline
- Extension notice must go out by Day 30 if needed, citing complex/numerous requests (Art. 12(3))
