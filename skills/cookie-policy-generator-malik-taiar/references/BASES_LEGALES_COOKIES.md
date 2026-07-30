# Bases Légales des Cookies et Traceurs

> Référence : Directive ePrivacy (2002/58/CE) + RGPD (Art. 6) + Lignes directrices CNIL 2020
> **Documentation** : [RGPD_texte_officiel.pdf](assets/RGPD_texte_officiel.pdf), [CNIL_transparence.pdf](assets/CNIL_transparence.pdf)

## Vue d'ensemble

Le dépôt de cookies et traceurs est régi par deux textes complémentaires :
- **Directive ePrivacy** : règle le consentement pour l'accès à l'appareil de l'utilisateur
- **RGPD** : s'applique dès que des données personnelles sont collectées via les cookies

Le principe : **consentement préalable obligatoire**, sauf exceptions limitées.

---

## Principe général : le consentement (Art. 82 Loi Informatique et Libertés)

### Définition

Avant de déposer des cookies non essentiels, l'éditeur doit :
1. **Informer** l'utilisateur de la finalité des cookies
2. **Obtenir son consentement** préalable
3. **Permettre un refus aussi simple que l'acceptation**

### Conditions de validité du consentement (CNIL 2020)

| Critère | Exigence |
|---------|----------|
| **Libre** | Pas de cookie wall strict, alternative proposée |
| **Spécifique** | Par finalité (analytics, pub, réseaux sociaux...) |
| **Éclairé** | Information claire sur les cookies et leurs finalités |
| **Univoque** | Acte positif (clic sur "Accepter"), pas de silence ou pré-cochage |
| **Préalable** | AVANT le dépôt du cookie |

### Ce qui n'est PAS un consentement valide

```
❌ Continuer à naviguer = acceptation
❌ Case pré-cochée
❌ Bannière sans bouton "Refuser"
❌ Bouton "Refuser" caché ou moins visible
❌ "En continuant, vous acceptez..." sans action requise
❌ Cookie wall sans alternative
```

---

## Exception : cookies exemptés de consentement

### Critères d'exemption (Art. 82 al. 2)

Un cookie est exempté de consentement s'il est **strictement nécessaire** :
- À la fourniture du service demandé par l'utilisateur
- OU à la transmission de la communication

### Cookies exemptés

| Type | Exemples | Justification |
|------|----------|---------------|
| **Session** | `session_id`, `PHPSESSID` | Maintien de la connexion |
| **Authentification** | `auth_token`, `jwt` | Identification de l'utilisateur |
| **Panier** | `cart`, `basket` | Mémorisation des achats |
| **Sécurité** | `csrf_token`, `__Host-` | Protection contre les attaques |
| **Préférences utilisateur** | `lang`, `theme` | Personnalisation demandée |
| **Choix cookies** | `cookie_consent` | Mémorisation du consentement |
| **Load balancer** | `SERVERID` | Répartition de charge |

### Cookies NON exemptés (consentement requis)

| Type | Exemples | Pourquoi non exempté |
|------|----------|----------------------|
| **Analytics** | `_ga`, `_gid`, `_gat` | Mesure d'audience ≠ service demandé |
| **Publicité** | `_fbp`, `IDE`, `fr` | Profilage publicitaire |
| **Réseaux sociaux** | Boutons partage, embeds | Suivi cross-site |
| **Personnalisation pub** | Retargeting, remarketing | Finalité commerciale |

---

## Cas particulier : Analytics exempté

### Conditions strictes (CNIL)

Un cookie analytics peut être exempté de consentement SI :

```
✅ Finalité strictement limitée à la mesure d'audience
✅ Données anonymisées (pas d'identifiant utilisateur)
✅ Pas de recoupement avec d'autres traitements
✅ Pas de transfert à des tiers
✅ Durée de vie limitée
✅ Information de l'utilisateur + droit d'opposition
```

### Google Analytics : NON exempté

Google Analytics ne remplit PAS ces conditions car :
- Données transférées à Google (tiers)
- Possibilité de recoupement avec autres services Google
- Identifiants utilisateur persistants

### Matomo : peut être exempté

Matomo (ex-Piwik) peut être configuré en mode exempté :
- Hébergement interne (pas de transfert)
- Anonymisation IP
- Pas de cookies persistants
- Pas de recoupement

---

## Tableau récapitulatif par type de cookie

| Type de cookie | Consentement | Base légale | Notes |
|----------------|--------------|-------------|-------|
| Session | **Non requis** | Exécution contrat | Strictement nécessaire |
| Authentification | **Non requis** | Exécution contrat | Strictement nécessaire |
| Panier | **Non requis** | Exécution contrat | Strictement nécessaire |
| Sécurité | **Non requis** | Obligation légale / Intérêt légitime | Protection du site |
| Préférences | **Non requis** | Exécution contrat | Demandé par l'utilisateur |
| Choix cookies | **Non requis** | Obligation légale | Preuve du consentement |
| Analytics (standard) | **Requis** | Consentement | Ex: Google Analytics |
| Analytics (exempté) | **Non requis** | Intérêt légitime | Ex: Matomo configuré |
| Publicité | **Toujours requis** | Consentement | Pas d'exception |
| Réseaux sociaux | **Requis** | Consentement | Boutons, embeds |
| Fonctionnalité | **Requis** | Consentement | Chat, vidéo, etc. |

---

## Durée de validité du consentement

> **LIRE LA SOURCE** : `assets/CNIL_recommandation_cookies_et_traceurs.pdf` + https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies

### Recommandation CNIL : 6 mois (préférable) - 13 mois maximum

| Élément | Durée recommandée CNIL | Durée max |
|---------|------------------------|-----------|
| **Cookie de consentement** | **6 mois** | 13 mois |
| Validité du consentement | **6 mois** (puis redemander) | 13 mois |
| Cookies déposés | Selon finalité | 13 mois max |

> **IMPORTANT** : La CNIL recommande **6 mois** pour le cookie de consentement. Utiliser 6 mois par défaut.

### Obligations

- **Redemander le consentement** après expiration (6 mois recommandé, 13 mois max)
- **Conserver la preuve** du consentement pendant toute sa durée
- **Permettre le retrait** à tout moment

---

## Preuve du consentement

### Ce qu'il faut conserver

| Élément | Obligatoire |
|---------|-------------|
| Identifiant de l'utilisateur | Oui (anonymisé possible) |
| Date et heure du consentement | Oui |
| Version de la bannière | Oui |
| Choix effectués (par catégorie) | Oui |
| Version de la politique cookies | Recommandé |

### Durée de conservation

La preuve doit être conservée **pendant toute la durée de validité du consentement** (13 mois max).

---

## Sanctions de référence

| Entreprise | Amende | Motif |
|------------|--------|-------|
| Google | 150 M€ | Refus plus difficile que l'acceptation |
| Facebook | 60 M€ | Absence de bouton "tout refuser" |
| Amazon | 35 M€ | Cookies déposés sans consentement |
| Microsoft | 60 M€ | Cookies déposés sans consentement |
| Carrefour | 2,25 M€ | Cookies déposés avant consentement |

---

## Formulation pour la politique cookies

```
## Quels cookies utilisons-nous ?

### Cookies strictement nécessaires

Ces cookies sont indispensables au fonctionnement du site. Ils ne nécessitent
pas votre consentement et ne peuvent pas être désactivés.

[Tableau : Nom | Fournisseur | Durée | Finalité]

### Cookies analytics

Avec votre consentement, nous utilisons des cookies pour mesurer l'audience
de notre site et améliorer nos services.

[Tableau : Nom | Fournisseur | Durée | Finalité]

### Cookies publicitaires

Avec votre consentement, nous utilisons des cookies pour vous proposer des
publicités personnalisées et mesurer l'efficacité de nos campagnes.

[Tableau : Nom | Fournisseur | Durée | Finalité]

### Cookies de réseaux sociaux

Avec votre consentement, ces cookies permettent de partager du contenu sur
les réseaux sociaux et d'afficher des contenus intégrés.

[Tableau : Nom | Fournisseur | Durée | Finalité]
```

---

## Bonnes pratiques

### 1. Bannière conforme

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  Nous utilisons des cookies                                             │
│                                                                         │
│  Nous utilisons des cookies pour améliorer votre expérience,           │
│  analyser notre trafic et à des fins publicitaires.                    │
│                                                                         │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐      │
│  │  Tout accepter   │  │   Tout refuser   │  │   Personnaliser  │      │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2. Refus aussi simple que l'acceptation

- Bouton "Tout refuser" **au même niveau** que "Tout accepter"
- Même taille, même visibilité
- Pas besoin de cliquer sur "Personnaliser" pour refuser

### 3. Pas de dark patterns

```
❌ Bouton "Accepter" en couleur vive, "Refuser" grisé
❌ "Refuser" en petit texte sous la bannière
❌ Pré-sélection de cookies non essentiels
❌ "Continuer sans accepter" au lieu de "Tout refuser"
❌ Message culpabilisant ("Vous allez rater des fonctionnalités...")
```

### 4. Information complète

- Liste exhaustive des cookies avec finalités
- Identité des tiers déposant des cookies
- Durée de chaque cookie
- Lien vers les politiques des tiers

---

## Erreurs fréquentes

| Erreur | Conséquence | Solution |
|--------|-------------|----------|
| Cookies déposés avant consentement | Amende | Attendre le clic explicite |
| Analytics sans consentement | Amende | Consentement ou Matomo exempté |
| Durée > 13 mois | Non-conformité | Respecter 13 mois max |
| Pas de preuve du consentement | Non-conformité | Logger les choix |
| Cookie wall strict | Amende | Alternative payante ou contenu réduit |
| Bouton "Refuser" caché | Amende | Même visibilité que "Accepter" |
