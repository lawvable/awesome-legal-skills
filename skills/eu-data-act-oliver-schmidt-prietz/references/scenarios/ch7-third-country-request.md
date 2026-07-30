# ch7-third-country-request

**Anchor:** Provider × Ch VII × Art. 32 third-country governmental access to non-personal data held in the Union. The card walks the two operative paths (international agreement under Art. 32(2); the cumulative three-condition path under Art. 32(3)) and the procedural duties under Art. 32(1), (4) and (5).

**Routes from:**

- "We've received a subpoena/court order/administrative request from a non-EU authority for customer data."
- "How do we respond to a US CLOUD Act warrant against EU-stored data?"
- "Can we comply with a third-country production order? What does Art. 32 require?"
- "Our cloud customer is asking about our Art. 32 framework."
- "Does Art. 32 cover transfers between our EU and US affiliates?"

**Adjacent cards (route there instead if the facts indicate):**

- The data requested is personal data: Art. 32 does not apply. GDPR Chapter V governs (Arts. 44 to 50 GDPR plus Schrems II / EDPB transfer-impact assessment framework). Route to `cross-gdpr-boundary.md` for the boundary and to specialist GDPR Ch V counsel.
- The request is a private-to-private transfer (no governmental authority involved): Art. 32 does not apply (FAQ Q61). Contractual analysis only.
- The provider is the addressee of an internal company directive (not an external authority decision): Art. 32 does not engage. Internal compliance review only.

---

## Canonical fact pattern

A provider of data processing services within the meaning of Art. 2(8) of Regulation (EU) 2023/2854 (Data Act) holds non-personal data in the Union for one or more customers. The provider receives a decision, judgment, or production order from a third-country court, tribunal, or administrative authority requiring transfer of, or access to, that data. The provider's compliance with the order would risk a conflict with Union law or the national law of the Member State in which the data is held (typically: trade-secret protection under Directive (EU) 2016/943; intellectual property rights; commercial confidentiality undertakings; national security or defence interests of the Union or a Member State).

The data in scope is non-personal. If any personal data is implicated, the GDPR Chapter V regime governs that portion in parallel, on a separate legal track.

---

## Critical disciplines

Three points trip up almost every Art. 32 compliance posture in the practitioner literature.

- **Art. 32 is non-personal-data-only.** Art. 32(2), (3) and (4) speak to "non-personal data falling within the scope of this Regulation." Personal data is governed by GDPR Chapter V, not by the Data Act. A provider that holds mixed datasets must split the analysis: Data Act Art. 32 for the non-personal portion, GDPR Chapter V for the personal portion. FAQ Q61 confirms: "International transfers of personal data are regulated under the GDPR." See `references/gotchas.md` entry 18.
- **Art. 32(3) is conjunctive.** The three conditions are joined by "and." All three must be met for the transfer or access to be permissible on the Art. 32(3) path. Reading the list as a menu of options is the most common Art. 32 drafting error. See `references/gotchas.md` entry 18.
- **Art. 32(2) and 32(3) are alternative routes.** Art. 32(2) provides the recognised/enforceable route via international agreement (e.g. an MLAT). Art. 32(3) provides the residual route in the absence of such an agreement. The provider chooses based on whether an applicable international agreement exists, not based on which is more convenient.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. The provider must be a "provider of data processing services" within Art. 2(8). The data must be "non-personal data falling within the scope of this Regulation" and "held in the Union" (Art. 32(1) to (4)). The Art. 1(6) carve-outs apply: if the matter falls under Union or national legal acts on criminal-law cooperation (Regulations (EU) 2021/784, (EU) 2022/2065, (EU) 2023/1543 and Directive (EU) 2023/1544 are listed) or under Regulation (EU) 2015/847 and Directive (EU) 2015/849 (anti-money laundering), the Data Act does not displace those instruments.

National security, defence, public security, and the maintenance of law and order remain Member State competence and outside the scope of Union law (Art. 1(6) final sub-paragraph). Where the order touches on these, the provider escalates within the Member State framework in parallel with the Art. 32 analysis.

### Step 2: Chapter identification

Chapter VII. Art. 32 is the operative provision for international governmental access and transfer. Adjacent Ch VI provisions on switching are not engaged by an Art. 32 request. Adjacent Ch II provisions on user access are not engaged unless the underlying user is making a parallel request.

### Step 3: Role mapping

Required entity-by-entity mapping.

| Entity | Data Act role | GDPR role (if personal data also in scope) | Other |
|--------|---------------|---------------------------------------------|-------|
| The provider receiving the order | Provider of data processing service (Art. 2(8)); addressee of the third-country decision (Art. 32(3)) | Processor for customer personal data, typically; controller for its own operational data |  |
| The customer whose data is requested | Customer of the data processing service (Art. 2(30)); typically also user of any connected products integrated with the service | Controller of any personal data within the dataset |  |
| The third-country authority | Outside the Data Act addressee scheme; the order is what the Data Act assesses |  | Authority of [third country] under its national or federal law |
| The relevant national body or authority for international cooperation in legal matters | Consultation body under Art. 32(3) second sub-paragraph |  | Bundesjustizamt in Germany; Bureau de l'entraide pénale internationale in France (FAQ Q63 framing) |
| The Member State data coordinator | Optional consultation body under FAQ Q63 |  | Designated under Art. 37 |

The provider's GDPR role for any incidentally personal data routinely shifts the analysis. A provider that is a processor for its customer's personal data is also bound by Art. 28 GDPR controller-processor terms, which typically include obligations not to disclose to third-country authorities except as required by Union or Member State law.

### Step 4: Fact-category sorting

Card-specific dimensions to sort the requested data against.

- **Personal vs non-personal data.** Drives whether Art. 32 or GDPR Ch V governs. If the requested data is mixed (Recital 7 inextricably-linked), the provider runs Art. 32 for the non-personal portion and the GDPR transfer regime for the personal portion. The two tracks may yield different outcomes.
- **Trade-secret data vs not.** Within the non-personal portion, identify whether any of the data is protected as a trade secret under Directive (EU) 2016/943 or as commercial confidentiality. Recital 101 of the Data Act flags trade-secret protection, intellectual property rights, and confidentiality undertakings as the principal Union-law conflicts that bring Art. 32(1) and (3) into operation.
- **National security or defence interests.** A separate flag. The Art. 32(3) second sub-paragraph allows the addressee to consult the relevant national body to determine whether the order impinges on Union or Member State national-security or defence interests. If so, refusal on those grounds is available independently of the three conjunctive conditions.
- **Data held in the Union vs elsewhere.** Art. 32 applies to non-personal data held in the Union. Data held outside the Union is not protected by Art. 32 even where the provider is otherwise Union-established. The location-of-data fact is load-bearing.

### Step 5: Limb-by-limb application of Art. 32

#### Art. 32(1): general preventive duty

The provider takes "all adequate technical, organisational and legal measures, including contracts, in order to prevent international and third-country governmental access and transfer of non-personal data held in the Union where such transfer or access would create a conflict with Union law or with the national law of the relevant Member State." Recital 102 elaborates: encryption, audits, certification, and corporate policy modification are among the measures. The duty is preventive and pre-litigation; it operates before any specific order is received. See FAQ Q62 (Commission interpretation).

#### Art. 32(2): international agreement path

A decision or judgment of a third-country authority "shall be recognised or enforceable in any manner only if based on an international agreement, such as a mutual legal assistance treaty, in force between the requesting third country and the Union, or any such agreement between the requesting third country and a Member State."

The threshold test:

1. Does an international agreement exist between the requesting third country and either the Union or the relevant Member State?
2. Is the agreement in force at the time of the request?
3. Does the agreement cover the type of request in question (criminal MLAT, civil cooperation, sectoral agreement)?

If yes to all three, the order can be recognised or enforced on the Art. 32(2) path. The provider's compliance posture is then governed by the agreement's terms (typically including domestic procedural channels rather than direct compliance by the provider).

If no, Art. 32(2) is unavailable and the provider proceeds to Art. 32(3).

#### Art. 32(3): the three cumulative conditions

In the absence of an international agreement under Art. 32(2), and where compliance would risk a conflict with Union or Member State law, transfer or access "shall take place only where" all three conditions are met:

1. **Reasoned and specific decision.** The third-country system requires the reasons and proportionality of the decision to be set out, and requires the decision to be specific in character, "for instance by establishing a sufficient link to certain suspected persons or infringements" (Art. 32(3)(a)).
2. **Reviewable on reasoned objection.** The reasoned objection of the addressee is subject to a review by a competent third-country court or tribunal (Art. 32(3)(b)).
3. **Court empowered to weigh Union interests.** The competent third-country court or tribunal "is empowered under the law of that third country to take duly into account the relevant legal interests of the provider of the data protected by Union law or by the national law of the relevant Member State" (Art. 32(3)(c)).

All three are required. Missing any one means the provider may not grant access on the Art. 32(3) path. The conditions assess the third-country legal system, not the individual order; the inquiry is structural.

#### Art. 32(3) second sub-paragraph: consultation right

The addressee "may ask the opinion of the relevant national body or authority competent for international cooperation in legal matters" to determine whether the three conditions are met, particularly where the order may relate to trade secrets, commercially sensitive data, IP-protected content, or where transfer may lead to re-identification.

National-body identification, per the Commission's interpretation in FAQ Q63: the provider checks which administrative entity in its Member State is normally responsible for implementing Mutual Legal Assistance Treaties. The Commission gives two examples: Bundesjustizamt in Germany; Bureau de l'entraide pénale internationale in France. The Member State data coordinator (designated under Art. 37) is a back-up consultation point in case of doubt.

The national body may consult the Commission. If the addressee has not received a reply within one month, or if the opinion concludes that the conditions are not met, the addressee "may reject the request for transfer or access, to non-personal data, on those grounds."

A separate national-security consultation track exists where the addressee considers the order may impinge on Union or Member State national-security or defence interests. The addressee shall (not may) ask the relevant national body in that case. If the body confirms national-security or defence interests are engaged, refusal on those grounds is available independently.

The EDIB (Art. 42) advises and assists the Commission in developing guidelines on the assessment of whether the Art. 32(3) conditions are met. Guidelines have not been published as of the skill's source date.

#### Art. 32(4): minimisation

Where the provider may lawfully respond on either path, it provides "the minimum amount of data permissible in response to a request, on the basis of the reasonable interpretation of that request by the provider or relevant national body or authority." The provider is not at liberty to over-comply.

#### Art. 32(5): customer notification

The provider "shall inform the customer about the existence of a request of a third-country authority to access its data before complying with that request." The duty is mandatory ("shall"), pre-compliance, and subject to one narrow carve-out: law-enforcement requests for as long as customer notification would prejudice the effectiveness of the law-enforcement activity. The carve-out is narrow and time-limited; it does not authorise indefinite non-notification.

### Step 6: Cross-regime gate check

- **GDPR overlay (load if any personal data in scope).** Art. 32 does not govern personal data. Where the dataset is mixed, run `references/gates/gdpr-overlay.md` for the personal portion and address Chapter V GDPR (transfer mechanisms, derogations, Schrems II / EDPB TIA) in a parallel track. Confirm in the output that the two tracks were run separately. Personal data may not be transferred to satisfy the third-country order if no GDPR transfer mechanism applies, even where the Art. 32 analysis would permit the non-personal portion.
- **Trade Secrets Directive overlay.** Trade-secret-protected data within the non-personal portion strengthens the Union-law-conflict argument under Art. 32(1) and (3). Recital 101 names trade secrets specifically. Run `references/gates/trade-secrets-directive.md` if the data includes trade-secret-protected material; the gate file's analytical framework supports the conflict assessment.
- **Sectoral lex specialis (warn-only).** If the customer's data relates to a regulated sector (financial services, energy, health, defence-related, NIS2-covered, eIDAS), sectoral law may impose additional restrictions on cross-border disclosure to third-country authorities. Run `references/gates/sectoral-lex-specialis.md` and flag the overlay.
- **Member State implementing law.** The "relevant national body or authority competent for international cooperation in legal matters" varies by Member State. Identify the body for the Member State where the data is held; this is the operative jurisdiction for the Art. 32(3) consultation. Run `references/gates/member-state.md` if the Member State is not on the FAQ Q63 list.
- **Criminal-law-cooperation carve-out.** Art. 1(6) carves out criminal-law-cooperation acts (Regulations (EU) 2021/784, (EU) 2022/2065, (EU) 2023/1543; Directive (EU) 2023/1544). If the order is for criminal-law purposes and one of these instruments applies, Art. 32 does not displace the sectoral regime. The provider runs the sectoral regime first; Art. 32 may still apply residually.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 32(1) to (5) of Regulation (EU) 2023/2854 (Data Act) governs. The three Art. 32(3) conditions are conjunctive. National-body consultation is available. Customer notification under Art. 32(5) is mandatory. Verbatim text at `sources/regulation-2023-2854.md` Art. 32; Recitals 101 and 102.
- **Proposed amendment under Digital Omnibus.** COM(2025) 833 final (19 November 2025) does not propose substantive amendment to Art. 32 as such, but the proposed new Art. 4(8) and 5(11) refusal ground for substantial risk of unlawful trade-secret acquisition, use, or disclosure to third-country entities operating under weaker-protection legal regimes is structurally adjacent. The proposal does not change Art. 32 itself. Status: co-legislator negotiation, not adopted. See `sources/digital-omnibus-amendments-tracker.md`.

The output cites current law as operative. Art. 32 is not on the principal Omnibus amendment list.

---

## Decision point

After Steps 5 and 6, the analysis yields one of four paths.

1. **Art. 32(2) available: international agreement in force.** Compliance is on the agreement's terms, which typically route the request through the Member State's domestic legal channels rather than direct provider action. The provider notifies the customer under Art. 32(5) and follows the agreement's procedural channel.
2. **Art. 32(3) all three conditions met.** Transfer or access is permitted, subject to Art. 32(4) data minimisation and Art. 32(5) customer notification. The provider produces a structured Art. 32(4) minimisation analysis before responding.
3. **Art. 32(3) at least one condition unmet, or national-body opinion negative, or national-security or defence interests engaged.** Provider refuses on those grounds. The Art. 32(3) second sub-paragraph framing applies: "the addressee may reject the request for transfer or access, to non-personal data, on those grounds." The provider notifies the customer under Art. 32(5) of the request and the refusal.
4. **Art. 32 does not govern (personal data in scope, criminal-law-cooperation carve-out, private-to-private context).** The Art. 32 analysis does not produce the answer. Run the applicable regime (GDPR Ch V, sectoral act, or contract) and route accordingly.

---

## Output skeleton: Path 1 or 2 (compliance possible)

Memorandum-style internal note plus a structured external response. Markdown by default.

```
Subject: Response to [third-country authority] data request dated [date]
Reference: [Provider's internal reference]

1. The request
   [Identification of the requesting authority, the order, the data
   requested, and the deadline.]

2. Scope of Article 32
   [Identification of the data as non-personal data falling within
   the scope of Reg. (EU) 2023/2854. If the dataset is mixed, the
   personal-data portion is addressed separately under GDPR Ch V.]

3. Article 32(2) assessment
   [Whether an applicable international agreement exists. If so,
   identification of the instrument and the procedural channel.]

4. Article 32(3) assessment (if applicable)
   4(a) Reasoned and specific decision (Art. 32(3)(a)).
   4(b) Reasoned-objection review (Art. 32(3)(b)).
   4(c) Empowerment of the third-country court to weigh Union
        interests (Art. 32(3)(c)).
   [Each condition assessed against the third-country legal system,
   with citation to the operative provisions of that system. If a
   condition is unmet, the analysis stops here and the refusal track
   engages.]

5. National-body consultation (Art. 32(3) sub-para. 2)
   [Whether the relevant national body has been consulted, the body
   identified ([Bundesjustizamt for Germany; Bureau de l'entraide
   pénale internationale for France; identify the body for the
   relevant Member State]), the question asked, and the opinion
   received or the one-month deadline status.]

6. Data minimisation (Art. 32(4))
   [Identification of the minimum amount of data permissible in
   response. The provider's reasonable interpretation of the
   request's scope.]

7. Customer notification (Art. 32(5))
   [Confirmation that the customer has been informed before
   compliance, with copy of the notification or reasons for the
   law-enforcement carve-out.]

8. Compliance response
   [The data being provided, the format, the recipient, the
   transmission channel. The response references the Art. 32
   compliance posture and reserves rights to refuse further access
   beyond the order's terms.]
```

---

## Output skeleton: Path 3 (refusal on Art. 32(3) grounds)

Refusal letter to the third-country authority. Markdown. Lead with the legal ground; the addressee is foreign counsel.

```
To: [Third-country authority]
Date: [Date of response]
Subject: Response to [order reference] dated [order date]

The addressee is unable to comply with the order on the following
grounds.

1. The data requested is non-personal data held in the Union by a
   provider of data processing services within the meaning of
   Regulation (EU) 2023/2854 (Data Act) Art. 2(8).

2. No international agreement under Article 32(2) of the Data Act
   covers the order. [Brief statement of MLAT or other agreement
   review.]

3. Article 32(3) of the Data Act conditions compliance, in the
   absence of an international agreement, on three cumulative
   requirements: a reasoned and specific decision; review of the
   addressee's reasoned objection by a competent court; and the
   court being empowered to weigh Union legal interests of the
   provider. The addressee has determined that condition [(a) /
   (b) / (c) / multiple conditions] is/are not met because [specific
   structural feature of the third-country legal system].

4. [If applicable] The addressee has consulted the [relevant
   national body], which has issued an opinion concluding that the
   Article 32(3) conditions are not met. [Or: The addressee has
   sought such opinion and the one-month deadline has expired
   without reply.] On those grounds, the addressee rejects the
   request for transfer or access pursuant to Art. 32(3),
   sub-paragraph 2 of the Data Act.

5. [If applicable] The order also engages national-security or
   defence interests of [Member State / the Union], and the
   addressee has consulted [body] on that ground. Refusal on those
   grounds is independent of the Art. 32(3) conditions.

6. The customer whose data is the subject of the order has been
   informed of the existence of the order pursuant to Art. 32(5) of
   the Data Act. [Or: notification has been deferred pursuant to the
   law-enforcement carve-out, subject to review at [date].]

The addressee remains available to engage through the appropriate
international channels, in particular [MLAT route if any, or the
relevant cooperation framework].

[Signature block placeholder]
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 32(1) to (5) (always); Art. 1(2)(f), 1(3)(f), 1(5), 1(6) (scope and carve-outs); Art. 2(8) (data processing service); Art. 2(30) (customer); Art. 37 (competent authority); Art. 42 (EDIB).
- `sources/regulation-2023-2854.md` Recital 7 (mixed datasets); Recital 101 (Union law conflicts; trade secrets, IP, confidentiality); Recital 102 (Art. 32(1) preventive measures).
- `sources/faq-v1-4.md` Q60 (aim of Art. 32), Q61 (scope: not private-to-private), Q62 (Art. 32(1) measures), Q63 (national-body identification: Bundesjustizamt, Bureau de l'entraide pénale internationale). Frame all four as the Commission's interpretation.
- Directive (EU) 2016/943 (Trade Secrets Directive) where trade-secret-protected data is in scope; the gate file `references/gates/trade-secrets-directive.md` carries the framing.
- Regulation (EU) 2016/679 (GDPR) Chapter V (Arts. 44 to 50) for any personal-data portion. The Data Act analysis does not address this; route to GDPR Ch V counsel.
- `sources/digital-omnibus-amendments-tracker.md` (no Art. 32 amendment proposed; the adjacent Art. 4(8) and 5(11) third-country misuse-risk ground is not part of Art. 32).

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (load if any personal data in scope; Art. 32 is non-personal-data-only).
- `references/gates/trade-secrets-directive.md` (load if any trade-secret-protected data in scope).
- `references/gates/sectoral-lex-specialis.md` (warn-only; load if the customer's data is sector-regulated).
- `references/gates/member-state.md` (load to identify the relevant national body for international-cooperation consultation; FAQ Q63 covers Germany and France).
- `references/gotchas.md` entry 18 (Art. 32(3) three-condition conjunction; mandatory check). Also entry 19 (FAQ Q60 to Q63 framing as Commission interpretation) and entry 20 (Digital Omnibus status; Art. 32 not principally affected).
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `cross-gdpr-boundary.md` (for the personal-data vs non-personal-data split when the dataset is mixed).
- `cross-omnibus-impact.md` (for the proposal-status framing across the build).

---

## Drafter notes

Operational observations for using this card.

- **The three Art. 32(3) conditions assess the legal system, not the order.** The conditions are structural features of the third-country legal regime. A reasoned, specific, well-drafted individual order does not by itself satisfy the conditions if the third-country system as a whole does not provide for reasoned-objection review or for empowerment of the court to weigh Union interests. The analysis is system-level.
- **National-body consultation is a one-month-clock instrument.** The Art. 32(3) sub-paragraph 2 framework gives the addressee a structured deadline: the body answers within one month or refusal on the consulted grounds becomes available. Build the consultation into the response timeline from day one; the order's deadline will not pause for the consultation.
- **Customer notification is the most-likely-breached duty.** Providers facing time-critical orders frequently defer notification past what Art. 32(5) permits. The carve-out is narrow (law-enforcement effectiveness, for as long as necessary). Deferred notification needs documented justification and a fixed review date; indefinite non-notification is not lawful.
- **Personal data is the parallel track, not the same track.** Cloud customers asking about "Art. 32 protection" frequently mean "protection from the US CLOUD Act and similar regimes." Art. 32 covers the non-personal portion of their data; the personal portion is on the GDPR Ch V track. Both tracks must be run, and the answer may differ between them.
