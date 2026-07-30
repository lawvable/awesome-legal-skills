# Drafter notes: art4-6-trade-secret-safeguards-agreement

The stage-1 safeguards agreement is the foundational document for the entire trade-secret regime under Ch II. The strength of a stage-2 withholding or a stage-3 refusal later turns on what happened at stage 1. Drafters should treat stage-1 as the most important paperwork, not as a procedural pre-step.

## Substantive risks of using the template

- **Proportionality is the operative standard, and it cuts both ways.** Art. 4(6) requires "proportionate technical and organisational measures." The data holder cannot demand excessive safeguards (on-premises-only access, no internal sharing, NDA-by-NDA chains for each named accessor) where remote sandboxed access with logging is technically secure. Equally, the user cannot accept token safeguards (a verbal undertaking, an unsigned NDA, no access controls) and expect to defeat a later stage-2 withholding. The drafter should calibrate the package to the actual sensitivity of the data. See `references/gates/trade-secrets-directive.md` on the layered-approach recommendation.
- **Identification in the metadata is constitutive.** Art. 4(6) second sentence requires the data holder (or trade secret holder where different) to "identify the data which are protected as trade secrets, including in the relevant metadata." If the metadata does not flag the trade-secret records, the protection is at risk: the user can argue it did not know which records were protected and therefore did not breach. The template surfaces this in section 2; drafters should verify that the operational delivery actually carries the metadata flag, not just that the agreement says it does.
- **Single-layer NDA reliance is fragile.** NDAs alone are rarely sufficient under the regulation's standard. The McIntyre OSS enforcement signals show that competent authorities expect a layered approach (at least one strong technical measure plus organisational measures). Drafters should not let the negotiation collapse into NDA-only; if the data holder accepts NDA-only, it weakens any future stage-2 or stage-3 posture.
- **The "such as" list in Art. 4(6) is illustrative, not exhaustive.** Model contractual terms, confidentiality agreements, strict access protocols, technical standards, and codes of conduct are named. Other proportionate measures are admissible. Drafters can introduce watermarking, sandboxing, differential privacy treatments, or sectoral-specific measures as appropriate.
- **The MCTs are non-binding.** The Commission's model contractual terms (see `sources/mcts-sccs-recommendation-pointer.md`) provide a useful starting point. No safe harbour attaches to verbatim adoption. The drafter should adapt the MCTs to the actual matter rather than copy-paste them.
- **Use restrictions are layered.** Section 7 of the template cross-references Art. 4(10) and the TSD. Drafters should not duplicate those restrictions in the safeguards agreement (creating drafting drift between the source and the contract). Cross-reference is cleaner.
- **Stage-2 and stage-3 reservation in section 8.** The reservation does not give the data holder unilateral authority to invoke stage 2 or 3; it merely puts the user on notice that the data holder will use those mechanisms if the triggers arise. The reservation is not a substitute for actually meeting the stage-2 or stage-3 substantive thresholds.
- **The data holder vs trade secret holder distinction.** Where the data holder licenses-in trade secrets from a third party (e.g. a component supplier), the data holder is not the trade-secret holder for Art. 4(8) purposes. The template's preamble flags this. The drafter should ensure the licence permits the data holder to share the trade-secret data under the Art. 4(6) safeguards; some licences require the trade-secret holder's consent. This is a common stage-1 failure mode where a data holder cannot consummate stage-1 because its upstream licence is too restrictive.

## Pointers to gates and scenarios

- Scenario card: `references/scenarios/ch2-trade-secret-stages-1-2.md` (stage-1 and stage-2 mechanics).
- Trade-secret gate: `references/gates/trade-secrets-directive.md` (always loaded; technical and organisational measures section catalogues the menu the drafter selects from).
- GDPR gate: `references/gates/gdpr-overlay.md` (relevant where the trade-secret data is also personal data; the safeguards are cumulative, not alternative).
- Sectoral gate: `references/gates/sectoral-lex-specialis.md` (relevant where the connected product is in a regulated sector that may have its own confidentiality or trade-secret framework, e.g. type-approval data carve-outs for vehicles).

## Common drafting mistakes the drafter should check for

- Naming the trade-secret data only at the category level when field-level identification is available. Where the data holder can identify trade-secret fields, it should. Over-broad identification ("all telematics records") is treated as suspect and may not survive competent-authority scrutiny.
- Treating the safeguards agreement as a standalone NDA without the Art. 4(6) framing. The agreement should explicitly invoke Art. 4(6) so that the regulatory protection track is clear. A bare NDA may be valid contract but does not put the data holder in the Art. 4(6) stage-1 posture.
- Defining "trade secret" by reference to the agreement rather than to the TSD. The TSD Art. 2(1) three-limb test is the source. Drafting a contractual definition that diverges from the TSD makes a later substantive defence weaker.
- Imposing audit rights that exceed reasonable necessity. Audit-on-demand without notice, in perpetuity, is disproportionate. The template uses "reasonable notice" and a specified number of working days.
- Setting a duration that ends with the data delivery. Trade-secret obligations should outlast the underlying access period because the data, once delivered, retains its trade-secret character until it becomes generally known. The template uses "for the duration that the data retains trade-secret character" as the typical formulation.
- Drafting out the user's redress. Section 9 cross-references Art. 4(9), Art. 10, and Art. 37. A safeguards agreement that purports to bar the user from competent-authority complaint or dispute settlement is partly unenforceable under Art. 7(2) and substantially unenforceable as a matter of EU law.
- Forgetting the cross-reference to the underlying request. Where the safeguards agreement is meant to operationalise an Art. 4(1) response, the reference number and date of the underlying request should be visible. This matters for later evidence of the stage-1 record.

## Length and tone

Formal contract style, not a unilateral notice. The agreement is bilateral; both parties' obligations and rights are set out. Avoid stage-2 and stage-3 language elsewhere in the contract; section 8 is the only place those regimes are mentioned, and only as reservations.
