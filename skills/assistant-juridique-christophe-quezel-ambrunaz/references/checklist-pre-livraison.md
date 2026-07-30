# Checklist obligatoire pré-livraison — Anti-hallucination

<!-- NOYAU-ANTIHALLUCINATION v3 — synchronisé mandarinat 1.4.0 / assistant-juridique-fr 7.4.0. Fichier commun aux deux skills : toute modification doit être répercutée à l'identique (à l'exception des renvois « ci-dessus/ci-dessous » propres à chaque montage). -->

Cette checklist constitue une **étape de contrôle non négociable** à exécuter **avant toute remise** d'un livrable contenant des citations jurisprudentielles, des références à des textes normatifs (articles de codes, lois, ordonnances, décrets, règlements, conventions collectives) ou des références doctrinales.

Elle ne peut être présentée comme accomplie si elle ne l'a pas été. Elle doit être exécutée **explicitement**, sous la forme d'un **tableau structuré** (artefact obligatoire défini ci-dessous), et non mentalement en passant. Son but est double :

1. prévenir la livraison de références hallucinées au sens strict — incident dont le coût académique et professionnel est disproportionné ;
2. prévenir la livraison de références **formellement traçables mais matériellement non concordantes** (hallucination par mauvaise attribution) — c'est-à-dire des références appelées par un outil dans la session, mais dont le contenu retourné ne soutient pas l'assertion qu'elles sont censées fonder.

## Quand exécuter la checklist

À exécuter **après** la production du livrable et **avant** sa remise effective au destinataire (utilisateur, étudiant, client, jury, comité). C'est le dernier filtre.

Aucune exception : la checklist s'applique aux livrables courts comme aux livrables longs, aux corrigés de cas pratique comme aux mémoires de recherche, aux consultations comme aux fiches de TD.

## Modalités d'exécution selon l'environnement

### En modes COWORK et CHAT_CU (filesystem disponible)

L'exécution est **bloquante** : tant que la checklist n'a pas été passée intégralement et que le tableau structuré n'a pas été produit, le livrable n'est pas remis.

1. **Générer le tableau de vérification depuis le journal de références** : `python3 scripts/reference_journal.py table --journal verification/journal-references.ndjson` (le journal a été alimenté au fil de l'eau à chaque appel d'outil — cf. étape 8 du workflow). Vérifier d'abord sa complétude : `python3 scripts/reference_journal.py check --journal verification/journal-references.ndjson` (exit 1 tant qu'une entrée est incomplète). Le tableau dérivé du journal proscrit le remplissage de la colonne « extrait » de mémoire. À défaut de journal (oubli), reconstituer le tableau en re-consultant les appels d'outils de la session — jamais de mémoire.
2. Compiler la liste exhaustive des URLs Légifrance figurant dans le livrable, dans un fichier JSON intermédiaire.
3. Exécuter `scripts/verify_links.py --from-file urls.json --check-content` (mode `--check-content` activé par défaut), et reporter dans la colonne 3 du tableau l'extrait textuel pertinent retourné pour chaque référence.
4. Examiner la sortie : **toute URL en échec** (pattern non reconnu, HTTP ≠ 200, contenu non concordant) doit être traitée selon la procédure de la section « Conduite à tenir en cas d'échec » ci-dessous, et la ligne correspondante du tableau passe alors à ✗.
5. Ne procéder à la remise que lorsque toutes les lignes du tableau portent ✓ et que la formule de clôture a été prononcée explicitement.

### En mode CHAT (sans filesystem)

L'exécution se fait **explicitement**, référence par référence, sous la forme du tableau structuré. Le script `verify_links.py` n'est pas exécutable, mais la même logique doit être appliquée :

1. Produire le tableau de vérification dans la session (artefact-modèle ci-dessous).
2. Énumérer chaque référence du livrable et la reporter en colonne 1.
3. Pour chacune, identifier dans la session l'appel à OpenLegi (ou à un autre outil de recherche) qui l'a produite — colonne 2.
4. Lire le contenu retourné par l'appel (motifs, dispositif, alinéa d'article) et reporter un extrait pertinent en colonne 3.
5. Confronter cet extrait à l'assertion fondée par la citation et renseigner la colonne 4 (✓ / ✗ / reformulation).
6. Si l'appel n'a pas été effectué : exécuter la recherche manquante avant remise. Si l'utilisateur ne peut pas attendre, signaler la référence comme « à vérifier » et le porter en colonne 4.
7. Confirmer que le lien Légifrance figurant dans le livrable provient bien de la réponse de l'outil — non d'une reconstruction de mémoire.
8. Prononcer la formule de clôture explicite avant de remettre le livrable.

## Dégradation conditionnelle (préflight d'accès réseau)

En modes COWORK et CHAT_CU, l'exécution effective de `verify_links.py --check-content` requiert que le sandbox Cowork puisse atteindre `www.legifrance.gouv.fr`. Cet accès est susceptible d'être bloqué par l'allowlist réseau de l'organisation.

**Procédure de détection automatique** — avant d'exécuter la vérification complète à l'étape 4, exécuter le mode préflight :

```bash
python3 scripts/verify_links.py --preflight
```

Codes de retour :

| Exit code | Statut | Conduite à tenir |
|---|---|---|
| `0` | Réseau opérationnel | Procéder à la vérification complète (`--check-content`). |
| `2` | Bloqué par l'allowlist Cowork | **Basculer en mode dégradé** (production manuelle du tableau structuré, comme en mode CHAT). Afficher à l'utilisateur le message d'allowlist (voir ci-dessous). |
| `3` | Autre erreur réseau | Tenter à nouveau ; si échec persistant, basculer en mode dégradé et signaler le détail technique à l'utilisateur. |
| `4` | Bloqué par challenge anti-bot Cloudflare | **Basculer sur le canal OpenLegi** (cf. section ci-dessous). Ce blocage est imposé par Légifrance lui-même, indépendamment de Cowork ; aucune action de l'utilisateur ne peut le lever. |

**Message à afficher à l'utilisateur en cas de blocage par allowlist** (à reproduire textuellement) :

> ⚠️ La vérification automatique des liens Légifrance n'est pas possible dans ce sandbox : l'accès réseau à `www.legifrance.gouv.fr` est bloqué par l'allowlist Cowork. Je bascule sur la vérification en mode dégradé : énumération explicite des références une par une, confirmation de la traçabilité de chaque appel d'outil dans la session.
>
> **Pour activer la vérification automatique** (qui constitue un gage de fiabilité supplémentaire — détection des URL bien formées mais pointant vers une décision sans rapport, par exemple), autorise les domaines suivants dans *Settings → Capabilities → Network access* :
>
> - `www.legifrance.gouv.fr`
> - `www.conseil-constitutionnel.fr`
> - `hudoc.echr.coe.int`
> - `curia.europa.eu`
> - `eur-lex.europa.eu`
>
> Sur Team / Enterprise, contacter l'admin de l'organisation. Une fois l'autorisation effective, la vérification automatique reprendra automatiquement à la session suivante.

Le mode dégradé n'est pas un échec de la checklist : c'est une dégradation gracieuse, conforme à la même rigueur de fond que le mode CHAT, simplement sans la double vérification automatique du contenu HTML.

### Bascule sur le canal OpenLegi (exit code 4 — challenge anti-bot)

Depuis le déploiement par Légifrance d'un challenge anti-bot Cloudflare, le serveur retourne systématiquement HTTP 403 (avec en-tête `cf-mitigated: challenge`) aux requêtes automatisées émanant des sandbox d'agents, *quelle que soit la configuration de l'allowlist Cowork*. La couche réseau est opérationnelle ; c'est Légifrance qui rejette la requête.

Dans ce cas, la vérification HTTP directe via `--check-content` est inopérante pour les domaines Légifrance, mais reste opérationnelle pour les domaines voisins (HUDOC, Curia, EUR-Lex, conseil-constitutionnel.fr) qui ne pratiquent pas ce challenge. La stratégie de vérification se scinde donc en deux canaux :

1. **Pour les identifiants Légifrance** (LEGIARTI, JURITEXT, CETATEXT, JORFTEXT, JORFARTI, LEGITEXT, CNILTEXT, KALITEXT) : **vérification par appel API via OpenLegi**, qui ne passe pas par le frontal Cloudflare et reste donc accessible. Le mode `--extract-ids` du script identifie chaque identifiant dans le livrable et indique l'outil OpenLegi à appeler :

   ```bash
   python3 scripts/verify_links.py --extract-ids --from-file urls.json
   ```

   La sortie JSON liste, pour chaque identifiant, les champs `openlegi_tool` (par exemple `OpenLegi:get_decision_judiciaire` pour un JURITEXT), `openlegi_argument` et `openlegi_verification_instruction` qui décrit ce qu'il faut vérifier (juridiction, date, numéro d'affaire, état juridique du texte, date d'entrée en vigueur, etc.). L'agent appelle ensuite OpenLegi pour chaque identifiant et confronte la réponse à la citation.

2. **Pour les domaines non-Légifrance** (HUDOC, Curia, EUR-Lex, conseil-constitutionnel.fr) : la vérification HTTP par `--check-content` reste utilisable normalement.

Cette bascule est *plus rigoureuse* que la vérification HTTP, et non moins : OpenLegi retourne, en sus de l'existence de l'identifiant, l'état juridique du texte et la date d'entrée en vigueur de la rédaction citée — ce qui couvre directement la règle (c) « vérification temporelle obligatoire » de l'étape 5.

**Message à afficher à l'utilisateur en cas de blocage anti-bot** (à reproduire textuellement) :

> ℹ️ La vérification automatique des liens Légifrance par requête HTTP n'est plus possible : Légifrance bloque désormais les requêtes automatisées des sandbox d'agents par un challenge anti-bot Cloudflare. La couche réseau est opérationnelle (autres domaines accessibles), mais le serveur Légifrance refuse les requêtes. Je bascule sur la vérification par appel API OpenLegi, qui n'est pas affectée par ce blocage et qui apporte en outre la vérification de l'état juridique et de la date d'entrée en vigueur des textes cités. Aucune action de votre part n'est requise.


## Tableau structuré obligatoire — artefact de vérification

À compter de la version 1.3.0 / 7.3.0, l'« énumération mentale » est proscrite : la checklist prend la forme d'un **tableau structuré produit avant livraison effective et inscrit dans la session** (en mode COWORK, il peut également être sauvegardé comme livrable séparé). Le tableau est l'artefact concret qui démontre que la checklist a été passée intégralement.

**Une ligne par citation effective dans le document.** Une référence appelée à plusieurs endroits du livrable compte autant de fois qu'elle est citée — chaque occurrence doit être confrontée à l'assertion qu'elle fonde dans son contexte propre.

**Quatre colonnes** (cinq en cassation, avec la voix énonciative) :

| Citation telle qu'écrite dans le document | Outil + identifiant (CID/JURITEXT/CETATEXT/JORFTEXT/DOI/HAL) | Extrait textuel pertinent retourné par l'outil | Voix (cassation) | Soutient l'assertion ? (✓ / ✗ / reformulation) |

**Priorisation pour les livrables volumineux (passage à l'échelle)** :

La règle « une ligne par occurrence » convient aux livrables courts (corrigé, fiche de TD, consultation brève). Pour un cours complet ou un ouvrage comportant des dizaines de citations, elle devient ingérable et fait courir le risque d'une exécution tronquée. Appliquer alors :

- **P1** — référence fondant une majeure, citée en introduction/conclusion, ou répétée plus de trois fois : vérification **à l'occurrence** (content-matching dans chaque contexte).
- **P2** — référence illustrative citée une à trois fois : vérification **à la référence** (content-matching unique).
- **P3** — référence en bibliographie seule : vérification d'existence et d'identifiant, sans content-matching d'assertion.

Le squelette du tableau peut être pré-rempli via `scripts/extract_references.py --file [livrable]`, qui détecte les références et leur localisation (et permet d'attribuer la priorité P1/P2/P3 à partir du nombre d'occurrences).

**Règles d'usage** :

- Le tableau est produit avant livraison effective et inscrit dans la session (ou comme livrable séparé en mode COWORK).
- Le critère d'avancement est binaire : tant qu'une ligne porte un ✗ ou une mention « à reformuler », la livraison est **bloquée**. Pour ces lignes, appliquer l'une des trois issues du content-matching — (i) changer de référence, (ii) reformuler la proposition pour qu'elle corresponde au contenu réel, (iii) basculer en formulation impersonnelle — puis remettre la ligne à jour.
- L'omission du tableau équivaut à l'omission de la checklist : la livraison ne peut être déclarée conforme sans lui.
- Une ligne ne peut être marquée ✓ que si l'extrait porté en colonne 3 fonde effectivement, et non par approximation, l'assertion correspondante du livrable.

### Artefact-modèle copiable

Le squelette ci-dessous est à dupliquer pour chaque livrable. Il est rédigé de telle sorte qu'il puisse être copié-collé (mode CHAT) ou inscrit dans un fichier séparé `tableau-verification-pre-livraison.md` (mode COWORK / CHAT_CU).

```markdown
# Tableau de vérification pré-livraison

**Livrable concerné** : [titre du document]
**Date** : [AAAA-MM-JJ]
**Mode** : [CHAT / CHAT_CU / COWORK]
**Préflight `verify_links.py`** : [exit code 0 / 2 / 3 / 4 — sans objet en mode CHAT]

| # | Citation telle qu'écrite dans le document | Outil + identifiant (CID/JURITEXT/CETATEXT/JORFTEXT/DOI/HAL) | Extrait textuel pertinent retourné par l'outil | Voix (cassation) | Soutient l'assertion ? (✓ / ✗ / reformulation) |
|---|---|---|---|---|---|
| 1 | [citation telle qu'elle figure dans le livrable] | [ex. `OpenLegi:rechercher_code` — LEGIARTI000006437058] | « [extrait textuel ou résumé fidèle des motifs / de l'article] » | — | ✓ |
| 2 | [citation] | [outil + identifiant] | « [extrait] » | — | ✗ → reformulation effectuée → ligne 2bis |
| 2bis | [nouvelle formulation impersonnelle ou nouvelle référence] | [outil + identifiant ou « formulation impersonnelle »] | « [extrait, le cas échéant] » | — | ✓ |
| 3 | [extrait d'arrêt de cassation] | [`Themia:...` + `OpenLegi:...` (lien Légifrance)] | « [motif propre de la Cour] » | voix_cour | ✓ |
| … | … | … | … | … | … |

**Synthèse** :
- Lignes contrôlées : X
- Reformulations effectuées : Y
- Références non tracées résiduelles : 0 (impérativement)

**Formule de clôture** :

> « Tableau de vérification produit ; X lignes contrôlées ; Y reformulations effectuées ; aucune référence non tracée ne subsiste. La livraison est autorisée. »
```

### Formule de clôture explicite

À l'issue de la checklist — et seulement si toutes les lignes du tableau portent ✓ —, la skill prononce explicitement, dans la session, la formule suivante (en adaptant les variables `X` et `Y`) :

> « Tableau de vérification produit ; X lignes contrôlées ; Y reformulations effectuées ; aucune référence non tracée ne subsiste. La livraison est autorisée. »

Sans cette formule prononcée explicitement, **et** sans l'artefact-tableau correspondant, la livraison **ne doit pas être déclarée**. La présence de la formule sans le tableau associé est aussi grave que l'absence de l'une et de l'autre : la formule est l'attestation de la production du tableau, non son substitut.

## Les cinq étapes obligatoires

Les cinq étapes ci-dessous correspondent aux opérations qui alimentent les colonnes du tableau structuré.

### Étape 1 — Lister exhaustivement les références citées

Lister **toutes** les références citées dans le document, en trois catégories distinctes :

**(a) Citations jurisprudentielles** — pour chacune, recenser : juridiction, date, numéro de pourvoi / requête / affaire, lien Légifrance. En cassation (Themia), noter la **voix énonciative** de tout extrait cité.

**(b) Références à des textes normatifs précis** — pour chacune, recenser : intitulé du texte ou code, numéro d'article, version applicable (date d'entrée en vigueur de la rédaction citée), lien Légifrance.

**(c) Références doctrinales** — pour chacune, recenser : auteur, titre, support (revue/ouvrage/thèse), année, et **identifiant vérifiable** (DOI, identifiant HAL, ou URL d'une base reconnue). Une référence doctrinale sans identifiant vérifiable est traitée comme « non vérifiée » (cf. Conduite à tenir en cas d'échec).

L'inventaire doit être exhaustif : toute référence présente dans le livrable y figure, y compris celles que la skill jugerait « évidentes » ou « ultra-classiques » (art. 1240 C. civ., arrêt Costedoat, etc.). C'est précisément sur ces références que la vigilance doit être maximale.

### Étape 2 — Vérifier la traçabilité de chaque référence (colonne 2 du tableau)

Pour chaque référence inventoriée à l'étape 1, vérifier qu'un appel à un outil de recherche (OpenLegi, LegalDataHunter, web_search ciblé sur une source officielle) figure dans la session courante **pour cette référence précise**, et reporter l'outil + l'identifiant en colonne 2 du tableau.

La traçabilité ne se présume pas : si la référence n'est pas rattachable à un appel d'outil identifiable, elle est **présumée hallucinée** jusqu'à preuve du contraire.

### Étape 3 — Content-matching : confronter le contenu retourné à l'assertion (colonnes 3 et 4)

C'est l'étape qui prévient les hallucinations par mauvaise attribution. Pour chaque référence tracée à l'étape 2 :

1. **Lire le contenu réel** retourné par l'outil — motifs et dispositif de la décision, alinéa exact de l'article, contenu textuel de la fiche OpenLegi. La fiche de métadonnées seule ne suffit pas.
2. **Reporter en colonne 3** un extrait textuel pertinent (motif d'arrêt, alinéa d'article, etc.).
3. **Confronter cet extrait à l'assertion** que la référence est censée fonder. Renseigner la colonne « Soutient l'assertion ? » :
   - **✓** : le contenu retourné soutient effectivement l'assertion.
   - **✗** : le contenu retourné ne soutient pas l'assertion (mauvaise attribution).
   - **reformulation** : l'écart est levé en reformulant la proposition pour qu'elle colle au contenu réel.
4. **En cassation (Themia)** : renseigner la colonne « Voix » et vérifier la cohérence de l'attribution énonciative — un extrait présenté comme position de la Cour doit provenir de `passage_voix_cour` / `passage_visas` / `passage_chapeau` (tag `voix:cour_cassation`), non de `passage_motifs_ca` (cour d'appel) ni de `passage_moyens` (parties). Une attribution énonciative erronée vaut ✗.
5. **Pour la doctrine** : vérifier que l'identifiant (DOI/HAL/URL) résout vers la référence annoncée et que la thèse attribuée à l'auteur correspond au contenu réel (résumé, propos effectivement tenu) — non à une reconstruction plausible.

Pour toute ligne non-✓, appliquer l'une des trois issues du content-matching :

1. **Changer de référence** — relancer une recherche pour identifier le texte qui soutient effectivement l'assertion. Créer une nouvelle ligne du tableau (ou un sous-numéro `nbis`) reflétant la substitution.
2. **Reformuler la proposition** pour qu'elle corresponde au contenu réel de la référence. La nouvelle rédaction figure en colonne 1 ; la colonne 4 passe alors à « reformulation ».
3. **Basculer en formulation impersonnelle** — remplacer la citation par une formule du type « la jurisprudence constante retient que… » / « le droit commun de la responsabilité prévoit que… », sans numéro ni date précise. La référence numérique disparaît du livrable.

Tant qu'une ligne porte un ✗ ou une mention « à reformuler », la livraison est bloquée.

Pour toute référence par ailleurs **non tracée** (échec à l'étape 2), appliquer trois solutions strictement parallèles :

1. **Vérifier immédiatement** — exécuter la recherche manquante. Si elle confirme la référence ET que le contenu soutient l'assertion, conserver et passer à l'étape 4. À défaut, suivre l'une des deux voies ci-dessous.
2. **Supprimer** — retirer purement et simplement la référence du livrable.
3. **Convertir en formulation impersonnelle**.

Une quatrième voie, à utiliser avec parcimonie, consiste à conserver la référence en la signalant explicitement comme « à vérifier » dans le livrable et dans la colonne 4 du tableau. Cette voie n'est admise que si l'utilisateur a explicitement accepté de recevoir des références non vérifiées (ce qui doit toujours être préféré à une livraison silencieuse de références incertaines).

### Étape 4 — Vérifier la présence et la validité du lien officiel / identifiant vérifiable

Pour chaque référence **jurisprudentielle et normative**, vérifier que :

1. un lien Légifrance figure dans le livrable ;
2. le lien correspond à un pattern Légifrance reconnu (`JURITEXT`, `CETATEXT`, `JORFTEXT`, `JORFARTI`, `LEGIARTI`, `LEGITEXT`, `CNILTEXT`, `KALITEXT`) ;
3. l'identifiant cité correspond bien, sur le fond, à la référence du livrable. Le canal de vérification dépend du résultat du préflight (cf. section « Dégradation conditionnelle » plus haut) :
   - **Exit code 0** (réseau opérationnel) : exécuter `verify_links.py --check-content` qui récupère la page HTML et confronte le numéro / mot-clé attendu au contenu.
   - **Exit code 4** (blocage anti-bot Cloudflare — cas le plus fréquent en sandbox depuis 2026) : exécuter `verify_links.py --extract-ids` qui produit, pour chaque identifiant Légifrance, le nom de l'outil OpenLegi à appeler. L'agent appelle alors OpenLegi pour chaque identifiant et vérifie que la réponse confirme la citation. Pour les domaines non-Légifrance (HUDOC, Curia, EUR-Lex, conseil-constitutionnel.fr), conserver la vérification HTTP par `--check-content` qui reste opérationnelle.
   - **Exit code 2** (blocage par allowlist Cowork) : vérification ligne par ligne par lecture de la fiche OpenLegi correspondante (mode dégradé), comme en mode CHAT.

Pour chaque référence **doctrinale**, vérifier qu'un **identifiant vérifiable** (DOI, identifiant HAL, ou URL d'une base reconnue) figure et résout vers la référence annoncée. Une référence doctrinale sans identifiant vérifiable est traitée selon la procédure de l'étape 3 (non vérifiée → signalée ou supprimée).

Toute référence sans lien ou identifiant valide est traitée selon la procédure de l'étape 3.

### Étape 5 — Vérifier la rédaction applicable des textes normatifs

Pour chaque texte normatif cité (article de code, loi, décret, etc.), vérifier que :

1. la rédaction citée est bien celle **en vigueur à la date pertinente** : pour un cas pratique ou un commentaire d'arrêt, la **date des faits de l'énoncé** (ou de l'espèce commentée), et non la date du jour ; pour une consultation prospective ou un cours portant sur le droit positif, la date du jour. La date pivot est déterminée explicitement et, si l'énoncé est muet, fixée par hypothèse signalée ;
2. lorsque le texte a connu des modifications récentes susceptibles d'affecter le raisonnement, la version applicable est explicitement précisée. Exemple de mention attendue : « art. 1242 al. 4 C. civ., dans sa rédaction issue de la loi n° 2025-568 du 23 juin 2025 ».

## Conduite à tenir en cas d'échec

Toute référence qui ne passe pas l'une des cinq étapes ci-dessus relève de **l'une** de ces trois issues — jamais d'autre :

1. **Vérification réussie tardive** — la référence est tracée *a posteriori* via une recherche et confirmée. Conserver.
2. **Suppression** — la référence est retirée. Le raisonnement est éventuellement reformulé sans elle (formulation impersonnelle, recours à une autre référence vérifiée).
3. **Mention explicite « à vérifier »** — la référence est conservée mais signalée par une mention explicite dans le livrable, et l'utilisateur est informé.

L'inaction (livraison du livrable malgré l'échec) est **interdite**.

## Exemples illustratifs

### Exemple A — Checklist passée

Un corrigé de cas pratique de responsabilité du fait des choses cite :

| # | Citation | Outil + identifiant | Extrait | Soutient ? |
|---|---|---|---|---|
| 1 | art. 1242 al. 1er C. civ. | `OpenLegi:rechercher_code` — LEGIARTI000006437058 | « On est responsable non seulement du dommage que l'on cause par son propre fait, mais encore de celui qui est causé par le fait […] des choses que l'on a sous sa garde. » | ✓ |
| 2 | Cass. ch. réunies, 13 févr. 1930, *Jand'heur* | `OpenLegi:rechercher_jurisprudence_judiciaire` — JURITEXT… | « la présomption de responsabilité […] ne peut être détruite que par la preuve d'un cas fortuit ou de force majeure ou d'une cause étrangère qui ne lui soit pas imputable » | ✓ |

> « Tableau de vérification produit ; 2 lignes contrôlées ; 0 reformulations effectuées ; aucune référence non tracée ne subsiste. La livraison est autorisée. »

### Exemple B — Checklist échouée pour défaut de traçabilité, et corrigée

Un corrigé de cas pratique mentionne « Cass. civ. 2e, 8 juill. 2004, n° 03-12.244 ».

À l'étape 2, la skill constate qu'aucun appel à `OpenLegi:rechercher_jurisprudence_judiciaire` ne figure dans la session pour cette référence. La colonne 2 du tableau reste vide ; la colonne 4 passe à ✗ par défaut de traçabilité.

À l'étape 3, la skill exécute `OpenLegi:rechercher_jurisprudence_judiciaire` avec `champ: "NUM_AFFAIRE"`, `type_recherche: "EXACTE"`, `search: "03-12.244"`. La réponse retourne un arrêt portant sur l'administrateur judiciaire, sans rapport avec la responsabilité du fait des choses : la référence est **infirmée** sur le fond. La colonne 3 — « extrait » — porte les motifs réels de l'arrêt, qui ne soutiennent pas l'assertion ; la colonne 4 reste donc à ✗.

La skill applique alors la troisième issue (formulation impersonnelle) et reformule le passage concerné : « la jurisprudence constante de la deuxième chambre civile retient que la garde implique une maîtrise effective de la chose ». La référence numérique disparaît du livrable, et la ligne du tableau passe à « reformulation ».

Livrable corrigé, tableau repassé, formule de clôture prononcée :

> « Tableau de vérification produit ; 1 ligne contrôlée ; 1 reformulation effectuée ; aucune référence non tracée ne subsiste. La livraison est autorisée. »

### Exemple C — Hallucination par mauvaise attribution (tracée formellement mais infirmée par le contenu)

Un corrigé de cas pratique de responsabilité civile mentionne « la conduite d'un engin sciemment débridé en violation de l'article R. 412-43-3 du Code de la route ».

À l'étape 2, la skill constate qu'un appel à `OpenLegi:rechercher_code` a bien été exécuté dans la session pour cet article : la traçabilité formelle est satisfaite, et la colonne 2 est renseignée (`OpenLegi:rechercher_code` — CID identifiant l'art. R. 412-43-3 C. route).

À l'étape 3 (content-matching), la skill **lit le contenu retourné** par OpenLegi et le reporte en colonne 3 : l'article R. 412-43-3 fixe l'âge minimum de quatorze ans pour la conduite d'un EDPM et impose le port d'équipement rétro-réfléchissant la nuit. Confronté à l'assertion (la conduite d'un engin débridé), il ne la soutient pas : la colonne 4 passe à ✗.

La skill applique l'issue (i) (changer de référence) : recherche complémentaire sur la vitesse maximale par construction des EDPM ; OpenLegi retourne l'art. R. 311-1, 6.15, du Code de la route, dont le contenu fixe précisément la vitesse maximale par construction à 25 km/h. Le tableau est mis à jour : nouvelle ligne dont la colonne 4 passe à ✓.

> « Tableau de vérification produit ; 1 ligne contrôlée ; 1 reformulation/substitution effectuée ; aucune référence non tracée ne subsiste. La livraison est autorisée. »

Cet exemple illustre le scénario nouveau couvert par la version 1.3.0 / 7.3.0 : la vérification de traçabilité formelle (étape 2) est insuffisante ; seule l'étape 3 de content-matching prévient ce type d'hallucination.
