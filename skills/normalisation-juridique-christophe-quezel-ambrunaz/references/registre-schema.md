# Schéma du registre JSON

Fichier écrit dans `.normjur/registre.json`, à côté du document. **Jamais déversé dans la conversation** : seul le tableau `recap` y figure.

```jsonc
{
  "version": "1.0",
  "document_original": "/chemin/abs/original.docx",   // source intacte, base des reconstructions
  "document_corrige":  "/chemin/abs/normalise.docx",
  "horodatage": "2026-06-18T10:30:00Z",
  "auteur_revisions": "Claude — normalisation",
  "scope": "all",                                       // all | body | body+notes

  "groupes": [                                          // une ligne du récapitulatif = un groupe
    {
      "n": 1,                                            // numéro affiché, stable
      "cle": "apostrophes",
      "libelle": "Apostrophes droites → courbes",
      "categorie": "typographie",                        // typographie|lexique|citation|ia|stylistique
      "regime": "determin",                              // determin | jugement
      "type_edition": "direct",                          // direct | tracked
      "actif": true,
      "occurrences": 42,
      "exemples": ["l'article → l’article"]              // 1 à 3 exemples tronqués (~40 car.)
    }
  ],

  "editions": [                                          // une modification atomique
    {
      "n": 1, "i": 1,                                    // groupe n, occurrence i (→ "défais 1.1")
      "cle": "apostrophes",
      "regime": "determin",
      "partie": "document",                              // document | footnotes | endnotes
      "actif": true,
      "avant": "l'",
      "apres": "l’",
      "contexte": "…dans l'article 9…",                  // facultatif, tronqué
      "w_ids": []                                        // ids des révisions Word (régime jugement/tracked)
    }
  ],

  "regles_desactivees": [],                              // ["anglicismes_surs", ...] — reconstruction déterministe
  "occurrences_desactivees": []                          // ["7.2", "9.1"] — exclusions fines
}
```

## Conventions

- **Numérotation** : les groupes déterministes reçoivent `n` = 1…k dans l'ordre fixe des règles ; les groupes de jugement suivent (`k+1`, `k+2`…) dans l'ordre d'ajout par `registre.py add-jugement`.
- **Régime déterministe** : la réversibilité passe par **reconstruction** depuis `document_original` en réappliquant les règles/occurrences encore actives (`regles_desactivees`, `occurrences_desactivees`). Pas de réécriture en place : pas de dérive.
- **Régime jugement** : la réversibilité passe par **rejet des révisions** identifiées par `w_ids`. Si l'utilisateur les a déjà acceptées dans Word, basculer sur un remplacement `apres → avant`.
- **Idempotence** : un groupe déjà désactivé n'est pas réappliqué ; une occurrence déjà conforme n'est pas recomptée.
