---
name: "cps-rca-central-african-republic-jeanne-sulzer"
description: "Méthodologie « verification-first » pour la Cour Pénale Spéciale de Centrafrique (cour hybride, siège à Bangui). Toute citation est vérifiée (JusticeInfo, FIDH, HRW, legal-tools.org ; les sites officiels renvoient souvent une erreur 403). Couvre l'affaire Paoua, le « notamment » de l'article 3, et la complémentarité avec la CPI. Aide à la recherche, pas un conseil juridique. Fait partie de la bibliothèque open source « Skills for International Justice » — méthodologie : github.com/jeannesulzer/international-criminal-tribunals-skills"
metadata:
  author: "Jeanne Sulzer"
  license: "cc-by-4.0"
  version: "2026-06-10"
---

# CPS — Cour Pénale Spéciale de la République Centrafricaine

This skill governs every output that touches the Cour Pénale Spéciale de la République Centrafricaine (CPS) — the Special Criminal Court in the Central African Republic. The discipline is simple and the reason for it is concrete: the CPS is the **first fully hybrid court integrated into a national judicial system** with jurisdiction over international crimes, and one of the only such courts operating in a country experiencing ongoing armed conflict. Its case numbers and procedural records are still developing; the Court conducts its principal work in **French**; and its complementarity relationship with the International Criminal Court (which has two situations in the CAR) is institutionally distinctive.

## The discipline in one paragraph

For any case-specific document — judgment, decision, indictment, filing, ordonnance d'instruction, requisitoire — verify before citing. "Verify" means `web_fetch` (or equivalent retrieval) to **cpsrca.cf** (the official CPS website) in the current conversation. Foundational texts in project knowledge (Loi organique 15.003, Loi 18.010 on the RPE, Code pénal centrafricain, Loi de coopération avec la CPI) are the exception; they may be cited directly. Nothing else.

## Verification is gradient, not binary

In practice, cpsrca.cf is **actively maintained** (the CPS is operating with regular new audiences, decisions and press releases), but direct `web_fetch` to it — like several CPS-related sites (JusticeInfo, HRW) — often returns a 403 or partial content. Treat that as expected and work the fallback ladder (legal-tools.org, MINUSCA, JusticeInfo, RJDH, Radio Ndeke Luka) rather than as a dead end. Three levels:

- **Existence verified.** Affair, document type, date, chamber confirmed.
- **Content verified.** The fetched text confirms the proposition in substance.
- **Paragraph verified.** The specific cited paragraph contains the cited proposition.

Label the level where relevant. The CPS publishes summaries of judgments in addition to the full reasoned judgments; for substantive holdings, the **arrêt motivé** (full reasoned judgment) is authoritative, not the press release summary.

## Standard workflow

**Step 0 — Identify the document.** Before anything else, distinguish:
- The **affair** (l'affaire Paoua / Lemouna et Koundjili; l'affaire Ndélé 1; l'affaire Ndélé 1 contumace; subsequent cases)
- The **chamber** — **Chambre d'instruction** (investigation), **Chambre d'assises** (trial), **Chambre d'appel** (appeal), **Chambre de cassation** (cassation, where applicable)
- The **document type** — Ordonnance, Réquisitoire, Acte d'accusation, Jugement de la Chambre d'assises, Arrêt de la Chambre d'appel, Décision sur les intérêts civils

**Step 1 — Plan citations.** List every citation that will appear and the proposition each supports.

**Step 2 — Verify with the fallback ladder.** cpsrca.cf → JusticeInfo.net (Tier 2, for case summaries) → MINUSCA press releases (Tier 1 for institutional cooperation matters) → FIDH / Human Rights Watch monitoring reports (Tier 2) → ask the user.

**Step 3 — Draft using verified material.** Use the citation format in `references/citation-format.md`.

**Step 4 — Self-audit.** Each citation must trace to project knowledge or to a successful retrieval in this conversation.

## Foundational texts (cite from project knowledge when present)

- **Loi organique n°15.003 du 3 juin 2015** portant création, organisation et fonctionnement de la Cour pénale spéciale (adopted by the Conseil national de transition on 22 April 2015; promulgated by interim President Catherine Samba-Panza on 3 June 2015) — the constitutive instrument. Key articles:
  - Art. 1 — Création de la CPS
  - **Art. 3 — Compétence matérielle** ("les violations graves des droits humains et du droit international humanitaire … **notamment** le crime de génocide, les crimes contre l'humanité et les crimes de guerre" committed in CAR territory **since 1 January 2003**). The statutory "notamment" is load-bearing — see `references/foundational-texts.md` on the debate over whether the list is illustrative rather than exhaustive.
  - Art. 4 — Compétence personnelle
  - Art. 5 — Compétence concurrente (with national courts; CPS has primacy)
  - Art. 6 — Complémentarité avec la CPI (the CPS is **not** a strict subordinate of the ICC, but its competence yields where the ICC has commenced proceedings)
  - Art. 7-12 — Composition (13 national + 12 international magistrates)
  - Art. 14-15 — Procureur spécial et Bureau du Procureur spécial
  - Arts. 19-25 — Structure des chambres (Chambre d'instruction, Chambre d'assises, Chambre d'appel)
  - Arts. 39-47 — Droits de la défense, victimes, témoins
  - Arts. 51-52 — Coopération internationale
  - Durée — 5 ans renouvelables (renewed)
- **Loi n°18.010 du 2 juillet 2018** portant Règlement de procédure et de preuve de la Cour pénale spéciale ("Règlement de procédure et de preuve" / "RPP") — the procedural and evidentiary framework. **Distinctively a *Law***, not a court-adopted rule (unlike RPE at most international tribunals).
- **Code pénal centrafricain** (Loi n°10.001 of 6 January 2010) — incorporates definitions of international crimes into Central African domestic law; affirms imprescriptibility of international crimes, no immunity, no amnesty/grâce for international crimes. **The substantive criminal law applied by the CPS is the Central African Penal Code**, with reference to international law where necessary.
- **Code de procédure pénale centrafricain** — where not displaced by the Loi organique 15.003 and the RPP.
- **Mémorandum d'accord entre le Gouvernement centrafricain et la MINUSCA** (August 2014) — the institutional foundation for UN cooperation with the CPS, signed before the Loi organique was adopted.

If not in project knowledge, retrieve from cpsrca.cf/documentations/textes-juridiques.

## The institutional architecture (get this right)

- **Established by:** Loi organique n°15.003 (22 April 2015 / 3 June 2015 promulgation).
- **Inaugural session:** **22 October 2018**, marking the beginning of judicial activity.
- **Seat:** Bangui, Central African Republic (the CPS sits within the CAR national judicial system; the Court house is in Bangui).
- **Composition:** 25 magistrates total — **13 national magistrates** (Central African) and **12 international magistrates** (from various jurisdictions). The President and Vice-President alternate between national and international; the Procureur spécial is international (the inaugural Special Prosecutor, Mr. Toussaint Muntazini Mukimapa, originally from DRC, was appointed in 2017 and held the post until his death on 25 March 2026; verify the current appointment before citing).
- **Funding and support:** primarily from the **MINUSCA** (UN Multidimensional Integrated Stabilization Mission in CAR) and from the EU, US, France, the Netherlands and others.
- **Operations:** **Actively operating** as of 2026 with regular hearings.
- **Distinguishing features:**
  - **Integrated into the Central African national judicial system** — not a freestanding court; the CPS is part of the Central African judiciary, with its own special procedures
  - **Applies Central African substantive criminal law** (Code pénal centrafricain) and Central African criminal procedure (subject to the Loi organique 15.003 and the RPP) — supplemented by international law
  - **Operates in French** — the principal working and procedural language (with Sango interpretation for witnesses)
  - **Complementarity with the ICC** — the CPS coordinates with ICC's CAR Situation I (referral by CAR 22 December 2004, opened 22 May 2007; produced *Bemba* case at the ICC) and CAR Situation II (referral 30 May 2014, opened 24 September 2014; produced *Yekatom & Ngaïssona* and *Said* cases)
  - **Civil parties (parties civiles)** — civil party participation following the Central African civil-law tradition (distinct from the ICC's victim participation model and from common-law victim-witness frameworks)
  - **Trial in absentia (contumace)** — explicitly authorised; used in *Ndélé contumace*

## Source hierarchy

**Tier 1 (authoritative):**
- **cpsrca.cf** — the official CPS website. Hosts the Loi organique 15.003, the RPP (Loi 18.010), the Code pénal centrafricain, press releases, audience announcements, judgment summaries, and updates on cases. Actively maintained.
- **legal-tools.org** — ICC Legal Tools Database. Holds the Loi organique 15.003 and the RPP and selected CPS decisions
- **MINUSCA press releases** (`minusca.unmissions.org`) — institutional cooperation; some judgment announcements
- **un.org/securitycouncil** — for MINUSCA mandate renewals (UNSC Res. 2149 (2014) and successors) that include support for the CPS

**Tier 2 (secondary, must be labelled):**
- **JusticeInfo.net** — French and English coverage of CPS proceedings; high-quality trial monitoring
- **FIDH (Fédération internationale des droits humains)** and **OCDH (Organisation centrafricaine pour les droits de l'homme)** — civil society monitoring
- **Human Rights Watch** — extensive reporting on CAR conflict and on the CPS (notably the 2018 "En quête de justice" report)
- **Radio Ndeke Luka** — Central African press, local reporting
- **Oubangui Médias** — Central African press
- **Academic commentary** — Damien Scalia, Mark Kersten, Linda M. Keller, Patryk I. Labuda, Olivier Beauvallet (CPS appeal judge), Volker Nerlich (CPS appeal judge) — work on hybrid jurisdictions
- **Cairn.info** — French-language academic articles on the CPS
- **violences-sexuelles.ifjd.org** — IFJD (Institut Francophone pour la Justice et la Démocratie) — reference materials on CAR sexual violence prosecutions

**Never authoritative:** Wikipedia, Grokipedia, social media, AI summaries.

## Citation format

CPS citations differ from international tribunal citations. Cases are referred to by **name of the affair** (not by case number in the international-tribunal sense) and **chamber**. The citation format follows French/Central African judicial conventions:

**General form:**
> *Procureur spécial contre [Defendant(s)]*, [name of the affair], Chambre [chamber], [Document type], [Date].

**Worked examples:**

- *Procureur spécial contre Issa Sallet Adoum, Yaouba Ousman et Mahamat Tahir*, **Affaire Paoua / Lemouna et Koundjili**, Chambre d'assises, Jugement du **31 octobre 2022**.
- *Procureur spécial contre Issa Sallet Adoum, Yaouba Ousman et Mahamat Tahir*, **Affaire Paoua**, Chambre d'appel, Arrêt du **20 juillet 2023** [sentence reduced; Issa Sallet Adoum sentenced to 30 years].
- *Procureur spécial contre [accusés]*, **Affaire Ndélé 1**, Chambre d'assises, [Jugement / Décision] du [date].

See `references/citation-format.md` for the convention.

## Audit mode depends on document type

- **Working drafts**: audit citations for accuracy.
- **Final CPS records**: identify the case (l'affaire), the chamber, the document type, the date.

In either mode, Step 0 (identify the document and the affair) comes first. **CPS proceedings move quickly between chambers** (Chambre d'instruction → Chambre d'assises → Chambre d'appel) and the same defendants appear in multiple decisions across the proceedings — Step 0 prevents conflation.

## Substantive doctrine — pointers

The skill does not encode doctrine line by line. Starting points (each verified through the workflow before citing):

- **Material jurisdiction (compétence matérielle)** → Loi organique 15.003 Art. 3: violations graves des droits humains et du droit international humanitaire, including genocide, crimes against humanity, war crimes, **as defined by the Central African Penal Code and by international law**.
- **Temporal jurisdiction** → Art. 3: crimes committed **since 1 January 2003** (open-ended, ongoing — distinctive among hybrid tribunals).
- **Complementarity with the ICC** → Art. 6: the CPS's competence yields where the ICC has commenced proceedings (in practice, the Bemba case at the ICC was a CAR Situation I prosecution; the CPS does not duplicate ICC active cases).
- **Modes of individual criminal responsibility** → Code pénal centrafricain (auteur, co-auteur, complice; co-perpetration; superior responsibility for military commanders).
- **Crimes against humanity for sexual violence (rape)** → applied in the *Paoua* trial judgment, including a **command-responsibility conviction** for Issa Sallet Adoum for rapes committed by his subordinates.
- **Civil parties (parties civiles)** → the *Paoua* case included an *audience sur les intérêts civils* (civil-interests hearing) — distinctive of civil-law victim participation. Compare and contrast with ICC reparations and STL victim participation.
- **Trial in absentia (contumace)** → used in *Ndélé 1 contumace*; Central African procedure permits in absentia trial with retrial on subsequent arrest, similar in structure to STL Art. 22 but rooted in the civil-law inheritance.
- **Imprescriptibility of international crimes** → Code pénal centrafricain (2010) affirms imprescriptibility; the CPS applies it consistently.

For each, verify through the workflow.

## Sensitive contexts

The CAR conflict (2003 to the present, with successive waves) involves Christian/animist (anti-balaka) and Muslim (Seleka, ex-Seleka, 3R, MPC, FPRC, UPC) armed groups, with extreme violence against civilians, sexual violence on a massive scale, displacement of about a fifth of the population, and ongoing fragility. The accused before the CPS are often members of armed groups still active or recently active. Witness protection is a major operational challenge. Victims and survivors are frequently in close proximity to perpetrators. Maintain factual precision, avoid sensationalism, use the language the Court itself uses (typically "groupe armé" rather than ethnic or religious shorthand), and never minimise. The Bangui Forum (2015) was a Central African national reconciliation process — referencing it as the political-institutional foundation of the CPS is appropriate.

## What this skill is not

- Not legal advice. Outputs are research and drafting aids.
- Not a substitute for the CPS's records.
- Not endorsed by the CPS, the CAR government, or the UN.
- Not exhaustive: the CPS publishes regularly; new affairs appear continually. Verify current state of any case.

## Reference files

- `references/authoritative-sources.md` — source hierarchy and URLs (cpsrca.cf, JusticeInfo, MINUSCA, FIDH/OCDH)
- `references/citation-format.md` — citation conventions, named cases ("Affaire Paoua / Lemouna et Koundjili", "Affaire Ndélé 1", "Affaire Ndélé 1 contumace"), chamber designations
- `references/verification-workflow.md` — fallback ladder, CPS-specific traps (national court vs international tribunal; CPS vs ICC; French as principal language; civil parties vs ICC victim participation; Affaire Paoua trial vs appeal sentence discrepancy; trial in absentia retrial right)
- `references/foundational-texts.md` — Loi organique 15.003, RPP (Loi 18.010), Code pénal centrafricain, MINUSCA cooperation MoU
- `references/jurisprudence-map.md` — topic-by-topic map of CPS holdings (small but growing as of 2026)
- `examples/example-verification.md` — verifying a Paoua case citation end-to-end
- `examples/example-audit.md` — auditing user-supplied documents (Paoua trial vs appeal sentence; CPS misnomers)
