# Art. 49 Derogations — Balanced Assessment Path

Sources:
- GDPR Article 49 — Derogations for specific situations
- EDPB Guidelines 2/2018 on derogations of Article 49 under Regulation 2016/679 (adopted 25 May 2018)
- OLG München, Hinweisbeschluss of 11.05.2026 — 21 U 3882/25 e (Art. 49(1)(b) for global services)
- Reported remarks of Judge Thomas von Danwitz (CJEU rapporteur, Schrems II) on the underuse of Art. 49

This file presents BOTH the EDPB's restrictive position AND the emerging judicial counter-position. The skill lets the practitioner make an informed risk-appetite choice; it does not pre-decide.

---

## Why a Balanced Treatment

The EDPB has consistently read Art. 49 narrowly, framing the derogations as "exceptions of last resort" unsuitable for systematic or repetitive transfers. This is guidance, not statute.

A growing line of judicial and academic commentary takes a broader view. Most notably, OLG München (21 U 3882/25 e, 11.05.2026) accepted Art. 49(1)(b) as a legitimate basis for routine US transfers by a global social media platform, reasoning that the contract is inherently international and the transfer is necessary to perform it. Reported remarks of Judge von Danwitz (the Schrems II rapporteur) have indicated that Art. 49 may cover more transfer scenarios than the EDPB acknowledges — Schrems II was, in his view, "overrated" insofar as it ignored the breadth of Art. 49.

The skill surfaces both positions. The practitioner chooses.

---

## Per-Derogation Assessment

### Art. 49(1)(a) — Explicit consent

**Statutory text (paraphrased):** Transfer is permissible where the data subject has explicitly consented after being informed of the possible risks of such transfers for the data subject due to the absence of an adequacy decision and appropriate safeguards.

**Conditions:**
- Explicit (not just unambiguous) consent
- Specific to the transfer in question
- Freely given (no detriment for refusal)
- Informed — must include the specific risks of the destination country

**EDPB position:** Cannot be relied on for systematic / repetitive transfers (Guidelines 2/2018, para 23).

**Broader view:** For user-initiated services where the user explicitly opts into a transfer (e.g., enabling a feature that necessarily involves a third-country provider), Art. 49(1)(a) has been treated more accommodatingly in practice.

**Documentation requirements (either view):**
- Consent capture mechanism with timestamps
- Risk disclosure text shown to the data subject
- Withdrawal mechanism (Art. 7(3))

### Art. 49(1)(b) — Contract performance

**Statutory text (paraphrased):** Transfer is necessary for the performance of a contract between the data subject and the controller or the implementation of pre-contractual measures taken at the data subject's request.

**Conditions:**
- Contract is between data subject and controller (not between controller and a third party)
- Transfer is *necessary* for performance (not merely convenient)

**EDPB position:** "Necessary" means strictly necessary; not suitable for systematic transfers; the transfer itself must be necessary, not just the contract.

**Broader view (OLG München 21 U 3882/25 e):** For globally operating services where the contract is inherently international (e.g., a social media platform where EU and US users must be able to interact), routine data transfers ARE necessary for contract performance. Technical blockades between continents would be incompatible with the service architecture.

**Documentation requirements (either view):**
- Identify the contract and contractual obligations
- Explain why the transfer is necessary for those obligations (not just convenient)
- For systematic transfers under the broader view: document the inherently international nature of the service and the architectural reasons why localisation is not feasible

### Art. 49(1)(c) — Contract in the interest of the data subject

**Statutory text (paraphrased):** Transfer is necessary for the conclusion or performance of a contract concluded in the interest of the data subject between the controller and another natural or legal person.

**Conditions:**
- Contract between controller and third party (not data subject)
- Concluded in the data subject's interest
- Transfer necessary for that contract

**EDPB position:** Narrow — must genuinely be in the data subject's interest, not just incidentally beneficial.

**Use cases:** Insurance contracts where a third-country counterparty is needed; travel bookings on behalf of the data subject.

### Art. 49(1)(d) — Important reasons of public interest

**Statutory text (paraphrased):** Transfer is necessary for important reasons of public interest.

**Conditions:**
- "Important reasons" must be recognised in Union or Member State law (Recital 112)
- Cannot be self-assessed — must have legal grounding

**EDPB position:** Public interest must be of an entity, not commercial. Limited applicability.

**Use cases:** Disease outbreak response, law enforcement cooperation under international treaties, anti-money-laundering data sharing.

### Art. 49(1)(e) — Legal claims

**Statutory text (paraphrased):** Transfer is necessary for the establishment, exercise or defence of legal claims.

**Conditions:**
- Specific legal proceeding or claim (existing or reasonably anticipated)
- Transfer necessary for those proceedings (e.g., discovery, evidence)

**EDPB position:** Case-by-case; not for blanket / standing arrangements.

**Use cases:** US discovery, cross-border litigation, regulatory investigations.

### Art. 49(1)(f) — Vital interests

**Statutory text (paraphrased):** Transfer is necessary to protect the vital interests of the data subject or other persons where the data subject is physically or legally incapable of giving consent.

**Conditions:**
- Vital interests = life-or-death or serious injury
- Data subject incapable of consenting (unconscious, minor without guardian present, etc.)

**Use cases:** Emergency medical care abroad.

### Art. 49(1) second subparagraph — Compelling legitimate interest

**Statutory text (paraphrased):** Where transfer cannot rely on any of (a)–(f) and not on Art. 46/47, transfer may take place if it is:
- Not repetitive
- Concerns only a limited number of data subjects
- Necessary for compelling legitimate interests pursued by the controller, which are not overridden by the data subject's interests / rights / freedoms
- Suitable safeguards assessed and documented
- SA informed of the transfer

**EDPB position:** Genuine last resort. Documentation burden is heavy. SA notification required.

**Use cases:** Truly exceptional one-off transfers where no other basis is available.

---

## How the Skill Routes Art. 49

After Step 2 (Identify the Transfer Tool), the skill asks: "Could any Art. 49 derogation apply as a primary or alternative basis for this transfer?"

If the user proceeds with Art. 49:
1. The skill identifies which derogation(s) apply.
2. Presents both the EDPB position and (where relevant) the broader view.
3. Requires the user to document the justification thoroughly.
4. Does NOT require a full Step 3–4 country-law deep dive (Art. 49 doesn't require a TIA).
5. Surfaces the risk: SA enforcement will apply the EDPB position; courts may apply a broader reading. The user chooses their risk appetite.

If the user uses Art. 49 as a *backup* to Art. 46 (belt and braces): the skill documents both bases. This is increasingly common practice — primary reliance on SCCs + TIA, with Art. 49(1)(b) noted as a fallback in case the primary mechanism is challenged.

---

## Documentation Template

For any Art. 49 reliance, the TIA output must capture:

| Field | Content |
|---|---|
| Derogation | Which Art. 49 sub-provision |
| Primary or fallback | Primary basis OR fallback alongside Art. 46 |
| Justification | Why this derogation applies on the facts |
| EDPB view considered | Yes/no — and how addressed |
| Broader view considered | Yes/no — citing OLG München / academic sources where applicable |
| Documentation evidence | Consent records / contract / SA notification / etc. |
| Risk acknowledgement | The practitioner accepts the residual risk of SA challenge |

---

## Final Note

The skill does not push the practitioner toward Art. 49. It presents Art. 49 as one legitimate option among the Chapter V mechanisms, with the EDPB position and the judicial counter-position laid out honestly. The user decides.
