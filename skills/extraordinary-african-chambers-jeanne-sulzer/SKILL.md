---
name: "eac-habre-jeanne-sulzer"
description: "Méthodologie « verification-first » pour les Chambres Africaines Extraordinaires (procès Hissène Habré, Dakar). Toute citation est vérifiée (forumchambresafricaines.org, legal-tools.org). Couvre le jugement du 30 mai 2016, l'arrêt d'appel du 27 avril 2017 (réparations de 82,290 milliards FCFA pour 7 396 victimes), et la compétence universelle. Aide à la recherche, pas un conseil juridique. Fait partie de la bibliothèque open source « Skills for International Justice » — méthodologie : github.com/jeannesulzer/international-criminal-tribunals-skills"
metadata:
  author: "Jeanne Sulzer"
  license: "agpl-3.0"
  version: "2026-06-10"
---

# CAE / EAC — Chambres Africaines Extraordinaires (affaire Habré)

This skill governs every output that touches the Chambres Africaines Extraordinaires au sein des juridictions sénégalaises (CAE) — known in English as the Extraordinary African Chambers in the Courts of Senegal (EAC). The discipline is simple and the reason for it is concrete: the EAC tried one person — Hissène Habré, former President of the Republic of Chad — and produced a foundational moment in international criminal justice: the **first prosecution of an African former Head of State by African institutions for international crimes**, and the **first prosecution under universal jurisdiction in Africa to proceed to trial**. Habré's death on 24 August 2021 closed the criminal phase; the reparations phase, transferred to the African Union Trust Fund for Victims, remains substantively open.

## The discipline in one paragraph

For any case-specific document — judgment, decision, indictment, filing, civil party submission — verify before citing. "Verify" means `web_fetch` (or equivalent retrieval) to the **EAC archives** (the historical domain `chambresafricaines.org` is intermittently unavailable; the mirror `forumchambresafricaines.org` and the ICC Legal Tools Database remain reliable Tier 1 sources) in the current conversation. Foundational texts in project knowledge (Accord UA-Sénégal 2012, Statut des CAE) are the exception; they may be cited directly. Nothing else.

## Verification is gradient, not binary

The EAC's documentary corpus is **finite and well-mapped** — only one accused, four key decisions, a defined civil party register. Three levels:

- **Existence verified.** Decision title, date, chamber confirmed against an authoritative source.
- **Content verified.** The fetched text confirms the proposition in substance.
- **Paragraph verified.** The specific cited paragraph or page contains the cited proposition.

Label the level where relevant. The EAC decisions are voluminous (the Trial Judgment of 30 May 2016 exceeds 600 pages); use page references where paragraph numbers are not authoritative.

## Standard workflow

**Step 0 — Identify the document.** Before anything else, distinguish:

- The **Trial Judgment of 30 May 2016** (Ministère Public v. Hissein Habré, Chambre Africaine Extraordinaire d'Assises) — the criminal judgment on the merits
- The **Reparations Decision of 29 July 2016** (Décision sur les Réparations Civiles, Chambre Africaine Extraordinaire d'Assises) — the first instance civil/reparations decision, often appended to the Trial Judgment
- The **Appeals Judgment of 27 April 2017** (Procureur Général v. Hissein Habré, Chambre Africaine Extraordinaire d'Assises d'Appel) — the final criminal and civil judgment, which confirmed conviction but acquitted on one direct rape count and fixed total reparations at 82.290 billion CFA francs
- **Investigative phase decisions** (Chambre Africaine Extraordinaire d'Instruction) — indictment of 13 February 2015, decisions on protective measures over Habré's assets
- The **antecedent jurisprudence** that conditioned the EAC's creation: ECOWAS Court judgment of 18 November 2010 (*Habré v. Senegal*), ICJ judgment of 20 July 2012 (*Belgium v. Senegal*)

**Step 1 — Plan citations.** List every citation that will appear and the proposition each supports. Distinguish criminal and civil dispositions.

**Step 2 — Verify with the fallback ladder.** EAC archive (forumchambresafricaines.org) → legal-tools.org → African Union legal portal (au.int) → HRW Habré case page (Tier 1 for procedural milestones given Reed Brody's central documentary role) → academic commentary (Tier 2) → ask the user.

**Step 3 — Draft using verified material.** Use the citation format in `references/citation-format.md`. Where verification is partial, say so.

**Step 4 — Self-audit.** Each citation must trace to project knowledge or to a successful retrieval in this conversation.

## Foundational texts (cite from project knowledge when present)

- **Accord entre le Gouvernement de la République du Sénégal et l'Union africaine sur la création de Chambres africaines extraordinaires au sein des juridictions sénégalaises** — signed 22 August 2012 at Dakar. The bilateral establishing instrument between the African Union and Senegal.
- **Statut des Chambres africaines extraordinaires** — annexed to the Accord. The operative substantive and procedural framework. Key articles:
  - Art. 3 — Compétence ratione temporis (**7 June 1982 to 1 December 1990**), ratione loci (crimes committed in Chad), ratione personae ("le ou les principaux responsables")
  - Art. 4-7 — Compétence ratione materiae (genocide, crimes against humanity, war crimes, torture)
  - Art. 8 — Modes of individual criminal responsibility (commission, ordering, planning, instigating, aiding and abetting, joint criminal enterprise, command/superior responsibility)
  - Art. 9 — Immunities — explicit exclusion of immunity (including for heads of State)
  - Art. 10 — Statute of limitations (non-applicable to international crimes)
  - Arts. 11-12 — Composition: judges nominated by Senegal, formally appointed by the African Union Commission
  - Arts. 14-16 — Investigative, Trial, and Appeals Chambers
  - Arts. 27-28 — Reparations to victims; Trust Fund
- **Code de procédure pénale sénégalais** and **Code pénal sénégalais** — applicable supplementarily where not displaced by the Accord and the Statute
- **Loi n° 2007-05 du 12 février 2007** modifying the Senegalese Penal Code to incorporate international crimes (genocide, crimes against humanity, war crimes)
- **Loi n° 2007-04 du 12 février 2007** establishing extraterritorial jurisdiction of Senegalese courts over international crimes
- **Antecedent regional instruments:**
  - ICJ judgment, *Questions concerning the Obligation to Prosecute or Extradite (Belgium v. Senegal)*, 20 July 2012 (*aut dedere, aut judicare* under Article 7 of the Convention against Torture)
  - ECOWAS Court of Justice judgment, *Hissène Habré v. Republic of Senegal*, ECW/CCJ/JUD/06/10, 18 November 2010 — held that any prosecution of Habré must take place before an ad hoc court of an "international character" given the non-retroactivity issues with the 2007 Senegalese legislation

If not in project knowledge, retrieve from forumchambresafricaines.org or legal-tools.org.

## The institutional architecture (get this right)

- **Established by:** Accord between the African Union and the Republic of Senegal of **22 August 2012**.
- **Operational:** **8 February 2013 – 27 April 2017**.
- **Seat:** Dakar, Senegal (within the Palais de Justice of Dakar; the EAC operated as chambers integrated into the Senegalese judicial system).
- **Composition:** Hybrid Senegalese-African — Senegalese judges nominated by Senegal and formally appointed by the African Union Commission, with the President of the Trial Chamber and the President of the Appeals Chamber being non-Senegalese African nationals appointed by the African Union (the Trial Chamber was presided over by Judge Gberdao Gustave Kam of Burkina Faso).
- **Investigative phase:** Chambre Africaine Extraordinaire d'Instruction. Habré arrested 30 June 2013; indictment confirmed 13 February 2015.
- **Trial:** Chambre Africaine Extraordinaire d'Assises. Trial commenced 20 July 2015; closing statements February 2016; judgment 30 May 2016.
- **Appeals:** Chambre Africaine Extraordinaire d'Assises d'Appel. Hearings 9-12 January 2017; judgment 27 April 2017.
- **Closure:** the EAC concluded its mandate on 27 April 2017 and was dissolved shortly thereafter. Residual functions (reparations execution) transferred to the African Union Trust Fund for Victims.
- **Distinguishing features:**
  - **The first prosecution under universal jurisdiction in Africa to proceed to trial**
  - **The first prosecution of a former African Head of State by African institutions** for international crimes
  - **Hybrid model uniquely African** — created by accord between the AU and a single African State, with judges appointed by the AU, applying both Senegalese and international law
  - **One accused** — Hissène Habré alone (six co-accused were initially indicted at the EAC but proceedings against them were not pursued at the EAC; some were tried before Chadian courts in 2015)
  - **Universal jurisdiction with treaty anchoring** — the EAC's jurisdiction is grounded in Senegal's *aut dedere aut judicare* obligations under the Convention against Torture (confirmed by the ICJ in *Belgium v. Senegal*)
  - **Substantial reparations award** — 82.290 billion CFA francs (approximately 125 million EUR / 145 million USD) to 7,396 named civil parties, the largest amount of reparations ever awarded by an international(ised) criminal tribunal at the time of issuance

## Source hierarchy

**Tier 1 (authoritative):**
- **forumchambresafricaines.org** — Forum des Chambres Africaines Extraordinaires, the principal mirror archive for EAC decisions, transcripts and procedural records. Hosts the Trial Judgment of 30 May 2016, the Reparations Decision of 29 July 2016, and the Appeals Judgment of 27 April 2017
- **chambresafricaines.org** — the historical official EAC website. Intermittently available; check both
- **legal-tools.org** — ICC Legal Tools Database, hosts the Statut and principal decisions
- **au.int** — African Union legal portal, for the Accord of 22 August 2012 and Trust Fund documents
- **ICJ archives** (icj-cij.org) — for *Belgium v. Senegal* (2012)
- **ECOWAS Court archives** — for *Habré v. Senegal* (ECW/CCJ/JUD/06/10, 2010)

**Tier 2 (secondary, must be labelled):**
- **Human Rights Watch** (hrw.org/habre-case) — Reed Brody's near-complete documentary archive of the Habré case; Tier 1 in practice for procedural milestones given Brody's central role as civil party counsel and investigator over three decades
- **Amnesty International** — extensive coverage; particularly *Chad: Hissène Habré appeal ruling closes dark chapter for victims* (28 April 2017)
- **REDRESS** — amicus curiae brief on reparations (February 2017); analytical work on the Trust Fund
- **Sarah Williams** — *The Extraordinary African Chambers in the Senegalese Courts: An African Solution to an African Problem?*, JICJ 11 (2013) 1139 — the principal scholarly treatment of the institutional design
- **Naomi Roht-Arriaza** — comparative work on universal jurisdiction
- *The President on Trial: Prosecuting Hissène Habré* (Oxford University Press 2020) — Sharon Williams and Sharan Srinivasan (eds.) — the standard scholarly volume
- **Oxford Public International Law** entry "Extraordinary African Chambers" (opil.ouplaw.com)
- **Nordic Journal of Human Rights**, vol. 34 no. 3 (2016) — special issue on the Habré case
- **Journal of African Law** (Cambridge UP) — Diab and others on reparations practice
- **ATPDH** (Association Tchadienne pour la Promotion et la Défense des Droits de l'Homme) — civil party organisation led by Jacqueline Moudeina
- **JusticeInfo.net** — coverage of trial and post-trial reparations execution

**Never authoritative:** Wikipedia, Grokipedia, social media, AI-generated summaries.

See `references/authoritative-sources.md`.

## Citation format

EAC citations follow Senegalese civil-law conventions adapted to a hybrid context. Two pieces matter:

1. **The case designation** — the criminal proceedings are *Ministère Public v. Hissein Habré* at first instance; *Procureur Général v. Hissein Habré* on appeal. The civil dimension is captured in the Décision sur les Réparations Civiles, which lists civil parties (the lead case for civil parties is often referenced as *Clément Abaïfouta and 6,999 Others*, after the lead civil party).

2. **The chamber designation:**
   - **Chambre Africaine Extraordinaire d'Instruction** (Investigative Chamber)
   - **Chambre Africaine Extraordinaire d'Assises** (Trial Chamber)
   - **Chambre Africaine Extraordinaire d'Assises d'Appel** (Appeals Chamber)

**Worked examples:**

- *Ministère Public v. Hissein Habré*, Chambre Africaine Extraordinaire d'Assises, Jugement, 30 May 2016.
- *Ministère Public v. Hissein Habré*, Chambre Africaine Extraordinaire d'Assises, Décision sur les Réparations Civiles, 29 July 2016.
- *Procureur Général v. Hissein Habré*, Chambre Africaine Extraordinaire d'Assises d'Appel, Arrêt, 27 April 2017.

See `references/citation-format.md` for the full convention.

## Audit mode depends on document type

When the user supplies a document:
- **Working drafts**: audit citations for accuracy.
- **Final EAC records**: inventory and spot-check; the EAC corpus is small enough that comprehensive review is feasible.

In either mode, Step 0 (identify the document and the chamber) comes first. The most common confusion is between the Trial Judgment (30 May 2016) and the Appeals Judgment (27 April 2017); the substantive holdings differ on at least one important count (rape direct commission).

## Substantive doctrine — pointers

The skill does not encode doctrine line by line. Starting points:

- **Universal jurisdiction grounded in treaty obligations** → Convention against Torture Art. 7 (*aut dedere aut judicare*); ICJ *Belgium v. Senegal* of 20 July 2012 confirming Senegal's obligation
- **Material competence** → genocide, crimes against humanity, war crimes, torture (Statute Arts. 4-7)
- **Temporal competence — strictly bounded** → 7 June 1982 to 1 December 1990 (the Habré presidency)
- **Personal competence** → the "person or persons most responsible" — in practice, Habré alone before the EAC
- **Modes of liability** → the EAC applied an unusual construction of **command/superior responsibility** and **joint criminal enterprise** adapted to the specific factual configuration of an authoritarian state (the DDS — Direction de la Documentation et de la Sécurité — was Habré's secret police, the principal instrument of repression). Sarah Williams (n 6 above) and the *Journal of International Criminal Justice* coverage discuss the doctrinal innovations
- **No immunity for heads of State** → Statute Art. 9; consistent with customary international law and with the ICJ's framework in *Belgium v. Senegal*
- **Civil parties (parties civiles)** → robust civil party participation following the Senegalese civil-law tradition; civil parties represented by Senegalese, Chadian and international counsel (Jacqueline Moudeina as lead Chadian counsel; Reed Brody as principal investigator and advocate); 7,396 named civil parties accredited
- **Reparations** → Statute Arts. 27-28; Trial Chamber decision of 29 July 2016 set individual reparations by category (rape and sexual violence victims: 20 million CFA francs each ≈ USD 33,880; arbitrary detention, torture, prisoners of war and survivors: 15 million CFA francs each ≈ USD 25,410; indirect victims: 10 million CFA francs each ≈ USD 16,935); Appeals Chamber of 27 April 2017 confirmed the framework and set the total at **82,290 billion CFA francs** for 7,396 victims; Trust Fund for Victims under African Union management was tasked with execution

For each, verify the specific decision through the workflow.

## Sensitive contexts

The Habré regime (1982-1990) is characterised in the EAC judgments as having killed approximately **40,000 victims** through systematic killings, mass torture, sexual violence, and the activities of the DDS secret police. The Chambres' findings are now historically authoritative. Civil parties include rape and sexual violence survivors whose courage in testifying — particularly the women of the Centre-Sud region — was foundational to the judgment.

Habré died on **24 August 2021**, which legally extinguishes the criminal proceedings against him personally but does not affect the validity of the EAC's judgments or the obligation of the African Union Trust Fund to execute reparations. As of 2026, the Trust Fund's operational status remains a major concern: only minimal assets have been recovered and reparations have not yet been substantially disbursed. Treat the reparations question with attention to both the doctrinal achievement and the practical disappointment.

Habré's defence team contested the EAC's legitimacy throughout the proceedings (questioning the Senegalese ratione temporis, the Senegalese 2007 legislation's non-retroactivity, and the AU's institutional role). Habré refused to recognise the court, did not attend the opening of the trial (which proceeded after appointment of court-appointed counsel), and never accepted the proceedings. These defence arguments are documented in the procedural record; they do not affect the substantive validity of the judgments but they are part of the institutional history.

## What this skill is not

- Not legal advice. Outputs are research and drafting aids.
- Not a substitute for the EAC's records.
- Not endorsed by the EAC, the African Union, the Republic of Senegal, or the Republic of Chad.
- Not a position on the contested doctrinal questions raised by the EAC's case law (notably the construction of JCE and command responsibility for an entire State apparatus over an 8-year period). The skill enables accurate citation of the EAC's findings; the academic debate is left to the user.

## Reference files

- `references/authoritative-sources.md` — source hierarchy and URLs
- `references/citation-format.md` — case-name conventions, chamber designations, worked examples
- `references/verification-workflow.md` — fallback ladder, EAC-specific traps
- `references/foundational-texts.md` — Accord UA-Sénégal 2012, Statut des CAE, ICJ *Belgium v. Senegal*, ECOWAS Court *Habré v. Senegal*
- `references/jurisprudence-map.md` — topic-by-topic map of EAC holdings
- `examples/example-verification.md` — verifying one EAC citation end-to-end
- `examples/example-audit.md` — auditing user-supplied documents
