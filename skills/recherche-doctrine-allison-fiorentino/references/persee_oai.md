# Persée OAI-PMH — Référence Complète

## Vue d'ensemble

Persée est un programme de numérisation et de diffusion en ligne des collections rétrospectives de revues scientifiques françaises. Il offre un accès libre à plus de 800 000 documents en texte intégral, dont de nombreuses revues juridiques historiques.

L'accès programmatique se fait via le protocole OAI-PMH (Open Archives Initiative Protocol for Metadata Harvesting).

**Base URL OAI** : https://oai.persee.fr/oai

## Intérêt pour la Recherche Juridique

- **Collections rétrospectives** : articles de revues juridiques depuis le XIXe siècle
- **Texte intégral** : accès libre et gratuit
- **Qualité OCR** : textes numérisés et corrigés
- **Stabilité des URLs** : identifiants pérennes

## Protocole OAI-PMH — Requêtes de Base

### 1. Identifier le dépôt

```bash
curl "https://oai.persee.fr/oai?verb=Identify"
```

### 2. Lister les collections (Sets)

```bash
curl "https://oai.persee.fr/oai?verb=ListSets"
```

Retourne la liste complète des collections/revues disponibles.

### 3. Lister les formats de métadonnées

```bash
curl "https://oai.persee.fr/oai?verb=ListMetadataFormats"
```

Formats disponibles :
- `oai_dc` : Dublin Core simple (recommandé)
- `mets` : METS (plus détaillé)

### 4. Lister les enregistrements d'une collection

```bash
curl "https://oai.persee.fr/oai?verb=ListRecords&metadataPrefix=oai_dc&set=NOM_COLLECTION"
```

### 5. Obtenir un enregistrement spécifique

```bash
curl "https://oai.persee.fr/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=IDENTIFIANT"
```

## Collections Juridiques Principales

Voici les collections Persée pertinentes pour le droit (noms de sets) :

| Set | Revue | Période approximative |
|-----|-------|----------------------|
| `revue_rfsp` | Revue française de science politique | 1951-2004 |
| `revue_ridc` | Revue internationale de droit comparé | 1949-2014 |
| `revue_ride` | Revue internationale de droit économique | 1987-2014 |
| `revue_adef` | Annales de droit et de sciences politiques | Historique |
| `revue_rcdip` | Revue critique de droit international privé | 1934-2005 |
| `revue_lgdj` | Publications LGDJ diverses | Variable |
| `revue_reco` | Revue économique | 1950-2014 |
| `revue_rfas` | Revue française des affaires sociales | 1967-2014 |
| `revue_pop` | Population | 1946-2014 |

Note : La liste complète s'obtient via `ListSets`. Les noms exacts des sets peuvent varier — toujours vérifier avec la requête ListSets.

## Structure de Réponse OAI-PMH (Dublin Core)

```xml
<OAI-PMH>
  <ListRecords>
    <record>
      <header>
        <identifier>oai:persee:article/ridc_0035-3337_2023_num_75_1_21250</identifier>
        <datestamp>2023-06-15</datestamp>
        <setSpec>revue_ridc</setSpec>
      </header>
      <metadata>
        <oai_dc:dc>
          <dc:title>Titre de l'article</dc:title>
          <dc:creator>Nom, Prénom</dc:creator>
          <dc:subject>Droit comparé</dc:subject>
          <dc:description>Résumé de l'article...</dc:description>
          <dc:publisher>Société de législation comparée</dc:publisher>
          <dc:date>2023</dc:date>
          <dc:type>article</dc:type>
          <dc:format>application/pdf</dc:format>
          <dc:identifier>https://www.persee.fr/doc/ridc_0035-3337_2023_num_75_1_21250</dc:identifier>
          <dc:language>fr</dc:language>
          <dc:rights>free</dc:rights>
        </oai_dc:dc>
      </metadata>
    </record>
  </ListRecords>
</OAI-PMH>
```

## Filtrage par Date

OAI-PMH supporte le filtrage temporel :

```bash
# Documents ajoutés/modifiés depuis une date
curl "https://oai.persee.fr/oai?verb=ListRecords&metadataPrefix=oai_dc&set=revue_ridc&from=2020-01-01"

# Documents ajoutés/modifiés avant une date
curl "https://oai.persee.fr/oai?verb=ListRecords&metadataPrefix=oai_dc&set=revue_ridc&until=2000-12-31"

# Dans une plage de dates
curl "https://oai.persee.fr/oai?verb=ListRecords&metadataPrefix=oai_dc&set=revue_ridc&from=1990-01-01&until=2000-12-31"
```

**Attention** : `from` et `until` filtrent par date de mise en ligne/modification dans Persée, pas par date de publication originale de l'article.

## Pagination (resumptionToken)

Pour les grandes collections, OAI-PMH utilise un système de tokens :

```bash
# Première page
curl "https://oai.persee.fr/oai?verb=ListRecords&metadataPrefix=oai_dc&set=revue_ridc"
# → Retourne un <resumptionToken>TOKEN_VALUE</resumptionToken>

# Pages suivantes
curl "https://oai.persee.fr/oai?verb=ListRecords&resumptionToken=TOKEN_VALUE"
```

Le token est retourné à la fin de chaque page de résultats. Quand il est vide, tous les résultats ont été parcourus.

## Accès Direct aux Articles

Les URLs Persée suivent un format prévisible :

```
https://www.persee.fr/doc/REVUE_ISSN_ANNEE_num_VOL_NUM_PAGEID
```

Exemple :
```
https://www.persee.fr/doc/ridc_0035-3337_2023_num_75_1_21250
```

## API REST Persée (Complément)

En plus de l'OAI-PMH, Persée offre un accès REST via data.persee.fr :

```bash
# Recherche dans les données Persée (SPARQL endpoint)
curl "https://data.persee.fr/sparql?query=SELECT+*+WHERE+{?s+?p+?o}+LIMIT+10&format=json"
```

Le SPARQL endpoint est plus flexible mais plus complexe. Pour la plupart des usages, l'OAI-PMH suffit.

## Exemples Pratiques

### 1. Explorer la Revue internationale de droit comparé

```bash
# Premiers articles de la RIDC
curl "https://oai.persee.fr/oai?verb=ListRecords&metadataPrefix=oai_dc&set=revue_ridc"
```

### 2. Récupérer un article spécifique

```bash
curl "https://oai.persee.fr/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:persee:article/ridc_0035-3337_2023_num_75_1_21250"
```

### 3. Lister toutes les collections disponibles

```bash
curl "https://oai.persee.fr/oai?verb=ListSets" | grep -i "droit\|juridique\|law"
```

## Parsing des Réponses XML

Les réponses OAI-PMH sont en XML. Pour les parser en bash :

```bash
# Avec xmllint (si disponible)
curl "https://oai.persee.fr/oai?verb=ListRecords&metadataPrefix=oai_dc&set=revue_ridc" | \
  xmllint --xpath '//dc:title/text()' -

# Avec Python
python3 -c "
import xml.etree.ElementTree as ET
import urllib.request
url = 'https://oai.persee.fr/oai?verb=ListRecords&metadataPrefix=oai_dc&set=revue_ridc'
response = urllib.request.urlopen(url).read()
root = ET.fromstring(response)
ns = {'dc': 'http://purl.org/dc/elements/1.1/', 'oai_dc': 'http://www.openarchives.org/OAI/2.0/oai_dc/'}
for record in root.iter('{http://www.openarchives.org/OAI/2.0/}record'):
    title = record.find('.//dc:title', ns)
    creator = record.find('.//dc:creator', ns)
    if title is not None:
        print(f'{creator.text if creator is not None else \"?\"} - {title.text}')
"
```

## Limitations

- **Protocole OAI-PMH** : Conçu pour le moissonnage, pas la recherche full-text
- **Pas de recherche par mots-clés** : On parcourt les collections, on ne cherche pas dedans
- **Collections rétrospectives** : Pas de publications récentes (embargo éditeur)
- **Format XML** : Plus complexe à parser que JSON
- **Débit** : Pagination séquentielle, pas de recherche parallèle

Pour la recherche par mots-clés dans Persée, privilégier ISIDORE qui indexe Persée.

## Quand Utiliser Persée OAI vs ISIDORE

| Besoin | Outil recommandé |
|--------|-----------------|
| Recherche par mots-clés | ISIDORE (indexe Persée) |
| Parcourir une collection complète | Persée OAI |
| Accéder aux métadonnées détaillées d'un article | Persée OAI |
| Doctrine historique d'une revue précise | Persée OAI |
| Recherche thématique large | ISIDORE |

## Ressources

- **Portail Persée** : https://www.persee.fr
- **Documentation technique** : https://www.persee.fr/entrepot-oai
- **SPARQL endpoint** : https://data.persee.fr
