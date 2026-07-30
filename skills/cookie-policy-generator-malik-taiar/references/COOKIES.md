# Cookies et Traceurs

> Référence : Lignes directrices CNIL (2020) + Directive ePrivacy
> **Documentation** : [CNIL_transparence.pdf](assets/CNIL_transparence.pdf)

## Vue d'ensemble

Les cookies et traceurs sont soumis à des règles spécifiques issues de la directive ePrivacy, complétées par les recommandations de la CNIL. Le consentement est requis pour la plupart des cookies, sauf exceptions.

---

## Cadre réglementaire

### Principe : consentement préalable

Avant de déposer des cookies non essentiels, l'éditeur doit :
1. Informer l'utilisateur de la finalité des cookies
2. Obtenir son consentement
3. Permettre un refus aussi simple que l'acceptation

---

## Catégories de cookies

### 1. Cookies strictement nécessaires (exemptés)

**Définition** : Cookies indispensables au fonctionnement du site, sans lesquels l'utilisateur ne pourrait pas utiliser le service.

**Exemples** :
```
- Cookie de session (maintien de la connexion)
- Cookie de panier d'achat
- Cookie d'authentification
- Cookie de sécurité (CSRF)
- Cookie de préférence de langue
- Cookie de mémorisation du choix cookies (!)
```

**Pas de consentement requis** : Ces cookies peuvent être déposés dès l'arrivée sur le site.

---

### 2. Cookies de mesure d'audience / Analytics

**Définition** : Cookies permettant de mesurer la fréquentation et l'utilisation du site.

**Exemples** :
```
- Google Analytics
- Matomo (ex-Piwik)
- AT Internet
- Adobe Analytics
```

**Consentement** : **Requis**, sauf si :
- Finalité strictement limitée à la mesure d'audience
- Données anonymisées
- Pas de recoupement avec d'autres traitements
- Pas de transfert à des tiers

> **Astuce CNIL** : Matomo configuré en mode exempté peut fonctionner sans consentement.

---

### 3. Cookies de fonctionnalité

**Définition** : Cookies améliorant l'expérience utilisateur sans être strictement nécessaires.

**Exemples** :
```
- Mémorisation des préférences d'affichage
- Personnalisation de l'interface
- Chat en ligne
- Lecteur vidéo intégré
```

**Consentement** : **Requis**

---

### 4. Cookies publicitaires / Marketing

**Définition** : Cookies permettant d'afficher des publicités ciblées ou de mesurer l'efficacité des campagnes.

**Exemples** :
```
- Google Ads / DoubleClick
- Facebook Pixel
- LinkedIn Insight Tag
- Criteo
- Retargeting
```

**Consentement** : **Toujours requis** - Pas d'exception possible

---

### 5. Cookies de réseaux sociaux

**Définition** : Cookies déposés par les boutons de partage ou les intégrations de réseaux sociaux.

**Exemples** :
```
- Boutons "J'aime" Facebook
- Boutons de partage Twitter/LinkedIn
- Vidéos YouTube intégrées
- Instagram embeds
```

**Consentement** : **Requis**

> **Astuce** : Utiliser des boutons de partage en 2 clics (activation puis partage) pour éviter le dépôt automatique.

---

## Bannière de consentement

### Exigences CNIL (2020)

1. **Refus aussi simple que l'acceptation**
   - Bouton "Tout refuser" visible au même niveau que "Tout accepter"
   - Pas de design trompeur (dark patterns)

2. **Information préalable**
   - Finalités des cookies
   - Identité des responsables (ou lien vers la liste)
   - Conséquences du refus

3. **Consentement granulaire**
   - Possibilité d'accepter par catégorie
   - Pas d'acceptation globale par défaut

4. **Pas de cookie wall** (en principe)
   - L'accès au site ne peut pas être conditionné à l'acceptation des cookies
   - Exception : si alternative équitable proposée

5. **Preuve du consentement**
   - Conserver la preuve pendant la durée de validité
   - Pouvoir démontrer : qui, quand, quoi

### Exemple de bannière conforme

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  🍪 Nous utilisons des cookies                                         │
│                                                                         │
│  Nous utilisons des cookies pour améliorer votre expérience,           │
│  analyser notre trafic et à des fins publicitaires.                    │
│                                                                         │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐      │
│  │  Tout accepter   │  │   Tout refuser   │  │   Personnaliser  │      │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘      │
│                                                                         │
│  En savoir plus dans notre Politique de confidentialité                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Durée de vie des cookies

> **LIRE LA SOURCE** : `assets/CNIL_recommandation_cookies_et_traceurs.pdf` + https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies

### Recommandation CNIL : 6 mois (préférable) - 13 mois maximum

| Type | Durée recommandée CNIL | Durée max |
|------|------------------------|-----------|
| **Cookie de consentement** | **6 mois** | 13 mois |
| Cookie analytics | Selon finalité | 13 mois max |
| Cookie publicitaire | Selon finalité | 13 mois max |
| Cookie de session | Durée de la session | - |

> **IMPORTANT** : La CNIL recommande **6 mois** pour le cookie de consentement. Utiliser 6 mois par défaut, sauf justification.

Le consentement doit être renouvelé au-delà de la durée choisie.

---

## Solutions de gestion du consentement (CMP)

| Solution | Avantages | Inconvénients |
|----------|-----------|---------------|
| **Axeptio** | UX soignée, français | Payant |
| **Didomi** | Complet, conforme | Payant, complexe |
| **Cookiebot** | Scan automatique | Peut être lent |
| **OneTrust** | Entreprise, complet | Coûteux |

---

## Liste des cookies - Modèle

Pour la politique de confidentialité, fournir un tableau détaillé :

```
┌───────────────────────────────────────────────────────────────────────────┐
│ COOKIES STRICTEMENT NÉCESSAIRES (pas de consentement requis)              │
├──────────────┬────────────────┬────────────┬─────────────────────────────┤
│ Nom          │ Fournisseur    │ Durée      │ Finalité                    │
├──────────────┼────────────────┼────────────┼─────────────────────────────┤
│ session_id   │ [Entreprise]   │ Session    │ Maintien de la session      │
│ csrf_token   │ [Entreprise]   │ Session    │ Sécurité                    │
│ cookie_consent│ [Entreprise]  │ 6 mois     │ Mémorisation du choix       │
└──────────────┴────────────────┴────────────┴─────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────────┐
│ COOKIES ANALYTICS (consentement requis)                                   │
├──────────────┬────────────────┬────────────┬─────────────────────────────┤
│ Nom          │ Fournisseur    │ Durée      │ Finalité                    │
├──────────────┼────────────────┼────────────┼─────────────────────────────┤
│ _ga          │ Google         │ 2 ans      │ Distinction des visiteurs   │
│ _gid         │ Google         │ 24h        │ Distinction des visiteurs   │
│ _gat         │ Google         │ 1 min      │ Limitation du taux requêtes │
└──────────────┴────────────────┴────────────┴─────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────────┐
│ COOKIES PUBLICITAIRES (consentement requis)                               │
├──────────────┬────────────────┬────────────┬─────────────────────────────┤
│ Nom          │ Fournisseur    │ Durée      │ Finalité                    │
├──────────────┼────────────────┼────────────┼─────────────────────────────┤
│ _fbp         │ Facebook       │ 3 mois     │ Suivi publicitaire          │
│ fr           │ Facebook       │ 3 mois     │ Publicité ciblée            │
│ IDE          │ Google         │ 13 mois    │ Publicité DoubleClick       │
└──────────────┴────────────────┴────────────┴─────────────────────────────┘
```

---

## Formulation pour la politique

```
9. COOKIES ET TRACEURS

9.1 Qu'est-ce qu'un cookie ?

Un cookie est un petit fichier texte déposé sur votre appareil lors de la
visite d'un site web. Il permet de stocker des informations relatives à votre
navigation.

9.2 Les cookies que nous utilisons

COOKIES STRICTEMENT NÉCESSAIRES
Ces cookies sont indispensables au fonctionnement du site. Ils ne peuvent pas
être désactivés.
[Tableau des cookies nécessaires]

COOKIES ANALYTICS
Avec votre consentement, nous utilisons des cookies pour mesurer l'audience
de notre site et améliorer nos services.
[Tableau des cookies analytics]

COOKIES PUBLICITAIRES
Avec votre consentement, nous utilisons des cookies pour vous proposer des
publicités personnalisées.
[Tableau des cookies publicitaires]

9.3 Comment gérer vos préférences ?

Lors de votre première visite, une bannière vous permet de choisir les cookies
que vous acceptez. Vous pouvez modifier vos choix à tout moment en cliquant
sur [lien vers le gestionnaire de cookies].

Vous pouvez également configurer votre navigateur pour refuser les cookies :
- Chrome : [lien]
- Firefox : [lien]
- Safari : [lien]
- Edge : [lien]

9.4 Durée de conservation

Les cookies ont une durée de vie maximale de 13 mois. Au-delà, votre
consentement vous sera à nouveau demandé.
```

---

## Erreurs fréquentes

| Erreur | Sanction possible | Solution |
|--------|-------------------|----------|
| Cookies déposés avant consentement | Amende | Attendre le clic "Accepter" |
| Pas de bouton "Refuser" visible | Amende | Bouton au même niveau que "Accepter" |
| Cookie wall strict | Amende | Proposer une alternative |
| Durée > 13 mois | Mise en demeure | Respecter la durée max |
| Pas de liste des cookies | Non-conformité | Tableau détaillé |
| Dark patterns | Amende | Design neutre et clair |
