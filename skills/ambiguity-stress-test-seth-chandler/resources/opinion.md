# Profile D — Judicial Opinions

A judicial opinion is a *partly* legal-normative text. Its holding is a normative rule — law applied to future facts; its recited facts, its reasoning, and its dicta are not. The profile targets the opinion's normative core, and it differs from the first three profiles in a way that shapes everything below.

## The two layers of ambiguity

The other three profiles read a text whose operative rule is *given* — the enacted clause, the numbered section, the regulatory provision — and the ambiguity lies in applying it. An opinion is different: its rule is not on the page as enacted text. It must be *reconstructed* from a decision, and the reconstruction is itself contested. So the opinion profile works on two layers.

- **Layer 1 — what is the rule?** What did the court actually hold; how broadly; on which facts; with a determinate rationale or not. This layer does not exist for the other profiles.
- **Layer 2 — how far does the rule reach?** Given a holding, does it govern a new fact pattern, or is that pattern distinguishable. This is the ordinary edge-case construction (SKILL.md Step 3), which transfers unchanged.

Layer 1 is the new front; most opinion-specific defect families live there. In Step 1 (Parse), map the opinion's structure first — holding, reasoning, dicta, disposition, separate opinions — and treat the contestable boundaries of that map as the first batch of scenarios.

## Domain defect families

The universal six still run inside an opinion. The opinion-specific families, mostly Layer 1:

- **Holding/dicta indeterminacy** — which statements are the binding holding and which were said in passing. Unique to opinions: a single document carries tiers of authority.
- **Ratio uncertainty / level of generality** — the holding can be stated narrowly, tied to its facts, or broadly; future courts contest which.
- **Material-fact ambiguity** — which facts were outcome-determinative and which incidental. The engine of "distinguishable" versus "controlled by."
- **Fragmented court / no controlling rationale** — pluralities, concurrences in the judgment, the *Marks* "narrowest grounds" problem; and, even where there is a majority on the result, separate writings that destabilize the method.
- **Reasoning–result gap** — the stated rationale does not entail the holding, or proves more than the court decided.
- **Unoperationalized standard** — the court announces a multi-factor or balancing test with undefined factors. The universal vague-term family, court-generated.
- **Precedent tension** — the opinion silently narrows, or sits in unacknowledged conflict with, a prior decision. The cross-clause-tension family, run across cases.
- **Disposition / remedy scope** — what the decree, remand instruction, or injunction actually requires.

## Lexicon additions

Opinion-specific tells: "we hold," "we conclude only that," "we need not decide," "we assume without deciding," "we express no opinion on," "on the facts of this case," "under the circumstances presented," "it is enough to say," "narrowest grounds," "plurality," "concurring in the judgment," "concurring in part," footnote-buried qualifications, and hedges that mark tentativeness ("arguably," "it may be that," "cf.").

## Competing interpreters

The party urging a broad reading of the opinion against the party urging a narrow one; the lower courts bound by it; and the issuing court itself in a later case. In prospective mode, add the authoring chambers, drafting against all of those as anticipated readers.

## Interpretive doctrines

The resolver runs on the doctrines of precedent: holding versus dicta; ratio decidendi; the *Marks* "narrowest grounds" rule for fragmented courts; levels of generality; the materiality test that governs distinguishing; vertical versus horizontal stare decisis; the weight of considered dicta against bare obiter; the principle that an opinion is read against the facts before the court; and the presumption against overruling sub silentio.

## Two modes — prospective (default) and retrospective

The scan and the scenario construction are identical in both modes; only the final output field differs.

- **Prospective mode (the default).** The opinion is a draft, or a freshly issued decision, and the user is the authoring chambers or a court watching its own doctrine. The output's fix is a *tightening* — how the opinion could be written to foreclose the future dispute. This keeps the profile parallel to the other three (improve the text) and makes the skill a drafting-QA tool for judges and clerks.
- **Retrospective mode.** The opinion is final and the user is a litigator or a lower court. There is no fix — a decided opinion cannot be redrafted — so the output is instead an **argument pair**: the brief-ready contention each side would press (the case controls / the case is distinguishable).

### Choosing the mode

Default to prospective unless the user signals litigation use. The most value is created before publication, when the dispute can still be foreclosed. Read the signals in this order:

- **The user's own instruction governs.** "Tighten this draft" and "find me arguments" resolve the question outright.
- **Prospective** where the user is the authoring chambers, a clerk, or a court watching its own doctrine, and the opinion is a draft or freshly issued.
- **Retrospective** where the user is a litigator, a lower-court judge, an advocate, or a law professor working with a final opinion.
- **If the user's role is not apparent, ask one short question before scanning** — "Are you the court, drafting or about to release, or a reader working with the final opinion?" — and let the answer pick the mode. Ask once; do not interrogate.

The scan is identical either way, so a wrong guess costs only the shape of the final field. But it costs the user the whole point of the audit: a litigator handed redraft suggestions for an opinion that already issued has been given advice nobody can act on.

## Quality-bar adjustment — the precedent gauntlet

Keep a candidate scenario only if it survives the precedent doctrines above: if holding/dicta doctrine plainly settles that the contested language is dicta, or the court fixed the level of generality with an explicit statement, the ambiguity is not live — drop it.

## Output

In prospective mode the record carries the standard schema, with `redraft` becoming a *tightening* of the opinion's own language. In retrospective mode `redraft` is replaced by `argument_pair` — two short, citable contentions, one per interpreter. Everything else — title, narrative, anchors, defect family, weak point — is unchanged; `anchors` point to passages of the opinion, and for a precedent-tension defect to the prior case as well.

This profile is adjacent to others a user may know — a case brief *summarizes* an opinion, a casebook edit *condenses* it, a brief review *critiques an advocate's* document. The opinion profile does none of those: it adversarially stress-tests a *court's* document for the seams along which future litigation will form.

## Research step

Check the opinion's place in its precedent line and how later courts have read it. Follow the source order in the core file's "Research and sources" section — the user's named source first, then any connected legal-research tool, then ordinary web search, then the text alone with that fact disclosed.

Two checks are specific to this profile:

- **Is the audited opinion still standing?** An opinion that has been narrowed, distinguished into irrelevance, or overruled cannot support predictions about its future reach. Where this cannot be checked, say so — a retrospective argument pair built on a superseded holding is worse than no output.
- **Has a later court already resolved the seam?** A scope question that an intermediate court has since answered is no longer contestable and the scenario should be dropped, or recast as a live question only where the courts have split.

## Worked example — *United States v. Rahimi* (2024)

*United States v. Rahimi*, 602 U.S. 680 (2024), was decided 8–1, Chief Justice Roberts for the Court, with five concurrences (Sotomayor joined by Kagan, and Gorsuch, Kavanaugh, Barrett, and Jackson each separately) and a lone dissent by Thomas. The Court upheld 18 U.S.C. § 922(g)(8) — the federal bar on firearm possession by a person subject to a domestic-violence restraining order — against a Second Amendment facial challenge, holding that a person whom a court has found to pose "a credible threat to the physical safety of another" may be "temporarily disarmed," and that the post-*Bruen* historical inquiry asks whether a modern law is "relevantly similar" to, and "consistent with the principles that underpin," the regulatory tradition rather than demanding a "historical twin." It decided the case narrowly on purpose and left much of its own scope open. Each scenario is shown in both modes.

**1 — How far the holding reaches: the reserved § 922(g)(8)(C)(ii) prong.** A later defendant is subject to a § 922(g)(8) order under subsection (C)(ii) — an order that by its terms forbids the use of physical force — but no court ever made the "credible threat" finding (C)(i) requires. The government reads *Rahimi* as sustaining § 922(g)(8); the defendant reads it as sustaining only the application to a person under a (C)(i) finding. *Family:* ratio uncertainty / level of generality. *Weak point:* the holding is stated around a judicial credible-threat finding, the statute also reaches orders without one, and the opinion never says whether its reasoning extends there. *Prospective tightening:* state whether the holding is confined to (C)(i)-type findings, and whether (C)(ii) is reserved. *Retrospective argument pair:* government — "the Court sustained § 922(g)(8); a court order plus a prohibition on force is enough"; defendant — "every operative sentence ties the result to a credible-threat finding, and the Court expressly reserved (C)(ii)."

**2 — Whether the logic reaches the other § 922(g) categories.** A defendant convicted under § 922(g)(1) (felon in possession) or § 922(g)(3) (drug user) argues *Rahimi* controls in his favor. *Rahimi* disarmed a person subject to an individualized judicial finding and stressed the disarmament was temporary; § 922(g)(1) is categorical, requires no finding, and is permanent. *Family:* material-fact ambiguity. *Weak point:* the opinion never says whether the individualized finding and the temporariness were *necessary conditions* or merely features of the case. *Prospective tightening:* name which facts were material to the holding. *Retrospective argument pair:* government — "*Rahimi* confirms the legislature may disarm the dangerous"; defendant — "*Rahimi* turned on a court's individualized finding and a temporary order; § 922(g)(1) has neither."

**3 — The "principles" standard, announced without a metric.** Two courts of appeals apply *Rahimi*'s test — valid if "relevantly similar" to historical regulation and "consistent with the principles that underpin" the tradition — to the same modern law and split, each stating the governing "principle" at a different level of generality. *Family:* unoperationalized standard. *Weak point:* the opinion supplies no metric for the level of generality at which the historical "principle" is stated. *Prospective tightening:* specify the level of generality at which the historical inquiry runs and what makes an analogue "relevantly similar." *Retrospective argument pair:* the law's defender states the principle broadly ("disarming the dangerous"); the challenger narrowly ("disarming only those a court has individually adjudged a threat").

**4 — A majority on the result, five separate writings on the method.** A lower court must apply *Rahimi*'s methodology; the majority commands eight votes on the *result*, but the five concurrences read its method in materially different ways. *Family:* fragmented court / no controlling rationale on method. *Weak point:* a majority on the judgment is not a majority on a determinate method; the concurrences signal the methodology is unsettled even though the result is not. *Prospective tightening:* state the method specifically enough that a concurrence cannot plausibly re-gloss it, or say the method is reserved. *Retrospective argument pair:* one side reads the majority's general language through the narrowest concurrence, the other through the broadest, and both cite "the Court."
