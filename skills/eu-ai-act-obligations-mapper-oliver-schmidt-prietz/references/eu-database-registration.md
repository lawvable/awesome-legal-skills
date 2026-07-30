# EU Database Registration — Art. 49

## 1. Overview

**Legal basis:** Art. 49 AI Act (registration obligations), Art. 71 (database establishment)

*German: Registrierung in der EU-Datenbank*

**Recitals:** 128-131

Art. 49 establishes a dual-track registration mechanism in the EU-wide database for high-risk AI systems. The database serves three interconnected objectives:

1. **Public transparency** — enabling citizens, civil society, and affected persons to access information about high-risk AI systems operating in the EU
2. **Market surveillance support** — providing national authorities (Marktaufsichtsbehoerden) with a centralized registry to identify, track, and investigate AI systems within their jurisdiction
3. **Deployer access** — allowing deployers to verify provider information, conformity status, and intended purpose before putting a system into service

The Commission is mandated under Art. 71 to establish and maintain this database, ensuring public accessibility for the non-confidential portions of registration entries. The database is distinct from national product registries and operates as a Union-level instrument.

---

## 2. Who Must Register

Art. 49 creates two separate registration tracks with different triggering conditions.

### Provider Registration (Art. 49(1)-(2))

All providers of high-risk AI systems must register **themselves** and **each individual system** before placing on the market or putting into service. This applies regardless of provider location:

- **EU-established providers** register directly
- **Third-country providers** register through their authorized representative (Bevollmaechtigter) per Art. 22
- **Art. 6(3) exception claimants** must still register per Art. 6(4)/Art. 49(2), documenting why the system is assessed as non-high-risk despite falling under Annex III

### Deployer Registration (Art. 49(3))

The deployer registration obligation applies only to a defined subset of deployers:

- Public authorities (Behoerden)
- EU institutions, bodies, offices, and agencies
- Private entities acting on behalf of a public body

**Key distinction:** Private-sector deployers operating in their own capacity are generally NOT required to register, even when deploying Annex III high-risk systems. This asymmetry reflects the legislator's focus on public-sector accountability.

### Boundary Analysis — Registration Triggers by Scenario

| Scenario | Provider Must Register? | Deployer Must Register? |
|----------|------------------------|------------------------|
| Private company deploys Annex III system | YES | NO (unless acting for public body) |
| Public authority deploys Annex III system | YES | YES |
| Private entity contracted by municipality | YES | YES (acting on behalf of public body) |
| Annex I product embedding AI component | YES (follows sectoral product legislation pathway) | Depends on deployer type |
| GPAI model provider | Separate registration per Art. 49(2) | N/A |
| Art. 6(3) exception claimed | YES (with exception documentation) | N/A — system classified as non-high-risk |

---

## 3. Required Information Fields

### Provider Registration Fields (Art. 49(1))

| # | Field | Description |
|---|-------|-------------|
| 1 | Provider identity (Anbieteridentitaet) | Legal name, registered address, contact details, authorized representative where applicable |
| 2 | System name and identifiers | Trade name, version designation, unique system reference number |
| 3 | Classification basis | Annex I product category or Annex III application area triggering high-risk classification |
| 4 | Intended purpose (Zweckbestimmung) | Provider-defined intended purpose per Art. 3(12), sufficiently detailed for deployer evaluation |
| 5 | Conformity assessment status | Whether conformity assessment per Art. 43 is completed; EU declaration of conformity reference |
| 6 | CE marking status | Confirmation of CE marking affixed per Art. 48 |
| 7 | Member States of availability | EU/EEA countries where system is or will be placed on the market |
| 8 | System lifecycle status | Current status: on market, withdrawn, or recalled |

### Deployer Registration Fields (Art. 49(3))

| # | Field | Description |
|---|-------|-------------|
| 1 | Deployer identity (Betreiberidentitaet) | Entity name, legal classification (public authority, EU institution, contracted entity) |
| 2 | System reference | Cross-reference to provider's existing registration entry |
| 3 | Deployment context | Specific intended use, categories of affected persons or groups |
| 4 | Member State of deployment | Jurisdiction where the system is being operated |

**Note on public accessibility:** Not all fields are publicly visible. Art. 71(4) distinguishes between publicly accessible data (e.g., provider identity, system name, intended purpose) and restricted data available only to market surveillance authorities.

---

## 4. Step-by-Step Registration Process

| Step | Action | Key Considerations |
|------|--------|--------------------|
| 1 | **Access portal** | Navigate to the EU AI database via the AI Office portal (managed by the Commission) |
| 2 | **Authenticate** | Verify organizational identity through the designated electronic identification mechanism |
| 3 | **Prepare documentation** | Gather all required fields per Section 3; ensure conformity assessment is completed (providers) |
| 4 | **Complete entry** | Fill in all mandatory fields; use precise Annex III category references where applicable |
| 5 | **Verify accuracy** | Review classification basis and intended purpose for consistency with technical documentation |
| 6 | **Submit** | Submit the registration entry — note that certain fields become publicly accessible upon submission |
| 7 | **Maintain** | Update the registration whenever system status, availability scope, or version changes |

**Provider-specific note:** Registration must be complete before the system is placed on the market. An incomplete or inaccurate registration does not satisfy Art. 49(1), even if the system otherwise meets all Chapter III requirements.

**Deployer-specific note:** Public-body deployers must complete registration before putting the system into service or using it. The deployer entry references (not duplicates) the provider's existing registration.

---

## 5. Timeline and Update Obligations

| Milestone | Obligation | Trigger |
|-----------|-----------|---------|
| Provider: before placing on market | Complete initial registration (Art. 49(1)) | Decision to make system available in the EU |
| Deployer (public body): before putting into service | Complete deployer registration (Art. 49(3)) | Decision to deploy a specific high-risk system |
| Information change | Update registration without undue delay (Art. 49(4)) | Any material change to registered information |
| System withdrawal | Update system status to "withdrawn" | Provider decision to remove from market |
| System recall | Update system status to "recalled" | Safety or compliance-driven recall |
| New Member State | Add Member State to availability scope | Expansion of geographic availability |
| New system version | Evaluate whether new registration or update required | Substantial modification per Art. 6(1) second sentence |

**Database operational status:** Art. 71 mandates the Commission to establish the database. Organisations should monitor AI Office communications for portal availability and any implementing acts specifying technical registration formats.

---

## 6. Practical Guidance and Common Pitfalls

### Frequent Errors

| Error | Why It Matters | Mitigation |
|-------|---------------|------------|
| Incorrect Annex III category | Misclassification undermines the entire registration's accuracy and may trigger wrong conformity assessment pathway | Cross-check system functionality against each Annex III sub-category; document reasoning |
| Incomplete intended purpose | Deployers rely on registered intended purpose to evaluate whether their use falls within scope | Draft intended purpose with sufficient specificity for third-party evaluation |
| Failing to update after modification | Outdated registration creates a false public record and potential enforcement exposure | Establish internal change-management triggers linked to registration updates |
| Confusing product CE marking with AI system CE marking | Annex I products may carry a product-level CE mark that is distinct from the AI Act CE marking requirement | Verify that CE marking covers AI Act conformity specifically, not only sectoral product legislation |

### Interaction with National Registers

Some Member States may establish supplementary national AI databases or reporting obligations. The EU database does not preempt national requirements — verify whether additional national registration applies in each deployment jurisdiction.

### Multiple Annex III Categories

Where a system's intended purpose spans multiple Annex III application areas, all applicable categories must be documented in the registration. A single registration entry should reflect the full classification scope to avoid fragmented records.

### Art. 6(3) Exception and Registration

Providers claiming the Art. 6(3) exception (system falls under Annex III but is assessed as non-high-risk) must still register per Art. 6(4)/Art. 49(2). The registration entry must include documentation of the exception reasoning. See [references/art6-4-documentation.md] for the full documentation framework.

### Cross-References

- Provider obligation context: see [references/high-risk-provider-obligations.md], Art. 16(f)
- Deployer obligation context: see [references/high-risk-deployer-obligations.md], Section B6
- Art. 6(3) exception documentation: see [references/art6-4-documentation.md]

---

## RACI and Effort Assessment

| Aspect | Detail |
|--------|--------|
| Legal basis | Art. 49, Art. 71 |
| Frequency | One-time registration + ongoing updates |
| Time effort | 2/5 |
| Expertise required | 2/5 |
| AI competency | 1/5 |
| RACI | Legal/Compliance=R, IT=C, Management=I |
