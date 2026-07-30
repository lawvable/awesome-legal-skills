# Grille d'analyse DPA — Article 28 RGPD

> Référence métier pour l'analyse systématique des Data Processing Agreements.
> Sources : RGPD art. 28, lignes directrices EDPB 07/2020 (concepts de responsable du traitement et sous-traitant, v2.1, 20 sept. 2022), lignes directrices EDPB 02/2024 (obligations des responsables du traitement dans la chaîne de sous-traitance, adoptées 7 oct. 2024), recommandations CNIL, CCT 2021 (décision d'exécution 2021/914).

---

## Clauses obligatoires (Article 28§3 RGPD)

### 1. Objet et durée du traitement

**Référence** : Art. 28§3 RGPD (chapeau).

**Ce qu'il faut vérifier** :
- L'objet du traitement est-il décrit avec précision (pas juste « fournir le service ») ?
- La durée est-elle alignée sur la durée du contrat principal ?
- Les conditions de prolongation/renouvellement sont-elles cohérentes ?

**Pièges courants** :
- Durée « indéterminée » sans mécanisme de revue
- Objet trop vague (« traiter les données nécessaires à l'exécution du contrat »)

**Seuil de conformité** :
- 🟢 Objet précis + durée définie + alignement avec le contrat principal
- 🟡 Objet vague mais durée définie, ou inversement
- 🔴 Ni objet précis ni durée définie

---

### 2. Nature et finalité du traitement

**Référence** : Art. 28§3 RGPD (chapeau).

**Ce qu'il faut vérifier** :
- Les opérations de traitement sont-elles listées (collecte, stockage, consultation, extraction, suppression…) ?
- La finalité est-elle spécifique et limitée au service rendu ?
- Y a-t-il une clause interdisant l'utilisation des données à d'autres fins ?
- En cas d'utilisation d'IA par le sous-traitant : l'entraînement de modèles est-il explicitement exclu de la finalité ?

**Pièges courants** :
- Finalité générique (« améliorer nos services ») qui pourrait couvrir de l'entraînement de modèles IA
- Absence de clause d'interdiction d'utilisation à des fins propres
- Clause autorisant l'utilisation de données « agrégées » ou « anonymisées » sans précision des techniques d'anonymisation (risque de pseudonymisation déguisée)

**Seuil de conformité** :
- 🟢 Opérations listées + finalité spécifique + interdiction d'utilisation à d'autres fins (incluant l'entraînement IA)
- 🟡 Finalité spécifique mais opérations non détaillées
- 🔴 Finalité vague OU possibilité d'utilisation à des fins propres du sous-traitant

---

### 3. Types de données à caractère personnel

**Référence** : Art. 28§3 RGPD (chapeau).

**Ce qu'il faut vérifier** :
- Les catégories de données sont-elles listées explicitement ?
- Des données sensibles (art. 9) ou pénales (art. 10) sont-elles concernées ? Si oui, des garanties supplémentaires sont-elles prévues ?
- La liste est-elle cohérente avec l'objet du traitement ?

**Pièges courants** :
- Liste absente (renvoi à une annexe qui n'existe pas)
- Catégories trop larges (« toutes les données fournies par le client »)

**Seuil de conformité** :
- 🟢 Liste explicite et cohérente, données sensibles identifiées si applicables
- 🟡 Liste présente mais incomplète ou trop large
- 🔴 Aucune liste ou renvoi à une annexe manquante

---

### 4. Catégories de personnes concernées

**Référence** : Art. 28§3 RGPD (chapeau).

**Ce qu'il faut vérifier** :
- Les catégories sont-elles identifiées (employés, clients, prospects, mineurs…) ?
- Si des mineurs sont concernés, des garanties spécifiques sont-elles prévues ?

**Pièges courants** :
- Catégories absentes ou « tous les utilisateurs du service »
- Mineurs non identifiés alors que le service peut les concerner

**Seuil de conformité** :
- 🟢 Catégories identifiées et cohérentes avec le service
- 🟡 Catégories trop larges mais présentes
- 🔴 Aucune mention

---

### 5. Instructions documentées du responsable du traitement

**Référence** : Art. 28§3(a) RGPD.

**Ce qu'il faut vérifier** :
- Le sous-traitant s'engage-t-il à ne traiter les données QUE sur instructions documentées ?
- Le DPA constitue-t-il lui-même une instruction ?
- Le sous-traitant informe-t-il le responsable si une instruction constitue une violation ?
- Le mécanisme de transmission d'instructions complémentaires est-il prévu ?
- Les instructions couvrent-elles explicitement les transferts vers un pays tiers ou une organisation internationale (exigence expresse de l'art. 28§3(a)) ?

**Pièges courants** :
- Clause prévoyant le traitement « conformément à la loi applicable » (trop large)
- Pas de mécanisme d'alerte si l'instruction viole le RGPD
- Omission de la mention des transferts internationaux dans le périmètre des instructions

**Seuil de conformité** :
- 🟢 Engagement sur instructions documentées + alerte violation + mécanisme complémentaire + couverture des transferts
- 🟡 Engagement sur instructions mais sans mécanisme d'alerte ou sans mention des transferts
- 🔴 Pas d'engagement ou clause trop permissive

**Note EDPB 02/2024** : les lignes directrices EDPB 02/2024 (§§ 68-82) précisent que l'inclusion de la mention « sauf obligation au titre du droit de l'Union ou du droit d'un État membre » est hautement recommandée mais non strictement obligatoire, le droit impératif s'appliquant de plein droit. En revanche, un renvoi au droit d'un pays tiers dans cette exception serait problématique.

---

### 6. Confidentialité

**Référence** : Art. 28§3(b) RGPD.

**Ce qu'il faut vérifier** :
- Les personnes autorisées à traiter les données sont-elles soumises à une obligation de confidentialité (contractuelle ou légale) ?
- L'obligation couvre-t-elle les sous-traitants ultérieurs ?

**Pièges courants** :
- Confidentialité limitée à la durée du contrat (devrait survivre)
- Pas de mention de la formation du personnel

**Seuil de conformité** :
- 🟢 Obligation de confidentialité légale ou contractuelle + survie post-contrat
- 🟡 Obligation présente mais limitée dans le temps
- 🔴 Aucune clause de confidentialité

---

### 7. Mesures de sécurité (Article 32)

**Référence** : Art. 28§3(c) renvoyant à l'art. 32 RGPD.

**Ce qu'il faut vérifier** :
- Des mesures techniques et organisationnelles appropriées sont-elles décrites ?
- Sont-elles suffisamment spécifiques (pas juste « mesures appropriées ») ?
- Références à des normes ou certifications (ISO 27001, SOC 2 Type II) ?
- Processus de revue et mise à jour des mesures ?

**Pièges courants** :
- Mesures vagues (« le sous-traitant met en œuvre des mesures de sécurité appropriées »)
- Renvoi à une annexe technique qui n'existe pas ou est périmée
- Pas de processus de mise à jour

**Seuil de conformité** :
- 🟢 Mesures détaillées OU certification reconnue + processus de revue
- 🟡 Mesures mentionnées mais vagues, ou certification sans détail des mesures
- 🔴 Aucune mesure décrite ou clause purement déclarative

---

### 8. Sous-traitants ultérieurs

**Référence** : Art. 28§2 et art. 28§3(d) renvoyant au §4 RGPD.

**Ce qu'il faut vérifier** :
- Autorisation préalable requise (spécifique ou générale) ?
- Si autorisation générale : notification des changements AVEC droit d'opposition ?
- Les sous-traitants ultérieurs sont-ils liés par les mêmes obligations ?
- Le sous-traitant reste-t-il responsable des actes de ses sous-traitants ultérieurs ?
- La liste des sous-traitants ultérieurs est-elle accessible ?
- L'identité complète (nom, adresse, contact) de tous les sous-traitants et sous-traitants ultérieurs est-elle disponible à tout moment ?

**Pièges courants** :
- Autorisation générale SANS notification ni droit d'opposition (= non-conforme art. 28§2)
- Liste non tenue à jour ou inaccessible
- Sous-traitants ultérieurs dans des pays sans protection adéquate

**Seuil de conformité** :
- 🟢 Autorisation (spécifique ou générale avec notification + opposition) + liste accessible + obligations transmises + responsabilité maintenue
- 🟡 Autorisation générale avec notification mais sans droit d'opposition clair
- 🔴 Autorisation blanket sans notification NI opposition

**Note EDPB 02/2024** : les lignes directrices EDPB 02/2024 (§§ 83-107) insistent sur l'obligation de vérification continue par le responsable des garanties offertes par l'ensemble des sous-traitants de la chaîne (pas seulement le sous-traitant direct). Le responsable doit disposer à tout moment de l'identité de tous les sous-traitants ultérieurs. Le sous-traitant initial doit communiquer ces informations de manière proactive et les tenir à jour.

---

### 9. Assistance aux droits des personnes concernées

**Référence** : Art. 28§3(e) RGPD.

**Ce qu'il faut vérifier** :
- Le sous-traitant s'engage-t-il à assister le responsable dans la gestion des demandes d'exercice de droits ?
- Les modalités sont-elles précisées (délai, format, coût) ?
- Le sous-traitant transmet-il les demandes reçues directement ?

**Pièges courants** :
- Assistance « dans la mesure du possible » (trop faible)
- Facturation excessive de l'assistance
- Pas de mécanisme de transmission des demandes reçues directement

**Seuil de conformité** :
- 🟢 Engagement ferme + modalités précisées + transmission des demandes directes
- 🟡 Engagement présent mais modalités floues
- 🔴 Pas d'engagement ou assistance conditionnée à un coût prohibitif

---

### 10. Assistance sécurité, notification de violations et AIPD

**Référence** : Art. 28§3(f) renvoyant aux art. 32 à 36 RGPD.

**Ce qu'il faut vérifier** :
- **Notification de violation** : délai de notification au responsable (recommandation contractuelle ≤ 48h pour permettre au responsable de respecter son propre délai de 72h vis-à-vis de l'autorité de contrôle au titre de l'art. 33§1)
- Contenu de la notification (nature de la violation, catégories de données, mesures prises, coordonnées du DPO ou point de contact — cf. art. 33§3)
- **AIPD** : engagement à assister pour les analyses d'impact (art. 35-36)
- **Consultation préalable** : engagement à assister pour les consultations de l'autorité de contrôle (art. 36)

**Pièges courants** :
- Délai de notification > 72h (empêche le responsable de respecter son propre délai)
- Notification « dès que raisonnablement possible » sans délai chiffré
- Pas de contenu minimum défini pour la notification
- Pas de mention de l'AIPD

**Seuil de conformité** :
- 🟢 Délai ≤ 48h + contenu défini + assistance AIPD + assistance consultation
- 🟡 Délai 48-72h OU contenu partiellement défini
- 🔴 Délai > 72h OU pas de délai chiffré OU pas de clause de notification

**Note importante** : l'article 33§2 RGPD n'impose pas de délai chiffré au sous-traitant pour notifier le responsable du traitement. Il exige une notification « dans les meilleurs délais après en avoir pris connaissance ». Le seuil contractuel de 48h est une recommandation de bonne pratique visant à laisser au responsable le temps de respecter son propre délai de 72h (art. 33§1 RGPD) vis-à-vis de l'autorité de contrôle.

---

### 11. Suppression ou restitution des données

**Référence** : Art. 28§3(g) RGPD.

**Ce qu'il faut vérifier** :
- À la fin du contrat : suppression OU restitution au choix du responsable ?
- Délai de suppression après la fin du contrat ?
- Suppression des copies existantes (sauf obligation légale de conservation) ?
- Certification de suppression disponible ?

**Pièges courants** :
- Suppression « dans un délai raisonnable » sans chiffre (viser 30-90 jours max)
- Pas de mention des copies (backups, logs, archives)
- Pas de certification de suppression
- Conservation prolongée « pour obligations légales » sans préciser lesquelles

**Seuil de conformité** :
- 🟢 Choix suppression/restitution + délai ≤ 90 jours + copies incluses + certification disponible
- 🟡 Choix prévu mais délai flou ou copies non mentionnées
- 🔴 Pas de clause de suppression ou délai > 6 mois

---

### 12. Droit d'audit

**Référence** : Art. 28§3(h) RGPD.

**Ce qu'il faut vérifier** :
- Le responsable a-t-il le droit de réaliser des audits et inspections ?
- Les audits par des tiers mandatés sont-ils acceptés ?
- Des rapports d'audit tiers (SOC 2 Type II, ISO 27001) sont-ils proposés comme alternative ?
- Le coût et les modalités pratiques sont-ils définis ?

**Pièges courants** :
- Droit d'audit uniquement via rapports tiers (sans possibilité d'audit direct même pour cause)
- Fréquence d'audit limitée (1x/an) sans exception pour cause légitime
- Coûts d'audit à la charge du responsable sans plafond

**Seuil de conformité** :
- 🟢 Audit direct possible + rapports tiers acceptables en routine + coûts raisonnables
- 🟡 Rapports tiers uniquement mais de qualité (SOC 2 Type II) + audit direct sur cause
- 🔴 Aucun droit d'audit ou rapports uniquement sur demande payante

---

### 13. Transferts internationaux

**Référence** : Art. 28§3(a) RGPD (les instructions documentées couvrent explicitement « les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale »), art. 44 à 49 RGPD.

> **Note de reclassification** : les transferts internationaux étaient traditionnellement traités comme une clause complémentaire. Or, l'article 28§3(a) RGPD inclut explicitement les transferts dans le périmètre obligatoire des instructions documentées. Cette clause est donc **obligatoire** au titre de l'art. 28§3(a) combiné aux art. 44-49 RGPD. Les lignes directrices EDPB 02/2024 confirment cette lecture.

**Ce qu'il faut vérifier** :
- Les pays de traitement sont-ils identifiés ?
- Un mécanisme de transfert valide est-il en place (décision d'adéquation, CCT 2021, BCR) ?
- Si CCT : le bon module est-il sélectionné (C2P, C2C, P2P, P2C) ?
- Une évaluation d'impact du transfert (TIA) a-t-elle été réalisée ?
- Des mesures supplémentaires sont-elles prévues si nécessaire ?
- Si données UK : l'addendum UK (International Data Transfer Agreement ou UK Addendum aux CCT) est-il inclus ?
- Si données suisses : le DPA prend-il en compte la nLPD et la position du PFPDT ?

**Seuil de conformité** :
- 🟢 Pays identifiés + mécanisme valide + TIA si nécessaire + mesures supplémentaires
- 🟡 Mécanisme en place mais TIA absente ou CCT ancienne version
- 🔴 Transfert hors UE sans mécanisme identifié OU CCT périmées (pré-2021)

---

## Clauses complémentaires (non obligatoires art. 28 mais recommandées)

### 14. Accès gouvernemental pays tiers

**Référence** : Recommandations EDPB 01/2020 (mesures supplémentaires, v2.0, 18 juin 2021), CJUE C-311/18 Schrems II, 16 juillet 2020.

**Ce qu'il faut vérifier** :
- Le sous-traitant s'engage-t-il à informer le responsable du traitement en cas de demande d'accès aux données par une autorité gouvernementale d'un pays tiers ?
- Cette notification est-elle prévue « sauf si le droit applicable l'interdit » (et dans ce cas, le sous-traitant s'engage-t-il à contester l'interdiction de notification) ?
- Le sous-traitant s'engage-t-il à évaluer la compatibilité de la demande avec le droit de l'UE avant d'y donner suite ?
- Un mécanisme de transparence est-il prévu (rapport de transparence, notification agrégée) ?

**Pièges courants** :
- Aucune clause sur le sujet alors que le sous-traitant est soumis à des législations de pays tiers permettant l'accès gouvernemental (Cloud Act, FISA 702, législations équivalentes)
- Engagement limité à « informer si la loi le permet » sans engagement de contestation

**Seuil de conformité** :
- 🟢 Notification prévue + engagement de contestation + évaluation compatibilité UE
- 🟡 Notification prévue mais sans engagement de contestation
- 🔴 Aucune clause alors que le sous-traitant est soumis à une législation de pays tiers (Cloud Act, etc.)

---

### 15. Assurance

**Ce qu'il faut vérifier** :
- Le sous-traitant est-il tenu de maintenir une assurance RC Pro / cyber ?
- Les montants minimaux sont-ils définis ?
- Une preuve d'assurance est-elle exigible ?

**Seuil de conformité** :
- 🟢 RC Pro + cyber exigées avec montants définis + attestation exigible
- 🟡 Assurance mentionnée mais montants non définis
- 🔴 Aucune mention (clause complémentaire — 🔴 réservé si volume/sensibilité des données le justifie)

---

### 16. Responsabilité et indemnisation

**Ce qu'il faut vérifier** :
- Le DPA s'articule-t-il avec les clauses de responsabilité du contrat principal ?
- Y a-t-il une clause d'indemnisation en cas de violation par le sous-traitant ?
- Les plafonds de responsabilité sont-ils cohérents entre DPA et contrat ?
- Un carve-out données personnelles est-il prévu pour exclure la responsabilité RGPD du plafond général ?

**Seuil de conformité** :
- 🟢 Articulation claire avec le contrat principal + carve-out données personnelles + indemnisation
- 🟡 Articulation présente mais sans carve-out explicite
- 🔴 Aucune articulation ou plafond manifestement insuffisant au regard du risque

---

### 17. Sort des données en cas de défaillance du sous-traitant

**Référence** : Bonne pratique contractuelle. Cf. recommandations ANSSI sur la continuité d'activité.

**Ce qu'il faut vérifier** :
- Le DPA prévoit-il un mécanisme de récupération des données en cas d'insolvabilité, cessation d'activité, ou changement de contrôle du sous-traitant ?
- Un séquestre ou un tiers de confiance est-il prévu pour garantir l'accès aux données ?
- Le format de restitution est-il spécifié (format structuré, couramment utilisé et lisible par machine) ?

**Pièges courants** :
- Aucune clause sur le sujet alors que le sous-traitant est une startup ou un acteur à risque
- Clause de restitution classique (art. 28§3(g)) insuffisante en cas de liquidation judiciaire

**Seuil de conformité** :
- 🟢 Mécanisme de récupération prévu (séquestre, escrow, etc.) + format spécifié
- 🟡 Clause de restitution standard (art. 28§3(g)) sans mécanisme de défaillance
- 🔴 Aucune clause (clause complémentaire — 🔴 réservé si le risque opérationnel le justifie)

---

### 18. Vérification Règlement IA (Règlement (UE) 2024/1689)

**Référence** : Règlement (UE) 2024/1689, en particulier art. 3(4) (déployeur), art. 26 (obligations des déployeurs de systèmes d'IA à haut risque), art. 50 (obligations de transparence), art. 53 (obligations des fournisseurs de modèles d'IA à usage général).

> **Note** : cette clause est complémentaire au sens de l'art. 28 RGPD, mais devient essentielle dans tout DPA impliquant un sous-traitant qui utilise ou fournit des systèmes d'IA pour traiter les données du responsable du traitement.

**Ce qu'il faut vérifier** :
- Le sous-traitant utilise-t-il des systèmes d'IA pour traiter les données personnelles du responsable ? Si oui, ces systèmes sont-ils identifiés dans le DPA ?
- La classification de ces systèmes au regard du Règlement IA est-elle documentée (risque inacceptable, haut risque, risque limité, risque minimal) ?
- Si le sous-traitant est qualifiable de **déployeur** (art. 3(4)) d'un système d'IA à haut risque : les obligations de l'art. 26 sont-elles reflétées dans le DPA (contrôle humain, journalisation, information des personnes) ?
- Si le sous-traitant est **fournisseur** d'un modèle d'IA à usage général (GPAI) : les obligations de l'art. 53 sont-elles adressées (documentation technique, politique de respect du droit d'auteur, transparence sur les données d'entraînement) ?
- Les obligations de transparence de l'art. 50 sont-elles couvertes si le sous-traitant opère des systèmes interagissant avec des personnes physiques, des systèmes de reconnaissance des émotions, de catégorisation biométrique, ou des systèmes générant des contenus (deepfakes, textes, images) ?
- L'interdiction d'utiliser les données pour entraîner des modèles IA est-elle explicite (cf. point 2 de la présente grille) ?

**Pièges courants** :
- DPA silencieux sur l'utilisation d'IA alors que le sous-traitant est un éditeur SaaS intégrant de l'IA (chatbots, résumé automatique, classification, scoring)
- Finalité « amélioration du service » couvrant potentiellement l'entraînement de modèles sans base légale
- Absence de clause de transparence alors que le service utilise de la prise de décision automatisée (art. 22 RGPD combiné avec art. 26§5 et art. 50 du Règlement IA)

**Seuil de conformité** :
- 🟢 Systèmes IA identifiés + classification documentée + obligations Règlement IA reflétées dans le DPA
- 🟡 Utilisation d'IA mentionnée mais classification et obligations non détaillées
- 🔴 Utilisation d'IA probable ou avérée sans aucune mention dans le DPA (clause complémentaire — 🔴 réservé si le risque le justifie)

---

## Tableau récapitulatif des seuils

### Clauses obligatoires (art. 28§3 RGPD)

| # | Clause | Réf. art. 28§3 | 🟢 Conforme | 🟡 À compléter | 🔴 Non-conforme |
|---|---|---|---|---|---|
| 1 | Objet/durée | Chapeau | Précis + défini | Partiel | Absent/vague |
| 2 | Nature/finalité | Chapeau | Spécifique + interdit IA | Spécifique seul | Vague |
| 3 | Types de données | Chapeau | Liste explicite | Trop large | Absent |
| 4 | Catégories personnes | Chapeau | Identifiées | Trop larges | Absent |
| 5 | Instructions | (a) | Documentées + alerte + transferts | Sans alerte | Absent |
| 6 | Confidentialité | (b) | Obligation + survie | Limitée temps | Absent |
| 7 | Sécurité (art. 32) | (c) | Détaillé ou certifié | Vague | Absent |
| 8 | Sous-traitants | (d) → §2, §4 | Autorisation + notif + oppo | Notif sans oppo | Blanket |
| 9 | Droits personnes | (e) | Engagement ferme | Engagement flou | Absent |
| 10 | Notification violation / AIPD | (f) → art. 32-36 | ≤ 48h + contenu + DPO | 48-72h | > 72h ou absent |
| 11 | Suppression | (g) | Choix + délai + certif | Choix sans délai | Absent |
| 12 | Audit | (h) | Direct + rapports | Rapports seuls | Absent |
| 13 | Transferts internationaux | (a) + art. 44-49 | Mécanisme + TIA | Mécanisme sans TIA | Pas de mécanisme |

### Clauses complémentaires (recommandées)

| # | Clause | 🟢 Conforme | 🟡 À compléter | 🔴 Non-conforme |
|---|---|---|---|---|
| 14 | Accès gouvernemental | Notification + contestation | Notification seule | Absent (si Cloud Act applicable) |
| 15 | Assurance | RC Pro + cyber + montants | Mention sans montants | Absent (si justifié) |
| 16 | Responsabilité | Carve-out DP + indemnisation | Sans carve-out | Absent (si risque élevé) |
| 17 | Défaillance sous-traitant | Séquestre + format | Restitution standard | Absent (si risque opérationnel) |
| 18 | Règlement IA | IA identifiée + classification | IA mentionnée sans détail | Absent (si IA utilisée) |

---

> Version 2026.05.05 — Skill `analyse-dpa-fournisseur-hugo-salard`. Intègre les lignes directrices EDPB 02/2024, la terminologie RGPD officielle (« responsable du traitement »), la reclassification des transferts internationaux en clause obligatoire au titre de l'art. 28§3(a), et les vérifications Règlement (UE) 2024/1689.
