# API OpenAlex — Référence Complète

## Vue d'ensemble

OpenAlex est une base de données bibliographique ouverte et gratuite qui indexe plus de 250 millions de travaux scientifiques. Successeur de Microsoft Academic Graph, maintenu par OurResearch. Particulièrement utile pour le droit comparé grâce à sa couverture internationale et ses données de citations ouvertes.

**Base URL** : https://api.openalex.org

## Avantages pour le Droit Comparé

- **Couverture mondiale** : 250M+ travaux dans toutes les langues
- **Données ouvertes** : pas de clé API requise, pas de paywall sur les métadonnées
- **Citations ouvertes** : graphe de citations complet et gratuit
- **Concepts enrichis** : classification automatique par thème/domaine
- **Données d'affiliation** : identification des institutions et pays des auteurs
- **Accès open access** : liens directs vers les versions OA quand disponibles

## Endpoints Principaux

### 1. Recherche de Travaux (Works)

```
GET https://api.openalex.org/works?search=TERMES
```

**Paramètres essentiels :**
- `search` : recherche plein texte (titre, résumé, texte intégral)
- `filter` : filtres combinables (voir section Filtres)
- `sort` : tri des résultats
- `per_page` : nombre de résultats (défaut: 25, max: 200)
- `page` : numéro de page
- `select` : champs à retourner (optimisation)
- `mailto` : email pour accès "polite pool" (recommandé, rate limit plus élevé)

**Exemple complet :**
```bash
curl "https://api.openalex.org/works?search=employment%20law%20comparative&filter=topics.domain.id:https://openalex.org/domains/2,publication_year:2020-2025,type:article&sort=relevance_score:desc&per_page=20&mailto=votre@email.fr"
```

### 2. Recherche d'Auteurs

```
GET https://api.openalex.org/authors?search=NOM
```

Utile pour trouver le profil complet d'un chercheur et toutes ses publications.

```bash
curl "https://api.openalex.org/authors?search=dupont%20droit%20travail&per_page=5&mailto=votre@email.fr"
```

### 3. Recherche de Sources (Revues)

```
GET https://api.openalex.org/sources?search=NOM_REVUE
```

```bash
curl "https://api.openalex.org/sources?search=revue%20droit%20travail&per_page=5&mailto=votre@email.fr"
```

### 4. Recherche de Concepts/Topics

```
GET https://api.openalex.org/topics?search=TERME
```

```bash
curl "https://api.openalex.org/topics?search=labor%20law&per_page=10&mailto=votre@email.fr"
```

## Filtres pour le Droit

### Par domaine (Topics)

OpenAlex utilise un système de topics hiérarchiques : Domain > Field > Subfield > Topic.

```
# Domaine "Social Sciences" (inclut le droit)
filter=topics.domain.id:https://openalex.org/domains/2

# Sous-domaine "Law" spécifiquement
filter=topics.subfield.id:https://openalex.org/subfields/3308
```

**Domaines et sous-domaines pertinents pour le droit :**
- `domains/2` : Social Sciences
- `subfields/3308` : Law
- `subfields/3312` : Sociology and Political Science
- `subfields/3301` : Social Sciences (general)

### Par concept (ancien système, encore fonctionnel)

```
# Concept "Law" (ID: C138885662)
filter=concepts.id:C138885662

# Concept "Labour law" (ID: C107457646)  
filter=concepts.id:C107457646

# Concept "Employment" (ID: C162324750)
filter=concepts.id:C162324750

# Concept "Comparative law" (ID: C2776548165)
filter=concepts.id:C2776548165
```

### Par date

```
filter=publication_year:2024
filter=publication_year:2020-2025
filter=from_publication_date:2023-01-01
```

### Par type de document

```
filter=type:article
filter=type:book
filter=type:book-chapter
filter=type:dissertation
filter=type:review
```

### Par langue

```
filter=language:fr        # Français
filter=language:en        # Anglais
filter=language:de        # Allemand
```

### Par accès open access

```
filter=is_oa:true                    # Uniquement OA
filter=open_access.oa_status:gold    # Gold OA
filter=open_access.oa_status:green   # Green OA
```

### Par pays des auteurs

```
filter=authorships.countries:FR      # Auteurs affiliés en France
filter=authorships.countries:GB      # Auteurs affiliés au Royaume-Uni
filter=authorships.countries:US      # Auteurs affiliés aux USA
```

### Combinaison de filtres

Les filtres se combinent avec des virgules (AND logique) :

```bash
# Articles de droit, auteurs français, depuis 2020, open access
curl "https://api.openalex.org/works?search=labor%20law&filter=concepts.id:C138885662,authorships.countries:FR,publication_year:2020-2025,is_oa:true&sort=cited_by_count:desc&per_page=20"
```

## Tri des Résultats

```
sort=relevance_score:desc       # Pertinence (défaut avec search)
sort=cited_by_count:desc        # Plus cités
sort=publication_date:desc      # Plus récents
sort=publication_date:asc       # Plus anciens
```

## Structure de Réponse JSON (Works)

```json
{
  "meta": {
    "count": 1234,
    "per_page": 20,
    "page": 1
  },
  "results": [
    {
      "id": "https://openalex.org/W1234567890",
      "doi": "https://doi.org/10.1234/example",
      "title": "Comparative Employment Law in France and the UK",
      "display_name": "Comparative Employment Law in France and the UK",
      "publication_year": 2023,
      "publication_date": "2023-06-15",
      "type": "article",
      "language": "en",
      "open_access": {
        "is_oa": true,
        "oa_status": "green",
        "oa_url": "https://hal.archives-ouvertes.fr/hal-01234567/document"
      },
      "authorships": [
        {
          "author": {
            "id": "https://openalex.org/A1234567",
            "display_name": "Jean Dupont",
            "orcid": "https://orcid.org/0000-0001-2345-6789"
          },
          "institutions": [
            {
              "id": "https://openalex.org/I12345",
              "display_name": "Université de Rouen Normandie",
              "country_code": "FR"
            }
          ]
        }
      ],
      "primary_location": {
        "source": {
          "id": "https://openalex.org/S1234567",
          "display_name": "Revue de droit du travail",
          "issn_l": "1234-5678",
          "type": "journal"
        }
      },
      "cited_by_count": 45,
      "abstract_inverted_index": { ... },
      "concepts": [
        {
          "id": "https://openalex.org/C138885662",
          "display_name": "Law",
          "score": 0.95
        }
      ],
      "topics": [
        {
          "id": "https://openalex.org/T12345",
          "display_name": "Employment Protection and Labor Markets",
          "subfield": { "display_name": "Law" },
          "field": { "display_name": "Social Sciences" },
          "domain": { "display_name": "Social Sciences" }
        }
      ]
    }
  ]
}
```

### Note sur les résumés

OpenAlex stocke les résumés sous forme d'`abstract_inverted_index` (index inversé). Pour reconstruire le texte :

```python
# L'index inversé est un dict: {mot: [positions]}
# Trier par position pour reconstruire le texte
abstract_index = result.get("abstract_inverted_index", {})
if abstract_index:
    words = sorted(
        [(pos, word) for word, positions in abstract_index.items() for pos in positions],
        key=lambda x: x[0]
    )
    abstract_text = " ".join(word for _, word in words)
```

## Sélection de Champs (Optimisation)

Pour réduire la taille des réponses, utiliser `select` :

```
select=id,doi,title,publication_year,authorships,primary_location,cited_by_count,open_access,language
```

## Pagination

```bash
# Page 1
curl "https://api.openalex.org/works?search=...&per_page=50&page=1"

# Page 2
curl "https://api.openalex.org/works?search=...&per_page=50&page=2"
```

Pour de grands ensembles (>10 000 résultats), utiliser le curseur :

```bash
curl "https://api.openalex.org/works?filter=...&per_page=200&cursor=*"
# Puis utiliser la valeur de meta.next_cursor pour la page suivante
```

## Rate Limits

- **Sans email** : ~10 req/sec (pool partagé)
- **Avec mailto** : ~100 req/sec (polite pool, recommandé)
- **Avec clé API** : Limite plus élevée (premium, payant)

Toujours ajouter `&mailto=votre@email.fr` pour un meilleur débit.

## Exemples Pratiques pour le Droit

### 1. Doctrine récente en droit du travail comparé

```bash
curl "https://api.openalex.org/works?search=comparative%20labor%20law&filter=concepts.id:C138885662,publication_year:2020-2025&sort=cited_by_count:desc&per_page=20&mailto=user@example.fr"
```

### 2. Articles français sur le licenciement (auteurs FR)

```bash
curl "https://api.openalex.org/works?search=licenciement%20droit%20travail&filter=authorships.countries:FR,type:article&sort=publication_date:desc&per_page=20&mailto=user@example.fr"
```

### 3. Thèses sur le harcèlement moral

```bash
curl "https://api.openalex.org/works?search=harcelement%20moral%20workplace%20bullying&filter=type:dissertation&sort=publication_date:desc&per_page=15&mailto=user@example.fr"
```

### 4. Publications d'une institution

```bash
# D'abord trouver l'ID de l'institution
curl "https://api.openalex.org/institutions?search=universite%20rouen&per_page=3"

# Puis chercher ses publications en droit
curl "https://api.openalex.org/works?filter=authorships.institutions.id:https://openalex.org/I[ID],concepts.id:C138885662&sort=publication_date:desc&per_page=20"
```

### 5. Articles les plus cités sur l'unfair dismissal

```bash
curl "https://api.openalex.org/works?search=%22unfair%20dismissal%22&filter=concepts.id:C138885662&sort=cited_by_count:desc&per_page=10&mailto=user@example.fr"
```

## Limitations

- **Résumés** : Format index inversé (nécessite reconstruction)
- **Volume/numéro/pages** : OpenAlex ne retourne PAS ces champs dans la réponse standard. Pour obtenir volume, numéro et pages, il faut résoudre le DOI via CrossRef. NE JAMAIS inventer ces données.
- **Couverture francophone** : Bonne mais moins exhaustive qu'ISIDORE pour la doctrine française
- **Classification** : Automatique (peut manquer certains articles juridiques classés ailleurs)
- **Texte intégral** : Liens OA quand disponibles, sinon métadonnées seulement

## Ressources

- **Documentation officielle** : https://docs.openalex.org
- **API playground** : https://api.openalex.org (navigable dans le navigateur)
- **Code source** : https://github.com/ourresearch/openalex-api-tutorials
