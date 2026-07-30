# Tâche 8 — Analyse d'un article de loi

> **Pré-requis environnement** : aucun — exécutable en tout mode. COWORK/CHAT_CU : livrable Word. CHAT : réponse conversationnelle structurée.

## Objectif

Produire une fiche technique complète sur un article de loi ou de code : texte intégral, contexte, historique, jurisprudence thématique, bibliographie.

## Processus

### 1. Récupération du texte

**EXÉCUTER via OpenLegi :**
- `rechercher_code` (champ `NUM_ARTICLE`, type `EXACTE`) → texte intégral de l'article
- Extraire : texte complet, état juridique, date début/fin vigueur, chemin dans le code (arborescence), articles cités
- Si l'article est abrogé : identifier le texte de remplacement
- Si l'article a été modifié : identifier les versions successives

### 2. Contexte normatif

**EXÉCUTER :**
- Identifier le texte d'origine (loi, ordonnance, décret ayant créé ou modifié l'article)
- `rechercher_dans_texte_legal` → texte d'origine, exposé des motifs si accessible
- Situer l'article dans l'arborescence du code (titre, chapitre, section)
- Identifier les articles connexes (même section, articles cités, articles citant celui-ci)
- web_search → travaux parlementaires, rapports, débats (éléments d'interprétation)

### 3. Historique de l'article

Retracer les versions successives :
- Rédaction d'origine
- Modifications (loi de modification, date, nature du changement)
- Rédaction actuelle
- Projets de modification en cours si identifiés

### 4. Jurisprudence thématique

**EXÉCUTER selon la séquence descendante :**

**4a. Jurisprudence suprême** :
- `rechercher_jurisprudence_judiciaire` (recherche par référence textuelle) → arrêts de la Cour de cassation appliquant cet article
- `rechercher_jurisprudence_administrative` si article applicable en contentieux administratif
- `rechercher_decisions_constitutionnelles` → QPC éventuelles sur cet article
- Identifier : interprétation jurisprudentielle, conditions d'application, exceptions, revirements

**4b. Jurisprudence du fond** :
- Illustrations concrètes de l'application par les juridictions du fond
- Quantification si pertinent (montants, quantum)

### 5. Doctrine

**EXÉCUTER :**
- `scripts/hal_search.py` → articles analysant cet article
- web_search → commentaires sur Cairn, Dalloz, Persée
- Identifier : critiques, propositions de réforme, interprétations divergentes

### 6. Rédaction du document Word

**Structure :**

1. **Texte intégral** de l'article (version en vigueur, encadré)
2. **Données techniques** : code, numéro, état, dates de vigueur, texte d'origine
3. **Arborescence** : situation dans le code
4. **Historique** : versions successives et modifications
5. **Interprétation jurisprudentielle** : arrêts de principe, conditions, exceptions
6. **Illustrations par le fond** : applications concrètes
7. **Analyse doctrinale** : positions, débats, critiques
8. **Perspectives** : projets de modification, tendances
9. **Notes et références**

### 7. Livraison

Nommage : `[AAAA-MM-JJ]-fiche-art-[numero]-[code-abrege].docx`
Exemple : `2026-03-23-fiche-art-1240-C-civ.docx`
