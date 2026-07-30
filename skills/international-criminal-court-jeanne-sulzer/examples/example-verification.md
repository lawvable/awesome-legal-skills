# Example: verifying citations end-to-end

Two cases. The first is full level-C verification (the ideal). The second is partial verification when icc-cpi.int blocks the full fetch — the more common real-world pattern.

---

## Case 1 — full verification (level C)

**Task:** "What did the Bemba Trial Chamber say about the standard for 'effective control' under Article 28(a)? Give me a paragraph I can use in a memo."

### Identify

- Case: *Prosecutor v. Bemba* (CAR situation)
- Document: Trial Chamber III judgment under Article 74
- Topic: effective control under Article 28(a) (military command responsibility)
- Expected document number: `ICC-01/05-01/08-3343`
- Expected date: 21 March 2016

The Bemba Trial Chamber conviction was set aside by the Appeals Chamber on 8 June 2018 (`ICC-01/05-01/08-3636-Red`). Any memo on Bemba effective control needs to address this — both decisions go on the verification list.

### Verify

```
web_fetch("https://www.icc-cpi.int/court-record/icc-01/05-01/08-3343")
→ full document retrieved. Read the Article 28(a) / effective control section. Note the paragraph(s) articulating the standard.

web_fetch("https://www.icc-cpi.int/court-record/icc-01/05-01/08-3636-Red")
→ full document retrieved. Read the Appeals Chamber reasoning on command responsibility.
```

Both at level C.

### Draft

> Under Article 28(a) of the Rome Statute, a military commander incurs criminal responsibility for crimes committed by forces under his "effective command and control". The Trial Chamber in *Bemba* held that effective control turns on the material ability to prevent or repress the commission of crimes; de jure authority is one factor but not determinative — the inquiry is one of fact, to be assessed in light of all the circumstances [Bemba TJ, paras. [X]–[Y]]. **This judgment was set aside on appeal.** The Appeals Chamber found, by majority, that the Trial Chamber erred on two grounds — convicting Bemba for criminal acts outside the scope of the confirmed charges, and in its assessment of the measures he took to prevent and repress crimes by the MLC contingent in the CAR — and acquitted the accused [Bemba AJ, paras. [X]–[Y]].

Full citations (first occurrence):
- *Prosecutor v. Bemba*, Trial Chamber III, "Judgment pursuant to Article 74 of the Statute", ICC-01/05-01/08-3343, 21 March 2016.
- *Prosecutor v. Bemba*, Appeals Chamber, "Judgment on the appeal of Mr Jean-Pierre Bemba Gombo against Trial Chamber III's 'Judgment pursuant to Article 74 of the Statute'", ICC-01/05-01/08-3636-Red, 8 June 2018.

Paragraph numbers filled from the fetched text, not guessed.

---

## Case 2 — partial verification (level B; level C not achievable in this conversation)

**Task:** "Summarise the Ntaganda Appeals Chamber's holding on the nexus requirement for war crimes of sexual violence within an armed group."

### Identify and disambiguate

Two Ntaganda Appeals Chamber moments touch this issue:
- **15 June 2017** — interlocutory appeal on jurisdiction over Counts 6 and 9 (rape and sexual slavery of child soldiers within the UPC/FPLC). This is the controlling holding on whether members of the same armed group are excluded from the protection of these war crimes.
- **30 March 2021** — final conviction appeal, confirming the Trial Chamber's 8 July 2019 judgment on all 18 counts. The 2021 judgment did not re-open the 2017 jurisdictional holding.

The user almost certainly wants the 2017 decision. Surface this to the user if there is any doubt, rather than picking silently.

### Verify

```
web_fetch("https://www.icc-cpi.int/court-record/icc-01/04-02/06-1962")
→ 403
web_fetch("https://www.icc-cpi.int/drc/ntaganda")
→ 403
web_search("Ntaganda Appeals Chamber 15 June 2017 jurisdiction counts 6 and 9")
→ ICC press release of 15 June 2017 (icc-cpi.int domain) confirms document number, title, chamber, date, and holding-in-substance
→ OUP ORIL entry confirms case citation and section structure (paras 46–70 contain the determinative reasoning)
```

**Levels achieved:**
- Level A (document, title, number, date, chamber): confirmed via the icc-cpi.int press release
- Level B (holding in substance): confirmed via the press release and ORIL
- Level C (paragraph-specific): not reached — full text not retrieved in this conversation

### Output structure

> The Ntaganda Appeals Chamber held in 2017 that the war crimes of rape and sexual slavery under Articles 8(2)(b)(xxii) and 8(2)(e)(vi) of the Statute are not subject to a "status requirement" that would exclude members of the same armed group as the perpetrator. The Defence had argued that war crimes under common Article 3 of the Geneva Conventions cannot be committed by members of an armed force against members of the same armed force, and that finding otherwise would amount to an unjustified extension of the scope of war crimes law. The Appeals Chamber rejected this position. It reasoned that neither the text of Articles 8(2)(b)(xxii) or 8(2)(e)(vi), nor the chapeaux of Articles 8(2)(b) or 8(2)(e), nor the "established framework of international law" referenced in those provisions, imposes such a limitation; the nexus requirement (Element 3: conduct "in the context of and associated with" an armed conflict) was therefore capable of being satisfied for intra-group conduct.
>
> *Prosecutor v. Ntaganda*, Appeals Chamber, "Judgment on the appeal of Mr Ntaganda against the 'Second decision on the Defence's challenge to the jurisdiction of the Court in respect of Counts 6 and 9'", ICC-01/04-02/06-1962 OA5, 15 June 2017.
>
> **Verification status:** Document, title, number, date, chamber, and the holding in substance were verified via the ICC's press release of 15 June 2017 and the OUP ORIL summary. The full text of the judgment was not retrieved in this conversation (icc-cpi.int returned 403; the document is also available on legal-tools.org and from the Court itself). Specific paragraph numbers within the judgment's reasoning are therefore not paragraph-pinned here. Before citation in a brief or filing, confirm the precise paragraphs (the determinative reasoning is in the section beginning around paras. 46–70 per the ORIL section structure).

### Why this structure

The output gives the practitioner what they actually need: an accurate summary of the holding, the correct citation in the Court's form, and an explicit note about what was verified at what level. This is more useful than refusing to draft anything without level C, and far more useful than inventing paragraph numbers to make the citation look complete. The user can take this directly into research notes or an explanatory memo; for a brief or filing, the verification note tells them exactly what additional check is needed.
