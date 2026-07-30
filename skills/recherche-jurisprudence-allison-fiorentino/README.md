# Skill Judilibre pour Claude

_Rechercher la jurisprudence judiciaire française (Cour de cassation) directement depuis Claude_

Ce guide explique en trois étapes comment mettre en service le skill Judilibre : récupérer votre identifiant PISTE, autoriser les domaines réseau nécessaires, puis installer le skill dans Claude. Comptez une dizaine de minutes la première fois.

> **À retenir avant de commencer**
>
> - L'accès à Judilibre passe par le portail PISTE : il faut un compte gratuit et une clé d'API (KeyId).
> - Le skill couvre uniquement l'ordre judiciaire (Cour de cassation, et de plus en plus cours d'appel et premier degré).
> - Votre clé est strictement personnelle : ne la partagez jamais et ne la publiez nulle part.

---

## 1. Récupérer son identifiant PISTE

PISTE (Plateforme d'Intermédiation des Services pour la Transformation de l'État) héberge l'API Judilibre de la Cour de cassation. L'inscription et l'usage sont gratuits.

1. Créer un compte sur **piste.gouv.fr/registration**. Renseignez vos nom et adresse e-mail.
2. Activer le compte via le lien reçu par e-mail, puis **se connecter** au portail.
3. Valider les conditions générales d'utilisation (CGU) de Judilibre : dans votre espace, recherchez « Judilibre » et acceptez les CGU pour l'environnement **production** (et/ou bac à sable si vous testez).
4. Créer **une application** depuis votre tableau de bord PISTE (une application = un conteneur auquel sont rattachées vos clés).
5. Rattacher l'API Judilibre à cette application, puis **générer une clé d'API (API Key / KeyId)**.
6. Copier la valeur du **KeyId** : c'est l'unique information dont le skill a besoin pour fonctionner.

> **Astuce**
>
> Le « mode KeyId » suffit dans l'immense majorité des cas : une simple clé envoyée dans l'en-tête de la requête. Le couple client_id / client_secret (OAuth2) n'est utile que pour des usages avancés.

---

## 2. Autoriser les domaines extérieurs

Le skill s'exécute dans l'environnement d'exécution de code de Claude, dont l'accès réseau est restreint par défaut. Il faut donc autoriser le domaine vers lequel partent les requêtes Judilibre.

### Où régler cela

Dans Claude, ouvrez **Paramètres → Capacités**. Faites défiler jusqu'à la rubrique « Liste d'autorisation de domaines », puis saisissez chaque domaine dans le champ « Domaines supplémentaires autorisés » et cliquez sur « Ajouter ».

### Quels domaines ajouter

| Domaine                         | Statut        | Quand l'ajouter                         |
| ------------------------------- | ------------- | --------------------------------------- |
| **api.piste.gouv.fr**           | Indispensable | Toujours (production, mode KeyId)       |
| **piste.gouv.fr**               | Indispensable | Toujours (en complément du précédent)   |
| **sandbox-api.piste.gouv.fr**   | Optionnel     | Uniquement en environnement bac à sable |
| **oauth.piste.gouv.fr**         | Optionnel     | Uniquement en mode OAuth2 (avancé)      |
| **sandbox-oauth.piste.gouv.fr** | Optionnel     | Uniquement bac à sable + OAuth2         |

En pratique, pour un usage normal en production, deux domaines suffisent : **api.piste.gouv.fr** et **piste.gouv.fr**. Les autres ne servent qu'au bac à sable ou au mode OAuth2.

> **Bon à savoir**
>
> Les liens publics vers les arrêts pointent vers www.courdecassation.fr, mais le skill ne s'y connecte pas : il se contente de construire l'adresse. Inutile donc d'autoriser ce domaine.
>
> Si une requête échoue avec « connexion impossible » ou « domaine non autorisé », c'est presque toujours **api.piste.gouv.fr** ou **piste.gouv.fr** qui manque dans la liste.

---

## 3. Installer le skill

Le skill se présente sous la forme d'un dossier contenant un fichier SKILL.md et un sous-dossier scripts/. Voici comment le mettre en place.

1. **Télécharger le skill** depuis le lien fourni (Notion ou Lawve AI — voir le premier commentaire de la publication).
2. **Ajouter le skill à Claude** : ouvrez **Personnaliser → Compétences**, puis cliquez sur le bouton **+** en haut de la liste pour importer le dossier du skill (ou son archive .zip).
3. **Renseigner votre clé PISTE — à la première utilisation**. Une fois le skill installé, ouvrez une conversation et indiquez simplement à Claude, dans le chat, que vous lui transmettez votre clé : par exemple « Voici ma clé PISTE pour Judilibre : _[votre KeyId]_ ».
4. **Claude l'enregistre pour vous** : il crée (ou complète) le fichier _scripts/config.json_ du skill en plaçant votre clé dans le champ `key_id` et en réglant l'environnement sur `prod`. Vous n'avez donc aucun fichier à éditer à la main. L'opération n'est à faire qu'une seule fois : la clé reste mémorisée pour les usages suivants.
5. **Vérifier l'installation** : demandez une première recherche (par exemple « cherche un arrêt de la chambre sociale sur la période d'essai »). Si une liste de décisions s'affiche, tout fonctionne.

> **Sécurité**
>
> Le fichier config.json contient votre clé en clair. Ne le partagez jamais et ne le publiez pas (ni sur un dépôt public, ni dans une capture d'écran).

---

## En cas de problème

- **Clé manquante** : fournissez votre KeyId à Claude pour qu'il l'enregistre.
- **Erreur 401** : clé incorrecte ou mauvais environnement (bac à sable au lieu de production).
- **Erreur 403** : CGU Judilibre non validées, ou API non rattachée à votre application PISTE.
- **Erreur 429 / 5xx** : quota atteint ou API momentanément indisponible — patientez puis réessayez.
- **« Domaine non autorisé »** : ajoutez api.piste.gouv.fr dans les réglages réseau (étape 2).

---

_Une fois ces trois étapes franchies, vous interrogez la jurisprudence de la Cour de cassation en langage naturel, directement dans vos conversations._
