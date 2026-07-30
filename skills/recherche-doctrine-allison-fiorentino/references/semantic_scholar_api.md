# API Semantic Scholar - Référence Complète

## Vue d'ensemble

Semantic Scholar est un moteur de recherche académique gratuit alimenté par l'IA, couvrant plus de 200 millions d'articles scientifiques dans toutes les disciplines. Particulièrement utile pour la doctrine juridique internationale anglophone.

**Base URL** : https://api.semanticscholar.org/graph/v1

## Authentification

- **Sans clé API** : 1 requête/seconde
- **Avec clé API** : Limite plus élevée (gratuit)
- **Demander une clé** : https://www.semanticscholar.org/product/api

**Usage avec clé API :**
```bash
curl -H "x-api-key: YOUR_API_KEY" "https://api.semanticscholar.org/..."
```

## Endpoints Principaux

### 1. Recherche Bulk (Recommandé)
```
GET /paper/search/bulk
```

Meilleure performance, supporte le tri et les opérateurs avancés.

**Paramètres :**
- `query` : termes de recherche (obligatoire)
- `fields` : champs à retourner (séparés par virgules)
- `limit` : nombre de résultats (max: 100)
- `offset` : décalage pour pagination
- `year` : filtre par année (ex: `2020-2024`)
- `publicationTypes` : types de publication
- `fieldsOfStudy` : domaines d'étude
- `sort` : tri (`citationCount:desc`, `publicationDate:desc`)

**Exemple :**
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=employment%20law&fields=paperId,title,authors,year,abstract,url,citationCount&limit=20&year=2020-2024"
```

### 2. Recherche Standard
```
GET /paper/search
```

Plus simple mais moins de fonctionnalités.

### 3. Détails d'un Paper
```
GET /paper/{paper_id}
```

Obtenir les détails complets d'un article spécifique.

## Champs Disponibles

### Champs Essentiels
- **paperId** : Identifiant unique
- **title** : Titre
- **abstract** : Résumé
- **year** : Année de publication
- **url** : URL Semantic Scholar
- **externalIds** : Identifiants externes (DOI, ArXiv, etc.)

### Auteurs
- **authors** : Liste des auteurs
  - `authorId` : ID auteur
  - `name` : Nom complet
  - `affiliations` : Affiliations

### Métriques
- **citationCount** : Nombre de citations
- **influentialCitationCount** : Citations influentes
- **referenceCount** : Nombre de références

### Publication
- **venue** : Lieu de publication (revue, conférence)
- **publicationDate** : Date de publication
- **publicationTypes** : Types (Journal, Conference, etc.)

### Relations
- **citations** : Articles qui citent ce papier
- **references** : Articles cités
- **fieldsOfStudy** : Domaines d'étude

## Champs Recommandés pour Droit

```
fields=paperId,title,authors,year,abstract,venue,publicationDate,citationCount,url,externalIds,fieldsOfStudy,publicationTypes
```

## Opérateurs de Recherche

### Opérateurs Booléens
- **AND** : mots séparés par espace (implicite)
  - `employment law` = employment AND law
- **OR** : utiliser `|`
  - `employment | labor law`
- **NOT** : utiliser `-`
  - `employment law -criminal`

### Phrases Exactes
```
"employment contract"
```

### Groupement
```
(employment | labor) law
```

### Exemples Combinés
```
"labor law" (France | UK) -criminal
```

## Filtres par Domaine (fieldsOfStudy)

Domaines pertinents pour le droit :
- `Law`
- `Political Science`
- `Sociology`
- `Economics`
- `Business`

**Exemple :**
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=contract%20law&fields=title,authors,year&fieldsOfStudy=Law&limit=20"
```

## Types de Publication

- `JournalArticle`
- `Conference`
- `Review`
- `Book`
- `BookSection`

## Exemples Pratiques

### 1. Recherche Simple - Droit du Travail
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=employment%20law&fields=title,authors,year,abstract,citationCount,url&limit=20&fieldsOfStudy=Law"
```

### 2. Recherche Récente avec Citations
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=labor%20rights&fields=title,authors,year,citationCount,url&year=2020-2024&sort=citationCount:desc&limit=20"
```

### 3. Phrase Exacte + Filtre Année
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=\"employment%20contract\"&fields=title,authors,year,abstract,url&year=2022-2024&limit=15"
```

### 4. Comparaison Juridique
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=comparative%20labor%20law%20(France%20|%20UK)&fields=title,authors,year,abstract,url&fieldsOfStudy=Law&limit=20"
```

### 5. Avec Clé API (Rate Limit Plus Élevé)
```bash
curl -H "x-api-key: YOUR_KEY" \
  "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=employment%20discrimination&fields=title,authors,year,url&limit=50"
```

## Structure de Réponse JSON

```json
{
  "data": [
    {
      "paperId": "abc123",
      "title": "Employment Law and Worker Rights",
      "authors": [
        {
          "authorId": "xyz789",
          "name": "John Smith"
        }
      ],
      "year": 2023,
      "abstract": "This paper examines...",
      "venue": "Harvard Law Review",
      "citationCount": 45,
      "url": "https://www.semanticscholar.org/paper/abc123",
      "externalIds": {
        "DOI": "10.1234/example",
        "ArXiv": "2301.12345"
      },
      "fieldsOfStudy": ["Law", "Political Science"],
      "publicationTypes": ["JournalArticle"]
    }
  ],
  "next": 20
}
```

## Pagination

Pour parcourir les résultats :

```bash
# Page 1 (0-19)
curl "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=...&offset=0&limit=20"

# Page 2 (20-39)
curl "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=...&offset=20&limit=20"

# Page 3 (40-59)
curl "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=...&offset=40&limit=20"
```

Le champ `next` dans la réponse indique l'offset pour la page suivante.

## Tri des Résultats

Options de tri (`sort`) :
- `citationCount:desc` : Plus cités en premier
- `citationCount:asc` : Moins cités en premier
- `publicationDate:desc` : Plus récents en premier
- `publicationDate:asc` : Plus anciens en premier

**Exemple :**
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=labor%20law&sort=citationCount:desc&limit=20"
```

## Accès aux Identifiants Externes

Le champ `externalIds` peut contenir :
- **DOI** : Digital Object Identifier
- **ArXiv** : Identifiant ArXiv
- **PubMed** : ID PubMed
- **MAG** : Microsoft Academic Graph ID
- **CorpusId** : Semantic Scholar Corpus ID

Utile pour récupérer le texte intégral via d'autres plateformes.

## Rate Limits

### Sans Clé API
- 1 requête/seconde (100 req/minute)
- Partagé entre tous les utilisateurs non authentifiés
- Peut être limité en période de forte utilisation

### Avec Clé API
- Limite plus élevée (non spécifiée publiquement)
- Requêtes non partagées
- Meilleure stabilité

### Demander une Augmentation
Si besoin de plus : contacter via le formulaire sur le site officiel.

## Bonnes Pratiques

1. **Toujours utiliser bulk search** (pas search standard)
2. **Spécifier les champs nécessaires** uniquement
3. **Filtrer par fieldsOfStudy=Law** pour le droit
4. **Utiliser year filter** pour publications récentes
5. **Trier par citationCount** pour articles influents
6. **Encoder les caractères spéciaux** dans l'URL
7. **Gérer les erreurs** (HTTP 429 = rate limit)

## Limitations

- **Couverture** : Principalement anglophone
- **Texte intégral** : Pas toujours disponible (liens externes)
- **Métadonnées** : Qualité variable selon sources
- **Rate limits** : Restrictifs sans clé API
- **Domaines** : Meilleur pour sciences que SHS parfois

## Avantages pour Droit Comparé

1. **Large couverture** internationale
2. **Métriques de citations** pour évaluer influence
3. **Gratuit** avec bonnes fonctionnalités
4. **API stable** et bien documentée
5. **Recherche sémantique** intelligente

## Ressources

- **Documentation officielle** : https://api.semanticscholar.org/api-docs/
- **Demander une clé API** : https://www.semanticscholar.org/product/api
- **Tutorial** : https://www.semanticscholar.org/product/api/tutorial
- **Postman Collection** : Disponible sur le site

## Conseils pour Doctrine Juridique

1. **Combiner avec HAL/ISIDORE** pour sources françaises
2. **Filtrer fieldsOfStudy=Law** systématiquement
3. **Utiliser opérateurs** pour recherches précises
4. **Trier par citations** pour identifier articles clés
5. **Vérifier DOI** pour accès texte intégral
6. **Recherches comparatives** : utiliser OR pour pays multiples

## Gestion des Erreurs

**HTTP 429** - Trop de requêtes
```
Attendre 1 seconde puis réessayer
Obtenir une clé API si problème récurrent
```

**HTTP 400** - Requête invalide
```
Vérifier syntaxe des opérateurs
Encoder correctement l'URL
```

**HTTP 404** - Non trouvé
```
Vérifier l'endpoint
Vérifier le paperId si recherche par ID
```

## Exemple Complet - Recherche Comparative en Droit

```bash
#!/bin/bash
# Recherche comparative : droit du travail France vs UK

API_KEY="your-api-key-here"

# Recherche générale
curl -H "x-api-key: $API_KEY" \
  "https://api.semanticscholar.org/graph/v1/paper/search/bulk?\
query=comparative%20labor%20law%20(France%20OR%20UK%20OR%20\"United%20Kingdom\")&\
fields=paperId,title,authors,year,abstract,venue,citationCount,url,externalIds&\
fieldsOfStudy=Law&\
year=2015-2024&\
sort=citationCount:desc&\
limit=30"
```

Ce type de recherche est complémentaire à ISIDORE/HAL pour une vue internationale.
