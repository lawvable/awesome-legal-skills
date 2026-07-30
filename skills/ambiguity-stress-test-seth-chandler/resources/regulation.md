# Profile C — Regulations

A regulation is a public, unilateral legal text like a statute — but a *subordinate* one. It is issued by an agency under power delegated by a statute, and that subordination is the profile's whole character. Everything in the statute profile carries over; the regulation profile adds a *vertical* dimension. The detector now asks not only "is this internally ambiguous" but "does this stay within the instrument above it." Read `resources/statute.md` as well — the statute families, lexicon, canons, as-applied frame, canon gauntlet, and research step all apply here too.

## Domain defect families

The universal six and the seven statute families all apply. Three vertical families are specific to regulations:

- **Statute–regulation mismatch (ultra vires).** The regulation exceeds, contradicts, or steps outside the authority of its enabling statute. The *vertical form of cross-clause tension* (Family F) — the signature defect of the profile. The scenario is the collision between what the regulation does and what the statute authorized.
- **Under-implementation.** The regulation purports to implement a statutory condition but reads it out — converts a conditional grant into a categorical one, or deems a required finding automatically satisfied. It does not contradict the statute on its face; it hollows out a limit the statute imposed.
- **Incorporation-by-reference drift.** The regulation defines a term by pointing to an external source — the statute, another regulation, an industry standard, a dated publication — and the reference is ambiguous, circular, or has since changed. A specialization of definitional boundary (Family C) along the cross-instrument link.

The universal families still run *inside* the regulation's own text — a regulation can be internally vague or self-contradictory exactly as a contract can.

## Lexicon additions

The statute lexicon, plus: *"for purposes of [statutory section]," "as authorized by," "under the Act," "pursuant to section"* (the enabling link — every one is a mismatch checkpoint); *"includes," "is deemed," "shall be considered"* attached to a statutory term (under-implementation — the agency redefining what the statute conditioned); *"as defined in," "as set forth in [external standard]," "as amended"* (incorporation drift).

## Competing interpreters

The regulated party vs. the promulgating agency; the agency vs. a reviewing court; and — distinctively — a *beneficiary of the statute* vs. the agency that under-implemented it (the person the statute meant to protect, against the agency whose rule cut the protection back). Behind all of them sits the enabling legislature, whose statute is the measure the regulation is tested against.

## Interpretive doctrines

The statutory canons (see `resources/statute.md`), plus the vertical layer that drives `likely_outcome`:

- **Ultra vires review** — a regulation is valid only within the scope of the authority the enabling statute confers; a regulation that exceeds or contradicts the statute is unenforceable to that extent.
- **Independent judgment on the statute (post-*Loper Bright*, 2024)** — a reviewing court interprets the enabling statute *de novo* and no longer defers to the agency's reading under *Chevron*; the agency's view may still earn *Skidmore* respect to the extent persuasive and consistent.
- ***Auer* / *Kisor* deference** — an agency's interpretation of *its own* genuinely ambiguous regulation may receive deference, but only after the regulation is found genuinely ambiguous and the reading is reasonable, official, and considered; *Kisor v. Wilkie* sharply cabined this.
- **Arbitrary-and-capricious review (APA / *State Farm*)** — a regulation must rest on reasoned decisionmaking and consideration of the relevant factors.
- **Major questions doctrine** — a regulation asserting authority over a matter of vast economic or political significance requires clear statutory authorization.
- **Saving construction** — where possible, a regulation is read to stay within its enabling statute; where that is not possible, the regulation, not the statute, yields.

## The vertical scenario frame

Statute scenarios run horizontally — text against text, or text against silence, within one instrument. Regulation scenarios add a vertical axis: the regulation against the statute above it. The signature regulation scenario is a two-instrument collision — "the regulation says X; the enabling statute authorized only Y" — and its anchors span both instruments. The competing readings are often "valid exercise of delegated authority" against "ultra vires."

## Quality-bar adjustment

The canon gauntlet applies (see `resources/statute.md`).

## Redraft register

The tightest of the four. A regulation's drafter — the agency — is constrained by the enabling statute *and* the constitution. The `redraft` field must propose language that both closes the seam and stays within the delegated authority. Be willing to report the honest hard case: sometimes there is no valid regulatory fix, and the correct `redraft` is "this cannot be cured by regulation — the enabling statute must be amended."

## Research step

Consult the enabling statute and, where available, the rulemaking record before output (see the statute profile's research step).

## Worked example — an illustrative regulation under the drone statute

Promulgated by the Department under §4(d) of the illustrative statute in `resources/statute.md`:

> **Reg. 12-300. Commercial Drone Operations.**
> (a) For purposes of § 4(d), a "commercial operation conducted in the public interest" includes any operation by a delivery service licensed under this title.
> (b) A licensed delivery service may operate an unmanned aircraft over private property at any altitude, provided no single overflight of a parcel exceeds ninety (90) seconds.
> (c) Operations conducted in compliance with this section are exempt from the consent requirement of § 4(a).

**R-1 — The agency defining the statutory condition out of existence.** *Narrative:* A property owner sues to enjoin a licensed delivery company's drone flights over her land. The company invokes Reg. 12-300(a), which deems any licensed delivery service to be operating "in the public interest." The owner argues §4(d) authorized exceptions only for commercial operations *conducted in the public interest* — a condition the agency must apply case by case — and that a rule deeming every licensed service to satisfy it reads the condition out of the statute and is ultra vires. The agency responds that classifying licensed delivery as public-interest is a reasonable exercise of delegated rulemaking power. *Anchors:* Reg. 12-300(a) **×** §4(d). *Family:* under-implementation. *Weak point:* the regulation converts a conditional statutory grant into a categorical one. *Likely outcome:* the owner has the stronger position — post-*Loper Bright* the court reads §4(d) without deference, and "in the public interest" is a limit the agency must apply, not erase. *Redraft:* require a public-interest determination, with stated criteria, for each class of operation — or, for a categorical rule, seek a statutory amendment that supplies one.

**R-2 — When an exception swallows the rule.** *Narrative:* The same company runs roughly forty drone passes a day over a single residential parcel, each under ninety seconds, all without consent, relying on Reg. 12-300(b)–(c). The owner argues §4(a)'s consent protection has been nullified as to her property and that §4(d)'s power to create "exceptions" does not include the power to repeal §4(a) by regulation for an entire industry. The agency argues each flight is a bounded exception within the ninety-second cap, and bounded exceptions are what §4(d) authorizes. *Anchors:* Reg. 12-300(b)–(c) **×** §4(a), §4(d). *Family:* statute–regulation mismatch. *Weak point:* a per-overflight time cap, applied to high-frequency operations, lets a regulatory "exception" extinguish the statutory protection it excepts. *Likely outcome:* genuinely contestable — the agency's per-flight reading is textually available, but a court attentive to the whole-act structure may hold that an "exception" defeating the rule's purpose for a whole class exceeds §4(d). *Redraft:* tie the exception to a cumulative limit (total overflight time or passes per parcel per day) so it cannot aggregate into a de facto repeal.

The universal taxonomy still runs inside the regulation: "no single overflight of a parcel exceeds ninety seconds" carries a Family C defect of its own — "parcel" is undefined, and the text does not say whether hovering, or a path that leaves and re-enters the airspace, counts as one overflight or several.
