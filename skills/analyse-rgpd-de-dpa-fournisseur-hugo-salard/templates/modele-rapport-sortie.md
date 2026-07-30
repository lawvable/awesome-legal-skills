# Modèle de rapport — Analyse DPA fournisseur

> Format de sortie standard pour l'analyse d'un DPA.
> Ce document définit la structure exacte que le rapport doit suivre.

---

## Structure du rapport

### 1. En-tête

```
ANALYSE DPA — [Nom du fournisseur]
Date de l'analyse : [date]
Analysé par : [Nom du praticien] assisté par IA
Référence DPA : [référence/version du document analysé]
```

### 2. Synthèse exécutive (5 lignes maximum)

Résumé en 3-5 phrases de l'état général du DPA : niveau de conformité global, points critiques principaux (max 3), recommandation d'action (acceptable en l'état / nécessite des modifications / à rejeter).

Exemple :
> Le DPA de [Fournisseur] couvre les clauses obligatoires de l'article 28 RGPD mais présente 3 non-conformités critiques : absence de délai chiffré de notification de violation, autorisation blanket des sous-traitants ultérieurs sans droit d'opposition, et transferts hors UE sans TIA documentée. Le DPA nécessite des modifications substantielles avant signature.

### 3. Tableau d'analyse clause par clause

| # | Clause | Statut | Constat | Remédiation proposée | Priorité |
|---|---|---|---|---|---|
| 1 | Objet et durée | 🟢/🟡/🔴 | Description factuelle | Libellé de modification si 🟡 ou 🔴 | Haute/Moyenne/Basse |
| 2 | Nature et finalité | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |

**Clauses obligatoires (art. 28§3 RGPD) : n° 1 à 13**

| # | Clause | Réf. art. 28§3 |
|---|---|---|
| 1 | Objet et durée | Chapeau |
| 2 | Nature et finalité | Chapeau |
| 3 | Types de données | Chapeau |
| 4 | Catégories de personnes concernées | Chapeau |
| 5 | Instructions documentées | (a) |
| 6 | Confidentialité | (b) |
| 7 | Mesures de sécurité (art. 32) | (c) |
| 8 | Sous-traitants ultérieurs | (d) → §2, §4 |
| 9 | Droits des personnes concernées | (e) |
| 10 | Notification violations / AIPD | (f) → art. 32-36 |
| 11 | Suppression / restitution | (g) |
| 12 | Droit d'audit | (h) |
| 13 | Transferts internationaux | (a) + art. 44-49 |

**Clauses complémentaires (recommandées) : n° 14 à 18**

| # | Clause |
|---|---|
| 14 | Accès gouvernemental pays tiers |
| 15 | Assurance |
| 16 | Responsabilité et indemnisation |
| 17 | Sort des données en cas de défaillance |
| 18 | Vérification Règlement IA |

Pour chaque clause :
- **Statut** : 🟢 Conforme / 🟡 À compléter / 🔴 Non-conforme
- **Constat** : description factuelle de ce que dit le DPA (citer le texte si pertinent entre guillemets avec référence de section)
- **Remédiation proposée** : libellé de clause alternatif prêt à insérer (pour les 🟡 et 🔴 uniquement)
- **Priorité** : Haute (bloquant) / Moyenne (souhaitable) / Basse (amélioration)

**Règle spécifique aux clauses complémentaires (14-18)** : le statut 🔴 est réservé aux situations où l'absence crée un risque juridique concret (ex. : transfert hors UE sans mécanisme, sous-traitant soumis au Cloud Act sans clause d'accès gouvernemental, utilisation d'IA sans aucune mention). Pour une clause complémentaire absente sans risque concret, attribuer 🟡 avec la mention « Clause complémentaire (non obligatoire art. 28 RGPD) — recommandée. »

### 4. Section transferts internationaux (si applicable)

Analyse dédiée si le DPA mentionne des transferts hors UE/EEE.

**4.1 Tableau structuré des transferts (obligatoire si transferts identifiés)**

Présenter les informations transferts en tableau pour faciliter la lecture et le report dans le registre du responsable du traitement.

| Sous-traitant ultérieur | Pays / Organisation | Mécanisme de transfert | TIA réalisée | Mesures supplémentaires | Accès gouvernemental | Lien vers le document |
|---|---|---|---|---|---|---|
| [Nom] | [Pays] | [DPF / CCT 2021 (module) / BCR / Adéquation] | [Oui / Non / Non précisé] | [Liste ou « Aucune »] | [Cloud Act / FISA 702 / Aucun applicable] | [URL ou référence section DPA] |

**Une ligne par sous-traitant ultérieur identifié.** Si la liste n'est pas fournie dans le DPA, indiquer une seule ligne synthétique pour le fournisseur principal avec mention « Liste des sous-traitants ultérieurs non fournie ».

Si aucun transfert hors UE/EEE n'est identifié, **omettre le tableau** et écrire : « Aucun transfert hors UE/EEE identifié dans le DPA. »

**4.2 Analyse complémentaire (prose, si nécessaire)**

Compléter le tableau par 3-5 lignes de prose si des points méritent un développement :
- Cohérence du mécanisme avec la jurisprudence Schrems II
- Risque spécifique lié à un pays de destination (ex. : pays sans cadre de protection robuste)
- Articulation entre le DPA et un éventuel Transfer Impact Assessment du fournisseur
- Recommandation de TIA si non réalisée

**4.3 Accès gouvernemental (focus)**

Si le sous-traitant est soumis à une législation de pays tiers permettant l'accès aux données (Cloud Act US, FISA 702 US, législations équivalentes) :
- Le préciser dans la colonne « Accès gouvernemental » du tableau 4.1
- Détailler en prose les garanties prévues par le DPA (notification, contestation, transparence)
- Référer à la clause 14 du tableau d'analyse clause par clause (clauses complémentaires)

### 5. Section Règlement IA (si applicable)

Analyse dédiée si le sous-traitant utilise ou fournit des systèmes d'IA pour traiter les données :
- Systèmes d'IA identifiés dans le DPA (ou absence d'identification)
- Classification au regard du Règlement (UE) 2024/1689 (si documentée)
- Obligations applicables (art. 26 pour déployeurs haut risque, art. 50 pour transparence, art. 53 pour GPAI)
- Interdiction d'entraînement IA sur les données du responsable (présente ou absente)
- Interaction avec les droits des personnes (art. 22 RGPD — décision individuelle automatisée)

Si aucun système d'IA n'est identifié ou suspecté, indiquer : « Aucune utilisation de systèmes d'IA identifiée dans le DPA. Si le service intègre des fonctionnalités d'IA, recommander au fournisseur de documenter les systèmes utilisés et leur classification au regard du Règlement (UE) 2024/1689. »

### 6. Recommandation globale

En 3 lignes :
- Verdict : Acceptable en l'état / Modifications nécessaires / À rejeter
- Prochaine action recommandée
- Points de vigilance pour la relation contractuelle

### 7. Questions à poser au fournisseur

Liste de 3-5 questions concrètes à envoyer au fournisseur pour clarifier les points ambigus. Chaque question doit être formulée de manière professionnelle et directement utilisable dans un email.

Inclure systématiquement, si pertinent :
- Une question sur l'utilisation de systèmes d'IA dans le traitement des données (si non documentée)
- Une question sur les sous-traitants ultérieurs et leur localisation (si liste incomplète)
- Une question sur l'accès gouvernemental (si sous-traitant soumis au Cloud Act ou législation équivalente)

---

## Règles de présentation

- Le rapport doit être compréhensible par un client non-juriste (direction, DSI, RSSI)
- Les citations du DPA sont entre guillemets avec référence de section
- Les remédiations sont des libellés de clause prêts à insérer (pas des descriptions vagues)
- Le vocabulaire est professionnel mais accessible
- La terminologie RGPD officielle est utilisée (« responsable du traitement », « sous-traitant », « personne concernée », « violation de données à caractère personnel »)
- Longueur cible : 2-5 pages (hors annexes) — la section Règlement IA peut ajouter 0,5-1 page

---

> Version 2026.05.05 — Skill `analyse-dpa-fournisseur-hugo-salard`. Modèle incluant la reclassification des transferts en clause obligatoire (13 obligatoires + 5 complémentaires = 18 clauses), la section Règlement IA et la clause d'accès gouvernemental.
