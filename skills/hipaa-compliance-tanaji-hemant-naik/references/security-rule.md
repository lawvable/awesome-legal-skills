# HIPAA Security Rule Reference
## 45 CFR Part 164, Subparts A and C

---

## Table of Contents
1. [Scope & Applicability](#1-scope--applicability)
2. [General Rules](#2-general-rules)
3. [Administrative Safeguards](#3-administrative-safeguards)
4. [Physical Safeguards](#4-physical-safeguards)
5. [Technical Safeguards](#5-technical-safeguards)
6. [Organizational Requirements](#6-organizational-requirements)
7. [Policies, Procedures & Documentation](#7-policies-procedures--documentation)
8. [Risk Analysis Deep Dive](#8-risk-analysis-deep-dive)
9. [Cloud & Modern Architecture Guidance](#9-cloud--modern-architecture-guidance)
10. [Implementation Checklist](#10-implementation-checklist)

---

## 1. Scope & Applicability

The Security Rule applies to **ePHI** (electronic Protected Health Information) — PHI that is:
- Created, received, maintained, or transmitted in electronic form
- Stored on any electronic media (servers, workstations, laptops, mobile devices, removable media, cloud)

**Applies to:**
- Covered Entities (CEs)
- Business Associates (BAs) — directly under HITECH (2009)

**Does NOT cover:**
- PHI in paper form (Privacy Rule covers this)
- Verbal communications

---

## 2. General Rules

### Three Safeguard Categories
All CEs and BAs must implement:
1. **Administrative Safeguards** — Policies, procedures, workforce management
2. **Physical Safeguards** — Facility access, workstation, device controls
3. **Technical Safeguards** — Technology-based protections for ePHI

### Required vs. Addressable
| Designation | Meaning |
|------------|---------|
| **Required** | Must implement — no flexibility |
| **Addressable** | Must assess whether reasonable and appropriate; if so implement; if not, document why and implement an equivalent alternative |

> **Common Misconception**: "Addressable" does NOT mean optional. You must either implement it or formally document why you didn't and what you did instead.

### Flexibility Principle (§164.306(b))
Implementation may consider:
- Size, complexity, and capabilities of the CE/BA
- Technical infrastructure, hardware, and software security capabilities
- Costs of security measures
- Probability and criticality of potential risks

---

## 3. Administrative Safeguards
### §164.308

| Standard | Req/Addr | Description |
|----------|----------|-------------|
| **Security Management Process** (§164.308(a)(1)) | Required | Framework for protecting ePHI |
| → Risk Analysis | Required | Assess threats, vulnerabilities, likelihood, impact |
| → Risk Management | Required | Implement security measures to reduce risk to reasonable level |
| → Sanction Policy | Required | Apply sanctions for workforce violations |
| → Information System Activity Review | Required | Regularly review audit logs, access reports, incident reports |
| **Assigned Security Responsibility** (§164.308(a)(2)) | Required | Designate a Security Official |
| **Workforce Security** (§164.308(a)(3)) | Required | Control workforce access to ePHI |
| → Authorization/Supervision | Addressable | Supervise workforce members working with ePHI |
| → Workforce Clearance Procedure | Addressable | Determine appropriate access levels |
| → Termination Procedures | Addressable | Revoke access upon termination |
| **Information Access Management** (§164.308(a)(4)) | Required | Grant appropriate access to ePHI |
| → Isolating Healthcare Clearinghouse Function | Required (if applicable) | Separate clearinghouse from rest of org |
| → Access Authorization | Addressable | Process for authorizing access |
| → Access Establishment and Modification | Addressable | Process for granting/modifying access |
| **Security Awareness and Training** (§164.308(a)(5)) | Required | Train all workforce members |
| → Security Reminders | Addressable | Periodic security updates |
| → Protection from Malicious Software | Addressable | Anti-malware procedures |
| → Log-in Monitoring | Addressable | Monitor failed log-in attempts |
| → Password Management | Addressable | Guidance on creating/changing passwords |
| **Security Incident Procedures** (§164.308(a)(6)) | Required | Respond to security incidents |
| → Response and Reporting | Required | Identify, respond to, mitigate, document incidents |
| **Contingency Plan** (§164.308(a)(7)) | Required | Respond to emergencies affecting ePHI |
| → Data Backup Plan | Required | Create retrievable exact copies of ePHI |
| → Disaster Recovery Plan | Required | Restore lost ePHI data |
| → Emergency Mode Operation Plan | Required | Continue critical business processes during emergency |
| → Testing and Revision | Addressable | Implement procedures for periodic testing of contingency plans |
| → Applications and Data Criticality Analysis | Addressable | Assess relative criticality of applications |
| **Evaluation** (§164.308(a)(8)) | Required | Periodic technical/non-technical evaluation |
| **Business Associate Contracts** (§164.308(b)(1)) | Required | BAA with all BAs handling ePHI |

---

## 4. Physical Safeguards
### §164.310

| Standard | Req/Addr | Description |
|----------|----------|-------------|
| **Facility Access Controls** (§164.310(a)(1)) | Required | Limit physical access to systems containing ePHI |
| → Contingency Operations | Addressable | Access during disaster recovery |
| → Facility Security Plan | Addressable | Safeguard facility and equipment |
| → Access Control and Validation | Addressable | Control access to facilities based on role |
| → Maintenance Records | Addressable | Document repairs/modifications to physical security |
| **Workstation Use** (§164.310(b)) | Required | Specify proper functions and physical surroundings for workstations |
| **Workstation Security** (§164.310(c)) | Required | Physical safeguards for workstations accessing ePHI |
| **Device and Media Controls** (§164.310(d)(1)) | Required | Govern receipt and removal of hardware/media |
| → Disposal | Required | Properly dispose of media containing ePHI (wiping, destruction) |
| → Media Re-use | Required | Remove ePHI before reuse of electronic media |
| → Accountability | Addressable | Track movements of hardware/media |
| → Data Backup and Storage | Addressable | Create retrievable copy before moving equipment |

---

## 5. Technical Safeguards
### §164.312

| Standard | Req/Addr | Description |
|----------|----------|-------------|
| **Access Control** (§164.312(a)(1)) | Required | Allow only authorized persons/software to access ePHI |
| → Unique User Identification | Required | Assign unique names/numbers to identify and track user identity |
| → Emergency Access Procedure | Required | Obtain ePHI during emergency |
| → Automatic Logoff | Addressable | Terminate sessions after inactivity |
| → Encryption and Decryption | Addressable | Encrypt/decrypt ePHI |
| **Audit Controls** (§164.312(b)) | Required | Hardware/software/procedural mechanisms to record and examine activity in systems containing ePHI |
| **Integrity** (§164.312(c)(1)) | Required | Protect ePHI from improper alteration or destruction |
| → Mechanism to Authenticate ePHI | Addressable | Corroborate that ePHI has not been altered |
| **Person or Entity Authentication** (§164.312(d)) | Required | Verify identity of person/entity seeking access |
| **Transmission Security** (§164.312(e)(1)) | Required | Guard against unauthorized access to ePHI transmitted over electronic networks |
| → Integrity Controls | Addressable | Ensure ePHI is not improperly modified during transmission |
| → Encryption | Addressable | Encrypt ePHI in transit |

---

## 6. Organizational Requirements
### §164.314

### Business Associate Contracts (§164.314(a)):
BAA must require the BA to:
- Implement Administrative, Physical, and Technical Safeguards
- Ensure subcontractors do the same (sign sub-BAAs)
- Report security incidents (including successful and unsuccessful attempts)
- Authorize termination of contract if CE determines BA has violated a material term

### Group Health Plans (§164.314(b)):
Plan documents must require plan sponsors to:
- Implement reasonable and appropriate security measures
- Not use/disclose ePHI except as permitted
- Report security incidents to the plan

---

## 7. Policies, Procedures & Documentation
### §164.316

### Policies and Procedures (§164.316(a)):
- Must implement reasonable and appropriate policies to comply with the Security Rule
- Must update as necessary

### Documentation Requirements (§164.316(b)):
- Maintain written (electronic or paper) policies, procedures, and records required by the Security Rule
- **Retention**: 6 years from creation date OR date last in effect (whichever is later)
- Make documentation available to those responsible for implementing procedures
- Review documentation periodically and update as needed

---

## 8. Risk Analysis Deep Dive

Risk Analysis (§164.308(a)(1)(ii)(A)) is the **foundation** of HIPAA Security compliance. HHS has emphasized it is the most commonly cited deficiency in enforcement actions.

### Required Components:
1. **Scope**: All ePHI created, received, maintained, or transmitted (not just EHR — includes backups, emails, mobile devices)
2. **Threat Identification**: Identify potential threats to ePHI (natural, human, environmental)
3. **Vulnerability Identification**: Identify security vulnerabilities
4. **Likelihood Assessment**: Assess probability that each threat would exploit each vulnerability
5. **Impact Assessment**: Assess potential impact of threat occurrence
6. **Risk Level Determination**: Combine likelihood + impact = risk level (High/Medium/Low)
7. **Current Controls**: Document existing security measures and their effectiveness

### Risk Management (§164.308(a)(1)(ii)(B)):
- Implement security measures sufficient to reduce risks to a reasonable and appropriate level
- Prioritize based on risk level
- Document all decisions

### Common Risk Analysis Mistakes (HHS Enforcement Findings):
- Only analyzing the EHR system (missing emails, mobile devices, backups, printers)
- Performing once and never updating
- Not documenting the analysis
- Confusing risk analysis with gap analysis
- Assigning risk levels without methodology

### NIST Framework Alignment:
HHS recommends NIST SP 800-30 for risk analysis methodology. NIST SP 800-66 is the HIPAA-specific guidance.

---

## 9. Cloud & Modern Architecture Guidance

### Cloud Service Providers (CSPs):
- CSPs storing ePHI are Business Associates — **BAA is required**
- AWS, Azure, GCP all offer HIPAA-eligible services under BAA
- BAA does not transfer compliance responsibility — CE/BA must configure properly

### Key Cloud Considerations:

**Encryption:**
- At rest: AES-256 minimum (addressable but industry standard)
- In transit: TLS 1.2+ minimum; TLS 1.3 recommended
- Key management: Use dedicated KMS (AWS KMS, Azure Key Vault, GCP Cloud KMS)
- Customer-managed keys preferred for higher sensitivity

**Access Control:**
- Implement IAM with least-privilege principle
- Use MFA for all accounts with ePHI access
- Separate service accounts from human accounts
- Regularly audit and rotate credentials

**Audit Logging:**
- Enable CloudTrail (AWS), Activity Log (Azure), Cloud Audit Logs (GCP)
- Log: API calls, data access, authentication events, configuration changes
- Immutable log storage (S3 with Object Lock, etc.)
- Retention: Minimum 6 years for HIPAA records
- Alert on anomalous access patterns

**Network Security:**
- VPC/private network for ePHI systems
- Security groups / network policies: deny-by-default
- No direct internet exposure of ePHI datastores
- WAF for any public-facing applications handling ePHI

**Mobile & BYOD:**
- MDM/EMM solution required if devices access ePHI
- Remote wipe capability
- Screen lock enforcement
- Encrypted storage
- App-level controls (MAM) if possible

### API & Application Security:
- Authentication: OAuth 2.0 + OIDC; consider SMART on FHIR for health apps
- Input validation to prevent injection attacks
- No ePHI in URLs (appears in logs)
- No ePHI in error messages
- Rate limiting on endpoints handling ePHI
- FHIR APIs: HL7 FHIR R4 with SMART on FHIR is the modern standard

### DevOps / CI-CD:
- No real PHI in dev/test environments (use synthetic data)
- Secrets management (never hardcode credentials)
- SAST/DAST scanning in pipeline
- Dependency scanning for vulnerabilities
- Infrastructure as Code security scanning

---

## 10. Implementation Checklist

### Administrative
- [ ] Designate Security Official
- [ ] Conduct and document Risk Analysis covering ALL ePHI
- [ ] Implement Risk Management Plan with prioritized remediation
- [ ] Implement sanction policy for violations
- [ ] Review system activity regularly (audit logs)
- [ ] Establish workforce clearance procedures
- [ ] Implement access authorization process
- [ ] Conduct annual Security Awareness Training (document it)
- [ ] Implement anti-malware protection
- [ ] Monitor failed login attempts
- [ ] Document and implement Password/Credential Policy
- [ ] Implement Security Incident Response Plan
- [ ] Create Data Backup Plan (test it)
- [ ] Create Disaster Recovery Plan (test it)
- [ ] Create Emergency Mode Operation Plan
- [ ] Execute BAAs with all vendors handling ePHI
- [ ] Conduct periodic Security Rule evaluations

### Physical
- [ ] Implement facility access controls (badge, keypad, locks)
- [ ] Create and implement Facility Security Plan
- [ ] Document workstation use policies
- [ ] Implement workstation physical security
- [ ] Implement media disposal procedures (certificates of destruction)
- [ ] Implement media re-use procedures (secure wiping)
- [ ] Track hardware/media movements

### Technical
- [ ] Assign unique user IDs (no shared accounts)
- [ ] Implement role-based access control (RBAC)
- [ ] Implement MFA for all ePHI access
- [ ] Implement automatic session timeout
- [ ] Implement encryption at rest (AES-256)
- [ ] Implement encryption in transit (TLS 1.2+)
- [ ] Enable and monitor audit logs
- [ ] Implement integrity controls (checksums, digital signatures)
- [ ] Implement entity authentication mechanisms
- [ ] Test transmission security controls
