# Civil Procedure — Essay Bank  *(EXEMPLAR — gold standard)*

> This is the fullest topic file and the model the other 12 follow. CA Civ Pro
> essays test **federal** procedure heavily, often with a "would CA differ?"
> wrinkle. All rule language is original. Flag uncertain law `> ⚠️ VERIFY`.

**High-frequency note:** Subject-matter jurisdiction (diversity + amount in
controversy), personal jurisdiction, and Erie are the perennial anchors. Essays
typically chain SMJ → PJ → venue → Erie → joinder → a pleading/jury wrinkle. CA
divergences cluster in **personal jurisdiction is the same, but California has no
amount-in-controversy / diversity gate** and uses its own pleading (fact pleading,
not notice pleading) and discovery rules.

---

## Part 1 — Attack Outline (condensed, one-screen)

```
SUBJECT MATTER JURISDICTION — trigger: case is in FEDERAL court
   rule: federal court needs federal-question OR diversity SMJ; cannot be waived
   ├─ federal question — trigger: claim arises under fed law on face of well-pleaded complaint
   ├─ diversity — trigger: parties from different states + >$75k
   │     ├─ complete diversity — no P shares a state with any D (Strawbridge)
   │     ├─ citizenship — natural person = domicile; corp = state of incorp + PPB (nerve center)
   │     ├─ amount in controversy — >$75k, good faith; aggregation rules; equity = either viewpoint
   ├─ supplemental jx — trigger: extra claim with no independent SMJ
   │     rule: common nucleus of operative fact; §1367(b) bars some diversity add-ons
   ├─ removal — trigger: D wants out of state court
   │     rule: D may remove to fed court that would have had SMJ; 30 days; in-state-D bar for diversity
PERSONAL JURISDICTION — trigger: is it fair to haul D into THIS state
   rule: statute (long-arm) + constitutional due process (min contacts + fair play)
   ├─ traditional bases — domicile, presence/service in state, consent
   ├─ minimum contacts — purposeful availment + relatedness
   ├─ fair play — burden, forum interest, P interest, efficiency, shared policy
VENUE — trigger: which district
   rule: where any D resides (if all same state) OR where substantial part of events occurred
   ├─ transfer — §1404 (convenience) vs §1406 (improper venue); forum non conveniens
ERIE DOCTRINE — trigger: fed court in DIVERSITY, which law applies
   rule: apply state substantive law, federal procedural law
   ├─ on-point FRCP/statute → apply it if valid (Hanna)
   ├─ no on-point fed rule → outcome-determinative / twin aims of Erie
PLEADINGS — trigger: complaint/answer adequacy, amendments
   rule (fed): notice pleading — plausible claim (Twombly/Iqbal)
   ├─ Rule 9(b) — fraud/mistake pled with particularity
   ├─ Rule 11 — certification; sanctions; 21-day safe harbor
   ├─ amendments — once as of right; relation back (15(c))
JOINDER — trigger: extra claims or parties
   ├─ claims — plaintiff joins any claims (18a)
   ├─ counterclaims — compulsory (same T/O, or waived) vs permissive
   ├─ crossclaims — co-parties, same T/O, permissive
   ├─ permissive party joinder (20) — same T/O + common question
   ├─ compulsory/necessary party (19) — necessary + feasible; indispensable
   ├─ impleader (14) — D brings in 3rd party derivatively liable
   ├─ intervention (24) — of right vs permissive
   ├─ interpleader — rule 22 vs statutory §1335
   ├─ class action (23) — numerosity, commonality, typicality, adequacy + (b)(1/2/3)
DISCOVERY — scope = relevant + proportional; privilege; work product; sanctions
PRETRIAL / TRIAL DISPOSITION
   ├─ 12(b)(6) — failure to state a claim, on the pleadings
   ├─ summary judgment (56) — no genuine dispute of material fact
   ├─ JMOL (50a) / renewed JMOL (50b) — no reasonable jury could find
   ├─ new trial (59)
JURY TRIAL — trigger: 7th Am demand
   rule: legal claims → jury; equitable → court; legal issues tried first
PRECLUSION
   ├─ claim preclusion (res judicata) — same claim, same parties, final judgment on merits
   ├─ issue preclusion (collateral estoppel) — actually litigated + essential; mutuality relaxed
```

---

## Part 2 — IRAC Rule Blocks (full, memorizable)

### Subject Matter Jurisdiction
🟢  ·  *gate every federal essay with this*

**Rule.** A federal court is one of limited jurisdiction and may hear a case only if
it has subject-matter jurisdiction, which exists through either (1) federal-question
jurisdiction or (2) diversity jurisdiction. SMJ cannot be waived and may be raised at
any time, including by the court sua sponte.

**Here.** Here, the suit was filed in federal court, so it proceeds only if a federal
question appears or the diversity requirements are met.

**Thus.** Thus, the court must find a basis for SMJ or dismiss.

### Federal-Question Jurisdiction
🟢

**Rule.** Federal-question jurisdiction exists when the plaintiff's claim arises
under the Constitution, laws, or treaties of the United States, and the federal issue
appears on the face of a well-pleaded complaint — not by anticipated defense or
counterclaim.

**Here.** Here, the claims sound in [state contract/tort] law, so no federal right
appears on the face of the complaint.

**Thus.** Thus, there is no federal-question jurisdiction.

### Diversity Jurisdiction
🟢

**Rule.** Diversity jurisdiction exists when (1) there is complete diversity — no
plaintiff is a citizen of the same state as any defendant — and (2) the amount in
controversy exceeds $75,000, exclusive of interest and costs.

**Here.** Here, [P] is a citizen of [state] and [D] of [other state], and the claim
seeks more than $75,000.

**Thus.** Thus, diversity jurisdiction [exists/fails].

> **CA divergence:** California superior courts are courts of *general* jurisdiction —
> there is **no diversity requirement and no $75,000 floor** in CA state court. (CA
> does have a $35,000 floor dividing limited vs. unlimited civil cases — jurisdictional
> classification, not a bar to the courthouse.)

### Citizenship of the Parties
🟢

**Rule.** A natural person is a citizen of the state of her domicile — the state where
she is physically present and intends to remain indefinitely. A corporation is a
citizen of both its state of incorporation and the state of its principal place of
business (its "nerve center," where its officers direct and control operations).

**Here.** Here, [party] lived in [state] with intent to remain, making [state] her
domicile.

**Thus.** Thus, [party] is a citizen of [state].

### Amount in Controversy
🟡

**Rule.** The amount in controversy must exceed $75,000 and is measured by the
plaintiff's good-faith allegation, which controls unless it appears to a legal
certainty that the claim is for less. A single plaintiff may aggregate all claims
against a single defendant. For injunctive/equitable relief, courts measure the value
from either the plaintiff's (benefit) or defendant's (cost of compliance) viewpoint.

**Here.** Here, [P] seeks $[amount] (and/or specific performance of a $[X] obligation),
which under either viewpoint exceeds $75,000.

**Thus.** Thus, the amount-in-controversy requirement is satisfied.

### Supplemental Jurisdiction
🟡

**Rule.** A federal court with original jurisdiction over one claim may exercise
supplemental jurisdiction over related claims that share a common nucleus of operative
fact (part of the same case or controversy). In a diversity case, §1367(b) withholds
supplemental jurisdiction over certain claims by plaintiffs against parties joined
under Rules 14, 19, 20, or 24 when doing so would defeat complete diversity. Courts may
decline supplemental jurisdiction (novel state issue, state claim predominates, etc.).

**Here.** Here, the added claim arises from the same facts as the anchor claim, so it
shares a common nucleus, but [§1367(b) bar / discretionary decline] may apply.

**Thus.** Thus, supplemental jurisdiction [is/ is not] available.

### Removal
🟡

**Rule.** A defendant may remove a state-court action to the federal district court
embracing the state court if that federal court would have had original jurisdiction.
All defendants must join, and removal must occur within 30 days of service of the
removable pleading. A diversity case may **not** be removed if any defendant is a
citizen of the forum state (the in-state-defendant bar), and generally not more than 1
year after commencement.

**Here.** Here, [D] seeks removal of a [diversity/federal-question] case, and [no
forum-state defendant exists / the 30-day clock is met].

**Thus.** Thus, removal is [proper/improper].

### Personal Jurisdiction
🟢

**Rule.** A court has personal jurisdiction over a defendant if (1) a statute (the
long-arm statute) authorizes it and (2) the exercise comports with constitutional due
process. Due process is satisfied by a traditional basis — domicile, physical presence
when served, or consent — or by minimum contacts with the forum such that suit does
not offend traditional notions of fair play and substantial justice.

**Here.** Here, [D] [is domiciled in / was served in / purposefully directed activity
toward] the forum.

**Thus.** Thus, personal jurisdiction [exists/fails].

> **CA divergence:** California's long-arm statute (CCP §410.10) is **coextensive with
> due process** — it reaches as far as the Constitution allows, so the PJ analysis
> collapses into the constitutional minimum-contacts test. Functionally same result as
> federal.

### Minimum Contacts & Fair Play
🟢

**Rule.** Minimum contacts require **purposeful availment** of the benefits of the
forum (such that the defendant could foresee being haled into court there) and
**relatedness** between the claim and those contacts (specific jurisdiction) or
contacts so continuous and systematic as to render the defendant essentially at home
(general jurisdiction). Fairness is then weighed using factors: the burden on the
defendant, the forum state's interest, the plaintiff's interest in convenient relief,
the interstate judicial system's efficiency, and shared substantive policies.

**Here.** Here, [D]'s contacts — [contracted with a forum resident / directed goods
into the forum] — show purposeful availment, and the claim arises from them.

**Thus.** Thus, the assertion of jurisdiction is constitutionally reasonable.

### Venue
🟢

**Rule.** In federal court, venue is proper in (1) any district where any defendant
resides, if all defendants reside in the same state, or (2) any district where a
substantial part of the events or omissions giving rise to the claim occurred, or where
a substantial part of the property is situated. If neither applies, a fallback provision
governs.

**Here.** Here, [a substantial part of the events occurred in / all defendants reside
in] this district.

**Thus.** Thus, venue is [proper/improper].

### Transfer of Venue / Forum Non Conveniens
🟡

**Rule.** Where venue is proper, a court may transfer under §1404(a) to another district
where the case might have been brought, for the convenience of parties and witnesses
and in the interest of justice. Where venue is improper, §1406(a) allows dismissal or
transfer to a proper district. Forum non conveniens permits dismissal when the far more
convenient forum is in a different judicial system (e.g., a foreign country).

**Here.** Here, [the case could have been brought in District X and convenience favors
it / venue is improper here].

**Thus.** Thus, transfer under §[1404/1406] is appropriate.

### Erie Doctrine
🟢  ·  *high-frequency, examiner favorite*

**Rule.** A federal court sitting in diversity applies federal procedural law but the
**substantive** law of the state in which it sits (including that state's choice-of-law
rules). When a Federal Rule of Civil Procedure or federal statute is on point and valid
under the Rules Enabling Act / Constitution, the federal court applies it (Hanna). When
no federal rule is on point, the court asks whether the state rule is outcome-
determinative in light of the **twin aims of Erie** — discouraging forum-shopping and
avoiding inequitable administration of the laws.

**Here.** Here, the issue of [contract elements / SOL] is substantive, so state law
governs; the manner of [service / pleading mechanics] is procedural and governed by the
FRCP.

**Thus.** Thus, the court applies [California substantive law / the on-point Federal
Rule].

### Pleadings — Complaint & Notice Pleading
🟢

**Rule.** A federal complaint must contain (1) a short and plain statement of the
grounds for subject-matter jurisdiction, (2) a short and plain statement of the claim
showing entitlement to relief, and (3) a demand for relief. Under notice pleading, the
complaint must state a claim that is **plausible on its face** — pleading facts that
permit a reasonable inference of liability, not merely conceivable (Twombly/Iqbal).

**Here.** Here, [P]'s complaint [did/did not] plead the jurisdictional basis and pled
facts making the claim plausible.

**Thus.** Thus, the complaint [satisfies / fails] the pleading requirements.

> **CA divergence:** California is a **fact-pleading** state — the complaint must allege
> the *ultimate facts* constituting each element of the cause of action, a higher bar
> than federal notice pleading. (CA does not follow Twombly/Iqbal plausibility.)

### Pleadings — Rule 9(b) Fraud Particularity
🟢  ·  *cross-ref: Torts (fraud), Remedies*

**Rule.** Although most claims need only notice pleading, fraud and mistake must be
pled **with particularity** — the circumstances (who, what, when, where, how of the
misrepresentation). State of mind — malice, intent, knowledge — may be alleged
generally.

**Here.** Here, [P] alleged only "[fraud in the supposed value]" without pleading the
misrepresentation, scienter, reliance, or causation with particularity.

**Thus.** Thus, the fraud claim fails the particularity requirement.

### Rule 11 Sanctions
🟡

**Rule.** By signing a pleading or motion, an attorney certifies that, after a
reasonable inquiry, it is not for an improper purpose, the legal contentions are
warranted, and the factual contentions have evidentiary support. A motion for sanctions
must be served and the offending party given a **21-day safe harbor** to withdraw before
filing with the court.

**Here.** Here, [the filing lacked a reasonable factual basis], and [the safe harbor
was/was not honored].

**Thus.** Thus, Rule 11 sanctions are [available/premature].

### Amendments & Relation Back
🟡

**Rule.** A party may amend a pleading once as of right within 21 days of serving it
(or within 21 days of a responsive pleading/motion); otherwise by leave of court, freely
given when justice so requires. An amendment adding a **claim** relates back if it arose
from the same conduct, transaction, or occurrence. An amendment changing a **party**
relates back if, additionally, within the service period the new party knew of the
action and knew it would have been named but for a mistake.

**Here.** Here, the amendment [arises from the same transaction / changes a party who
had notice].

**Thus.** Thus, the amendment relates back to the original filing date.

### Joinder of Claims
🟢

**Rule.** A plaintiff may join as many claims as it has against an opposing party,
whether or not related. Each joined claim must still have an independent or supplemental
basis for subject-matter jurisdiction.

**Here.** Here, [P] joined the [fraud] and [breach of contract] claims against [D],
which is permitted.

**Thus.** Thus, joinder of the claims is proper.

### Counterclaims
🟢

**Rule.** A counterclaim is **compulsory** — and waived if not asserted — when it arises
out of the same transaction or occurrence as the opposing party's claim. Any other
counterclaim is **permissive**. A compulsory counterclaim falls within supplemental
jurisdiction; a permissive counterclaim needs its own jurisdictional basis.

**Here.** Here, [D]'s counterclaim [does/does not] arise from the same transaction.

**Thus.** Thus, the counterclaim is [compulsory and must be raised now / permissive].

### Crossclaims
🟡

**Rule.** A crossclaim is a claim against a **co-party** that arises out of the same
transaction or occurrence as the original action or relates to property at issue.
Crossclaims are always **permissive**.

**Here.** Here, co-defendant [A] asserts a same-transaction claim against co-defendant
[B].

**Thus.** Thus, the crossclaim is proper but not mandatory.

### Permissive Joinder of Parties (Rule 20)
🟡

**Rule.** Plaintiffs may join, or defendants may be joined, if (1) the claims arise from
the same transaction, occurrence, or series, and (2) there is a common question of law
or fact.

**Here.** Here, the claims by/against [parties] arise from the same series of events and
share a common question.

**Thus.** Thus, permissive party joinder is proper.

### Compulsory / Necessary & Indispensable Parties (Rule 19)
🟡

**Rule.** A party is **necessary** if, in its absence, complete relief cannot be
accorded among existing parties, or the absentee's interest would be impaired, or
existing parties face a substantial risk of multiple/inconsistent obligations. A
necessary party must be joined if feasible (jurisdiction and venue allow). If joinder is
not feasible, the court decides whether the party is **indispensable** — such that the
action cannot in equity and good conscience proceed — and if so, dismisses.

**Here.** Here, [absentee] [holds a joint interest / risks inconsistent obligations].

**Thus.** Thus, [absentee] is a necessary party who must be joined [or the case
dismissed].

### Impleader (Rule 14)
🟡

**Rule.** A defending party may, as a third-party plaintiff, implead a non-party who is
or may be **derivatively liable** to it for all or part of the plaintiff's claim
(indemnity, contribution). Impleader is of right within 14 days of serving the answer,
later by leave.

**Here.** Here, [D] seeks to bring in [X] on a theory of [indemnity/contribution].

**Thus.** Thus, impleader is proper because the claim is derivative.

### Intervention (Rule 24)
🟡

**Rule.** Intervention **of right** is allowed when the absentee has an interest in the
subject matter that may be impaired and is not adequately represented by existing
parties. **Permissive** intervention is discretionary when the absentee's claim or
defense shares a common question with the action.

**Here.** Here, [intervenor]'s interest [will be impaired and is not adequately
represented].

**Thus.** Thus, intervention [of right / by permission] is appropriate.

### Class Actions (Rule 23)
🟡

**Rule.** A class action requires (1) **numerosity** (joinder impracticable), (2)
**commonality** (common questions), (3) **typicality** (reps' claims typical), and (4)
**adequacy** (reps fairly protect the class), plus one of: (b)(1) risk of inconsistent
adjudications, (b)(2) injunctive relief appropriate to the class as a whole, or (b)(3)
common questions predominate and a class action is superior (requires notice and opt-out).

**Here.** Here, the proposed class [meets the four prerequisites] and fits Rule 23(b)(__).

**Thus.** Thus, certification is [proper/improper].

### Discovery — Scope & Work Product
🟡

**Rule.** Parties may discover any non-privileged matter relevant to a claim or defense
and proportional to the needs of the case. **Work product** — material prepared in
anticipation of litigation — is protected from discovery absent substantial need and
undue hardship; an attorney's mental impressions and legal theories receive near-absolute
protection.

**Here.** Here, the requested [documents] are relevant but [constitute opinion work
product].

**Thus.** Thus, the material is [discoverable/protected].

### 12(b)(6) — Failure to State a Claim
🟢

**Rule.** A motion to dismiss for failure to state a claim tests the legal sufficiency
of the complaint, accepting well-pleaded facts as true and asking whether they state a
plausible claim for relief. Courts do not credit legal conclusions.

**Here.** Here, even taking [P]'s allegations as true, the complaint [omits an essential
element].

**Thus.** Thus, the 12(b)(6) motion should be [granted/denied].

### Summary Judgment (Rule 56)
🟢

**Rule.** Summary judgment is proper when, viewing the evidence in the light most
favorable to the non-movant, there is no genuine dispute of material fact and the movant
is entitled to judgment as a matter of law. The movant bears the initial burden; the
non-movant must then point to specific evidence creating a triable issue.

**Here.** Here, the [undisputed evidence] shows [no triable issue on element X].

**Thus.** Thus, summary judgment is [warranted/denied].

### JMOL / Renewed JMOL (Rule 50)
🟡

**Rule.** Judgment as a matter of law may be granted after a party has been fully heard
at trial when no reasonable jury could find for that party. A renewed motion (50(b))
after the verdict is available only if a Rule 50(a) motion was made before the case went
to the jury.

**Here.** Here, [the evidence permits only one reasonable conclusion].

**Thus.** Thus, JMOL is [proper/improper].

### Right to Jury Trial (7th Amendment)
🟢  ·  *cross-ref: Remedies (legal vs equitable)*

**Rule.** The Seventh Amendment preserves the right to a jury trial in civil actions at
law where the amount in controversy exceeds $20; it does not apply to equitable claims.
When legal and equitable claims share common fact issues, the **legal issues are tried
first to the jury**, and the jury's findings bind the court on the equitable claims. A
jury must be demanded in writing within 14 days after service of the last pleading
directed to the triable issue, or it is waived.

**Here.** Here, [P]'s [fraud-damages] claim is legal (jury), while the [specific
performance] claim is equitable (court); [P] timely demanded a jury.

**Thus.** Thus, [P] is entitled to a jury on the legal claim but not the equitable one.

> **CA divergence:** The Seventh Amendment is **not incorporated** against the states;
> California's civil jury right comes from the **CA Constitution, art. I, §16**, which
> likewise turns on the legal/equitable ("gist of the action") distinction. Same
> functional test, different source.

### Claim Preclusion (Res Judicata)
🟢

**Rule.** Claim preclusion bars relitigation of the same claim when there was (1) a
final judgment on the merits, (2) between the same parties (or those in privity), and
(3) the claim arises from the same transaction or occurrence as the first suit. It bars
not only what was litigated but what could have been litigated.

**Here.** Here, the prior suit ended in a merits judgment between the same parties on the
same transaction.

**Thus.** Thus, the later claim is barred.

> **CA divergence:** California uses the **primary rights** theory of a "claim" — a claim
> is defined by the primary right violated (one right, one injury), which can be narrower
> than the federal transactional test. Watch this in CA-vs-federal preclusion crossovers.

### Issue Preclusion (Collateral Estoppel)
🟢

**Rule.** Issue preclusion bars relitigation of an issue of fact or law that was (1)
actually litigated and determined, (2) essential to a valid final judgment, and (3) is
being asserted against a party (or privy) who had a full and fair opportunity to litigate
it. Mutuality is no longer required in many courts, so non-parties may sometimes invoke
it offensively or defensively.

**Here.** Here, the issue of [X] was actually litigated and necessary to the prior
judgment.

**Thus.** Thus, [party] is estopped from relitigating it.

---

## Part 3 — Crossovers & Exam Tactics

- **Common pairings:** Civ Pro is usually a **standalone** essay, but jury-trial and
  remedy questions bridge to **Remedies** (legal vs. equitable), and Rule 9(b)/12(b)(6)
  bridge to the substantive **Torts/Contracts** elements being pleaded.
- **Sleeper issues:** forgetting that SMJ can't be waived; missing the §1367(b) diversity
  carve-out on supplemental jurisdiction; missing the in-state-defendant removal bar;
  conflating venue with personal jurisdiction.
- **CA-divergence cheat list:**
  1. No diversity / no $75k floor in CA state court (general jurisdiction).
  2. CA = **fact pleading**, not notice pleading; no Twombly/Iqbal.
  3. CA long-arm (CCP §410.10) is coextensive with due process.
  4. CA jury right = CA Const. art. I §16 (7th Am. not incorporated).
  5. CA preclusion uses **primary rights**, not the federal transactional test.
  6. CA has its own discovery act (Civil Discovery Act) — distinct deadlines/limits.
- **Call-of-the-question patterns:** "Does the federal court have SMJ?" → run
  FQ-then-diversity-then-supplemental. "May the court apply [State] law?" → Erie. "On
  what issues is there a jury right?" → legal/equitable split + timely demand.

---
*Study aid only — verify against current CA authority. Not legal advice.*
