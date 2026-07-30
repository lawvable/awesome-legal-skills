# Workflow: JOINT_CONTROLLER

The relationship is (or includes) joint control under Art. 26 GDPR. This workflow produces a Joint Controller Agreement (JCA) — not a DPA. The Art. 28 mandatory content does not apply; the Art. 26 mandatory content does.

This workflow is invoked when:
- The user explicitly asks for an "Art. 26 arrangement" / "joint controller agreement" / "JCA" / "gemeinsame Verantwortliche".
- The roles screen during another mode (REVIEW_*, DRAFT, REDLINE) reveals 3+ joint-control indicators per `references/art26-joint-controller.md`.

## Step 1 — Confirm joint control

Even if the user asked for a JCA explicitly, confirm with the screen test. Document the screen result in the output. JCAs are sometimes requested when the relationship is actually:
- Controller–processor (should use DPA / Art. 28).
- Two separate controllers exchanging data (should use a data-sharing agreement, not a JCA).
- A mix (multiple instruments needed).

Load `references/art26-joint-controller.md` and run the screen with the user's facts.

If the screen does NOT confirm joint control, **do not proceed**. Surface the misclassification and recommend the appropriate instrument:

| Result | Recommended instrument |
|---|---|
| 0–1 joint-control indicators | DPA under Art. 28 (switch to `draft.md` or `redline.md`) |
| 2 indicators with no shared purpose | Data-sharing agreement (separate controllers; not in scope of this skill) |
| 3+ joint-control indicators | Proceed with this workflow |
| Hybrid (some processing joint, some processor) | Multiple instruments needed — propose a JCA + DPA bundle |

## Step 2 — Intake

### Mandatory intake

| # | Field | Notes |
|---|---|---|
| J-I1 | Controller A — full legal name, registered seat, signatory | |
| J-I2 | Controller B — same | |
| J-I3 | Underlying business arrangement — what brings the parties together (joint venture, partnership, group HR services, co-marketing, etc.) | |
| J-I4 | Subject matter of the joint processing | What processing operation is jointly controlled? |
| J-I5 | Purpose(s) — for both parties | Joint controllers can have aligned but not necessarily identical purposes |
| J-I6 | Lawful basis — for each party | May differ (Art. 6) |
| J-I7 | Data categories | |
| J-I8 | Categories of data subjects | |
| J-I9 | Joint vs. separate processing — what processing is in scope of joint control vs. each party's separate processing | Critical to delineate |
| J-I10 | Data subjects' primary contact point | Either Controller A, Controller B, or both |
| J-I11 | Internal allocation preferences | Where each party is willing/able to take responsibility |
| J-I12 | Public summary distribution channel | Privacy notice, dedicated page, contractual disclosure to data subjects |
| J-I13 | Language | DE / EN / bilingual |
| J-I14 | Governing law and venue | |
| J-I15 | Coexisting relationships | Are there also Art. 28 (processor) or separate-controllership flows between the parties for other processing? If yes, separate instruments needed. |

### Conditional intake

| # | Field | When |
|---|---|---|
| J-C1 | Special-category data | Yes/no — affects security and DPIA allocation |
| J-C2 | International transfers from joint processing | If yes, transfer mechanisms must be jointly determined |
| J-C3 | Sub-processor / vendor relationships of either party | Each party engages its own processors; flag if shared |
| J-C4 | Existing JCA with same parties for related processing | Coordinate, don't duplicate |

## Step 3 — Allocation matrix

This is the central operational artefact. Walk through the matrix from `references/art26-joint-controller.md` and populate every cell:

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

**Empty cells are deferred decisions** — do not deliver a JCA with empty cells. If the user does not have a position on a cell, propose an allocation and flag for confirmation.

**Common allocation patterns**:
- Primary contact for data subjects: usually the party with the closer customer relationship (e.g. the party operating the user-facing platform).
- Information duties: party publishing the privacy notice typically takes lead; cross-reference and signposting to other party's notice.
- Breach notification to authority: party with the closer connection to the establishment for one-stop-shop purposes; or both if separate establishments.
- DPIA: usually joint, with the party initiating new processing taking the drafting lead.
- Security: each party for systems under its control; coordination requirement for joint infrastructure.

## Step 4 — Body of the JCA

Walk the JCA template (`templates/jca-{lang}.md`) and populate from intake.

### Mandatory sections

1. **Parties**.
2. **Recitals** — describe the underlying arrangement; cite Art. 26 GDPR.
3. **Definitions** — including: joint processing, joint controllers, separate processing (if relevant), data subjects, primary contact, public summary.
4. **Subject matter and scope** — define the joint processing precisely; explicitly delineate from any separate processing each party conducts.
5. **Purposes and lawful bases** — one paragraph per party.
6. **Allocation of responsibilities** — body text + reference to the matrix as Annex A.
7. **Data subjects' rights** — primary contact, routing, response timelines, mutual cooperation; Art. 26(3) acknowledgement (data subjects may exercise rights against either party).
8. **Information duties (Art. 13/14)** — who drafts, where the notice lives, change-management.
9. **Personal data breach** — mutual notification ("each party shall notify the other without undue delay and in any event within [X] hours of becoming aware of a Personal Data Breach affecting the joint processing"); allocation of Art. 33 / Art. 34 notifications; cooperation duty.
10. **Security (Art. 32)** — each party for its own systems; coordination on joint infrastructure or shared interfaces.
11. **DPIA / prior consultation** — initiation, drafting, consultation between the parties before changes that may trigger DPIA.
12. **Records of processing (Art. 30)** — each party maintains its own; data exchange to keep them consistent.
13. **International transfers** — joint approach; if the joint processing involves transfers, parties agree on mechanism.
14. **Sub-processors / vendors** — each party engages its own processors under separate Art. 28 contracts; mutual disclosure of vendors involved in joint processing.
15. **Liability between the parties** — internal allocation of costs of breaches, regulatory fines, data subject claims; **note that Art. 26(3) preserves joint and several liability towards data subjects irrespective of internal allocation**.
16. **Cooperation with supervisory authorities** — each party may have its own competent SA; cooperation if both are involved.
17. **Public summary** — text or reference to where the summary is published; obligation on each party to maintain accurate signposting in its privacy notice.
18. **Term, termination, post-termination** — if the joint processing ends, each party's obligations to the other for data hand-back, deletion, and ongoing data subject rights.
19. **Amendments and notices**.
20. **Governing law and venue**.

### Annexes

- **Annex A — Allocation Matrix** (the table from Step 3).
- **Annex B — Description of Joint Processing** (mirroring Art. 28 Annex 1 in level of detail; not because Art. 28 applies, but because the parties need a shared factual baseline).
- **Annex C — Public Summary** (the document or text to be made available to data subjects under Art. 26(2)).
- **Annex D — Sub-processors / Vendors of either party involved in joint processing** (informational; not a flow-down regime).

## Step 5 — Public summary

Art. 26(2) requires "the essence of the arrangement" to be made available to data subjects. The public summary is its own deliverable.

Drafting principles:
- Plain language; avoid Art. 26 / Art. 28 / GDPR jargon.
- Identify both parties by name with contact details.
- State what the joint processing is, in one paragraph.
- State the allocation of responsibilities at a high level (who handles requests, who notifies authorities, who provides information).
- State that data subjects may exercise rights against either party (Art. 26(3)).
- Provide contact information for data subject rights requests.
- Distribution: typically embedded in privacy notice as a dedicated section ("Joint Controllership with [Other Party]" / "Gemeinsame Verantwortlichkeit mit [Other Party]").

## Step 6 — Coexisting relationships

If the parties have other processing relationships (Art. 28 processing, separate controllership), produce a brief addendum to the JCA output:

- A list of the coexisting relationships.
- For each: which instrument should govern (DPA, data-sharing agreement, separate JCA).
- Recommendation on whether existing instruments need revision in light of the JCA.

## Step 7 — Output assembly

```markdown
# Joint Controller Arrangement (JCA) / Vereinbarung über die gemeinsame Verantwortlichkeit — Draft v1

## Roles analysis
[Why this is JC, not processor; screen test results; EDPB 07/2020 anchors.]

## JCA body
[Per Step 4 — populated]

---

## Annex A — Allocation Matrix
[Populated table]

## Annex B — Description of Joint Processing
[Populated]

## Annex C — Public Summary (Art. 26(2))
[Drafted summary]

## Annex D — Vendors involved
[List or "None at signing"]

---

## Drafting notes

### Open items
[List of items requiring user confirmation]

### Coexisting relationships requiring separate instruments
[List]

### Practitioner's note
[2–4 sentences on next steps: signature, public summary publication, internal communication, cross-functional alignment.]
```

## Quality gates before delivering

- [ ] Roles screen run and joint control confirmed (or correctly redirected).
- [ ] All J-I1–J-I15 mandatory intake items reflected.
- [ ] Allocation matrix has no empty cells.
- [ ] Public summary is plain-language, accurate, and distribution channel is identified.
- [ ] Art. 26(3) language present in body (joint and several towards data subjects).
- [ ] Coexisting relationships flagged where applicable.
- [ ] Body does not contain Art. 28(3)(a)–(h) clauses copied across (this is a JCA, not a DPA).
- [ ] Sub-processor flow-down language not present (each party engages its own processors separately).

## Anti-pattern guardrails

- **Do not paper a JC arrangement as a DPA.** Art. 28(3)(a)–(h) clauses in a JC context are nonsense — there is no controller giving instructions to a processor.
- **Do not omit the public summary.** Art. 26(2) makes it mandatory; a JCA without a public summary is incomplete.
- **Do not draft mutual indemnity for regulatory fines without acknowledging Art. 26(3).** External liability is joint-and-several towards data subjects; internal allocation is between the parties.
- **Do not collapse joint processing and separate processing into a single instrument.** Different legal characterisations require different documents.
- **Do not import audit-rights language from Art. 28(3)(h).** Joint controllers cooperate; they do not audit each other unilaterally.
