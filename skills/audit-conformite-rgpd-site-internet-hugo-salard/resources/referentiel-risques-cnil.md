# Référentiel risques et sources réglementaires — Audit RGPD site internet

> Knowledge file 2/2 — Skill `audit-rgpd-site-internet`
> Sert de base à l'attribution des niveaux de risque (1/2/3) dans l'audit et à la rédaction des constats sourcés.

---

## 1. Échelle de risque

L'audit utilise une échelle à trois niveaux pour la conformité de chaque item.

| Code | Niveau | Description | Action attendue |
|---|---|---|---|
| **1** | Conformité totale | L'item est présent ET complet ET conforme à l'exigence applicable | Aucune action |
| **2** | Conformité moyenne | L'item est présent mais incomplet, vague, ou ne respecte qu'une partie de l'exigence applicable | Mise en conformité recommandée — point de vigilance |
| **3** | Conformité faible | L'item est absent, ou son contenu est contraire à l'exigence applicable, ou crée un risque concret pour les personnes concernées | Mise en conformité immédiate — point bloquant |

### Règles d'attribution

- **Statut au plus défavorable** : si plusieurs sous-items composent une exigence, le risque retenu est celui du sous-item le moins conforme.
- **Cohérence avec le tableau principal** : un item du tableau principal noté « Non » sur une exigence obligatoire ne peut pas avoir un risque < 3 dans l'annexe.
- **Cohérence avec les annexes manquantes** : si une politique référencée (ex : politique cookies) est annoncée mais inaccessible techniquement, l'item est noté en risque 3 minimum.
- **Risque 3 sans risque ≥ 2 ailleurs** : si un seul item est en risque 3 mais qu'il s'agit d'un point critique (cookies déposés sans consentement, politique fusionnée avec CGV, transferts hors UE non documentés vers un sous-traitant US), le niveau global du site reste « Mise en conformité nécessaire ».

---

## 2. Niveau de conformité global

Le niveau global du site est calculé à partir de la répartition des risques.

| Niveau global | Critère quantitatif | Verdict |
|---|---|---|
| **Total** | 0 ou 1 item en risque 3, max 3 items en risque 2 | Conforme |
| **Moyen** | 2 à 5 items en risque 3, OU plus de 5 items en risque 2 | Mise en conformité nécessaire |
| **Faible** | 6 items ou plus en risque 3 | Non conforme |

**Règle de dégradation prioritaire** : indépendamment du compte, certains items en risque 3 dégradent automatiquement le niveau global :

| Item bloquant | Effet sur le niveau global |
|---|---|
| Politique de confidentialité absente | Niveau global ≤ Moyen |
| Cookies optionnels déposés avant consentement | Niveau global ≤ Moyen |
| Boutons accept/refuse non équivalents (CNIL 2020-091) | Niveau global ≤ Moyen |
| Sous-traitant hors UE non documenté avec mécanisme de transfert | Niveau global ≤ Moyen |
| Mentions légales totalement absentes | Niveau global ≤ Moyen |

---

## 3. Sources réglementaires par section

### Section 1 — Mentions légales

| Source | Objet |
|---|---|
| LCEN art. 6-III (loi 2004-575) | Obligation d'identification de l'éditeur d'un service en ligne |
| Décret 2007-1010 | Mentions légales pour les sites professionnels |
| Code de la consommation art. L221-5 | Mentions précontractuelles pour la vente à distance (e-commerce) |
| Loi 78-17 (Informatique et Libertés) art. 32 anciens (abrogés mais repris au RGPD) | Information des personnes concernées |

### Section 2 — Hébergeur

| Source | Objet |
|---|---|
| LCEN art. 6-III alinéa 2 | Obligation de communiquer le nom et les coordonnées de l'hébergeur |

### Section 3 — Formulaires de collecte

| Source | Objet |
|---|---|
| RGPD art. 13 | Information lors de la collecte directe |
| RGPD art. 14 | Information lors de la collecte indirecte |
| RGPD art. 7 | Conditions du consentement |
| RGPD art. 4(11) | Définition du consentement (libre, spécifique, éclairé, univoque) |
| Lignes directrices EDPB 05/2020 | Consentement |

### Section 4 — Newsletter

| Source | Objet |
|---|---|
| RGPD art. 7 + 4(11) | Consentement |
| Code des postes et des communications électroniques art. L34-5 | Prospection commerciale par voie électronique |
| Délibération CNIL n°2020-091 | Lignes directrices cookies et traceurs (s'applique aussi aux mécanismes de consentement plus largement) |
| Position CNIL B2B vs B2C | Prospection vers professionnels possible avec opt-out, vers particuliers nécessite opt-in (sauf clients existants pour produits analogues) |

### Section 5 — Politique de confidentialité

| Source | Objet |
|---|---|
| RGPD art. 12 | Modalités de l'information (transparente, intelligible, accessible) |
| RGPD art. 13 | Information lors de la collecte directe (12 items) |
| RGPD art. 14 | Information lors de la collecte indirecte (10 items dont source des données) |
| Lignes directrices CEPD/EDPB sur la transparence (WP260) | Recommandations sur la rédaction d'une politique |
| Recommandation CNIL — page « Information des personnes » | Bonnes pratiques de rédaction |

### Section 6 — Politique cookies et bandeau

| Source | Objet |
|---|---|
| Loi Informatique et Libertés art. 82 | Recueil du consentement avant dépôt de cookies non essentiels |
| Directive ePrivacy 2002/58/CE art. 5(3) | Cadre européen — consentement préalable |
| Délibération CNIL n°2020-091 (lignes directrices) | Précise les modalités d'obtention du consentement |
| Délibération CNIL n°2020-092 (recommandation) | Modalités pratiques recueil consentement cookies |
| EDPB — Lignes directrices 05/2020 | Consentement |
| Sanction CNIL Google LLC du 31 décembre 2021 | Précédent sur les bandeaux cookies non conformes (refus aussi simple qu'accepter) |

### Section 7 — Mots de passe

| Source | Objet |
|---|---|
| Délibération CNIL n°2022-100 du 21 juillet 2022 | Recommandation relative aux mots de passe |
| Référentiel ANSSI | Bonnes pratiques de sécurité (complémentaire) |

### Section 8 — Trackers et mesure d'audience

| Source | Objet |
|---|---|
| Délibération CNIL n°2020-091 | Cadre général cookies |
| Recommandation CNIL — Mesure d'audience | Critères d'exemption de consentement |
| Décision CNIL du 10 février 2022 (Google Analytics) | Constat de non-conformité GA aux exigences post-Schrems II |
| CJUE C-311/18 (Schrems II) — 16 juillet 2020 | Invalidation du Privacy Shield, exigences sur les transferts US |
| Décision d'exécution UE 2023/1795 (Data Privacy Framework) | Nouveau cadre adéquation US (juillet 2023) |

### Section 9 — Sous-traitants et transferts hors UE

| Source | Objet |
|---|---|
| RGPD art. 28 | Obligations de sous-traitance — DPA |
| RGPD art. 44-49 | Encadrement des transferts internationaux |
| Décision d'exécution 2021/914 | Clauses contractuelles types (CCT 2021) |
| EDPB — Recommandations 01/2020 (v2.0 du 18 juin 2021) | Mesures supplémentaires post-Schrems II |
| EDPB — Lignes directrices 07/2020 (v2.1) | Concepts de responsable et sous-traitant |
| EDPB — Lignes directrices 02/2024 | Obligations des responsables dans la chaîne de sous-traitance |
| Décision d'exécution 2023/1795 | Adéquation Data Privacy Framework (US) |

### Section 10 — Accessibilité du recueil des droits

| Source | Objet |
|---|---|
| RGPD art. 12 | Modalités d'exercice des droits |
| RGPD art. 15-22 | Droits des personnes concernées |
| RGPD art. 77 | Droit d'introduire une réclamation auprès d'une autorité de contrôle |
| Lignes directrices EDPB 01/2022 sur le droit d'accès | Modalités pratiques d'exercice |
| Recommandation CNIL — Identification du demandeur | Proportionnalité des justificatifs demandés |

---

## 4. Critères d'attribution du risque par section

Cette grille aide à attribuer le bon niveau de risque par item lors de l'audit.

### 4.1 Mentions légales et hébergeur

| Constat observé | Risque attribué |
|---|---|
| Page mentions légales absente | 3 (sanctionnable LCEN — peines amende + emprisonnement) |
| Page présente mais SIRET ou dénomination sociale absent | 3 |
| Page présente mais TVA intra ou téléphone absent (autres items présents) | 2 |
| Page présente, tous les items présents | 1 |
| Hébergeur non mentionné | 3 |
| Hébergeur partiellement mentionné (nom seul) | 2 |

### 4.2 Formulaires

| Constat observé | Risque attribué |
|---|---|
| Aucune mention RGPD sur le formulaire ni renvoi à la politique | 3 |
| Renvoi à la politique mais sans rappel des finalités | 2 |
| Mention complète au pied du formulaire | 1 |
| Données sensibles collectées sans consentement explicite | 3 |

### 4.3 Newsletter

| Constat observé | Risque attribué |
|---|---|
| Case à cocher pré-cochée par défaut | 3 |
| Inscription par simple saisie d'email sans case à cocher (consentement non explicite) | 3 |
| Case vide + mention conforme | 1 |
| Mention présente mais imprécise (manque finalité ou droit de retrait) | 2 |

### 4.4 Politique de confidentialité

| Constat observé | Risque attribué |
|---|---|
| Politique absente | 3 sur tous les items de l'annexe |
| Politique fusionnée avec CGV | 3 sur l'item « Page dédiée » et 2 minimum sur l'accessibilité |
| Politique présente mais sans date de mise à jour | 2 |
| Politique complète, à jour, claire | 1 |

### 4.5 Cookies — bandeau et politique

| Constat observé | Risque attribué |
|---|---|
| Bandeau absent | 3 |
| Bandeau présent mais cookies optionnels déposés avant consentement | 3 |
| Bouton « Refuser » absent ou nécessitant des clics supplémentaires | 3 (CNIL 2020-091) |
| Boutons accept/refuse de tailles ou couleurs différentes | 3 (CNIL 2020-091) |
| Bandeau complet et boutons équivalents | 1 |
| Politique cookies absente alors que cookies optionnels utilisés | 3 |
| Politique cookies présente mais incomplète (sous-traitants tiers non identifiés) | 2 |

### 4.6 Mots de passe

| Constat observé | Risque attribué |
|---|---|
| Pas d'exigence minimale (acceptation de tout mot de passe) | 3 |
| Exigence < 8 caractères | 3 |
| Exigence 8-11 caractères | 2 |
| Exigence ≥ 12 caractères avec complexité (CNIL 2022-100) | 1 |
| Mot de passe communiqué en clair par email | 3 |

### 4.7 Trackers et mesure d'audience

| Constat observé | Risque attribué |
|---|---|
| Google Analytics standard utilisé sans consentement | 3 |
| Google Analytics standard utilisé avec consentement valide | 2 (rester vigilant — questionnement CNIL persistant sur transferts US) |
| Mesure d'audience exemption CNIL (configuration conforme) | 1 |
| Trackers tiers non listés dans la politique cookies | 3 |
| Pixel publicitaire (Meta, TikTok) utilisé sans consentement | 3 |

### 4.8 Sous-traitants et transferts

| Constat observé | Risque attribué |
|---|---|
| Sous-traitants détectés non listés dans la politique | 3 |
| Sous-traitant US identifié sans mention DPF / CCT | 3 |
| Mention « DPF » ou « CCT 2021 » sans précision sur l'opérateur | 2 |
| reCAPTCHA / Google Fonts chargés avant consentement | 3 |
| Mention complète : sous-traitant, localisation, mécanisme transfert, finalité | 1 |

### 4.9 Accessibilité du recueil des droits

| Constat observé | Risque attribué |
|---|---|
| Pas de canal dédié pour exercer ses droits | 2 |
| Délai de réponse non annoncé | 2 |
| Demande systématique de pièce d'identité disproportionnée | 3 (sanction CNIL fréquente) |
| Mention CNIL absente | 2 |
| Canal dédié + délai annoncé + identification proportionnée + mention CNIL complète | 1 |

---

## 5. Sanctions et précédents CNIL pertinents

| Précédent | Date | Manquement | Sanction |
|---|---|---|---|
| Google LLC + Google Ireland | 31 décembre 2021 | Bandeau cookies (refus complexe) | 150 M€ + 90 M€ |
| Facebook Ireland | 31 décembre 2021 | Bandeau cookies (refus complexe) | 60 M€ |
| Yahoo EMEA | 27 décembre 2023 | Bandeau cookies + cookies déposés sans consentement | 10 M€ |
| Cdiscount | 23 juillet 2024 | Cookies déposés sans consentement | 5 M€ |
| Amazon France Logistique | 23 décembre 2023 | Vidéosurveillance, mais analogie possible : transparence et information | 32 M€ |
| Doctolib | (Avis CE — janv. 2021) | Cas validé par le Conseil d'État sur l'hébergement de données de santé via AWS Luxembourg | Pas de sanction |

Ces précédents servent de référence pour calibrer la sévérité du constat dans le rapport. Les manquements relatifs au bandeau cookies, au dépôt de cookies sans consentement et à l'absence de mécanisme de transfert valable sont parmi les plus sanctionnés.

---

## 6. Ressources de référence à connaître

| Ressource | URL | Usage |
|---|---|---|
| CNIL — Bandeaux cookies | cnil.fr/cookies-traceurs-que-dit-la-loi | Référence opérationnelle |
| CNIL — Modèle de mentions d'information | cnil.fr/fr/modeles | Modèles à proposer au client |
| CNIL — Information des personnes | cnil.fr/fr/respecter-les-droits-des-personnes/quelles-informations-communiquer | Bonnes pratiques |
| EDPB — Guidelines | edpb.europa.eu/our-work-tools/general-guidance | Lignes directrices européennes |
| Service-Public — Mentions légales | service-public.fr/professionnels-entreprises/vosdroits/F31228 | Référentiel mentions légales |
| EDPS — Website Evidence Collector | github.com/EU-EDPS/website-evidence-collector | Outil open source |

Ces ressources sont citables dans le rapport pour appuyer les recommandations.
