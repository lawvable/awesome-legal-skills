# Changelog — JEP skill

## [1.0.3] — 2026-06-02

### Fixed
- `references/jurisprudence-map.md`: the four additional macrocasos (08-11) opened in **2022-2023** (Caso 11 in September 2023), not "2022".

## [1.0.2] — 2026-06-02

### Changed
- Softened the over-confident reliability claim in `SKILL.md` ("retrieval to jep.gov.co succeeds reliably") to acknowledge that direct fetch can fail (HTTP 403, timeout, non-rendering PDF) and that such failure is structural, not fatal — pointing to the fallback ladder rather than treating a successful fetch as guaranteed. Aligns the JEP skill with the repository-wide direct-fetch-failure posture (`CLAUDE.md` §3).

## [1.0.1] — 2026-05-30

### Fixed
- Corrected the description of `Auto 033 de 2021` in `references/jurisprudence-map.md`: it is the Caso 03 **prioritisation** auto (12 February 2021, prioritising six subcasos), not a "determinación de hechos y conductas, Subcaso Antioquia". Added dates to the Caso 03 autos and confirmed `Auto 128 de 2021` (Costa Caribe, Batallón La Popa) against jep.gov.co.

## [1.0.0] — initial release

### Added
- `SKILL.md` — entry point, verification-first discipline, standard workflow (Step 0 identifies macrocaso + organ + document type), institutional architecture (SIVJRNR; JEP + CEV + UBPD; constitutional anchoring; 2018 launch; first sentences September 2025), source hierarchy, citation format with 11 macrocasos table, principal organs (3 Salas de Justicia + Tribunal Especial para la Paz with 4 Secciones + UIA + Sala Plena), tripartite sanctions regime (propias / alternativas / ordinarias), substantive doctrine pointers (material/temporal/personal competence; non-amnestiable crimes; TOAR; régimen de condicionalidad; victim participation), sensitive contexts (52-year conflict, 450,000+ killed, restorative justice politically contested)
- `references/authoritative-sources.md` — Tier 1 (jep.gov.co principal, CEV, UBPD, Corte Constitucional, Misión Verificación ONU), Tier 2 (Dejusticia, Kai Ambos, Uprimny, García Villegas; El Espectador, La Silla Vacía, Razón Pública; Mark Kersten, Naomi Roht-Arriaza, EJIL:Talk!; CINEP, Hacemos Memoria, Colombia Check), language note (Spanish authoritative)
- `references/foundational-texts.md` — Acuerdo Final (24 Nov 2016, Punto 5), Acto Legislativo 01 de 2017 (4 abril 2017, transitional articles 5-18), **Ley Estatutaria 1957 de 2019** (6 junio 2019; Arts. 1, 5 competencia material, 6 condicionalidad, 8 temporal, 16 no amnistía, 19 estructura, 79 SRVR, 89 Tribunal Especial, 125-145 sanciones, 143 sanciones propias), Ley 1922 de 2018 (RPP), Reglamento General, Sentencias C-674/2017 y C-080/2018 de la Corte Constitucional, Código Penal (Ley 599/2000), instrumentos internacionales (Estatuto de Roma, GC + AP I y II, otros)
- `references/citation-format.md` — convenciones de derecho civil colombiano, 11 macrocasos table (Caso 01-11 con temas), organ designations (Salas de Justicia: SRVR/SDSJ/SAI; Tribunal Especial para la Paz: 4 Secciones), document types (Auto/Providencia/Resolución/Sentencia/Lineamiento/Comunicado), worked examples for Caso 01 and Caso 03 September 2025 sentences, conventions for comparecientes designations (FARC-EP vs FARC vs Comunes; Fuerza Pública; terceros civiles)
- `references/verification-workflow.md` — fallback ladder (jep.gov.co → CEV → Corte Constitucional → UN Mission → Tier 2), **7 JEP-specific traps**: (1) sanciones propias ≠ impunidad, (2) macrocaso ≠ subcaso, (3) FARC ≠ FARC-EP temporal terminology, (4) Sala de Reconocimiento ≠ Sección de Reconocimiento, (5) September 2025 sentences are historic (previously only autos/providencias), (6) Spanish is procedural language, (7) restorative justice applied to non-amnestiable crimes is institutional innovation not amnesty
- `references/jurisprudence-map.md` — 7 sections: institutional architecture, constitutional control (C-674/2017, C-080/2018), 11 macrocasos opening and prioritisation, **first sentences September 2025** (Caso 01 secuestro 16 sept — 7 ex-Secretariado FARC-EP for 21,936 kidnappings — sanciones propias 5-8 years + $35,762M TOAR; Caso 03 Subcaso Costa Caribe 18 sept — 12 ex-Batallón "La Popa" Valledupar for 135 ejecuciones extrajudiciales — sanciones propias 5-8 years + $86,096M TOAR; combined 1,247 pages), prior autos (Autos 19/2021, 033/2021, 128/2021), emerging doctrine (macrocriminalidad, command responsibility, condicionalidad, victim participation), ongoing work (Cases 02-11 status)
- `examples/example-verification.md` — verificación de la sentencia Caso 01 del 16 septiembre 2025, manejando 5 trampas simultáneamente (sanciones propias = vocabulario técnico; FARC-EP; Sección no Sala; sentencia no auto; restauradora no amnistía)
- `examples/example-audit.md` — dos auditorías: sanciones propias mal caracterizadas como "amnistía/impunidad"; Sala vs Sección confusion + FARC vs FARC-EP terminology error

### Skill scope at v1.0.0
- Cubre la JEP desde su origen (Acuerdo Final 2016, Acto Legislativo 01/2017, Estatutaria 1957/2019) hasta las primeras sentencias condenatorias (septiembre 2025) y el trabajo en curso (2026)
- Codifica la misma metodología verification-first que los demás skills del repository
- Específicamente equipado para gestionar las particularidades de la JEP: justicia restaurativa para crímenes no amnistiables, sanciones propias con TOAR, régimen de condicionalidad, lenguaje español autoritativo, terminología temporal (FARC-EP vs FARC vs Comunes), distinción Sala/Sección
- Cartografía las primeras sentencias (Caso 01 secuestro y Caso 03 Subcaso Costa Caribe) y mapea los otros 9 macrocasos en su estado al 2026

### Known limitations
- La JEP es una jurisdicción **activa y en construcción jurisprudencial** — verificar el estado de cada caso en jep.gov.co antes de citar
- Las sentencias de la JEP son voluminosas (1,247 páginas combinadas para las dos primeras); el skill no codifica el contenido sustantivo línea por línea — recuperar el texto integral para citaciones puntuales
- El debate político en torno a la JEP es intenso y polarizado en Colombia; el skill cartografía la naturaleza contestada pero deja la evaluación normativa al usuario
- Las traducciones inglesas de las decisiones de la JEP (raras, por la propia JEP o por terceros como JusticeInfo, EJIL:Talk!, CNN) son traducciones libres no autoritativas — citar la versión española y proporcionar traducción libre identificada como tal
- Los casos 02, 04, 05 (territoriales) y los casos 06-11 (temáticos) están en fases variables; sus sentencias futuras desarrollarán la doctrina y requerirán una v1.1
- La articulación JEP-CEV y JEP-UBPD continúa desarrollándose; el skill indica los puntos de coordinación pero no traza la relación caso por caso
