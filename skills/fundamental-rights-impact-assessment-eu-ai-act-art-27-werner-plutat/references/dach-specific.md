# DACH-Specific Considerations for FRIA

This reference adds a Germany/Austria/Switzerland overlay to a FRIA under Article 27 AI Act.

## Why a DACH Overlay Matters

Article 27 is an EU-law obligation, but its practical application often depends on:
- which authority is competent,
- how public-law bodies are organised,
- national constitutional principles,
- labour co-determination rules,
- and sector-specific governance in regulated industries.

For Werner's audience, Germany is the main practical focus.

## Germany - Key Considerations

### 1. Additional constitutional lens: Grundgesetz

For Germany-based assessments, use the **EU Charter** as the primary Article 27 framework, but also consider corresponding **Grundrechte** of the **Grundgesetz** as an additional analytical lens.

Especially relevant:
- **Art. 1 GG** - human dignity
- **Arts. 1 + 2 GG** - general right of personality / informational self-determination
- **Art. 3 GG** - equality / non-discrimination
- **Art. 5 GG** - freedom of expression
- **Art. 12 GG** - occupational freedom
- **Art. 19(4) GG** - effective legal protection

This is particularly helpful in public-administration, healthcare, education, labour, and enforcement contexts.

### 2. Public-law deployers and administrative law

Where the deployer is a German public body, the FRIA should be written with administrative-law realities in mind.

Assess especially:
- proportionality,
- equal treatment,
- proper exercise of discretion,
- documentation of reasons,
- traceability for administrative or judicial review,
- ability to explain the role of AI in the decision process.

A public authority should not use AI in a way that empties out legally required discretion or turns review into a black box.

### 3. Data protection authority mapping

The relevant data protection authority depends on who the deployer is.

#### Federal public bodies
- Likely competence of the **BfDI** (Bundesbeauftragte für den Datenschutz und die Informationsfreiheit).

#### State-level public bodies or private entities
- Likely competence of the relevant **Landesdatenschutzbehörde**.

Always confirm the exact authority based on the deployer's status and seat.

### 4. AI Act market surveillance / sector supervision

For German deployments, identify which authority is competent for AI Act oversight in practice at the time of the assessment.

Potentially relevant:
- **BNetzA** in designated AI Act roles,
- sector supervisors in regulated industries,
- healthcare, financial, or public-sector oversight bodies depending on the use case.

Do not assume a single authority fits every case.

### 5. Public procurement (VgV and procurement governance)

Where the AI system is procured by a public body or public-service operator, the FRIA should connect with procurement practice.

Questions to ask:
- Were Article 27 and Article 26 obligations reflected in the specification or tender documents?
- Does the contract require provider support for FRIA evidence, documentation, data quality, logging, incident response, and updates?
- Can the deployer obtain enough information from the vendor to perform a credible FRIA?
- Are transparency, audit, and exit rights contractually protected?

A weak procurement setup often becomes a weak FRIA because the deployer lacks facts.

### 6. Works council rights - BetrVG

If the AI system affects employees in Germany, the FRIA should flag possible works council participation rights under the **BetrVG**, especially:
- **§ 87(1) Nr. 6 BetrVG** - technical devices designed to monitor behaviour or performance,
- and potentially broader co-determination or consultation obligations depending on the use case and organisational context.

This matters for systems used in:
- recruitment,
- performance evaluation,
- scheduling,
- access control,
- productivity monitoring,
- internal fraud/security analytics.

FRIA questions should include:
- Are employees affected directly or indirectly?
- Does the system monitor or evaluate worker behaviour/performance?
- Has the works council been informed/consulted where required?
- Could lack of co-determination undermine lawful deployment?

### 7. Banking, insurance, and healthcare as public-service contexts

For private entities providing public services, German-sector practice matters.

#### Banking / insurance
- access to essential financial services,
- discrimination concerns,
- explanation and complaint handling,
- alignment with sector governance expectations.

#### Healthcare
- patient safety,
- medical-device / clinical governance overlap,
- vulnerable populations,
- strong need for human override and documentation.

The more essential the service, the stronger the proportionality and remedy analysis should be.

## Austria

For Austria, apply the same core AI Act logic but verify:
- the competent data protection authority,
- market-surveillance arrangements,
- sector supervision,
- and any administrative-law requirements affecting public authorities.

The same themes remain central: proportionality, equality, transparency, and effective remedy.

## Switzerland

Switzerland is not an EU Member State, so Article 27 does not apply as such to purely Swiss domestic deployments.

However, Switzerland is relevant where:
- an organisation operates cross-border into the EU,
- an EU deployer or provider group includes Swiss functions,
- the FRIA is being used as a governance best practice for Swiss operations,
- or Swiss law/governance is being benchmarked against EU standards.

For Swiss contexts, be explicit whether Article 27 applies directly, indirectly, or only as a best-practice benchmark.

## DACH Practical Checklist

Use this overlay checklist in DACH assessments:
- Is the deployer a public body under national public-law structures?
- If private, is it providing a public service in substance?
- Which supervisory authority is competent for data protection?
- Which authority is competent for AI Act market surveillance?
- Are procurement and vendor clauses sufficient to support the FRIA?
- Are works council / employee participation rights triggered?
- Does the German constitutional lens change the proportionality analysis?
- Are sector rules in finance, health, education, or public administration relevant?

## Practical Warning

In DACH settings, the hardest part is often not identifying the rights. It is proving that:
- the deployer is actually in Article 27 scope,
- the use of AI is proportionate in the national governance context,
- and the organisation can explain and defend the deployment before multiple stakeholders at once: legal, DPO, regulator, procurement, HR, and works council.
