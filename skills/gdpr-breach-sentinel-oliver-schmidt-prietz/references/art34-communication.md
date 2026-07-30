# Art. 34 Decision Framework — Communication to Data Subjects

Art. 34 is its own legal decision, not a footnote to Art. 33. Run this framework whenever the facts or the ENISA score suggest possible high risk, and record the outcome in an **Art. 34 Decision Memo** (see [templates.md](templates.md)).

---

## 1. Trigger — Art. 34(1)

Communicate the breach to data subjects when it is **"likely to result in a high risk to the rights and freedoms of natural persons"**.

- "High risk" is a higher threshold than the Art. 33(1) "risk" trigger — every Art. 34 case is also an Art. 33 case, never the reverse.
- Factors raising risk to "high": special-category or financial data, identity-theft or fraud potential, vulnerable subjects, scale, malicious actor with intent to misuse, irreversibility of consequences, possibility of physical or psychological harm.
- This is a normative legal test: bridge the ENISA score to the conclusion in writing (Legal Bridge in SKILL.md). SE ≥ 3 creates a presumption of high risk — it does not decide it.

## 2. Timing — "Without Undue Delay"

- No fixed 72h deadline, but urgency scales with the protective value of the communication: where subjects can act (change passwords, block cards, watch for phishing), every hour of delay transfers risk to them.
- Coordination with law enforcement may justify a short delay; document the request.
- The SA can be notified first and subject communication follow — but do not hold subject communication hostage to a complete investigation; phased communication is acceptable.

## 3. Exceptions — Art. 34(3) (assess ALL three, in order)

### (a) Appropriate protection measures applied — *before* the breach

Technical and organisational measures were in place **and applied to the affected data**, in particular measures rendering the data unintelligible to unauthorised persons (e.g., state-of-the-art encryption).

- Run the encryption logic tree in [enisa-methodology.md](enisa-methodology.md) §5 — do not duplicate it here. Key compromised or stored with the data → exception NOT available.
- The EDPB template asks for this directly ("was the data unintelligible…"); answer (a)-intact, (b)-likely-subvertible, or (c)-no — claim the exception only for (a).

### (b) Subsequent measures — *after* the breach

The controller has taken subsequent measures which **ensure that the high risk is no longer likely to materialise**.

- Examples: forced credential reset + session invalidation before any misuse; remote wipe confirmed; recipient of a misdirected message verifiably and credibly deleted the data before reading/use; stolen device recovered intact with forensic confirmation of no access.
- The bar is "no longer likely to materialise" — not "reduced". Document the measure, the evidence it worked, and why residual risk is no longer high.
- If the measure's effectiveness is unconfirmed (e.g., remote wipe not acknowledged by the device), the exception is **not yet** available — keep the decision open and re-assess.

### (c) Disproportionate effort → public communication instead

Where individual communication would involve **disproportionate effort** (e.g., contact details lost in the breach itself, very large populations with no usable channel), the controller must instead make a **public communication or similar measure** informing subjects in an **equally effective manner**.

- This exception changes the *form*, not the duty: silence is not an option under (c).
- Equally effective means: prominent website notice, press release, social channels the subjects actually use, in the relevant languages — combined where needed.
- Cost alone rarely makes effort "disproportionate" when channels exist; document the comparison.

## 4. Content — Art. 34(2) (referencing Art. 33(3)(b)–(d))

In clear and plain language, at minimum:

1. **Nature of the breach** — what happened, in words a non-lawyer understands.
2. **Name and contact details of the DPO** or other contact point.
3. **Likely consequences** — honest, specific to the data involved (e.g., "phishing emails that appear to come from us", "fraudulent payment attempts").
4. **Measures taken or proposed** — containment, mitigation, prevention.
5. **Concrete self-protection steps** — actionable, prioritised: password changes (and everywhere reused), card blocking, fraud alerts, scepticism toward unexpected contact referencing the breach.

Avoid: minimising language ("out of an abundance of caution"), burying the action steps, legalese, blaming the subject.

## 5. Communication Strategy

| Dimension | Guidance |
|-----------|----------|
| **Channel** | Direct (letter/email/in-app) is the default; public only under (c) or as a supplement. Do not use the breached channel alone if it may be attacker-controlled |
| **Phasing** | Notify confirmed-affected subjects first; widen as the investigation scopes. Document the phasing rationale |
| **Vulnerable subjects** | Minors (via holders of parental responsibility where appropriate), patients, elderly — prioritise and adapt language |
| **Languages** | Communicate in the languages of the affected Member States / the languages used to provide the service |
| **Support channel** | For scale or sensitive data: dedicated contact line / mailbox / FAQ; brief the staff answering it |
| **Fraud/phishing warning** | Warn that criminals may exploit the breach itself ("we will never call you to ask for your password"); give the only legitimate contact route |
| **Record** | Keep the dated content actually sent — the EDPB template (§5) and the attachment inventory both require it |

## 6. Backstop — Art. 34(4)

If the controller has not communicated, the SA may — after considering the likelihood of high risk — **require** communication or decide that an exception applies. Factor this in: a weak exception claim invites an SA order plus scrutiny of the delay.

## 7. Decision Memo

Record in the Art. 34 Decision Memo ([templates.md](templates.md)): the high-risk analysis (Legal Bridge), each Art. 34(3) exception considered with reasons, the timing decision, the strategy choices above, and approval (DPO/counsel). This memo populates §5 of the EDPB evidence file 1:1.
