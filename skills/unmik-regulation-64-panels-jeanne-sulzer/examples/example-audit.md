# Example — auditing a user-supplied document on Reg. 64 Kosovo

**Scenario.** A user submits a draft chapter on internationalised criminal justice that contains the following passage and asks the assistant to "fact-check the legal references":

> "The Kosovo Specialist Chambers were established by UNMIK Regulation 2000/64 in December 2000 and operated within the ordinary Kosovo district courts until 2008. Their composition was 2 international judges and 1 Kosovo Albanian judge, and they applied the Kosovo Criminal Code of 2003. The KWECC was a parallel chamber for war crimes. After Kosovo's independence in 2008, EULEX took over and the panels were moved to The Hague."

This passage contains **multiple serious errors**. This example walks through the audit discipline.

## Error 1 — Institutional misidentification (CRITICAL)

> "The **Kosovo Specialist Chambers** were established by UNMIK Regulation 2000/64..."

**False.** The Kosovo Specialist Chambers (KSC) are a **separate, later, relocated tribunal** at The Hague, established by **Law No. 05/L-053 of 3 August 2015 of the Republic of Kosovo** and related instruments. They have **no institutional continuity** with the Reg. 64 Panels.

What UNMIK Reg. 2000/64 established is the **Regulation 64 Panels** (Reg. 64 Panels) — a mechanism for designating panels with majority international judges within ordinary Kosovo district courts.

**Audit correction:**

> "The **Regulation 64 Panels** (Reg. 64 Panels) were established by UNMIK Regulation 2000/64 of 15 December 2000..."

**Flag for user:** the KSC and the Reg. 64 Panels are commonly conflated. The KSC has its own dedicated treatment in the literature and in this repository. If the chapter intended to discuss the KSC, the entire passage requires reconstruction with KSC-specific information.

## Error 2 — Operative date partially correct

> "...in December 2000 and operated within the ordinary Kosovo district courts until 2008."

**Partially correct.** UNMIK Reg. 2000/64 was indeed adopted in December 2000 (specifically, **15 December 2000**). The operational period of "until 2008" requires nuance:

- UNMIK Reg. 2000/64 itself remained in force until superseded; case-by-case Reg. 64 designations continued through the UNMIK administration period
- Kosovo declared independence on **17 February 2008**
- EULEX achieved full operational capability on **9 December 2008**
- The transition was not instantaneous; some Reg. 64 cases were ongoing when EULEX took over and were continued under the new framework

**Audit correction:**

> "...established by UNMIK Regulation 2000/64 of 15 December 2000 and operated within the ordinary Kosovo district courts (Pristina, Mitrovica, Peja/Peć, Prizren, Gjilan/Gnjilane) throughout the UNMIK administration period, with the transition to the EULEX framework beginning after Kosovo's declaration of independence on 17 February 2008 and EULEX achieving full operational capability on 9 December 2008."

## Error 3 — Composition (significant)

> "Their composition was **2 international judges and 1 Kosovo Albanian judge**..."

**Partially correct, but misleadingly framed.** Under UNMIK Reg. 2000/64, Section 2.2, the panel consists of **three professional judges**, of whom **at least two must be international judges** (with one designated as presiding). Identifying the non-international judge as "Kosovo Albanian" is **factually inaccurate as a categorical description**: the third judge was a professional judge from the Kosovo court system, who **could be** Kosovo Albanian but could also be from other ethnic communities depending on the case and availability.

**Audit correction:**

> "Panel composition under UNMIK Reg. 2000/64, Section 2.2: three professional judges, of whom at least two must be international judges (with one of the international judges presiding). The third judge is a professional judge from the Kosovo court system."

## Error 4 — Substantive law (temporally wrong)

> "...and they applied **the Kosovo Criminal Code of 2003**."

**Two errors.** First, there is no "Kosovo Criminal Code of 2003" as a discrete codified instrument; the user likely means the **Provisional Criminal Code of Kosovo**, which was promulgated by **UNMIK Regulation 2003/25 of 6 July 2003** and **entered into force on 6 April 2004**. Second, this code was not applied throughout the operational period: cases initiated before 6 April 2004 applied the **Yugoslav Federal Criminal Code 1976** (as continued in force by UNMIK Reg. 1999/1 and 1999/24, applying law in force as of 22 March 1989).

**Audit correction:**

> "Reg. 64 Panels applied the substantive criminal law in force at the time of the alleged conduct. For conduct before 6 April 2004, this was generally the Yugoslav Federal Criminal Code 1976 (as continued by UNMIK Regulations 1999/1 and 1999/24). From 6 April 2004, the Provisional Criminal Code of Kosovo (UNMIK Reg. 2003/25 of 6 July 2003) applied, subject to non-retroactivity protections."

## Error 5 — KWECC factual error (CRITICAL)

> "The **KWECC was a parallel chamber for war crimes**."

**False.** The Kosovo War and Ethnic Crimes Court (KWECC) was **proposed** as a separate court but was **abandoned in autumn 2000** in favour of the Reg. 64 mechanism. The KWECC **never operated**. The institutional choice to abandon KWECC and instead use Reg. 64 designations within ordinary district courts is a **substantive doctrinal point** in the literature on the design of internationalised criminal justice: integration rather than separation.

**Audit correction:**

> "The Kosovo War and Ethnic Crimes Court (KWECC) was a proposed separate court for war crimes that was **abandoned in autumn 2000** before becoming operational. The Reg. 64 Panel mechanism was adopted as the alternative, embedding internationalised adjudication within existing district courts rather than creating a separate tribunal."

## Error 6 — EULEX transition geographic error (CRITICAL)

> "After Kosovo's independence in 2008, EULEX took over and **the panels were moved to The Hague**."

**False.** EULEX is the **European Union Rule of Law Mission in Kosovo** (Joint Action 2008/124/CFSP of 4 February 2008). EULEX judges and prosecutors operate **in Kosovo**, not at The Hague. The successor framework is Law No. 2008/03-L053 of 13 March 2008 (Republic of Kosovo) on the Jurisdiction, Case Selection and Case Allocation of EULEX Judges and Prosecutors in Kosovo.

The user appears to have **confused this with the Kosovo Specialist Chambers**, which (as a separate later institution) **is** relocated to The Hague — but that is a different tribunal (see Error 1).

**Audit correction:**

> "After Kosovo's declaration of independence on 17 February 2008, EULEX (the European Union Rule of Law Mission in Kosovo) took over international judicial functions, operating **within Kosovo** under Law No. 2008/03-L053 of 13 March 2008. The Reg. 64 mechanism was succeeded by this new framework. (The later Kosovo Specialist Chambers, established in 2015 and located at The Hague, are a separate institution and should not be conflated with either the Reg. 64 Panels or EULEX.)"

## Audit summary report to user

When reporting back to the user, the assistant might write:

> The passage contains six categorical errors that require correction:
>
> 1. **Institutional misidentification** — the passage refers to the Kosovo Specialist Chambers, but UNMIK Reg. 2000/64 established the **Regulation 64 Panels**. The KSC is a separate, later, relocated tribunal at The Hague (2015–).
> 2. **Operative date** — UNMIK Reg. 2000/64 was adopted on **15 December 2000**, not generically "in December 2000". Operational period ran throughout UNMIK administration until the EULEX transition completed on **9 December 2008**.
> 3. **Composition** — the panel is three judges, of whom **at least two are international**, with one international judge presiding. The third is a professional judge of the Kosovo system, not categorically a "Kosovo Albanian judge".
> 4. **Substantive law** — pre-2004 cases applied the **Yugoslav Federal Criminal Code 1976**; from **6 April 2004**, the **Provisional Criminal Code of Kosovo** (UNMIK Reg. 2003/25 of 6 July 2003) applied.
> 5. **KWECC** — the Kosovo War and Ethnic Crimes Court was **abandoned in autumn 2000** and never operated; the Reg. 64 mechanism was adopted as the alternative.
> 6. **EULEX location** — EULEX operates **in Kosovo**, not at The Hague. The Hague location applies to the **Kosovo Specialist Chambers**, a separate institution.
>
> The most consequential confusion in the passage is between the **Reg. 64 Panels** (UNMIK-era panels within ordinary Kosovo district courts) and the **Kosovo Specialist Chambers** (a separate, later, relocated tribunal at The Hague). These are institutionally, temporally, and geographically distinct.
>
> I have drafted corrected formulations for each error above. Recommend the user clarify which institution they intended to discuss before redrafting.

## What this example demonstrates

- Reg. 64 / KSC confusion is the highest-frequency error in user-supplied texts; flag explicitly
- KWECC misattribution (treating it as operative rather than abandoned) is a common doctrinal error
- Geographic errors about EULEX location reveal underlying institutional confusion
- Temporal sequencing of substantive law (Yugoslav Federal Code → Provisional Criminal Code) requires explicit handling
- Panel composition descriptions must follow Section 2.2 of Reg. 2000/64 precisely
- When multiple errors compound, the most efficient response is a structured audit report listing each error with corrected formulations
