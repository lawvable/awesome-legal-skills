# Contraintes pour QCM Léger

## Principe directeur

Les QCM légers sont conçus pour un usage ludique et engageant (Kahoot!, Wooclap), avec des contraintes strictes de longueur. Ces contraintes ne sont pas arbitraires : elles garantissent la lisibilité sur écrans (projecteurs, tablettes, smartphones) et le rythme dynamique des quiz.

## Contraintes de longueur

### Énoncés de questions

**Limite stricte : 95 caractères maximum (espaces inclus)**

Cette contrainte s'applique à l'énoncé complet de la question, incluant :
- Le texte de la question
- Les éventuels articles ou prépositions
- La ponctuation

**Comptage** : Chaque caractère compte, y compris espaces et ponctuation.

**Exemple conforme** (87 caractères) :
```
Quel scientifique a formulé la théorie de la relativité générale en 1915 ?
```

**Exemple NON conforme** (132 caractères) :
```
Quel scientifique allemand naturalisé américain a formulé la théorie de la relativité générale en 1915, révolutionnant notre compréhension de l'espace-temps ?
```

### Réponses

**Limite stricte : 60 caractères maximum par réponse (espaces inclus)**

Chaque option de réponse doit être concise et directe.

**Exemple conforme** (31 caractères) :
```
Albert Einstein
```

**Exemple NON conforme** (89 caractères) :
```
Albert Einstein, physicien théoricien allemand naturalisé américain (1879-1955)
```

## Stratégies de reformulation

### Pour les énoncés trop longs

#### Stratégie 1 : Suppression du contexte superflu

**Avant** (124 caractères) :
```
Dans le cadre du droit de la responsabilité civile français, quel est le régime juridique applicable en cas de dommage ?
```

**Après** (73 caractères) :
```
Quel régime juridique s'applique en responsabilité civile française ?
```

#### Stratégie 2 : Passage du style indirect au style direct

**Avant** (108 caractères) :
```
Pourriez-vous indiquer quelle est la capitale administrative et politique de la République française ?
```

**Après** (48 caractères) :
```
Quelle est la capitale de la France ?
```

#### Stratégie 3 : Suppression des qualifications redondantes

**Avant** (97 caractères) :
```
Quel philosophe allemand célèbre a écrit l'ouvrage majeur "Critique de la raison pure" ?
```

**Après** (58 caractères) :
```
Qui a écrit "Critique de la raison pure" ?
```

#### Stratégie 4 : Utilisation d'abréviations standard

**Avant** (102 caractères) :
```
En quelle année la Seconde Guerre mondiale a-t-elle officiellement pris fin en Europe ?
```

**Après** (60 caractères) :
```
En quelle année s'est terminée la 2nde Guerre mondiale ?
```

#### Stratégie 5 : Question directe plutôt que périphrase

**Avant** (115 caractères) :
```
Pouvez-vous identifier l'élément chimique dont le numéro atomique est 6 dans le tableau périodique ?
```

**Après** (57 caractères) :
```
Quel élément a le numéro atomique 6 ?
```

### Pour les réponses trop longues

#### Stratégie 1 : Suppression des dates ou précisions

**Avant** (68 caractères) :
```
Marie Curie (1867-1934), physicienne et chimiste française
```

**Après** (11 caractères) :
```
Marie Curie
```

#### Stratégie 2 : Utilisation de formulations courtes

**Avant** (78 caractères) :
```
La responsabilité civile contractuelle fondée sur l'inexécution du contrat
```

**Après** (37 caractères) :
```
Responsabilité contractuelle
```

#### Stratégie 3 : Acronymes ou abréviations

**Avant** (65 caractères) :
```
Organisation des Nations Unies pour l'éducation et la culture
```

**Après** (6 caractères) :
```
UNESCO
```

#### Stratégie 4 : Réponses nominales plutôt que phrases

**Avant** (72 caractères) :
```
C'est le processus par lequel les plantes fabriquent leur nourriture
```

**Après** (14 caractères) :
```
Photosynthèse
```

## Cas problématiques et solutions

### Cas 1 : Question nécessitant contextualisation

**Problème** : Certains concepts ne peuvent être testés sans contexte.

**Solution** : Simplifier radicalement ou **choisir QCM approfondi**.

**Exemple** :
Si vous devez tester : "Dans le cadre d'un contrat de vente conclu entre un professionnel et un consommateur, quelles sont les obligations du vendeur concernant la conformité du bien vendu selon le Code de la consommation ?"

→ Cette question ne peut pas être reformulée en <95 caractères sans perdre son sens.
→ **Recommandation** : Basculer vers QCM approfondi.

### Cas 2 : Formules mathématiques ou scientifiques

Les formules comptent dans le nombre de caractères.

**Exemple conforme** (42 caractères) :
```
Quelle est la formule de l'énergie ?
A. E = mc²
B. F = ma
C. P = mv
D. W = Fd
```

### Cas 3 : Citations

Les citations longues sont incompatibles avec le format léger.

**Non conforme** : Demander d'analyser une citation de 3 lignes.

**Conforme** : Tester la connaissance de l'auteur d'une citation courte.

### Cas 4 : Noms propres longs

**Exemple** :
```
Jean-Baptiste Poquelin, dit Molière
```
(37 caractères - acceptable)

Si contexte nécessaire dépasse 60 caractères, utiliser seulement le nom usuel :
```
Molière
```

## Protocole de génération pour QCM léger

### Étape 1 : Génération initiale

Générer la question en visant la concision maximale dès le départ.

### Étape 2 : Vérification automatique

Compter les caractères :
- Énoncé : ≤ 95 ?
- Chaque réponse : ≤ 60 ?

### Étape 3 : Reformulation si nécessaire

Si dépassement, appliquer les stratégies de reformulation ci-dessus.

**Limite de tentatives** : 2 reformulations maximum.

### Étape 4 : Alerte si échec

Si après 2 tentatives la question ne respecte pas les contraintes :
1. Alerter l'utilisateur
2. Proposer soit :
   - Supprimer cette question
   - Passer en QCM approfondi pour cette question
   - Simplifier encore davantage (avec validation utilisateur)

## Validation des questions légères

### Checklist de conformité

Pour chaque question, vérifier :

- [ ] Énoncé ≤ 95 caractères (compter avec espaces et ponctuation)
- [ ] Toutes les réponses ≤ 60 caractères
- [ ] La question reste compréhensible malgré la concision
- [ ] Les distracteurs sont plausibles même dans version courte
- [ ] Aucune ambiguïté introduite par la reformulation

### Test de lisibilité

Après reformulation, se demander :
- Un étudiant comprend-il immédiatement ce qui est demandé ?
- Les réponses sont-elles univoques ?
- La concision nuit-elle à l'équité de la question ?

Si réponse "non" à l'une de ces questions → Reformuler ou basculer en approfondi.

## Exemples complets conformes

### Exemple 1 - Primaire (71 caractères)

```
Question : Combien y a-t-il de continents sur Terre ?

A. 5
B. 6
C. 7
D. 8

(Énoncé : 43 car. | Réponses : 1 car.)
```

### Exemple 2 - Collège (85 caractères)

```
Question : Quelle est la langue la plus parlée au monde en nombre de locuteurs natifs ?

A. Anglais
B. Mandarin
C. Espagnol
D. Hindi

(Énoncé : 85 car. | Réponses : max 8 car.)
```

### Exemple 3 - Lycée (94 caractères)

```
Question : Quel événement marque le début de la Révolution française selon la tradition ?

A. Prise de la Bastille (14 juillet 1789)
B. Déclaration des Droits (26 août 1789)
C. Serment du Jeu de Paume (20 juin 1789)
D. États généraux (5 mai 1789)

(Énoncé : 94 car. | Réponses : max 43 car.)
```

### Exemple 4 - Licence (88 caractères)

```
Question : Quel concept désigne l'obligation de réparer un dommage causé à autrui ?

A. Responsabilité civile
B. Responsabilité pénale
C. Obligation contractuelle
D. Faute intentionnelle

(Énoncé : 88 car. | Réponses : max 26 car.)
```

### Exemple 5 - Master (93 caractères)

```
Question : Quelle théorie économique prône l'intervention minimale de l'État ?

A. Keynésianisme
B. Libéralisme économique
C. Économie planifiée
D. Social-démocratie

(Énoncé : 77 car. | Réponses : max 24 car.)
```

## Outils de vérification

### Comptage manuel

Pour compter manuellement :
1. Copier le texte dans un éditeur
2. Utiliser fonction "Nombre de caractères" (avec espaces)
3. Vérifier ≤ seuil

### Formule de vérification automatique

En Python :
```python
def check_light_mcq(question, answers):
    if len(question) > 95:
        return False, f"Question trop longue : {len(question)} car."
    for i, ans in enumerate(answers):
        if len(ans) > 60:
            return False, f"Réponse {i+1} trop longue : {len(ans)} car."
    return True, "Conforme"
```

## Conclusion

Les contraintes du QCM léger ne sont pas des limitations arbitraires mais des garde-fous garantissant l'efficacité pédagogique du format ludique. Lorsqu'une question ne peut être formulée conformément à ces contraintes sans perte de sens, c'est généralement le signe qu'elle nécessite le format approfondi.

**Règle d'or** : Privilégier toujours la clarté et la précision sur la concision. Si impossible de concilier les deux, basculer vers QCM approfondi.
