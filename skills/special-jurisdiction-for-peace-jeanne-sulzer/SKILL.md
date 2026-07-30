---
name: "jep-jeanne-sulzer"
description: "Verification-first methodology for the Jurisdicción Especial para la Paz (JEP), Colombia's transitional justice court under the 2016 Acuerdo Final with FARC-EP. Citations are verified against jep.gov.co before use. Covers the 11 macrocasos (from Caso 01 secuestro through Caso 11 violencia sexual, including Caso 03 falsos positivos), the three sanction tiers (propias, alternativas, ordinarias), TOAR, and the SIVJRNR sister bodies (CEV, UBPD). Guards the key structural distinctions (Sala de Reconocimiento vs Tribunal para la Paz; comparecientes FARC-EP vs Fuerza Pública vs terceros civiles; Acto Legislativo 01/2017 vs Ley Estatutaria 1957/2019). Research aid, not legal advice."
metadata:
  author: "Jeanne Sulzer"
  license: "cc-by-4.0"
  version: "2026-07-04"
---

# JEP — Jurisdicción Especial para la Paz (Colombia)

This skill governs every output that touches the Jurisdicción Especial para la Paz (JEP) — the Special Jurisdiction for Peace, the judicial component of Colombia's transitional justice system established by the **24 November 2016 Final Peace Agreement** between the Government of Colombia and the FARC-EP. The discipline is simple and the reason for it is concrete: the JEP applies a distinctive restorative-justice model — it issued its **first sentences in September 2025** applying *sanciones propias* (restorative non-custodial sanctions) for the gravest crimes of an internal armed conflict that lasted more than fifty years. Its procedure mixes Colombian civil-law structure, international criminal law standards, and a uniquely restorative-justice approach. Citation discipline matters acutely.

## The discipline in one paragraph

For any case-specific document — auto, providencia, resolución, sentencia, lineamiento — verify before citing. "Verify" means `web_fetch` (or equivalent retrieval) to **jep.gov.co** (the official JEP website) in the current conversation. Foundational texts in project knowledge (Acuerdo Final, Acto Legislativo 01 of 2017, Ley Estatutaria 1957 of 2019, Reglamento General) are the exception; they may be cited directly. Nothing else.

## Verification is gradient, not binary

The JEP publishes extensively and the website is **actively maintained**, so jep.gov.co is the right first stop. But do not treat a successful fetch as guaranteed: direct retrieval can fail — an HTTP 403, a timeout, or a PDF that will not render — and that failure is **structural, not a dead end**. When it happens, walk the fallback ladder in `references/verification-workflow.md` rather than abandoning verification or citing from memory. Three levels:

- **Existence verified.** Macrocaso, document type, date, organ confirmed.
- **Content verified.** The fetched text confirms the proposition in substance.
- **Paragraph verified.** The specific cited paragraph or section contains the cited proposition. JEP sentences and autos are voluminous (the two September 2025 sentences total over 1,247 pages between them) and contain numbered sections rather than the international-tribunal-style paragraph numbering. Verify by section and page where paragraph numbers are not available.

Label the level where relevant.

## Standard workflow

**Step 0 — Identify the document.** Before anything else, distinguish:
- The **macrocaso** (Casos 01 to 11 — see citation format below)
- The **organ** that issued the document:
  - **Salas de Justicia** — three Salas: **Sala de Reconocimiento de Verdad y Responsabilidad y de Determinación de los Hechos y Conductas** (SRVR or "Sala de Reconocimiento"); **Sala de Amnistía o Indulto** (SAI); **Sala de Definición de Situaciones Jurídicas** (SDSJ)
  - **Tribunal Especial para la Paz** — the trial-level court (with four "Secciones": **Sección de Reconocimiento de Verdad y Responsabilidad**, **Sección de Ausencia de Reconocimiento de Verdad y Responsabilidad**, **Sección de Apelaciones**, plus the **Sección de Revisión de Sentencias**)
  - **Unidad de Investigación y Acusación (UIA)** — the prosecutorial unit
  - The **Plenary** (Sala Plena) — for administrative and general matters
- The **document type** — Auto (procedural), Providencia (interim), Resolución (administrative), Sentencia (judgment), Lineamiento (guideline)
- **Comparecientes** type — **FARC-EP** (former combatants), **Fuerza Pública** (military and police), or **terceros civiles** (third-party civilians, including paramilitary, businesspeople, financiers)
- **The September 2025 sentences are the JEP's first** — and a watershed moment for the institution

**Step 1 — Plan citations.** List every citation that will appear and the proposition it supports.

**Step 2 — Verify with the fallback ladder.** jep.gov.co → UN Verification Mission in Colombia (`colombia.unmissions.org`) → Tier 2 academic / monitoring sources clearly labelled → ask the user.

**Step 3 — Draft using verified material.** Use the citation format in `references/citation-format.md`.

**Step 4 — Self-audit.** Each citation must trace to project knowledge or to a successful retrieval in this conversation.

## Foundational texts (cite from project knowledge when present)

- **Acuerdo Final para la Terminación del Conflicto y la Construcción de una Paz Estable y Duradera** (the Final Peace Agreement), signed at Bogotá on **24 November 2016** by the Colombian Government and the FARC-EP. **Point 5 ("Acuerdo sobre las Víctimas del Conflicto: Sistema Integral de Verdad, Justicia, Reparación y No Repetición")** is the constitutive text of the JEP, the CEV, and the UBPD. Often referred to in scholarship as the "Acuerdo Final" or "Acuerdo de Paz de 2016".
- **Acto Legislativo 01 of 2017** (constitutional amendment of 4 April 2017) — incorporated the JEP and the Sistema Integral into the Colombian Constitution. **Transitional articles 5 to 18** establish the JEP. Approved by the Senate on 14 March 2017 (60 votes for, 2 against).
- **Ley Estatutaria 1957 of 6 June 2019** — the **Estatutaria de la JEP** (Statutory Law of the JEP). Detailed framework law on JEP competence, organisation, and procedure. **Crucial**: this is the principal substantive legal framework, the most often cited foundational text.
- **Ley 1922 of 18 July 2018** — Reglas de Procedimiento de la JEP (Rules of Procedure). Procedural framework.
- **Reglamento General de la JEP** — adopted by the Sala Plena; internal organisational rules.
- **Colombian Penal Code** (Ley 599 of 2000) and **Code of Criminal Procedure** — applicable supplementarily.
- **International instruments** — Colombia is party to the **Rome Statute** (ratified 5 August 2002, with a 7-year exclusion for war crimes that expired in 2009), the four **Geneva Conventions** and **Additional Protocols I and II**, the **Convention against Torture**, the **Inter-American Convention on Forced Disappearance**, the **American Convention on Human Rights**, the **ICCPR**, and the **Genocide Convention**. The JEP applies these alongside domestic law.

If not in project knowledge, retrieve from jep.gov.co (Documentos / Marco Normativo).

## The institutional architecture (get this right)

- **Established by:** the Acuerdo Final (2016), constitutionalised by Acto Legislativo 01 of 2017, framework law in Ley Estatutaria 1957 of 2019.
- **Seat:** Bogotá, Colombia.
- **Operations:** judicial activity since **15 March 2018** (formal launch); first comparecencias (appearances) of FARC-EP leaders in 2018; **first sentences on 16 and 18 September 2025** in Caso 01 (FARC secuestros) and Caso 03 (falsos positivos in the Costa Caribe).
- **Composition:** 38 Magistrados (judges) plus alternates; the Magistrados are Colombian; the JEP also has internationally-trained foreign experts (Amici Curiae and Expertos Extranjeros) that may participate in specific functions. President as of 2024-2026: **Alejandro Ramelli Arteaga** (elected October 2024 for a two-year term).
- **Distinguishing features:**
  - **Restorative justice as principal model** — *sanciones propias* (restorative non-custodial sanctions of 5-8 years for those who recognise responsibility) ; *sanciones alternativas* (alternative sanctions, 5-8 years of effective restriction of liberty, for late recognition) ; *sanciones ordinarias* (ordinary criminal sanctions, up to 20 years of imprisonment, for non-recognition)
  - **TOAR** — *Trabajos, Obras y Actividades con contenido Reparador y Restaurador* — concrete reparative activities undertaken by comparecientes (mine clearance, environmental restoration, infrastructure for victims, search for the disappeared)
  - **Régimen de condicionalidad** — the conditionality regime: benefits (sanciones propias, reduced sentences) conditional on full truth, reparation, and non-repetition
  - **11 macrocasos** by thematic and territorial categories
  - **Civil-law procedure** with substantial Colombian-tradition features (autos, providencias, sentencias)
  - **Comparecientes are both FARC-EP combatants and Fuerza Pública** (the JEP has jurisdiction over both sides of the conflict, plus civilian third parties)
  - **Integrated within the SIVJRNR** alongside the CEV (Truth Commission, concluded 2022) and the UBPD (search for disappeared, ongoing)

## Source hierarchy

**Tier 1 (authoritative):**
- **jep.gov.co** — the official JEP website. Hosts the Acuerdo Final, the Acto Legislativo 01, Ley Estatutaria 1957, Ley 1922, Reglamento General, all macrocaso pages, autos, sentencias, comunicados de prensa, audiencias. Actively maintained.
- **legal-tools.org** — selectively mirrors JEP foundational texts
- **CEV / Comisión de la Verdad** (`comisiondelaverdad.co`) — the Truth Commission's final report (June 2022) — Tier 1 for truth-and-historical-record findings, but not the JEP's own judicial record
- **UBPD** (`ubpdbusquedadesaparecidos.co`) — for matters related to the search for the disappeared
- **Colombian Constitutional Court** (`corteconstitucional.gov.co`) — for constitutional rulings affecting the JEP (notably the Sentencia C-080 of 2018 and subsequent decisions on the constitutionality of the Estatutaria)
- **UN Verification Mission in Colombia** (`colombia.unmissions.org`) — UN reporting and verification work

**Tier 2 (secondary, must be labelled):**
- **Academic commentary in Spanish** — Kai Ambos (the German expert who has worked extensively with the JEP), Manuel Iturralde, Camilo Umaña, Yesid Reyes, Rodrigo Uprimny, Mauricio García Villegas (Dejusticia)
- **Academic commentary in English** — Mark Kersten (Justice in Conflict), Jennifer Easterday, Naomi Roht-Arriaza, EJIL:Talk! analyses
- **Dejusticia** (`dejusticia.org`) — Colombian think tank; high-quality monitoring and analysis
- **Rodeemos el Diálogo** — civil society analysis
- **Colombian press** — *El Espectador*, *El Tiempo*, *Semana*, *La Silla Vacía*, *El Colombiano*, *Razón Pública* (the latter for serious legal analysis)
- **JusticeInfo.net** — international coverage
- **CINEP / Programa por la Paz** — civil society
- **Hacemos Memoria** (Universidad de Antioquia) — memory studies analysis
- **Colombia Check** — fact-checking, useful for verification of JEP statements
- **University commentary** — Universidad de los Andes (Centro de Estudios sobre Genocidio, Política y Derecho), Universidad Externado, Universidad Javeriana

**Never authoritative:** Wikipedia, Grokipedia, social media (even though the JEP has an active Twitter/X account — citing the JEP's own institutional Twitter is Tier 1 only for the specific press-release content; the substantive decisions are in the autos and sentencias).

## Citation format

JEP citations follow Colombian civil-law conventions. The citation format:

**Macrocasos:**
- Caso 01 — Toma de rehenes, graves privaciones de la libertad y otros crímenes (secuestros por las FARC-EP)
- Caso 02 — Situación territorial de Nariño
- Caso 03 — Asesinatos y desapariciones forzadas presentados como bajas en combate por agentes del Estado ("falsos positivos")
- Caso 04 — Situación territorial de Urabá
- Caso 05 — Situación territorial del Norte del Cauca y sur del Valle del Cauca
- Caso 06 — Victimización de miembros de la Unión Patriótica (UP)
- Caso 07 — Reclutamiento y utilización de niñas y niños en el conflicto armado
- Caso 08 — Crímenes cometidos por la Fuerza Pública, otros agentes del Estado o en asocio con paramilitares
- Caso 09 — Crímenes no amnistiables cometidos contra pueblos étnicos
- Caso 10 — Crímenes cometidos por las FARC-EP (no incluidos en macrocasos anteriores)
- Caso 11 — Violencia basada en género, violencia sexual y reproductiva y otros crímenes cometidos por motivos de prejuicio basados en orientación sexual o identidad de género diversa

**General form:**
> *[Compareciente(s)]*, **[Macrocaso]**, [Organ — Sala/Sección/Tribunal], [Document type], [Identifier and date].

**Worked examples:**

- **The September 2025 secuestro sentence (Caso 01):**
> Jurisdicción Especial para la Paz, Tribunal Especial para la Paz, **Sección de Reconocimiento de Verdad y Responsabilidad**, Sentencia (Caso 01 — Secuestro), **16 September 2025**.

- **The September 2025 falsos positivos sentence (Caso 03):**
> Jurisdicción Especial para la Paz, Tribunal Especial para la Paz, **Sección de Reconocimiento de Verdad y Responsabilidad**, Sentencia (Caso 03 — Subcaso Costa Caribe, Batallón La Popa, Valledupar), **18 September 2025**.

- **Constitutional ruling:**
> Corte Constitucional de Colombia, Sentencia **C-080 of 2018** (15 August 2018, M.P. Alejandro Linares Cantillo) — constitutional review of the Ley Estatutaria of the JEP.

See `references/citation-format.md` for the detailed convention.

## Audit mode depends on document type

When the user supplies a document:
- **Working drafts**: audit citations for accuracy. Macrocaso, organ, document type, date all to verify.
- **Final JEP records**: inventory and identify the procedural posture.

In either mode, Step 0 (identify the macrocaso, organ, and document type) comes first.

## Substantive doctrine — pointers

The skill does not encode doctrine line by line. Starting points (each verified through the workflow):

- **Material competence** → Ley Estatutaria 1957/2019 Art. 5: serious violations of human rights and international humanitarian law committed by reason of, on the occasion of, or in direct or indirect relation with the Colombian internal armed conflict
- **Personal competence** → comparecientes are: (i) FARC-EP former combatants; (ii) Fuerza Pública members; (iii) third-party civilians (terceros civiles) who participated directly or indirectly in the conflict — the latter via a separate procedure with consent
- **Temporal competence** → conflict-related crimes committed before **1 December 2016** (entry into force of the Acuerdo Final's transitional provisions)
- **Non-amnestiable crimes** → war crimes, crimes against humanity, genocide, hostage-taking, torture, forced disappearance, sexual violence and related conducts; recruitment of children; killings of protected persons
- **Sanciones propias** → 5-8 years of effective restriction of liberty (not prison) with TOAR, for comparecientes who fully recognise responsibility before the Sala de Reconocimiento
- **Sanciones alternativas** → 5-8 years of effective imprisonment, for late recognition before the Tribunal Especial para la Paz
- **Sanciones ordinarias** → up to 20 years of imprisonment in ordinary prison, for non-recognition (when the Sección de Ausencia de Reconocimiento finds responsibility after adversarial proceedings)
- **Régimen de condicionalidad** → benefits conditional on truth, reparation, and non-repetition; revocable on breach
- **TOAR** → restorative activities; the September 2025 sentences detail the specific TOAR programmes for the convicted (mine clearance, environmental restoration, memory projects, search for disappeared, infrastructure for victims)
- **Victim participation** → robust victim-participation framework with *víctimas acreditadas* (accredited victims); representación judicial for victims

For each, verify through the workflow.

## Sensitive contexts

The Colombian internal armed conflict, from approximately the mid-1960s to 2016, killed more than 450,000 people, displaced more than 7 million, and produced widespread atrocities by all parties: FARC-EP (kidnapping, attacks on civilians, recruitment of minors); other guerrilla groups (ELN, EPL, M-19); the Fuerza Pública (extrajudicial executions / "falsos positivos", forced disappearances, joint operations with paramilitary groups); paramilitaries (AUC, AGC, etc.); and others. The JEP's restorative-justice model — particularly the non-custodial sanciones propias for senior FARC-EP commanders responsible for 21,000 kidnappings — has been **politically contested** in Colombia. Maintain factual precision. Avoid characterising the sanciones propias as "impunity" or as "appropriate" in your own voice; reflect the contested character of the debate where relevant. Recognise that victims, FARC-EP, military, paramilitary survivors, and Colombian civil society are all reading this work. Use the JEP's own terminology (e.g. "comparecientes", "víctimas acreditadas", "sanciones propias", "TOAR"). Avoid both *Manichean* simplification and false equivalence.

The JEP issues *versiones reservadas* of many documents to protect victims, witnesses, and *comparecientes*. Cite only the public version, say so, and never reproduce reserved identifying information or attempt to identify a protected participant — the same public-record discipline the other skills in this suite apply to protected witnesses.

## What this skill is not

- Not legal advice. Outputs are research and drafting aids.
- Not a substitute for JEP records.
- Not a political evaluation of the Acuerdo Final or the JEP's institutional choices. The skill enables accurate citation of the JEP's record; political and moral evaluation is left to the user and the public debate.
- Not endorsed by the JEP, the Colombian Government, or any party to the Acuerdo Final.

## Reference files

- `references/authoritative-sources.md` — source hierarchy and URLs (jep.gov.co primary; CEV, UBPD, Constitutional Court, UN Mission)
- `references/citation-format.md` — Colombian civil-law citation conventions, the 11 macrocasos table, organ designations (Salas de Justicia, Tribunal Especial para la Paz, UIA), document types
- `references/verification-workflow.md` — fallback ladder, JEP-specific traps (sanciones propias ≠ impunity; macrocaso vs case; FARC ≠ FARC-EP after 2017 transformation; Sala de Reconocimiento vs Tribunal Especial para la Paz; September 2025 historic sentences)
- `references/foundational-texts.md` — Acuerdo Final 2016, Acto Legislativo 01 of 2017, Ley Estatutaria 1957 of 2019, Ley 1922 of 2018, Reglamento General, Colombian Constitutional Court Sentencia C-080 of 2018
- `references/jurisprudence-map.md` — topic-by-topic map of JEP holdings (limited as of 2026 — first sentences only September 2025; primarily structural and procedural decisions before that)
- `examples/example-verification.md` — verifying the Caso 01 (secuestro) September 2025 sentence
- `examples/example-audit.md` — auditing user-supplied documents (sanciones propias vs prison sentence; FARC vs FARC-EP)
