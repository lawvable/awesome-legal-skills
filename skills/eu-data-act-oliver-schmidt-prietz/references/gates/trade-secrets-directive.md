# Trade Secrets Directive overlay

This gate covers the interaction between the Data Act and Directive (EU) 2016/943 on the protection of undisclosed know-how and business information (trade secrets) against their unlawful acquisition, use and disclosure (the Trade Secrets Directive, TSD). The TSD is the underlying substantive regime for trade secrets in the Union; the Data Act layers a specific access regime on top, with the three-stage handbrake described in Art. 4(6)-(8) and Art. 5(9)-(11).

The gate's job is to identify when trade-secret protection is in play, run the operative limbs of the Data Act handbrakes against the TSD's substantive baseline, and produce an output that respects both regimes. Most Data Act practitioners are reasonably familiar with the handbrake structure but less familiar with the underlying TSD; the gate keeps both in view.

The structure: scope and applicability; the TSD baseline; the Data Act trade-secret regime (the three-stage ladder); the "serious and irreparable" conjunction; objective elements; technical and organisational measures; the data holder's notification and substantiation obligations; redress for users and third parties; what the skill produces in the output.

---

## When the gate applies

The gate runs whenever any of the following is true:

- A data holder asserts or considers asserting that some or all of the requested data is a trade secret
- The user or third party requests data that the data holder has previously treated as confidential, proprietary, or non-public
- The scenario involves data that contains information likely to qualify as a trade secret (technical specifications, manufacturing processes, customer data with commercial sensitivity, proprietary algorithms, business intelligence)
- The scenario involves negotiation or drafting of safeguards under Art. 4(6) or Art. 5(9)
- The scenario involves drafting of a withholding, suspension, or refusal notice under Art. 4(7), Art. 4(8), Art. 5(10), or Art. 5(11)
- The scenario involves competent authority notification under any of the above
- The scenario involves a challenge to a refusal by a user or third party

The skill runs the gate even when the data holder has not yet explicitly invoked trade-secret protection. Trade-secret considerations are often unstated until the access request is made; the gate identifies the considerations proactively.

---

## The Trade Secrets Directive baseline

Directive (EU) 2016/943 establishes the EU-harmonised substantive regime for trade secrets. The TSD does not create trade-secret rights as property; it creates remedies against unlawful acquisition, use, and disclosure. The TSD applies regardless of the Data Act and is the analytical baseline for what is and is not a trade secret.

**Definition of trade secret (Art. 2(1) TSD).** Information that meets all of the following requirements:

- It is secret, in the sense that it is not generally known among or readily accessible to persons within the circles that normally deal with the kind of information in question.
- It has commercial value because it is secret.
- It has been subject to reasonable steps under the circumstances, by the person lawfully in control of the information, to keep it secret.

All three limbs are cumulative. Information that is generally known fails the first limb. Information that is confidential but has no commercial value (e.g. embarrassing internal memos) fails the second. Information that is commercially valuable but has not been actively protected (no NDAs, no access controls, no markings) fails the third. The Data Act adopts this definition by reference in Art. 2(18).

**Lawful acquisition, use, and disclosure (Art. 3 TSD).** The TSD lists categories of lawful acquisition: independent discovery, reverse engineering of lawfully obtained products, exercise of rights of workers' representatives, and "any other practice which, under the circumstances, is in conformity with honest commercial practices." Lawful use and disclosure where required or allowed by Union or national law is also covered. The Data Act's mandatory access regime is such a Union law requirement; access to and disclosure of trade-secret data under the Data Act handbrake is therefore lawful within the TSD framework. Recital 31 of the Data Act makes this connection explicit.

**Unlawful acquisition, use, and disclosure (Art. 4 TSD).** Acquisition without consent of the trade-secret holder where carried out by unauthorised access to documents or by any other conduct contrary to honest commercial practices. Use or disclosure where the person uses without authorisation, in breach of a confidentiality agreement, or where the person knew or ought to have known the trade secret was obtained unlawfully.

**Exceptions (Art. 5 TSD).** Acquisition, use, or disclosure for the exercise of the right to freedom of expression; for revealing misconduct, wrongdoing, or illegal activity (whistleblowing); for the exercise of workers' representative functions; and for protecting a legitimate interest recognised by Union or national law.

**Remedies (Arts. 9-15 TSD).** Provisional and precautionary measures (Art. 10), injunctions and corrective measures (Art. 12), damages (Art. 14), publication of judicial decisions (Art. 15). Member State implementation has produced varied procedural and enforcement landscapes; the skill does not opine on Member State remedies.

The TSD's substantive definition and lawfulness framework operate in the background of every Data Act trade-secret analysis. The Data Act handbrake is a specific access-and-disclosure regime under Art. 3(2)(d) TSD ("required or allowed by Union or national law"); it does not override the TSD's underlying definition or remedies.

---

## The Data Act trade-secret regime: the three-stage ladder

The Data Act layers three stages of trade-secret protection on top of the TSD baseline. The ladder is the same for users (Art. 4(6)-(8)) and for third parties to whom the user directs disclosure (Art. 5(9)-(11)). The stages are mandatory in sequence: the data holder cannot jump to stage three without first attempting stage one and, if unsuccessful, considering stage two.

### Stage 1: identify and safeguard (Art. 4(6), Art. 5(9))

The data holder identifies the trade secrets in the requested data before disclosure and agrees with the user or third party proportionate technical and organisational measures necessary to preserve the confidentiality of the shared data.

The data holder bears the identification burden. The data holder cannot pass an undifferentiated dataset to the user with a blanket "all is trade secret" assertion. Identification is data-by-data, or category-by-category where the categories are objectively defined. The relevant metadata can be tagged to identify trade-secret data.

The safeguards are negotiated, not imposed. The regulation lists examples: model contractual terms, confidentiality agreements, strict access protocols, technical standards, codes of conduct. The list is illustrative ("such as"); other measures are admissible if they are proportionate. The measures must be agreed prior to the disclosure.

Proportionality is the operative standard. Excessive safeguards (NDA-by-NDA chains, on-premises only access where remote access is technically secure, restrictions on internal sharing within a recipient organisation that prevent reasonable use) are not proportionate. Inadequate safeguards (verbal undertakings, no contract, no access controls) do not meet the standard either.

Recital 31 of the Data Act elaborates: "data holders should be able to require users, or third parties of a user's choice, to preserve the confidentiality of data considered to be trade secrets. To that end, data holders should identify trade secrets prior to the disclosure, and should have the possibility to agree with users, or third parties of a user's choice, on necessary measures to preserve their confidentiality, including by the use of model contractual terms, confidentiality agreements, strict access protocols, technical standards and the application of codes of conduct."

FAQ Q23 confirms the stage-1 obligation: "When a data holder receives a request to access data, it must identify the trade secrets that need to be shared and agree with the user/third party on the necessary measures to preserve their confidentiality (Articles 4(6) and 5(7) of the Data Act). These safeguards need to be in place prior to the sharing of data."

The Commission's MCTs (pointer at `sources/mcts-sccs-recommendation-pointer.md`) provide template safeguard clauses that can serve as the starting point. The MCTs are non-binding; use is voluntary; safe harbour does not attach to verbatim use.

### Stage 2: withhold or suspend (Art. 4(7), Art. 5(10))

If there is no agreement on the necessary measures, or if the recipient fails to implement the agreed measures, or if the recipient undermines the confidentiality of the trade secrets, the data holder may withhold or suspend the sharing of data identified as trade secrets.

Stage 2 is conditional, not unconditional. The trigger is one of three:

- **No agreement.** The data holder and recipient have negotiated in good faith and cannot agree on proportionate measures. Disagreement that the data holder has caused by demanding disproportionate measures is not a stage 2 trigger.
- **Failure to implement.** The recipient has agreed to measures and not implemented them. The data holder must demonstrate the failure; mere assertion does not suffice.
- **Undermining confidentiality.** The recipient has acted to compromise the trade secret (disclosure to a third party, removal of technical protections, breach of access protocols). The data holder must demonstrate the undermining.

Where any of the three is met, the data holder may withhold the data not yet shared or suspend sharing of data already in flight. The decision must be duly substantiated and provided in writing to the recipient without undue delay.

Competent authority notification is mandatory. The data holder must notify the competent authority designated under Art. 37, identifying which measures have not been agreed or implemented and, where relevant, which trade secrets have had their confidentiality undermined.

Stage 2 is procedurally less burdensome than stage 3 but substantively still requires evidence. A data holder that withholds without satisfying one of the three triggers exposes itself to challenge by the recipient and to complaint to the competent authority.

### Stage 3: refuse (Art. 4(8), Art. 5(11))

In exceptional circumstances, where the data holder is a trade secret holder and is able to demonstrate that it is highly likely to suffer serious economic damage from the disclosure of trade secrets, despite the technical and organisational measures taken by the recipient under stage 1, the data holder may refuse on a case-by-case basis a request for access to the specific data in question.

Stage 3 is the most demanding. The cumulative limbs:

- **Exceptional circumstances.** Not the ordinary case. The recital and the regulation use the language "in exceptional circumstances" deliberately to signal that stage 3 is the residual, last-resort option. Routine application is a misuse.
- **Data holder is a trade secret holder.** The data holder must itself be the trade secret holder within the meaning of Art. 2(19) of the Data Act (which references Art. 2(2) TSD: any natural or legal person lawfully controlling a trade secret). A data holder that has licensed-in third-party trade secrets faces a more complex analysis.
- **Highly likely to suffer serious economic damage.** The standard. "Highly likely" is more demanding than "possible" or "likely." "Serious economic damage" is defined in Recital 31 as "serious and irreparable economic loss." Both elements (serious AND irreparable) must be demonstrated.
- **Despite the safeguards.** The damage must be highly likely notwithstanding the stage-1 technical and organisational measures the recipient has taken. A data holder that has not first attempted stage 1 cannot reach stage 3.
- **Demonstrated on objective elements.** Not subjective concern. Recital 31 lists illustrative elements: enforceability of trade secret protection in third countries, nature and level of confidentiality of the data requested, uniqueness and novelty of the connected product. The list is non-exhaustive; other objective elements are admissible.
- **Case by case.** Each request is assessed on its own facts. A blanket "we refuse all requests for X category of data" is not a case-by-case refusal.
- **In writing without undue delay.** The substantiation is provided to the recipient in writing, promptly.
- **Competent authority notification.** The data holder notifies the competent authority of the refusal.

A refusal that misses any of these limbs is exposed to challenge. The recipient may lodge a complaint with the competent authority, agree to refer the matter to a dispute settlement body, or seek redress before a court or tribunal.

---

## The "serious and irreparable" conjunction

Recital 31 of the Data Act states: "Serious economic damage implies serious and irreparable economic loss."

Both elements are required.

- **Serious.** The loss must be of significant magnitude. Reasonable cost increases, foregone opportunities of modest value, or temporary competitive disadvantage do not meet the standard. The loss must rise to a level where the underlying business viability or competitive position is materially affected.
- **Irreparable.** The loss must be incapable of repair through ordinary commercial mitigation. Damage that can be recovered through subsequent commercial action, that is covered by insurance, that can be undone through contractual remedies against the recipient, or that diminishes over time as the underlying trade secret becomes obsolete is not irreparable.

The conjunction is the principal substantive guardrail against stage-3 misuse. A data holder that demonstrates serious loss but not irreparable loss has not met the threshold. A data holder that demonstrates irreparable loss but of modest magnitude has not met it either. The combination is what justifies refusal of a Data Act access right.

This is the single most common Data Act drafting failure in this area, as discussed in `references/gotchas.md` entries 6, 7, and 8 (the circular trap cluster). The skill flags the conjunction in every stage-3 deliverable.

---

## Objective elements

Recital 31 lists three illustrative objective elements:

- **Enforceability of trade secret protection in third countries.** Where the recipient is established in a third country with weak or non-existent trade secret protection, the data holder's stage-3 demonstration is strengthened. The element addresses the practical reality that EU-internal safeguards have limited reach against extra-EU recipients in jurisdictions where Union and Member State remedies are unavailable.
- **Nature and level of confidentiality of the data requested.** The more sensitive and tightly held the data, the stronger the demonstration. Information that the data holder treats as top-tier proprietary (manufacturing processes, AI model parameters, customer pricing strategies) supports a stronger case than information held in less restrictive confidentiality categories.
- **Uniqueness and novelty of the connected product.** Trade-secret data tied to a unique or novel product carries more weight than data tied to a commoditised or mature product. The element protects R&D investment in cutting-edge connected products against premature competitive exposure.

The list is introduced by "in particular." It is illustrative, not exhaustive (see `references/gotchas.md` entry 8). Other objective elements admissible in a stage-3 demonstration:

- The specific risk that the recipient or its affiliates compete with the data holder in the relevant product market
- The inadequacy of the stage-1 safeguards offered by the recipient in light of past incidents or the recipient's compliance record
- The scale of the data requested in relation to the recipient's stated purpose (a stage-3 demonstration is stronger where the recipient's purpose can be served by significantly less data)
- The risk that the trade secret will be reverse-engineered from the disclosed data even with the stage-1 safeguards in place
- The cybersecurity exposure introduced by disclosure (some trade secrets, once compromised, expose downstream systems to attack)
- AI-related risks, including the risk that the disclosed data will be used to train models that will then compete with the data holder's products or services

The skill recommends documenting the specific objective elements relied on in any stage-3 refusal letter. Vague reliance on "competitive harm" without naming the elements is exposed to challenge.

---

## Technical and organisational measures

Stage 1 safeguards are technical and organisational. The regulation does not specify minimum measures; the standard is proportionality.

Common technical measures:

- **Access controls.** Authentication, authorisation, role-based access, segregation of duties within the recipient organisation.
- **Encryption.** Data encrypted in transit and at rest; key management on the data holder side or via independent key escrow.
- **Audit logging.** Recipient maintains immutable logs of access and use; the data holder may audit on reasonable notice.
- **Data minimisation.** The recipient receives only the trade-secret data it needs for the agreed purpose; surrounding non-trade-secret data is provided separately.
- **Watermarking and fingerprinting.** Technical markers in the data that allow the data holder to identify leaks if the data appears outside the recipient's controlled environment.
- **Sandboxed environments.** The recipient processes the data only within an environment controlled by or jointly with the data holder, preventing local copies.
- **Differential privacy and synthetic data.** Where the purpose permits, the recipient receives data treated to remove specific trade-secret information while preserving analytical utility.

Common organisational measures:

- **NDAs and confidentiality agreements.** Standard but rarely sufficient on their own.
- **Restricted-access teams.** The recipient designates specific individuals authorised to access the trade-secret data; access is segregated within the recipient organisation.
- **Training.** Authorised recipient personnel trained on the trade-secret nature of the data and the consequences of misuse.
- **Background checks.** For personnel with access to highly sensitive trade secrets.
- **Sub-recipient controls.** Restrictions or prohibitions on the recipient's onward sharing within its corporate group or with sub-recipients.
- **Audit rights.** The data holder has contractual audit rights over the recipient's compliance with the technical and organisational measures.
- **Incident response.** Defined procedures for the recipient to notify the data holder of any suspected confidentiality breach, with cooperation obligations for investigation.

The skill recommends a layered approach: at least one strong technical measure (typically encryption with sandboxed access or watermarking) plus organisational measures (NDA, restricted-access team, audit rights, incident response). Single-layer reliance on NDAs alone is fragile.

---

## Data holder substantiation obligations

The data holder bears the substantiation burden at every stage of the ladder.

- **Stage 1.** Identification of trade secrets, including in the relevant metadata. Proposal of proportionate safeguards. Good-faith negotiation with the recipient.
- **Stage 2.** Written, duly substantiated decision to withhold or suspend, provided to the recipient without undue delay. Competent authority notification with identification of which measures have not been agreed or implemented and, where relevant, which trade secrets have had their confidentiality undermined.
- **Stage 3.** Written, duly substantiated refusal, on objective elements demonstrating highly likely serious and irreparable economic damage, on a case-by-case basis, without undue delay. Competent authority notification.

The substantiation must be in writing. Oral assertions are not sufficient. The standard is "duly substantiated," not "asserted." A data holder that asserts trade-secret status without identifying the data, without proposing safeguards, or without explaining the objective basis for refusal has not substantiated.

The competent authority notification under Art. 37 makes the data holder's decision visible to the regulator. The competent authority may scrutinise the substantiation. Repeated, unsupported invocations of the handbrake by a single data holder will attract enforcement attention.

---

## Redress for users and third parties

Where the data holder withholds, suspends, or refuses, the user or third party has redress under Art. 4(9) and Art. 5(12).

- **Court or tribunal.** The user or third party may seek redress at any stage before a court or tribunal of a Member State. This is the unconditional baseline.
- **Complaint to competent authority.** Under Art. 37(5)(b), the user or third party may lodge a complaint with the competent authority designated under Art. 37. The competent authority shall, without undue delay, decide whether and under which conditions data sharing should start or resume.
- **Dispute settlement body.** The user or third party may agree with the data holder to refer the matter to a dispute settlement body certified under Art. 10. Dispute settlement is voluntary; the data holder's consent is required.

The redress mechanisms are alternatives, not sequential. The user may choose the most appropriate forum. The skill flags all three options in any deliverable involving a contested refusal.

---

## What the skill produces in the output

When the gate is run, the output includes a dedicated "Trade-secret regime" section. Minimum content:

- Identification of the data the data holder claims as trade secret, with the TSD Art. 2(1) three-limb test applied (secret, commercial value, reasonable steps).
- The stage of the ladder engaged (stage 1, 2, or 3).
- For stage 1: identification of the proposed technical and organisational measures, with proportionality analysis.
- For stage 2: identification of which trigger (no agreement, failure to implement, undermining) is engaged, with evidence.
- For stage 3: identification of the objective elements relied on, with explicit treatment of both "serious" and "irreparable" elements of the damage demonstration.
- The competent authority notification status.
- The redress options available to the user or third party.

Where the deliverable is a stage-3 refusal letter, the structure additionally tracks the regulatory limbs of Art. 4(8) or Art. 5(11):

1. Identification of the requesting user or third party and the data requested.
2. Statement that the data holder is the trade secret holder for the specific data.
3. Identification of the exceptional circumstances justifying recourse to stage 3.
4. Identification of the safeguards proposed under stage 1 and the reasons they are insufficient.
5. Demonstration of highly likely serious AND irreparable economic damage, on objective elements, naming the elements.
6. Statement that the refusal is on a case-by-case basis.
7. Notification to the competent authority (in parallel).
8. Information on the user or third party's redress options.

The skill produces the letter in formal correspondence format, ready for adoption with minimal edit. The skill does not include CYA padding; the letter is a substantive legal communication.

---

## The McIntyre OSS perspective and enforcement signals

Practitioner commentary on the Data Act trade-secret regime has emerged in the period since 12 September 2025. The McIntyre OSS enforcement digest (and similar practitioner sources) has documented early competent authority practice on stage-2 and stage-3 notifications. Patterns visible:

- Competent authorities are scrutinising stage-3 refusals more closely than stage-2 withholds. The exceptional-circumstances threshold is being applied strictly.
- The conjunction error (serious without irreparable) is the most common defect in stage-3 refusals submitted to competent authorities in the first months of application.
- Data holders that have engaged in good-faith stage-1 negotiation and documented the negotiation are treated more favourably than data holders that have refused without preliminary negotiation.
- Competent authorities are willing to order resumption of data sharing where the stage-3 substantiation is weak, even before a court has ruled.

The skill treats these as enforcement signals to factor into stage-3 deliverables. The risk profile of a stage-3 refusal is not "we refuse and the user sues if they care enough" but "we refuse, the user complains to the competent authority, and the competent authority orders resumption within weeks." Stage-3 refusals are high-risk and should be reserved for cases where the substantiation is genuinely strong.

---

## Cross-references

- `references/gotchas.md` entries 6, 7, and 8 are the failure-mode catalogue versions of the ladder structure, the conjunction error, and the illustrative objective elements. The gate file gives the operational mechanics; the gotchas give the traps.
- `references/method/analysis-method.md` calls this gate "the circular trap" at the cognitive-discipline level; the gate file unpacks the discipline into operational steps.
- `references/gates/gdpr-overlay.md` runs in parallel where the trade-secret data also includes personal data. The TSD safeguards and GDPR safeguards are cumulative.
- `sources/regulation-2023-2854.md` Art. 2(18)-(19) (definitions), Art. 4(6)-(8), Art. 5(9)-(11), Art. 19(3) (Ch V trade-secret disclosure), Recital 31.
- `sources/faq-v1-4.md` FAQ Q4 (trade secrets handbrake referenced in the IoT scope table), Q23 (handling trade secrets and activating the handbrake), Q24 (Art. 3 direct access does not benefit from the handbrake by default).
- `sources/mcts-sccs-recommendation-pointer.md` for safeguard clause templates.
- Directive (EU) 2016/943 (TSD), particularly Art. 2 (definitions), Art. 3 (lawful acquisition), Art. 4 (unlawful acquisition), Art. 5 (exceptions), Arts. 9-15 (remedies).
- Member State implementing legislation of the TSD: not maintained in this skill. The TSD has been implemented across all Member States; national procedural and remedial variation is material. Consult local counsel for litigation strategy.
