# Modifying AI Under the EU AI Act: Classification and Compliance

Analysis of how modifications to AI systems affect classification and compliance obligations under the AI Act.

| Aspect | Detail |
|--------|--------|
| Institution | artificialintelligenceact.eu |
| Date | 2025 |
| Source URL | https://artificialintelligenceact.eu/modifying-ai-classification-compliance/ |
| NotebookLM Source ID | c96d4792-... |

*German: Aenderung von KI gemaess der KI-Verordnung: Klassifizierung und Compliance*

---

This is a guest post written by legal compliance professionals Oystein Endal, Andrea Vrcic, Sidsel Nag, Nick Malter and Daylan Araz (see section about authors at the end), drawing on their experience from running or consulting businesses integrating AI. For any questions or suggestions, please contact Nick Malter at nick@trail-ml.com.

> **Disclaimer:** The information provided and discussed in the article does not and is not intended to constitute legal advice. Please obtain professional legal counsel where necessary. The content of the EU AI Act may be interpreted differently than stated.

## Summary

- Those modifying AI systems or models, including GPAI models, may become providers under the EU AI Act, resulting in a higher compliance burden. A proper assessment of the AI system, model and use case is key.
- A proper assessment of the modification presumes that the scope of the AI system or GPAI model, as well as the provider role is clear. Read [this article about the "Providers of General-Purpose AI Models"](https://artificialintelligenceact.eu/providers-of-general-purpose-ai-models-what-we-know-about-who-will-qualify/) for more information.
- A shift in compliance responsibilities of the provider is triggered when an AI system gets modified and is high-risk, or when a GPAI model is significantly changed in its generality, capabilities, or systemic risk. This may be the case when a GPAI model is fine-tuned.
- The EU AI Act, and specifically the obligations for GPAI model providers are manageable. Keeping technical documentation and summaries of the GPAI model is limited to the scope of modification. In most cases, these are even required for other purposes than compliance.
- The European Commission chose to set relatively high compute-based thresholds for what qualifies as substantial modifications of GPAI models, and currently expects only few modifiers to become GPAI model providers.

## Introduction

The EU AI Act primarily regulates providers of general purpose AI (GPAI) models and AI systems, establishing a comprehensive framework for the development and deployment of AI within the European Union. While the EU AI Act clearly identifies the developer of a completely new AI system or GPAI model as a provider, it becomes more complex when someone further down in the value chain modifies an existing third-party AI system or GPAI model. This raises questions about compliance responsibilities, specifically who should and can fulfil the provider obligations under the EU AI Act.

The EU AI Act acknowledges the modification scenarios by defining circumstances under which a modifier of an AI system or GPAI model becomes a provider -- effectively transferring regulatory obligations from the original provider to the modifier, either partly or fully.

This shift in compliance responsibilities, especially when looking at high-risk AI systems or GPAI models, is a scenario that businesses typically seek to avoid due to the additional compliance cost and burden. Misclassifying the role, risk category, or the AI model under the EU AI Act poses a significant compliance risk for businesses, as it can lead to fines of up to EUR 15 million or 3% of global annual revenue for non-compliance with the provisions on high-risk AI systems or GPAI models.

With the GPAI model provider obligations taking effect since 2 August 2025, discussions about AI model and system modifications and the resulting compliance implications have become increasingly urgent and relevant for businesses.

In this article, we -- a working group of AI Pact members and AI Act early adopters -- discuss the classification resulting from modifications under the EU AI Act and discuss compliance challenges from a practitioner's perspective. We are specifically focussing on GPAI models and applications.

## The Issues with Modifications Under the EU AI Act

Due to the EU AI Act's broad definitions, it can be hard for businesses to figure out when a modification results in provider obligations for the model used. The decisive definition of a "substantial modification" (see [Article 3(23)](https://artificialintelligenceact.eu/article/3/)) remains vaguely described in the EU AI Act. This creates uncertainty for organisations.

The challenge of a correct classification is especially relevant when considering scenarios in which businesses build systems or applications upon GPAI models, such as OpenAI's GPT-4.5 or Anthropic's Sonnet 4. These models are deliberately designed to be adaptable across a broad set of use cases and to be customised by downstream operators in the value chain. In these scenarios, answering the question of who needs to fulfil what obligations can be difficult.

There are (on-going) initiatives by the European Commission that aim to clarify concepts in the AI Act. With regards to high-risk AI systems, the development of CEN/CENELEC standards is ongoing with expected publication earliest in 2026. These should provide concrete guidance on how to obtain presumption of conformity with the EU AI Act's provisions on high-risk AI systems but do not focus on GPAI models. With regards to GPAI models, the [GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) from the European Commission's AI Office is focused on fulfilling the GPAI model provider obligations as well as GPAI models with systemic risk. The Code of Practice has been recently complemented with official [Guidelines for GPAI providers](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act) (GPAI guidelines). While these are good first steps, uncertainties remain about when a modifier becomes a provider in practice.

The GPAI guidelines introduce a threshold of one-third of the initial computing power required to train the original GPAI model (measured in [FLOPs](https://blog.heim.xyz/flop-for-quantity-flop-s-for-performance/)) as a distinction between substantial and insubstantial modifications. This threshold aims to clarify when compliance obligations shift to the modifier. However, this computing-based threshold, while potentially useful for certain modifications like fine-tuning, may remain insufficient for other types of modifications that substantially change model behaviour and risks without requiring extensive computational resources. The guidelines state that this threshold is merely an indicative criterion. In accordance with the [GPAI guidelines](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act) paragraph 62, the overarching rule for determining when a modification is substantial comes down to whether the modifications potentially result in substantially modified generality, capabilities or systemic risk of the model.

Given these circumstances, organisations face challenges in implementing the appropriate measures to comply with the EU AI Act as well as in determining whether their use cases and modifications qualify them to become a (GPAI model) provider in the first place.

### Common Issues with Modifications of AI Models and Systems

- **Timing:** GPAI model provider obligations apply from 2 August 2025. Businesses are still struggling to find out if they need to comply with additional provisions for providers or not.
- **Vagueness:** The conditions under which modifications trigger the provider status remain vaguely defined, creating lots of room for interpretation.
- **Lack of guidance:** Official standards by CEN/CENELEC are not released to give the highly needed guidance. The GPAI guidelines of the AI Office have been released late and still leave some open questions and legal uncertainty.
- **Impractical proposals:** The proposed computing-based thresholds for significant modifications in the GPAI guidelines offer limited utility. It may be difficult to measure, especially for downstream actors. Further, other types of modification may not require a lot of compute, but can have significant impact on the model and risks. The question remains if the latter actually changes compliance burdens under the EU AI Act.
- **Grandfathering:** It is unclear how actors that substantially modify existing GPAI models after August 2, 2025, are required to fulfil provider obligations when the upstream model providers may not have to fulfill provider obligations until August 2027.
- **Lack of vendor transparency:** It is difficult to conduct thorough conformity and impact assessments and maintain control over third-party AI systems and models. Further, there is often a lack of clearly defined contractual obligations and ambiguity around accountabilities due to insufficient vendor communication.

## What Modifications Can Qualify You as a Provider?

Prior to the considerations of whether there is a modification that can qualify someone as a provider, it is advised to conduct an assessment of whether the system or model at hand actually lies within the scope of the EU AI Act's definitions of an AI system or GPAI model. This may seem trivial, but when classifying the operating role, it has proved to be difficult at times.

There are various ways to become a provider under the EU AI Act, both at the AI system and AI model level. In particular, the EU AI Act outlines several scenarios where a business modifying or deploying an AI system can potentially inherit the role and responsibilities of a provider:

1. **Integration** of an existing AI model into a new or existing AI system (see [Article 3(68)](https://artificialintelligenceact.eu/article/3/))
2. **Rebranding** a high-risk AI system as one's own product (see [Article 25](https://artificialintelligenceact.eu/article/25/))
3. **Repurposing** an AI system or model so that it becomes high-risk (see [Article 25](https://artificialintelligenceact.eu/article/25/))
4. **(Substantial) modifications** to an existing high-risk AI system or a GPAI model (see [Article 25](https://artificialintelligenceact.eu/article/25/) and [Recital 109](https://artificialintelligenceact.eu/recital/109/))

The first case refers to the EU AI Act's definition of a "downstream provider" (see [Article 3(68)](https://artificialintelligenceact.eu/article/3/)), which likely describes the current circumstances of many organisations best. For instance, bringing your own model ("BYOM") into an AI system may qualify as an integration. However, being a downstream provider does not necessarily trigger a shift in the compliance responsibilities for GPAI model providers, as it rather describes the role of an AI system provider. In this situation, an organisation would need to validate if the high-risk AI system or transparency obligations apply, and if the upstream provider of the GPAI model has clearly excluded the distribution and use of the model within the EU.

While the second and third case -- rebranding and repurposing -- are generally quite straightforward thresholds for a shift in compliance responsibility, the cases involving substantial modifications are more ambiguous and pose significant interpretive challenges for organisations.

## Substantial Modifications of AI Systems

According to the AI Act, a substantial modification refers to a change of an AI system which has not been foreseen by the original provider's conformity assessment, and which affects the compliance with requirements on high-risk AI systems or which affects the intended purpose of the AI system (see [Article 3(23)](https://artificialintelligenceact.eu/article/3/) and [Recital 128](https://artificialintelligenceact.eu/recital/128/)). Note that an official conformity assessment for a high-risk AI system can only be conducted when there are notified bodies that perform an external audit or when the harmonised standards (by CEN/CENELEC) can be applied. At the time of writing, this is therefore not helpful guidance yet.

The AI Act further addresses modifications explicitly in [Article 25](https://artificialintelligenceact.eu/article/25/), where it states that substantial changes to a high-risk AI system shifts the role of a provider to the modifier -- but only if the system remains high-risk. This links the concept of substantial modifications to the impact of the modification on the risk level.

## Substantial Modifications of GPAI Models

When it comes to modifications of GPAI models, the EU AI Act becomes less defined. [Recital 109](https://artificialintelligenceact.eu/recital/109/) and the [FAQ by the European Commission](https://digital-strategy.ec.europa.eu/en/faqs/general-purpose-ai-models-ai-act-questions-answers) clarify that provider obligations for GPAI models are limited to the scope of the modification, but the EU AI Act does not directly link GPAI model modifications to specific risk levels (only to systemic or non-systemic risk). Further, the EU AI Act does not explicitly speak of substantial modifications in the context of GPAI models -- but it does explicitly highlight fine-tuning of GPAI models as modification, suggesting that the modification also needs to have a rather substantial effect on the model. The AI Office confirms the latter in the [GPAI guidelines](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act), as it states that, in their view, modifications usually involve training a model on additional data. The guidelines also extensively focus on fine-tuning and retraining a GPAI model.

To further support this distinction, the [GPAI guidelines](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act) introduce a compute-based threshold: if a modification uses at least one-third of the computational resources originally required to train the model, the modifier is presumed to have become a GPAI model provider. While this threshold adds some clarity, its limitations were highlighted during the public consultation of the guidelines and acknowledged by the AI Office. The threshold may not capture low-compute modifications that still substantially affect a model's risk profile, and it may be difficult for modifiers to reliably estimate the required compute -- especially without access to information from upstream providers. The European Commission chose to set relatively high thresholds, and currently expects only few modifiers to become GPAI model providers.

Again, the threshold is an indicative criterion, and other model modifications could also qualify as substantial modifications. Whether the risk-focussed logic of [Article 25](https://artificialintelligenceact.eu/article/25/) (the article regulating changes in high-risk AI system cases) is also applicable to the modifications of GPAI models, as suggested by some, remains an open question.

### Types of AI Model Modifications

A modification to an AI model can take many forms. As outlined by [Philipp Hacker and Matthias Holweg (2025)](https://dx.doi.org/10.2139/ssrn.5289125), the most relevant types of modifications to an AI model can be grouped into the following categories:

1. **No change:** Using a pretrained AI model without any modifications.
2. **Modifying hyperparameters:** Adjusting parameters like temperature.
3. **Retrieval-Augmented Generation (RAG):** Building applications that enhance a model's outputs by referencing an external knowledge base or proprietary data.
4. **Custom GPTs:** Creating variants of base models with specified instructions, tools, and personalities.
5. **Fine-tuning:** Training the base model on proprietary or domain-specific datasets to tailor its performance.
6. **Model or knowledge distillation:** Training a smaller "student" model based on the outputs of a larger "teacher" model, often to reduce computational requirements.

As Hacker and Holweg (2025) argue, substantial modifications, i.e. substantially changed risk profiles or model behaviour, exist in cases of fine-tuning, model distillation, jailbreaking via parameter manipulation, or changing the core architecture of a model. Other modifications, especially when not changing the risk profile, architecture, generality or intended purpose of an AI model, are likely insubstantial, meaning not triggering a change in GPAI model provider obligations.

## What Does This Mean in Practice?

Following the broader logic of the EU AI Act, it is useful to anchor the assessment of whether there is a change in compliance responsibilities, both regarding AI systems and GPAI models, in an assessment of whether the modification is substantial or insubstantial -- which in turn requires looking at the modification's effect on risks.

For **AI systems**, the exercise is relatively clear: businesses modifying AI systems should review whether changes affect the system's risk classification, e.g. clarifying if it becomes high-risk or remains high-risk.

For **GPAI models**, the exercise is a bit more complex. Until further guidance is available and standards are in place, businesses modifying GPAI models can consider two approaches:

- **A more conservative approach**, treating any adaptation as a potential trigger for a shift in the GPAI model provider obligations by default. This essentially includes maintaining documentation and summaries of the performed modifications, even though these may not be mandatory.
- **A more pragmatic approach**, under which GPAI model provider obligations are assumed to apply only if the modification clearly alters the model's behaviour, generality, or risk profile, or if the compute thresholds are met. This approach limits governance burdens, but may require stronger justifications if challenged.

In any case, businesses should conduct risk and impact assessments when making any changes to GPAI models or (high-risk) AI systems.

## GenAI in Action: Practitioner's Examples and Open Challenges

To give an idea of current challenges for practitioners when it comes to the right categorisation, below are (partly anonymised) real example cases. Further compliance challenges under the AI Act that are related to GenAI cases, which are yet to be solved, are also highlighted.

### Case 1: Enterprise IT Service Provider

An enterprise IT service provider makes use of the GPT-4 model by OpenAI to provide and sell a platform that orchestrates different chatbots in one centralised solution. End users can then both chat with the bots to access general knowledge, but also their company's internal knowledge, within a secure environment. This is a very common "Custom GPT" case, in which the service provider limits their modifications to changes in prompts and adding RAG techniques, while distributing the system under a new name.

The following considerations were particularly relevant to the IT service provider in assessing compliance:

- First, it was unclear whether building custom bots around the GPT-4 model and providing services under their own brand name qualifies them as a GPAI model provider.
- Second, there was confusion about whether the August 2, 2025 GPAI deadline applies to their business of selling GPT-based solutions without substantially modifying the core model.
- Third, they struggle with ensuring that OpenAI delivers the required documentation.

While the IT service provider does qualify as a downstream provider, due to the integration of OpenAI's model, they neither qualified themselves as a provider of a high-risk AI system (excluded in usage policy and limited through technical means) nor as GPAI model provider due to the very limited scope of modification which does not significantly change the model's risk. In this case, and at least for compliance purposes, they don't need to rely on OpenAI's documentation and they do not face additional obligations under the GPAI model provisions. The IT service provider consulted with the compliance company of one of the authors, [Trail](https://www.trail-ml.com/), and decided to follow a conservative approach, meaning to keep sufficient technical documentation around the architecture and functionality of the GPAI system, which should be available for development purposes anyway.

### Case 2: Agentic AI Platform of Scale-up

A Swiss scale-up, [Unique AI](https://www.unique.ai/), offers a platform to build agentic AI solutions that help banks, insurance companies and private equity firms to improve their financial operations. These include workflows, such as investment research, due diligence, and KYC processes. The main challenge here was to ensure compliance and proper security of AI agents that are capable of performing actions independently. However, the role under the EU AI Act was unclear at the beginning.

Unique AI conducted in-depth research on the EU AI Act, both internally and with support from a law firm, WalderWyss, where they obtained a legal opinion on the positioning of Unique AI regarding the EU AI Act. Based on the client setup and deployment model, Unique AI can have various roles under the EU AI Act.

Most of the clients chose a single tenant deployment model where Unique AI hosts and runs the software. Based on the legal interpretation of the EU AI Act, Unique's operational approach positions them as a distributor rather than a provider while making the AI systems and models available. This is because Unique AI leverages existing commercial AI products like Microsoft Azure and OpenAI models, and enriches them with context-specific functionalities through prompt chaining, RAG, and prompt-to-SQL techniques, without altering the original Large Language Model (LLM). Unique AI does not use client data for model training purposes, and excludes the use for high-risk purposes, which further supports this classification. Therefore, the company is not considering themselves as a modifier of the GPAI model and the GPAI model provider obligations remain on upstream providers' side.

They have adopted an AI Governance Framework, which serves as the foundation for their agentic AI development, embedding trust, safety, accountability, reliability, and transparency into the core architecture of every intelligent agent and workflow, while regular internal benchmarking prevents model drift and maintains consistent quality across all use cases.

To proactively work towards AI Act compliance, Unique AI conducted an internal conformity assessment following [David Rosenthal's methodology](https://www.vischer.com/en/knowledge/blog/part-7-the-eu-ai-act-what-it-means-in-practice-for-most-companies/) in June 2024, led by the company's Chief Information Security Officer and Chief Data Officer.

As the regulatory landscape continues to evolve, the company maintains a forward-looking approach through continuous updates to their public AI Governance Framework, active participation in regulatory consultations, and open and transparent collaboration with industry peers through initiatives like annually hosted AI Governance Roundtables.

## Going Forward

As the EU AI Act moves further into its implementation stage, there remain open questions and compliance challenges, specifically for businesses integrating and modifying AI models and systems.

In any case, the overall obligations for GPAI model providers are manageable, as they are essentially limited to keeping technical documentation and summaries within the scope of the modifications. Of course, GPAI model providers with systemic risk face more complex compliance requirements. The AI Office assumes that, as of today, [only few downstream modifications would meet the respective compute-thresholds](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act) which would trigger a shift in compliance responsibilities. Proper guidance is under way, and there are sufficient hints and proxies available that allow both integrators and modifiers to work towards EU AI Act compliance in the meantime.

The AI Office has also indicated in the [GPAI guidelines](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act) that GPAI model providers, including those performing modifications, who are anticipating compliance difficulties with respect to the August 2025 deadline should proactively get in touch with the AI Office through its recently launched [AI Act service desk](https://ai-act-service-desk.ec.europa.eu/en). The AI Act service desks established by individual EU Member States, such as the ones from [Germany](https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/EN/2025/20250703_KI_ServiceDesk.html) and [Austria](https://www.rtr.at/rtr/service/ki-servicestelle/KI-Servicestelle.en.html), can be another option to proactively reach out to authorities in complex cases.

Further, many big GPAI model providers have [committed](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai#ecl-inpage-Signatories-of-the-AI-Pact) to the GPAI Code of Practice, including [OpenAI](https://openai.com/global-affairs/eu-code-of-practice/), [Anthropic](https://www.anthropic.com/news/eu-code-practice), [Google](https://www.mlex.com/mlex/artificial-intelligence/articles/2370945/google-signs-eu-s-code-of-practice-for-ai-models) and [Mistral](https://www.linkedin.com/posts/audreyherblinstoop_we-were-the-first-to-announce-it-and-today-activity-7355617443525881858-OT9j/), signalling that there is also an intent to support downstream operators with appropriate documentation on AI models. This can help to mitigate the lack of vendor transparency, as highlighted above, in the upcoming months.

## General Recommendations for Organisations

If you are concerned about modifications of GPAI models and systems under the EU AI Act, review the [official GPAI guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers) of the AI Office and start assessing the use cases along the interpretations of the AI Office. The guidelines include further examples of when an organisation is to be considered a GPAI model provider.

Organisations that have now started to think about their EU AI Act compliance in more detail should use their momentum and proactively get going with AI governance initiatives, respecting that AI governance is much broader than regulatory compliance. Voluntary programmes like the European Commission's [AI Pact](https://digital-strategy.ec.europa.eu/en/policies/ai-pact) offer opportunities for peer exchange around the EU AI Act and can help to gain internal buy-in and create awareness for AI governance. The contributors of this article, for instance, proactively created a small, informal community of AI Pact members ("AIPEX") earlier this year to discuss current challenges and solutions to these in direct meetings, and members of the AI Office took the time to join one of their meetings.

### Recommended Actions and Resources for EU AI Act Preparation

- **Catalogue and classify AI use cases and systems**, as this is the foundation for proper assessment of role and risk under the EU AI Act. You can make use of free compliance checkers, such as from the [AI Office](https://ai-act-service-desk.ec.europa.eu/en/eu-ai-act-compliance-checker), on the [AI Act website](https://artificialintelligenceact.eu/assessment/eu-ai-act-compliance-checker/), or from the [AI governance platform provider Trail](https://www.trail-ml.com/eu-ai-act-compliance-checker). In edge cases, perform a thorough analysis internally and externally, e.g. with a law firm.
- **Conduct risk and impact assessments** when integrating or adapting GPAI models and AI systems.
- **Maintain documentation** for any modifications to AI systems or models. This is a straightforward measure, especially useful for periods of legal uncertainty. Even where regulatory obligations are not triggered, this is often useful and necessary for both internal stakeholders or customers.
- **Stay informed** with the developments around the EU AI Act to proactively work toward compliance as new guidelines are getting released. More detailed analyses and opinions can also help to refine your governance approaches, such as the "Compute and Consequence Screening" approach for granular differentiation of AI model modifications, proposed by [Hacker and Holweg (2025)](https://dx.doi.org/10.2139/ssrn.5289125).

## About the Authors

From the informal AI Pact Exchange Group ("AIPEX"):

- [Oystein Endal](https://www.linkedin.com/in/%C3%B8ystein-endal-10832162/), AI risk and compliance manager within the financial services and insurance sector.
- [Andrea Vrcic](https://www.linkedin.com/in/andrea-johansson-vrcic-6716a81b2/), legal counsel in AI regulation within the financial services and insurance sector.
- [Sidsel Nag](https://www.linkedin.com/in/sidsel-nag/), manager of AI ethics, regulation, and governance within the consulting sector, and member of the Danish Standardisation Committee.
- [Nick Malter](https://www.linkedin.com/in/nickmalter/), AI policy and governance manager at [trail GmbH](https://www.trail-ml.com/), an AI governance software company. Initiator of the AIPEX group.

From [Unique AI](https://www.unique.ai/):

- [Daylan Araz](https://www.linkedin.com/in/daylan-a-720ba5227/) is Data Compliance Officer at Unique AI in Zurich. He was instrumental in developing Unique's comprehensive AI Governance Framework. He has taken a lead role in achieving the ISO 42001 certification as well as contributing to ISO 27001, ISO 9001, and SOC 2 certifications. Reach out for more information: aigovernance@unique.ai.
