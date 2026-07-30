# Annex III Area 1 — Biometrics

**Annex III citation:** Nr. 1
**Effective date:** 2 December 2027 (per AI Omnibus)
**Source:** Commission Guidelines Annex III, Area 1 section. Full text: the Commission Draft Guidelines on Art. 6 classification (2026), Annex III section.

## Scope of the area

Point 1 of Annex III covers three biometrics-related use cases that the legislator has classified as high-risk because of their intrinsic intrusiveness on fundamental rights and their reliance on biometric data: (a) remote biometric identification (RBI) systems; (b) biometric categorisation according to sensitive or protected attributes; and (c) emotion recognition systems. Each use case applies only "in so far as such use is permitted under relevant Union or national law" — high-risk classification does not legalise an otherwise unlawful use (Commission Guidelines ¶119–¶121).

All three sub-categories depend on the definition of "biometric data" in Art. 3(34) AI Act: personal data resulting from specific technical processing relating to physical, physiological or behavioural characteristics of a natural person (e.g. facial images, fingerprints, gait, voice, keystroke rhythm, iris, DNA, EEG, ECG). The AI Act's definition is intentionally broader than the GDPR/LED/EUDPR definition — it omits the "which allow or confirm the unique identification" qualifier, so it covers biometric data used for identification, categorisation, emotion recognition or other purposes (¶122, ¶125). Data extracted from deceased persons or human remains is not biometric data within the Annex III Nr. 1 use case (¶123).

The Art. 5 vs Art. 6 boundary is decisive in this area. Some biometric uses are outright **prohibited** under Art. 5(1)(f), (g), (h); others — including systems falling under an Art. 5 exception or outside the prohibition's narrow scope — are **high-risk** under Annex III Nr. 1. A system that meets all conditions of an Art. 5 prohibition is not classified under Annex III at all because it cannot be placed on the market or put into service (¶126). Conversely, most systems that escape the Art. 5 prohibitions will fall under Annex III Nr. 1 and be high-risk under Art. 6(2), unless an Art. 6(3) exception applies.

## Sub-categories

- **Nr. 1(a) Remote biometric identification (RBI)** — AI systems for biometric identification of natural persons without their active involvement, typically at a distance, by comparing biometric data against a reference database. Three cumulative conditions: (i) purpose is biometric identification, (ii) no active involvement (remoteness), (iii) comparison against a reference database (Commission Guidelines ¶127–¶144).
- **Nr. 1(b) Biometric categorisation** — AI systems assigning natural persons to specific categories on the basis of their biometric data, where the categorisation is by sensitive or protected attributes (Art. 9(1) GDPR) inferred from the biometric data, and which are not prohibited under Art. 5(1)(g) (¶165–¶170).
- **Nr. 1(c) Emotion recognition** — AI systems identifying or inferring emotions or intentions of natural persons on the basis of their biometric data; concept is interpreted broadly and includes attitudes; excludes physical states (e.g. pain, fatigue) and mere detection of expressions/gestures not used to infer emotions (¶171–¶177).

## Practical examples — HIGH-RISK

- Facial/voice recognition for media archives — identifying individuals in audiovisual content by comparing against a media archive reference database without active involvement (Nr. 1(a), ¶144).
- Voiceprint matching against a database of known speakers without their active involvement (Nr. 1(a), ¶144).
- Post-incident stadium CCTV facial recognition: comparing captured facial images against a biometric database to identify offenders after an incident (Nr. 1(a), ¶144).
- CSAM-related RBI: comparing facial images and tattoos extracted from child sexual abuse material against a national/international suspect database (Nr. 1(a), ¶144).
- Reverse-image internet search to locate a terrorist living undercover, using biometric templates from publicly available material (Nr. 1(a), ¶144).
- Gait-based tracking via CCTV: comparing a fugitive's stored gait profile against transport-hub CCTV feeds to track them after first detection (Nr. 1(a), ¶135).
- Keystroke biometrics for fraud investigation: matching a person's distinctive typing rhythm against previously captured keystroke templates (Nr. 1(a), ¶141).
- Patient categorisation by gait: capturing gait, inferring health data (Art. 9(1) GDPR sensitive attribute), and classifying patients into disease-stage categories (Nr. 1(b), ¶170).
- Airport passenger categorisation by inferred ethnic origin from facial templates and gait, used to build aggregate passenger profiles (Nr. 1(b), ¶170).
- AI-enhanced police body-cams flagging "aggressive posture" via gait, body posture and facial analysis to infer anger or impending violence (Nr. 1(c), ¶177).
- Gaming-industry system measuring player excitement, anger, frustration, amusement via facial expressions, eye gaze and posture (Nr. 1(c), ¶177).
- Concert-venue crowd-mood monitoring: ceiling cameras analysing voices, faces and movements to detect aggression in specific areas (Nr. 1(c), ¶177).
- Call-centre emotion recognition: analysing customer voice (tone, pitch, volume) to gauge satisfaction or anger and route to a human agent (Nr. 1(c), ¶177).
- Smart-watch mood monitor inferring user emotions (sad, curious, happy, bored) from voice and heart-rate biometrics (Nr. 1(c), ¶177).

## Practical examples — NOT HIGH-RISK

- Object/clothing tracking without biometrics — following a person identified only by a red scarf or blue jacket; ANPR-based vehicle tracking; supermarket basket detection; transport-ticket validation tracking (no biometric data, ¶124, ¶134).
- Biometric verification (one-to-one): unlocking a smartphone; ABC-gate face-to-passport-chip comparison; online banking login authentication; remote proctoring; roadside fingerprint-to-ID-card check (¶136, ¶138).
- Direct access control by face recognition at a stadium entrance, smart-home entry system, or "smart corridor" registered-attendee access: persons consciously present themselves, so remoteness condition fails (¶140, ¶144).
- Crime-scene screening systems analysing footage from the scene itself (closed dataset) without matching persons against external biometric databases — pre-initial-identification work-step (¶144, ¶152).
- Cross-border age/gender estimation: AI inferring age and gender at border crossings — not sensitive Art. 9(1) GDPR attributes, so outside Nr. 1(b) (¶170; may fall under Annex III Nr. 7 if used for risk assessment).
- Age-estimation tools to gate access to age-restricted services or content (vending machines, betting platforms, harmful online content) — age is not a sensitive Art. 9(1) GDPR attribute (¶170).
- Driver-drowsiness detection via posture, eye closure and gaze — fatigue is a physical state explicitly excluded from emotion recognition (¶177).
- Content moderation scanning text/images for inappropriate content — not based on biometric data (¶170).
- Infrared/thermal human-presence detection (train seat occupancy, track trespasser detection, drone search for missing persons in forests) — not biometric data and not for identification (¶144).
- Mere observation of readily apparent expressions — counting how often a news presenter smiles is not emotion recognition (¶177).

## Boundary with Art. 5 prohibitions

- **Art. 5(1)(f)** — emotion recognition in workplace and education institutions, except where used for medical or safety reasons. Emotion-recognition systems outside workplace/education, and those inside workplace/education used for medical or safety reasons, escape the prohibition and become **high-risk under Nr. 1(c)** (¶126).
- **Art. 5(1)(g)** — biometric categorisation that individually classifies natural persons by inferring race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation. Categorisation by other Art. 9(1) GDPR sensitive attributes (e.g. **ethnic origin, genetic data, health data**) is **not prohibited** and becomes **high-risk under Nr. 1(b)** (¶169).
- **Art. 5(1)(h)** — real-time RBI in publicly accessible spaces for law-enforcement purposes, subject to three narrow exceptions (targeted search of victims of specific serious crimes/missing persons; prevention of imminent threats to life/physical safety or terrorist attacks; localisation/identification of suspects of Annex II offences). RBI systems falling under one of these exceptions, plus all **post-RBI** and all **non-law-enforcement RBI**, are **high-risk under Nr. 1(a)** (¶126, ¶144).

Systems that fall into the Art. 5 prohibitions are NOT high-risk — they are prohibited (placing on the market, putting into service, and use are all forbidden). Systems falling into Art. 5 exceptions or outside the prohibition's narrow scope become high-risk under Annex III Nr. 1.

## Common Art. 6(3) exception scenarios

The Art. 6(3) exception (system does not pose a significant risk of harm because it falls into one of the four limbs: narrow procedural task, improve a previously completed human activity, detect deviation from prior decision patterns, or preparatory task) is **almost always unavailable in Area 1** due to the profiling re-exception in Art. 6(3) final subparagraph: an Annex III system that performs profiling of natural persons is always high-risk regardless of the four limbs.

- **Nr. 1(a) RBI** — Identification of a specific individual via biometric comparison against a reference database is inherently profiling: it singles out a natural person and produces personal data attached to that individual. The exception is structurally precluded.
- **Nr. 1(b) Biometric categorisation** — Assigning a natural person to a category by inferring a sensitive Art. 9(1) GDPR attribute from biometric data is profiling by definition (GDPR Art. 4(4)). Exception precluded.
- **Nr. 1(c) Emotion recognition** — Inferring an emotion or intention from biometric data of a natural person evaluates a personal aspect and constitutes profiling. Exception precluded.

In practice: do not rely on Art. 6(3) for Area 1 systems. The realistic path to non-high-risk status is to fall outside the use-case definitions in the first place (e.g. genuine biometric verification under Nr. 1(a); inference of non-sensitive attributes under Nr. 1(b); detection of physical states or readily-apparent-but-uninterpreted expressions under Nr. 1(c)).

## Common profiling considerations

Profiling under GDPR Art. 4(4) means any automated processing of personal data consisting of using personal data to evaluate certain personal aspects relating to a natural person. All three Annex III Nr. 1 sub-categories perform exactly this:

- RBI evaluates "who is this person" by matching biometric features to identity records.
- Biometric categorisation evaluates a sensitive personal aspect (ethnic origin, health, genetic predisposition) by inferring it from biometric input.
- Emotion recognition evaluates the emotional or mental state of a natural person, again from biometric input.

Because the Art. 6(3) final-subparagraph re-exception applies whenever an Annex III system performs profiling, the Art. 6(3) "no significant risk" exception is effectively closed in this area. Classifiers should default to **high-risk** for any system that survives the Art. 5 prohibition filter and meets the Annex III Nr. 1 use-case conditions.

## Cross-references

- [art-6-3-exception-decision-tree.md](art-6-3-exception-decision-tree.md) — full decision tree for the Art. 6(3) exception (and its profiling re-exception).
- Related follow-on activities: **role determination** (provider/deployer/distributor/importer), and **obligation mapping** once high-risk status is confirmed.
- AI Act Art. 5(1)(f), (g), (h) for the boundary with prohibited practices; Commission Guidelines on prohibited practices for detailed interpretation of each prohibition's conditions.
- AI Act Art. 26(10) — additional authorisation, documentation and reporting obligations for law-enforcement deployers of post-RBI systems.
- AI Act Art. 50 — transparency obligation applies to emotion-recognition and biometric-categorisation systems regardless of whether they are high-risk; deployers must inform exposed natural persons of the system's operation.
- GDPR Art. 9(1) — the catalogue of sensitive attributes that triggers the Nr. 1(b) high-risk classification (and the narrower Art. 5(1)(g) prohibition catalogue).
