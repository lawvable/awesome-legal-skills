---
name: "MCQ Generator"
description: "AI-assisted generation of MCQs (multiple-choice questionnaires) with export to Moodle (GIFT, XML), Wooclap (Excel), Kahoot!, and Word. Supports light MCQs (gamified) and in-depth MCQs (evaluative), with single-answer and multiple-answer formats."
metadata:
  author: "Christophe Quézel-Ambrunaz"
  license: "agpl-3.0"
  version: "2026-04-10"
---

# QCM Generator - Version 3.0

## Vue d'ensemble

Cette skill guide la création de QCM de qualité académique avec recherche documentaire systématique, validation factuelle rigoureuse, construction méthodique des distracteurs, et génération de fichiers prêts pour divers usages pédagogiques.

**Nouveautés V.3** :
- Dichotomie QCM léger (ludique, sans feedbacks) / QCM approfondi (évaluatif, avec feedbacks)
- Randomisation de la position des bonnes réponses (visible dès la prévisualisation)
- Échelle de niveau adaptée : Primaire, Collège, Lycée, Licence, Master
- Export Kahoot! (.xlsx) pour QCM légers
- Export Word (.docx) avec feuille questions + grille correction + corrigé détaillé
- Précision : XML Moodle importable directement dans Wooclap

**Héritées de V.2** :
- Système de pénalités configurable pour réponses incorrectes
- Méthodologie formalisée de construction des distracteurs (5/6 conceptuels, 1/6 linguistiques)
- Progression de difficulté croissante obligatoire
- Protocole de versionnement pour modifications itératives
- Guidelines détaillées pour feedbacks pédagogiques de qualité

## Workflow en 5 phases

### Phase 1 : Collecte des informations

**PREMIÈRE QUESTION PRIORITAIRE** : Lire `references/usage_type_choice.md` et demander à l'utilisateur de choisir entre :
- **QCM Léger** (ludique, révision, Kahoot!/Wooclap) : Sans feedbacks, contraintes longueur strictes
- **QCM Approfondi** (évaluatif, formatif) : Avec feedbacks détaillés, longueur libre

Ce choix conditionne toute la suite du processus.

---

Puis vérifier systématiquement que l'utilisateur a fourni :

1. Nombre de questions
2. Nombre de réponses par question (recommandation : 4-6)
3. Type de réponses : choix unique ou réponses multiples
4. **Système de pénalités** : Points négatifs pour réponses incorrectes ? Si oui, quelle pénalité ?
5. Thématique/sujet précis
6. **Niveau** : Primaire, Collège, Lycée, Licence, ou Master (accepter précisions : "Licence 3", "Master 2", etc.)
7. Objectif pédagogique (vérification connaissances / évaluation compréhension / réflexion)

**Toujours demander** si l'utilisateur souhaite charger des documents de référence.

Si informations manquantes, lire `references/collect_information_missing.md` et demander les informations.

### Phase 2 : Recherche documentaire

**Principe absolu** : Exactitude factuelle prime sur tout.

**Recherche web OBLIGATOIRE** pour :
- Droit (législation, jurisprudence, doctrine) - Priorité Légifrance pour droit français
- Sciences et techniques (évolutions récentes)
- Politique, médecine, économie, tout domaine où la fraîcheur importe

**Sources** : Privilégier sources académiques, institutionnelles, gouvernementales.

**Validation** : Croiser au moins 2 sources indépendantes pour chaque fait important.

### Phase 3 : Génération du document de prévisualisation

**LECTURE CONDITIONNELLE selon type de QCM** :

**Si QCM LÉGER** :
- Lire obligatoirement `references/constraints_light_mcq.md` (contraintes 95/60 caractères)
- NE PAS générer de feedbacks
- Focus : questions factuelles courtes et percutantes
- Régénérer automatiquement si dépassement de contraintes (max 2 tentatives)

**Si QCM APPROFONDI** :
- Lire obligatoirement `references/feedback_guidelines.md`
- Générer feedbacks détaillés pour chaque réponse selon guidelines
- Longueur libre pour énoncés et réponses

**DANS TOUS LES CAS, lire obligatoirement** :
- `references/distractor_methodology.md` pour construction des distracteurs
- `references/difficulty_progression.md` pour organisation des questions

---

Créer un document Markdown structuré avec pour chaque question :

**Principes de rédaction** :
- Énoncés clairs, univoques, sans ambiguïté
- **Distracteurs** : 5/6 conceptuels (erreurs de compréhension), 1/6 linguistiques (mots proches)
- Feedbacks apportant valeur pédagogique selon guidelines (si approfondi)
- Longueur homogène des réponses
- **Ordre des questions** : Progression stricte de la plus simple à la plus difficile

**RANDOMISATION OBLIGATOIRE** :
- Mélanger l'ordre des réponses pour chaque question (algorithme Fisher-Yates)
- Appliquer la randomisation DÈS la prévisualisation
- Marquer visuellement les bonnes réponses : **✅ [Texte de la réponse]**
- Identifier clairement quelle(s) position(s) occupe(nt) la/les bonne(s) réponse(s)

**Structure par question** :
1. Numéro et énoncé
2. Réponses (randomisées, avec ✅ pour les correctes)
3. Feedbacks détaillés pour chaque option (si approfondi uniquement)
4. Justification du niveau de difficulté
5. Sources documentaires consultées

### Phase 4 : Révision et validation

**AVERTISSEMENT OBLIGATOIRE** : Lire `references/revision_warning.md` et rappeler que :
- Claude peut faire des erreurs
- Révision humaine indispensable
- Possibilité de modifications

**Si l'utilisateur demande des modifications** :
- Lire `references/versioning_protocol.md`
- Documenter les changements dans un changelog
- Numéroter les versions (X.Y)
- Générer une comparaison avant/après si demandé

Puis proposer choix du format en lisant `references/output_format_choice.md`

### Phase 5 : Génération des fichiers

Selon le format choisi et le type de QCM, lire les spécifications dans references/ :

**Formats disponibles pour QCM LÉGER** :
- **Kahoot!** : `references/format_kahoot.md` - Format natif optimisé
- **Wooclap Excel** : `references/format_wooclap.md`
- **GIFT** : `references/format_gift.md` (sans feedbacks)
- **XML Moodle** : `references/format_xml_moodle.md` (sans feedbacks)

**Formats disponibles pour QCM APPROFONDI** :
- **GIFT** : `references/format_gift.md` (avec feedbacks)
- **XML Moodle** : `references/format_xml_moodle.md` (avec feedbacks)
  - **IMPORTANT** : Les fichiers XML Moodle peuvent être importés directement dans Wooclap via "Importer un événement"
- **Wooclap Excel** : `references/format_wooclap.md` (feedbacks à ajouter manuellement après import)
- **Word** : `references/format_word.md` (feuille questions + grille correction + corrigé détaillé)

Puis fournir instructions d'utilisation : `references/usage_[format].md`

**Note sur Wooclap** : 
- Format Excel disponible pour léger ET approfondi
- Pour QCM approfondis, privilégier XML Moodle importable dans Wooclap (préserve mieux les feedbacks)

## Limitations

**Types NON supportés** : Questions ouvertes, réponse courte, appariement, numériques pures, texte à trous, classement.
Si demandé : `references/unsupported_question_type.md`

**Contenu problématique** : Refus catégorique si factuellement faux, discriminatoire, biaisé, ou nuisible.
Si détecté : `references/refuse_problematic_content.md`
