# Tâche 1 — Recherche juridique approfondie

> **Pré-requis environnement** : aucun — exécutable en tout mode. COWORK/CHAT_CU : livrable Word. CHAT : réponse conversationnelle structurée.

## Objectif

Produire une synthèse approfondie avec références vérifiées sur un point de droit, avec un **accent doctrinal renforcé** adapté au contexte académique. Prioriser l'état actuel du droit tout en traitant les évolutions, les controverses doctrinales et les dynamiques jurisprudentielles.

## Processus

### 1. Exécuter le playbook (tâche 0)

Identifier les questions juridiques et le droit applicable. Le playbook oriente les axes de recherche.

### 2. Recherche documentaire — Séquence descendante

Suivre la séquence du §3 du SKILL.md dans cet ordre strict :

**EXÉCUTER :**

**2a. Textes normatifs** via OpenLegi :
- `rechercher_code` → articles des codes applicables
- `rechercher_dans_texte_legal` → lois, ordonnances, décrets
- `recherche_journal_officiel` → textes récents
- Vérifier les métadonnées temporelles de chaque texte (état juridique, dates de vigueur)
- Qualifier le statut temporel dans chaque citation

**2b. Jurisprudence suprême** via OpenLegi :
- `rechercher_jurisprudence_judiciaire` (filtre Cour de cassation, `publication_bulletin: true` en premier)
- `rechercher_jurisprudence_administrative` (filtre Conseil d'État, `publication_recueil: true` en premier)
- `rechercher_decisions_constitutionnelles` si pertinent
- Identifier les arrêts de principe, les revirements, la jurisprudence constante

**2c. Jurisprudence du fond** via OpenLegi :
- `rechercher_jurisprudence_judiciaire` (filtre cours d'appel, tribunaux judiciaires)
- `rechercher_jurisprudence_administrative` (filtre CAA, TA)
- Sélectionner les décisions illustrant concrètement l'application de la règle

**2d. Doctrine** (priorité renforcée — contexte académique) :
- `scripts/doctrine_search.py` → recherche doctrinale multi-sources (HAL + OpenAlex + Isidore), identifiant vérifiable par référence ; `scripts/hal_search.py` pour les notes d'arrêt par pourvoi
- web_search → Cairn, Dalloz Actualité, Persée, OpenEdition
- Rechercher les notes d'arrêt par numéro de pourvoi (HAL : `--pourvoi "NUMÉRO"`)
- Dédoublonner HAL / web_search
- **Minimum 10 sources doctrinales** pour les recherches approfondies, variées en supports (articles, ouvrages, thèses, notes, mélanges) et en auteurs
- Rechercher les thèses récentes (HAL : `--query "TERMES" --all-types` puis filtrer THESE)
- Identifier les débats doctrinaux en cours, les écoles de pensée, les positions divergentes

**2e. Droit comparé** (si pertinent) :
- `LegalDataHunter:search` avec les filtres pays et namespace appropriés
- Voir `references/guide-legaldatahunter.md` pour les stratégies de recherche
- Intégrer la dimension comparative uniquement si elle éclaire la question de droit français

**INTERROMPRE UNIQUEMENT SI :**
- Aucun résultat pertinent sur l'ensemble des sources → signaler et proposer des axes alternatifs
- Contradiction majeure entre textes normatifs → exposer le conflit et la résolution proposée

### 3. Vérification

Pour chaque référence citée :
1. Confirmer l'existence via OpenLegi ou web_search (cf. `references/principes-cardinaux.md`)
2. Vérifier le statut temporel (en vigueur / abrogé / futur)
3. Qualifier la nature de la source (normatif / travaux parlementaires / informatif)
4. Créer un lien hypertexte vers la source

### 4. Rédaction du document Word

**Structure :**

1. **Synthèse** (réponse directe aux questions posées, en début de document)
2. **Introduction** : définitions, contexte historique, enjeux contemporains
3. **Développement** en plan structuré :
   - Titres descriptifs en sentence case
   - Citations exactes entre guillemets français « … » avec notes de fin
   - Confrontation des points de vue doctrinaux dans le corps du texte (dialectique, pas énumération)
   - Faits clés et éléments importants en gras
   - Identification explicite des zones de consensus, de controverse et d'incertitude
4. **Bibliographie classée** :
   - Textes normatifs
   - Jurisprudence (classée par juridiction, puis chronologique)
   - Doctrine (classée : traités/manuels, thèses, articles, notes, contributions)
5. **Notes et références** en fin de document

**Traitement de la doctrine dans le corps du texte :**
- Intégrer les citations exactes des auteurs directement dans le développement
- Confronter les points de vue divergents : présenter la thèse, l'antithèse, expliquer les raisons du désaccord
- Indiquer les zones de consensus et de controverse
- Citer les thèses de doctorat pertinentes avec indication de la contribution scientifique
- Mentionner les écoles de pensée ou courants doctrinaux identifiables

**Format des citations** : voir `references/format-citations.md`

### 5. Livraison

Écrire le fichier Word selon le mode d'environnement (cf. §6 du SKILL.md). Nommage : `[AAAA-MM-JJ]-recherche-[sujet].docx`.

Proposer des tâches connexes : création de sujet d'examen sur le thème, mise à jour d'un cours existant, préparation d'un support de cours.
