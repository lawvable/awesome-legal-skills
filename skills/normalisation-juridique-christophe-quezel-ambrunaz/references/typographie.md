# Typographie et ponctuation — schéma de normalisation

Règles **déterministes** appliquées par le script aux nœuds de texte. Le principe de prudence est de **normaliser une espace existante** plutôt que d'**insérer** une espace manquante (pour ne pas casser une URL, une heure, un fragment de code).

## 1. Espaces insécables

Schéma retenu (typographie française fine) :

| Contexte | Caractère inséré |
|---|---|
| avant `;` `?` `!` | espace **fine** insécable `U+202F` |
| avant `:` | espace insécable `U+00A0` |
| après `«` et avant `»` | espace fine insécable `U+202F` |
| avant le tiret d'incise `—` | espace insécable `U+00A0` |

Mise en œuvre **conservatrice** : le script **remplace une espace ordinaire déjà présente** devant le signe par l'insécable correspondante ; il **n'insère pas** d'espace là où il n'y en a pas (évite `http://`, `12:30`, `n°` collés, etc.). L'insertion d'une espace manquante relève du jugement.

> Variante admise : certaines maisons emploient l'espace insécable `U+00A0` partout. Le script est paramétrable ; conserver la cohérence interne du document.

## 2. Apostrophe courbe

Remplacer l'apostrophe droite `'` (`U+0027`) par l'apostrophe courbe `’` (`U+2019`) lorsqu'elle est **précédée d'une lettre** (élisions `l’`, `d’`, `qu’`, `n’`, `j’`, `s’`, `c’`, `t’`, et mots comme `aujourd’hui`). Idempotent : ne pas retoucher une apostrophe déjà courbe.

## 3. Guillemets français

Convertir les paires de guillemets droits `"…"` en guillemets français `« … »` avec espace fine insécable à l'intérieur. Ne convertir que les paires **équilibrées** dans le paragraphe ; en cas de déséquilibre, s'abstenir et signaler. Les guillemets anglais internes (citation dans citation) deviennent `“ ”`.

## 4. Tirets

- **Tiret cadratin** `—` : **conservé** (incises, dialogues). Le script garantit l'espacement : espace insécable avant, espace ordinaire après (`mot — mot`), et supprime l'usage collé à l'anglaise (`mot—mot`).
- **Tiret demi-cadratin** `–` : laissé tel quel s'il sépare des bornes numériques (`p. 30–35`).
- **Trait d'union** `-` : non touché.

## 5. Espaces multiples et fins de ligne

Réduire toute suite d'espaces ordinaires à une seule. Supprimer les espaces en fin de paragraphe. Ne pas toucher aux tabulations de mise en forme.

## 6. Majuscules accentuées — *jugement*

En français, les majuscules **s'accentuent** : `État`, `Île`, `Œuvre`, `À`, `É`, `È`, `Ç`. Le script corrige un petit ensemble sûr (`Etat→État`, `Etats→États`). Les autres cas (notamment `A`→`À` en tête de phrase, ambigu) relèvent du jugement, car ils supposent de distinguer l'initiale d'un sigle (`ETAT` en capitales d'un acronyme) d'un mot.

## 7. Ordinaux, civilités, ligatures, références — *déterministe (v1.1)*

- **Ordinaux** : `1ère`/`1ere` → `1re` ; `2ème`/`2eme`/`2è` → `2e` ; `Xième` chiffré → `Xe`. Les formes `1er`, `2nd`/`2nde` sont conservées ; les mots en « ème » (système, deuxième) ne sont pas touchés (la règle exige un chiffre).
- **Civilité** : `Mr`/`Mr.` → `M.` (`Mr` est un anglicisme pour Monsieur).
- **Ligatures œ** : `oeu` → `œu` (cœur, œuvre, manœuvre, vœu, nœud, bœuf, sœur, mœurs) ; liste fermée pour `oe` → `œ` (œil, œdème, œsophage, œcuménique, fœtus, œstrogène, Œdipe). Les hiatus (coexister, coefficient, moelle) sont exclus.
- **Insécables des références** : l'espace devient insécable entre une abréviation et ce qui suit — `art.`, `al.`, `p.`, `pp.`, `vol.`, `t.`, `ch.`, `fasc.`, `col.`, `§`, `L./R./D.` (articles de code), `n°` + nombre ; civilités `M./Mme/Mlle/Me/Mgr/Dr/Pr` + nom propre ; **fine insécable** devant `%` et `€`.
- **Points de suspension** : `...` → `…`.
- **Espace parasite** : suppression d'une espace placée à tort devant `,` ou `.`.
