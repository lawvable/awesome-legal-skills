# archeologue-gallica

Archéologie des sources juridiques anciennes dans les fonds numérisés de la
Bibliothèque nationale de France (Gallica).

## Ce que fait le skill

- **Débats parlementaires** : JO Débats, Chambre des députés (1881-1940) et
  Sénat (1880-1940), Annales de l'Assemblée nationale (1871-1876) — la genèse
  des lois de la IIIe République, séance par séance.
- **Textes officiels** : JO Lois et décrets (1881-2015), tables annuelles,
  Bulletin des lois pour le XIXe siècle antérieur.
- **Jurisprudence ancienne** : Bulletin civil (1793-1913), Bulletin criminel
  (1805-1953), Recueil Lebon (1848-1954), Gazette des tribunaux (depuis 1775).
- **Doctrine d'origine** : recueils Sirey et Dalloz, Journal du palais, Revue
  critique de législation, RTD civ. ancienne, Bulletin de l'Inspection du
  travail, thèses et traités du domaine public.

Chaque résultat est localisé à la page, avec extrait océrisé et lien pérenne
(identifiant ark) vers le fac-similé, pour vérification.

## Contenu du paquet

    archeologue-gallica/
    ├── SKILL.md                    instructions et workflows
    ├── README.md                   ce fichier
    ├── references/
    │   └── periodiques.md          catalogue des fonds juridiques (ark de titre)
    └── scripts/
        └── gallica_client.py       client des API Gallica

## Installation

1. Importer le dossier `archeologue-gallica/` comme compétence dans le client
   (Claude : Paramètres → Capacités → Compétences).
2. Autoriser deux domaines réseau supplémentaires :
   - `gallica.bnf.fr`
   - `api.bnf.fr`
3. Aucune clé d'API, aucun compte, aucune dépendance à installer : le script
   n'utilise que la bibliothèque standard de Python 3
   (`argparse`, `json`, `re`, `sys`, `time`, `unicodedata`, `urllib`).

## Limites à connaître

- **Couverture numérisée ≠ couverture cataloguée.** La Gazette des tribunaux,
  par exemple, saute de 1865 à 1951. Le skill vérifie les années réellement
  disponibles avant d'affirmer qu'une source existe ou non. Une absence dans
  Gallica signifie « non numérisé », jamais « n'existe pas ».
- **L'OCR des imprimés anciens comporte des coquilles.** Toute citation
  littérale destinée à un écrit doit être contrôlée sur l'image du document,
  que le skill fournit systématiquement par son lien ark.
- **Les fonds récents restent sous droits** (RTD civ. d'après-guerre, Dalloz
  contemporain…) : le skill renvoie vers les bases sous licence, il ne
  contourne aucune restriction.

## Sources

Fonds numérisés par la Bibliothèque nationale de France et diffusés via
Gallica (https://gallica.bnf.fr), au moyen d'API publiques, ouvertes et
stables. Les documents anciens exploités relèvent du domaine public.

Ce skill n'est qu'une surcouche d'interrogation : le travail de numérisation,
d'océrisation et de catalogage est celui des équipes de la BNF.
