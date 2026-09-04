# Connected-Product Data Access and B2B Sharing

This reference covers Articles 3 to 12. First confirm Chapter II scope and the Article 7 conditions using `scope-assessment.md`.

## Contents

1. Article 3 design and transparency
2. Article 4 user access
3. Article 5 third-party sharing
4. Article 6 recipient controls
5. Trade-secret decision sequence
6. Articles 8 and 9 B2B terms and compensation
7. Dispute and misuse controls
8. Operational validation

## 1. Article 3 Design and Transparency

### Article 3(1): access by design

For connected products and related services placed on the market after 12 September 2026, assess whether product data, related-service data, and necessary metadata are by default:

- easy and secure to access;
- free of charge;
- comprehensive, structured, commonly used, and machine-readable;
- directly accessible where relevant and technically feasible.

The operative date comes from Article 50. It is a placing-on-the-market rule, not a design-start date.

### Article 3(2): product-contract information

Before purchase, rent, or lease, the seller, rentor, or lessor must provide clear and comprehensible information on:

- data type, format, and estimated volume;
- continuous and real-time generation;
- on-device or remote storage and retention;
- access, retrieval, and, where relevant, erasure, including technical means, terms of use, and quality of service.

### Article 3(3): related-service information

Before the related-service contract, the provider must supply the listed information on product and service data, use purposes, holder identity and contact, third-party sharing, complaint rights, trade secrets, duration, and termination.

## 2. Article 4 User Access

Where direct access is unavailable, Article 4(1) applies to readily available data and necessary metadata. Build the control against each element:

| Requirement | Evidence |
|---|---|
| Simple electronic request where technically feasible | request interface and user journey |
| Without undue delay | timestamps and service records |
| Same quality available to holder | source/output comparison |
| Easy, secure, free to user | authentication, authorization, fee schedule |
| Comprehensive, structured, common, machine-readable | schema and export sample |
| Continuous and real-time where relevant and technically feasible | technical assessment and interface behavior |

The Regulation does not set a universal hour or day response target for Article 4. Internal service levels may be implementation recommendations, but must be labeled as such.

### Limits and safeguards

- Article 4(2): contractually restrict or prohibit processing only where it could undermine legally grounded product security requirements and seriously harm natural persons' health, safety, or security. A refusal triggers competent-authority notification.
- Article 4(4): do not make rights unduly difficult or use non-neutral interface design.
- Article 4(5): request only information necessary to verify user status; limit access logging to execution, security, and maintenance needs.
- Article 4(6) to (9): apply the trade-secret sequence below.
- Article 4(10): user may not develop a competing connected product or share with that intent and may not derive specified insights about the manufacturer or holder.
- Article 4(11): no coercion or abuse of infrastructure gaps.
- Article 4(12): where user and data subject differ, personal-data disclosure requires a valid GDPR basis and, where relevant, Article 9 GDPR and Article 5(3) ePrivacy conditions.
- Article 4(13) and (14): control the holder's use and onward sharing of non-personal readily available data.

## 3. Article 5 Third-Party Sharing

On a user request, Article 5(1) requires the holder to make readily available data and necessary metadata available to an eligible third party. Apply the same quality, ease, security, format, timing, and conditional continuous/real-time elements. Access is free to the user, while Articles 8 and 9 govern B2B terms and compensation with the recipient.

Before release, verify:

- requester is the user or authorized agent;
- recipient is not a DMA gatekeeper under Article 5(3);
- purpose and recipient identity are recorded;
- personal-data basis exists under Article 5(7);
- trade-secret measures satisfy Article 5(9) to (12);
- B2B arrangements meet Articles 8 and 9.

Article 5(2) excludes testing data for new connected products, substances, or processes not yet placed on the market unless third-party use is contractually permitted.

## 4. Article 6 Recipient Controls

The third party must use data only for the purpose and conditions agreed with the user and erase it when no longer necessary, unless the user agrees otherwise for non-personal data.

Article 6(2) prohibits, among other things:

- manipulative or obstructive user interfaces;
- profiling unless necessary to provide the requested service;
- onward sharing without the user's contractual basis and trade-secret measures;
- making data available to a DMA gatekeeper;
- developing a competing connected product or sharing for that purpose;
- specified detrimental insights about the data holder;
- use that adversely affects product or service security;
- disregarding agreed trade-secret safeguards;
- preventing a consumer user from sharing received data with others.

Do not recast Article 6 as a list of holder refusal grounds.

## 5. Trade-Secret Decision Sequence

For user access, apply Article 4(6) to (9). For third-party sharing, apply Article 5(9) to (12).

1. Identify the protected data, including in metadata, and the trade-secret holder.
2. Agree proportionate technical and organisational measures before disclosure.
3. If measures are not agreed or implemented, or confidentiality is undermined, the holder may withhold or suspend the identified trade-secret data. Give a substantiated written decision without undue delay and notify the Article 37 authority.
4. A case-specific refusal is available only in exceptional circumstances where the holder as trade-secret holder objectively demonstrates a high likelihood of serious economic damage despite safeguards. Give reasons in writing and notify the authority.
5. Inform the user or third party of complaint, dispute-settlement, and judicial routes.

Trade-secret status is not a blanket exclusion.

## 6. Articles 8 and 9 B2B Terms and Compensation

Article 8 requires fair, reasonable, non-discriminatory, transparent terms when a holder must make data available to a business recipient.

Article 9 permits reasonable, non-discriminatory compensation that may include a margin. The parties consider:

- making-available costs, particularly formatting, electronic dissemination, and storage;
- investments in collecting and producing data, including others' contributions;
- volume, format, and nature of data.

For an SME or qualifying not-for-profit research recipient without non-SME partner or linked enterprises, compensation cannot exceed Article 9(2)(a) costs. The holder must explain the calculation basis in sufficient detail under Article 9(7).

There is no statutory rule permitting a fee solely because a request is frequent or complex.

## 7. Dispute and Misuse Controls

- Article 10: certified dispute settlement for Article 4(3), Article 5(12), Articles 8 and 9, and certain trade-secret safeguards. A decision is binding only if the parties explicitly consent before the proceeding.
- Article 11: proportionate technical protection measures and remedies for specified unauthorized acquisition, use, or disclosure.
- Article 12: Chapter III applies to qualifying B2B statutory data-sharing duties; detrimental contractual derogation is not binding.

## 8. Operational Validation

Test at least:

- one ordinary user-access request;
- one authorized-agent request;
- one third-party request containing personal data;
- one trade-secret scenario;
- one ineligible gatekeeper recipient;
- one request spanning unavailable, inferred, and readily available data;
- one SME recipient compensation calculation;
- export quality, completeness, security, latency, and revocation.

Record the result, evidence artifact, legal anchor, and any deviation. Do not treat a policy document as proof that the technical path works.
