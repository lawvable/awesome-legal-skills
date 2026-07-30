---
name: recherche-doctrine
description: "Recherche académique dans les bases de données de doctrine juridique française, européenne et internationale. Utiliser cette skill lorsque l'utilisateur demande de rechercher des articles de doctrine, des thèses, des ouvrages académiques, ou des travaux universitaires en droit — y compris en droit comparé. Sources principales : ISIDORE (agrégateur SHS du CNRS incluant Cairn.info, Persée, OpenEdition), HAL (archive ouverte française), OpenAlex (base ouverte mondiale 250M+ travaux), Semantic Scholar, CrossRef, Persée (OAI direct), et CORE. Couvre la doctrine juridique francophone ET internationale avec workflow bilingue intégré pour le droit comparé. Déclencher aussi pour : bibliographie commentée, état de l'art, revue de littérature juridique, recherche d'auteur, vérification de citation, analyse bibliométrique."
---

# Recherche de Doctrine Juridique — v2 (Droit français & Comparé)

Skill de recherche académique multi-sources pour juristes, chercheurs et doctorants. Conçue pour la doctrine française ET le droit comparé (recherche bilingue FR/EN intégrée).

## Architecture des Sources

### Tier 1 — Sources Francophones (prioritaires)

| Source | Couverture | Accès | Usage principal |
|--------|-----------|-------|----------------|
| **ISIDORE** (CNRS) | 5M+ docs SHS, agrège HAL/Cairn/Persée/OpenEdition | API ouverte | Recherche francophone principale |
| **HAL** | Archive ouverte FR, textes intégraux | API ouverte | Compléments ciblés, recherche par auteur/labo |
| **Persée OAI** | Collections rétrospectives, revues juridiques historiques | OAI-PMH | Doctrine classique, collections anciennes |

### Tier 2 — Sources Internationales (droit comparé)

| Source | Couverture | Accès | Usage principal |
|--------|-----------|-------|----------------|
| **OpenAlex** | 250M+ travaux, open access mondial | API ouverte | Recherche internationale, bibliométrie, citations |
| **Semantic Scholar** | 200M+ articles, IA sémantique | API (1 req/s sans clé) | Doctrine anglophone, articles influents |
| **CrossRef** | 150M+ DOI, métadonnées éditoriales | API ouverte | Vérification citations, métadonnées de qualité |
| **CORE** | Plus grand agrégateur OA mondial | API (clé recommandée) | Complément open access |

## RÈGLE CRITIQUE : Intégrité des Métadonnées Bibliographiques

**NE JAMAIS INVENTER, DEVINER OU EXTRAPOLER** les informations bibliographiques suivantes :
- Numéro de volume / tome
- Numéro de la revue / livraison
- Numéros de pages (première et dernière page)
- Date précise (mois, jour) — ne rapporter que ce que l'API retourne
- Numéro de DOI

**Principe fondamental** : Si une API ne retourne pas un champ (volume, numéro, pages), ne PAS l'inclure dans la référence. Une référence incomplète mais exacte vaut infiniment mieux qu'une référence complète mais fausse.

**Sources de fiabilité pour les métadonnées éditoriales** (par ordre) :
1. **CrossRef** : seule source fiable pour volume/numéro/pages (données fournies par les éditeurs)
2. **DOI** : si un DOI est disponible, TOUJOURS résoudre via CrossRef pour obtenir les métadonnées complètes
3. **HAL / ISIDORE / OpenAlex** : fiables pour titre, auteurs, année, revue — mais souvent SANS volume/numéro/pages

**Workflow obligatoire de vérification** :
- Après chaque recherche ISIDORE/HAL/OpenAlex, si des DOI sont présents dans les résultats, résoudre les DOI via CrossRef (`https://api.crossref.org/works/DOI`) pour récupérer volume, numéro et pages
- Si aucun DOI n'est disponible et que volume/numéro/pages sont absents, l'indiquer explicitement : `[vol./n°/p. non disponibles — vérifier sur la source]`
- Ne JAMAIS reconstituer un numéro de page à partir d'un DOI (ex: ne pas déduire "p. 45" de `rdli.095.0045`)

## Workflow de Recherche

### Principe directeur

Toujours adapter la stratégie au type de recherche demandée :

- **Recherche française pure** → ISIDORE d'abord, HAL en complément
- **Droit comparé** → Recherche parallèle FR (ISIDORE) + EN (OpenAlex/Semantic Scholar)
- **Recherche d'auteur** → HAL (auteurs FR) + OpenAlex (auteurs internationaux)
- **Vérification bibliographique** → CrossRef en priorité (données éditeurs)
- **Doctrine historique** → Persée OAI pour les collections rétrospectives
- **État de l'art / revue de littérature** → Toutes sources, synthèse comparative

### Étape 1 : Analyse de la requête

Avant toute recherche, identifier :
1. **Langue/juridiction cible** : droit français seul ? comparé ? international ?
2. **Période** : doctrine récente (5 ans) ? historique ? sans limite ?
3. **Type de document** : articles ? thèses ? tout type ?
4. **Profondeur souhaitée** : résultats rapides (5-10) ou exhaustif (50+) ?

### Étape 2 : Recherche francophone (ISIDORE + HAL)

**TOUJOURS commencer par ISIDORE** — il agrège la majorité des sources francophones.

```bash
# Recherche de base ISIDORE
curl "https://api.isidore.science/resource/search?q=TERMES_FR&output=json&replies=20"

# Avec filtres juridiques
curl "https://api.isidore.science/resource/search?q=TERMES_FR&type=http://isidore.science/ontology%23article&discipline=http://purl.org/dc/terms/subject/law&output=json&replies=20&sort=date"
```

Si résultats insuffisants ou recherche par auteur/institution, compléter avec HAL :

```bash
curl "https://api.archives-ouvertes.fr/search/?q=TERMES_FR&fq=domain_s:shs.droit&fl=halId_s,title_s,authFullName_s,abstract_s,publicationDateY_i,uri_s,doiId_s,journalTitle_s,volume_s,issue_s,page_s,fileMain_s&wt=json&rows=20&sort=publicationDateY_i%20desc"
```

> Voir `references/hal_api.md` et `references/isidore_api.md` pour la documentation complète des paramètres.

### Étape 3 : Recherche internationale (si droit comparé ou élargissement)

**OpenAlex** (recommandé en priorité pour l'international — meilleure couverture juridique que Semantic Scholar) :

```bash
# Recherche avec filtre juridique
curl "https://api.openalex.org/works?search=TERMES_EN&filter=topics.domain.id:https://openalex.org/domains/2,publication_year:2020-2025&sort=relevance_score:desc&per_page=20"

# Recherche par concept juridique spécifique
curl "https://api.openalex.org/works?search=TERMES_EN&filter=concepts.id:C138885662&per_page=20"
```

> Le concept `C138885662` correspond à "Law" dans OpenAlex. Voir `references/openalex_api.md` pour les filtres avancés et les concepts juridiques.

**Semantic Scholar** (complément, surtout pour les métriques de citations) :

```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=TERMES_EN&fields=paperId,title,authors,year,abstract,venue,citationCount,url,externalIds&fieldsOfStudy=Law&limit=20&year=2020-2025"
```

> Voir `references/semantic_scholar_api.md` pour la documentation complète.

### Étape 4 : Vérification et enrichissement via CrossRef (OBLIGATOIRE)

**Cette étape est SYSTÉMATIQUE, pas optionnelle.** CrossRef est la seule source fiable pour les métadonnées éditoriales (volume, numéro, pages).

**Pour chaque résultat qui possède un DOI** (trouvé via ISIDORE, HAL ou OpenAlex) :

```bash
# Résolution d'un DOI — récupère volume, numéro, pages, date précise
curl "https://api.crossref.org/works/10.xxxx/yyyy"
```

Extraire et compléter : `volume`, `issue`, `page`, `published.date-parts`.

**Pour les résultats SANS DOI**, tenter une recherche CrossRef par titre + auteur :

```bash
# Recherche bibliographique pour trouver le DOI et les métadonnées
curl "https://api.crossref.org/works?query.bibliographic=AUTEUR+TITRE_PARTIEL&rows=3"
```

**Si CrossRef ne retourne rien** : laisser les champs volume/numéro/pages VIDES dans la référence et l'indiquer clairement.

> Voir `references/crossref_api.md` pour les filtres par type, date, éditeur.

### Étape 5 : Doctrine historique (si pertinent)

**Persée OAI** — pour les collections rétrospectives de revues juridiques :

```bash
# Liste des collections juridiques disponibles
curl "https://oai.persee.fr/oai?verb=ListSets"

# Recherche dans une collection spécifique
curl "https://oai.persee.fr/oai?verb=ListRecords&metadataPrefix=oai_dc&set=revue_rfsp"
```

> Voir `references/persee_oai.md` pour les collections juridiques et la navigation.

## Workflow Spécial : Droit Comparé

Pour les recherches comparatives, exécuter les recherches en parallèle dans les deux langues avec un thesaurus bilingue.

### Thesaurus Bilingue — Termes Juridiques Courants

| Français | English |
|----------|---------|
| Contrat de travail | Employment contract |
| Licenciement | Dismissal / Termination |
| Licenciement abusif | Unfair dismissal / Wrongful termination |
| Période d'essai | Probationary period / Trial period |
| Négociation collective | Collective bargaining |
| Convention collective | Collective agreement |
| Représentant du personnel | Employee representative |
| Comité social et économique | Works council |
| Harcèlement moral | Workplace bullying / Moral harassment |
| Harcèlement sexuel | Sexual harassment |
| Discrimination | Discrimination |
| Rupture conventionnelle | Negotiated termination |
| Temps de travail | Working time |
| Salaire minimum | Minimum wage |
| Droit de grève | Right to strike |
| Transfert d'entreprise | Transfer of undertaking (TUPE) |
| Responsabilité civile | Civil liability / Tort liability |
| Responsabilité contractuelle | Contractual liability |
| Obligation de sécurité | Duty of care / Safety obligation |
| Protection des données | Data protection |
| Propriété intellectuelle | Intellectual property |
| Droit de la consommation | Consumer law |
| Droit des sociétés | Company law / Corporate law |
| Procédure civile | Civil procedure |
| Voies de recours | Remedies / Appeals |

Ce thesaurus est indicatif. Pour des termes spécialisés, adapter la traduction au contexte juridique précis de chaque système.

### Stratégie de recherche comparée

1. **Traduire les termes** en utilisant le thesaurus ci-dessus comme point de départ
2. **Lancer ISIDORE** avec les termes français + "droit comparé" ou "comparative"
3. **Lancer OpenAlex** avec les termes anglais + filtre Law
4. **Lancer Semantic Scholar** si besoin de métriques de citations
5. **Synthétiser** : regrouper par juridiction, identifier les auteurs-clés des deux côtés

## Format de Sortie

Adapter le format selon la demande (résultats rapides vs état de l'art complet).

### Format standard (résultats de recherche)

Pour chaque résultat, fournir **uniquement les informations effectivement retournées par les API** :

```
[N]. AUTEUR(S) (ANNÉE). « Titre complet ». Revue/Source, [vol. X, n° Y, p. Z-W — UNIQUEMENT si disponible via CrossRef ou l'API source].
    → Type : Article | Thèse | Ouvrage | Chapitre | Communication
    → Source : ISIDORE | HAL | OpenAlex | Semantic Scholar | CrossRef
    → Résumé : [2-3 lignes si disponible]
    → Accès : [URL directe] | DOI : [si disponible]
    → [Citations : N (si donnée disponible via OpenAlex/Semantic Scholar)]
    → [⚠ Métadonnées incomplètes : vol./n°/p. non disponibles — si pertinent]
```

**Règles strictes du format de sortie :**
- Si volume/numéro/pages ne sont PAS retournés par une API, ne PAS les inclure. Écrire simplement le nom de la revue et l'année.
- Ne JAMAIS écrire `p. 1` ou `vol. 1` par défaut — l'absence de données n'est pas `1`.
- Si un DOI a été résolu via CrossRef et que les métadonnées complètes sont disponibles, les inclure.
- Indiquer en fin de liste le taux de complétude : "X références sur Y disposent de métadonnées éditoriales complètes (volume/pages)."

### Format bibliographie commentée (si demandé)

```
## Bibliographie commentée : [THÈME]

### Doctrine française

[Référence formatée]
↳ Commentaire : pertinence pour la question posée, positionnement doctrinal, apport principal.

### Doctrine internationale / comparée

[Référence formatée]
↳ Commentaire : pertinence comparative, système juridique traité, méthodologie.

### Synthèse
[Analyse des tendances doctrinales, lacunes identifiées, pistes de recherche]
```

## Formats de Citation

Proposer le format adapté au contexte. En cas de doute, utiliser le format revue juridique française.

**RÈGLE ABSOLUE** : ne remplir que les champs dont on dispose effectivement. Un champ absent de l'API est absent de la citation. Ne JAMAIS compléter par déduction, approximation ou invention.

**Format revue juridique française :**
> A. NOM, « Titre de l'article », *Nom de la Revue* année[, vol. X][, n° Y][, p. Z].
> *(les crochets indiquent des champs conditionnels : inclure SEULEMENT si l'information a été retournée par CrossRef ou une autre API)*

**Format APA 7 :**
> Nom, P. (Année). Titre de l'article. *Nom de la Revue*[, *volume*(numéro), pages]. https://doi.org/xxx

**Format Chicago (notes de bas de page) :**
> Prénom Nom, « Titre de l'article », *Nom de la Revue* [vol, n°] (année)[ : pages].

**Exemple de référence incomplète mais honnête :**
> J. DUPONT, « Le licenciement pour motif personnel », *Revue de droit du travail* 2023 [vol./n°/p. : consulter la source — DOI : 10.xxxx/yyyy]

## Bonnes Pratiques

### Stratégie de recherche

1. **Commencer par ISIDORE** pour la doctrine francophone (couvre ~80% des besoins)
2. **HAL en complément** pour recherches ciblées (auteur, institution, textes intégraux)
3. **OpenAlex pour l'international** — meilleure couverture et données ouvertes que Semantic Scholar
4. **Semantic Scholar en complément** — utile pour les métriques de citations et la recherche sémantique
5. **CrossRef pour la bibliographie** — données éditeurs fiables, résolution DOI
6. **Persée pour l'historique** — collections rétrospectives de revues françaises

### Optimisation des requêtes

- Utiliser des **termes français** pour ISIDORE/HAL, **anglais** pour OpenAlex/Semantic Scholar
- **Phrases exactes** entre guillemets : `"contrat de travail"`, `"unfair dismissal"`
- **Combiner les opérateurs** : `(licenciement OR rupture) AND jurisprudence`
- **Filtrer par date** pour doctrine récente, par citations pour doctrine influente
- Pour le droit comparé, toujours chercher dans **les deux langues**

### Gestion des erreurs et alternatives

Si une API ne répond pas :
1. Vérifier la syntaxe de la requête
2. Réessayer avec des termes simplifiés
3. Passer à la source alternative (ISIDORE ↔ HAL, OpenAlex ↔ Semantic Scholar)
4. Informer l'utilisateur de l'échec et des sources effectivement consultées

### Qualité, attribution et intégrité bibliographique

- **Toujours** fournir les URLs d'accès et les DOI
- **Toujours** indiquer la source de chaque résultat
- **Toujours** résoudre les DOI via CrossRef pour compléter volume/numéro/pages
- **JAMAIS** inventer un numéro de volume, de page, de revue ou une date précise non retournée par l'API
- **JAMAIS** déduire des métadonnées d'un identifiant (ex: ne pas extraire un n° de page d'un DOI)
- **Privilégier** les résultats avec texte intégral disponible
- **Signaler** quand un résultat n'est disponible que via abonnement (Cairn, LGDJ, etc.)
- **Vérifier** les doublons entre sources (un même article peut apparaître dans ISIDORE et OpenAlex)
- **Indiquer explicitement** en fin de résultats le niveau de complétude des métadonnées

## Exemples d'Utilisation

**Exemple 1 : Recherche thématique simple**
```
Utilisateur : "Trouve-moi des articles récents sur la période d'essai en droit du travail"
→ ISIDORE : "période d'essai droit travail", filtre article, tri par date
→ Présenter 15-20 résultats les plus récents
```

**Exemple 2 : Recherche comparative**
```
Utilisateur : "Je cherche de la doctrine sur le licenciement abusif en droit comparé franco-britannique"
→ ISIDORE : "licenciement abusif droit comparé" + "unfair dismissal"
→ OpenAlex : "unfair dismissal French British comparative"
→ Semantic Scholar : "wrongful termination comparative labor law France UK"
→ Synthèse regroupée par juridiction
```

**Exemple 3 : Recherche d'auteur**
```
Utilisateur : "Quelles sont les publications de X sur le droit du travail ?"
→ HAL : authFullName_t:"Nom" + domain_s:shs.droit
→ OpenAlex : filter=authorships.author.display_name:Nom
→ Présenter liste chronologique complète
```

**Exemple 4 : État de l'art**
```
Utilisateur : "Fais-moi un état de l'art sur le télétravail en droit du travail"
→ ISIDORE + HAL (français) : "télétravail" + filtres droit
→ OpenAlex (international) : "telework remote work employment law"
→ Bibliographie commentée avec synthèse des tendances
```

**Exemple 5 : Vérification de citation**
```
Utilisateur : "Peux-tu vérifier cette référence : Dupont, RDT 2023, p. 45"
→ CrossRef : query="Dupont" + filter container-title + date
→ HAL : recherche auteur + revue
→ Confirmer ou corriger la référence
```

## Références Détaillées

Pour la documentation technique complète de chaque API :
- **ISIDORE** : `references/isidore_api.md`
- **HAL** : `references/hal_api.md`
- **OpenAlex** : `references/openalex_api.md`
- **Semantic Scholar** : `references/semantic_scholar_api.md`
- **CrossRef** : `references/crossref_api.md`
- **Persée OAI** : `references/persee_oai.md`

## Limitations Connues

- **ISIDORE** : Mise à jour mensuelle (peut manquer les publications très récentes)
- **HAL** : Couverture principalement française ; champs volume/numéro/pages rarement renseignés
- **OpenAlex** : Couverture juridique francophone limitée (meilleur pour l'anglophone) ; PAS de volume/numéro/pages dans les réponses
- **Semantic Scholar** : Rate limit strict sans clé API (1 req/s) ; PAS de volume/numéro/pages
- **CrossRef** : Pas de texte intégral, mais SEULE source fiable pour volume/numéro/pages
- **Persée** : Collections rétrospectives uniquement (pas de publications en cours)
- **Cairn.info** : Pas d'API directe — accès uniquement via ISIDORE (métadonnées) ou abonnement institutionnel
- **Dalloz, LGDJ, LexisNexis** : Bases propriétaires non accessibles via cette skill

## Pièges d'Hallucination à Éviter (rappel critique)

Ces erreurs sont les plus fréquentes et les plus dommageables pour la crédibilité académique :

| Erreur | Exemple | Pourquoi c'est grave |
|--------|---------|---------------------|
| Inventer un n° de page | « p. 45 » sans source | Impossible à vérifier, induit en erreur le lecteur |
| Inventer un n° de volume | « vol. 12 » sans source | La revue n'a peut-être pas de vol. 12 |
| Déduire du DOI | DOI `...095.0045` → « p. 45 » | Le DOI est un identifiant, pas un code de pagination |
| Compléter une date | API retourne 2023 → écrire « juin 2023 » | Le mois n'est pas connu |
| Inventer un ISSN/ISBN | Fournir un numéro non retourné par l'API | Peut correspondre à une autre revue |
| Halluciner un titre de revue | Écrire « Droit social » quand l'API dit « Dr. soc. » | L'abréviation peut correspondre à autre chose |

**Règle d'or : en cas de doute sur une métadonnée, NE PAS l'inclure et signaler l'information manquante.**
