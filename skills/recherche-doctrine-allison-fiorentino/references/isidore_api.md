# API ISIDORE - Référence Complète

## Vue d'ensemble

ISIDORE est un agrégateur de données de recherche en SHS du CNRS. Il moissonne et enrichit automatiquement les métadonnées de :
- HAL (archives ouvertes)
- Cairn.info (revues SHS)
- Persée (collections rétrospectives)
- OpenEdition (Journals et Books)
- theses.fr
- Et 5000+ autres sources

**Base URL** : https://api.isidore.science

## Endpoints Principaux

### 1. Recherche de Ressources
```
GET https://api.isidore.science/resource/search
```

**Paramètres obligatoires :**
- `q` : termes de recherche

**Paramètres optionnels :**
- `output` : format (`json` ou `xml`, défaut: xml)
- `replies` : nombre de résultats (défaut: 10, max: 100)
- `page` : numéro de page
- `lang` : langue (`fr`, `en`, `es`)
- `type` : type de document (URI)
- `discipline` : discipline (URI)
- `facet` : facettes à retourner
- `sort` : tri (`score` ou `date`)

**Exemple complet :**
```bash
curl "https://api.isidore.science/resource/search?q=contrat%20travail&type=http://isidore.science/ontology%23article&discipline=http://purl.org/dc/terms/subject/law&output=json&replies=20&sort=date"
```

### 2. Autocomplétion
```
GET https://api.isidore.science/resource/suggest
```

**Paramètres :**
- `q` : début du terme
- `replies` : nombre de suggestions (défaut: 10)

**Exemple :**
```bash
curl "https://api.isidore.science/resource/suggest?q=droit%20trav&replies=5"
```

### 3. Recherche dans les Vocabulaires
```
GET https://api.isidore.science/vocabulary/search
```

Utile pour trouver les termes normalisés des thésaurus.

## Types de Documents (URIs)

Types principaux pour le droit :

```
http://isidore.science/ontology#article            # Article de revue
http://isidore.science/ontology#thesis             # Thèse
http://isidore.science/ontology#book               # Ouvrage
http://isidore.science/ontology#chapter            # Chapitre d'ouvrage
http://isidore.science/ontology#report             # Rapport
http://isidore.science/ontology#conference_paper   # Communication
http://isidore.science/ontology#working_paper      # Document de travail
```

## Disciplines (URIs)

Pour le droit :

```
http://purl.org/dc/terms/subject/law              # Droit (général)
http://aurehal.archives-ouvertes.fr/subject/shs.droit    # Droit (HAL)
```

## Structure de la Réponse JSON

```json
{
  "response": {
    "numFound": 1234,
    "docs": [
      {
        "uri": "...",
        "title": ["Titre de l'article"],
        "creator": ["Nom, Prénom", "Autre auteur"],
        "date": ["2023"],
        "publisher": ["Nom éditeur"],
        "source": ["Nom de la revue"],
        "abstract": ["Résumé..."],
        "type": ["http://isidore.science/ontology#article"],
        "discipline": ["http://purl.org/dc/terms/subject/law"],
        "language": ["fra"],
        "identifier": ["DOI:10.xxxx/yyyy"],
        "access_URL": ["https://..."]
      }
    ]
  }
}
```

## Champs Importants

- **uri** : Identifiant unique ISIDORE
- **title** : Titre (tableau)
- **creator** : Auteurs (tableau)
- **date** : Date de publication (tableau)
- **abstract** : Résumé
- **identifier** : Identifiants (DOI, HAL ID, etc.)
- **access_URL** : URL d'accès au document
- **source** : Source de publication
- **type** : Type de document
- **discipline** : Disciplines
- **language** : Langue

## Opérateurs de Recherche

ISIDORE supporte les opérateurs booléens :

- **AND** : `contrat AND travail`
- **OR** : `contrat OR emploi`
- **NOT** : `contrat NOT commercial`
- **"phrase exacte"** : `"contrat de travail"`
- **Troncature** : `travail*` (travail, travailleur, etc.)

## Exemples Pratiques

### Recherche simple
```bash
curl "https://api.isidore.science/resource/search?q=licenciement&output=json&replies=10"
```

### Articles de revue uniquement
```bash
curl "https://api.isidore.science/resource/search?q=responsabilité%20civile&type=http://isidore.science/ontology%23article&output=json"
```

### Thèses récentes (avec opérateur booléen)
```bash
curl "https://api.isidore.science/resource/search?q=droit%20numérique&type=http://isidore.science/ontology%23thesis&output=json&sort=date"
```

### Recherche par auteur et sujet
```bash
curl "https://api.isidore.science/resource/search?q=creator:Dupont%20AND%20droit%20travail&output=json"
```

## Rate Limits

- Pas de limite stricte documentée
- Utilisation raisonnable recommandée (< 10 req/sec)
- Pas d'authentification requise

## Enrichissements Sémantiques

ISIDORE enrichit automatiquement les métadonnées avec :
- Termes de thésaurus (Rameau, etc.)
- Liens vers personnes/organisations
- Géolocalisation si pertinent
- Relations entre documents

Ces enrichissements améliorent la qualité des recherches.

## Conseils d'Utilisation

1. **Commencer simple** : recherche basique puis affiner
2. **Utiliser output=json** : plus facile à parser
3. **Filtrer par type** : article, thesis selon besoin
4. **Pagination** : utiliser `page` pour parcourir résultats
5. **Trier par date** : `sort=date` pour publications récentes

## Sources de Données Agrégées

ISIDORE moissonne notamment :
- HAL-SHS
- Cairn.info
- Persée
- OpenEdition Journals
- OpenEdition Books
- Gallica (BnF)
- Erudit
- theses.fr
- Calenda
- Hypothèses
- Et des milliers d'autres dépôts institutionnels

## Documentation Officielle

https://isidore.science/api
https://documentation.huma-num.fr/isidore/
