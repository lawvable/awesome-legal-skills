# Fiche d'intégration — connecteurs OpenLegi et LibreJustice

Ce skill s'appuie sur deux connecteurs MCP complémentaires. Il fonctionne sans eux, mais en mode dégradé : sans accès aux sources primaires, la règle du §1 impose de renoncer aux références chiffrées. **Installer les deux avant tout usage professionnel.**

## Vue d'ensemble

| | OpenLegi | LibreJustice |
|---|---|---|
| Site | https://www.openlegi.fr/ | https://librejustice.fr/ |
| Endpoint MCP | `https://mcp.openlegi.fr` | `https://librejustice.fr/mcp/` |
| Guide | https://www.openlegi.fr/documentation/ | https://librejustice.fr/mcp-guide |
| Accès | Compte gratuit ; OAuth ou token | OAuth |
| Force | Textes officiels via l'API PISTE de Légifrance | Recherche sémantique et lexicale de jurisprudence |
| Couverture | 75 codes, LODA, JORF, CETAT, CONSTIT, CNIL, KALI, BODACC, BOFiP | Décisions et textes, judiciaire et administratif |

Ils ne font pas la même chose : OpenLegi répond à « que dit le texte ? », LibreJustice à « comment les juges tranchent-ils ce point ? ». Les deux sont nécessaires en droit des étrangers, où le texte seul ne suffit presque jamais.

## Installation — OpenLegi

1. Créer un compte gratuit sur https://www.openlegi.fr/accounts/signup/
2. Récupérer le token MCP dans l'espace du compte.
3. **Claude web et bureau** : ajouter le connecteur avec l'endpoint `https://mcp.openlegi.fr` — OAuth recommandé, ou token dans l'URL. Un abonnement Claude payant (Pro, Max, Team ou Enterprise) est requis pour les connecteurs sur claude.ai.
4. **Claude Desktop** : configuration locale via `claude_desktop_config.json`, avec le token — gratuit.
5. Vérifier la disponibilité du service sur https://www.openlegi.fr/status/

Sources sur abonnement, à activer sur demande si le dossier l'exige : **EUR-Lex** (indispensable pour les règlements du Pacte européen), **Judilibre**, **RNE**. Sans EUR-Lex, le droit de l'Union se vérifie directement sur https://eur-lex.europa.eu — cette limite est documentée par l'éditeur, pas contournable par l'outil.

Documentation destinée aux modèles : https://www.openlegi.fr/llms-full.txt
Liste officielle des outils : https://www.openlegi.fr/documentation/outils/liste-des-outils/
Guide de construction d'un skill utilisant OpenLegi : https://www.openlegi.fr/documentation/plugins-et-skills/construire-un-skill-claude-qui-utilise-openlegi/

## Installation — LibreJustice

1. **Claude web et bureau** : ouvrir la fiche dans le répertoire des connecteurs — https://claude.ai/directory/connectors/librejustice — puis **Connect** et validation OAuth. Le connecteur est ensuite actif dans les conversations et les projets.
2. **Autres clients** (ChatGPT en mode développeur, Le Chat de Mistral, Perplexity) : ajouter un connecteur MCP personnalisé avec l'endpoint `https://librejustice.fr/mcp/`, méthode OAuth.
3. **Installation par prompt** sur les applications de bureau : coller `Installe LibreJustice (MCP + skills) en suivant ce guide : https://github.com/librejustice/librejustice/blob/main/llms-install.md`

L'éditeur publie deux skills compagnons — *recherche-jurisprudence* et *recherche-normes* — téléchargeables depuis https://librejustice.fr/mcp-guide et installables via **Paramètres → Personnaliser → Skills**. Ils sont compatibles avec le présent skill et le complètent sur la méthode de recherche ; le connecteur reste nécessaire dans tous les cas.

## Vérification après installation

Trois requêtes de contrôle, à passer avant de traiter un dossier réel :

1. « Donne-moi le texte en vigueur de l'article L.435-1 du CESEDA avec son lien Légifrance. » — teste OpenLegi sur les codes. Attendu : un texte accompagné d'un lien `LEGIARTI`.
2. « Trouve des décisions récentes sur le refus de renouvellement d'un certificat de résidence algérien. » — teste LibreJustice sur la recherche sémantique. Attendu : des décisions avec juridiction, date et numéro.
3. « Quelles versions successives a connues l'article L.611-1 du CESEDA ? » — teste l'accès aux versions. Un échec ici est normal et documenté : les versions historiques sont hors périmètre d'OpenLegi et se consultent sur Légifrance, onglet « Versions ».

Si une requête échoue, vérifier dans l'ordre : le statut du service, l'autorisation OAuth, et l'activation de la source concernée.

## Répartition des rôles dans ce skill

| Besoin | Outil |
|---|---|
| Texte d'un article du CESEDA en vigueur | OpenLegi (codes) |
| Décret, arrêté, loi hors code (liste métiers en tension, décrets d'application) | OpenLegi (LODA, JORF) |
| Jurisprudence du Conseil d'État, des CAA et TA | OpenLegi (CETAT) ou LibreJustice |
| Recherche jurisprudentielle sans numéro connu, par le sens | LibreJustice |
| Texte d'une décision en intégralité avant citation | LibreJustice |
| Décision du Conseil constitutionnel (ex. n° 2023-863 DC) | OpenLegi (CONSTIT) |
| Rétention, JLD, état civil, nationalité (judiciaire) | LibreJustice |
| Version d'un article à une date passée | Légifrance directement — hors périmètre des deux outils |
| Règlements du Pacte européen, directives | EUR-Lex directement, ou OpenLegi si la source est activée |
| Accords bilatéraux | Aucun des deux n'indexe les textes consolidés — voir `accords-bilateraux.md` |

Cette dernière ligne est la plus importante : les zones que les outils ne couvrent pas sont exactement celles où un modèle est tenté de combler par la mémoire. Les connaître, c'est savoir où se taire.
