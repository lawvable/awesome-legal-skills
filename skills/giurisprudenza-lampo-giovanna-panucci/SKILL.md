---
name: giurisprudenza-lampo
description: >
  Ricerca giurisprudenziale rapida per ottenere un quadro di orientamento
  iniziale su un tema giuridico. Si attiva con "giurisprudenza-lampo [tema]",
  "cerca giurisprudenza su [tema]", "sentenze su [tema]", "pronunce su [tema]",
  "orientamento giurisprudenziale su [tema]", o qualsiasi variante che chieda
  di cercare sentenze, pronunce, massime, orientamenti giurisprudenziali o
  precedenti su un argomento giuridico. Usa questa skill anche quando l'utente
  dice "cosa dice la giurisprudenza su", "ci sono sentenze su", "precedenti su",
  "come si è espressa la Cassazione/il TAR/il Consiglio di Stato su".
metadata:
  author: "Giovanna Panucci"
  license: "agpl-3.0"
  version: "2026-05-12"
---

Stai eseguendo una ricerca giurisprudenziale rapida.
L'obiettivo è un quadro di orientamento iniziale,
non un parere esaustivo.

## Invocazione

"giurisprudenza-lampo [tema giuridico]".

## Step 1: Ricerca

Cerca sul web pronunce recenti e rilevanti sul tema.
Fonti prioritarie: DeJure, Italgiure, siti istituzionali
dei TAR e del Consiglio di Stato, Corte di Cassazione,
riviste giuridiche online (Altalex, Diritto.it,
Giurisprudenza Penale, Foro Italiano).
Cerca almeno 3-5 pronunce se disponibili.

## Step 2: Quadro

### Tema
[1-2 frasi. La questione giuridica esaminata.]

### Pronunce trovate
Per ogni pronuncia rilevante:
- Estremi: [Autorità, sezione, data, numero]
- Massima sintetica: [1-2 frasi sul principio affermato]
- Rilevanza: [perché conta per il caso in esame]

### Orientamento prevalente
[1 paragrafo. Come si orienta la giurisprudenza
maggioritaria. Se c'è contrasto, segnalarlo.]

### Implicazioni operative
[2-3 spunti concreti per il parere o la strategia.]

### Fonti
[Link alle fonti usate.]

## Step 3: Avvertenza

Concludi sempre con:
"Ricerca di orientamento iniziale.
Verificare gli estremi e completare
con ricerca su banche dati specializzate."

## Step 4: Salva

research/giurisprudenza-[tema-slug]-[YYYY-MM-DD].md
