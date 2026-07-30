---
name: "stl-lebanon-jeanne-sulzer"
description: "Verification-first methodology for the Special Tribunal for Lebanon. Citations are verified against the STL legacy archive and legal-tools.org. Covers the Ayyash et al. case, the two contempt cases (STL-14-05 New TV/Al-Khayat and STL-14-06 Akhbar Beirut/Al-Amin), and the 2011 terrorism decision. Research aid, not legal advice. Part of the open-source \"Skills for International Justice\" library — methodology: github.com/jeannesulzer/international-criminal-tribunals-skills"
metadata:
  author: "Jeanne Sulzer"
  license: "cc-by-4.0"
  version: "2026-06-10"
---

# STL — Special Tribunal for Lebanon

This skill governs every output that touches the Special Tribunal for Lebanon. The discipline is simple and the reason for it is concrete: the STL is the only international tribunal in modern history to have adjudicated a single political assassination as terrorism under a hybrid framework applying Lebanese domestic law within an international procedural architecture. Its case numbers are exact, its in absentia trial framework is unusual, and its 2011 Interlocutory Decision on the Applicable Law is one of the most-cited (and most-contested) post-9/11 jurisprudential developments in international criminal law. A fabricated citation here misrepresents holdings that are still being debated.

## The discipline in one paragraph

For any case-specific document — judgment, decision, indictment, filing, OTP submission, victim participation order — verify before citing. "Verify" means `web_fetch` (or equivalent retrieval) to stl-tsl.org (the legacy site, archived since closure on 31 December 2023) or legal-tools.org in the current conversation. Foundational texts in project knowledge (UN-Lebanon Agreement, Statute of the STL annexed to Resolution 1757, Rules of Procedure and Evidence) are the exception; they may be cited directly. Nothing else.

## Verification is gradient, not binary

In practice, retrieval to stl-tsl.org usually works — the site is preserved as a legacy archive but is no longer actively maintained, so some materials are more reliably reached on legal-tools.org. Three levels:

- **Existence verified.** Document number, case number, date, chamber confirmed against an authoritative source. Sufficient for "X was indicted in case Y."
- **Content verified.** The fetched text confirms the proposition in substance. Sufficient for "the Trial Chamber held that…".
- **Paragraph verified.** The specific cited paragraph(s) contain the cited proposition. Required for any quotation and for any paragraph-pinpoint citation.

Label the level where relevant. The 2011 Interlocutory Decision and the Ayyash Trial Judgment are constantly paraphrased; if quoting, verify the exact wording against the official text.

## Standard workflow

**Step 0 — Identify the document.** Before anything else, distinguish:
- The **Ayyash et al. main case** (STL-11-01) — the principal trial concerning the 14 February 2005 attack against Hariri and others
- The **connected/related-attacks cases** under STL-11-01 (attacks of 1 October 2004 against Marwan Hamadeh; 21 June 2005 against George Hawi; 12 July 2005 against Elias El-Murr)
- The **Merhi case** (STL-13-04) — joined with the main case
- The **STL-18-10 case** — Ayyash on related attacks (El-Murr, Hamadeh, Hawi) tried separately after the main judgment
- The **contempt cases** — STL-14-05 (New TV S.A.L. and Al-Khayat), STL-14-06 (Akhbar Beirut S.A.L. and Al-Amin)
- The **2011 Interlocutory Decision on the Applicable Law** (STL-11-01/I/AC/R176bis) — the famous standalone Appeals Chamber decision

The case identifier matters. STL-11-01 is the principal case; STL-18-10 is a related-attacks case that was opened later. Confusing them corrupts everything downstream.

**Step 1 — Plan citations.** List every citation that will appear in the output. For each, note the proposition it supports and the source to verify against.

**Step 2 — Verify with the fallback ladder.** For each case-specific citation, work the ladder in `references/verification-workflow.md`: stl-tsl.org → legal-tools.org → ICC Legal Tools (which mirrors STL documents) → secondary source clearly labelled → ask the user. Capture case number, document number, chamber, date, paragraph.

**Step 3 — Draft using verified material.** Use the citation format in `references/citation-format.md`. Where verification is partial, say so.

**Step 4 — Self-audit.** Each citation must trace to project knowledge or to a successful retrieval in this conversation, with verification level appropriate to the claim.

## Foundational texts (cite from project knowledge when present)

- **Agreement between the United Nations and the Lebanese Republic on the establishment of a Special Tribunal for Lebanon** (signed at New York 23 January 2007 and at Beirut 6 February 2007; entered into force 10 June 2007 by operation of Resolution 1757)
- **UN Security Council Resolution 1757 (2007)** of 30 May 2007 (adopted under Chapter VII of the UN Charter), with annexed Agreement and **Statute of the Special Tribunal for Lebanon**
- **Statute of the Special Tribunal for Lebanon** (annexed to the Agreement, in turn annexed to Resolution 1757) — key articles: Art. 1 (jurisdiction), Art. 2 (applicable criminal law — Lebanese criminal law), Art. 3 (individual criminal responsibility), Art. 4 (concurrent jurisdiction), Art. 5 (non bis in idem), Art. 16 (rights of the accused), Art. 17 (victim participation), Art. 22 (trial in absentia), Art. 26 (appellate proceedings)
- **Rules of Procedure and Evidence of the STL** (adopted by the judges 20 March 2009, amended numerous times — the revision in force at the date of a cited decision controls; particular relevance: Rule 86 on victim participation, Rule 105 bis on sentencing, Rule 106 on review)

If not in project knowledge, retrieve from stl-tsl.org/en/documents/statute-of-the-tribunal before citing. See `references/foundational-texts.md`.

## The institutional architecture (get this right)

- **Established:** by UN Security Council Resolution 1757 (2007) of 30 May 2007, under Chapter VII of the UN Charter, after Lebanese parliamentary ratification of the bilateral UN-Lebanon Agreement failed to occur within the prescribed deadline. The Agreement and Statute entered into force on **10 June 2007**.
- **Seat:** **Leidschendam, Netherlands** (near The Hague), with a field office in Beirut.
- **Operations:** commenced **1 March 2009**.
- **Closure:** the Tribunal formally closed on **31 December 2023**. A small residual mechanism continues to handle specific tasks (post-completion functions, witness protection, sentence enforcement coordination) under the supervision of the United Nations.
- **Composition:** Lebanese and international judges (a hybrid bench), a Pre-Trial Judge, three Trial Chamber judges and two alternates, five Appeals Chamber judges, a President, a Prosecutor, a Registrar, a Head of Defence Office, and a Victims' Participation Unit.
- **Distinguishing features:**
  - **Apply Lebanese domestic criminal law** for substantive offences (the only international tribunal to do so as its principal substantive law)
  - **Trial in absentia** explicitly authorised by Statute Art. 22 — and used in Ayyash et al.
  - **Defence Office** as an independent organ on equal footing with the Prosecutor (one of the most institutionally robust defence frameworks in international criminal justice)
  - Subject-matter jurisdiction narrowly drawn around the 14 February 2005 attack and connected attacks (the latter on a "connection" test set out in the Statute)

## Source hierarchy

**Tier 1 (authoritative):**
- **stl-tsl.org** — the official STL website, preserved as a legacy archive after the 31 December 2023 closure. Hosts the Statute, the Agreement, RPE (all amended versions), all major judgments and decisions, indictments, public records of the proceedings
- **legal-tools.org** — ICC Legal Tools Database, mirrors STL principal decisions
- **un.org/sc** for the founding resolutions (1644, 1664, 1686, 1757) and Secretary-General reports on the establishment of the STL

**Tier 2 (secondary, must be labelled):**
- UN Audiovisual Library of International Law (`legal.un.org/avl/`) — for the Statute introductory note and Resolution 1757 commentary
- Academic commentary — Cassese, Boas, Schabas, Sluiter, Stahn, Tochilovsky on the STL specifically; Michael P. Scharf and the Case Western Reserve War Crimes Research Office publications on the 2011 Interlocutory Decision; Marko Milanović and Sergey Vasiliev on the terrorism-as-customary-law debate
- *Journal of International Criminal Justice* (Oxford) — symposium issues on STL doctrine
- Trial-monitoring NGOs (Lebanese Center for Human Rights — CLDH, Justice Without Frontiers)
- Journalism (Naharnet, JusticeInfo.net, L'Orient-Le Jour)

**Never authoritative:** Wikipedia, Grokipedia, social media, AI-generated summaries, blogs (unless from a serious scholar).

See `references/authoritative-sources.md`.

## Citation format

STL citations are precise. Two pieces matter for every case-specific citation:

1. **The Case Number** — `STL-[YY]-[NN]` (year of indictment confirmation + sequential number). Examples:
   - `STL-11-01` — Ayyash et al. (main case)
   - `STL-13-04` — Merhi (joined with main case in 2014)
   - `STL-18-10` — Ayyash et al. (connected attacks of El-Murr, Hawi, Hamadeh)
   - `STL-14-05` — New TV S.A.L. and Al-Khayat (contempt)
   - `STL-14-06` — Akhbar Beirut S.A.L. and Al-Amin (contempt)

2. **The Document Reference** — `STL-[YY]-[NN]/[Phase]/[Chamber]` followed by a filing number. Phase suffixes:
   - `I` — Pre-Trial / Interlocutory
   - `PT` — Pre-Trial Chamber
   - `T` — Trial Chamber
   - `S` — Sentencing
   - `A` — Appeals Chamber
   - `A-1` — Appeal of the first judgment
   - `R[number]bis` — Rule-based proceedings (e.g. R176 bis for the 2011 Applicable Law decision)

Document references work like ICC: filing number assigned in chronological order by the Court Records Office. Example: `STL-11-01/T/TC/F3840` (filing 3840 in case STL-11-01 before the Trial Chamber, with TC indicating Trial Chamber sealing).

Decisions cite by case number, document type, chamber, title, date, paragraph.

**Worked examples:**
- *Prosecutor v. Ayyash et al.*, STL-11-01/T/TC, Judgment, Trial Chamber, 18 August 2020.
- *Prosecutor v. Ayyash et al.*, STL-11-01/S/TC, Sentencing Judgment, Trial Chamber, 11 December 2020.
- *Prosecutor v. Ayyash et al.*, STL-11-01/I/AC/R176bis, Interlocutory Decision on the Applicable Law: Terrorism, Conspiracy, Homicide, Perpetration, Cumulative Charging, Appeals Chamber, 16 February 2011.

See `references/citation-format.md` for the full guide, case-name conventions, and the table of frequently cited authorities.

## The 2011 Interlocutory Decision — handle with extra care

The Appeals Chamber's **Interlocutory Decision on the Applicable Law** of 16 February 2011 (STL-11-01/I/AC/R176bis) is among the most discussed STL decisions, and the most often miscited. Its key findings:

1. **Terrorism as a crime under customary international law in peacetime** — the Appeals Chamber held that an emerging customary international law definition of "transnational terrorism" had crystallised. **This is heavily contested in scholarship** (Milanović, Saul, Ambos, Kress) and was not followed in subsequent international jurisprudence. When citing, note the contested status.
2. **Modes of liability** — clarified joint criminal enterprise (JCE I and II) as applicable under STL law to terrorism; refused JCE III on grounds of *nullum crimen sine lege* applied to specific intent.
3. **Cumulative charging** — addressed how Lebanese criminal law characterisations interact with international modes of liability.
4. Multiple substantive points on perpetration, conspiracy and homicide under Lebanese law.

Always indicate the contested character of the customary-international-law finding when relevant. The decision is a Tier 1 source for STL jurisprudence; it is not a universally accepted statement of customary international law.

## Audit mode depends on document type

When the user supplies a document:
- **Working drafts** (briefs, memos, submissions in progress): audit citations for accuracy. Existence and proposition both need verification.
- **Final Court records**: citations within the document are by definition Court-issued. The audit task shifts to inventorying which referenced documents downstream work will need to fetch, and distinguishing public from confidential versions.

In either mode, Step 0 (identify the document) comes first.

## Substantive doctrine — pointers

The skill does not encode doctrine line by line. Starting points:

- **Subject-matter jurisdiction** → Statute Art. 1 (the 14 February 2005 attack against Hariri; connected attacks between 1 October 2004 and 12 December 2005; any later date determined by the Parties with the consent of the Security Council). The "connection" test (criminal intent, purpose, victims targeted, modus operandi, perpetrators) is set out in Art. 1.
- **Applicable substantive criminal law** → Statute Art. 2: Lebanese criminal law — specifically the **Criminal Code of Lebanon** provisions on acts of terrorism (Art. 314), crimes and offences against human life (Art. 547-551), illicit associations (Art. 188-189, 335), the **Law on Increasing the Punishments of Sedition, Civil War and Inter-Confessional Strife** (11 January 1958). International criminal modes of liability under Statute Art. 3.
- **Modes of individual criminal responsibility** → Statute Art. 3: commission, participation, attempted commission, aiding and abetting, ordering, instigating, command responsibility. JCE applied per 2011 Interlocutory Decision (JCE I and II); JCE III rejected for terrorism specific-intent crime.
- **Trial in absentia** → Statute Art. 22; activated by the Trial Chamber in *Ayyash et al.* on 1 February 2012 following Pre-Trial Judge's decision; controlled by Rule 106 (Rules of Procedure and Evidence) for review on arrest.
- **Victim participation** → Statute Art. 17 and Rule 86 of the RPE; over 70 victims granted Victim-Participating-in-Proceedings (VPP) status in *Ayyash et al.*
- **Reparations** → Statute does not establish a reparations mechanism; victims may seek compensation through Lebanese national courts on the basis of the STL conviction (Statute Art. 25(3)).

For each, verify the specific decision through the workflow before citing. See `references/jurisprudence-map.md`.

## Sensitive contexts

The STL adjudicated the 14 February 2005 attack on Hariri — a political assassination embedded in the Lebanese sectarian political system, the Syrian withdrawal from Lebanon, and the Hezbollah question. The Tribunal's findings continue to be politically contested in Lebanon, and the convicted defendant remains at large. Maintain factual precision, identify holdings carefully, and remember that the *Ayyash* Trial Judgment expressly noted that the evidence did not implicate Hezbollah's leadership — a sensitive and important finding. Avoid sensationalism. Use the public, non-confidential versions of documents.

## What this skill is not

- Not legal advice. Outputs are research and drafting aids.
- Not a substitute for the STL's records.
- Not a position on the contested findings of the 2011 Interlocutory Decision on customary international law terrorism. The skill enables accurate citation of the STL's finding; the academic debate on its customary status is left to the user.
- Not endorsed by the STL, the UN, or the Lebanese Republic. This is an independent open-source project.

## Reference files

- `references/authoritative-sources.md` — source hierarchy and URL patterns specific to the STL
- `references/citation-format.md` — case-number anatomy, phase suffixes, party-designation conventions, and the table of frequently cited authorities (Ayyash, Merhi, the 2011 Interlocutory Decision, contempt cases)
- `references/verification-workflow.md` — step-by-step procedure, fallback ladder, the in-absentia / Defence Office discipline
- `references/foundational-texts.md` — the UN-Lebanon Agreement, Resolution 1757, the Statute, and the Rules of Procedure and Evidence; how to work with them
- `references/jurisprudence-map.md` — topic-by-topic map of the STL's principal holdings
- `examples/example-verification.md` — verifying one STL citation end-to-end (the 2011 Interlocutory Decision)
- `examples/example-audit.md` — auditing user-supplied documents (Ayyash Trial Judgment and the 2011 Interlocutory Decision typical errors)
