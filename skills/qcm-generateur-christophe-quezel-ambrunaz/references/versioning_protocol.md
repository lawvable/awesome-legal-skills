# Protocole de versionnement des QCM

## Principe général

Lorsque l'utilisateur demande des modifications sur un QCM déjà généré, un système de versionnement rigoureux permet de :
- Tracer l'évolution du contenu
- Comparer les versions successives
- Éviter les régressions involontaires
- Maintenir une documentation claire des changements

## Numérotation des versions

### Schéma de numérotation : X.Y

**X = Numéro de version majeure**
- Incrémenté lors de modifications structurelles importantes
- Exemples : ajout/suppression de plusieurs questions, changement de thématique, refonte complète

**Y = Numéro de version mineure**
- Incrémenté lors de modifications localisées
- Exemples : correction d'une question, reformulation d'un distracteur, ajout d'un feedback

### Exemples d'évolution
- **Version 1.0** : QCM initial généré
- **Version 1.1** : Correction de deux distracteurs dans Q3 et Q7
- **Version 1.2** : Ajout d'un feedback détaillé sur Q5
- **Version 2.0** : Suppression de 3 questions et ajout de 5 nouvelles questions

## Structure du changelog

Pour chaque version, documenter systématiquement :

### En-tête de version

```markdown
## Version X.Y - [Date JJ/MM/AAAA]

**Type de modification** : [Mineure / Majeure]
**Demandeur** : [Utilisateur / Révision automatique]
**Raison** : [Brève description de la motivation]
```

### Détail des modifications

Pour chaque modification, indiquer :

1. **Question concernée** (par son numéro et titre)
2. **Type de modification** :
   - Ajout
   - Suppression
   - Modification (préciser l'élément : énoncé, réponse, distracteur, feedback)
3. **Contenu modifié** : Avant → Après
4. **Justification** : Raison pédagogique ou factuelle

### Template de changelog

```markdown
### Modifications détaillées

#### Question N - [Titre abrégé]

**Élément modifié** : [Énoncé / Réponse correcte / Distracteur X / Feedback]

**Avant** :
> [Texte original]

**Après** :
> [Nouveau texte]

**Justification** : [Explication de la modification]

---
```

## Exemple complet de changelog

```markdown
# Changelog - QCM Droit de la Responsabilité Civile

## Version 1.0 - 25/11/2024

**Type de modification** : Initiale
**Demandeur** : Utilisateur
**Raison** : Création du QCM de 10 questions niveau M1

- Génération initiale de 10 questions
- Recherche documentaire effectuée sur Légifrance et doctrine
- Validation des sources selon protocole

---

## Version 1.1 - 26/11/2024

**Type de modification** : Mineure
**Demandeur** : Utilisateur
**Raison** : Amélioration de la précision factuelle et pédagogique

### Modifications détaillées

#### Question 3 - Responsabilité du fait des choses

**Élément modifié** : Distracteur 2

**Avant** :
> "La responsabilité du fait des choses nécessite une faute prouvée"

**Après** :
> "La responsabilité du fait des choses nécessite la preuve du caractère anormal du dommage"

**Justification** : Le premier distracteur confondait responsabilité pour faute et responsabilité du fait des choses (régime objectif). Le nouveau distracteur reflète mieux une erreur conceptuelle courante (confusion avec le régime du trouble anormal de voisinage).

---

#### Question 7 - Préjudice réparable

**Élément modifié** : Feedback de la réponse correcte

**Avant** :
> "Correct. Le préjudice moral est réparable."

**Après** :
> "Excellent. Le préjudice moral est effectivement réparable en droit français depuis l'arrêt de principe de la Cour de cassation (Civ. 1ère, 24 mai 1975). Cette extension du dommage réparable au-delà du seul préjudice matériel constitue une évolution majeure de la responsabilité civile, reflétant une conception extensive de la réparation intégrale. Voir également l'article 1240 du Code civil."

**Justification** : Enrichissement du feedback avec contextualisation historique et référence normative pour renforcer la valeur pédagogique.

---

## Version 2.0 - 27/11/2024

**Type de modification** : Majeure
**Demandeur** : Utilisateur
**Raison** : Ajustement du niveau de difficulté et extension thématique

### Modifications structurelles

- **Suppression** : Questions 2, 5, 9 (niveau trop basique pour M1)
- **Ajout** : 5 nouvelles questions de niveau avancé sur la causalité juridique
- **Réorganisation** : Ordre des questions modifié selon progression difficulté croissante

### Modifications détaillées

#### Question 2 - [SUPPRIMÉE]

**Titre** : Définition de la responsabilité civile

**Raison de suppression** : Question de niveau L1, inadaptée pour un public M1. Remplacée par question plus complexe sur les régimes spéciaux.

---

#### Question 11 - [NOUVELLE] Théorie de la causalité adéquate

**Énoncé** :
> "Selon la théorie de la causalité adéquate, adoptée par certaines juridictions, un fait est considéré comme cause juridique d'un dommage si :"

**Réponse correcte** :
> "Il était de nature, selon le cours normal des choses, à produire ce type de dommage"

**Justification de l'ajout** : Comble une lacune thématique sur les théories de la causalité, sujet central en M1 responsabilité civile.

---
```

## Procédure d'archivage des versions

### Organisation des fichiers

Lors de modifications, créer une copie archivée de la version précédente :

```
/QCM_ResponsabiliteCivile/
├── QCM_v1.0.md (archive)
├── QCM_v1.1.md (archive)
├── QCM_v2.0.md (version actuelle)
└── CHANGELOG.md (document de suivi)
```

### Contenu du fichier CHANGELOG.md

Un fichier unique `CHANGELOG.md` documente l'historique complet de toutes les versions, permettant une traçabilité exhaustive.

## Comparaison avant/après

### Sur demande de l'utilisateur

Si l'utilisateur souhaite comparer deux versions, générer un tableau comparatif :

```markdown
## Comparaison Version 1.1 vs Version 2.0

| Élément | Version 1.1 | Version 2.0 | Type de modification |
|---------|-------------|-------------|---------------------|
| Nombre de questions | 10 | 12 | Extension |
| Question 2 | "Définition..." | [Supprimée] | Suppression |
| Question 11 | - | "Théorie causalité..." | Ajout |
| Question 3, Distracteur 2 | "...faute prouvée" | "...caractère anormal" | Modification |
```

### Synthèse des changements

Après chaque modification, proposer une synthèse :

```markdown
## Synthèse des modifications v1.1 → v2.0

**Questions modifiées** : 3, 7
**Questions supprimées** : 2, 5, 9
**Questions ajoutées** : 11, 12, 13, 14, 15
**Feedbacks enrichis** : 7, 8

**Impact global** :
- Niveau de difficulté : Basique-Intermédiaire → Intermédiaire-Avancé
- Couverture thématique : +25% (ajout théories causalité)
- Qualité pédagogique feedbacks : +40% (enrichissement références)
```

## Gestion des demandes de modification

### Workflow standardisé

1. **Réception de la demande** : L'utilisateur exprime son souhait de modification
2. **Clarification** : Si nécessaire, demander précisions sur la portée des modifications
3. **Proposition** : Soumettre les modifications envisagées pour validation
4. **Implémentation** : Appliquer les modifications validées
5. **Documentation** : Mettre à jour le changelog
6. **Archivage** : Sauvegarder la version précédente
7. **Livraison** : Fournir la nouvelle version avec changelog

### Questions de clarification types

Lorsque l'utilisateur demande une modification, systématiquement vérifier :
- Quelle(s) question(s) spécifiquement ?
- Quel élément précis (énoncé, distracteur, feedback) ?
- Quelle est la raison pédagogique ou factuelle ?
- Souhaitez-vous une reformulation ou un remplacement complet ?
- Faut-il maintenir la cohérence avec d'autres questions ?

## Prévention des régressions

### Checklist de validation post-modification

Après chaque modification, vérifier :

- [ ] La modification répond-elle à la demande initiale ?
- [ ] La cohérence pédagogique d'ensemble est-elle préservée ?
- [ ] Les sources sont-elles toujours valides et à jour ?
- [ ] Les feedbacks restent-ils cohérents avec les modifications ?
- [ ] Le niveau de difficulté global est-il maintenu ou ajusté volontairement ?
- [ ] La progression difficulté croissante est-elle respectée ?
- [ ] Les distracteurs restent-ils plausibles et équilibrés (5/6 conceptuels, 1/6 linguistiques) ?

### Alerte en cas de modification majeure

Si une demande de modification entraîne plus de 30% de changements dans le QCM, proposer à l'utilisateur :
- Soit procéder par itérations progressives
- Soit considérer la création d'un nouveau QCM distinct
- Soit valider explicitement qu'une refonte complète est souhaitée

## Notes finales

Le versionnement n'est pas une contrainte bureaucratique mais un outil pédagogique et scientifique :
- Il permet à l'enseignant de documenter l'évolution de son matériel pédagogique
- Il facilite la collaboration entre enseignants (partage de versions annotées)
- Il assure la traçabilité en cas de contestation d'évaluation
- Il soutient l'amélioration continue de la qualité pédagogique

Chaque version du QCM est datée et archivée, constituant ainsi un historique complet de son développement.
