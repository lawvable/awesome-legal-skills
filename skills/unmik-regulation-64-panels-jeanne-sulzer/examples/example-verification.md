# Example — verifying one Reg. 64 Kosovo citation end-to-end

**Scenario.** A user drafting an article on internationalised criminal proceedings asks the assistant: "Can you confirm that UNMIK Regulation 2000/64 required a majority of international judges on Reg. 64 Panels? Please cite the exact provision."

This example walks through the verification discipline required by this skill.

## Step 0 — Identify the document

The user is asking about the **operative instrument** itself — UNMIK Reg. 2000/64 of 15 December 2000. This is a foundational text (see SKILL.md and `references/foundational-texts.md`), so it **may be cited from project knowledge if present**. Otherwise, retrieve from authoritative archive.

Check: Is Reg. 2000/64 in the project knowledge attached to this conversation? If yes, cite directly. If no, proceed to Step 1.

## Step 1 — Plan citations

The proposition has two distinct legal claims:

1. **Composition requirement** — that a Reg. 64 Panel has a majority of international judges
2. **Source of the rule** — that this is established in UNMIK Reg. 2000/64

Both need verification at the level of the cited provision.

## Step 2 — Verify with the fallback ladder

The fallback ladder for foundational instruments:

1. **Project knowledge** — check first
2. **unmik.unmissions.org** — official UNMIK legacy archive
3. **unmikonline.org** — legacy URL (may redirect)
4. **legal-tools.org** — ICC Legal Tools Database (covers UNMIK regulations)
5. **OSCE Mission in Kosovo legal archive**

Assuming Reg. 2000/64 is not in project knowledge for this conversation:

```
web_fetch: https://unmik.unmissions.org/sites/default/files/old_dnn/Res/ru2000_64.pdf
```

(or the equivalent current URL at unmik.unmissions.org)

Read the regulation. The relevant provision is **Section 2.2**:

> "The College designated by the Department of Judicial Affairs shall be a panel of three (3) judges, including at least two (2) international judges, of whom one shall be the presiding judge."

This confirms the proposition: a Reg. 64 Panel = 3 judges total, of which **minimum 2 international** — i.e., a majority of international judges.

## Step 3 — Draft using verified material

A correctly verified citation might read:

> Under UNMIK Regulation No. 2000/64 of 15 December 2000 (On Assignment of International Judges/Prosecutors and/or Change of Venue), Section 2.2, a Reg. 64 Panel is composed of three professional judges, of whom at least two must be international judges, with the presiding judge to be chosen from among the international judges. The effect is a structural majority of international judges on every Reg. 64 Panel, designed to overcome the impartiality concerns that had limited the effectiveness of the earlier minority-position international judges program under UNMIK Reg. 2000/6 of 15 February 2000.

**Verification level: paragraph verified** (the specific cited paragraph or page contains the cited proposition).

## Step 4 — Self-audit

Trace each element:

- ☑ "UNMIK Regulation No. 2000/64" — official short form, confirmed from retrieved instrument header
- ☑ "15 December 2000" — date confirmed from retrieved instrument
- ☑ "Section 2.2" — section number confirmed by direct reading
- ☑ "three professional judges, of whom at least two must be international judges" — paraphrase faithful to the retrieved text
- ☑ "earlier minority-position international judges program under UNMIK Reg. 2000/6 of 15 February 2000" — historical claim verified separately against `references/jurisprudence-map.md` Phase 1 description and against Hartmann's USIP report

If any element fails the trace, **delete the citation** and either re-verify or use a less specific formulation that is supported.

## Common variations

### Variation 1 — "Reg. 64 covered all serious crimes."

This is **false** as stated. Reg. 64 was a **case-by-case designation mechanism**, not an automatic jurisdictional grant. The petition must be made (by prosecutor, defence, or DJA own motion); the SRSG must approve; the DJA must designate.

Correct formulation:

> Reg. 64 designation was available for "important or sensitive" cases (UNMIK Reg. 2000/64, Section 1.2) but operated on a **case-by-case** basis, requiring petition by prosecutor or defence counsel, or own-motion recommendation by the Department of Judicial Affairs, with approval by the SRSG. It was not an automatic jurisdictional regime.

### Variation 2 — "Reg. 64 Panels operated at the Kosovo Specialist Chambers."

This is **categorically false**. The KSC is a **separate, later, relocated tribunal** at The Hague (established by Law 05/L-053 of 3 August 2015 of the Republic of Kosovo). The Reg. 64 Panels operated within **ordinary Kosovo district courts** (Pristina, Mitrovica, Peja/Peć, Prizren, Gjilan/Gnjilane) under UNMIK administration.

If the user has confused these, **flag the distinction explicitly** and redirect to the appropriate institutional framework. The KSC has its own dedicated skill (`ksc` in this repository) — recommend it explicitly.

### Variation 3 — "The Provisional Criminal Code applied throughout the Reg. 64 Panels' operation."

This is **temporally inaccurate**. The Provisional Criminal Code (UNMIK Reg. 2003/25 of 6 July 2003) **entered into force on 6 April 2004**. Reg. 64 Panel cases initiated before that date applied the **Yugoslav Federal Criminal Code 1976** as continued in force by UNMIK Reg. 1999/1 and 1999/24.

Correct formulation:

> Reg. 64 Panel cases applied the substantive criminal law in force at the time of the alleged conduct. For conduct predating 6 April 2004, this was typically the Yugoslav Federal Criminal Code 1976 (as continued in force by UNMIK Regulations 1999/1 and 1999/24, applying the law in force as of 22 March 1989). From 6 April 2004, the Provisional Criminal Code of Kosovo (UNMIK Reg. 2003/25) applied, subject to non-retroactivity protections.

## What this example demonstrates

- Foundational texts may bypass `web_fetch` if in project knowledge — but this exception is narrow
- Section-level citations require section-level verification
- Adjacent historical claims (Phase 1 vs Phase 2, etc.) must each be verified, even if they seem like "context"
- The KSC distinction is a high-frequency confusion trap — flag it proactively
- Temporal applicability of substantive law is a Reg. 64-specific issue
