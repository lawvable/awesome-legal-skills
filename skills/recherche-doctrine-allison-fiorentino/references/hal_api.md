# API HAL - Référence Complète

## Vue d'ensemble

HAL (Hyper Articles en Ligne) est l'archive ouverte pluridisciplinaire française. Elle contient des publications scientifiques (articles, thèses, communications, etc.) de la recherche française et francophone.

**Base URL** : https://api.archives-ouvertes.fr

## Endpoint Principal : Recherche

```
GET https://api.archives-ouvertes.fr/search/
```

## Paramètres de Recherche

### Paramètres Obligatoires

- **q** : requête de recherche
  - Syntaxe Solr/Lucene
  - Peut contenir des champs spécifiques (ex: `title:contrat`)

### Paramètres de Format

- **wt** : format de sortie
  - `json` (recommandé)
  - `xml`
  - `csv`
  
### Paramètres de Pagination

- **rows** : nombre de résultats (défaut: 10, max: 10000)
- **start** : position de départ (défaut: 0)

### Paramètres de Filtrage

- **fq** : filtres (filter query)
  - `domain_s:shs.droit` - Domaine droit
  - `docType_s:ART` - Articles
  - `docType_s:THESE` - Thèses
  - `publicationDateY_i:[2020 TO *]` - Depuis 2020
  - `language_s:fr` - Langue française

### Paramètres de Tri

- **sort** : champ de tri
  - `publicationDateY_i desc` - Date décroissante
  - `producedDateY_i desc` - Date de production
  - `score desc` - Pertinence

### Paramètres de Sélection

- **fl** : champs à retourner (séparés par virgules)
  - Par défaut : tous les champs
  - Recommandé : spécifier pour réduire la taille

## Domaines Juridiques

```
domain_s:shs.droit              # Droit (général)
domain_s:shs.droit.civil        # Droit civil
domain_s:shs.droit.public       # Droit public
domain_s:shs.droit.prive        # Droit privé
domain_s:shs.droit.inter        # Droit international
domain_s:shs.droit.euro         # Droit européen
```

## Types de Documents

```
docType_s:ART          # Article
docType_s:THESE        # Thèse
docType_s:HDR          # Habilitation à Diriger des Recherches
docType_s:COMM         # Communication dans un congrès
docType_s:COUV         # Chapitre d'ouvrage
docType_s:OUV          # Ouvrage
docType_s:REPORT       # Rapport
docType_s:UNDEFINED    # Type non défini
```

## Champs Principaux

### Identification
- **halId_s** : Identifiant HAL
- **docid** : ID du document
- **uri_s** : URI HAL
- **doiId_s** : DOI

### Métadonnées de Base
- **title_s** : Titre (tableau)
- **authFullName_s** : Noms complets des auteurs
- **authIdHal_s** : Identifiants HAL auteurs
- **abstract_s** : Résumé (tableau, multilingue)

### Dates
- **publicationDateY_i** : Année de publication
- **producedDateY_i** : Année de production
- **modifiedDateY_i** : Année de modification

### Classification
- **domain_s** : Domaine scientifique
- **docType_s** : Type de document
- **language_s** : Langue

### Publication
- **journalTitle_s** : Titre de la revue
- **journalPublisher_s** : Éditeur de la revue
- **volume_s** : Volume (souvent absent — ne pas inventer si manquant)
- **issue_s** : Numéro (souvent absent — ne pas inventer si manquant)
- **page_s** : Pages (souvent absent — ne pas inventer si manquant)
- **bookTitle_s** : Titre de l'ouvrage
- **conferenceTitle_s** : Titre de la conférence

> **ATTENTION** : Les champs volume_s, issue_s et page_s sont rarement renseignés dans HAL. Si absents, utiliser CrossRef via le DOI pour récupérer ces métadonnées. NE JAMAIS inventer ces données.

### Fichiers
- **fileMain_s** : Fichier principal
- **files_s** : Liste des fichiers

## Exemples de Requêtes

### 1. Recherche Simple
```bash
curl "https://api.archives-ouvertes.fr/search/?q=contrat%20de%20travail&wt=json&rows=10"
```

### 2. Articles de Droit Uniquement
```bash
curl "https://api.archives-ouvertes.fr/search/?q=licenciement&fq=domain_s:shs.droit&fq=docType_s:ART&wt=json&rows=20"
```

### 3. Thèses Récentes
```bash
curl "https://api.archives-ouvertes.fr/search/?q=*&fq=domain_s:shs.droit&fq=docType_s:THESE&fq=publicationDateY_i:[2020%20TO%20*]&wt=json&sort=publicationDateY_i%20desc&rows=15"
```

### 4. Recherche par Auteur
```bash
curl "https://api.archives-ouvertes.fr/search/?q=authFullName_t:\"Dupont\"&fq=domain_s:shs.droit&wt=json"
```

### 5. Recherche dans le Titre
```bash
curl "https://api.archives-ouvertes.fr/search/?q=title_t:responsabilité&fq=domain_s:shs.droit&wt=json"
```

### 6. Recherche avec Champs Spécifiques
```bash
curl "https://api.archives-ouvertes.fr/search/?q=droit%20numérique&fq=domain_s:shs.droit&fl=halId_s,title_s,authFullName_s,publicationDateY_i,abstract_s,uri_s,doiId_s&wt=json&rows=20"
```

## Structure de Réponse JSON

```json
{
  "response": {
    "numFound": 1234,
    "start": 0,
    "docs": [
      {
        "halId_s": "hal-01234567",
        "docid": "1234567",
        "uri_s": "https://hal.archives-ouvertes.fr/hal-01234567",
        "title_s": ["Titre de l'article"],
        "authFullName_s": ["Dupont, Jean", "Martin, Marie"],
        "abstract_s": ["Résumé en français...", "Abstract in English..."],
        "publicationDateY_i": 2023,
        "domain_s": ["shs.droit"],
        "docType_s": "ART",
        "language_s": ["fr"],
        "journalTitle_s": "Revue de droit du travail",
        "doiId_s": "10.1234/exemple",
        "fileMain_s": "https://hal.archives-ouvertes.fr/hal-01234567/document"
      }
    ]
  }
}
```

## Opérateurs de Recherche Solr

### Opérateurs Booléens
- **AND** : `contrat AND travail`
- **OR** : `contrat OR emploi`
- **NOT** : `contrat NOT commercial`
- **Parenthèses** : `(contrat OR emploi) AND travail`

### Recherches de Champs
- **Champ spécifique** : `title:contrat`
- **Phrase exacte** : `title:"contrat de travail"`
- **Wildcards** : `travail*` ou `tr?vail`

### Plages
- **Plages de dates** : `publicationDateY_i:[2020 TO 2024]`
- **Depuis une date** : `publicationDateY_i:[2020 TO *]`
- **Jusqu'à une date** : `publicationDateY_i:[* TO 2024]`

## Champs Recommandés pour Retour (fl)

Pour réduire la taille de la réponse :

```
fl=halId_s,docid,uri_s,title_s,authFullName_s,abstract_s,publicationDateY_i,domain_s,docType_s,language_s,journalTitle_s,volume_s,issue_s,page_s,doiId_s,fileMain_s
```

## Rate Limits

- Pas de limite stricte officielle
- Usage raisonnable recommandé
- Pas d'authentification requise
- Service gratuit

## Accès aux Textes Intégraux

- **fileMain_s** : URL du fichier principal (si disponible)
- **files_s** : Liste de tous les fichiers
- Tous les fichiers ne sont pas en open access
- Vérifier la licence avant utilisation

## Collections Spécialisées

### HAL-SHS
Pour limiter aux SHS uniquement :
```
fq=collCode_s:SHS
```

### Institutions
Filtrer par établissement :
```
fq=structure_t:"Université Paris 1"
```

## Conseils d'Utilisation

1. **Toujours spécifier wt=json** pour faciliter le parsing
2. **Utiliser fq plutôt que q** pour les filtres (meilleure performance)
3. **Limiter les champs retournés** avec `fl` pour réduire la bande passante
4. **Combiner plusieurs fq** : chaque fq est un filtre indépendant
5. **Encoder les URLs** : utiliser %20 pour espaces, etc.
6. **Vérifier numFound** avant de paginer

## Pagination Efficace

Pour parcourir de nombreux résultats :

```bash
# Page 1 (résultats 0-19)
curl "https://api.archives-ouvertes.fr/search/?q=...&rows=20&start=0&wt=json"

# Page 2 (résultats 20-39)
curl "https://api.archives-ouvertes.fr/search/?q=...&rows=20&start=20&wt=json"

# Page 3 (résultats 40-59)
curl "https://api.archives-ouvertes.fr/search/?q=...&rows=20&start=40&wt=json"
```

## Limitations

- Maximum 10,000 résultats par requête
- Métadonnées uniquement (texte intégral variable)
- Mise à jour continue mais délai possible
- Pas de garantie sur la disponibilité des fichiers

## Ressources Additionnelles

- Documentation : https://api.archives-ouvertes.fr/docs
- Formulaire de recherche : https://hal.archives-ouvertes.fr/search
- Support : hal-support@ccsd.cnrs.fr
