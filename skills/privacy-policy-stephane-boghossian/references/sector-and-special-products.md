# Verified Reference Pack — Sector Overlays, Security/Breach & Special Product Types

> **Zero-hallucination rule:** cite only from this pack or a live lookup. Several items below were
> "snippet-verified" (the primary host blocked automated fetch but its text was returned by search) or
> flagged UNVERIFIED — those are marked. Do NOT quote statutory damage figures without confirming.
> For ALL sector overlays the skill should FLAG that a specialist/lawyer is needed — do not draft these
> notices generically. Last verified 2026-06.

---

## 1. Security & breach (what to say + the obligations behind it)

### GDPR
- **Art 32 (security of processing):** implement "appropriate technical and organisational measures"
  appropriate to the risk — example measures: pseudonymisation/encryption; confidentiality, integrity,
  availability, resilience; ability to restore after an incident; regular testing/evaluation.
  https://gdpr-info.eu/art-32-gdpr/
- **Art 33 (notify the authority):** "without undue delay and, where feasible, not later than **72
  hours**" after becoming aware, unless unlikely to risk individuals' rights. Processor notifies its
  controller without undue delay. https://gdpr-info.eu/art-33-gdpr/
- **Art 34 (notify individuals):** when the breach is likely to result in a **high risk**, notify
  affected individuals without undue delay in plain language — NOT required if data was encrypted/
  unintelligible, risk was mitigated, or it would be disproportionate effort (then public communication).
  https://gdpr-info.eu/art-34-gdpr/

### United States
- **All 50 states + DC/territories** have breach-notification laws; **no general federal law**. The
  dominant timing standard is **"without unreasonable delay"**; some states add a hard cap (commonly
  cited 30/45/60 days — verify the specific state statute before stating a number; per-state day counts
  are UNVERIFIED here). Encrypted-data exemptions are common. https://www.ncsl.org/technology-and-communication/security-breach-notification-laws

### Recommended security clause language (truthful, non-absolute)
- "We implement reasonable administrative, technical, and physical safeguards designed to protect your
  personal information." Reference specific controls (encryption in transit/at rest, access controls)
  **only if actually true** — false security claims are FTC-deceptive.
- Always include the hedge: "No method of transmission or storage is 100% secure; we cannot guarantee
  absolute security." **Ban** "military-grade," "bank-grade," "fully secure," "guaranteed."
- A breach-response line: "we will notify you and/or regulators as required by applicable law."

---

## 2. Children's products
- **COPPA** (16 CFR Part 312): under-13 audiences need online notice + **direct parental notice** +
  **verifiable parental consent before collection**, data-minimization, retention limits, parental
  review/delete. 2025 amendments (compliance by **Apr 22, 2026**): biometric + gov-ID are now PI;
  **separate consent for third-party disclosure**; **no indefinite retention**; new VPC methods.
  https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312
- **GDPR Art 8:** digital age of consent default **16**, member states may lower to **13**; parental
  authorisation below the threshold. https://gdpr-info.eu/art-8-gdpr/
- **UK Age-Appropriate Design Code ("Children's Code"):** applies to any online service **likely to be
  accessed by under-18s** in the UK; 15 standards incl. high-privacy by default, geolocation & profiling
  off by default, no dark patterns, age-appropriate notices.
  https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/

> Any children's product → **HARD "get a lawyer before publishing" flag.**

---

## 3. Health / wellness
- **HIPAA applies only to covered entities / business associates** — most direct-to-consumer health/
  fitness apps are NOT HIPAA-covered. If covered: a separate **Notice of Privacy Practices** is required
  (a website privacy policy ≠ a HIPAA NPP).
- **FTC Health Breach Notification Rule (HBNR, 16 CFR Part 318)** fills the non-HIPAA gap: vendors of
  personal health records / health apps must notify affected individuals + the FTC of breaches of
  **unsecured** identifiable health data **within 60 calendar days** (500+ people → notify FTC within 10
  business days; 500+ in one locale → notify prominent media). 2024 amendments confirm health apps/
  connected devices are in scope. https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0
- **Washington My Health My Data Act (MHMDA, RCW 19.373):** protects consumer health data outside HIPAA;
  **opt-in consent** to collect, **separate consent to share**, signed **authorization to sell**;
  requires a **stand-alone Consumer Health Data Privacy Policy** (separate doc, homepage-linked, only the
  Act-required content, naming specific affiliates). https://app.leg.wa.gov/RCW/default.aspx?cite=19.373&full=true

> Health/PHI → **HARD lawyer flag**; if biometric/genetic too, see §5.

---

## 4. Fintech
- **GLBA Financial Privacy Rule:** "financial institutions" must give a clear written privacy notice at
  the start of the relationship + **annually**, explain sharing, and offer an **opt-out** before sharing
  NPI with certain nonaffiliated third parties; the **Safeguards Rule** mandates a written infosec program.
  https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act
- **PCI-DSS** is **contractual** (card networks), not a statute, and not itself a privacy-policy
  disclosure — but commonly referenced. (Characterization is general knowledge — confirm before relying.)

> Fintech/payments beyond a standard processor → **HARD lawyer flag.**

---

## 5. Biometric
- **Illinois BIPA (740 ILCS 14):** requires a **publicly available written policy** with a **retention
  schedule + destruction guidelines** (destroy when purpose satisfied or within **3 years** of last
  interaction, whichever first); written notice + **written release** before collection; restricts
  disclosure/sale. **Private right of action** with statutory damages — the major litigation driver
  (do NOT cite specific damage figures). https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3004&ChapterID=57
- **Texas CUBI (Bus. & Com. §503.001):** inform + consent **before capture** (consent need not be
  written); destroy within ~1 year after purpose expires; **no private right of action** (Texas AG
  enforces; civil penalty up to $25,000/violation). https://statutes.capitol.texas.gov/Docs/BC/htm/BC.503.htm
- **Washington (RCW 19.375):** notice/consent before enrolling a biometric identifier for commercial
  purposes (UNVERIFIED specifics this run).

> Biometric data → **HARD lawyer flag** (esp. IL/TX/WA).

---

## 6. Browser extensions
- **Chrome Web Store Developer Program (Privacy + Limited Use):** any extension handling user data needs
  an accurate, up-to-date privacy policy disclosing collection/use/sharing + **all parties**; the
  **Limited Use** policy restricts data to disclosed practices; collecting **web-browsing activity is
  prohibited** except where required for a prominently-described user feature; an affirmative compliance
  statement re: Google API data is required. https://developer.chrome.com/docs/webstore/program-policies/limited-use

---

## 7. IoT / connected devices
- **California SB-327 (Civil Code §§1798.91.04-.06):** manufacturers of connected devices must include
  **reasonable security features** (e.g., unique per-device password or forced password change on first
  use). It's a **security** mandate on manufacturers, not a privacy-disclosure rule; no private right of
  action. https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201720180SB327
- IoT data-minimisation is GDPR best practice (Art 5(1)(c)), not an SB-327 requirement. Federal **IoT
  Cybersecurity Improvement Act 2020** is federal-procurement only (UNVERIFIED this run).

---

## 8. Location-based services
- **CCPA/CPRA:** **precise geolocation** (within ~1,850 ft) is **sensitive personal information** →
  consumers can **limit** its use; disclose collection, purpose, sensitive treatment, and the "Limit Use
  of My Sensitive Personal Information" opt-out. Under GDPR, precise location tied to a person is personal
  data and often needs consent. https://oag.ca.gov/privacy/ccpa

---

## 9. Ed-tech
- **FERPA** governs schools/institutions receiving federal funds; enforced against the institution (DOE).
- **California SOPIPA:** direct liability on K-12 online operators — **no targeted ads to students, no
  selling student data, no non-educational profiling**; reasonable security; **delete on school request**.
  https://iapp.org/news/a/state-student-privacy-laws-a-game-changer-for-service-providers
- COPPA also applies to ed-tech for under-13s (schools may provide consent in the educational context —
  UNVERIFIED specifics this run).

> Ed-tech for minors → **HARD lawyer flag** (FERPA + SOPIPA + COPPA stack).

### Primary sources (verified / snippet-verified)
- GDPR Art 32/33/34/8: https://gdpr-info.eu/
- NCSL US breach laws: https://www.ncsl.org/technology-and-communication/security-breach-notification-laws
- COPPA: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312
- FTC HBNR: https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0
- Washington MHMDA: https://app.leg.wa.gov/RCW/default.aspx?cite=19.373&full=true
- GLBA: https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act
- BIPA: https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3004&ChapterID=57 · Texas CUBI: https://statutes.capitol.texas.gov/Docs/BC/htm/BC.503.htm
- Chrome Web Store: https://developer.chrome.com/docs/webstore/program-policies/limited-use
- CA SB-327 (IoT): https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201720180SB327
- UK Children's Code: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/
