# FRIA Methodology - Structured Assessment for Article 27

This reference provides a practical method for conducting a **Fundamental Rights Impact Assessment (FRIA)** under Article 27 EU AI Act.

## Purpose

The goal is not to produce a perfect mathematical score. The goal is to create a **defensible, structured judgment** about whether a concrete high-risk AI deployment creates unacceptable or insufficiently mitigated risks to fundamental rights.

Use this method to:
- identify relevant rights and affected groups,
- assess inherent and residual risk,
- evaluate proportionality and necessity,
- define mitigations,
- support a deployment recommendation,
- and document whether notification may be required.

## Assessment Logic

Run the FRIA in six analytical layers:

1. **Use case definition** - What exactly is the AI system doing in practice?
2. **Affected group mapping** - Who may be impacted directly or indirectly?
3. **Rights engagement** - Which Charter rights are plausibly engaged?
4. **Risk assessment** - How likely, severe, and reversible are the harms?
5. **Safeguards assessment** - Do current controls materially reduce the risks?
6. **Residual risk + proportionality** - Can the deployment proceed, and on what conditions?

## Step-by-Step Method

### Step 1 - Define the unit of assessment

The unit of assessment is the **specific deployer + specific use case + specific process**.

Document at minimum:
- deployer entity,
- system name/vendor/version,
- legal high-risk basis,
- process where used,
- intended output,
- intended users,
- affected individuals/groups,
- intended duration/frequency/scale.

If any of these are missing, note the assessment as provisional.

### Step 2 - Build a rights impact matrix

For each affected group, create a row covering:
- affected group,
- right engaged,
- risk scenario,
- harm mechanism,
- inherent likelihood,
- inherent severity,
- reversibility,
- existing safeguards,
- residual risk,
- required action.

Use one row per **meaningful scenario**, not one row per right in the abstract.

### Step 3 - Score inherent risk

Score each scenario before safeguards are applied.

#### Likelihood scale

| Score | Meaning | Practical cue |
|------|---------|---------------|
| 1 | Rare | Exceptional, strong controls already embedded in context |
| 2 | Unlikely | Possible but not expected in ordinary operation |
| 3 | Possible | Realistic in normal operation or foreseeable edge cases |
| 4 | Likely | Expected to arise repeatedly without intervention |
| 5 | Very likely | Structural or frequent risk pattern |

#### Severity scale

| Score | Meaning | Practical cue |
|------|---------|---------------|
| 1 | Negligible | Minor inconvenience, no meaningful rights effect |
| 2 | Low | Limited impact, quickly correctable |
| 3 | Moderate | Material burden or disadvantage for the affected person |
| 4 | Serious | Significant exclusion, denial, stigma, financial or health harm |
| 5 | Severe | Major or systemic harm, lasting deprivation, major dignity/health/liberty impact |

#### Reversibility scale

| Score | Meaning | Practical cue |
|------|---------|---------------|
| 1 | Easily reversible | Quickly corrected with low burden |
| 2 | Mostly reversible | Correctable, though some burden remains |
| 3 | Partly reversible | Remediation possible but incomplete |
| 4 | Hard to reverse | Correction difficult, delayed, or costly |
| 5 | Irreversible / near-irreversible | Harm cannot realistically be undone fully |

### Step 4 - Derive an inherent risk rating

Use the following practical formula:

**Inherent Risk Score = Likelihood × Severity × Reversibility**

This yields a directional score from **1 to 125**.

#### Suggested interpretation bands

| Score | Interpretation |
|------|----------------|
| 1–10 | Low inherent risk |
| 11–30 | Moderate inherent risk |
| 31–60 | High inherent risk |
| 61–125 | Very high inherent risk |

**Important:** This is a support tool, not the decision itself. A low numerical score does not override legal concerns, and a high score does not automatically prohibit deployment. Rights such as dignity, non-discrimination, effective remedy, and access to essential services often require heightened qualitative judgment.

## Qualitative Overlays - Mandatory

In addition to the numerical score, answer these questions for each material scenario:

1. **Affected population:** Does the risk fall mainly on vulnerable, dependent, or structurally disadvantaged groups?
2. **Opacity:** Would the affected person know the AI system contributed to the outcome?
3. **Contestability:** Can the person challenge the result meaningfully and in time?
4. **Dependency:** Does the system affect access to essential services, income, healthcare, liberty, education, or public benefits?
5. **Cumulative effects:** Could repeated small impacts create systemic disadvantage?
6. **Automation bias:** Are human decision-makers likely to over-trust the output?

If one of these factors is strongly present, consider **uplifting** the practical risk rating even if the raw score looks moderate.

## Step 5 - Assess safeguards

Evaluate whether each safeguard is:
- real,
- implemented,
- role-assigned,
- tested,
- and actually capable of reducing the identified risk.

A safeguard should generally only count as strong if it is:
- specific to the risk,
- operational in day-to-day use,
- supported by training and accountability,
- and capable of preventing or detecting the problem before harm escalates.

### Typical safeguard categories

- Human review / human-in-the-loop
- Override rights and escalation paths
- Input data validation
- Error and bias monitoring
- Thresholds preventing full automation
- Audit trails and logging
- Complaint and redress procedures
- Stop-use / kill-switch governance
- Special treatment of vulnerable groups
- Contractual provider obligations and incident escalation

## Step 6 - Assess residual risk

After considering safeguards, assign a **residual risk** rating for each scenario:
- Low
- Moderate
- High
- Very high

Then explain **why** the risk changed or remained high.

### Residual risk cues

- **Low:** Safeguards are likely to prevent or quickly remedy most harms.
- **Moderate:** Risks remain meaningful but manageable with documented controls.
- **High:** Significant harm remains plausible despite current controls.
- **Very high:** Rights impact remains severe, weakly controlled, or hard to justify.

## Step 7 - Proportionality and necessity test

For each material scenario and for the overall use case, ask:

### Necessity
- Why is AI used here at all?
- Is the objective legitimate and specific?
- Is there a less rights-intrusive way to achieve the same purpose?
- Has the deployer considered non-AI alternatives or narrower use?

### Proportionality
- Do the benefits justify the burden on affected rights?
- Are the burdens distributed fairly?
- Are safeguards commensurate with the stakes?
- Is the use excessive in duration, scope, frequency, or data intensity?

A use case can fail the proportionality analysis even if formal safeguards exist.

## Step 8 - Decision recommendation

Use one of four recommendation outcomes:

1. **Proceed** - residual risks are acceptable with current controls.
2. **Proceed with conditions** - deployment is acceptable only after defined measures are implemented.
3. **Pause / redesign** - material gaps must be closed before go-live.
4. **Do not proceed** - rights impact appears disproportionate or insufficiently mitigable.

For each recommendation, specify:
- required mitigation measures,
- owner,
- deadline,
- and whether reassessment is required before launch.

## Notification Trigger Support

Where the FRIA identifies a **specific risk** to natural persons or groups, document:
- what the specific risk is,
- who is affected,
- why existing safeguards are insufficient or conditional,
- and whether Article 27(3) notification is likely required.

The FRIA should not just say "notification may be needed." It should state the factual basis clearly.

## Practical Scoring Example

### Example: Public-sector fraud screening tool

**Scenario:** Welfare applicants are flagged as high risk for manual investigation.

- Likelihood: 4 (likely - model runs continuously at scale)
- Severity: 4 (serious - delays/denials, stigma, procedural burden)
- Reversibility: 3 (partly reversible - later correction possible, but interim harm remains)

**Inherent Score:** 4 × 4 × 3 = 48 → **High inherent risk**

**Qualitative overlays:** vulnerable population, opaque flagging, limited contestability → practical concern remains high.

**Safeguards:** manual review exists, but reviewers over-trust model and explanations are poor.

**Residual risk:** still **High**

**Recommendation:** Proceed only with conditions / pause until explanation, review protocol, and appeal safeguards are strengthened.

## Red Flags That Usually Warrant Escalation

Treat the following as strong escalation signals:
- essential services or benefits can be denied,
- children or patients are affected,
- strong discrimination indicators exist,
- the system is effectively non-contestable,
- the deployer cannot explain how the AI affected the outcome,
- human oversight is nominal only,
- residual risk remains high for dignity, equality, or remedy rights.

## Documentation Standard

A robust FRIA methodology section should always show:
- the scoring approach used,
- the qualitative overlays considered,
- how safeguards were evaluated,
- how residual risk was determined,
- and why the final recommendation follows.

The goal is not mathematical certainty. The goal is a transparent, reviewable, rights-focused decision trail.
