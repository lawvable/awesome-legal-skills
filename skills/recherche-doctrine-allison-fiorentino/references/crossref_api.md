# API CrossRef — Référence Complète

## Vue d'ensemble

CrossRef est le registre officiel des DOI (Digital Object Identifiers) pour les publications scientifiques. Il contient les métadonnées de plus de 150 millions de publications, directement fournies par les éditeurs. Source de référence pour la vérification bibliographique et les métadonnées de qualité éditoriale.

**Base URL** : https://api.crossref.org

## Avantages pour la Recherche Juridique

- **Données éditeurs** : métadonnées directement fournies par les éditeurs (haute fiabilité)
- **Résolution DOI** : accès direct aux métadonnées d'un article via son DOI
- **Couverture juridique** : nombreuses revues de droit indexées
- **Gratuit** : API ouverte sans authentification
- **Citations** : comptage de citations (via OpenCitations)

## Endpoints Principaux

### 1. Recherche de Travaux

```
GET https://api.crossref.org/works?query=TERMES
```

**Paramètres :**
- `query` : recherche générale
- `query.title` : recherche dans le titre uniquement
- `query.author` : recherche par auteur
- `query.bibliographic` : recherche bibliographique combinée
- `query.container-title` : recherche par nom de revue
- `filter` : filtres (voir section Filtres)
- `sort` : tri (`relevance`, `published`, `is-referenced-by-count`)
- `order` : ordre (`asc`, `desc`)
- `rows` : nombre de résultats (défaut: 20, max: 1000)
- `offset` : décalage pour pagination
- `select` : champs à retourner

### 2. Résolution DOI

```
GET https://api.crossref.org/works/DOI
```

```bash
# Exemple : résolution d'un DOI
curl "https://api.crossref.org/works/10.3917/rdli.095.0045"
```

### 3. Recherche de Revues

```
GET https://api.crossref.org/journals?query=NOM_REVUE
```

### 4. Travaux d'une Revue

```
GET https://api.crossref.org/journals/ISSN/works?query=TERMES
```

## Filtres

### Par date

```
filter=from-pub-date:2020,until-pub-date:2025
filter=from-pub-date:2023-01-01
```

### Par type

```
filter=type:journal-article
filter=type:book-chapter
filter=type:dissertation
filter=type:book
filter=type:monograph
filter=type:proceedings-article
```

### Par disponibilité

```
filter=has-abstract:true          # Avec résumé
filter=has-full-text:true         # Avec texte intégral
filter=has-references:true        # Avec références
```

### Par licence / Open Access

```
filter=license.url:http://creativecommons.org/licenses/by/4.0/
```

### Par ISSN (revue spécifique)

```
filter=issn:1234-5678
```

### Par éditeur

```
filter=publisher-name:Dalloz
filter=publisher-name:LGDJ
filter=publisher-name:Cairn
```

### Combinaison de filtres

Les filtres se combinent avec des virgules :

```bash
curl "https://api.crossref.org/works?query=droit+travail+licenciement&filter=from-pub-date:2020,type:journal-article,has-abstract:true&sort=relevance&rows=20"
```

## Structure de Réponse JSON

```json
{
  "status": "ok",
  "message-type": "work-list",
  "message": {
    "total-results": 456,
    "items": [
      {
        "DOI": "10.3917/rdli.095.0045",
        "type": "journal-article",
        "title": ["Le licenciement pour motif personnel"],
        "author": [
          {
            "given": "Jean",
            "family": "Dupont",
            "ORCID": "https://orcid.org/0000-0001-2345-6789",
            "affiliation": [{"name": "Université de Rouen"}]
          }
        ],
        "container-title": ["Revue de droit du travail"],
        "published": {
          "date-parts": [[2023, 6]]
        },
        "volume": "95",
        "page": "45-62",
        "abstract": "<jats:p>Résumé de l'article...</jats:p>",
        "URL": "http://dx.doi.org/10.3917/rdli.095.0045",
        "ISSN": ["1234-5678"],
        "is-referenced-by-count": 12,
        "references-count": 35,
        "publisher": "Dalloz",
        "subject": ["Law"],
        "language": "fr"
      }
    ]
  }
}
```

### Note sur les résumés

Les résumés CrossRef sont souvent en format JATS XML. Extraire le texte en supprimant les balises :

```
<jats:p>Texte du résumé...</jats:p>  →  Texte du résumé...
```

## Exemples Pratiques

### 1. Recherche générale en droit du travail

```bash
curl "https://api.crossref.org/works?query=droit+travail+licenciement&filter=type:journal-article,from-pub-date:2020&sort=relevance&rows=15"
```

### 2. Recherche par auteur

```bash
curl "https://api.crossref.org/works?query.author=Dupont&query.bibliographic=droit+travail&filter=from-pub-date:2015&rows=20"
```

### 3. Publications d'une revue spécifique

```bash
# Par ISSN
curl "https://api.crossref.org/journals/1234-5678/works?query=licenciement&sort=published&order=desc&rows=10"
```

### 4. Vérification d'une référence bibliographique

```bash
# Recherche combinée titre + auteur + année
curl "https://api.crossref.org/works?query.bibliographic=Dupont+licenciement+abusif+2023&rows=5"
```

### 5. Résolution d'un DOI

```bash
curl "https://api.crossref.org/works/10.3917/rdli.095.0045"
```

## "Polite Pool" (Recommandé)

Pour un meilleur débit, inclure un email dans les requêtes :

```bash
curl "https://api.crossref.org/works?query=...&mailto=votre@email.fr"
```

Ou via le header User-Agent :
```bash
curl -H "User-Agent: MonApp/1.0 (mailto:votre@email.fr)" "https://api.crossref.org/works?query=..."
```

## Rate Limits

- **Sans email** : ~50 req/sec (pool partagé, peut être limité)
- **Avec mailto** : Rate limit plus élevé et prioritaire
- **Avec token Crossref Plus** : Encore plus rapide (payant)

## Sélection de Champs

Pour réduire la taille des réponses :

```
select=DOI,title,author,container-title,published,volume,page,abstract,URL,is-referenced-by-count,type,language
```

## Revues Juridiques Françaises sur CrossRef (exemples)

Beaucoup de revues juridiques françaises ont des DOI et sont indexées :
- Revues Dalloz (via CAIRN)
- Revues LGDJ
- Revues Lextenso
- Revues universitaires avec DOI

Pour trouver une revue spécifique :
```bash
curl "https://api.crossref.org/journals?query=revue+droit+travail"
```

## Limitations

- **Couverture** : Dépend de l'attribution de DOI par les éditeurs
- **Revues françaises** : Couverture variable (meilleures pour les grandes maisons d'édition)
- **Texte intégral** : Pas de texte intégral, métadonnées seulement
- **Résumés** : Pas toujours disponibles, format JATS XML quand présents
- **Classification** : Le champ `subject` est souvent vague

## Ressources

- **Documentation** : https://api.crossref.org/swagger-ui/index.html
- **Guide** : https://www.crossref.org/documentation/retrieve-metadata/rest-api/
