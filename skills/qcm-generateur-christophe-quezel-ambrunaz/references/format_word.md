# Format Word - Spécifications techniques

## Vue d'ensemble

Le format Word génère un document .docx complet structuré en trois parties :
1. **Feuille de questions** : Pour distribution aux étudiants (avec cases à cocher)
2. **Grille de correction rapide** : Tableau synthétique des réponses
3. **Corrigé détaillé** : Feedbacks complets pour chaque question

**Usage** : Examens papier, contrôles imprimés, ou export pour archivage/documentation.

## Structure du document

### Partie 1 : Feuille de questions (pour étudiants)

#### En-tête du document

```
QCM - [Titre/Thématique]
Date : [Date de génération]
Niveau : [Primaire/Collège/Lycée/Licence/Master]
Durée estimée : [Calculée automatiquement : nombre de questions × 1-2 minutes]

Nom : ___________________________  Prénom : ___________________________

Instructions :
- Cochez la ou les case(s) correspondant à votre/vos réponse(s)
- Pour les questions à réponses multiples, plusieurs cases peuvent être cochées
- Une réponse fausse peut entraîner une pénalité [si applicable]
```

#### Format par question

```markdown
**Question [N] :**  [Énoncé de la question]

☐ A. [Texte réponse A]
☐ B. [Texte réponse B]
☐ C. [Texte réponse C]
☐ D. [Texte réponse D]
[☐ E. [Texte réponse E]] (si 5+ réponses)

---
```

**Caractéristiques** :
- Cases à cocher Unicode : ☐ (U+2610)
- Numérotation claire et visible
- Espacement entre questions pour lisibilité
- Pas de couleurs (pour compatibilité impression N&B)

#### Exemple complet d'une question

```
Question 1 : Quelle est la capitale de la France ?

☐ A. Paris
☐ B. Londres
☐ C. Berlin
☐ D. Madrid

---

Question 2 : Quelles sont les couleurs du drapeau français ? (Plusieurs réponses possibles)

☐ A. Bleu
☐ B. Blanc
☐ C. Rouge
☐ D. Vert

---
```

#### Saut de page

Après la dernière question, insérer un **saut de page** avant le corrigé pour faciliter l'impression séparée.

---

### Partie 2 : Grille de correction rapide

#### En-tête

```
═══════════════════════════════════
        GRILLE DE CORRECTION
═══════════════════════════════════
```

#### Format du tableau

Tableau à 2 colonnes avec bordures visibles :

```
┌─────────────┬──────────────────────────────────┐
│  Question   │     Réponse(s) correcte(s)       │
├─────────────┼──────────────────────────────────┤
│      1      │              A                   │
│      2      │            A, B, C               │
│      3      │              B                   │
│     ...     │             ...                  │
└─────────────┴──────────────────────────────────┘
```

**Règles de formatage** :
- **Choix unique** : Une seule lettre (ex: `A`)
- **Choix multiple** : Lettres séparées par virgules (ex: `A, B, C`)
- **Ordre** : Toujours alphabétique, même si réponses randomisées à l'origine
- **Alignement** : Centré dans les cellules

#### Exemple de grille complète

```
┌─────────────┬──────────────────────────────────┐
│  Question   │     Réponse(s) correcte(s)       │
├─────────────┼──────────────────────────────────┤
│      1      │              A                   │
│      2      │            A, B, C               │
│      3      │              B                   │
│      4      │              D                   │
│      5      │            B, D                  │
│      6      │              C                   │
│      7      │              A                   │
│      8      │            A, C                  │
│      9      │              B                   │
│     10      │              D                   │
└─────────────┴──────────────────────────────────┘
```

**Note** : Cette grille permet une correction manuelle rapide sans avoir à consulter le corrigé détaillé pour chaque copie.

#### Saut de page

Après la grille de correction, insérer un **saut de page** avant le corrigé détaillé.

---

### Partie 3 : Corrigé détaillé avec feedbacks

#### En-tête

```
═══════════════════════════════════
        CORRIGÉ DÉTAILLÉ
═══════════════════════════════════
```

#### Format par question

```markdown
═══════════════════════════════════
Question [N]
═══════════════════════════════════

**Énoncé :** [Texte complet de la question]

**Réponses proposées :**
A. [Texte réponse A]
B. [Texte réponse B]
C. [Texte réponse C]
D. [Texte réponse D]

**Réponse(s) correcte(s) : [Lettre(s)]**

---

**FEEDBACK - Réponse correcte ([Lettre]) :**
[Feedback détaillé expliquant pourquoi cette réponse est correcte, avec contextualisation, références, etc.]

**FEEDBACK - Réponse A :** [si A incorrecte]
[Explication de pourquoi cette réponse est incorrecte, identification de l'erreur conceptuelle, orientation vers la compréhension correcte]

**FEEDBACK - Réponse B :** [si B incorrecte]
[...]

**FEEDBACK - Réponse C :** [si C incorrecte]
[...]

**FEEDBACK - Réponse D :** [si D incorrecte]
[...]

**Sources consultées :**
- [Source 1]
- [Source 2]

═══════════════════════════════════
```

#### Exemple complet d'une question avec feedbacks

```
═══════════════════════════════════
Question 1
═══════════════════════════════════

Énoncé : Quelle est la capitale de la France ?

Réponses proposées :
A. Paris
B. Londres
C. Berlin
D. Madrid

Réponse correcte : A

---

FEEDBACK - Réponse correcte (A) :
Exact. Paris est la capitale de la France depuis 987, date à laquelle Hugues Capet établit sa résidence dans l'Île de la Cité. La ville a depuis lors maintenu son statut de capitale politique, administrative et culturelle de la France. Paris compte aujourd'hui environ 2,2 millions d'habitants dans la ville elle-même et plus de 12 millions dans l'aire urbaine.

FEEDBACK - Réponse B :
Londres est la capitale du Royaume-Uni, pas de la France. Cette confusion est fréquente car les deux villes sont des capitales européennes majeures séparées par seulement 340 kilomètres. Londres et Paris ont historiquement entretenu des relations complexes, oscillant entre rivalité et coopération.

FEEDBACK - Réponse C :
Berlin est la capitale de l'Allemagne depuis la réunification en 1990. Cette erreur peut provenir d'une confusion entre grandes capitales européennes. Berlin se situe à environ 880 kilomètres à l'est de Paris.

FEEDBACK - Réponse D :
Madrid est la capitale de l'Espagne, pays voisin de la France au sud. Cette confusion géographique est compréhensible pour qui débuterait l'étude de la géographie européenne, mais les deux capitales se distinguent par leur histoire, leur culture et leur position géographique.

Sources consultées :
- INSEE, Démographie de Paris, 2024
- Encyclopédie Universalis, "Paris - Histoire"

═══════════════════════════════════
```

## Mise en page et formatage

### Police et tailles

- **Titre principal** : Arial ou Calibri, 16pt, gras
- **Titres de sections** : Arial ou Calibri, 14pt, gras
- **Numéros de questions** : 12pt, gras
- **Énoncés** : 11pt, normal
- **Réponses** : 11pt, normal
- **Feedbacks** : 11pt, normal ou italique pour distinction

### Espacements

- **Entre questions** : 1,5 lignes
- **Avant feedbacks** : 1 ligne
- **Entre feedbacks** : 0,5 ligne
- **Marges** : 2,5 cm de chaque côté

### Numérotation des pages

- **Pied de page** : "Page X / Y" centré
- **En-tête optionnel** : Titre du QCM (répété sur chaque page)

### Couleurs (optionnelles, pour version numérique)

Si le document est destiné à usage numérique et non impression :
- Réponses correctes surlignées en **vert clair** (#D4EDDA)
- Titres de sections en **bleu foncé** (#0056B3)

Pour impression N&B, utiliser uniquement :
- **Gras** pour réponses correctes
- Bordures de tableau en noir

## Génération avec python-docx

### Structure du code

```python
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Créer document
doc = Document()

# === PARTIE 1 : FEUILLE DE QUESTIONS ===

# En-tête
heading = doc.add_heading('QCM - Droit de la Responsabilité Civile', level=1)
doc.add_paragraph(f'Date : {date}')
doc.add_paragraph(f'Niveau : {niveau}')
doc.add_paragraph(f'Durée estimée : {duree} minutes')
doc.add_paragraph()
doc.add_paragraph('Nom : ___________________________  Prénom : ___________________________')
doc.add_paragraph()

# Instructions
doc.add_heading('Instructions', level=2)
instructions = [
    'Cochez la ou les case(s) correspondant à votre/vos réponse(s)',
    'Pour les questions à réponses multiples, plusieurs cases peuvent être cochées',
    'Une réponse fausse entraîne une pénalité de -0.25 point'
]
for inst in instructions:
    p = doc.add_paragraph(inst, style='List Bullet')

doc.add_paragraph()

# Questions
for i, question in enumerate(questions, 1):
    # Numéro et énoncé
    doc.add_heading(f'Question {i} :', level=3)
    doc.add_paragraph(question['enonce'])
    doc.add_paragraph()
    
    # Réponses avec cases à cocher
    for lettre, reponse in question['reponses'].items():
        p = doc.add_paragraph()
        p.add_run(f'☐ {lettre}. {reponse}')
    
    doc.add_paragraph()
    doc.add_paragraph('─' * 50)  # Séparateur
    doc.add_paragraph()

# Saut de page
doc.add_page_break()

# === PARTIE 2 : GRILLE DE CORRECTION ===

doc.add_heading('GRILLE DE CORRECTION', level=1)
doc.add_paragraph()

# Tableau
table = doc.add_table(rows=len(questions)+1, cols=2)
table.style = 'Light Grid Accent 1'

# En-têtes de tableau
header_cells = table.rows[0].cells
header_cells[0].text = 'Question'
header_cells[1].text = 'Réponse(s) correcte(s)'

# Remplir le tableau
for i, question in enumerate(questions, 1):
    row_cells = table.rows[i].cells
    row_cells[0].text = str(i)
    row_cells[1].text = question['reponses_correctes']  # Ex: "A" ou "A, B, C"

# Saut de page
doc.add_page_break()

# === PARTIE 3 : CORRIGÉ DÉTAILLÉ ===

doc.add_heading('CORRIGÉ DÉTAILLÉ', level=1)

for i, question in enumerate(questions, 1):
    doc.add_paragraph('═' * 50)
    doc.add_heading(f'Question {i}', level=2)
    doc.add_paragraph('═' * 50)
    doc.add_paragraph()
    
    # Énoncé
    p = doc.add_paragraph()
    p.add_run('Énoncé : ').bold = True
    p.add_run(question['enonce'])
    doc.add_paragraph()
    
    # Réponses proposées
    doc.add_paragraph('Réponses proposées :').bold = True
    for lettre, texte in question['reponses'].items():
        doc.add_paragraph(f'{lettre}. {texte}')
    doc.add_paragraph()
    
    # Réponse correcte
    p = doc.add_paragraph()
    p.add_run(f'Réponse(s) correcte(s) : {question["reponses_correctes"]}').bold = True
    doc.add_paragraph()
    doc.add_paragraph('─' * 50)
    doc.add_paragraph()
    
    # Feedbacks
    for lettre, feedback in question['feedbacks'].items():
        p = doc.add_paragraph()
        p.add_run(f'FEEDBACK - {feedback["titre"]} :').bold = True
        doc.add_paragraph(feedback['texte'])
        doc.add_paragraph()
    
    # Sources
    if question.get('sources'):
        doc.add_paragraph('Sources consultées :').bold = True
        for source in question['sources']:
            doc.add_paragraph(f'- {source}', style='List Bullet')
    
    doc.add_paragraph()
    doc.add_paragraph('═' * 50)
    doc.add_paragraph()

# Sauvegarder
doc.save('qcm_complet.docx')
```

## Variantes et adaptations

### Variante 1 : Version étudiante seule

Générer uniquement la Partie 1 (feuille de questions) pour distribution aux étudiants.

### Variante 2 : Version enseignant seule

Générer uniquement Parties 2 et 3 (grille + corrigé détaillé) pour l'enseignant.

### Variante 3 : Questions numérotées sans cases

Remplacer les cases à cocher par :
```
Question 1 : [Énoncé]
A. [Réponse A]
B. [Réponse B]
C. [Réponse C]
D. [Réponse D]

Réponse(s) choisie(s) : __________
```

### Variante 4 : Feedbacks simplifiés

Pour un corrigé moins volumineux, limiter les feedbacks à :
- Feedback de la réponse correcte uniquement
- Mention courte de l'erreur pour distracteurs (1 phrase)

## Gestion de la randomisation

**Important** : Les réponses dans le document Word sont déjà dans l'ordre randomisé.

**Conséquence** :
- Dans la feuille de questions, les réponses apparaissent dans l'ordre A, B, C, D après randomisation
- Dans la grille de correction, indiquer la/les lettre(s) correspondant à la position après randomisation
- Dans le corrigé détaillé, les feedbacks suivent l'ordre A, B, C, D du document

**Exemple** :
Si la bonne réponse "Paris" se retrouve en position C après randomisation :
- Feuille de questions : `☐ C. Paris`
- Grille de correction : `Question 1 : C`
- Corrigé détaillé : Feedback marqué "Réponse correcte (C)"

## Validation avant génération

### Checklist

- [ ] En-tête complet avec toutes les métadonnées
- [ ] Instructions claires pour les étudiants
- [ ] Cases à cocher Unicode (☐) bien affichées
- [ ] Numérotation cohérente (1, 2, 3...)
- [ ] Sauts de page entre les 3 parties
- [ ] Grille de correction complète et alignée
- [ ] Tous les feedbacks présents (bonne réponse + distracteurs)
- [ ] Sources documentées pour chaque question
- [ ] Mise en page homogène
- [ ] Pagination fonctionnelle

## Avantages du format Word

- ✅ Impression facile pour examens papier
- ✅ Distribution physique aux étudiants
- ✅ Archivage documentation qualité (traçabilité)
- ✅ Édition manuelle possible (ajustements de dernière minute)
- ✅ Conversion facile en PDF
- ✅ Compatible avec tous les systèmes (Windows, Mac, Linux)
- ✅ Pas de dépendance à une plateforme LMS

## Utilisation recommandée

### Pour enseignant

1. Imprimer **Partie 1** uniquement pour distribution aux étudiants
2. Conserver **Partie 2** (grille) pour correction rapide
3. Consulter **Partie 3** (corrigé détaillé) en cas de :
   - Contestation de note
   - Demande d'explication détaillée
   - Préparation de séance de correction collective

### Pour étudiant (version complète fournie après examen)

1. Consulter **Partie 2** pour vérifier rapidement ses réponses
2. Lire **Partie 3** pour comprendre ses erreurs et apprendre

## Exportation vers autres formats

À partir du document Word généré :

- **PDF** : Enregistrer sous > PDF (préserve mise en page)
- **HTML** : Enregistrer sous > Page web filtrée
- **ODT** : Enregistrer sous > OpenDocument (LibreOffice)

## Notes finales

Le format Word constitue le format le plus polyvalent pour l'enseignement traditionnel. Il combine :
- Flexibilité d'utilisation (numérique ou papier)
- Richesse pédagogique (feedbacks complets)
- Accessibilité universelle (pas de plateforme requise)
- Traçabilité académique (archivage, qualité)

**Recommandation** : Pour tout QCM approfondi destiné à une évaluation certificative, générer systématiquement la version Word en complément des autres formats, ne serait-ce que pour archivage institutionnel.
