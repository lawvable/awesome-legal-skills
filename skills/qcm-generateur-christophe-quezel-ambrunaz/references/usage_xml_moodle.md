# Instructions d'utilisation - Fichier XML Moodle

Votre QCM a été généré au format XML Moodle. Ce format est compatible avec Moodle et **peut également être importé directement dans Wooclap**.

## ✨ Import direct dans Wooclap (Nouveauté)

**Le fichier XML Moodle peut être importé dans Wooclap sans conversion !**

### Procédure d'import dans Wooclap

1. Connectez-vous à votre compte Wooclap ([https://app.wooclap.com](https://app.wooclap.com))
2. Cliquez sur **Importer un événement** (bouton en haut de page)
3. Sélectionnez **Moodle XML** comme format source
4. Uploadez le fichier .xml généré
5. Wooclap convertit automatiquement vos questions
6. Cliquez sur **Importer** pour finaliser

**Avantages de l'import XML Moodle dans Wooclap** :
- ✅ Conservation des feedbacks (si QCM approfondi)
- ✅ Préservation de la structure des questions
- ✅ Pas besoin de générer un fichier Excel Wooclap séparé
- ✅ Import plus rapide pour QCM volumineux

**Note** : Pour les QCM légers, vous pouvez toujours utiliser le format Excel Wooclap si vous préférez (plus simple pour petits QCM de 5-15 questions).

---

## Procédure d'importation dans Moodle

Cette section détaille l'importation dans votre cours Moodle.

## Caractéristiques du fichier généré

- **Format** : XML structuré (.xml)
- **Encodage** : UTF-8 avec déclaration XML
- **Norme** : Format XML propriétaire Moodle
- **Contenu** : Questions avec métadonnées complètes, feedbacks et pondérations

## Procédure d'importation dans Moodle

### Étape 1 : Accéder à la banque de questions

1. Connectez-vous à votre cours Moodle
2. Dans le panneau d'administration du cours : **Banque de questions**
3. Sélectionnez l'onglet **Import**

### Étape 2 : Configurer les paramètres d'importation

1. **Format de fichier** : Sélectionnez **Format XML Moodle**
2. **Catégorie de destination** :
   - Option 1 : Sélectionnez une catégorie existante
   - Option 2 : Cochez "Obtenir la catégorie à partir du fichier" si des catégories sont spécifiées dans le XML
   - Option 3 : Cochez "Obtenir le contexte à partir du fichier" pour respecter l'organisation hiérarchique
3. **Gestion des erreurs** : 
   - Recommandé : "Arrêter en cas d'erreur" pour identifier immédiatement tout problème
   - Alternative : "Continuer" pour importer le maximum de questions malgré les erreurs

### Étape 3 : Téléverser le fichier

1. Cliquez sur **Choisir un fichier** ou glissez-déposez le fichier XML
2. Sélectionnez le fichier `.xml` généré
3. Cliquez sur **Importer**

### Étape 4 : Vérification et confirmation

1. **Aperçu pré-importation** :
   - Moodle affiche le nombre de questions détectées
   - Un aperçu des questions apparaît
   - Vérifiez que le nombre correspond à vos attentes

2. **Contrôle visuel** :
   - Parcourez quelques questions pour vérifier le rendu
   - Assurez-vous que les formules, images (si présentes) s'affichent correctement
   - Vérifiez la structure des réponses multiples

3. **Confirmation finale** :
   - Si tout est conforme, cliquez sur **Continuer**
   - Les questions sont désormais dans votre banque

### Étape 5 : Intégration dans un test

1. Créez ou éditez une activité **Test/Quiz**
2. Accédez à l'édition du test : **Modifier le test**
3. Ajoutez les questions :
   - **Ajouter** → **à partir de la banque de questions**
   - Sélectionnez la catégorie contenant vos questions
   - Cochez les questions à inclure ou sélectionnez **Tout**
4. Configurez les paramètres du test (durée, modalités de notation, feedback, etc.)

## Vérifications post-importation indispensables

### Intégrité structurelle
- [ ] Toutes les questions sont présentes (vérifier le nombre)
- [ ] Les types de questions sont corrects (choix unique/multiple)
- [ ] Les catégories sont correctement créées (si applicable)

### Rendu du contenu
- [ ] Les énoncés s'affichent sans corruption
- [ ] Les caractères spéciaux et accentués sont corrects
- [ ] Les formules mathématiques (LaTeX, MathML) sont rendues
- [ ] Les balises HTML ne sont pas visibles en texte brut

### Correction automatique
- [ ] Les bonnes réponses attribuent 100% (ou pondération appropriée)
- [ ] Les mauvaises réponses attribuent 0% ou pénalité correcte
- [ ] Pour les réponses multiples, la somme des fractions = 100%

### Feedbacks
- [ ] Les feedbacks spécifiques s'affichent après réponse
- [ ] Les feedbacks généraux apparaissent (si configurés)
- [ ] Le formatage des feedbacks est préservé

### Test de validation obligatoire
**Procédure recommandée** :
1. Créez un test de validation
2. Activez le mode "Prévisualisation" ou créez un étudiant test
3. Répondez à toutes les questions (correctement et incorrectement)
4. Vérifiez que la notation fonctionne comme attendu
5. Contrôlez l'affichage des feedbacks

## Résolution de problèmes

### Erreur "XML mal formé"
**Symptôme** : Moodle refuse d'importer le fichier
**Causes possibles** :
- Ligne vide avant la déclaration XML `<?xml version="1.0"?>`
- Caractère spécial non échappé dans le contenu
- Balise XML non fermée

**Solutions** :
1. Ouvrez le fichier dans un éditeur XML ou navigateur (Firefox affiche les erreurs XML)
2. Supprimez toute ligne vide avant `<?xml`
3. Vérifiez que tous les `<` et `>` dans le texte sont dans des blocs `<![CDATA[...]]>`

### Caractères corrompus
**Symptôme** : Caractères bizarres (é → Ã©)
**Cause** : Problème d'encodage
**Solution** :
- Assurez-vous que le fichier est bien en UTF-8
- Sur Windows : utilisez Notepad++ pour vérifier/convertir l'encodage
- Sur Mac/Linux : utilisez `file -i fichier.xml` pour vérifier

### Questions importées mais vides
**Symptôme** : Questions visibles mais sans contenu
**Cause** : Balises `<text>` manquantes ou mal placées
**Solution** : Vérifiez la structure XML, particulièrement les balises `<questiontext><text>...</text></questiontext>`

### Feedbacks non affichés
**Cause** : Paramètres du test qui désactivent les feedbacks
**Solution** : 
1. Éditez le test
2. **Paramètres** → **Options de relecture**
3. Activez "Feedback spécifique" et "Feedback général"

### Pondérations incorrectes (réponses multiples)
**Symptôme** : Somme des points ≠ 100%
**Cause** : Erreur dans les attributs `fraction`
**Solution** : 
- Éditez manuellement chaque question dans Moodle
- Ajustez les fractions pour que le total des bonnes réponses = 100%

## Avantages du format XML

Comparé au format GIFT, le XML Moodle offre :
- **Métadonnées complètes** : notes par défaut, pénalités, indices
- **Structure hiérarchique** : catégories et sous-catégories
- **Feedbacks riches** : support HTML complet, images embarquées
- **Interopérabilité** : échange avec d'autres systèmes supportant le format
- **Traçabilité** : informations d'auteur, dates, versions

## Édition post-importation

Toutes les métadonnées XML sont conservées et éditables dans l'interface Moodle :
- Modification du texte des questions/réponses
- Ajustement des pondérations
- Enrichissement des feedbacks
- Ajout de médias (images, vidéos, audio)
- Paramétrage des options avancées

## Documentation de référence

- Format XML Moodle : [https://docs.moodle.org/fr/Format_XML_Moodle](https://docs.moodle.org/fr/Format_XML_Moodle)
- Import de questions : [https://docs.moodle.org/fr/Importer_des_questions](https://docs.moodle.org/fr/Importer_des_questions)

---

**En cas de difficulté persistante, n'hésitez pas à me transmettre le message d'erreur exact affiché par Moodle pour un diagnostic précis.**
