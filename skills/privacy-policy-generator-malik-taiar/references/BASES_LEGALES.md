# Bases Légales du Traitement

> Référence : Article 6 du RGPD
>
> **Documentation** : [RGPD_texte_officiel.pdf](assets/RGPD_texte_officiel.pdf)

## Vue d'ensemble

Pour être licite, tout traitement de données personnelles doit reposer sur l'une des 6 bases légales prévues à l'article 6 du RGPD. Le choix de la base légale doit être fait AVANT de commencer le traitement et doit être documenté.

---

## Les 6 bases légales

### 1. Consentement (Art. 6.1.a)

**Définition** : La personne a donné son accord explicite pour le traitement de ses données pour une ou plusieurs finalités spécifiques.

**Conditions de validité** (Art. 7 RGPD) :
- **Libre** : Pas de déséquilibre de pouvoir, pas de conséquence négative en cas de refus
- **Spécifique** : Pour chaque finalité distincte
- **Éclairé** : Information préalable claire et complète
- **Univoque** : Acte positif clair (pas de case pré-cochée)

**Caractéristiques** :
- Retirable à tout moment
- L'entreprise doit pouvoir prouver le consentement
- Le retrait doit être aussi simple que le don

**Exemples d'utilisation** :
```
- Inscription à une newsletter
- Cookies publicitaires et analytics
- Partage de données avec des partenaires commerciaux
- Profilage à des fins de personnalisation publicitaire
- Transferts de données hors UE (en dernier recours)
```

**Formulation type** :
```
"J'accepte de recevoir des offres commerciales par email de la part de [Entreprise]."
□ Oui

"J'accepte que mes données soient partagées avec les partenaires de [Entreprise]
pour recevoir leurs offres."
□ Oui
```

---

### 2. Exécution du contrat (Art. 6.1.b)

**Définition** : Le traitement est nécessaire à l'exécution d'un contrat auquel la personne est partie, ou à l'exécution de mesures précontractuelles prises à sa demande.

**Conditions** :
- Un contrat existe ou est en cours de négociation
- Le traitement est objectivement nécessaire à son exécution
- Pas d'alternative moins intrusive

**Exemples d'utilisation** :
```
- Livraison d'une commande (nom, adresse, téléphone)
- Création d'un compte client
- Facturation (données de paiement)
- Service après-vente
- Gestion des garanties
- Fourniture d'un service SaaS souscrit
```

**Attention** : La prospection commerciale NE PEUT PAS reposer sur cette base.

**Formulation type** :
```
"Nous traitons vos données d'identification et de livraison pour exécuter
votre commande et vous livrer les produits achetés. Ce traitement est
nécessaire à l'exécution du contrat de vente qui nous lie."
```

---

### 3. Obligation légale (Art. 6.1.c)

**Définition** : Le traitement est nécessaire au respect d'une obligation légale à laquelle le responsable de traitement est soumis.

**Conditions** :
- L'obligation doit être prévue par le droit de l'UE ou national
- L'obligation doit être contraignante
- Le traitement doit être proportionné à l'objectif de l'obligation

**Exemples d'utilisation** :
```
- Conservation des factures (10 ans - Code de commerce)
- Conservation des logs de connexion (1 an - LCEN)
- Communication aux autorités fiscales
- Déclarations sociales (URSSAF, etc.)
- Signalement Tracfin (lutte anti-blanchiment)
- Réponse à une réquisition judiciaire
```

**Formulation type** :
```
"Nous conservons vos factures pendant 10 ans conformément à nos obligations
comptables et fiscales (article L123-22 du Code de commerce)."
```

---

### 4. Sauvegarde des intérêts vitaux (Art. 6.1.d)

**Définition** : Le traitement est nécessaire à la sauvegarde des intérêts vitaux de la personne concernée ou d'une autre personne physique.

**Conditions** :
- Situation d'urgence mettant en jeu la vie de la personne
- À utiliser uniquement si aucune autre base n'est applicable
- Base exceptionnelle

**Exemples d'utilisation** :
```
- Transmission de données médicales aux services d'urgence
- Localisation d'une personne en danger
- Accès aux données en cas de catastrophe naturelle
```

**Remarque** : Cette base est rarement utilisée dans le contexte commercial.

---

### 5. Mission d'intérêt public (Art. 6.1.e)

**Définition** : Le traitement est nécessaire à l'exécution d'une mission d'intérêt public ou relevant de l'exercice de l'autorité publique.

**Conditions** :
- Fondement dans le droit de l'UE ou national
- Généralement réservé aux autorités publiques
- Possibilité d'opposition de la personne concernée

**Exemples d'utilisation** :
```
- Traitements par les administrations publiques
- Recherche scientifique d'intérêt public
- Statistiques publiques (INSEE)
- Santé publique
```

**Remarque** : Peu utilisée par les entreprises privées, sauf exceptions.

---

### 6. Intérêt légitime (Art. 6.1.f)

**Définition** : Le traitement est nécessaire aux fins des intérêts légitimes poursuivis par le responsable de traitement ou par un tiers, sauf si les intérêts ou droits fondamentaux de la personne prévalent.

**Test en 3 étapes** (obligatoire) :
1. **Identification de l'intérêt** : Est-il légitime ? (légal, clair, réel)
2. **Nécessité** : Le traitement est-il vraiment nécessaire ?
3. **Mise en balance** : Les droits des personnes prévalent-ils ?

**Exemples d'utilisation** :
```
- Sécurité du réseau et prévention de la fraude
- Prospection commerciale B2B (avec droit d'opposition)
- Statistiques anonymisées
- Amélioration des services
- Gestion des ressources humaines
- Transferts intra-groupe pour gestion administrative
```

**Attention** :
- Documenter le test de mise en balance
- Mentionner les intérêts légitimes dans la politique
- Garantir un droit d'opposition effectif

**Formulation type** :
```
"Nous traitons vos données de navigation à des fins de statistiques et
d'amélioration de notre site. Ce traitement repose sur notre intérêt légitime
à comprendre l'utilisation de notre plateforme et à l'améliorer. Vous pouvez
vous y opposer à tout moment en nous contactant."
```

---

## Tableau récapitulatif

| Base légale | Caractère | Opposition possible | Exemple typique |
|-------------|-----------|---------------------|-----------------|
| Consentement | Retirable | Oui (retrait) | Newsletter |
| Exécution contrat | Obligatoire | Non | Commande |
| Obligation légale | Obligatoire | Non | Factures 10 ans |
| Intérêts vitaux | Exceptionnel | Non | Urgence médicale |
| Mission publique | Public | Oui | Administration |
| Intérêt légitime | Conditionnel | Oui | Statistiques |

---

## Erreurs fréquentes

| Erreur | Conséquence | Solution |
|--------|-------------|----------|
| Utiliser le consentement pour tout | Consentement non valide | Choisir la base appropriée |
| Prospection sur base "exécution contrat" | Traitement illicite | Consentement ou intérêt légitime |
| Intérêt légitime sans test de balance | Non-conformité | Documenter le test |
| Case pré-cochée pour le consentement | Consentement invalide | Case à cocher par l'utilisateur |
| Pas de base légale définie | Traitement illicite | Définir AVANT le traitement |

---

## Bonnes pratiques

### 1. Documenter le choix

Pour chaque traitement, consigner :
- La base légale retenue
- La justification du choix
- Le test de balance (si intérêt légitime)

### 2. Communiquer clairement

Dans la politique de confidentialité :
- Indiquer la base légale pour chaque finalité
- Si intérêt légitime : préciser l'intérêt poursuivi

### 3. Anticiper le changement

La base légale ne peut pas être changée en cours de route. Si le consentement est retiré, le traitement doit cesser (pas de bascule sur intérêt légitime).

---

## Formulation pour la politique

```
3. POURQUOI ET SUR QUELLE BASE TRAITONS-NOUS VOS DONNÉES ?

| Finalité | Base légale | Explications |
|----------|-------------|--------------|
| Gestion de vos commandes | Exécution du contrat | Nécessaire pour vous livrer |
| Envoi de la newsletter | Votre consentement | Vous pouvez vous désinscrire à tout moment |
| Statistiques de navigation | Notre intérêt légitime | Améliorer notre site. Vous pouvez vous y opposer |
| Conservation des factures | Obligation légale | 10 ans (Code de commerce) |
| Prospection B2B | Notre intérêt légitime | Développer notre activité. Droit d'opposition |
```
