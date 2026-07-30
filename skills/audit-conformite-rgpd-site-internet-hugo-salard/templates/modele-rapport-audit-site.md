# Modèle de rapport d'audit RGPD — Site internet

> Template 1/1 — Skill `audit-rgpd-site-internet`
> Format de sortie OBLIGATOIRE pour tout audit produit par ce skill.

---

## Structure du rapport

```
AUDIT DE CONFORMITÉ RGPD — [Nom du site / URL]

Date de l'audit : [Date]
Audité par : [Nom du praticien] assisté par IA
URL principale : [https://...]
Pages auditées : [Nombre + liste des principales URLs]
Outil de navigation utilisé : [Claude in Chrome / Cowork / Mode copier-coller / Autre]

---

SYNTHÈSE EXÉCUTIVE

[3-5 lignes max]
- Niveau de conformité global : Total / Moyen / Faible
- Points critiques principaux : [max 3 points bloquants]
- Verdict : Conforme / Mise en conformité nécessaire / Non conforme

---

TABLEAU 1 — AUDIT DU SITE

[Reproduire les 10 sections de la checklist avec :
Item / Description / Oui-Non-N/A / Observations]

Section 1 — Mentions légales
Section 2 — Informations relatives à l'hébergeur
Section 3 — Formulaires de collecte des données
Section 4 — Newsletter
Section 5 — Politique de confidentialité
Section 6 — Politique cookies et bandeau
Section 7 — Mots de passe (si applicable)
Section 8 — Trackers et mesure d'audience
Section 9 — Sous-traitants détectables et transferts hors UE
Section 10 — Accessibilité du recueil des droits

---

TABLEAU 2 — ANNEXE : ANALYSE DE LA POLITIQUE DE CONFIDENTIALITÉ (Art. 13/14 RGPD)

22 lignes (les 22 items de la checklist) :

| # | Exigence | Existence | Complet | Risque (1/2/3) | Observations |
|---|---|---|---|---|---|

---

POINTS BLOQUANTS

[Liste des items en risque 3 (conformité faible) qui nécessitent une mise en conformité immédiate]

---

POINTS DE VIGILANCE

[Liste des items en risque 2 (conformité moyenne) à améliorer]

---

RECOMMANDATIONS PRIORITAIRES

[3 à 5 actions concrètes à mener par ordre de priorité, formulées comme des actions à confier au client]

1. [Action 1 — formulée à l'impératif]
2. [Action 2]
3. [Action 3]

---

NOTES TECHNIQUES

[Observations factuelles sur la collecte (URLs visitées, captures si disponibles,
sections du site qui n'ont pas pu être auditées et raisons)]

---

Audit réalisé par [Nom du praticien] assisté par IA — [Date]
```

---

## Règles de remplissage

### Synthèse exécutive

- Maximum 5 lignes
- Niveau global :
  - **Total** : 0 ou 1 item en risque 3, max 3 items en risque 2
  - **Moyen** : 2 à 5 items en risque 3, ou plus de 5 items en risque 2
  - **Faible** : 6 items ou plus en risque 3
- Citer les 3 points bloquants principaux (les plus critiques en risque)
- Verdict actionnable :
  - **Conforme** : risque global Total
  - **Mise en conformité nécessaire** : risque global Moyen
  - **Non conforme** : risque global Faible

### Tableau 1 — Audit du site

Reproduire la structure exacte des 10 sections de la checklist (`resources/checklist-audit-site-rgpd.md`). Pour chaque item :
- **Oui** si l'élément est présent et conforme
- **Non** si absent ou non conforme
- **N/A** si non applicable au site (ex : pas de newsletter, pas d'authentification, pas d'e-commerce)
- **Observations** : citation textuelle exacte de l'extrait observé sur le site, ou URL de la page concernée. Si absent, écrire « Non identifié sur le site ».

### Tableau 2 — Annexe politique de confidentialité

Si la politique de confidentialité existe :
- Reproduire les 22 items
- Pour chaque item : Existence Oui/Non, Complet Oui/Non, Risque 1/2/3
- Observations : citation textuelle exacte de la politique pour chaque item

Si la politique n'existe pas : écrire en haut du tableau « Politique de confidentialité absente — annexe non applicable. Risque 3 sur l'ensemble des items art. 13/14. »

### Points bloquants

Liste des items en **Risque 3** uniquement, regroupés par section.

Format :
```
- [Section] : [Item court] — [Constat factuel]
```

Exemples :
```
- Mentions légales : SIRET absent — Aucun numéro SIRET identifié sur la page Mentions légales
- Bandeau cookies : Cookies déposés par défaut — Google Analytics et un pixel publicitaire déposés avant consentement utilisateur
- Politique de confidentialité : Pas de politique distincte — Politique fusionnée avec les CGV (page /cgv-confidentialite)
- Sous-traitants : Mécanisme de transfert non documenté — Stripe et un fournisseur de newsletter US identifiés sans mention DPF ou CCT
```

### Points de vigilance

Liste des items en **Risque 2**, regroupés par section. Même format que les points bloquants.

### Recommandations prioritaires

3 à 5 actions concrètes, formulées à l'impératif, ordonnées par priorité.

Format :
```
1. [Verbe à l'impératif] [objet précis] : [détail si nécessaire]
```

Exemples :
- « Ajouter le numéro de TVA intracommunautaire dans les mentions légales »
- « Reconfigurer le bandeau cookies pour qu'aucun cookie optionnel ne soit déposé avant consentement explicite »
- « Séparer la politique de confidentialité des CGV en créant une page /politique-confidentialite distincte »
- « Vider la case à cocher par défaut sur le formulaire newsletter et adapter la mention de consentement »
- « Compléter les exigences sur les mots de passe pour atteindre 12 caractères + majuscule + chiffre + caractère spécial »

### Notes techniques

Mentionner :
- Date et heure de l'audit
- Outil de navigation utilisé (Claude in Chrome, Cowork, mode copier-coller, autre)
- Nombre total de pages visitées
- URLs des principales pages auditées
- Sections du site qui n'ont pas pu être auditées (page bloquée, navigation impossible, JavaScript requis non chargé) et raisons
- Si l'audit a été partiel (ex : 10 formulaires sur 15 audités), le préciser
- Mention « Données personnelles identifiantes accidentellement publiées » le cas échéant (alerte au praticien sans reproduction des données)

---

## Format de sortie en .docx

Si le praticien demande une sortie en `.docx` :
- Préserver la structure et tous les tableaux
- Utiliser les styles standard Word :
  - Heading 1 : sections principales (Synthèse exécutive, Tableau 1, Tableau 2, Points bloquants, etc.)
  - Heading 2 : sous-sections (Section 1, Section 2, etc.)
- Tableaux markdown → tableaux Word natifs (avec en-têtes formatés, bordures fines, lignes alternées)
- Pied de page : « Audit réalisé par [Nom du praticien] assisté par IA — [Date] »
- En-tête : logo / nom du cabinet du praticien si fourni, sinon vide
- Numérotation des pages en pied de page
- Marges 2,5 cm
- Police : Calibri 11 pour le corps, Calibri 14 gras pour les Heading 1, Calibri 12 gras pour les Heading 2

Le skill peut s'appuyer sur la skill `docx` (si disponible) pour produire la sortie Word.

---

## Exemple complet — Audit fictif

```
AUDIT DE CONFORMITÉ RGPD — Boutique Exemple SAS (https://www.boutique-exemple.fr)

Date de l'audit : 5 mai 2026
Audité par : Le praticien assisté par IA
URL principale : https://www.boutique-exemple.fr
Pages auditées : 12 pages — accueil, mentions légales, politique de confidentialité, CGV, contact, newsletter, créer un compte, panier, paiement, FAQ, à propos, blog (échantillon)
Outil de navigation utilisé : Claude in Chrome

---

SYNTHÈSE EXÉCUTIVE

Niveau de conformité global : MOYEN.
3 points bloquants : (1) bandeau cookies non conforme — boutons accept/refuse de tailles différentes ; (2) politique de confidentialité fusionnée avec CGV ; (3) absence de mention sur les transferts hors UE pour les sous-traitants américains identifiés (paiement et newsletter).
Verdict : Mise en conformité nécessaire avant toute campagne marketing élargie.

---

TABLEAU 1 — AUDIT DU SITE

Section 1 — Mentions légales

| Item | Description | Oui/Non/N/A | Observations |
|---|---|---|---|
| Présence | Page Mentions légales | Oui | https://www.boutique-exemple.fr/mentions-legales |
| Dénomination sociale | Nom de l'entreprise | Oui | « Boutique Exemple SAS » |
| SIRET | Numéro SIRET | Oui | « RCS Paris 123 456 789 » |
| TVA intracommunautaire | Numéro TVA intra | Non | Non identifié sur la page |
| Forme juridique | Forme juridique | Oui | « SAS au capital de 50 000 € » |
| Capital social | Capital | Oui | « 50 000 € » |
| Adresse | Siège social | Oui | « 10 rue de la Boutique, 75001 Paris » |
| Téléphone | Numéro de téléphone | Non | Non identifié sur la page Mentions |
| Directeur de la publication | Nom directeur publication | Oui | « Le directeur général » |
| RCS / RM | Numéro RCS | Oui | « RCS Paris 123 456 789 » |

Section 2 — Hébergeur

| Item | Description | Oui/Non/N/A | Observations |
|---|---|---|---|
| Nom | Nom hébergeur | Oui | « OVH SAS » |
| Raison sociale | Raison sociale | Oui | « OVH SAS » |
| Adresse | Adresse | Oui | « 2 rue Kellermann, 59100 Roubaix » |
| SIRET | SIRET hébergeur | Non | Non mentionné |
| Téléphone | Téléphone hébergeur | Non | Non mentionné |
| Localisation serveurs | Pays | Oui | « France (Roubaix / Strasbourg) » |

Section 6 — Politique cookies et bandeau (extrait significatif)

| Item | Description | Oui/Non/N/A | Observations |
|---|---|---|---|
| Bandeau présent | Bandeau au premier accès | Oui | Bandeau s'affiche dès le chargement |
| Boutons équivalents (CNIL 2020-091) | Accept/refuse même taille et couleur | Non | « Accepter tout » : bouton vert vif large ; « Refuser » : lien gris pâle 50% plus petit |
| Cookies non déposés par défaut | Cookies bloqués avant consentement | Non | Google Analytics et un pixel Meta déposés au chargement (vérifié via outils dev navigateur) |
| Refus aussi simple | Refuser en 1 clic | Non | « Refuser tout » nécessite de cliquer sur « Paramétrer » puis désactiver chaque catégorie |

Section 9 — Sous-traitants détectables (extrait)

| Sous-traitant | Catégorie | Localisation | Mécanisme transfert | Mentionné dans politique ? |
|---|---|---|---|---|
| Stripe | Paiement | US | DPF (présumé) | Non mentionné |
| Fournisseur newsletter US | Newsletter | US | DPF (présumé) | Non mentionné |
| Google Analytics | Mesure d'audience | US | DPF (présumé) | Non mentionné |
| OVH | Hébergement | France | N/A (UE) | Oui |

[... autres sections détaillées de la même manière ...]

---

TABLEAU 2 — ANNEXE : ANALYSE DE LA POLITIQUE DE CONFIDENTIALITÉ

| # | Exigence | Existence | Complet | Risque | Observations |
|---|---|---|---|---|---|
| 1 | Identité du responsable de traitement (art. 13(1)(a)) | Oui | Oui | 1 | « Boutique Exemple SAS » mentionnée |
| 2 | Coordonnées du responsable (art. 13(1)(a)) | Oui | Non | 2 | Email présent (contact@boutique-exemple.fr) mais adresse postale absente de la politique |
| 3 | Coordonnées DPO (art. 13(1)(b)) | Non | N/A | 1 | Pas de DPO désigné — non obligatoire pour l'activité (vérifier seuils) |
| 4 | Finalité du traitement (art. 13(1)(c)) | Oui | Non | 2 | Finalités listées mais finalité de mesure d'audience non mentionnée alors que Google Analytics présent |
| 5 | Base juridique (art. 13(1)(c)) | Oui | Non | 2 | « intérêt légitime » mentionné sans description précise |
| 6 | Intérêts légitimes poursuivis (art. 13(1)(d)) | Non | N/A | 3 | Pas de description des intérêts légitimes alors que la base est invoquée |
| 7 | Destinataires (art. 13(1)(e)) | Oui | Non | 2 | « Nos prestataires » mentionné mais sans liste précise |
| 8 | Transferts hors UE (art. 13(1)(f)) | Non | N/A | 3 | Aucune mention de transferts alors que sous-traitants US identifiés |
[... etc. jusqu'à 22 ...]

---

POINTS BLOQUANTS

- Section 6 — Bandeau cookies : Boutons non équivalents — « Accepter tout » bouton vert vif et large, « Refuser » lien gris pâle 50% plus petit (délibération CNIL 2020-091 non respectée)
- Section 6 — Bandeau cookies : Cookies déposés par défaut — Google Analytics et pixel publicitaire déposés au chargement avant consentement
- Section 5 — Politique de confidentialité : Fusion politique/CGV — Politique intégrée comme section 5 du document CGV, contraire au principe CNIL de séparation
- Section 9 — Transferts hors UE : Sous-traitants US non documentés — Stripe et fournisseur de newsletter US identifiés, aucun mécanisme de transfert (DPF, CCT) mentionné dans la politique

---

POINTS DE VIGILANCE

- Section 1 — Mentions légales : TVA intracommunautaire absente, téléphone absent
- Section 2 — Hébergeur : SIRET et téléphone hébergeur absents
- Section 5 — Politique : adresse postale du responsable absente
- Section 5 — Politique : base « intérêt légitime » non décrite précisément
- Section 4 — Newsletter : case à cocher pré-cochée par défaut sur le formulaire de souscription
- Section 7 — Mots de passe : exigence de 8 caractères seulement, sans complexité (CNIL 2022-100 recommande 12+)
- Section 10 — Recueil des droits : pas d'adresse dédiée privacy@, délai de réponse non annoncé

---

RECOMMANDATIONS PRIORITAIRES

1. Reconfigurer le bandeau cookies pour mettre les boutons « Accepter tout », « Refuser tout » et « Paramétrer » à la même taille, même couleur et même disposition (délibération CNIL 2020-091). Bloquer le dépôt des cookies optionnels avant consentement explicite.
2. Séparer la politique de confidentialité des CGV en créant une page /politique-confidentialite distincte, accessible depuis le footer de chaque page.
3. Compléter la politique de confidentialité avec une section « Transferts hors UE » mentionnant les mécanismes applicables pour chaque sous-traitant US identifié (DPF + CCT 2021), et lister les sous-traitants par catégorie.
4. Vider la case à cocher par défaut sur le formulaire newsletter et reformuler la mention de consentement (finalité, droit de retrait, identité du responsable).
5. Renforcer les exigences de mots de passe à 12 caractères minimum + majuscule + chiffre + caractère spécial (délibération CNIL 2022-100).

---

NOTES TECHNIQUES

Audit réalisé via Cowork + Claude in Chrome le 5 mai 2026, 14h30-16h00.
12 pages visitées (échantillon représentatif du site, navigation principalement automatique avec quelques pages rechargées en mode copier-coller pour les contenus dynamiques).
1 formulaire non audité : page /candidature/cv accessible uniquement via lien direct depuis la page « Nous rejoindre », non identifié dans la navigation principale.
Bandeau cookies vérifié au premier accès et après suppression des cookies du navigateur.
Trackers tiers identifiés via les outils dev navigateur (onglet Réseau) : Google Analytics, Meta Pixel, reCAPTCHA, Google Fonts (CDN), Stripe Checkout.

---

Audit réalisé par Le praticien assisté par IA — 5 mai 2026
```
