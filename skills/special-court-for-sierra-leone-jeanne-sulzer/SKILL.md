---
name: "scsl-rscsl-special-court-for-sierra-leone-jeanne-sulzer"
description: "Verification-first methodology for the Special Court for Sierra Leone and its Residual Special Court. Citations are verified against rscsl.org and legal-tools.org. Covers Taylor, the AFRC/CDF/RUF cases, the child-soldier and forced-marriage holdings, the head-of-State immunity decision, and the fixed-term (no life) penalty regime. Research aid, not legal advice. Part of the open-source \"Skills for International Justice\" library — methodology: github.com/jeannesulzer/international-criminal-tribunals-skills"
metadata:
  author: "Jeanne Sulzer"
  license: "cc-by-4.0"
  version: "2026-06-10"
---

# SCSL — Special Court for Sierra Leone and the Residual Special Court (RSCSL)

This skill governs every output that touches the Special Court for Sierra Leone and its Residual Special Court. The discipline is simple and the reason for it is concrete: the SCSL produced landmark jurisprudence on the recruitment of child soldiers as a war crime, on forced marriage as a crime against humanity, on the responsibility of a sitting head of State, and on the joint criminal enterprise doctrine in the Sierra Leone armed conflicts. It is also the only modern hybrid tribunal that convicted a former head of State (Charles Taylor, 26 April 2012). Case numbers, document references, and the parallel structure of the three main joint trials (AFRC, CDF, RUF) need to be cited with precision.

## The discipline in one paragraph

For any case-specific document — judgment, decision, indictment, filing, OTP submission — verify before citing. "Verify" means `web_fetch` (or equivalent retrieval) to **rscsl.org** (the official Residual Special Court website, which preserves the SCSL legacy) or legal-tools.org in the current conversation. Foundational texts in project knowledge (UN-Sierra Leone Agreement, SCSL Statute, Rules of Procedure and Evidence) are the exception; they may be cited directly. Nothing else.

## Verification is gradient, not binary

In practice, retrieval to rscsl.org succeeds (the site is the legacy repository, actively maintained for the Residual Court's functions). Three levels:

- **Existence verified.** Case number, document type, date, chamber confirmed.
- **Content verified.** The fetched text confirms the proposition in substance.
- **Paragraph verified.** The specific cited paragraph contains the cited proposition.

Label the level where relevant.

## Standard workflow

**Step 0 — Identify the document.** Before anything else, distinguish:
- The **case** (Taylor; AFRC; CDF; RUF; or contempt/residual)
- The **chamber** — Trial Chamber I, Trial Chamber II, Appeals Chamber, or Residual Special Court
- The **document type** — Indictment (Initial / Amended / Consolidated), Decision, Trial Judgement, Sentencing Judgement, Appeals Judgement, Contempt Decision

**Step 1 — Plan citations.** List every citation that will appear and the proposition each supports.

**Step 2 — Verify with the fallback ladder.** rscsl.org → legal-tools.org → secondary source (clearly labelled) → ask the user.

**Step 3 — Draft using verified material.** Use the citation format in `references/citation-format.md`.

**Step 4 — Self-audit.** Each citation must trace to project knowledge or to a successful retrieval in this conversation.

## Foundational texts (cite from project knowledge when present)

- **UN Security Council Resolution 1315 (2000)** of 14 August 2000 — requested the Secretary-General to negotiate an agreement with the Government of Sierra Leone to create an independent special court
- **Agreement between the United Nations and the Government of Sierra Leone on the Establishment of a Special Court for Sierra Leone** (Freetown, 16 January 2002) — the bilateral establishing agreement
- **Statute of the Special Court for Sierra Leone**, annexed to the Agreement — the operative text. Key articles:
  - Art. 1 — Competence (persons who bear the greatest responsibility for serious violations of international humanitarian law and Sierra Leonean law committed in Sierra Leone since 30 November 1996)
  - Art. 2 — Crimes against humanity
  - Art. 3 — Violations of Article 3 common to the Geneva Conventions and Additional Protocol II
  - Art. 4 — Other serious violations of international humanitarian law (including **Art. 4(c): conscripting or enlisting children under the age of 15 years into armed forces or groups or using them to participate actively in hostilities** — the landmark child-soldier provision)
  - Art. 5 — Crimes under Sierra Leonean law (specific offences from the Prevention of Cruelty to Children Act 1926; the Malicious Damage Act 1861)
  - Art. 6 — Individual criminal responsibility (modes including commission, ordering, soliciting, inducing, aiding and abetting, JCE; superior responsibility under Art. 6(3))
  - Art. 6(2) — **No immunity for heads of State** — the basis for the Taylor case
  - Art. 7 — Jurisdiction over persons of 15 years of age and above at the time of the alleged commission (an important departure: SCSL does not prosecute child perpetrators)
  - Art. 8 — Concurrent jurisdiction with Sierra Leonean courts; SCSL has primacy
  - Art. 9 — Non bis in idem
  - Art. 12 — Composition of the Chambers (Trial Chamber and Appeals Chamber)
  - Art. 17 — Rights of the accused
  - Art. 19 — Penalties (imprisonment for a specified number of years — the SCSL Statute provides no life-imprisonment penalty and no death penalty; the longest sentence imposed in practice was Taylor's 50 years)
- **Rules of Procedure and Evidence of the SCSL** — adopted by the judges; multiple revisions
- **Agreement between the United Nations and the Government of Sierra Leone on the Establishment of a Residual Special Court for Sierra Leone** (signed 29 July 2010 in New York and 11 August 2010 in Freetown; the RSCSL commenced functioning on the SCSL's dissolution on 2 December 2013)
- **Statute of the Residual Special Court for Sierra Leone**, annexed to the 2010 Agreement — provides for residual functions: supervision of sentences, witness protection, archives, contempt prosecutions, claims for compensation

If not in project knowledge, retrieve from rscsl.org/Documents.

## The institutional architecture (get this right)

- **SCSL established:** by Agreement of 16 January 2002, pursuant to UN Security Council Resolution 1315 (2000).
- **SCSL seat:** **Freetown, Sierra Leone** (the Charles Taylor trial was moved to The Hague for security reasons by UN Security Council Resolution 1688 (2006); judgment delivered at the ICC premises in The Hague).
- **SCSL operations:** 2002 – 2 December 2013.
- **RSCSL succeeded SCSL:** on dissolution of the SCSL on 2 December 2013, the Residual Special Court for Sierra Leone (RSCSL) inherited the legacy and residual functions, including supervision of Taylor's sentence and witness protection. **The RSCSL has a seat in Freetown and an "interim" seat in The Hague** for matters requiring an out-of-Sierra-Leone location. Active as of 2026.
- **Distinguishing features:**
  - **Hybrid Sierra Leonean / international** — international and Sierra Leonean judges, both Sierra Leonean and international law applicable (Statute Arts. 2-5)
  - **First international tribunal in modern history to convict a former head of State** — Charles Taylor, 26 April 2012
  - **First international tribunal to convict for conscripting / enlisting children under 15 as a war crime** — affirmed multiple times across the AFRC, CDF, RUF, and Taylor cases
  - **First international tribunal to convict for forced marriage as an "other inhumane act" crime against humanity** — AFRC Appeal Judgment 2008
  - **No reparations** to victims (Statute does not establish a reparations mechanism)
  - **No death penalty** (Statute Art. 19)

## Source hierarchy

**Tier 1 (authoritative):**
- **rscsl.org** — the official Residual Special Court website. Hosts the SCSL Statute, the RSCSL Statute, the Rules of Procedure and Evidence, all major judgments and decisions, indictments, hearing transcripts, and case files for all completed cases (Taylor, AFRC, CDF, RUF, contempt cases)
- **legal-tools.org** — ICC Legal Tools Database. Mirrors SCSL principal decisions
- **un.org** — for Resolution 1315 (2000), Resolution 1688 (2006) (relocation of Taylor trial), and Secretary-General reports
- **worldcourts.com/scsl** — sometimes useful for older filings (Tier 1 only when the rscsl.org or legal-tools.org version cannot be located)

**Tier 2 (secondary, must be labelled):**
- **Cassese / Boas / Schabas / Mettraux / Jalloh** — academic commentary
- **Charles C. Jalloh (ed.)** — *The Sierra Leone Special Court and Its Legacy: The Impact for Africa and International Criminal Law* (Cambridge UP 2014) — the standard scholarly treatment
- **Stuart Beresford & Hafida Lahiouel**, **Maya Steinitz**, **Sara Kendall & Sarah Nouwen** — academic articles
- **Journal of International Criminal Justice** — symposium issues
- **No Peace Without Justice** — Italian NGO trial monitoring
- **International Crisis Group**, **Human Rights Watch**, **Amnesty International** — context reporting
- **Charles Taylor case-specific journalism** — JusticeInfo.net, BBC, AP

**Never authoritative:** Wikipedia, Grokipedia, social media, AI summaries.

See `references/authoritative-sources.md`.

## Citation format

SCSL citations follow a specific format. Two pieces matter:

1. **Case Number** — `SCSL-[YY]-[NN]` followed by phase suffix:
   - `SCSL-03-01` — Taylor
   - `SCSL-04-14` — CDF (Norman, Fofana, Kondewa)
   - `SCSL-04-15` — RUF (Sesay, Kallon, Gbao)
   - `SCSL-04-16` — AFRC (Brima, Kamara, Kanu)
   - Phase suffixes: `-I` (Initial/Indictment), `-PT` (Pre-Trial), `-T` (Trial), `-A` (Appeal)

2. **Document Reference** — case number + filing number, e.g. `SCSL-03-01-T-1281`.

**Worked examples:**
- *Prosecutor v. Taylor*, Case No. SCSL-03-01-T, Judgement (Trial Chamber II), 18 May 2012 [Trial Judgement], with Corrigendum SCSL-03-01-T-1284, 30 May 2012.
- *Prosecutor v. Taylor*, Case No. SCSL-03-01-T-1285, Sentencing Judgement, 30 May 2012.
- *Prosecutor v. Taylor*, Case No. SCSL-03-01-A, Appeal Judgement (Appeals Chamber), 26 September 2013.
- *Prosecutor v. Sesay, Kallon and Gbao*, Case No. SCSL-04-15-A, Appeal Judgement, 26 October 2009 [the RUF case].
- *Prosecutor v. Fofana and Kondewa*, Case No. SCSL-04-14-A, Appeal Judgement, 28 May 2008 [the CDF case].
- *Prosecutor v. Brima, Kamara and Kanu*, Case No. SCSL-04-16-A, Appeal Judgement, 22 February 2008 [the AFRC case].

See `references/citation-format.md` for the full convention.

## Audit mode depends on document type

When the user supplies a document:
- **Working drafts**: audit citations for accuracy.
- **Final SCSL/RSCSL records**: inventory and spot-check.

In either mode, Step 0 (identify the document and the case) comes first.

## Substantive doctrine — pointers

The skill does not encode doctrine line by line. Starting points (each verified through the workflow before citing):

- **Child soldiers as a war crime** → SCSL Statute Art. 4(c); central holdings across the AFRC Trial Judgement (20 June 2007), the AFRC Appeal Judgement (22 February 2008), the CDF Trial Judgement (2 August 2007), the CDF Appeal Judgement (28 May 2008), the RUF Trial Judgement (2 March 2009), the RUF Appeal Judgement (26 October 2009), and the Taylor Trial Judgement (18 May 2012). The SCSL is the modern foundation of the doctrine.
- **Forced marriage as a crime against humanity** → first recognised as "other inhumane act" under Statute Art. 2(i) in the AFRC Appeal Judgement of 22 February 2008 (paras 175-203); affirmed in the RUF and Taylor cases. Landmark jurisprudence.
- **No immunity for sitting/former heads of State** → SCSL Statute Art. 6(2); the Taylor case is the modern foundation. The 31 May 2004 Appeals Chamber Decision on Immunity from Jurisdiction (in the early Taylor proceedings) is one of the most-cited decisions of the SCSL.
- **Aiding and abetting standard** → the Taylor Appeal Judgement of 26 September 2013 articulates the "substantial effect" standard for aiding and abetting at the international tribunals — a major doctrinal landmark, in some tension with the parallel ICTY *Perišić* jurisprudence.
- **Joint criminal enterprise** → AFRC, CDF, RUF, Taylor — applied throughout; the JCE jurisprudence at the SCSL draws on *Tadić* (ICTY) but adds Sierra Leone-specific elaboration.
- **Sexual slavery and sexual violence** → AFRC, RUF, Taylor — sexual violence as crimes against humanity and war crimes.
- **Destruction of religious or cultural property** → CDF case (Norman, Fofana, Kondewa).
- **Crime against humanity of "other inhumane acts"** → forced marriage (AFRC), forced labour (RUF), etc.

For each, verify through the workflow.

## Sensitive contexts

The Sierra Leone conflict (1991-2002) was characterised by extreme cruelty — amputations, abductions, child soldier recruitment, forced marriages, sexual slavery. Tens of thousands killed; over a million displaced. Survivors and victims continue to live with the consequences. Outputs may be read by victim communities, by the Sierra Leone Truth and Reconciliation Commission's institutional successors, and by survivors. Maintain factual precision, avoid sensationalism, never minimise. Use the public, non-confidential versions of documents. The CDF defendants were former government / pro-government militia — accurately characterising the political affiliations matters and is often contested.

## What this skill is not

- Not legal advice. Outputs are research and drafting aids.
- Not a substitute for the SCSL/RSCSL records.
- Not endorsed by any institution.

## Reference files

- `references/authoritative-sources.md` — source hierarchy and URLs (rscsl.org, legal-tools.org)
- `references/citation-format.md` — case-number anatomy (SCSL-03-01, SCSL-04-14, SCSL-04-15, SCSL-04-16), phase suffixes, party-designation conventions, table of frequently cited authorities
- `references/verification-workflow.md` — fallback ladder, the four case-confusion traps (AFRC vs CDF vs RUF; Taylor seat location; head-of-state immunity; aiding-and-abetting standard tension with Perišić)
- `references/foundational-texts.md` — Resolution 1315, UN-Sierra Leone Agreement, SCSL Statute, RPE, RSCSL Statute
- `references/jurisprudence-map.md` — topic-by-topic map of SCSL holdings
- `examples/example-verification.md` — verifying the Taylor Trial Judgement and a child-soldier citation
- `examples/example-audit.md` — auditing user-supplied documents
