# new-designation-screening-test

A Claude skill that turns each fresh round of OFAC, OFSI, and EU sanctions designations into a screening test set for analyst review — original names, deliberate variations, and the metadata an analyst needs to interpret hits and misses.

## What it does

When invoked, the skill:

1. Pulls newly designated names from OFAC's Recent Actions, the OFSI consolidated list / notices, and the EU CFSP consolidated list over a chosen lookback window (default: trailing 7 days).
2. Generates 6–8 deliberate variations of each name, each tagged with the **failure mode** it probes: transposition, initials, spacing/punctuation, diacritic stripping, transliteration drift, script substitution, common misspellings, honorifics, truncation.
3. Tags every row with an **expected match strength** (`exact` / `strong` / `moderate` / `weak`) so the resulting hit/miss pattern reads as diagnostic information about the screening tool, not just a pass/fail.
4. Outputs a single-sheet `.xlsx` the compliance team can load into their screening engine for testing.

## Who it's for

Sanctions and financial-crime compliance teams who need to:

- Verify their screening list is current after a designation update.
- Run a regression test set against their screening tool.
- Calibrate fuzzy-match thresholds against realistic name variations rather than synthetic noise.

## How to use

Add the skill to Claude (place this folder under your skills directory), then ask Claude something like:

- "Generate sanctions list update test data for this week."
- "Build me a screening regression set from the latest OFAC and OFSI additions."
- "Test my screening list — has it caught the new EU designations from the last 14 days?"

## Output format

A single-sheet `.xlsx` with one row per test entry. Columns:

| # | Column | Description |
|---|---|---|
| 1 | `original_name` | Primary name as listed by the regulator |
| 2 | `variation` | The actual test string to feed into screening |
| 3 | `variation_type` | `exact`, `transposition`, `transliteration`, etc. |
| 4 | `expected_match_strength` | `exact` / `strong` / `moderate` / `weak` |
| 5 | `entity_type` | Individual / Entity / Vessel / Aircraft |
| 6 | `source_list` | OFAC SDN / OFAC Non-SDN / OFSI / EU CFSP |
| 7 | `program` | Sanctions program / authority |
| 8 | `designation_date` | YYYY-MM-DD |
| 9 | `aliases_aka` | Semicolon-separated AKAs |
| 10 | `dob_or_incorporation` | DOB or incorporation date |
| 11 | `pob_or_place_of_incorporation` | Place of birth or incorporation |
| 12 | `nationality_or_jurisdiction` | Nationality or jurisdiction |
| 13 | `address` | Listed address(es) |
| 14 | `identifiers` | Pipe-separated IDs (passport, national ID, tax ID, IMO, tail number) |
| 15 | `regulator_url` | Direct link to the listing or notice |

See [`examples/sample_output.xlsx`](./examples/sample_output.xlsx) for a worked example with three illustrative designations (one Iranian individual, one Russian entity, one vessel).

## Variation taxonomy

The skill probes ten common failure modes in screening systems:

1. **Transposition** — word-order changes (`Lee John` from `John Lee`)
2. **Initials / abbreviation** — `J. Lee`, `John L.`
3. **Spacing & punctuation** — hyphens collapsed or added, doubled spaces, missing spaces
4. **Diacritic & special-character stripping** — `José` → `Jose`
5. **Transliteration drift** — `Mohammad` / `Muhammad` / `Mohammed` / `Mohamed`
6. **Script substitution** — name rendered in Arabic, Cyrillic, Chinese, Persian, or Hebrew
7. **Common misspellings / typos** — single-character substitutions, adjacent-key transpositions
8. **Honorifics & titles** — Sheikh, Dr., Hajji, Sayyid, Mullah
9. **Truncation** — dropping middle names, suffixes, or one of multiple given names
10. **Cross-regulator variant** — same person spelled differently by OFAC / OFSI / EU / UN (e.g., DAGALO vs DAGLO)

See [SKILL.md](./SKILL.md) for the full taxonomy with examples and tagging rules.

## Limitations

- Output reflects what the regulator had published on the source pages at run time. Holiday weekends, system outages, or late "What's New" PDFs will be reflected as gaps.
- Variation generation is heuristic. The skill picks modes based on name origin and structure, which is a judgment call — pair the output with a sanctions analyst's review before treating it as exhaustive.
- v1 covers OFAC, OFSI, and EU. UN, Canada (SEMA), Australia (DFAT/Consolidated List), Switzerland (SECO), and Japan are out of scope.
- **Default scope: individuals and entities only.** Vessels and aircraft are excluded by default since most financial-transaction screening doesn't surface ship or aircraft names. Vessel/aircraft test data is relevant for trade finance, ship/aircraft financing, marine and aviation insurance, shipping and logistics firms, and port operators — request explicitly to generate a separate set for those entity types.
- Match-strength tags reflect general behavior of name-matching algorithms, not any specific vendor (LexisNexis, Dow Jones, Refinitiv World-Check, ComplyAdvantage, etc.). Calibrate against your own engine's score distribution.

## License

MIT — see [LICENSE](./LICENSE).

## Disclaimer

This tool is provided for testing, research, and educational purposes only. It is not a sanctions screening system, does not constitute legal, regulatory, or compliance advice, and is not a substitute for an independent sanctions compliance program or the judgment of a qualified compliance professional. Outputs are heuristic and may contain errors, omissions, or inaccuracies, including in the variation generation and expected match strength tags. Users are solely responsible for their own regulatory obligations and for independently validating any output before relying on it for any compliance, business, or operational decision. No warranty of accuracy, completeness, fitness for a particular purpose, or regulatory sufficiency is made or implied. Sanctrust and the contributors disclaim all liability arising from use of this tool to the fullest extent permitted by law.

## Author

Built and maintained by **Sanctrust** ([sanctrust.com](https://sanctrust.com)).

Issues and pull requests welcome.
