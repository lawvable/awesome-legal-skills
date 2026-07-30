# United Arab Emirates — TIA Country Profile

Last verified: 2026-05-29

## Adequacy Status

**Adequacy:** None. Art. 46 + TIA required.

## Data Protection Framework

**Layered framework — critical to identify which regime applies:**

### Federal level
- Federal Decree-Law No. 45 of 2021 on Personal Data Protection (PDPL). Mainland UAE.
- UAE Data Office (UDO) as federal authority.
- Implementing regulations still phasing in.

### DIFC (Dubai International Financial Centre)
- DIFC Data Protection Law DIFC Law No. 5 of 2020. GDPR-aligned.
- DIFC Commissioner of Data Protection. Genuine independent regulator.
- No EU Commission Art. 45 adequacy decision exists for DIFC. DIFC runs its *own* outbound-transfer adequacy list (~43 jurisdictions recognised by the DIFC Commissioner) and has been pursuing EU/UK adequacy — but transfers **into** DIFC from the EEA still require an Art. 46 tool + TIA. DIFC's GDPR-alignment does NOT equal EEA adequacy.

### ADGM (Abu Dhabi Global Market)
- Data Protection Regulations 2021. GDPR-aligned.
- ADGM Office of Data Protection.

**Critical step:** Identify whether the UAE importer is in DIFC, ADGM, or mainland UAE. The applicable regime — and thus the TIA — differ substantially.

## Data Protection Framework — by regime

**DIFC:** Substantively equivalent to GDPR. Data subject rights, controller/processor distinction, breach notification, DPO requirements.

**ADGM:** Substantively equivalent to GDPR.

**Mainland UAE (PDPL):** GDPR-influenced but distinct. Consent-heavy; cross-border transfer rules under Articles 22–23 (Art. 22 adequacy-based transfers; Art. 23 transfers absent adequacy via contract/consent/necessity derogations).

## Surveillance & Government Access Laws

### UAE Federal — Cybercrimes Law (Federal Decree-Law No. 34 of 2021)

**Scope:** Principally a substantive offences statute (cybercrimes, online content) with provider-cooperation duties — not the core lawful-interception authority.

**Powers:** The operative compelled-access mechanisms sit elsewhere: telecom interception under TDRA (Telecommunications and Digital Government Regulatory Authority) regulation, compelled disclosure under the Penal Code / Criminal Procedure Law, and the State Security Apparatus's statutory mandate. Identify the specific instrument for the importer's sector.

**Guarantee A — Clear, precise, accessible rules:** **Concerns.** Broad framing of national security offences.

**Guarantee B — Necessary and proportionate:** **Concerns.**

**Guarantee C — Independent oversight:** **Insufficient.** Judiciary not fully independent of executive.

**Guarantee D — Effective remedies:** **Insufficient.**

### State Security framework

**Scope:** The State Security Apparatus (federal) holds broad surveillance authority for national security under its institutional/decree-based mandate (not a publicly accessible statute in the Schrems II sense); access can be non-transparent and judicial remedy is weak.

**Profile:** Insufficient across all four guarantees.

### DIFC and ADGM regimes

**Scope:** DIFC and ADGM have more limited surveillance applicability — federal security laws can still apply but the DIFC/ADGM regulatory structures provide some insulation.

## Practical Risk Factors

- DIFC and ADGM importers benefit from more bounded surveillance applicability
- Mainland UAE importers operate under broader federal security frameworks
- Sectoral targeting: defence, security, political dissent are higher-risk subjects
- Routine commercial transfers (B2B SaaS, HR) lower risk profile
- Identity of importer's beneficial ownership and jurisdiction critical

## Recommended Supplementary Measures

**For DIFC/ADGM importers:**
- **TM-1** (encryption) — defence-in-depth
- **CM-1** (transparency obligation)
- **OM-3** (request handling policy)

**For mainland UAE importers:**
- Above + **TM-2** (pseudonymisation) where viable
- **CM-2** (challenge clause)
- Consider whether DIFC/ADGM alternative is feasible

**When NOT effective (mainland UAE):** Transparency/challenge clauses (CM-1/CM-2) give little protection against State Security access where notification can be barred and judicial remedy is weak; encryption (TM-1) only helps where the importer never needs plaintext. For sensitive data to mainland UAE, supplementary measures may be insufficient and suspension is the honest outcome.

## TIA Output

For UAE transfers:
- Section 1: clearly identify DIFC/ADGM/mainland
- Section 3 Block A: substantially different by regime
- Section 3 Block B: federal surveillance laws apply across regimes; DIFC/ADGM partially insulating
- Section 3 conclusion: (1) or (2) for DIFC/ADGM with low-sensitivity data; (2) with stronger measures for mainland UAE; suspend for sensitive data without effective mitigation

## Key Sources

- Federal Decree-Law No. 45 of 2021 (UAE PDPL)
- DIFC Data Protection Law (DIFC Law No. 5 of 2020)
- ADGM Data Protection Regulations 2021
- Federal Decree-Law No. 34 of 2021 (Cybercrimes Law)
- DIFC Commissioner of Data Protection guidance
- UDO guidance
