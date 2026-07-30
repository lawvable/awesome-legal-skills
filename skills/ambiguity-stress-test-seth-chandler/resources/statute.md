# Profile B — Statutes

A statute is a public, unilateral legal text. Three differences from a contract drive the profile. It governs an *indefinite class* of future actors, not two known parties. Its ambiguity is resolved not by recovering a bargain but by a contested toolkit — the interpretive canons — over which textualists and purposivists themselves disagree. And it sits inside a *corpus*: a title, a code, a body of case law, a constitution. The detector still runs from the four corners, but the resolver cannot.

## Domain defect families

The universal six all apply. Seven public-law families extend them — some genuinely new, some specializations:

- **Scope / coverage ambiguity.** Does the statute reach this actor or this conduct *at all*? Jurisdictional reach, "engaged in commerce," extraterritoriality, the line between covered and uncovered persons. A specialization of definitional boundary (Family C), but elevated: in public law, whether the text applies is often the whole fight.
- **Statute–statute conflict.** Two provisions — in the same act or across acts — that both apply and point opposite ways. A cross-instrument form of internal contradiction (Family A); resolved, if at all, by general/specific, later/earlier, and the presumption against implied repeals.
- **Mens rea gap.** A criminal or quasi-criminal provision is silent on the required mental state, or on *which elements* a stated mental state modifies (does "knowingly" run through every element, or only the verb?).
- **Temporal / transitional defect.** Effective dates, retroactivity, grandfathering, sunsets — and provisions silent on which conduct, occurring when, they govern.
- **Remedy / enforcement gap.** The statute creates a duty but is silent on the consequence of breach — no stated penalty, or no indication whether a private right of action exists.
- **Delegation breadth.** The statute hands an agency open-ended power ("as the Secretary deems necessary," "in the public interest") with no intelligible principle. A specialization of standardless discretion (Family D), with a constitutional dimension.
- **Constitutional-avoidance trigger.** One available reading would raise a serious constitutional doubt — void-for-vagueness, free speech, federalism, retroactive punishment. The scenario is the fork between the fraught reading and the saving one.

## Lexicon additions

Beyond the universal lexicon: *"the Secretary / Administrator / Department may," "shall promulgate," "as deemed necessary," "in the public interest"* (delegation breadth); *"knowingly," "willfully," "intentionally," "with intent to"* — and the absence of any such word in a penalty provision (mens rea gap); *"engaged in," "affecting commerce," "any person who"* (scope / coverage); *"this Act applies to," "effective," "on or after," "notwithstanding any other provision of law"* (temporal and statute–statute); *"shall be unlawful"* with no stated remedy (enforcement gap).

## Competing interpreters

Not two, and not fixed. Identify, per defect, who lands on opposite sides: the enforcing agency vs. the regulated party; a private plaintiff vs. a private defendant; the prosecution vs. a criminal defendant; one agency vs. another — and, above all, the court as the actor who ultimately decides. Name the realistic adversaries for *that* provision.

## Interpretive doctrines

The doctrine set that drives `likely_outcome` is the canons of construction:

- **Ordinary / plain meaning** — words carry their ordinary public meaning at enactment.
- **Whole-act rule and the rule against surplusage** — read the statute as a coherent whole; no provision rendered meaningless.
- ***Noscitur a sociis*** — a word is known by the company it keeps.
- ***Ejusdem generis*** — general words following an enumerated list are limited to the same class as the list.
- ***Expressio unius est exclusio alterius*** — to express one thing is to exclude others.
- **Presumption of consistent usage** — the same term means the same thing throughout an act; different terms mean different things.
- **Rule of lenity** — genuine ambiguity in a criminal statute is resolved in the defendant's favor.
- **Presumption of mens rea** — courts read a mental-state requirement into otherwise-silent offenses, extending it to the elements that separate innocent from wrongful conduct.
- **Constitutional avoidance** — between two fair readings, choose the one that avoids serious constitutional doubt.
- **Presumptions against retroactivity and against implied repeals.**
- **Major questions doctrine** — an agency claim of authority over a matter of vast economic or political significance requires clear congressional authorization.
- **Methodological background** — textualism and purposivism resolve hard cases differently; note in `likely_outcome` when the result turns on which method the deciding court follows.

## The as-applied scenario frame

The contract binary ("Party A claims X; Party B argues Y") still works, but a statute governs a class, so the strongest scenarios often take an *as-applied* form: the same provision means one thing applied to actor type 1 and another applied to actor type 2. The triggering event is one concrete actor's situation, but the scenario states explicitly that the provision will recur across the class, and the dispute is the divergence.

## Quality-bar adjustment — the canon gauntlet

A facial ambiguity is not enough. Because the canons frequently dissolve apparent ambiguity, run each candidate ambiguity through the canons above and keep it only if it remains genuinely contestable *after* the canons are applied. An "ambiguity" that *ejusdem generis* or the whole-act rule would settle in one paragraph is a false positive — drop it. A live statutory scenario survives the canons, not merely the dictionary.

## Research step

The statute profile cannot resolve from the four corners alone — `likely_outcome` almost always depends on related provisions of the same code, the constitutional backdrop, and whether a court has already construed the language. Between Construct and Output, consult the surrounding statutory neighborhood and existing case law.

Follow the source order in the core file's "Research and sources" section: the user's named source first, then any connected legal-research tool (CourtListener, Descrybe, Midpage, Lexis and similar all serve), then ordinary web search, then the text alone with that fact disclosed. Check a candidate scenario against decisions that may already have settled it, and drop the ones that have been settled. Where no source is available, keep the scenarios but state the doctrine rather than naming cases, and record in the sources note that they were not checked against existing construction.

## Redraft register

The drafter is the legislature, not a party. The `redraft` field proposes a statutory amendment and is constrained by the constitution above it. Unlike a contract redraft, it cannot assume two parties will agree to cleaner language — it is a proposal addressed to a lawmaker — so flag when a defect is more honestly cured by amendment than papered over by interpretation.

## Worked example — an illustrative drone statute

> **§ 4. Operation of Unmanned Aircraft.**
> (a) No person shall operate an unmanned aircraft over private property at an altitude below 250 feet without the consent of the property owner.
> (b) Subsection (a) does not apply to operation by a public agency for a governmental purpose.
> (c) A person who knowingly violates subsection (a) commits a Class B misdemeanor.
> (d) The Department may by regulation establish exceptions for commercial operations conducted in the public interest.

**S-1 — What counts as "operating an unmanned aircraft."** *Narrative:* A resident releases a large mylar party balloon carrying a lightweight GPS tag; wind carries it across a neighbor's yard at roughly 100 feet. The county cites the resident under §4(a). The prosecution argues "unmanned aircraft" reaches any uncrewed airborne object and the resident "operated" it by releasing it; the resident argues "operate … an aircraft" denotes controlled flight of a craft designed to fly, not the release of a balloon at the mercy of the wind. *Anchors:* §4(a). *Family:* scope / coverage ambiguity. *Weak point:* neither "unmanned aircraft" nor "operate" is defined, and the statute does not say whether control is required. *Likely outcome:* the resident likely prevails — *noscitur a sociis* reads "operate" and "aircraft" together to imply controlled flight of a designed craft, and lenity resolves the residual doubt for a criminal defendant. *Redraft:* define "unmanned aircraft" and define "operate" to specify whether active control is an element.

**S-2 — How far "knowingly" reaches.** *Narrative:* A photographer flies a camera drone at 120 feet over what she reasonably believes is public parkland; the parcel is in fact private and the owner gave no consent. She is charged under §4(c). The prosecution argues "knowingly" attaches only to the act of operating, which she plainly did knowingly; she argues "knowingly" must extend to the private-property and consent elements, because those separate an innocent flight from a criminal one. *Anchors:* §4(a), §4(c). *Family:* mens rea gap. *Weak point:* §4(c) does not say which elements of §4(a) "knowingly" modifies. *Likely outcome:* the defendant's reading is favored — courts presume the mental state extends to the elements that criminalize otherwise-lawful conduct, and lenity reinforces it. *Redraft:* specify the mental state element by element.

The scan also flags §4(d) — "exceptions for commercial operations conducted in the public interest" — as **delegation breadth**: "in the public interest" supplies no standard to constrain the Department. Its consequences appear once the Department writes the regulation; see the regulation profile.
