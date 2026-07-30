---
name: "sujet-crfpa-allison-fiorentino"
description: ">Ce skill génère des sujets d'entraînement pour les deux épreuves écrites de consultation du CRFPA : l'épreuve de droit des obligations (tronc commun) et l'épreuve de spécialité (civil, affaires, social, pénal, administratif, international et européen, fiscal). Chaque sujet est accompagné d'une grille de notation détaillée sur 20 points. Vous ciblez un thème précis, ou vous laissez le skill procéder à un tirage au sort couvrant l'ensemble du programme. Connexion aux MCP OpenLegi et GoodLegal requise : toutes les références d'articles et d'arrêts sont vérifiées sur les sources officielles, sans citation inventée"
metadata:
  author: "Allison Fiorentino"
  license: "agpl-3.0"
  version: "2026-06-12"
---

# Générateur de Sujets CRFPA – Droit des obligations & matières de spécialité

Cette skill génère des sujets d'entraînement au format officiel des deux épreuves écrites de 3 heures (coefficient 2) de l'examen d'accès au CRFPA, accompagnés d'une grille de notation rigoureuse conforme au modèle de la Commission nationale. Livraison en fichier `.docx` unique (ou deux fichiers sujet/grille séparés sur demande).

**Épreuves couvertes** :
1. **Droit des obligations** — épreuve commune à tous les candidats (le plus large public)
2. **Épreuve de spécialité** — au choix : droit civil, droit des affaires, droit social, droit pénal, droit administratif, droit international et européen, droit fiscal

Depuis la session 2026, le CNB précise que ces épreuves consistent en « une ou plusieurs consultations » : employer le vocabulaire « consultation(s) / cas pratique(s) ». Hors champ de cette skill : la note de synthèse (5 h), l'épreuve de procédure (2 h) et le grand oral.

## Étape 0 — Identifier l'épreuve, la matière et lire les références

1. Identifier l'épreuve : droit des obligations (par défaut si l'utilisateur dit « le tronc commun », « l'épreuve commune ») ou une matière de spécialité. Si ambigu (« un sujet sur les contrats » : obligations ? civil/contrats spéciaux ?), demander.
2. Lire **obligatoirement** :
   - `references/format_officiel.md` — invariants du format CRFPA, cadre réglementaire, gabarit de la grille de notation
   - `references/matieres/<matiere>.md` — la fiche de l'épreuve : structure type observée dans les annales, barème, documents autorisés, arborescence de révision, sources, pièges

| Épreuve / matière | Fichier |
|---|---|
| **Droit des obligations (épreuve commune)** | `references/matieres/droit_des_obligations.md` |
| Droit civil | `references/matieres/droit_civil.md` |
| Droit des affaires | `references/matieres/droit_des_affaires.md` |
| Droit social | `references/matieres/droit_social.md` |
| Droit pénal | `references/matieres/droit_penal.md` |
| Droit administratif | `references/matieres/droit_administratif.md` |
| Droit international et européen | `references/matieres/droit_international_europeen.md` |
| Droit fiscal | `references/matieres/droit_fiscal.md` |

3. **Mise à jour annuelle** : le cadre est l'arrêté du 17 octobre 2016 modifié, complété chaque année par les communications de la Commission nationale (hébergées par le CNB). Si le sujet est destiné à la session en cours ou à venir, faire une recherche web rapide (« CRFPA [année] commission nationale programme documents autorisés ») pour vérifier les précisions de programme et de documents autorisés de l'année (ex. 2026 : fonds de commerce incluant vente, nantissement, location-gérance et bail commercial en affaires ; TVA sur situations antérieures au 1er septembre 2026 en fiscal ; CESEDA hors contentieux en administratif). Intégrer ces précisions au sujet.

Si l'utilisateur fournit un sujet existant et ne veut que la grille/corrigé : sauter aux étapes 3 puis 5.

## Architecture commune — Ce que le format exige

Invariants des deux épreuves de 3 heures (détail dans `format_officiel.md`) :

1. **Page de garde au format officiel, avec mentions de non-officialité obligatoires** (titre « ENTRAÎNEMENT À L'EXAMEN D'ACCÈS AU CRFPA », mention « sujet original d'entraînement… document non officiel » — règles dans `format_officiel.md` § 0 bis) : session, matière, durée, coefficient, documents autorisés (formule générique réglementaire pour le droit des obligations ; liste de codes spécifique pour chaque spécialité — voir fiches). Pour un sujet d'entraînement, omettre la logistique de salle d'examen (complétude du sujet, décompte des pages, sanction du zéro) — règle détaillée dans `format_officiel.md`.
2. **Consultations narratives** : prose continue, faits juridiquement pertinents noyés dans le récit, dates/montants/délais précis et opérants. Le candidat est en position de conseil (« Mme X vous soumet les questions suivantes », « Renseignez-le »).
3. **Barème affiché** entre parenthèses à la fin de chaque cas ou question — y compris pour les sous-questions au sein d'un même cas (modèle droit des obligations 2021 : I = 8 + 3 + 4 points, II = 5 points). Total impératif : **20 points**.
4. **Ancrage jurisprudentiel récent** : la plupart des sous-problèmes transposent un arrêt de moins de 2 ans — c'est la signature du CRFPA.
5. **Gradation** : points accessibles, points techniques, et au moins un point discuté exigeant une argumentation contradictoire.

## Processus de génération

### Étape 1 — Cadrage

Recueillir ou inférer : l'épreuve et la matière, les sous-thèmes souhaités — l'utilisateur peut viser n'importe quelle entrée de l'**arborescence de révision** de la fiche matière (ex. « un sujet d'obligations centré sur les restitutions et la cession de créance ») —, la session fictive, le niveau de difficulté éventuel, le format de livraison.

#### Variation des thèmes (OBLIGATOIRE si l'utilisateur n'impose pas de thèmes)

Sans consigne thématique, ne JAMAIS choisir les thèmes « au jugé » : le choix spontané gravite vers les thèmes vedettes (imprévision, résolution, vices cachés, faute grave…) et vers ceux dont la jurisprudence récente est la plus facile à vérifier, ce qui appauvrit la couverture du programme. Appliquer à la place le protocole suivant :

1. **Tirage au sort outillé** : extraire les entrées de l'arborescence de révision de la fiche matière, puis effectuer un tirage aléatoire réel en Python (bash), avec une contrainte de couverture : chaque cas/question du sujet relève d'un **bloc majeur différent** du programme (ex. en obligations : un tirage dans « contrat », un dans « responsabilité extracontractuelle », un dans « régime général » ou « preuves » ; en social : individuel / collectif / protection sociale). Exemple :
   `python3 -c "import random; blocs={'contrat':[...], 'resp':[...], 'regime':[...], 'preuve':[...]}; [print(b, '->', random.choice(t)) for b,t in blocs.items()]"`
   Tirer un thème de plus que nécessaire par bloc pour disposer d'une solution de repli (cf. règle 3).
2. **Quota hors vedettes** : au moins un sous-problème du sujet doit porter sur un thème « de second rideau » rarement traité (quasi-contrats, preuve et signature électronique, modalités de l'obligation, restitutions, porte-fort, novation/délégation… — et leurs équivalents dans les autres matières). Les annales réelles le font systématiquement (Dailly et signature électronique en 2021).
3. **La vérifiabilité ne gouverne pas le choix** : si la recherche (étape 3) ne fournit pas d'arrêt récent vérifié sur un thème tiré, NE PAS remplacer le thème par un thème vedette ; utiliser d'abord le thème de repli tiré au même bloc, ou construire le point sur le texte et la jurisprudence classique consolidée (un point de pur texte est légitime dans un sujet réel). Le remplacement d'un thème tiré doit rester l'exception et être signalé à l'utilisateur.
4. **Anti-répétition inter-sessions** : demander à l'utilisateur, dans la question de cadrage, s'il y a des thèmes déjà traités à exclure (le skill n'a pas de mémoire entre conversations) ; exclure du tirage les thèmes listés. Si l'outil de recherche de conversations passées est disponible et que l'utilisateur évoque des sujets antérieurs, le consulter pour reconstituer la liste d'exclusion.

Variante « fil de l'actualité » (sur demande ou en alternance) : au lieu du tirage, partir d'un panorama de la jurisprudence des 12-18 derniers mois dans la matière (recherche outillée), et construire le sujet sur 2-3 décisions marquantes — ce mode varie naturellement avec le temps, mais ne doit pas devenir exclusif sous peine de réintroduire le biais de vérifiabilité.

Dans tous les cas, annoncer à l'utilisateur les thèmes retenus (tirés ou choisis) AVANT la rédaction complète, pour validation rapide.

### Étape 2 — Architecture du sujet

Plan AVANT rédaction : découpage en cas/questions conforme à la structure type de l'épreuve (fiche), répartition des points (somme = 20, sous-barèmes affichés), pour chaque sous-problème la question de droit + l'arrêt-matrice pressenti, couverture du programme exigée, cohérence narrative (client unique reliant les cas en obligations ; entreprise unique en social ; cas indépendants en civil/affaires…).

### Étape 3 — Recherche et vérification des sources (OBLIGATOIRE)

**Règle cardinale : ne JAMAIS inventer ni citer de mémoire une référence.** Chaque article et chaque décision cités dans la grille doivent être vérifiés pendant la session via les outils. Mieux vaut 4 arrêts vérifiés que 8 dont 3 douteux.

**A. Documents fournis** (`/mnt/user-data/uploads/`) : prioritaires pour orienter, mais leurs références sont quand même vérifiées.

**B. OpenLegi** (prioritaire, droit français) :
- `rechercher_code` / `rechercher_dans_texte_legal` : numéro exact et **version en vigueur** de chaque article (vigilance réformes : obligations 2016/2018, sûretés 2021, et conflits de lois dans le temps si les faits du cas sont datés)
- `rechercher_jurisprudence_judiciaire` (Cass.), `rechercher_jurisprudence_administrative` (CE/CAA), `rechercher_decisions_constitutionnelles` (QPC)
- `get_decision_judiciaire` / `get_decision_administrative` : lire le texte intégral d'un arrêt AVANT de le transposer — jamais sur la foi d'un résumé

**C. GoodLegal** : `case_search`, `legislation_search`, `article_citation_search` en croisement ; `eu_caselaw_search` + `eu_retrieve` (CJUE, indispensable en international/européen) ; `web_search` pour la CEDH et les décisions très récentes.

**D. Web search standard** en dernier recours ; si la confirmation échoue, **abandonner la référence** et restructurer le point.

Pour chaque décision retenue : juridiction/formation, date exacte, n° de pourvoi/requête/affaire, solution précise. Formats de citation par contentieux dans `format_officiel.md` et les fiches.

### Étape 4 — Rédiger le sujet

Suivre le gabarit de l'épreuve (fiche matière) et les invariants :
- **Style** : prose narrative ; détails concrets (noms variés, lieux, dates, chiffres) ; questions fermes en fin de bloc, formulées comme des demandes de consultation.
- **Écriture sans marqueurs IA** (sujet ET grille) : aucun tiret cadratin ou demi-cadratin en incise (préférer virgule, parenthèse, deux-points ou scinder la phrase ; seuls les tirets structurels du format officiel sont conservés : « I – », « Question n° X – Y points ») ; aucun gras dans le corps du texte ; pas de formules méta (« et c'est le point attendu ») ni de rythmes ternaires systématiques. Si la skill detecteur-tics-ia est disponible, l'appliquer en relecture finale du sujet et de la grille avant production du docx.
- **Transposition des arrêts** : changer noms, lieux, secteurs, chiffres ; conserver les faits qui déclenchent la règle ; ne jamais recopier l'exposé des faits d'une décision.
- **Clauses et annexes** : reproduire in extenso une clause quand son interprétation est l'objet de la question (modèle 2021 : clause de signature électronique, mentions du bordereau Dailly citées dans l'énoncé) ; annexer après « xxxx » les textes absents des documents autorisés (systématique en administratif), dans leur version exacte vérifiée.
- **Documents autorisés** : reproduire la formule/liste officielle de l'épreuve sur la page de garde.

### Étape 5 — Rédiger la grille de notation

Modèle de la Commission nationale, gabarit complet dans `format_officiel.md`. Exigences non négociables : en-tête d'entraînement avec mention de non-officialité (jamais la Commission nationale en émetteur, pas de bloc réglementaire de l'art. 51-1 — voir `format_officiel.md` § 0 bis) + « qualité rédactionnelle (retrait maximum de 2 points) » + double correction recommandée ; « Question n° X – Y points » puis sous-problèmes pondérés (sommes exactes, total 20) ; **prose continue** (jamais de puces) : qualification → texte exact → jurisprudence (date, n° de pourvoi, solution citée avec précision, identification transparente de l'arrêt-matrice) → application (« En l'espèce… ») → solution nuancée ; **raisonnement par élimination** pour les points discutés (« Plusieurs solutions pouvaient être envisagées… Néanmoins… ») ; marge d'appréciation signalée pour les raisonnements alternatifs admissibles du candidat ; **aucune référence non vérifiée**.

### Étape 6 — Produire le ou les documents Word

Consulter la skill docx (`/mnt/skills/public/docx/SKILL.md`). Par défaut un fichier unique en deux parties (saut de page) : SUJET puis GRILLE DE NOTATION ; deux fichiers séparés si distribution à des candidats. Times New Roman/Calibri 11-12, interligne 1,15-1,5, marges 2,5 cm, références au fil du texte, pagination « Page : x/y » accompagnée en pied de page de la mention « Sujet d'entraînement original — document non officiel ». Nommage : `sujet_crfpa_<epreuve>_<theme_ou_session>.docx` dans `/mnt/user-data/outputs/`.

### Étape 7 — Validation qualité (checklist)

**Sujet :**
- [ ] Page de garde conforme, documents autorisés exacts de l'épreuve (formule générique en obligations, liste spécifique en spécialité)
- [ ] Mentions de non-officialité présentes : page de garde, en-tête de grille, pied de page de chaque page (jamais supprimables)
- [ ] Structure et barème conformes à la fiche, sous-barèmes affichés, total = 20
- [ ] Si thèmes non imposés : protocole de variation appliqué (tirage Python tracé dans la session, blocs majeurs distincts, au moins un thème hors vedettes, exclusions de l'utilisateur respectées)
- [ ] Couverture du programme / des sous-thèmes demandés
- [ ] Faits suffisants et seulement suffisants ; dates, délais, chiffres cohérents (vérifier les computations)
- [ ] Annexes présentes si nécessaires

**Grille :**
- [ ] Sous-problèmes pondérés, sommes exactes
- [ ] 100 % des arrêts et articles vérifiés pendant la session (versions en vigueur à la date fictive)
- [ ] Raisonnement complet par point ; alternatives envisagées et écartées pour les points discutés
- [ ] Prose continue, ton du corrigé officiel, aucun tiret cadratin/demi-cadratin en incise ni autre marqueur IA

**Cohérence :**
- [ ] La grille répond exactement aux questions du sujet ; niveau M1/M2-CRFPA
- [ ] En fiscal : calculs refaits en Python avant inscription dans la grille

## Références

- `references/format_officiel.md` — cadre réglementaire (arrêté du 17 oct. 2016 modifié, communications CNB), invariants du format, pages de garde, gabarit complet de la grille. **À lire à chaque utilisation.**
- `references/matieres/*.md` — une fiche par épreuve : structure type issue des annales, documents autorisés, arborescence de révision (programme officiel décliné en sous-thèmes générables), sources et outils, pièges. **Lire uniquement la fiche de l'épreuve demandée.**

## Exemples d'utilisation

> « Un sujet blanc de droit des obligations sur l'inexécution contractuelle et la responsabilité du fait des choses, avec corrigé. »

1. Lire `format_officiel.md` + `matieres/droit_des_obligations.md` ; 2. OpenLegi : jurisprudence récente (chambres civiles/commerciale) sur ces sous-thèmes, textes intégraux des arrêts retenus ; 3. Architecture : client unique, cas I contractuel à sous-questions barémées (~15 pts), cas II délictuel (~5 pts) ; 4-7. Rédiger sujet puis grille vérifiée, produire le docx, checklist, livrer.

> « Génère une consultation CRFPA droit fiscal sur la TVA et les droits de mutation, session 2026. »

Vérifier d'abord par recherche web les précisions CNB 2026 (TVA : situations antérieures au 1er septembre 2026 ; transmission du patrimoine incluse), puis dérouler le processus avec calculs vérifiés en Python.
