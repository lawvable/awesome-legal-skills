---
name: "skill-pour-interroger-judilibre-allison-fiorentino"
description: >-
  >Ce skill donne accès à l'API de judilibre. Vous formulez votre demande en français, il interroge la base Judlibre et renvoie les réponses.
  
  Attention le skill ne fonctionne que si des domaines supplémentaires sont utilisés et que l'utilisateur a rentré sa propre clé Judlibre.
  
  Ce skill et son auteur n'ont aucun lien avec la Cour de cassation ou Judilibre
metadata:
  author: "Allison Fiorentino"
  license: "agpl-3.0"
  version: "2026-06-25"
---

# Judilibre — jurisprudence judiciaire

Ce skill interroge l'API Judilibre (Cour de cassation) pour rechercher et lire
des décisions de justice de l'ordre judiciaire. Le travail se fait via le script
`scripts/judilibre_client.py`, qui gère l'authentification et renvoie du JSON.

## Périmètre — à dire à l'utilisateur si besoin

- ✅ Couvre : Cour de cassation (toutes chambres), et de plus en plus les cours
  d'appel et juridictions du premier degré (montée en charge progressive).
- ❌ Ne couvre PAS : les textes (codes, lois, décrets) ni la jurisprudence
  administrative (Conseil d'État, CAA, TA). Pour cela, renvoyer vers OpenLegi /
  Légifrance ou une autre source.

## Configuration (une seule fois)

Le script a besoin d'une clé PISTE et d'un accès réseau autorisé.

1. **Clé d'API (mode KeyId — recommandé).** Une simple clé d'API suffit : c'est
   le mode KeyId, où la clé est envoyée dans l'en-tête HTTP. Le script lit la clé
   dans cet ordre : argument `--key`, variable d'environnement
   `JUDILIBRE_KEY_ID`, puis `scripts/config.json`. Si aucune clé n'est trouvée,
   le script renvoie une erreur explicite. Dans ce cas, demander sa clé à
   l'utilisateur, puis créer `scripts/config.json` à partir de
   `scripts/config.example.json` en collant la clé dans le champ `key_id` et en
   réglant `env` sur `prod` (ou `sandbox`). Le client OAuth (`client_id` /
   `client_secret`) n'est PAS nécessaire en mode KeyId : laisser ces champs vides.

   *Mode OAuth2 (avancé, repli).* Si l'utilisateur n'a pas de KeyId mais un couple
   `client_id` / `client_secret`, renseigner ces deux champs et laisser `key_id`
   vide ; le script obtiendra et mettra en cache un jeton Bearer automatiquement.

   ⚠️ `scripts/config.json` contient la clé en clair : ne jamais l'afficher ni le
   partager.

2. **Réseau.** L'appel sort vers `*.piste.gouv.fr`. Si le script renvoie une
   erreur « Connexion impossible à piste.gouv.fr » ou « Domaine réseau non
   autorisé », prévenir l'utilisateur qu'il doit autoriser le domaine dans les
   réglages réseau de l'exécution de code de Claude :
   - `api.piste.gouv.fr` — **indispensable** (production, mode KeyId) ;
   - `sandbox-api.piste.gouv.fr` — seulement pour le bac à sable ;
   - `oauth.piste.gouv.fr` et `sandbox-oauth.piste.gouv.fr` — seulement pour le
     mode OAuth2.

Vérifier que tout fonctionne : `python3 scripts/judilibre_client.py test`.
Cette commande effectue une vraie recherche authentifiée (et non un simple
healthcheck), donc un succès confirme bien que la clé est acceptée.

## Utilisation

Installer la dépendance si nécessaire : `pip install requests` (silencieux si
déjà présent).

### Rechercher

```bash
python3 scripts/judilibre_client.py search "période d'essai rupture abusive" \
  --chamber soc --page-size 10
```

Filtres disponibles (tous facultatifs). Plusieurs valeurs sont acceptées pour
les filtres de catégorie (les séparer par un espace) :
`--chamber` (soc, civ1, civ2, civ3, comm, crim…), `--jurisdiction` (cc, ca, tj),
`--type`, `--theme`, `--publication`, `--solution`, `--field`,
`--operator` (and|or|exact), `--date-start AAAA-MM-JJ`, `--date-end AAAA-MM-JJ`,
`--page`, `--page-size` (max 50), `--sort` (score|date), `--order` (asc|desc).

Exemple multi-valeurs : `--chamber soc comm` cherche dans les deux chambres.

La sortie est du JSON. Champs utiles par résultat : `id`, `number`/`numbers`,
`jurisdiction`, `chamber`, `formation`, `decision_date`, `solution`, `ecli`,
`publication`, `summary`, `themes`, `score`, et `url` (lien public direct vers
la décision sur courdecassation.fr, ajouté par le script).

### Lire une décision complète

Reprendre l'`id` d'un résultat de recherche :

```bash
python3 scripts/judilibre_client.py decision <id>
```

Renvoie le texte intégral (`text`), un lien public (`url`) et le zonage
(`zones` : introduction, exposé, moyens, motivations, dispositif, annexes).

### Connaître les valeurs d'un filtre

```bash
python3 scripts/judilibre_client.py taxonomy chamber
```

## Présentation des résultats à l'utilisateur — TOUJOURS

Après une recherche, ne pas recracher le JSON brut. Présenter une liste claire,
classée par pertinence, où chaque décision indique : juridiction et chambre,
**numéro de pourvoi**, date, solution (cassation, rejet…), niveau de publication
(P, B…), un résumé court si disponible, et le **lien public** (`url`) vers le
texte. Conserver l'`id` pour pouvoir ouvrir le texte intégral à la demande.
Proposer d'afficher l'arrêt complet ou d'affiner la recherche (chambre, période).

Toujours rappeler que ce sont des décisions de l'ordre judiciaire uniquement.

## En cas d'erreur

Le script renvoie des messages JSON explicites (`error` + `fix`). Les relayer
simplement à l'utilisateur :
- clé manquante → demander la clé et l'enregistrer dans `scripts/config.json` ;
- 401 → mauvaise clé ou mauvais environnement (sandbox vs prod) ;
- 403 → CGU Judilibre non validées ou API non rattachée à l'application PISTE ;
- 429 / 5xx → quota atteint ou API indisponible ; le script réessaie
  automatiquement, sinon attendre un peu et relancer ;
- connexion impossible / domaine non autorisé → autoriser `api.piste.gouv.fr`
  dans les réglages réseau.
