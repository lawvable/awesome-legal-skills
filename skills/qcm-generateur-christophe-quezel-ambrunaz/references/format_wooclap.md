# Format Excel Wooclap - Spécifications techniques

## Structure du tableur

| Type | Title | Correct | Choice | Choice | Choice | Choice |
|------|-------|---------|--------|--------|--------|--------|
| MCQ | Énoncé question 1 | 2 | Réponse A | Réponse B | Réponse C | Réponse D |
| MCQ | Énoncé question 2 | 1,3 | Réponse A | Réponse B | Réponse C | Réponse D |

## Colonnes obligatoires

### Type
**Valeur** : `MCQ` (pour QCM)
Autres types disponibles mais hors scope : Rating, OpenQuestion, Poll, etc.

### Title
**Contenu** : Énoncé complet de la question
**Format** : Texte libre
**LaTeX supporté** : `$formule$`

### Correct
**Choix unique** : Numéro de colonne (1, 2, 3, 4...)
**Choix multiple** : Numéros séparés par virgules (1,3 ou 2,4)

Exemple :
- `2` → La 2ème réponse (Choice colonne 2) est correcte
- `1,3` → Les 1ère et 3ème réponses sont correctes

### Choice (colonnes multiples)
Une colonne par option de réponse.
Minimum 2, recommandé 4-6 colonnes Choice.

## Encodage et format

- **Format** : .xlsx (Excel)
- **Encodage** : UTF-8 (géré automatiquement par Excel)
- **Première ligne** : En-têtes (Type, Title, Correct, Choice, Choice, ...)
- **LaTeX** : `$E = mc^2$` pour formules mathématiques

## Exemple complet

```
Type  | Title                                    | Correct | Choice       | Choice       | Choice       | Choice
------|------------------------------------------|---------|--------------|--------------|--------------|-------------
MCQ   | Quelle est la capitale de la France ?    | 1       | Paris        | Londres      | Berlin       | Madrid
MCQ   | Quelles sont les couleurs du drapeau ?   | 1,2,3   | Bleu         | Blanc        | Rouge        | Vert
MCQ   | La formule $E=mc^2$ est de qui ?         | 2       | Newton       | Einstein     | Planck       | Bohr
```

## Génération avec Python

Utiliser openpyxl ou xlsxwriter :

```python
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['Type', 'Title', 'Correct', 'Choice', 'Choice', 'Choice', 'Choice'])
ws.append(['MCQ', 'Énoncé ?', '1', 'Réponse A', 'Réponse B', 'Réponse C', 'Réponse D'])
wb.save('qcm_wooclap.xlsx')
```

## Limitations

- Pas de feedbacks dans le fichier Excel (à ajouter manuellement dans Wooclap après import)
- Pas de pondération fine (système Wooclap gère automatiquement)
