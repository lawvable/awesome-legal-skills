# Key NDA Clauses (What to Look For)

This reference supports clause-by-clause review for commercial NDAs in a jurisdiction-agnostic way. Focus on business risk allocation and operational feasibility.

## Contents
- Definition of “Confidential Information”
- Purpose / Permitted Use
- Non-disclosure / standard of care
- Term and survival
- Exclusions from confidentiality
- Compelled disclosure
- Return / destruction
- Residuals

## 1) Definition of “Confidential Information”

### What to check
- Scope: is it limited to information disclosed **in connection with the stated purpose**?
- Identification: does it require marking (“CONFIDENTIAL”) or does it cover unmarked disclosures?
- Formats: written, oral, visual, electronic, demo access, source code, samples.
- Derived information: does it include analyses, notes, compilations created by Recipient?

### Recipient red flags
- “All information of any kind, whether marked or not, is confidential” with no reasonableness.
- Confidentiality applies even if information is independently developed or already known.
- “Residuals” / “retained in memory” undermines confidentiality.

### Discloser red flags
- Definition requires strict marking only, with no mechanism for oral disclosures.

### Suggested redline language (modular)
**Reasonableness + connection to purpose**
```
“Confidential Information” means non-public information disclosed by or on behalf of Discloser to Recipient in connection with the Purpose that is identified as confidential at the time of disclosure or that a reasonable person would understand to be confidential given the nature of the information and the circumstances of disclosure.
```

**Oral disclosure confirmation (discloser-friendly but balanced)**
```
Oral or visual disclosures will be treated as Confidential Information if Discloser confirms their confidential nature in writing within [30] days after disclosure.
```

## 2) Purpose / Permitted Use

### What to check
- Purpose is specific enough (not “any business purpose”).
- Use restriction matches the transaction (evaluation vs implementation).

### Recipient red flags
- Use restriction prevents internal evaluation (e.g., bans sharing with employees who need to assess).
- Prohibits contact with customers, suppliers, or employees (non-solicit / no-contact) hidden inside NDA.

### Suggested redline language
```
Recipient may use Confidential Information solely for the Purpose and may disclose it to its Representatives who have a need to know for the Purpose and who are bound by confidentiality obligations at least as protective as this Agreement.
```

> **Employment / contractor variation:** NDAs sometimes add IP assignment, invention disclosure, non-compete, and non-solicit. Treat those as separate topics and escalate.

## 3) Non-disclosure / standard of care

### What to check
- Standard of care: “reasonable care”, “same degree as its own”, or absolute.
- Security obligations: required controls or policies.

### Recipient red flags
- Absolute obligations (“shall ensure no unauthorized disclosure”) → strict liability.
- Mandatory named security frameworks without feasibility.

### Suggested redline language
```
Recipient will protect Confidential Information using at least the same degree of care it uses to protect its own confidential information of similar sensitivity, and in any event no less than reasonable care.
```

## 4) Term and survival

### What to check
- Term of NDA (how long relationship lasts)
- Survival (how long confidentiality obligations last)
- Start date triggers (effective date vs first disclosure)

### Recipient red flags
- Perpetual confidentiality for all information.

### Balanced approach
- Fixed period for ordinary confidential information.
- Longer (potentially indefinite) protection for trade secrets, if defined.

**Suggested language**
```
Confidentiality obligations will apply during the Term and for [2–5] years thereafter; however, obligations for Trade Secrets (if any) will continue for so long as such information remains a trade secret under applicable law.
```

## 5) Exclusions from confidentiality

(See also: STANDARD_EXCEPTIONS.md)

### What to check
- Standard carve-outs exist and are workable.
- Who bears burden of proof.

### Recipient red flags
- No carve-outs.
- Carve-outs exist but require impossible proof.

## 6) Compelled disclosure

### What to check
- Ability to disclose if required by law/regulator.
- Notice requirement and timing.

### Recipient red flags
- Notice “immediately” or within 24 hours, even if prohibited.
- No permission to disclose the minimum required.

**Suggested language**
```
If Recipient is required by law, regulation, or court order to disclose Confidential Information, Recipient may do so provided that (to the extent legally permitted) it gives Discloser prompt notice and reasonably cooperates with Discloser’s efforts to seek protective treatment.
```

## 7) Return / destruction

### What to check
- Practicality: backups, archives, legal holds.

### Recipient red flags
- Requires wiping all backups immediately and certifying deletion of everything.

**Suggested language**
```
Upon written request, Recipient will return or destroy Confidential Information, except that Recipient may retain copies (i) as required to comply with law, regulation, or internal compliance requirements, and (ii) in routine backup systems that are not reasonably accessible in the ordinary course, provided such retained information remains subject to confidentiality.
```

## 8) Residuals

### Why it matters
Residuals clauses can allow Recipient to use generalized knowledge “retained in memory,” which can swallow the confidentiality obligation.

### Recipient position
- Prefer deletion.
- If unavoidable: narrow scope heavily (exclude source code, product roadmaps, customer lists, pricing).

**Suggested narrowing language**
```
Residuals do not include source code, customer-identifiable information, pricing, product roadmaps, or any information that is intentionally memorized for the purpose of circumventing this Agreement.
```
