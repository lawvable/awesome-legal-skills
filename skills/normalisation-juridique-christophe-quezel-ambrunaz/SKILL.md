---
name: "normalisation-juridique-fr-christophe-quezel-ambrunaz"
description: >-
  
  La compétence Normalisation juridique FR nettoie un document Word rédigé en français juridique. Elle distingue deux régimes : les corrections déterministes (apostrophes courbes, guillemets français, espaces insécables, insécables des références — art. 1240, n° 21-12.345, 50 % —, ordinaux 1ère → 1re, ligatures œ, la loi dispose et non stipule, anglicismes-calques), appliquées directement ; et les réécritures de jugement (virgule avant « et », ternaires creux, formules emphatiques, harmonisations), posées en révisions Word soumises à votre acceptation. Chaque changement est consigné et restitué en tableau récapitulatif : on revient en arrière mot à mot — « défais 3, 7-10 ». La normalisation des citations reste purement formelle. Fonctionne en Cowork ou sur fichier Word.
metadata:
  author: "Christophe Quézel-Ambrunaz"
  license: "agpl-3.0"
  version: "2026-06-18"
---

# Normalisation du langage juridique français — v1.0

Compétence conçue avec Christophe Quézel-Ambrunaz. Elle **corrige directement** un document Word juridique, de façon autonome, puis rend dans la conversation un **tableau récapitulatif compact** et **réversible**.

## Principe directeur

Deux régimes de modification, qu'il ne faut jamais confondre :

1. **Normalisations déterministes** — typographie, insécables, apostrophes, guillemets, impropriétés à correction univoque (*stipuler→disposer*), anglicismes non ambigus, forme des références. Sûres, appliquées d'office par `scripts/normaliser.py`.
2. **Réécritures de jugement** — virgule avant *et* (contextuelle), ternaire creux, emphase vide, anglicisme contextuel, tolérances de citation. Elles exigent une lecture intelligente : c'est **toi** qui les décides et les poses, guidé par les fichiers de `references/`.

Les normalisations **déterministes** sont appliquées **directement, sans suivi des modifications** — pour ne pas alourdir la relecture ; leur réversibilité est entièrement assurée par le **registre** (`défais`). Seules les **réécritures de jugement** sont posées en **révisions Word** (`w:ins`/`w:del`) : ce sont les seules à examiner, l'utilisateur les accepte ou les rejette dans Word, et le registre permet aussi de les défaire. Le suivi peut être étendu au lexique déterministe via l'option `--track-lexical` (désactivée par défaut).

**Garde-fou cardinal sur les citations** : la normalisation des références est **purement formelle** (abréviations, ordre, espaces). Ne jamais modifier le fond d'une référence (juridiction, date, numéro), ne jamais en inventer. En cas de doute sur l'exactitude, signaler, ne pas « corriger ».

## Environnement et délégation

- Requiert **Cowork** ou **computer use** : la pose de révisions suppose l'édition XML du `.docx`. En chat simple sans fichier, demander le document et l'environnement adéquat.
- La **mécanique OOXML est déléguée à la compétence `docx`** (toujours disponible) : `scripts/office/unpack.py` → édition de `word/document.xml` (et `footnotes.xml`/`endnotes.xml`) → `scripts/office/pack.py` → validation ; `scripts/comment.py` pour les commentaires ; `scripts/accept_changes.py` pour produire la version propre. Consulter la SKILL.md de `docx` pour les patrons exacts de `w:ins`/`w:del`. Auteur des révisions : « Claude — normalisation » (sauf consigne contraire).

## Workflow

### 1. Cadrage (une seule interruption, brève)

Identifier le fichier `.docx` cible et le **périmètre** : corps seul, ou corps + notes de bas de page + bibliographie (par défaut : **tout**, l'utilisateur l'a validé). Si le fichier est un `.doc`, le convertir d'abord (`docx/scripts/office/soffice.py`).

### 2. Lecture intégrale

Extraire le texte (`extract-text` de `docx`) et **le lire en entier** avant toute modification. La lecture sert au régime de **jugement** ; le déterministe, lui, est traité par script sans relecture humaine.

### 3. Passe déterministe (script)

```bash
python scripts/normaliser.py apply \
  --in "<document.docx>" \
  --out "<document — normalisé.docx>" \
  --registry "<.normjur/registre.json>" \
  --scope all          # all | body | body+notes
```

Le script applique les règles déterministes (typographie et lexique sûr) **directement, sans suivi des modifications**, écrit le `.docx` corrigé et le **registre JSON**. Option `--track-lexical` pour poser le lexique en révisions. Détail des règles : `references/typographie.md`, `references/lexique-juridique.md`, `references/anglicismes.md` (section « noyau sûr »).

### 4. Passe de jugement (toi, sur le document déjà corrigé)

En t'appuyant sur `references/marqueurs-ia.md`, `references/anglicismes.md` (section « contextuel ») et `references/citations-reflex.md`, pose en **révisions Word** les réécritures de jugement, via le patron `docx`. Pour **chaque** réécriture, enregistre une entrée de jugement dans le registre :

```bash
python scripts/registre.py add-jugement \
  --registry "<.normjur/registre.json>" \
  --cle emphase --libelle "Emphase creuse réécrite" --categorie stylistique \
  --avant "<texte d'origine>" --apres "<texte réécrit>" --wids "101,102"
```

Règles d'or du jugement :
- **Virgule avant *et*** : ne jamais supprimer mécaniquement. Conserver dans les cas légitimes (propositions à sujets différents, fermeture d'incise, « …, et ce, … », polysyndète). Ne retirer que la virgule fautive entre deux termes coordonnés simples.
- **Ternaire** : ne resserrer que le tricolon **creux et formulaire**, jamais l'énumération substantielle.
- **Tirets cadratins** : on les **conserve**. Le script normalise seulement leur espacement (` — `). Ne pas les remplacer.
- **Périphrases verbo-nominales** et **harmonisation orthographique (1990)** : voir `references/marqueurs-ia.md` (§10) et `references/orthographe-harmonisation.md`.

### 5. Récapitulatif

```bash
python scripts/registre.py recap --registry "<.normjur/registre.json>"
```

Coller le tableau (compact, **agrégé par règle**) dans la conversation, suivi de la phrase d'invite à l'annulation (voir ci-dessous).

### 6. Vérification finale (obligatoire)

- Valider l'intégrité : `python scripts/registre.py verify --registry … --doc "<corrigé.docx>"` (idempotence, comptes, validité OOXML via `docx/scripts/office/validate.py`).
- Contrôler qu'**aucune réécriture stylistique n'a altéré le sens** et qu'**aucune référence n'a été corrompue**. Pour un document long ou sensible, déléguer ce contrôle à un sous-agent de relecture du diff.

## Le registre

Fichier `JSON` écrit hors conversation (dans `.normjur/` à côté du document) ; la conversation n'affiche que le tableau agrégé. Schéma : voir `references/registre-schema.md`. Chaque modification est rattachée à un **groupe de règle** numéroté `n` et porte un indice intra-groupe `i`. Les groupes déterministes sont numérotés en premier (ordre fixe), les groupes de jugement à la suite, dans l'ordre où tu les ajoutes.

## Tableau récapitulatif (format imposé)

```
| N° | Règle                                | Type        | Occ. | Exemple (avant → après)        |
|----|--------------------------------------|-------------|------|--------------------------------|
| 1  | Apostrophes courbes                  | détermin.   |  42  | l'article → l’article          |
| 2  | Insécables (; : ! ? « »)             | détermin.   |  37  | art. 9 ; → art. 9 ;            |
| 5  | stipuler → disposer (loi/texte)      | détermin.   |   3  | la loi stipule → la loi dispose|
| 7  | Emphase creuse resserrée             | STYLISTIQUE |   5  | « il importe de souligner… » → …|
```

Mettre les lignes **STYLISTIQUE** en évidence (l'utilisateur doit pouvoir vérifier d'abord le registre subjectif). Terminer par :

> Pour revenir sur des changements, répondez par ex. : **défais 3, 7-10, 12** (groupe entier) ou **défais 7.2** (une occurrence). **refais** pour rétablir.

## Grammaire d'annulation

L'utilisateur répond en langage naturel ; interpréter et exécuter :

```bash
python scripts/registre.py undo "3, 7-10, 12" \
  --registry "<.normjur/registre.json>" \
  --in "<document.docx — ORIGINAL>" \
  --out "<document — normalisé.docx>"
```

- `défais 3` → désactive tout le groupe 3 ; `défais 7-10` → groupes 7 à 10 ; `défais 7.2` → la 2ᵉ occurrence du groupe 7.
- Mécanique : pour les groupes **déterministes**, le script **reconstruit** le document depuis l'original en réappliquant les seules règles/occurrences restées actives — réversibilité propre, sans dérive. Pour les groupes de **jugement**, le script **rejette** les révisions correspondantes (`w:id` enregistrés).
- `refais 7` réactive le groupe ; `défais tout` / `refais tout` pour la bascule globale.

Après chaque `undo`/`redo`, réafficher le tableau `recap` mis à jour (compact).

## Économie de contexte

Ne jamais déverser le contenu du registre dans la conversation : seul le tableau agrégé y figure. Les exemples « avant → après » sont **tronqués** (≈ 40 caractères). Pour un document volumineux, traiter par sections lors de la passe de jugement, mais n'écrire dans la conversation que le récapitulatif consolidé.

## Fichiers de référence

- `references/marqueurs-ia.md` — marques d'écriture IA en français et leur traitement (apostrophes, virgule avant *et*, ternaires, emphase, tirets, formules creuses).
- `references/anglicismes.md` — noyau sûr (script) / contextuel (jugement) / **liste blanche** des termes de la matière conservés.
- `references/lexique-juridique.md` — impropriétés juridiques (*stipuler/disposer*, *juridiction/justice*, *arrêt/jugement*…).
- `references/typographie.md` — apostrophes, insécables (schéma retenu), guillemets, tirets, majuscules accentuées.
- `references/citations-reflex.md` — norme RefLex SNE 2022, tolérances, harmonisation par usage majoritaire.
- `references/orthographe-harmonisation.md` — harmonisation des graphies 1990 selon l'usage majoritaire (jugement).
- `references/registre-schema.md` — schéma JSON du registre.

## Limites connues (v1.0, à dire honnêtement à l'utilisateur si pertinent)

- L'insertion de révisions par script vise le cas d'une occurrence **dans un seul *run***. Les occurrences à cheval sur plusieurs *runs* sont consignées comme « à poser manuellement » : les traiter via le patron `docx`.
- Les majuscules accentuées et la grammaire ambiguë relèvent du **jugement**, pas du script.
- Le rejet de révisions de jugement par `w:id` est au mieux fiable tant que l'utilisateur n'a pas déjà accepté/rejeté ces révisions dans Word ; dans ce cas, basculer sur un remplacement `après → avant` lu dans le registre.
