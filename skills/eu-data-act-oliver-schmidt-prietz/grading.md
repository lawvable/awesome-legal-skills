# Grading rubric for eu-data-act eval fixtures

Per-fixture rubric used during `/skill-creator` eval to grade with-skill outputs against expected behaviour. Each fixture lists pass criteria (must be present), fail conditions (anti-patterns that disqualify the output), and the disciplines being tested.

The rubric is designed for binary grading per criterion (present/absent), with fixtures requiring all pass-criteria met and zero fail-conditions triggered. Diagnostic value comes from comparison against the no-skill baseline: where the with-skill output catches a discipline the baseline misses, that is the substantive demonstration of the skill's value.

---

## Eval 0: circular trap (Art. 4(8) refusal on weak facts)

**Discipline tested:** the circular trap. Recital 31 conjunction. Refusal as a skill response (not "I can't help" but "the analysis as posed would be wrong"). References: `references/gotchas.md` entries 6, 7, 8; `references/gates/trade-secrets-directive.md`; SKILL.md refusal cases.

**Pass criteria (all required):**

1. Output refuses to draft the refusal letter as posed.
2. Output identifies that trade-secret status is necessary but not sufficient for Art. 4(8).
3. Output cites Recital 31 and quotes (or paraphrases accurately) the "serious AND irreparable" conjunction.
4. Output demands additional facts before a lawful refusal can be drafted (the specific damage scenario; why irreparable; the stage-1 negotiation record; competent authority notification status).
5. Output flags that stage-1 safeguards typically must be attempted before stage 3 is reachable.

**Fail conditions (any disqualifies):**

- Output produces a refusal letter on the facts as given.
- Output treats trade-secret status alone as sufficient for refusal.
- Output omits the "irreparable" element of the conjunction.

---

## Eval 1: sectoral overlay (connected-car aftermarket)

**Discipline tested:** sectoral lex specialis as warn-only; horizontal analysis with explicit gate. References: `references/gates/sectoral-lex-specialis.md`; `sources/vehicle-data-guidance-pointer.md`.

**Pass criteria:**

1. Output runs the horizontal Data Act analysis: scope; chapter (Ch II, Art. 5(1)); role mapping; fact-categories; limb-by-limb Art. 5(1).
2. Output explicitly flags the sectoral overlay (Vehicle Data Guidance pointer; automotive lex specialis).
3. Output treats the sectoral piece as warn-only (does not opine substantively on sectoral specifics).
4. Output redirects sectoral specifics to specialist counsel.
5. Output runs the DMA gatekeeper check (Art. 5(3)).

**Fail conditions:**

- Output produces detailed sectoral guidance as if the skill were a sectoral expert.
- Output omits the sectoral overlay entirely.

---

## Eval 2: temporal applicability (Ch IV pre-Sept-2025 contract)

**Discipline tested:** Art. 50 temporal applicability; the 12 Sept 2027 cutover for indefinite contracts.

**Pass criteria:**

1. Output identifies that Art. 13 generally applies to contracts concluded after 12 September 2025.
2. Output identifies the transitional rule for indefinite-duration contracts concluded on/before 12 Sept 2025: Art. 13 applies from 12 September 2027.
3. Output correctly concludes that Art. 13 does NOT apply to the 2024 perpetual contract until 12 September 2027.
4. Output cites Art. 50.

**Fail conditions:**

- Output states or implies Art. 13 applies to the contract today (May 2026).
- Output runs the Art. 13 unfairness analysis as if the regime were currently operative on this contract.

---

## Eval 3: Digital Omnibus (Art. 31 current vs proposal)

**Discipline tested:** current-law-vs-proposal discipline (Step 7 + house-style tagging convention). References: `sources/digital-omnibus-amendments-tracker.md`; `references/gotchas.md` entries 13, 20.

**Pass criteria:**

1. Output applies CURRENT LAW first: Art. 31(1) limb-by-limb, with the negative-limb finding (SaaS offered in the service catalogue typically fails the "not offered at broad commercial scale" limb).
2. Output concludes that Art. 31 carve-out does NOT apply on current law.
3. Output THEN separately addresses the Digital Omnibus proposal (broadened carve-out for pre-12-Sept-2025 contracts + SME / small-mid-cap exemptions for non-IaaS pre-12-Sept-2025 contracts).
4. Output flags the proposal's status: co-legislator negotiation, NOT adopted.
5. Output never presents the proposal as if it were law.

**Fail conditions:**

- Output applies the proposed Omnibus broadening as current law.
- Output omits the Omnibus impact entirely.

---

## Eval 4: Ch V Art. 15 exceptional need limb-by-limb

**Discipline tested:** limb-by-limb cumulative test application; Art. 15(1) two-limb (a)/(b) structure; market-purchase-exhaustion requirement.

**Pass criteria:**

1. Output identifies that the request is non-emergency, so Art. 15(1)(b) (not (a)) governs.
2. Output applies the Art. 15(1)(b) cumulative limbs: specific legal task; non-personal data only; alternatives exhausted including market purchase.
3. Output specifically calls out the market-purchase-exhaustion requirement as the critical limb here.
4. Output identifies that Art. 15(2) microenterprise/small-enterprise carve-out does not help the large enterprise.
5. Output identifies Art. 17 procedural requirements (form, specificity, identification of data needed).
6. Output identifies Art. 18 decline-or-modify options and the 5/30 working-day window.
7. Output references Art. 20 compensation rights.

**Fail conditions:**

- Output collapses the cumulative limbs into a single test.
- Output skips the market-purchase-exhaustion limb.
- Output applies Art. 15(1)(a) emergency limb to a non-emergency request.

---

## Eval 5: GDPR overlay (Case B; Recital 34 user-as-controller)

**Discipline tested:** GDPR-Data-Act boundary; Recital 34 user-not-data-subject route; Art. 4(12) legal basis requirement; gotcha 3.

**Pass criteria:**

1. Output identifies the Case-B route: user (employer) is not the data subject (drivers).
2. Output cites Recital 34 of the Data Act placing the user-not-data-subject in the controller role.
3. Output cites Art. 4(12) conditioning disclosure on a valid GDPR legal basis.
4. Output runs the GDPR Art. 6 legal-basis options critically: Art. 6(1)(b) only for strictly necessary employment-contract performance; Art. 6(1)(f) legitimate interest subject to LIA in employment context; Art. 6(1)(a) consent typically not free for employees.
5. Output flags potential Art. 9 special-category concerns (driving behaviour data may permit inferences about health/fatigue).
6. Output concludes that the Data Act structurally allows the request but GDPR may substantially constrain or block it.

**Fail conditions:**

- Output treats the Data Act request as self-contained (no GDPR engagement).
- Output asserts Art. 6(1)(a) consent as a clean legal basis in the employment context.

---

## Eval 6: multi-chapter cross-analysis

**Discipline tested:** cross-chapter analysis as separate per-chapter analyses (gotcha, do not blend); role shifts across phases; multi-gate run.

**Pass criteria:**

1. Output produces a separate analysis per chapter: Ch II (Art. 4(1)), Ch VI (switching), Ch IV (Art. 13 unfair terms).
2. Output performs role mapping that explicitly shifts across phases (logistics group is user in Ch II, customer in Ch VI).
3. Output runs the relevant gates per chapter: GDPR (driver personal data); sectoral (automotive, warn-only); DMA gatekeeper check; Member State for competent authority.
4. Output flags Ch IV temporal applicability per Art. 50 depending on contract date.
5. Output flags Digital Omnibus impact on Art. 25 and Art. 31.

**Fail conditions:**

- Output blends the three chapters into a single analysis.
- Output omits role shifts across phases.
- Output omits the sectoral or Member State warn-only flags.

---

## Eval 7: Art. 32 third-country cumulative conditions

**Discipline tested:** Art. 32(3) cumulative conditions (gotcha 18); non-personal-data-only scope; international agreement path under Art. 32(2).

**Pass criteria:**

1. Output identifies Art. 32 scope: non-personal data only (personal data falls under GDPR Ch V).
2. Output identifies Art. 32(2) international-agreement path and confirms inapplicability on the facts.
3. Output applies Art. 32(3) as CUMULATIVE three conditions, not disjunctive: (a) reasons + proportionality + specificity; (b) reasoned objection subject to court review; (c) court empowered to consider EU-protected legal interests.
4. Output recommends national-body consultation per Art. 32 implementation (Bundesjustizamt / Bureau de l'entraide pénale internationale equivalents) per FAQ Q63.
5. Output warns that non-compliance with Art. 32(3) plus compliance with the third-country order would be unlawful under EU law.

**Fail conditions:**

- Output treats the three Art. 32(3) conditions as disjunctive (pick any one).
- Output conflates Art. 32 with GDPR Ch V personal-data transfers.
- Output advises compliance with the US court order without Art. 32(3) satisfaction.

---

## Cross-fixture quality checks (apply to every output)

These are house-style and discipline checks applied to every eval output. A pass on any individual fixture also requires:

- **House style.** No em dashes; no "Furthermore"/"Moreover"/"Indeed"/"It should be noted"/"Notably"/"Importantly"; no marketing language; no preambles; no exclamation marks; no emoji; no CYA padding addressed to the user as if the user were a lay reader.
- **Lead with the answer.** First substantive sentence states the conclusion or most load-bearing fact.
- **Role mapping explicit.** Every entity in the scenario receives an explicit role assignment (Data Act role; GDPR role if personal data).
- **Verbatim citation.** Articles and recitals cited inline using the Art. N(M) / Recital N convention. Quotes from the regulation are verbatim, not paraphrased.
- **Limb-by-limb.** Where the test has multiple limbs, the limbs are enumerated and tested separately.
- **Gate results stated, not buried.** Gate results appear in the output text, not in footnotes.
- **Temporal applicability stated where it matters.** No assumption that the Data Act applies now without checking against Art. 50.
- **Digital Omnibus flagged where applicable.** Provisions on the tracker (Arts. 4(8), 5(11), 15, 25, 31) carry the current-law-first, proposal-second flag.
- **Assumptions stated where facts were assumed.** No silent extrapolation from missing facts.

Failure on any of the cross-fixture quality checks does not necessarily fail a fixture, but materially diminishes the with-skill output's value over the baseline and is recorded in the diagnostic notes.
