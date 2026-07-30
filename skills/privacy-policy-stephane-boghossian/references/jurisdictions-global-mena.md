# Verified Reference Pack — Global (non-EU/US) + MENA

> **Zero-hallucination rule:** cite only from this pack or a live `legal-data-hunter` lookup. Name laws
> in plain terms and describe obligations functionally; do not invent article numbers, penalty amounts,
> or effective dates beyond what is sourced here. Local-language and local-counsel review is strongly
> advised for every jurisdiction in this file. Last verified 2026-06.

These regimes converge on a **common core** (see §Synthesis). Build to the common core, then branch on
the per-jurisdiction divergences flagged below.

---

## Brazil — LGPD (Lei Geral de Proteção de Dados); regulator: ANPD
- LGPD has strong **transparency** duties; a published **privacy policy** is the standard way to meet
  them. **10 legal bases** (broader than GDPR's six; includes "legitimate interest," "credit
  protection," "regular exercise of rights").
- Data-subject rights: confirmation of processing, access, correction, anonymization/blocking/deletion,
  portability, information about sharing, info on consequences of refusing consent, revoke consent.
- A **DPO (encarregado)** is generally required. Cross-border transfers permitted to adequate countries
  or with safeguards (SCCs/BCRs as ANPD operationalizes them).
- Source: https://www.dlapiperdataprotection.com/index.html?t=law&c=BR · https://iapp.org/news/a/an-overview-of-brazils-lgpd

## Canada — federal PIPEDA + Quebec Law 25
- **PIPEDA** (federal, private sector): built on **10 fair-information principles**; the **Openness**
  principle requires making privacy policies/practices readily available; **meaningful consent**.
  (Federal reform — Bill C-27/CPPA — has been in flux; verify current status before citing it.)
- **Quebec Law 25** (Act respecting the protection of personal information in the private sector): **§8.2
  requires anyone who collects personal information through technology to publish a confidentiality
  (privacy) policy in clear and simple language.** Stricter than the rest of Canada: **privacy by
  default**, granular **consent specific to each purpose**, mandatory **privacy impact assessments** for
  certain projects, transfer assessments, breach reporting, and a **person in charge of protection**
  (a DPO-equivalent, by default the highest-ranking person). Source:
  https://www.legisquebec.gouv.qc.ca/en/document/cs/p-39.1 · https://www.onetrust.com/blog/quebecs-law-25-what-is-it-and-what-do-you-need-to-know/

## Australia — Privacy Act 1988 + Australian Privacy Principles (APPs)
- **APP 1 (open and transparent management)** requires a **clearly expressed and up-to-date APP privacy
  policy** with specified content: the kinds of personal information collected/held, how it's collected
  and held, the purposes, how individuals can access/correct it and **complain**, and whether information
  is likely to be disclosed **overseas** (and to which countries).
- **APP 5 (collection notice)** requires notifying individuals of specified matters at/around collection
  (a notice is distinct from the policy).
- **2024–2025 reforms** added (e.g.) a statutory tort for serious invasions of privacy and transparency
  duties around automated decisions — verify specifics/timing before citing. Source:
  https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines (Ch. 1 & Ch. 5)

## India — DPDP Act 2023 + DPDP Rules 2025
- A **Data Fiduciary** must give the **Data Principal a standalone notice** (separate, plain-language)
  with/before a consent request: an **itemized description of the personal data**, the **purposes**, and
  a **link/means to withdraw consent, exercise rights, and complain to the Data Protection Board of
  India**. Notice must be available in **English + the 22 scheduled Indian languages**.
- Consent must be **free, specific, informed, unconditional, unambiguous**, via clear affirmative action;
  **Consent Managers** are a defined role. Cross-border transfers via a "negative list" model.
- Source: https://www.ey.com/en_in/insights/cybersecurity/decoding-the-digital-personal-data-protection-act-2023 ·
  https://www.hoganlovells.com/en/publications/india-publishes-consent-management-rules-under-digital-personal-data-protection-act

## China — PIPL (Personal Information Protection Law)
- Notice (Art 17) must state the handler's identity/contact, purposes & methods, categories, retention,
  and how individuals exercise rights — in clear, easily-understood language. **Separate consent** (Art
  23/25/39) is required for: sharing with third parties, processing **sensitive** PI, **public
  disclosure**, and **cross-border transfer**. "Separate consent" must be specific and explicit and
  **cannot be bundled** — checkbox consent to a general privacy policy is NOT sufficient.
- Cross-border transfer requires one of: a **CAC security assessment**, **CAC standard contract**, or
  **certification**, plus the Art-39 separate consent + notice of the foreign recipient's identity,
  purposes, categories, and how to exercise rights against them. Source:
  https://www.china-briefing.com/doing-business-guide/china/company-establishment/pipl-personal-information-protection-law ·
  https://iapp.org/news/a/top-5-operational-impacts-of-chinas-pipl-part-1-scope-key-definitions-and-lawful-handling-of-personal-information

## Other notable (brief — verify specifics before citing)
- **Japan — APPI**: notice of purpose of use; consent for sensitive data and most third-party provision;
  cross-border consent/adequacy.
- **South Korea — PIPA**: among the strictest; detailed consent (often opt-in, itemized), data-localization
  sensitivities, breach notice.
- **South Africa — POPIA**: 8 conditions for lawful processing; an Information Officer; notice at collection.
- **Switzerland — revFADP** (in force Sept 2023): GDPR-aligned; needs its own controller/representative
  handling; a Swiss-specific privacy notice.
- **Also exist (flag, don't draft):** Nigeria NDPA, Thailand PDPA, Singapore PDPA, New Zealand Privacy Act 2020.

---

## MENA (priority region)

> Note: **UAE PDPL does not apply inside the DIFC or ADGM free zones** — each has its own regime. Get the
> free zone vs onshore distinction right. Arabic-language versions are expected/required for several
> jurisdictions (see `structure-clauses-and-craft.md` for RTL/Arabic build rules).

- **UAE — Federal Decree-Law No. 45 of 2021 (PDPL):** controllers must process transparently and disclose
  via formal policies/privacy notices; **explicit, specific, freely-given, unambiguous, revocable consent**
  (affirmative action) is the baseline; cross-border transfers allowed to adequate countries or with
  appropriate safeguards (contractual clauses/BCRs) or via exceptions (e.g., explicit consent, contract
  necessity). The **Executive Regulations** have been pending — verify their status before citing details.
  Source: https://uaelegislation.gov.ae/en/legislations/1972/download · https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws
- **DIFC — Data Protection Law No. 5 of 2020:** **GDPR-aligned**; enhanced transparency information
  requirements substantially in line with GDPR; transfers need an adequate level of protection as
  determined by the Commissioner. Effective 1 July 2020 (enforceable 1 Oct 2020). Source:
  https://www.difc.com/business/registrars-and-commissioners/commissioner-of-data-protection
- **ADGM — Data Protection Regulations 2021:** separate GDPR-aligned regime in the Abu Dhabi Global Market.
- **Saudi Arabia — PDPL (SDAIA):** in effect **14 Sept 2023**, with a **one-year grace period (compliance
  by 14 Sept 2024)**. A controller must use a **privacy policy** to make required information available;
  policies should be **comprehensive, plain, and available in Arabic and English** where appropriate.
  Cross-border transfer is restricted: needs adequacy (SDAIA has not yet published an official adequacy
  list), **SDAIA-approved SCCs/BCRs**, or an exception (e.g., explicit consent), plus a **risk assessment**
  for continuous/large-scale sensitive transfers. Registration obligations may apply. Source:
  https://sdaia.gov.sa/en/SDAIA/about/Pages/PersonalDataProtection.aspx · https://www.dlapiperdataprotection.com/?c=SA ·
  https://cms-lawnow.com/en/ealerts/2025/09/one-year-anniversary-saudi-personal-data-protection-law
- **Also (flag, verify before citing specifics):** **Bahrain PDPL**, **Qatar PDPPL**, **Egypt Law 151/2020**
  (executive regs status to confirm), **Turkey KVKK** (GDPR-adjacent; registration with VERBIS for some).

---

## Cross-jurisdiction synthesis (build strategy)

**The common core that satisfies *most* laws** (build this in every policy):
1. Who you are + contact (controller identity).
2. What data you collect, by category.
3. Why (purposes) + (where required) the legal basis/consent.
4. Who you share it with (recipients/categories).
5. Whether/where it's transferred internationally + the safeguard.
6. How long you keep it (retention).
7. The individual's rights + how to exercise them + how to complain.
8. Cookies/tracking + consent.
9. Security (in general terms) + breach handling.
10. Children handling.
11. Automated decisions/AI (if any).
12. Effective date + how changes are notified.

**The key divergences to branch on:**
- **Consent model:** opt-IN by default (EU, China sensitive/cross-border, Quebec, India, Korea, most
  sensitive-data cases) vs opt-OUT (US CCPA "sale/share"). When unsure of the audience → use opt-IN
  (strictest).
- **Separate/explicit consent** for specific acts (China cross-border & sensitive; sensitive data under GDPR Art 9; sale of sensitive in US).
- **Local representative / DPO / registration:** EU/UK rep (Art 27), DPO (GDPR/Brazil/Quebec "person in
  charge"), Turkey VERBIS, Saudi registration — ask, never assume one exists.
- **Data localization / transfer friction:** China (CAC), Saudi/Russia/India nuances — disclose transfer
  mechanism and host country.
- **Breach notification specifics:** GDPR 72h to authority / high-risk to individuals; US = all 50 states,
  mostly "without unreasonable delay"; many others have their own clocks (see `sector-and-special-products.md`).
- **Children's age threshold:** 13 (US COPPA, UK, several EU states) vs 16 (GDPR default, several EU states)
  vs local rules — ask the target country.
- **Language:** provide the notice in the audience's language; **Arabic** for Saudi/UAE-onshore and MENA
  consumer audiences (RTL build rules apply).

### Primary sources (verified)
- DLA Piper "Data Protection Laws of the World" (per-country): https://www.dlapiperdataprotection.com/
- Brazil LGPD: https://www.dlapiperdataprotection.com/index.html?t=law&c=BR
- Quebec Law 25: https://www.legisquebec.gouv.qc.ca/en/document/cs/p-39.1
- Australia APPs: https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines
- India DPDP: https://www.ey.com/en_in/insights/cybersecurity/decoding-the-digital-personal-data-protection-act-2023
- China PIPL: https://www.china-briefing.com/doing-business-guide/china/company-establishment/pipl-personal-information-protection-law
- UAE PDPL: https://uaelegislation.gov.ae/en/legislations/1972/download · DIFC: https://www.difc.com/business/registrars-and-commissioners/commissioner-of-data-protection
- Saudi PDPL: https://www.dlapiperdataprotection.com/?c=SA
