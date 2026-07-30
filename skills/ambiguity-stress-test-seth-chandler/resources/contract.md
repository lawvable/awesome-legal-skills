# Profile A — Contracts

A contract is a private, bilateral legal text. Its defining feature for this skill: ambiguity is resolved by recovering the bargain — what these two parties agreed. That makes the contract profile the simplest of the four. Run the core engine; apply the elements below.

## Domain defect families

The universal six carry almost all contract work. One specialization is worth naming:

**Characterization conflict.** The same entitlement is described in two incompatible registers — "guaranteed" in one clause, "based upon performance criteria" in another. A near-relative of internal contradiction (Family A), but the clauses do not flatly collide; they pull the same right toward two different theories of when it vests. Worth its own label because the scenario turns on which characterization controls, not on which clause wins.

## Lexicon additions

Beyond the universal lexicon: *"at will," "for any or no reason"* (Family A, against any notice or term language); *"or person designated by," "as may be assigned," "as in effect from time to time"* (Family F — unilateral-modification powers that erode bargained protections); *"guaranteed," "shall be entitled to"* sitting near conditional language (characterization conflict); *"sole discretion of the Company / the Committee"* (Family D).

## Competing interpreters

Two, fixed: the contracting parties (and their successors and assigns). Every scenario is "Party A claims X; Party B argues Y." The binary is native to the domain.

## Interpretive doctrines

The doctrine set that drives `likely_outcome`:

- **Harmonization** — read the contract as a whole; give effect to every provision; a reading that makes a clause surplusage is disfavored.
- **Specific governs general** — a specific provision controls a general one on the same subject.
- **Contra proferentem** — genuine ambiguity is construed against the drafting party, with extra force in an adhesion contract.
- **Implied covenant of good faith and fair dealing** — discretion granted by the contract must be exercised reasonably and in good faith, not to recapture forgone opportunities.
- **Prevention doctrine** — a party who wrongfully prevents a condition from occurring cannot rely on its non-occurrence.
- **Course of dealing / course of performance / usage of trade** — how the parties and the trade have actually behaved informs meaning.
- **Four-corners rule and the parol evidence rule** — interpretation begins, and often ends, inside the document.

## Redraft register

The drafter is a private party; the parties can rewrite anything by agreement. The `redraft` field proposes clean contract language and is constrained only by governing law and bargaining power. (Whether the redraft is *enforceable* is a separate question — see the Scope note in SKILL.md.)

## Quality-bar adjustment

None. The contract profile has no gauntlet; four-corners resolution is acceptable.

## Worked example — an executive employment agreement

Run against an executive employment agreement (Recursive Designs, Inc. / Stuart Sowinski), the profile produced these scenarios. Outcomes are predictions, hedged; California law governs.

| # | Title | Target clause(s) | Defect family |
|---|-------|------------------|---------------|
| 1 | Reporting structure change reduces the executive's role | §1(a) Position & Duties **×** §4(g)(ii) "Good Reason" | Cross-clause tension |
| 2 | Immediate termination vs. the 14-day notice | §2(a) at-will rule **×** §2(b) 14-day notice | Internal contradiction |
| 3 | "Good Reason" on a change of business direction | §4(g)(ii)(4) | Vague operative term |
| 4 | "Competitive Activity" decided by sole discretion | §4(e)(ii) discretion **×** §4(g)(vi) "Competitor" | Standardless discretion + definitional boundary |
| 5 | A "guaranteed" bonus with no performance criteria | §3(b) Bonus | Gap + characterization conflict |

**1 — Reporting structure.** *Weak point:* §4(g)(ii)(2) protects against "a change in position substantially reducing duties or responsibility," but "substantially" is undefined and §1(a) expressly lets the CEO redirect the reporting line. *Likely outcome:* the company probably prevails on these facts — same title, same core duties, an added reporting layer is unlikely to be a *substantial* reduction — but the result is fact-driven, and the implied covenant bars a sham demotion. *Redraft:* define "substantially reducing duties or responsibility," and state whether a reporting-line change alone counts.

**2 — Immediate termination vs. notice.** *Weak point:* §2(a) says employment may end "at any time"; §2(b) says it ends "by giving … fourteen (14) days' notice in writing"; neither provides pay in lieu of notice, which the executive demands. *Likely outcome:* a court harmonizes rather than voids — the specific clause controls, so §2(b)'s 14-day notice stands as a timing requirement on at-will status; damages for skipping it approximate 14 days' pay. *Redraft:* permit termination effective immediately *upon payment of 14 days' Base Salary in lieu of notice*, and conform §2(a).

**3 — "Good Reason" business pivot.** *Weak point:* §4(g)(ii)(4) requires "a substantial reduction in sales," with no baseline, no measurement period, and no rule on projected versus realized figures. *Likely outcome:* a dip in *projected* sales is unlikely to qualify, so the company likely prevails; ambiguity construed against the drafter would flip it on a measurable actual decline. *Redraft:* define the metric (e.g., a decline over X% in trailing-twelve-month booked revenue against the comparable prior period).

**4 — Discretionary competition ruling.** *Weak point:* §4(e)(ii) grants the Compensation Committee "sole discretion," but the discretion is to apply the §4(g)(vi) "Competitor" definition, which reaches 3D graphics only "for entertainment or educational use" — a geological-survey tool falls outside that qualifier. *Likely outcome:* the executive likely prevails — the implied covenant requires discretion exercised reasonably, and a committee cannot use discretion to override the definition it is charged with applying. *Redraft:* cabin the discretion with a reasonableness standard tied to the defined terms; conform "Competitor" to the industries actually meant to be covered.

**5 — Guaranteed bonus, no criteria.** *Weak point:* §3(b) calls the bonus "guaranteed" on a service condition yet also "based upon performance criteria to be established," and is silent on what governs if criteria are never set. *Likely outcome:* the executive likely recovers the full bonus — the prevention doctrine and the implied covenant bar a party from profiting from its own failure to set the criteria, and "guaranteed" breaks the tie. *Redraft:* provide that if criteria are not established and communicated by a fixed date, the full bonus is payable on the service condition alone.

## Common pitfalls

- **Anchor imprecision** — anchor every scenario to a native citation (§4(g)(ii)), not a positional guess.
- **Under-tagging** — when a defect is a cross-clause interaction, anchor *every* provision in the interaction, not just one.
- **Recall gaps** — a handful of scenarios is a sample, not an audit. When the user wants an audit, scan systematically and report coverage; defect-dense clauses (compensation, termination, definitions) often yield several distinct scenarios each.
