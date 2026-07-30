# Fiche matière — DROIT FISCAL

## Structure type du sujet (modèle session 2025)

**2 dossiers indépendants de 10 points chacun**, l'un en fiscalité des entreprises (TVA en 2025), l'autre en fiscalité des personnes (impôt sur le revenu).

- **Dossier I (10 points)** : une société (forme, lieu, activité, régime d'imposition précisés) et une **série d'opérations lettrées (a à f)** dont il faut déterminer le traitement fiscal, avec **calcul final demandé** : « Monsieur X vous demande, en rappelant les règles applicables, le montant de TVA dont la société sera redevable au titre du mois de [mois] compte tenu de ces opérations (« a » à « f »). » Les opérations couvrent typiquement : livraison à soi-même/prélèvement, indemnité d'assurance (hors champ), prestations de services et exigibilité (option pour les débits), importation (autoliquidation), livraison interne (fait générateur/exigibilité), exportation ou prestation sur biens à l'étranger (territorialité).
- **Dossier II (10 points)** : un couple (régime matrimonial précisé — il peut être un piège : séparation de biens n'empêche pas l'imposition commune), revenus de catégories variées : traitements et salaires (frais réels vs 10 %), revenus fonciers (charges déductibles, intérêts d'emprunt — capital exclu —, CSG déductible), pensions alimentaires (plafond enfant majeur), réductions/dons, BNC (recettes encaissées, créances acquises, année de rattachement), et une **question de doctrine administrative ou de théorie** (acte anormal de gestion en BNC : applicable ? renvoi à la jurisprudence CE sur l'inapplicabilité partielle aux BNC / liberté de fixer ses honoraires).

Questions finales : « Le couple souhaite savoir quel(s) va(vont) être leur(s) revenu(s) net(s) imposable(s) pour [année]. » + « Elle vous demande de confirmer ou infirmer ce risque. »

## Documents autorisés (page de garde, à reproduire)

```
• Code fiscal (incluant le code des impositions sur les biens et les services et Livre des
  procédures fiscales) : Francis Lefebvre
• Code général des impôts : Dalloz, LexisNexis, Revue Fiduciaire
```

## Programme et thèmes récurrents

TVA (champ, territorialité des livraisons et prestations, importations et autoliquidation, fait générateur et exigibilité, option pour les débits, déductions et régularisations, livraisons à soi-même, exonérations des exportations), IR (foyer fiscal et imposition commune, TS et frais réels, revenus fonciers micro/réel, BNC/BIC — créances acquises vs recettes encaissées —, charges déductibles du revenu global, pensions alimentaires et plafonds, réductions et crédits d'impôt), IS (territorialité, charges déductibles, acte anormal de gestion, intégration), procédures fiscales (rectification, abus de droit L. 64 LPF, garanties du contribuable).

## Sources et outils

- OpenLegi `rechercher_code` : CGI, CIBS, LPF — vérifier impérativement les montants, plafonds et taux **de l'année fiscale du sujet** (plafond pension alimentaire enfant majeur, barème, abattements, franchise) ; ces chiffres changent chaque année.
- OpenLegi `rechercher_jurisprudence_administrative` : Conseil d'État (plénière fiscale, 8e-3e ch.), pour l'acte anormal de gestion, la territorialité, etc.
- GoodLegal `legislation_search` / `case_search` en croisement ; `web_search` pour la doctrine BOFiP (citer `BOI-...` seulement si la référence est vérifiée).
- **Vérifier tous les calculs avec bash/Python** avant de les inscrire dans la grille : montants de TVA collectée/déductible, revenu net imposable par catégorie, plafonnements. La grille doit donner le détail chiffré opération par opération puis le total.

## Pièges classiques

- Prélèvement d'un bien de l'entreprise pour un usage privé : livraison à soi-même imposable (art. 257, II CGI) dès lors que la TVA d'amont a été déduite ; base = valeur d'achat/coût de revient.
- Indemnité d'assurance : hors champ (pas de livraison ni prestation), pas de régularisation pour destruction justifiée (art. 207 ann. II).
- Option pour les débits mentionnée SUR LA FACTURE du prestataire : l'exigibilité chez le fournisseur conditionne la déduction chez le client — TVA déductible dès le débit (facturation), même si paiement le mois suivant.
- Importation : autoliquidation obligatoire sur la déclaration de TVA (depuis 2022), TVA collectée ET déductible le même mois = effet net nul, mais il faut le dire et le chiffrer.
- Livraison interne de biens : exigibilité à la livraison (septembre) même si paiement en octobre.
- Prestation sur biens / travaux au Maroc : qualifier livraison avec montage vs prestation de services ; territorialité (lieu d'exécution matérielle hors UE → non imposable en France) ; distinguer de l'exportation exonérée avec droit à déduction.
- IR : séparation de biens + vie commune = imposition commune quand même ; frais réels > 10 % à justifier ; capital d'emprunt non déductible des revenus fonciers (seuls les intérêts) ; CSG déductible (fraction de 6,8 points) ; pension alimentaire enfant majeur non rattaché plafonnée (vérifier le plafond de l'année) ; BNC : recettes encaissées en janvier N+1 rattachées à N+1 (sauf option créances acquises) ; acte anormal de gestion : en principe inapplicable à la libre fixation des honoraires en BNC sauf diminution délibérée de recettes contraire à l'intérêt de l'exploitation — citer la jurisprudence CE vérifiée.

## Format de citation

`art. 256 CGI`, `art. 269, 2 CGI`, `art. 83, 3° CGI`, `art. L. 64 LPF`, `CE, [date], n° [requête]`, `BOI-XXX-XXX (le cas échéant, vérifié)`.

## Arborescence de révision (déclinaison du programme officiel)

Programme officiel : sources du droit fiscal ; imposition du résultat des entreprises ; TVA ; imposition du revenu et du patrimoine des personnes physiques ; contrôle et contentieux fiscal. Précisions CNB 2026 : l'imposition du revenu et du patrimoine inclut l'imposition de la transmission du patrimoine (y compris biens professionnels) ; les questions de TVA porteront sur des situations antérieures au 1er septembre 2026 (recodification de la TVA dans le CIBS) — adapter la base textuelle (CGI vs CIBS) à la session visée.

- **Sources** : légalité de l'impôt, doctrine administrative (BOFiP, garantie L. 80 A/B LPF), conventions fiscales, droit de l'UE et TVA.
- **Résultat des entreprises** : BIC/IS (champ, territorialité de l'IS), produits et charges déductibles, acte anormal de gestion, amortissements et provisions, déficits, régimes des plus-values professionnelles, intégration fiscale (notions), distributions.
- **TVA** : champ et assujettis, opérations imposables/exonérées, livraisons à soi-même, territorialité (livraisons, prestations B2B/B2C, importations/exportations, échanges intracommunautaires, autoliquidation), fait générateur et exigibilité (débits), base et taux, droit à déduction (coefficients, régularisations), obligations et régimes.
- **Revenu des personnes physiques** : foyer fiscal et imposition commune, TS (frais réels), revenus fonciers (micro/réel, charges), BNC/BIC/BA, RCM et PFU, plus-values des particuliers (mobilières, immobilières, exonérations), charges déductibles du revenu global (pensions, CSG déductible), réductions/crédits, quotient familial, prélèvement à la source (notions).
- **Patrimoine et transmission** : IFI (assiette, exonération biens professionnels), droits de mutation à titre gratuit (successions, donations, abattements, démembrement art. 669/751, Dutreil — biens professionnels, précision CNB 2026), droits d'enregistrement (cessions de fonds, de droits sociaux).
- **Contrôle et contentieux** : procédures de rectification (contradictoire, taxation d'office), abus de droit (L. 64, mini-abus L. 64 A) et acte anormal de gestion, garanties du contribuable, prescription, sanctions, contentieux de l'assiette (réclamation préalable, juge compétent : ordre administratif vs judiciaire selon l'impôt), sursis de paiement.
