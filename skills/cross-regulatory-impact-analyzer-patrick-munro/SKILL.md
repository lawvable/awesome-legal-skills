---
name: cross-regulatory-impact-analyzer-patrick-munro
description: Analyzes how multiple regulations interact for a specific product, service, or business model. Identifies where obligations overlap, reinforce, complement, duplicate, or conflict; builds a priority matrix; produces an integrated compliance timeline; and estimates the total compliance burden. Use when (1) scoping a new product or service against the full regulatory landscape before launch, (2) conducting M&A due diligence on a target's multi-regulation exposure, (3) building a strategic compliance roadmap where single-regulation analyses miss the interactions, (4) advising on complex situations where regulations touch the same conduct from different angles, or (5) estimating budget and resourcing for multi-regulation compliance. Primary coverage of EU digital regulation (GDPR, Data Act, AI Act, CRA, NIS2, DORA, DMA, DSA, ePrivacy) and national implementations; the framework extends to any jurisdiction where overlapping regulatory regimes apply to the same activity.
metadata:
  author: "Patrick Munro"
  license: "agpl-3.0"
  version: "2026-04-25"
---

# Cross-Regulatory Impact Analyzer

## Purpose

Most regulatory analyses treat regulations one at a time. This is fine when a business is subject to one regulation. It stops being fine the moment multiple regulations reach the same activity, because the real compliance questions live in the overlap: which obligation is stricter, which deadline comes first, what satisfies both, and what conflicts. This skill produces the analysis that single-regulation guides do not.

## When to use

- New product or service launch where more than one regulation plausibly applies
- M&A due diligence on a target with multi-regulation exposure
- Strategic compliance planning where a siloed, regulation-by-regulation approach has hit its limits
- Complex client advisory on regulatory interactions
- Budget and resourcing estimation for multi-regulation programmes
- Triaging incident response playbooks where multiple reporting regimes trigger simultaneously

## Analysis framework

The analysis proceeds in six phases. Each phase produces an output that feeds the next.

### Phase 1: Scope determination

Identify which regulations apply based on:

- **Product or service type**: hardware, software, SaaS, IoT, AI system, platform, financial service
- **Sector**: financial services, healthcare, critical infrastructure, public sector, consumer, etc.
- **Entity size**: headcount, revenue, balance sheet (matters for NIS2, DORA size thresholds, SME carve-outs)
- **Data processing**: personal data types, volumes, special categories
- **Geographic scope**: EU-wide, specific Member States, third-country targeting
- **Risk profile**: safety, security, fundamental rights implications
- **Designation status**: VLOP/VLOSE (DSA), gatekeeper (DMA), critical ICT TPP (DORA), critical entity (NIS2/CER)

Document the inclusion rationale for each regulation. Document the exclusion rationale too, because "we considered X and concluded it does not apply because Y" is half the value of the analysis.

### Phase 2: Obligation extraction

For each applicable regulation, extract:

- **Core requirements**: what must be done
- **Deadlines**: when compliance is required, distinguishing phased application dates
- **Penalties**: administrative fines, criminal sanctions, private rights of action
- **Conformity or certification**: assessment type, notified bodies, self-assessment vs. third-party
- **Documentation**: records, reports, impact assessments
- **Ongoing obligations**: monitoring, review, update, training

Cite articles precisely. Flag where obligations depend on delegated acts or guidance not yet adopted.

### Phase 3: Overlap classification

Classify each interaction using this taxonomy:

- **Reinforcing**: multiple regulations require the same action. One implementation satisfies both.
- **Complementary**: regulations address different aspects of the same topic. Coordinate, do not duplicate.
- **Duplicative**: near-identical obligations with different wording. Single implementation, dual documentation.
- **Conflicting**: requirements appear contradictory. Need interpretation, legal opinion, or regulator engagement.
- **Lex specialis**: a sector-specific regulation prevails over a general one (e.g., DORA over NIS2 for financial entities).

The taxonomy matters because each classification triggers a different compliance strategy.

### Phase 4: Priority matrix

Rank obligations on five axes:

1. **Legal severity**: prohibited practices > high-risk obligations > medium > low
2. **Timeline**: earliest deadline first
3. **Dependency**: prerequisites before dependents (you cannot build a DPIA before you have mapped processing)
4. **Impact**: highest business impact or penalty exposure first
5. **Feasibility**: quick wins vs. long-horizon builds

Produce a stack-ranked list. Do not produce one with "priorities" that has everything at priority 1.

### Phase 5: Timeline coordination

Build an integrated timeline showing:

- All regulatory deadlines across regulations
- Dependencies between obligations
- Resource allocation points
- Milestones and checkpoints
- Buffer for delegated acts, guidance publications, and regulatory engagement

Deliverable forms: Gantt chart for implementation planning, calendar view for supervisory deadlines, dependency diagram where the interactions are the point.

### Phase 6: Cost estimation

Estimate total compliance cost with explicit ranges and assumptions:

- **Legal**: external counsel, regulatory advice, opinions, litigation reserve
- **Technical**: system modifications, security measures, API development, SBOM tooling
- **Personnel**: compliance headcount, training, ongoing monitoring
- **Certification**: third-party assessments, audits, notified body fees
- **Opportunity**: delayed market entry, feature constraints, jurisdictional carve-outs

Ranges, not point estimates. Assumptions visible. Sensitivity analysis for the major drivers.

## Output formats

Choose based on audience and use case.

### Executive summary (1-2 pages)

For board or C-suite consumption.

- Applicable regulations at a glance
- Top risks and conflicts
- Five priority actions
- Total estimated compliance cost with range
- Recommended timeline with go/no-go gates

### Detailed analysis (10-30 pages)

For legal and compliance teams.

- Scope determination with rationale
- Regulation-by-regulation obligation map
- Overlap and conflict analysis with classification
- Prioritized obligation list
- Integrated timeline
- Cost breakdown with assumptions
- Risk mitigation and open questions

### Implementation roadmap (visual)

For programme management.

- Timeline chart colour-coded by regulation
- Dependencies visible
- Resource requirements marked at key points
- Milestones and gate decisions

### Compliance matrix (spreadsheet)

For operational tracking.

- Row per obligation
- Columns: regulation, article, requirement, deadline, priority, cost, owner, status, evidence
- Filterable and sortable
- Progress tracking capability

## Typical workflow

1. **Intake**. Gather product description, technical architecture, processing activities, target markets, entity profile.
2. **Research**. Verify current text of each applicable regulation. Note recent amendments, pending delegated acts, national implementations.
3. **Scope**. Apply inclusion criteria systematically. Document rationale. Address edge cases.
4. **Extract**. Build obligation maps per regulation, cited at article level.
5. **Classify**. Apply the interaction taxonomy to every pairwise interaction that matters.
6. **Prioritize**. Build the priority matrix. Stress-test it against timelines and resource constraints.
7. **Estimate**. Cost and timeline. Ranges with assumptions.
8. **Produce**. Choose the output format. Write it.

## Conflict resolution hierarchy

When regulations conflict, apply in order:

1. **Lex specialis**: sector-specific prevails over general. DORA over NIS2 for financial entities. MDR over AI Act for medical device AI where MDR addresses the specific risk.
2. **Stricter standard**: where both apply cumulatively, meet the higher bar. NIS2 24-hour early warning beats GDPR 72-hour for personal data breaches that also qualify as significant incidents.
3. **Cumulative compliance**: where neither is specialis and neither is clearly stricter, meet both. CRA and AI Act for AI-enabled connected products.
4. **Transition provisions**: check for grandfathering, phased application, or carve-outs for products placed on the market before a specific date.
5. **Regulator guidance**: consult EC guidance, EDPB opinions, ENISA publications, national competent authority positions.
6. **Formal legal opinion**: for novel or ambiguous situations, obtain a written opinion from qualified counsel in the relevant jurisdiction. Document the reasoning.

## Common interaction patterns

See `references/regulation-interactions.md` for detailed analysis of the most common overlap scenarios, including:

- GDPR and Data Act (data access, portability)
- AI Act and GDPR (automated decision-making, data governance)
- CRA and AI Act (product security, vulnerability handling)
- NIS2 and DORA (incident reporting, third-party risk, financial services)
- GDPR and NIS2 (security measures, breach notification timelines)
- Data Act and CRA (connected product requirements, API security)
- DSA and DMA (layered platform obligations for gatekeepers)
- AI Act and sectoral regulations (medical devices, automotive, financial services)

## Regulation quick reference

See `references/regulation-profiles.md` for concise profiles of the core EU digital regulations covered here (GDPR, Data Act, AI Act, CRA, NIS2, DORA, DMA, DSA, ePrivacy) with scope, key deadlines, major obligations, and penalty ranges. Profiles are reference material and must be verified against current primary sources before use in a binding context.

## Industry templates

Common combinations worth pre-thinking:

- **IoT product manufacturer**: GDPR + Data Act + CRA + AI Act (if AI system on board)
- **Cloud or SaaS provider**: GDPR + Data Act + NIS2 + CRA (for software)
- **Financial platform**: GDPR + DORA + AI Act (if high-risk AI) + NIS2 (DORA takes precedence for financial-specific ICT)
- **Healthcare application**: GDPR + MDR or IVDR + AI Act (if medical AI)
- **Large online platform**: GDPR + DSA + DMA (if gatekeeper) + ePrivacy
- **Critical infrastructure operator**: GDPR + NIS2 + CER + sectoral regulation

## Quality checklist

Before delivering:

- [ ] Every regulation in scope has a documented inclusion rationale
- [ ] Current version of each regulation verified against primary source
- [ ] Article-level citations throughout
- [ ] All material overlaps classified using the taxonomy
- [ ] Conflicts flagged explicitly, not buried in neutral prose
- [ ] Priority matrix is stack-ranked; no "everything is priority 1"
- [ ] Timeline shows every material deadline
- [ ] Cost estimates include ranges and named assumptions
- [ ] Recommendations are specific and actionable
- [ ] Executive summary captures the five points that matter most
- [ ] Known gaps and unresolved questions are listed, not hidden

## Limitations

This analysis reflects regulations in force and publicly available guidance as of the date of the output. Three common sources of drift to watch:

- **Delegated and implementing acts**: many EU regulations have delegated acts adopted separately and on a later timeline than the main regulation
- **National implementations**: directives and some regulations leave Member State discretion; national measures drift from the EU framework over time
- **Enforcement practice**: supervisory authorities develop interpretations through guidance and enforcement; what is compliant today may be renegotiated tomorrow

State these limitations visibly in the deliverable. Recommend annual refresh at minimum, with triggered updates on material regulatory change.

## Output location

Use a clear naming convention:

```
cross-regulatory-analysis-[product-or-client]-[YYYY-MM-DD].docx
compliance-matrix-[product-or-client]-[YYYY-MM-DD].xlsx
```

## Disclaimer

This analysis is a strategic planning tool, not legal advice. Regulatory interactions are fact-sensitive; specific questions require qualified counsel in the applicable jurisdiction. Supervisory practice and guidance evolve; dates and thresholds cited here must be re-verified before use in a binding context.
