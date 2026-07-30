# TSA CRMP — Detailed Requirements and Implementation Guidance

Source: Based on publicly available TSA Security Directive summaries, Federal Register notices, and DHS/CISA publications.

---

## CRMP Component 1: Cybersecurity Implementation Plan (CIP) / COIP

### Purpose
The CIP (or COIP under the NPRM) is the master compliance document that demonstrates how the covered entity implements and maintains all required cybersecurity measures. It must be submitted to TSA for review and approval.

### Required Sections

**Section 1: Leadership and Accountability**
- Identity of the Accountable Executive (named C-suite individual with authority over cybersecurity decisions and resources)
- Identity of the Cybersecurity Coordinator (primary) and backup designee
- Contact information for both (including 24/7 phone numbers)
- Reporting structure between coordinator and accountable executive

**Section 2: Critical Cyber System (CCS) Inventory**
- Complete list of systems designated as Critical Cyber Systems
- For each CCS: system name, type (IT/OT/ICS), function, owner, physical location, network zone
- Methodology used for CCS determination
- Process for updating the inventory when architecture changes

**Section 3: Network Architecture Overview**
- Current network topology diagrams (IT and OT — must be accurate and current)
- Description of IT/OT boundary mechanisms (firewalls, DMZs, data diodes)
- Remote access architecture into OT environments
- Third-party and vendor connectivity to CCS
- Identification of any legacy systems with limited segmentation capability

**Section 4: Cybersecurity Measures (Four Technical Domains)**

*Domain 1 — Network Segmentation:*
- Segmentation policy and how it is enforced
- Description of technical controls implementing the IT/OT boundary
- Compensating controls for systems that cannot be fully segmented
- Process for authorising exceptions

*Domain 2 — Access Controls:*
- Authentication requirements for CCS access (MFA for remote and privileged access)
- Account lifecycle management (provisioning, review, de-provisioning)
- Privileged access management approach
- Third-party/vendor access controls

*Domain 3 — Continuous Monitoring:*
- Monitoring tools and coverage (IT and OT)
- Log collection and retention policy
- Alerting thresholds and escalation procedures
- Integration with SOC or monitoring team

*Domain 4 — Patch Management:*
- Risk-based patch prioritisation methodology
- Patch timelines by severity (critical, high, medium, low)
- OT-specific patching process (vendor approval, testing, maintenance windows)
- Compensating controls for unpatched legacy OT systems

**Section 5: Incident Detection and Response**
- High-level description of how incidents are detected (monitoring, alerting, user reporting)
- Escalation path from detection to Cybersecurity Coordinator
- Reference to the Cybersecurity Incident Response Plan (separate document)
- CISA 24-hour reporting procedure

**Section 6: Annual Review Process**
- Frequency and process for reviewing and updating the CIP
- Triggers for out-of-cycle review (major architecture change, significant incident, new threat intelligence)
- Approval process for CIP updates
- TSA submission process for material changes

### CIP Approval Process
1. Covered entity submits CIP to TSA via designated secure channel
2. TSA reviews for completeness and alignment with directive requirements
3. TSA may approve, request modifications, or reject
4. Entity implements CIP; cannot claim TSA-approved CIP until approval is granted
5. Material changes to CIP require resubmission

---

## CRMP Component 2: Incident Response Plan (IRP / CIRP)

### Required IRP Elements

**1. Scope and Objectives**
- What systems are covered (all CCS)
- IRP objectives: contain, eradicate, recover, report

**2. Roles and Responsibilities**
- Incident Commander (typically Cybersecurity Coordinator)
- IT response team
- OT/ICS response team (may include OT vendor support)
- Legal and communications (for regulatory reporting)
- Executive escalation path

**3. Incident Classification**
Define severity tiers:
| Tier | Definition | Response Time |
|------|-----------|--------------|
| Critical | Active threat to CCS operations/safety | Immediate — all hands |
| High | Confirmed unauthorised access to CCS | Within 1 hour |
| Medium | Suspected compromise; investigation underway | Within 4 hours |
| Low | Indicator of compromise; no confirmed access | Within 24 hours |

**4. Detection and Initial Analysis**
- How anomalies are identified (monitoring alerts, user reports, third-party notification)
- Initial triage process: confirm vs false positive
- Evidence preservation from first moments

**5. Containment Procedures**
- IT containment: isolate affected systems from network
- OT containment: procedures for isolating OT from IT (IT/OT segregation under incident conditions)
- Manual operation fallback: how to operate OT assets if control systems are isolated
- Preserve operational capability while containing cyber threat

**6. Eradication and Recovery**
- Threat removal procedures
- Backup restoration: integrity verification before restoration
- System rebuild and hardening before reconnecting
- Phased return to operation

**7. CISA and TSA Notification**
- 24-hour CISA reporting trigger (see `tsa-incident-reporting.md`)
- TSA notification procedure
- Internal escalation to Accountable Executive
- Regulatory notification log (record of all notifications made)

**8. Post-Incident Review**
- After-action review within 30 days of incident closure
- Root cause analysis
- Lessons learned documented
- CIP/IRP updated based on findings
- Consider sharing with CISA/ISAC

### Annual IRP Testing

Covered entities must **test at least two IRP objectives annually**. Testing may be conducted via:
- **Tabletop exercise**: Discussion-based walkthrough of a scenario (minimum viable testing)
- **Functional exercise**: Partial activation of IRP with actual system interaction
- **Full-scale exercise**: Complete IRP activation with IT/OT teams

**Recommended test scenarios for TSA compliance**:
1. **IT/OT segregation drill**: Simulate IT compromise; test ability to isolate OT and continue operations manually
2. **Ransomware response drill**: Malware detected on IT; test containment, backup integrity check, restoration procedure
3. **Unauthorised access to OT**: Simulate credential compromise leading to OT access; test detection and response
4. **Vendor access abuse**: Simulate third-party remote access misuse; test detection and revocation

**Test documentation required**:
- Date and type of exercise
- Scenario description
- Participants
- Objectives tested
- Pass/fail for each objective
- Findings and corrective actions
- Corrective action closure tracking

---

## CRMP Component 3: Architecture Design Review (ADR)

### ADR Objectives
1. Confirm network diagrams are current, accurate, and complete
2. Assess effectiveness of IT/OT segmentation
3. Identify undocumented or unauthorised connections to CCS
4. Evaluate remote access security
5. Assess vendor/third-party connectivity risks
6. Produce findings and remediation plan

### ADR Process

**Step 1: Inventory and Documentation Review**
- Collect current network topology diagrams (IT and OT)
- Review CCS inventory for completeness
- Compare diagrams to actual architecture (passive discovery or authorised scan)
- Document any discrepancies

**Step 2: Segmentation Assessment**
For each IT/OT boundary connection:
- Is the connection documented and authorised?
- What security controls enforce the boundary (firewall, DMZ, data diode)?
- Are firewall rules reviewed and minimised?
- Is there a default-deny rule on the OT side?
- Are any direct connections from internet to OT environment?

**Step 3: Remote Access Review**
- Inventory all remote access paths into OT (VPN, RDP, vendor jump servers)
- Confirm MFA is enforced for all remote OT access
- Confirm all remote access is logged and monitored
- Confirm vendor access is time-limited and requires explicit approval

**Step 4: Third-Party Connectivity**
- Map all third-party connections to CCS (vendor remote support, SCADA hosting, cloud-based OT monitoring)
- Assess contractual cybersecurity obligations of third parties
- Confirm third parties cannot access OT without entity approval and monitoring

**Step 5: Vulnerability and Risk Identification**
- Identify high-risk architecture patterns:
  - Flat networks where IT and OT share the same subnet
  - OT devices with direct internet connectivity
  - Obsolete OT systems with no compensating controls
  - Shared accounts between IT and OT
  - Unencrypted protocols on OT networks (Telnet, FTP, HTTP to HMIs)

**Step 6: Findings and Remediation Plan**
For each finding:
| Finding ID | Description | Risk Level | Recommendation | Owner | Target Date |
|-----------|-------------|-----------|----------------|-------|-------------|
| ADR-001 | PLC subnet not segmented from corporate LAN | Critical | Deploy firewall; implement DMZ | OT Manager | Q2 |

### ADR Outputs
- Updated and validated network topology diagrams
- Findings report (findings, risk ratings, recommendations)
- Remediation action plan with owners and target dates
- Sign-off by Accountable Executive

---

## CRMP Component 4: Cybersecurity Assessment Plan (CAP)

### Purpose
The CAP documents how the entity will assess the effectiveness of its CRMP each year. It is not the assessment itself — it is the plan for conducting assessments. Results are reported to TSA annually.

### Required CAP Elements

**1. Assessment Scope**
- Which CCS and CRMP components are in scope each assessment cycle
- Rationale for any CCS excluded from scope (with compensating coverage explanation)

**2. Assessment Methodology**
Define the types of assessments to be performed:
| Assessment Type | Description | Applicable To |
|----------------|-------------|---------------|
| Vulnerability scan | Automated scan of IT/OT assets for known CVEs | IT; limited OT (passive preferred) |
| Penetration testing | Authorised simulated attack to test defences | IT; OT where safe and agreed |
| Configuration review | Compare system configs against hardening standards | IT servers; network devices; OT where possible |
| Process review | Interview-based review of policies and procedures | All CRMP components |
| Red team exercise | Adversary simulation against CCS | Large/complex environments |

**OT assessment cautions**:
- Active scanning of OT networks can disrupt industrial communications — use passive monitoring tools
- Penetration testing in OT requires vendor coordination and operational approval
- Prioritise configuration review and architecture review over intrusive testing for OT

**3. Assessment Schedule**
Provide a 12-month schedule:
| Quarter | Assessment Activity | CCS in Scope |
|---------|-------------------|-------------|
| Q1 | Vulnerability scan (IT); IRP tabletop exercise | All IT CCS; IRP |
| Q2 | Configuration review (OT); ADR | OT CCS; architecture |
| Q3 | Penetration test (IT external + internal) | IT CCS |
| Q4 | Process review (all CRMP components); CAP results compilation | All |

**4. Responsible Parties**
- Internal assessment teams or third-party assessors
- OT assessment requires OT-qualified personnel (GICSP, GCIA, or equivalent)
- Independence requirements: assessors should not assess their own implementations

**5. Annual Reporting to TSA**
- Compile assessment findings and remediation status
- Submit results to TSA via designated secure channel annually
- Include: findings summary, risk ratings, remediation plan, open items, corrective action progress

---

## Four Technical Domains — Detailed Implementation Guidance

### Domain 1: Network Segmentation — Implementation Details

**Minimum acceptable architecture:**
```
[Internet] → [Edge Firewall] → [Corporate IT Network]
                                      ↓
                              [IT/OT Firewall / DMZ]
                                      ↓
                              [OT Network / ICS Network]
                                      ↓
                              [Field Devices: PLCs, RTUs, HMIs]
```

**Security controls for each boundary:**
- **Edge to IT**: Stateful firewall; DMZ for internet-facing services; IDS/IPS
- **IT to OT**: Dedicated firewall or data diode; default-deny; whitelist only required protocols/ports; no direct routing
- **OT to field**: Segmented VLANs for different process areas; restrict inter-VLAN traffic

**Data diodes / unidirectional gateways**: Preferred for highest-security OT environments. Data flows one way (OT → IT for monitoring/historian) — no return path possible. Vendors: Waterfall Security, Owl Cyber Defense, Bayshore Networks.

**Compensating controls for flat networks** (where full segmentation is not immediately feasible):
- Host-based firewall on all IT systems to block OT traffic
- Enhanced monitoring and alerting at the flat network level
- Documented exception with remediation timeline
- Enhanced access controls at OT device level

### Domain 2: Access Controls — OT-Specific Guidance

**OT account management challenges**:
- Many OT systems have limited account management capability (single shared admin account)
- Legacy HMIs may not support MFA natively
- Vendor accounts are often needed for maintenance but may be always-on

**Solutions for OT access control limitations**:
| Challenge | Solution |
|-----------|---------|
| Legacy HMI, no MFA | Deploy a jump server/bastion host with MFA in front of HMI; access HMI only via jump server |
| Shared OT admin account | Log all access via PAM tool; require check-out with approval for shared account use |
| Vendor remote access | Use vendor-specific VPN with MFA; time-limited sessions; all sessions logged; revoke after job |
| No LDAP/AD support in OT | Maintain local accounts on OT devices with strong passwords; rotate quarterly |

**Privileged Access Management (PAM) for OT**:
- Check-out workflows for privileged OT credentials
- Session recording for all privileged OT access
- Automatic expiry of vendor sessions
- Alert on out-of-hours privileged access

### Domain 3: Continuous Monitoring — OT-Specific Tools

**Recommended OT monitoring approaches:**
| Approach | Tools | Notes |
|---------|-------|-------|
| Passive network monitoring | Claroty, Dragos Platform, Nozomi Networks Guardian, Armis | No traffic injection; learn by listening |
| Asset discovery | Passive discovery via monitoring tools | Builds CCS inventory automatically |
| Anomaly detection | Dragos, Claroty, Nozomi | Alert on deviations from OT communication baselines |
| Log collection | Syslog from OT-capable devices; SIEM with OT parsers | Not all PLCs support syslog |
| Threat intelligence | Dragos WorldView, Claroty Team82, CISA ICS-CERT advisories | OT-specific threat intelligence |

**What to monitor in OT environments:**
- New devices appearing on OT network (unauthorised asset)
- New communication paths (protocol, endpoint pair)
- Engineering workstation connections to PLCs outside maintenance windows
- Remote access sessions to OT
- Command injection attempts (Modbus, DNP3, EtherNet/IP abnormal commands)
- Authentication failures on OT devices

### Domain 4: Patch Management — OT-Specific Guidance

**OT patching lifecycle:**
1. **Vendor notification**: Receive patch/advisory from OT vendor
2. **Risk assessment**: Evaluate CVE severity vs operational impact of patching
3. **Vendor confirmation**: Confirm patch is supported for your firmware version
4. **Test environment**: Test patch in lab/test environment before production
5. **Change approval**: Change management ticket; operations approval for downtime window
6. **Deployment**: Apply during planned maintenance window
7. **Verification**: Confirm system operation post-patch
8. **Documentation**: Record patch applied, date, version

**Unpatched legacy OT systems (compensating controls)**:
| Compensating Control | Description |
|--------------------|-------------|
| Network isolation | Further isolate the legacy system to its own VLAN; restrict to minimum required communications |
| Enhanced monitoring | Increase monitoring sensitivity for the legacy system |
| Application whitelisting | If OS supports it, whitelist only authorised executables |
| Removal from internet path | Ensure no internet connectivity path to the legacy device |
| Documentation | Document the legacy system, its risks, and compensating controls in the CIP |

**Patch prioritisation (risk-based):**
| CVSS Score | Severity | Target Patch Timeline |
|-----------|---------|----------------------|
| 9.0–10.0 | Critical | 30 days (or compensating controls within 7 days) |
| 7.0–8.9 | High | 60 days |
| 4.0–6.9 | Medium | 90 days |
| 0.1–3.9 | Low | 180 days or next planned maintenance |
