# Instructions d'utilisation - Fichier GIFT pour Moodle

Votre QCM a été généré au format GIFT. Voici la procédure complète pour l'importer dans votre cours Moodle.

## Caractéristiques du fichier généré

- **Format** : Fichier texte (.txt)
- **Encodage** : UTF-8 (compatible avec les caractères accentués)
- **Contenu** : Questions formatées selon la syntaxe GIFT de Moodle

## Procédure d'importation dans Moodle

### Étape 1 : Accéder à la banque de questions

1. Connectez-vous à votre cours Moodle
2. Dans le menu d'administration du cours, sélectionnez : **Banque de questions**
3. Cliquez sur l'onglet **Import**

### Étape 2 : Configurer l'importation

1. **Format de fichier** : Sélectionnez **Format GIFT** dans le menu déroulant
2. **Catégorie de destination** : 
   - Choisissez une catégorie existante, ou
   - Cochez "Obtenir la catégorie à partir du fichier" si des catégories sont définies dans le fichier GIFT
3. **Comportement si erreur** : Recommandé : "Arrêter en cas d'erreur"

### Étape 3 : Charger le fichier

1. Cliquez sur **Choisir un fichier**
2. Sélectionnez le fichier `.txt` généré
3. Cliquez sur **Importer**

### Étape 4 : Vérification

1. Moodle affiche un aperçu des questions importées
2. Vérifiez le nombre de questions importées (doit correspondre au nombre attendu)
3. Parcourez les questions pour vérifier que l'importation s'est correctement déroulée
4. Confirmez l'importation

### Étape 5 : Utilisation dans un test

1. Créez ou modifiez une activité **Test**
2. Cliquez sur **Modifier le test**
3. Cliquez sur **Ajouter** puis **à partir de la banque de questions**
4. Sélectionnez les questions importées
5. Configurez les paramètres du test (durée, notes, tentatives, etc.)

## Vérifications recommandées après importation

### Affichage des questions
- Les énoncés s'affichent-ils correctement ?
- Les formules LaTeX (le cas échéant) sont-elles rendues correctement ?
- Les caractères accentués sont-ils préservés ?

### Fonctionnement des réponses
- Les bonnes réponses sont-elles bien marquées comme correctes ?
- Les pondérations (pour réponses multiples) sont-elles appropriées ?
- Les feedbacks s'affichent-ils après chaque réponse ?

### Test de validation
**Fortement recommandé** : Effectuez un test complet en tant qu'étudiant (mode prévisualisation) pour vérifier le comportement de chaque question avant de rendre le test disponible aux étudiants.

## Résolution de problèmes courants

### Erreur d'encodage (caractères accentués mal affichés)
- **Cause** : Le fichier n'est pas en UTF-8
- **Solution** : Ouvrez le fichier dans un éditeur de texte, enregistrez-le explicitement en UTF-8 (sans BOM)

### Caractères de contrôle non échappés
- **Cause** : Un caractère `~`, `=`, `#`, `{`, `}` ou `:` apparaît dans le texte sans antislash
- **Solution** : Éditez le fichier manuellement et ajoutez `\` devant ces caractères

### Questions non importées
- **Cause** : Syntaxe GIFT incorrecte
- **Solution** : Consultez les logs d'erreur Moodle pour identifier la ligne problématique, corrigez la syntaxe

### Feedbacks manquants
- **Cause** : Les feedbacks n'ont pas été générés avec le symbole `#`
- **Solution** : Vérifiez la structure du fichier GIFT

## Modifications post-importation

Une fois importé, vous pouvez modifier chaque question directement dans Moodle :
- Éditer l'énoncé ou les réponses
- Ajouter ou modifier les feedbacks
- Ajuster les pondérations
- Ajouter des images ou des médias

## Documentation Moodle officielle

Pour plus d'informations : [https://docs.moodle.org/fr/Format_GIFT](https://docs.moodle.org/fr/Format_GIFT)

---

**N'hésitez pas à me solliciter si vous rencontrez des difficultés lors de l'importation.**
