# DPIA Risk Catalog

Risks to rights and freedoms of data subjects. Derived from Recital 75 GDPR, EDPB Guidelines WP 248 rev.01, EDPB DPIA Template v1.0 (March 2026), CNIL PIA knowledge bases, EDPB Opinion 28/2024 (AI), EDPB Guidelines 3/2019 (video surveillance), EDPB Guidelines 1/2020 (connected vehicles), and enforcement practice.

Use this catalog to **proactively propose risks** based on the processing description. Select relevant risks — don't present the entire catalog.

**Risk tracks:** Each risk is tagged as **Track A** (inherent-by-design — risks from processing working as intended) or **Track B** (operational — risks from accidental/unlawful/abnormal events). See `scoring.md` for methodology.

---

## Rights Impact Categories

### Discrimination (Art. 21 EU Charter)
| ID | Track | Risk | Common Triggers | Modulating Factors |
|----|-------|------|-----------------|-------------------|
| DISC-01 | A | Algorithmic bias producing discriminatory outcomes | AI/ML scoring, hiring algorithms, credit decisions, insurance pricing | ↑ vulnerable subjects, AI opacity; ↓ human-in-the-loop review, bias auditing |
| DISC-02 | A | Proxy discrimination via neutral data correlating with protected characteristics | Zip code profiling, browsing patterns, purchasing behavior | ↑ large population, automated decisions; ↓ fairness testing, feature audit |
| DISC-03 | A | Differential service quality based on profiling | Dynamic pricing, tiered service, customer value scoring | ↑ essential services; ↓ transparency, opt-out mechanisms |
| DISC-04 | A | Health-status discrimination from wearable/medical data | Insurance exclusions, employment screening via health profiling | ↑ Art. 9 data, employment context; ↓ purpose limitation, data minimization |

### Identity Theft and Fraud (Art. 8 EU Charter)
| ID | Track | Risk | Common Triggers | Modulating Factors |
|----|-------|------|-----------------|-------------------|
| IDTH-01 | B | Identity theft from exposed personal identifiers | Large-scale databases with names, IDs, dates of birth | ↑ large population, internet-facing systems; ↓ encryption, pseudonymization |
| IDTH-02 | B | Account takeover from compromised credentials | Password stores, biometric template databases | ↑ high-value targets, weak auth; ↓ MFA, credential hashing |
| IDTH-03 | B | Social engineering enabled by detailed profiles | Comprehensive CRM data, behavioral profiles | ↑ detailed profiles, external exposure; ↓ data minimization, access controls |
| IDTH-04 | B | Deepfake creation from biometric data | Facial images, voice recordings | ↑ public availability of biometric data; ↓ access restrictions, watermarking |

### Financial Loss (Art. 17 EU Charter)
| ID | Track | Risk | Common Triggers | Modulating Factors |
|----|-------|------|-----------------|-------------------|
| FINL-01 | B | Direct loss from unauthorized transactions | Payment data, banking integrations | ↑ real-time payment systems, high volumes; ↓ fraud detection, transaction limits |
| FINL-02 | A | Credit damage from inaccurate automated scoring | Credit scoring, shared blacklists | ↑ essential service denial, no human review; ↓ accuracy audits, correction mechanisms |
| FINL-03 | A | Insurance denial or inflation from profiling | Health data, driving behavior, lifestyle data | ↑ Art. 9 data, essential service; ↓ transparency, right to object |
| FINL-04 | A | Employment loss from unfair automated evaluation | Performance AI, hiring/firing algorithms | ↑ employment dependency, AI opacity; ↓ human oversight, explainability |

### Reputational Damage (Art. 1, 7 EU Charter)
| ID | Track | Risk | Common Triggers | Modulating Factors |
|----|-------|------|-----------------|-------------------|
| REPD-01 | B | Public exposure of private information | Data breaches, unauthorized sharing | ↑ sensitive data, public figures; ↓ encryption, breach response |
| REPD-02 | A | Incorrect association with criminal/unethical activity | AML false positives, blacklist errors | ↑ automated decisions, no human review; ↓ accuracy audits, correction rights |
| REPD-03 | B | Social stigma from disclosed sensitive data | Health conditions, sexual orientation, addiction | ↑ Art. 9 data, small communities; ↓ access controls, pseudonymization |
| REPD-04 | A | AI-generated false biographical information | LLM hallucinations producing incorrect personal facts | ↑ public-facing AI, no grounding; ↓ RAG, human review, disclaimers |

### Loss of Confidentiality (Art. 7 EU Charter, professional secrecy)
| ID | Track | Risk | Common Triggers | Modulating Factors |
|----|-------|------|-----------------|-------------------|
| CONF-01 | B | Breach of professional secrecy (legal, medical, tax) | Law firm data, medical records — connects to §203 StGB in Germany | ↑ professional secrecy obligation, high sensitivity; ↓ encryption, access logging |
| CONF-02 | B | Unauthorized disclosure to third parties | Processor breaches, over-broad access, cloud provider access | ↑ multiple processors, cloud; ↓ contractual controls, access audits |
| CONF-03 | B | Foreign government access to protected data | US CLOUD Act, Schrems II transfer risks | ↑ US cloud providers, no supplementary measures; ↓ EU hosting, encryption with EU keys |
| CONF-04 | A | AI model memorization and data leakage | LLMs reproducing training data, model inversion attacks | ↑ large training sets, public-facing model; ↓ differential privacy, output filtering |

### Reversal of Pseudonymization (Art. 8 EU Charter, Art. 25 GDPR)
| ID | Track | Risk | Common Triggers | Modulating Factors |
|----|-------|------|-----------------|-------------------|
| PSEU-01 | B | Re-identification through data linkage | Pseudonymized data + auxiliary data | ↑ rich auxiliary datasets, unique attributes; ↓ key separation, access controls |
| PSEU-02 | B | Model inversion / membership inference attacks | ML models revealing training data | ↑ public model access, sensitive training data; ↓ differential privacy, access restrictions |
| PSEU-03 | A | Singling out in "anonymous" datasets | Location traces, transaction patterns, behavioral fingerprints | ↑ high-dimensional data, temporal granularity; ↓ aggregation, k-anonymity |

### Physical Harm (Art. 2, 3 EU Charter)
| ID | Track | Risk | Common Triggers | Modulating Factors |
|----|-------|------|-----------------|-------------------|
| PHYS-01 | B | Stalking/harassment via location data | Real-time tracking, movement history | ↑ real-time access, vulnerable subjects; ↓ access controls, data minimization |
| PHYS-02 | B | Domestic violence risk from exposed personal data | Shared accounts, family trackers, address disclosure | ↑ vulnerable subjects, shared access; ↓ individual access controls, address suppression |
| PHYS-03 | B | Safety risks from vehicle data manipulation | Connected vehicle systems, remote vehicle control | ↑ remote access, safety-critical systems; ↓ air-gapping, integrity checks |
| PHYS-04 | A | Medical harm from inaccurate health data | Wrong medication alerts, faulty diagnostic AI | ↑ clinical decision support, no human oversight; ↓ human-in-the-loop, accuracy validation |

### Loss of Control Over Personal Data (informational self-determination)
| ID | Track | Risk | Common Triggers | Modulating Factors |
|----|-------|------|-----------------|-------------------|
| CTRL-01 | A | Opaque processing — data subjects cannot understand how data is used | Complex AI, multi-layered data flows | ↑ AI opacity, complex data flows; ↓ transparency notices, explainability |
| CTRL-02 | A | Inability to exercise rights effectively | Technical barriers, cross-system complexity | ↑ cross-system processing, legacy; ↓ self-service portals, response automation |
| CTRL-03 | A | Function creep — data repurposed beyond original collection | Ecosystem platforms, M&A integration, AI training | ↑ platform ecosystem, AI training; ↓ purpose limitation controls, consent management |
| CTRL-04 | A | Indefinite retention without justification | No deletion policy, blockchain immutability | ↑ blockchain, no deletion mechanism; ↓ retention schedules, automated purging |

### Chilling Effect on Freedoms (Art. 11, 12, 45 EU Charter)
| ID | Track | Risk | Common Triggers | Modulating Factors |
|----|-------|------|-----------------|-------------------|
| CHIL-01 | A | Self-censorship due to surveillance awareness | Workplace monitoring, public surveillance, online tracking | ↑ continuous monitoring, employment context; ↓ proportional scope, transparency |
| CHIL-02 | A | Deterrence from legitimate activity | Political profiling, social media monitoring, protest surveillance | ↑ political/religious context; ↓ purpose limitation, judicial oversight |
| CHIL-03 | A | Behavioral conformity pressure | Social scoring, employee ranking, reputation systems | ↑ visible scoring, employment dependency; ↓ opt-out, appeals process |

### Denial of Services (access to essential services)
| ID | Track | Risk | Common Triggers | Modulating Factors |
|----|-------|------|-----------------|-------------------|
| DENY-01 | A | Automated denial of essential services | Algorithmic gatekeeping in banking, insurance, housing | ↑ essential service, no alternative; ↓ human review, Art. 22 safeguards |
| DENY-02 | A | Platform ban with significant consequences | Content moderation algorithms | ↑ dominant platform, professional dependency; ↓ appeals process, human review |
| DENY-03 | A | Cross-sector blocking from shared blacklists | Industry exclusion lists, credit bureau entries | ↑ cross-sector reach, no recourse; ↓ accuracy audits, correction mechanisms |

### Manipulation and Exploitation (Art. 1 EU Charter — dignity)
| ID | Track | Risk | Common Triggers | Modulating Factors |
|----|-------|------|-----------------|-------------------|
| MANP-01 | A | Behavioral manipulation through dark patterns | UX exploiting psychological biases | ↑ vulnerable subjects, children; ↓ ethical UX review, regulatory compliance |
| MANP-02 | A | Exploitation of psychological vulnerabilities | Targeted ads to gambling addicts, persons in distress | ↑ health/addiction data, real-time targeting; ↓ exclusion lists, content policies |
| MANP-03 | A | Micro-targeting for political manipulation | Behavioral profiling for political advertising | ↑ election context, granular profiling; ↓ transparency, ad libraries |

---

## Processing-Specific Risk Profiles

Each profile lists Track A (inherent-by-design) risks first, then Track B (operational) scenarios for the three standard threat vectors.

### AI/ML Systems (EDPB Opinion 28/2024)

**Training phase (Track A):** DISC-01 (bias), DISC-02 (proxy discrimination), CONF-04 (memorization), PSEU-03 (singling out), CTRL-03 (function creep from scraping)
**Deployment phase (Track A):** REPD-04 (hallucinations), DISC-01 (discriminatory outputs), CTRL-01 (opacity), CTRL-02 (rights exercise difficulty), DENY-01 (automated decisions)
**Track B — Operational:**
- Illegitimate access: training data exfiltration, model theft, unauthorized API access to model outputs
- Undesired modification: training data poisoning, adversarial input manipulation, model parameter tampering
- Data disappearance: training dataset loss, model checkpoint corruption, inference log deletion

Key point: The anonymization challenge — controllers claiming training data is "anonymous" must be scrutinized. If singling out is possible, data is personal.

### Employee Monitoring (DSK, UODO, CNIL blacklists)
**Track A:** Email/internet: CHIL-01, CTRL-01. DLP: DISC-01 (false positives → discipline), REPD-02. GPS/fleet: CHIL-01, CTRL-03 (off-hours tracking).
**Track B — Operational:**
- Illegitimate access: supervisor accessing personal emails, DLP logs leaked, GPS data accessed for non-work purposes
- Undesired modification: monitoring logs tampered to hide misconduct, incorrect attribution of activity
- Data disappearance: monitoring records lost before dispute resolution, GPS logs deleted before accident investigation

### Video Surveillance / Facial Recognition (EDPB Guidelines 3/2019)
**Track A:** Standard CCTV: CHIL-01, CTRL-03, CHIL-02. Facial recognition: DISC-01 (differential accuracy), REPD-02 (misidentification), CHIL-01 (mass surveillance).
**Track B — Operational:**
- Illegitimate access: unauthorized viewing of footage, biometric template database breach, IDTH-04 (biometric theft)
- Undesired modification: footage tampering, template corruption, timestamp manipulation
- Data disappearance: retention policy failure destroying evidence, storage failure losing footage

### Connected Vehicles (EDPB Guidelines 1/2020)
**Track A:** Location/telemetry: CHIL-01, CTRL-03, FINL-03 (insurance). Biometric (drowsiness): DISC-04, CHIL-01. Driving behavior: DISC-03, FINL-03, CONF-03.
**Track B — Operational:**
- Illegitimate access: remote vehicle tracking by unauthorized parties, telematics data intercepted, PHYS-01 (stalking)
- Undesired modification: odometer/telemetry manipulation, PHYS-03 (safety-critical system compromise)
- Data disappearance: vehicle data loss after accident (evidence destruction), OTA update wiping diagnostic logs

Key mitigation: Edge/local processing. If biometric data stays in the vehicle and never transmits, risk substantially decreases (EDPB recommendation).

### Health/Genetic Data
**Track A:** Health warehouses: PSEU-01, DISC-04, CTRL-01. Genetic testing: DISC-04 (familial privacy), FINL-03. Implantable devices: PHYS-04, CTRL-01.
**Track B — Operational:**
- Illegitimate access: CONF-01 (breach of professional secrecy), patient records exposed, genetic data breach affecting family members
- Undesired modification: wrong patient data in clinical system, diagnostic AI corruption, PHYS-04 (medical harm from inaccurate data)
- Data disappearance: patient records lost, genetic test results corrupted, implant data unavailable in emergency

### Financial/Credit Processing
**Track A:** Credit scoring: DISC-01, FINL-02, DENY-01, CTRL-01. Shared blacklists: DENY-03, FINL-02, REPD-02. AML/KYC: REPD-02, DENY-01.
**Track B — Operational:**
- Illegitimate access: FINL-01 (unauthorized transactions), account data breach, insider access to credit files
- Undesired modification: credit score corruption, false blacklist entries, AML flag manipulation
- Data disappearance: transaction records lost, audit trail gaps, KYC documentation destroyed before retention expiry
