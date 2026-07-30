# LawyerScrib

Skill (Claude Code / Cursor) qui supprime les traces d’écriture IA dans les textes juridiques français, pour un ton naturel et professionnel.

## Installation

### Recommandé (clone dans le répertoire des skills)

**Claude Code :**
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/VOTRE_ORG/Lawyer-scrib.git ~/.claude/skills/lawyerscrib
# ou, si vous avez déjà cloné le projet : cp /chemin/vers/Lawyer-scrib/SKILL.md ~/.claude/skills/lawyerscrib/
```

**Cursor :**
```bash
mkdir -p ~/.cursor/skills
git clone https://github.com/VOTRE_ORG/Lawyer-scrib.git ~/.cursor/skills/lawyerscrib
# ou : cp /chemin/vers/Lawyer-scrib/SKILL.md ~/.cursor/skills/lawyerscrib/
```

### Installation manuelle (fichier skill uniquement)

Si le dépôt est déjà cloné (ou si vous n’avez que `SKILL.md`), copiez le skill :

```bash
# Claude Code
mkdir -p ~/.claude/skills/lawyerscrib
cp SKILL.md ~/.claude/skills/lawyerscrib/

# Cursor
mkdir -p ~/.cursor/skills/lawyerscrib
cp SKILL.md ~/.cursor/skills/lawyerscrib/
```

## Utilisation

Dans Claude Code ou Cursor, invoquez le skill :

```
/lawyerscrib

[collez votre texte ici]
```

Ou demandez directement :

```
Humanise / révisé ce texte juridique : [votre texte]
```

## Aperçu

Le skill repose sur les mêmes principes que le [Humanizer](https://github.com/blader/humanizer) (Wikipedia, « Signs of AI writing »), adaptés à l’écriture juridique française : conclusions, consultations, notes, mails et actes.

Il inclut une **passe finale « anti-IA »** : repérer ce qui trahit encore l’IA, puis réécrire une version finale.

### Idée centrale

> Un LLM entraîné sur du juridique reproduit les *tics de forme* (références en latin, formules de politesse, structure en parties) sans la *substance argumentative* d’un praticien. L’objectif n’est pas un texte neutre, mais un texte **engagé et précis**.

## 17 patterns détectés (résumé)

### Contenu

| # | Pattern | Avant (typique IA) | Après |
|---|--------|---------------------|--------|
| 1 | **Inflation de la portée** | « s'inscrit dans le cadre plus large de... » | Énoncé factuel + portée réelle |
| 2 | **Attributions vagues** | « La doctrine majoritaire s'accorde... » | Citation précise (auteur, ouvrage, n°) |
| 3 | **Chevilles rhétoriques** | « Il convient de noter... Force est de constater... » | Phrase directe ou suppression |
| 4 | **Évitement du verbe « être »** | « revêt un caractère... se traduit par... » | « est... », « constitue... » |
| 5 | **Passivation excessive** | « Il a été soutenu par la demanderesse que... » | « La demanderesse soutient que... » |
| 6 | **Nominalisation abusive** | « La mise en œuvre de la procédure de résiliation... » | « Pour résilier le bail... » |
| 7 | **Règle des trois** | « pour trois raisons : d'abord... ensuite... enfin... » | Nombre d’arguments naturel |
| 8 | **Sections « Enjeux et perspectives »** | « Des défis persistent. La solution pourrait évoluer. » | Constat concret ou suppression |

### Langage

| # | Pattern | Avant | Après |
|---|--------|--------|--------|
| 9 | **Vocabulaire IA sur du juridique** | « problématique fondamentale, enjeux cruciaux » | Termes précis, régime applicable |
| 10 | **Formules de politesse IA** | « J'espère que ce message vous trouve... N'hésitez pas... » | Formule courte et professionnelle |
| 11 | **Conclusion générique** | « La situation est complexe... Il conviendra d'apprécier... » | Position claire + recommandation datée |
| 12 | **« Ledit », « susmentionné » abusifs** | « Ledit contrat... lesdites parties... ladite clause » | « Le contrat du 3 janvier 2023... » |
| 13 | **Parallélismes négatifs** | « Il ne s'agit pas seulement de X ; il s'agit de Y » | Énoncé direct |

### Style et communication

| # | Pattern | Avant | Après |
|---|--------|--------|--------|
| 14 | **Tiret long (—) abusif** | « La clause est nulle — c'est indiscutable — et ce pour... » | Virgules ou deux points |
| 15 | **Gras mécanique** | **responsabilité contractuelle**, **manquement** | Pas de gras systématique |
| 16 | **Hedging excessif** | « Il semblerait que... pourrait potentiellement... » | « Cette position est contestable :... » |
| 17 | **Ouvertures sycophantiques** | « Excellente question ! Vous avez tout à fait raison... » | « Voici l'analyse. » |

## Exemple complet

**Avant (saturé IA) :**
> Comme il a été souligné supra, la problématique de la validité de la clause de non-concurrence revêt un caractère fondamental dans le cadre du présent litige. Il convient, à cet égard, de rappeler que la doctrine majoritaire s'accorde à reconnaître que ladite clause doit, pour être valide, répondre à des conditions cumulatives que la jurisprudence a progressivement précisées. Force est de constater que ces conditions ne semblent pas réunies en l'espèce. Il s'agit non seulement d'une question de droit, mais d'une question de justice contractuelle. En conclusion, la situation est complexe et nécessite une analyse approfondie. Je reste à votre entière disposition pour tout complément.

**Après (humanisé) :**
> La clause de non-concurrence est nulle faute de contrepartie financière, condition que la chambre sociale exige depuis 2002 (Cass. soc., 10 juill. 2002, n° 00-45.135). La nullité est relative : votre client peut s'en prévaloir ou y renoncer. S'il entend se réinstaller immédiatement, une lettre de renonciation adressée à l'employeur avant la fin du préavis est suffisante.

## Personnalisation

Pour adapter le skill à votre style juridique (registre, formules, types de documents) : voir le **[Guide de personnalisation](GUIDE_PERSONNALISATION.md)**, qui détaille les concepts clés et propose des modèles de règles.

## Références

- [Humanizer](https://github.com/blader/humanizer) – skill source (anglais, usage général)
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) – base des patterns

## Historique des versions

- **1.0.0** – Version initiale : humanizer juridique français (17 patterns, voix avocat, passe anti-IA)

## Licence

MIT © LegalFab
