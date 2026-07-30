# Drafter notes: art31-custom-built-assessment

The Art. 31 carve-out is narrow and is being used aggressively by some cloud providers to escape the most demanding Ch VI obligations. The drafter's job is to apply Art. 31 strictly. A loose assessment exposes the provider to enforcement and exposes the customer to Ch VI workarounds.

## Substantive risks of using the template

- **The carve-out is narrow.** Art. 31(1) requires either (a) majority of main features custom-built to accommodate the specific needs of an individual customer, OR (b) all components developed for the purposes of an individual customer; AND (c) not offered at broad commercial scale via the service catalogue. The conjunction is constitutive. Many providers who claim Art. 31 have services where some features are customised but the underlying platform is broadly available; these fail limb (c).
- **"Customisation" vs "custom-built".** Default configuration of a standard product is not custom-built. Choosing options from a feature menu is not custom-built. Custom-built means the feature was developed for the customer, in response to the customer's specific needs, and exists for that customer's engagement.
- **"Broad commercial scale" is the load-bearing limb.** A service offered to even a few other customers through the catalogue is typically not within the carve-out. The drafter should be strict; the standard is "not at broad commercial scale" not "not at large scale." Section 5 of the template forces the four sub-tests.
- **Art. 31(2) testing/evaluation is a separate carve-out.** Art. 31(2) excludes data processing services provided as a non-production version for testing and evaluation purposes and for a limited period of time. This is a different carve-out from Art. 31(1) and applies to a different class of service. The template focuses on Art. 31(1); for Art. 31(2), use a separate analysis (typically less complex).
- **Art. 31(3) information obligation is mandatory.** Where the carve-out applies, the provider must inform the prospective customer of the obligations of Ch VI that do not apply. This is pre-contractual. A provider that relies on the carve-out without giving the Art. 31(3) information is itself non-compliant; the carve-out applies but the provider has breached the disclosure obligation. The template's Part 2 produces the customer-facing extract.
- **The carve-out does not relieve the full chapter.** Section 7 of the template enumerates what is and is not carved out. Arts. 25, 26, 27, 28 still apply. Drafters who treat Art. 31 as a comprehensive escape from Ch VI are wrong.
- **Aggressive carve-out claims attract competent-authority attention.** The competent authority under Art. 37(4)(b) (with experience in data and electronic communications services) is positioned to scrutinise carve-out claims. Providers should expect that a carve-out claim, particularly where the customer disputes it, will be reviewed.
- **The Digital Omnibus.** COM(2025) 833 final proposes amendments that may affect Art. 31 mechanics. The current source-freshness date is 15 May 2026; the proposal is in co-legislator negotiation, not adopted. The drafter should check `sources/digital-omnibus-amendments-tracker.md` and draft on current law.

## Pointers to gates and scenarios

- Scenario card: `references/scenarios/ch6-custom-built-carve-out.md` (Art. 31 narrow reading).
- Sectoral gate: `references/gates/sectoral-lex-specialis.md` (relevant where the service is sector-specific and the carve-out interacts with sectoral cloud regulation, e.g. DORA in financial services).
- Member State gate: `references/gates/member-state.md` (relevant for the competent authority).

## Common drafting mistakes the drafter should check for

- Treating "configured" as "custom-built". Configuration within a standard product's parameter space is not custom-built.
- Treating "available on request" or "not in the public catalogue" as equivalent to "not offered at broad commercial scale". A service that is sold to multiple customers, even off-catalogue, may not be within the carve-out.
- Treating a single past engagement as not "broad commercial scale" without thinking through the future. A service intended for one customer today but designed to scale to a wider commercial base is borderline; the drafter should be conservative.
- Failing to identify the main features clearly. The "majority of main features" test depends on a coherent feature enumeration. A vague or padded list can be manipulated; a strict and exhaustive list produces a defensible analysis.
- Applying limb (b) loosely. "All components developed for the customer" is a high bar. Most services use at least some off-the-shelf components (cloud infrastructure, standard libraries, common UI elements). Limb (b) fails for these services; limb (a) may still succeed.
- Failing to update the assessment as the service evolves. A service that genuinely was custom-built for one customer at inception may, over time, be offered to other customers; once it does, the carve-out lapses.
- Omitting the Art. 31(3) information notification. The pre-contractual information is mandatory; section 8 of the template surfaces it.
- Treating the carve-out as a defence against customer switching demand. The carve-out exempts specific obligations; it does not exempt the provider from supporting the customer's actual exit, which is governed by Arts. 25 and 26 and remains in force.

## Length and tone

Documented, evidence-based, conservative. The assessment is a compliance artefact that the provider may need to defend before a competent authority. The drafter should produce an assessment that survives scrutiny, not one that maximally favours the provider's carve-out claim.

Conservative drafting is the right posture: where the analysis is borderline, treat the carve-out as not applying. The cost of mistakenly claiming the carve-out is enforcement and possible customer complaint; the cost of mistakenly disclaiming the carve-out is some additional Ch VI obligations the provider would meet anyway. The asymmetry favours conservatism.
