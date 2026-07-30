# Commission Guidance on Vehicle Data accompanying the Data Act — pointer file

**This file does not redistribute the guidance text.** It documents the existence, status, and intended use of the Commission's sectoral guidance on vehicle data, and points to the authoritative Commission source. This skill treats sectoral lex specialis as gate-only: outputs warn the user that vehicle-data scenarios touch a sectoral overlay, and direct them to the Commission's guidance and to specialist vehicle counsel, rather than attempting full vehicle-specific analysis within the skill.

## Basics

| Field | Value |
|-------|-------|
| Instrument | Commission Guidance on vehicle data, accompanying the Data Act |
| Legal status | Commission guidance document. Non-binding. Reflects the Commission's interpretation of how the Data Act interacts with the automotive sector. Does not override Regulation (EU) 2018/858 (vehicle type-approval), Regulation (EU) 2019/2144 (general safety), or any other vehicle-specific Union law. |
| Authoritative source | https://digital-strategy.ec.europa.eu/en/library/guidance-vehicle-data-accompanying-data-act |
| Licence | CC BY 4.0 (European Union) |
| Position in Commission Data Act guidance suite | Listed alongside the Data Act FAQs and the MCTs/SCCs Recommendation on the Data Act explained landing page (https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained) as one of the three main Commission guidance publications. |

## Why the skill keeps this as gate-only

Vehicle data is a sectoral lex specialis space layered on top of horizontal Data Act rules. Doing it properly requires knowing:

- Regulation (EU) 2018/858 on the approval and market surveillance of motor vehicles (vehicle type-approval framework). Provides certain access rights for repairers and independent operators that pre-exist the Data Act.
- Regulation (EU) 2019/2144 on type-approval requirements for general safety (event data recorders, driver monitoring, etc.).
- Sector-specific delegated and implementing acts under those instruments.
- Long-standing market practice in extended vehicle data (ExVe) and in-vehicle data access debates that go back to the 2010s.
- The Commission's view, expressed in this Guidance, on how Articles 3, 4, and 5 of the Data Act apply to connected vehicles and how the type-approval regime interacts.

This is a specialist field. A general Data Act skill that attempts to opine on connected-vehicle deliverables without that sectoral knowledge will produce wrong answers. The skill's role here is to recognise the scenario, gate it, and redirect.

## How the skill should use this Guidance

- **Recognise the gate.** If the scenario involves a connected vehicle, a fleet of connected vehicles, vehicle telematics, ExVe, in-vehicle access, or a related service tied to a vehicle (e.g. a connected-vehicle app, an aftermarket service for vehicles), the skill should detect this and route to the gate behaviour described below.
- **Gate behaviour.** Output should:
  1. Confirm the horizontal Data Act analysis the user asked for, framed as "this is the general Data Act position; sectoral overlays may alter the analysis".
  2. Flag that Regulation (EU) 2018/858, Regulation (EU) 2019/2144, and any implementing acts may impose specific obligations or grant specific rights that interact with the Data Act answer.
  3. Point to the Commission's Vehicle Data Guidance at the URL above as the Commission's published view on the interaction.
  4. Recommend that the user consult specialist automotive counsel for any matter that will reach a deliverable, contract, or product decision, especially for type-approval, safety-recall, and ExVe scenarios.
- **Do not redistribute.** Skill outputs should not paste guidance text from this skill into deliverables; the authoritative version is the one on the Commission's page.
- **FAQ Q12 supports the gate.** FAQ Q12 (in this skill) confirms that the Data Act applies to connected products subject to conformity assessment or type approval, but that the specific need for conformity assessment is determined by legislation other than the Data Act. The skill's vehicle gate aligns with this: horizontal Data Act rules apply, but sectoral type-approval rules govern the specifics.

## Cross-references in this skill

- `references/gates/sectoral-lex-specialis.md` (to be drafted in Phase 3) is the gate catalogue. The vehicle gate will be one of the entries there, alongside MDR (medical devices), DORA (financial services), CRA (cyber resilience), AI Act, eIDAS, and energy/agricultural sector overlays.
- This pointer file is referenced from the gate; the gate is the routing mechanism, and this file is the substantive backstop pointer.

## Provenance

- Pointer file authored: 2026-05-15
- The Commission's vehicle data debate has been active since at least 2017. Confirm the current page status and the published date of the Guidance before each major client deliverable that depends on it.
