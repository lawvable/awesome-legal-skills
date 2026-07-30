---
name: "EU-Legislation"
description: "Access EU law. Search and retrieve Directives, Regulations, Treaties and CJEU case law from EUR-Lex."
allowed-tools: Bash(curl:*), WebFetch
metadata:
  author: "Malik Taiar"
  license: "agpl-3.0"
  version: "2026-04-15"
---

# EU Legislation & Case Law

Access EU law directly. Search and retrieve Directives, Regulations, Decisions, Treaties and CJEU case law from EUR-Lex.

## Capabilities

| Action                                    | Method          |
|-------------------------------------------|-----------------|
| **Search legislation/case law**           | EUR-Lex Search  |
| **Document info, status, modifications**  | EUR-Lex /ALL/   |
| **Procedure history**                     | EUR-Lex /HIS/   |
| **National transposition status**         | EUR-Lex /NIM/   |
| **National transposition full text**      | Official National Databases (27 MS) |

---

## Method 1: EUR-Lex Search (Semantic Search)

**Best for:** Finding documents by concept, topic, or keyword.

### URL Pattern

```
https://eur-lex.europa.eu/search.html?scope=EURLEX&text=QUERY&lang=LANG&type=quick&locale=LOCALE
```

### Languages (All 24 Official EU Languages)

| Language    | Code | Native Name        |
|-------------|------|--------------------|
| Bulgarian   | bg   | Български          |
| Czech       | cs   | Čeština            |
| Danish      | da   | Dansk              |
| Dutch       | nl   | Nederlands         |
| English     | en   | English            |
| Estonian    | et   | Eesti keel         |
| Finnish     | fi   | Suomi              |
| French      | fr   | Français           |
| German      | de   | Deutsch            |
| Greek       | el   | Ελληνικά           |
| Croatian    | hr   | Hrvatski           |
| Hungarian   | hu   | Magyar             |
| Irish       | ga   | Gaeilge            |
| Italian     | it   | Italiano           |
| Latvian     | lv   | Latviešu valoda    |
| Lithuanian  | lt   | Lietuvių kalba     |
| Maltese     | mt   | Malti              |
| Polish      | pl   | Polski             |
| Portuguese  | pt   | Português          |
| Romanian    | ro   | Română             |
| Slovak      | sk   | Slovenčina         |
| Slovenian   | sl   | Slovenščina        |
| Spanish     | es   | Español            |
| Swedish     | sv   | Svenska            |

Use code for both `lang=` and `locale=` parameters.

### Document Types (Form)

When reading search results, identify the document type from the "Form" field:

| Form                              | Type     | Description                    |
|-----------------------------------|----------|--------------------------------|
| Judgment                          | JUDG     | CJEU/General Court judgment   |
| Opinion of the Advocate General   | OPIN_AG  | AG conclusions                 |
| Directive                         | DIR      | EU Directive                   |
| Regulation                        | REG      | EU Regulation                  |
| Decision                          | DEC      | EU Decision                    |
| Treaty                            | TREATY   | EU Treaty                      |
| Proposal                          | PROP     | Commission proposal            |

**Note:** Prefer broad searches WITHOUT FM_CODED filter to catch more results. Filter by reading the Form field in results instead.

### Examples

```
# Broad search (recommended - catches all document types)
https://eur-lex.europa.eu/search.html?scope=EURLEX&text=cookies+consent&lang=en&type=quick&locale=en

# Search in French
https://eur-lex.europa.eu/search.html?scope=EURLEX&text=protection+donnees&lang=fr&type=quick&locale=fr

# Search CSRD
https://eur-lex.europa.eu/search.html?scope=EURLEX&text=CSRD&lang=en&type=quick&locale=en
```

### Pagination

- Page 1: No `&page` parameter
- Page 2+: Add `&page=2`, `&page=3`, etc.

---

## Method 2: EUR-Lex Document Pages (Advanced)

### URL Patterns

Replace `{CELEX}` with the CELEX ID (e.g., `32016R0679`).

| Page            | URL Pattern                    | Content                                    |
|-----------------|--------------------------------|--------------------------------------------|
| **Full text**   | `/TXT/?uri=CELEX:{CELEX}`      | Document text                              |
| **All info**    | `/ALL/?uri=CELEX:{CELEX}`      | Related docs, modifications, annexes       |
| **Procedure**   | `/HIS/?uri=CELEX:{CELEX}`      | Legislative procedure history              |
| **Transposition** | `/NIM/?uri=CELEX:{CELEX}`      | National implementation (directives)       |

### Base URL

```
https://eur-lex.europa.eu/legal-content/{LANG}/{PAGE}/?uri=CELEX:{CELEX}
```

### Examples

**GDPR - All information:**
```
https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32016R0679
```

**Whistleblower Directive - National transposition:**
```
https://eur-lex.europa.eu/legal-content/EN/NIM/?uri=CELEX:32019L1937
```

**CSRD - Procedure history:**
```
https://eur-lex.europa.eu/legal-content/EN/HIS/?uri=CELEX:32022L2464
```

---

## What You Can Find

### /ALL/ Page (Document Information)

- **Legal status**: In force, amended, repealed
- **Consolidated version date**
- **ELI**: European Legislation Identifier
- **Modifications**: What acts modified this one
- **Modified by**: List of amending acts with dates
- **Corrected by**: Corrigenda
- **Related documents**: Annexes, proposals, opinions

### /NIM/ Page (National Implementation)

- **Transposition status** by member state
- **National measures** implementing the directive
- **Links to national legislation**
- **Transposition deadlines**

> **IMPORTANT**: EUR-Lex /NIM/ links to national texts often show "Texte non disponible". When this happens, use the **Official National Legal Databases** (see below) to retrieve the actual text.

### /HIS/ Page (Procedure)

- **Legislative procedure** (ordinary, special)
- **Commission proposal**
- **Parliament readings**
- **Council positions**
- **Final adoption date**

---

## Cross-Reference Verification

EU law contains extensive cross-references. **Always verify referenced texts** to provide accurate answers.

### Types of References

| Reference Type                      | Example                          | How to Verify                                                                      |
|-------------------------------------|----------------------------------|------------------------------------------------------------------------------------|
| Internal article                    | "Article 21"                     | Re-read the full text                                                              |
| External act                        | "Regulation (EU) 2016/679"       | GoodLegal API or EUR-Lex /TXT/                                                     |
| Annex                               | "Annex I, Part B"                | EUR-Lex /ALL/ page                                                                 |
| Implementing act (Art. 291 TFEU)    | "Commission Implementing Regulation" | EUR-Lex /ALL/ → "Internal procedures based on this legislative basic act"       |
| Delegated act (Art. 290 TFEU)       | "Commission Delegated Regulation" | EUR-Lex /ALL/ → "Internal procedures based on this legislative basic act"       |
| CJEU case law                       | "Case C-xxx/xx"                  | EUR-Lex /ALL/ → "Affected by case"                                                 |

### Verification Workflow

```
Reading EU text
    │
    ├─► Found "Article X" reference?
    │       └─► WebFetch same document, extract Article X
    │
    ├─► Found "Directive/Regulation XXXX/XXX" reference?
    │       └─► GoodLegal API with CELEX ID
    │           OR WebFetch EUR-Lex /TXT/ page
    │
    ├─► Found "Annex" reference?
    │       └─► WebFetch EUR-Lex /ALL/ page
    │           Look for "Annexes" section
    │
    └─► Need related/implementing acts?
            └─► WebFetch EUR-Lex /ALL/ page
                Look for:
                - "Implemented by"
                - "Delegated acts"
                - "Related documents"
                - "Based on"
```

### Using /ALL/ for Related Documents

The /ALL/ page shows the complete document ecosystem:

```
https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:{CELEX}
```

**What to look for:**

| EUR-Lex Label                                              | Contains                                                          |
|-----------------------------------------------------------|-------------------------------------------------------------------|
| **Legal basis**                                            | Treaties (Art. 290, 291 TFEU), parent legislation                |
| **Internal procedures based on this legislative basic act** | Implementing acts (Art. 291 TFEU) and Delegated acts (Art. 290 TFEU) |
| **Modified by**                                            | Amending acts with dates and affected subdivisions                |
| **Modifies**                                               | Acts that this document amends                                    |
| **Corrected by**                                           | Corrigenda (language-specific corrections)                        |
| **Subsequent related instruments**                         | Follow-up legislation, related acts                               |
| **Affected by case**                                       | CJEU judgments interpreting this act                              |
| **Consolidated text**                                      | Link to consolidated version with all amendments                  |

**Note:** Implementing acts (uniform application conditions) and Delegated acts (supplement/amend non-essential elements) are often grouped together under "Internal procedures".

### Example: Answering a Legal Question

```
User asks: "What are the penalties under Directive 20XX/XXX?"

Step 1: Get full text
        → GoodLegal API: "320XXLXXXX"

Step 2: Find sanctions article (e.g., Article 30)
        → WebFetch EUR-Lex /TXT/ page, extract Article 30
        → Found: "Member States shall lay down penalties..."
        → References Article 5 (obligations) and Article 10 (reporting)

Step 3: Verify internal references
        → WebFetch same page, extract Articles 5 and 10
        → Article 5: Main compliance obligations
        → Article 10: Notification requirements

Step 4: Check for external references
        → Article 30 references Regulation (EU) 20YY/YYY
        → GoodLegal API: "320YYRYYYY"
        → Extract relevant provisions

Step 5: Check /ALL/ for implementing acts
        → WebFetch EUR-Lex /ALL/?uri=CELEX:320XXLXXXX
        → Found: Commission Implementing Regulation 20ZZ/ZZZ
        → Retrieve and review implementing details
```

### Reference Chain Documentation

When answering legal questions, document the reference chain:

```
**Question:** What are the reporting obligations under Directive 20XX/XXX?

**Answer:**
- Article 10: Notification within 72 hours
- Article 11: Content requirements (see Annex II)

**Internal references verified:**
- Article 5 → Scope of application
- Annex II → Notification template

**External references verified:**
- Regulation 20YY/YYY Article 15 → Definitions
- Commission Implementing Regulation 20ZZ/ZZZ → Technical standards

**Related acts from /ALL/ page:**
- 3 implementing regulations
- 1 delegated act
- 2 amending acts
```

---

## Decision Flow

```
User request
    │
    ├─► Full text needed?
    │       └─► GoodLegal API (CELEX ID or reference)
    │
    ├─► Search by concept?
    │       └─► EUR-Lex Search via WebFetch
    │           Read Form field to identify document type
    │
    ├─► Legal status / modifications?
    │       └─► EUR-Lex /ALL/ page via WebFetch
    │
    ├─► Transposition status?
    │       └─► EUR-Lex /NIM/ page via WebFetch
    │
    └─► Legislative procedure?
            └─► EUR-Lex /HIS/ page via WebFetch
```

---

## Parallel Search Strategy

For comprehensive research, launch multiple WebFetch calls in parallel:

```
# Search pages 1-5 simultaneously
Page 1: .../search.html?scope=EURLEX&text=QUERY&lang=en&type=quick&locale=en
Page 2: .../search.html?scope=EURLEX&text=QUERY&lang=en&type=quick&locale=en&page=2
Page 3: .../search.html?scope=EURLEX&text=QUERY&lang=en&type=quick&locale=en&page=3
Page 4: .../search.html?scope=EURLEX&text=QUERY&lang=en&type=quick&locale=en&page=4
Page 5: .../search.html?scope=EURLEX&text=QUERY&lang=en&type=quick&locale=en&page=5
```

Then filter results by Form field (Judgment, Directive, Regulation, etc.) based on user needs.

---

## Common References

### Legislation

| Name          | CELEX ID    |
|---------------|-------------|
| GDPR          | 32016R0679  |
| AI Act        | 32024R1689  |
| DSA           | 32022R2065  |
| DMA           | 32022R1925  |
| NIS2          | 32022L2555  |
| Whistleblower | 32019L1937  |
| ePrivacy      | 32002L0058  |
| CSRD          | 32022L2464  |

### Key CJEU Cases

| Name              | Case Number | Topic                    |
|-------------------|-------------|--------------------------|
| Costa v ENEL      | C-6/64      | Primacy                  |
| Google Spain      | C-131/12    | Right to be forgotten    |
| Schrems II        | C-311/18    | Data transfers           |
| Planet49          | C-673/17    | Cookie consent           |

---

## Output Format

### Legislation
```
**Directive (EU) 2019/1937 — Whistleblower Protection**
Status: In force (consolidated: 25/07/2024)
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L1937

Modifications: 6 amending acts
Transposition: 27/27 Member States
```

### Case Law
```
**Case C-311/18 — Schrems II**
Date: 16/07/2020
Topic: Data transfers, Privacy Shield invalidation
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62018CJ0311
```

---

## Error Handling

### No Results
- Try different search terms
- Try both EN and User's language
- Use EUR-Lex Search as fallback
- Check CELEX ID format

### EUR-Lex National Text Unavailable
When EUR-Lex /NIM/ links show "Texte non disponible" or "Text not available", follow the **National Transposition Text Retrieval** workflow below.

---

## Method 3: National Transposition Texts

### Problem

EUR-Lex /NIM/ pages list national transposition measures but **the links to actual text often fail** ("Texte non disponible" / "Text not available"). The /NIM/ page provides:
- Name of the national measure (e.g., "Decreto Legislativo 10 marzo 2023, n. 24")
- Official Journal reference (e.g., "Gazzetta Ufficiale n. 63 del 15 marzo 2023")
- Transposition deadline

### Workflow

```
Step 1: EUR-Lex /NIM/ Page
        │
        └─► WebFetch https://eur-lex.europa.eu/legal-content/EN/NIM/?uri=CELEX:{CELEX}
            Extract: measure name, Official Journal reference, date
        │
        ▼
Step 2: Try EUR-Lex Link
        │
        └─► Click/fetch the link provided on the /NIM/ page
            (e.g., https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=NIM:202302012)
        │
        ├─► Text available? → USE IT ✓
        │
        └─► "Texte non disponible" / "Text not available"?
                │
                ▼
Step 3: Official National Database (see table below)
        │
        └─► Use the measure reference from Step 1
            Search in the official national legal database
            (e.g., Normattiva for Italy, Légifrance for France)
        │
        ├─► Text found? → USE IT ✓
        │
        └─► Not found?
                │
                ▼
Step 4: Web Search (last resort)
        │
        └─► Search for official sources using:
            - Measure name + number + year
            - Official Journal reference
            - Filter by official government domains (.gov, .gv, .gouv, etc.)
```

### Official National Legal Databases (All 27 EU Member States)

Sources verified via [N-Lex](https://n-lex.europa.eu/n-lex/index), [European e-Justice Portal](https://e-justice.europa.eu/6/EN/national_legislation), and [European Forum of Official Gazettes](https://op.europa.eu/en/web/forum).

| Country | Code | Official Database | URL |
|---------|------|-------------------|-----|
| Austria | AT | RIS (Rechtsinformationssystem) | https://www.ris.bka.gv.at |
| Belgium | BE | Belgisch Staatsblad / Moniteur Belge | https://www.ejustice.just.fgov.be |
| Bulgaria | BG | Държавен вестник (State Gazette) | https://dv.parliament.bg |
| Croatia | HR | Narodne Novine | https://narodne-novine.nn.hr |
| Cyprus | CY | CyLaw + Official Gazette | http://www.cylaw.org |
| Czechia | CZ | Sbírka zákonů / Zákony pro lidi | https://www.zakonyprolidi.cz |
| Denmark | DK | Retsinformation | https://www.retsinformation.dk |
| Estonia | EE | Riigi Teataja | https://www.riigiteataja.ee |
| Finland | FI | Finlex | https://www.finlex.fi |
| France | FR | Légifrance | https://www.legifrance.gouv.fr |
| Germany | DE | Gesetze im Internet | https://www.gesetze-im-internet.de |
| Greece | EL | Εφημερίδα της Κυβερνήσεως (ΦΕΚ) | https://www.et.gr |
| Hungary | HU | Nemzeti Jogszabálytár | https://njt.hu |
| Ireland | IE | Irish Statute Book | https://www.irishstatutebook.ie |
| Italy | IT | Normattiva / Gazzetta Ufficiale | https://www.normattiva.it |
| Latvia | LV | Likumi.lv | https://likumi.lv |
| Lithuania | LT | e-TAR (Teisės aktų registras) | https://www.e-tar.lt |
| Luxembourg | LU | Legilux | https://legilux.public.lu |
| Malta | MT | Laws of Malta | https://legislation.mt |
| Netherlands | NL | Wetten.overheid.nl | https://wetten.overheid.nl |
| Poland | PL | ISAP (Sejm) | https://isap.sejm.gov.pl |
| Portugal | PT | DRE (Diário da República) | https://dre.pt |
| Romania | RO | Legislatie.just.ro | https://legislatie.just.ro |
| Slovakia | SK | Slov-Lex | https://www.slov-lex.sk |
| Slovenia | SI | PISRS | http://www.pisrs.si |
| Spain | ES | BOE (Boletín Oficial del Estado) | https://www.boe.es |
| Sweden | SE | Lagrummet / Svensk författningssamling | https://lagrummet.se |

### Country-Specific URL Patterns

#### Italy (Normattiva)
```
# By URN (preferred)
https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:YYYY-MM-DD;NUM

# Example: D.Lgs. 24/2023 (Whistleblower)
https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2023-03-10;24

# By Gazzetta Ufficiale
https://www.gazzettaufficiale.it/eli/id/YYYY/MM/DD/XXXXXXXX/sg
```

#### France (Légifrance)
```
# By JORF text number
https://www.legifrance.gouv.fr/jorf/id/JORFTEXT{NUMBER}

# By law number (search)
https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query=loi+{YEAR}-{NUMBER}

# Example: Loi Waserman 2022-401
https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045388745
```

#### Germany (Gesetze im Internet)
```
# By law abbreviation
https://www.gesetze-im-internet.de/{abbrev}/

# Federal Law Gazette (BGBl)
https://www.bgbl.de/xaver/bgbl/start.xav
```

#### Spain (BOE)
```
# By BOE reference
https://www.boe.es/buscar/doc.php?id=BOE-A-YYYY-NNNNN

# By law reference
https://www.boe.es/buscar/act.php?id=BOE-A-YYYY-NNNNN
```

#### Netherlands (Overheid.nl)
```
# By BWBR number
https://wetten.overheid.nl/BWBR{NUMBER}

# By Staatsblad reference
https://zoek.officielebekendmakingen.nl/stb-{YEAR}-{NUMBER}
```

#### Poland (ISAP)
```
# By Dz.U. reference
https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU{YEAR}{NUMBER}
```

### Example: Retrieving Italian Transposition Text

```
User asks: "Get the Italian transposition of the Whistleblower Directive"

Step 1: Check EUR-Lex /NIM/
        → WebFetch https://eur-lex.europa.eu/legal-content/EN/NIM/?uri=CELEX:32019L1937
        → Found: "Decreto Legislativo 10 marzo 2023, n. 24"
                 "Gazzetta Ufficiale n. 63 del 15 marzo 2023"

Step 2: Try EUR-Lex link
        → WebFetch the provided link
        → Result: "Texte non disponible"

Step 3: Go to Normattiva (official Italian database)
        → WebFetch https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2023-03-10;24
        → SUCCESS: Full text of D.Lgs. 24/2023 retrieved ✓

If Step 3 fails:
Step 4: Web search (last resort)
        → WebSearch "D.Lgs. 24/2023 whistleblowing site:normattiva.it OR site:gazzettaufficiale.it"
```

### Regulatory Authority Websites

For **implementation guidelines, interpretive guidance, and FAQs**, also check the national regulatory authority responsible for the directive:

| Directive | Topic | Key National Authorities |
|-----------|-------|--------------------------|
| 2019/1937 (Whistleblower) | Anti-corruption | IT: [ANAC](https://www.anticorruzione.it), FR: [Défenseur des droits](https://www.defenseurdesdroits.fr), DE: [BfJ](https://www.bundesjustizamt.de) |
| 2016/679 (GDPR) | Data protection | IT: [Garante Privacy](https://www.garanteprivacy.it), FR: [CNIL](https://www.cnil.fr), DE: [BfDI](https://www.bfdi.bund.de) |
| 2022/2555 (NIS2) | Cybersecurity | IT: [ACN](https://www.acn.gov.it), FR: [ANSSI](https://www.ssi.gouv.fr), DE: [BSI](https://www.bsi.bund.de) |

---

## CELEX Format Reference

### Legislation: `3{YEAR}{TYPE}{NUMBER}`

| Type       | Code | Example     |
|------------|------|-------------|
| Directive  | L    | 32019L1937  |
| Regulation | R    | 32016R0679  |
| Decision   | D    | 32021D0914  |

### Case Law: `6{YEAR}{COURT}{NUMBER}`

| Court            | Code | Example     |
|------------------|------|-------------|
| Court of Justice | CJ   | 62018CJ0311 |
| General Court    | TJ   | 62022TJ0354 |
| AG Opinion       | CC   | 62017CC0673 |
