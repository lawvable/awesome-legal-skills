# Generic Country Assessment Questionnaire

Use this file when assessing a transfer to a country NOT covered by a dedicated profile (i.e., not in `us-non-dpf.md`, `us-dpf.md`, `uk-post-adequacy.md`, `in.md`, `cn.md`, `br.md`, `au.md`, `sg.md`, `tr.md`, `ae.md`, `za.md`, `ru.md`).

This is a structured framework — the practitioner (or the skill, with practitioner input) walks through the questions and builds an ad hoc profile for the country.

---

## Step 1: Adequacy Status Check

Before running the assessment, check whether the country has an adequacy decision. Current adequacy countries (as of 2026-05-29, not exhaustive — verify with Commission Implementing Decisions database):

- Andorra, Argentina, Canada (PIPEDA-regulated only), Faroe Islands, Guernsey, Isle of Man, Israel, Japan (with supplementary rules), Jersey, New Zealand, Republic of Korea (PIPA-regulated; note decision carve-outs), Switzerland, United Kingdom (until 27 Dec 2031), Uruguay, USA (DPF-certified only — see `us-dpf.md`).

If the destination has adequacy → lightweight assessment only. Document the adequacy decision reference, any conditions, expiry/review dates.

**If no adequacy → first identify the Chapter V transfer tool** in use (SCCs and which module, BCRs, ad hoc clauses, or an Art. 49 derogation) before assessing third-country law — the tool determines whether a full TIA (Art. 46) or an Art. 49 documentation path applies. Then continue.

## Step 2: Data Protection Framework Questions

**Block A — Data protection law:**
1. Does the country have a general data protection law?
   - If yes: name, year, scope of application.
   - If no: sectoral laws may exist (health, finance, telecoms) — list applicable ones.

2. Is there a supervisory authority?
   - Name and structural position (independent agency, executive ministry, advisory body).
   - Enforcement track record (administrative fines, civil claims, criminal sanctions).

3. What data subject rights exist?
   - Access, correction, deletion, objection, portability, automated decision objection.
   - Note gaps vs. GDPR.

4. Are there effective remedies?
   - Administrative complaints to SA.
   - Civil claims with monetary damages.
   - Criminal sanctions for data protection violations.

## Step 3: Surveillance & Government Access Law Questions

**Block B — For each applicable surveillance/access law:**

1. What is the law's scope?
   - Which entities are subject to it (telecoms only, internet providers, any provider)?
   - Which data types are accessible?
   - Which authorities can compel access?

2. What powers does it grant?
   - Targeted vs. bulk access.
   - Content vs. metadata.
   - Real-time vs. stored data.
   - Decryption / bypass capabilities.

3. **Guarantee A — Clear, precise, accessible rules:**
   - Is the legal basis published?
   - Are implementing rules public?
   - Are the categories of persons / data / circumstances defined?

4. **Guarantee B — Necessary and proportionate:**
   - Is the measure limited to defined objectives?
   - Is bulk access avoided or strictly controlled?
   - Are retention periods limited?

5. **Guarantee C — Independent oversight:**
   - Is there an oversight body?
   - Is it independent (not appointed by / removable by the surveilling executive)?
   - Does it have access to underlying materials?
   - Does it have effective enforcement powers?

6. **Guarantee D — Effective remedies:**
   - Can data subjects challenge surveillance?
   - Is there a notification mechanism?
   - Are remedies effective (binding, with meaningful consequences)?
   - Are remedies available to non-citizens?

## Step 4: Practical Risk Factors (Block C)

1. **Importer history of government access requests:**
   - Does the importer publish transparency reports?
   - What is the volume and trend of requests?
   - Has the importer received NSL-equivalent gag-orders?

2. **Realistic targeting basis:**
   - Sector (intelligence-relevant vs. ordinary commercial)
   - Data type (communications content vs. operational)
   - Scale (mass-user data vs. niche)
   - Geopolitical relevance

3. **Importer's technical posture:**
   - Plaintext access necessary for service?
   - Encryption with exporter-held keys feasible?
   - Local processing requirements?

4. **Authority interest:**
   - Is this data plausibly of interest to local authorities?
   - Any precedent of access requests for similar data sets?

## Step 5: Sources to Consult

When building a generic profile, prioritise:
- **Primary law** — official gazettes, ministry websites, legal databases.
- **EDPB and EDPS work** — Article 64 opinions; recent SA decisions involving the country.
- **CJEU case law** — any cases involving the country.
- **Major provider transparency reports** — Google, Microsoft, Meta, Apple publish country-by-country breakdowns.
- **Academic and NGO analyses** — Privacy International, EFF, country-specific research centres.
- **Local data protection community** — IAPP knowledge net, local DPO associations, country chapter publications.
- **Rosenthal questionnaire approach** — the Rosenthal EU SCC TIA Toolbox (v1.10) includes a structured "lawful access" questionnaire worth borrowing; see `../sources.md` for the reference. (The toolbox itself is not bundled in this skill.)

## Step 6: Conclude the Assessment

Apply the standard Step 3 three-way fork from `edpb-six-steps.md`:
1. Transfer tool effective → proceed.
2. Transfer tool not effective, supplementary measures needed → proceed to Step 4.
3. Transfer tool not effective on paper, but no realistic basis to believe problematic law will apply → proceed with thorough documentation.

When using this generic framework, the documentation burden is higher — the practitioner is doing the country-law research that pre-built profiles encode. Cite sources explicitly.

## Step 7: Recommend Profile Promotion

If a generic assessment is run for the same country multiple times, the practitioner should consider promoting it to a pre-built profile (PR to the skill). Provide the structured findings to the maintainer for inclusion in the next version.
