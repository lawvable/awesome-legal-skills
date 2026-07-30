# USA (DPF-certified) — TIA Country Profile

Last verified: 2026-05-31

Use this profile ONLY when the US importer is actively certified under the EU-US Data Privacy Framework (verify at dataprivacyframework.gov). For non-DPF US importers, use `us-non-dpf.md`.

## Adequacy Status

**Adequacy:** Yes — Implementing Decision (EU) 2023/1795 of 10 July 2023. Lightweight TIA only.

**Coverage limitations:**
- Only organisations subject to FTC or Department of Transportation jurisdiction
- Only organisations that have certified and are actively recertified annually
- Some sectors sit outside FTC/DoT jurisdiction and so cannot rely on the DPF (e.g. banks and many financial institutions subject to GLBA; common carriers under the Communications Act)

**Verification step:** Verify importer's current certification at dataprivacyframework.gov before relying on DPF. Status can change between annual recertifications.

## DPF Conditions and Requirements

Certified organisations must:
- Adhere to seven DPF principles (notice, choice, accountability for onward transfer, security, data integrity & purpose limitation, access, recourse & enforcement)
- Participate in an independent recourse mechanism
- Submit to FTC/DoT enforcement
- Re-certify annually

## Political Fragility (Critical Risk Factor)

The DPF rests on:
- Executive Order 14086 (signed October 2022) — establishes signals-intelligence safeguards
- The Data Protection Review Court — provides redress for EU data subjects

Both are executive-branch constructs. Risks:
- Future US administration could rescind EO 14086
- The DPRC could be defunded or restructured
- Schrems III challenge is a foreseeable possibility
- DPF status of an individual organisation can lapse (failure to recertify, FTC action)

**Realised degradations since the 2023 adequacy decision (as at 2026-05-31):** the risks above are no longer purely hypothetical. The PCLOB — part of the oversight architecture the adequacy decision relied on — lost its quorum in January 2025 (three members removed; reinstatement ordered then stayed on appeal, deferred pending the Supreme Court) and cannot start new oversight; and *Trump v. Slaughter* (US Supreme Court, argued 8 December 2025, ruling expected ~June 2026) may strip for-cause removal protection from FTC/PCLOB members. The EU General Court **dismissed** the Latombe challenge and upheld the DPF on 3 September 2025, but judged only the facts as they stood at the 2023 adequacy determination — it did not bless this later erosion (Latombe's CJEU appeal, filed 31 October 2025, is pending). These are the precise arguments a Schrems III challenge would run.

**Practical implication:** Do NOT rely on DPF as the sole basis for long-term transfers. Maintain SCCs (with TIA per `us-non-dpf.md`) as a fallback mechanism so transfers can continue if DPF status changes.

## Data Protection Framework (under DPF)

For DPF-certified organisations, the seven principles approximate EU data protection rights:
- **Notice** — clear privacy notice
- **Choice** — opt-out for disclosure and material new uses; opt-in for sensitive data
- **Accountability for onward transfer** — contracts/agreements with onward recipients
- **Security** — reasonable security measures
- **Data integrity and purpose limitation** — relevance and accuracy
- **Access** — data subject access right with limited exceptions
- **Recourse, enforcement, and liability** — independent recourse + FTC/DoT enforcement

## Surveillance & Government Access Laws

The same underlying US laws apply (Section 702 FISA, EO 12333, CLOUD Act). EO 14086 imposes new limits:
- Signals intelligence must be "necessary" and "proportionate" to validated intelligence priorities
- Bulk collection only when "necessary" for specific, defined purposes
- DPRC provides individual redress for qualifying complaints

**EU Commission's adequacy assessment:** Concluded these safeguards bring US protection to a level "essentially equivalent" to EU law.

**Critics' position:** EO can be rescinded; bulk collection still possible under defined purposes; DPRC effectiveness untested.

**Four essential guarantees (post-EO 14086 regime):**

- **Guarantee A — clear, precise, accessible rules:** *Concerns.* EO 14086 and its implementing procedures are published, but the underlying FISA 702 targeting/minimisation procedures and EO 12333 activities remain partly classified.
- **Guarantee B — necessary and proportionate:** *Concerns.* EO 14086 introduces binding necessity/proportionality limits, but bulk collection remains permitted for defined objectives; critics dispute whether this meets the CJEU's strict-necessity standard.
- **Guarantee C — independent oversight:** *Concerns, weakening.* The FISC and PCLOB provide oversight and the DPRC adds a redress layer, but all sit within or adjacent to the executive branch — and the PCLOB has lacked a quorum since January 2025 (reinstatement litigation stayed, deferred pending the Supreme Court), so its independent-oversight role is currently impaired.
- **Guarantee D — effective remedies:** *Contested.* The DPRC is available to EU data subjects (EU designated a qualifying state, 30 June 2023) but its independence and effectiveness as an Article 47 remedy are untested by the CJEU.

The EU Commission rated these "essentially equivalent"; this is the precise point a Schrems III challenge is expected to test.

## Practical Risk Factors

- Verify certification at dataprivacyframework.gov on the day of the assessment
- Subscribe to recertification status if relying long-term
- Monitor US political developments (rescission risk)
- Monitor Schrems III / Latombe litigation: the EU General Court dismissed Latombe and upheld the DPF on 3 September 2025 (judging only the 2023 adequacy facts); Latombe's CJEU appeal (filed 31 October 2025) is pending
- Monitor *Trump v. Slaughter* (US Supreme Court, ruling expected ~June 2026) and PCLOB quorum status — both bear on the DPF's independent-oversight foundations
- Document the fallback path (SCCs + TIA) in case DPF status changes

## Recommended Supplementary Measures

For DPF transfers, additional measures are NOT formally required, but consider:
- **TM-1** (encryption with exporter-held keys) — defence-in-depth against DPF lapse and the underlying surveillance laws (FISA 702, EO 12333, CLOUD Act continue to apply behind the DPF). **Effective only where the importer does not need plaintext to perform the service; where it must decrypt to process, encryption does not close the gap against compelled disclosure.**
- **Fallback documentation** — pre-execute SCCs as a standby mechanism

## TIA Output

For DPF transfers, the formal TIA document is light:
- Section 2: document DPF as primary mechanism, SCCs as fallback (recommended)
- Section 3: document DPF verification status, EO 14086 reliance, fragility risk
- Section 4: no measures required, but recommend TM-1 for defence-in-depth
- Section 6: monitor: annual recertification check, US political developments, Schrems III status

## Key Sources

- Implementing Decision (EU) 2023/1795 (DPF adequacy)
- Executive Order 14086 (October 2022)
- 28 CFR Part 201 (Data Protection Review Court rules)
- dataprivacyframework.gov (certification register)
- See `us-non-dpf.md` for the underlying surveillance law analysis
