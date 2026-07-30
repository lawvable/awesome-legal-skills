# Low-Risk / Minimal Risk AI — Obligations

## Overview

AI systems that are NOT classified as high-risk or prohibited still carry certain obligations under the AI Act. These fall into two categories:

1. **Limited risk (Art. 50):** Systems triggering specific transparency obligations
2. **Minimal risk:** Systems with only the universal AI competence obligation (Art. 4)

Additionally, the Art. 6(4) documentation requirement applies to systems classified as non-high-risk under the Art. 6(3) exception.

---

## Universal Obligation: AI Competence — Art. 4

**Applies to:** ALL providers and deployers of ALL AI systems (including minimal risk).

**Legal text:**

> Providers and deployers of AI systems shall take measures to ensure, to their best extent, a sufficient level of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training and the context the AI systems are to be used in, and considering the persons or groups of persons on whom the AI systems are to be used.

*German: KI-Kompetenz*

**Recital:** 20

**What this means:**
- Staff training on AI fundamentals
- Understanding of the specific AI system's capabilities and limitations
- Awareness of risks and ethical considerations
- Proportionate to role — technical staff need deeper understanding than end users
- Consider the vulnerability of persons affected by the system

**Implementation:**
| Action | Description | Effort |
|--------|-------------|--------|
| Needs assessment | Identify who interacts with AI systems | Low |
| Training program | Develop/acquire AI literacy training | Medium |
| Role-specific training | Technical vs. managerial vs. end-user tracks | Medium |
| Documentation | Record training delivered and competencies | Low |
| Updates | Periodic refresher training | Low |

---

## Transparency Obligations — Art. 50

### Art. 50(1): Interaction with Natural Persons

**Obligation:** Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural person is informed that they are interacting with an AI system, unless this is obvious from the circumstances and context of use.

**Applies to:** Chatbots, virtual assistants, AI telephone agents, AI customer service, AI avatars.

**Exceptions:**
- Where obvious from context (e.g., clearly labeled AI assistant on website)
- Law enforcement or migration contexts (with safeguards)

**Implementation:**
- Clear disclosure at start of interaction: "You are interacting with an AI system"
- Disclosure must be timely, clear, and intelligible
- Cannot be buried in terms of service

---

### Art. 50(2): Synthetic Content Marking

**Obligation:** Providers of AI systems that generate synthetic audio, image, video or text content shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated.

**Applies to:** Generative AI producing text, images, audio, video, code.

**Technical requirement:** Machine-readable marking (watermarking, metadata, provenance signals).

**Exception:** Where the AI system performs an assistive function for standard editing, or where it does not substantially alter the input data.

---

### Art. 50(3): Emotion Recognition Disclosure

**Obligation:** Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system.

**Applies to:** Any emotion recognition or biometric categorisation system (where not prohibited under Art. 5(1)(f) or (g)).

**Note:** Emotion recognition in workplace/education is prohibited (Art. 5(1)(f)). This obligation applies to permitted contexts (e.g., medical, safety, entertainment).

---

### Art. 50(4): Deep Fake Labeling

**Obligation:** Deployers of an AI system that generates or manipulates image, audio or video content constituting a deep fake, shall disclose that the content has been artificially generated or manipulated.

**Applies to:** Deepfake content — realistic synthetic media portraying persons saying or doing things they did not.

**Exceptions:**
- Content that is part of an obviously creative, satirical, artistic, or fictional work
- Law enforcement purposes (with safeguards)
- Exercise of fundamental rights (freedom of expression, arts)

---

## Art. 6(4) Documentation Requirement

**Applies to:** Providers of Annex III systems classified as non-high-risk under the Art. 6(3) exception.

**Obligation:** Document the assessment of why Art. 6(3) exception applies, before placing on market or putting into service.

**Required documentation:**
1. Which Art. 6(3) condition is met ((a), (b), (c), or (d))
2. Why the system does not pose significant risk of harm
3. Confirmation the system does not perform profiling
4. Register the system in the EU database (Art. 49(2))

**Make available to authorities upon request.**

---

## Voluntary Codes of Conduct — Art. 95

**For minimal-risk systems:** The AI Act encourages (but does not require) providers and deployers to voluntarily apply the requirements for high-risk systems or develop codes of conduct.

**Art. 95 specifics:**
- Codes of conduct may address: environmental sustainability, AI literacy, inclusive design, diversity in development teams
- Commission and Member States shall facilitate development of codes of conduct
- Codes may be drawn up by individual providers/deployers or by industry organizations

---

## Obligation Summary by Risk Level

### Limited Risk (Art. 50)

| # | Obligation | Legal Basis | Applies When |
|---|-----------|-------------|-------------|
| 1 | AI interaction disclosure | Art. 50(1) | System interacts with natural persons |
| 2 | Synthetic content marking | Art. 50(2) | System generates synthetic content |
| 3 | Emotion recognition disclosure | Art. 50(3) | System performs emotion recognition |
| 4 | Deep fake labeling | Art. 50(4) | System generates deepfakes |
| 5 | AI competence | Art. 4 | Always |

### Minimal Risk

| # | Obligation | Legal Basis | Applies When |
|---|-----------|-------------|-------------|
| 1 | AI competence | Art. 4 | Always |
| 2 | Voluntary codes of conduct | Art. 95 | Encouraged, not required |

### Non-High-Risk Under Art. 6(3) Exception

| # | Obligation | Legal Basis | Applies When |
|---|-----------|-------------|-------------|
| 1 | Document Art. 6(3) assessment | Art. 6(4) | Provider of Annex III system classified as non-high-risk |
| 2 | Register in EU database | Art. 49(2) | Same as above |
| 3 | AI competence | Art. 4 | Always |
| 4 | Art. 50 obligations | Art. 50 | If transparency triggers apply |

---

## Timeline

| Date | Obligation Becomes Effective |
|------|------------------------------|
| 2 Feb 2025 | Art. 4 AI competence (applies to all) |
| 2 Feb 2025 | Art. 5 prohibitions |
| 2 Aug 2026 | Art. 50 transparency obligations — 50(1)/(3)/(4) + 50(2) for new systems *(50(2) legacy generative-AI marking: 2 Dec 2026)* |
| **2 Dec 2027** *(Omnibus-postponed from 2 Aug 2026)* | High-risk obligations for Annex III systems |
| **2 Aug 2028** *(Omnibus-postponed from 2 Aug 2027)* | High-risk obligations for Annex I systems |
