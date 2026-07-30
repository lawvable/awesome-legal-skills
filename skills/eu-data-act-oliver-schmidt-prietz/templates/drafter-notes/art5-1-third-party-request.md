# Drafter notes: art5-1-third-party-request

The Art. 5(1) request is more procedurally complex than the Art. 4(1) request because three parties are involved (user, data holder, third party) and because Art. 5(3) introduces a gatekeeper exclusion that is the most common substantive defect in third-party requests.

## Substantive risks of using the template

- **The DMA gatekeeper exclusion is constitutive, not optional.** Art. 5(3) excludes DMA-designated gatekeepers as eligible third parties. A request directing data to a gatekeeper is invalid as an Art. 5(1) request, and the data holder cannot lawfully comply. The exclusion bites at three points: the gatekeeper cannot be the named third party (Art. 5(3)(c)); the gatekeeper cannot solicit or incentivise the user to direct data to it (Art. 5(3)(a) and (b)); and downstream, the third party cannot forward data to a gatekeeper under Art. 6(2)(d). The drafter must verify gatekeeper status against the Commission's current designation list (not a stale copy from a prior matter). See `references/gates/dma-gatekeeper.md`. The verification date should be recorded in the request itself.
- **Compensation is between the data holder and the third party, not the user.** Art. 5(1) requires delivery to the third party "free of charge to the user." The data holder may charge the third party under Arts. 8 and 9. The template does not negotiate compensation; that is for the third party's separate engagement with the data holder. Drafters sometimes inadvertently make compensation commitments on the user's behalf; do not.
- **Closed list of Art. 6(2) prohibitions.** Art. 6(2) lists eight prohibitions on the third party (dark patterns, profiling beyond service necessity, onward sharing without contract, sharing with a gatekeeper, competing-product development, security impact, undermining trade secrets, blocking consumer onward sharing). The user request should reflect the user's awareness of these; the third party's separate undertaking is the procedurally cleaner route, which is why the template suggests the third party's confirmation as an enclosure.
- **Personal data path under Art. 5(7) is identical to the Art. 4(12) path.** Where the user is an enterprise and is not the data subject, the user is a controller and needs a GDPR Art. 6(1) legal basis. The data holder cannot disclose personal data to the third party absent the legal basis. The third party will, on receipt, also be a controller (or sometimes joint controller, sometimes processor depending on facts) and must run its own GDPR analysis. The template puts the burden on the user to substantiate the legal basis; the drafter should make sure the user has actually done that work rather than rely on the placeholder.
- **The Art. 5(13) data subject rights preservation.** Art. 5(13) provides that the Art. 5(1) right "shall not adversely affect the rights of data subjects pursuant to the applicable Union and national law on the protection of personal data." Data subject rights run in parallel with the third-party right. The template does not need a clause on this; it follows from the GDPR overlay. But the drafter should verify that the user, where the user is not the data subject, has informed the data subjects of the disclosure path under GDPR Arts. 13 and 14.
- **Testing data carve-out under Art. 5(2).** Art. 5(2) carves out readily available data in the context of testing new connected products, substances or processes not yet placed on the market, unless the third party use is contractually permitted. The template assumes the connected product is on the market; check before sending.

## Pointers to gates and scenarios

- Scenario card: `references/scenarios/ch2-user-third-party-request.md` (includes gatekeeper check via DMA gate; trade-secret pre-engagement).
- DMA gate: `references/gates/dma-gatekeeper.md` (always run for Art. 5(1) requests).
- Trade-secret gate: `references/gates/trade-secrets-directive.md` (run if any trade-secret claim is anticipated; section 6 of the template engages stage 1 under Art. 5(9)).
- GDPR gate: `references/gates/gdpr-overlay.md` (always run if personal data is in scope; the section 7 personal-data clause selection depends on it).

## Common drafting mistakes the drafter should check for

- Naming the third party only by trade name rather than legal entity. Legal entity identification matters because gatekeeper designations are at the corporate-group level and because Art. 6 obligations attach to the legal entity, not the brand.
- Failing to specify the purpose. Art. 6(1) restricts the third party to processing for the purposes agreed with the user. A request without a specified purpose makes Art. 6(1) enforcement against the third party difficult and gives the data holder a defence to delay engagement.
- Including a generic "for any lawful purpose" clause. This collapses the Art. 6(1) restriction and weakens the user's later remedies if the third party processes for unauthorised purposes.
- Forgetting that "free of charge to the user" is one-sided. The user is not the cost-bearer; the third party is. Do not insert clauses about user payment obligations.
- Asking the data holder to validate the user-third-party purpose agreement. The data holder is entitled to verify user status (Art. 5(4)) but is not the policer of the user-third-party purpose agreement. Do not invite the data holder to second-guess it.
- Conflating Art. 4(1) and Art. 5(1) rights in the same letter. Where the user wants data both for itself and for a third party, draft two separate requests. The two regimes have different recipients, different downstream restrictions, and different gate triggers.
- Routing through the third party where the user should be the sender. The user is the rights-holder under Art. 5(1); the third party is the recipient. Where a party "acts on behalf of" the user under Art. 5(1) first sentence, the mandate should be enclosed. A request signed only by the third party without user authorisation is procedurally defective.

## Length and tone

Direct, three-party-aware. The letter is to the data holder but the third party is operationally on the receiving end. The drafter should ensure the third party has confirmed its operational readiness (endpoints, security posture, GDPR position) before the user sends the request; a request that lands at the data holder without the third party being ready is an own goal.
