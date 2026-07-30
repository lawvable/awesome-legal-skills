# Format XML Moodle - Spécifications techniques

## Structure minimale

```xml
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
  <question type="multichoice">
    <n><text>Titre question</text></n>
    <questiontext format="html">
      <text><![CDATA[<p>Énoncé</p>]]></text>
    </questiontext>
    <single>true</single>
    <answer fraction="100" format="html">
      <text><![CDATA[<p>Réponse correcte</p>]]></text>
    </answer>
    <answer fraction="0" format="html">
      <text><![CDATA[<p>Réponse incorrecte</p>]]></text>
    </answer>
  </question>
</quiz>
```

## Choix unique vs multiple

**Choix unique** :
```xml
<single>true</single>
<answer fraction="100">...</answer>
<answer fraction="0">...</answer>
```

**Réponses multiples** :
```xml
<single>false</single>
<answer fraction="50">...</answer>
<answer fraction="50">...</answer>
<answer fraction="-100">...</answer>
```

## Règles critiques

1. **Première ligne** : `<?xml version="1.0" encoding="UTF-8"?>` SANS ligne vide avant
2. **HTML dans CDATA** : `<![CDATA[...]]>` pour tout HTML
3. **Encodage UTF-8** : Explicitement déclaré
4. **Fraction** : 0-100 pour notes, négatif pour pénalités

## Structure complète question

```xml
<question type="multichoice">
  <n><text>Q1 - Titre</text></n>
  
  <questiontext format="html">
    <text><![CDATA[<p>Énoncé de la question</p>]]></text>
  </questiontext>
  
  <defaultgrade>1.0000000</defaultgrade>
  <penalty>0.3333333</penalty>
  <hidden>0</hidden>
  <single>true</single>
  <shuffleanswers>true</shuffleanswers>
  <answernumbering>abc</answernumbering>
  
  <answer fraction="100" format="html">
    <text><![CDATA[<p>Réponse correcte</p>]]></text>
    <feedback format="html">
      <text><![CDATA[<p>Feedback positif</p>]]></text>
    </feedback>
  </answer>
  
  <answer fraction="0" format="html">
    <text><![CDATA[<p>Réponse incorrecte</p>]]></text>
    <feedback format="html">
      <text><![CDATA[<p>Explication</p>]]></text>
    </feedback>
  </answer>
</question>
```

## Catégories

```xml
<question type="category">
  <category>
    <text>$course$/Nom Catégorie/Sous-catégorie</text>
  </category>
</question>
```

## Validation XML

Ouvrir dans Firefox/navigateur pour détecter erreurs XML avant import.
