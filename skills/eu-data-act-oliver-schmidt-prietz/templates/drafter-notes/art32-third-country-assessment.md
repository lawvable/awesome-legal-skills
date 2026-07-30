# Drafter notes: art32-third-country-assessment

The Art. 32 assessment is among the highest-risk provider-side analyses in the skill. The provider is positioned between conflicting legal obligations: the third-country authority's order, the Union and national law, and contractual undertakings to the customer. Errors expose the provider to enforcement on multiple fronts, customer claims, and reputational damage. Drafters must hold all three regimes in view.

## Substantive risks of using the template

- **Art. 32 is non-personal data only.** Personal data is governed by GDPR Chapter V (Arts. 44-50), with Art. 48 GDPR providing a parallel regime for third-country judicial or administrative orders. The Data Act does not displace the GDPR; both regimes operate. Mixed datasets require dual analysis: the personal-data component under GDPR Chapter V; the non-personal-data component under Art. 32. The template focuses on Art. 32. For personal data, the provider must run the GDPR analysis separately (likely with a separate template or workflow).
- **Path A and Path B are alternatives, not sequential.** Path A (international agreement) is the cleaner route. Path B (cumulative conditions) applies only where Path A does not. A provider that has an applicable MLAT route may not need to run Path B at all. The drafter should look hard at Path A first; many third-country orders are issued without reference to an applicable MLAT, but if an MLAT is available and properly invoked, the analysis is shorter.
- **The Art. 32(3) cumulative conditions are conjunctive.** Three limbs, all must be met. The most commonly failed limb is (c): the competent third-country court or tribunal must be empowered to take duly into account the relevant legal interests of the provider protected by Union or national law. Many third-country systems do not give the reviewing court that power. Where any limb fails, the provider may reject.
- **The national body consultation is a powerful tool.** Art. 32(3) second subparagraph allows the provider to consult the relevant national body or authority competent for international cooperation in legal matters. The opinion, where supportive of rejection, strengthens the provider's position. The one-month window is a procedural safeguard: if no reply within one month, the provider may proceed (typically to reject) on the basis the conditions are not met. Drafters should consult promptly upon receiving a third-country request.
- **The Commission consultation route.** The national body may consult the Commission. Where the matter is significant, this can produce a Union-level position on the request. Drafters should signal this possibility to the national body in the consultation request.
- **National security and defence interest path.** Where the request may impinge on national security or defence interests of the Union or its Member States, the provider asks the relevant national body whether the data requested concerns those interests. This is a separate consultation track and may also produce grounds to reject.
- **Minimum-data response under Art. 32(4).** Even where the conditions are met (Path A or Path B), the provider provides the minimum amount of data permissible. The drafter should construct the minimum-data response carefully: too much exposes the provider to over-disclosure liability; too little exposes the provider to enforcement by the third-country authority. The "reasonable interpretation" standard gives the provider room to construe the request narrowly.
- **Customer notification under Art. 32(5).** Pre-compliance notification is the default. The law-enforcement carve-out is narrow: only where the request serves law enforcement purposes and only for as long as necessary to preserve effectiveness. Providers should not extend the law-enforcement window beyond what is strictly necessary. Where the carve-out applies, the provider should diary the moment when notification becomes possible.
- **Recitals 102-104 background.** The recitals reflect the legislator's concern about overreach by third-country authorities, particularly those that issue orders extraterritorially. The drafter should read the recitals as a hermeneutic guide: Art. 32 is to be interpreted with the protective intent in mind, not as a permissive transit mechanism.
- **Documentation and the Art. 37 competent authority.** The assessment may need to be provided to the competent authority on request. Documentation is therefore a compliance asset, not just an internal record.

## Pointers to gates and scenarios

- Scenario card: `references/scenarios/ch7-third-country-request.md` (Art. 32(3) cumulative limbs; national body consultation).
- GDPR gate: `references/gates/gdpr-overlay.md` (always run where the data is mixed; Art. 48 GDPR parallel; Schrems II considerations for any personal-data component).
- Trade-secret gate: `references/gates/trade-secrets-directive.md` (relevant where the data is trade-secret-protected; trade-secret considerations strengthen the consultation case under Art. 32(3) second subparagraph).
- Sectoral gate: `references/gates/sectoral-lex-specialis.md` (relevant where the data is in a regulated sector; sectoral confidentiality regimes may provide additional grounds for conflict under Art. 32(1)).
- Member State gate: `references/gates/member-state.md` (relevant for the national body identification and procedural mechanics).

## Common drafting mistakes the drafter should check for

- Running the Art. 32 analysis as if it covered personal data. Personal data falls under GDPR Chapter V. Mixed datasets need dual analysis.
- Treating Path A and Path B as cumulative. They are alternatives.
- Conceding the Art. 32(3) cumulative conditions without scrutiny. Each limb requires real analysis; the (c) limb in particular often fails because third-country reviewing courts cannot consider EU legal interests.
- Failing to consult the national body where consultation is appropriate. The opinion (or the expiry of the one-month window without reply) is procedurally and substantively valuable.
- Over-disclosing under Art. 32(4). The minimum-data discipline is real; the provider should construe the request narrowly.
- Misapplying the law-enforcement notification carve-out. The carve-out is for the time strictly necessary; it is not a blanket exemption from customer notification.
- Treating the customer notification as merely procedural. Customer engagement may reveal facts that affect the assessment (the data is trade-secret-protected, contains IP, has national security implications) and may produce contractual or commercial issues the provider must address.
- Forgetting the provider's GDPR posture for personal data. Even if the Art. 32 non-personal-data analysis concludes the data may be transferred, the GDPR may prohibit the transfer of personal data in the same dataset.
- Treating "in force between the requesting third country and the Union" as covering bilateral US-EU MLATs alone. The text covers EU-level and Member-State-level agreements.
- Failing to document the assessment. The Art. 37 competent authority can request the assessment; the provider needs the audit trail.

## Length and tone

Documented, conservative, legally tight. The provider is operating at the intersection of Union law, Member State national law, third-country law, and contractual obligations to the customer. The assessment should survive scrutiny by all of them. The tone is restrained; assertions are evidenced; conclusions are reasoned.

The provider's posture is typically reactive: the third-country authority has acted, and the provider is responding. Speed matters (the third-country authority will have a compliance deadline), but the substantive analysis must not be rushed. The provider's competent authority and the customer will look at the assessment; the provider's legal exposure depends on it being right.
