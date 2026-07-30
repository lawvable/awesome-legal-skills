# Member State implementing law gate

This gate is warn-only. The Data Act is a Regulation and is directly applicable across the Union, but several provisions delegate procedural or institutional decisions to Member State law. The skill recognises when a scenario depends on Member State implementation, identifies the relevant Member State, points to the Commission's public register where applicable, and recommends local counsel for procedural matters.

The gate does not produce Member State-specific analysis. Doing so would require current knowledge of every Member State's implementing law and competent authority designation, which the skill does not have. Member State implementation status changes regularly, and the public register is the source of truth. The gate's job is to detect the dependency, flag it, and redirect.

---

## When the gate applies

The gate runs whenever the scenario depends on any of the following:

- Identification of the competent authority responsible for application and enforcement of the Data Act
- Identification of the data coordinator
- Filing or response to a complaint under Art. 38
- Dispute settlement under Art. 10
- Penalty determination under Art. 40
- Identification of the legal representative of a non-EU entity under Art. 37(11)
- Procedural questions about cross-border requests under Art. 22 or Art. 37(15)-(16)
- Determination of the main establishment of an entity established in more than one Member State (Art. 37(10))
- Member State-specific rules on the production of official statistics under Art. 15(3) and Art. 20(4)
- Member State implementation law that may govern aspects not directly regulated by the Data Act

---

## What the Data Act delegates to Member State law

The Data Act delegates specific institutional and procedural decisions to Member State law. The main delegations:

**Competent authority designation (Art. 37(1)).** Each Member State must designate one or more competent authorities responsible for the application and enforcement of the Data Act. The Data Act does not specify which national body should be designated. Member States may designate existing authorities (data protection authority, telecommunications regulator, competition authority, sectoral regulator) or create new ones. The Commission maintains a public register under Art. 37(7).

**Data coordinator designation (Art. 37(2)).** Where a Member State designates more than one competent authority, it must designate a data coordinator from among them. The data coordinator is the single point of contact, facilitates cooperation, and handles certain specific tasks listed in Art. 37(6). Member States with a single competent authority do not designate a separate data coordinator; the competent authority assumes the tasks.

**Dispute settlement body certification (Art. 10(5)).** Member States certify dispute settlement bodies on the body's request, against criteria laid down in Art. 10(5). The Data Act does not require Member States to establish dispute settlement bodies; it provides the certification framework if and when bodies seek certification. Member States are free to adopt specific certification procedure rules, including expiry and revocation. The Commission maintains a public list under Art. 10(6).

**Penalty regime (Art. 40).** Member States lay down rules on penalties and take measures necessary to ensure implementation. Penalties must be effective, proportionate, and dissuasive. Member States were to notify the Commission of these rules by 12 September 2025; Art. 40(2) requires ongoing notification of amendments. For infringements of Chapters II, III, and V, DPAs may impose administrative fines under Art. 83 GDPR up to the amount in Art. 83(5) GDPR. The Commission maintains a public register of national penalty regimes.

**Legal representative designation (Art. 37(11)).** Non-EU entities falling within the scope of the Data Act must designate a legal representative in one of the Member States. The Member State of the representative determines the competent authority for the non-EU entity (Art. 37(13)).

**Complaint forum (Art. 38(1)).** Natural and legal persons lodge complaints with the competent authority in the Member State of their habitual residence, place of work, or establishment. This is a Member State-of-the-complainant rule, not a Member State-of-the-respondent rule.

**Main establishment rule (Art. 37(10)).** Entities established in more than one Member State are under the competence of the Member State of main establishment, defined as the head office or registered office from which the principal financial functions and operational control are exercised. This is a fact-based test, not a self-declared rule.

**Subsidiary universal competence (Art. 37(13)).** Until a non-EU entity designates a legal representative, it is under the competence of all Member States. Any competent authority may exercise its competence, including by imposing penalties, provided that the entity is not already subject to enforcement proceedings under the Data Act regarding the same facts by another competent authority. The ne bis in idem principle applies (Recital 109).

**National statistics rule (Art. 15(3), Art. 20(4)).** Member States may notify the Commission that national law does not allow national statistical institutes or other national authorities responsible for the production of statistics to compensate data holders. In such cases, the Art. 20(2) compensation entitlement does not apply for Ch V data requested for the production of official statistics. The Member State's national law is the determinant.

---

## How the skill runs the gate

Operational steps:

1. **Identify the relevant Member State.** Depending on the scenario, this may be the Member State of the data holder's establishment, the user's habitual residence, the public sector body's location, the data processing service provider's main establishment, the complainant's location, or several of these. The skill states which Member State is relevant and why.

2. **Identify the procedural decision that depends on Member State implementation.** Examples: which competent authority handles the complaint; whether the Member State has designated a dispute settlement body; what penalty range applies; whether the Member State has notified the Commission that national statistics law precludes compensation.

3. **Point to the public register.** Where the Commission maintains a public register (competent authorities under Art. 37(7), dispute settlement bodies under Art. 10(6), penalty regimes under Art. 40(2)), the skill directs the user to the register as the source of truth.

4. **Flag uncertainty in implementation status.** Where the Member State's implementation is recent, partial, or not yet notified, the skill flags this. As of the skill's source date, implementation across Member States is uneven. Some Member States designated competent authorities by 12 September 2025; others have proceeded more slowly. The skill does not assume implementation is complete.

5. **Recommend local counsel for procedural matters.** Member State procedural rules (complaint form, time limits, appeal routes, evidence rules, penalty calculation) are not addressed by the Data Act. The skill recommends local counsel for any matter that reaches a procedural decision.

---

## What the skill does not do

- **Identify the current competent authority for a specific Member State.** This changes; the Commission's register is the source of truth.
- **Calculate national penalties for a specific Member State.** Penalty ranges vary; local counsel computes the exposure.
- **Predict the outcome of a complaint or dispute settlement.** Member State procedural and substantive practice varies; the skill does not predict national tribunal behaviour.
- **Apply Member State-specific procedural rules** (time limits for appeal, evidence rules, language of proceedings). These are local counsel matters.
- **Opine on Member State implementing law beyond the Data Act framework.** Some Member States have adopted broader national data regulation that interacts with the Data Act; the skill does not analyse this.

---

## Cross-border cooperation

Several provisions govern cross-border cooperation between competent authorities:

- **Art. 22.** Mutual assistance and cross-border cooperation for Ch V requests. A public sector body intending to request data from a data holder established in another Member State must first notify the competent authority in the data holder's Member State. The competent authority of the data holder's Member State examines the request and may transmit it to the data holder or reject it on substantiated grounds.
- **Art. 37(15)-(16).** Cooperation between competent authorities on assistance and enforcement measures. Reasoned requests; obligation to respond detailing action taken; principles of confidentiality and professional secrecy.
- **Art. 38(3).** Cooperation between competent authorities to handle complaints effectively and in a timely manner, including by exchanging information by electronic means. Without prejudice to cooperation mechanisms under the GDPR and the CPC Regulation.

The skill flags cross-border dimensions in any scenario where parties are in different Member States. The cooperation mechanisms are mandatory but procedural; the skill does not predict how cooperation will be exercised in any specific case.

---

## Member State implementation status (as of source date)

The skill's source date is 2026-05-15. As of that date, Member State implementation of the Data Act is uneven. The Commission's public register under Art. 37(7) is the authoritative source for current designation status. The skill does not maintain a parallel list because such a list would be stale by the time the skill runs.

What the skill knows generally:

- Most Member States have designated at least a provisional competent authority. The specific national body varies (data protection authority, telecommunications regulator, competition authority, ministry-level body).
- Penalty regimes have been notified by some Member States and not others.
- Dispute settlement body certification is at an early stage in most Member States. Few certifications have been notified to the Commission.
- DPAs are universally responsible for the personal-data aspects of Data Act enforcement (Art. 37(3)).

If a scenario depends on the current status of a specific Member State, the skill directs the user to the Commission register and to local counsel.

---

## Germany-specific note

Germany has designated its competent authority through the **Data Act-Durchführungsgesetz (DA-DG)** — the *Gesetz zur Durchführung der Verordnung (EU) 2023/2854*. The DA-DG is **in force since 30 May 2026** — adopted by the Bundestag on 26 March 2026 (Referentenentwurf 7 February 2025; Kabinettsbeschluss 29 October 2025), cleared by the Bundesrat without objection on 8 May 2026 (1065th session), promulgated in the Bundesgesetzblatt on 29 May 2026, and in force the following day. The German designation is therefore **settled law, not pending**: the skill states BNetzA's competence as operative and points to the Commission's Art. 37(7) register and German counsel only for procedural specifics and any later amendments.

What the DA-DG provides:

- **Bundesnetzagentur (BNetzA) — central competent authority (§ 2 DA-DG; Art. 37(1) Data Act).** The DA-DG designates BNetzA as the single competent authority "für alle Angelegenheiten der Durchführung der VO 2023/2854". It handles complaints (Art. 38), reports refusals of data-access requests to the Commission, certifies dispute-settlement bodies (Art. 10), and promotes data-sharing with research institutions. This supersedes the earlier position in this file that BNetzA (or the Bundeskartellamt) was merely a *plausible* candidate — the DA-DG centralises competence in BNetzA, so there is no longer a multi-candidate question for the general designation.
- **Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)** and the **Landesdatenschutzbeauftragte**. Competent for the personal-data aspects of Data Act enforcement under Art. 37(3), alongside GDPR enforcement. The DA-DG does not displace DPA competence for personal data.
- **Penalty regime (Art. 40 Data Act).** The DA-DG provides administrative fines of up to **€500,000** for general infringements and up to **4 % of the annual turnover generated in the Union** for undertakings that are DMA gatekeepers (Reg. (EU) 2022/1925). For infringements touching personal data, the Art. 83 GDPR ranges apply (see "Penalty regime (Art. 40)" above). The figures are as enacted in the DA-DG; for a live matter, confirm them against the published text (Bundesgesetzblatt, 29 May 2026).
- **Sectoral authorities** (BaFin, Kraftfahrt-Bundesamt, BfArM) remain relevant for sector-specific Data Act matters where lex specialis applies, and the **Bundeskartellamt** for the competition / DMA-gatekeeper interface — but none of these is the Data Act competent authority, which is BNetzA.

Even with the DA-DG, the gate keeps its warn-only posture for procedural questions (complaint forms, time limits, appeal routes, penalty calculation): these are German procedural-law and counsel matters, not horizontal Data Act analysis.

---

## What the skill produces in the output

When the gate is run, the output includes a "Member State procedural matters" section or paragraph. Minimum content:

- The relevant Member State(s) for the matter.
- The Data Act provisions that delegate to Member State law (e.g. Art. 37, Art. 38, Art. 40).
- A statement that the procedural answer depends on Member State implementation, which is not addressed by the horizontal Data Act analysis.
- A clear redirection: consult the Commission's public register (where available) and local counsel for procedural matters.

Sample phrasing the skill may use:

> Member State procedural matters: the procedural [or enforcement, or complaint] aspect of this matter depends on [Member State name]'s implementing law and competent authority designation, which the Data Act delegates under Art. [37 / 38 / 40]. The current competent authority designation should be confirmed against the Commission's public register at [URL or reference]. Local [Member State] counsel should be consulted for procedural rules including [time limits / appeal routes / penalty calculation].

The phrasing is calibrated. The skill does not say "the German competent authority is X" unless it has actively confirmed the current designation. The skill does not invent procedural rules.

---

## Cross-references

- `references/gotchas.md` does not currently have a Member State-specific entry. The skill checks Member State implementation through this gate.
- `sources/regulation-2023-2854.md` Art. 10 (dispute settlement), Art. 22 (mutual assistance for Ch V), Art. 37 (competent authorities and data coordinators), Art. 38 (complaints), Art. 40 (penalties), Recitals 107, 109.
- `sources/faq-v1-4.md` FAQ Q63 (national bodies for international cooperation, illustrative Bundesjustizamt for Germany and Bureau de l'entraide pénale internationale for France), Q67-Q70 (enforcement, complaints, Commission role, penalty harmonisation), Q71 (legal representative).
- Commission public register of competent authorities (to be confirmed at https://digital-strategy.ec.europa.eu and equivalent pages; the register URL may change).
- Member State implementing legislation: only Germany's Data Act-Durchführungsgesetz (DA-DG) is summarised, in the Germany-specific note above. For all other Member States this is not maintained in the skill; consult local counsel and the Commission register.
