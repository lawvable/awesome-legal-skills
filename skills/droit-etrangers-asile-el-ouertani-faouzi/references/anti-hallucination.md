# Couche anti-hallucination

Fichier à charger avant toute rédaction comportant des références. Il ne répète pas des principes généraux : il liste les mécanismes concrets par lesquels une référence fausse entre dans un document juridique, et le contrôle qui l'arrête.

Prémisse à garder en tête : **un outil MCP réduit le risque d'hallucination, il ne l'élimine pas.** OpenLegi est une interface d'accès à Légifrance, pas Légifrance. Ce que retourne l'outil est une représentation intermédiaire — filtrée, mise en forme, mise en cache — du texte officiel. Seul le texte lu sur Légifrance fait foi. Cette limite est documentée par l'éditeur lui-même ; l'ignorer, c'est déplacer la confiance aveugle d'un cran sans la supprimer.

## A. Les six mécanismes de contamination

### A1 — Numéro réaffecté après renumérotation
Une réforme peut réaffecter un ancien numéro à un article entièrement différent. L'outil retourne l'article en vigueur portant ce numéro, sans signaler qu'il ne s'agit pas du texte historiquement attendu.

En droit des étrangers, ce risque est maximal : le CESEDA a été intégralement renuméroté en 2021.

*Contrôle* : croiser le numéro retourné avec **la section parente** et **les premiers mots du texte**. Si un article censé traiter du séjour retourne un texte sur autre chose, c'est une réaffectation, pas une erreur de l'outil.

### A2 — Renvois internes orphelines
Un article en vigueur peut renvoyer à un article abrogé. L'outil retourne le texte brut sans valider la cohérence des renvois.

*Signal d'alerte* : article de version faible (v1.0, v2.0) avec une date de vigueur ancienne, surtout en partie réglementaire (R. ou D.).
*Contrôle* : vérifier chaque renvoi cité dans le raisonnement, pas seulement l'article principal.

### A3 — Troncature silencieuse
L'API peut retourner un texte tronqué, signalé par `...`. Un modèle peut restituer ce texte incomplet sans mentionner la coupure — ou pire, **compléter la fin de mémoire**.

*Signaux d'alerte* : texte se terminant par `…` ; alinéas numérotés (I., II., 1°, 2°) dont certains manquent ; article de version élevée (≥ 5.0).
*Contrôle* : ne jamais citer un article dont la complétude n'a pas été vérifiée sur Légifrance. Si la troncature est constatée, la signaler — jamais la combler.

### A4 — Paraphrase qui déplace la portée
Reformuler une disposition en modifiant son champ est la forme d'erreur la plus insidieuse, parce qu'elle est invisible au lecteur. Transformer « à titre privé **ou** confidentiel » en « en privé » efface une condition alternative et change le champ de la règle.

*Contrôle* : reproduire exactement le texte retourné, entre guillemets, quand la formulation porte l'analyse. Paraphraser est admis pour expliquer, jamais pour citer. En cas de doute : citer d'abord, expliquer ensuite.

### A5 — Faux positif du statut, et texte abrogé servi sans alerte
Le statut `VIGUEUR` confirme seulement que l'article existe dans la base consolidée. Il ne garantit ni la complétude du texte, ni la validité des renvois, ni que le numéro corresponde au texte cherché.

**Cas vérifié, spécifique au CESEDA** : interroger un ancien article (L.313-11) retourne un texte long, détaillé et parfaitement plausible — l'ancienne rédaction. Trois signaux, faciles à manquer dans une réponse volumineuse, révèlent le piège :
- `"etat": "ABROGE"`
- `"date_fin": "2021-05-01"` — la date de la recodification
- un champ `note` du type *« Article non trouvé à la date demandée ; version la plus récente retournée »*

Un modèle qui ne lit que le champ `texte` produit une citation impeccablement formatée d'un article mort depuis cinq ans.

*Contrôle* : lire `etat`, `date_debut`, `date_fin` et `note` **avant** le texte. Traiter `VIGUEUR` comme une condition nécessaire, jamais suffisante ; traiter tout `note` ou `ABROGE` comme un arrêt immédiat.

### A6 — Décalage de cache, et référence à une directive déjà remplacée
Une modification législative très récente peut ne pas être reflétée par les données servies. En droit des étrangers — trois réformes structurelles en cinq ans — ce risque est permanent.

**Cas vérifié** : l'article L.551-8 du CESEDA, en vigueur, renvoie encore explicitement à la « directive 2013/33/UE » alors que celle-ci est abrogée depuis le 12 juin 2026 par la directive (UE) 2024/1346. Le texte est authentique et à jour du point de vue de la base — c'est le **droit lui-même** qui n'a pas encore été mis en cohérence avec la réforme européenne, faute de loi d'habilitation (voir `etat-du-droit-2026.md` §4). Ne pas confondre ce décalage législatif réel avec un défaut de l'outil.

*Contrôle* : pour tout point touché par la loi de 2024, la circulaire de 2025, le décret nationalité de 2025 ou le Pacte européen de 2026, consulter Légifrance directement — et vérifier si le texte français cite encore une norme européenne abrogée.

## B. Les trois mécanismes propres au modèle

### B1 — Complétion par familiarité
Les références les plus connues sont les moins vérifiées, précisément parce qu'elles semblent évidentes. En droit des étrangers : L.435-1, L.611-1, L.423-23, la décision GISTI de 1978, l'article 8 CEDH.

*Contrôle* : la familiarité d'une référence augmente l'exigence de vérification au lieu de la réduire. Aucune exemption pour les « grands classiques ».

### B2 — Référence réelle, attribution fausse
Une décision qui existe, citée pour une solution qu'elle ne contient pas. C'est l'hallucination la plus difficile à détecter : le numéro est correct, le lien fonctionne, seul le contenu ne correspond pas.

*Contrôle* : le **content-matching** est non négociable. Lire le passage retourné et vérifier qu'il soutient l'assertion. Avoir appelé la décision ne suffit jamais.

### B3 — URL reconstruite par analogie
Fabriquer un lien en imitant le format d'un autre produit des liens morts ou pointant vers un autre texte.

*Contrôle* : recopier l'URL exactement telle que l'outil la retourne. Ne jamais construire un identifiant `LEGIARTI`, `LEGITEXT`, `JORFTEXT`, `CETATEXT` ou `JURITEXT` par déduction.

### B4 — Décision renversée, citée comme si elle tenait toujours
Une décision réelle, correctement attribuée, mais dont la solution a été renversée par une décision postérieure. C'est différent de B2 (mauvaise attribution) : ici le contenu retourné soutient bien l'assertion — au moment où la décision a été rendue. Le risque est temporel, pas d'attribution.

*Contrôle* : pour toute décision judiciaire fondant un moyen, vérifier son statut de validité via le graphe de citations (Legal Data Hunter — `decisions impactées`, `statut superseded`) avant de la citer. Une décision "superseded" n'est plus le droit, même si elle continue de décrire fidèlement ce qu'un juge a dit un jour donné.

## C. Checklist de validation avant citation

À passer sur chaque référence fondant une majeure du raisonnement :

- [ ] Le texte a été obtenu par un outil, pas restitué de mémoire
- [ ] Il ne se termine pas par `...` et les alinéas attendus sont présents
- [ ] La section parente correspond à la matière recherchée
- [ ] Le numéro et la date de version sont cohérents avec la réforme attendue
- [ ] Les renvois internes cités ont été vérifiés
- [ ] Le lien officiel est recopié depuis la réponse de l'outil, non reconstruit
- [ ] Le passage cité **soutient effectivement** l'assertion (content-matching)
- [ ] La citation est exacte, sans paraphrase déplaçant la portée
- [ ] Pour une décision judiciaire (rétention, JLD) : statut de validité vérifié — pas de mention "superseded" ou de décision impactée postérieure qui la contredit
- [ ] Pour tout point touché par une réforme 2024-2026 : vérification sur Légifrance
- [ ] Pour une décision : triplet complet juridiction + date + numéro, et contrôle qu'elle n'a pas été renversée

Priorisation quand les références sont nombreuses : contrôle complet pour toute référence portant une étape du raisonnement ou répétée ; contrôle allégé pour les références illustratives ; contrôle d'existence seul pour la bibliographie.

## D. Tableau de contrôle à produire

Avant remise, produire ce tableau — visible ou non selon le livrable, mais toujours établi :

| Référence citée | Outil et identifiant | Extrait retourné | Soutient l'assertion ? |
|---|---|---|---|
| | | | ✓ / ✗ / reformulé |

Règle binaire : **tant qu'une ligne porte un ✗, la livraison est bloquée.** Une ligne « reformulé » impose de revenir à la citation exacte ou de retirer la référence.

## E. Formulations de repli

Quand la vérification échoue, ces formulations sont des réponses professionnelles, pas des aveux d'échec :

- « Il résulte des principes gouvernant le droit au séjour que… » — sans numéro d'article.
- « La jurisprudence administrative retient de façon constante que… » — sans référence chiffrée.
- « Ce point est régi par un accord bilatéral dont la stipulation exacte doit être vérifiée dans la version consolidée. »
- « La recherche n'a pas permis de confirmer ce point ; il doit être vérifié sur Légifrance avant tout usage. »

Le principe : **zéro référence vaut mieux qu'une référence inventée.** Un praticien qui lit « à vérifier » va vérifier. Un praticien qui lit un numéro d'article faux fonde un recours dessus.

## Journal des cas vérifiés en conditions réelles

Cinq erreurs de rédaction ont été détectées et corrigées par confrontation aux connecteurs, avant toute mise en production du skill. Elles sont conservées ici comme illustration concrète des mécanismes A1-A6 et B1-B3 — la théorie seule ne convainc pas, ces cas montrent qu'elle s'applique à ce skill lui-même :

1. **Délai OQTF** — le premier jet raisonnait sur « délai de départ volontaire oui/non » (4 régimes : 48h/7j/15j/30j). Le critère réel, vérifié sur L.911-1/R.911-1/L.921-1/L.921-2, est la **situation de contrainte** (aucune / assignation-détention / rétention), avec un renvoi réglementaire depuis le décret n° 2026-455.
2. **Numérotation morte** — L.313-11 interrogé volontairement a retourné un texte long et plausible marqué `ABROGE` / `date_fin: 2021-05-01`, sans que cela saute aux yeux dans une réponse formatée. Mécanisme A5.
3. **Accords bilatéraux, erreur par excès** — le premier jet affirmait qu'aucune régularisation n'était possible hors CESEDA pour un Algérien. La lecture intégrale d'un arrêt de CAA (mécanisme B2, content-matching) a révélé que le préfet garde un pouvoir discrétionnaire de régularisation fondé sur l'accord bilatéral lui-même.
4. **Pacte européen, fait présumé** — le premier jet supposait la loi d'habilitation « en cours d'adoption ». Vérifiée sur le dossier Sénat, elle a en réalité été **rejetée en commission** à l'Assemblée nationale ; une ordonnance identifiée dans un corpus (n° 2026-671) a été prise à tort pour un texte de transposition alors qu'elle est fiscale et sans rapport. Mécanisme A6 étendu : un texte du CESEDA en vigueur peut citer une directive européenne déjà abrogée, sans que ce soit une erreur de l'outil.
5. **Délai de visa** — le premier jet indiquait un RAPO de 2 mois. La lecture de D.312-4 donne **30 jours** pour le RAPO ; le délai de 2 mois s'applique seulement à l'étape contentieuse suivante (R.312-6 renvoyant au CJA). Découverte annexe : le court séjour est jugé en premier et dernier ressort (R.811-1 CJA), sans appel — absente du premier jet.
6. **Angle mort structurel — le judiciaire de la rétention** — les versions précédentes de ce skill ne couvraient le contentieux de la rétention (JLD, appel) qu'en passant, sans outil dédié. L'essai d'une recherche filtrée par domaine/chambre a montré que ce contentieux se juge dans des chambres spécialisées ("chambre étrangers", "rétention_recoursJLD") mal atteintes par une recherche généraliste — et a révélé un mécanisme d'erreur non couvert jusque-là : une décision peut être correctement attribuée et pourtant avoir été renversée depuis (mécanisme B4). Corrigé en ajoutant le contrôle de statut de validité au tableau de vérification.

Aucune de ces cinq erreurs n'était extravagante : chacune était plausible, cohérente avec le reste du texte, et aurait pu passer sans la vérification systématique imposée par ce fichier.

## F. Ce qui ne relève pas de cette couche

La vérification porte sur les références, pas sur le raisonnement. Un document dont toutes les références sont exactes peut rester juridiquement faux — mauvaise qualification, régime inapplicable, moyen inopérant. La couche anti-hallucination est une condition de fiabilité, pas une garantie de justesse : les cinq pièges du §4 du SKILL.md traitent l'autre moitié du problème.
