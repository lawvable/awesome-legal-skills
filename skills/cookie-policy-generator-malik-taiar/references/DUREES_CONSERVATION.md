# Durées de Conservation des Données

> Référence : Article 5.1.e du RGPD (limitation de la conservation)
> **Documentation** : [CNIL_durees_conservation.pdf](assets/CNIL_durees_conservation.pdf)

## Principe fondamental

Le RGPD impose que les données personnelles soient conservées pendant une durée **limitée** et **proportionnée** à la finalité du traitement. Au-delà, les données doivent être supprimées ou anonymisées.

> **Article 5.1.e RGPD** : Les données sont « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées »

---

## Les 3 phases de conservation

### 1. Base active

**Définition** : Données accessibles en temps réel pour les besoins opérationnels courants.

**Exemple** : Compte client actif, commande en cours de traitement.

### 2. Archivage intermédiaire

**Définition** : Données non utilisées au quotidien mais conservées pour des besoins administratifs, juridiques ou de preuve.

**Accès restreint** : Seules les personnes habilitées y ont accès.

**Exemple** : Factures d'un client ayant clôturé son compte.

### 3. Archivage définitif (rare)

**Définition** : Conservation pérenne pour des raisons d'intérêt public (archives historiques, recherche scientifique).

**Encadrement** : Conditions strictes, généralement hors contexte commercial.

---

## Tableau des durées de conservation par catégorie

### Données clients / prospects

| Type de données | Durée de conservation | Base légale / Justification |
|-----------------|----------------------|----------------------------|
| **Compte client actif** | Durée de la relation commerciale | Exécution du contrat |
| **Compte client inactif** | 3 ans après dernière activité | Prospection (intérêt légitime) |
| **Prospects (non clients)** | 3 ans après dernier contact | Recommandation CNIL |
| **Données de contact newsletter** | Jusqu'au désabonnement + 3 ans | Preuve du consentement |
| **Historique des commandes** | 5 ans (prescription civile) | Protection juridique |

### Données de paiement / Comptabilité

| Type de données | Durée de conservation | Base légale / Justification |
|-----------------|----------------------|----------------------------|
| **Factures** | 10 ans | Obligation légale (Code de commerce L123-22) |
| **Pièces comptables** | 10 ans | Obligation légale (CGI) |
| **Données de paiement (CB)** | Le temps de la transaction | Sécurité / PCI-DSS |
| **Preuves de transaction** | 5 ans | Prescription civile |
| **Mandats SEPA** | 5 ans après fin du mandat | Recommandation CNIL |

### Données RH / Salariés

| Type de données | Durée de conservation | Base légale / Justification |
|-----------------|----------------------|----------------------------|
| **Dossier du salarié actif** | Durée du contrat | Exécution du contrat |
| **Dossier après départ** | 5 ans | Prescription en droit du travail |
| **Bulletins de paie** | 5 ans (employeur) / 50 ans (Archives) | Obligation légale |
| **Candidatures non retenues** | 2 ans | Recommandation CNIL |
| **Candidatures avec consentement** | Durée du consentement (max 2 ans) | Consentement |

### Données de connexion / Logs

| Type de données | Durée de conservation | Base légale / Justification |
|-----------------|----------------------|----------------------------|
| **Logs de connexion (FAI/hébergeur)** | 1 an | LCEN (obligation légale) |
| **Logs applicatifs (sécurité)** | 6 mois à 1 an | Intérêt légitime (sécurité) |
| **Adresses IP** | 1 an maximum | LCEN |
| **Données de trafic** | 1 an | Obligation légale |

### Cookies et traceurs

> **LIRE LA SOURCE** : `assets/CNIL_recommandation_cookies_et_traceurs.pdf` + https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies

| Type de données | Durée recommandée CNIL | Durée max | Base légale / Justification |
|-----------------|------------------------|-----------|----------------------------|
| **Cookie de consentement** | **6 mois** | 13 mois | Recommandation CNIL |
| **Cookies (autres)** | Selon finalité | 13 mois | Recommandation CNIL |
| **Données analytics** | À réduire | 25 mois (défaut GA) | Paramétrage par défaut à réduire |

> **IMPORTANT** : La CNIL recommande **6 mois** pour le cookie de consentement.

### Données de santé (si applicable)

| Type de données | Durée de conservation | Base légale / Justification |
|-----------------|----------------------|----------------------------|
| **Dossier médical** | 20 ans après dernière consultation | Code de la santé publique |
| **Données de santé au travail** | 40 ans | Médecine du travail |

### Données contractuelles

| Type de données | Durée de conservation | Base légale / Justification |
|-----------------|----------------------|----------------------------|
| **Contrats** | 5 ans après fin du contrat | Prescription civile |
| **Contrats avec consommateurs** | 5 ans | Prescription |
| **Garanties** | Durée de la garantie + 2 ans | Action en justice |
| **Contentieux** | Jusqu'à épuisement des voies de recours | Protection juridique |

### Données de vidéosurveillance

| Type de données | Durée de conservation | Base légale / Justification |
|-----------------|----------------------|----------------------------|
| **Images de vidéosurveillance** | 1 mois maximum | Code de la sécurité intérieure |
| **En cas d'incident** | Durée de la procédure | Preuve |

---

## Obligations légales de conservation

### Textes de référence

| Obligation | Durée | Texte |
|------------|-------|-------|
| Documents comptables | 10 ans | Code de commerce L123-22 |
| Factures | 10 ans | Code général des impôts |
| Logs de connexion | 1 an | LCEN (Art. 6 II) |
| Bulletins de paie | 5 ans | Code du travail |
| Contrats électroniques B2C > 120€ | 10 ans | Code de la consommation |
| Vidéosurveillance | 1 mois | Code de la sécurité intérieure |

---

## Bonnes pratiques

### 1. Définir une politique de conservation

Documenter pour chaque catégorie de données :
- La durée de conservation
- La justification (finalité, obligation légale)
- La procédure d'archivage/suppression

### 2. Automatiser la purge

```
Mettre en place des processus automatiques :
- Alerte avant suppression (si pertinent)
- Suppression automatique à échéance
- Anonymisation en alternative à la suppression
- Journalisation des suppressions
```

### 3. Distinguer les phases

```
BASE ACTIVE (accès courant)
    │
    │ [Fin de la relation]
    ▼
ARCHIVE INTERMÉDIAIRE (accès restreint)
    │
    │ [Fin de la durée légale]
    ▼
SUPPRESSION ou ANONYMISATION
```

### 4. Informer dans la politique

Toujours indiquer les durées de conservation dans la politique de confidentialité, avec une justification compréhensible.

---

## Formulation pour la politique

```
6. COMBIEN DE TEMPS CONSERVONS-NOUS VOS DONNÉES ?

Nous conservons vos données personnelles uniquement le temps nécessaire aux
finalités pour lesquelles elles ont été collectées, ou pour respecter nos
obligations légales.

┌─────────────────────────────────────────────────────────────────────────┐
│ Type de données           │ Durée              │ Justification          │
├───────────────────────────┼────────────────────┼────────────────────────┤
│ Compte client             │ Durée de la        │ Fourniture du service  │
│                           │ relation + 3 ans   │                        │
├───────────────────────────┼────────────────────┼────────────────────────┤
│ Données de commande       │ 5 ans              │ Obligations légales    │
│                           │                    │ et garanties           │
├───────────────────────────┼────────────────────┼────────────────────────┤
│ Factures                  │ 10 ans             │ Obligations comptables │
├───────────────────────────┼────────────────────┼────────────────────────┤
│ Données de newsletter     │ Jusqu'au           │ Votre consentement     │
│                           │ désabonnement      │                        │
├───────────────────────────┼────────────────────┼────────────────────────┤
│ Données de connexion      │ 1 an               │ Obligation légale      │
│                           │                    │ (LCEN)                 │
├───────────────────────────┼────────────────────┼────────────────────────┤
│ Cookies                   │ 13 mois max        │ Recommandation CNIL    │
├───────────────────────────┼────────────────────┼────────────────────────┤
│ Prospects                 │ 3 ans sans         │ Prospection            │
│                           │ interaction        │ commerciale            │
└───────────────────────────┴────────────────────┴────────────────────────┘

À l'issue de ces durées, vos données sont supprimées ou anonymisées de
manière irréversible.
```

---

## Erreurs fréquentes

| Erreur | Conséquence | Solution |
|--------|-------------|----------|
| Pas de durée définie | Non-conformité RGPD | Tableau systématique |
| Conservation illimitée | Sanction CNIL | Purge automatique |
| Même durée pour tout | Disproportionné | Adapter par finalité |
| Pas de distinction actif/archive | Accès non maîtrisé | Phases de conservation |
| Oubli des obligations légales | Problème en cas de contrôle | Conserver les factures 10 ans |
| Suppression sans journalisation | Pas de preuve de conformité | Logs de suppression |

---

## Cas particuliers

### Données anonymisées

Les données véritablement anonymisées (identification impossible, même par recoupement) ne sont plus des données personnelles et peuvent être conservées sans limite.

**Attention** : La pseudonymisation n'est PAS l'anonymisation.

### Droit à l'effacement demandé

Si une personne demande l'effacement :
- Supprimer les données de la base active
- Conserver si obligation légale (factures, logs)
- Informer la personne des données conservées et pourquoi

### Contentieux en cours

En cas de litige, les données pertinentes peuvent être conservées jusqu'à l'issue de la procédure, y compris au-delà de la durée normale.
