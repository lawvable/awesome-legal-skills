# ch2-safety-security-handbrake

**Anchor:** Data holder × Ch II × Art. 4(2) safety/security handbrake. The data holder considers contractually restricting or prohibiting access, use, or further sharing of data on grounds that the processing could undermine security requirements of the connected product, resulting in a serious adverse effect on the health, safety, or security of natural persons. The handbrake is bilateral (negotiated with the user), not unilateral, and triggers notification to the competent authority under Art. 37.

**Routes from:**

- "Can we refuse data access because the data is safety-critical?"
- "We are worried that sharing this data with the user could undermine the product's security. What do the Data Act options look like?"
- "Draft an Art. 4(2) safety notification to the competent authority."
- "What are the limits on contractual restrictions on access to safety-relevant data?"
- "The user wants real-time sensor data from a medical device. We have CRA and MDR concerns."

**Adjacent cards (route there instead if the facts indicate):**

- The gravamen is trade-secret protection, not safety or security: `ch2-trade-secret-stages-1-2.md` and `ch2-trade-secret-stage-3-refusal.md`.
- The data holder is responding to an Art. 4(1) request without invoking the handbrake: `ch2-data-holder-response.md`.
- The user is challenging an Art. 4(2) restriction: the redress route runs under Art. 4(3) (complaint or dispute settlement); the user-side review card is implicit in the response on the user's request preparation (`ch2-user-direct-request.md`).

---

## Canonical fact pattern

A data holder controls readily available data from a connected product or related service. Some or all of that data, if accessed, used, or further shared on the Art. 4(1) standard, could undermine security requirements of the connected product as laid down in Union or national law, with a serious adverse effect on the health, safety, or security of natural persons. The data holder is considering an Art. 4(2) contractual restriction or prohibition rather than honouring the access request on the default Art. 4(1) standard.

The connected product is typically safety-critical: a medical device, a vehicle, industrial machinery, a building management system, an energy infrastructure component, an NIS2-covered entity's system, a Cyber Resilience Act covered product. The security requirements are typically sectoral, with the Data Act layered on top. The user is typically an enterprise; consumer-user scenarios also exist but are rarer in the safety-critical bracket.

---

## Critical disciplines

- **Three cumulative limbs, not a five-item checklist.** Art. 4(2) is often misread as an enumeration of independent safety considerations. The correct reading: a contractual restriction or prohibition is permitted where (i) the processing could undermine security requirements of the connected product, AND (ii) those security requirements are laid down in Union or national law, AND (iii) the consequence is a serious adverse effect on the health, safety, or security of natural persons. Missing any one limb defeats the handbrake. See `references/gotchas.md` entry 5.
- **The handbrake is bilateral.** Art. 4(2) authorises a contractual restriction or prohibition between the data holder and the user, not a unilateral refusal. Users may challenge under Art. 4(3) by complaint to the competent authority or by reference to a dispute settlement body. A data holder that imposes a restriction without engagement and without the contractual framing has overshot the article.
- **Not a trade-secret regime.** The Art. 4(2) handbrake protects health, safety, and security of natural persons through the connected product's security requirements. It is not a trade-secret handbrake. A data holder concerned about competitive harm or commercial sensitivity routes to Art. 4(6)-(8), not Art. 4(2). Misrouting between the two is the most common substantive error on the data-holder side.
- **Notification to the competent authority is constitutive on refusal.** Where the data holder refuses to share data pursuant to Art. 4(2), it must notify the competent authority designated pursuant to Art. 37. The notification is not merely advisory; it is part of the refusal. Contractual restrictions short of refusal also benefit from documentation but the notification duty under Art. 4(2) is specifically tied to refusal.
- **Sectoral authorities may provide technical expertise.** Art. 4(2) third sentence. In safety-critical sectors, the sectoral authority (e.g. medical device authority, motor vehicle type-approval authority, ENISA-coordinated NIS2 authorities) can supply the technical assessment. The data holder should engage the sectoral expertise where the regulatory baseline is genuinely sectoral.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check, Art. 1(6) carve-outs (national security may be relevant), and the Art. 2(22) placement test. Confirm the device is a "connected product" under Art. 2(5). For non-connected products with safety implications, the Data Act does not govern; the analysis runs sectorally.

### Step 2: Chapter identification

Chapter II. Art. 4(2) is the user-side safety/security handbrake. The parallel Art. 5(1) third-party route does not have a dedicated 4(2)-style handbrake (Art. 5(13) preserves data subject rights but does not replicate the safety handbrake structurally). Where the data holder is restricting on safety grounds against a third-party route, the analysis still anchors on Art. 4(2) for the underlying data-flow and on the Ch III conditions for the third-party leg.

### Step 3: Role mapping

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Data holder | Data holder (Art. 2(13)) | Controller, typically | Possibly covered entity under NIS2, manufacturer under CRA, manufacturer under MDR, or other sectoral status |
| Requesting user | User (Art. 2(12)) | Data subject if natural person; controller if enterprise (Recital 34) |  |
| Affected natural persons (the safety constituency) |  | Data subjects if their personal data is involved | The "natural persons" whose health, safety, or security the handbrake protects |
| Sectoral authority | Outside the Data Act roles | Outside | Source of technical expertise under Art. 4(2) third sentence |
| Competent authority under Art. 37 (Member State of establishment) | Outside | Outside | Recipient of the Art. 4(2) notification |

The "natural persons" limb is the safety constituency. They are not parties to the Data Act request but the regulation pivots on their interests. The data holder's response should name the affected category at a high level (e.g. patients fitted with the medical device, drivers and passengers of vehicles equipped with the system, workers operating the industrial machine).

### Step 4: Fact-category sorting

Card-specific dimensions to sort the requested data against.

- **Safety-critical data vs not.** Most requests will combine safety-critical and non-safety-critical data. The handbrake applies to the safety-critical portion; the non-safety-critical portion is disclosed on the Art. 4(1) standard.
- **Personal vs non-personal.** Drives the GDPR overlay independently. The safety constituency may be the data subject; their GDPR rights are preserved separately.
- **Connected product data vs related service data.** Both can carry safety implications.
- **Real-time vs historical.** Real-time access typically poses higher safety risk because it can be coupled to operational systems. Historical pulls are usually lower risk.
- **The security-requirement source.** Identify the specific Union or national law that lays down the security requirement: MDR, IVDR, vehicle type-approval (Regulation (EU) 2018/858 and delegated acts), Network and Information Systems Directive (NIS2), Cyber Resilience Act, sector-specific law. The handbrake's second limb fails if the requirement is internal company policy rather than law.

### Step 5: Limb-by-limb application of Art. 4(2)

Art. 4(2) cumulative limbs. Each independent; missing any one defeats the handbrake.

1. **The processing could undermine security requirements of the connected product.** "Processing" refers to the user's accessing, using, or further sharing of the data. "Could undermine" is a forward-looking risk assessment, not a certainty. "Security requirements of the connected product" focuses on the product's security, not the data holder's commercial security or trade-secret security. A request that does not engage the product's security (e.g. a request for historical billing data) does not engage Art. 4(2) even if the data holder views the data as sensitive.
2. **Those security requirements are laid down in Union or national law.** The requirement must have a statutory or regulatory source. Internal policies, industry guidelines without statutory backing, contractual obligations to component suppliers, do not satisfy this limb. Identify the specific source.
3. **The consequence is a serious adverse effect on the health, safety, or security of natural persons.** "Serious" is a substantive threshold; trivial or speculative effects do not meet it. "Health, safety, or security of natural persons" is the protected interest. Commercial harm to the data holder, business-continuity concerns, or reputational risk to the manufacturer do not engage this limb.

If all three limbs are satisfied, the data holder may contractually restrict or prohibit access, use, or further sharing. The restriction is contractual, meaning the data holder negotiates with the user; the article does not authorise an out-of-contract unilateral refusal.

Procedural obligations on the data holder:

- **Engage with the user.** Art. 4(2) presupposes bilateral negotiation. The data holder explains the safety analysis and proposes the restriction; the user has the right to challenge the analysis or propose alternative safeguards that would address the safety concern.
- **Notify the competent authority where the data holder refuses to share.** Art. 4(2) fourth sentence. Where the bilateral engagement results in refusal rather than a negotiated restriction, the data holder notifies the competent authority designated pursuant to Art. 37 of the Member State of establishment.
- **Engage sectoral expertise where relevant.** Art. 4(2) third sentence allows sectoral authorities to provide technical expertise.

### Step 6: Cross-regime gate check

- **Sectoral lex specialis (always loaded on this card).** Read `references/gates/sectoral-lex-specialis.md`. The card cannot be applied without identifying the sectoral law that grounds the second limb. Common sources:
  - Regulation (EU) 2017/745 (MDR) and Regulation (EU) 2017/746 (IVDR) for medical devices: post-market surveillance, cybersecurity provisions, MDCG 2019-16 guidance on cybersecurity.
  - Regulation (EU) 2018/858 and delegated acts for motor vehicle type approval; UNECE Regulations No. 155 (cybersecurity management system) and No. 156 (software update management system).
  - Directive (EU) 2022/2555 (NIS2) for cybersecurity of network and information systems in essential and important entities.
  - Regulation (EU) 2024/2847 (Cyber Resilience Act) for products with digital elements: cybersecurity essential requirements; vulnerability handling.
  - Regulation (EU) 2024/1689 (AI Act) for safety in high-risk AI systems.
  - Regulation (EU) 2022/2554 (DORA) for financial entities and their ICT third-party providers.
- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. The safety handbrake does not displace GDPR rights of the data subject. Where the data subject is the user (natural person), the data subject's Art. 15 GDPR right runs in parallel and is not affected by an Art. 4(2) restriction on the Data Act access right.
- **Trade Secrets Directive overlay (not applicable on this card).** If the data holder's concern is competitive harm, route to the trade-secret cards. The safety handbrake is a separate regime.
- **DMA gatekeeper (not applicable on this card).** Art. 5(3) does not interact with Art. 4(2).
- **Member State implementing law (warn-only).** Run `references/gates/member-state.md` to identify the competent authority for the Art. 4(2) notification.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 4(2) and Art. 4(3) of Regulation (EU) 2023/2854 (Data Act) govern. Verbatim text at `sources/regulation-2023-2854.md` Art. 4(2); operative recital at Recital 31 (last sentence preserves data subject rights against the handbrake) and Recital 29.
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final does not propose substantive amendments to Art. 4(2). The new proposed Art. 4(8) ground (third-country trade-secret misuse) is a parallel addition on a different regime; the safety handbrake is not amended. See `sources/digital-omnibus-amendments-tracker.md`.

---

## Decision point

After Steps 5 and 6, the analysis yields one of four paths.

1. **All three limbs satisfied, bilateral engagement produces an agreed restriction.** Document the restriction in the data-sharing contract or in a side letter. Disclose the non-safety-critical portion on the Art. 4(1) standard. Output Path 1A.
2. **All three limbs satisfied, bilateral engagement fails, data holder refuses to share.** Issue the refusal in writing to the user; notify the competent authority under Art. 37; signal the user's redress options. Output Path 1B.
3. **Limb 2 fails (no Union or national law grounding).** The handbrake does not apply. The data holder cannot invoke Art. 4(2). If the concern is genuinely safety-critical, route to internal review and consider whether sectoral law has been overlooked. If the concern is commercial or trade-secret, route to the trade-secret cards.
4. **Limb 3 fails (no serious adverse effect on health, safety, or security of natural persons).** The handbrake does not apply. The data holder cannot invoke Art. 4(2) for matters that do not engage the protected interest. Route to the trade-secret or sectoral analyses depending on the actual concern.

---

## Output skeleton: Path 1A (bilateral restriction agreed)

Side letter or contract amendment. Markdown by default. Length: typically one page.

Structure:

```
[Data holder letterhead placeholder]

To: [User]
Date: [Date of letter]
Subject: Article 4(2) safety and security restriction in
         relation to your Article 4(1) request dated
         [request date]

1. The request and context
   [Identification of the user's Art. 4(1) request. The
   identified safety-critical data within the requested
   scope.]

2. Article 4(2) analysis

   2(a) Security requirement engaged. [The connected product
        is subject to security requirements laid down in
        [specific Union or national law, e.g. Article [X] of
        Regulation (EU) 2017/745 (MDR) and MDCG 2019-16
        cybersecurity guidance; UNECE Regulation No. 155 as
        incorporated into Regulation (EU) 2018/858 type
        approval; Regulation (EU) 2024/2847 (CRA) Annex I
        Part 1].]

   2(b) Risk of undermining. [Specific factual scenario in
        which the user's access, use, or further sharing of
        the data could undermine those security requirements.
        Reference to sectoral expertise where engaged.]

   2(c) Serious adverse effect. [Specific factual scenario in
        which the undermining could result in a serious
        adverse effect on the health, safety, or security of
        [identified natural-person constituency, e.g. patients
        fitted with the device; vehicle drivers and
        passengers; workers operating the machinery].]

3. Agreed restriction
   [Specific contractual restriction on the user's access,
   use, or further sharing of the safety-critical data
   portion. Examples:
   - Access subject to read-only, non-real-time pull only;
     no API integration to operational systems.
   - Onward sharing prohibited absent the data holder's
     consent on a per-instance basis.
   - User to implement [specified technical and
     organisational measures] before any operational use of
     the data.
   The restriction is proportionate to the safety risk
   identified in section 2(c) and does not extend beyond
   what is necessary to address it.]

4. Non-restricted data
   [Identification of the non-safety-critical portion of
   the request, which is being disclosed on the Art. 4(1)
   standard by [channel] in [format].]

5. Redress
   [Information that the user may, under Art. 4(3), without
   prejudice to its right to seek redress before a court or
   tribunal of a Member State:
   (a) lodge a complaint with the competent authority of
       [Member State] under Art. 37(5)(b); or
   (b) agree with the data holder to refer the matter to a
       dispute settlement body under Art. 10.]

[Signature block placeholder]
```

## Output skeleton: Path 1B (refusal under Art. 4(2) with Art. 37 notification)

Two documents in parallel: the refusal letter to the user, and the notification to the competent authority. Markdown. Length: typically one to two pages combined.

Refusal letter to the user:

```
[Data holder letterhead placeholder]

To: [User]
Date: [Date of refusal]
Subject: Refusal to share data under Article 4(2) of
         Regulation (EU) 2023/2854 (Data Act) in response to
         your Article 4(1) request dated [request date]

1. The request and context
   [As Path 1A section 1.]

2. Article 4(2) analysis
   [As Path 1A section 2, with the additional finding that
   bilateral engagement to negotiate a restriction did not
   yield an arrangement that adequately addresses the
   safety risk identified in section 2(c).]

3. Engagement record
   [Brief factual account of the engagement: [dates,
   meetings, proposals exchanged]. Statement of why the
   proposed restrictions discussed did not adequately
   address the safety risk.]

4. Refusal
   [Statement that the data holder is refusing to share the
   identified safety-critical data on Art. 4(2) grounds.
   The non-safety-critical portion of the request is being
   disclosed on the Art. 4(1) standard.]

5. Notification to the competent authority
   [Statement that the data holder has, in parallel with
   this refusal, notified the competent authority of
   [Member State] designated pursuant to Art. 37.
   Notification reference number where available.]

6. Redress
   [As Path 1A section 5.]

[Signature block placeholder]
```

Notification to the competent authority:

```
[Data holder letterhead placeholder]

To: Competent authority of [Member State] designated
    pursuant to Article 37 of Regulation (EU) 2023/2854
    (Data Act)
Date: [Date of notification]
Subject: Notification under Article 4(2) of Regulation (EU)
         2023/2854 (Data Act): refusal to share data on
         safety and security grounds

1. Data holder identification
   [Legal name, address, Art. 37(10) Member State of
   establishment, contact person.]

2. The connected product or related service
   [Identification.]

3. The request refused
   [Identification of the user, date and scope of the
   request.]

4. Grounds for refusal
   [Concise statement of the Art. 4(2) three-limb analysis,
   with the specific Union or national law engaged and the
   safety constituency affected.]

5. Engagement record
   [Brief reference to the bilateral engagement.]

6. Sectoral expertise (where engaged)
   [Reference to any sectoral authority consulted under
   Art. 4(2) third sentence.]

[Signature block placeholder]
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 4(2), Art. 4(3) (always); Art. 37(5)(b), Art. 37(10), Art. 37(6)(c) (Commission annual reporting of refusals); Art. 38(1), Art. 10 (redress).
- `sources/regulation-2023-2854.md` Recital 29 (safety and security framing), Recital 31 last sentence (data subject GDPR rights preserved).
- `sources/faq-v1-4.md` Q25 (the "safety and security handbrake" framing), framed as Commission interpretation.
- The specific sectoral instrument identified in Step 4 (cited by full title and the operative provision laying down the security requirement).
- Where personal data is in scope, Regulation (EU) 2016/679 (GDPR) Art. 15 to confirm that the data subject's access right is unaffected by an Art. 4(2) restriction on the Data Act right.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/sectoral-lex-specialis.md` (always loaded on this card; identifies the security-requirement source).
- `references/gates/gdpr-overlay.md` (loaded if personal data in scope).
- `references/gates/member-state.md` (warn-only, for the competent authority of establishment).
- `references/gates/trade-secrets-directive.md` (not loaded on this card; if the concern is trade-secret, route to the dedicated cards).
- `references/gotchas.md` entries 5 (Art. 4(2) is not a five-item checklist), 4 ("without undue delay" has no numeric SLA, relevant if the engagement timing is challenged), 6 (do not conflate Art. 4(2) with the trade-secret ladder).
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `ch2-data-holder-response.md` (the default response card; routes here when safety is genuinely in play).
- `ch2-trade-secret-stages-1-2.md` and `ch2-trade-secret-stage-3-refusal.md` (alternative refusal regimes; do not confuse).
- `ch2-user-direct-request.md` (the user-side card; users challenging an Art. 4(2) restriction work from the redress route there).

---

## Drafter notes

- **Do not blend regimes in the same letter.** Art. 4(2) refusals and Art. 4(8) refusals are different in legal structure and in notification mechanics. A letter that purports to refuse on "safety and trade-secret grounds" is procedurally defective and signals that the data holder has not done the analysis. If both concerns are present, run them separately and produce two parallel responses (or restrict on safety and propose Art. 4(6) safeguards on trade-secret separately).
- **Sectoral expertise is a strength, not a weakness.** Engaging the sectoral authority under Art. 4(2) third sentence before issuing a refusal materially strengthens the data holder's posture if the competent authority later reviews the notification. The Art. 37 competent authority is rarely the sectoral authority; coordination is the data holder's job.
- **The bilateral character is not a formality.** Art. 4(2) presupposes that the data holder will discuss the safety analysis with the user. Skipping the engagement and going straight to refusal weakens the procedural standing of the refusal even where the substantive limbs are satisfied. Document the engagement in the refusal letter and in the Art. 37 notification.
