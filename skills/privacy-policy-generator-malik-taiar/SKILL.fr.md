---
name: politique-confidentialite-malik-taiar
description: Guide pour la rédaction de politiques de confidentialité conformes au RGPD. Contient les recommandations CNIL 2020, un template de référence et les bonnes pratiques. À utiliser lors de la rédaction ou révision d'une politique de confidentialité pour un site web ou une application.
metadata:
  author: Malik Taiar
  license: AGPL-3.0
  version: 2025.12.24
---

# Guide des Politiques de Confidentialité - RGPD

## Vue d'ensemble

La politique de confidentialité est le document principal d'information des personnes concernées au titre des articles 13 et 14 du RGPD. Elle doit être claire, accessible et exhaustive.

### Objectifs de la politique

| Objectif | Exigence RGPD |
|----------|---------------|
| **Transparence** | Informer clairement sur les traitements (Art. 12) |
| **Information** | Fournir toutes les mentions obligatoires (Art. 13-14) |
| **Droits** | Permettre l'exercice des droits des personnes (Art. 15-22) |
| **Confiance** | Rassurer les utilisateurs sur la protection de leurs données |

---

## Ressources de référence

### Templates

| Template | Description |
|----------|-------------|
| `assets/sample_template_politique_confidentialite.docx` | Template par défaut à utiliser si aucun modèle privé n'est fourni |
| Template interne fourni par l'avocat | À utiliser si l'avocat dispose d'un modèle privé plus adapté |

> **IMPORTANT** : Le template par défaut `sample_template_politique_confidentialite` est conçu pour un **site vitrine sans utilisateurs**. Si la demande concerne une **application ou plateforme avec des utilisateurs**, il faudra ajouter des catégories supplémentaires de données collectées, telles que :
> - Gestion de comptes utilisateurs (création, authentification, profil)
> - Données de connexion et historique d'activité
> - Données générées par l'utilisation de l'application
> - Communications entre utilisateurs (messages, commentaires, etc.)
> - Préférences et paramètres utilisateur
>
> Adaptez le template en fonction du type de plateforme (site vitrine, e-commerce, SaaS, application mobile, marketplace, etc.).

### Documentation CNIL

| Document | Contenu |
|----------|---------|
| **[CNIL_droits_personnes.pdf](./assets/CNIL_droits_personnes.pdf)** | Guide sur les droits des personnes (accès, rectification, effacement, etc.) |
| **[CNIL_durees_conservation.pdf](./assets/CNIL_durees_conservation.pdf)** | Recommandations sur les durées de conservation par type de données |
| **[CNIL_finalites.pdf](./assets/CNIL_finalites.pdf)** | Comment définir correctement les finalités de traitement |
| **[CNIL_transparence.pdf](./assets/CNIL_transparence.pdf)** | Guide sur l'information et la transparence envers les personnes |
| **[CNIL_principes_rgpd.pdf](./assets/CNIL_principes_rgpd.pdf)** | Les principes fondamentaux du RGPD |
| **[RGPD_texte_officiel.pdf](./assets/RGPD_texte_officiel.pdf)** | Texte intégral du Règlement UE 2016/679 |

### Fiches de connaissance

| Document | Contenu |
|----------|---------|
| **[BASES_LEGALES.md](./references/BASES_LEGALES.md)** | Les 6 bases légales du traitement (Art. 6 RGPD) avec exemples et formulations |
| **[DROITS_PERSONNES.md](./references/DROITS_PERSONNES.md)** | Les 8 droits des personnes concernées (Art. 15-22 RGPD) avec modalités d'exercice |
| **[COOKIES.md](./references/COOKIES.md)** | Recommandations CNIL 2020 sur les cookies, catégories, bannières, sanctions |
| **[DUREES_CONSERVATION.md](./references/DUREES_CONSERVATION.md)** | Tableaux des durées de conservation par type de données avec justifications légales |

---

## Informations à collecter auprès du client

> **IMPORTANT** : Avant de rédiger la politique, collecter TOUTES les informations ci-dessous auprès du client.

### 1. Informations sur le responsable de traitement

- [ ] Dénomination sociale complète
- [ ] Forme juridique (SAS, SARL, etc.)
- [ ] Numéro SIREN/SIRET
- [ ] Adresse du siège social
- [ ] Représentant légal (nom et fonction)
- [ ] Email de contact général
- [ ] DPO désigné ? Si oui, coordonnées

### 2. Nature du site/application

- [ ] URL du site web existant (pour analyse)
- [ ] Type de plateforme :
  - Site vitrine
  - E-commerce
  - SaaS / Application web
  - Application mobile
  - Marketplace
  - Autre : ___________
- [ ] Secteur d'activité
- [ ] Audience cible (B2B, B2C, les deux)
- [ ] Pays ciblés (France uniquement, UE, international)

### 3. Données collectées

Pour chaque catégorie, préciser si applicable :

- DONNÉES D'IDENTIFICATION
  - [ ] Nom, prénom
  - [ ] Email
  - [ ] Téléphone
  - [ ] Adresse postale
  - [ ] Date de naissance
  - [ ] Photo / Avatar

- DONNÉES DE CONNEXION
  - [ ] Adresse IP
  - [ ] Logs de connexion
  - [ ] Device ID
  - [ ] Identifiants de compte

- DONNÉES DE NAVIGATION
  - [ ] Pages visitées
  - [ ] Temps passé
  - [ ] Clics
  - [ ] Source de trafic

- DONNÉES DE TRANSACTION
  - [ ] Historique des commandes
  - [ ] Données de paiement (via prestataire)
  - [ ] Factures

- DONNÉES SENSIBLES (attention particulière)
  - [ ] Données de santé
  - [ ] Opinions politiques/religieuses
  - [ ] Origine ethnique
  - [ ] Données biométriques

### 4. Bases légales des traitements

> **QUESTION CLÉ** : Pour chaque traitement, quelle est la base légale ?

| Base légale | Quand l'utiliser | Exemple |
|-------------|------------------|---------|
| **Exécution du contrat** (Art. 6.1.b) | Traitement nécessaire pour fournir le service | Livraison d'une commande, création de compte |
| **Consentement** (Art. 6.1.a) | Choix libre de la personne, retirable à tout moment | Newsletter, cookies marketing, partage avec partenaires |
| **Intérêt légitime** (Art. 6.1.f) | Intérêt de l'entreprise, équilibré avec les droits des personnes | Statistiques anonymisées, sécurité, prospection B2B |
| **Obligation légale** (Art. 6.1.c) | Imposée par la loi | Conservation des factures 10 ans, obligations fiscales |


**TABLEAU À REMPLIR AVEC LE CLIENT :**

| Finalité du traitement | Base légale | Données concernées |
|------------------------|-------------|-------------------|
| Gestion des commandes  |             |                   |
| Création de compte     |             |                   |
| Newsletter             |             |                   |
| Statistiques           |             |                   |
| Service client         |             |                   |
| Prospection commerciale|             |                   |
| ___________________    |             |                   |

### 5. Destinataires et sous-traitants

- SOUS-TRAITANTS TECHNIQUES
  - [ ] Hébergeur : ___________
  - [ ] Prestataire emailing : ___________
  - [ ] Prestataire paiement : ___________
  - [ ] Analytics : ___________
  - [ ] CRM : ___________
  - [ ] Support/Ticketing : ___________

- TRANSFERTS HORS UE
  - [ ] Oui / Non
  - [ ] Si oui, vers quels pays ? ___________
  - [ ] Garanties mises en place :
    - [ ] Clauses contractuelles types
    - [ ] Décision d'adéquation
    - [ ] Autre : ___________

### 6. Cookies et traceurs

- COOKIES UTILISÉS
  - [ ] Cookies strictement nécessaires (session, panier, authentification)
  - [ ] Cookies analytics (Google Analytics, Matomo, etc.)
  - [ ] Cookies publicitaires (Facebook Pixel, Google Ads, etc.)
  - [ ] Cookies de réseaux sociaux (boutons de partage)
  - [ ] Autres : ___________

- SOLUTION DE GESTION DU CONSENTEMENT
  - [ ] Aucune
  - [ ] Axeptio
  - [ ] Didomi
  - [ ] Cookiebot
  - [ ] Autre : ___________

### 7. Durées de conservation

| Type de données | Durée proposée | Justification |
|-----------------|----------------|---------------|
| Compte client actif | Durée de la relation |  |
| Compte client inactif | 3 ans après dernière activité | Prospection |
| Prospects | 3 ans sans interaction | Recommandation CNIL |
| Factures | 10 ans | Obligation légale |
| Logs de connexion | 1 an | LCEN |
| Cookies | 13 mois max | Recommandation CNIL |

---

## Workflow de rédaction

### Étape 1 : Sélection du template (OBLIGATOIRE)

> **NE JAMAIS RÉDIGER UNE POLITIQUE DE ZÉRO.**
> Il est indispensable de toujours partir d'un template donné pour la rédaction, soit :
> - le template par défaut dans `assets/sample_template_politique_confidentialite.docx` ;
> - un autre modèle interne fourni par l'utilisateur.
>
> Ce template est ta référence de base. Tu dois :
> - **Reproduire fidèlement la structure et la rédaction du template**
> - **Garder les formulations exactes du template** (elles sont validées)
> - **Uniquement remplacer les placeholders** par les informations du client
> - **Ne PAS réécrire les phrases** même si tu penses pouvoir mieux formuler
> - **Ne PAS ajouter de sections** qui ne sont pas dans le template
>
> Les informations collectées (CGS, site, etc.) servent à **remplir** le template, **pas à le réécrire**.

**1. PREMIÈRE ACTION : Confirmer le template à utiliser AVANT toute rédaction. Demander à l'utilisateur :**
```
"Je vais rédiger la politique de confidentialité en partant du template fourni par défaut. Disposez-vous d'un template interne plus adapté sur lequel vous souhaiteriez partir ?"
```

| Option | Action |
|--------|--------|
| Template par défaut | Utiliser `assets/sample_template_politique_confidentialite.docx` |
| Template interne | Utiliser le document fourni par l'avocat |

**2. Considérez le choix de l'utilisateur et sélectionnez le template de départ.**

---

### Étape 2 : Comprendre l'activité du client

> **OBJECTIF PRINCIPAL** : Comprendre vraiment ce que le client fait, son activité, le parcours utilisateur sur sa plateforme.

**1. Demander à l'avocat les éléments dont il dispose :**
```
"Pour rédiger une politique parfaitement adaptée, merci de me transmettre :
- Les informations que vous avez sur le client et son activité
- Les documents existants (CGS, CGV, bons de commande, contrats...)
- Les échanges ou points clés remontés par le client
- L'URL du site/application (si accessible)
- Les points qui doivent absolument figurer selon vous

Vous pouvez transmettre ces informations de manière anonymisée si nécessaire pour des raisons de confidentialité.

Plus vous fournissez d'informations, plus la politique sera adaptée au cas réel. Sinon, nous ferons nos propres recherches mais elles seront limitées aux informations publiquement accessibles."
```

**2. Analyser les documents fournis :**

| Document | Ce qu'on en tire |
|----------|------------------|
| CGS / CGV | Fonctionnement de la plateforme, services proposés, obligations |
| Bons de commande | Données collectées, prestations, sous-traitants éventuels |
| Échanges client | Points clés, préoccupations spécifiques, particularités métier |

**3. Recherches complémentaires sur le site (si accessible) :**

> Note : Certains sites n'affichent qu'un formulaire "Demander un devis" sans accès à la plateforme. Dans ce cas, se baser principalement sur les documents fournis.

L'objectif est de **comprendre l'activité** ET **identifier les éléments techniques** :
- Comprendre ce que fait concrètement l'entreprise
- Lire la politique de confidentialité existante (si présente)
- Lire les CGV/CGU/mentions légales existantes
- Identifier le parcours utilisateur type (si visible)
- **Identifier les formulaires de collecte** (inscription, contact, commande...)
- **Repérer les cookies/traceurs** via la bannière
- **Lister les fonctionnalités** (compte, newsletter, chat, paiement...)

**4. Synthèse avant rédaction :**

```
CLIENT : [Nom]
ACTIVITÉ : [Description en 2-3 phrases]
TYPE DE PLATEFORME : [SaaS, e-commerce, app mobile, etc.]
PARCOURS UTILISATEUR : [Étapes clés]
DONNÉES COLLECTÉES : [Liste par moment de collecte]
COOKIES IDENTIFIÉS : [Types de cookies repérés]
FORMULAIRES : [Liste des points de collecte]
POINTS CLÉS AVOCAT : [Ce qui doit absolument figurer]
SPÉCIFICITÉS : [Ce qui rend ce cas particulier]
```

> Une fois la synthèse prête → Passer à la rédaction du Draft 1

---

### Étape 3 : Rédaction du Draft 1

> **RÈGLE ABSOLUE** : Le template est votre base validée.
>
> - **PARTIR du template** : structure, formulations, ton → c'est ta référence
> - **ADAPTER au cas client** : intégrer les informations spécifiques collectées
> - **NE PAS tout réécrire** : garde la rédaction du template, adapte uniquement ce qui doit l'être
>
> En résumé : Template + informations client = Draft 1. Pas une réécriture complète.

Compléter le template section par section avec les informations collectées :

1. **Identité du responsable de traitement**
2. **Données collectées** (par catégorie)
3. **Finalités et bases légales** (tableau)
4. **Destinataires et sous-traitants**
5. **Transferts internationaux**
6. **Durées de conservation** (tableau)
7. **Droits des personnes**
8. **Modalités d'exercice des droits**
9. **Cookies et traceurs**
10. **Sécurité des données**
11. **Modifications de la politique**
12. **Contact**

> **Vérification conformité immédiate :** Avant de présenter le Draft 1, vérifier la checklist des mentions obligatoires (Art. 13 RGPD) :
> - [ ] Identité et coordonnées du responsable
> - [ ] Coordonnées du DPO (si désigné)
> - [ ] Finalités du traitement
> - [ ] Base légale pour chaque finalité
> - [ ] Intérêts légitimes poursuivis (si applicable)
> - [ ] Destinataires ou catégories de destinataires
> - [ ] Transferts hors UE et garanties
> - [ ] Durée de conservation ou critères de détermination
> - [ ] Droits des personnes (accès, rectification, effacement, limitation, portabilité, opposition)
> - [ ] Droit de retirer le consentement (si applicable)
> - [ ] Droit de réclamation auprès de la CNIL
> - [ ] Caractère obligatoire/facultatif de la fourniture des données
> - [ ] Existence d'une prise de décision automatisée (si applicable)
>
> Si Draft 1 conforme → Passer à l'étape 3.

---

### Étape 4 : Livraison Draft 1 + benchmark + propositions d'amélioration

**1. Livrer le Draft 1 avec explication :**
```
Voici le Draft 1 de la politique de confidentialité.

**Ce que j'ai pris en compte :**
- [Résumé des éléments clés intégrés]
- [Spécificités du client prises en compte]
- [Points particuliers mentionnés par l'avocat]

**Conformité :** Le document respecte les exigences de l'Art. 13 RGPD.
```

**2. Présenter le benchmark (systématique) :**

Rechercher 3-5 politiques de confidentialité d'entreprises du même secteur, puis présenter :
```
**Benchmark réalisé :**

J'ai analysé les politiques de confidentialité de :
- [Entreprise 1] - [ce qu'on a noté]
- [Entreprise 2] - [ce qu'on a noté]
- [Entreprise 3] - [ce qu'on a noté]

**Améliorations possibles identifiées :**
- [Amélioration 1] : [explication]
- [Amélioration 2] : [explication]
- [Amélioration 3] : [explication]

Souhaitez-vous intégrer ces éléments au Draft fourni ?
```

**3. Si l'avocat valide des améliorations → Produire le Draft 2.**

---

### Étape 5 : Vérification finale

Dernière relecture avant livraison définitive :

- [ ] Toutes les mentions Art. 13 RGPD présentes
- [ ] Informations client correctement intégrées
- [ ] Langage clair et accessible
- [ ] Pas de références internes (template, sources) dans le document final
- [ ] Date de mise à jour présente

---

## Structure type de la politique

```
POLITIQUE DE CONFIDENTIALITÉ
[Nom de l'entreprise]
Dernière mise à jour : [DATE]

SOMMAIRE (si document long)

1. QUI SOMMES-NOUS ?
   - Identité du responsable
   - Coordonnées du DPO

2. QUELLES DONNÉES COLLECTONS-NOUS ?
   - Données d'identification
   - Données de navigation
   - Données de transaction
   - Etc.

3. POURQUOI COLLECTONS-NOUS VOS DONNÉES ?
   - Tableau finalités / bases légales

4. AVEC QUI PARTAGEONS-NOUS VOS DONNÉES ?
   - Services internes
   - Sous-traitants
   - Partenaires (si consentement)
   - Autorités (obligations légales)

5. VOS DONNÉES SONT-ELLES TRANSFÉRÉES HORS DE L'UE ?
   - Pays concernés
   - Garanties

6. COMBIEN DE TEMPS CONSERVONS-NOUS VOS DONNÉES ?
   - Tableau des durées par type de données

7. QUELS SONT VOS DROITS ?
   - Liste des droits avec explication simple
   - Comment les exercer

8. COOKIES ET TRACEURS
   - Types de cookies utilisés
   - Gestion des préférences

9. SÉCURITÉ
   - Mesures mises en place (sans détails techniques sensibles)

10. MODIFICATIONS DE CETTE POLITIQUE
    - Procédure d'information

11. NOUS CONTACTER
    - Email
    - Adresse postale
    - Lien vers formulaire
```

---

## Bonnes pratiques de rédaction

### Style rédactionnel

| À faire | À éviter |
|---------|----------|
| Utiliser "vous" / "vos données" | Utiliser "l'utilisateur" / "la personne concernée" |
| Phrases courtes et simples | Jargon juridique excessif |
| Exemples concrets | Formulations vagues ("diverses données") |
| Tableaux pour clarifier | Paragraphes denses |
| Titres clairs et explicites | Renvois multiples sans explication |

### Accessibilité

- **Langage clair** : compréhensible par un utilisateur non-juriste
- **Structure visible** : sommaire, titres numérotés
- **Information en couches** : résumé + détails si besoin
- **Date de mise à jour** : visible en haut du document

---

## Erreurs fréquentes à éviter

| Erreur | Conséquence | Solution |
|--------|-------------|----------|
| Copier-coller d'un modèle générique | Non-conformité, incohérence | Adapter à chaque cas |
| Bases légales incorrectes | Traitement illicite | Analyser chaque finalité |
| Durées de conservation absentes | Non-conformité Art. 13 | Tableau systématique |
| Oubli des transferts hors UE | Amende potentielle | Vérifier les sous-traitants |
| Droits mentionnés sans modalités | Droits non exerçables | Adresse email dédiée |
| Cookie wall | Interdit par la CNIL | Refus aussi simple que acceptation |

---

## Sanctions CNIL de référence

| Entreprise | Montant | Motif principal |
|------------|---------|-----------------|
| Google | 150 M€ | Cookies : refus plus difficile que acceptation |
| Facebook | 60 M€ | Cookies : absence de bouton "tout refuser" |
| Carrefour | 3 M€ | Information insuffisante, durées excessives |
| Amazon | 35 M€ | Cookies déposés sans consentement |

> Ces sanctions illustrent l'importance d'une politique conforme et d'une gestion rigoureuse des cookies.

---

## Questions fréquentes

### 1. La politique doit-elle être en français ?

**Oui**, si le site cible des utilisateurs français. Elle peut être bilingue si le site est international.

### 2. Faut-il une politique séparée pour l'application mobile ?

**Pas nécessairement**, mais la politique doit couvrir les spécificités de l'app (permissions, données collectées par le device).

### 3. Comment gérer les mises à jour ?

- Dater chaque version
- Informer les utilisateurs des modifications substantielles
- Conserver les versions antérieures

### 4. Le DPO est-il obligatoire ?

**Non systématiquement.** Obligatoire si :
- Autorité publique
- Traitement à grande échelle de données sensibles
- Suivi régulier et systématique à grande échelle

---

## Utilisation de ce guide

1. **Étape 1 - Choisir le template** : Par défaut, ou template interne de l'avocat
2. **Étape 2 - Comprendre l'activité** : Collecter les docs de l'avocat + recherches sur le site
3. **Étape 3 - Rédiger le Draft 1** : Compléter le template + vérification conformité
4. **Étape 4 - Livrer + Benchmark** : Présenter le Draft 1 + benchmark systématique + propositions d'amélioration
5. **Étape 5 - Finaliser** : Intégrer les améliorations validées + vérification finale

> **RAPPEL TEMPLATE** : Ne jamais rédiger depuis zéro. Toujours partir du template et l'adapter.
>
> **RAPPEL SOURCES** : Les références CNIL et RGPD de ce guide servent au rédacteur. Elles ne doivent pas apparaître dans le document final, sauf les mentions légales obligatoires (droit de réclamation CNIL, etc.).
