# Russia — TIA Country Profile

Last verified: 2026-05-29

## Adequacy Status

**Adequacy:** None. Art. 46 + TIA required, but in practice transfers to Russia are heavily restricted by EU sanctions (since 2022) and by Russian data localisation requirements. **In most cases, transfers to Russia should be assessed as not permissible.**

## Sanctions Context

EU sanctions packages since 24 February 2022 restrict numerous categories of trade and services with Russia. The TIA cannot authorise a transfer that is otherwise prohibited under sanctions law. Verify sanctions compliance BEFORE running the TIA.

## Data Protection Framework

**General law:** Federal Law 152-FZ on Personal Data (2006, as amended). Provides notice, consent, security obligations, data subject rights — but operates under significant state-access carve-outs.

**Supervisory authority:** Roskomnadzor (Federal Service for Supervision of Communications, Information Technology and Mass Media). Executive agency; not independent.

**Data subject rights:** Access, correction, deletion (limited), withdrawal of consent. Practical effectiveness against state actors is very limited.

**Effective remedies:** Roskomnadzor complaints + court proceedings. Practical effectiveness against state surveillance: very limited.

## Surveillance & Government Access Laws

### SORM (System for Operative Investigative Activities)

**Scope:** All Russian telecommunications and internet providers must install SORM equipment giving FSB direct, real-time access to communications and data.

**Powers:** Direct access, no per-request authorisation from providers; warrants required by law but not visible to providers.

**Guarantee A — Clear, precise, accessible rules:** **Insufficient.** Implementing rules partly classified.

**Guarantee B — Necessary and proportionate:** **Insufficient.** Bulk access by design.

**Guarantee C — Independent oversight:** **Insufficient.** No independent oversight; judicial role nominal.

**Guarantee D — Effective remedies:** **Insufficient.** ECtHR (Roman Zakharov v. Russia, 2015) found the Russian interception regime in breach of ECHR Article 8. Russia was expelled from the Council of Europe on 16 March 2022 and ceased to be a party to the ECHR on 16 September 2022 — removing the Zakharov-style remedy avenue for any future interception.

### "Yarovaya Law" (2016 amendments)

**Scope:** Compelled data retention by telecommunications and online services; mandatory decryption capability.

**Profile:** Insufficient across all four guarantees.

### Federal Law 242-FZ — Data Localisation

**Scope:** Personal data of Russian citizens must be initially processed (collected and recorded) in databases located in Russia.

**Implication:** Affects controllers offering services to Russian data subjects; localised data sits physically within reach of SORM/FSB direct access.

### Sovereign Internet Law 2019

**Scope:** Centralised control over Russian internet routing and DNS, with provider obligations.

## Practical Risk Factors

- SORM gives FSB structurally unrestricted access to any data on Russian providers
- Major Russian providers are subject to direct state cooperation requirements
- Yarovaya Law expanded data retention and decryption mandates
- ECtHR Roman Zakharov v. Russia confirmed the regime violates ECHR; Russia was expelled from the Council of Europe (16 March 2022) and ceased to be an ECHR party (16 September 2022)
- EU sanctions further restrict permissible engagements

## Recommended Supplementary Measures

In most cases, NO combination of supplementary measures can close the essential guarantee gaps. SORM provides direct state access; encryption with exporter-held keys is partially protective only if the importer never needs plaintext.

**Realistic outcome:** Transfers to Russia should generally be suspended unless:
- Sanctions compliance is verified
- The transfer is necessary for narrow legitimate purposes (e.g., personal communications, humanitarian)
- Art. 49 derogations apply on the specific facts

## TIA Output

For Russia transfers:
- Section 0: verify EU sanctions compliance FIRST
- Section 3 Block A: 152-FZ provides framework but state actors carved out
- Section 3 Block B: all four guarantees insufficient
- Section 3 Block C: SORM means realistic risk is high for any data
- Section 3 conclusion: typically suspend; narrow Art. 49 exceptions may apply

## Key Sources

- Federal Law 152-FZ on Personal Data
- Federal Law 242-FZ (data localisation)
- Yarovaya Law (2016 amendments)
- Sovereign Internet Law 2019
- Roman Zakharov v. Russia (ECtHR, Grand Chamber, 4 December 2015) — ECHR finding
- EU sanctions regulations (Regulations 269/2014, 833/2014, and subsequent packages)
