# Kit minimo di fonti gratuite per materia

Per ogni materia di pratica, il nucleo minimo di fonti ufficiali e liberamente accessibili: normativa, prassi/autorità, giurisprudenza e decisioni. Gli estremi degli atti normativi sono in `fonti_normative.md`; condizioni d'accesso, licenze e regole di riuso trasversali in `fonti_dati_giuridici.md`.

- Data di verifica: 2026-07-06 (tutti gli URL verificati via fetch o curl); voci aggiunte il 2026-07-17 (§§19-21) verificate separatamente alla stessa data.
- Regole: nessuna fonte a pagamento; le fonti con login gratuito riservato a una categoria sono marcate "(per categoria)"; i siti che bloccano l'accesso automatico sono marcati "(anti-bot: fallback con ricerca `site:` o istruzioni all'utente)".

---

## 1. Civile (base comune) [copertura piena]

- Normativa: codice civile, codici di procedura, preleggi — Normattiva.
- Legittimità: SentenzeWeb (full-text civile, booleani AND/OR/NOT, filtri sezione/anno/riferimenti normativi).
- Merito: Banca Dati di Merito / BDP (bdp.giustizia.it) — civile dal 2016 con abstract, **richiede SPID/CIE/CNS** (per categoria: istruzioni all'utente); esclusi famiglia, minori e stato della persona.
- Liquidazione del danno: Tabelle milanesi (tribunale-milano.giustizia.it, PDF liberi).
- Orientamenti: rassegne civili dell'Ufficio del Massimario (§ Massime in `fonti_dati_giuridici.md`).

## 2. Penale [copertura parziale]

- Normativa: codice penale, c.p.p., ordinamento penitenziario, T.U. stupefacenti — Normattiva.
- Legittimità: SentenzeWeb (archivio penale, stessi filtri del civile); rassegne penali dell'Ufficio del Massimario.
- Corti superiori: Corte costituzionale; CEDU via HUDOC; CGUE via InfoCuria.
- Riviste gratuite (contenuto editoriale, solo citazione): Sistema Penale (CC BY-NC-ND 4.0), Giurisprudenza Penale, archivio Diritto Penale Contemporaneo 2010-2019 (CC BY-NC 4.0).
- **Lacuna strutturale:** la giurisprudenza penale di merito non ha alcuna fonte gratuita strutturata (la BDP è solo civile). Dichiararlo sempre.

## 3. Amministrativo [copertura piena]

- Normativa: L. 241/1990, c.p.a., T.U. enti locali, T.U. pubblico impiego — Normattiva.
- Giurisprudenza: giustizia-amministrativa.it (CdS, TAR, CGARS, full-text liberi); OpenGA (openga.giustizia-amministrativa.it) — open data **CC BY 4.0**, API CKAN.
- Contabile: banchedati.corteconti.it.

## 4. Tributario [copertura piena]

- Normativa: TUIR, T.U. IVA, T.U. registro, Statuto del contribuente — Normattiva.
- Prassi: Agenzia delle Entrate "Normativa e prassi"; def.finanze.it (documentazione economica e finanziaria).
- Giurisprudenza: Massimario nazionale della giurisprudenza tributaria (def.finanze); Cassazione tributaria su SentenzeWeb; rassegne tributarie del Massimario.

## 5. Lavoro e previdenza [copertura piena]

- Normativa: Statuto dei lavoratori, Jobs Act, D.lgs. 81/2015, T.U. sicurezza 81/2008 — Normattiva.
- Prassi: INL (circolari e note, ispettorato.gov.it); interpelli Ministero del Lavoro ex art. 9 D.lgs. 124/2004; INPS "Circolari, Messaggi e Normativa"; INAIL (inail.it, sezione normativa e circolari) per infortuni e malattie professionali — verificato liberamente consultabile, nessuna licenza di riuso dichiarata esplicitamente (presunto permissivo, atto pubblico).
- **CCNL:** archivio nazionale CNEL (cnel.it/Archivio-Contratti) — fonte ufficiale ex art. 17 L. 936/1986, testi depositati dalle parti; dataset **open data IODL 2.0** (riuso anche commerciale con attribuzione) su cnel.it/Archivio-Contratti-Collettivi/Contratti-Open-Data.
- Pubblico impiego: ARAN (aranagenzia.it) — CCNL per comparto e orientamenti applicativi (anti-bot: fallback `site:aranagenzia.it`).
- Giurisprudenza: Cassazione lavoro su SentenzeWeb; merito su BDP (SPID).

## 6. Bancario, assicurativo e finanziario [copertura piena]

- Normativa: T.U.B., T.U.F. — Normattiva; per il quadro UE articolo per articolo: EBA Interactive Single Rulebook (CRR/CRD/PSD2/DORA/MiCA), EIOPA Solvency II Single Rulebook.
- Vigilanza bancaria: Banca d'Italia — normativa di vigilanza (Circ. 285/2013 ecc.), orientamenti di vigilanza, provvedimenti sanzionatori (nota copyright del sito restrittiva: riuso sicuro limitato al testo dei singoli atti con citazione).
- Assicurativo: IVASS — regolamenti e lettere al mercato (archivio per anno, ricerca per keyword).
- Finanziario: CONSOB — bollettino (delibere, comunicazioni, sanzioni) e sezione regolamentazione (TUF, regolamenti, orientamenti ESMA).
- Antiriciclaggio: UIF (uif.bancaditalia.it) — indicatori di anomalia (Provv. 12.5.2023), schemi di comportamenti anomali, Quaderni.
- Autorità UE: EBA Single Rulebook Q&A; ESMA Document Library (~7.000 documenti, riuso con citazione e obbligo di dichiarare le modifiche); EIOPA (riuso con "Source: EIOPA").
- **Decisioni ADR:** ABF — Arbitro Bancario Finanziario (arbitrobancariofinanziario.it): decisioni dal 2010, ricerca avanzata libera per oggetto/anno/testo; ACF — Arbitro per le Controversie Finanziarie (acf.consob.it): decisioni dal 2017. Valore: orientamenti ADR, non giurisprudenza; citare come tali.

## 7. Societario [copertura piena]

- Normativa: codice civile libro V, T.U.F., T.U. società a partecipazione pubblica — Normattiva.
- Orientamenti notarili (contenuto redazionale protetto, libera consultazione, solo citazione con fonte): Massime della Commissione Società del Consiglio Notarile di Milano (~230 massime, indice sistematico); Orientamenti societari del Comitato Triveneto dei Notai.
- Bilancio: principi contabili OIC (fondazioneoic.eu) — PDF liberi ma riuso vietato oltre consultazione e citazione (diritti editoriali riservati).
- Giurisprudenza: Cassazione su SentenzeWeb; merito su BDP e ilcaso.it (livello gratuito).

## 8. Crisi d'impresa [copertura piena]

- Normativa: Codice della crisi d'impresa e dell'insolvenza (D.lgs. 14/2019), legge fallimentare per il ratione temporis — Normattiva.
- Giurisprudenza e materiali: Diritto della Crisi (dirittodellacrisi.it, rivista ANVUR, provvedimenti full-text liberi); IL CASO.it (merito per tribunale, dal 1996, livello gratuito); Unijuris (osservatorio fallimentare, Univ. Udine); Cassazione su SentenzeWeb.
- Nota riuso: i provvedimenti pubblicati da queste riviste sono atti pubblici citabili; massime redazionali e note sono protette.
- Sovraindebitamento (consumatore, piccolo imprenditore): registro pubblico degli Organismi di Composizione della Crisi (L. 3/2012, D.M. 202/2014) su crisisovraindebitamento.giustizia.it (landing page su giustizia.it verificata raggiungibile) — **il sotto-dominio del registro blocca ogni fetch automatico** (testato con WebFetch, curl con User-Agent da browser, navigazione reale: tutti falliti, pattern coerente con altri domini `*.giustizia.it` già noti nel repo, es. SentenzeWeb): fonte reale ma verificabile solo da browser umano dell'utente finale, non instradabile per ricerca automatica.

## 9. Famiglia e minori [copertura parziale]

- Normativa: codice civile libro I, L. divorzio 898/1970, L. adozione 184/1983, L. Cirinnà 76/2016, riforma Cartabia — Normattiva.
- Giurisprudenza: Cassazione su SentenzeWeb; Corte costituzionale; CEDU (HUDOC, art. 8).
- Materiali: AGIA — Autorità Garante Infanzia e Adolescenza (linee guida, pareri); AIMMF (minoriefamiglia.org, contenuti pubblici); Tabelle milanesi per il danno.
- **Lacuna strutturale:** la BDP esclude famiglia, minori e stato della persona: il merito di famiglia non ha fonte gratuita. Dichiararlo sempre.

## 10. Proprietà intellettuale [copertura piena]

- Normativa: Codice della proprietà industriale (D.lgs. 30/2005), L. 633/1941 sul diritto d'autore — Normattiva.
- Registri: banca dati UIBM (titoli italiani dal 1989); EUIPO eSearch plus (marchi UE, disegni); TMview/DesignView (aggregatore TMDN); EPO European Patent Register + Espacenet (anti-bot: per accesso programmatico usare l'API OPS, gratuita con registrazione); WIPO PATENTSCOPE e Global Brand Database.
- Giurisprudenza e decisioni: EUIPO eSearch Case Law (Commissioni di ricorso, sentenze UE su marchi/disegni); EPO Boards of Appeal (decisioni dal 1979, full-text); UPC — Unified Patent Court, decisions and orders (anti-bot: fallback `site:unifiedpatentcourt.org`); sezioni specializzate impresa via BDP (SPID).

## 11. Diritto dei consumatori e concorrenza [copertura piena]

- Normativa: Codice del consumo (D.lgs. 206/2005) — Normattiva.
- Autorità: AGCM — ricerca avanzata provvedimenti (intese, abusi, pratiche commerciali scorrette, clausole vessatorie); l'intero dominio agcm.it risponde 403 ai fetch automatici: fallback `site:agcm.it` o Bollettino PDF.
- ADR: elenco nazionale organismi ADR del MIMIT; elenco UE degli organismi ADR (consumer-redress.ec.europa.eu); ConciliaWeb AGCOM (telecomunicazioni, accesso SPID); Servizio Conciliazione ARERA (energia, acqua, rifiuti); ABF e ACF per banche/investimenti (§6).
- **Attenzione:** la piattaforma ODR europea è **dismessa dal 20 luglio 2025** (Reg. UE 2024/3228): non instradare più verso ec.europa.eu/consumers/odr.

## 12. Real estate ed edilizia [copertura piena]

- Normativa: T.U. edilizia (D.P.R. 380/2001), T.U. espropri, codice civile libro III — Normattiva.
- Dati immobiliari: quotazioni OMI dell'Agenzia delle Entrate (semestrali per zona, citare "Agenzia delle Entrate – OMI"); pubblicazioni OMI (rapporti immobiliari, statistiche); Geoportale Cartografico Catastale — **CC BY 4.0**, servizi WMS/WFS interrogabili.
- Visure catastali e ispezioni ipotecarie: gratuite via SPID/CIE/CNS (per categoria: istruzioni all'utente).
- Giurisprudenza: edilizia/urbanistica su giustizia-amministrativa.it; civile su SentenzeWeb e BDP.
- Studi del Consiglio Nazionale del Notariato (notariato.it): consultazione libera ma **riproduzione vietata** dalle note legali — solo link e breve citazione con fonte.

## 13. Privacy e data protection [copertura piena]

- Normativa: GDPR (Reg. UE 2016/679) su EUR-Lex; Codice privacy (D.lgs. 196/2003) — Normattiva.
- Autorità: Garante — provvedimenti in banca dati DocWeb (gpdp.it, citare il numero doc web); EDPB — linee guida e opinioni.
- Giurisprudenza: CGUE via InfoCuria (fondamentale in materia); CEDU via HUDOC; Cassazione su SentenzeWeb.

## 14. Compliance e responsabilità degli enti (231) [copertura piena]

- Normativa: D.lgs. 231/2001, D.lgs. 231/2007 (antiriciclaggio), D.lgs. 24/2023 (whistleblowing) — Normattiva.
- Linee guida: Confindustria — Linee Guida 231 (ed. 2021, approvate dal Ministero della Giustizia; documento protetto, citazione con fonte); UIF — indicatori di anomalia e schemi; ANAC — linee guida whistleblowing (delibera 311/2023 e successive).
- Giurisprudenza: Cassazione su SentenzeWeb (responsabilità enti, Sez. pen.); rassegne del Massimario.

## 15. Diritto scolastico [copertura piena]

- Normativa: T.U. istruzione (D.lgs. 297/1994), L. 107/2015 — Normattiva; normativa e circolari MIM (mim.gov.it/web/guest/normativa, filtri per tipologia/tematica/data, niente full-text: fallback `site:mim.gov.it`).
- CCNL: comparto Istruzione e Ricerca su ARAN e archivio CNEL.
- Contenzioso: giustizia-amministrativa.it (ricorsi su graduatorie, concorsi, dimensionamento); Cassazione lavoro per il rapporto d'impiego.

## 16. Immigrazione e protezione internazionale [copertura piena]

- Normativa: T.U. immigrazione (D.lgs. 286/1998), D.lgs. 251/2007, D.lgs. 25/2008 — Normattiva (permalink URN-NIR stabili).
- Prassi: circolari del Dipartimento Libertà Civili e Immigrazione del Ministero dell'Interno (libertaciviliimmigrazione.dlci.interno.gov.it, solo filtro data: fallback `site:`); Commissione nazionale per il diritto di asilo.
- UE: EUAA (riproduzione autorizzata con citazione) — Asylum Report, Country Guidance, Case Law Database; portale COI (coi.euaa.europa.eu) per le informazioni sui paesi di origine.
- Giurisprudenza: Cassazione su SentenzeWeb; rassegne del Massimario sulla protezione internazionale; CEDU via HUDOC; CGUE via InfoCuria.
- Raccolta di settore: banca dati ASGI (asgi.it/banca-dati, licenza CC BY-NC-SA 4.0: riuso solo non commerciale con attribuzione; i provvedimenti in sé restano atti pubblici).

## 17. Deontologia forense [copertura parziale]

- Normativa: legge professionale forense (L. 31 dicembre 2012, n. 247) — Normattiva (v. `fonti_normative.md`); Codice Deontologico Forense adottato dal CNF, testo consolidato pubblicato in PDF su consiglionazionaleforense.it/codice-deontologico-forense (non è fonte legislativa su Normattiva: autoregolamentazione dell'Ordine, verificare sempre l'ultima modifica sul sito, es. l'art. 25-bis sull'equo compenso).
- Organo competente: Consigli Distrettuali di Disciplina (CDD, istituiti dalla L. 247/2012, artt. 50 ss.) in primo grado; Consiglio Nazionale Forense in sede di impugnazione.
- **Lacuna strutturale:** nessuna banca dati pubblica gratuita e ricercabile di giurisprudenza disciplinare risulta verificata (solo comunicati e circolari sparsi sul sito CNF); non presumerne l'esistenza.

## 18. Appalti [copertura piena]

- Normativa: Codice dei contratti pubblici (D.lgs. 31 marzo 2023, n. 36) — Normattiva; i previgenti D.lgs. 50/2016 e D.lgs. 163/2006 sono abrogati e rilevano solo ratione temporis (v. `fonti_normative.md`).
- Prassi: ANAC (anticorruzione.it) — delibere, pareri, linee guida, bandi-tipo; dati di gara aperti su dati.anticorruzione.it/opendata (BDNCP, formati CSV/JSON/OCDS, API via PDND).
- Giurisprudenza: contenzioso su giustizia-amministrativa.it; open data su OpenGA (CC BY 4.0).
- Arbitrati: Camera Arbitrale per i Contratti Pubblici presso ANAC (anticorruzione.it/en/arbitrati, ex art. 214 D.lgs. 36/2023) — lodi arbitrali scaricabili in PDF, dati delle persone fisiche senza ruolo funzionale già anonimizzati dalla fonte; verificato liberamente accessibile.
- Rito: termini processuali speciali (rito appalti, art. 120 c.p.a.) in `percorsi_processuali.md`.

## 19. Successioni e regimi patrimoniali della famiglia [copertura parziale]

- Normativa: codice civile, libro II (successioni) e libro I, titolo VI (regime patrimoniale della famiglia) — Normattiva; T.U. imposta sulle successioni e donazioni (D.lgs. 31 ottobre 1990, n. 346) — estremi verificati in `fonti_normative.md`.
- Prassi: Agenzia delle Entrate — circolari e risposte a interpello sulla dichiarazione di successione; Studi del Consiglio Nazionale del Notariato (notariato.it/ufficio-studi): consultazione libera ma **riproduzione vietata** — solo link e breve citazione con fonte (stesso regime di riuso di § 12).
- Giurisprudenza: Cassazione su SentenzeWeb; merito su BDP (SPID) quando non rientra nell'esclusione famiglia/stato della persona (v. § 1, § 9).
- **Lacuna dichiarata:** nessun cancello procedurale specifico (termini per accettazione con beneficio d'inventario, rinuncia, azione di riduzione) è ancora verificato in `percorsi_processuali.md`: verificare gli articoli puntuali prima di citarli.

## 20. Ambiente ed energia [copertura parziale]

- Normativa: Codice dell'ambiente (D.lgs. 3 aprile 2006, n. 152) — Normattiva, estremi già verificati in `fonti_normative.md`.
- Autorizzazioni: portale nazionale VIA-VAS-AIA del MASE (va.mite.gov.it) — provvedimenti conclusivi e procedimenti in corso; **al 2026-07-17 il servizio interattivo risulta temporaneamente disabilitato per verifica dei requisiti di sicurezza informatica** (banner esplicito sul sito), ma i contenuti restano consultabili in sola lettura: verificare lo stato all'uso.
- Dati tecnici: ISPRA (isprambiente.gov.it) — relazioni e dati ambientali.
- Energia: ARERA (arera.it) — delibere di regolazione, distinte dallo sportello ADR già censito in § 11; GSE (gse.it) per gli incentivi FER — **licenza di riuso non verificata**: trattare come atto pubblico citabile, non presumere riuso massivo.
- Giurisprudenza: contenzioso su giustizia-amministrativa.it (v. § 3).

## 21. Diritto sportivo [solo instradamento]

- Normativa: riparto di giurisdizione sportiva, L. 17 ottobre 2003, n. 280 (conversione del D.L. 220/2003) — **estremi da verificare su Normattiva prima di citarli puntualmente**, non ancora in `fonti_normative.md`.
- Prassi/autoregolamentazione: Codice della Giustizia Sportiva del CONI (coni.it) — atto di autoregolamentazione, non fonte legislativa statale: verificare sempre la versione corrente sul sito.
- Decisioni: Collegio di Garanzia dello Sport del CONI (coni.it/it/attivita-istituzionali/collegio-di-garanzia-dello-sport/giudizi.html) — archivio dei giudizi; il fetch diretto ha dato errore nei test (pattern anti-bot noto per i portali istituzionali già censiti nel repo): verificare accessibilità e continuità dell'archivio all'uso.
- **Lacuna dichiarata:** nessuna giurisprudenza federale di settore (es. giustizia sportiva FIGC) è stata verificata: non presumerne la reperibilità gratuita.

## 22. Terzo settore [copertura parziale]

- Normativa: Codice del Terzo Settore (D.lgs. 3 luglio 2017, n. 117) — Normattiva, estremi già verificati in `fonti_normative.md`; abrogazioni espresse e differite ex art. 102: verificare sempre la vigenza puntuale della singola disposizione.
- Registro: RUNTS — Registro Unico Nazionale del Terzo Settore (servizi.lavoro.gov.it/runts, Ministero del Lavoro) — ricerca enti iscritti, pubblica e gratuita; verificato consultabile senza login. Nota legale sul riuso non esplicita in home page: trattare come atto pubblico citabile, non come dataset da acquisire in blocco.
- Prassi: circolari del Ministero del Lavoro in materia di terzo settore (lavoro.gov.it, stessa fonte già citata in § 5).
- **Lacuna dichiarata:** nessuna giurisprudenza specifica di settore risulta verificata; il contenzioso ricade nel civile o amministrativo generale a seconda della materia (v. § 1, § 3), da instradare di conseguenza.

## 23. Diritto dei trasporti [solo instradamento]

- Normativa: disciplina di settore (ferroviario, portuale, aeroportuale) frammentata su Normattiva per atto; **estremi da verificare puntualmente prima di citarli**, non ancora in `fonti_normative.md`.
- Autorità: Autorità di Regolazione dei Trasporti — ART (autorita-trasporti.it/ricerca-avanzata) per delibere, pareri, consultazioni e segnalazioni su accesso alle infrastrutture, oneri di servizio pubblico, tariffe; verificato liberamente consultabile senza login, filtri per anno/tipo atto/modalità di trasporto; nessuna licenza di riuso esplicita oltre il copyright generico di sito (presunto permissivo, atto pubblico).
- Giurisprudenza: contenzioso su giustizia-amministrativa.it (v. § 3) quando incide su provvedimenti autorizzatori.
- **Lacuna dichiarata:** diritto della navigazione/marittimo (codice della navigazione, Guardia Costiera, Autorità di Sistema Portuale) è stato esplorato ma non ancora inserito in questo catalogo: le fonti delle 16 Autorità di Sistema Portuale sono frammentate su portali distinti senza un indice unico, verificarle singolarmente prima di instradare un utente.

---

## Lacune trasversali (da dichiarare quando rilevano)

1. **Massime CED con numero Rv:** non liberamente accessibili al pubblico; surrogati gratuiti in § Massime di `fonti_dati_giuridici.md`; per gli avvocati iscritti a Cassa Forense esiste l'accesso gratuito a ItalgiureWeb (per categoria).
2. **Citator:** nessuna fonte gratuita dice se un precedente è superato; ricostruire con ricerche incrociate e relazioni su contrasti del Massimario.
3. **Merito penale** e **merito famiglia/minori:** privi di fonte gratuita strutturata.
4. **Ricerca trasversale unificata:** non esiste gratis; instradare su più motori distinti secondo il routing.
5. **Accesso programmatico:** API disponibili solo per Normattiva, EUR-Lex, OpenGA (CKAN), EPO OPS, dataset CNEL; molti siti istituzionali bloccano i fetch automatici — prevedere sempre il fallback (`site:` o istruzioni all'utente).
