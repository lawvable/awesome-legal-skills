# Tâche 4 — Analyse et synthèse de pièces d'un dossier

> **Pré-requis environnement** : COWORK ou CHAT_CU requis pour la lecture des pièces. En mode CHAT, exécutable uniquement si les documents sont visibles dans la fenêtre de contexte — sinon, interrompre et demander d'activer computer use. Recommander COWORK si le dossier dépasse 5 pièces ou 30 pages cumulées (persistance nécessaire pour un travail fiable).

## Objectif

Organiser, analyser et synthétiser un ensemble de documents constituant un dossier. Produire un bordereau de pièces, une synthèse factuelle, une chronologie et, si pertinent, une analyse des délais juridiques.

## Processus

### 1. Exécuter le playbook (tâche 0)

### 2. Scanner le dossier de travail (approfondi)

**Les documents du dossier sont la matière première de cette tâche.**

EXÉCUTER :
1. Inventorier chaque fichier (nom, type, taille)
2. Lire chaque document : extraire les éléments factuels (dates, montants, parties, faits)
3. Identifier la nature de chaque pièce : contrat, courrier, facture, certificat médical, décision de justice, correspondance, photographie, attestation, etc.
4. Construire une chronologie des événements à partir de l'ensemble des pièces
5. Identifier les parties et leurs positions respectives
6. Repérer les pièces manquantes évidentes (ex : contrat mentionné mais non fourni)

### 3. Bordereau de pièces

Produire un bordereau numéroté :

| N° | Description | Date | Nature | Observations |
|---|---|---|---|---|
| 1 | Contrat de bail entre X et Y | 15/01/2024 | Contrat | Bail meublé, durée 1 an |
| 2 | … | … | … | … |

Numérotation continue. Classement chronologique ou thématique selon la logique du dossier.

### 4. Chronologie des faits

Produire un tableau chronologique exhaustif, distinct du bordereau :

| Date | Fait | Pièce(s) source(s) |
|---|---|---|
| [date] | [événement] | [N° pièce] |

- Ordonner strictement par date
- Signaler les faits sans date certaine (mention : « date incertaine »)
- Identifier les contradictions entre pièces

### 5. Vérification des délais juridiques

**EXÉCUTER si des délais légaux sont susceptibles d'avoir un impact** (prescription, recours, garantie, etc.) :

1. **Identifier les délais potentiellement applicables** à partir des faits et de la nature du litige :
   - Délai de prescription de droit commun (art. 2224 C. civ. : 5 ans à compter de la connaissance des faits)
   - Délais spéciaux (prescription biennale consommateur, décennale construction, quinquennale contrats d'assurance, garantie des vices cachés, etc.)
   - Délais de recours contentieux (2 mois en matière administrative, etc.)
   - Délais contractuels stipulés dans les pièces

2. **Vérifier chaque délai via OpenLegi** (`rechercher_code`) — ne jamais affirmer un délai de mémoire.

3. **Calculer le délai résiduel** à partir des dates de la chronologie :
   - Point de départ du délai (fait générateur, connaissance du dommage, réception des travaux, etc.)
   - Date d'échéance théorique
   - Date du jour → délai restant ou dépassement éventuel

4. **Signaler explicitement** :
   - ⚠️ **Délai expiré** : prescription ou forclusion potentiellement acquise
   - ⚠️ **Délai imminent** (moins de 3 mois) : avertir l'utilisateur
   - ✅ **Délai non couru ou largement ouvert** : le préciser

5. Mentionner les faits interruptifs ou suspensifs identifiables dans les pièces (mise en demeure, demande en justice, minorité, etc.).

**⚠️ Précaution** : si les dates nécessaires au calcul sont absentes des pièces, l'indiquer et exposer les hypothèses.

### 6. Synthèse factuelle

Produire une synthèse structurée :
1. Parties en présence (identité, qualité)
2. Chronologie des faits (tableau)
3. Points de convergence et de divergence entre les parties
4. Éléments de preuve disponibles par point litigieux
5. Pièces manquantes identifiées

### 7. Analyse juridique préliminaire

Si le playbook a identifié des questions juridiques :
- Rattacher chaque pièce aux questions juridiques identifiées
- Évaluer la force probante de chaque pièce pertinente
- Identifier les éléments factuels qui fondent ou affaiblissent chaque prétention

### 8. Livraison

Un seul document Word comprenant : bordereau + chronologie + analyse des délais (si pertinent) + synthèse + analyse préliminaire.
Nommage : `[AAAA-MM-JJ]-analyse-pieces-[nom-dossier].docx`
