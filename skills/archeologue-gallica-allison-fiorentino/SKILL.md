---
name: archeologue-gallica
description: >-
  Archéologie des sources juridiques anciennes via Gallica (BNF, API stables,
  sans clé) : débats parlementaires du JO depuis 1871 (genèse des lois de la
  IIIe République), notes d'arrêt et doctrine d'origine dans les recueils
  Sirey et Dalloz, Bulletins civil et criminel anciens, Recueil Lebon, JO Lois
  et décrets 1881-2015, thèses et traités du XIXe-début XXe, Gazette des
  tribunaux, Bulletin de l'Inspection du travail. Déclencher dès que
  l'utilisateur cherche l'origine historique d'un texte, d'un concept ou d'une
  jurisprudence : « débats de la loi de 1884 », « note de Josserand », « que
  disait la doctrine en 1900 », « première apparition de la notion de… »,
  « généalogie / histoire de l'article… », « arrêt ancien », « thèse
  d'avant-guerre », « Gallica », « BNF », ou toute recherche juridique
  antérieure aux bases modernes (Légifrance ne remonte pas avant l'époque
  contemporaine, Judilibre non plus). Déclencher aussi en COMPLÉMENT de
  travaux-preparatoires quand la loi étudiée est antérieure à 1958.
---

# L'archéologue Gallica

Exhumer les sources juridiques anciennes numérisées par la BNF : débats
parlementaires in extenso, recueils de jurisprudence et de doctrine,
textes officiels, thèses et traités — avec extraits océrisés, localisation
à la page et lien vers l'image du document pour vérification.

## Outillage

Tout passe par `scripts/gallica_client.py` (stdlib pure, sortie JSON,
relances automatiques). Lire son en-tête pour la syntaxe complète.

Deux familles d'identifiants ark, à ne jamais confondre :
- `cb…` = un **titre de périodique** (le JO Débats, le Recueil Sirey…) →
  commandes `annees`, `fascicules`, `feuilleter` ;
- `bpt…` = un **document** (un fascicule daté, une thèse) → commandes
  `chercher`, `texte`, `pages`, `notice`.

Le catalogue des périodiques juridiques déjà résolus est dans
`references/periodiques.md` — le consulter AVANT toute commande
`periodique`, la plupart des grands titres y figurent déjà.

## Réseau

Domaines requis : `gallica.bnf.fr` (et `api.bnf.fr`), déjà prévus dans la
configuration réseau habituelle de l'utilisateur. Le script envoie un
User-Agent de navigateur (Gallica renvoie 403 aux robots) et retente
4 fois en cas d'erreur DNS transitoire du proxy. Si le blocage persiste,
transmettre le message `fix` du script (ajout du domaine dans
Paramètres > Capacités > Domaines autorisés).

## Workflows types

### 1. Généalogie parlementaire d'une loi ancienne (le cas roi)

Exemple : « retrouve les débats de la loi Waldeck-Rousseau de 1884 ».

1. Identifier la fenêtre temporelle (date de promulgation, connue ou via
   une recherche web rapide).
2. `feuilleter cb328020951 "expression clé" --de 1883 --a 1884` (Chambre)
   puis la même chose sur `cb34363182v` (Sénat). Choisir une expression
   discriminante du texte (« syndicats professionnels », pas « loi »).
3. Sur les fascicules retournés (triés par date), `chercher <bpt…>
   "expression"` pour localiser les vues et lire les extraits.
4. `texte <bpt…> --vue N` (ou `N-M`, max 20) pour lire les pages entières :
   interventions nominatives, amendements, votes.
5. `pages <bpt…>` pour convertir la vue en **numéro de page imprimé du JO**
   (pagination continue de l'année) — indispensable à la citation.

### 2. Doctrine d'origine d'un concept

Exemple : « que disait la doctrine sur l'abus de droit vers 1900 ? »

1. `recherche "abus de droit" --champ titre --type monographie --de 1890
   --a 1939` → thèses et traités (Josserand 1905, Desserteaux 1906…).
2. `recherche "abus de droit" --de 1890 --a 1914 --tri date` en plein
   texte pour la première pénétration de l'expression dans les sources.
3. Pour les notes d'arrêt : `feuilleter` sur le Sirey (cb34363188x) ou le
   Dalloz (cb344196192) avec le nom des parties ou l'expression.
4. Lire via `chercher` puis `texte`.

### 3. Jurisprudence ancienne

Bulletin civil (cb34488540t), Bulletin criminel (cb34508686x), Lebon
(cb343630608) : `annees` pour vérifier la couverture réelle, `fascicules
<ark> <année>` pour l'année de l'arrêt, puis `chercher` avec le nom des
parties ou les mots du dispositif.

### 4. État d'un texte officiel ancien

JO Lois et décrets (cb34378481r, 1881-2015) : retrouver la publication
originale d'une loi ou d'un décret à sa date, y compris pour des textes
absents de Légifrance. Articulation naturelle avec la skill
machine-a-remonter-le-droit quand celle-ci bute sur une version antérieure
aux fonds Légifrance.

## Règles de restitution

1. **L'OCR ment parfois.** Le texte océrisé du XIXe contient des coquilles
   (« lIberté », « qa.' »). Avant toute citation littérale : afficher le
   lien `image` (IIIF) et prévenir que la vérification sur l'image
   s'impose. Corriger silencieusement les coquilles OCR évidentes dans les
   citations courtes, en le signalant (« orthographe restituée »).
2. **Citer à l'ancienne.** Pour un débat : JO Déb. parl., Chambre des
   députés, séance du 13 mars 1884, p. 737 (page imprimée via `pages`,
   pas le numéro de vue). Pour un recueil : S. 1905.1.… / D. 1902.2.…
   selon la structure visible sur la page. Toujours joindre l'URL ark
   pérenne (`https://gallica.bnf.fr/ark:/12148/…`).
3. **Couverture réelle ≠ couverture cataloguée.** Vérifier avec `annees`
   avant d'affirmer qu'une année est disponible ; une absence dans Gallica
   se dit « non numérisé », jamais « n'existe pas ».
4. **Droits.** Documents anciens : domaine public, reproduction libre.
   Si la notice porte « restricted use », le signaler. Pour des documents
   récents (RTD civ. après-guerre…), l'accès Gallica peut être restreint :
   ne pas contourner, renvoyer vers les bases sous licence.
5. **Ne pas noyer.** `feuilleter` peut renvoyer des dizaines de
   fascicules : restituer une frise datée resserrée sur les séances
   décisives (discussion générale, articles, adoption), pas la liste
   brute.

## En cas d'erreur

- JSON `{"error": …, "fix": …}` du script : appliquer le `fix`.
- `feuilleter` renvoie 0 fascicule : élargir la fenêtre de dates, varier
  l'expression (orthographe d'époque ! « ouvriers » plutôt que
  « salariés », graphies anciennes), ou tenter `recherche` sans arkPress.
- `chercher` renvoie 0 sur un fascicule pourtant remonté par
  `feuilleter` : l'index SRU et ContentSearch divergent parfois ;
  essayer un mot unique de l'expression, puis `texte` sur les premières
  vues.
- OCR illisible (colonnes mélangées) : renvoyer l'utilisateur à l'image
  IIIF, qui reste la source de vérité.
