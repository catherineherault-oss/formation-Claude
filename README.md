# Mon espace de recherche académique

Bienvenue ! Ce dépôt est votre espace de travail pour rédiger des articles de
recherche assistés par IA. Aucune compétence technique n'est nécessaire :
décrivez simplement ce que vous voulez faire à Claude.

## Comment démarrer

1. Dites à Claude ce que vous voulez faire — par exemple :
   - « Je veux écrire un article sur [sujet] »
   - « Fais une revue de littérature sur [thème] »
   - « Rédige un article complet sur [sujet] »
   - « Évalue cet article » (collez votre texte)
2. Claude utilise les compétences installées dans `.claude/` et range les
   résultats au bon endroit.
3. Votre cahier de laboratoire (`lab/`) est mis à jour automatiquement
   après chaque échange important.

## À quoi servent les dossiers

| Dossier              | Ce qu'il contient                                              |
|----------------------|----------------------------------------------------------------|
| `articles/`          | Vos manuscrits en cours de rédaction                           |
| `data/raw/`          | Données brutes (ne jamais modifier — c'est la source)          |
| `data/processed/`    | Données nettoyées et prêtes à analyser                         |
| `code/`              | Scripts d'analyse (R, Python, etc.)                            |
| `figures/svg/`       | Graphiques en version vectorielle (qualité publication)        |
| `figures/png/`       | Graphiques en version PNG 300 dpi (Word, web)                  |
| `references/`        | Bibliographie : fichiers `.bib`, PDFs annotés                  |
| `outputs/latex/`     | Fichiers `.tex` et `.bib` prêts pour Overleaf                  |
| `outputs/word/`      | Fichiers `.docx` prêts pour Word                               |
| `outputs/submitted/` | Versions soumises à des revues                                 |
| `lab/`               | Votre cahier de laboratoire et journal de bord (auto)          |
| `.claude/`           | Le moteur d'assistance (ne pas modifier à la main)             |

## Vos fichiers de traçabilité

- `lab/lab_notebook.md` — cahier de laboratoire vivant (directions explorées,
  hypothèses, choix). Mis à jour à chaque échange substantiel.
- `lab/prompt_log.md` — journal des prompts et résultats. Trace complète de
  votre démarche pour la transparence et la reproductibilité.

Demandez à Claude « montre-moi mon cahier de labo » ou « synthèse de ma
recherche » à tout moment.

## Vos préférences

Elles sont enregistrées dans `.claude/user_preferences.md`. Vous pouvez les
modifier à tout moment : dites simplement « change ma langue préférée » ou
« je veux désormais des sorties en LaTeX ».
