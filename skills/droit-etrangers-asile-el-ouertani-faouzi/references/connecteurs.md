# Connecteurs — usage opérationnel

Installation et vérification : `installation-connecteurs.md`.
Limites et contrôles : `anti-hallucination.md`.

Les outils MCP sont différés : appeler `tool_search` avec des mots-clés avant utilisation, puis employer les noms de paramètres exacts retournés. Ne jamais deviner un nom d'outil ni un paramètre — un appel inventé échoue silencieusement ou retourne autre chose que ce qu'on croit avoir demandé.

Trois connecteurs, trois rôles qui se chevauchent volontairement peu : OpenLegi pour le texte et l'administratif, LibreJustice pour la recherche par le sens tous ordres confondus, Legal Data Hunter pour le judiciaire de la rétention et le contrôle de validité d'une décision.

## OpenLegi — les textes

Serveur MCP donnant accès aux sources officielles françaises via l'API PISTE de Légifrance. Endpoint : `https://mcp.openlegi.fr`.

Fonds mobilisables en droit des étrangers :

| Fonds | Usage |
|---|---|
| **CODE** | CESEDA, code civil (nationalité), code de la sécurité sociale, code de justice administrative, CRPA |
| **LODA** | Lois, ordonnances, décrets, arrêtés — dont la loi n° 2024-42 et les arrêtés « métiers en tension » |
| **JORF** | Textes récemment publiés — décrets d'application, actualisation des listes |
| **CETAT** | Conseil d'État, CAA, TA — le cœur du contentieux administratif des étrangers |
| **CONSTIT** | Conseil constitutionnel — DC et QPC (dont la décision sur la loi de 2024) |
| **KALI** | Conventions collectives — utile pour le volet travail |
| **BOFiP** | Doctrine fiscale — marginal ici |

La liste exacte des outils et de leurs paramètres est publiée sur https://www.openlegi.fr/documentation/outils/liste-des-outils/ — la consulter plutôt que de supposer.

**Séquence type pour une question de séjour** : rechercher l'article par son objet → obtenir son texte en vigueur → contrôler la section parente et l'absence de troncature → rechercher son application par les juges dans le fonds CETAT.

**Hors périmètre, documenté par l'éditeur** — ne pas insister, basculer sur la source directe :
- versions historiques d'un article → Légifrance, onglet « Versions » ;
- règlements et directives de l'UE → EUR-Lex, sauf si la source EUR-Lex est activée sur le compte.

Ce second point est structurant depuis le 12 juin 2026 : le Pacte européen s'analyse sur EUR-Lex, pas dans le CESEDA.

## LibreJustice — la recherche par le sens, tous ordres

Connecteur de recherche sémantique et lexicale sur la jurisprudence et les textes français. Endpoint : `https://librejustice.fr/mcp/`.

| Outil | Usage |
|---|---|
| `search_decisions` | Recherche combinant sens et mots-clés — l'outil de premier recours quand aucun numéro n'est connu |
| `get_decision` | Texte intégral et métadonnées d'une décision à partir de son URL |
| `search_legal_texts` | Retrouver un article à partir de son objet ou de sa formulation |
| `get_legal_text` | Article tel qu'il était rédigé à une date donnée |

Deux usages où LibreJustice est le premier réflexe :
1. **La question posée en langage naturel** — « à quelles conditions le juge admet-il l'erreur manifeste d'appréciation sur la vie privée et familiale ? » — là où une recherche par numéro d'article ne mène nulle part.
2. **Le texte d'un article**, avec sa rédaction à une date donnée.

Règle d'usage propre à cet outil : **lire la décision en intégralité avec `get_decision` avant de la citer.** Un extrait de résultat de recherche indique qu'une décision parle du sujet, pas ce qu'elle en dit. C'est le mécanisme B2 de `anti-hallucination.md` — référence réelle, attribution fausse.

## Legal Data Hunter — le judiciaire et le contrôle de validité

Moteur de recherche jurisprudentielle avec reranking sémantique et graphe de citations. Deux usages précis en droit des étrangers, distincts de ce que couvrent les deux autres connecteurs.

### Recherche par filtres structurés

L'outil de recherche accepte des filtres combinables : `domaine` (utiliser `administratif` pour la quasi-totalité des dossiers étrangers), `jurisdiction`, `chamber`, `solution`, dates. C'est l'outil à privilégier quand le dossier touche au **judiciaire de la rétention** :

- **rétention administrative et JLD** — les cours d'appel disposent de chambres dédiées (« chambre étrangers », « rétention_recoursJLD ») que ni OpenLegi (fonds administratifs uniquement) ni une recherche générique LibreJustice ne ciblent aussi précisément ;
- notification irrégulière d'une mesure d'éloignement, erreur manifeste d'appréciation sur les garanties de représentation, proportionnalité d'un placement en rétention au regard de la vie privée et familiale — des questions qui se jugent devant le juge judiciaire (JLD, cour d'appel), pas devant le juge administratif.

Chaque résultat retourne une fiche structurée : problème de droit, faits, procédure, solution, articles cités — ce qui permet un premier tri avant lecture intégrale, sans dispenser de la lecture intégrale pour toute décision effectivement citée dans un livrable.

### Contrôle de validité — la fiche décision complète

Pour toute décision identifiée comme pertinente, la fiche complète retourne un **graphe** : décisions qu'elle cite, décisions qui la citent, lignée procédurale (décision attaquée, pourvois joints), et surtout un champ **statut de validité** signalant si la décision a été renversée par une décision postérieure.

C'est le contrôle qui manquait structurellement à ce skill avant son intégration : citer une décision sans savoir si elle a été renversée est une hallucination silencieuse — la référence existe, le lien fonctionne, mais la solution qu'elle porte n'est plus le droit. **Avant de fonder un moyen sur une décision judiciaire, vérifier son statut de validité par ce canal.**

## Répartition

| Question | Outil |
|---|---|
| « Que dit l'article X ? » | OpenLegi |
| « Quel texte régit cette situation ? » | OpenLegi, ou LibreJustice si la formulation est incertaine |
| « Comment les juges tranchent-ils ce point ? » (administratif) | LibreJustice, ou OpenLegi (fonds CETAT) |
| « Comment les juges tranchent-ils ce point ? » (rétention, JLD) | Legal Data Hunter |
| « Cette décision dit-elle vraiment cela ? » | LibreJustice (`get_decision`) ou Legal Data Hunter (fiche complète) |
| « Cette décision a-t-elle été renversée ? » | Legal Data Hunter (graphe, statut de validité) |
| « Ce décret est-il paru ? » | OpenLegi (JORF, LODA) |
| « Quelle était la version applicable en 2023 ? » | Légifrance directement |
| « Que dit le règlement européen ? » | EUR-Lex |

Les deux derniers cas sont des angles morts assumés des trois connecteurs. Les traiter par la source directe — ou, à défaut, par les formulations de repli de `anti-hallucination.md`.

## Sources complémentaires

`service-public` pour les démarches, formulaires et guichets compétents — utile pour un livrable destiné à une permanence.

`web_search` et `web_fetch` pour ce qu'aucune base n'indexe : doctrine associative, accords bilatéraux, actualité réglementaire des dernières semaines. Toujours `web_fetch` la page avant de la citer.

## En cas d'échec

Reformuler, changer d'outil, élargir la période. Trois connecteurs se recouvrent partiellement — un échec sur l'un n'interdit pas d'essayer un autre avant de conclure à une recherche infructueuse. Après trois tentatives infructueuses au total, l'écrire dans le livrable — « la recherche n'a pas permis de confirmer ce point » — et basculer sur les formulations de repli. Un vide de recherche ne se comble jamais par la mémoire du modèle.
