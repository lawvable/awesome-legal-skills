# Art. 26 GDPR — Joint Controllers

This file governs the `JOINT_CONTROLLER` sub-mode. It is loaded **before** the Art. 28 checklist when the screen below indicates joint control, because misclassifying joint control as processing produces a substantively defective agreement.

## When does Art. 26 apply?

> Art. 26(1): "Where two or more controllers jointly determine the purposes and means of processing, they shall be joint controllers."

Joint control exists where two or more parties **jointly determine** **the purposes and means** of the same processing operation. The decisive criterion is **convergent influence** on essential aspects of the processing — not formal labels, not market power, not which party operates the technical infrastructure.

The reference framework is **EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR** (final version adopted 7 July 2021).

## Screen test — Art. 28 (controller–processor) vs Art. 26 (joint controllers)

Run this screen at intake whenever there is any ambiguity about roles. Each "yes" pulls towards joint control; multiple "yes" responses make a processor framing untenable.

| # | Question | Pulls towards |
|---|---|---|
| S1 | Do both parties have their own purpose for the processing (e.g. both want to use the data for their own benefit, not just provide a service to the other)? | **Joint control** |
| S2 | Is the data shared between the parties such that each can use it for its own determined purposes? | **Joint control** |
| S3 | Did one party design the processing arrangement and the other just executes it on instructions? | Processor |
| S4 | Does one party benefit from the processing only via service fees, with no autonomous use of the data? | Processor |
| S5 | Do the parties jointly decide on essential aspects: which data are collected, how long they are kept, who has access, what they are used for? | **Joint control** |
| S6 | Is the processing inseparable — neither party could meaningfully carry it out alone? | **Joint control** |
| S7 | Do the parties have independent legal bases (different Art. 6 grounds for the same operation)? | **Joint control** |
| S8 | Could the parties' relationship be described as "the Provider performs Service X for the Customer using Customer Data"? | Processor |
| S9 | Are the parties presented to data subjects as collaborating (joint branding, joint privacy notice, shared sign-up form)? | **Joint control** |
| S10 | Does one party benefit commercially from the data beyond service fees (e.g. analytics insights, model training, advertising)? | **Joint control** (and possibly separate controllership for that benefit) |

**Decision rule**:
- 0 "joint control" answers → processor relationship; use Art. 28 / DPA.
- 1–2 "joint control" answers → likely processor with caveats; verify by re-examining S1, S2, S5; if those are "no", proceed with DPA but include Art. 28(10) acknowledgment.
- 3+ "joint control" answers → joint control; switch to `JOINT_CONTROLLER` mode and draft an Art. 26 arrangement.
- **Special case**: if S10 is "yes" and the processor benefit involves the same data, the processor likely acts as a **separate controller** for that derived processing, even if it remains a processor for the original processing. Document both relationships.

## Common scenarios and their classification

| Scenario | Typical classification | Why |
|---|---|---|
| Cloud hosting (IaaS) | Processor | Provider has no own purpose for customer data |
| SaaS analytics tool used by one customer | Processor | Same as above |
| SaaS analytics tool that aggregates data across customers for benchmarking | **Joint control** for benchmarking + processor for primary use | Provider has own purpose for the aggregate |
| Payment service provider | **Often joint control or separate controllership** | PSPs determine fraud screening and AML purposes themselves |
| HR shared services across group companies | **Joint control** (unless intra-group processor structure with documented allocation) | Same purpose, same data, multiple controllers |
| Joint marketing campaign with shared lead form | **Joint control** | Both parties get the leads |
| Co-branded webinar with attendee data shared post-event | **Joint control** | Both parties want their own use of leads |
| Employer + occupational health provider | Separate controllers (not joint) | Different purposes, different legal bases |
| Co-located data centre (just space and power) | Neither (no personal data processing) | If no access to data |
| Email marketing service sending controller's lists | Processor | No own purpose |
| Email marketing service that enriches lists from its own database | **Joint control** for enrichment | Provider contributes own data with own purpose |
| Embedded social-plugin (like-button, tracking pixel) | **Joint control** for collection | Fashion ID / Wirtschaftsakademie line of CJEU cases |

## What an Art. 26 arrangement must contain

Art. 26(1)–(2) requires that joint controllers determine **in a transparent manner their respective responsibilities** for compliance with the GDPR, **in particular** as regards:

1. **Exercise of data subject rights**: which controller is the primary point of contact, how requests are routed, who responds.
2. **Information duties under Arts. 13 and 14**: who provides information, what content, in what format.

In practice, a JCA must address — beyond the two minimums above:

| # | Element | Notes |
|---|---|---|
| J1 | Scope of joint control | Which processing operations are joint; which remain separate-controllership or processing relationships |
| J2 | Allocation of GDPR compliance responsibilities | Allocation matrix — see below |
| J3 | Data subject rights — primary contact and routing | Data subject may exercise rights against either controller (Art. 26(3) — irrespective of allocation) |
| J4 | Information duties (Arts. 13/14) | Who drafts, publishes, updates the privacy notice; who handles changes |
| J5 | Breach handling | Who notifies the supervisory authority (Art. 33); who notifies data subjects (Art. 34); cooperation duties |
| J6 | Security (Art. 32) | Each party's TOMs; coordination mechanism |
| J7 | DPIA (Art. 35) | Who conducts; consultation with each other |
| J8 | Records of processing (Art. 30) | Each party maintains its own; data exchange to keep them consistent |
| J9 | International transfers | Joint approach to transfer mechanisms |
| J10 | Audit / inspection rights between joint controllers | Mutual cooperation, not the unilateral right typical of Art. 28(3)(h) |
| J11 | Liability between the joint controllers | Internal allocation (Art. 26(3) does not affect external joint-and-several liability) |
| J12 | Public summary of the arrangement | Required by Art. 26(2) — to be made available to data subjects, typically via privacy notice |
| J13 | Term, termination, and post-termination data handling | What happens to shared data when joint control ends |

### The Art. 26(2) public summary

A JCA must be summarised and **made available to the data subject**. This is usually achieved by:

- Including a section in the privacy notice titled "Joint Controllership with [Other Party]" or "Gemeinsame Verantwortlichkeit".
- The summary must explain (in plain language) the **essence** of the arrangement — at minimum the allocation of responsibilities and the contact point for rights.
- Note: data subjects may exercise rights against **either** controller regardless of the internal allocation (Art. 26(3)).

A JCA without an accompanying public-summary plan is incomplete.

## Allocation matrix template

This is the central operational artefact of any JCA. It is reproduced in `templates/jca-{lang}.md` as Annex A.

| Compliance topic | Controller A | Controller B | Joint / coordinated |
|---|---|---|---|
| Lawful basis determination | | | |
| Purpose limitation | | | |
| Data minimisation | | | |
| Storage limitation / retention | | | |
| Information duties (Art. 13/14) | | | |
| Data subject access (Art. 15) | | | |
| Rectification (Art. 16) | | | |
| Erasure (Art. 17) | | | |
| Restriction (Art. 18) | | | |
| Portability (Art. 20) | | | |
| Objection (Art. 21) | | | |
| Automated decision-making (Art. 22) | | | |
| Security measures (Art. 32) | | | |
| Breach notification to authority (Art. 33) | | | |
| Breach communication to data subjects (Art. 34) | | | |
| DPIA (Art. 35) | | | |
| Prior consultation (Art. 36) | | | |
| Records of processing (Art. 30) | | | |
| International transfers | | | |
| Cooperation with supervisory authorities | | | |

Every cell must be filled. Empty cells are deferred decisions — do not deliver a JCA with blanks.

## What does NOT belong in a JCA

- **Art. 28 mandatory clauses** — these apply controller→processor; they have no analogue in a controller↔controller relationship, and copying them produces nonsense.
- **Sub-processor clauses** — joint controllers may each engage their own processors, but those are governed by separate Art. 28 contracts, not by the JCA.
- **Audit rights modelled on Art. 28(3)(h)** — joint controllers cooperate; they do not audit each other in the same sense.

## Hybrid relationships

It is common for the same parties to have **multiple coexisting roles** for different processing operations:

- Joint controllers for the primary processing operation; AND
- Separate controllers for derived processing operations they each conduct on their own copies of the data; AND
- Controller-processor where one party also performs purely operational services for the other.

In this case, document each relationship with the appropriate instrument — a JCA for the joint part, a DPA for the processing part, and (if needed) a data-sharing agreement for the separate-controllership part. **Do not collapse them into a single document** — the legal characterisation of each piece is different and each requires different mandatory content.

## Output checklist for `JOINT_CONTROLLER` mode

- [ ] Roles analysis written, with EDPB 07/2020 anchors cited.
- [ ] Screen test results documented (which questions pulled towards joint control).
- [ ] JCA main body addresses J1–J13.
- [ ] Allocation matrix completed (no empty cells).
- [ ] Public summary drafted (separate document or insertable privacy-notice section).
- [ ] Recital noting Art. 26(3) (data subjects may exercise rights against either controller).
- [ ] Any coexisting Art. 28 / separate-controllership relationships flagged with recommendation to paper separately.
