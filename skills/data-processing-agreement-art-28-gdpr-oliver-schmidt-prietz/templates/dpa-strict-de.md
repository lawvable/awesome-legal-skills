# DPA-Vorlage — Tier 2 (Strict): 2021/915 durch Verweis inkorporiert — Deutsch

## Was diese Vorlage ist

Ein Wrapper, der **die unveränderten Standardvertragsklauseln nach Durchführungsbeschluss (EU) 2021/915 der Kommission** als datenschutzrechtliche Substanz der Vereinbarung inkorporiert und ein minimales kommerzielles Overlay (Abschnitt 4) für Aspekte ergänzt, die der Kommissionstext nicht regelt (anwendbares Recht, Mitteilungen, Unterzeichnung, optionale Haftungsbegrenzung).

Die Compliance-Vermutung nach Art. 28 Abs. 7 DSGVO knüpft an den unveränderten Kommissionstext an. Diese Wrapper-Struktur erhält die Vermutung.

## Wann diese Vorlage zu nutzen ist

Tier 2 (Strict) für **maximale aufsichtsbehördliche Verteidigungsfähigkeit**:
- Engagement im öffentlichen Sektor (Verantwortlicher ist eine Behörde)
- Stark regulierter Sektor (Finanzdienstleistungen, Gesundheit, kritische Infrastruktur)
- Post-Incident-Aufarbeitung, bei der der Nachweis eines Safe-Harbor-Instruments Teil der Korrekturmaßnahmen ist
- Gegenpartei verlangt ausdrücklich 2021/915
- Jede Situation, in der die Compliance-Vermutung wichtiger ist als die kommerzielle Flexibilität, die dabei verloren geht

Für gewöhnliche kommerzielle AVV-Arbeit verwende **Tier 1** (`dpa-commercial-de.md`) oder **Tier 3 — Hybrid** (`dpa-hybrid-de.md`).

## Anwendung der Vorlage

1. Lade `references/2021-915-commission-text-de.md` für die Praktiker-Anleitung und die ABl.-Links.
2. Bestätige, dass der amtliche ABl.-DE-Text die verbindliche Fassung ist. Der Text steht unter: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021D0915
3. Arbeite den Abschnitt **Wahlmöglichkeiten** unten ab und fixiere die Optionen/Werte.
4. Befülle die Anhänge I–IV aus dem Intake.
5. Befülle Abschnitt 4 (kommerzielles Overlay).
6. Unterzeichne und vollziehe.

Der Kommissionstext wird in diesem Wrapper **nicht reproduziert**. Er wird nach Abschnitt 1.2 unten durch Verweis inkorporiert. Dies ist eine bewusste architektonische Entscheidung — siehe Referenzdatei für die Begründung.

---

# AUFTRAGSVERARBEITUNGSVERTRAG

Dieser **Auftragsverarbeitungsvertrag** (der "**AVV**") wird am `{{INKRAFTTRETEN}}` geschlossen zwischen:

**`{{VERANTWORTLICHER_NAME}}`**, einer/einem `{{RECHTSFORM}}` mit Sitz in `{{ADRESSE}}`, eingetragen im Handelsregister `{{HANDELSREGISTER}}` unter HRB `{{HRB_NR}}` (der "**Verantwortliche**")

— und —

**`{{AUFTRAGSVERARBEITER_NAME}}`**, einer/einem `{{RECHTSFORM}}` mit Sitz in `{{ADRESSE}}`, eingetragen im Handelsregister `{{HANDELSREGISTER}}` unter HRB `{{HRB_NR}}` (der "**Auftragsverarbeiter**", zusammen mit dem Verantwortlichen die "**Parteien**" und einzeln eine "**Partei**").

## Präambel

A. Die Parteien haben am `{{HAUPTVERTRAG_DATUM}}` `{{HAUPTVERTRAG_TITEL}}` (der "**Hauptvertrag**") geschlossen, im Rahmen dessen der Auftragsverarbeiter dem Verantwortlichen bestimmte Leistungen erbringt (die "**Leistungen**").

B. Im Rahmen der Erbringung der Leistungen verarbeitet der Auftragsverarbeiter personenbezogene Daten im Auftrag des Verantwortlichen im Sinne des Art. 4 Nr. 8 DSGVO.

C. Die Parteien sind übereingekommen, ihr datenschutzrechtliches Verhältnis durch die Standardvertragsklauseln zwischen Verantwortlichen und Auftragsverarbeitern im Anhang zum **Durchführungsbeschluss (EU) 2021/915 der Kommission** vom 4. Juni 2021 (ABl. L 199 vom 7.6.2021, S. 18) (der "**SCC-Beschluss**" und die "**SCCs**") zu regeln.

D. Dieser AVV inkorporiert die SCCs durch Verweis und ergänzt einen Abschnitt 4 als kommerzielles Overlay für Aspekte, die die SCCs nicht regeln.

## ABSCHNITT 1 — INKORPORATION DER SCCs

### 1.1 Inkorporation durch Verweis

Die Parteien nehmen die SCCs gemäß dem Anhang zum SCC-Beschluss vollständig und unverändert an. Die SCCs (Abschnitte I, II, III sowie Anhänge I, II, III, IV) sind Bestandteil dieses AVV. Im Fall von Widersprüchen zwischen diesem Abschnitt 1 und den SCCs gehen die SCCs nach Klausel 4 der SCCs vor.

### 1.2 Verbindlicher Text

Die Parteien erkennen an, dass der verbindliche Text der SCCs der im Amtsblatt der Europäischen Union veröffentlichte Text ist (ABl. L 199 vom 7.6.2021, S. 18), abrufbar unter https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021D0915. Alle EU-Sprachfassungen sind gleichermaßen authentisch. Im Zweifel über den verbindlichen Text gilt der ABl.-Text.

### 1.3 Geltungsumfang

Die SCCs werden ausschließlich nach Verordnung (EU) 2016/679 (Datenschutz-Grundverordnung) abgeschlossen. Der optionale Verweis auf Verordnung (EU) 2018/1725 in Klausel 1 der SCCs wird nicht übernommen.

### 1.4 Wahlmöglichkeiten der Parteien

Die Parteien treffen folgende Wahlmöglichkeiten zu den SCCs:

| Wahl | Auswahl |
|---|---|
| Optionale Beitrittsklausel (Klausel 5) | `{{AKTIVIERT / NICHT AKTIVIERT — Standard: AKTIVIERT}}` |
| Genehmigungsregime für Unterauftragsverarbeiter (Klausel 7.7) | `{{OPTION 1 (spezifisch) / OPTION 2 (allgemein) — Standard: OPTION 2}}` |
| Vorlauffrist für Genehmigungsantrag / Änderungsmitteilung | `{{30 Tage — Standard}}` |

## ABSCHNITT 2 — AUSGEFÜLLTE ANHÄNGE ZU DEN SCCs

Die Anhänge zu den SCCs sind in **Anlage 1** (Anhang I), **Anlage 2** (Anhang II), **Anlage 3** (Anhang III) und **Anlage 4** (Anhang IV) zu diesem AVV ausgefüllt.

## ABSCHNITT 3 — DRITTLANDÜBERMITTLUNGEN (soweit anwendbar)

### 3.1 Anerkenntnis

Die Parteien erkennen an, dass die SCCs nach Klausel 1 lit. f keine Übermittlungen personenbezogener Daten außerhalb des EWR nach Kapitel V DSGVO abdecken.

### 3.2 Übermittlungsmechanismus

`{{Sind Übermittlungen im Spiel, befülle Anlage 5 (Drittlandübermittlungen) und nenne den Mechanismus: Angemessenheitsbeschluss / Durchführungsbeschluss (EU) 2021/914-SCCs / BCRs / Ausnahmetatbestand nach Art. 49 DSGVO. Sind keine Übermittlungen im Spiel, markiere Anlage 5 mit "Nicht anwendbar" und entferne ggf. verwaiste Querverweise in Abschnitt 3.}}`

## ABSCHNITT 4 — KOMMERZIELLES OVERLAY 💼

> 💼 *Dieser Abschnitt 4 ist nach Klausel 2 lit. b der SCCs zulässig. Er regelt kommerzielle Fragen, die die SCCs nicht regeln. Er ist so formuliert, dass er den SCCs nicht widerspricht. Änderungen dieses Abschnitts 4 durch die Parteien beeinträchtigen die Compliance-Vermutung der SCCs nicht.*

### 4.1 Laufzeit

Dieser AVV tritt zum Inkrafttreten in Kraft und gilt für die Dauer der Erbringung der Leistungen. Er endet automatisch mit Beendigung des Hauptvertrags, vorbehaltlich der Bestimmungen, die ihrer Natur nach fortgelten.

### 4.2 Kündigung aus wichtigem Grund

Jede Partei kann diesen AVV mit einer Frist von dreißig (30) Tagen schriftlich bei wesentlicher Verletzung dieses AVV oder der SCCs durch die andere Partei kündigen, die nicht innerhalb der Kündigungsfrist behoben wurde. Eine Kündigung dieses AVV aus diesem Grund berechtigt die kündigende Partei zur Kündigung des entsprechenden Teils des Hauptvertrags ohne Vertragsstrafe.

### 4.3 Haftungsverteilung

`[ALT 1: verantwortlichen-freundlich]` Unbeschadet der Haftung aus Verletzungen der SCCs ist die Gesamthaftung des Auftragsverarbeiters für Schäden aus oder im Zusammenhang mit diesem AVV, einschließlich Verletzungen anwendbaren Datenschutzrechts und Verletzungen des Schutzes personenbezogener Daten, auf den zweifachen (2-fachen) Betrag der vom Verantwortlichen unter dem Hauptvertrag in den dem haftungsbegründenden Ereignis vorangegangenen zwölf (12) Monaten gezahlten oder zu zahlenden Entgelte begrenzt. Diese Begrenzung gilt zusätzlich (nicht anstelle) zur allgemeinen Haftungsbegrenzung des Hauptvertrags und nicht für die Haftung wegen (a) grober Fahrlässigkeit oder Vorsatz, (b) Verletzung der Vertraulichkeit oder (c) sonstiger nach anwendbarem Recht nicht beschränkbarer Haftungstatbestände.

`[ALT 2: auftragsverarbeiter-freundlich]` Die Haftung der Parteien unter diesem AVV unterliegt den Haftungsbegrenzungs- und -ausschlussklauseln des Hauptvertrags.

### 4.4 Kostenverteilung für Unterstützungsleistungen

`{{Routineunterstützung nach Klauseln 8 und 9 der SCCs ist im Leistungsentgelt enthalten. Außergewöhnlicher Aufwand (z. B. Anfragenvolumen, das das übliche Maß deutlich überschreitet, oder spezialisierte Datenextraktionen) kann nach vorheriger Vereinbarung mit dem Verantwortlichen zu den angemessenen Sätzen des Auftragsverarbeiters in Rechnung gestellt werden.}}`

### 4.5 Mitteilungen

Mitteilungen unter diesem AVV haben schriftlich an die im Kopf dieses AVV genannten Adressen zu erfolgen oder an eine andere Adresse, die eine Partei der anderen schriftlich mitteilt. Mitteilungen werden mit Zugang wirksam.

### 4.6 Änderungen

Änderungen dieses AVV bedürfen der Schriftform und der Unterzeichnung durch beide Parteien. Änderungen der inkorporierten SCCs sind unzulässig; nur die Anhänge dürfen nach Klausel 2 lit. a der SCCs aktualisiert werden.

### 4.7 Salvatorische Klausel

Sollte eine Bestimmung dieses Abschnitts 4 unwirksam oder nicht durchsetzbar sein, bleiben die übrigen Bestimmungen davon unberührt. Die Salvabilität einzelner Klauseln der SCCs richtet sich nach den SCCs selbst.

### 4.8 Anwendbares Recht und Gerichtsstand

Dieser AVV unterliegt dem Recht von `{{ANWENDBARES_RECHT}}`. Ausschließlicher Gerichtsstand ist `{{GERICHTSSTAND}}`.

### 4.9 Rangfolge

Im Fall von Widersprüchen zwischen diesem Abschnitt 4 und den SCCs (Abschnitte I–III + Anhänge I–IV) gehen die SCCs nach Klausel 4 der SCCs vor. Im Fall von Widersprüchen zwischen diesem AVV (einschließlich der SCCs) und dem Hauptvertrag in Datenschutzfragen geht dieser AVV vor.

## Unterschriften

Für den **Verantwortlichen**:
Name: ___________________
Funktion: ___________________
Datum: ___________________
Unterschrift: ___________________

Für den **Auftragsverarbeiter**:
Name: ___________________
Funktion: ___________________
Datum: ___________________
Unterschrift: ___________________

---

# Anlage 1 — Anhang I zu den SCCs (Liste der Parteien)

| Rolle | Name | Adresse | Ansprechpartner | Unterschrift und Datum |
|---|---|---|---|---|
| Verantwortlicher | `{{VERANTWORTLICHER_NAME}}` | `{{ADRESSE}}` | `{{ANSPRECHPARTNER}}` | (am Ende des AVV unterzeichnet) |
| Auftragsverarbeiter | `{{AUFTRAGSVERARBEITER_NAME}}` | `{{ADRESSE}}` | `{{ANSPRECHPARTNER}}` | (am Ende des AVV unterzeichnet) |

# Anlage 2 — Anhang II zu den SCCs (Beschreibung der Verarbeitung)

**Gegenstand**: `{{GEGENSTAND}}`

**Dauer**: Für die Dauer der Erbringung der Leistungen unter dem Hauptvertrag, zuzüglich des für die Rückgabe oder Löschung personenbezogener Daten nach Klausel 10 der SCCs erforderlichen Zeitraums nach Beendigung.

**Art der Verarbeitung**: `{{ART — z. B. Erheben, Speichern, Hosten, Organisieren, Strukturieren, Abrufen, Übermitteln, Löschen}}`

**Zwecke**: `{{ZWECK — Zweck des Verantwortlichen, nicht des Auftragsverarbeiters}}`

**Kategorien personenbezogener Daten**:
- `{{Identifikatoren (z. B. Name, Personalnummer)}}`
- `{{Kontaktdaten (z. B. E-Mail, Telefon)}}`
- `{{Weitere Kategorien je nach Sachverhalt}}`
- Besondere Kategorien nach Art. 9 DSGVO: `{{ja / nein — falls ja, angeben}}`
- Personenbezogene Daten zu strafrechtlichen Verurteilungen und Straftaten nach Art. 10 DSGVO: `{{ja / nein}}`

**Kategorien betroffener Personen**:
- `{{z. B. Beschäftigte, Kunden, Interessenten, Endnutzer}}`

**Häufigkeit der Verarbeitung**: `{{kontinuierlich / periodisch / einmalig}}`

**Aufbewahrung**: `{{z. B. an Hauptvertrag gekoppelt, zzgl. Rückgabe-/Löschungszeitraum nach Beendigung}}`

# Anlage 3 — Anhang III zu den SCCs (Technische und organisatorische Maßnahmen)

Der Auftragsverarbeiter setzt folgende Maßnahmen um, um ein dem Risiko angemessenes Schutzniveau zu gewährleisten, im Einklang mit Art. 32 DSGVO und Klausel 7.4 der SCCs.

## 1. Pseudonymisierung und Verschlüsselung (Art. 32 Abs. 1 lit. a)
- **Verschlüsselung in der Übertragung**: TLS 1.2 oder höher.
- **Verschlüsselung im Ruhezustand**: AES-256 oder gleichwertig; Schlüssel in einem Schlüsselverwaltungssystem mit Rotation.
- **Pseudonymisierung**: soweit mit dem Zweck vereinbar, mit Schlüsseltrennung.

## 2. Vertraulichkeit, Integrität, Verfügbarkeit, Belastbarkeit (Art. 32 Abs. 1 lit. b)
- **Zugriffskontrolle**: rollenbasiert, minimale Berechtigung, protokolliert und überprüft.
- **Authentifizierung**: Mehr-Faktor-Authentifizierung für Systeme, die personenbezogene Daten verarbeiten.
- **Netzwerksegmentierung**: Produktivumgebung von Entwicklungs- und Testumgebungen getrennt.
- **Änderungsmanagement**: dokumentierter Prozess für Änderungen, die personenbezogene Daten betreffen.
- **Schwachstellenmanagement**: regelmäßige Scans und Patching.
- **Monitoring**: 24/7-Überwachung von Verfügbarkeit und sicherheitsrelevanten Ereignissen.
- **Vorfallreaktion**: dokumentierter Plan mit definierten Rollen.

## 3. Wiederherstellung (Art. 32 Abs. 1 lit. c)
- **Sicherungen**: verschlüsselt, getrennt gespeichert, Wiederherstellung getestet.
- **Aufbewahrung**: höchstens `{{30–90 Tage}}`.
- **Notfallwiederherstellung**: dokumentierter Plan mit definierten RTO und RPO.

## 4. Regelmäßige Überprüfung (Art. 32 Abs. 1 lit. d)
- **Penetrationstests**: jährlich durch qualifizierte unabhängige Dritte.
- **Interne Audits**: regelmäßig.
- **Zertifizierungen**: `{{z. B. ISO/IEC 27001, SOC 2 Type II, BSI C5 — mit Zertifizierungsstelle}}`.

## 5. Personelle Maßnahmen
- **Vertraulichkeit**: schriftliche Vertraulichkeitsverpflichtungen.
- **Schulungen**: Datenschutz- und Sicherheitsschulungen bei Einstellung und mindestens jährlich.
- **Datenschutz-Ansprechpartner**: `{{Name und Kontakt}}`.

## 6. Steuerung von Unterauftragsverarbeitern
- **Sorgfaltsprüfung**: dokumentiert.
- **Verträge**: mit datenschutzrechtlichen Pflichten, die nicht weniger streng sind als die der SCCs.
- **Periodische Überprüfung** der Compliance der Unterauftragsverarbeiter.

## 7. Sensible Daten (Klausel 7.5 SCCs) — nur soweit anwendbar
`{{Falls Anlage 2 Daten nach Art. 9 / Art. 10 DSGVO ausweist, befülle diesen Abschnitt. Andernfalls "Nicht anwendbar".}}`
- Verpflichtende Pseudonymisierung, soweit technisch realisierbar.
- Verschärfte Zugriffskontrollen (Need-to-know-Prinzip mit dokumentierter Begründung).
- Getrennte Verarbeitungsumgebungen.
- Erweitertes Logging und Monitoring mit verlängerter Logaufbewahrung.
- Flow-down zu Unterauftragsverarbeitern erfordert gleichwertige verschärfte Maßnahmen.

## 8. Maßnahmen zur Unterstützung des Verantwortlichen (Klauseln 8 und 9 SCCs)

### 8.1 Betroffenenrechte (Klausel 8 SCCs)
- Weiterleitungspflicht: vom Auftragsverarbeiter unmittelbar erhaltene Anträge werden innerhalb von `{{5}}` Werktagen an den Verantwortlichen weitergeleitet.
- Unterstützung bei Auskunft, Berichtigung, Löschung, Einschränkung, Übertragbarkeit, Widerspruch: innerhalb von `{{10}}` Werktagen nach Anfrage des Verantwortlichen oder einer kürzeren Frist, die dessen gesetzliche Fristen vernünftigerweise erfordern.

### 8.2 Verletzung des Schutzes personenbezogener Daten (Klausel 9 SCCs)
- Der Auftragsverarbeiter teilt jede Verletzung des Schutzes personenbezogener Daten unverzüglich, in jedem Fall innerhalb von `{{48}}` Stunden nach Kenntniserlangung, dem Verantwortlichen mit.
- Die Erstmitteilung enthält den Informationsumfang nach Art. 33 Abs. 3 DSGVO, soweit zum Zeitpunkt vernünftigerweise verfügbar; Folgemitteilungen, sobald Informationen verfügbar werden.

### 8.3 DSFA / Vorabkonsultation (Art. 35–36 DSGVO)
- Für die DSFA des Verantwortlichen erforderliche Informationen werden auf Anfrage bereitgestellt.

# Anlage 4 — Anhang IV zu den SCCs (Liste der Unterauftragsverarbeiter)

`[Option A — befüllt]`

| Nr. | Unterauftragsverarbeiter (Firmierung) | Sitz | Verarbeitungsstandort | Verarbeitungstätigkeit | Datenkategorien | Garantien (bei Drittland) |
|---|---|---|---|---|---|---|
| 1 | `{{UAV 1}}` | `{{Sitz}}` | `{{Standort}}` | `{{Tätigkeit}}` | `{{Daten}}` | `{{Mechanismus}}` |
| ... | | | | | | |

`[Option B — keine bei Vertragsschluss]`

Der Auftragsverarbeiter bestätigt, dass zum Zeitpunkt des Abschlusses dieses AVV keine Unterauftragsverarbeiter eingesetzt werden. Vor Einsatz eines Unterauftragsverarbeiters ist Klausel 7.7 der SCCs (Option `{{1 / 2}}` gemäß Auswahl in Abschnitt 1.4) einzuhalten.

# Anlage 5 — Drittlandübermittlungen (nur soweit anwendbar)

`{{Sind Drittlandübermittlungen im Spiel, identifiziere Empfänger, Land/Länder, Rolle und Kapitel-V-Mechanismus. Verweise auf Durchführungsbeschluss (EU) 2021/914 (Modul 2 oder 3 nach Maßgabe), befülle dessen Anhänge I.A / I.B / I.C / II / III und referenziere etwaige TIA nach Klausel 14 dieser SCCs. Sind keine Übermittlungen im Spiel, markiere "Nicht anwendbar".}}`

---

# Hinweise zum Entwurf (vor Unterzeichnung löschen)

- Firmierung, Adresse, Registrierungsnummern und Unterzeichner beider Parteien bestätigen.
- Verbindlichen ABl.-DE-Text gegen `references/2021-915-commission-text-de.md` und den ABl.-Link vor Unterzeichnung verifizieren.
- Wahlmöglichkeiten in Abschnitt 1.4 fixieren (Beitritt, UAV-Option, Vorlauffrist).
- Anlage 1 (Anhang I), Anlage 2 (Anhang II), Anlage 3 (Anhang III), Anlage 4 (Anhang IV) befüllen.
- Bei sensiblen Daten (Art. 9 / Art. 10): Anlage 3 Abschnitt 7 befüllen.
- Bei Drittlandübermittlungen: Anlage 5 befüllen und sicherstellen, dass die 2021/914-SCCs flankierend abgeschlossen werden.
- `[ALT 1]` oder `[ALT 2]` in Abschnitt 4.3 (Haftung) je nach Perspektive wählen.
- Anwendbares Recht und Gerichtsstand in Abschnitt 4.8 bestätigen.

# Praktikerhinweis (für Mandanten-Deliverables OneZero Legal)

Diese Vorlage nutzt den Durchführungsbeschluss (EU) 2021/915 mit Inkorporation durch Verweis, mit den Anhängen als Anlagen zu diesem AVV und einem minimalen kommerziellen Abschnitt 4 als Overlay. Die Compliance-Vermutung nach Art. 28 Abs. 7 DSGVO knüpft an die unveränderten SCCs an.

Hauptvorteil von Tier 2 (Strict) ist der Safe-Harbor-Effekt — nützlich für Engagements, bei denen aufsichtsbehördliche Prüfung wahrscheinlich ist. Die Trade-offs sind kommerziell: Abschnitt 4 ist bewusst dünn, die Rangfolgeklausel (Klausel 4 SCCs) hebt widersprüchliche Hauptvertragsregelungen still auf, und es besteht keine Flexibilität bei Klauseln in Abschnitt II.

Für Situationen, die einen stärkeren kommerziellen Abschnitt III (Laufzeit, ordentliche Kündigung, Übergabe, ausgefeilte Haftungsverteilung) erfordern, verwende stattdessen Tier 3 (Hybrid) — gleicher Safe-Harbor-Vorteil für Abschnitte I + II, mit verhandeltem Abschnitt-III-Ersatz nach Klausel 2 lit. b SCCs.
