# Exemple travaillé

Cas réel, testé en conditions réelles avec les connecteurs le 8 août 2026 (voir le journal de `anti-hallucination.md`, cas 5). Reproduit ici au format entrée/sortie pour montrer la méthode de bout en bout — qualification, recherche, content-matching, tableau, formule de clôture.

## Entrée

> « Ma sœur a eu un refus de visa long séjour conjoint de Français au consulat. Elle veut attaquer directement au tribunal administratif de sa ville. C'est possible ? »

## Qualification (§3 du SKILL.md)

- Nationalité : non précisée — sans incidence ici, le régime des visas est uniforme (pas d'accord bilatéral dérogatoire sur cette procédure).
- Situation administrative : refus de visa long séjour, catégorie conjoint de Français.
- Date pivot : non donnée — à fixer par hypothèse explicite (voir sortie).
- Prémisse à vérifier avant de répondre sur le fond : la personne suppose qu'une saisine directe du TA est possible. C'est le point à qualifier en premier.

## Recherche (§2 du SKILL.md — OpenLegi puis LibreJustice)

1. Recherche par objet : « recours administratif préalable obligatoire refus de visa commission de recours Nantes » → retourne D.312-3, D.312-4, D.312-7 du CESEDA.
2. Lecture intégrale de D.312-4 : délai du RAPO fixé à 30 jours.
3. Lecture intégrale de D.312-3 : répartition Commission (long séjour) / sous-directeur des visas (court séjour) ; RAPO « préalable obligatoire à l'exercice d'un recours contentieux, à peine d'irrecevabilité ».
4. Recherche complémentaire sur la compétence : « tribunal administratif de Nantes compétence exclusive recours contentieux refus visa » → retourne R.312-18 CJA (compétence exclusive du TA de Nantes) et le décret n° 2022-962 du 29 juin 2022 qui l'a institué.
5. Lecture de l'article 3 du décret n° 2022-962 : révèle, en creux, une distinction non anticipée — R.811-1, 10° CJA place les visas de court séjour en premier et dernier ressort (pas d'appel).
6. Lecture intégrale de R.312-6 CESEDA : le délai contentieux devant le TA, après RAPO, est celui de droit commun du CJA (R.421-1, R.421-2) — 2 mois.

## Content-matching

| Assertion | Article retourné | Extrait pertinent | Soutient l'assertion ? |
|---|---|---|---|
| RAPO obligatoire avant tout recours contentieux | D.312-3 CESEDA | « La saisine de l'une ou l'autre de ces autorités […] est un préalable obligatoire à l'exercice d'un recours contentieux, à peine d'irrecevabilité » | ✓ |
| Délai du RAPO : 30 jours | D.312-4 CESEDA | « Les recours administratifs doivent être formés dans un délai de trente jours à compter de la notification » | ✓ |
| Autorité compétente pour le long séjour : la Commission | D.312-3 CESEDA | « Une commission […] est chargée d'examiner les recours administratifs contre les décisions de refus de visa de long séjour » | ✓ |
| Recours contentieux ensuite dans le délai de droit commun (2 mois) | R.312-6 CESEDA | renvoie explicitement à R.421-1 et R.421-2 CJA | ✓ |
| TA de Nantes seul compétent | R.312-18 CJA | « ressortissent à la compétence du tribunal administratif de Nantes » | ✓ |
| Jugement de long séjour susceptible d'appel (à la différence du court séjour) | R.811-1, 10°, CJA | insère le court séjour et les autorisations ETIAS dans la liste des premiers-et-derniers ressorts ; le long séjour n'y figure pas → appel de droit commun | ✓ (par déduction a contrario, signalée comme telle dans la sortie) |

## Sortie

*Hypothèse retenue : date pertinente = aujourd'hui, puisque la question porte sur la marche à suivre pour une décision qu'on suppose récente. Si le refus est ancien, vérifier que le délai n'est pas expiré avant d'agir.*

Non, une saisine directe du tribunal administratif serait irrecevable.

**Le recours administratif préalable est obligatoire.** Avant tout recours contentieux, votre sœur doit saisir la Commission de recours contre les décisions de refus de visa (visa de long séjour), dans un délai de **30 jours** à compter de la notification du refus (art. D.312-3 et D.312-4 du CESEDA — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045998669/2022-07-02). Saisir directement le tribunal sans ce recours préalable rend la requête irrecevable.

**Ensuite seulement**, en cas de rejet exprès ou de silence de la Commission pendant deux mois (rejet implicite), le recours contentieux s'ouvre dans le délai de droit commun de **2 mois** (art. R.312-6 CESEDA, renvoyant aux art. R.421-1 et R.421-2 du code de justice administrative).

**Ce recours contentieux doit être porté devant le tribunal administratif de Nantes**, seul compétent pour l'ensemble du contentieux des visas, quel que soit le lieu de résidence de votre sœur (art. R.312-18 du code de justice administrative — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045998672/2022-07-02).

Point utile pour la suite : s'agissant d'un visa de **long séjour**, le jugement du TA de Nantes sera, à la différence d'un visa de court séjour, susceptible d'**appel** devant la cour administrative d'appel de Nantes.

---

Tableau de vérification produit ; 6 références contrôlées (5 en P1, 1 en P2) ; 0 reformulation effectuée ; aucune référence non tracée ne subsiste.

## Ce que cet exemple illustre

- La prémisse de la question (« attaquer directement ») était fausse et a été corrigée avant toute autre réponse — c'est la fonction du §3 du SKILL.md.
- Un délai « connu » (2 mois) a failli être appliqué au mauvais endroit — c'est exactement le mécanisme B1 de `anti-hallucination.md` (familiarité comme piège), détecté ici parce que chaque article a été lu en entier plutôt que résumé de mémoire.
- La distinction premier/dernier ressort n'était dans aucune version antérieure de ce skill : elle est apparue en lisant un article que la recherche initiale n'avait pas ciblé directement (l'article 3 du décret constitutif). Une recherche qui s'arrête au premier résultat pertinent manque ce type de nuance.
