# Checklist d'audit RGPD d'un site internet — Référentiel praticien

> Knowledge file 1/2 — Skill `audit-rgpd-site-internet`
> Source : pratique de praticien RGPD/DPO, consolidée à partir de la doctrine CNIL (2020-091, 2022-100, exemption mesure d'audience), des articles 12-14 RGPD, de la LCEN, de la directive ePrivacy et des recommandations EDPB.

---

## Périmètre

L'audit couvre **dix sections**, toutes vérifiées par observation directe du site (navigation + outils développeur du navigateur). Pour chaque item, le praticien (assisté par IA) statue **Oui / Non / N/A** et complète la colonne **Observations** avec une citation textuelle, une URL ou une capture d'écran.

L'annexe 22 items reproduit les exigences des articles 13 et 14 RGPD pour la politique de confidentialité.

| # | Section | Référentiel principal |
|---|---|---|
| 1 | Mentions légales | LCEN art. 6-III, Décret 2007-1010 |
| 2 | Informations relatives à l'hébergeur | LCEN art. 6-III |
| 3 | Formulaires de collecte | RGPD art. 13 |
| 4 | Newsletter | RGPD art. 7 + ePrivacy art. 5(3) |
| 5 | Politique de confidentialité | RGPD art. 12-14 |
| 6 | Politique cookies et bandeau | Loi Informatique et Libertés art. 82 + délibération CNIL 2020-091 |
| 7 | Mots de passe (si authentification) | Délibération CNIL 2022-100 |
| 8 | Trackers et mesure d'audience | Recommandation CNIL exemption mesure d'audience |
| 9 | Sous-traitants détectables et transferts hors UE | RGPD art. 28 + 44-49, CCT 2021, EDPB 01/2020 |
| 10 | Accessibilité du recueil des droits | RGPD art. 12, 15-22 |

---

## Section 1 — Mentions légales

Objectif : vérifier la présence et la complétude des mentions légales obligatoires.

| Item | Description | Oui/Non |
|---|---|---|
| Présence | Le site comporte-t-il une page « Mentions légales » accessible ? | |
| Dénomination sociale | Nom de l'entreprise ou de l'éditeur | |
| SIRET | Numéro SIRET | |
| TVA intracommunautaire | Numéro de TVA intracommunautaire (si applicable) | |
| Forme juridique | Forme juridique (SAS, SARL, SCI, EI, etc.) | |
| Capital social | Montant du capital social (si applicable) | |
| Adresse | Adresse du siège social | |
| Téléphone | Numéro de téléphone | |
| Directeur de la publication | Nom du directeur de la publication |
| RCS / RM | Numéro d'inscription au RCS ou au Registre des métiers (si applicable) | |
| Numéro CNIL (si applicable) | Numéro de déclaration CNIL pour les traitements anciens encore notifiés | |

---

## Section 2 — Informations relatives à l'hébergeur

Objectif : vérifier la présence des informations sur l'hébergeur (LCEN art. 6-III).

| Item | Description | Oui/Non |
|---|---|---|
| Nom | Nom de l'hébergeur | |
| Raison sociale | Raison sociale de l'hébergeur | |
| Adresse | Adresse du siège social de l'hébergeur | |
| SIRET | Numéro SIRET de l'hébergeur (ou équivalent étranger) | |
| Téléphone | Numéro de téléphone de l'hébergeur | |
| Localisation des serveurs | Pays / zone d'hébergement (UE / US / autre) | |

---

## Section 3 — Formulaires de collecte des données

Objectif : vérifier que chaque formulaire de collecte sur le site comporte une mention d'information RGPD complète (art. 13 RGPD).

Pour CHAQUE formulaire identifié sur le site (contact, devis, candidature, création de compte, etc.), vérifier :

| Sous-item | Description | Oui/Non |
|---|---|---|
| Identité du responsable de traitement | Identifié sur le formulaire ou par renvoi | |
| Finalités | Finalités du traitement explicitées (« pour répondre à votre demande », « pour vous adresser nos communications commerciales », etc.) | |
| Base légale | Base légale indiquée ou inférable (consentement / contrat / intérêt légitime) | |
| Caractère obligatoire / facultatif | Champs obligatoires distingués des facultatifs (astérisque ou mention) | |
| Durée de conservation | Durée annoncée ou critère de détermination | |
| Renvoi à la politique de confidentialité | Renvoi explicite et cliquable | |
| Consentement données sensibles | Si données sensibles collectées (santé, opinions, syndicat, etc.) : consentement explicite recueilli ? | |
| Recueil de mineurs | Si mineurs concernés : mention adaptée et, si <15 ans, recueil consentement parental ? | |

---

## Section 4 — Newsletter

Objectif : vérifier la conformité du formulaire de souscription à la newsletter (consentement libre, spécifique, éclairé, univoque).

| Item | Description | Oui/Non |
|---|---|---|
| Recueil du consentement | Le formulaire recueille-t-il le consentement (si requis) ? | |
| Case à cocher vide par défaut | La case à cocher est-elle vide par défaut (pas de pré-cochage) ? | |
| Mention conforme | La mention de recueil du consentement est-elle conforme (finalité, droit de retrait, identité du responsable) ? | |
| Opt-out alternatif (B2B et clients existants) | Si pas de consentement requis (prospection vers clients existants pour produits analogues — art. L34-5 CPCE) : case d'opposition prévue ? | |
| Lien de désabonnement | Présent dans chaque email (vérification ultérieure si possible) ? | |

---

## Section 5 — Politique de confidentialité

Objectif : vérifier la présence et la conformité de la politique de confidentialité (art. 13 et 14 RGPD).

| Item | Description | Oui/Non |
|---|---|---|
| Présence | Le site comporte-t-il une politique de confidentialité ? | |
| Page dédiée | Figure-t-elle sur une page dédiée (et non noyée dans CGV) ? | |
| Complète | Est-elle complète (voir annexe 22 items art. 13/14 ci-dessous) ? | |
| Finalités exhaustives | Les finalités indiquées sont-elles exhaustives (ex : recrutement, prospection, mesure d'audience, etc.) ? | |
| Accessibilité | Est-elle facilement accessible depuis chaque page (footer, max 2 clics) ? | |
| Langue compréhensible | Est-elle dans une langue compréhensible par les personnes concernées (français pour un public francophone) ? | |
| Adaptée aux mineurs | Si les personnes concernées peuvent être des mineurs : compréhensible par eux ? | |
| Termes clairs et simples | Rédigée dans des termes clairs et simples (CNIL — principe de transparence) ? | |
| Date de mise à jour | Date de la dernière mise à jour visible ? | |
| Historique des versions | Possibilité de consulter les versions antérieures (recommandation CNIL) ? | |

---

## Section 6 — Politique cookies et bandeau

Objectif : vérifier la présence et la conformité de la politique cookies et du bandeau de consentement (art. 82 Loi Informatique et Libertés / art. 5(3) ePrivacy + délibération CNIL 2020-091).

### 6.1 Politique cookies

| Item | Description | Oui/Non |
|---|---|---|
| Politique cookies présente | Le site comporte-t-il une page ou une section politique cookies ? | |
| Politique cookies complète | Liste exhaustive des cookies (nom, finalité, durée, émetteur — first/third party) ? | |
| Distinction par finalité | Cookies regroupés par finalité (techniques, mesure d'audience, publicité, réseaux sociaux) ? | |
| Sous-traitants identifiés | Émetteurs tiers nommés explicitement (ex : Google Ireland Limited, Meta Platforms Ireland Ltd) ? | |
| Modalités de gestion | Modalités de gestion du consentement (renvoi vers paramétrage navigateur + lien rappel) ? | |

### 6.2 Bandeau cookies

| Item | Description | Oui/Non |
|---|---|---|
| Bandeau présent | Le site comporte-t-il un bandeau cookies au premier accès ? | |
| Identité responsable | Le bandeau indique-t-il l'identité du responsable de traitement (ou renvoi clair) ? | |
| Finalités cookies | Le bandeau indique-t-il la finalité de chaque type de cookies utilisés ? | |
| Modalités accept/refus | Le bandeau indique-t-il la manière d'accepter ou de refuser les traceurs ? | |
| Conséquences | Le bandeau indique-t-il les conséquences d'un refus ou d'une acceptation ? | |
| Droit de retrait | Le bandeau indique-t-il l'existence du droit de retirer son consentement ? | |
| Réapparition du bandeau | Une icône permanente facilement accessible permet-elle de faire ré-apparaître le bandeau ? | |
| Boutons équivalents (CNIL 2020-091) | Les boutons « accepter », « refuser » et « paramétrer » sont-ils de même couleur, taille et disposition ? | |
| Refus aussi simple | Refuser est-il aussi simple qu'accepter (pas de clics supplémentaires nécessaires) ? | |
| Cookies non déposés par défaut | Les cookies optionnels NE sont PAS déposés par défaut (avant consentement) ? | |
| Durée conservation choix | Combien de temps les choix sont-ils conservés ? (max 6 mois — recommandation CNIL) | |
| Granularité du consentement | Possibilité de consentir cookie par cookie ou par finalité ? | |

### 6.3 Mentions obligatoires des finalités (rappel CNIL)

- Cookies techniques : « afin de faciliter votre navigation sur le site »
- Cookies publicitaires : « vous proposer des publicités personnalisées en fonction de votre profil de navigation et de votre localisation »
- Cookies de réseaux sociaux : « partager des contenus sur les réseaux sociaux et autres plateformes en ligne »
- Cookies de mesure d'audience : « établir des statistiques ayant pour objectif d'améliorer votre expérience sur notre site »

---

## Section 7 — Mots de passe (si site avec authentification)

Objectif : vérifier que les exigences sur les mots de passe sont conformes aux recommandations CNIL (délibération 2022-100).

| Item | Description | Oui/Non |
|---|---|---|
| Conformité CNIL | Les exigences sur les mots de passe sont-elles conformes aux recommandations CNIL ? | |
| Verrouillage après échecs | Verrouillage temporaire après plusieurs échecs (force brute) ? | |
| Réinitialisation sécurisée | Procédure de réinitialisation par email avec lien à durée limitée ? | |
| Pas de communication en clair | Pas d'envoi du mot de passe par email après inscription ? | |
| MFA disponible | Authentification multi-facteurs disponible (recommandé pour comptes sensibles) ? | |

**Trois exemples conformes CNIL (au choix) :**
- **Exemple 1** : 12 caractères minimum + majuscules + minuscules + chiffres + caractères spéciaux (parmi ≥37)
- **Exemple 2** : 14 caractères minimum + majuscules + minuscules + chiffres (sans caractère spécial obligatoire)
- **Exemple 3** : Phrase de passe ≥ 7 mots

---

## Section 8 — Trackers et mesure d'audience

Objectif : vérifier la conformité des outils de mesure d'audience et des pixels publicitaires (référentiel CNIL — exemption de consentement pour la mesure d'audience).

### 8.1 Identification des trackers

Lister tous les trackers détectés (via outils dev navigateur — onglet Réseau + extension uBlock Origin / Privacy Badger pour identification rapide) :

| Tracker | Émetteur | Finalité | Cookie tiers ? | Consentement requis ? |
|---|---|---|---|---|
| ex : Google Analytics 4 | Google Ireland Ltd | Mesure d'audience | Oui (third-party) | Oui (pas exemptable en l'état actuel) |
| ex : Meta Pixel | Meta Platforms Ireland Ltd | Publicité ciblée | Oui | Oui |
| ex : Matomo (self-hosted) | [Hébergeur du site] | Mesure d'audience | Non (first-party) | Non si configuration exemption CNIL |
| ex : Hotjar / Microsoft Clarity | Hotjar Ltd / Microsoft | Heatmap, replay session | Oui | Oui |

### 8.2 Critères d'exemption CNIL pour la mesure d'audience

Pour qu'un outil de mesure d'audience soit exempté de consentement, il doit cumulativement :

| Critère | Description | Oui/Non |
|---|---|---|
| Finalité strictement limitée | Mesure de l'audience du site et de ses performances uniquement | |
| Pas de croisement | Données non recoupées avec d'autres traitements ou retransmises à des tiers | |
| Anonymisation IP | Adresse IP tronquée (au moins le dernier octet) avant stockage | |
| Pas de tracking inter-sites | Pas de suivi de la navigation sur d'autres sites | |
| Durée raisonnable | Durée de vie du cookie ≤ 13 mois, durée de conservation des données ≤ 25 mois | |
| Hébergement | Données hébergées dans l'UE ou pays adéquat (Schrems II) | |

**Point d'attention** : Google Analytics (GA4) ne respecte pas tous ces critères dans sa configuration standard. La CNIL a confirmé que GA4 n'est pas exempté de consentement. Une configuration avec server-side proxying peut être envisagée mais reste discutée.

### 8.3 Cohérence avec la politique cookies

| Item | Description | Oui/Non |
|---|---|---|
| Tous les trackers listés | Chaque tracker observé techniquement est-il listé dans la politique cookies ? | |
| Cohérence finalités | Les finalités annoncées correspondent-elles à l'usage réel ? | |
| Cohérence consentement | Les trackers nécessitant consentement sont-ils effectivement bloqués jusqu'à acceptation ? | |

---

## Section 9 — Sous-traitants détectables et transferts hors UE

Objectif : identifier les sous-traitants visibles via l'analyse du site et vérifier les transferts hors UE (RGPD art. 28 + 44-49).

### 9.1 Cartographie des sous-traitants détectables

Pour chaque type de service, identifier le sous-traitant utilisé :

| Catégorie | Exemples de sous-traitants courants | Localisation typique | Mécanisme transfert si hors UE |
|---|---|---|---|
| Hébergement web | OVH, Scaleway, AWS, Google Cloud, Azure | UE ou US | DPF / CCT 2021 / Profil régional |
| CDN | Cloudflare, Akamai, Fastly | US (mais POPs UE) | DPF / CCT 2021 |
| Paiement en ligne | Stripe, PayPal, Adyen, Worldline | US ou UE | DPF / CCT 2021 |
| Newsletter | Mailchimp, Brevo, Sendinblue, Mailjet | US ou UE | DPF / CCT 2021 |
| CRM / Marketing | HubSpot, Salesforce, Marketo, ActiveCampaign | US | DPF / CCT 2021 |
| Mesure d'audience | Google Analytics, Matomo, Plausible, Fathom | US ou UE | DPF / CCT 2021 si US |
| Chat / Support | Intercom, Crisp, Zendesk, Freshdesk | US ou UE | DPF / CCT 2021 si US |
| Vidéo embarquée | YouTube, Vimeo, Dailymotion | US ou UE | DPF / CCT 2021 si US |
| Polices web | Google Fonts (CDN), Adobe Fonts | US | DPF / CCT 2021 si appel API externe |
| Carte interactive | Google Maps, OpenStreetMap, Mapbox | US ou UE | DPF / CCT 2021 si US |
| reCAPTCHA / anti-bot | Google reCAPTCHA, hCaptcha, Cloudflare Turnstile | US ou UE | DPF / CCT 2021 si US |

### 9.2 Vérifications par sous-traitant identifié

Pour chaque sous-traitant identifié sur le site :

| Item | Description | Oui/Non |
|---|---|---|
| Mentionné dans la politique | Le sous-traitant est-il nommé dans la politique de confidentialité ? | |
| Finalité documentée | La finalité du traitement délégué est-elle documentée ? | |
| Localisation indiquée | La localisation du traitement (UE / hors UE) est-elle indiquée ? | |
| Mécanisme de transfert | Si hors UE : mécanisme indiqué (DPF, CCT 2021, BCR, dérogation art. 49) ? | |
| TIA mentionnée | Si transfert vers pays tiers à risque : TIA réalisée et mesures supplémentaires (EDPB 01/2020) ? | |

### 9.3 Cas Google reCAPTCHA et Google Fonts

Cas fréquents et souvent oubliés :
- **reCAPTCHA** : transmet l'IP et des données de comportement à Google Inc. (US). Consentement souvent non recueilli (chargé avant accept/refus du bandeau).
- **Google Fonts hébergé chez Google** : transmet l'IP au CDN Google. Recommandation : héberger les fontes en local ou utiliser un proxy.

---

## Section 10 — Accessibilité du recueil des droits

Objectif : vérifier que les personnes concernées peuvent exercer leurs droits RGPD facilement (art. 12 + 15-22 RGPD).

| Item | Description | Oui/Non |
|---|---|---|
| Adresse dédiée | Adresse email dédiée (privacy@, dpo@, donneespersonnelles@) ou seulement contact@ ? | |
| Formulaire dédié | Formulaire en ligne pour les demandes d'exercice des droits ? | |
| Liste des droits | Liste exhaustive des droits dans la politique de confidentialité (accès, rectification, effacement, limitation, opposition, portabilité, retrait du consentement) ? | |
| Délai annoncé | Délai de réponse annoncé (1 mois, prolongation possible 2 mois — art. 12§3) ? | |
| Modalités d'identification | Modalités d'identification proportionnées (pas de demande systématique de pièce d'identité) ? | |
| Mention CNIL | Mention de la possibilité d'introduire une réclamation auprès de la CNIL (art. 77) ? | |
| Coordonnées CNIL | Coordonnées de la CNIL fournies (3 Place de Fontenoy, 75007 Paris — www.cnil.fr/plaintes) ? | |
| Gratuité | Gratuité de la première demande mentionnée (art. 12§5) ? | |

---

## Annexe — Analyse de la politique de confidentialité (22 items art. 13/14 RGPD)

> Cette annexe complète la Section 5 « Politique de confidentialité ». Elle vérifie la complétude au regard des articles 13 et 14 RGPD.

Pour chaque item, statuer **Existence Oui/Non**, **Complet Oui/Non**, **Risque** (1 = conformité totale, 2 = conformité moyenne, 3 = conformité faible) et **Observations**.

| # | Exigence | Existence | Complet | Risque |
|---|---|---|---|---|
| 1 | Identité du responsable de traitement (art. 13(1)(a)) | Oui/Non | Oui/Non | |
| 2 | Coordonnées du responsable de traitement (art. 13(1)(a)) | Oui/Non | Oui/Non | |
| 3 | Coordonnées du délégué à la protection des données (art. 13(1)(b)) | Oui/Non | Oui/Non | |
| 4 | Finalité du traitement (art. 13(1)(c)) | Oui/Non | Oui/Non | |
| 5 | Base juridique du traitement (art. 13(1)(c)) | Oui/Non | Oui/Non | |
| 6 | Intérêts légitimes poursuivis (si base = intérêt légitime) (art. 13(1)(d)) | Oui/Non | Oui/Non | |
| 7 | Destinataires ou catégories de destinataires (art. 13(1)(e)) | Oui/Non | Oui/Non | |
| 8 | Transferts hors UE et garanties appropriées (art. 13(1)(f)) | Oui/Non | Oui/Non | |
| 9 | Durée de conservation ou critères (art. 13(2)(a)) | Oui/Non | Oui/Non | |
| 10 | Droit d'accès (art. 13(2)(b)) | Oui/Non | Oui/Non | |
| 11 | Droit de rectification (art. 13(2)(b)) | Oui/Non | Oui/Non | |
| 12 | Droit d'effacement (art. 13(2)(b)) | Oui/Non | Oui/Non | |
| 13 | Droit à la limitation (art. 13(2)(b)) | Oui/Non | Oui/Non | |
| 14 | Droit d'opposition (art. 13(2)(b)) | Oui/Non | Oui/Non | |
| 15 | Droit à la portabilité (art. 13(2)(b)) | Oui/Non | Oui/Non | |
| 16 | Droit de retirer le consentement (art. 13(2)(c)) | Oui/Non | Oui/Non | |
| 17 | Droit d'introduire une réclamation auprès d'une autorité de contrôle (art. 13(2)(d)) | Oui/Non | Oui/Non | |
| 18 | Caractère règlementaire ou contractuel de la fourniture (art. 13(2)(e)) | Oui/Non | Oui/Non | |
| 19 | Conséquences de la non-fourniture (art. 13(2)(e)) | Oui/Non | Oui/Non | |
| 20 | Décision automatisée / profilage et logique sous-jacente (art. 13(2)(f)) | Oui/Non | Oui/Non | |
| 21 | Si collecte indirecte : catégories de données (art. 14(1)(d)) | Oui/Non | Oui/Non | |
| 22 | Si collecte indirecte : source des données (art. 14(2)(f)) | Oui/Non | Oui/Non | |

---

## Échelle de risque (utilisée dans l'annexe)

| Code | Signification | Critère d'attribution |
|---|---|---|
| **1** | Conformité totale | Item présent et complet, conforme à l'exigence RGPD |
| **2** | Conformité moyenne | Item présent mais incomplet, vague, ou ne respecte qu'une partie de l'exigence |
| **3** | Conformité faible | Item absent, ou contenu contraire à l'exigence RGPD |

---

## Pages à parcourir lors de l'audit

L'audit porte sur **toutes les pages du site**, en priorité :

1. Page d'accueil (présence des liens vers mentions légales, politique de confidentialité, politique cookies dans le footer)
2. Page « Mentions légales »
3. Page « Politique de confidentialité »
4. Page « Politique cookies » (si distincte)
5. Page « Conditions générales de vente / d'utilisation » (vérifier qu'elle ne fusionne PAS avec la politique de confidentialité)
6. Toutes les pages contenant un formulaire de collecte (contact, devis, newsletter, création de compte, candidature, etc.)
7. Page de paiement (si e-commerce — vérification de la mention sur les données bancaires et le sous-traitant de paiement)
8. Footer de chaque page (vérification de la persistance des liens permanents)
9. Bandeau cookies (au premier accès et icône de réapparition)
10. Pages où s'affichent des données dynamiques (recherche, profil utilisateur, espace client si accessible)
11. Page de création de compte et de réinitialisation de mot de passe (si authentification)
12. Plan du site / sitemap (pour identifier toutes les pages publiques)

---

## Outils techniques recommandés pour l'audit

| Outil | Usage |
|---|---|
| Outils de développement du navigateur (F12) | Onglet Application → Cookies (cookies déposés), onglet Réseau (requêtes tierces, trackers) |
| Extension uBlock Origin ou Privacy Badger | Identification rapide des trackers tiers |
| Extension Wappalyzer ou BuiltWith | Identification des technologies (CMS, frameworks, analytics, hébergeur) |
| Whois / DNS lookup | Identification de l'hébergeur, du CDN, du registrar |
| Lighthouse (audit Chrome) | Audit complémentaire performance + accessibilité (utile pour les recommandations) |
| EDPS Website Evidence Collector (open source) | Outil officiel européen pour collecte automatisée de preuves d'audit |

L'utilisation de ces outils relève de l'observation passive du site et ne constitue PAS une atteinte à la sécurité (pas de scan de vulnérabilités, pas d'injection, pas de tentative d'accès non autorisé).
