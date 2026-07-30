# France (RGPD + Loi Informatique et Libertés + LCEN)

## Table of Contents
1. [Legal Framework](#legal-framework)
2. [Supervisory Authority](#supervisory-authority)
3. [Language & Formalities](#language--formalities)
4. [Legal Bases — French Specifics](#legal-bases)
5. [Retention Periods](#retention-periods)
6. [Cookie & Tracking Rules](#cookie--tracking-rules)
7. [Children's Data](#childrens-data)
8. [DPO Requirements](#dpo-requirements)
9. [Standard Wording Templates](#standard-wording)

---

## Legal Framework

| Law | Scope |
|-----|-------|
| **RGPD** (= GDPR) | Directly applicable EU regulation |
| **Loi Informatique et Libertés** (LIL, loi n°78-17 modifiée) | National implementing law; health data, research, criminal data |
| **LCEN** (Loi pour la Confiance dans l'Économie Numérique) | Log retention obligations (1 year), hosting liability |
| **Code des postes et communications électroniques** | ePrivacy transposition, cookie consent |

## Supervisory Authority

| Authority | Details |
|-----------|---------|
| **CNIL** (Commission Nationale de l'Informatique et des Libertés) | Single national SA |
| Address | 3 Place de Fontenoy – TSA 80715 – 75334 Paris Cedex 07 |
| Online complaint | https://www.cnil.fr/fr/plaintes |

## Language & Formalities

- Privacy notice MUST be in **French** if targeting French users
- "Vous" (formal) is standard
- Common title: **"Politique de confidentialité"** or **"Protection des données personnelles"**
- Mentions légales (Art. 6 LCEN) is legally separate but often co-located
- The CNIL recommends **layered approach**: summary + full text

## Legal Bases

### Prospection commerciale (commercial prospecting)
- **B2C email**: Consent required (Art. L.34-5 CPCE) UNLESS existing customer + similar products + opt-out (soft opt-in)
- **B2B email**: Legitimate interest possible if related to professional function, opt-out required
- **SMS/MMS**: Always consent

### Health Data
- Art. 44 et seq. LIL: additional safeguards for health data
- Hébergeur de données de santé (HDS) certification required for health data hosting
- Pre-employment medical examinations: Art. 9(2)(h) RGPD + Art. R.4624-10 Code du travail. Only fitness/unfitness result disclosed to employer, not diagnosis.

### Special Category Data — French Specifics (Art. 9 RGPD + LIL)
- **Biometric data**: CNIL Règlement type (Délibération n°2019-001) governs biometric access control in the workplace. Requires DPIA, strict necessity test, and prior information to employees. Explicit consent or Art. 9(2)(b) employment law basis.
- **Trade union membership**: Art. L.2141-5 Code du travail prohibits discrimination based on union activity. If payroll-related (union dues deduction): Art. 9(2)(b) + Art. 6(1)(c). Access must be strictly limited.
- **Religious data**: France's principle of laïcité restricts collection of religious data. Generally prohibited except where legally required (e.g., dietary accommodations in certain contexts). No equivalent to German church tax.
- **Health data in employment**: Sick leave (arrêt maladie): employer receives attestation only, not diagnosis. Occupational health (médecine du travail): Art. 9(2)(h) RGPD + Code du travail. CNIL recommends separate storage and restricted access.
- **Genetic data**: Art. 75 LIL provides additional restrictions. Processing only permitted for medical, scientific research, or judicial purposes.

### Research & Statistics
- LIL Chapter III provides specific regimes for scientific research
- CNIL simplified procedures (méthodologies de référence MR-001 to MR-006)

## Retention Periods

| Data Category | Duration | Legal Basis |
|---|---|---|
| Active customer data | Duration of contractual relationship | Art. 6(1)(b) RGPD |
| Inactive prospects | 3 years from last contact | CNIL recommendation |
| Invoices & accounting | 10 years | Art. L.123-22 Code de commerce |
| Commercial contracts | 5 years after end | Art. 2224 Code civil |
| Connection logs (hosting) | 1 year | Art. 6 II LCEN, Décret n°2011-219 |
| Payroll data | 5 years | Art. L.3243-4 Code du travail |
| Applicant data (rejected) | 2 years max | CNIL recommendation |
| Cookie consent proof | 6 years (contractual limitation) | Art. 2224 Code civil |
| CCTV footage | 30 days max | Art. L.252-3 Code de la sécurité intérieure |
| Medical records | 20 years from last visit | Art. R.1112-7 Code de la santé publique |

## Cookie & Tracking Rules

### CNIL Guidelines 2020
The CNIL's "Lignes directrices cookies et traceurs" (Délibération n°2020-091) and "Recommandation cookies" (Délibération n°2020-092) set the standard:

- **Consent required** for all non-essential cookies/trackers
- "Continue browsing" does NOT constitute valid consent
- Refuse must be as easy as accept (no dark patterns)
- Cookie wall: generally prohibited unless access alternative exists
- Max cookie lifespan: **13 months**; consent renewal every **6 months** recommended
- Consent proof must be stored

### CNIL Sanctions Reference
| Company | Amount | Reason |
|---------|--------|--------|
| Google LLC & Ireland | €150M | Refusing cookies more complex than accepting |
| Facebook Ireland | €60M | No "reject all" button |
| Amazon Europe | €35M | Cookies placed without prior consent |
| Microsoft Ireland | €60M | Cookies without consent |
| Criteo | €40M | Cookie consent and information deficiencies |
| TikTok | €5M | Cookie refusal mechanism too complex |

### Exempt Cookies (no consent needed)
- Session/authentication cookies
- Shopping cart cookies
- Load balancer cookies
- Cookie consent choice storage
- Audience measurement under specific CNIL conditions (Matomo with specific config)

### CNIL-Compliant Analytics
The CNIL maintains a list of analytics tools exempted from consent under specific configurations. Matomo (with CNIL-recommended settings) is the primary example.

## Children's Data

- France: **15 years** (Art. 45 LIL, implementing GDPR Art. 8)
- Below 15: dual consent (child + parental authority holder)
- Notice must be written in language understandable by minors

## DPO Requirements

Same as GDPR Art. 37 — no additional French threshold (unlike Germany's § 38 BDSG).

Mandatory when:
- Public authority/body
- Core activities: large-scale regular/systematic monitoring
- Core activities: large-scale processing of special categories

CNIL strongly recommends voluntary appointment in all cases.

## Standard Wording

### Complaint Right (French)
```
Vous disposez du droit d'introduire une réclamation auprès de la Commission Nationale de l'Informatique et des Libertés (CNIL) :

CNIL
3 Place de Fontenoy – TSA 80715
75334 Paris Cedex 07
www.cnil.fr
```

### Right to Object (French)
```
DROIT D'OPPOSITION

Vous pouvez vous opposer à tout moment au traitement de vos données personnelles fondé sur l'intérêt légitime (article 6.1.f du RGPD), pour des raisons tenant à votre situation particulière.

Si vos données personnelles sont traitées à des fins de prospection commerciale, vous pouvez vous y opposer à tout moment, sans avoir à justifier de motifs particuliers.
```

### Responsible Party Intro (French)
```
Le responsable du traitement de vos données personnelles est :

[Dénomination sociale]
[Forme juridique], au capital de [montant] euros
Immatriculée au RCS de [ville] sous le numéro [SIREN/SIRET]
Siège social : [adresse complète]
Représentée par [Nom], en qualité de [fonction]
E-mail : [email]
Téléphone : [téléphone]
```
