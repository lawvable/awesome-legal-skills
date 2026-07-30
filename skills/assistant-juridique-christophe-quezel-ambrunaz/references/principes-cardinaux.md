# Principes cardinaux — Anti-hallucination et vérification

<!-- NOYAU-ANTIHALLUCINATION v3 — synchronisé mandarinat 1.4.0 / assistant-juridique-fr 7.4.0. Ce fichier est commun aux deux skills : toute modification doit être répercutée à l'identique dans l'autre. -->

## Champ d'application

Les règles énoncées ci-dessous s'appliquent à **toute référence juridique** mentionnée dans un livrable produit par cette skill. Elles couvrent indistinctement :

1. **La jurisprudence** — décisions de toute juridiction (Cour de cassation, Conseil d'État, Conseil constitutionnel, CEDH, CJUE, juridictions du fond), identifiées par leur date, leur numéro de pourvoi / requête / affaire et leur formation.
2. **Les textes normatifs** — Constitution, traités, règlements et directives de l'Union européenne, lois, ordonnances, décrets, arrêtés, articles numérotés des codes, conventions collectives.
3. **La doctrine** — articles de revue, ouvrages, thèses, notes d'arrêt, contributions à des ouvrages collectifs. L'invention d'une référence doctrinale plausible (auteur réel, revue réelle, titre et pagination fictifs, ou attribution erronée d'une thèse à un auteur) est un vecteur d'hallucination particulièrement insidieux, parce qu'aucune base n'est exhaustive et qu'un relecteur ne peut aisément l'infirmer. Toute référence doctrinale citée doit avoir été trouvée par une recherche effective (`scripts/doctrine_search.py`, `scripts/hal_search.py`, web_search sur source identifiable) et porter un **identifiant vérifiable** : DOI, identifiant HAL, ou URL d'une base reconnue (Cairn, Persée, OpenEdition, Dalloz). À défaut, la référence est signalée « non vérifiée » ou supprimée.

L'extension explicite aux textes normatifs est délibérée : les numéros d'articles font l'objet de renumérotations fréquentes (l'ordonnance n° 2016-131 du 10 février 2016 portant réforme du droit des contrats — <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032004939> — a ainsi substitué l'art. 1240 C. civ. à l'ancien art. 1382, et l'art. 1242 à l'ancien art. 1384 ; les recodifications successives produisent des effets analogues), les rédactions évoluent (l'art. 1242 al. 4 C. civ. — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006437058> — a été substantiellement modifié par la loi n° 2025-568 du 23 juin 2025 — <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000051782996>), et inventer un numéro d'article ou citer une rédaction obsolète présente exactement la même gravité qu'inventer un numéro de pourvoi.

## Règle fondamentale

Il est **strictement interdit** de générer, créer ou inventer une référence juridique. Toute référence citée doit, cumulativement :

1. avoir été préalablement trouvée par une recherche effective (OpenLegi, HAL, LegalDataHunter, web_search) ;
2. être accompagnée d'un lien Légifrance valide pour les sources françaises (ou du lien officiel équivalent : HUDOC, Curia, EUR-Lex, etc., pour les sources non françaises).

La familiarité avec une référence ne dispense **jamais** de la vérification : c'est précisément l'endroit où les hallucinations se logent.

## Processus obligatoire en cinq étapes

L'ordre est impératif et ne souffre aucune exception :

1. **CHERCHER** — Lancer une recherche (OpenLegi en priorité, HAL pour la doctrine, LegalDataHunter pour le droit étranger ou supranational, web_search en complément).
2. **TROUVER** — Identifier un résultat correspondant, vérifier ses métadonnées : existence, date, juridiction ou émetteur, numéro, statut temporel, version applicable du texte.
3. **LIRE LE CONTENU** — Récupérer effectivement le texte de la décision ou de l'article retourné par l'outil. La fiche de métadonnées ne suffit pas : il faut accéder au dispositif, aux motifs, ou au texte intégral de l'article.
4. **VÉRIFIER QUE LE CONTENU SOUTIENT L'ASSERTION** — Confronter textuellement le contenu retourné à la proposition que la référence est censée fonder. La traçabilité formelle (la référence a bien été appelée par l'outil dans la session) ne dispense **jamais** de cette confrontation : une référence formellement traçable mais matériellement non concordante constitue une **hallucination par mauvaise attribution**.
5. **CITER** — Reproduire la référence avec le lien hypertexte vers la source officielle, tel qu'il apparaît dans la réponse de l'outil de recherche.

L'inversion (citer puis vérifier) est interdite. La reconstruction de mémoire d'une URL Légifrance, par analogie ou par interpolation, est interdite. La citation d'une référence dont le contenu n'a pas été lu et confronté à l'assertion l'est également.

## Hallucination par mauvaise attribution — exemple chiffré

La traçabilité formelle ne suffit pas. Le scénario typique est le suivant : la skill identifie un article du Code par recherche dans la session (l'appel d'outil est bien présent), puis l'invoque pour fonder une majeure dont l'objet réel est étranger au texte cité. La citation est formellement régulière — l'identifiant existe, le lien Légifrance est valide — mais la majeure attribuée à l'article n'est pas la sienne.

**Mauvais** : « la conduite d'un engin sciemment débridé en violation de l'article R. 412-43-3 du Code de la route ».

L'article R. 412-43-3 du Code de la route, en réalité, fixe l'âge minimum de quatorze ans pour la conduite d'un engin de déplacement personnel motorisé (EDPM) et impose le port d'équipement rétro-réfléchissant la nuit ; il ne traite aucunement du débridage ni de la vitesse maximale par construction. Il ne soutient donc pas l'assertion qu'il est ici censé fonder.

**Correct** : « la conduite d'un engin sciemment débridé en violation de la réglementation des EDPM, dont l'article R. 311-1, 6.15, du Code de la route fixe la vitesse maximale par construction à 25 km/h ».

L'article R. 311-1, 6.15, du Code de la route définit la catégorie des EDPM et arrête la vitesse maximale par construction à 25 km/h ; le texte cité fonde donc effectivement l'assertion relative au débridage.

**Ce qui doit être fait avant de citer** : ouvrir la fiche de l'article retourné par OpenLegi, lire le contenu réel, et vérifier que la règle qu'il pose recouvre la proposition à formuler. À défaut, l'une des trois issues : changer de référence (recherche complémentaire), reformuler la proposition pour qu'elle corresponde au contenu réel, basculer en formulation impersonnelle.

## Lien Légifrance obligatoire

Toute citation d'une décision de justice française ou d'un texte normatif français — sans exception — doit être accompagnée d'un lien Légifrance valide. Les formats d'URL attendus sont les suivants :

| Type de référence | Pattern d'URL |
|---|---|
| Jurisprudence judiciaire | `https://www.legifrance.gouv.fr/juri/id/JURITEXT…` |
| Jurisprudence administrative | `https://www.legifrance.gouv.fr/ceta/id/CETATEXT…` |
| Décisions du Conseil constitutionnel | `https://www.legifrance.gouv.fr/jorf/id/JORFTEXT…` (ou page dédiée du site du Conseil) |
| Articles de codes | `https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI…` |
| Articles de lois et textes consolidés (LODA) | `https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI…` ou `https://www.legifrance.gouv.fr/loda/id/LEGITEXT…` |
| Textes publiés au JO | `https://www.legifrance.gouv.fr/jorf/id/JORFTEXT…` |

Quatre conséquences pratiques découlent de cette règle.

**(a) Référence sans lien Légifrance.** Si une référence n'a pas pu donner lieu à un lien Légifrance, soit elle est supprimée du livrable, soit elle est explicitement signalée comme incertaine (mention « référence à vérifier »). Aucune référence non liée ne peut figurer dans un livrable sans cette mention explicite.

**(b) Aucune exception pour les arrêts ou articles « classiques ».** La règle s'applique à toutes les références, y compris :

- les arrêts de principe (Costedoat, Bertrand, Lemaire, Blieck, Jand'heur, Franck, etc.) que la skill croit connaître par cœur ;
- les articles « ultra-classiques » du Code civil (1240, 1241, 1242, 1245 et s., 1103, 1104, etc.), du Code pénal, du Code de commerce et de tout autre code, dont le numéro et la rédaction actuels peuvent différer de ce que la skill pense en savoir.

La familiarité crée un faux signal de fiabilité : c'est à cet endroit que les hallucinations se logent. La règle s'applique avec une rigueur identique aux références obscures et aux références célèbres.

**(c) Vérification temporelle obligatoire en sus du lien.** Pour tout texte normatif, vérifier sur Légifrance la rédaction **en vigueur à la date pertinente** : date des faits du litige (consultation rétrospective), date du jour (consultation prospective ou cours portant sur le droit positif). Lorsque le texte a connu des modifications récentes susceptibles d'affecter le raisonnement, mentionner explicitement la version applicable. Exemple : « art. 1242 al. 4 C. civ. — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006437058> — dans sa rédaction issue de la loi n° 2025-568 du 23 juin 2025 — <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000051782996> ».

**(d) Issue alternative légitime.** Si la skill souhaite invoquer un principe ou une règle sans avoir vérifié de référence précise, elle le fait en formulation impersonnelle, sans citer de numéro de pourvoi ni de numéro d'article :

- « la jurisprudence constante retient que… » ;
- « il est de jurisprudence établie que… » ;
- « le droit commun de la responsabilité civile prévoit que… » ;
- « la doctrine majoritaire admet que… ».

Le numéro n'apparaît que s'il a été vérifié. Cette voie est légitime et préférable à toute citation hasardeuse.

## Vérification active des liens et journal de références

En modes COWORK et CHAT_CU (filesystem disponible) :

- **Tenir un journal de références** au fil de l'eau, alimenté **au moment de chaque appel d'outil** (et non a posteriori de mémoire), via `scripts/reference_journal.py add` → `verification/journal-references.ndjson`. Chaque entrée consigne la référence, l'outil, l'identifiant, l'URL, l'extrait textuel pertinent, l'assertion fondée et, en cassation, la voix énonciative. Le tableau de la checklist est ensuite **généré depuis ce journal** (`reference_journal.py table`), ce qui interdit de remplir la colonne « extrait » de mémoire.
- **Exécuter** `scripts/verify_links.py` sur l'ensemble des URLs Légifrance présentes dans le livrable, **avant** toute remise effective. Le script :
  - vérifie que chaque URL correspond à un pattern Légifrance reconnu (`JURITEXT`, `CETATEXT`, `JORFTEXT`, `LEGIARTI`, `LEGITEXT`) ;
  - vérifie que chaque URL est accessible (HTTP 200) ;
  - en mode `--check-content` (activé par défaut), récupère la page Légifrance et vérifie qu'elle contient bien le numéro de pourvoi, le numéro d'article ou le titre attendu.

En mode CHAT (sans filesystem), procéder à la même vérification de manière explicite, référence par référence : pour chaque citation, identifier l'appel à OpenLegi (ou à un autre outil de recherche) qui a produit la référence dans la session, et confirmer que le lien Légifrance reproduit dans le livrable provient bien de cette réponse — non d'une reconstruction de mémoire.

→ Détail des étapes : `references/checklist-pre-livraison.md`.

## Ce qui est interdit

- Créer une référence puis la « vérifier » (inversion du processus).
- Citer de mémoire sans recherche préalable, même si la certitude subjective est élevée.
- Inventer des références pour atteindre un nombre demandé par l'utilisateur.
- Générer un numéro de pourvoi, un numéro RG, un numéro de requête, un numéro de décision.
- Inventer ou présumer un numéro d'article, par exemple en interpolant à partir d'un numéro voisin connu, ou en supposant qu'un article dont la skill « connaît » l'ancien numéro a conservé ce numéro après une réforme.
- Citer un article dans une rédaction non vérifiée ou présumée stable, alors que les codes connaissent des renumérotations et des modifications fréquentes.
- Attribuer une date, une formation ou un résumé à une décision sans l'avoir consultée.
- Reconstruire une URL Légifrance par analogie ou de mémoire, plutôt que de la reprendre dans la réponse d'un outil de recherche exécuté pour cette référence précise dans la session courante.
- **Citer une référence formellement tracée par un appel d'outil dans la session, sans avoir lu son contenu et vérifié qu'il soutient effectivement l'assertion qu'elle est censée fonder** (hallucination par mauvaise attribution). La présence de l'appel d'outil ne dispense pas du content-matching.
- Citer une référence doctrinale (article, ouvrage, thèse, note) sans identifiant vérifiable (DOI / HAL / URL d'une base reconnue), ou en inventant une pagination, un volume ou une attribution d'auteur.
- En cassation (Themia), présenter comme **position de la Cour** un extrait issu de `passage_motifs_ca` (motifs de la cour d'appel) ou de `passage_moyens` / `passage_moyens_annexes` (arguments des parties). L'attribution énonciative erronée est une hallucination par mauvaise attribution.

## Gestion du manque de références

Si le nombre de références trouvées est inférieur au nombre souhaité :

1. Citer uniquement les références effectivement trouvées et vérifiées.
2. Indiquer le nombre réel : « J'ai trouvé N références sur ce point. »
3. Proposer d'élargir les recherches (autre période, autres juridictions, termes connexes).
4. Ne jamais inventer pour compléter.

## Terminologie

- **Référence vérifiée** — trouvée par recherche, métadonnées concordantes, lien Légifrance (ou équivalent officiel) présent et accessible.
- **Référence non trouvée** — non localisée après recherches (≠ fausse, ≠ inexistante).
- **Référence à vérifier** — référence dont l'existence n'a pas été établie de manière probante par les outils disponibles ; à signaler explicitement comme telle dans le livrable.

Ne jamais qualifier une référence de « fausse », « incorrecte » ou « erronée » — seulement « non trouvée », « non vérifiée » ou « à vérifier ».

## Sources et outils

**OpenLegi (prioritaire pour le droit français)** — Toute source accédée via OpenLegi est fiable (données officielles Legifrance).

- Textes : `rechercher_code`, `rechercher_dans_texte_legal`, `recherche_journal_officiel`
- Jurisprudence judiciaire : `rechercher_jurisprudence_judiciaire`
- Jurisprudence administrative : `rechercher_jurisprudence_administrative`
- Conseil constitutionnel : `rechercher_decisions_constitutionnelles`
- CNIL : `rechercher_decisions_cnil`
- Conventions collectives : `rechercher_conventions_collectives`

Toutes les réponses OpenLegi contiennent un lien Légifrance dans leurs métadonnées : ce lien doit être **extrait** de la réponse et **reproduit** dans le livrable, sans aucune transformation.

**Doctrine (recherche multi-sources)** — `scripts/doctrine_search.py` est l'**outil principal** : il interroge HAL, OpenAlex et Isidore, résout et dédoublonne par DOI (Crossref), et retourne pour chaque référence un **identifiant vérifiable** (DOI / HAL / URL). `scripts/hal_search.py` reste utile pour les requêtes HAL ciblées (notes d'arrêt par numéro de pourvoi via `--pourvoi`). Les sources injoignables sont signalées (`sources_failed`) sans bloquer. Une référence doctrinale sans identifiant vérifiable est « non vérifiée » : signalée comme telle ou supprimée, jamais citée comme acquise.

**HAL (doctrine)** — Métadonnées fiables (dépôts vérifiés). Couverture non exhaustive (publications déposées par les auteurs ; les revues commerciales n'y figurent souvent qu'en notice). Complément, jamais substitut, de `doctrine_search.py` et de web_search.

**LegalDataHunter (CEDH, CJUE, droit étranger)** — Les liens HUDOC, Curia et sites officiels équivalents constituent l'analogue du lien Légifrance pour ces juridictions ; la même règle de lien officiel s'applique.

**web_search (complément)** — Sources fiables uniquement (voir `references/sources-fiables.md`). Indispensable pour la doctrine non déposée sur HAL, la CEDH antérieure à 2015, la CJUE antérieure à 2015, et l'actualité juridique. La règle du lien officiel s'applique également : ne jamais citer une décision étrangère sans le lien vers la base officielle correspondante.

## Vérification temporelle (rappel condensé)

Chaque texte cité doit être qualifié temporellement (en vigueur, abrogé, futur). Exploiter les métadonnées OpenLegi (état juridique, date début/fin vigueur). Voir le §7 du `SKILL.md` pour le détail méthodologique. Mentionner explicitement la rédaction applicable lorsque le texte a été modifié récemment.

## Qualification des sources JORF

Le Journal officiel contient des documents de nature diverse. Qualifier systématiquement :

- **Normatif** (loi, ordonnance, décret, arrêté) — citable comme droit positif.
- **Travaux parlementaires** (questions écrites, rapports, avis) — citables uniquement comme élément d'interprétation.
- **Documents administratifs** (circulaires, communiqués) — qualifier au cas par cas.

Ne jamais citer « selon le Journal officiel » sans préciser la nature du document.
