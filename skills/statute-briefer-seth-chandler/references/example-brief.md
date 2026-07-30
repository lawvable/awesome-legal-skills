# Example: MAPS + RULES Brief

This example demonstrates the output format for a Mode A (text-only) brief of a simple statute.

---

## MAPS

### Citation and text status

**Citation:** 15 U.S.C. § 1692e (Fair Debt Collection Practices Act – False or misleading representations)

**Text status:** Codified version; text-as-provided

### Purpose

**Express statutory purpose (15 U.S.C. § 1692(e)):**
> "It is the purpose of this subchapter to eliminate abusive debt collection practices by debt collectors, to insure that those debt collectors who refrain from using abusive debt collection practices are not competitively disadvantaged, and to promote consistent State action to protect consumers against debt collection abuses."

### Structure map (entire Act)

```
15 U.S.C. §§ 1692-1692p (FDCPA)
├── § 1692 – Congressional findings and purpose [purpose/findings]
├── § 1692a – Definitions [definitions]
├── § 1692b – Acquisition of location information [substantive restriction]
├── § 1692c – Communication in connection with debt collection [substantive restriction]
├── § 1692d – Harassment or abuse [substantive prohibition]
├── § 1692e – False or misleading representations [substantive prohibition] ← FOCUS
├── § 1692f – Unfair practices [substantive prohibition]
├── § 1692g – Validation of debts [procedural requirement]
├── § 1692h – Multiple debts [procedural rule]
├── § 1692i – Legal actions by debt collectors [venue restriction]
├── § 1692j – Furnishing certain deceptive forms [prohibition]
├── § 1692k – Civil liability [enforcement/remedies]
├── § 1692l – Administrative enforcement [agency enforcement]
├── § 1692m – Reports to Congress [reporting]
├── § 1692n – Relation to State laws [preemption/savings]
├── § 1692o – Exemption for State regulation [exemption]
├── § 1692p – Exception for certain bad check enforcement [exemption]
```

### Scope and coverage

- **Covered actors:** "debt collector" as defined in § 1692a(6) – persons whose principal business is debt collection, or who regularly collect debts owed to another
- **Covered conduct:** "communication" in connection with collection of a "debt"
- **Covered transactions:** "debt" = obligation arising from consumer credit transaction (§ 1692a(5))
- **Geography:** United States
- **Jurisdictional hook:** Use of instrumentality of interstate commerce or mails
- **Explicit exclusions:** Original creditors (generally); certain nonprofit organizations; government officers

### Definitions and interpretive rules

| Term | Definition | Location |
|------|------------|----------|
| "debt" | Obligation to pay money arising from consumer transaction | § 1692a(5) |
| "debt collector" | Person who regularly collects debts owed to another | § 1692a(6) |
| "consumer" | Natural person obligated to pay debt | § 1692a(3) |
| "communication" | Conveying information through any medium | § 1692a(2) |

**Interpretive provisions:** None explicit; 16 false representation categories in § 1692e(1)-(16) are non-exhaustive ("without limiting the general application of the foregoing").

---

## RULES

### Rule-Module: 15 U.S.C. § 1692e

**1. Provision:** 15 U.S.C. § 1692e

**2. Trigger conditions (elements):**
1. Defendant is a "debt collector" under § 1692a(6)
2. Defendant used a "false, deceptive, or misleading representation or means"
3. The representation or means was used "in connection with the collection of any debt"

**3. Legal effect:** Prohibition – "A debt collector may not use any false, deceptive, or misleading representation or means in connection with the collection of any debt."

**4. Exceptions / defenses / safe harbors:**
- Bona fide error defense (§ 1692k(c)): Not liable if violation "was not intentional and resulted from a bona fide error notwithstanding the maintenance of procedures reasonably adapted to avoid any such error"
- Not applicable to original creditors (definitional exclusion)

**5. Procedure / decision-maker:**
- No administrative exhaustion required
- Standard: Least sophisticated consumer (judicially created)
- Decision-maker: Court (federal or state)

**6. Consequences:**
Per § 1692k:
- Actual damages
- Statutory damages: Up to $1,000 per action (individual); up to lesser of $500,000 or 1% of net worth (class action)
- Attorney's fees and costs to prevailing plaintiff

**7. Forum / enforcer:**
- **Enforcer:** Private plaintiff (consumer); FTC; CFPB; state attorneys general
- **Forum:** Federal court (15 U.S.C. § 1692k(d)); state court (concurrent)
- **Venue:** District where violation occurred or defendant resides

**8. Interaction rules:**
- **Preemption/savings (§ 1692n):** Does not annul, alter, or affect state laws except to extent inconsistent; state law providing greater protection not inconsistent
- **Statute of limitations:** One year from date of violation (§ 1692k(d))
- **Cross-references:** § 1692a (definitions); § 1692k (remedies); § 1692l (administrative enforcement)

---

## Example: Scenario-Driven Brief (Mode B)

When a scenario is provided, prepend the Scenario Module before MAPS.

**Sample scenario:** A debt collector sent Consumer a letter stating "Pay within 10 days or we will sue" when the collector had no present intention to sue.

### Scenario Module

**Scenario synopsis:**
Debt collector sent collection letter to consumer threatening litigation ("Pay within 10 days or we will sue") without present intention to file suit.

**Issues framed as statutory questions:**
1. Does threatening litigation without present intent to sue constitute a "false, deceptive, or misleading representation" under § 1692e?
2. Specifically, does it violate § 1692e(5) ("threat to take any action that cannot legally be taken or that is not intended to be taken")?

**Relevant excerpts (verbatim):**

**§ 1692e (general prohibition):**
> "A debt collector may not use any false, deceptive, or misleading representation or means in connection with the collection of any debt."

**§ 1692e(5) (specific prohibition):**
> "The threat to take any action that cannot legally be taken or that is not intended to be taken."

**Application map (statute-to-facts):**

| Element | Fact Status | Analysis |
|---------|-------------|----------|
| "debt collector" | Fact needed | Need confirmation defendant meets § 1692a(6) definition |
| "false, deceptive, or misleading representation" | Met | Threat of action not intended to be taken |
| "in connection with collection of debt" | Met | Letter was collection communication |
| "threat to take action" | Met | "We will sue" is a threat |
| "not intended to be taken" | Met | Scenario states no present intention |

**Missing facts:** Confirmation that defendant is a "debt collector" under the statutory definition.

**Context map (where excerpts live):**
```
15 U.S.C. § 1692e(5)
  └─ § 1692e: False or misleading representations [prohibition]
      └─ (5): Threats of unintended action [specific violation]
```

**Not used but structurally important:**
- § 1692d (harassment or abuse) – not alleged
- § 1692f (unfair practices) – not alleged  
- § 1692g (validation notice requirements) – not at issue
- § 1692c (communication restrictions) – not at issue
