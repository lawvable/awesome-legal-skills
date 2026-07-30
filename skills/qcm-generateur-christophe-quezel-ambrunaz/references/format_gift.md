# Format GIFT - Spécifications techniques

## Structure de base

```gift
::Titre question:: Énoncé de la question {
=Réponse correcte
~Réponse incorrecte 1
~Réponse incorrecte 2
}
```

## Choix unique vs réponses multiples

**Choix unique** :
```gift
::Q1:: Énoncé {
=Réponse correcte (100%)
~Réponse fausse 1 (0%)
~Réponse fausse 2 (0%)
}
```

**Réponses multiples** :
```gift
::Q2:: Énoncé {
~%33.33%Réponse correcte 1
~%33.33%Réponse correcte 2
~%33.34%Réponse correcte 3
~%-100%Réponse incorrecte 1
~%-100%Réponse incorrecte 2
}
```

## Caractères de contrôle

Caractères spéciaux à échapper avec `\` :
- `~` (tilde) : Précède une réponse
- `=` (égal) : Précède la bonne réponse
- `#` (dièse) : Précède un feedback
- `{` `}` (accolades) : Délimitent les réponses
- `:` (deux-points) : Dans le titre

Exemple échappement :
```gift
::Question\: exemple:: Quelle formule contient \= ? {
=La formule a \= b
~La formule c \~ d
}
```

## LaTeX

Entourer de `$` pour formules :
```gift
La formule $E = mc^2$ est célèbre {
=Vrai
~Faux
}
```

## Encodage

**CRITIQUE** : UTF-8 obligatoire (pas UTF-16/Unicode)

Vérifier encodage :
- Linux/Mac : `file -i fichier.txt`
- Windows : Notepad++ > Encodage > Convertir en UTF-8

## Structure complète

```gift
// ============================================
// QCM GÉNÉRÉ PAR CLAUDE
// Thématique : [...]
// Date : [...]
// Nombre de questions : [N]
// ============================================

// CATÉGORIE (optionnel)
$CATEGORY: $course$/[Nom de catégorie]

// Question 1
::Q1 - [Titre court]:: [Énoncé] {
=Réponse correcte
~Réponse incorrecte 1
~Réponse incorrecte 2
~Réponse incorrecte 3
}

// Question 2 - Réponses multiples
::Q2 - [Titre]:: [Énoncé] {
~%50%Réponse correcte 1
~%50%Réponse correcte 2
~%-100%Réponse incorrecte 1
}
```

## Bonnes pratiques

1. **Séparer questions** : 1+ ligne vide entre questions
2. **Commentaires** : Lignes commençant par `//`
3. **Titre court** : Max 40 caractères pour lisibilité
4. **Ordre aléatoire** : Moodle peut mélanger automatiquement
5. **Feedbacks** (optionnel) : `#Feedback après réponse`
