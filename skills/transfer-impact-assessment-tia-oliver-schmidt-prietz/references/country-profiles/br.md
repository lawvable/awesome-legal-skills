# Brazil — TIA Country Profile

Last verified: 2026-05-29

## Adequacy Status

**Adequacy:** None. No formal EU adequacy proceeding is open as of 2026-05. Art. 46 + TIA required.

## Data Protection Framework

**General law:** Lei Geral de Proteção de Dados (LGPD) — Law 13,709/2018, effective 18 September 2020. Closely modelled on GDPR (legal bases, rights, controller/processor distinction, DPO).

**Supervisory authority:** Autoridade Nacional de Proteção de Dados (ANPD). Independent agency since 2022 reorganisation. Increasing enforcement activity.

**Data subject rights:** Confirmation, access, correction, anonymisation/blocking/deletion, portability, information on sharing, withdrawal of consent, opposition. Substantively similar to GDPR.

**Effective remedies:** ANPD administrative process + judicial proceedings. Administrative fines under LGPD Art. 52 of up to 2% of the entity's (or group's) revenue in Brazil in the prior fiscal year, capped at BRL 50 million per infraction; plus daily fines, publicity of the violation, blocking/deletion of data, and partial/total suspension of processing.

## Surveillance & Government Access Laws

### Marco Civil da Internet (Law 12,965/2014)

**Scope:** Internet civil framework. Article 7 establishes user rights including inviolability and confidentiality of communications.

**Government access:** A judicial order is required to obtain stored connection/access logs (Marco Civil Art. 22); real-time interception of communications *content* is governed by the Wiretap Law (Lei 9.296/1996), which also requires a judicial order. Limited bulk surveillance by design.

**Guarantee A — Clear, precise, accessible rules:** **Adequate.** Statutory framework with judicial process.

**Guarantee B — Necessary and proportionate:** **Adequate.** Judicial order requirement provides proportionality control.

**Guarantee C — Independent oversight:** **Adequate.** Judiciary as oversight; STF (Supreme Court) plays active role.

**Guarantee D — Effective remedies:** **Adequate.** Habeas data action, civil claims, ANPD process.

### Anti-Terrorism Law (Law 13,260/2016)

**Scope:** Targeted investigative powers for terrorism cases. Judicial authorisation required.

**Profile:** Narrower than US/Chinese counterparts; constitutional protections apply.

### Brazilian Intelligence System (Sisbin)

**Scope:** Sistema Brasileiro de Inteligência, established by Law 9,883/1999 (which also created ABIN). Intelligence coordination framework; operations subject to Brazilian constitutional protections.

## Practical Risk Factors

- Brazilian constitutional framework (1988 Constitution) provides robust privacy protections
- STF active on data protection — in ADI 6387 et al. (May 2020) it suspended Provisional Measure 954/2020, which had required telecom operators to share subscriber data with the statistics agency IBGE during COVID, recognising informational self-determination as a constitutionally protected right (later made express in Art. 5, LXXIX, by Constitutional Amendment 115/2022)
- Lower realistic risk of state access compared to high-surveillance jurisdictions
- Major providers report comparatively low government request volumes for Brazilian data

## Recommended Supplementary Measures

For most Brazil transfers, supplementary measures are advisable but the gaps are modest:

- **TM-1** (encryption) — defence-in-depth for sensitive data
- **CM-1** (transparency obligation)
- **OM-2** (access controls) and **OM-3** (request handling policy)

**When NOT effective:** TM-1 helps only where the Brazilian importer does not need plaintext; CM-1 gives no protection where a judicial order imposes secrecy; OM-3 has no force against a valid court order. For ordinary commercial data the residual risk is low — but state these limits rather than implying the measures fully close the gap.

## TIA Output

For Brazil transfers:
- Section 3 Block A: LGPD provides robust framework
- Section 3 Block B: surveillance laws have judicial process; concerns are limited
- Section 3 conclusion: typically (1) for ordinary cases; (2) with light supplementary measures for sensitive data

## Key Sources

- LGPD (Law 13,709/2018)
- Marco Civil da Internet (Law 12,965/2014)
- ANPD regulations and decisions
- STF jurisprudence on data protection
- Brazilian Constitution Arts. 5(X), 5(XII), and 5(LXXIX) (express data-protection right, added by Constitutional Amendment 115/2022)
- Wiretap Law (Lei 9.296/1996); Sisbin / ABIN (Law 9,883/1999)
