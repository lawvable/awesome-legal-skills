# Registro delle lacune dichiarate

Elenco unico delle lacune strutturali già dichiarate nei singoli cataloghi — nessun contenuto nuovo rispetto a `fonti_per_materia.md`, `fonti_dati_giuridici.md` e `percorsi_processuali.md`: solo un punto d'ingresso per vederle tutte insieme prima di prioritizzare un aggiornamento. In caso di conflitto tra questo file e il catalogo di origine, prevale il catalogo di origine.

- Data di consolidamento: 2026-07-21.

## Maturità per area (`fonti_per_materia.md`)

Ogni sezione porta l'etichetta nel titolo; qui solo l'indice, verificato staticamente da `scripts/verifica_skill.py`.

| Copertura piena (15) | Copertura parziale (6) | Solo instradamento (2) |
|---|---|---|
| Civile, Amministrativo, Tributario, Lavoro e previdenza, Bancario/assicurativo/finanziario, Societario, Crisi d'impresa, Proprietà intellettuale, Consumatori e concorrenza, Real estate ed edilizia, Privacy e data protection, Compliance e 231, Diritto scolastico, Immigrazione, Appalti | Penale (merito scoperto), Famiglia e minori (merito scoperto), Deontologia forense (giurisprudenza disciplinare non verificata), Successioni (cancelli non verificati), Ambiente ed energia (portale MASE instabile, licenza GSE non verificata), Terzo settore (giurisprudenza specifica non verificata) | Diritto sportivo (estremi normativi da verificare), Diritto dei trasporti (estremi normativi da verificare) |

## Copertura giurisprudenziale

- **Merito penale**: privo di fonte gratuita strutturata (`fonti_per_materia.md` § 2, § Lacune trasversali).
- **Merito famiglia e minori**: escluso dalla Banca Dati di Merito, privo di fonte gratuita (`fonti_per_materia.md` § 9, § Lacune trasversali).
- **Giurisprudenza disciplinare forense**: nessuna banca dati pubblica gratuita e ricercabile verificata (`fonti_per_materia.md` § 17).
- **Giurisprudenza federale sportiva** (es. FIGC): non verificata, non presumerne la reperibilità gratuita (`fonti_per_materia.md` § 21).
- **Giurisprudenza specifica del terzo settore**: non verificata; il contenzioso ricade nel civile o amministrativo generale (`fonti_per_materia.md` § 22).
- **Citator gratuito**: nessuna fonte dice se un precedente è superato; si ricostruisce con ricerche incrociate e le relazioni su contrasti del Massimario (`fonti_per_materia.md` § Lacune trasversali; `fonti_dati_giuridici.md` § 3-bis).
- **Massime CED con numero Rv**: non liberamente accessibili (per categoria: ItalgiureWeb, avvocati Cassa Forense) — surrogati in `fonti_dati_giuridici.md` § 3-bis.

## Copertura normativa e di cancelli procedurali

- **Successioni**: nessun cancello procedurale specifico (termini per accettazione con beneficio d'inventario, rinuncia, azione di riduzione) ancora verificato in `percorsi_processuali.md` (`fonti_per_materia.md` § 19).
- **Percorsi processuali**: il catalogo copre solo civile (incluse esecuzione forzata e azione di classe), condominio, lavoro e previdenza, famiglia (rito), amministrativo, tributario, crisi d'impresa, proprietà intellettuale, immigrazione, penale — le altre 14 aree di `fonti_per_materia.md` non hanno ancora un cancello procedurale dedicato (`percorsi_processuali.md`, Regole d'uso, punto 4).

## Copertura di fonti per materia

- **Diritto della navigazione e marittimo**: esplorato ma non catalogato — le fonti delle 16 Autorità di Sistema Portuale sono frammentate su portali distinti senza indice unico (`fonti_per_materia.md` § 23).
- **Registro OCC (sovraindebitamento)**: fonte reale ma il sotto-dominio blocca ogni fetch automatico testato — verificabile solo da browser umano dell'utente finale (`fonti_per_materia.md` § 8).

## Limiti strutturali trasversali

- **Ricerca unificata trasversale**: non esiste gratis; si instrada su più motori distinti secondo il Routing (`fonti_per_materia.md` § Lacune trasversali).
- **Accesso programmatico**: API disponibili solo per Normattiva, EUR-Lex, OpenGA (CKAN), EPO OPS, dataset CNEL; molti siti istituzionali bloccano i fetch automatici, con fallback `site:` o istruzioni all'utente (`fonti_per_materia.md` § Lacune trasversali).
- **Copertura eval di minimizzazione**: solo una minoranza delle eval verifica `tool_input_must_not_include` (conteggio esatto riportato da `scripts/verifica_skill.py` a ogni esecuzione) — la maggior parte della disciplina di minimizzazione resta verificata solo narrativamente o a mano.
