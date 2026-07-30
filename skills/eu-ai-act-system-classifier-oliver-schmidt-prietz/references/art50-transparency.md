# Art. 50 Transparency Obligations — Comprehensive Reference

This reference provides the full Art. 50 transparency framework, incorporating the Second Draft Code of Practice on Transparency of AI-Generated Content (March 2026). It covers all six obligation categories, the Code of Practice's multi-layered marking and labelling architecture, exceptions, boundary analysis, and practical implementation guidance.

**Penalty tier:** Tier 2 — up to EUR 15,000,000 or 3% of total worldwide annual turnover (Art. 99(4))
**Applies from:** 2 August 2026 (Art. 113 general application — Chapter IV; *not* the 113(b) 2 Aug 2025 tranche). Legacy generative-AI 50(2) marking: 2 December 2026 (Omnibus grace).

---

## 1. The Six Art. 50 Obligation Categories

Art. 50 creates transparency obligations that apply **regardless of risk tier** — even minimal-risk systems must comply if they trigger any Art. 50 category. These obligations bind providers and deployers differently.

### 1.1 Art. 50(1): AI Interaction Disclosure — Provider Obligation

**Legal summary:** Providers must design AI systems that interact directly with natural persons to inform those persons that they are interacting with an AI system — unless this is obvious from the circumstances and context of use.

| Element | Detail |
|---------|--------|
| **Who it binds** | Provider (Anbieter) |
| **Trigger** | AI system interacts directly with natural persons (e.g., chatbot, voice agent, AI avatar) |
| **Implementation** | Clear, timely disclosure at the start of interaction |
| **Standard** | "Obvious from circumstances" exemption assessed from the perspective of a reasonably well-informed, observant, and circumspect person |
| **Exception** | Not required where obviously apparent; law enforcement and migration contexts with authorization and safeguards (Art. 50(1) last sentence) |

**Key design requirement:** Disclosure must be proactive and occur before substantive interaction begins. Embedding disclosure solely in terms of service or privacy policies does not satisfy Art. 50(1).

---

### 1.2 Art. 50(2): Synthetic Content Marking — Provider Obligation

**Legal summary:** Providers of AI systems that generate synthetic audio, image, video, or text content must ensure outputs are marked in a machine-readable format and detectable as artificially generated or manipulated. The marking must be effective, interoperable, robust, and reliable.

| Element | Detail |
|---------|--------|
| **Who it binds** | Provider (Anbieter) |
| **Trigger** | AI system generates synthetic audio, image, video, or text |
| **Implementation** | Machine-readable marking (metadata, watermarking, or equivalent technical means) |
| **Standard** | Marking must survive reasonably foreseeable content transformations |
| **Exception** | Assistive functions for standard editing; no substantial alteration of input data (Art. 50(2) last sentence) |

This is the most technically demanding Art. 50 obligation. The Code of Practice (Section 1 below) provides the detailed implementation framework.

---

### 1.3 Art. 50(3): Emotion Recognition / Biometric Categorization Disclosure — Deployer Obligation

**Legal summary:** Deployers of emotion recognition or biometric categorization systems must inform exposed natural persons of the system's operation and process personal data in accordance with applicable Union law.

| Element | Detail |
|---------|--------|
| **Who it binds** | Deployer (Betreiber) |
| **Trigger** | System performs emotion recognition (Emotionserkennung) or biometric categorization |
| **Implementation** | Clear disclosure of system operation to affected persons |
| **Interaction with Art. 5** | Emotion recognition in workplace/education is prohibited (Art. 5(1)(f)); biometric categorization for sensitive characteristics is prohibited (Art. 5(1)(g)). Art. 50(3) applies only to permitted uses (e.g., medical, safety, entertainment, security) |

**GDPR coordination:** Art. 50(3) explicitly requires compliance with applicable data protection law. Deployers must also satisfy GDPR Art. 13/14 information obligations and, where applicable, Art. 35 DPIA requirements.

---

### 1.4 Art. 50(4): Deep Fake Labelling — Deployer Obligation

**Legal summary:** Deployers of AI systems that generate or manipulate image, audio, or video content constituting a deep fake must disclose that the content has been artificially generated or manipulated.

| Element | Detail |
|---------|--------|
| **Who it binds** | Deployer (Betreiber) |
| **Trigger** | AI-generated or AI-manipulated content that constitutes a deep fake (Art. 3(60): content that appreciably resembles existing persons, objects, places, or events and would falsely appear authentic) |
| **Implementation** | Clear, visible labelling that content is AI-generated or manipulated |
| **Exceptions** | (1) Law enforcement / national security with authorization; (2) artistic, creative, satirical, or fictional works where disclosure would be disproportionate (with safeguards — see Section 4); (3) text content published for public information where human editorial review and control over publication exist |

The Code of Practice (Section 2 below) provides the modality-specific labelling framework.

---

### 1.5 Art. 50(5): Delivery Requirements — Cross-Cutting

**Legal summary:** Information provided under Art. 50(1)–(4) must be provided in a clear and distinguishable manner, at the latest at the time of first interaction or exposure. The information must comply with applicable accessibility requirements.

This is not a separate obligation but a **quality standard** governing how all Art. 50 disclosures must be delivered. Key requirements:

- **Clarity:** Plain language, no technical jargon, adapted to audience
- **Distinguishability:** Disclosure must be visually or aurally distinct from surrounding content
- **Timeliness:** Before or at the moment of first interaction/exposure, not retroactively
- **Accessibility:** Must comply with Directive (EU) 2019/882 (European Accessibility Act) requirements where applicable

---

### 1.6 Art. 50(6): Exceptions Governance — Cross-Cutting

Art. 50(6) does not create a separate obligation but governs exceptions across all categories:

- The Art. 50(2) assistive function exception is self-executing (provider self-assessment)
- The Art. 50(4) exceptions for law enforcement, artistic works, and text publications are interpreted narrowly
- The Commission may adopt implementing acts specifying technical details of Art. 50(2) marking (Art. 50(6a))
- Codes of practice under Art. 56 may establish compliance paths for Art. 50(2) and Art. 50(4)

---

## 2. Code of Practice — Provider Marking Requirements (Art. 50(2))

The Second Draft Code of Practice on Transparency of AI-Generated Content (March 2026) establishes a multi-layered marking architecture for providers of AI systems generating synthetic content. This section synthesizes the provider-side framework (Working Group 1).

### 2.1 Commitment 1: Multi-Layered Content Marking

The Code of Practice's central requirement is **redundant marking** — multiple independent marking techniques applied simultaneously, so that provenance information survives common content transformations (screenshots, re-encoding, compression, format conversion).

#### Sub-measure 1.1.1: Digitally Signed Metadata

Providers must embed provenance metadata at the point of content generation, using established open standards:

| Element | Requirement |
|---------|-------------|
| **Standard** | C2PA (Coalition for Content Provenance and Authenticity) manifest or equivalent open, interoperable standard; IPTC metadata fields for image content |
| **Content** | (a) Identifier of the AI system or provider; (b) timestamp of generation; (c) declaration that content is AI-generated or AI-manipulated; (d) content type (image, audio, video, text) |
| **Integrity** | Digitally signed to prevent tampering; signature verification must be publicly accessible |
| **Persistence** | Metadata must be embedded in the content file, not merely stored externally or linked |

**Practical note:** C2PA manifests have established industry adoption (Adobe Content Credentials, Google SynthID metadata, Microsoft Content Integrity). Providers may extend the minimum required fields with additional provenance data.

#### Sub-measure 1.1.2: Imperceptible Watermarking

In addition to metadata, providers must apply imperceptible watermarking to generated content:

| Element | Requirement |
|---------|-------------|
| **Perceptibility** | Must not degrade content quality or be perceivable by humans under normal conditions |
| **Robustness** | Must survive common transformations: compression, resizing, cropping, format conversion, re-encoding, screenshot capture |
| **Decodability** | Provider must offer a mechanism to verify watermark presence (see Commitment 2) |
| **Modality coverage** | Required for image, audio, and video content; for text, statistical watermarking where technically feasible |

**Text watermarking note:** Text watermarking is technically less mature than image/audio/video watermarking. The Code of Practice acknowledges this asymmetry — text providers should implement available techniques (e.g., distributional watermarking, lexical substitution patterns) but are held to a lower robustness standard pending technological development.

#### Sub-measure 1.1.3: Fingerprinting and Logging (Optional)

Providers may additionally maintain content fingerprints (perceptual hashes) in a registry, enabling post-hoc verification even when metadata and watermarks have been stripped:

- Content hash at generation time stored in provider registry
- Query API for third parties to check content against registry
- Not mandatory under the Code of Practice, but recommended for providers generating high-volume content

### 2.2 Measure 1.2: Non-Removal Obligations

Providers must take reasonable steps to prevent removal of their marking:

| Measure | Description |
|---------|-------------|
| **Contractual** | Terms of service must prohibit intentional stripping of provenance metadata or watermarks by downstream users |
| **Technical** | Where feasible, use marking techniques resistant to intentional removal; provide mechanisms to re-embed metadata after authorized editing |
| **Informational** | Document marking techniques used (without compromising security-relevant details) so downstream actors can preserve them |

### 2.3 Measure 1.3: Provenance Chain Transparency (Optional)

Providers may implement provenance chain tracking — recording the sequence of modifications to content, so that each transformation (original generation → editing → re-generation) is traceable. This builds on C2PA's ingredient manifest capability.

### 2.4 Measure 1.4: Perceptible Marking Functionality for Deployers (Optional)

Providers may offer deployers optional tools to add **visible** (human-perceptible) markings to content — such as watermark overlays, badges, or border indicators. This is not required of providers but supports deployers in meeting their Art. 50(4) labelling obligations.

---

### 2.5 Commitment 2: Detection Mechanisms

Providers must make detection of their marking technically feasible for third parties:

| Mechanism | Requirement |
|-----------|-------------|
| **Detection API or tool** | Publicly accessible service to verify whether content carries the provider's marking (metadata and/or watermark) |
| **Response content** | Detection result must indicate: (a) whether marking is present; (b) confidence level; (c) provider identity where determinable |
| **Access** | Available to deployers, downstream providers, researchers, and — where technically appropriate — the general public |
| **Forensic detection** (optional) | Advanced detection for degraded or manipulated content, available to authorized parties (authorities, researchers) |

### 2.6 Commitment 3: Quality Requirements

Marking and detection mechanisms must satisfy four quality dimensions:

| Dimension | Requirement |
|-----------|-------------|
| **Effectiveness** | Marking must be successfully embedded in a very high proportion of generated content (target: > 99% for metadata, > 95% for watermarks) |
| **Reliability** | Detection must have low false-positive and false-negative rates under normal conditions |
| **Robustness** | Marking must survive a defined set of common transformations without losing decodability |
| **Interoperability** | Marking formats must be based on open standards; detection mechanisms must be accessible across platforms and systems |

### 2.7 Commitment 4: Testing, Verification, and Compliance

| Element | Requirement |
|---------|-------------|
| **Internal testing** | Regular testing of marking effectiveness and robustness against defined transformation scenarios |
| **Transparency reporting** | Annual disclosure of marking deployment status, detection accuracy metrics, and identified limitations |
| **Red-teaming** (recommended) | Adversarial testing of marking robustness against removal or spoofing attacks |
| **Third-party audit** (for signatories) | Independent verification of compliance with Code of Practice commitments |

---

## 3. Code of Practice — Deployer Labelling Requirements (Art. 50(4))

The deployer-side framework (Working Group 2) establishes how deployers must disclose deep fake content to the public.

### 3.1 Commitment 1: Disclosure via Labelling

Deployers must label deep fake content with a clear disclosure indicator. The Code of Practice establishes a harmonized approach:

**Primary label:** The letters "AI" (representing artificial intelligence) presented as a visual icon or equivalent textual indicator. Member States or the Commission may adopt a standardized EU icon.

#### Design Requirements

| Requirement | Specification |
|-------------|--------------|
| **Contrast** | Minimum 4.5:1 contrast ratio between label and background (WCAG AA) |
| **Size** | Sufficiently prominent to be noticed by a reasonably attentive viewer; minimum dimensions proportional to content display size |
| **Legibility** | Must be readable at the resolution and size at which content is typically consumed |
| **Persistence** | Label must remain visible for the duration of content display or playback |
| **Accessibility** | Must be perceivable by persons with visual impairments through alternative means (alt text, audio description) |

#### Placement Requirements by Modality

| Modality | Placement Rule |
|----------|---------------|
| **Real-time video** (livestream, video call) | Persistent on-screen indicator throughout the stream; positioned to avoid obstruction of essential content |
| **Non-real-time video** (recorded, shared) | (a) Persistent on-screen indicator during playback, OR (b) prominent disclosure at the start of the video (minimum 3 seconds) plus a persistent smaller indicator |
| **Image** (still) | (a) Visible label within the image, OR (b) immediately adjacent caption/label when displayed on a platform |
| **Audio** (spoken, music) | (a) Spoken disclosure at the beginning of the audio, OR (b) written label in any visual interface displaying the audio, OR (c) both for maximum reach |
| **Text** | Clear textual disclosure at the beginning of the text content (e.g., "This text was generated by AI") or as a persistent header/footer |
| **Multimodal** | Apply the placement rule for each modality present; if content contains both video and audio deep fake elements, label both the video and audio streams |

### 3.2 Commitment 2: Internal Compliance and Training

Deployers generating or distributing deep fake content must:

- Establish internal procedures for identifying content that requires Art. 50(4) labelling
- Train staff involved in content creation and distribution on labelling obligations
- Maintain records of labelling decisions (which content was labelled, which exceptions were applied, and why)

### 3.3 Commitment 3: Artistic and Creative Works — Proportionate Disclosure

For deep fake content that is part of an artistic, creative, satirical, or fictional work, deployers may apply a **proportionate** disclosure approach rather than the full labelling regime:

| Element | Proportionate Approach |
|---------|----------------------|
| **Placement** | Disclosure may appear in credits, description, or metadata rather than as a persistent on-screen indicator — provided it is reasonably discoverable |
| **Timing** | May appear at the end rather than the beginning, if beginning-of-content disclosure would undermine the artistic purpose |
| **Format** | May be textual rather than iconographic, where the creative context makes icon labelling impractical |
| **Condition** | Must still be clear and accessible to the audience; "proportionate" does not mean "hidden" |

**Safeguard:** The artistic exception does not apply where the content is disseminated outside its original artistic context (e.g., a satirical deep fake clip shared on social media without the surrounding satirical framing must be labelled).

### 3.4 Commitment 4: Human Review Exception for Text Publications

For text content published to inform the public on matters of public interest:

| Condition | Requirement |
|-----------|-------------|
| **Human editorial review** | A natural person has reviewed the content and bears editorial responsibility for its accuracy and quality |
| **Publisher accountability** | The publishing entity assumes legal responsibility for the publication |
| **Disclosure standard** | If both conditions are met, the Art. 50(4) labelling obligation does not apply — the content is treated as the publisher's own |

**Important limitation:** This exception applies only to text. Audio, image, and video deep fake content must always be labelled regardless of editorial review, because the deceptive potential of audiovisual deep fakes is qualitatively different from AI-assisted text.

---

## 4. Exceptions and Boundaries

### 4.1 Art. 50(4) Exceptions

| Exception | Scope | Conditions |
|-----------|-------|------------|
| **Law enforcement / national security** | Art. 50(4) second subparagraph | Prior authorization by competent authority; specific investigation; cannot be applied as blanket exemption |
| **Artistic / creative / satirical / fictional** | Art. 50(4) third subparagraph | Content must be recognizable as artistic/fictional in context; deployer must apply proportionate disclosure (see 3.3 above); exception lost when content leaves original artistic context |
| **Text — human review** | Art. 50(4) fourth subparagraph | Natural person reviews and takes editorial responsibility; publisher accountability; applies only to text modality |

### 4.2 Art. 50(2) Exception — Assistive Function

The provider's marking obligation under Art. 50(2) does not apply where the AI system:

- Performs an **assistive function** for standard editing (e.g., spell-check, grammar correction, basic formatting)
- Does **not substantially alter** the input data provided by the user or its semantics

**Boundary test:** The determining factor is whether the AI system's output constitutes a new creative work versus an improved version of the user's own work. Content generation (new text, images from prompts) always requires marking. Content refinement (correcting typos, adjusting brightness) does not.

### 4.3 Boundary Analysis

| WITHIN SCOPE (marking/labelling required) | OUT OF SCOPE | Distinguishing Factor |
|------------------------------------------|--------------|----------------------|
| AI-generated image from text prompt | AI-enhanced photo brightness/contrast | Creation vs. enhancement: new content vs. minor adjustment to existing content |
| AI voice clone synthesizing speech | AI noise reduction on recorded speech | Synthetic generation vs. quality improvement: fabricated voice vs. cleaned original |
| AI-generated article published as news | AI spell-checker correcting typos | Substantial alteration vs. assistive function: new content creation vs. correction |
| AI face-swap video (deep fake) | AI video stabilization of genuine footage | Identity manipulation vs. technical improvement: altering who appears vs. how content looks |
| AI music generation from scratch | AI audio mastering of recorded performance | Generation vs. post-processing: new work vs. refinement of existing work |
| AI text rewriting that changes meaning | AI translation of existing text | Semantic alteration vs. language transfer: changed substance vs. equivalent in another language |

### 4.4 Gray Zone Scenarios

1. **AI-assisted creative collaboration:** A designer uses an AI system to generate multiple variations of a logo concept, selects one, and substantially modifies it. The final logo contains elements originated by the AI and elements created by the designer. **Key question:** Does the final work require Art. 50(2) marking? If the AI's contribution is substantial (the overall composition, key visual elements), marking is required. If the designer's subsequent modifications are so extensive that the AI's contribution is no longer recognizable as the creative origin, the assistive function exception may apply — but the threshold for "no longer recognizable" is high.

2. **AI-enhanced old photographs:** A restoration service uses AI to colorize, upscale, and fill in damaged portions of historical photographs. The original photograph is genuine; the AI additions are synthetic. **Key question:** Does restoring historical photos constitute "substantial alteration"? Where the AI fills in missing portions (inpainting), it is generating new content and the output should be marked. Where it only enhances existing pixels (upscaling), the assistive function exception is stronger. The mixed nature of most restoration workflows suggests marking is the safer default.

3. **AI-generated background for real presenter:** A video creator uses AI to generate a virtual background while the human presenter is real. The deep fake definition requires content that "appreciably resembles existing persons, objects, places, or events and would falsely appear authentic." **Key question:** If the virtual background depicts a realistic location, it may constitute a deep fake of the place. If it is an obviously fantastical or abstract background, Art. 50(4) is likely not triggered — but Art. 50(2) marking of the synthetic background component is still required from the provider.

4. **Corporate AI writing assistant:** An organization deploys an AI writing assistant that drafts emails, reports, and presentations based on employee prompts. Employees review and edit before sending. **Key question:** Is the output "text content" requiring Art. 50(2) marking? Yes — the AI system generates text, so the provider must implement machine-readable marking. Whether the deployer must also label under Art. 50(4) depends on whether the content could constitute a "deep fake" (typically not for routine business communication). The human review exception under Art. 50(4) may apply to published text, but Art. 50(2) provider marking still applies.

---

## 5. Interaction with Other AI Act Provisions

### 5.1 Art. 50 ↔ Art. 53: GPAI Transparency

GPAI model providers are subject to both Art. 53 transparency obligations and Art. 50(2) synthetic content marking:

| Provision | Obligation | Scope |
|-----------|-----------|-------|
| **Art. 53(1)(b)** | Drawing up and maintaining technical documentation, including for downstream providers | Applies to all GPAI models |
| **Art. 53(1)(d)** | Putting in place a policy to comply with Art. 50(2) | GPAI providers whose models can generate synthetic content |
| **Art. 50(2)** | Marking synthetic content in machine-readable format | Applied to the AI system built on the GPAI model |

**Practical implication:** A GPAI model provider (e.g., foundation model developer) must implement Art. 50(2) marking capabilities in their model or API, so that downstream providers deploying the model in AI systems can meet their own Art. 50(2) obligations. This creates a **layered responsibility**: the model provider builds the marking capability; the system provider ensures it is activated and properly configured.

### 5.2 Art. 50 ↔ Art. 13: High-Risk Transparency

Art. 50 obligations apply **on top of** high-risk transparency requirements under Art. 13:

| Requirement | Art. 13 (High-Risk) | Art. 50 (All Tiers) |
|-------------|---------------------|---------------------|
| **Focus** | Users understand AI system and interpret outputs correctly | General public knows they are interacting with AI or seeing AI-generated content |
| **Audience** | Deployers and professional users | Natural persons (general public) |
| **Content** | Technical documentation, performance metrics, limitations | Disclosure of AI nature, provenance marking |

A high-risk AI system that also generates synthetic content or interacts with natural persons must satisfy **both** Art. 13 (detailed technical transparency to deployers) **and** Art. 50 (public-facing disclosure and content marking).

### 5.3 Art. 50 ↔ Art. 5: Prohibited Practices

| Interaction | Analysis |
|-------------|----------|
| **Art. 50(3) ↔ Art. 5(1)(f)** | Emotion recognition in workplace/education is prohibited. Art. 50(3) disclosure obligation applies only where emotion recognition is permitted (medical, safety, entertainment). If a deployer deploys emotion recognition in a prohibited context, the Art. 5 violation takes precedence — Art. 50(3) compliance does not cure a prohibition. |
| **Art. 50(3) ↔ Art. 5(1)(g)** | Biometric categorization for sensitive characteristics is prohibited. Art. 50(3) applies only to non-sensitive biometric categorization (e.g., age estimation). |
| **Art. 50(1) ↔ Art. 5(1)(a)** | A system that fails to disclose AI involvement and uses this concealment to manipulate behavior may trigger both Art. 50(1) non-compliance and the Art. 5(1)(a) deception prohibition. |

### 5.4 Art. 50 ↔ Open-Source Exemption

Art. 2(12) exempts certain open-source AI systems from most AI Act requirements — but **Art. 50 is explicitly excluded from this exemption**. Open-source AI systems that generate synthetic content, interact with natural persons, or produce deep fakes must comply with Art. 50, even if they are otherwise exempt under Art. 2(12).

| Open-Source System Type | Art. 50 Status |
|------------------------|----------------|
| Open-source chatbot framework | Art. 50(1) applies — must inform users of AI interaction |
| Open-source image generator | Art. 50(2) applies — must mark generated images |
| Open-source voice synthesis tool | Art. 50(2) and potentially Art. 50(4) apply |
| Open-source text generation model | Art. 50(2) applies — must implement text marking |

---

## 6. Practical Implementation Checklist

### 6.1 Provider Checklist (Art. 50(1) + Art. 50(2))

| # | Action | Code of Practice Reference | Priority |
|---|--------|---------------------------|----------|
| 1 | Identify all AI systems that interact with natural persons or generate synthetic content | — | Prerequisite |
| 2 | Implement AI interaction disclosure for user-facing systems | Art. 50(1) | High |
| 3 | Integrate digitally signed metadata (C2PA or equivalent) into content generation pipeline | Commitment 1, Sub-measure 1.1.1 | High |
| 4 | Implement imperceptible watermarking for image, audio, and video outputs | Commitment 1, Sub-measure 1.1.2 | High |
| 5 | Assess text watermarking options; implement where technically feasible | Commitment 1, Sub-measure 1.1.2 | Medium |
| 6 | Deploy detection API or verification tool for marking validation | Commitment 2 | High |
| 7 | Update terms of service to prohibit intentional marking removal | Measure 1.2 | Medium |
| 8 | Establish testing regime for marking robustness and effectiveness | Commitment 4 | Medium |
| 9 | Publish annual transparency report on marking deployment | Commitment 4 | Medium |
| 10 | Consider optional fingerprinting/logging registry | Sub-measure 1.1.3 | Low |

### 6.2 Deployer Checklist (Art. 50(3) + Art. 50(4))

| # | Action | Code of Practice Reference | Priority |
|---|--------|---------------------------|----------|
| 1 | Inventory all AI systems that perform emotion recognition, biometric categorization, or generate deep fakes | — | Prerequisite |
| 2 | Implement disclosure notices for emotion recognition / biometric systems | Art. 50(3) | High |
| 3 | Design and apply modality-appropriate labels for deep fake content | Commitment 1 (WG2) | High |
| 4 | Verify label contrast (≥ 4.5:1), size, and accessibility compliance | Design requirements | High |
| 5 | Establish internal procedures for labelling decision-making | Commitment 2 (WG2) | Medium |
| 6 | Train staff on labelling obligations and exception criteria | Commitment 2 (WG2) | Medium |
| 7 | Document exception decisions (artistic works, human review) with reasoning | Commitments 3-4 (WG2) | Medium |
| 8 | Coordinate Art. 50(3) disclosure with GDPR Art. 13/14 information obligations | Art. 50(3) | High |

### 6.3 SME / Startup Proportionality

The Code of Practice acknowledges that technical marking requirements may impose disproportionate burdens on smaller organizations:

| Measure | Full Requirement | Proportionate Alternative for SMEs |
|---------|-----------------|-------------------------------------|
| Metadata embedding | Full C2PA manifest integration | Use established libraries or API services that handle C2PA embedding (e.g., open-source C2PA toolkits) |
| Watermarking | Custom imperceptible watermarking | Use third-party watermarking services or open-source watermarking implementations |
| Detection API | Self-hosted detection service | Use shared detection infrastructure or integrate with established verification platforms |
| Annual reporting | Comprehensive transparency report | Simplified reporting covering key metrics (marking activation rate, known limitations) |
| Testing regime | Internal red-teaming and robustness testing | Use publicly available benchmark suites; participate in collaborative testing initiatives |

**AI regulatory sandbox access:** SMEs may access national AI regulatory sandboxes (Art. 57-62) to test compliance approaches with reduced regulatory risk.

---

## 7. Regulatory Status and Timeline

### 7.1 Current Status

| Element | Status (as of March 2026) |
|---------|--------------------------|
| **Art. 50 obligations** | Apply from **2 August 2026** (Art. 113 general application; Art. 50 is Chapter IV — *not* the 113(b) 2 Aug 2025 tranche). 50(1)/(3)/(4) and 50(2) for newly-placed systems: 2 Aug 2026, no transition. Legacy generative-AI 50(2) marking: 2 Dec 2026 (Omnibus grace). |
| **Code of Practice (Art. 50(2) + (4))** | Second draft published March 2026; final version expected June 2026 |
| **Commission implementing acts (Art. 50(6a))** | Under development; expected to specify technical standards for machine-readable marking |
| **Commission guidelines on Art. 50** | First draft December 2025; further drafts in progress |
| **Harmonized standards for marking** | Under development by CEN/CENELEC; not yet published |

### 7.2 Code of Practice Legal Effect

The Code of Practice is **not legally binding** but serves as a compliance pathway:

- Compliance with the Code of Practice creates a **presumption of conformity** with Art. 50(2) and Art. 50(4) (Art. 56(8))
- Providers and deployers may choose alternative means to demonstrate compliance, but the burden of proof shifts to them
- Once the Commission adopts implementing acts under Art. 50(6a), those acts will define mandatory technical standards — the Code of Practice may be supplemented or partially superseded

### 7.3 Web Search Queries for Updates

```
EU AI Act Code of Practice transparency AI-generated content final [current year]
EU AI Act Art. 50 Commission implementing act technical standards
EU AI Act Art. 50 guidelines marking watermarking [current year]
CEN CENELEC AI Act harmonized standards transparency marking
EU AI Act Art. 50 national implementation guidance [country]
```
