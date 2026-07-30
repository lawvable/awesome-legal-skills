# ch4-contract-drafting

**Anchor:** Drafter × Ch IV × pre-contract review. Forward-looking Art. 13 application: drafting B2B data-related contractual terms in a way that survives the black-list at Art. 13(4) and the grey-list at Art. 13(5). The drafter holds the pen on a contract that will be subject to Art. 13 either from conclusion (post-12 September 2025) or from 12 September 2027 (pre-existing indefinite or long-duration contracts). The card avoids the post-execution challenge route by drafting it out at source.

**Routes from:**

- "Review this draft data-sharing contract against Art. 13 before we sign."
- "We are renegotiating a long-running customer contract; what do we need to change to be Art. 13-compliant by 12 September 2027?"
- "Help me draft a data-licensing clause that will not be struck down under Art. 13(4) or (5)."
- "Audit our standard B2B contract template for unfairness risk under the Data Act."
- "Which of our termination, IP, and pricing clauses are at risk under Art. 13(5)?"

**Adjacent cards (route there instead if the facts indicate):**

- The contract has been signed and one party is challenging a term: `ch4-unfairness-challenge.md`.
- The drafting is for a Ch III mandatory sharing contract (Art. 5 or other law trigger) and the focus is FRAND terms under Art. 8 / Art. 9: `ch3-frand-terms.md`.
- The drafting is for a Ch VI cloud services contract (switching, exit, term, non-amendment): not yet drafted; route to `ch6-cloud-contract-drafting.md` when available. Art. 13 still applies to data-related terms in cloud contracts; this card covers the Art. 13 layer.

---

## Canonical fact pattern

A drafter (in-house counsel, external counsel, or a contracts team) is preparing or reviewing a B2B data-related contract. The contract may be a data-sharing agreement, a connected-product sale contract with data clauses, a cloud services contract, a logistics or industrial supply contract with telemetry-sharing, a financial-services contract with data-access provisions, or any other B2B contract containing terms about access to and use of data or liability and remedies for breach or termination of data-related obligations.

The drafter is acting for either side: the enterprise that proposes the standard form (imposer-side drafting, with exposure to Art. 13(4) and (5) invalidation), or the enterprise that receives the standard form (imposed-upon-side drafting, with the inverse interest in protecting its Art. 13 rights and not pre-conceding them). The card serves both perspectives because the substantive operative content of Art. 13 is the same; only the strategic posture changes.

The contract may be concluded after 12 September 2025 (caught by Art. 13 immediately from the Data Act application date) or before that date with effect from 12 September 2027 (caught later, if indefinite or expiring at least 10 years from 11 January 2024). The drafter handles the appropriate window.

---

## Critical disciplines

These three are load-bearing for any Art. 13 drafting. Hold all three.

- **Three nested tests, applied to every data-related clause.** The drafter runs each clause through (i) the gateway (data-related, B2B), (ii) the Art. 13(2) mandatory-law carve-out, (iii) the substantive routes (general clause; black-list; grey-list). The black-list at Art. 13(4) is unrebuttable: a clause whose object or effect falls within (a), (b), or (c) is unfair regardless of commercial justification. The grey-list at Art. 13(5) is rebuttable but the drafter cannot assume a rebuttal will succeed; safer drafting avoids the grey-list entirely.
- **Art. 13 is B2B only.** The unfairness control does not apply to consumer contracts (those run on Directive 93/13/EEC, the Unfair Contract Terms Directive (UCTD), and on national consumer law). A drafter producing a contract that will be issued to consumers needs the UCTD analysis, not Art. 13. Where the drafter is operating a B2B and B2C contract template in parallel, the two regimes are different and the drafting needs both. Misapplying Art. 13 to consumer contracts (or, more commonly, assuming Art. 13 covers all customer-facing terms) is a category error.
- **Anti-derogation is express (Art. 13(9)).** The parties cannot exclude, derogate from, or vary the effect of Art. 13. Choice-of-law clauses purporting to do so are themselves not binding. The drafter cannot draft around Art. 13; the drafter has to draft within it.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check; Art. 13 is horizontal across the EU economy and the Art. 1(6) carve-outs rarely apply, but the check is cheap. Confirm both parties are enterprises. Confirm the contract contains terms concerning access to and use of data or liability and remedies for data-related obligations.

Confirm the temporal hook. Art. 50, fifth and sixth sub-paragraphs:

- Contracts concluded after 12 September 2025: Art. 13 applies immediately.
- Contracts concluded on or before 12 September 2025 that are of indefinite duration, or that expire at least 10 years from 11 January 2024: Art. 13 applies from 12 September 2027. The drafter has until 12 September 2027 to renegotiate. FAQ Q42b (Commission interpretation) confirms the renegotiation rationale.

For new drafting today, the contract will be concluded after 12 September 2025; Art. 13 applies from execution.

### Step 2: Chapter identification

Chapter IV. Art. 13 is the operative provision; Art. 10 is the dispute settlement option once a dispute crystallises (relevant to the drafter only as a forum-selection consideration).

Where the contract is also a Ch III contract (data sharing under Art. 5 or other Union or national law), Art. 8(2) cross-references Art. 13 expressly. Where the contract is a Ch VI cloud services contract, Art. 25(1) and 25(2) impose specific contract content requirements; the Art. 13 layer applies to the data-related terms inside the cloud contract. Where the contract is a Ch II connected-product contract, Art. 8(2) again applies to the data terms.

### Step 3: Role mapping

Required entity-by-entity mapping. Show as a table in the output (or in the drafting brief).

| Entity | Data Act role | GDPR role (if personal data in scope) | Art. 13 posture |
|--------|---------------|----------------------------------------|-----------------|
| Drafter's client (imposer or imposed-upon, depending) | Variable: data holder, recipient, provider, customer, etc. | Variable | Imposer if standard form; imposed-upon if accepting the counterparty's standard form |
| Counterparty | Variable | Variable | Opposite of the drafter's client |
| Affected user or data subject (if any) |  |  | Indirectly protected through Art. 8(2) and Art. 12(2) anti-derogation |

For Art. 13 specifically, the load-bearing question is: which party will be "the contracting party that supplied the contractual term" in the meaning of Art. 13(6)? That party bears the burden of showing the term was not unilaterally imposed. Record this on the drafting brief.

Note the consumer-vs-enterprise check on the role mapping. Art. 13 does not catch one-sided terms inflicted on consumers by enterprises; that is UCTD territory. If the contract has consumer-facing variants, the role mapping splits and the analysis runs in two parallel tracks.

### Step 4: Fact-category sorting

The drafting analysis turns on classifying each clause along these lines. Run the analysis clause by clause, not as a single contract-wide pass.

- **Data-related vs not.** Art. 13(1) catches terms concerning access to and use of data or liability and remedies for data-related obligations. Recital 60 and FAQ Q42a (Commission interpretation) extend this to any data-related term in any contract, not only contracts whose main subject is data. Clauses about non-data subject matter (price for non-data services, product specifications, IP licensing of finished works) are outside Art. 13. The drafter identifies which clauses are caught.
- **Imposed vs negotiated.** Art. 13(6): a term is unilaterally imposed if supplied by one party and the other party has not been able to influence its content despite attempting to negotiate it. Where the drafter is producing a standard form, the burden of proving non-imposition will lie on the drafter's client. Where the drafter is producing a bespoke contract that both parties genuinely negotiated, the term is not unilaterally imposed and Art. 13 does not bite at all. The drafter knows which is which.
- **Main subject matter vs not.** Art. 13(8): Art. 13 does not apply to terms defining the main subject matter or to the adequacy of the price as against the data supplied in exchange. The carve-out is narrow.
- **Mandatory Union law overlap.** Art. 13(2): a term reflecting mandatory Union law or default Union law is not unfair. The drafter can use this productively: where a clause merely restates a mandatory rule (GDPR Art. 5 principles, for example), the unfairness risk is zero on that limb.
- **Contract date and duration.** Art. 50 temporal scoping. For new drafting today, this is always "concluded after 12 September 2025" and Art. 13 applies immediately. For renegotiations of pre-existing contracts, the drafter sets the new conclusion date and treats the renegotiated contract as a new contract under Art. 50.

### Step 5: Limb-by-limb application of Art. 13 to the draft

The drafter runs each clause through the three substantive routes. The output is a redlined contract or a drafting memorandum identifying clauses that need work.

1. **Art. 13(4) black-list scan.** For each clause, ask whether its object or effect is:
   - (a) to exclude or limit the imposing party's liability for intentional acts or gross negligence. Common drafting traps: liability-cap clauses with no carve-out for intent or gross negligence; clauses purporting to exclude all liability for misuse of data the imposer accesses; arbitration or limitation clauses that effectively immunise the imposer for serious breach.
   - (b) to exclude the imposed-upon party's remedies for non-performance, or the imposing party's liability for breach. Common drafting traps: "no consequential damages" clauses applied to data breaches that cause real loss; sole-remedy clauses that limit the imposed-upon party to terminate-only with no damages; force-majeure or sole-discretion clauses that wipe out remedies for breach.
   - (c) to give the imposing party the exclusive right to determine conformity of data with the contract or to interpret any contractual term. Common drafting traps: "imposing party's good-faith determination shall be conclusive" clauses; "imposing party shall determine in its sole discretion whether the data meets the specifications" clauses; "any dispute over interpretation shall be resolved by the imposing party" clauses.
   The black-list is unrebuttable. A clause hitting any of (a)-(c) by object or effect must be rewritten. The drafter cannot rely on "but commercially we need this"; commercial need does not rebut Art. 13(4).

2. **Art. 13(5) grey-list scan.** For each clause, ask whether its object or effect is:
   - (a) to inappropriately limit remedies or extend the imposed-upon party's liability. Drafting risk: asymmetric indemnities; one-sided liability allocations beyond a reasonable proportionality.
   - (b) to allow the imposing party to access and use the imposed-upon party's data in a manner significantly detrimental to the imposed-upon party's legitimate interests, particularly trade-secret or IP-protected data. Drafting risk: broad data-use grants for the imposing party with no scope limits; "any data we collect under this contract may be used for any purpose" clauses; absence of trade-secret carve-outs where the data is commercially sensitive.
   - (c) to prevent the imposed-upon party from using its own data or to limit such use that the party cannot exploit the data's value. Drafting risk: exclusivity clauses for the imposing party that lock out the data-generating party; non-compete or non-use clauses on data generated by the imposed-upon party's connected products.
   - (d) to prevent the imposed-upon party from terminating the contract within a reasonable period. Drafting risk: long lock-in periods with no exit; termination only on six months' notice in a contract with three-month service cycles.
   - (e) to prevent the imposed-upon party from obtaining a copy of its own data during the contract or within a reasonable period after termination. Drafting risk: data ownership clauses that strip the imposed-upon party of access to data it generated; exit clauses with no data-export obligation.
   - (f) to enable the imposing party to terminate at unreasonably short notice. Drafting risk: short termination notice in service contracts where the imposed-upon party has switching costs; "termination for convenience on 7 days' notice" in a multi-year service relationship.
   - (g) to enable the imposing party to substantially change the price or substantive condition related to nature, format, quality, or quantity of data, without a valid reason and without the imposed-upon party's termination right. Drafting risk: unilateral price-change clauses; unilateral specification-change clauses. The sub-proviso for indeterminate-duration contracts requires: a valid reason specified in the contract; reasonable notice; and the other party's freedom to terminate at no cost in the event of change.
   The grey-list is rebuttable but only by demonstrating that the listed term is not unfair in the specific case (Recital 62). The drafter cannot assume the rebuttal will succeed. Safer drafting avoids the grey-list.

3. **Art. 13(3) general clause check.** Even where a clause is not on the black-list or grey-list, the drafter checks against the general clause: does the clause grossly deviate from good commercial practice in data access and use, contrary to good faith and fair dealing? Recital 61: grossly deviating includes "objectively impairing the ability of the party upon whom the term has been unilaterally imposed to protect its legitimate commercial interest in the data in question." The general clause is the safety net; it catches clauses that escape the listed categories but still cross the line.

4. **Art. 13(2) carve-out use.** Where a clause merely restates mandatory Union law, the drafter can label it as such; that defeats the unfairness analysis on the merits. This is useful for GDPR-mandated clauses (legal basis, data-subject rights, breach notification), for sectoral mandatory provisions (DORA contractual safeguards, MDR data-sharing obligations), and for Data Act-mandated provisions themselves (Ch III FRAND duties under Art. 8 are mandatory, so a clause restating them is not unfair).

5. **Art. 13(6) negotiability evidence.** Where the drafter's client is the imposer, build the evidentiary record that the term was open to negotiation. Recital 59: a term that was negotiated and subsequently agreed in an amended form is not unilaterally imposed. The drafter can structure the negotiation process (issue redlines, accept amendments, document the back-and-forth) so the imposer can later show the term was negotiable. Empty markup of a standard form, with no substantive negotiation, will not suffice.

6. **Art. 13(7) severability drafting.** Include a severability clause that survives in the case of a single-term invalidation. The default outcome under Art. 13(7) is that the contract continues without the unfair term; the drafter can confirm that intent expressly. Severability protects the imposer (who keeps the rest of the contract) and the imposed-upon party (who keeps the benefit minus the unfair term).

7. **Art. 13(8) main-subject-matter framing.** Where a clause genuinely defines the main subject matter (the price for the data in exchange, the data item to be supplied), labelling it as such may insulate it from Art. 13. Use sparingly and only where genuine; the carve-out is narrow and a court or dispute body will read it strictly.

8. **Art. 13(9) anti-derogation acknowledgement.** Do not include a choice-of-law clause purporting to displace Art. 13. Do not include a clause stating "the parties agree Art. 13 does not apply"; such a clause is itself not binding.

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. A data-related clause must also be GDPR-compliant; an Art. 13-compliant clause that violates GDPR is invalid on a separate ground. The Art. 13(2) carve-out is useful for clauses restating mandatory GDPR provisions.
- **Trade Secrets Directive overlay (loaded if any data is claimed as trade-secret).** Read `references/gates/trade-secrets-directive.md`. Art. 13(5)(b) singles out commercially sensitive data, trade secrets, and IP-protected data. Where the imposed-upon party's data is trade-secret protected, broad data-use grants for the imposer are presumptively unfair.
- **UCTD overlay (warn-only).** If the contract or any variant is consumer-facing, run UCTD (Directive 93/13/EEC) in parallel. Art. 13 does not catch B2C; UCTD does. The two regimes have different operative content; do not assume Art. 13-compliant drafting is UCTD-compliant.
- **Sectoral lex specialis (warn-only).** Run `references/gates/sectoral-lex-specialis.md` if the contract is in a regulated sector. Sectoral mandatory contract content may overlap with Art. 13 either positively (Art. 13(2) carve-out useful) or negatively (sectoral law imposes additional fairness or balance requirements).
- **Member State implementing law (warn-only).** Art. 38 complaint procedures are Member State-level; the drafter may consider forum-selection in light of likely complaint routes. Run `references/gates/member-state.md`.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 13 of Regulation (EU) 2023/2854 (Data Act) governs. Verbatim text at `sources/regulation-2023-2854.md` Art. 13 (lines 917-958); operative recitals at Recitals 58-62. Temporal scoping at Art. 50.
- **Proposed amendment under Digital Omnibus.** COM(2025) 833 final does not materially alter Art. 13 itself. The proposal touches adjacent Ch IV matters (Art. 25 early-termination penalties in Ch VI). The drafter checks `sources/digital-omnibus-amendments-tracker.md` at the start of any new drafting cycle; if any Art. 13-affecting amendment is adopted between drafting and execution, the drafter updates.

The output cites current law as operative.

---

## Decision point

After Steps 5 and 6, the drafting analysis yields one of three paths.

1. **Draft is clean.** All data-related clauses pass the black-list, grey-list, and general-clause checks. Produce the clean-bill confirmation (Output Path 1 below) with a short note flagging any latent risks (for example, clauses that are not technically on the grey-list but sit close to it).
2. **Draft has clauses to rewrite.** One or more clauses hit the black-list, hit the grey-list without a strong rebuttal argument, or risk the general clause. Produce the redlined draft with annotations (Output Path 2 below).
3. **Draft is the wrong instrument.** The intended contract is consumer-facing (use UCTD analysis), the contract has no data-related terms (Art. 13 does not bite), or the contract is outside the Art. 50 temporal window (e.g. fixed-term contract pre-12 September 2025 with no indefinite-or-long-duration extension). Produce a short note (Output Path 3 below) explaining the scope or scoping defect.

---

## Output skeleton: Path 1 (clean-bill review note)

Short memorandum. Markdown. Confirms the draft passes Art. 13.

```
Memorandum: Art. 13 review of [contract identifier]

The draft data-related contract reviewed on [date] is consistent with
Art. 13 of Regulation (EU) 2023/2854 (Data Act). The substantive
review covered the data-related clauses identified in section 2 below.

1. Scope confirmation
   1.1 B2B contract: confirmed; both parties are enterprises.
   1.2 Data-related terms: identified in section 2.
   1.3 Temporal scope: contract to be concluded on [date]; Art. 13
       applies from execution.

2. Data-related clauses identified
   [List of clause references and brief descriptions: data access
   scope; data use scope; liability for data breaches; termination
   data return; etc.]

3. Black-list (Art. 13(4)) check: passed
   [Brief account of each clause against Art. 13(4)(a), (b), (c).]

4. Grey-list (Art. 13(5)) check: passed
   [Brief account of each clause against Art. 13(5)(a)-(g). Where a
   clause is close to but does not hit a grey-list point, flag the
   proximity.]

5. General clause (Art. 13(3)) check: passed
   [Brief account of why the contract does not grossly deviate from
   good commercial practice in data access and use.]

6. Latent risks
   [Any clauses that sit close to the grey-list or general clause and
   may attract challenge if commercial conditions change. The drafter's
   client should be aware of these even though the current drafting is
   clean.]

7. Recommendation
   The draft may be executed as drafted, subject to any further
   commercial review. Severability clause [identifier] is included and
   covers the Art. 13(7) default outcome.
```

---

## Output skeleton: Path 2 (redlined draft with annotations)

Annotated draft. Markdown. The drafter produces specific redlines on the failing clauses.

```
Memorandum: Art. 13 redlines on [contract identifier]

The following clauses in the draft data-related contract are at risk
under Art. 13 of Regulation (EU) 2023/2854 (Data Act). Redlines and
explanatory notes below.

Clause [N]: [Heading or topic]
   Current text:
   > [Quote verbatim.]
   Risk: [Art. 13(4)(N) black-list / Art. 13(5)(N) grey-list / Art.
   13(3) general clause]. [One- or two-sentence explanation, with
   operative basis cited.]
   Proposed text:
   > [Replacement clause that addresses the failure while preserving
   > the commercial purpose where possible.]
   Notes: [Brief justification for the replacement; alternative
   formulations if the client prefers; any commercial trade-offs.]

[Repeat for each at-risk clause.]

Cross-cutting observations
   [Patterns across the draft that the drafter should note: for
   example, asymmetric drafting throughout; absence of severability
   clause; weak negotiability record; etc.]

Recommendation
   [Specific next steps: incorporate redlines and re-execute; share
   redlined version with counterparty as a renegotiation marker;
   document the back-and-forth to build Art. 13(6) negotiability
   evidence; etc.]
```

---

## Output skeleton: Path 3 (wrong instrument)

Very short response. Identifies the scoping defect.

```
Art. 13 of the Data Act is not the operative instrument here.

[Identify the defect: contract is consumer-facing (UCTD applies, not
Art. 13); contract has no data-related terms (Art. 13(1) gateway not
met); contract is outside Art. 50 temporal scope; contract is wholly
within the Art. 13(8) main-subject-matter carve-out; or all parties to
the contract are public sector bodies (Ch IV is B2B in commercial
practice, though the Data Act does not formally exclude public sector
contracts from Art. 13).]

[Brief note on the operative regime: UCTD analysis (Directive
93/13/EEC) for consumer contracts; national contract law on
unconscionability or good faith; sectoral fairness rules where
applicable.]
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 13 in full (always); Art. 8(2) (where the contract is also Ch III); Art. 10 (dispute settlement; relevant to forum selection); Art. 12(2) (anti-derogation if Ch III is also engaged); Art. 50 (temporal scoping).
- `sources/regulation-2023-2854.md` Recital 58 (rationale); Recital 59 (unilaterally imposed; take-it-or-leave-it); Recital 60 (scope of data-related terms); Recital 61 (grossly deviates standard; legitimate commercial interest); Recital 62 (black-list, grey-list, severability; rebuttal opportunity).
- `sources/faq-v1-4.md` Q41 (Commission interpretation on SME benefit from Ch IV); Q42 (Commission interpretation on assessment procedure); Q42a (Commission interpretation on mixed-subject contracts); Q42b (Commission interpretation on temporal scoping). Frame as Commission interpretation.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded if personal data in scope).
- `references/gates/trade-secrets-directive.md` (loaded if trade-secret data is in scope; Art. 13(5)(b) interaction).
- `references/gates/sectoral-lex-specialis.md` (warn-only).
- `references/gates/member-state.md` (warn-only).
- `references/gotchas.md` entries 4 ("without undue delay" has no numeric SLA), 19 (FAQ is non-authoritative), 20 (Digital Omnibus is a proposal). Check on each.
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (no material Art. 13 amendments; re-check on every new drafting cycle).
- Adjacent card: `ch4-unfairness-challenge.md` (post-execution challenge to the same kind of term).

---

## Drafter notes

Operational observations for using this card. Three only.

- **Build the negotiability evidence at drafting, not at challenge.** Where the drafter's client is the imposer of a standard form, the burden of showing the term was not unilaterally imposed will fall on the client under Art. 13(6). The strongest evidence is a documented redline exchange and substantive concessions on at least some terms. A drafter who issues a standard form, refuses every counterparty redline, and then asks counsel to defend the contract under Art. 13(6) will have lost the case on the burden allocation. Structure the negotiation process so the back-and-forth is on record.
- **The grey-list bites hardest on long-running standard contracts.** Art. 13(5)(d) (no termination in reasonable period), (f) (unreasonably short termination by the imposing party), and (g) (unilateral price or condition changes) are common drafting features of long-running B2B service contracts. The drafter should be sceptical of clauses that say "the imposing party may change [X] on N days' notice" without a corresponding right of the imposed-upon party to terminate at no cost. The sub-proviso to Art. 13(5)(g) for indeterminate-duration contracts is the safe-harbour template for unilateral-change clauses; use it.
- **Art. 13(2) is a productive carve-out, not just a defensive one.** Where a clause restates mandatory Union law, label it as such. GDPR clauses, sectoral mandatory clauses (DORA, MDR, etc.), and Data Act-mandatory clauses themselves all qualify. The drafter can build a contract structure where most of the at-risk surface area is Art. 13(2)-carved-out, leaving the genuinely commercial terms (which are inherently negotiable) to bear the Art. 13 scrutiny. This is sound drafting strategy; it is not gaming the regulation.
