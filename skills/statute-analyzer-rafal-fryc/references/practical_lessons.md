# Practical Lessons from Multi-Statute Analysis

These lessons were learned from analyzing 19+ state privacy laws, comparing automated extraction against professional legal analyses, and conducting cross-jurisdictional compliance projects.

---

## Extraction vs. Analysis

### Lesson 1: Extraction Is Not Analysis

Extracting what a statute SAYS is different from understanding what it MEANS.

| Activity | What It Does |
|----------|--------------|
| **Extraction** | Captures text, requirements, definitions |
| **Analysis** | Interprets ambiguity, prioritizes, provides practical guidance |

**Implication:** Complete extraction is valuable as source material, but professional analysis adds:
- Interpretation of ambiguous terms
- Prioritization of which requirements matter most
- Practical compliance guidance
- Risk assessment

### Lesson 2: Flag Ambiguous Terms

Certain statutory terms inherently require judgment:
- "Reasonable" measures
- "Appropriate" safeguards
- "Material" changes
- "Unreasonable" risk
- "Significant" effects

**Action:** When extracting requirements, flag these terms. They mark where legal judgment adds the most value and where enforcement may be unpredictable.

---

## Structural Insights

### Lesson 3: Statutes Follow Predictable Patterns

Most statutes are organized similarly:
1. Purpose/findings
2. Definitions
3. Applicability/scope
4. Substantive requirements
5. Rights granted
6. Duties imposed
7. Exemptions
8. Enforcement
9. Penalties
10. Effective dates

**Benefit:** Recognizing this pattern allows rapid navigation of unfamiliar statutes.

### Lesson 4: Definitions Create Interconnected Webs

Statutory definitions are not independent:
- "Critical harm" may depend on "frontier model"
- "Frontier model" may depend on "compute cost"
- Tracing the chain is essential

**Action:** Map definition dependencies before analyzing substantive provisions.

### Lesson 5: Applicability Thresholds Determine Everything

Before extracting requirements, know WHO must comply:
- Revenue thresholds ($25M, $50M)
- Volume thresholds (35K, 100K, 175K consumers)
- Revenue-from-activity thresholds (25%, 50% from data sales)
- Entity type definitions

**Critical Distinction:**
- **Disjunctive (OR):** Meet ANY threshold = covered
- **Conjunctive (AND):** Must meet ALL thresholds = covered

A statute requiring "$25M revenue AND 100K consumers" covers far fewer entities than one requiring either.

---

## Requirement Types

### Lesson 6: Separate Disclosure from Operational Requirements

Statutes mix WHAT must be STATED with HOW parties must OPERATE:

| Type | Belongs In | Does NOT Belong In |
|------|------------|-------------------|
| **Disclosure** | Privacy policy, notice | Internal process documentation |
| **Operational** | Process design, training | Public-facing documents |
| **Technical** | System specifications | Policy language |
| **UI** | Design requirements | Policy text |

**Common Mistake:** Including "respond within 45 days" in a privacy policy requirements checklist. That's an operational deadline, not a disclosure requirement.

### Lesson 7: Time-Based Requirements Are High Priority

Time-specific obligations create hard deadlines:
- Response periods (45 days, 90 days)
- Reporting windows (72 hours)
- Retention periods (5 years)
- Review cycles (annual)
- Phase-in periods

**Action:** Extract time-based requirements separately and create a timeline view.

### Lesson 8: Consent Requirements Imply Disclosure Requirements

When a statute requires consent:
- There's an implied disclosure requirement (state that consent is obtained)
- But the consent mechanism is operational
- The policy says "we obtain consent"; the process actually obtains it

---

## Exemptions

### Lesson 9: Entity vs. Data Exemptions

Two fundamentally different exemption types:
- **Entity exemption:** The whole organization is exempt
- **Data exemption:** Only certain data is exempt; comply for other data

**Example:** HIPAA-covered data may be exempt, but the covered entity must still comply for non-HIPAA data.

### Lesson 10: Delayed Application Is Not Exemption

Some entities get delayed compliance dates, not permanent exemptions:
- Nonprofits may have 6-12 month grace periods
- The obligation eventually applies

**Action:** Track both permanent exemptions AND delayed effective dates.

### Lesson 11: Industry-Specific Exemptions Rarely Appear in Summaries

Beyond standard federal law carve-outs, statutes may exempt:
- Air carriers
- Electric utilities
- Riverboat casinos
- Licensed professionals

**Action:** Read the full exemptions section; don't rely on summaries.

---

## Cross-Jurisdictional Patterns

### Lesson 12: States Cluster Into Regulatory Philosophies

After reading several statutes, patterns emerge:

| Pattern | Characteristics | Example States |
|---------|-----------------|----------------|
| **Consumer-Protective** | Lower thresholds, fewer exemptions, stricter requirements | Maryland, California |
| **Business-Friendly** | Higher thresholds, broad exemptions, permanent cure periods | Indiana, Iowa, Kentucky |
| **Model-Following** | Based on existing templates with minor variations | Many post-2020 states |

**Benefit:** Recognizing which model a new statute follows accelerates analysis.

### Lesson 13: Rights Are Not Uniform

Do not assume all statutes grant the same rights:
- Some omit the right to correct
- Deletion scope varies ("all data" vs. "data provided by" the person)
- Sensitive data treatment differs (consent vs. opt-out)
- Not all provide profiling opt-out

**Action:** Verify which rights actually exist before listing them.

### Lesson 14: Definitions Vary More Than Expected

Key terms may differ across jurisdictions:
- "Sale" (monetary consideration only vs. "other valuable consideration")
- Sensitive data categories expand with each new statute
- Age cutoffs vary (13, 15, 16, 17, 18)
- Threshold formulations use different metrics

**Action:** Never assume a term means the same thing across jurisdictions.

### Lesson 15: The Most Protective Standard May Be the Safest Baseline

If complying across multiple jurisdictions:
- Identify the strictest requirements
- Use that as baseline
- Note where other jurisdictions are more permissive

---

## Enforcement Dynamics

### Lesson 16: Enforcement Mechanisms Shape Priorities

Two identical provisions may have different practical importance:

| Factor | Impact on Priority |
|--------|-------------------|
| AG-only enforcement | Moderate priority |
| Private right of action | High priority |
| Dedicated enforcement agency | High priority |
| High penalties ($10K+/violation) | High priority |
| Permanent cure period | Lower urgency |
| Expiring cure period | Higher urgency |

### Lesson 17: What the Statute Doesn't Say Matters

Important information includes:
- Rights or remedies explicitly EXCLUDED
- Common provisions notably ABSENT
- Issues left to regulatory discretion
- Safe harbors that DO exist

**Action:** Compare against checklists of typical provisions to identify gaps.

### Lesson 18: Political and Constitutional Context Affects Enforceability

A statute's requirements may never take effect if:
- Federal law preempts it
- Constitutional challenges succeed
- Political changes lead to repeal
- Enforcement resources aren't allocated

**Action:** For controversial statutes, assess preemption risks and pending litigation.

---

## The Analysis Process

### Lesson 19: Work Section by Section

Read an entire section before extracting individual requirements:
- Context from surrounding provisions clarifies ambiguous language
- Related requirements are often grouped
- Cross-references within sections modify meaning

### Lesson 20: Cross-Reference Rights with Duties

- Rights sections list what people can DO
- Duties sections specify what must be DONE or DISCLOSED
- Both inform complete compliance picture

### Lesson 21: Generate Practical Next Steps

After extracting requirements, translate to action:
- What must be done?
- By when?
- Who is responsible?
- What's the non-compliance risk?

---

## Common Pitfalls

### Pitfall 1: Mixing Requirement Types

A "policy requirements" checklist should not include:
- Response deadlines (operational)
- System capabilities (technical)
- Button placement (UI)

### Pitfall 2: Assuming Threshold Uniformity

Threshold language varies:
- Alternative vs. cumulative criteria
- Revenue percentage vs. dollar amount
- Consumer volume vs. transaction volume
- Different measurement periods

### Pitfall 3: Stopping at the Statute

Complete picture requires:
- Implementing regulations
- Agency guidance
- Court interpretations
- Enforcement history

### Pitfall 4: Ignoring Model Law Origins

Many statutes follow templates:
- Uniform laws
- Earlier state laws
- Federal frameworks
- Industry-drafted models

Identifying the model helps predict interpretation.

---

## Summary: Layered Analysis Approach

| Layer | Purpose | Method |
|-------|---------|--------|
| 1. Verification | Confirm current version, dates | Legal research |
| 2. Orientation | Understand structure, definitions | Reading |
| 3. Extraction | Capture requirements, exemptions | Systematic review |
| 4. Categorization | Group by type | Classification |
| 5. Contextualization | Compare to related laws | Research |
| 6. Interpretation | Resolve ambiguities | Legal analysis |
| 7. Prioritization | Identify key provisions | Judgment |
| 8. Action Planning | Convert to tasks | Project management |

Each layer builds on previous ones. Rushing to action planning without proper extraction leads to incomplete compliance.
