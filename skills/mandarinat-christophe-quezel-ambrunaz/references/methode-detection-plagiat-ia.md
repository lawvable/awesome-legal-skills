# Méthode de détection d'indices de plagiat et de génération par IA

> Ce document définit le protocole heuristique utilisé par la tâche 2 (relecture) pour identifier des indices de plagiat ou de génération par intelligence artificielle. **Aucun outil externe de détection n'est recommandé** : les outils existants (GPTZero, Turnitin AI, etc.) ne sont pas fiables et produisent des faux positifs fréquents.

## Principes fondamentaux

### Terminologie obligatoire
- ✅ « indices », « éléments suggestifs », « signaux »
- ❌ « preuve », « certitude », « détection confirmée »

### Posture épistémique
- Un texte bien écrit n'est PAS suspect en soi
- Un texte mal écrit n'est PAS exempt de plagiat
- La détection repose sur des **convergences d'indices**, jamais sur un indicateur unique
- Le résultat est TOUJOURS une appréciation qualitative, jamais un score ou un pourcentage
- L'objectif est d'alerter, pas d'accuser

### Ce que cette méthode ne fait PAS
- Affirmer qu'un texte est plagié ou généré par IA
- Produire un « taux de plagiat » ou un « score IA »
- Recommander un outil externe de détection
- Se substituer au jugement humain de l'enseignant

---

## Protocole de détection d'indices de plagiat

### 1. Analyse stylistique interne

**Rechercher des ruptures de style au sein du document :**
- Changement brutal de registre de langue (passages très soutenus alternant avec passages familiers)
- Changement de qualité rédactionnelle (passages excellents alternant avec passages faibles)
- Changement de vocabulaire technique (terminologie experte puis imprécise)
- Incohérence dans le système de citation (format qui change brusquement)
- Variations de typographie (guillemets français puis anglais, espaces insécables puis absentes)

**Grille d'évaluation :**
| Indice | Force |
|---|---|
| Rupture stylistique isolée | Faible |
| Ruptures stylistiques multiples et localisées | Moyen |
| Passages entiers dans un style radicalement différent du reste | Fort |

### 2. Recherche de similitudes textuelles (web_search)

**Pour les passages suspects (identifiés par l'analyse stylistique) :**
1. Extraire du passage suspect un **n-gramme distinctif** : une suite de 6 à 10 mots peu banale (tournure rare, collocation inhabituelle, enchaînement spécifique), de préférence sans nom propre trivial.
2. Rechercher ce n-gramme via web_search **sans guillemets et sans opérateur de recherche exacte** : les moteurs actuels dégradent fortement (voire ignorent) la recherche d'expression exacte entre guillemets, de sorte qu'une requête « phrase exacte » renvoie souvent zéro résultat alors que la source existe. Une requête en mots-clés sur un n-gramme distinctif retrouve la source de façon plus robuste.
3. Si une source ressort : ouvrir la page et **comparer le texte** mot à mot avec le passage suspect (la correspondance se vérifie à la lecture, pas au seul fait que le moteur ait répondu).
4. Répéter pour 3 à 5 n-grammes distinctifs du même passage, idéalement dispersés.

**Interprétation :**
- Correspondance textuelle forte avec une source non citée → indice fort de plagiat
- Correspondance partielle (reformulation légère, mêmes idées et même structure) → indice moyen
- Aucune correspondance → pas d'indice (mais pas de certitude d'originalité ; l'absence de résultat peut tenir aux limites du moteur)

### 3. Analyse des références

**Vérifier la cohérence des références avec le niveau du rédacteur :**
- Références très spécialisées dans un travail par ailleurs superficiel → indice
- Références toutes issues de la même source (copie d'une bibliographie) → indice
- Références non vérifiables (titre plausible mais introuvable) → indice de génération IA

---

## Protocole de détection d'indices de génération par IA

### 1. Uniformité stylistique excessive

Les textes générés par LLM présentent souvent :
- Une **régularité syntaxique anormale** (phrases de longueur similaire, structures parallèles répétées)
- Un **vocabulaire uniformément policé** (absence de marques personnelles, d'hésitations, de choix stylistiques individuels)
- Une **ponctuation excessivement régulière** (emploi systématique de virgules d'incise, absence d'écarts)
- Un **ton constamment mesuré** (absence de passion, de parti-pris, de formulations vives)

### 2. Marqueurs caractéristiques des LLM

**Structures fréquemment générées :**
- Listes à puces systématiques là où un texte académique utiliserait de la prose
- Phrases d'introduction trop lisses (« Il convient de noter que... », « Il est important de souligner que... »)
- Conclusions résumant mécaniquement chaque partie
- Transitions artificiellement symétriques

**Vocabulaire caractéristique (à pondérer — non suffisant seul) :**
- « Il est essentiel de », « Il convient de », « Force est de constater »
- Usage fréquent de « notamment », « par ailleurs », « en outre » comme connecteurs mécaniques
- Formulations excessivement équilibrées (« d'une part... d'autre part... »)

### 3. Indices structurels

- **Absence d'ancrage personnel** : le texte ne fait jamais référence à un enseignement reçu, une lecture personnelle, une expérience de stage ou de clinique juridique
- **Exhaustivité suspecte** : le texte couvre « tous les aspects » sans approfondir réellement aucun
- **Références plausibles mais non vérifiables** : citations d'auteurs existants avec des titres d'articles qui n'existent pas (hallucinations de LLM)

### 4. Analyse quantitative de la ponctuation

Sur un échantillon de 50 phrases :
- Calculer la **variance de la longueur des phrases** (en mots)
- Calculer le **ratio virgules/phrases**
- Un texte humain présente une variance élevée ; un texte IA tend vers l'uniformité

**Seuils indicatifs (non absolus) :**
| Métrique | Texte humain typique | Texte IA typique |
|---|---|---|
| Variance longueur phrases | > 100 | < 50 |
| Ratio virgules/phrases | Variable (1.5-4) | Régulier (2-3) |
| % phrases >30 mots | 10-25% | <10% |

---

## Présentation des résultats

### Format du rapport d'indices

```
## Indices de plagiat / génération IA

### Observations générales
[Appréciation qualitative globale : aucun indice / indices faibles / indices significatifs]

### Indices relevés (le cas échéant)

**Indice 1** : [Description]
- Localisation : [page, paragraphe]
- Type : [plagiat / IA / indéterminé]
- Force : [faible / moyen / fort]
- Fondement : [analyse stylistique / web_search / analyse des références / ponctuation]

[...]

### Conclusion
[Synthèse prudente. Rappeler que ces indices ne constituent pas une preuve.]
```

### Formulations admissibles

- ✅ « Plusieurs indices convergents suggèrent que ce passage pourrait ne pas être de la main de l'auteur déclaré »
- ✅ « L'uniformité stylistique de ce document présente des caractéristiques compatibles avec une génération par IA, sans qu'il soit possible de l'affirmer avec certitude »
- ✅ « La recherche de similitudes textuelles a identifié une correspondance significative avec [source], non citée dans le document »
- ❌ « Ce texte est généré par ChatGPT »
- ❌ « L'étudiant a plagié ce passage »
- ❌ « Le taux de plagiat est de X% »
