# Copyright Obligations — GPAI Code of Practice

Complete requirements for Copyright chapter (Commitment 1, Measures 1.1–1.7).

**Legal basis:** Article 53(1)(c), referencing Directive (EU) 2019/790 (DSM Directive), particularly Article 4(3) on text and data mining (TDM) rights reservations.

**Applies to:** ALL GPAI model providers, including those with open-source models. There is no open-source exemption for copyright obligations.

---

## Table of Contents

1. [Legal Framework](#legal-framework)
2. [Commitment 1: Copyright Policy](#commitment-1-copyright-policy)
3. [Measure 1.1: Policy Development](#measure-11-policy-development)
4. [Measure 1.2: Lawful Access](#measure-12-lawful-access)
5. [Measure 1.3: Rights Reservations](#measure-13-rights-reservations)
6. [Measure 1.4: Record-Keeping](#measure-14-record-keeping)
7. [Measure 1.5: Output Safeguards](#measure-15-output-safeguards)
8. [Measure 1.6: Terms of Service](#measure-16-terms-of-service)
9. [Measure 1.7: Complaints Handling](#measure-17-complaints-handling)
10. [Practical Compliance Steps](#practical-compliance-steps)

---

## Legal Framework

EU copyright law operates on the principle of **prior authorisation** — using protected works requires the rights holder's permission unless a specific exception applies.

### Key exception: Text and Data Mining (TDM)
- **Article 3, DSM Directive:** TDM for scientific research by research organisations and cultural heritage institutions — no opt-out possible
- **Article 4, DSM Directive:** TDM for any purpose — BUT rights holders can "reserve their rights" (opt out), and providers must comply with these reservations
- **Article 4(3):** Rights reservations must be expressed "in an appropriate manner, such as machine-readable means"

The Code of Practice operationalises the obligation to "put in place a policy to comply" with these rules. Adherence to the Code **does not guarantee** copyright compliance — that depends on interpretation by national courts and the CJEU.

---

## Commitment 1: Copyright Policy

Signatories commit to establishing, maintaining, and executing a comprehensive copyright policy that applies to all GPAI models distributed within the EU.

**Critical note:** The Code measures supplement but do not replace the fundamental obligation to comply with Union and national copyright law. Providers retain full responsibility for ensuring their operations conform to applicable legal frameworks.

---

## Measure 1.1: Policy Development

### Requirements:
- **Draw up** a unified copyright policy covering all GPAI models placed on the EU market
- **Keep up-to-date** — review and revise regularly to reflect legal developments and operational changes
- **Implement** the policy operationally — it cannot be a paper exercise
- **Define internal accountability** — clear ownership of copyright compliance responsibilities
- **Publish a summary** of the policy (encouraged, not mandatory, but strongly recommended for demonstrating good faith)

### Policy should address:
- Scope: which models and training activities are covered
- Legal basis relied upon for data use (authorisation, TDM exception, etc.)
- Process for identifying and complying with rights reservations
- Internal roles and responsibilities
- Training and awareness for relevant staff
- Review and update schedule
- Escalation process for identified compliance issues

### Example: What a Good Copyright Policy Covers

A compliant copyright policy is NOT a generic legal disclaimer. It is an operational document. Here is what a well-structured policy looks like in practice:

```
1. SCOPE
   "This policy applies to all training data acquisition for [Model X] 
   and any derivative models placed on the EU market."

2. LEGAL BASIS
   "We rely on the TDM exception under Article 4(1) DSM Directive for 
   publicly available web content where no rights reservation has been 
   expressed. For licensed datasets, we hold direct authorisation from 
   [Dataset Provider]."

3. RIGHTS RESERVATION PROCESS
   "Before crawling, our pipeline checks robots.txt for AI-specific 
   directives, scans for TDM-Reservation HTTP headers, and cross-
   references the EU piracy site registry. Content from opted-out 
   sources is excluded before ingestion."

4. INTERNAL ACCOUNTABILITY
   "The Data Governance Lead owns this policy. The Legal team reviews 
   quarterly. Engineering implements technical controls. Escalation 
   path: Engineer → Data Gov Lead → General Counsel."

5. COMPLAINT HANDLING
   "Copyright complaints: copyright@[company].com. Acknowledged within 
   5 business days. Resolution target: 30 days. Appeals process 
   available."

6. REVIEW CYCLE
   "Reviewed quarterly and upon: new model training runs, changes to 
   data sources, legal developments, or complaint patterns."
```

**Common mistakes:**
- A one-paragraph statement saying "we respect copyright" — too vague, not operational
- Policy exists but no one in engineering knows about it — must be implemented, not shelf-ware
- No designated contact point — required by Measure 1.7
- Policy covers training but not output safeguards — must address the full chain

---

## Measure 1.2: Lawful Access

### Requirements:
- Web crawling for training purposes must **only access lawfully available content**
- **Prohibited:** Deliberately circumventing technical protection measures (paywalls, access restrictions, login requirements)
- **Prohibited:** Accessing websites known to "persistently and repeatedly" infringe copyright

### Piracy site exclusion:
- The EU Commission will maintain a publicly available registry of websites identified by EU/EEA authorities as persistent copyright violators
- Providers must exclude these sites from crawling activities
- Until the registry is published, providers should implement their own measures to identify and exclude known piracy sources

### Practical considerations:
- "Lawfully accessible" means content that a human user could access without circumventing protections
- Freely available web content is generally lawfully accessible
- Content behind registration-only access (no payment) may be lawfully accessible — but providers should assess case by case
- Content behind paywalls is NOT lawfully accessible for crawling purposes unless authorised

---

## Measure 1.3: Rights Reservations

### Requirements:
- **Comply with robots.txt** directives specifically related to AI training and data mining
- **Comply with machine-readable opt-out signals** expressed pursuant to Article 4(3) of the DSM Directive
- Implement "state-of-the-art technologies" to identify rights reservations

### Practical implementation:
- Monitor and respect robots.txt, specifically crawl directives aimed at AI/ML bots
- Check for TDM-specific reservation headers or meta tags (e.g., `tdm-reservation` protocols)
- Implement technical systems to detect and act on opt-out signals at scale
- Keep records of how rights reservations were identified and handled

### Open questions:
- Whether robots.txt constitutes a legally sufficient "machine-readable means" under Article 4(3) remains debated
- The scope of what constitutes "state-of-the-art technologies" for identifying reservations is evolving
- Providers should document their approach and rationale to demonstrate good faith compliance

---

## Measure 1.4: Record-Keeping

### Requirements:
- Maintain records of crawling activities and data collection processes
- Document how rights reservations were identified and complied with
- Records should be sufficient to demonstrate compliance upon request from the AI Office

### Practical scope:
- Crawl logs with timestamps and sources
- Rights reservation checks and outcomes
- Data filtering and exclusion records
- Any correspondence with rights holders regarding training data use

---

## Measure 1.5: Output Safeguards

### Requirements:
- Implement **technical safeguards** to minimise the risk of generating copyright-infringing outputs
- Measures should reduce the likelihood of:
  - Verbatim reproduction of copyrighted material
  - Substantial similarity to specific copyrighted works
  - Generation of content that could constitute derivative works without authorisation

### Examples of technical safeguards:
- Output filtering to detect near-verbatim reproduction
- Training techniques that reduce memorisation of specific works
- Content attribution mechanisms where feasible
- Watermarking or provenance tracking for generated content

---

## Measure 1.6: Terms of Service

### Requirements:
- Terms of service must **clearly prohibit** unauthorised use of generated content in ways that infringe copyright
- Users must be informed of their own copyright responsibilities when using GPAI model outputs

### Practical implementation:
- Include explicit clauses on copyright compliance in user/API agreements
- Specify that users are responsible for ensuring their use of model outputs complies with applicable copyright law
- Prohibit use of the model to systematically reproduce copyrighted works

---

## Measure 1.7: Complaints Handling

### Requirements:
- **Designate a contact point** for copyright holders to submit complaints
- Establish **efficient and fair processes** for handling copyright-related complaints
- Respond to complaints in a reasonable timeframe

### Practical implementation:
- Published email address or web form for copyright complaints
- Clear intake process with acknowledgment and expected timelines
- Internal escalation process for complex or high-stakes complaints
- Record-keeping of all complaints and their resolution
- Regular review of complaint patterns to identify systemic issues

---

## Practical Compliance Steps

### Immediate actions (if not already done):
1. **Audit current practices** — map all data sources, crawling activities, and rights reservation handling
2. **Draft copyright policy** — covering all elements from Measure 1.1
3. **Implement robots.txt compliance** — ensure crawling infrastructure respects opt-out signals
4. **Set up complaints process** — designated contact, intake form, response procedures
5. **Review terms of service** — add or strengthen copyright compliance clauses
6. **Publish policy summary** — demonstrate transparency and good faith

### Ongoing obligations:
- Regular policy review and updates (at least annually, more frequently if legal landscape changes)
- Monitor EU Commission piracy site registry (when published) and update exclusion lists
- Track rights reservation technologies and standards as they evolve
- Maintain crawl and compliance records
- Review and respond to complaints promptly

### Common gaps:
- No formalised copyright policy (only informal practices)
- Robots.txt compliance not systematically verified for AI-specific directives
- No designated contact point for copyright complaints
- Terms of service silent on user copyright responsibilities
- Incomplete records of training data provenance and rights status
- No output safeguards against copyright-infringing generation

---

## DACH-Specific Considerations

### Germany:
- **UrhG (Urheberrechtsgesetz)** implements the DSM Directive — §44b covers TDM
- §44b(3): Rights reservations must be "machine-readable" — German courts may interpret this specifically
- Active litigation around AI training and copyright (ongoing as of 2025/2026)
- German publishers particularly active in asserting rights reservations

### Austria:
- UrhG-AT implements DSM Directive provisions similarly
- Less enforcement activity to date, but aligned with EU framework

### Switzerland:
- **Not directly subject to DSM Directive** — Swiss copyright law (URG) has different TDM provisions
- For models placed on the EU market, EU copyright rules apply regardless of where training occurs
- Providers based in Switzerland must still comply with EU copyright rules for EU-targeted models

---

*Source: GPAI Code of Practice (Final Version, July 2025), Regulation (EU) 2024/1689 Article 53(1)(c), Directive (EU) 2019/790 Articles 3, 4.*
