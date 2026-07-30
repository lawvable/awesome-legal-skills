# Site démo — Boutique Exemple SAS

> **Document de démonstration pour le skill `audit-rgpd-site-internet`**
> Ce document simule l'extraction des pages clés d'un site fictif e-commerce.
> Il sert UNIQUEMENT à tester le skill. Toute ressemblance avec un site réel est fortuite.

URL fictive : `https://www.boutique-exemple.fr`
Date de l'extraction : 5 mai 2026
Mode : extraction textuelle (mode dégradé copier-coller)

---

## 1. Page d'accueil — Footer

Liens visibles dans le footer de chaque page :
- Mentions légales → `/mentions-legales`
- CGV → `/cgv` (la politique de confidentialité est intégrée à l'article 11 des CGV)
- Nous contacter → `/contact`
- Newsletter → champ d'inscription en bas du footer
- Aucun lien « Politique de confidentialité » distinct
- Aucun lien « Politique cookies » distinct
- Aucune icône permanente de réapparition du bandeau cookies

---

## 2. Page Mentions légales — `/mentions-legales`

> ## Mentions légales
>
> Le site `boutique-exemple.fr` est édité par :
>
> **Boutique Exemple SAS**
> SAS au capital de 50 000 €
> RCS Paris 123 456 789
> Siège social : 10 rue de la Boutique, 75001 Paris
> Directeur de la publication : Le directeur général
>
> **Hébergeur** :
> OVH SAS
> 2 rue Kellermann, 59100 Roubaix
>
> Pour toute question, contactez-nous à `contact@boutique-exemple.fr`.

**Éléments présents** : dénomination sociale, forme juridique, capital social, RCS, adresse, directeur de la publication, nom et adresse hébergeur.

**Éléments manquants** : numéro SIRET, numéro de TVA intracommunautaire, numéro de téléphone, SIRET de l'hébergeur, téléphone de l'hébergeur.

---

## 3. Page CGV — Article 11 « Données personnelles et cookies » — `/cgv`

> **Article 11 — Données personnelles et cookies**
>
> Boutique Exemple SAS attache une grande importance à la protection de vos données personnelles. Les données collectées sur le site sont traitées dans le cadre de notre relation commerciale.
>
> **Finalités** : nous traitons vos données pour la gestion de vos commandes, la livraison, le service client, et l'envoi de communications commerciales sur nos produits.
>
> **Base légale** : intérêt légitime de l'entreprise.
>
> **Destinataires** : nos prestataires.
>
> **Durée de conservation** : 3 ans après le dernier contact pour les prospects, 10 ans pour les clients (obligations comptables).
>
> **Vos droits** : vous disposez d'un droit d'accès, de rectification, et de suppression de vos données. Pour exercer vos droits, contactez `contact@boutique-exemple.fr`.
>
> **Cookies** : notre site utilise des cookies pour améliorer votre expérience.

**Constat** : la « politique de confidentialité » est fusionnée dans l'article 11 des CGV. Elle est très lacunaire : pas de DPO mentionné, intérêt légitime non décrit, transferts hors UE non mentionnés, droit d'opposition / portabilité / limitation absents, droit de réclamation CNIL absent, sources de collecte indirecte absentes, finalités non exhaustives (mesure d'audience non listée alors que GA est utilisé).

---

## 4. Page Contact — `/contact`

Formulaire de contact comprenant les champs : Nom\*, Email\*, Message\*.

Mention sous le formulaire :
> *« En soumettant ce formulaire, j'accepte que mes données soient utilisées pour traiter ma demande. Plus d'informations dans nos CGV. »*

**Constat** : mention présente mais minimaliste. Pas de mention explicite du responsable de traitement, pas de finalité détaillée, pas de durée de conservation, pas de mention des droits, pas d'astérisque distinguant champs obligatoires et facultatifs.

---

## 5. Bloc Newsletter (présent sur toutes les pages — bas de footer)

Champ unique : « Votre email pour recevoir nos offres ».
Sous le champ, une case à cocher **pré-cochée par défaut** avec le texte :
> *« J'accepte de recevoir les offres commerciales de Boutique Exemple. »*

Bouton « S'inscrire » à droite du champ.

**Constat** : case pré-cochée par défaut → consentement non valide (art. 7 RGPD + délibération CNIL). Pas de mention du droit de retrait, pas de finalité précise, pas de mention du responsable de traitement.

---

## 6. Bandeau cookies (au premier accès au site)

Capture textuelle du bandeau qui s'affiche au premier accès (en bas de la page d'accueil) :

> ### Nous utilisons des cookies
>
> Notre site utilise des cookies pour améliorer votre expérience et vous proposer des contenus adaptés.
>
> **[Tout accepter]** (gros bouton vert vif, occupant 60% de la largeur du bandeau)
> [Personnaliser] (lien texte gris pâle, taille standard, à droite)
>
> *Aucun bouton « Tout refuser » direct n'est proposé.*

Pour refuser, l'utilisateur doit :
1. Cliquer sur « Personnaliser »
2. Décocher chaque catégorie individuellement (3 catégories : Mesure d'audience, Publicité, Réseaux sociaux)
3. Cliquer sur « Enregistrer mes préférences »

**Cookies déposés AVANT toute interaction avec le bandeau** (vérifié dans les outils dev navigateur, onglet Application > Cookies, dès le chargement de la page d'accueil) :
- `_ga` (Google Analytics — durée 13 mois)
- `_ga_XXXXXXX` (Google Analytics 4 — durée 13 mois)
- `_fbp` (Meta Pixel — durée 90 jours)
- `_grecaptcha` (Google reCAPTCHA — durée session)

**Constat** : bandeau non conforme à la délibération CNIL 2020-091. Cookies optionnels déposés avant consentement. Refus disproportionné par rapport à l'acceptation.

---

## 7. Page de création de compte — `/creer-compte`

Formulaire avec champs : Email\*, Mot de passe\*, Confirmer mot de passe\*, Nom, Prénom, Adresse de livraison.

Exigence de mot de passe affichée :
> *« Votre mot de passe doit comporter au moins 8 caractères. »*

Aucune autre exigence (pas de majuscule, pas de chiffre, pas de caractère spécial).

Mention RGPD sous le bouton « Créer mon compte » :
> *« En créant un compte, j'accepte les CGV. »*

**Constat** : exigence de mot de passe insuffisante au regard de la délibération CNIL 2022-100 (12 caractères minimum recommandés avec complexité). Pas de mention RGPD spécifique à la création de compte (renvoi uniquement aux CGV).

---

## 8. Page de paiement — `/paiement` (étape de checkout)

Le formulaire de paiement charge un script externe depuis `https://js.stripe.com/v3/`.

Mention affichée :
> *« Paiement sécurisé. Vos données bancaires ne transitent pas par nos serveurs. »*

Aucune mention sur le sous-traitant de paiement (Stripe), sa localisation (États-Unis), ou le mécanisme de transfert applicable.

**Constat** : Stripe identifié comme sous-traitant US, non documenté dans la « politique » (article 11 des CGV) et non listé dans les destinataires.

---

## 9. Trackers et requêtes tierces détectés (analyse réseau)

Capture des requêtes tierces observées via les outils dev du navigateur (onglet Réseau) sur la page d'accueil :

| Domaine | Outil | Finalité | Localisation | Cookie tiers |
|---|---|---|---|---|
| `google-analytics.com` | Google Analytics 4 | Mesure d'audience | États-Unis | Oui (`_ga`, `_ga_XXXXXXX`) |
| `googletagmanager.com` | Google Tag Manager | Conteneur de tags | États-Unis | Non |
| `connect.facebook.net` | Meta Pixel | Publicité ciblée + retargeting | États-Unis (Meta Platforms Ireland) | Oui (`_fbp`) |
| `www.google.com/recaptcha` | Google reCAPTCHA | Anti-bot (formulaire contact) | États-Unis | Oui (`_grecaptcha`) |
| `fonts.googleapis.com` | Google Fonts (CDN Google) | Polices web | États-Unis | Non (mais transmet l'IP) |
| `js.stripe.com` | Stripe | Paiement (page checkout uniquement) | États-Unis | Non sur la home |
| `cdn-newsletter-us.com` (fictif) | Fournisseur de newsletter US | Newsletter | États-Unis | Non (POST API uniquement) |

Aucun de ces sous-traitants n'est mentionné nommément dans l'article 11 des CGV.

---

## 10. Données sensibles

Le site est un e-commerce de produits courants (vêtements et accessoires de mode). **Pas de données sensibles** au sens de l'art. 9 RGPD. L'arbre de décision « secteurs sensibles » ne s'applique pas.

---

## 11. Accessibilité du recueil des droits

Aucune adresse email dédiée (`privacy@`, `dpo@`, `donneespersonnelles@`) — uniquement `contact@boutique-exemple.fr`.
Aucun formulaire dédié pour les demandes d'exercice des droits.
Aucun délai de réponse annoncé dans l'article 11 des CGV.
Aucune mention de la possibilité d'introduire une réclamation auprès de la CNIL.
Aucune coordonnée de la CNIL fournie.

---

## 12. Données identifiantes accidentellement publiées

Aucune donnée personnelle identifiante observée sur les pages publiques auditées (pas de témoignage avec nom complet et email, pas de fiche équipe avec emails directs, pas de page démo avec données réelles).

---

## Récapitulatif des pages auditées

| Page | URL | Auditée |
|---|---|---|
| Accueil | `https://www.boutique-exemple.fr/` | Oui |
| Mentions légales | `/mentions-legales` | Oui |
| CGV (avec article 11 sur les données) | `/cgv` | Oui |
| Contact | `/contact` | Oui |
| Newsletter | (intégrée au footer) | Oui |
| Création de compte | `/creer-compte` | Oui |
| Paiement (checkout) | `/paiement` | Oui (mode anonyme — pas de panier rempli) |
| Politique de confidentialité distincte | — | **Absente** |
| Politique cookies distincte | — | **Absente** |

Outil utilisé : extraction textuelle (mode dégradé copier-coller).
Bandeau cookies vérifié au premier accès et après suppression des cookies.
Trackers identifiés via les outils dev navigateur (onglet Réseau).
