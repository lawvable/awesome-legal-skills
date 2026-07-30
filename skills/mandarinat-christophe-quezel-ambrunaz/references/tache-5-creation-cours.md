# Tâche 5 — Création de cours

> **Pré-requis environnement** : COWORK **obligatoire**. Cette tâche produit un ou plusieurs fichiers lourds (Word + potentiellement PPTX). **Bloquer** en mode CHAT et CHAT_CU.

## Objectif

Créer un cours juridique complet ou une séquence pédagogique, avec support écrit (Word) et optionnellement support de présentation (PPTX).

## Processus

### 1. Qualification de la demande

Recueillir auprès de l'utilisateur (ou déduire du contexte) :
- **Matière** : droit civil, droit administratif, droit pénal, droit des affaires, etc.
- **Sous-matière / thème** : responsabilité civile, contrats spéciaux, droit de l'urbanisme, etc.
- **Niveau** : L1 / L2 / L3 / M1 / M2 / Formation continue / Préparation concours
- **Volume horaire** : nombre d'heures de cours magistral et/ou de TD
- **Format** : cours magistral seul / cours + TD / séquence pédagogique
- **Supports attendus** : Word seul / Word + PPTX / Word + PPTX + exercices

Si des éléments manquent et sont indispensables : demander clarification.

### 2. Exécuter le playbook (tâche 0)

Cadrage juridique du thème. Identifier les axes structurants, les questions-clés, les évolutions récentes.

### 3. Recherche documentaire approfondie

Suivre intégralement la séquence de recherche du §3 du SKILL.md :
- Textes normatifs (OpenLegi)
- Jurisprudence suprême puis fond (OpenLegi)
- Doctrine (`scripts/doctrine_search.py` multi-sources + web_search) — **minimum 15 sources doctrinales** pour un cours complet, chacune avec identifiant vérifiable (DOI/HAL/URL)
- Droit comparé (LegalDataHunter) si pertinent pour le thème

**Objectif spécifique** : identifier non seulement l'état du droit mais aussi les problématiques pédagogiques (ce que les étudiants comprennent mal, les confusions fréquentes, les points de controverse).

### 4. Conception du plan de cours

**Structure type d'un cours :**
```
INTRODUCTION GÉNÉRALE
  - Définitions
  - Intérêt de la matière
  - Évolution historique (synthétique)
  - Plan du cours

PARTIE I — [Titre analytique]
  Chapitre 1 — [Titre]
    Section 1 — [Titre]
    Section 2 — [Titre]
  Chapitre 2 — [Titre]
    Section 1 — [Titre]
    Section 2 — [Titre]

PARTIE II — [Titre analytique]
  [même structure]

BIBLIOGRAPHIE INDICATIVE
```

**Règles :**
- Structure binaire au niveau des parties (tradition française)
- Titres sans verbes conjugués
- Progression logique (du général au particulier, du simple au complexe)
- Équilibre entre les parties
- Adapté au volume horaire (un chapitre ≈ 3-6 heures selon le niveau)

### 5. Rédaction du support écrit (Word)

**Invoquer la skill `docx` pour la génération du document.**

**Contenu du cours :**
- Texte rédigé intégralement (pas de plan-notes)
- Citations exactes des textes normatifs et de la jurisprudence (avec notes de fin)
- Références doctrinales intégrées au développement
- Encadrés pédagogiques :
  - « À retenir » (synthèse des points essentiels)
  - « Illustration » (arrêt commenté brièvement)
  - « Attention » (pièges, confusions fréquentes)
  - « Pour aller plus loin » (approfondissements, lectures recommandées)
- Bibliographie en fin de cours

**Format des citations** : voir `references/format-citations.md`

### 6. Création du support PPTX (si demandé)

**Invoquer la skill `pptx` pour la génération de la présentation.**

**Principes du support PPTX :**
- Le PPTX est un **support de présentation**, pas une duplication du cours
- Contenu épuré : titres, schémas, points-clés, citations marquantes
- Pas de paragraphes de texte longs sur les slides
- 1 slide ≈ 1 idée
- Utiliser des schémas pour les mécanismes juridiques (ex. : chaîne de responsabilité, hiérarchie des normes)
- Inclure les références des arrêts-clés (sans les développer — le cours Word fait foi)

**Structure type du PPTX :**
- Slide de titre (matière, thème, enseignant, année)
- Slide de plan
- Slides de contenu (1 par point-clé ou par section)
- Slides « Illustration » (arrêt + question posée)
- Slide de synthèse par chapitre
- Slide de bibliographie indicative

### 7. Vérification

Avant livraison :
1. Vérifier toutes les références citées (anti-hallucination, §2 du SKILL.md)
2. Vérifier la temporalité des textes (§7 du SKILL.md)
3. Vérifier la cohérence du plan et l'équilibre des parties
4. Vérifier l'adaptation au niveau annoncé

### 8. Livraison

Nommage :
- Cours : `[AAAA-MM-JJ]-cours-[matiere]-[theme].docx`
- PPTX : `[AAAA-MM-JJ]-cours-[matiere]-[theme].pptx`

Proposer des tâches connexes :
- Création de sujets d'examen (tâche 3)
- Création de QCM (rediriger vers skill `qcm-generator`)
- Création de fiches de TD
- Mise à jour future (tâche 4)
