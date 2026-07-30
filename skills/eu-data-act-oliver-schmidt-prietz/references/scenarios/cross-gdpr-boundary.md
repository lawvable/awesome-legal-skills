# cross-gdpr-boundary

**Anchor:** Any × cross-chapter × GDPR-Data Act boundary. The card operationalises the Art. 1(5) bridge clause, walks the Case A (user-as-data-subject) and Case B (user-not-data-subject) bifurcation, and resolves the three recurring questions practitioners face: when GDPR prevails over the Data Act; when the Data Act adds obligations on top of GDPR; when the two regimes overlap on the same fact pattern without conflict. Loads `references/gates/gdpr-overlay.md` in full.

**Routes from:**

- "Does GDPR or the Data Act govern this request?"
- "Can we use the Data Act as our legal basis under Art. 6 GDPR?"
- "Our user is an enterprise and the data is personal data of employees. What's our legal basis?"
- "The data subject's Art. 15 GDPR request overlaps with a Data Act access request. Which do we run?"
- "Mixed dataset (personal + non-personal). Which regime applies to which part?"
- "Where does ePrivacy fit in for connected-product data?"

**Adjacent cards (route there instead if the facts indicate):**

- The question is entirely a GDPR question with no Data Act dimension: route out of the skill to GDPR specialist counsel.
- The personal-data question is specifically third-country transfer of personal data under GDPR Chapter V (e.g. CLOUD Act response): route to `ch7-third-country-request.md` for the non-personal-data portion and to GDPR Ch V counsel for the personal portion. The boundary card explains why the two tracks run separately.
- The question is a sector-specific overlay (employment data, health data, financial data) where sectoral law adds obligations: run the boundary card for the horizontal analysis, then run `references/gates/sectoral-lex-specialis.md`.

---

## Canonical fact pattern

A Data Act matter (user access under Art. 4; third-party sharing under Art. 5; cloud switching under Ch VI; third-country governmental access under Ch VII; or a Ch IV unfair-terms review) involves personal data. The personal data may be of the user (Case A) or of a natural person who is not the user (Case B). The dataset may be all personal, all non-personal, or mixed (Recital 7 inextricably linked).

The organisation needs to know: which regime governs each operation; what legal basis the data holder has for the disclosure; what data subject rights remain available; what additional obligations the Data Act imposes on top of GDPR; and what additional obligations GDPR imposes that the Data Act does not displace.

---

## Critical disciplines

Three points trip up almost every GDPR-Data Act boundary analysis.

- **The Data Act is never a GDPR legal basis.** Art. 1(5) is a "without prejudice" clause, not a legal-basis grant. Recital 7 confirms: "This Regulation does not constitute a legal basis for the collection or generation of personal data by the data holder." A data holder cannot rely on the Data Act access right under Art. 4(1) or 5(1) as the Art. 6(1) GDPR basis for processing or disclosure. The basis must come from elsewhere. See `references/gates/gdpr-overlay.md`.
- **Art. 1(5) conflict rule: GDPR prevails.** "In the event of a conflict between this Regulation and Union law on the protection of personal data or privacy, or national legislation adopted in accordance with such Union law, the relevant Union or national law on the protection of personal data or privacy shall prevail." Where the Data Act would require disclosure and GDPR forbids it (no valid legal basis, no Art. 9 condition, no transfer mechanism for third-country transfer), GDPR governs the outcome. The Data Act access right is conditional on GDPR compliance.
- **Case A vs Case B is the decisive bifurcation.** A user-as-data-subject scenario (Case A) is a complementarity scenario: Data Act extends GDPR data subject rights. A user-not-data-subject scenario (Case B) is a legal-basis scenario: the user becomes a controller under Recital 34, and the data holder needs a valid Art. 6(1) basis for the disclosure under Art. 4(12) or 5(7). The two cases produce different analyses, different deliverables, and different risk profiles. See `references/gotchas.md` entry 3.

---

## The seven-step walk

### Step 1: Scope check

Confirm the Data Act applies to the underlying matter (Art. 1(2), (3), (6)). Confirm GDPR applies (Art. 2 and 3 GDPR; in particular Art. 3(2) GDPR for non-EU-established controllers offering goods or services to data subjects in the Union or monitoring their behaviour). The two scopes are independent. Most Data Act matters touching personal data are within both scopes; rare cases (e.g. a Data Act matter on non-personal data only) sit within Data Act scope and outside GDPR. The boundary card runs only where GDPR scope also applies.

If terminal equipment is in scope (most connected products qualify per Recital 36 Data Act), the ePrivacy Directive Art. 5(3) is also engaged, on top of GDPR. Three regimes (Data Act, GDPR, ePrivacy) interact in the typical connected-product scenario.

### Step 2: Chapter identification

The boundary applies whichever Data Act chapter is engaged. Common combinations:

- **Ch II + GDPR.** User access (Case A or Case B) and third-party sharing (Art. 5 + Art. 6(2)(b) profiling restriction, which is narrower than Art. 22 GDPR in some respects and adds an explicit prohibition).
- **Ch III + GDPR.** Mandatory B2B sharing under other Union law (e.g. sectoral data-sharing acts) often involves personal data. The "without prejudice" rule means GDPR controls the personal portion.
- **Ch IV + GDPR.** Unfair B2B contractual terms can include personal-data processing terms. Art. 13 unfairness control runs alongside Arts. 26 / 28 GDPR.
- **Ch V + GDPR.** Public-sector exceptional need is principally for non-personal data (Art. 1(2)(d) "with a focus on non-personal data"). Where personal data is in scope, GDPR governs the disclosure to the public sector body.
- **Ch VI + GDPR.** Cloud switching involves customer personal data. GDPR's controller-processor regime under Art. 28 GDPR runs alongside Ch VI obligations.
- **Ch VII + GDPR.** Third-country governmental access. Art. 32 Data Act covers non-personal data only; GDPR Chapter V covers personal data. The two tracks run separately (see `ch7-third-country-request.md`).

### Step 3: Role mapping

Required entity-by-entity mapping, with both Data Act and GDPR roles per phase.

| Entity | Data Act role | GDPR role | Other | Case A or Case B |
|--------|---------------|-----------|-------|-------------------|
| Natural-person consumer using their own connected product | User (Art. 2(12)) | Data subject | | Case A |
| Enterprise (fleet operator, employer, hospital) using connected products with personal data of natural persons not the user | User (Art. 2(12)) | Controller (Recital 34) for the data the user requests under Art. 4(1) or 5(1) | | Case B |
| Manufacturer / data holder | Data holder (Art. 2(13)) | Controller, typically, for its own product-improvement and related-service processing | Possible trade-secret holder | Both cases |
| Driver / employee / patient (natural person whose data is generated by the use of the connected product) | (None directly; the user role belongs to the enterprise) | Data subject | | Case B (the data subject is not the user) |
| Joint controllership candidate (manufacturer + user enterprise) | | Joint controllers under Art. 26 GDPR where they jointly determine purposes and means | | Case B |

Joint controllership is a fact-driven test. Recital 34 Data Act flags it; the CJEU's Wirtschaftsakademie (C-210/16), Jehovah's Witnesses (C-25/17), and Fashion ID (C-40/17) lines apply. Where joint controllership exists, an Art. 26 GDPR arrangement is required.

### Step 4: Fact-category sorting

Dimensions that matter for the boundary analysis.

- **Personal vs non-personal data.** Drives whether GDPR applies at all. Mixed datasets (Recital 7 Data Act; the personal and non-personal parts inextricably linked) trigger GDPR for the personal portion regardless of the Data Act analysis. Anonymisation removes the GDPR overlay for the anonymised portion (Recital 26 GDPR), but pseudonymisation does not.
- **Special category data under Art. 9 GDPR.** Health data from connected medical devices; biometric data from authentication-enabled wearables; political-opinion data from media-consumption habits. An Art. 9(2) condition is required in addition to the Art. 6 legal basis. Recital 35 Data Act explicitly preserves the Art. 9 / Art. 5(3) GDPR conditions: "in accordance with Regulation (EU) 2016/679, a contract does not allow for the processing of special categories of personal data by the data holder or the third party."
- **Terminal equipment access.** Most connected products are terminal equipment (Recital 36 Data Act). ePrivacy Art. 5(3) consent applies to storing information in, or accessing information from, terminal equipment, unless strictly necessary for the user-requested service. Two layers of authorisation typically required: ePrivacy for the on-device access; GDPR Art. 6 (or 9) for the subsequent personal-data processing.
- **Provided-by-the-data-subject (Art. 20 GDPR limitation) vs observed.** Art. 20 GDPR portability is limited to data the data subject has provided to the controller. Data Act Art. 5 is broader: it covers all readily available product and related-service data regardless of whether actively provided or passively observed (Recital 35 Data Act). Where the data is observed, Data Act portability is available but Art. 20 GDPR is not.
- **Legal basis of underlying processing.** Art. 20 GDPR portability is limited to processing on Art. 6(1)(a) (consent) or 6(1)(b) (contract). Data Act portability applies regardless of legal basis. A data subject can port telematics data under Data Act Art. 5 even where the underlying processing is on Art. 6(1)(f) legitimate interests.

### Step 5: Limb-by-limb application of Art. 1(5)

Art. 1(5) Data Act has three operative limbs.

#### Limb 1: without prejudice

"This Regulation is without prejudice to Union and national law on the protection of personal data, privacy and confidentiality of communications and integrity of terminal equipment, which shall apply to personal data processed in connection with the rights and obligations laid down herein, in particular Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive 2002/58/EC, including the powers and competences of supervisory authorities and the rights of data subjects."

GDPR, EUDPR (for EU institutions), and ePrivacy apply in full to any personal-data processing in the context of Data Act activities. The Data Act does not displace, narrow, or modify these regimes. Supervisory authority powers (Arts. 51 et seq. GDPR) and data subject rights (Arts. 12 to 22 GDPR) are unaffected.

#### Limb 2: complementarity for Ch II rights

"Insofar as users are data subjects, the rights laid down in Chapter II of this Regulation shall complement the rights of access by data subjects and rights to data portability under Articles 15 and 20 of Regulation (EU) 2016/679."

For a Case A user (data subject), Ch II Data Act rights are additive to Arts. 15 and 20 GDPR. The user has GDPR rights for personal data plus Data Act rights for all readily available product and related-service data (personal, non-personal, or mixed; provided or observed; on any legal basis). FAQ Q18 makes the complementarity explicit.

#### Limb 3: conflict rule

"In the event of a conflict between this Regulation and Union law on the protection of personal data or privacy, or national legislation adopted in accordance with such Union law, the relevant Union or national law on the protection of personal data or privacy shall prevail."

The Data Act access right does not override GDPR constraints. Where disclosure under the Data Act would breach GDPR, the disclosure does not happen on the personal-data portion. FAQ Q1 confirms. The data holder may still need to disclose the non-personal portion of a mixed dataset under the Data Act, with the personal portion anonymised or withheld.

### Step 6: Case A vs Case B

The structural test that determines the legal-basis question.

#### Case A: user is the data subject

The user is a natural person and the personal data in scope relates to them. The user requests access to their own data under Art. 4(1) (or directs disclosure to a third party under Art. 5(1)).

Legal-basis question: straightforward. The data holder discloses personal data to the data subject on whichever Art. 6(1) basis it was relying on for the underlying processing (typically Art. 6(1)(b) contract or 6(1)(f) legitimate interests). The Data Act access right does not require a new legal basis; it is a statutory channel through which the data subject exercises GDPR rights enhanced by Data Act extensions.

Data Act adds, on top of GDPR Art. 15 / 20:

- Real-time portability where technically feasible (Art. 5(1) Data Act; Art. 20 GDPR's "where technically feasible" standard is not the cap).
- All readily available data, not just provided-by-the-data-subject data (Art. 5 Data Act; Recital 35).
- Regardless of legal basis (Art. 5 Data Act applies even where underlying processing is on Art. 6(1)(c), (d), (e), or (f); Art. 20 GDPR is limited to (a) and (b)).
- Engineered technical feasibility (Art. 3(1) Data Act design obligation; not optional, unlike Art. 20 GDPR).

Conflict rule rarely engages in Case A. The data subject is requesting their own data; GDPR does not forbid that disclosure.

#### Case B: user is not the data subject

The user is an enterprise (employer, fleet operator, hospital, rental company, sole trader) and the personal data in scope is of a natural person who is not the user (employee, driver, patient, renter, customer).

Recital 34 Data Act: "Where the user is not the data subject but an enterprise, including a sole trader, and not in cases of shared household use of the connected product, the user is considered to be a controller." The user becomes a controller for the data it requests.

Art. 4(12) Data Act conditions the data holder's disclosure to a Case B user: "any personal data generated by the use of a connected product or related service shall be made available by the data holder to the user only where there is a valid legal basis for processing under Article 6 of Regulation (EU) 2016/679 and, where relevant, the conditions of Article 9 of that Regulation and of Article 5(3) of Directive 2002/58/EC are fulfilled."

Art. 5(7) Data Act applies the same rule to disclosure to a third party.

Legal-basis question: the candidates are:

- **Art. 6(1)(a) consent.** Workable for consumer-facing flows; impractical in employment or other power-imbalance contexts. EDPB Guidelines 05/2020 on consent.
- **Art. 6(1)(b) contract.** Available where the data subject is a party to the contract (e.g. car-sharing user agreement). Not available where the data subject is the employee of the user.
- **Art. 6(1)(c) legal obligation.** Recital 7 Data Act explicitly rejects the Data Act itself as a legal obligation for non-data-subject access. Other Union or national law obligations may apply (sectoral disclosure duties, employment law).
- **Art. 6(1)(f) legitimate interests.** The most commonly relied-on basis; requires a documented LIA balancing the user's and data holder's interests against the data subject's reasonable expectations and rights. The data holder runs the LIA; the user (as the new controller) runs its own LIA for its subsequent processing.

Where consent is unavailable and Art. 6(1)(b) is not engaged, anonymisation is the cleanest practical alternative. The Commission, in FAQ Q25a, takes the view that "the controller could explore whether providing the data is necessary for the performance of the contract with the data subject or service legitimate interest of data holder or a third party" and that anonymised disclosure is a valid alternative. Anonymisation removes the data from GDPR scope (Recital 26 GDPR) and resolves the legal-basis question.

The gap that practitioners regularly miss: Case B exposes scenarios where the user's purpose specifically requires personal data (accident investigation, performance monitoring, billing reconciliation) and anonymisation defeats the purpose. In those scenarios, if no Art. 6 basis can be established, the Data Act access right cannot be exercised for the personal-data portion. See `references/gates/gdpr-overlay.md` "Case B" section.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 1(5) Data Act bridge clause; Arts. 4(12) and 5(7) Data Act legal-basis conditions; Recitals 7, 34, 35, 36 Data Act; Art. 6 and 9 GDPR; Art. 5(3) ePrivacy. Verbatim text at `sources/regulation-2023-2854.md`.
- **Proposed amendment under Digital Omnibus.** The Digital Omnibus (COM(2025) 833 final, 19 November 2025) proposes amendments to both GDPR and ePrivacy in addition to Data Act amendments. The Data Act-side amendments (Arts. 4(8), 5(11), 15, 25, 31) do not directly affect the boundary mechanics under Art. 1(5). The GDPR-side amendments in the Omnibus (legitimate-interest framing for AI training; cookie-consent simplification; ePrivacy modernisation) may shift the Art. 6(1)(f) calibration but do not affect the Art. 1(5) bridge structure. Status: co-legislator negotiation, not adopted. See `sources/digital-omnibus-amendments-tracker.md` and `cross-omnibus-impact.md`.

The output cites current law as operative. The proposal-side adjustments are awareness only.

---

## Decision point

After Steps 5 and 6, the boundary analysis yields one of four outcomes for any specific operation.

1. **Data Act applies; GDPR also applies; no conflict; complementarity (Case A).** The data subject has both regimes available. Identify which is more advantageous for the matter (Data Act typically broader for portability; GDPR equivalent for access; GDPR exclusive for rectification, erasure, restriction).
2. **Data Act applies; GDPR also applies; Case B legal basis available.** The data holder establishes an Art. 6 basis (and Art. 9 condition where applicable, and Art. 5(3) ePrivacy where terminal-equipment access). The disclosure proceeds. The user is the new controller for its subsequent processing and runs its own GDPR analysis.
3. **Data Act applies; GDPR also applies; Case B legal basis unavailable; anonymisation defeats the purpose.** The Data Act access right cannot be exercised for the personal-data portion. The non-personal portion may still be disclosed. The output explains the gap explicitly.
4. **Data Act applies; GDPR also applies; conflict; GDPR prevails (Art. 1(5) limb 3).** The Data Act access right is overridden for the personal-data portion. The non-personal portion may still be disclosed.

For mixed datasets, the analysis runs for each portion. The output presents the personal-data analysis and the non-personal-data analysis side by side; the same dataset may yield different outcomes for its two halves.

---

## Output skeleton: GDPR-Data Act boundary memorandum

Markdown memorandum. Length depends on the matter; typically 2 to 5 pages. The deliverable is internal-facing and assumes the reader is a DPO, GC, or product counsel.

```
# GDPR-Data Act boundary: [matter] as of [Date]

## Lead conclusion
[The boundary outcome in one sentence. Example: "The data holder
may disclose the non-personal portion of the requested telematics
data to the user on the Data Act Art. 5 path; the personal portion
requires anonymisation before disclosure because no valid Art. 6
GDPR legal basis is available for the enterprise user (Case B) and
the data subjects (drivers) have not consented."]

## Scope and chapters engaged
- Data Act chapters: [list]
- GDPR provisions: [list]
- ePrivacy: [engaged / not engaged]

## Role mapping
[Table per Step 3 above. Show Case A / Case B label per entity.]

## Data classification
[Table: personal vs non-personal; special category vs ordinary;
terminal-equipment access vs not; provided vs observed; legal basis
of underlying processing.]

## The Art. 1(5) bridge
- Limb 1 (without prejudice): [how the limb applies on these facts].
- Limb 2 (complementarity): [Case A complementarity findings; or
  "not engaged" if Case B].
- Limb 3 (conflict rule): [whether GDPR prevails; on which point].

## Case A or Case B analysis

### [Case A subsection]
- Data subject's GDPR Art. 15 / 20 rights: [available].
- Data Act Ch II extensions: [list extensions that apply to the
  matter].
- Recommended disclosure path: [Art. 4(1) Data Act / Art. 5(1) Data
  Act / Art. 15 GDPR / Art. 20 GDPR / combination].

### [Case B subsection]
- The user is a controller under Recital 34 Data Act.
- Art. 4(12) / 5(7) Data Act condition: valid Art. 6 GDPR legal
  basis required.
- Legal-basis assessment:
  - Art. 6(1)(a) consent: [available / not available; reason].
  - Art. 6(1)(b) contract: [available / not available; reason].
  - Art. 6(1)(c) legal obligation: [available / not available; the
    Data Act itself is not a legal obligation per Recital 7].
  - Art. 6(1)(f) legitimate interests: [available / not available;
    LIA outline if relevant].
- Art. 9 GDPR conditions (if special category data): [the operative
  condition].
- Art. 5(3) ePrivacy (if terminal-equipment access): [consent or
  strictly necessary].
- Anonymisation route: [available / defeats purpose; reason].

## Joint controllership
[Whether the data holder and the user are joint controllers under
Art. 26 GDPR. If so, draft an Art. 26 arrangement (referenced
separately).]

## Supervisory authority competence
- DPA competent for the personal-data aspects (Art. 37(3) Data
  Act).
- Data Act competent authority (Art. 37(1) Data Act).
- For mixed matters, both authorities may engage; complaints may be
  lodged with either.
- Note: DPAs may impose Art. 83(5) GDPR fines for Data Act Chapter
  II, III, V infringements within their competence (Art. 40(4) Data
  Act).

## Outcome
[One of the four decision-point outcomes above, applied to the
matter.]

## Watch-list
- Digital Omnibus: [any Omnibus item that may shift the analysis,
  with status note.]
- Forthcoming guidelines: [EDPB Art. 9 / legitimate-interest
  guidance; EDIB Art. 32(3) guidance; Commission Art. 9(5)
  compensation guidance.]
```

---

## Sample phrasing

The skill may use phrasing of this kind in deliverables.

For Case A:

> The user is the data subject for the personal data in scope (Case A). Art. 1(5) of the Data Act complements the data subject's GDPR rights with the Ch II access right. The data holder may disclose to the user on the basis of Art. 6(1)(b) GDPR (contract performance), which is the same basis on which the data holder is processing the data for the related service. The Ch II right adds real-time portability and removes the Art. 20 GDPR provided-by-the-data-subject limitation.

For Case B:

> The user is an enterprise (fleet operator); the data subjects are the drivers of the vehicles. Recital 34 of the Data Act characterises the user as a controller for the requested personal data. Art. 4(12) of the Data Act conditions the data holder's disclosure on a valid GDPR legal basis. Consent (Art. 6(1)(a) GDPR) is not workable in the employment context. Art. 6(1)(b) GDPR is not available because the data subjects are not parties to the contract between the data holder and the user. Art. 6(1)(f) GDPR legitimate interests is the candidate basis, supported by a documented LIA balancing the user's interest in fleet management against the drivers' reasonable expectations and privacy rights. The data holder should also consider whether anonymisation of the telematics data meets the user's purpose; if it does, anonymised disclosure removes the data from GDPR scope and resolves the legal-basis question.

For a conflict-rule outcome:

> The Data Act Art. 4(1) access right does not override Art. 9 GDPR. The connected medical device's health-data outputs are special category data under Art. 9(1) GDPR. Disclosure to the enterprise user (Case B) requires an Art. 9(2) condition in addition to the Art. 6 legal basis. The available Art. 9(2) condition on these facts is [(a) explicit consent / (h) preventive or occupational medicine / (i) public health], depending on the user's processing purpose. Where no Art. 9(2) condition applies, the Data Act Art. 1(5) limb 3 conflict rule means GDPR prevails: the data is not disclosed.

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 1(5) (always); Arts. 4(12) and 5(7) (Case B legal-basis condition); Art. 5(8) (data subject rights not impeded); Art. 5(13) (data subject rights preserved on third-party route); Art. 6(2)(b) (third-party profiling restriction); Art. 37(3) (DPA competence); Art. 40(4) (DPA fining powers under Art. 83(5) GDPR); Recital 7 (mixed datasets and no GDPR legal basis); Recital 34 (Case B as controller); Recital 35 (Art. 20 GDPR complementarity and Art. 9 reservation); Recital 36 (ePrivacy and terminal equipment).
- `sources/faq-v1-4.md` Q1 (general interaction), Q2 (DPA competence), Q18 (data portability complementarity), Q25 (safety-security handbrake reference), Q25a (Case B legal-basis assessment and anonymisation), Q25b (controller-to-controller information sharing), Q30 (user verification and personal data), Q33 (no Data Act right to erasure of non-personal data). Frame each as Commission interpretation.
- Regulation (EU) 2016/679 (GDPR) Arts. 4(11), 6, 7, 9, 12 to 22, 26, 28, 32, 51 to 58, 83.
- Directive 2002/58/EC (ePrivacy) Art. 5(3).
- EDPB Guidelines 05/2020 on consent; Guidelines 07/2020 on controllers and processors; EDPB Opinion 22/2018 on the future of consent in the ePrivacy Regulation (relevant where the proposed ePrivacy Regulation is mentioned).

Never paraphrase GDPR or the Data Act from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (the operational mechanics of the boundary; this card's seven-step walk uses the gate's framing).
- `references/gates/sectoral-lex-specialis.md` (load where sectoral law adds further constraints on the personal-data portion: employment law for employee monitoring; MDR for medical-device data; DORA for financial-services data).
- `references/gotchas.md` entry 3 (user-not-data-subject becomes controller; the operative trap for Case B). Also entries 19 (FAQ framing) and 20 (Digital Omnibus status).
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `ch7-third-country-request.md` (for the split between Data Act Art. 32 non-personal-data path and GDPR Chapter V personal-data path).
- `cross-gap-analysis.md` (for the consolidated multi-chapter posture; boundary findings appear in the gap-analysis output under the GDPR-overlay heading per chapter).
- `cross-omnibus-impact.md` (for the proposal-side framing across the build).

---

## Drafter notes

Operational observations for using this card.

- **The "Data Act as legal basis" misconception is the most common error.** Practitioners and product teams routinely propose to use the Data Act access right itself as the Art. 6(1) GDPR basis for disclosure to a Case B user. The deliverable must close this off explicitly. Recital 7 is the operative citation; Art. 4(12) and 5(7) are the operative conditions.
- **Anonymisation is operationally underrated.** Where the user's purpose is statistical, aggregate, or trend-analysis, anonymisation defeats the legal-basis problem and removes the data from GDPR scope. The deliverable should ask the user what they need the data for before assuming personal-data disclosure is required. Where the user can articulate a purpose for which anonymised data suffices, the boundary analysis ends.
- **Joint controllership is plausible more often than practitioners assume.** Fleet operators that specify telematics collection parameters jointly with manufacturers; hospitals that specify medical-device data collection jointly with manufacturers; employers that specify connected-workstation telemetry jointly with vendors. The deliverable flags joint controllership wherever the facts support it; the drafting consequence is an Art. 26 GDPR arrangement.
- **DPA fining powers are high-consequence.** Art. 40(4) Data Act gives the DPA competence to fine under Art. 83(5) GDPR (the higher band: EUR 20 million or 4% of global annual turnover) for Data Act Chapter II, III, V infringements touching personal data. Boundary-related compliance failures (no legal basis; conflict with GDPR; absence of Art. 26 arrangement where joint controllership exists) sit in this fining band. The boundary analysis is not a low-risk exercise.
