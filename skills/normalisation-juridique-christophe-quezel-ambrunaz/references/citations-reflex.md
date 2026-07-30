# Harmonisation des références — norme RefLex et usage majoritaire

Référence normative : **Guide de rédaction SNE RefLex 2022**. La normalisation des citations est **purement formelle** : abréviations, ordre des éléments, espaces. Ne jamais altérer le fond (juridiction, date, numéro) ni inventer une référence. Cette tâche recoupe les tâches 9-10 de `assistant-juridique-fr` ; en réutiliser la logique.

## Principe : norme + cohérence interne

Là où RefLex laisse une **tolérance**, on adopte la forme **majoritaire dans le document** plutôt qu'une norme imposée. Détecter les variantes, retenir la dominante, harmoniser le reste.

| Élément | Variantes tolérées | Règle |
|---|---|---|
| Initiale du prénom d'auteur | `BRUN Ph.` / `Brun (Ph.)` / `Ph. Brun` | usage majoritaire du document |
| Chambre de la Cour de cassation | `Cass. civ. 2e` / `Cass. 2e civ.` / `Civ. 2e` | usage majoritaire |
| Date | `12 juill. 2023` / `12 juillet 2023` | usage majoritaire (abrégé recommandé) |
| Titre de revue | `RTD civ.` / nom complet | usage majoritaire |
| Guillemets de titre | `« … »` / `"…"` | aligner sur la typographie du document (`« »`) |
| Renvoi | `V.` / `v.` / `Cf.` | usage majoritaire |
| Pagination | `p.` / `pp.` | `p.` (RefLex) |

## Erreurs de forme à corriger (non tolérées)

- Ordinal : `1re`, `2e`, `3e` (pas `1ère`, `2ème`, `2nd` mal placé).
- Mois abrégés : `janv., févr., mars, avr., mai, juin, juill., août, sept., oct., nov., déc.`
- Numéro de pourvoi : `n° 21-12.345` (avec le point intérieur).
- Espaces insécables dans `n° 21-12.345`, `art. 1240`, `p. 45`.

## Formes de référence (rappel RefLex)

- **Cassation** : `Cass. [chambre], [JJ mois abrégé AAAA], n° [XX-XX.XXX]` — chambres : `civ. 1re/2e/3e, com., soc., crim.` ; solennelles : `Ass. plén., Ch. mixte`.
- **Conseil d'État** : `CE, [formation], [date], n° [XXXXXX]`.
- **Conseil constitutionnel** : `Cons. const., [date], n° [AAAA-NNN] [DC/QPC]`.
- **Cour d'appel** : `CA [ville], [chambre], [date], n° RG [XX/XXXXX]`.
- **Article de code** : `Art. [L./R./D.] [numéro] [code abrégé]` — `C. civ., C. pén., C. com., C. trav., CPC, CPP, CJA, CSP, CSS`.
- **Loi** : `Loi n° [AAAA-NNN] du [JJ mois AAAA] [titre court]`.
- **Doctrine (article)** : `NOM Initiale., « Titre », Revue abrégée AAAA, p. X`.

## Procédure

1. Inventorier les références (corps, notes, bibliographie).
2. Regrouper par catégorie, relever les variantes et leurs effectifs.
3. Retenir la forme dominante pour chaque tolérance ; appliquer la norme RefLex pour les erreurs non tolérées.
4. Poser les corrections en **révisions Word** ; consigner chaque correction au registre (groupe « Harmonisation des références »).
5. **Ne pas** modifier un numéro, une date ou une juridiction : si une incohérence de fond apparaît, la **signaler par commentaire** (`docx/scripts/comment.py`), sans la corriger d'autorité.
