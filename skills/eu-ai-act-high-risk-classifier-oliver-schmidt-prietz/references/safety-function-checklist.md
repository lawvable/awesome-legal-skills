# Safety function checklist (Art. 3(14) AI Act)

> Use this checklist for **Scenario (i)** of the Art. 3(14) two-prong test — the **intent-based** safety-function determination.

## Preventive functions (any one triggers safety-function status)

- Monitoring and detection of situations leading to physical harm (e.g., AI detecting abnormal system behaviour).
- Monitoring/detection of maintenance or inspection needs whose failure may lead to harm.
- Prevention of physical harm to people or property (e.g., AI preventing start-up on abnormal behaviour).
- Supervision of another system that performs a safety function (e.g., AI monitoring in real time a safety component via sensors).

## Mitigation functions (any one triggers safety-function status)

- Control or limitation of physical harm.
- Mitigation of consequences (e.g., safe-stop triggers).
- Control of another system that performs a safety function.

## NOT safety functions (explicit non-examples)

- Performance optimisation where failure does not directly risk health/safety.
- Service efficiency or product functioning optimisation (e.g., billing, claims).
- Quality control of non-safety functions (e.g., quality-of-service monitoring).
- Comfort, convenience, user-preference automation.

## Worked safety-component examples (¶45 — safety function path)

- Machinery: AI vision detecting human presence in robot cell, triggering safe stop.
- ATEX: AI monitoring gas concentrations, commanding shutdown.
- Pressure equipment: AI predicting runaway pressure, actuating shutdown.
- Rail: AI monitoring speed / preventing collisions.

## Worked safety-component examples (¶46 — failure-based path)

- Lifts: AI for door closing / obstacle detection — efficiency intent but failure injures.
- Vehicles: lane-assist AI — UX intent but failure causes collision.
- Agriculture: chemical-spray targeting AI — optimisation intent but failure endangers nearby persons.

## Worked NON-safety-component examples (¶47)

- Toys: AI recommending music in a connected toy.
- Agriculture: AI for yield forecasting / irrigation optimisation (where failure does not endanger).

## Borderline / vulnerable-user considerations (¶48 footnote 5)

For consumer smart appliances (thermostats, washing machines, air purifiers, refrigerators, TVs), the default is NOT a safety component. Exception: smart door locks, child-lock functions, devices used by/around children or vulnerable users may qualify under the failure-based prong.

## Source

- Art. 3(14) AI Act (definition of safety component).
- Commission Guidelines Annex I, ¶37 box, ¶¶45–49.
- Full text: the Commission Draft Guidelines on Art. 6 classification (2026), Annex I section.
