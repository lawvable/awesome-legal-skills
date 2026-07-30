# Drafter notes: art4-8-refusal-letter

The Art. 4(8) refusal is the highest-stakes drafting in the skill. The substantive bar is the highest in Chapter II. The failure mode (the circular trap) is the most consequential, and stage-3 refusals attract the closest competent-authority scrutiny. The McIntyre OSS enforcement digest and similar practitioner sources show that competent authorities have been ordering resumption of data sharing within weeks where stage-3 substantiation is weak.

The drafter must hold three disciplines:
- The circular trap: trade-secret status alone never justifies refusal.
- The conjunction: highly likely serious AND irreparable damage; both elements separately demonstrated.
- Stage 3 is residual: it is reachable only after stage 1 has been attempted.

## Substantive risks of using the template

- **The conjunction in section 5 is the single most important construct.** Recital 31 reads "serious economic damage" as "serious and irreparable economic loss." Both elements are required. Section 5 of the template forces three independent sub-sections: 5(a) highly likely, 5(b) serious, 5(c) irreparable. Section 5(c) MUST stand alone. The most common defect in stage-3 refusals reviewed in the practitioner literature is the collapse of "irreparable" into "serious" or its omission entirely. A refusal in which section 5(c) cannot be drafted independently of section 5(b) is a refusal that should not be sent. See `references/gates/trade-secrets-directive.md` on the serious-and-irreparable conjunction and `references/gotchas.md` entry 7.
- **Trade-secret status alone never justifies refusal.** Recital 31: "Data holders cannot, in principle, refuse a data access request under this Regulation solely on the basis that certain data is considered to be a trade secret, as this would subvert the intended effects of this Regulation." Section 2 of the template (trade-secret status) is necessary but not sufficient. Sections 3, 4, 5, and 6 are independently required. A draft that establishes section 2 well and section 5 poorly is invalid.
- **The eight-step regulatory structure is the spine.** The template's eight sections correspond to the eight cumulative limbs of Art. 4(8) identified in `references/gates/trade-secrets-directive.md` (the eight-step refusal-letter structure section). Drafters should not collapse the sections (e.g. merging sections 3 and 5 into a single "competitive harm" section). Each section addresses a distinct limb; competent authorities and dispute settlement bodies will look at each.
- **Section 3 (exceptional circumstances) must be specific.** "All our trade-secret data justifies refusal" or "competitors should not have this data" are not exceptional. Recital 31 and Art. 4(8) use "exceptional circumstances" to signal residual application. The drafter must identify specific facts that make this matter different from the ordinary case. Common patterns that may be exceptional: third-country recipient with weak enforcement; uniquely novel product in a fragile competitive position; demonstrable past pattern of trade-secret misuse by the user.
- **Section 4 (stage-1 status) is constitutive.** Art. 4(8) refers to damage "despite the technical and organisational measures taken by the user pursuant to paragraph 6." A refusal without engagement of stage 1 cannot reach section 4 and therefore cannot reach section 5. The McIntyre OSS pattern is clear: competent authorities scrutinise the stage-1 record before assessing stage 3. Stage-1 documentation matters more than the refusal letter itself.
- **Section 5(d) (objective elements) requires named elements, not vague reliance.** Recital 31 lists three illustrative elements introduced by "in particular": third-country enforceability; nature and level of confidentiality; uniqueness and novelty. The list is illustrative, not exhaustive (see `references/gotchas.md` entry 8). Other admissible elements are catalogued in `references/gates/trade-secrets-directive.md`. The drafter names the elements relied on with specific factual basis. Padding with elements the facts do not support weakens the substantiation.
- **Section 6 (case-by-case) is not a formality.** A refusal that operates as a blanket policy ("we refuse all category-X requests") is not case-by-case and is invalid as a stage-3 refusal. The drafter should be prepared to explain why this request is being refused while past or hypothetical other requests would be honoured. If the data holder genuinely treats all category-X requests the same way, the matter is not within Art. 4(8) and should be addressed through a different lawful mechanism (e.g. exclusion from Ch II scope, sectoral law carve-out, or as part of the data holder's general posture documented under Art. 3 transparency).
- **Section 7 (competent authority notification) runs in parallel, not subsequently.** Art. 4(8) third sentence: "Where the data holder refuses to share data pursuant to this paragraph, it shall notify the competent authority designated pursuant to Article 37." Notification is part of the refusal, not a downstream administrative step. The drafter should ensure the notification is dispatched on or immediately before the date of the refusal letter to the user.
- **Section 8 (user's redress) and the GDPR carve-out.** Recital 31 last sentence: "The exceptions to data access rights in this Regulation should not in any case limit the right of access and right to data portability of data subjects under Regulation (EU) 2016/679." The data subject's GDPR Art. 15 right of access runs independently of the Data Act refusal. The template includes the explicit GDPR carve-out in section 8.

## Pointers to gates and scenarios

- Scenario card: `references/scenarios/ch2-trade-secret-stage-3-refusal.md` (the full Path-1 / Path-2 / Path-3 / Path-4 decision tree; the template implements Path 1).
- Trade-secret gate: `references/gates/trade-secrets-directive.md` (always loaded; carries the eight-step refusal-letter structure, the conjunction analysis, the objective elements catalogue, and the McIntyre OSS enforcement signals).
- GDPR gate: `references/gates/gdpr-overlay.md` (always run; the GDPR carve-out in section 8 of the template is a function of Recital 31 last sentence).
- DMA gate: `references/gates/dma-gatekeeper.md` (relevant where the requesting user is or acts for a DMA-designated gatekeeper; gatekeeper status does not by itself defeat an Art. 4(1) request, but it changes the third-party-onward-sharing assessment).
- Sectoral gate: `references/gates/sectoral-lex-specialis.md` (always run; stage-3 in regulated sectors carries additional layered considerations).
- Member State gate: `references/gates/member-state.md` (always run to identify the correct competent authority).
- Gotchas: entries 6 (ladder, not switch), 7 (conjunction), 8 (objective elements illustrative).

## Common drafting mistakes the drafter should check for

- Drafting section 5 as one continuous paragraph. The structure 5(a)/(b)/(c)/(d) is constitutive of the conjunction; collapsing it is a defect.
- Section 5(c) restating section 5(b) in different words. "Serious damage that cannot be undone" is not a substantiation of irreparability; it is a restatement. The irreparability must be substantiated independently with the reasons damages, insurance, contract remedies, or other mitigation cannot cure the loss.
- Treating "highly likely" as equivalent to "possible" or "likely." Art. 4(8) elevates the probability threshold. The drafter must identify the specific causal pathway and the probability factors that make damage highly likely.
- Identifying objective elements without specific factual basis. Section 5(d) is not a list of labels; it is a list of elements with the facts that support each.
- Failing to engage the Trade Secrets Directive Art. 2(1) three-limb test in section 2. The Data Act adopts the TSD definition. A refusal that asserts trade-secret status without running the TSD test invites the user to challenge whether the data even qualifies.
- Including the Digital Omnibus proposed amendment as if it were operative law. The proposal is in co-legislator negotiation; it is not adopted. The refusal must be grounded in current Art. 4(8), which does not include the new third-country misuse ground proposed by the Digital Omnibus.
- Missing the parallel competent authority notification. The notification is part of the refusal under Art. 4(8) third sentence. A refusal sent to the user without parallel notification is procedurally defective.
- Drafting a refusal in the face of a Path-2 facts pattern. If the drafter cannot complete section 5(c) (irreparability) on the facts, the refusal cannot be drafted. Route to Path 2 in the scenario card: refuse to draft, explain the conjunction failure, identify the missing facts.
- Refusing on safety/security grounds dressed as trade-secret grounds. The Art. 4(2) regime is the right mechanism for safety/security; the Art. 4(8) regime is the right mechanism for trade secrets. Mixing them weakens both.
- Drafting the refusal in the user's voice or as a contract amendment. The Art. 4(8) refusal is a unilateral substantiated decision in writing; it is not a negotiation.

## Length and tone

Formal, substantiated, precise. The refusal is a regulatory action with serious consequences for the user; the tone is restrained, not adversarial. Section 5 is the substance; it carries the highest line count in the letter. Drafters should resist the temptation to pad earlier sections at the expense of section 5.

The deliverable is for adoption with minimal edit by senior in-house or external counsel. The drafter should treat the placeholders as instructions to gather facts, not as suggestions to write generically.

## Final pre-send checklist

Before sending:
- Has stage 1 been attempted and documented? (If no, do not send.)
- Can section 5(c) be drafted independently of section 5(b)? (If no, do not send. Route to Path 2.)
- Is section 5(d) populated with named elements and specific facts? (If no, redraft.)
- Has the competent authority notification been prepared and is it ready to send in parallel? (If no, do not send.)
- Has the GDPR carve-out in section 8 been included if any personal data is in scope? (If no, add.)
- Is the case-by-case statement in section 6 truthful and defensible against a "blanket policy" challenge? (If no, the matter is not stage-3.)
- Is the data holder genuinely the trade-secret holder under Art. 2(19) Data Act and Art. 2(2) TSD for the data refused? (If no, the matter may require trade-secret-holder involvement before refusal can be sustained.)
