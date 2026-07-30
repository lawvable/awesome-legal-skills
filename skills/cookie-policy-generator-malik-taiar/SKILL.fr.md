---
name: politique-cookies-malik-taiar
description: Guide pour la rédaction de politiques cookies conformes au RGPD et à la directive ePrivacy. Contient les recommandations CNIL 2020, un template de référence et les bonnes pratiques. À utiliser lors de la rédaction ou révision d'une politique cookies pour un site web ou une application.
metadata:
  author: Malik Taiar
  license: AGPL-3.0
  version: 2025.12.24
---

# Guide des Politiques Cookies

## Vue d'ensemble

La politique cookies informe les utilisateurs sur les cookies et traceurs déposés sur leur appareil. Elle est distincte de la politique de confidentialité mais peut y être intégrée. Elle doit respecter les lignes directrices CNIL de 2020.

### Objectifs de la politique cookies

| Objectif | Exigence |
|----------|----------|
| **Transparence** | Informer sur les cookies utilisés et leurs finalités |
| **Consentement** | Obtenir un consentement libre, éclairé et préalable |
| **Contrôle** | Permettre à l'utilisateur de gérer ses préférences |
| **Conformité** | Respecter RGPD + ePrivacy + recommandations CNIL |

---

## Ressources de référence

### Template

| Template | Description |
|----------|-------------|
| `assets/sample_template_politique_cookies.docx` | Template par défaut à utiliser si aucun modèle privé n'est fourni |
| Template interne fourni par l'avocat | À utiliser si l'avocat dispose d'un modèle privé plus adapté |

### Documentation CNIL

| Fichier PDF à LIRE (tool Read) | URL à CONSULTER (tool WebFetch) | Sujet |
|--------------------------------|---------------------------------|-------|
| `assets/CNIL_lignes_directrices_cookies_et_traceurs.pdf` | - | Lignes directrices cookies |
| `assets/CNIL_recommandation_cookies_et_traceurs.pdf` | https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies | Recommandation cookies |
| `assets/CNIL_faq_cookies_et_traceurs.pdf` | https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/FAQ | FAQ cookies |
| `assets/CNIL_evolution_regles_utilisation_cookies.pdf` | https://www.cnil.fr/fr/evolution-des-regles-dutilisation-des-cookies-quels-changements-pour-les-internautes | Évolution des règles |
| `assets/CNIL_transparence.pdf` | - | Guide sur l'information et la transparence |
| `assets/CNIL_principes_rgpd.pdf` | - | Les principes fondamentaux du RGPD |
| `assets/RGPD_texte_officiel.pdf` | - | Texte intégral du Règlement UE 2016/679 |

> **OBLIGATION** : Pour TOUTE information concernant les cookies, le consentement, les durées de conservation, les exemptions ou les bonnes pratiques :
> 1. **LIRE les fichiers PDF** avec le tool Read AVANT de répondre sur un point réglementaire
> 2. **CONSULTER les URLs en ligne** avec WebFetch pour vérifier les informations les plus récentes
> 3. **CITER l'URL CNIL** dans ta réponse quand tu mentionnes une règle ou une durée
> 4. **NE JAMAIS inventer** une durée ou une règle sans l'avoir vérifiée dans les sources

### Fiches de connaissance

| Document | Contenu |
|----------|---------|
| **[COOKIES.md](references/COOKIES.md)** | Catégories de cookies, bannières, sanctions CNIL, durées |
| **[BASES_LEGALES_COOKIES.md](references/BASES_LEGALES_COOKIES.md)** | Bases légales spécifiques aux cookies (consentement, exemptions) |
| **[DROITS_PERSONNES.md](references/DROITS_PERSONNES.md)** | Droits des personnes concernées |
| **[DUREES_CONSERVATION.md](references/DUREES_CONSERVATION.md)** | Durées de conservation (6 mois recommandé CNIL pour consentement, 13 mois max) |

---

## Informations à collecter auprès du client

> **IMPORTANT** : Avant de rédiger la politique, collecter les informations ci-dessous.

### 1. Informations sur l'éditeur du site

- [ ] Dénomination sociale complète
- [ ] Forme juridique (SAS, SARL, etc.)
- [ ] Adresse du siège social
- [ ] Email de contact
- [ ] URL du site web

### 2. Cookies utilisés

COOKIES STRICTEMENT NÉCESSAIRES (exemptés de consentement)
- [ ] Cookie de session
- [ ] Cookie d'authentification
- [ ] Cookie de panier
- [ ] Cookie de sécurité (CSRF)
- [ ] Cookie de préférence de langue
- [ ] Cookie de mémorisation du choix cookies

COOKIES ANALYTICS
- [ ] Google Analytics
- [ ] Matomo
- [ ] AT Internet
- [ ] Autre : ___________

COOKIES PUBLICITAIRES / MARKETING
- [ ] Google Ads
- [ ] Facebook Pixel
- [ ] LinkedIn Insight Tag
- [ ] Criteo
- [ ] Autre : ___________

COOKIES RÉSEAUX SOCIAUX
- [ ] Boutons de partage Facebook
- [ ] Boutons de partage Twitter/X
- [ ] Boutons de partage LinkedIn
- [ ] Vidéos YouTube intégrées
- [ ] Autre : ___________

COOKIES DE FONCTIONNALITÉ
- [ ] Chat en ligne (ex: Intercom, Crisp)
- [ ] Lecteur vidéo
- [ ] Personnalisation interface
- [ ] Autre : ___________

### 3. Solution de gestion du consentement (CMP)

- [ ] Aucune
- [ ] Axeptio
- [ ] Didomi
- [ ] Cookiebot
- [ ] OneTrust
- [ ] Autre : ___________

### 4. Durées de conservation

> **LIRE LA SOURCE CNIL** : `assets/CNIL_recommandation_cookies_et_traceurs.pdf` + https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies
> **IMPORTANT** : La CNIL recommande **6 mois** pour le cookie de consentement. Utiliser 6 mois par défaut.

| Cookie | Durée recommandée CNIL | Durée max |
|--------|------------------------|-----------|
| Cookie de consentement | 6 mois | 13 mois |
| Cookies analytics | Selon finalité | 13 mois |
| Cookies publicitaires | Selon finalité | 13 mois |

---

## Workflow de rédaction

### Étape 1 : Sélection du template (OBLIGATOIRE)

> **NE JAMAIS RÉDIGER UNE POLITIQUE DE ZÉRO.**
> Il est indispensable de toujours partir d'un template donné pour la rédaction, soit :
> - le template par défaut dans `assets/sample_template_politique_cookies.docx` ;
> - un autre modèle interne fourni par l'utilisateur.
>
> Ce template est ta référence de base. Tu dois :
> - **Reproduire fidèlement la structure et la rédaction du template**
> - **Garder les formulations exactes du template** (elles sont validées)
> - **Uniquement remplacer les placeholders** par les informations du client
> - **Ne PAS réécrire les phrases** même si tu penses pouvoir mieux formuler
> - **Ne PAS ajouter de sections** qui ne sont pas dans le template
>
> Les informations collectées (cookies utilisés, CMP, etc.) servent à **remplir** le template, **pas à le réécrire**.

**1. PREMIÈRE ACTION : Confirmer le template à utiliser AVANT toute rédaction. Demander à l'utilisateur :**
```
"Je vais rédiger la politique de confidentialité en partant du template fourni par défaut. Disposez-vous d'un template interne plus adapté sur lequel vous souhaiteriez partir ?"
```

| Option | Action |
|--------|--------|
| Template par défaut | Utiliser `assets/sample_template_politique_cookies.docx` |
| Template interne | Utiliser le document fourni par l'avocat |

**2. Considérez le choix de l'utilisateur et sélectionnez le template de départ.**

---

### Étape 2 : Comprendre le site et les cookies utilisés

> **OBJECTIF PRINCIPAL** : Identifier précisément tous les cookies déposés par le site.

**1. Demander à l'avocat les éléments dont il dispose :**
```
"Pour rédiger une politique cookies parfaitement adaptée, merci de me transmettre :
- L'URL du site web
- La liste des cookies utilisés (si connue)
- La solution de gestion du consentement (CMP) utilisée
- Les outils tiers intégrés (analytics, publicité, réseaux sociaux...)
- Tout document existant sur les cookies du site

Vous pouvez transmettre ces informations de manière anonymisée si nécessaire pour des raisons de confidentialité.

Plus vous fournissez d'informations, plus la politique sera adaptée. Sinon, nous ferons nos propres recherches mais elles seront limitées aux informations publiquement accessibles."
```

**2. Recherches sur le site (si accessible) :**
- Visiter le site et observer la bannière cookies
- Identifier la CMP utilisée
- Lister les cookies visibles (via les outils navigateur)
- Noter les intégrations tierces (YouTube, réseaux sociaux, analytics...)
- Lire la politique cookies existante (si présente)

**3. Synthèse avant rédaction :**
```
SITE : [URL]
CMP UTILISÉE : [Nom de la solution]
COOKIES STRICTEMENT NÉCESSAIRES : [Liste]
COOKIES ANALYTICS : [Liste + fournisseurs]
COOKIES PUBLICITAIRES : [Liste + fournisseurs]
COOKIES RÉSEAUX SOCIAUX : [Liste + fournisseurs]
COOKIES FONCTIONNALITÉ : [Liste]
DURÉES : [Conformes aux 13 mois max ?]
POINTS CLÉS AVOCAT : [Ce qui doit absolument figurer]
```

> Une fois la synthèse prête → Passer à la rédaction du Draft 1.

---

### Étape 3 : Rédaction du Draft 1

> **RÈGLE ABSOLUE** : Le template de référence est ta base validée.
>
> - **PARTIR du template** : structure, formulations, ton → c'est ta référence
> - **ADAPTER au cas client** : intégrer les cookies spécifiques identifiés
> - **NE PAS tout réécrire** : garde la rédaction du template, adapte uniquement ce qui doit l'être
>
> En résumé : Template + cookies du client = Draft 1. Pas une réécriture complète.

Compléter le template section par section :

1. **Qu'est-ce qu'un cookie ?** (définition)
2. **Qui dépose les cookies ?** (éditeur + tiers)
3. **Cookies strictement nécessaires** (tableau détaillé)
4. **Cookies analytics** (tableau + finalités)
5. **Cookies publicitaires** (tableau + finalités)
6. **Cookies réseaux sociaux** (tableau + finalités)
7. **Comment gérer vos préférences ?** (bannière + navigateur)
8. **Durée de conservation**
9. **Mise à jour de la politique**
10. **Contact**

> **Vérification conformité immédiate :** Avant de présenter le Draft 1, vérifier la checklist des mentions de conformité cookies (CNIL 2020) :
> - [ ] Liste exhaustive des cookies avec nom, fournisseur, durée, finalité
> - [ ] Distinction cookies nécessaires vs cookies soumis au consentement
> - [ ] Information sur le refus aussi simple que l'acceptation
> - [ ] Durées de conservation ≤ 13 mois
> - [ ] Explication claire du fonctionnement de la bannière
> - [ ] Instructions pour gérer les cookies via le navigateur
> - [ ] Lien vers la CMP pour modifier les préférences
> - [ ] Date de mise à jour du document
> - [ ] Contact pour questions
>
> Si Draft 1 conforme → Passer à l'étape 3.

---

### Étape 4 : Livraison Draft 1 + Benchmark + Propositions d'amélioration

**1. Livrer le Draft 1 avec explication :**
```
"Voici le Draft 1 de la politique cookies.

**Ce que j'ai pris en compte :**
- [Liste des cookies identifiés]
- [CMP utilisée]
- [Durées de conservation]

**Conformité :** Le document respecte les lignes directrices CNIL 2020."
```

**2. Présenter le benchmark (systématique) :**

Rechercher 3-5 politiques cookies d'entreprises du même secteur, puis présenter :
```
"**Benchmark réalisé :**

J'ai analysé les politiques cookies de :
- [Entreprise 1] - [ce qu'on a noté]
- [Entreprise 2] - [ce qu'on a noté]
- [Entreprise 3] - [ce qu'on a noté]

**Améliorations possibles identifiées :**
- [Amélioration 1] : [explication]
- [Amélioration 2] : [explication]

Souhaitez-vous intégrer ces éléments au Draft fourni ?"
```

**3. Si l'avocat valide des améliorations → Produire le Draft 2**

---

### Étape 5 : Vérification finale

Dernière relecture avant livraison définitive :

- [ ] Tous les cookies du site sont listés
- [ ] Distinction nécessaires / soumis au consentement respectée
- [ ] Durées ≤ 13 mois
- [ ] Instructions de gestion claires (bannière + navigateur)
- [ ] Pas de références internes dans le document final
- [ ] Date de mise à jour présente

---

## Sanctions CNIL de référence

| Entreprise | Montant | Motif |
|------------|---------|-------|
| Google | 150 M€ | Refus des cookies plus difficile que l'acceptation |
| Facebook | 60 M€ | Absence de bouton "tout refuser" visible |
| Amazon | 35 M€ | Cookies déposés sans consentement préalable |
| Microsoft | 60 M€ | Cookies déposés sans consentement |

> Ces sanctions illustrent l'importance d'une politique cookies conforme et d'une bannière respectant le principe du refus aussi simple que l'acceptation.

---

## Erreurs fréquentes à éviter

| Erreur | Sanction possible | Solution |
|--------|-------------------|----------|
| Cookies déposés avant consentement | Amende | Attendre le clic "Accepter" |
| Pas de bouton "Refuser" visible | Amende | Bouton au même niveau que "Accepter" |
| Cookie wall strict | Amende | Proposer une alternative |
| Durée > 13 mois | Mise en demeure | Respecter la durée max |
| Pas de liste des cookies | Non-conformité | Tableau détaillé obligatoire |
| Dark patterns | Amende | Design neutre et clair |
| Liste de cookies incomplète | Non-conformité | Audit complet du site |

---

## Utilisation de ce guide

1. **Étape 1 - Choisir le template** : Template de référence par défaut, ou template interne de l'avocat
2. **Étape 2 - Identifier les cookies** : Collecter les infos avocat + analyse du site
3. **Étape 3 - Rédiger le Draft 1** : Compléter le template + vérification conformité
4. **Étape 4 - Livrer + Benchmark** : Présenter le Draft 1 + benchmark systématique + propositions d'amélioration
5. **Étape 5 - Finaliser** : Intégrer les améliorations validées + vérification finale

> **RAPPEL TEMPLATE** : Ne jamais rédiger depuis zéro. Toujours partir du template de référence et l'adapter.
> **RAPPEL DURÉE** : La CNIL recommande **6 mois** pour le cookie de consentement (13 mois max). Toujours vérifier dans les sources CNIL avant de mentionner une durée.
