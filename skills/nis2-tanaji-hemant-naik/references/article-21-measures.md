# NIS2 Article 21 — Cybersecurity Risk Management Measures

Directive (EU) 2022/2555, Art. 21 requires essential and important entities to take "appropriate and proportionate technical, operational and organisational measures" to manage risks and protect network and information systems. Proportionality is assessed against the entity's size, exposure, and the severity of potential impact.

---

## Measure 1 — Risk Analysis & Information Security Policies

**Requirement:** Documented policies covering risk analysis methodology and information security governance.

**Implementation guidance:**
- Adopt a formal risk management methodology (ISO 27005, NIST RMF, or equivalent)
- Produce and maintain an asset inventory covering in-scope network and information systems
- Define risk acceptance criteria aligned to business impact
- Review risk assessments at least annually and after significant incidents or changes
- Ensure the management body approves the risk management policy (Art. 20 link)

---

## Measure 2 — Incident Handling

**Requirement:** Procedures for detection, analysis, containment, eradication, and recovery.

**Implementation guidance:**
- Maintain a written Incident Response Plan (IRP) covering all NIS2 significant incident scenarios
- Define "significant incident" thresholds in line with Art. 23(3): substantial disruption to service delivery, financial loss to the entity, or material/non-material damage to other natural or legal persons
- Establish 24h/72h/1-month reporting workflows with pre-drafted notification templates for the national CSIRT or competent authority
- Conduct post-incident reviews; feed lessons learned back into risk assessment
- Test IRP at least annually via tabletop exercises or simulations

**Significant incident indicators (Art. 23(3)):**
- Service disruption affecting a significant number of users
- Duration > a few hours for critical services
- Geographic spread affecting other Member States
- Reputational, financial, or safety impact

---

## Measure 3 — Business Continuity, Backup & Disaster Recovery

**Requirement:** Plans for service continuity, backup management, disaster recovery (DR), and crisis management during and after incidents.

**Implementation guidance:**
- Define Recovery Time Objective (RTO) and Recovery Point Objective (RPO) per critical service
- Implement automated, encrypted, offsite backups; test restoration quarterly
- Maintain DR runbooks and infrastructure failover playbooks
- Define a crisis management structure with clear roles, decision authorities, and escalation paths
- Test BCP/DR at least annually; involve management body in crisis management exercises

---

## Measure 4 — Supply Chain Security

**Requirement:** Address security in supply chain relationships, including between entities and their direct suppliers and service providers.

**Implementation guidance:**
- Maintain a register of critical ICT suppliers and third-party service providers
- Perform pre-onboarding security assessments (questionnaires, certifications, audits)
- Include NIS2/security requirements as contractual obligations (right-to-audit, incident notification SLAs, minimum security baselines)
- Assess supply chain risks as part of the annual risk assessment
- Monitor ENISA and national authority supply chain risk assessments (Art. 22 coordinated risk assessments)
- Apply enhanced due diligence to high-risk ICT vendors identified by Member States

---

## Measure 5 — Secure Acquisition, Development & Maintenance

**Requirement:** Security in the acquisition, development, and maintenance of network and information systems, including vulnerability handling and disclosure.

**Implementation guidance:**
- Apply Secure SDLC practices: threat modelling, code review, SAST/DAST, penetration testing
- Establish a vulnerability management programme with defined SLAs for patching by severity (e.g., critical ≤ 7 days, high ≤ 30 days)
- Maintain a coordinated vulnerability disclosure (CVD) policy (aligned with ENISA CVD guidelines)
- Track CVEs relevant to in-scope systems using threat intelligence feeds
- Include security acceptance criteria in vendor contracts for purchased systems

---

## Measure 6 — Effectiveness Assessment

**Requirement:** Policies and procedures to assess the effectiveness of cybersecurity risk management measures.

**Implementation guidance:**
- Define KPIs/KRIs for each Art. 21 measure (e.g., mean time to detect, patch compliance rate, training completion rate)
- Conduct internal audits or management reviews at least annually
- Engage independent third-party assessors or penetration testers as appropriate
- Report effectiveness metrics to the management body
- Map findings to the risk register and trigger remediation plans

---

## Measure 7 — Cyber Hygiene & Training

**Requirement:** Basic cyber hygiene practices and cybersecurity training for staff.

**Implementation guidance:**
- Deploy mandatory security awareness training for all staff at least annually
- Cover: phishing, social engineering, password hygiene, incident reporting, BYOD/remote working
- Provide role-based training for IT/OT administrators, incident responders, and the management body
- Management body must complete cybersecurity training specific to Art. 20 governance obligations
- Track completion rates; address gaps before audit cycles

---

## Measure 8 — Cryptography & Encryption

**Requirement:** Policies and procedures on the use of cryptography and, where appropriate, encryption.

**Implementation guidance:**
- Define approved cryptographic algorithms (AES-256 for data at rest, TLS 1.2+ for data in transit, SHA-256/SHA-384 for hashing)
- Establish a key management lifecycle: generation, storage (HSM recommended for critical keys), rotation, and destruction
- Require encryption of sensitive data stored in cloud environments and on portable media
- Review cryptographic standards annually given evolving threats (e.g., post-quantum readiness)
- Document exceptions and compensating controls where encryption is not feasible

---

## Measure 9 — Human Resources Security, Access Control & Asset Management

**Requirement:** HR security, access control policies and asset management.

**Implementation guidance:**
- Apply least-privilege and need-to-know principles for system access
- Implement role-based access control (RBAC); review permissions quarterly
- Conduct background screening for roles with privileged access (subject to applicable employment law)
- Maintain an authoritative asset inventory (hardware, software, data assets)
- Enforce joiners/movers/leavers process with same-day revocation for leavers
- Apply identity lifecycle management; disable dormant accounts after 30–90 days inactivity

---

## Measure 10 — MFA, Secure Communications & Emergency Systems

**Requirement:** Use of multi-factor authentication (MFA) or continuous authentication solutions, secured voice, video, and text communications, and secured emergency communication systems.

**Implementation guidance:**
- Require MFA for all remote access, privileged accounts, and cloud management consoles
- Apply phishing-resistant MFA (FIDO2/hardware tokens) for highest-privilege accounts
- Enforce MFA for email access, VPN, and SaaS platforms holding sensitive data
- Use end-to-end encrypted channels for sensitive internal communications (e.g., incident coordination)
- Maintain a separate, documented emergency communication plan with out-of-band channels in case primary systems are compromised

---

## Proportionality Principle

Art. 21(1) requires measures to be "appropriate and proportionate" taking into account:
- The entity's exposure to risks
- The entity's size
- The likelihood and severity of incidents including societal and economic impact
- The cost of implementation

Essential Entities face more rigorous supervisory scrutiny (Art. 32 proactive) and should apply controls at the higher end of the proportionality spectrum. Important Entities are subject to reactive supervision (Art. 33) but face the same 10-measure obligations.
