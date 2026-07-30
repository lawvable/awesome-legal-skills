# Clauses de remédiation types — DPA

> Dictionnaire de clauses correctives prêtes à insérer dans un DPA.
> À utiliser quand l'analyse identifie une non-conformité (🟡 ou 🔴).
> Sources : RGPD art. 28, lignes directrices EDPB 07/2020 (v2.1, 20 sept. 2022), lignes directrices EDPB 02/2024 (obligations dans la chaîne de sous-traitance, 7 oct. 2024), recommandations EDPB 01/2020 (mesures supplémentaires post-Schrems II, v2.0, 18 juin 2021), CCT 2021 (décision d'exécution 2021/914), recommandations CNIL.

---

## 1. Notification de violation — Délai

**Problème** : Le DPA ne prévoit pas de délai chiffré ou prévoit un délai > 72h.

**Note juridique** : l'article 33§2 RGPD n'impose pas de délai chiffré au sous-traitant ; il exige une notification « dans les meilleurs délais après en avoir pris connaissance ». Le délai contractuel recommandé ci-dessous vise à permettre au responsable du traitement de respecter son propre délai de 72h vis-à-vis de l'autorité de contrôle (art. 33§1 RGPD).

**Clause type** :
> « Le Sous-traitant notifie le Responsable du traitement de toute violation de données à caractère personnel dans un délai maximum de [24/48] heures après en avoir pris connaissance. Cette notification inclut au minimum : (a) la nature de la violation, (b) les catégories et le nombre approximatif de personnes concernées, (c) les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés, (d) les conséquences probables de la violation, (e) les mesures prises ou proposées pour remédier à la violation, et (f) le nom et les coordonnées du délégué à la protection des données ou, à défaut, d'un autre point de contact. »

---

## 2. Sous-traitants ultérieurs — Notification et opposition

**Problème** : Autorisation générale sans mécanisme de notification ou de droit d'opposition.

**Clause type** :
> « Le Responsable du traitement autorise le Sous-traitant à recourir à des sous-traitants ultérieurs sous réserve du respect des conditions suivantes : (a) Le Sous-traitant informe le Responsable du traitement par écrit de tout projet de modification concernant l'ajout ou le remplacement de sous-traitants ultérieurs, en laissant au Responsable la possibilité d'émettre des objections dans un délai de [30] jours calendaires. (b) En cas d'objection justifiée, les parties se concertent de bonne foi pour trouver une solution. À défaut d'accord dans un délai de [15] jours, le Responsable peut résilier le contrat sans pénalité. (c) Le Sous-traitant impose à ses sous-traitants ultérieurs, par voie contractuelle, les mêmes obligations de protection des données que celles prévues au présent DPA. (d) Le Sous-traitant demeure pleinement responsable devant le Responsable du traitement de l'exécution des obligations de ses sous-traitants ultérieurs. (e) La liste actualisée des sous-traitants ultérieurs, incluant leur identité complète (nom, adresse, personne de contact), est accessible à l'adresse [URL] ou sur demande. Le Sous-traitant tient cette liste à jour de manière proactive et en informe le Responsable du traitement sans délai en cas de modification. »

**Note EDPB 02/2024** : les lignes directrices EDPB 02/2024 exigent que le responsable du traitement dispose à tout moment de l'identité de l'ensemble des sous-traitants de la chaîne (et non pas seulement des sous-traitants directs). La clause (e) ci-dessus reflète cette exigence.

---

## 3. Suppression des données — Délai et certification

**Problème** : Pas de clause de suppression, ou délai non défini, ou copies non mentionnées.

**Clause type** :
> « Au terme de la prestation de traitement, le Sous-traitant, au choix du Responsable du traitement : (a) supprime toutes les données à caractère personnel et toutes les copies existantes, y compris les sauvegardes et archives, dans un délai maximum de [30/60/90] jours, et fournit une attestation écrite de suppression ; ou (b) restitue toutes les données au Responsable du traitement dans un format structuré, couramment utilisé et lisible par machine, dans un délai de [30] jours. La suppression concerne l'ensemble des environnements (production, test, sauvegarde, archives). Seules les copies dont la conservation est imposée par une obligation légale expressément identifiée peuvent être conservées au-delà de ce délai. »

---

## 4. Transferts internationaux — Mécanisme

**Problème** : Transfert hors UE/EEE sans mécanisme identifié ou avec des CCT périmées.

**Clause type** :
> « Tout transfert de données à caractère personnel vers un pays tiers ou une organisation internationale n'est effectué que sur la base de : (a) une décision d'adéquation de la Commission européenne (art. 45 RGPD), ou (b) les Clauses Contractuelles Types adoptées par la Commission européenne le 4 juin 2021 (décision d'exécution 2021/914), module [indiquer le module applicable], ou (c) des Règles d'entreprise contraignantes approuvées (art. 47 RGPD). Le Sous-traitant s'engage à réaliser une évaluation de l'impact du transfert (Transfer Impact Assessment) pour tout transfert fondé sur les CCT vers un pays ne bénéficiant pas d'une décision d'adéquation, et à mettre en œuvre les mesures supplémentaires identifiées comme nécessaires, conformément aux recommandations EDPB 01/2020. »

---

## 5. Mesures de sécurité — Précision

**Problème** : Clause de sécurité vague (« mesures appropriées ») sans détail.

**Clause type** :
> « Le Sous-traitant met en œuvre les mesures techniques et organisationnelles suivantes, conformément à l'article 32 du RGPD : [liste à adapter selon le fournisseur]. Ces mesures comprennent au minimum : (a) le chiffrement des données en transit (TLS 1.2 minimum) et au repos (AES-256 ou équivalent), (b) la gestion des accès basée sur le principe du moindre privilège, (c) la journalisation des accès aux données, (d) les tests de sécurité réguliers (penetration testing annuel minimum), (e) un plan de continuité et de reprise d'activité documenté. Le Sous-traitant maintient une certification [ISO 27001 / SOC 2 Type II] en cours de validité ou s'engage à réaliser un audit de sécurité annuel par un tiers indépendant. Les résultats sont communiqués au Responsable du traitement sur demande. »

---

## 6. Droit d'audit — Accès effectif

**Problème** : Pas de droit d'audit, ou uniquement via rapports tiers sans possibilité d'audit direct.

**Clause type** :
> « Le Sous-traitant met à la disposition du Responsable du traitement toutes les informations nécessaires pour démontrer le respect des obligations prévues au présent DPA et permet la réalisation d'audits, y compris d'inspections, par le Responsable du traitement ou un auditeur mandaté par celui-ci. Les audits sont réalisés avec un préavis raisonnable de [15/30] jours, pendant les heures ouvrables, et dans le respect de la confidentialité des informations du Sous-traitant. Le Sous-traitant peut proposer la communication de rapports d'audit indépendants (SOC 2 Type II, ISO 27001) en alternative aux audits sur site, sauf en cas de motif légitime justifiant un audit direct (incident de sécurité, violation suspectée, demande d'une autorité de contrôle). »

---

## 7. Instructions documentées — Alerte

**Problème** : Pas de mécanisme d'alerte si une instruction du responsable constitue une violation.

**Clause type** :
> « Le Sous-traitant informe immédiatement le Responsable du traitement si, de son avis, une instruction reçue constitue une violation du RGPD ou d'autres dispositions du droit de l'Union ou du droit des États membres relatives à la protection des données. Dans l'attente de la réponse du Responsable du traitement, le Sous-traitant suspend l'exécution de l'instruction concernée. »

---

## 8. Assistance droits des personnes — Engagement ferme

**Problème** : Assistance vague (« dans la mesure du possible ») ou conditionnée à un coût prohibitif.

**Clause type** :
> « Le Sous-traitant aide le Responsable du traitement, par des mesures techniques et organisationnelles appropriées, dans toute la mesure du possible, à s'acquitter de son obligation de donner suite aux demandes d'exercice des droits des personnes concernées (accès, rectification, effacement, portabilité, limitation, opposition). Le Sous-traitant transmet au Responsable du traitement, sans délai et en tout état de cause dans un délai de [48h/5 jours ouvrés], toute demande reçue directement d'une personne concernée, sans y donner suite lui-même sauf instruction contraire du Responsable du traitement. Les coûts de cette assistance sont [inclus dans le prix du service / facturés au coût réel plafonné à X€/demande]. »

---

## 9. Assurance — Couverture cyber/RC professionnelle

**Problème** : Le DPA ne mentionne aucune obligation d'assurance, ou la couverture est insuffisante au regard du volume de données traitées.

**Clause type** :
> « Le Sous-traitant maintient en vigueur pendant toute la durée du contrat et pendant [12/24] mois après son terme : (a) une assurance responsabilité civile professionnelle d'un montant minimum de [X] euros par sinistre, et (b) une assurance couvrant spécifiquement les risques cyber (violation de données, interruption de service, frais de notification) d'un montant minimum de [X] euros par sinistre. Le Sous-traitant fournit au Responsable du traitement, sur demande, une attestation d'assurance en cours de validité. Le Sous-traitant informe le Responsable du traitement de tout changement significatif dans ses couvertures d'assurance dans un délai de [15] jours. »

**Note praticien** : clause complémentaire (non exigée par l'art. 28 RGPD). Le montant de couverture doit être proportionné au volume et à la sensibilité des données traitées.

---

## 10. Limitation de responsabilité — Carve-out données personnelles

**Problème** : Le DPA renvoie à une clause de limitation de responsabilité du contrat principal qui plafonne ou exclut la responsabilité en cas de violation de données personnelles, ou le DPA est silencieux sur ce point.

**Clause type** :
> « Nonobstant toute clause de limitation de responsabilité prévue au contrat principal, la responsabilité du Sous-traitant au titre des violations de ses obligations de protection des données à caractère personnel (y compris, sans limitation, les violations de sécurité, les traitements non autorisés, et le non-respect des instructions du Responsable du traitement) n'est pas plafonnée / est plafonnée à [X] euros ou [X] fois le montant annuel du contrat. Ce carve-out couvre notamment : (a) les amendes administratives imposées au Responsable du traitement du fait d'un manquement imputable au Sous-traitant, (b) les dommages et intérêts versés aux personnes concernées, (c) les frais de notification et de remédiation engagés par le Responsable du traitement. Le Sous-traitant indemnise le Responsable du traitement de tout préjudice résultant du non-respect par le Sous-traitant de ses obligations au titre du présent DPA. »

**Note praticien** : clause complémentaire (non exigée par l'art. 28 RGPD). Le choix entre plafonnement et absence de plafond dépend du rapport de force commercial. À minima, exiger un carve-out explicite pour que la responsabilité données personnelles ne soit pas couverte par un plafond générique trop bas du contrat principal.

---

## 11. Accès gouvernemental pays tiers — Notification et contestation

**Problème** : Le sous-traitant est soumis à une législation de pays tiers permettant l'accès gouvernemental aux données (Cloud Act, FISA 702, législations équivalentes) et le DPA ne prévoit aucun mécanisme de notification ou de contestation.

**Clause type** :
> « Le Sous-traitant s'engage à : (a) notifier le Responsable du traitement dans les meilleurs délais de toute demande juridiquement contraignante émanant d'une autorité publique d'un pays tiers visant l'accès aux données à caractère personnel traitées pour le compte du Responsable du traitement, sauf si une telle notification est interdite par le droit du pays tiers concerné ; (b) dans le cas où la notification serait interdite, contester cette interdiction devant les juridictions compétentes dans la mesure où une base raisonnable existe pour considérer que l'interdiction est illégale au regard du droit applicable ; (c) évaluer, avant de donner suite à la demande, sa compatibilité avec le droit de l'Union européenne, en particulier les articles 44 à 49 du RGPD et la Charte des droits fondamentaux de l'UE ; (d) fournir le minimum de données requis par l'interprétation raisonnable de la demande ; (e) publier un rapport de transparence annuel indiquant le nombre et la nature des demandes reçues, dans la mesure permise par la loi. »

**Note praticien** : clause complémentaire (non exigée par l'art. 28 RGPD). Toutefois, dans le cadre de transferts fondés sur les CCT 2021, les clauses 15 du module 2 (C2P) et du module 3 (P2P) imposent déjà des obligations similaires. Cette clause étend ces garanties à l'ensemble du DPA, y compris en l'absence de transfert formel (ex. : accès à distance depuis un pays tiers par le personnel du sous-traitant). Cf. CJUE, C-311/18, Schrems II, 16 juillet 2020 ; recommandations EDPB 01/2020 (mesures supplémentaires), v2.0, 18 juin 2021.

---

## 12. Sort des données en cas de défaillance du sous-traitant

**Problème** : Le DPA ne prévoit aucun mécanisme de récupération des données en cas d'insolvabilité, de cessation d'activité ou de changement de contrôle du sous-traitant.

**Clause type** :
> « En cas de procédure collective (sauvegarde, redressement, liquidation judiciaire), de cessation d'activité, ou de changement de contrôle du Sous-traitant, celui-ci s'engage à : (a) informer le Responsable du traitement dans les meilleurs délais de la survenance de l'événement ; (b) garantir la restitution de l'ensemble des données à caractère personnel dans un format structuré, couramment utilisé et lisible par machine, dans un délai de [30] jours à compter de la notification ; (c) [le cas échéant] mettre en place un mécanisme de séquestre logiciel (escrow) auprès d'un tiers de confiance permettant au Responsable du traitement d'accéder aux données et, si applicable, au code source nécessaire à leur exploitation, en cas de défaillance du Sous-traitant. Les obligations de protection des données prévues au présent DPA survivent à la défaillance du Sous-traitant et sont opposables à tout cessionnaire, repreneur ou liquidateur. »

**Note praticien** : clause complémentaire (non exigée par l'art. 28 RGPD). Particulièrement pertinente lorsque le sous-traitant est une startup, un acteur récent, ou un prestataire dont la viabilité financière n'est pas assurée. L'opposabilité au liquidateur reste soumise au droit des procédures collectives applicable.

---

## 13. Vérification Règlement IA — Transparence et documentation

**Problème** : Le sous-traitant utilise des systèmes d'IA pour traiter les données personnelles du responsable du traitement (classification, scoring, analyse automatisée, chatbots, résumé automatique…) mais le DPA est silencieux sur cette utilisation.

**Clause type** :
> « Le Sous-traitant déclare et garantit que : (a) les systèmes d'intelligence artificielle utilisés dans le cadre de l'exécution du présent contrat sont identifiés en Annexe [X], avec leur classification au regard du Règlement (UE) 2024/1689 ; (b) pour tout système d'IA à haut risque au sens de l'article 6 du Règlement (UE) 2024/1689, le Sous-traitant respecte les obligations de l'article 26 applicables aux déployeurs, notamment le contrôle humain (art. 26§2), la journalisation automatique (art. 26§5), et l'information des personnes physiques concernées (art. 26§7 combiné avec art. 50) ; (c) les données à caractère personnel traitées pour le compte du Responsable du traitement ne sont en aucun cas utilisées pour l'entraînement, l'ajustement ou l'amélioration de modèles d'IA, sauf instruction écrite préalable et spécifique du Responsable du traitement ; (d) pour tout système d'IA relevant des obligations de transparence de l'article 50 du Règlement (UE) 2024/1689, le Sous-traitant met en œuvre les mesures de transparence requises et en informe le Responsable du traitement. Le Sous-traitant communique au Responsable du traitement, sur demande, la documentation technique pertinente relative aux systèmes d'IA utilisés. »

**Note praticien** : clause complémentaire au sens de l'art. 28 RGPD. Toutefois, au regard de l'art. 2 du Règlement (UE) 2024/1689 et de l'interaction RGPD/IA Act (cf. fiches CNIL IA, avril-juin 2024), l'absence de cette clause dans un DPA impliquant de l'IA constitue une lacune significative. Entrée en application progressive : pratiques interdites (2 février 2025), obligations GPAI (2 août 2025), obligations générales haut risque (2 août 2026).

---

*Ce dictionnaire est évolutif. Le praticien peut ajouter ses propres clauses de remédiation issues de ses retours clients.*

---

> Version 2026.05.05 — Skill `analyse-dpa-fournisseur-hugo-salard`. Intègre la note art. 33§2 (absence de délai chiffré légal pour la notification de violation par le sous-traitant), les références EDPB 02/2024, et les clauses complémentaires (accès gouvernemental, défaillance sous-traitant, Règlement IA).
