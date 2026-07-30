# ch4-unfairness-challenge

**Anchor:** Any × Ch IV × Art. 13 unfairness challenge. Most-used Ch IV instrument in practice: an enterprise on whom a data-related contractual term was unilaterally imposed challenges the term's validity. Art. 13 is the only Data Act provision that invalidates a B2B contract term ex post; the test is structured (general clause plus black-list plus grey-list) and the temporal scoping is highly specific.

**Routes from:**

- "Is this clause in my data-sharing contract enforceable under Art. 13?"
- "We were told to sign this; we had no negotiating power. Can we get the data clause struck down?"
- "Does Art. 13 apply to a contract we signed in 2024?"
- "Our customer is invoking Art. 13 against a term in their cloud contract. How do we respond?"
- "Identify the unfair terms in this B2B data-sharing agreement."

**Adjacent cards (route there instead if the facts indicate):**

- The challenge is to compliance with Art. 8 FRAND duties on a Ch III contract (not to unilaterally imposed unfairness): `ch3-frand-terms.md` (holder-side) or `ch3-compensation-challenge.md` (recipient-side).
- The challenge is forward-looking: the drafter wants to write the contract correctly the first time: `ch4-contract-drafting.md`.
- The unfair term is imposed by a B2C party (consumer-facing), not B2B: out of Data Act scope. Use the Unfair Contract Terms Directive (UCTD, Directive 93/13/EEC) regime. Note the asymmetry: Art. 13 does not catch one-sided micro-vs-SME terms imposed on consumers.

---

## Canonical fact pattern

Two enterprises have a B2B contract that includes a data-related term. The term concerns access to and use of data, or liability and remedies for breach or termination of data-related obligations (Art. 13(1)). The term was unilaterally imposed by one party on the other (Art. 13(6)). The party on whom the term was imposed is challenging the term's validity.

The contract may be a data-sharing agreement, a cloud services contract, a connected-product sale contract with data clauses, a logistics or industrial supply contract with telemetry-sharing terms, a financial-services contract with data-access provisions, or any other B2B contract containing data-related obligations. FAQ Q42a (Commission interpretation) confirms Ch IV applies to any contractual term concerning data access and use or data-related liability and remedies, regardless of whether data is the main subject of the contract.

The temporal scoping is decisive and often misanalysed. Contracts concluded after 12 September 2025 are caught from the day the Data Act applies. Contracts concluded on or before 12 September 2025 are caught only from 12 September 2027, and only if they are of indefinite duration or due to expire at least 10 years after entry into force (11 January 2024). Contracts that fall outside both windows are not subject to Art. 13.

---

## Critical disciplines

These three are load-bearing for any unfairness challenge. Hold all three.

- **Three nested tests.** The Art. 13 analysis is structured: (i) Art. 13(1) and (6) gateway (data-related term unilaterally imposed in B2B); (ii) Art. 13(2) carve-out (terms reflecting mandatory Union law are not unfair); (iii) substantive unfairness, which has three operative routes: Art. 13(3) general clause (grossly deviates from good commercial practice in data access and use, contrary to good faith and fair dealing), Art. 13(4) black-list (always unfair on the listed object or effect), Art. 13(5) grey-list (presumed unfair, rebuttable by the imposing party). Each route is independent; an unfair term on one route is unfair regardless of the others.
- **Temporal applicability is constitutive.** Art. 50 sets two windows. Outputs that apply Art. 13 to a contract outside both windows are wrong on a threshold question. FAQ Q42b (Commission interpretation) is the cleanest exposition; the regulation text is at Art. 50, fifth and sixth sub-paragraphs.
- **Severability is the default outcome.** Art. 13(7): where the unfair term is severable from the remaining terms, those remaining terms are binding. The unfair term falls; the contract survives. This shapes the remedy: the challenger asks the body or court to declare the term not binding, not to void the contract.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies and the contract is B2B (both parties are enterprises). Run the Art. 1(2)/(3) scope check; the Art. 1(6) carve-outs rarely affect Art. 13 (which is horizontal across the digital economy), but check them. Confirm at least one party is an enterprise on whom the term was imposed and the other is the imposing enterprise.

Confirm the temporal hook. Art. 50, fifth and sixth sub-paragraphs:

- Chapter IV applies to contracts concluded after 12 September 2025 (fifth sub-paragraph).
- Chapter IV applies from 12 September 2027 to contracts concluded on or before 12 September 2025, where those contracts are of indefinite duration or due to expire at least 10 years from 11 January 2024 (sixth sub-paragraph).

A contract concluded in (say) March 2026 is caught. A perpetual data-sharing agreement signed in May 2024 will be caught from 12 September 2027; until that date Art. 13 does not bite. A fixed-term contract signed in June 2025 expiring in June 2030 is not caught (concluded before 12 September 2025, not of indefinite duration, not expiring at least 10 years from 11 January 2024).

### Step 2: Chapter identification

Chapter IV. Art. 13 is the only operative provision. Art. 10 supplies the dispute settlement route; Art. 38 supplies the complaint procedure if a competent authority is involved.

Where the contract is also a Ch III contract (data sharing under Art. 5 or other Union or national law), Art. 8(2) creates an explicit cross-reference: a contractual term concerning data access and use or liability and remedies is not binding if it is unfair within Art. 13. The two chapters operate in parallel on the same term.

### Step 3: Role mapping

Required entity-by-entity mapping. Show as a table in the output.

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Imposing party | Variable: data holder, data recipient, provider of data processing service, customer, etc. | Variable | Bears burden under Art. 13(6) of showing the term was not unilaterally imposed |
| Party on whom term was imposed | Variable | Variable |  |
| Affected user or data subject (if any) |  |  | Art. 8(2) protects users' Ch II rights independently |

For Art. 13 specifically, the load-bearing distinction is between the imposing enterprise and the party on whom the term was imposed. Art. 13(6) places the burden of proof on the contracting party that supplied the term, and that party "may not argue that the term is an unfair contractual term." The Data Act roles (holder, recipient, provider, customer) matter less for the unfairness analysis than for parallel Ch II, III, or VI analyses on the same facts.

Record which party imposed the term and which received it; this is the burden-of-proof allocation under Art. 13(6).

### Step 4: Fact-category sorting

The unfairness analysis turns on facts about the term and the negotiation, not primarily on the data itself. Sort the facts along these lines.

- **Data-related vs not.** Art. 13(1) applies to terms concerning access to and use of data, or liability and remedies for breach or termination of data-related obligations. Terms with another subject matter (price for non-data services, product specifications, intellectual-property licensing of finished works) are outside Art. 13. Recital 60 confirms; FAQ Q42a (Commission interpretation) elaborates: a single contract can have mixed subject matter; only the data-related terms fall within Art. 13.
- **Unilaterally imposed vs negotiated.** Art. 13(6): a term is unilaterally imposed if supplied by one party and the other contracting party has not been able to influence its content despite an attempt to negotiate it. The party that supplied the term bears the burden of proof. Recital 59 anchors the take-it-or-leave-it characterisation; a term that was negotiated and subsequently agreed in an amended form is not unilaterally imposed.
- **Main subject matter vs not.** Art. 13(8): Art. 13 does not apply to contractual terms defining the main subject matter of the contract or to the adequacy of the price as against the data supplied in exchange. This is a narrow carve-out; it does not cover ancillary terms even where they affect price (for example, a price-variation clause is not the main subject matter for these purposes).
- **Mandatory Union law overlap.** Art. 13(2): a term that reflects mandatory provisions of Union law (or provisions that would apply if the contractual terms did not regulate the matter) is not unfair. A clause merely restating GDPR Art. 6 legal-basis requirements, for example, is not unfair on Art. 13 grounds.
- **Contract date.** Art. 50 temporal scoping. Record the conclusion date precisely and identify which window applies.

### Step 5: Limb-by-limb application of Art. 13

The substantive test runs in three routes; the challenger runs whichever fits, or all three in parallel.

1. **Art. 13(3) general clause.** A term is unfair "if it is of such a nature that its use grossly deviates from good commercial practice in data access and use, contrary to good faith and fair dealing." Recital 61 anchors the standard: "grossly deviating from good commercial practice would include, inter alia, objectively impairing the ability of the party upon whom the term has been unilaterally imposed to protect its legitimate commercial interest in the data in question." The test is high (grossly), the comparator is "good commercial practice in data access and use", and the qualifier is good faith and fair dealing.
2. **Art. 13(4) black-list (always unfair on the listed object or effect).** A term whose object or effect is to:
   - (a) exclude or limit the liability of the imposing party for intentional acts or gross negligence;
   - (b) exclude the remedies available to the imposed-upon party for non-performance, or the liability of the imposing party for breach;
   - (c) give the imposing party the exclusive right to determine whether the data supplied are in conformity with the contract or to interpret any contractual term.
   The black-list is closed and final. A term hitting any of (a), (b), or (c) by object or effect is unfair without further analysis. The "object or effect" formulation captures terms that achieve the result indirectly.
3. **Art. 13(5) grey-list (presumed unfair, rebuttable).** A term whose object or effect is to:
   - (a) inappropriately limit remedies or extend liability of the imposed-upon party;
   - (b) allow the imposing party to access and use the imposed-upon party's data in a manner significantly detrimental to its legitimate interests, in particular for commercially sensitive data or data protected by trade secrets or IP;
   - (c) prevent the imposed-upon party from using the data it provided or generated during the contract, or limit such use to deprive it of adequate exploitation of the data's value;
   - (d) prevent the imposed-upon party from terminating the contract within a reasonable period;
   - (e) prevent the imposed-upon party from obtaining a copy of the data it provided or generated during the contract or within a reasonable period after termination;
   - (f) enable the imposing party to terminate at unreasonably short notice, taking into account the imposed-upon party's reasonable possibility to switch and the financial detriment, except where there are serious grounds;
   - (g) enable the imposing party to substantially change price or any other substantive condition related to the nature, format, quality, or quantity of the data to be shared, where no valid reason and no right of the other party to terminate the contract is specified.
   The Art. 13(5)(g) point has a sub-proviso for indeterminate-duration contracts: the imposing party may reserve the right to unilaterally change terms if the contract specifies a valid reason, the imposing party gives reasonable notice, and the other party is free to terminate at no cost in the case of a change.
   Recital 62: the imposing party can rebut the presumption by demonstrating that the listed term is not unfair in the specific case. Without rebuttal, the term is unfair.
4. **Art. 13(2) carve-out.** Terms reflecting mandatory Union law (or default Union law) are not unfair. Apply only after the term has been characterised as data-related and unilaterally imposed; the carve-out then defeats the unfairness on the merits.
5. **Art. 13(6) burden allocation.** The imposing party bears the burden of showing the term was not unilaterally imposed. The imposing party may not argue that the term is an unfair contractual term (i.e., the imposing party cannot use the unfairness regime as a sword to invalidate its own drafting; only the imposed-upon party can).
6. **Art. 13(7) severability.** Where the unfair term is severable from the rest, the rest of the contract remains binding. Severability is the default outcome; the contract survives. Where the unfair term is the linchpin of the contract structure, the imposing party may seek to argue non-severability, with the result that the contract falls in full; that is rare in practice.
7. **Art. 13(8) main-subject-matter carve-out.** Art. 13 does not apply to terms defining the main subject matter of the contract or to the adequacy of the price as against the data supplied in exchange. Narrow.
8. **Art. 13(9) anti-derogation.** The parties may not exclude the application of Art. 13, derogate from it, or vary its effects. A choice-of-law clause purporting to displace Art. 13 is itself not binding.

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. A term reflecting mandatory GDPR provisions (e.g. Art. 5 principles, Art. 6 legal basis requirements) falls within the Art. 13(2) carve-out. A term derogating from GDPR (e.g. purporting to make the imposed-upon party absorb the imposing party's controller liability) is independently invalid under GDPR; the Art. 13 analysis is in parallel.
- **Trade Secrets Directive overlay (loaded if any data is claimed as trade-secret).** Read `references/gates/trade-secrets-directive.md`. Art. 13(5)(b) specifically calls out commercially sensitive data, trade secrets, and IP-protected data. A term allowing the imposing party to access and use the imposed-upon party's trade-secret data in a manner significantly detrimental is presumptively unfair.
- **Sectoral lex specialis (warn-only).** Run `references/gates/sectoral-lex-specialis.md` if the contract is in a regulated sector. Sectoral unfair-terms regimes may apply in parallel (for example, DORA contractual safeguards in financial services, or the medical device contractual requirements).
- **Member State implementing law (warn-only).** Art. 38 complaint procedures and Art. 10 dispute settlement bodies are Member State level. Run `references/gates/member-state.md` to confirm the right body or authority.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 13 of Regulation (EU) 2023/2854 (Data Act) governs. Verbatim text at `sources/regulation-2023-2854.md` Art. 13 (lines 917-958); operative recitals at Recitals 58-62. Temporal scoping at Art. 50 (lines 1711-1727).
- **Proposed amendment under Digital Omnibus.** COM(2025) 833 final does not materially alter Art. 13. The proposal does affect adjacent Ch IV-touching matters (e.g. Art. 25 early-termination penalties in Ch VI; the consolidation absorbing other instruments) but the Art. 13 unfairness test stands. See `sources/digital-omnibus-amendments-tracker.md`.

---

## Decision point

After Steps 5 and 6, the analysis yields one of four paths.

1. **Term hits the black-list at Art. 13(4).** Strongest case. Produce the unfairness challenge letter (Output Path 1 below) citing the specific black-list point and operative effect. No rebuttal available to the imposing party on the unfairness limb; only the gateway questions (Art. 13(2) mandatory law; Art. 13(6) negotiation; Art. 13(8) main subject; Art. 50 temporal) remain disputable.
2. **Term hits the grey-list at Art. 13(5).** Presumption of unfairness, rebuttable by the imposing party. Produce the unfairness challenge letter (Output Path 1) citing the specific grey-list point and operative effect. Anticipate the rebuttal argument and address it.
3. **Term hits the general clause at Art. 13(3) only.** Harder case; the challenge has to show the term grossly deviates from good commercial practice in data access and use. Produce the analysis (Output Path 2 below) with the comparator references and the Recital 61 "objectively impairing legitimate commercial interest" anchor.
4. **Contract is outside the Art. 50 temporal scope, or term is not data-related, or the carve-outs apply.** No challenge under Art. 13. Produce a short note (Output Path 3 below) explaining the temporal or scope defect. UCTD or national law may apply on different grounds; flag and route to specialist counsel.

---

## Output skeleton: Path 1 (black-list or grey-list challenge letter)

Formal letter. Markdown. Lead with the operative effect.

Structure:

```
[Challenger letterhead placeholder]

To: [Imposing party]
Date: [Date]
Subject: Notice of unfairness of contractual term under Article 13 of
         Regulation (EU) 2023/2854 (Data Act)

1. The contract
   [Identification of the contract: date of conclusion, parties, brief
   subject. Confirm Art. 50 temporal scope applies: either concluded
   after 12 September 2025 (caught immediately from Data Act
   application date), or concluded on or before 12 September 2025 and
   either of indefinite duration or expiring at least 10 years from
   11 January 2024 (caught from 12 September 2027).]

2. The challenged term
   > [Quote the challenged term verbatim.]

3. The term is data-related
   [Brief statement that the term concerns access to and use of data,
   or liability and remedies for breach or termination of data-related
   obligations (Art. 13(1)). Cite Recital 60 and FAQ Q42a (Commission
   interpretation) for the proposition that a contract's primary
   subject need not be data for the term to be caught.]

4. The term was unilaterally imposed
   [Brief account of the negotiation. Attempt to negotiate the term;
   inability to influence its content (Art. 13(6)). The imposing party
   bears the burden of showing the term was not unilaterally imposed.]

5. Art. 13(2) carve-out does not apply
   [Brief statement that the term does not reflect mandatory provisions
   of Union law and would not apply if the term did not regulate the
   matter.]

6. The term is unfair
   6.1 Operative basis: [Art. 13(4)(N) or Art. 13(5)(N)].
   6.2 Object or effect: [exact mapping of the term's wording onto
       the listed point].
   6.3 If Art. 13(4): the term is unfair without further analysis.
       The presumption is unrebuttable.
       If Art. 13(5): the term is presumed unfair; the imposing party
       bears the rebuttal burden under Recital 62. [Anticipated
       rebuttal addressed if facts are known.]

7. Consequence
   The challenged term is not binding on the challenger under Art.
   13(1). Under Art. 13(7), the remaining terms of the contract
   continue to bind both parties as the challenged term is severable.

8. Demand
   [The challenger requests that the imposing party withdraw the term
   from the contract or treat it as not binding. The challenger
   reserves the right to refer the matter to a certified dispute
   settlement body under Art. 10 (which under Art. 10(1) covers
   disputes relating to fairness of contractual terms in Ch IV), to
   the competent authority designated under Art. 37 of the Member
   State of establishment, or to a court or tribunal under Art. 10(13).]

[Signature block placeholder]
```

---

## Output skeleton: Path 2 (general-clause challenge analysis)

Internal memorandum. Markdown. The general clause challenge is fact-intensive; the output structures the argument rather than producing a finished letter.

```
Memorandum: Art. 13(3) general-clause unfairness analysis

1. The challenged term
   [Quote verbatim.]

2. Gateway tests
   2.1 Data-related: [Art. 13(1) analysis].
   2.2 Unilaterally imposed: [Art. 13(6) negotiation account].
   2.3 No Art. 13(2) mandatory-law carve-out: [analysis].
   2.4 Not main subject matter: [Art. 13(8) analysis].
   2.5 Temporal scope: [Art. 50 analysis].

3. Substantive Art. 13(3) test
   3.1 Comparator: good commercial practice in data access and use.
       [Identify the comparator: industry standard terms, model
       contractual terms recommended by the Commission, sector-
       specific data-sharing codes, or other reference points.]
   3.2 Gross deviation: [analysis of how the challenged term deviates
       from the comparator, with specific points of departure].
   3.3 Contrary to good faith and fair dealing: [analysis].
   3.4 Recital 61 anchor: [whether and how the term objectively impairs
       the imposed-upon party's ability to protect its legitimate
       commercial interest in the data].

4. Strength assessment
   [Honest assessment of the strength of the general-clause argument.
   General-clause challenges are harder than black-list or grey-list
   challenges. The bar (grossly deviates) is high.]

5. Strategic options
   [Direct demand to the imposing party; Art. 10 dispute settlement;
   Art. 37 competent authority complaint; court proceedings under
   Art. 10(13). The choice depends on the strength of the case, the
   commercial relationship, and the value at stake.]
```

---

## Output skeleton: Path 3 (no Art. 13 hook)

Very short response. The Art. 13 framework does not apply.

```
Art. 13 of the Data Act does not bite on this term.

[Identify the defect: contract outside Art. 50 temporal scope (e.g.
fixed-term contract signed June 2024, expiring before 11 January 2034,
not of indefinite duration); or term is not data-related (e.g. price
of non-data services); or Art. 13(8) main-subject-matter carve-out
applies; or Art. 13(2) carve-out applies (term reflects mandatory
Union law).]

Other regimes may be available depending on the facts: the Unfair
Contract Terms Directive (Directive 93/13/EEC) applies to B2C
contracts but not to B2B; national contract law on unconscionability
or good faith may apply; competition law may catch abusive terms
imposed by a dominant undertaking. The Data Act Art. 13 route is not
the operative remedy here.
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 13 in full (always); Art. 8(2) (Art. 13 cross-reference if the contract is also a Ch III contract); Art. 10 (dispute settlement); Art. 12(2) (anti-derogation for Ch III contracts); Art. 50 (temporal scoping, fifth and sixth sub-paragraphs).
- `sources/regulation-2023-2854.md` Recital 58 (rationale for unfairness control); Recital 59 (unilaterally imposed; take-it-or-leave-it); Recital 60 (scope of data-related terms); Recital 61 (grossly deviates; objectively impairing legitimate commercial interest); Recital 62 (black-list, grey-list, severability).
- `sources/faq-v1-4.md` Q41 (Commission interpretation on SME benefit from Ch IV); Q42 (Commission interpretation on assessment procedure under Art. 13); Q42a (Commission interpretation on contracts with mixed subject matter); Q42b (Commission interpretation on temporal scoping). Frame as Commission interpretation.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded if personal data in scope; Art. 13(2) interaction).
- `references/gates/trade-secrets-directive.md` (loaded if trade-secret data is in scope; Art. 13(5)(b) interaction).
- `references/gates/sectoral-lex-specialis.md` (warn-only; sectoral unfair-terms regimes may apply in parallel).
- `references/gates/member-state.md` (warn-only; for Art. 10 body and Art. 37/38 authority).
- `references/gotchas.md` entry 4 ("without undue delay" has no numeric SLA), 19 (FAQ is non-authoritative), 20 (Digital Omnibus is a proposal). Check on each.
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (no material Art. 13 amendments).
- Adjacent card: `ch4-contract-drafting.md` (forward-looking application of the same article).

---

## Drafter notes

Operational observations for using this card. Three only.

- **Temporal scoping is the first thing to verify, not the last.** A challenge to a 2024 fixed-term contract that expires in 2028 is dead on Art. 50 grounds, regardless of how unfair the term is. Pin the conclusion date and the duration before drafting anything substantive. FAQ Q42b is the cleanest exposition; the regulation text is Art. 50, fifth and sixth sub-paragraphs.
- **Art. 13(4) wins are stronger than Art. 13(5) wins.** The black-list is unrebuttable on the unfairness limb; the imposing party can only attack the gateway questions (data-related, unilaterally imposed, temporal scope, Art. 13(2) carve-out). The grey-list is rebuttable, and Recital 62 gives the imposing party a real opportunity. Where the facts support a 13(4) characterisation, lead with 13(4) and treat 13(5) as a fallback.
- **Severability is the friend of the imposed-upon party.** Art. 13(7) is the default outcome: the unfair term falls, the contract survives. The challenger keeps the benefit of the contract minus the unfair term. The imposing party that argues non-severability (to bring down the whole contract) typically does so as a tactical threat; in most B2B data-sharing contracts the unfair term is severable in fact, and the challenger should expressly invoke Art. 13(7) in the demand to forestall the imposing party's "all or nothing" tactic.
