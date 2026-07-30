---
name: new-designation-screening-test
description: "Generate a spreadsheet of test entries — newly designated names from OFAC, OFSI, and EU sanctions lists plus deliberate variations of those names — to validate that a sanctions screening system catches fresh designations and is tuned to the right fuzziness threshold. Use this whenever the user asks for sanctions list update test data, screening regression test data, screening QA, fuzzy match calibration, or wants to verify their screening lists are current. Trigger even if the user doesn't say 'screening' explicitly — phrases like 'test my sanctions list', 'check our SDN coverage', 'is my list up to date', or 'build me a regression set from the latest designations' should also invoke this skill."
metadata:
  author: "Amir Fadavi"
  license: "mit"
  version: "2026-05-07"
---

# New Designation Screening Test Generator

This skill produces a spreadsheet that compliance teams can run through their sanctions screening system to verify two things at once:

1. **Coverage** — the screening list is current (catches names added in the most recent designations).
2. **Fuzzy tuning** — the screening engine is tuned to catch realistic name variations (transliterations, transpositions, alphabet swaps), not just exact strings.

Each row in the output is a single test entry: a designated name or a deliberate variation of one, plus the metadata an analyst needs to interpret a hit (or a miss).

## When to run

Run when the user asks for:
- New designation test data / screening regression set
- Validation that their sanctions list is up to date
- A fuzzy-match calibration test set
- Anything matching "test my screening" or "check our [SDN/OFSI/EU] coverage"

If the user doesn't specify a lookback window, default to the trailing 7 days. If they say "since last run" and provide a prior date, use that.

## Workflow

### Step 1 — Pull recent designations from the Big 3

| Regulator | Source | What to capture |
|---|---|---|
| OFAC | `https://ofac.treasury.gov/recent-actions` | Additions to the SDN List or sectoral/Non-SDN lists. Exclude amendments, removals, FAQ updates, and republished general licenses. |
| OFSI | `https://www.gov.uk/government/publications/the-uk-sanctions-list` plus the matching OFSI notice PDF (see sub-procedure below) | Entries marked **"Added"** only — exclude **"Amended"** and **"Removed"**. |
| EU | Two sources used together: (1) `https://data.europa.eu/apps/eusanctionstracker/` — the EU Sanctions Tracker; the middle of the page lists the most recently designated individuals and entities, used to identify in-window additions. (2) The relevant Council Implementing Regulation in the *Official Journal* (e.g., Regulation (EU) 2026/509 for the 20th Russia package), accessed via EUR-Lex — the canonical legal source for identifiers, addresses, designation reasoning, and listing references. | New entries on the consolidated CFSP financial sanctions list. |

#### OFSI sub-procedure

The UK Sanctions List page tells you the list changed and on what date. The designee detail you need (identifiers, designation reasoning, regulator-published name variations) lives in the matching OFSI notice PDF, published as a separate document.

**Always expand the full change log.** The "Updates to this page" section on `https://www.gov.uk/government/publications/the-uk-sanctions-list` is collapsed by default. The visible portion is partial; in-window entries can sit below the fold. Click **"show all updates"** (or expand the `#full-publication-update-history` anchor) every time, before reading the log.

Workflow:

1. Open `https://www.gov.uk/government/publications/the-uk-sanctions-list#full-publication-update-history` and expand "show all updates" so every entry is visible.
2. Read every entry within the lookback window. Identify those that list **"Added"** — exclude entries that are only variations, administrative amendments, corrections, or revocations. Note the date and the sanctions program(s) named.
3. For each program with additions, web-search `OFSI notice [program name] [day] [month] [year]` (e.g., `OFSI notice Sudan 29 April 2026`) and locate the matching PDF. The URL begins with `https://assets.publishing.service.gov.uk/media/...` followed by the notice name.
4. Confirm the PDF's publication date matches the change-log entry. If multiple notices for the program exist, only the one tied to the in-window date is the right source.
5. Parse the notice. The PDF itself states whether each entry is an **Addition**, **Variation**, or **Removal**. **Pull only entries under "Additions".** For each addition capture: primary name, unique ID, regime name, sanctions imposed, DOB, town/country of birth, all nationalities, all passports, national ID(s), address, position, designation source (UK / UN), date designated, and any UN reference number (e.g., SDi.011).
6. If the UK is implementing a UN Security Council listing, note the UN reference number in the `identifiers` column and check whether OFAC has the same individual — divergent transliterations across regulators produce useful test rows (see `cross_regulator_variant` in the taxonomy).

For each new entry across all three regulators, capture:
- Primary name as listed
- All AKAs / aliases the regulator publishes
- Entity type (individual, entity, vessel, aircraft)
- Sanctions program / authority
- Designation date
- Identifiers: DOB, POB, nationality/jurisdiction, address, passport / national ID / tax ID / IMO number / aircraft tail number
- Source URL (link directly to the listing or notice page, not just the homepage)

#### Default scope: individuals and entities only

By default, **exclude vessels and aircraft** from the test set. Most sanctions screening in financial transactions runs against payment narratives, beneficiary names, and counterparty entities — not ship registries or aircraft tail numbers. A general-purpose screening test seeded with vessel and aircraft names produces noise more than signal for typical compliance teams (banks, fintechs, professional services firms).

Vessel and aircraft screening *does* matter for:
- Trade finance and letter-of-credit operations
- Ship and aircraft financing
- Marine and aviation insurance
- Shipping, freight forwarding, and logistics companies
- Port operators and bunker / fueling services

If the user specifically requests vessel or aircraft test data, generate a **separate spreadsheet** for those entity types using the same column schema — don't fold them into the default output. Filename suggestion: `screening-test-vessels-YYYY-MM-DD.xlsx` or `screening-test-aircraft-YYYY-MM-DD.xlsx`.

In the response that delivers the default output, briefly note that vessels/aircraft were excluded and that a separate set is available on request.

#### Volume control

Apply this rule to each individual regulatory action separately (a single OFAC Recent Action page, a single OFSI notice, a single EU Council Implementing Regulation), **after removing vessels and aircraft from the population** unless the user requested them. Apply per-action, not to the combined cross-regulator total.

- **5 or fewer additions in the action** → take all of them.
- **More than 5 additions** → sample **5 random entries plus 10% of the total** (round up). E.g., a 120-designee EU package → 5 + ⌈12⌉ = 17 entries; a 30-designee OFAC action → 5 + 3 = 8 entries.

When sampling, stratify the random pick across `entity_type` (individuals vs entities) and program where possible, so the sample isn't accidentally one-sided. State in the response which entries were selected, the total post-exclusion population, and that the rest are available on request.

### Step 2 — Generate 6–8 variations per name, categorized by failure mode

Each variation must be tagged with the failure mode it tests, so the analyst can read the resulting hit/miss pattern as diagnostic information about their screening tool. Pick 6–8 modes per name from the taxonomy below, biased toward the modes most relevant to that name's origin and structure (e.g., transliteration and script substitution are critical for Arabic/Persian/Russian/Chinese names; legal-form variants matter most for entities).

#### Variation taxonomy

| # | Mode | What it tests | Example: "Mohammad Reza Hosseini" |
|---|---|---|---|
| 1 | **Transposition** | Word-order handling | "Hosseini Mohammad Reza"; "Hosseini, Mohammad Reza" |
| 2 | **Initials / abbreviation** | Partial-string matching | "M. R. Hosseini"; "Mohammad R. Hosseini" |
| 3 | **Spacing & punctuation** | Tokenization edge cases | "Mohammad-Reza Hosseini"; "MohammadReza Hosseini"; "Mohammad  Reza Hosseini" (double space) |
| 4 | **Diacritic & special-character stripping** | Unicode normalization | "Hosseini" → "Hoseyni"; "José" → "Jose"; "Ḥusayn" → "Husayn" |
| 5 | **Transliteration drift** | Phonetic spelling variants — critical for Arabic, Persian, Russian, Chinese names | "Mohammad" → "Muhammad" / "Mohammed" / "Mohamed" / "Muhamad" |
| 6 | **Script substitution** | Non-Latin script handling — render the name in its native script (Arabic, Cyrillic, Chinese, Persian, Hebrew) | "محمد رضا حسینی" |
| 7 | **Common misspelling / typo** | Single-character errors and adjacent-key transpositions | "Hossieni"; "Mohammed Rezza" |
| 8 | **Honorific & title handling** | Prefix noise — Sheikh, Dr., Hajji, Sayyid, Mr., Mullah | "Sheikh Mohammad Reza Hosseini" |
| 9 | **Truncation** | Dropping middle names, suffixes, or one of multiple given names | "Mohammad Hosseini" (drops "Reza") |
| 10 | **Cross-regulator variant** | Same person rendered differently by OFAC / OFSI / EU / UN. When the listed person appears on multiple lists with divergent spellings, each spelling is a separate test row tagged `cross_regulator_variant` with `strong` strength. This is critical for firms screening against multiple lists with one fuzzy threshold. | OFSI "DAGALO" vs OFAC "DAGLO" for the same family |

For **entities**, swap relevant modes for legal-form variants ("LLC" / "L.L.C." / "Ltd" / "Limited" / "Co." / "Company"), Latin/native-script swap, abbreviation of long names, and common ownership-prefix changes ("OAO" / "OOO" / "PJSC" for Russian entities; "JSC" / "Public Joint Stock Company"; etc.).

For **vessels**, vary spacing around "M/V", "M.V.", or "MV"; test the IMO number with and without the "IMO" prefix and with/without spaces; include the previous name if the regulator lists one.

For **aircraft**, vary tail number formatting (with/without dashes; with/without leading country code).

### Step 3 — Tag each variation with an expected match strength

So the analyst knows what their screening tool *should* be doing:

- **exact** — the variation is identical to a string the regulator publishes (the primary name or a listed AKA). A correctly-loaded screening list must catch this. Failure here means the list is stale or not loaded.
- **strong** — close edit distance (1–2 character changes, casing, spacing, diacritics). Should be caught at typical fuzzy thresholds (~85%+).
- **moderate** — transliteration variants, honorific noise, transposition. Should be caught at moderate thresholds (~70–85%).
- **weak** — script substitution, heavy truncation, multi-mode combinations. Tests the upper end of fuzziness or the screening tool's transliteration / non-Latin support.

### Step 4 — Build the spreadsheet

Use the `xlsx` skill to produce a single-sheet workbook. One row per test entry: each original name produces one `exact` row plus 6–8 variation rows, so a typical run with 5 new designees yields 35–45 rows.

Columns, in this order:

| # | Column | Notes |
|---|---|---|
| 1 | `original_name` | Primary name as listed by the regulator |
| 2 | `variation` | The actual test string to feed into screening |
| 3 | `variation_type` | From the taxonomy (`exact`, `transposition`, `transliteration`, etc.) |
| 4 | `expected_match_strength` | `exact` / `strong` / `moderate` / `weak` |
| 5 | `entity_type` | `Individual` / `Entity` / `Vessel` / `Aircraft` |
| 6 | `source_list` | `OFAC SDN` / `OFAC Non-SDN` / `OFSI` / `EU CFSP` |
| 7 | `program` | e.g., `RUSSIA-EO14024`, `SDGT`, `IRAN-HR`, `RUS` (UK), `2014/145/CFSP` (EU) |
| 8 | `designation_date` | YYYY-MM-DD |
| 9 | `aliases_aka` | Semicolon-separated AKAs as published |
| 10 | `dob_or_incorporation` | DOB for individuals; incorporation date for entities (when listed) |
| 11 | `pob_or_place_of_incorporation` | Place of birth (individuals) or place of incorporation (entities) |
| 12 | `nationality_or_jurisdiction` | Nationality or jurisdiction |
| 13 | `address` | Listed address(es), semicolon-separated |
| 14 | `identifiers` | Labeled and pipe-separated, e.g., `Passport: A12345 \| National ID: 1234567890 \| IMO: 9876543` |
| 15 | `regulator_url` | Link to the specific listing or notice page |

Filename: `screening-test-YYYY-MM-DD.xlsx` (use the date the skill is run).

Apply minimal formatting: bold header row, frozen top row, autosize columns. Do not add formulas — this file is a flat data set, not a model.

## Output checklist before delivering

- [ ] Every original name has 1 `exact` row plus 6–8 variation rows
- [ ] Every variation has a `variation_type` and `expected_match_strength`
- [ ] At least one script-substitution row per name when the name has a non-Latin origin
- [ ] Vessels and aircraft are excluded from the default output (or, if a separate set was requested, vessels include IMO and aircraft include tail number)
- [ ] `regulator_url` links to the specific listing or notice, not the regulator's homepage
- [ ] Header row is bold and frozen
- [ ] No empty rows, no merged cells
- [ ] Response notes the vessel/aircraft exclusion and offers a separate set

## Edge cases

- **Same person across multiple regulators with different spellings.** When OFAC, OFSI, and EU all designate the same person with slightly different spellings or DOBs, include each spelling as a separate row with its source list — that divergence *is* the test.
