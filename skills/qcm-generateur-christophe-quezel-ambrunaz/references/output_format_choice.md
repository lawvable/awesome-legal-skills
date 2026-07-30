# Choix du format de sortie

Le contenu de votre QCM est désormais validé. Je peux maintenant générer les fichiers finaux dans le format adapté à votre usage.

Les formats disponibles dépendent du **type de QCM** que vous avez choisi (léger ou approfondi).

---

## Formats disponibles pour QCM LÉGER

Votre QCM léger (sans feedbacks, contraintes longueur) peut être exporté vers :

### 🎮 Option A : Kahoot! (.xlsx)
**Format natif optimisé pour Kahoot!**

**Caractéristiques** :
- Format Excel avec colonnes : Question, Answer 1-4, Time limit, Correct answer(s)
- Import direct dans Kahoot! via "Import spreadsheet"
- Respect automatique des contraintes 95/60 caractères
- Temps par question : 20 secondes par défaut (modifiable)

**Idéal pour** : Quiz ludiques en classe, révisions interactives, gamification

---

### 🎯 Option B : Wooclap Excel (.xlsx)
**Format Excel pour import Wooclap**

**Caractéristiques** :
- Structure tabulaire Type/Title/Correct/Choice
- Import direct via interface Wooclap
- Support LaTeX pour formules
- Modifiable dans Excel avant import

**Idéal pour** : Sessions Wooclap interactives, questions en temps réel

---

### 📘 Option C : GIFT (.txt)
**Format texte pour Moodle**

**Caractéristiques** :
- Format texte simple et lisible
- Éditable dans n'importe quel éditeur
- Prise en charge native par Moodle
- Pas de feedbacks (QCM léger)

**Idéal pour** : Import Moodle rapide, banque de questions

---

### 📄 Option D : XML Moodle (.xml)
**Format XML pour Moodle**

**Caractéristiques** :
- Structure XML normalisée
- Métadonnées complètes
- Importable également dans Wooclap via "Importer un événement"
- Pas de feedbacks (QCM léger)

**Idéal pour** : Intégration Moodle avec métadonnées, import Wooclap via XML

---

## Formats disponibles pour QCM APPROFONDI

Votre QCM approfondi (avec feedbacks détaillés) peut être exporté vers :

### 📘 Option A : GIFT (.txt)
**Format texte pour Moodle avec feedbacks**

**Caractéristiques** :
- Format texte incluant feedbacks complets
- Éditable facilement
- Prise en charge native par Moodle
- Syntaxe légère pour feedbacks

**Idéal pour** : Moodle, banque de questions avec feedbacks

---

### 📄 Option B : XML Moodle (.xml)
**Format XML pour Moodle avec feedbacks**

**Caractéristiques** :
- Structure XML complète
- Feedbacks détaillés préservés
- Métadonnées riches
- **BONUS : Importable directement dans Wooclap via "Importer un événement"**

**Idéal pour** : Moodle, Wooclap (préserve feedbacks mieux qu'Excel)

---

### 🎯 Option C : Wooclap Excel (.xlsx)
**Format Excel pour Wooclap**

**Caractéristiques** :
- Structure tabulaire simple
- Import direct Wooclap
- ⚠️ **Limitation** : Feedbacks à ajouter manuellement après import dans Wooclap

**Idéal pour** : Wooclap quand feedbacks non prioritaires ou ajoutés manuellement après

**Note** : Pour préserver les feedbacks dans Wooclap, privilégiez l'Option B (XML Moodle) importable directement.

---

### 📋 Option D : Word (.docx)
**Document complet avec 3 parties**

**Fichier généré contient** :
1. **Feuille de questions** (pour étudiants)
   - Questions numérotées avec cases à cocher ☐
   - Instructions claires
   - Prêt à imprimer et distribuer

2. **Grille de correction rapide** (pour enseignant)
   - Tableau : Question | Réponse(s) correcte(s)
   - Format : "1 → A", "2 → A, B, C"
   - Correction manuelle rapide

3. **Corrigé détaillé avec feedbacks** (pour enseignant et étudiants)
   - Feedbacks complets pour chaque réponse
   - Explications des erreurs conceptuelles
   - Sources documentaires

**Idéal pour** : 
- Examens papier sur table
- Documentation pédagogique et archivage
- Correction collective en classe
- Distribution de corrigés détaillés aux étudiants

---

## Récapitulatif des compatibilités

| Format | QCM Léger | QCM Approfondi | Feedbacks | Moodle | Wooclap | Kahoot! | Papier |
|--------|-----------|----------------|-----------|--------|---------|---------|--------|
| **Kahoot! (.xlsx)** | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Wooclap Excel (.xlsx)** | ✅ | ✅* | ⚠️** | ❌ | ✅ | ❌ | ❌ |
| **GIFT (.txt)** | ✅ | ✅ | ✅*** | ✅ | ❌ | ❌ | ⚠️ |
| **XML Moodle (.xml)** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ |
| **Word (.docx)** | ⚠️ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |

*Disponible mais feedbacks non inclus dans Excel, à ajouter manuellement  
**Feedbacks à ajouter manuellement après import  
***Feedbacks présents seulement si QCM approfondi

---

## Quelle option choisissez-vous ?

Veuillez m'indiquer votre choix selon votre type de QCM :

**Si QCM LÉGER :**
- **A** : Kahoot! (.xlsx)
- **B** : Wooclap Excel (.xlsx)
- **C** : GIFT (.txt)
- **D** : XML Moodle (.xml)

**Si QCM APPROFONDI :**
- **A** : GIFT (.txt) - Moodle avec feedbacks
- **B** : XML Moodle (.xml) - Moodle et Wooclap avec feedbacks
- **C** : Wooclap Excel (.xlsx) - Sans feedbacks intégrés
- **D** : Word (.docx) - Document complet 3 parties

**Plusieurs formats :** Vous pouvez demander plusieurs formats simultanément si vous souhaitez disposer de versions différentes pour des usages distincts (ex: "B et D" pour avoir Moodle + Word).

---

## Recommandations par cas d'usage

### Vous voulez un quiz ludique en classe ?
→ **QCM léger + Kahoot!** (Option A)

### Vous voulez une évaluation Moodle avec feedbacks ?
→ **QCM approfondi + GIFT ou XML Moodle** (Options A ou B)

### Vous voulez un examen papier avec corrigé détaillé ?
→ **QCM approfondi + Word** (Option D)

### Vous voulez Wooclap avec feedbacks préservés ?
→ **QCM approfondi + XML Moodle** (Option B) puis import dans Wooclap

### Vous voulez plusieurs usages ?
→ Demandez **plusieurs formats** (ex: "B et D" pour Moodle + archivage Word)
