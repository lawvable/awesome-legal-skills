# Marques d'écriture « IA » en français — détection et traitement

Ce fichier guide la **passe de jugement**. Il ne s'agit pas d'éradiquer des structures par principe, mais de supprimer le **délayage** et les **tics** caractéristiques d'un texte généré, sans appauvrir une prose juridique légitime. Le critère décisif est presque toujours la **vacuité sémantique** : si l'on retire le segment et que l'argument ne perd rien, c'est du remplissage.

## Table

1. Apostrophes et guillemets droits (déterministe)
2. Tirets cadratins : conservation et espacement
3. Virgule avant « et » (contextuelle — jamais mécanique)
4. Rythmes ternaires creux
5. Formules emphatiques vides
6. Adjectifs et superlatifs d'enflure
7. Connecteurs surabondants
8. Tics métatextuels
9. Antithèses et parallélismes de remplissage

---

## 1. Apostrophes et guillemets droits — *déterministe (script)*

L'apostrophe droite `'` et les guillemets droits `"…"` sont un signe d'origine machine. Le script les convertit en apostrophe courbe `’` et en guillemets français `« … »`. Voir `typographie.md`. Aucune action de jugement requise.

## 2. Tirets cadratins — *conservés*

Le tiret cadratin `—` est **conservé** (choix de l'utilisateur). Le marqueur d'IA n'est pas le cadratin lui-même mais (a) sa **densité** et (b) son **espacement** à l'anglaise (`mot—mot`). Le script normalise l'espacement (`mot — mot`, espace insécable avant le tiret). N'intervenir au jugement que si la **densité** est manifestement excessive (plusieurs incises par phrase) : dans ce cas, convertir certaines incises en parenthèses ou en propositions, sans tout uniformiser. Ne jamais remplacer le cadratin par un autre signe.

## 3. Virgule avant « et » — *contextuelle, jamais mécanique*

Règle de défaut en français : **pas de virgule** devant *et* coordonnant deux termes ou deux propositions de même sujet.

> Le contrat est formé, et les parties sont engagées. → Le contrat est formé et les parties sont engagées.

**Cas où la virgule est légitime et doit être conservée :**
- Propositions à **sujets différents** : « Le débiteur s'exécutera, et le créancier donnera quittance. »
- **Fermeture d'une incise** juste avant *et* : « Le juge, après débats, et sans renvoi, statue. »
- Tournure **« …, et ce, … »** : « Il doit réparer, et ce, intégralement. »
- **Polysyndète** d'insistance (*et… et… et*).
- *Et* introduisant une proposition de sens **distinct ou conclusif** : « Les délais ont couru, et l'action est prescrite. »

Ne retirer que la virgule **fautive** entre deux éléments simplement coordonnés. En cas de doute, conserver.

## 4. Rythmes ternaires creux

Le tricolon est un procédé classique et souvent excellent. Ne resserrer que le ternaire **formulaire et vide**, reconnaissable à des membres redondants ou interchangeables.

- ❌ creux : « une analyse rigoureuse, précise et minutieuse » (les trois adjectifs disent la même chose) → « une analyse rigoureuse ».
- ❌ creux : « comprendre, analyser et appréhender la question » → « analyser la question ».
- ✅ substantiel : « la formation, l'exécution et l'extinction du contrat » (trois phases distinctes) → **conserver**.

Indice : suffixe « …, et ce de manière X » ou triade d'adverbes en *-ment*. Supprimer le délayage, garder l'information.

## 5. Formules emphatiques vides

Locutions d'amorce qui n'ajoutent rien et signalent la génération automatique. À **supprimer** ou à fondre dans la phrase :

- « Il convient de souligner / noter / rappeler / préciser que… » → supprimer l'amorce, énoncer directement le fait.
- « Il importe de relever que… », « Notons que… », « On notera que… », « Il est à noter que… ».
- « Force est de constater que… » (toléré une fois ; proscrire la répétition).
- « Il ne fait aucun doute que… », « Il va sans dire que… ».
- « joue un rôle clé / central / déterminant », « constitue un enjeu majeur », « est au cœur de », « pierre angulaire », « s'inscrit dans une logique de », « à l'ère de », « dans un monde où ».
- « véritable » en intensif (« une véritable révolution juridique ») → supprimer l'adjectif.

Principe : remplacer l'annonce de l'idée par l'idée.

## 6. Adjectifs et superlatifs d'enflure

*essentiel, crucial, primordial, fondamental, incontournable, majeur, considérable, indéniable, remarquable* employés sans mesure. Les conserver lorsqu'ils sont **justifiés et mesurés**, les retirer lorsqu'ils ne font que gonfler le propos. Préférer la démonstration à l'épithète.

## 7. Connecteurs surabondants

*en effet, ainsi, par ailleurs, en outre, notamment, dès lors, partant, de surcroît* : excellents isolément, suspects par accumulation (un connecteur en tête de presque chaque phrase). Alléger : supprimer les connecteurs qui ne marquent pas une vraie articulation logique. Attention : en droit, *dès lors*, *partant*, *en l'espèce* sont légitimes ; ne pas les bannir.

## 8. Tics métatextuels

Phrases qui commentent le texte au lieu de l'écrire : « Cette partie a pour objet de… », « Nous allons à présent examiner… », « Comme nous l'avons vu précédemment… », « En guise de conclusion… ». Les supprimer au profit de l'énoncé direct, sauf valeur d'annonce réellement utile dans un plan.

## 9. Antithèses et parallélismes de remplissage

« non pas X, mais bien Y », « tant sur le plan A que sur le plan B », « qu'il s'agisse de… ou de… », « d'une part… d'autre part… » employés sans contenu différenciant. Conserver lorsque l'opposition est réelle ; supprimer lorsqu'elle est décorative.

---

**Rappel de prudence** : chaque réécriture de jugement est posée en révision Word et consignée au registre. En cas d'hésitation sur le sens, **ne pas réécrire** : signaler par un commentaire `docx` plutôt qu'altérer.

## 10. Périphrases verbo-nominales — *jugement*

Marqueur d'un style administratif lourd, fréquent dans les textes générés : verbe support + nominalisation au lieu du verbe simple. Resserrer quand le sens n'y perd rien :
- « procéder à la vérification de » → « vérifier »
- « opérer un choix » → « choisir »
- « effectuer une analyse » → « analyser »
- « apporter une réponse à » → « répondre à »
- « avoir pour conséquence de » → « entraîner »

Conserver la périphrase lorsqu'elle est un **terme de l'art** porteur d'une nuance juridique : *mettre en demeure*, *porter à la connaissance*, *faire grief*, *mettre en œuvre* (un mécanisme), qui ne sont pas des périphrases creuses.
