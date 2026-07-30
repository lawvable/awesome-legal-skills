# Template: Provider's Art. 31 custom-built carve-out assessment

Produces the provider's documented assessment of whether a data processing service falls within the custom-built carve-out under Article 31(1) of Regulation (EU) 2023/2854 (Data Act), with the consequence that the obligations in Art. 23(d), Art. 29, and Art. 30(1) and (3) do not apply. Also addresses the Art. 31(2) testing/evaluation carve-out and the Art. 31(3) pre-contractual information obligation.

Form: written internal assessment, with a customer-facing extract for the Art. 31(3) information obligation. Markdown by default. Internal assessment typically two to three pages; customer-facing extract typically one page.

PRECONDITION: The carve-out is narrow. Recital 91 makes clear that the carve-out applies only where the service is genuinely tailored and not offered at broad commercial scale. A provider that classifies broadly-available SaaS as custom-built misuses the carve-out.

PRECONDITION: The carve-out does not exempt the provider from the entire Ch VI. Arts. 25, 26, 27, and 30(2) still apply.

---

## Part 1: Internal assessment

```
[Provider letterhead or internal memo format]

Art. 31 custom-built carve-out assessment

Service: [Service identification]
Customer: [Customer identification]
Assessment date: [Date]
Assessor: [Assessing party]

---

1. The service

   Service name: [Name]
   Service description: [Functional description]
   Service category under Data Act: [IaaS / PaaS / SaaS;
   reference to Art. 2(8) data processing service definition]
   Customer: [Customer name]
   Contract date: [Date; or "proposed"]

2. The Art. 31(1) limbs

   The carve-out applies where:

   (a) the majority of main features has been custom-built to
       accommodate the specific needs of an individual
       customer; OR

   (b) all components have been developed for the purposes of
       an individual customer;

   AND

   (c) those data processing services are NOT offered at broad
       commercial scale via the service catalogue of the
       provider.

   Both prongs of the "OR" are alternatives; either suffices.
   The "AND" condition on broad commercial scale is cumulative
   with the "OR" prong.

3. Assessment of Art. 31(1)(a): majority of main features
   custom-built

   3(a) Identification of the main features of the service:

   [List the main features. Examples for an analytics platform:
   data ingestion; processing engine; storage layer; user
   interface; integration APIs; reporting; ML pipeline; admin
   tooling. The list should be coherent and exhaustive for the
   service.]

   3(b) For each main feature, identify whether it is custom-
   built or off-the-shelf:

   [Tabulate. Custom-built means tailored to accommodate the
   specific needs of this customer, not merely configured from
   a standard catalogue. Default off-the-shelf parameters that
   the customer can set within the standard product do not
   convert the feature into custom-built.

   Feature | Custom-built (Y/N) | Specific need accommodated
   -------|---------------------|----------------------------
   [Feature 1] | [Y/N] | [Need]
   [Feature 2] | [Y/N] | [Need]
   [...]

   Calculation: number of custom-built main features / total
   number of main features. The majority threshold requires >
   50%.]

   3(c) Conclusion on limb (a): [Majority of main features
   custom-built? Yes / No / Borderline]

4. Assessment of Art. 31(1)(b): all components developed for
   the customer

   [The "all components" prong is stricter than the "majority
   of main features" prong. If any component is standard or
   shared with other customers' services, this prong fails.
   The provider may rely on (a) instead if (b) fails.]

   [Tabulate. List all components: software components,
   hardware components where relevant, infrastructure
   components.

   Component | Developed for this customer (Y/N) | Notes
   ---------|-----------------------------------|------
   [Component 1] | [Y/N] | [Notes]
   [...]

   Conclusion on limb (b): [All components developed for the
   customer? Yes / No]]

5. Assessment of "not offered at broad commercial scale"

   [This is the load-bearing limb. A service that has been
   tailored to a single customer's needs but is also available
   in the provider's service catalogue does not fall within
   Art. 31(1). The service must not be marketed, sold, or
   offered to other customers in the provider's catalogue,
   product offering, or sales process.]

   5(a) Is the service listed in the provider's public service
   catalogue or marketing materials? [Y/N. If yes, the carve-
   out is unlikely to apply.]

   5(b) Has the service been offered or sold to other
   customers? [Y/N. Even one other customer engagement with
   the same service may defeat the carve-out, depending on the
   extent of tailoring across engagements.]

   5(c) Is the service derived from a standard product
   offering by parameter configuration, profile selection, or
   feature toggling? [Y/N. Standard products with custom
   configuration are typically not within the carve-out.]

   5(d) Is the service marketed as bespoke, white-glove,
   professional-services-delivered, or under similar terms
   indicating non-catalogue status? [Y/N]

   Conclusion: [Not offered at broad commercial scale? Yes /
   No]

6. Overall conclusion

   Carve-out applies: [Yes / No]

   [Reasoning. The carve-out applies only where (a) or (b) is
   met AND (c) is also met. If either part fails, the carve-out
   does not apply and the full obligations of Arts. 23(d), 29,
   30(1) and 30(3) apply.]

7. Consequences of the carve-out

   [Where the carve-out applies:]

   The following obligations do NOT apply to this service:
   - Art. 23(d): functional equivalence in the destination
     service.
   - Art. 29: switching charges discipline (i.e. the provider
     is not bound by the cost-basis discipline or the 12
     January 2027 abolition date for this service).
   - Art. 30(1): functional equivalence for IaaS.
   - Art. 30(3): repository publication of harmonised
     standards.

   The following obligations STILL apply:
   - Art. 23(a), (b), (c), (e): the remaining elements of
     removing obstacles to switching.
   - Art. 25: mandatory contract terms.
   - Art. 26: pre-contractual transparency.
   - Art. 27: information requirements during the contract.
   - Art. 28: good faith.
   - Art. 30(2), (4), (5): the remainder of Art. 30 not
     carved out.

   [The Art. 31 carve-out is targeted; it does not relieve the
   provider of Ch VI entirely.]

   [Where the carve-out does not apply:]

   The full Ch VI applies to this service, including Arts.
   23(d), 29, 30(1) and 30(3).

8. Art. 31(3) pre-contractual information obligation

   Where the carve-out applies, the provider must, prior to the
   conclusion of the contract, inform the prospective customer
   of the obligations of this Chapter that do not apply.

   The customer-facing extract is at Part 2 of this assessment.

9. Documentation and audit trail

   This assessment is retained in the provider's compliance
   records. It is updated where the service composition
   materially changes (new components, expansion to additional
   customers, marketing in the public catalogue).

10. Reviewer sign-off

    [Reviewer name, position, date]
    [Approver name, position, date]
```

---

## Part 2: Customer-facing extract for Art. 31(3) notification

```
[Provider letterhead placeholder]

To: [Prospective customer]

Date: [Date prior to contract conclusion]

Subject: Information under Article 31(3) of Regulation (EU)
         2023/2854 (Data Act): obligations of Chapter VI that do
         not apply to the proposed service

The data processing service [identifier] proposed for delivery
to [customer] falls within the scope of Art. 31(1) of the Data
Act (custom-built carve-out) for the reasons set out in our
assessment dated [date]. In accordance with Art. 31(3), we
inform you that the following obligations of Chapter VI of the
Data Act do not apply to this service:

- Art. 23(d): functional equivalence in the destination service.
- Art. 29: the cost-basis discipline on switching charges and
  the 12 January 2027 abolition of switching charges.
- Art. 30(1): functional equivalence for IaaS.
- Art. 30(3): publication of harmonised standards references
  for this service.

The remainder of Chapter VI applies in full, including:
- Art. 25 contract terms on switching;
- Art. 26 pre-contractual transparency;
- Art. 27 information requirements during the contract;
- Art. 30(2), (4), (5).

The customer's right to seek redress under Art. 38 and to
complain to the competent authority designated under Art. 37 is
not affected by the carve-out.

[Signature block placeholder]
```

---

## Citations supporting this template

- Art. 2(8) (data processing service definition): `sources/regulation-2023-2854.md` Art. 2.
- Art. 23 (removing obstacles to effective switching; the Art. 23(d) carve-out): `sources/regulation-2023-2854.md` Art. 23.
- Art. 25, Art. 26, Art. 27, Art. 28: `sources/regulation-2023-2854.md`.
- Art. 29 (switching charges): `sources/regulation-2023-2854.md` Art. 29.
- Art. 30 (functional equivalence, open interfaces, repository): `sources/regulation-2023-2854.md` Art. 30.
- Art. 31 (all paragraphs): `sources/regulation-2023-2854.md` Art. 31.
- Recital 91 (custom-built carve-out interpretation): `sources/regulation-2023-2854.md` Recital 91.
- Art. 37 (competent authority): `sources/regulation-2023-2854.md` Art. 37.
- Art. 38 (right to lodge a complaint): `sources/regulation-2023-2854.md` Art. 38.
- `sources/digital-omnibus-amendments-tracker.md` for the Art. 31 entry; the proposal may affect Art. 31 mechanics. Check current legislative status.
