# Privacy Notice Document Template

For .docx generation. Always load the docx generation skill first (`/mnt/skills/public/docx/SKILL.md` in Claude.ai Projects, or the `docx-processing-anthropic` skill in Claude Code). If no docx skill is available, generate well-formatted Markdown as fallback.

Use `docx-js` (npm). Page size: A4 (11906 x 16838 DXA). Font: Arial. All table widths in DXA.

---

## Page & Style Specifications

### Page Layout

- **Page size**: A4 — width: 11906 DXA, height: 16838 DXA
- **Margins**: top/bottom: 1134 DXA (2 cm), left/right: 1418 DXA (2.5 cm)
- **Content width**: 9070 DXA (page width minus left and right margins)

### Color Scheme

| Token | Hex | Usage |
|-------|-----|-------|
| `primary` | `1B3A5C` | Dark navy — headings (H1), title, bold emphasis |
| `accent` | `2E86AB` | Teal — H2/H3 headings, subtitle, separator line |
| `lightBg` | `EDF4F8` | Very light blue — table header cell shading |
| `medBg` | `D6E8F2` | Medium blue — emphasis rows (if needed) |
| `border` | `B0C4D8` | Soft blue-grey — table borders |
| `text` | `2D2D2D` | Near-black — body text |
| `muted` | `5A6977` | Grey — secondary info, placeholders, footer |
| `white` | `FFFFFF` | White backgrounds |
| `alertBg` | `FFF3E0` | Warm highlight — Art. 21 objection box background |
| `alertBorder` | `E65100` | Orange — Art. 21 objection box border and title |

### Typography

| Element | Font | Size (half-points) | Style | Color |
|---------|------|---------------------|-------|-------|
| Title | Arial | 40 | Bold | `primary` |
| Subtitle | Arial | 26 | Normal | `accent` |
| Last updated | Arial | 20 | Italic | `muted` |
| Heading 1 | Arial | 28 | Bold | `primary` |
| Heading 2 | Arial | 24 | Bold | `accent` |
| Heading 3 | Arial | 22 | Bold | `accent` |
| Body text | Arial | 21 | Normal | `text` |
| Table header | Arial | 19 | Bold | `primary` |
| Table body | Arial | 19 | Normal | `text` |
| Placeholder text | Arial | 19 | Italic | `muted` |
| Header (running) | Arial | 16 | Italic | `muted` |
| Footer | Arial | 16 | Normal | `muted` |
| Art. 21 box title | Arial | 22 | Bold | `alertBorder` |
| Art. 21 box body | Arial | 20 | Normal | `text` |

### Heading Styles (for TOC outline levels)

- Heading 1: outlineLevel 0, spacing before 360 / after 120
- Heading 2: outlineLevel 1, spacing before 240 / after 80
- Heading 3: outlineLevel 2, spacing before 200 / after 60
- Body: spacing before 60 / after 120, line spacing 276

### Table Formatting

- **Borders**: SINGLE, size 1, color `border` (`B0C4D8`)
- **Header row shading**: fill `lightBg` (`EDF4F8`), type CLEAR
- **Cell margins**: top 60, bottom 60, left 100, right 100
- **Bullet lists**: LevelFormat.BULLET, text `\u2022`, indent left 720 / hanging 360

---

## Document Structure

### Cover / Title Block

Centered layout:
1. Empty spacer paragraph (spacing before 600)
2. **Title** — e.g. "Datenschutzerklaerung" / "Politique de confidentialite" / "Privacy Notice"
3. **Subtitle** — company name placeholder
4. **Last updated** — date placeholder, italic
5. **Separator line** — single-cell table, bottom border only (size 2, color `accent`), full content width

### Table of Contents

Auto-generated `TableOfContents` with hyperlinks, heading style range 1-2. Followed by a page break.

### Header (every page)

Right-aligned, italic, muted: "[Document title] — [Company Name]"

### Footer (every page)

Centered, muted: "[Last updated label]: [DATE] — Page {PAGE_NUMBER}"

---

## 13-Section Structure

### Section 1: Controller

- Heading 1: section title
- Intro paragraph
- Company details block: company name (bold), address, representative, registration, email, phone — all as separate body text paragraphs
- **Sub-heading (H2)**: DPO label
- DPO intro text
- DPO contact placeholder (italic, muted)

### Section 2: Data We Collect

- Heading 1: section title
- Intro paragraph
- Bullet list of data categories (placeholder items, italic, muted):
  - Identity data
  - Contact data
  - Technical data
  - Usage data
  - Transaction data

### Section 3: Purposes, Legal Bases & Retention

- Heading 1: section title
- Intro paragraph
- **Purposes table** — 4 columns, full content width:

| Column | Approx. width (DXA) |
|--------|---------------------|
| Purpose | 2200 |
| Data Categories | 2200 |
| Legal Basis | 2470 |
| Retention Period | 2200 |

- Header row with `lightBg` shading
- 3 placeholder data rows (italic, muted `[...]`)

### Section 4: Recipients

- Heading 1: section title
- Intro paragraph
- Bullet list of recipient categories (placeholder, italic, muted):
  - Hosting
  - Payment
  - Analytics
  - Email / Marketing
  - AI Services

### Section 5: International Transfers

- Heading 1: section title
- Intro paragraph
- Bullet list: country + mechanism placeholder (italic, muted)

### Section 6: Retention

- Note: retention is covered in the Section 3 table. This section may be omitted or used as a cross-reference to Section 3, depending on user preference.

### Section 7: Your Rights

- Heading 1: section title
- Intro paragraph
- Bullet list of 8 rights (normal text, not muted — these are substantive):
  1. Access (Art. 15)
  2. Rectification (Art. 16)
  3. Erasure (Art. 17)
  4. Restriction (Art. 18)
  5. Data Portability (Art. 20)
  6. Object (Art. 21) — with reference to dedicated box below
  7. Withdraw Consent (Art. 7(3))
  8. Lodge Complaint (Art. 77)
- Exercise paragraph: contact email, one-month response
- Supervisory authority: name (bold), address, URL

### Art. 21 Objection Box (after Section 7)

**Visually prominent box** — implemented as a single-cell table:
- **Left border**: size 8, color `alertBorder` (`E65100`)
- **Other borders**: size 3, color `alertBorder`
- **Background**: `alertBg` (`FFF3E0`), ShadingType.CLEAR
- **Cell margins**: top/bottom 120, left/right 200
- **Content**:
  1. Box title (bold, `alertBorder` color)
  2. Paragraph 1: legitimate interest objection right
  3. Paragraph 2: direct marketing objection right
  4. Paragraph 3: consequences of objection

This box must be **separate and prominent** per Art. 21(4) GDPR.

### Section 8: Cookies & Tracking

- Heading 1: section title
- Intro paragraph
- **Cookie table** — 5 columns, full content width:

| Column | Approx. width (DXA) |
|--------|---------------------|
| Category | 1600 |
| Tool / Provider | 1800 |
| Purpose | 2070 |
| Duration | 1400 |
| Legal Basis | 2200 |

- Header row with `lightBg` shading
- Placeholder data rows

### Section 9: AI Processing & Automated Decisions

- Heading 1: section title
- Intro paragraph
- **AI table** — 4 columns, full content width:

| Column | Approx. width (DXA) |
|--------|---------------------|
| AI System / Technology | 2200 |
| Purpose | 2600 |
| Decision Type | 2270 |
| Legal Basis | 2000 |

- Header row with `lightBg` shading
- Placeholder data rows
- Art. 22 rights paragraph

### Section 10: Data Security

- Heading 1: section title
- Body paragraph (Art. 32 reference, TOMs, regular review)

### Section 11: Children's Data

- Heading 1: section title
- Body paragraph (age threshold placeholder, deletion commitment)

### Section 12: Changes to This Notice

- Heading 1: section title
- Body paragraph (right to update, current version on website, material change notification)

### Section 13: Contact

- Heading 1: section title
- Contact intro paragraph
- Company name (bold), address, email, phone

---

## Multi-Language Support

The template supports three languages. Use the language matching the target jurisdiction. All section headings, intro texts, table headers, placeholder labels, and the Art. 21 box text must be in the target language.

### German (DE)

**Section Headings:**
| Section | Heading |
|---------|---------|
| Title | Datenschutzerklaerung |
| 1 | 1. Verantwortlicher |
| 2 | 2. Welche Daten wir erheben |
| 3 | 3. Zwecke, Rechtsgrundlagen und Speicherdauer |
| 4 | 4. Empfaenger Ihrer Daten |
| 5 | 5. Datenuebermittlung in Drittstaaten |
| 6 | 6. Speicherdauer |
| 7 | 7. Ihre Rechte |
| Art. 21 | Widerspruchsrecht (Art. 21 DSGVO) |
| 8 | 8. Cookies und Tracking |
| 9 | 9. KI-gestuetzte Verarbeitung und automatisierte Entscheidungen |
| 10 | 10. Datensicherheit |
| 11 | 11. Daten von Minderjaehrigen |
| 12 | 12. Aenderungen dieser Datenschutzerklaerung |
| 13 | 13. Kontakt |

**Table Headers:**
- Purposes: Zweck | Betroffene Daten | Rechtsgrundlage | Speicherdauer
- Cookies: Kategorie | Tool / Anbieter | Zweck | Speicherdauer | Rechtsgrundlage
- AI: KI-System / Technologie | Zweck | Art der Entscheidung | Rechtsgrundlage

**Key Texts:**
- Controller intro: "Verantwortlich im Sinne der Datenschutz-Grundverordnung (DSGVO) ist:"
- DPO label: "Datenschutzbeauftragter"
- Rights intro: "Die DSGVO gewaehrt Ihnen umfassende Rechte in Bezug auf Ihre personenbezogenen Daten:"
- Rights exercise: "Zur Ausuebung Ihrer Rechte wenden Sie sich bitte an: [KONTAKT-E-MAIL]. Wir werden Ihre Anfrage innerhalb eines Monats beantworten."
- Header: "Datenschutzerklaerung -- [Firmenname]"
- Footer prefix: "Stand: [DATUM] -- Seite "
- Placeholders: [Firmenname GmbH / AG / SE], [Strasse Nr., PLZ Ort], Vertreten durch: [Geschaeftsfuehrer/Vorstand], Registergericht: [Amtsgericht], HRB [Nr.]

**Art. 21 Box (DE):**
1. "Soweit wir Ihre personenbezogenen Daten auf Grundlage unseres berechtigten Interesses (Art. 6 Abs. 1 lit. f DSGVO) verarbeiten, haben Sie das Recht, aus Gruenden, die sich aus Ihrer besonderen Situation ergeben, jederzeit Widerspruch gegen diese Verarbeitung einzulegen."
2. "Werden Ihre personenbezogenen Daten verarbeitet, um Direktwerbung zu betreiben, haben Sie das Recht, jederzeit Widerspruch gegen die Verarbeitung Sie betreffender personenbezogener Daten zum Zwecke derartiger Werbung einzulegen. Dies gilt auch fuer das Profiling, soweit es mit solcher Direktwerbung in Verbindung steht."
3. "Im Falle Ihres Widerspruchs verarbeiten wir Ihre personenbezogenen Daten nicht mehr fuer diese Zwecke, es sei denn, wir koennen zwingende schutzwuerdige Gruende nachweisen, die Ihre Interessen, Rechte und Freiheiten ueberwiegen, oder die Verarbeitung dient der Geltendmachung, Ausuebung oder Verteidigung von Rechtsanspruechen."

**Rights List (DE):**
- Auskunft (Art. 15 DSGVO): Bestaetigung, ob und welche Daten ueber Sie verarbeitet werden, sowie eine kostenlose Kopie.
- Berichtigung (Art. 16 DSGVO): Unverzuegliche Korrektur unrichtiger oder Vervollstaendigung unvollstaendiger Daten.
- Loeschung (Art. 17 DSGVO): Loeschung Ihrer Daten, sofern kein gesetzlicher Aufbewahrungsgrund entgegensteht.
- Einschraenkung (Art. 18 DSGVO): Voruebergehende Einschraenkung der Verarbeitung unter bestimmten Voraussetzungen.
- Datenuebertragbarkeit (Art. 20 DSGVO): Herausgabe Ihrer Daten in einem gaengigen, maschinenlesbaren Format.
- Widerspruch (Art. 21 DSGVO): Widerspruch gegen die Verarbeitung auf Basis berechtigter Interessen -- siehe gesonderten Hinweis unten.
- Widerruf der Einwilligung (Art. 7 Abs. 3 DSGVO): Jederzeit moeglich, ohne dass die Rechtmaessigkeit der bis dahin erfolgten Verarbeitung beruehrt wird.
- Beschwerderecht (Art. 77 DSGVO): Sie haben das Recht, sich bei einer Datenschutzaufsichtsbehoerde zu beschweren.

**Body Texts (DE):**
- Data intro: "Im Rahmen der Nutzung unseres [Angebots/Dienstes/Webseite] verarbeiten wir folgende Kategorien personenbezogener Daten:"
- Purposes intro: "Die nachfolgende Tabelle gibt Ihnen einen Ueberblick ueber die Verarbeitungszwecke, die jeweilige Rechtsgrundlage und die Speicherdauer."
- Recipients intro: "Zur Erfuellung der oben genannten Zwecke koennen Ihre personenbezogenen Daten an folgende Kategorien von Empfaengern uebermittelt werden:"
- Transfers intro: "Einige unserer Dienstleister koennen ihren Sitz ausserhalb des Europaeischen Wirtschaftsraums (EWR) haben. In diesem Fall stellen wir durch geeignete Garantien sicher, dass ein angemessenes Datenschutzniveau gewaehrleistet ist:"
- Cookies intro: "Unser [Angebot/Webseite] verwendet Cookies und aehnliche Technologien. Die nachfolgende Tabelle gibt Ihnen einen Ueberblick:"
- AI intro: "Wir setzen im Rahmen unseres [Angebots/Dienstes] automatisierte Verarbeitungstechnologien ein, darunter Verfahren der kuenstlichen Intelligenz (KI). Im Folgenden informieren wir Sie ueber Art, Umfang und Zweck dieser Verarbeitung."
- AI rights: "Soweit automatisierte Entscheidungen Ihnen gegenueber rechtliche Wirkung entfalten oder Sie in aehnlicher Weise erheblich beeintraechtigen (Art. 22 DSGVO), haben Sie das Recht auf Eingreifen einer Person, auf Darlegung Ihres Standpunkts und auf Anfechtung der Entscheidung."
- Security: "Wir treffen angemessene technische und organisatorische Massnahmen gemaess Art. 32 DSGVO, um Ihre Daten vor unbefugtem Zugriff, Verlust, Zerstoerung oder Veraenderung zu schuetzen. Diese Massnahmen werden regelmaessig ueberprueft und dem Stand der Technik angepasst."
- Children: "Unser [Angebot/Dienst] richtet sich grundsaetzlich nicht an Personen unter [16] Jahren. Sollten wir feststellen, dass Daten von Minderjaehrigen ohne die erforderliche Einwilligung der Erziehungsberechtigten erhoben wurden, werden diese unverzueglich geloescht."
- Changes: "Wir behalten uns vor, diese Datenschutzerklaerung bei Bedarf anzupassen, um sie an geaenderte Rechtslage oder bei Aenderungen unseres Dienstes bzw. der Datenverarbeitung anzupassen. Die jeweils aktuelle Fassung finden Sie stets auf unserer Webseite. Bei wesentlichen Aenderungen werden wir Sie gesondert informieren."
- Contact: "Bei Fragen zur Verarbeitung Ihrer personenbezogenen Daten oder zur Ausuebung Ihrer Rechte erreichen Sie uns unter:"

### French (FR)

**Section Headings:**
| Section | Heading |
|---------|---------|
| Title | Politique de confidentialite |
| 1 | 1. Responsable du traitement |
| 2 | 2. Donnees que nous collectons |
| 3 | 3. Finalites, bases legales et durees de conservation |
| 4 | 4. Destinataires de vos donnees |
| 5 | 5. Transferts hors de l'Union europeenne |
| 6 | 6. Durees de conservation |
| 7 | 7. Vos droits |
| Art. 21 | Droit d'opposition (Art. 21 RGPD) |
| 8 | 8. Cookies et traceurs |
| 9 | 9. Traitement par intelligence artificielle et decisions automatisees |
| 10 | 10. Securite des donnees |
| 11 | 11. Donnees des mineurs |
| 12 | 12. Modifications de cette politique |
| 13 | 13. Contact |

**Table Headers:**
- Purposes: Finalite | Donnees concernees | Base legale | Duree de conservation
- Cookies: Categorie | Outil / Fournisseur | Finalite | Duree | Base legale
- AI: Systeme IA / Technologie | Finalite | Type de decision | Base legale

**Key Texts:**
- Controller intro: "Le responsable du traitement de vos donnees personnelles est :"
- DPO label: "Delegue a la protection des donnees"
- Rights intro: "Le RGPD vous confere des droits etendus sur vos donnees personnelles :"
- Rights exercise: "Pour exercer vos droits, adressez votre demande a : [E-MAIL DE CONTACT]. Nous repondrons dans un delai d'un mois."
- Supervisory authority: "L'autorite de controle competente est :" (default: CNIL, 3 Place de Fontenoy, TSA 80715, 75334 Paris Cedex 07, www.cnil.fr)
- Header: "Politique de confidentialite -- [Nom de l'entreprise]"
- Footer prefix: "Derniere mise a jour : [DATE] -- Page "
- Placeholders: [Denomination sociale, forme juridique], [Adresse du siege social], Representee par : [Nom], [Qualite], Immatriculee au RCS de [ville] sous le n. [SIREN/SIRET]

**Art. 21 Box (FR):**
1. "Lorsque nous traitons vos donnees personnelles sur la base de notre interet legitime (Art. 6.1.f RGPD), vous avez le droit de vous y opposer a tout moment pour des raisons tenant a votre situation particuliere."
2. "Si vos donnees personnelles sont traitees a des fins de prospection commerciale, vous pouvez vous y opposer a tout moment, sans avoir a justifier de motifs particuliers. Il en va de meme pour le profilage lie a cette prospection."
3. "En cas d'opposition, nous cesserons de traiter vos donnees a ces fins, sauf si nous demontrons l'existence de motifs legitimes et imperieux prevalant sur vos interets, droits et libertes, ou si le traitement est necessaire a la constatation, l'exercice ou la defense de droits en justice."

**Rights List (FR):**
- Acces (Art. 15 RGPD) : obtenir la confirmation que vos donnees sont traitees et en recevoir une copie.
- Rectification (Art. 16 RGPD) : faire corriger des donnees inexactes ou incompletes.
- Effacement (Art. 17 RGPD) : obtenir la suppression de vos donnees dans les cas prevus par la loi.
- Limitation (Art. 18 RGPD) : suspendre temporairement l'utilisation de certaines donnees.
- Portabilite (Art. 20 RGPD) : recuperer vos donnees dans un format structure et couramment utilise.
- Opposition (Art. 21 RGPD) : vous opposer au traitement fonde sur l'interet legitime -- voir l'encadre ci-dessous.
- Retrait du consentement (Art. 7.3 RGPD) : a tout moment, sans remettre en cause la liceite du traitement effectue avant le retrait.
- Reclamation (Art. 77 RGPD) : introduire une reclamation aupres de la CNIL.

**Body Texts (FR):**
- Data intro: "Dans le cadre de l'utilisation de notre [service/site web], nous traitons les categories de donnees personnelles suivantes :"
- Purposes intro: "Le tableau suivant vous donne un apercu des finalites de traitement, de la base legale applicable et de la duree de conservation."
- Recipients intro: "Pour la realisation des finalites decrites ci-dessus, vos donnees personnelles peuvent etre communiquees aux categories de destinataires suivantes :"
- Transfers intro: "Certains de nos prestataires peuvent etre etablis en dehors de l'Espace economique europeen (EEE). Dans ce cas, nous veillons a ce que des garanties appropriees soient mises en place :"
- Cookies intro: "Notre [site web/service] utilise des cookies et technologies similaires. Le tableau suivant vous en donne un apercu :"
- AI intro: "Nous utilisons dans le cadre de notre [service] des technologies de traitement automatise, y compris des procedes d'intelligence artificielle (IA). Vous trouverez ci-dessous les informations sur la nature, la portee et la finalite de ces traitements."
- AI rights: "Lorsqu'une decision automatisee produit des effets juridiques ou vous affecte de maniere significative (Art. 22 RGPD), vous disposez du droit d'obtenir une intervention humaine, d'exprimer votre point de vue et de contester la decision."
- Security: "Nous mettons en oeuvre des mesures techniques et organisationnelles appropriees conformement a l'Art. 32 RGPD pour proteger vos donnees contre tout acces non autorise, perte, destruction ou alteration. Ces mesures sont regulierement reevaluees et adaptees a l'etat de l'art."
- Children: "Notre [service] ne s'adresse pas en principe aux personnes de moins de [15] ans. Si nous constatons que des donnees de mineurs ont ete collectees sans le consentement requis du titulaire de l'autorite parentale, elles seront supprimees sans delai."
- Changes: "Nous nous reservons le droit de modifier cette politique a tout moment pour l'adapter a l'evolution de la reglementation ou de nos pratiques. La version en vigueur est toujours disponible sur notre site. En cas de modification substantielle, nous vous en informerons de maniere appropriee."
- Contact: "Pour toute question relative au traitement de vos donnees personnelles ou a l'exercice de vos droits, vous pouvez nous contacter :"

### English (EN)

**Section Headings:**
| Section | Heading |
|---------|---------|
| Title | Privacy Notice |
| 1 | 1. Data Controller |
| 2 | 2. Data We Collect |
| 3 | 3. Purposes, Legal Bases, and Retention Periods |
| 4 | 4. Recipients of Your Data |
| 5 | 5. International Data Transfers |
| 6 | 6. Retention Periods |
| 7 | 7. Your Rights |
| Art. 21 | Right to Object (Art. 21 GDPR) |
| 8 | 8. Cookies and Tracking Technologies |
| 9 | 9. AI Processing and Automated Decision-Making |
| 10 | 10. Data Security |
| 11 | 11. Children's Data |
| 12 | 12. Changes to This Notice |
| 13 | 13. Contact |

**Table Headers:**
- Purposes: Purpose | Data Categories | Legal Basis | Retention Period
- Cookies: Category | Tool / Provider | Purpose | Duration | Legal Basis
- AI: AI System / Technology | Purpose | Decision Type | Legal Basis

**Key Texts:**
- Controller intro: "The controller responsible for processing your personal data is:"
- DPO label: "Data Protection Officer"
- Rights intro: "Under the GDPR, you have the following rights regarding your personal data:"
- Rights exercise: "To exercise your rights, please contact: [CONTACT EMAIL]. We will respond within one month."
- Header: "Privacy Notice -- [Company Name]"
- Footer prefix: "Last updated: [DATE] -- Page "
- Placeholders: [Company Name, Legal Form], [Registered Address], Represented by: [Name], [Title], Registration: [Registry], [Number]

**Art. 21 Box (EN):**
1. "Where we process your personal data on the basis of our legitimate interest (Art. 6(1)(f) GDPR), you have the right to object at any time on grounds relating to your particular situation."
2. "Where your personal data is processed for direct marketing purposes, you have the right to object at any time, without needing to provide specific reasons. This also applies to profiling insofar as it is related to such direct marketing."
3. "In the event of your objection, we will cease processing your data for these purposes, unless we can demonstrate compelling legitimate grounds that override your interests, rights and freedoms, or the processing serves the establishment, exercise or defence of legal claims."

**Rights List (EN):**
- Access (Art. 15 GDPR): Obtain confirmation of whether your data is processed and receive a copy.
- Rectification (Art. 16 GDPR): Have inaccurate or incomplete data corrected without undue delay.
- Erasure (Art. 17 GDPR): Request deletion of your data where legally permissible.
- Restriction (Art. 18 GDPR): Request temporary restriction of processing under certain conditions.
- Data Portability (Art. 20 GDPR): Receive your data in a structured, commonly used, machine-readable format.
- Object (Art. 21 GDPR): Object to processing based on legitimate interests -- see dedicated section below.
- Withdraw Consent (Art. 7(3) GDPR): At any time, without affecting the lawfulness of prior processing.
- Lodge a Complaint (Art. 77 GDPR): File a complaint with the competent supervisory authority.

**Body Texts (EN):**
- Data intro: "In connection with your use of our [service/website], we process the following categories of personal data:"
- Purposes intro: "The following table provides an overview of the processing purposes, the applicable legal basis, and the retention period."
- Recipients intro: "To fulfil the purposes described above, your personal data may be disclosed to the following categories of recipients:"
- Transfers intro: "Some of our service providers may be established outside the European Economic Area (EEA). In such cases, we ensure appropriate safeguards are in place:"
- Cookies intro: "Our [website/service] uses cookies and similar technologies. The following table provides an overview:"
- AI intro: "We use automated processing technologies, including artificial intelligence (AI), in connection with our [service]. Below we inform you about the nature, scope, and purpose of this processing."
- AI rights: "Where an automated decision produces legal effects or similarly significantly affects you (Art. 22 GDPR), you have the right to obtain human intervention, express your point of view, and contest the decision."
- Security: "We implement appropriate technical and organisational measures pursuant to Art. 32 GDPR to protect your data against unauthorised access, loss, destruction, or alteration. These measures are regularly reviewed and adapted to the state of the art."
- Children: "Our [service] is generally not directed at persons under [16] years of age. If we become aware that data of minors has been collected without the required parental consent, it will be deleted without undue delay."
- Changes: "We reserve the right to update this notice at any time to reflect changes in legislation or our practices. The current version is always available on our website. We will notify you of material changes in an appropriate manner."
- Contact: "If you have any questions about the processing of your personal data or wish to exercise your rights, you can reach us at:"
