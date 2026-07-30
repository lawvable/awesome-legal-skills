# DMA gatekeeper gate

This gate covers the interaction between the Data Act and Regulation (EU) 2022/1925 (Digital Markets Act, DMA). The Data Act excludes DMA-designated gatekeepers from being eligible third-party recipients of data under Ch II. The exclusion is one of the few hard limits in the Data Act's third-party regime, and it has knock-on effects for downstream data-sharing arrangements.

The gate's job is to identify when a designated gatekeeper appears in a scenario, run the operative limbs of Art. 5(3) and Art. 6(2)(d), and modify the analysis accordingly.

---

## When the gate applies

The gate runs whenever any of the following is true:

- A scenario involves a user request to share data with a third party under Art. 5
- A scenario involves a third party receiving data under Art. 5 who may share data onwards
- A scenario involves an entity that is, or might be, a DMA-designated gatekeeper
- A scenario involves a large platform offering core platform services (search, social networking, video-sharing, messaging, operating systems, web browsers, online advertising, virtual assistants, cloud computing services, intermediation services), regardless of designation status

The gate also runs as a defensive check whenever the third-party identity is not specified in the scenario. The skill does not assume that the third party is not a gatekeeper; it verifies.

---

## What Art. 5(3) prohibits

Art. 5(3) excludes any DMA-designated gatekeeper from being an eligible third party under Art. 5. The exclusion has three operative limbs, all cumulative prohibitions on the gatekeeper itself.

**Limb (a).** A gatekeeper cannot "solicit or commercially incentivise a user in any manner, including by providing monetary or any other compensation, to make data available to one of its services that the user has obtained pursuant to a request under Article 4(1)." This prohibits the gatekeeper from approaching the user to obtain data the user already holds via direct access or via an Art. 4(1) data-holder request.

**Limb (b).** A gatekeeper cannot "solicit or commercially incentivise a user to request the data holder to make data available to one of its services pursuant to paragraph 1 of this Article." This prohibits the gatekeeper from inducing the user to fire off an Art. 5(1) request naming the gatekeeper as the third party. The intent is to prevent gatekeepers from using the Art. 5 channel as a back door for data acquisition.

**Limb (c).** A gatekeeper cannot "receive data from a user that the user has obtained pursuant to a request under Article 4(1)." This prohibits the gatekeeper from receiving Art. 4(1) data even where the user offers it without solicitation.

The three limbs together close the user-to-gatekeeper channel comprehensively. A user cannot lawfully share Art. 4(1) data with a gatekeeper, and a gatekeeper cannot lawfully accept it, regardless of who initiated the arrangement.

---

## What Art. 6(2)(d) prohibits

Art. 6(2)(d) closes the indirect channel. A third party who has received data under Art. 5 cannot "make the data it receives available to an undertaking designated as a gatekeeper pursuant to Article 3 of Regulation (EU) 2022/1925." A user cannot route data through a non-gatekeeper third party for onward delivery to a gatekeeper; the third party itself is prohibited from making the onward transfer.

The combined effect of Art. 5(3) and Art. 6(2)(d) is bidirectional and through-the-stack: data obtained under Art. 4(1) or Art. 5(1) cannot reach a gatekeeper through any path the Data Act creates.

---

## What the prohibition does not cover

Recital 40 sets the perimeter. The exclusion is targeted; it does not reduce gatekeepers to second-class commercial entities for all Data Act purposes.

- **Gatekeepers can provide data processing services that third parties use.** Recital 40 confirms: "this does not prevent third parties from using data processing services offered by a gatekeeper." A third party may use a gatekeeper's cloud infrastructure to process data the third party has received; the gatekeeper as cloud provider is in a different role and is not "receiving" the data within the meaning of Art. 5(3)(c) or Art. 6(2)(d).
- **Voluntary data sharing is not blocked.** Art. 5(3) excludes gatekeepers from the Art. 4/5 mandatory channel. Voluntary arrangements between gatekeepers and data holders or users, outside the Ch II right, are not within the exclusion. Recital 40: "voluntary agreements between gatekeepers and data holders remain unaffected."
- **Gatekeepers can lawfully obtain the same data through other means.** Recital 40: "Nor does it prevent those undertakings from obtaining and using the same data through other lawful means." If a user contracts directly with a gatekeeper to share data outside the Data Act framework, or if the data is publicly available, or if the gatekeeper acquires the data via a commercial dataset purchase, the Data Act does not block these channels.
- **Gatekeepers as customers of data processing services.** Art. 5(3) does not exclude gatekeepers from being customers of data processing services under Ch VI. A gatekeeper that buys cloud infrastructure from a non-gatekeeper provider has the same Ch VI rights as any other customer.

---

## Who is a gatekeeper

Designation is by Commission decision under Art. 3 of the DMA. The designation attaches to an undertaking with respect to specific core platform services (CPS). The same undertaking can be a designated gatekeeper for some of its services and not for others.

The Commission maintains a current list of designations on its DMA enforcement page. The skill checks the current list before applying the gate; designations can be added (new CPS, new entrants meeting thresholds) or removed (de-designation under Art. 4 DMA). The skill does not commit to a list of gatekeepers in this file, because the list changes; it commits to checking the list at runtime.

Practical implications for the gate:

- **Designation is at undertaking level for specific CPS.** When checking a counterparty, identify both the legal undertaking and the specific service being used. An undertaking may be designated as a gatekeeper for Service A but not for Service B; data flowing to Service B is not necessarily caught by Art. 5(3).
- **The DMA's "undertaking" concept includes the entire corporate group.** Designation of the parent extends to subsidiaries for the relevant CPS. The skill maps the counterparty to its ultimate undertaking before checking designation.
- **Designation status can change mid-contract.** Data-sharing arrangements concluded when a counterparty was not a gatekeeper may need to be revisited if the counterparty is subsequently designated. The skill flags this in any long-term data-sharing contract advice.

---

## How the gate runs

Operational steps when the skill processes a scenario involving any third party:

1. **Identify all parties that receive or might receive data.** This includes direct Art. 5 third parties, downstream recipients via Art. 6(2)(c) onward sharing, and service providers used by recipients for data processing.

2. **For each, determine whether the party is a DMA-designated gatekeeper.** Check the Commission's current designation list. Identify the specific core platform services that are designated. Map the data flow to the specific CPS to determine whether the gatekeeper's designated service is the actual recipient.

3. **If a gatekeeper is identified as a direct Art. 5 third party:** the request fails. Art. 5(3) excludes the gatekeeper. The skill advises that the user cannot designate this gatekeeper as the Art. 5 recipient.

4. **If a gatekeeper is identified as a downstream recipient via Art. 6(2)(c):** the onward sharing is blocked by Art. 6(2)(d). The third party must not transfer the data to the gatekeeper. The skill advises that the planned onward-sharing arrangement is unlawful under the Data Act and must be restructured.

5. **If a gatekeeper is identified as a data processing service provider used by a recipient (not as a data recipient itself):** the arrangement is permitted under Recital 40. The skill confirms this but flags the boundary: the gatekeeper must be processing on behalf of the recipient, not receiving data for its own account.

6. **If the counterparty's status is uncertain (newly emergent platform, recent designation pending):** the skill recommends a contractual representation and warranty from the counterparty that it is not a designated gatekeeper for the relevant CPS, plus a notification obligation if it is subsequently designated. This is a practical risk-allocation device, not a legal cure for an Art. 5(3) breach.

---

## Recipient attestation

For Ch II data-sharing arrangements, the data holder typically wants contractual assurance that the recipient is not a gatekeeper. A recipient attestation in the data-sharing contract is the standard mechanism. Minimum content:

- A representation that the recipient is not a designated gatekeeper under Art. 3 of the DMA for any core platform service relevant to the data-sharing arrangement.
- An undertaking to notify the data holder promptly if the recipient is designated, or if any service used to process the shared data is designated.
- An acknowledgement that the recipient will not, directly or via a sub-recipient, make the data available to any designated gatekeeper.
- A right for the data holder to terminate or suspend the data-sharing arrangement on the recipient's designation or breach of these representations.

The attestation does not displace the legal effect of Art. 5(3) or Art. 6(2)(d); it allocates risk and provides a contractual hook for enforcement.

---

## What the skill produces in the output

When the gate is run, the output must:

- State whether a designated gatekeeper appears in the scenario. If yes, identify the gatekeeper and the relevant CPS.
- Identify which limb of Art. 5(3) or Art. 6(2)(d) is engaged.
- State the legal consequence (the request or sharing arrangement is blocked, or is permitted under a Recital 40 carve-out, or requires restructuring).
- Recommend a contractual mechanism (attestation, notification, termination right) where the gate result depends on facts the user controls.
- Flag that designation status can change and recommend periodic re-checking for long-term arrangements.

The gate result appears in the role-mapping section of the output (the gatekeeper status is part of the third-party's role), not buried in the analysis.

---

## FAQ Q36

The Commission, in FAQ Q36, takes the view that the Art. 5(3) exclusion is justified on the ground that gatekeepers "typically have no difficulties in gaining access to large amounts of data" and "data already tend to gravitate towards these large undertakings due to their gateway position, control over platform ecosystems and superior bargaining power." The Commission emphasises that the exclusion is targeted at the Art. 4/5 mandatory channel and does not entirely exclude gatekeepers from IoT data markets: "DMA gatekeepers are prohibited from relying on the specific mandatory data sharing mechanisms created by Articles 4 and 5 of the Data Act but all other mechanisms (including regarding voluntary data sharing arrangements) remain unaffected."

The skill cites FAQ Q36 as Commission interpretation. The operative law is Art. 5(3) and Art. 6(2)(d).

---

## Cross-references

- `references/gotchas.md` entry 11 (Art. 5(3) tripartite reach) is the failure-mode catalogue version of this gate. The gate file gives the operational mechanics; the gotcha gives the trap to avoid.
- `references/gates/gdpr-overlay.md` runs in parallel for any personal data in the scenario. The gatekeeper exclusion under Art. 5(3) operates independently of GDPR; a personal-data flow to a gatekeeper would need to fail both the DMA gatekeeper gate and the GDPR overlay.
- `sources/regulation-2023-2854.md` Art. 5(3), Art. 6(2)(d), Recital 40.
- `sources/faq-v1-4.md` FAQ Q36.
- Regulation (EU) 2022/1925 (DMA) Art. 3 (gatekeeper designation), Art. 4 (de-designation), Art. 2 (definitions of core platform services).
