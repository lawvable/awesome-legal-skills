# Template: Data holder's response to an Art. 4(1) user request

Produces the data holder's substantive written response to a user's request for product and related service data under Article 4(1) of Regulation (EU) 2023/2854 (Data Act).

Form: formal letter. Markdown by default. One to two pages typical, depending on the scope of the requested data and any safeguards or limitations.

The template covers four typical response postures: (i) full compliance, (ii) compliance with trade-secret safeguards under Art. 4(6), (iii) compliance with format or scope clarifications, (iv) partial compliance with notice that trade-secret stage-1 negotiation is required before further data is released. For an outright refusal under Art. 4(8), use `art4-8-refusal-letter.md`. For a safety or security restriction under Art. 4(2), use `art4-2-safety-handbrake-notice.md`.

---

```
[Data holder letterhead placeholder]

To: [Requesting user, full legal entity name / natural person name
     and address]

Date: [Date of response]

Reference: [Internal reference; reference to the user's request
            date and any reference number the user used]

Subject: Response to your request for access to product data and
         related service data pursuant to Article 4(1) of
         Regulation (EU) 2023/2854 (Data Act)

1. Acknowledgement of the request

   [Data holder] received the user's request dated [date], in
   which the user requested access to [brief restatement of the
   scope of the request as the data holder understands it]. The
   data holder has identified the user as [the user of the
   following connected product(s): [identifiers] / the subscriber
   to the following related service(s): [identifiers]] and has
   verified user status on the basis of [enclosed user-status
   evidence / the data holder's records].

   [Where the user request named an acting party under Art. 4(1)
   second sentence: "The data holder has reviewed the mandate
   enclosed with the request and has confirmed [acting party]'s
   authority to act on behalf of the user."]

2. Scope of the data the data holder will make available

   The data holder will make the following data available, with
   the relevant metadata necessary to interpret and use the data:

   [Enumeration of categories of data with brief description.
   Indicate where the data is delivered as a one-time export, as a
   continuous feed, or via API access. Indicate the format
   (typically [JSON / CSV / Parquet / specified industry
   standard]).]

   [Where the data holder identifies data the user requested that
   falls outside Art. 4(1) scope, identify it and state the
   reason: "The following items requested by the user are not
   readily available data within the meaning of Art. 2(17) and
   are therefore not in scope of Art. 4(1): [items, with reason
   for each: e.g. derived data per Recital 15; data not generated
   in the use of the connected product or related service;
   information requested that is internal business data of the
   data holder]." If a substantial part of the request is out of
   scope, route the matter through `references/scenarios/ch2-data-
   holder-response.md` before sending; this template assumes the
   request is substantially in scope.]

3. Trade-secret identification (where applicable)

   [Where the data holder identifies any of the data as trade-
   secret-protected, identify it specifically:]

   The data holder has identified the following data as trade-
   secret-protected within the meaning of Art. 2(19) Data Act and
   Art. 2(1) of Directive (EU) 2016/943 (Trade Secrets Directive):

   [Category-by-category or field-by-field identification, with
   trade-secret tagging in the metadata where the data is
   provided in machine-readable form.]

   In accordance with Art. 4(6), the data holder proposes the
   following technical and organisational measures to preserve
   the confidentiality of the trade-secret-protected data:

   [Specific proposed measures. Examples (proportionality-
   calibrated; the actual measures are scenario-specific):

   - Confidentiality undertaking by the user, on the basis of
     [model contractual terms / a bespoke confidentiality
     agreement enclosed with this response].
   - Access control: data delivery to a designated point of
     contact authenticated as the user's authorised
     representative; restriction on internal sharing within the
     user organisation to named personnel.
   - Technical safeguards: encryption in transit and at rest;
     watermarking and fingerprinting for trade-secret records;
     audit logging on the user side with audit rights for the
     data holder on reasonable notice.
   - Incident response: defined notification procedure for
     suspected confidentiality breaches.]

   The data holder is prepared to negotiate proportionate
   adjustments to these measures with the user. The data holder
   will make the trade-secret-protected data available promptly
   upon the user's confirmation that the agreed measures are in
   place.

4. Delivery arrangements

   The data holder will deliver the data as follows:

   [Specifics of delivery: endpoint, format, schedule, real-time
   feed if applicable, retrieval window.]

   The data is provided of the same quality as is available to
   the data holder, in a comprehensive, structured, commonly used
   and machine-readable format, in accordance with Art. 4(1).
   [Where continuous and real-time delivery is feasible: "Where
   continuous and real-time delivery is technically feasible, the
   data holder will provide such delivery from [date]." Where it
   is not feasible: "Continuous and real-time delivery is not
   technically feasible at this time for the following reasons:
   [reasons]. The data holder will provide [alternative cadence]
   delivery."]

5. Compliance with personal data conditions (where applicable)

   [Where personal data is in scope and the user is the data
   subject: "The data includes personal data of the user as data
   subject. The user's rights under Regulation (EU) 2016/679
   (GDPR), including under Art. 15, are unaffected by this
   response."]

   [Where personal data is in scope and the user is not the data
   subject: "The data includes personal data of natural persons
   other than the user. The data holder is making this data
   available to the user on the basis that the user has
   represented that it has a valid legal basis for processing
   under Art. 6(1) GDPR and, where applicable, that the
   conditions of Art. 9 GDPR and Art. 5(3) of Directive 2002/58/EC
   are fulfilled, in accordance with Art. 4(12) of the Data Act.
   The data holder relies on this representation."]

6. Use restrictions notice (informational)

   The data holder draws the user's attention to the use
   restrictions in Art. 4(10) (no use of the data to develop a
   connected product that competes with the connected product
   from which the data originates; no sharing with a third party
   with that intent; no use to derive insights about the data
   holder's or manufacturer's economic situation, assets or
   production methods) and in Art. 4(11) (no use of coercive
   means or abuse of gaps in the data holder's technical
   infrastructure to obtain further data).

7. Contact point

   For questions regarding this response, including operational
   matters relating to data delivery, the user may contact [named
   contact or generic Data Act contact point under Art. 3(2)(g)].
   For matters related to the trade-secret safeguards under
   section 3, the user may contact [named contact, typically
   counsel-side or compliance-side].

8. Redress notice

   The user retains the right at any stage to lodge a complaint
   with the competent authority designated pursuant to Art. 37
   of the Data Act in the Member State of [data holder's
   establishment] and to seek redress before a court or tribunal
   of a Member State.

[Signature block placeholder]

Enclosures (where applicable):
- Confidentiality agreement / model contractual terms
- Technical specification for the proposed delivery arrangement
  (API documentation, schema, security posture)
- List of trade-secret-tagged metadata fields
```

---

## Citations supporting this template

- Art. 4(1) (the data holder's obligation to make data available): `sources/regulation-2023-2854.md` Art. 4(1).
- Art. 4(4) (no undue difficulty): `sources/regulation-2023-2854.md` Art. 4(4).
- Art. 4(5) (verification of user status): `sources/regulation-2023-2854.md` Art. 4(5).
- Art. 4(6) (trade-secret stage 1): `sources/regulation-2023-2854.md` Art. 4(6).
- Art. 4(10), (11), (13), (14): `sources/regulation-2023-2854.md` Art. 4.
- Art. 4(12) (personal data conditions where user is not data subject): `sources/regulation-2023-2854.md` Art. 4(12); Recital 34.
- Art. 2(17) (readily available data): `sources/regulation-2023-2854.md` Art. 2(17).
- Recital 15 (derived data exclusion): `sources/regulation-2023-2854.md` Recital 15.
- FAQ Q23 (Commission interpretation on stage-1 safeguards), framed as Commission interpretation.
