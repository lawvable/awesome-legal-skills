# Germany (DSGVO + BDSG + TDDDG)

## Table of Contents
1. [Legal Framework](#legal-framework)
2. [Supervisory Authorities](#supervisory-authorities)
3. [Language & Formalities](#language--formalities)
4. [Legal Bases — German Specifics](#legal-bases)
5. [Retention Periods](#retention-periods)
6. [Cookie & Tracking Rules (TDDDG)](#cookie--tracking-rules)
7. [Children's Data](#childrens-data)
8. [DPO Requirements](#dpo-requirements)
9. [Standard Wording Templates](#standard-wording)

---

## Legal Framework

| Law | Scope |
|-----|-------|
| **DSGVO** (= GDPR) | Directly applicable EU regulation |
| **BDSG** (Bundesdatenschutzgesetz) | Federal supplementary law; employee data (§ 26), DPO (§ 38), scoring (§ 31), video surveillance (§ 4) |
| **TDDDG** (Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz) | Cookie consent (§ 25), telecom/digital services privacy — replaced TTDSG (which had replaced TMG/TKG provisions) |
| **UWG** (Gesetz gegen den unlauteren Wettbewerb) | Relevant for direct marketing / commercial email consent |
| **HGB / AO** | Commercial and tax law retention obligations |

## Supervisory Authorities

Germany has **18 supervisory authorities** (1 federal BfDI + 16 Landesdatenschutzbeauftragte + 1 church-specific BfD EKD).

When drafting, reference the correct authority based on the controller's registered seat:

| State | Authority | Abbreviation |
|-------|-----------|-------------|
| Federal (telecom, postal, federal bodies) | BfDI | Bundesbeauftragter für den Datenschutz |
| Baden-Württemberg | LfDI BW | |
| Bayern (private sector) | BayLDA | Bayerisches Landesamt für Datenschutzaufsicht |
| Bayern (public sector) | BayLfD | |
| Berlin | BlnBDI | |
| Brandenburg | LDA Brandenburg | |
| Bremen | LfDI Bremen | |
| Hamburg | HmbBfDI | |
| Hessen | HBDI | |
| Mecklenburg-Vorpommern | LfDI M-V | |
| Niedersachsen | LfD Niedersachsen | |
| Nordrhein-Westfalen | LDI NRW | |
| Rheinland-Pfalz | LfDI RLP | |
| Saarland | ULD Saarland | |
| Sachsen | SächsDSB | |
| Sachsen-Anhalt | LfD LSA | |
| Schleswig-Holstein | ULD | |
| Thüringen | TLfDI | |

Include the complaint right with the correct authority name and URL.

## Language & Formalities

- Privacy notice MUST be in **German** if targeting German users
- "Sie" (formal) is standard; "Du" only if brand consistently uses informal tone
- Bilingual notices (DE + EN) recommended for international services
- Impressum (§ 5 TMG / DDG) is legally separate but often linked alongside
- Common title: **"Datenschutzerklärung"** (not "Datenschutzrichtlinie")
- Must be accessible with max **2 clicks** from any page (BGH ruling)

## Legal Bases

### Employee Data (§ 26 BDSG)
If the privacy notice covers employees (e.g., career portals, applicant tracking):
- Legal basis: **§ 26 Abs. 1 BDSG** (processing necessary for employment relationship)
- Special categories: **§ 26 Abs. 3 BDSG** (explicit consent or necessity)
- Works council agreements can serve as legal basis

### Special Category Data (§ 26(3) BDSG + Art. 9 DSGVO)
German employment law creates several common Art. 9 processing scenarios:
- **Church tax (Kirchensteuer)**: Religion is Art. 9 data. Legal basis: Art. 6(1)(c) + Art. 9(2)(b) DSGVO + § 26(3) BDSG + § 51a EStG. Employer must process religious affiliation for payroll; disclose in notice.
- **Disability status (Schwerbehinderung)**: Health data under Art. 9. Legal basis: Art. 6(1)(c) + Art. 9(2)(b) DSGVO + § 26(3) BDSG + §§ 164, 168 SGB IX. Required for additional leave, special dismissal protection.
- **Sick leave certificates (AU-Bescheinigungen)**: Health data. Legal basis: Art. 6(1)(c) + Art. 9(2)(b) DSGVO + § 26(3) BDSG + § 5 EFZG. Retention: typically 1 year after end of calendar year.
- **Occupational integration management (BEM)**: Health data. Legal basis: Art. 6(1)(c) + Art. 9(2)(b) DSGVO + § 26(3) BDSG + § 167(2) SGB IX. BEM files must be stored separately from personnel file.
- **Trade union dues**: Trade union membership is Art. 9 data. If deducted via payroll: Art. 6(1)(b)/(c) + Art. 9(2)(b) DSGVO + § 26(3) BDSG.
- **Biometric access control**: Fingerprint/facial recognition for building access. Art. 9(2)(a) explicit consent typically required (§ 26(3) Satz 2 BDSG). Works council co-determination applies (§ 87(1) Nr. 6 BetrVG). DPIA recommended.

### Video Surveillance (§ 4 BDSG)
If premises are monitored:
- Separate notice required at the entrance
- Art. 6(1)(f) DSGVO + § 4 BDSG
- Retention: typically 48–72 hours, max justified by purpose

### Scoring & Creditworthiness (§ 31 BDSG)
Relevant for e-commerce or financial services with credit checks.

### Consent under TDDDG § 25
- Cookie/tracking consent follows **TDDDG § 25** (implementing ePrivacy Directive Art. 5(3))
- Consent must meet DSGVO Art. 7 standards
- Planet49 (CJEU) and Cookie-Einwilligung II (BGH) case law applies

## Retention Periods

| Data Category | Duration | Legal Basis |
|---|---|---|
| Commercial correspondence | 6 years | § 257 HGB |
| Tax-relevant records, invoices | 10 years | § 147 AO, § 257 HGB |
| Applicant data (rejected) | 6 months after rejection | AGG statute of limitations |
| Employee data | Duration of employment + 3 years (limitation) | § 26 BDSG |
| Server log files | 7–30 days | Art. 6(1)(f) DSGVO |
| Contract data | Duration + 3 years (general limitation) | §§ 195, 199 BGB |
| Active customer account | Duration of relationship | Art. 6(1)(b) DSGVO |
| Inactive prospects | 3 years without interaction | Art. 6(1)(f) — balancing test |
| Cookie consent records | 3 years (proof of consent) | Art. 7(1) DSGVO |
| CCTV footage | 48–72 hours (standard), justified max | § 4 BDSG |
| Telecom traffic data | 10 weeks (§ 176 TKG) | TDDDG/TKG |

## Cookie & Tracking Rules

### TDDDG § 25 Framework
- **Consent required** for any access to or storage of information on end-user devices UNLESS strictly necessary
- "Strictly necessary" is narrowly interpreted (session cookies, cart, load balancer — yes; analytics, ads — no)
- Server-side analytics (e.g., Matomo without cookies) may fall outside § 25 scope but still require Art. 6(1)(f) assessment
- Consent banner must offer **reject all** equally prominent as **accept all** (Planet49, BGH)

### Common German CMP Solutions
Usercentrics, Cookiebot, Consentmanager, Borlabs Cookie (WordPress)

### Google Analytics Specific
The DSK (Datenschutzkonferenz) has repeatedly raised concerns. If used:
- Ensure Google Analytics 4 with IP anonymization
- Server-side tagging preferred
- Consent required (no legitimate interest)
- Consider Matomo/Plausible as compliant alternatives

## Children's Data

- GDPR Art. 8 threshold: Germany sets **16 years** (§ 2 Nr. 17 TDDDG, national implementation)
- If service targets minors: parental consent mechanism required
- Privacy notice must use age-appropriate language

## DPO Requirements

### Mandatory DPO (§ 38 BDSG)
- **≥ 20 persons** constantly engaged in automated processing
- Core activity: large-scale processing of special categories (Art. 9/10 DSGVO)
- Core activity: systematic monitoring (Art. 37(1)(c) DSGVO)

Always include DPO contact in the privacy notice if appointed. Use functional email (datenschutz@..., dpo@...).

## Standard Wording

### Complaint Right (German)
```
Sie haben das Recht, sich bei einer Datenschutzaufsichtsbehörde über die Verarbeitung Ihrer personenbezogenen Daten zu beschweren. Die für uns zuständige Aufsichtsbehörde ist:

[Name der Aufsichtsbehörde]
[Adresse]
[URL]
```

### Right to Object (Art. 21 — mandatory separate notice)
```
WIDERSPRUCHSRECHT

Sie haben das Recht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, jederzeit gegen die Verarbeitung Sie betreffender personenbezogener Daten, die auf Grundlage von Art. 6 Abs. 1 lit. e oder f DSGVO erfolgt, Widerspruch einzulegen.

Werden Ihre personenbezogenen Daten verarbeitet, um Direktwerbung zu betreiben, haben Sie das Recht, jederzeit Widerspruch gegen die Verarbeitung einzulegen.
```

### Responsible Party Intro (German)
```
Verantwortlich im Sinne der Datenschutz-Grundverordnung (DSGVO) ist:

[Firmenname]
[Rechtsform]
[Straße, PLZ Ort]
Vertreten durch: [Geschäftsführer/Vorstand]
E-Mail: [E-Mail]
Telefon: [Telefon]
```
