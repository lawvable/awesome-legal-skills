---
name: "ksc-jeanne-sulzer"
description: "Verification-first methodology for the Kosovo Specialist Chambers and Specialist Prosecutor's Office (The Hague, applying Kosovo law). Citations are verified against scp-ks.org before use; appeal registry numbers are cited only once confirmed. Covers Thaçi et al., Mustafa, Pjetër Shala and Gucati & Haradinaj. Research aid, not legal advice. Part of the open-source \"Skills for International Justice\" library — methodology: github.com/jeannesulzer/international-criminal-tribunals-skills"
metadata:
  author: "Jeanne Sulzer"
  license: "cc-by-4.0"
  version: "2026-06-10"
---

# KSC — Kosovo Specialist Chambers and Specialist Prosecutor's Office

This skill governs every output that touches the Kosovo Specialist Chambers (KSC), the Specialist Prosecutor's Office (SPO), and the Kosovo Relocated Specialist Judicial Institution (KRSJI). The discipline is simple and the reason for it is concrete: the KSC is the most institutionally unusual hybrid tribunal in operation — a Kosovo court relocated to The Hague, staffed exclusively by international judges and prosecutors, with jurisdiction over alleged crimes by Kosovo Liberation Army members emerging from the Council of Europe Parliamentary Assembly's 2011 "Marty Report". The institution is **actively operating** (as of 2026 the Thaçi et al. trial is in closing-statements phase), case numbers are specific and recent, and the political sensitivity of this jurisdiction makes citation accuracy especially important.

## The discipline in one paragraph

For any case-specific document — judgment, decision, indictment, filing, SPO submission, victim participation order — verify before citing. "Verify" means `web_fetch` (or equivalent retrieval) to **scp-ks.org** (the official KSC website, actively maintained) or legal-tools.org in the current conversation. Foundational texts in project knowledge (Law No. 05/L-053, Article 162 of the Kosovo Constitution, Rules of Procedure and Evidence) are the exception; they may be cited directly. Nothing else.

## Verification is gradient, not binary

In practice, retrieval to scp-ks.org succeeds reliably — the KSC is one of the best-documented active international tribunals. Three levels:

- **Existence verified.** Case number, document type, date, chamber/panel confirmed against an authoritative source.
- **Content verified.** The fetched text confirms the proposition in substance.
- **Paragraph verified.** The specific cited paragraph contains the cited proposition.

Label the level where relevant.

## Standard workflow

**Step 0 — Identify the document.** Before anything else, distinguish:
- The **case** (each KSC case has a distinct case number — see citation format)
- The **chamber or panel** — KSC has a four-tier architecture (Basic Court Chamber / Court of Appeals Chamber / Supreme Court Chamber / Constitutional Court Chamber) but cases are heard before specific **Panels** at each level (Pre-Trial Judge, Trial Panel I or II, Appeals Panel, etc.)
- The **document type** — Indictment, Decision Confirming Indictment, Trial Judgment, Sentencing Judgment, Reparation Order, Appeal Judgment, contempt decision
- **The status as of the date of writing** — the KSC is actively operating; case status changes (Thaçi et al. was in evidentiary phase 2023-2025, closing statements February 2026, awaiting judgment)

**Step 1 — Plan citations.** List every citation that will appear in the output. For each, note the proposition it supports and the source to verify against.

**Step 2 — Verify with the fallback ladder.** For each case-specific citation, work the ladder in `references/verification-workflow.md`: scp-ks.org → legal-tools.org → secondary source (clearly labelled) → ask the user. Capture case number, document number, date, panel/chamber.

**Step 3 — Draft using verified material.** Use the citation format in `references/citation-format.md`. Where verification is partial, say so.

**Step 4 — Self-audit.** Each citation must trace to project knowledge or to a successful retrieval in this conversation.

## Foundational texts (cite from project knowledge when present)

- **Article 162 of the Constitution of the Republic of Kosovo** — the constitutional basis (Amendment 24, adopted 2015) authorising the establishment of the Specialist Chambers and Specialist Prosecutor's Office as a temporary part of the Kosovo justice system, with a seat outside Kosovo
- **Law No. 05/L-053 on Specialist Chambers and Specialist Prosecutor's Office** (3 August 2015) — the principal substantive legal framework. The KSC has no separate "Statute" — Law 05/L-053 is the equivalent. Key articles:
  - Art. 1 — Object
  - Art. 3 — Status and seat
  - Art. 6-9 — Subject-matter jurisdiction (crimes against humanity, war crimes, other Kosovo law crimes)
  - Art. 10 — Personal and territorial jurisdiction
  - Art. 12 — Temporal jurisdiction (1 January 1998 – 31 December 2000)
  - Art. 13-18 — Applicable substantive law (Kosovo law + customary international law + international human rights law)
  - Art. 22 — Specialist Chambers structure (four chambers)
  - Art. 30-31 — Specialist Prosecutor's Office
  - Art. 34 — Detention
  - Art. 38 — Independence
  - Art. 39 — Cooperation
  - Art. 40 — Witness protection
  - Art. 41-43 — Rights of the accused, witness protection, victim participation
- **Rules of Procedure and Evidence before the Kosovo Specialist Chambers** — adopted by the judges, amended periodically. Rule 113 governs victim participation. The revision in force at the date of a cited decision controls.
- **Host State Agreement between Kosovo and the Netherlands** (15 February 2016) — names the KSC as the **Kosovo Relocated Specialist Judicial Institution (KRSJI)** and provides the legal basis for its operation in The Hague.

If not in project knowledge, retrieve from scp-ks.org/en/documents before citing.

## The institutional architecture (get this right)

- **Established by:** Article 162 of the Kosovo Constitution (Amendment 24, 2015) and Law No. 05/L-053 (3 August 2015), following an exchange of letters between Kosovo and the EU.
- **Background:** The Council of Europe Parliamentary Assembly Report by Senator Dick Marty of **7 January 2011** ("Inhuman treatment of people and illicit trafficking in human organs in Kosovo") led the EU to establish a **Special Investigative Task Force (SITF)** in September 2011. The SITF's evidence formed the basis of the SPO's investigations and indictments.
- **Seat:** The Hague, Netherlands (formally the "Kosovo Relocated Specialist Judicial Institution" under the 2016 Host State Agreement). The KSC may also sit in Kosovo.
- **Operations:** Began judicial operations 2016; first detentions late 2020.
- **Staffing:** **Exclusively international** judges and prosecutors (a defining institutional feature). EU and partner-state staffing (Canada, Norway, Switzerland, Turkey, USA).
- **Funding:** Primarily the European Union, with contributions from partner states.
- **Distinguishing features:**
  - A **domestic Kosovo court** (not an international tribunal *stricto sensu*), but located outside Kosovo and staffed only by internationals
  - **Four-chamber architecture** mirroring the Kosovo court system: Basic Court Chamber, Court of Appeals Chamber, Supreme Court Chamber, **Constitutional Court Chamber** (the last is unusual for any international or hybrid criminal tribunal — it handles constitutional referrals concerning KSC matters)
  - **Reparation orders** — the KSC orders reparations directly against convicted persons (see the Shala case, where Shala was ordered to pay €208,000 to victims). This is a substantive departure from the STL model.
  - **Concurrent (not complementary) jurisdiction** with Kosovo national courts, on the SPO's election
- **Status:** **Actively operating** as of 2026.

## Source hierarchy

**Tier 1 (authoritative):**
- **scp-ks.org** — the official KSC website. Actively maintained. Hosts the Law, the RPE, all major decisions and judgments, case information sheets, press releases, hearing transcripts (English, Albanian, Serbian), court records by case
- **legal-tools.org** — ICC Legal Tools Database, mirrors KSC principal decisions

**Tier 2 (secondary, must be labelled):**
- Council of Europe — the 2011 Marty Report and subsequent PACE resolutions
- Academic commentary — Michael G. Karnavas's KSC blog series (defence-side perspective); commentary in *Journal of International Criminal Justice*; Just Security and EJIL:Talk! analyses
- Trial monitoring — Balkan Investigative Reporting Network (BIRN), Humanitarian Law Center, KSC Watch
- Journalism — Balkan Insight, JusticeInfo.net

**Never authoritative:** Wikipedia, Grokipedia, social media, AI-generated summaries.

See `references/authoritative-sources.md`.

## Citation format

KSC citations follow a specific format. Two pieces matter:

1. **Case Number** — `KSC-BC-[YYYY]-[NN]` for criminal cases, `KSC-CA-[YYYY]-[NN]` for Court of Appeals proceedings, `KSC-SC-[YYYY]-[NN]` for Supreme Court proceedings, `KSC-CC-[YYYY]-[NN]` for Constitutional Court proceedings.

   The "BC" stands for "Before Chambers" (the Specialist Chambers as a whole). Year is the year of indictment confirmation or case opening.

2. **Document Reference** — case number + filing number (assigned chronologically by the Court Registry). Public filings receive an "F" prefix in some references but typically the structure is `KSC-BC-YYYY-NN/F[number]`.

**The principal KSC cases:**

| Case Number | Case Name | Status |
|---|---|---|
| **KSC-BC-2020-04** | *Specialist Prosecutor v. Pjetër Shala* | Concluded; Trial Judgment 16 July 2024; Appeal Judgment 14 July 2025 (sentence reduced from 18 to 13 years) |
| **KSC-BC-2020-05** | *Specialist Prosecutor v. Salih Mustafa* | Concluded; Trial Judgment 16 December 2022 (26 years); Appeal Judgment 14 December 2023 (reduced to 22 years); Supreme Court Panel annulled the sentence on 29 July 2024; resentenced to 15 years on 10 September 2024 (upheld February 2025) |
| **KSC-BC-2020-06** | *Specialist Prosecutor v. Thaçi, Veseli, Selimi and Krasniqi* | Trial ongoing; opening statements 3 April 2023; closing statements February 2026; awaiting judgment |
| **KSC-BC-2020-07** | *Specialist Prosecutor v. Hysni Gucati and Nasim Haradinaj* | Concluded; Trial Judgment 18 May 2022 (contempt — obstruction of justice); Appeal Judgment 2 February 2023 (sentences reduced) |
| **KSC-BC-2023-10** | *Specialist Prosecutor v. Sabit Januzi, Ismet Bahtijari and Haxhi Shala* | Concluded; guilty pleas December 2024 |
| **KSC-BC-2024-11** | *Specialist Prosecutor v. Thaçi et al. (administration of justice)* | Pre-trial; arrests December 2024; trial commenced 27 February 2026 |

See `references/citation-format.md` for the full convention.

## Audit mode depends on document type

When the user supplies a document:
- **Working drafts**: audit citations for accuracy. Existence and proposition both need verification.
- **Final Court records**: inventory and spot-check; distinguish public from confidential versions.

In either mode, Step 0 (identify the document) comes first.

## Substantive doctrine — pointers

The skill does not encode doctrine line by line. Starting points:

- **Subject-matter jurisdiction** → Law 05/L-053 Arts. 6-9: crimes against humanity, war crimes, other crimes under Kosovo law in relation to allegations in the 2011 Marty Report
- **Personal and temporal jurisdiction** → Law 05/L-053 Arts. 10, 12: crimes commenced or committed in Kosovo between **1 January 1998 and 31 December 2000** by or against citizens of Kosovo or the Federal Republic of Yugoslavia
- **Applicable substantive law** → Kosovo law (including the 1976 Yugoslav Criminal Code applicable at the time), customary international law, and international human rights law as in force at the time of the alleged conduct
- **Modes of individual criminal responsibility** → Law 05/L-053 Art. 16: commission, ordering, soliciting, inducing, aiding and abetting, joint criminal enterprise, command/superior responsibility
- **Reparation orders against convicted persons** → Law 05/L-053 Arts. 21-22 + RPE Rule 168: the KSC may order reparations against convicted persons directly. *Shala* set the leading practice (€208,000 reparation order, 29 November 2024)
- **Victim participation** → RPE Rule 113; victim status is granted by the Pre-Trial Judge; Victims' Counsel represents groups of victims at trial (155 participating victims in Thaçi et al.)
- **Contempt proceedings and obstruction of justice** → Law 05/L-053 Art. 15; KSC has its own contempt regime, used in *Gucati and Haradinaj* and forming the basis of the *Thaçi et al. (administration of justice)* case

For each, verify the specific decision through the workflow.

## Sensitive contexts

The KSC adjudicates alleged crimes by KLA members (Albanian-side). This is **politically extremely sensitive** in Kosovo, where the KLA is widely venerated and many of the accused (including Thaçi) are former senior political figures. Reverse-side allegations (Serbian forces' crimes in Kosovo) were the subject of ICTY proceedings, not KSC proceedings. Maintain factual precision. Avoid sensationalism. Avoid characterising defendants as guilty before judgment (Thaçi et al. is still awaiting judgment as of 2026). Use public, non-confidential versions of documents. The Marty Report itself is a Council of Europe parliamentary document, not a judicial finding — note this when citing.

## What this skill is not

- Not legal advice. Outputs are research and drafting aids.
- Not a substitute for the KSC's records.
- Not endorsed by the KSC or any institution.
- Not a political comment on the legitimacy of the KSC, which is a contested institution in Kosovo. The skill enables accurate citation of the KSC's record; political evaluation is left to the user.

## Reference files

- `references/authoritative-sources.md` — source hierarchy and URLs
- `references/citation-format.md` — case-number anatomy, party-designation conventions, frequently cited authorities
- `references/verification-workflow.md` — step-by-step procedure, fallback ladder, KSC-specific traps
- `references/foundational-texts.md` — Article 162 of the Kosovo Constitution, Law 05/L-053, RPE, Host State Agreement
- `references/jurisprudence-map.md` — topic-by-topic map of KSC holdings (still developing — current as of 2026)
- `examples/example-verification.md` — verifying one KSC citation end-to-end
- `examples/example-audit.md` — auditing user-supplied documents
