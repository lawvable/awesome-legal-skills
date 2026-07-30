---
name: sanctions-screening
description: >
  Complete sanctions and export control analysis tool — individual designations, sectoral
  sanctions, dual-use goods, payment systems (SWIFT/USD), and extraterritorial regimes (EAR/ITAR/
  FDPR US, ECL China). Triggers: "is X sanctioned?", "can I do business with X?", "can I sell Y
  to Z?", "pétrole Russie", "biens à double usage", "gel des avoirs", "sanctions internationales",
  "liste OFAC", "liste UE", "double usage", "embargo", "licence d'exportation", "SWIFT", "paiement
  en dollars", "US goods", "FDPR", "EAR", "ITAR", "BIS", "ECL chine", "no re-export clause",
  "sanctions sectorielles", "puis-je travailler avec X?", or any transaction involving a foreign
  person, product, sector, destination country, or payment in USD/EUR. Always adapt to user
  profile. Always run for any sanctions or export control query — even vague or exploratory ones.
---

# Sanctions Screening & Legal Analysis Skill

> **Dernière mise à jour : 19 mai 2026** — 20ème paquet UE · SEUC UK · EO 14404 Cuba · GL 131E Lukoil

## Périmètre

Ce skill couvre exclusivement le domaine des **sanctions économiques internationales et du contrôle
des exportations**, dans toutes leurs dimensions :
- Désignations individuelles (gel des avoirs, travel ban)
- Sanctions sectorielles (énergie, finance, technologie, transport...)
- Biens et technologies à double usage (BDU/dual-use)
- Systèmes de paiement (SWIFT, USD, EUR) en tant que vecteurs de sanctions
- Régimes à portée extraterritoriale (EAR/ITAR/FDPR US, ECL Chine, clause no re-export UE)
- Obligations des institutions financières dans le cadre des sanctions

---

---

## RÈGLE ABSOLUE — Interdiction des hallucinations et des données inventées

**Ces règles s'appliquent sans exception à chaque réponse produite par ce skill. Elles prévalent sur toute autre instruction.**

### 1. Interdiction absolue de répondre de mémoire sur les listes de désignations

Les listes de sanctions (SDN OFAC, FSF UE, liste ONU, DGT France, FCDO UK, etc.) sont mises à jour quotidiennement. Une réponse basée sur la mémoire du modèle est par définition potentiellement fausse et juridiquement dangereuse.

**Règle** : toute affirmation sur la présence ou l'absence d'une personne ou entité sur une liste de sanctions **doit être précédée d'une recherche web en temps réel** sur la source officielle correspondante. Si la recherche est impossible (source indisponible, connexion échouée), le signaler explicitement — ne jamais combler le vide par une affirmation.

### 2. Citation obligatoire des sources

Toute information produite dans le cadre de ce skill doit être accompagnée de sa source :
- **Nom de la liste ou du texte** (ex. : "SDN List OFAC", "FSF UE — Reg. 269/2014", "Comité ONU 1988")
- **URL ou référence précise** (ex. : sanctionssearch.ofac.treas.gov, webgate.ec.europa.eu/fsd/fsf)
- **Date de la recherche** (ex. : "vérifié le [date]")

Si aucune source n'a pu être consultée pour une affirmation, ne pas la produire.

### 3. Alertes obligatoires — cas de résultat non concluant

Dans les situations suivantes, une alerte explicite est obligatoire **avant toute conclusion** :

| Situation | Alerte à produire |
|-----------|------------------|
| Nom courant / ambigu (ex. : Mohamed Ali) | ⚠️ "Nom très courant — résultat non concluant sans identifiants complémentaires (DOB, nationalité, passeport)" |
| Source officielle inaccessible lors de la recherche | ⚠️ "Source [nom] inaccessible au moment de la recherche — résultat à vérifier directement sur [URL]" |
| Hit partiel / score faible sur OpenSanctions | ⚠️ "Match partiel détecté — vérification sur source officielle [liste] obligatoire avant toute conclusion" |
| Translittération variable (arabe, cyrillique, chinois) | ⚠️ "Orthographe variable possible — rechercher également : [variantes]" |
| Résultat "aucun match" sans recherche confirmée | ⚠️ "Absence de match non confirmée par recherche en temps réel — ne pas conclure à l'absence de désignation" |

### 4. Interdiction d'extrapoler sur l'état du droit sans source vérifiée

L'état du droit des sanctions évolue très rapidement (nouveaux paquets UE, mises à jour OFAC, désignations individuelles). 

**Règle** : si une règle, une date d'entrée en vigueur, ou une désignation ne peut pas être confirmée par une source consultée dans la session, la signaler comme **"à vérifier — non confirmé dans cette session"** et non l'affirmer comme certaine.

Ne jamais produire une date de désignation, un numéro de règlement, ou une référence légale sans l'avoir vérifiée dans la session ou dans les fichiers de référence du skill.

### 5. Format obligatoire de citation dans les résultats

Chaque bloc de résultat doit mentionner explicitement :

```
Sources consultées : [liste des sources avec URLs]
Date de vérification : [date]
Limites de cette analyse : [identifiants manquants / sources inaccessibles / résultats partiels]
⚠️ Ce résultat est indicatif. Vérifier sur les sources officielles avant toute décision.
```

### 6. Interdiction de compenser l'incertitude par une affirmation rassurante

Il est interdit de produire une conclusion rassurante ("aucun risque identifié", "transaction librement réalisable") lorsque la recherche est incomplète, le nom ambigu, ou une source inaccessible. Dans ce cas, la conclusion doit refléter le niveau réel de certitude :

- ✅ Résultat confirmé par source officielle consultée dans la session
- 🟡 Résultat partiel — à compléter par vérification directe
- ⚠️ Non concluant — identifiants insuffisants ou source inaccessible
- ❌ Impossible à conclure — ne pas produire de conclusion

---

## Step 0 — Profil et langue

- **Langue** → détecter et répondre dans la même langue tout au long
- **Non-expert** : langage simple, feux tricolores 🔴/🟡/✅, définir les acronymes, "quoi faire" clair
- **Juriste/compliance** : références réglementaires précises, concision, analyse extraterritoriale

---

## Step 1 — Analyse de la requête

Identifier les modules à activer :

| Signal | Module |
|--------|--------|
| Nom d'une personne physique | **A** — Screening individuel |
| Secteur / transaction / pays | **B** — Sanctions sectorielles + paiements |
| Bien / technologie / logiciel / composant | **C** — Biens à double usage |
| "US goods", "composant américain", "FDPR", "EAR", "ITAR" | **C2** — Régimes extraterritoriaux US/Chine |
| Pays tiers impliqué dans la transaction | **D** — Risque juridictionnel |

**Déclenchement combiné — exemples :**
- "Gillan Saleh + pétrole + Russie" → A + B + D
- "Machine américaine + extraction pétrolière + Irak + paiement USD" → B + C + C2 + D
- "Logiciel de cryptographie + Iran" → B + C + C2 + D
- "Est-ce que X est sanctionné ?" → A seul

Collecter avant de lancer :
- **A** : nom complet + nationalité/résidence (requis) ; DOB, alias (utile)
- **B** : secteur, nature transaction, pays
- **C/C2** : description du bien/technologie, destination, usage déclaré, origine (US ? chinoise ?)
- **D** : juridictions impliquées, devise de paiement

---

## MODULE A — Screening individuel

### A1 — Socle universel (toujours)
1. **ONU** → `"[nom]" UN Security Council consolidated sanctions list`
2. **UE** → `"[nom]" EU financial sanctions consolidated list`
3. **OpenSanctions** → `"[nom]" site:opensanctions.org` — filet 100+ listes
   - Hit non détecté en socle → identifier source → recherche ciblée officielle
   - Ne jamais citer OpenSanctions comme source autoritative

### A2 — Tier géographique (selon nationalité)

**UE** : socle suffit + DGT France si entité française concernée

**Pays européens autonomes alignés (NO/IS/LI/CH)** : socle + SECO (Suisse). Traiter quasi-UE.

**Pays candidats UE (RS/ME/AL/MK/MD/UA/BA/GE)** : socle. Alignement déclaré, base légale moins solide.

**Turquie** : ONU uniquement sur autonomes. Régime différent des sanctions UE/US Russie.

**UK** : UK Sanctions List (FCDO) → `"[nom]" site:gov.uk UK sanctions list`
NB : depuis 28 janv. 2026, liste unique FCDO — OFSI Consolidated List fusionnée.

**Ressortissant US / lien US** : OFAC SDN + Non-SDN + SSI + GLOMAG → `"[nom]" site:ofac.treas.gov`

**Russe / biélorusse** : UE (Reg. 269/2014) + OFAC + UK Sanctions List + SECO en priorité.

**Iranien** : ONU (snapback 28 sept. 2025, Res. 2231) + OFAC Iran programme + UE (Reg. 267/2012). Vigilance secondary sanctions USD.

**RPDC** : ONU (embargo quasi-total) + OFAC + UE. Vigilance travailleurs RPDC à l'étranger.

**Syrien** : ONU + UE (Reg. 36/2012) + OFAC. Post-déc. 2024 : situation en évolution — vérifier.

**Moyen-Orient** : socle + liste nationale si disponible (Qatar NCTC / UAE ECON / Arabie Saoudite PSS). Voir `references/regimes.md`.

**Africain** : socle suffit généralement. Afrique du Sud : + FIC. Voir `references/regimes.md`.

**CA/AU/JP/SG** : socle + liste propre (Global Affairs Canada / DFAT / METI-MOFA / MAS). Listes ≠ liste UE.

### A3 — Résultat screening
```
═══════════════════════════════════════════
SANCTIONS SCREENING — [NOM]     [DATE]
═══════════════════════════════════════════
🔴 MATCH / 🟡 AMBIGU / ✅ AUCUN MATCH / ⚠️ NON CONCLUANT
Listes vérifiées : [exhaustif]
Match sur : [liste + référence + motifs si applicable]
⚠️ Indicatif. Vérifier sur sources officielles. Pas un avis juridique.
═══════════════════════════════════════════
```
**Si ⚠️ NOM AMBIGU** : demander DOB, nationalité, passeport, alias. Minimum 2 identifiants concordants.

---

## MODULE B — Sanctions sectorielles et systèmes de paiement

### B1 — Sanctions sectorielles par régime

**Russie (UE Reg. 833/2014 + 20 paquets successifs — 20ème paquet : Reg. UE 2026/506, 2026/511, 2026/509 du 23 avr. 2026) :**
- Énergie : interdiction achat/importation pétrole brut et raffiné russe ; restrictions gaz, charbon
- Finance : interdiction accès marchés de capitaux UE pour banques désignées ; restrictions dépôts, prêts
- Transport : interdiction survol UE, accès aux ports et aéroports
- Technologie : interdiction exportation semiconducteurs, électronique avancée, BDU (Russie retirée des autorisations générales EU001-EU008 depuis Reg. 2022/699)
- Luxe : interdiction exportation biens >300€/article
- Services : interdiction conseil juridique, comptabilité, RP, cloud, informatique à entités russes
- Or, acier, bois, chimie, papier : restrictions importation
- Oil price cap G7 : plafonnement 60$/baril pétrole transporté par opérateurs G7
- **Embargo LNG russe (19ème paquet)** : effectif 25 avril 2026 (contrats courts conclus avant le 17 juin 2025) / 1er janvier 2027 (contrats longs >1 an)
- **Extension transaction ban à Mir et SBP** (système de paiement rapide russe) depuis le 25 janvier 2026 (19ème paquet)
- **Interdiction des crypto-actifs russes** : stablecoin A7A5 interdit depuis le 25 novembre 2025 ; extension du transaction ban aux fournisseurs de crypto-assets et services de paiement (Annexe XLV)
- **Services spatiaux commerciaux** (Earth observation, navigation satellite) : interdits à la Russie et au Belarus depuis le 19ème paquet
- **Désignation OFAC Rosneft et Lukoil** (22 oct. 2025) : les deux plus grandes compagnies pétrolières russes désormais sur la SDN List sous EO 14024 — toutes transactions US-nexus interdites ; secondaires sanctions risk pour entités non-américaines ; wind-down GL 131E prolongée jusqu'au 30 mai 2026 (OFAC, 29 avr. 2026) — pour cession Lukoil International GmbH uniquement ; aucun transfert de fonds vers la Russie autorisé
- **20ème paquet UE (23 avr. 2026) — nouvelles mesures clés :**
  - **Transaction ban étendu à 20 banques russes supplémentaires** (effectif 14 mai 2026) — total désormais 70 banques ; + 4 banques au Kirghizstan, Laos et Azerbaïdjan pour facilitation de contournement
  - **Interdiction totale des prestataires de services de crypto-actifs russes et plateformes décentralisées** (effectif 24 mai 2026) — interdiction catégorielle sans désignation individuelle requise ; rouble numérique et stablecoin RUBx interdits
  - **Services de sécurité gérés** (cybersécurité, tests de pénétration, audits) interdits au gouvernement russe et aux entités établies en Russie (effectif 25 mai 2026)
  - **Kirghizstan** : première activation de l'outil anti-contournement Art. 12f — restrictions commerciales étendues en raison du risque systématique de réexportation vers la Russie (+800% importations biens contrôlés, +1 200% réexportations vers Russie)
  - **Services de terminal LNG** interdits aux entités russes ; interdiction de maintenance pour tankers LNG russes et brise-glaces
  - **Shadow fleet** : 46 navires supplémentaires listés (total : 632) ; ports de Mourmansk et Touapse sanctionnés ; terminal de Karimun (Indonésie) — premier port de pays tiers sanctionné
  - **Payment agents** (Arneis, Asia Import Group, GPAgent, Platejka) listés à l'Annexe XLV Partie D (effectif 14 mai 2026)
  - **Mécanisme anti-suit injunction** (Art. 11ca Reg. 833/2014) : protection des opérateurs UE contre les procédures judiciaires russes abusives
  - **Interdictions export** (chimie, caoutchouc, acier, outillage, tracteurs industriels >365 M€) ; **interdictions import** (métaux, chimie, minéraux >530 M€)
- Clause "no re-export to Russia" (Art. 12g Reg. 833/2014, 12ème paquet déc. 2023, effectif mars 2024) : obligation pour exportateurs UE d'insérer clause interdisant réexportation vers Russie dans tous contrats avec partenaires pays tiers — **sauf si le pays tiers est en Annexe VIII** : US, JP, UK, CA, AU, NZ, NO, CH, LI, IS, Corée du Sud

**Iran (ONU + UE Reg. 267/2012 + OFAC) :**
- Pétrole/gaz : embargo UE ; interdictions US quasi-totales
- Finance : restrictions transactions banques iraniennes désignées
- Nucléaire/missiles/IRGC : interdictions élargies ONU + UE + OFAC
- **Snapback ONU (28 sept. 2025)** : réimposition sanctions ONU suite activation mécanisme Res. 2231 par E3 le 28 août 2025

**RPDC (ONU embargo quasi-total) :**
- Charbon, acier, fer, plomb, fruits de mer : interdictions ONU
- Pétrole : plafonnement exportations vers RPDC
- Travailleurs RPDC à l'étranger : interdiction emploi (Res. 2397)

**Syrie** : sanctions économiques larges **levées** (UE 28 mai 2025, US 1er juillet 2025, UK avril 2025). Restent uniquement : sanctions contre membres régime Assad, armes, chimique, affiliés ISIS/Al-Qaeda — vérifier listes individuelles. Voir `references/regimes.md` section 2.4.

**Myanmar / Belarus / Venezuela :** voir `references/regimes.md`

### B2 — Systèmes de paiement comme vecteurs de sanctions

**SWIFT — statut juridique et exclusions :**
SWIFT est incorporé en droit belge → directement soumis au droit UE → obligation de déconnecter les entités désignées par règlement UE.

Chronologie des exclusions russes :
- **12 mars 2022** (Reg. 2022/345) : 7 banques — VTB, Bank Otkritie, Novikombank, Promsvyazbank, Rossiya Bank, Sovcombank, VEB
- **Mai 2022** : + Sberbank, Credit Bank of Moscow, Russian Agricultural Bank
- **2022–2025** : extension progressive à d'autres banques russes et biélorusses
- **Juillet 2025** (Reg. UE 2025/1494) : **évolution majeure** — transformation de l'interdiction SWIFT en **interdiction totale de transaction** pour toutes entités désignées. Plus seulement la messagerie : tout opérateur UE est interdit de toute transaction directe ou indirecte avec les 50+ banques russes désignées, 4 banques biélorusses, 5 opérateurs financiers pays tiers désignés.
- **Juin 2024** : interdiction d'utilisation du SPFS (système russe de messagerie financière alternative) par opérateurs UE

**Risque USD (OFAC / correspondent banking) :**
Tout paiement en USD transitant par le système bancaire américain soumet la transaction à l'OFAC, indépendamment de la nationalité des parties. Les banques correspondantes américaines screenent chaque transaction. Si un élément de la chaîne touche une personne ou entité désignée → blocage.

**Alternatives aux paiements SWIFT/USD vers Russie :**
- SPFS (russe) : interdit aux opérateurs UE depuis juin 2024
- CIPS (chinois — Cross-Border Interbank Payment System) : non interdit en droit UE mais risque d'exposition aux sanctions US secondaires pour entités ayant des liens US

**Paiements en EUR vers zones sanctionnées :**
- Paiements en EUR transitant par des banques UE : soumis au régime UE de sanctions
- Interdiction de fourniture de billets en euros à la Russie (Reg. 2022/345) avec exemptions limitées (usage personnel voyageurs, missions diplomatiques)
- Gel des réserves de la Banque centrale russe déposées dans l'UE (depuis mars 2022) — revenus extraordinaires utilisés pour soutien à l'Ukraine depuis mai 2024

### B3 — Obligations des institutions financières dans le cadre des sanctions

**France / UE — obligation de résultat (pas de moyens) :**
Le gel des avoirs est une **obligation de résultat** — contrairement à la LCB-FT qui repose sur une approche par les risques. L'institution financière ne peut invoquer une démarche proportionnée pour justifier un manquement. Si une personne désignée détient des fonds : gel immédiat, sans appréciation discrétionnaire (principe rappelé par la Commission des sanctions de l'ACPR).

Obligations réglementaires spécifiques (France) :
- **Arrêté du 6 janvier 2021** : dispositif et contrôle interne obligatoires en matière de gel des avoirs
- **Lignes directrices conjointes DGT/ACPR** sur la mise en œuvre des mesures de gel (mise à jour 2024)
- **Orientations ABE 2024/14 et 2024/15** (14 novembre 2024) : politiques internes, procédures et contrôles pour mesures restrictives
- **Directive UE 2024/1226** : harmonisation européenne des incriminations pénales pour violation des sanctions
- **AMLA** (Règlement UE 2024/1620) : nouvelle Autorité européenne AML/CFT — premiers contrôles mi-2025 sur ~40 établissements financiers
- **Directive UE 2024/1640** : à transposer au plus tard le 10 juillet 2027
- Décision ACPR 2024-02 (19 juin 2025) : banque Delubac condamnée pour manquements gel des avoirs
- Sanctions ACPR 2024 : ~5 millions d'euros d'amendes — principaux griefs : défaillances contrôle interne, surveillance transactions, lacunes détection personnes désignées

**UK (OFSI) :**
- Régime de **strict liability** depuis SAMLA 2018 — pénalités civiles même sans connaissance de la violation
- Amende de £160 000 infligée à Bank of Scotland (filiale Lloyds) en janvier 2026 pour violation du régime Russie
- Depuis 28 janv. 2026 : liste unique FCDO — toute référence contractuelle à l'OFSI Consolidated List doit être mise à jour

**US (OFAC) :**
- Pas d'obligation légale générale d'établir un programme de compliance — mais le **OFAC Compliance Framework (2019)** crée une forte pression normative
- Programme de compliance robuste = facteur atténuant en cas de violation ; absence = facteur aggravant
- En pratique : toutes les banques US et leurs correspondants ont des programmes structurés

**Japon (FEFTA) :**
- Depuis **avril 2024** : obligation légale pour institutions financières et opérateurs de services de transfert de fonds d'établir des systèmes internes de conformité aux mesures de gel
- Depuis **décembre 2024** : prior reporting obligatoire pour transferts de technologies clés (15 items : MLCC, fibres de carbone, semiconducteurs...)
- Depuis **octobre 2025** : révision catch-all control — items à haut risque double usage classés "core items"

**Chine :**
- Pas d'obligation de conformité aux sanctions étrangères
- Loi anti-sanctions 2021 + Blocking Statute 2021 peuvent créer des **obligations inverses** pour entités en Chine — devoir de ne pas se conformer aux sanctions étrangères visant des entités chinoises

### B4 — Résultat sectoriel / paiements
```
═══════════════════════════════════════════
ANALYSE SECTORIELLE — [SECTEUR/PAIEMENT] / [PAYS]
═══════════════════════════════════════════
🔴 RESTRICTIONS / ✅ PAS DE RESTRICTION IDENTIFIÉE
Régime applicable : [règlement/résolution]
Nature : [interdiction totale / licence / plafonnement / restriction SWIFT]
Qui est obligé : [entités UE / US persons / institutions financières]
Dérogations : [oui/non — lesquelles]
Risque USD : [oui/non — correspondent banking OFAC]
Risque SWIFT : [banque concernée désignée ? transaction interdite depuis juil. 2025 ?]
═══════════════════════════════════════════
```

---

## MODULE C — Biens à double usage (BDU) — Régime UE

### C1 — Base légale UE
- **Règlement (UE) 2021/821** du 20 mai 2021 (refonte) — en vigueur depuis 9 sept. 2021, remplace Reg. 428/2009
- **Reg. délégué (UE) 2022/699** : Russie retirée des autorisations générales EU001-EU008
- **France** : SBDU (Service des Biens à Double Usage) — DGE, Ministère de l'Économie — plateforme EGIDE
- Mise à jour annuelle de l'Annexe I via règlements délégués de la Commission

### C2 — Les 10 catégories BDU (Annexe I Reg. 2021/821)

Structure de la nomenclature : `[Catégorie][Type][Régime][Numéro]` ex. `3A225`
- **Type** : A=équipement/composants · B=équipement d'essai/production · C=matériaux · D=logiciel · E=technologie

| Cat. | Intitulé | Exemples de codes |
|------|----------|------------------|
| **0** | Nucléaire | `0A001` (réacteurs), `0B001` (équipements enrichissement), `0C001` (matières fissiles) |
| **1** | Matériaux spéciaux | `1C010` (fibres composites), `1C011` (métaux/alliages) |
| **2** | Traitement matériaux | `2B001` (machines-outils CNC), `2B004` (fours haute température) |
| **3** | Électronique | `3A001` (composants électroniques), `3A225` (convertisseurs fréquence), `3E001` (tech. semicond.) |
| **4** | Informatique | `4A001` (ordinateurs haute performance), `4D001` (logiciels) |
| **5** | Télécom & sécurité info | `5A002` (chiffrement), `5D002` (logiciels cryptographiques), `5E002` (tech. chiffrement) |
| **6** | Capteurs et lasers | `6A002` (détecteurs optiques), `6A008` (radars), `6C005` (lasers) |
| **7** | Navigation et avionique | `7A003` (gyroscopes), `7A005` (GPS), `7E004` (tech. aérospatiale) |
| **8** | Marine | `8A001` (submersibles), `8A002` (équipements naval) |
| **9** | Aérospatial et propulsion | `9A004` (lanceurs spatiaux), `9A012` (UAV), `9C110` (propergols) |

> **Important** : pas de lien direct automatique entre code BDU et code douanier (NC/SH). Une table de corrélation NC–BDU est publiée annuellement par l'UE (EUR-Lex).

### C3 — Régimes internationaux de contrôle (base de la liste BDU)

| Régime | Objet | Membres |
|--------|-------|---------|
| **Wassenaar** (1996) | Armes conventionnelles + BDU | 42 États |
| **Groupe Australie** | Précurseurs chimiques et biologiques | 43 États |
| **NSG** | Matières et technologies nucléaires | 48 États |
| **MTCR** | Technologies de missiles et vecteurs | 35 États |

### C4 — Types d'autorisation UE/France

| Type | Référence | Conditions |
|------|-----------|------------|
| Autorisations générales UE | EU001–EU008 | Destinations autorisées — **Russie EXCLUE (Reg. 2022/699)** |
| Autorisation individuelle | SBDU/EGIDE | 1 exportateur, 1 bien, 1 destinataire — max. 2 ans |
| Autorisation globale | SBDU/EGIDE | 1 exportateur, opérations multiples — max. 2 ans |
| Autorisation générale nationale | SBDU | Complémentaire UE |

### C5 — Résultat BDU UE
```
═══════════════════════════════════════════
ANALYSE BDU — [BIEN] / [DESTINATION]
═══════════════════════════════════════════
🔴 LICENCE REQUISE / 🟡 À VÉRIFIER / ✅ PAS DE CONTRÔLE BDU
Classement potentiel : [code BDU]
Catégorie : [0-9 + description]
Régime source : [Wassenaar / NSG / Australie / MTCR]
Autorisation : [générale / individuelle / globale]
Autorité France : SBDU — plateforme EGIDE
Base légale : Reg. (UE) 2021/821, Annexe I
═══════════════════════════════════════════
```

---

## MODULE C2 — Régimes extraterritoriaux de contrôle des exportations

### C2.1 — Droit américain EAR/BIS

**Base légale** : Export Administration Regulations (EAR) — 15 CFR Parts 730-774 — Bureau of Industry and Security (BIS), US Department of Commerce.

**Commerce Control List (CCL)** : liste américaine équivalente à l'Annexe I UE — codifiée en ECCN (Export Control Classification Numbers), format `3A991`, `5E002`, etc.

**Règle de minimis** : si composants américains EAR-controlled représentent plus de **25%** de la valeur du produit final (10% pour destinations sous embargo strict : Iran, RPDC, Cuba, Syrie), le produit entier est soumis à l'EAR même fabriqué hors des US.

**Foreign Direct Product Rule (FDPR)** — 15 CFR § 734.9 : les produits fabriqués à l'étranger sont soumis à l'EAR s'ils sont le "direct product" de technologie ou logiciel américain spécifié, ou s'ils sont produits dans une usine elle-même fabriquée à partir de technologie US. **Portée extraterritoriale massive.**

**Russia/Belarus FDP Rule (depuis févr. 2022)** : extension de la FDPR à toute la Russie et Belarus — tout item produit dans le monde à partir d'outillage ou technologie US est soumis à l'EAR pour exportation vers la Russie/Belarus.

**Listes BIS distinctes de la SDN List OFAC** :
- **Entity List** : entités auxquelles toute exportation d'items EAR-controlled requiert une licence — souvent examinée sous politique de refus. Mention "footnote 3" = Russia-MEU FDP rule s'applique automatiquement à cette entité
- **Denied Persons List** : interdiction totale d'exportation vers ces personnes
- **Unverified List** : entités dont le end-use ne peut être vérifié → due diligence renforcée obligatoire
- **Military End-User (MEU) List** : entités militaires russes et chinoises — restrictions renforcées

**BIS Affiliates Rule (50% Rule BIS) — statut au 19 mai 2026** : BIS a adopté le 29 septembre 2025 une règle étendant les restrictions Entity List aux filiales détenues à 50%+. Cette règle a été **suspendue pour un an** à partir du 10 novembre 2025 dans le cadre des négociations commerciales US-Chine (accord Trump-Xi Busan). La règle sera réactivée le 10 novembre 2026 sauf prolongation. Pendant la suspension : la règle n'est pas opérationnelle — mais BIS recommande de maintenir la capacité d'analyse des chaînes de propriété en prévision de sa réactivation.

**End-use controls** : même si un item n'est pas sur la CCL ou si la destination n'est pas sous embargo, une licence BIS peut être requise si l'usage final est militaire, WMD, ou pour certains utilisateurs finaux désignés.

**BIS Affiliates Rule (règle des 50% BIS) — suspendue :**
- Adoptée le 29 septembre 2025 : extension des restrictions Entity List aux filiales détenues à 50%+ (analogue à la règle des 50% OFAC mais pour les contrôles exports)
- **Suspendue pour un an** depuis le 10 novembre 2025 (accord Trump-Xi — contrepartie de la suspension chinoise des contrôles sur terres rares)
- **Réactivation prévue le 10 novembre 2026** sauf prolongation — maintenir la capacité d'analyse des chaînes de propriété
- Pendant la suspension : la règle des 50% BIS n'est **pas opérationnelle** — mais les obligations Entity List sur les entités nommément listées restent en vigueur

**Semiconducteurs IA / Chine — politique révisée (janvier 2026) :**
- AI Diffusion Rule Biden (janvier 2025) **rescindée** par l'administration Trump
- Nouvelle politique BIS effective **15 janvier 2026** : puces IA sous certains seuils (TPP < 21 000 ; DRAM bandwidth < 6 500 GB/s — niveau H200/MI325X) peuvent désormais être évaluées **au cas par cas** pour exportation vers la Chine, au lieu du refus systématique antérieur
- Conditions : preuve que l'export ne réduit pas la capacité de production disponible pour clients US ; procédures KYC de l'acheteur chinois ; tests tiers indépendants sur le territoire US

**Clause "no re-export to Russia" UE (Art. 12g Reg. 833/2014)** : obligation pour tout exportateur UE d'insérer dans ses contrats avec partenaires de pays tiers une clause interdisant la réexportation vers la Russie — **sauf si le pays tiers est en Annexe VIII** (US, JP, UK, CA, AU, NZ, NO, CH, LI, IS, Corée du Sud). Effectif depuis mars 2024. Déclaration aux autorités nationales compétentes requise pour contrats avec autorités publiques étrangères ou organisations internationales.

### C2.2 — ITAR (International Traffic in Arms Regulations)

**Base légale** : 22 CFR Parts 120-130 — Directorate of Defense Trade Controls (DDTC), US Department of State.

**Distinct de l'EAR** : plus restrictif, vise les articles, services et données techniques de la **US Munitions List (USML)** — catégories I à XXI couvrant armements, munitions, aéronefs militaires, équipements militaires électroniques, missiles, armes chimiques/biologiques, etc.

**Si un composant d'un produit relève de l'ITAR** : aucune licence EAR ne suffit — c'est un régime séparé nécessitant une licence DDTC. Portée extraterritoriale : tout transfert d'articles ITAR ou de données techniques ITAR à un ressortissant étranger (y compris en territoire US) est soumis à l'ITAR.

**Règle "once ITAR, always ITAR"** : un produit incorporant un composant ITAR reste ITAR-controlled même si le composant représente une fraction minime du produit final.

**Pour l'utilisateur français** : si la machine américaine comporte des composants militaires ou à usage militaire potentiel, l'ITAR peut s'appliquer en plus ou en lieu et place de l'EAR → consultation d'un avocat spécialisé indispensable.

### C2.3 — Export Control Law chinoise (ECL)

**Base légale** : Loi sur le contrôle des exportations (Export Control Law — ECL) — entrée en vigueur le 1er décembre 2020. Complétée par le Règlement sur le contrôle des exportations de biens à double usage (2024).

**Portée extraterritoriale** (Article 44 ECL + Article 49 Règlement 2024) : les entités étrangères qui transfèrent hors de Chine des produits contenant des composants à double usage chinois "spécifiques" peuvent être soumises au Règlement 2024. **Mécanisme équivalent à la FDPR américaine** — encore en développement, application sélective.

**Terres rares et semiconducteurs (2025)** : mesures extraterritoriales spécifiques introduites en 2025 sur les terres rares, batteries lithium et matériaux superhard — avec une règle des 50% propre à la Chine pour les entités sur sa Control List.

**Unreliable Entity List (UEL)** : liste chinoise d'entités étrangères ayant pris des mesures discriminatoires contre des entités chinoises — peut entraîner des restrictions d'accès au marché chinois.

**Régime anti-sanctions parallèle** :
- Loi anti-sanctions 2021 (反外国制裁法) : interdit aux entités en Chine de se conformer aux sanctions étrangères unilatérales visant des ressortissants/entités chinoises ; droit d'action en dommages-intérêts
- Blocking Statute 2021 : contre l'application extraterritoriale "abusive" de lois étrangères
- Loi sur les relations étrangères 2023 : codifie et renforce ces mécanismes

**Praticité** : la Control List chinoise et la UEL ne sont pas publiquement accessibles de la même façon que la SDN List OFAC ou la liste UE — opacité plus grande.

### C2.4 — Autres régimes nationaux de contrôle des exportations

**UK** : Export Control Order 2008 + UK Strategic Export Controls Lists — alignement post-Brexit avec Wassenaar/NSG/MTCR/Australie Group ; régime propre distinct de l'UE depuis le 31 déc. 2020. **SEUC (Sanctions End-Use Controls — effectif 13 mai 2026)** : mécanisme complémentaire aux contrôles d'exportation existants — applicable aux biens non soumis aux listes stratégiques mais présentant un risque de détournement vers une destination sanctionnée. Déclenché par notification écrite de l'OTSI. Vérifier systématiquement pour toute exportation UK vers pays tiers à risque de réexportation (Turquie, EAU, Kirghizstan, Chine, Inde...).

**Canada** : Export and Import Permits Act (EIPA) + liste de contrôle des exportations (Export Control List) — alignement Wassenaar + mesures spécifiques Russie/Belarus post-2022.

**Australie** : Defence Export Controls (DEC) + Defence and Strategic Goods List (DSGL) — alignement Wassenaar/NSG/MTCR/Australie Group.

**Japon (FEFTA)** : pas de FDPR propre ; pas de secondary sanctions. Application des contrôles BIS US de fait pour exportateurs japonais de produits contenant des items EAR. Système catch-all révisé en oct. 2025 avec classification "core items". Prior reporting technologies clés depuis déc. 2024.

**Russie** : pas de régime de contrôle des exportations extraterritorial comparable à l'EAR/ECL. En revanche, contre-mesures visant les "États inamicaux" :
- Décrets 95 et 254 (mars/mai 2022) : restrictions transferts de dividendes — paiements uniquement en roubles sur compte de type "C"
- Décret 618 (sept. 2022) : approbation gouvernementale requise pour toute transaction d'un ressortissant d'"État inamical" sur participations dans sociétés russes
- Décret 302 (avril 2023) : autorisation de saisie des actifs russes détenus par personnes d'"États inamicaux" (Rosimushchestvo)

### C2.5 — Questions d'analyse pour Module C2

Dès qu'un bien ou une machine d'origine américaine est mentionné :
1. Le bien est-il listé à la CCL (ECCN) ? → vérifier BIS
2. Le produit final contient-il des composants US EAR-controlled à plus de 25% (ou 10% si destination sous embargo) ? → règle de minimis
3. Le produit a-t-il été fabriqué avec des outils ou technologies US ? → FDPR potentielle
4. Des composants relèvent-ils de la USML (ITAR) ? → régime distinct, plus restrictif
5. La destination est-elle soumise à une FDP Rule étendue (Russie/Belarus) ?
6. La transaction implique-t-elle une entité sur l'Entity List, Denied Persons List ou MEU List BIS ?
7. Le bien contient-il des composants à double usage d'origine chinoise ? → ECL 2024 Art. 49 potentiel
8. Le paiement est-il en USD ? → risque OFAC via correspondent banking

### C2.6 — Résultat Module C2
```
═══════════════════════════════════════════════════════════
ANALYSE RÉGIMES EXTRATERRITORIAUX — [BIEN] / [ORIGINE] / [DESTINATION]
═══════════════════════════════════════════════════════════
EAR/BIS (US) :
  🔴 LICENCE BIS REQUISE / 🟡 À VÉRIFIER / ✅ PAS DE CONTRÔLE
  ECCN potentiel : [code si identifiable]
  Règle de minimis : [applicable ? seuil ?]
  FDPR : [applicable ?]
  Listes BIS : [Entity List / Denied Persons / MEU / Unverified]

ITAR (US) :
  🔴 APPLICABLE — CATÉGORIE USML [X] / ✅ HORS USML
  Si applicable : licence DDTC obligatoire — EAR insuffisant

ECL CHINE :
  🟡 À ÉVALUER si composants chinois / ✅ PAS DE COMPOSANT CHINOIS IDENTIFIÉ

RISQUE USD :
  🔴 PAIEMENT USD → SCREENING OFAC OBLIGATOIRE / ✅ PAS DE PAIEMENT USD

CLAUSE NO RE-EXPORT (UE Art. 12g) :
  🔴 APPLICABLE — pays tiers hors Annexe VIII / ✅ PAYS TIERS EN ANNEXE VIII
═══════════════════════════════════════════════════════════
```

---

## MODULE D — Gestion du risque juridictionnel

> **Principe** : Les États exercent leur pleine souveraineté en matière de politique de sanctions. Un régime différent du régime UE/France n'implique aucun jugement sur la légitimité de la politique de cet État. L'analyse porte uniquement sur les obligations de l'utilisateur au titre de son propre régime juridique.

### D1 — Cartographie par zone (résumé — lire `references/regimes.md` pour détail)

**UE 27** : règlements PESC directement applicables — obligation automatique.

**Autonomes alignés (NO/IS/LI)** : quasi-UE ; Suisse (SECO) : forte convergence, vérification séparée.

**Candidats UE** : alignement déclaré, base légale moins solide — risque résiduel par transaction.

**Turquie** : ONU uniquement ; régime différent sur Russie.

**UK** : fort alignement G7 ; liste FCDO distincte ; strict liability OFSI depuis janv. 2026. **Nouveauté — SEUC (Sanctions End-Use Controls, effectif 13 mai 2026)** : nouveau mécanisme de licence pour exportations vers pays tiers non sanctionnés en cas de risque de détournement notifié par l'OTSI (Office of Trade Sanctions Implementation) — Sanctions (EU Exit) (Miscellaneous Amendments) Regulations 2026 (S.I. 2026/443).

**US** : régime le plus large + extraterritorial (secondary sanctions, USD). EU Blocking Statute Reg. 2018/1100 en principe pour Cuba/Iran. Nouvelles priorités 2026 : focus renforcé sur les **gatekeepers** (avocats, fonds PE, gestionnaires d'actifs) ; cartels mexicains désignés FTO (fév. 2025). **Nouveau — EO 14404 Cuba (1er mai 2026)** : sanctions US étendues (énergie, défense, métaux, mines, services financiers) avec menace de secondary sanctions sur institutions financières étrangères traitant avec des entités cubaines bloquées.

**CA/AU/JP** : fort alignement G7 ; listes distinctes — vérification séparée systématique.

**Singapour** : ONU + terrorisme ; exposition indirecte OFAC via USD.

**EAU** : ONU + terrorisme (ECON) ; régime différent sur Russie ; exposés designations OFAC Iran/Russie.

**Qatar** : liste NCTC terrorisme (la mieux structurée de la région). Pas de sanctions autonomes élargies.

**Arabie Saoudite** : cadre formel ONU (gel automatique CSNU 1267) ; liste PSS peu structurée ; régime différent sur sanctions unilatérales occidentales.

**Afrique du Sud** : seule liste autonome publique sub-saharienne (FIC).

**Reste Afrique** : pas de listes autonomes publiques ; obligation ONU variable ; désignations individuelles via ONU/UE/OFAC uniquement. UA/CEDEAO : régimes régionaux en construction.

**Chine** : ONU sélectif (abstentions Russie 2022) ; loi anti-sanctions 2021 ; régime inverti pour entités en Chine.

**Inde** : ONU ; régime différent sur Russie ; commerce bilatéral Inde-Russie en hausse depuis 2022.

**Russie** : contre-sanctions propres visant "États inamicaux" — contexte inversé pour entités françaises opérant en Russie.

### D2 — Questions risque résiduel

Même si Module A = ✅ et Module B = ✅ :
1. Paiement en USD ? → risque OFAC via correspondent banking même sans lien US direct
2. Entité détenue à 50%+ par une personne désignée ? → règle des 50% OFAC + règle UE contrôle indirect
3. Intermédiaires dans des juridictions à régime différent ? → analyser chaîne transactionnelle complète
4. Secteur lui-même sous sanctions même si contrepartie non désignée individuellement ?
5. Institution financière impliquée est-elle sur la liste des 50+ banques russes sous transaction ban (depuis juil. 2025) ?
6. Bien contient-il des composants US ou chinois déclenchant EAR/ECL ?

---

## Step 4 — Synthèse et qualification juridique croisée

Lire `references/qualification-juridique.md` pour grille complète.

```
═══════════════════════════════════════════════════════════
SYNTHÈSE — ANALYSE COMPLÈTE DE TRANSACTION
═══════════════════════════════════════════════════════════
PERSONNE          : [résultat Module A]
TRANSACTION       : [résultat Module B — sectoriel + SWIFT/USD]
BIEN/TECH UE      : [résultat Module C]
RÉGIMES EXTRAT.   : [résultat Module C2 — EAR/ITAR/FDPR/ECL]
JURIDICTION       : [résultat Module D]

CONCLUSION :
⛔ TRANSACTION NON RÉALISABLE EN L'ÉTAT
⚠️ RÉALISABLE SOUS CONDITIONS : [préciser — licence BIS / SBDU / autorisation DGT...]
✅ AUCUNE RESTRICTION IDENTIFIÉE

OBLIGATIONS IMMÉDIATES : [si applicable]
AUTORITÉS À CONTACTER : [DGT / SBDU / TRACFIN / ACPR / BIS / DDTC]
═══════════════════════════════════════════════════════════
```

---

## Step 5 — Guidance pratique

**Non-expert** : feu tricolore sur chaque dimension + explication "ce que ça veut dire pour vous" + "quoi faire" explicite (contacter le SBDU, un avocat spécialisé, la DGT...). Ne jamais laisser sans prochaine étape.

**Expert (juriste/compliance)** :
- Références réglementaires précises (numéros règlement, articles, CFR)
- Analyse extraterritorialité US (secondary sanctions, FDPR, EU Blocking Statute Reg. 2018/1100)
- Analyse ECL chinoise si composants chinois
- Risque résiduel juridictionnel (correspondent banking USD, chaîne transactionnelle)
- Obligations déclaratives (CMF L. 562-1 et s., pénalités L. 562-5)
- ACPR/AMF si secteur financier ; SBDU si BDU ; DDTC si ITAR

---

## Outils MCP — Intégration automatique

Lorsque des MCP sont disponibles dans la session, les utiliser **systématiquement et en priorité** sur la recherche web générale pour les tâches suivantes. Les MCP donnent accès aux textes consolidés officiels — plus fiables et précis que la recherche web.

### OpenLegi (Légifrance) — utiliser si disponible

Utiliser OpenLegi automatiquement pour toute vérification de droit français dans le cadre de ce skill :

**Cas d'usage obligatoires :**
- Vérifier la version consolidée en vigueur des articles du Code monétaire et financier (CMF) relatifs au gel des avoirs : **L. 562-1 à L. 562-10, R. 562-1 et s.**
- Rechercher les décrets de sanctions nationales autonomes publiés au JORF (décrets du Premier ministre pris en application de L. 562-2 CMF)
- Vérifier les arrêtés applicables aux institutions financières en matière de gel (ex. arrêté du 6 janvier 2021)
- Consulter la jurisprudence de la Commission des sanctions de l'ACPR sur le gel des avoirs
- Vérifier toute référence législative ou réglementaire française citée dans l'analyse

**Requêtes types OpenLegi :**
- `CMF L. 562-1` → texte consolidé de l'article
- `gel des avoirs décret [année]` → décrets de sanctions nationaux JORF
- `arrêté 6 janvier 2021 gel avoirs` → texte applicable aux organismes financiers

**Important** : si OpenLegi n'est pas disponible dans la session, utiliser `web_fetch` sur legifrance.gouv.fr en ciblant l'URL de l'article concerné.

### EUR-Lex — via web_fetch (pas de MCP dédié)

Il n'existe pas de MCP EUR-Lex natif — utiliser `web_fetch` directement sur EUR-Lex :

**Cas d'usage obligatoires :**
- Vérifier la version consolidée d'un règlement UE cité (ex. Reg. 833/2014 et ses 18+ modifications)
- Consulter l'Annexe I du Reg. (UE) 2021/821 (liste BDU) dans sa version actualisée
- Vérifier l'Annexe VIII du Reg. 833/2014 (pays exemptés clause no re-export)
- Vérifier l'Annexe VII du Reg. 833/2014 (biens soumis à la clause no re-export)
- Confirmer la date d'entrée en vigueur d'un paquet de sanctions

**URLs EUR-Lex directes — web_fetch :**
- Reg. 833/2014 consolidé : `https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02014R0833-20250224`
- Reg. 269/2014 consolidé : `https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02014R0269-20250224`
- Reg. 2021/821 consolidé (BDU) : `https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02021R0821-20241108`
- Liste consolidée sanctions financières UE (FSF) : `https://webgate.ec.europa.eu/fsd/fsf`

**Règle** : toujours utiliser la version consolidée la plus récente — ne pas citer un règlement de base sans vérifier ses modifications successives via EUR-Lex.

### Priorisation des outils

| Tâche | Outil prioritaire | Fallback |
|-------|------------------|---------|
| Textes français CMF / JORF / décrets | **OpenLegi MCP** | web_fetch legifrance.gouv.fr |
| Règlements UE consolidés | web_fetch EUR-Lex (CELEX) | web_search + vérification |
| Listes de désignations individuelles | web_search sur sources officielles | OpenSanctions |
| Jurisprudence ACPR | **OpenLegi MCP** | web_search site:acpr.banque-france.fr |
| BIS Entity List / OFAC SDN | web_search site:bis.doc.gov / site:ofac.treas.gov | opensanctions.org |

---

## Disclaimer

**FR** : *Orientation juridique indicative uniquement. Dernière mise à jour : 19 mai 2026 (20ème paquet UE, SEUC UK, EO 14404 Cuba). Résultats à vérifier sur sources officielles avant toute décision. Ne constitue pas un avis juridique (loi du 31 déc. 1971). En cas de doute : avocat spécialisé sanctions et contrôle des exportations / DGT (gel des avoirs) / SBDU (biens à double usage) / BIS (EAR) / DDTC (ITAR).*

**EN** : *Indicative legal guidance only. Verify against official sources before any decision. Not legal advice. When in doubt: sanctions and export control specialist / DGT (asset freeze) / SBDU (dual-use) / BIS (EAR) / DDTC (ITAR).*

---

## Fichiers de référence

- `references/sources-officielles.md` — URLs officielles + stratégies de recherche par juridiction
- `references/regimes.md` — Cartographie complète régimes par zone + matrice risque juridictionnel
- `references/qualification-juridique.md` — Grille qualification croisée + obligations déclaratives + sanctions pénales
