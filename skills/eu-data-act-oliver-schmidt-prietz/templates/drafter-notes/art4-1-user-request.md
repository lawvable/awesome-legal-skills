# Drafter notes: art4-1-user-request

The Art. 4(1) request is procedurally simple and substantively load-bearing. The drafting failures are almost entirely about under-specifying the dataset, mis-positioning the user under GDPR, and waiving rights inadvertently by adding boilerplate the regulation does not require.

## Substantive risks of using the template

- **Under-specifying the dataset.** The data holder's response quality tracks the request's specificity. A request for "all telematics data" invites a partial response that the data holder will later defend as compliant. Identify categories, fields where known, and time windows. Where the user lacks visibility into the schema, ask for the schema before naming fields, citing Art. 3(2)(c) where the data holder is subject to the pre-contractual transparency obligation.
- **Disclosing the purpose unnecessarily.** Art. 4(1) does not condition the access right on disclosure of purpose. Disclosure is sometimes tactically useful (it can preempt an Art. 4(2) safety objection or focus the data holder's response) but it is never required. Where the user's purpose is sensitive (planning a switch of service provider, building a competing aftermarket product within the limits of Art. 4(10), or supporting a regulatory complaint), purpose should be omitted.
- **The Art. 4(10) compete-with restriction.** The regulation prohibits the user from using the data to develop a connected product that competes with the connected product from which the data originate. A related service is permitted (Recital 32). Where the user's stated purpose risks reading as competitive-product development, the data holder will lean on Art. 4(10) and may try to convert the disagreement into a trade-secret refusal. Draft purpose statements (if included) with awareness of the competing-product line.
- **GDPR mis-positioning.** Recital 34 makes the user-not-data-subject route to controller status explicit. Enterprises requesting data that contains personal data of the connected product's natural-person users (drivers, employees, household members) act as controllers under Art. 4(12) and need a GDPR Art. 6(1) legal basis. Submitting an Art. 4(1) request without having the GDPR position settled exposes the user to a delayed response or partial refusal once the data holder runs the Art. 4(12) check. See `references/gates/gdpr-overlay.md` (Case B and C in the scoping table).
- **CYA language the regulation does not require.** "Without prejudice to all other rights" is fine. "This request is not a formal demand and the user reserves the right to withdraw" is harmful: it lets the data holder treat the request as exploratory and delay. The regulation requires no formula, but the request should be unambiguously an Art. 4(1) request.
- **The "without undue delay" SLA.** The regulation does not specify a numeric SLA. See `references/gotchas.md` entry 4. The template asks for confirmation within a stated period but does not invent a numeric deadline for the substantive response. Where the matter is time-critical, the user should be ready to lodge a complaint under Art. 37(5)(b) if the data holder does not engage within a reasonable window.

## Pointers to gates and scenarios

- Scenario card: `references/scenarios/ch2-user-direct-request.md` (request preparation, identity verification, safeguards expectations).
- Trade-secret gate: `references/gates/trade-secrets-directive.md` (relevant if the user anticipates a trade-secret pre-engagement under section 6 of the template).
- GDPR gate: `references/gates/gdpr-overlay.md` (always run if personal data is in scope; the section 7 personal-data clause selection turns on the gate's analysis).
- Sectoral gate: `references/gates/sectoral-lex-specialis.md` (run if the connected product is in a regulated sector; vehicles, medical devices, energy infrastructure, and CRA-covered devices have additional layered obligations that may affect format and metadata expectations).

## Common drafting mistakes the drafter should check for

- Naming "the data" without naming the connected product or related service. The Art. 4(1) right runs from the connected product or related service, not abstractly.
- Failing to verify user status before sending. Art. 4(5) entitles the data holder to verify the user's status but bars it from demanding more information than necessary. Pre-empt the verification by enclosing the user-status evidence in the first letter.
- Omitting the relevant metadata clause. Art. 4(1) covers "data" and "the relevant metadata necessary to interpret and use those data." Data without metadata is often useless. The template surfaces this; do not let the user delete the metadata clause in editing.
- Stating "real-time" without qualifying technical feasibility. Art. 4(1) requires continuous and real-time delivery "where relevant and technically feasible." A blunt demand for real-time delivery on a connected product that cannot support it gives the data holder an easy defence. Phrase as the template does: "where continuous or real-time delivery is technically feasible."
- Sending to a generic legal address. Where the data holder has published a Data Act contact point under Art. 3(2)(g), use it. Routing to a generic legal mailbox slows engagement.
- Forgetting the Art. 4(11) coercive-means line. The template does not include it because it is a restriction on the user, not a representation. But the drafter should ensure the request does not describe coercive or workaround techniques the user might have used to obtain data without the data holder's cooperation.

## Length and tone

This is a request, not a demand letter. Calm, precise, complete. Do not threaten litigation, do not enumerate competent-authority complaint procedures as if they were imminent. The reservation of rights in section 9 is sufficient. Where the user has reason to anticipate non-cooperation (prior disputes with the data holder, sector with known compliance gaps), reserve the harder posture for the follow-up communication after the data holder's first response.
