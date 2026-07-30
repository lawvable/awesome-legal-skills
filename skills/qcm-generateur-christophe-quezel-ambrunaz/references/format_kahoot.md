# Format Kahoot! - Spécifications techniques

## Vue d'ensemble

Kahoot! utilise un format Excel (.xlsx) pour l'import de questions. Ce format est strictement défini et toute déviation entraîne des erreurs d'import.

**Compatibilité** : Kahoot! n'accepte QUE des QCM légers respectant les contraintes de longueur.

## Structure du tableur

### Colonnes obligatoires (7)

| Colonne | Nom exact | Type | Contrainte |
|---------|-----------|------|------------|
| A | Question | Texte | ≤ 95 caractères |
| B | Answer 1 | Texte | ≤ 60 caractères |
| C | Answer 2 | Texte | ≤ 60 caractères |
| D | Answer 3 | Texte | ≤ 60 caractères (optionnel) |
| E | Answer 4 | Texte | ≤ 60 caractères (optionnel) |
| F | Time limit (seconds) | Nombre | 5, 10, 20, 30, 60, 90, 120, 240 |
| G | Correct answer(s) | Texte | Numéros séparés par virgules |

### Ligne 1 : En-têtes

**Impératif** : La première ligne DOIT contenir exactement ces en-têtes (respecter la casse).

```
Question | Answer 1 | Answer 2 | Answer 3 | Answer 4 | Time limit (seconds) | Correct answer(s)
```

### Lignes suivantes : Questions

Chaque ligne représente une question complète.

## Règles de formatage

### Colonne "Question"

- **Format** : Texte libre
- **Longueur** : Maximum 95 caractères (espaces inclus)
- **Obligatoire** : Oui
- **Caractères spéciaux** : Autorisés (é, à, ç, etc.)

**Exemple conforme** :
```
Quelle est la capitale de la France ?
```

### Colonnes "Answer 1" à "Answer 4"

- **Format** : Texte libre
- **Longueur** : Maximum 60 caractères chacune
- **Obligatoire** : Answer 1 et Answer 2 minimum (Answer 3 et 4 optionnels)
- **Nombre de réponses** : 
  - Minimum : 2
  - Maximum : 4 (plans gratuits) ou 6 (plans payants)
  - **Note** : Notre générateur se limite à 4 réponses pour compatibilité maximale

**Exemple conforme** :
```
Paris | Londres | Berlin | Madrid
```

### Colonne "Time limit (seconds)"

- **Format** : Nombre entier
- **Valeurs autorisées** : 5, 10, 20, 30, 60, 90, 120, 240
- **Recommandation** : 20 secondes (défaut)
- **Adaptation** :
  - Questions très simples (définition) : 10 secondes
  - Questions nécessitant réflexion : 30 secondes
  - Questions avec calcul rapide : 60 secondes

**Exemple** :
```
20
```

### Colonne "Correct answer(s)"

- **Format** : Numéros de colonnes séparés par virgules (sans espaces)
- **Numérotation** : 1 = Answer 1, 2 = Answer 2, 3 = Answer 3, 4 = Answer 4
- **Choix unique** : Un seul numéro (ex: `1`)
- **Choix multiple** : Plusieurs numéros séparés par virgules (ex: `1,3`)

**Exemples** :
- Choix unique : `2` (seule la réponse 2 est correcte)
- Choix multiple : `1,3` (les réponses 1 et 3 sont correctes)
- **ATTENTION** : Pas d'espaces → `1,3` et non `1, 3`

## Exemple complet de fichier

```
Question	Answer 1	Answer 2	Answer 3	Answer 4	Time limit (seconds)	Correct answer(s)
Quelle est la capitale de la France ?	Paris	Londres	Berlin	Madrid	20	1
Quels sont les couleurs du drapeau français ?	Bleu	Blanc	Rouge	Vert	20	1,2,3
Qui a écrit "Les Misérables" ?	Victor Hugo	Émile Zola	Gustave Flaubert	Honoré de Balzac	30	1
En quelle année a débuté la Révolution française ?	1789	1792	1799	1804	20	1
```

## Contraintes techniques Kahoot!

### Taille de fichier

- **Maximum** : 1 Mo
- Un fichier standard de 50 questions ≈ 20 Ko → largement sous la limite

### Encodage

- **Format** : .xlsx (Excel 2007 ou supérieur)
- **Encodage** : UTF-8 (géré automatiquement par Excel/openpyxl)

### Types de questions supportés

- ✅ **Quiz** (choix unique)
- ✅ **Multiple answers** (choix multiples)
- ❌ **True/False** (non supporté par import, mais possible dans l'interface)
- ❌ **Puzzle**, **Poll**, **Word cloud**, etc. (non supportables par import)

## Génération avec Python (openpyxl)

```python
import openpyxl

# Créer workbook
wb = openpyxl.Workbook()
ws = wb.active

# En-têtes (ligne 1)
headers = ['Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 
           'Time limit (seconds)', 'Correct answer(s)']
ws.append(headers)

# Exemple de question
question_data = [
    'Quelle est la capitale de la France ?',  # Question
    'Paris',                                    # Answer 1
    'Londres',                                  # Answer 2
    'Berlin',                                   # Answer 3
    'Madrid',                                   # Answer 4
    20,                                         # Time limit
    '1'                                         # Correct answer(s)
]
ws.append(question_data)

# Sauvegarder
wb.save('qcm_kahoot.xlsx')
```

## Gestion des réponses multiples

### Exemple avec 2 bonnes réponses

```python
question_data = [
    'Quelles sont des langues romanes ?',
    'Français',
    'Espagnol',
    'Allemand',
    'Anglais',
    30,
    '1,2'  # Français et Espagnol sont corrects
]
```

### Calcul automatique de la notation

Kahoot! gère automatiquement la notation :
- **Choix unique** : 100% pour la bonne réponse, 0% pour les autres
- **Choix multiple** : Points répartis équitablement entre bonnes réponses, pénalité pour mauvaises

## Randomisation de l'ordre des réponses

**IMPORTANT** : Lors de la génération, les réponses doivent déjà être dans l'ordre randomisé.

**Procédure** :
1. Générer les 4 réponses dans un ordre aléatoire
2. Noter quelle(s) position(s) occupe(nt) la/les bonne(s) réponse(s)
3. Indiquer ces positions dans la colonne "Correct answer(s)"

**Exemple** :
Question : "Quelle est la capitale de la France ?"
Réponse correcte : Paris

Après randomisation :
```
Answer 1: Londres
Answer 2: Berlin
Answer 3: Paris     ← Bonne réponse
Answer 4: Madrid

Correct answer(s): 3
```

## Erreurs courantes et solutions

### Erreur 1 : "Question too long"

**Cause** : Question > 95 caractères

**Solution** : Reformuler selon `references/constraints_light_mcq.md`

### Erreur 2 : "Answer too long"

**Cause** : Une réponse > 60 caractères

**Solution** : Raccourcir la réponse (utiliser nom seul, supprimer dates, etc.)

### Erreur 3 : "Invalid time limit"

**Cause** : Temps non dans la liste autorisée (5, 10, 20, 30, 60, 90, 120, 240)

**Solution** : Arrondir au temps autorisé le plus proche

### Erreur 4 : "Invalid correct answer"

**Cause** : Numéro de réponse incorrect (ex: `5` alors que seulement 4 réponses)

**Solution** : Vérifier que les numéros correspondent aux réponses présentes

### Erreur 5 : "Missing required answer"

**Cause** : Moins de 2 réponses fournies

**Solution** : Toujours fournir au minimum Answer 1 et Answer 2

### Erreur 6 : Espace dans "Correct answer(s)"

**Cause** : `1, 3` au lieu de `1,3`

**Solution** : Supprimer tous les espaces dans cette colonne

## Importation dans Kahoot!

### Procédure

1. Se connecter à Kahoot!
2. Cliquer sur **Create** (en haut à droite)
3. Sélectionner **Kahoot** (type Quiz)
4. Dans le panneau de droite, cliquer sur **Add question** → flèche déroulante
5. Sélectionner **Import spreadsheet**
6. Uploader le fichier .xlsx généré
7. Kahoot! vérifie le fichier et affiche les erreurs éventuelles
8. Cliquer sur **Continue** pour importer

### Après import

- Les questions apparaissent dans le créateur Kahoot!
- Possibilité d'ajouter des images, vidéos, ou médias
- Possibilité de modifier les questions importées
- Possibilité d'ajuster les paramètres (ordre des questions, etc.)

## Limitations par rapport aux autres formats

| Fonctionnalité | Kahoot! | Moodle/GIFT | Wooclap |
|----------------|---------|-------------|---------|
| Feedbacks | ❌ Non | ✅ Oui | ⚠️ Manuels |
| Longueur libre | ❌ Non | ✅ Oui | ✅ Oui |
| Images dans questions | ⚠️ Après import | ✅ Oui | ✅ Oui |
| Plus de 4 réponses | ⚠️ Plans payants | ✅ Oui | ✅ Oui |
| Pondération fine | ❌ Auto | ✅ Oui | ⚠️ Auto |

## Bonnes pratiques

1. **Toujours vérifier les longueurs** avant génération finale
2. **Tester l'import** avec 2-3 questions avant de générer tout le QCM
3. **Privilégier 20 secondes** comme temps par défaut (ajustable après import)
4. **Limiter à 4 réponses** par question pour compatibilité maximale
5. **Utiliser questions courtes et percutantes** adaptées au format ludique
6. **Prévoir ajout manuel** d'images ou médias après import si souhaité

## Validation avant export

### Checklist

- [ ] Toutes les questions ≤ 95 caractères
- [ ] Toutes les réponses ≤ 60 caractères
- [ ] Au moins 2 réponses par question
- [ ] Maximum 4 réponses par question (pour compatibilité)
- [ ] Time limit dans les valeurs autorisées
- [ ] Correct answer(s) sans espaces, numéros valides
- [ ] Format .xlsx (pas .xls ou .csv)
- [ ] Première ligne = en-têtes exacts

## Documentation officielle

Pour plus d'informations : [Kahoot! Help Center - Import from Spreadsheet](https://support.kahoot.com/hc/en-us/articles/115002812547)

---

**Note importante** : Kahoot! est optimisé pour des quiz ludiques et engageants, pas pour des évaluations académiques approfondies. Si votre QCM nécessite contextualisation, nuances, ou feedbacks détaillés, privilégiez le format Moodle/GIFT ou Word.
