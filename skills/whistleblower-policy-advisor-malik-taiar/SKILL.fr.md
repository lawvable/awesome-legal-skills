---
name: politique-lanceur-alerte-malik-taiar
description: Guide pour (a) évaluer la conformité d'un dispositif lanceur d'alerte existant ou (b) rédiger une politique de signalement conforme sur la base d'un template fourni. Couvre la Directive UE 2019/1937, la loi Sapin II modifiée (Waserman 2022), le décret 2022-1284, le référentiel CNIL, les spécificités fonction publique et le devoir de vigilance.
metadata:
  author: Malik Taiar
  license: AGPL-3.0
  version: 2025.12.31
---

# Dispositifs Lanceur d'Alerte - Évaluation & Rédaction

## Vue d'ensemble
Ce Guide peut vous aider pour (a) évaluer la conformité d'un dispositif lanceur d'alerte existant ou (b) rédiger un draft de politique de signalement sur la base d'un template fourni.

## Cadre juridique couvert
- Directive européenne 2019/1937
- Loi Sapin II modifiée (loi Waserman 2022)
- Décret n°2022-1284
- Référentiel CNIL alertes professionnelles

### Deux modes d'utilisation

| Mode | Description | Output |
|------|-------------|--------|
| **A. Évaluation de conformité** | Auditer un dispositif existant | Rapport d'évaluation + plan d'actions |
| **B. Rédaction de politique** | Créer un dispositif sur la base des sources mentionnées | Politique basée sur le template |

### Ce que ce skill fait / ne fait pas

| Ce que ce skill fait | Ce qu'il ne fait pas |
|:---------------------|:---------------------|
| Évalue la conformité d'un dispositif existant | Fournir des conclusions juridiques définitives |
| Rédige une politique de signalement sur la base du template fourni | Garantir l'opposabilité |

**Périmètre** : Dispositifs de signalement interne soumis à la loi Sapin II modifiée et au décret n°2022-1284.

> **Callouts variations** :
> - **Fonction publique** : Articulation avec l'art. 40 CPP
> - **Devoir de vigilance** : Entreprises ≥ 5 000 / 10 000 salariés

## Contenu

```
/
├── SKILL.md
├── LICENSE.txt
├── README.md
├── assets/
    ├── Template_Politique_Lanceur_Alerte.docx ← Template pour le Mode B
    ├── [PDF sources]
└── references/
    ├── TEXTES_LEGAUX.md      ← Citations verbatim des articles de loi
    ├── DECRET_PROCEDURE.md   ← Éléments obligatoires (décret 2022-1284)
    ├── RGPD_CNIL.md          ← Conformité RGPD et référentiel CNIL
    ├── FONCTION_PUBLIQUE.md  ← Spécificités fonction publique + art. 40 CPP
    └── VIGILANCE.md          ← Articulation devoir de vigilance
```

## AVERTISSEMENT

**CECI N'EST PAS UN AVIS JURIDIQUE.** Ce skill est fourni à des fins d'information et d'éducation uniquement. Les lois varient selon les juridictions et les circonstances individuelles, et seul un avocat ou juriste habilité peut fournir un conseil adapté à votre situation spécifique. Il ne constitue en aucun cas un acte ou un avis juridique, il s'agit d'un skill Claude à destination des professionnels du droit. Tous les outputs de ce skill doivent être relus par un professionnel du droit qualifié avant toute utilisation à des fins juridiques.

## Choisir le mode d'utilisation

### Mode A : Évaluation de conformité
**Quand l'utiliser** : Le client dispose déjà d'un dispositif et veut vérifier sa conformité.

→ Aller à la **Section 3** (Inputs) puis **Section 5** (Workflow évaluation)

### Mode B : Rédaction de politique
**Quand l'utiliser** : Le client n'a pas de dispositif ou veut en créer un nouveau.

→ Aller à la **Section 3** (Inputs) puis **Section 13** (Rédaction de politique)

| Template | Format | Usage |
|:---------|:-------|:------|
| `Template_Politique_Lanceur_Alerte.docx` | Word | Modèle de politique de signalement interne |

> **IMPORTANT** : Le template doit être repris **EXACTEMENT** tel que fourni. Seuls les éléments variables doivent être adaptés.

## Inputs à collecter (demander avant d'évaluer)

### A. Contexte organisationnel (obligatoire)
- [ ] Forme juridique et effectif (seuil ≥ 50 salariés/agents ?)
- [ ] Secteur d'activité et statut (droit privé / public / mixte)
- [ ] Existence d'un groupe (mutualisation possible ?)
- [ ] Dispositif existant : date de mise en place, mise à jour post-Waserman ?

### B. Documentation à demander
- [ ] Procédure de signalement interne
- [ ] Supports de communication aux collaborateurs
- [ ] Modèles utilisés (AR, retour d'information, clôture)
- [ ] Fiche de poste / désignation du référent
- [ ] Registre RGPD / AIPD si existante

### C. Contraintes pratiques (recommandé)
- [ ] Mutualisation avec d'autres entités envisagée ?
- [ ] Externalisation du canal de réception ?
- [ ] Articulation avec d'autres dispositifs (devoir de vigilance) ?

## Deliverables - Mode A : Évaluation

### Quick start (output par défaut)

TOUJOURS produire :
1) **Synthèse exécutive** (1 page)
2) **Tableau d'évaluation par phase** (8 phases)
3) **Plan d'actions recommandé**

### A. Synthèse exécutive
- [ ] Conformité globale : Conforme / Partiellement conforme / Non conforme
- [ ] Top 5 des écarts identifiés (classés par priorité)
- [ ] Recommandation : "Conforme" / "À corriger avant mise en service" / "Escalader"

### B. Tableau d'évaluation détaillé

| Phase | Point de contrôle | Conforme | Écart identifié | Priorité | Recommandation |
|-------|-------------------|:--------:|-----------------|:--------:|----------------|
| **1. Assujettissement** | | | | | |
| 1.1 | Seuil d'effectif atteint (≥ 50) | | | | |
| 1.2 | Type d'entité identifié (privé/public/mixte) | | | | |
| 1.3 | Mutualisation conforme si applicable (< 250, décision concordante) | | | | |
| **2. Canal de réception** | | | | | |
| 2.1 | Canal écrit **OU** oral prévu (au choix de l'entité) | | | | |
| 2.2 | *Si oral prévu* : téléphone ou messagerie vocale mentionné | | | | |
| 2.3 | *Si oral prévu* : visio/rencontre physique sur demande (délai 20 j ouvrés) | | | | |
| 2.4 | Transmission de tout type d'élément possible | | | | |
| 2.5 | Accusé de réception écrit sous 7 jours ouvrés | | | | |
| **3. Personnes désignées** | | | | | |
| 3.1 | Désignation formelle pour le recueil | | | | |
| 3.2 | Désignation formelle pour le traitement | | | | |
| 3.3 | Compétence suffisante | | | | |
| 3.4 | Autorité suffisante | | | | |
| 3.5 | Moyens suffisants | | | | |
| 3.6 | Garanties d'impartialité prévues | | | | |
| 3.7 | Si externalisation : obligations du tiers conformes | | | | |
| **4. Vérification / Traitement** | | | | | |
| 4.1 | Critères de recevabilité définis (art. 6 + art. 8 I.A.) | | | | |
| 4.2 | Information de l'auteur si non-recevabilité | | | | |
| 4.3 | Suites aux signalements non conformes précisées | | | | |
| 4.4 | Suites aux signalements anonymes précisées | | | | |
| 4.5 | Retour d'information écrit sous 3 mois | | | | |
| 4.6 | Contenu du retour conforme (mesures + motifs) | | | | |
| 4.7 | Clôture motivée prévue | | | | |
| 4.8 | Information écrite de clôture à l'auteur | | | | |
| **5. Confidentialité** | | | | | |
| 5.1 | Intégrité des informations garantie | | | | |
| 5.2 | Confidentialité de l'identité de l'auteur | | | | |
| 5.3 | Confidentialité des personnes visées | | | | |
| 5.4 | Confidentialité des tiers mentionnés | | | | |
| 5.5 | Accès restreint aux personnes autorisées | | | | |
| 5.6 | Transmission sans délai aux personnes désignées | | | | |
| 5.7 | Si oral : modalités de consignation définies | | | | |
| 5.8 | Droit de vérification/approbation par l'auteur | | | | |
| 5.9 | Durée de conservation limitée | | | | |
| **6. Diffusion / Information** | | | | | |
| 6.1 | Procédure diffusée avec publicité suffisante | | | | |
| 6.2 | Accessibilité permanente aux personnes éligibles | | | | |
| 6.3 | Conditions du statut de lanceur d'alerte | | | | |
| 6.4 | Catégories de personnes éligibles | | | | |
| 6.5 | Modalités de signalement (forme, canaux) | | | | |
| 6.6 | Délais de traitement (7j AR, 3 mois retour) | | | | |
| 6.7 | Garanties de confidentialité | | | | |
| 6.8 | Protections accordées | | | | |
| 6.9 | Information sur les canaux externes | | | | |
| 6.10 | Information RGPD | | | | |
| **7. Conformité RGPD (Réf. CNIL 06/07/2023)** | | | | | |
| 7.1 | Base légale identifiée (obligation légale ou intérêt légitime) | | | | |
| 7.2 | Finalités définies et pas de réutilisation incompatible | | | | |
| 7.3 | Minimisation des données respectée (par phase : recueil, instruction, post-décision) | | | | |
| 7.4 | Signalements anonymes possibles, pas de réidentification | | | | |
| 7.5 | Accédants documentés, habilités, traçabilité des accès | | | | |
| 7.6 | Règles de divulgation respectées (lanceur : consentement / visé : après fondé) | | | | |
| 7.7 | Durées de conservation définies par phase et communiquées | | | | |
| 7.8 | Information des personnes conforme (lanceur à l'AR, visé sous 1 mois) | | | | |
| 7.9 | Droits des personnes garantis (accès, opposition, rectification, limitation) | | | | |
| 7.10 | Mesures de sécurité conformes (17 catégories réf. CNIL) | | | | |
| 7.11 | Registre des traitements mis à jour | | | | |
| 7.12 | AIPD réalisée (recommandé) | | | | |
| **8. Spécificités sectorielles** | | | | | |
| 8.1 | *Fonction publique* : Articulation art. 40 CPP documentée | | | | |
| 8.2 | *Fonction publique* : Référent informé obligations art. 40 | | | | |
| 8.3 | *Vigilance* : Concertation syndicats représentatifs | | | | |
| 8.4 | *Vigilance* : Périmètre étendu (filiales, sous-traitants) | | | | |
| 8.5 | *Vigilance* : Parties prenantes externes éligibles | | | | |
| 8.6 | *Secteurs régulés* : Articulation obligations sectorielles | | | | |

## Workflow évaluation (Mode A)

### Étape 1 — Vérifier l'assujettissement

 > L'ORGANISATION EST-ELLE SOUMISE À L'OBLIGATION ?

- [ ] Personne morale de droit privé ≥ 50 salariés → OUI
- [ ] Personne morale de droit public ≥ 50 agents → OUI
- [ ] Commune ≥ 10 000 habitants → OUI
- [ ] Administration de l'État → OUI
- [ ] Autre → VÉRIFIER la réglementation sectorielle

> **Mutualisation possible** (< 250 salariés/agents) : Cf. Art. 8 I. B. et C. de la loi Sapin II modifiée + Art. 7 II du décret

### Étape 2 — Évaluer la conformité (utiliser les références)

> **IMPORTANT - LECTURE OBLIGATOIRE** : Avant toute évaluation, lire **INTÉGRALEMENT** le fichier `assets/Decret_2022_1284.pdf` (articles 1 à 8 + annexe). Ne pas se fier uniquement aux synthèses - le texte exact du décret fait foi.

Évaluer le dispositif de manière **systématique** en utilisant les références :

| Référence | Ce qu'elle couvre |
|---|---|
| **`assets/Decret_2022_1284.pdf`** | **TOUJOURS LIRE EN PREMIER** - Texte intégral du décret |
| [DECRET_PROCEDURE.md](references/DECRET_PROCEDURE.md) | Synthèse des éléments obligatoires (Art. 4-8 décret) |
| [RGPD_CNIL.md](references/RGPD_CNIL.md) | Conformité RGPD et référentiel CNIL |
| [FONCTION_PUBLIQUE.md](references/FONCTION_PUBLIQUE.md) | Spécificités fonction publique + art. 40 CPP |
| [VIGILANCE.md](references/VIGILANCE.md) | Articulation devoir de vigilance (si applicable) |
| [TEXTES_LEGAUX.md](references/TEXTES_LEGAUX.md) | Citations verbatim pour vérification |

**Méthode d'évaluation** :
1. **Lire le décret 2022-1284 en entier** avant de commencer l'évaluation
2. Vérifier que **tous les éléments obligatoires** sont présents (exhaustivité)
3. Vérifier que chaque clause est **conforme** au cadre légal et réglementaire (pas de contradiction)
4. Utiliser la **checklist Section 6** pour structurer l'évaluation par phase
5. En cas de doute, toujours **revenir au texte exact** du décret

### Étape 3 — Rédiger le rapport

```
STRUCTURE DU RAPPORT :
1. Synthèse exécutive (conformité globale, points forts, axes prioritaires)
2. Contexte et périmètre (organisation, cadre réglementaire, documents analysés)
3. Résultats détaillés (reprendre les 8 phases de la checklist)
4. Tableau de synthèse des écarts
5. Plan d'actions recommandé
6. Annexes (checklist complétée, textes applicables)
```

### Étape 4 — Hiérarchiser les recommandations

| **Priorité** | **Critère** | **Exemple** |
|--------------|-------------|-------------|
| CRITIQUE | Absence de dispositif, non-respect des délais légaux, défaut de confidentialité | Pas d'accusé de réception |
| IMPORTANT | Information insuffisante, référent non identifié, non-conformité RGPD | Risque d'impartialité du responsable traitement |
| À AMÉLIORER | Procédure perfectible, documentation incomplète, formation à renforcer | Supports de diffusion à compléter |

## Checklist d'évaluation (8 phases)

### Phase 1 : Assujettissement

> Cf. Art. 8 I. B. loi Sapin II modifiée + Art. 1 et 2 du décret

- [ ] Organisation soumise à l'obligation (seuil atteint)
- [ ] Type d'entité identifié (privé/public/mixte)
- [ ] Mutualisation le cas échéant conforme (< 250, décision concordante)

### Phase 2 : Canal de réception

> **→ Référence détaillée** : [DECRET_PROCEDURE.md - Section 1](references/DECRET_PROCEDURE.md)

- [ ] Canal écrit OU oral prévu (au choix de l'entité - art. 4 I décret)
- [ ] Si oral prévu : téléphone ou messagerie vocale mentionné
- [ ] Si oral prévu : visio/rencontre physique sur demande (délai 20 j ouvrés)
- [ ] Capacité de transmettre tout type d'élément
- [ ] Accusé de réception écrit sous 7 jours ouvrés prévu

### Phase 3 : Personnes désignées

> **→ Référence détaillée** : [DECRET_PROCEDURE.md - Section 3](references/DECRET_PROCEDURE.md)

- [ ] Désignation formelle dans la procédure (recueil ET traitement)
- [ ] Compétence, autorité et moyens suffisants
- [ ] Garanties d'impartialité prévues
- [ ] Si mutualisation (< 250 salariés) : conditions Art. 7 II respectées
- [ ] Si externalisation : obligations du tiers conformes Art. 7 I

### Phase 4 : Vérification et traitement

> **→ Référence détaillée** : [DECRET_PROCEDURE.md - Section 2](references/DECRET_PROCEDURE.md)

**VÉRIFICATION :**
- [ ] Critères de recevabilité définis (art. 6 et art. 8 I.A.)
- [ ] Information de l'auteur en cas de non-recevabilité prévue
- [ ] Suites aux signalements non conformes précisées
- [ ] Suites aux signalements anonymes précisées

**TRAITEMENT :**
- [ ] Retour d'information écrit sous 3 mois maximum prévu
- [ ] Contenu du retour conforme (mesures envisagées/prises + motifs)
- [ ] Clôture motivée prévue (allégations infondées ou sans objet)
- [ ] Information écrite de clôture à l'auteur prévue

### Phase 5 : Confidentialité

> **→ Référence détaillée** : [DECRET_PROCEDURE.md - Section 4](references/DECRET_PROCEDURE.md)

- [ ] Intégrité et confidentialité des informations garanties
- [ ] Protection de l'identité : auteur, personnes visées, tiers mentionnés
- [ ] Accès interdit aux personnes non autorisées
- [ ] Transmission sans délai aux personnes désignées prévue
- [ ] Si oral : modalités de consignation définies
- [ ] Durée de conservation limitée au strict nécessaire

### Phase 6 : Diffusion et information

> **→ Référence détaillée** : [DECRET_PROCEDURE.md - Section 6](references/DECRET_PROCEDURE.md)

- [ ] Procédure diffusée avec publicité suffisante
- [ ] Accessible de manière permanente aux personnes éligibles
- [ ] Contenu de l'information complet (cf. Section 7 du décret)
- [ ] Information sur les canaux externes disponible

### Phase 7 : Conformité RGPD (Référentiel CNIL 06/07/2023)

> **→ Référence détaillée** : [RGPD_CNIL.md](references/RGPD_CNIL.md)

- [ ] Base légale identifiée (obligation légale ou intérêt légitime)
- [ ] Finalités définies, pas de réutilisation incompatible
- [ ] Minimisation des données par phase (recueil, instruction, post-décision)
- [ ] Signalements anonymes possibles, pas de réidentification
- [ ] Accédants documentés, habilités, traçabilité des accès
- [ ] Règles de divulgation respectées (lanceur: consentement / visé: après fondé)
- [ ] Durées de conservation définies par phase et communiquées
- [ ] Information des personnes conforme (lanceur à l'AR, visé sous 1 mois)
- [ ] Droits des personnes garantis (accès, opposition, rectification, limitation)
- [ ] Mesures de sécurité conformes (17 catégories réf. CNIL)
- [ ] Registre des traitements mis à jour
- [ ] AIPD réalisée (recommandé)

### Phase 8 : Spécificités sectorielles

> **→ Fonction publique** → [FONCTION_PUBLIQUE.md](references/FONCTION_PUBLIQUE.md)

- [ ] Articulation avec l'art. 40 CPP documentée
- [ ] Référent informé de ses obligations art. 40

> **→ Devoir de vigilance** → [VIGILANCE.md](references/VIGILANCE.md)

- [ ] Mécanisme établi en concertation avec les syndicats représentatifs
- [ ] Périmètre étendu (filiales, sous-traitants, fournisseurs)
- [ ] Parties prenantes externes éligibles

> **→ Secteurs régulés** (financier, santé, etc.)

- [ ] Articulation avec les obligations sectorielles documentée

## Les trois canaux de signalement (Art. 8 loi Sapin II)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  CANAL 1 : SIGNALEMENT INTERNE (Art. 8 I)                                    │
│  ─────────────────────────────────────────                                   │
│  QUAND : Utilisable directement, sans condition préalable                    │
│                                                                              │
│  PERSONNES ÉLIGIBLES (Art. 8 I.A. 1° à 5°) :                                 │
│  → Membres du personnel (actuels ou anciens)                                 │
│  → Candidats à l'emploi                                                      │
│  → Actionnaires, associés, titulaires de droits de vote                      │
│  → Membres des organes d'administration, direction, surveillance             │
│  → Collaborateurs extérieurs et occasionnels                                 │
│  → Cocontractants, sous-traitants et leurs organes/personnel                 │
├──────────────────────────────────────────────────────────────────────────────┤
│  CANAL 2 : SIGNALEMENT EXTERNE (Art. 8 II)                                   │
│  ──────────────────────────────────────────                                  │
│  QUAND : Utilisable de deux manières                                         │
│    ✓ SOIT après avoir effectué un signalement interne                        │
│    ✓ SOIT directement (sans passer par l'interne)                            │
│                                                                              │
│  DESTINATAIRES POSSIBLES :                                                   │
│  1° Autorité compétente (liste en annexe du décret n°2022-1284)              │
│  2° Défenseur des droits                                                     │
│  3° Autorité judiciaire (Procureur de la République)                         │
│  4° Institution, organe ou organisme de l'UE compétent                       │
├──────────────────────────────────────────────────────────────────────────────┤
│  CANAL 3 : DIVULGATION PUBLIQUE (Art. 8 III)                                 │
│  ──────────────────────────────────────────────                              │
│  QUAND : Protection accordée uniquement dans les cas suivants                │
│                                                                              │
│  CAS 1 (Art. 8 III 1°) - Inefficacité des signalements :                     │
│    → Après signalement externe (précédé ou non d'un interne)                 │
│    → ET sans mesure appropriée prise à l'expiration du délai                 │
│                                                                              │
│  CAS 2 (Art. 8 III 2°) - Danger grave et imminent                            │
│                                                                              │
│  CAS 3 (Art. 8 III 3°) - Risques liés au signalement externe :               │
│    → Risque de représailles                                                  │
│    → OU impossibilité de remédier efficacement                               │
│                                                                              │
│  CAS DÉROGATOIRE (Art. 8 III avant-dernier alinéa) :                         │
│    → Danger IMMINENT ou MANIFESTE pour l'intérêt général                     │
│                                                                              │
│  ⚠️ EXCLUSION : Les cas 2°, 3° et dérogatoire ne s'appliquent PAS si la      │
│     divulgation porte atteinte à la défense/sécurité nationale               │
└──────────────────────────────────────────────────────────────────────────────┘
```

> **ATTENTION** : Depuis la loi Waserman (2022), le lanceur d'alerte peut **choisir librement** entre le canal interne et le canal externe. Il n'est plus obligé de passer d'abord par l'interne.

## Définition du lanceur d'alerte (Art. 6 loi Sapin II)

**LANCEUR D'ALERTE = Personne physique qui :**
- [ ] Signale ou divulgue SANS CONTREPARTIE FINANCIÈRE DIRECTE
- [ ] De BONNE FOI
- [ ] Des informations portant sur :
    - Un crime ou un délit
    - Une menace ou un préjudice pour l'intérêt général
    - Une violation OU une tentative de dissimulation d'une violation :
         - d'un engagement international
         - du droit de l'Union européenne
         - de la loi ou du règlement

**Exclusions (Art. 6 II)** : Secret de la défense nationale, secret médical, secret des délibérations judiciaires, secret de l'enquête/instruction, secret professionnel de l'avocat.

**Les facilitateurs (Art. 6-1)** : Personne physique ou morale de droit privé à but non lucratif qui aide le lanceur d'alerte.

## Protections du lanceur d'alerte

> **→ Référence détaillée** : [TEXTES_LEGAUX.md - Article 10-1](references/TEXTES_LEGAUX.md)

**Irresponsabilité civile et pénale** (Art. 10-1 I) si motifs raisonnables de croire que le signalement était nécessaire.

**Mesures de représailles interdites** (Art. 10-1 II) : suspension, licenciement, rétrogradation, transfert de fonctions, discrimination, harcèlement, mise sur liste noire, etc.

**Inversion de la charge de la preuve** (Art. 10-1 III) : c'est à l'employeur de prouver que sa décision est justifiée.

**Nullité de plein droit** de tout acte pris en méconnaissance de ces protections.

## Erreurs fréquentes

| **Erreur** | **Risque** | **Correction** |
|------------|------------|----------------|
| Dispositif non mis à jour depuis 2022 | Non-conformité Waserman | Révision complète |
| Exigence de passer par l'interne d'abord | Contraire au libre choix du canal | Supprimer cette obligation |
| Absence d'accusé de réception automatique | Non-respect du délai de 7 jours | Automatiser l'envoi |
| Confidentialité non garantie techniquement | Risque de compromission | Chiffrement, cloisonnement |
| Référent = membre de la direction générale | Conflit d'intérêts potentiel | Désigner un référent indépendant |
| Pas d'information sur les canaux externes | Obligation légale | Compléter l'information |
| Conservation illimitée des données | Non-conformité RGPD | Appliquer les durées CNIL |
| Pas de possibilité de signalement oral | Exigence du décret 2022-1284 | Prévoir un canal oral |

## Sanctions et risques

| **Infraction** | **Sanction** | **Base légale** |
|----------------|--------------|-----------------|
| Entrave au signalement | 1 an prison + 15 000 € amende | Art. 13 loi Sapin II |
| Représailles | 3 ans prison + 45 000 € amende | Art. 225-1 et 225-2 Code pénal |
| Divulgation de l'identité du lanceur | 2 ans prison + 30 000 € amende | Art. 9 loi Sapin II |
| Signalement abusif | 5 ans prison + 45 000 € amende | Art. 226-10 Code pénal |

## Textes de référence

| Texte | Date | Fichier |
|-------|------|---------|
| Directive (UE) 2019/1937 | 23/10/2019 | `assets/Directive_2019_1937.pdf` |
| Loi n°2016-1691 (Sapin II) | 09/12/2016 | `assets/Loi_Sapin_II_consolidee.pdf` |
| Loi n°2022-401 (Waserman) | 21/03/2022 | `assets/Loi_Waserman_2022.pdf` |
| Décret n°2022-1284 | 03/10/2022 | `assets/Decret_2022_1284.pdf` |
| Référentiel CNIL | 24/07/2023 | `assets/Referentiel_CNIL_alertes_professionnelles.pdf` |
| Circulaire fonction publique | 26/06/2024 | `assets/Circulaire_26_juin_2024.pdf` |
| Synthèse DREETS | 17/02/2025 | `assets/DREETS_synthese_2025.pdf` |
| Loi n°2017-399 (Vigilance) | 27/03/2017 | `assets/L225-102-1.pdf` et `assets/L225-102-2.pdf` |
| Directive (UE) 2024/1760 (CS3D) | 13/06/2024 | `assets/Directive_CS3D_2024_1760.pdf` |

## Rédaction de politique (Mode B)

### Template fourni

| Template | Format | Usage |
|:---------|:-------|:------|
| `Template_Politique_Lanceur_Alerte.docx` | Word | Modèle de politique de signalement interne |

> **IMPORTANT** : Le template doit être repris **EXACTEMENT** tel que fourni. Seuls les éléments variables doivent être adaptés à la situation du client. Ne pas reformuler, supprimer ou réorganiser les clauses du template.

### Workflow de rédaction

**ÉTAPE 1 — Collecter les informations client**
- [ ] Forme juridique et effectif
- [ ] Canaux choisis (écrit, oral, les deux)
- [ ] Identité du/des référent(s) désigné(s)
- [ ] Coordonnées du canal de signalement
- [ ] Périmètre des personnes éligibles
- [ ] Articulation avec d'autres dispositifs (devoir de vigilance)

**ÉTAPE 2 — Adapter le template**
- [ ] Ouvrir Template_Politique_Lanceur_Alerte.docx
- [ ] Compléter UNIQUEMENT les éléments variables
- [ ] Ne PAS reformuler les clauses existantes
- [ ] Ne PAS supprimer de sections
- [ ] Ajouter la clause obligatoire sur les canaux externes 

*Exemple de formulation à insérer dans la politique :*
```
Indépendamment du présent dispositif, toute personne peut adresser
directement un signalement externe au Défenseur des droits, à l'autorité
judiciaire, ou à l'autorité compétente selon le domaine concerné. La liste
des autorités externes est fixée par l'annexe du décret n°2022-1284 du
3 octobre 2022, consultable sur :
https://www.legifrance.gouv.fr/loda/id/JORFTEXT000046357368
```
 
**ÉTAPE 3 — Vérifier la conformité**
→ Utiliser [DECRET_PROCEDURE.md](references/DECRET_PROCEDURE.md) et [TEXTES_LEGAUX.md](references/TEXTES_LEGAUX.md) pour vérifier les éléments obligatoires
→ Utiliser [RGPD_CNIL.md](references/RGPD_CNIL.md) pour vérifier la conformité RGPD

**ÉTAPE 4 — Ajouter l'information sur les canaux externes**
(Obligation légale - Art. 8 al. 3 du décret n°2022-1284)

### Finalisation

**ÉTAPE 5 — Validation**
- [ ] Faire relire par la direction
- [ ] Consulter le CSE si applicable (≥ 50 salariés)
- [ ] Si devoir de vigilance : concertation avec syndicats représentatifs

**ÉTAPE 6 — Diffusion**
- [ ] Choisir les supports de diffusion (cf. Section 6 - Phase 6)
- [ ] S'assurer de l'accessibilité permanente
- [ ] Former les référents désignés
