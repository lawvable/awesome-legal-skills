# Instructions d'utilisation - Fichier Excel Wooclap

Votre QCM a été généré au format Excel compatible avec l'importation directe dans Wooclap.

## Caractéristiques du fichier généré

- **Format** : Excel (.xlsx)
- **Structure** : Tableau avec colonnes Type, Title, Correct, Choice (×N)
- **Encodage** : UTF-8 intégré
- **Contenu** : Questions formatées selon les spécifications Wooclap

## Structure du fichier

Le tableur contient les colonnes suivantes :

| Colonne | Description | Exemple |
|---------|-------------|---------|
| **Type** | Type de question (toujours "MCQ" pour QCM) | MCQ |
| **Title** | Énoncé complet de la question | Quelle est la capitale de la France ? |
| **Correct** | Numéro(s) de la/des bonne(s) réponse(s) | `2` (choix unique) ou `1,3` (multiple) |
| **Choice** | Propositions de réponses (une par colonne) | Paris, Londres, Berlin, Madrid |

## Procédure d'importation dans Wooclap

### Étape 1 : Accéder à votre compte Wooclap

1. Connectez-vous sur [https://app.wooclap.com](https://app.wooclap.com)
2. Authentifiez-vous avec vos identifiants institutionnels ou personnels

### Étape 2 : Créer un événement

1. Cliquez sur **Créer un événement**
2. Nommez votre événement (ex : "QCM Thermodynamique - Séance 3")
3. Choisissez le mode :
   - **Session en direct** : Rythme imposé par l'enseignant (recommandé pour cours magistral)
   - **Session en autonomie** : Chaque étudiant progresse à son rythme (recommandé pour auto-évaluation)

### Étape 3 : Importer les questions

1. Dans l'événement créé, cliquez sur **Importer des questions**
2. Sélectionnez **Depuis un fichier Excel**
3. Cliquez sur **Importer un classeur Excel**
4. Sélectionnez le fichier `.xlsx` généré
5. Cliquez sur **Ouvrir**

### Étape 4 : Vérification automatique

Wooclap importe les questions automatiquement. Vérifiez :
- Le nombre de questions importées correspond à vos attentes
- Les questions s'affichent correctement dans la liste
- Aucun message d'erreur n'apparaît

### Étape 5 : Prévisualisation et ajustements

1. **Parcourez chaque question** :
   - Cliquez sur chaque question dans la liste
   - Vérifiez l'énoncé, les réponses et la/les réponse(s) correcte(s)
   - Vérifiez le rendu des formules LaTeX (si présentes)

2. **Modifications possibles** :
   - Cliquez sur l'icône de modification (crayon) pour chaque question
   - Ajustez le texte, les réponses, ou l'indication de la bonne réponse
   - Réorganisez l'ordre des questions (glisser-déposer)

### Étape 6 : Configuration de l'événement

1. **Paramètres généraux** (icône engrenage) :
   - Mode de participation (avec ou sans authentification)
   - Affichage des résultats (immédiat ou différé)
   - Nombre de tentatives autorisées
   - Mélange aléatoire des réponses

2. **Options de notation** (si en mode autonomie) :
   - Note de passage
   - Feedback immédiat ou à la fin
   - Affichage du score

### Étape 7 : Lancement

#### Pour une session en direct :
1. Cliquez sur **Lancer**
2. Un code de participation est généré (ex : ABCD12)
3. Les étudiants se connectent sur **www.wooclap.com** et saisissent le code
4. Vous contrôlez le passage d'une question à l'autre
5. Affichez ou masquez les résultats en temps réel

#### Pour une session en autonomie :
1. Cliquez sur **Partager**
2. Choisissez le mode de partage :
   - Lien direct
   - QR Code
   - Intégration LMS (Moodle, Canvas, etc.)
3. Les étudiants accèdent au questionnaire et progressent à leur rythme

## Vérifications recommandées

### Avant le lancement
- [ ] Testez le questionnaire en mode prévisualisation
- [ ] Vérifiez que les bonnes réponses sont correctement identifiées
- [ ] Assurez-vous que les formules mathématiques s'affichent correctement
- [ ] Contrôlez que les paramètres de notation sont appropriés

### Pendant la session (mode direct)
- [ ] Surveillez le taux de participation
- [ ] Observez les résultats en temps réel pour ajuster le rythme
- [ ] Utilisez les résultats pour identifier les points à clarifier

### Après la session
- [ ] Exportez les résultats (Format Excel ou CSV)
- [ ] Analysez les questions où le taux d'erreur est élevé
- [ ] Consultez les rapports individuels si nécessaire

## Fonctionnalités avancées Wooclap

### Mélange des réponses
Les réponses peuvent être présentées dans un ordre aléatoire pour chaque étudiant, limitant ainsi la copie.

### Feedback pédagogique
Bien que le fichier Excel généré ne contienne pas de feedbacks (limitation du format), vous pouvez les ajouter manuellement dans Wooclap :
1. Éditez chaque question
2. Ajoutez un message de feedback dans le champ prévu
3. Le feedback s'affichera après la réponse de l'étudiant

### Intégration LMS
Wooclap peut être intégré directement dans Moodle, Canvas, Blackboard :
- Les notes sont synchronisées automatiquement
- Les étudiants accèdent directement depuis le LMS
- Pas besoin de code de participation

### Collaboration
Vous pouvez partager l'événement avec des collègues pour co-construction ou réutilisation.

## Résolution de problèmes

### Erreur "Format de fichier incorrect"
**Cause** : Le fichier n'est pas un Excel valide ou la structure est incorrecte
**Solution** : 
- Ouvrez le fichier dans Excel pour vérifier qu'il n'est pas corrompu
- Vérifiez que la première ligne contient bien les en-têtes : Type, Title, Correct, Choice...

### Questions non importées
**Cause** : Cellules vides ou format incorrect dans la colonne "Correct"
**Solution** : 
- Vérifiez que chaque ligne a un type "MCQ"
- La colonne "Correct" doit contenir un nombre (ex : 2) ou plusieurs séparés par virgules (ex : 1,3)

### Formules LaTeX non rendues
**Cause** : Syntaxe LaTeX incorrecte ou non supportée
**Solution** : 
- Assurez-vous d'utiliser les délimiteurs `$...$` pour inline ou `$$...$$` pour bloc
- Testez la formule sur un service comme [LaTeX Online Editor](https://latexeditor.lagrida.com/)

### Caractères spéciaux corrompus
**Cause** : Problème d'encodage (rare avec .xlsx)
**Solution** : 
- Ré-enregistrez le fichier depuis Excel en vous assurant de l'encodage UTF-8
- Utilisez LibreOffice Calc comme alternative

## Export des résultats

Après la session, vous pouvez exporter :
- **Résultats par question** : Taux de réussite, réponses données
- **Résultats par participant** : Score individuel, détail des réponses
- **Format disponible** : Excel, CSV, PDF

Procédure :
1. Accédez à votre événement
2. Onglet **Résultats** ou **Rapports**
3. Cliquez sur **Exporter** et choisissez le format

## Documentation Wooclap

- Centre d'aide : [https://docs.wooclap.com/fr/](https://docs.wooclap.com/fr/)
- Importation Excel : [https://docs.wooclap.com/fr/articles/674845](https://docs.wooclap.com/fr/articles/674845)
- Intégration Moodle : [https://docs.wooclap.com/fr/articles/1980934](https://docs.wooclap.com/fr/articles/1980934)

---

**N'hésitez pas à me solliciter en cas de difficulté. Je peux également régénérer le fichier dans un format différent si nécessaire.**
