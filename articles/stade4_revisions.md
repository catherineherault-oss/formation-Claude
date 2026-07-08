# Stade 4 — Éléments quantitatifs de révision (revue DM)

Données : enquête 24407, N = 1025. Généré par `code/10_revisions_stade4.py`.

## 1. Diagnostics de la typologie (R1, AD-2)

### 1a. Inertie des axes factoriels (ACM)

| Axe | Valeur propre | % inertie | % cumulé |
|-----|--------------|-----------|----------|
| 1 | 0.3461 | 38.8% | 38.8% |
| 2 | 0.2101 | 23.6% | 62.4% |
| 3 | 0.1264 | 14.2% | 76.5% |
| 4 | 0.1129 | 12.7% | 89.2% |
| 5 | 0.0962 | 10.8% | 100.0% |

### 1b. Qualité et stabilité de la partition (k = 4, 5, 6)

| k | Silhouette (moy.) | Pseudo-F (Calinski-Harabasz) | Effectifs des classes |
|---|-------------------|------------------------------|-----------------------|
| 4 | 0.207 | 283 | [650, 249, 79, 47] |
| 5 | 0.237 | 297 | [624, 249, 79, 47, 26] |
| 6 | 0.232 | 322 | [358, 266, 249, 79, 47, 26] |

*Lecture : silhouette modérée (structure faible à moyenne, typique d'une ACM sur variables d'usage) ; la solution à 5 classes est retenue pour son interprétabilité — l'ajout d'une 6e classe scinde un groupe sans gain de silhouette. Les effectifs confirment une classe majoritaire et des classes de queue de distribution, à interpréter avec prudence.*

### 1c. Effectifs bruts et profil des 5 classes

| Classe | n | % éch. | Canaux fréq. | Canaux rég. | Budget | % VD incl. | % VD rég. |
|--------|---|--------|--------------|-------------|--------|-----------|-----------|
| C1 Multi-canal modérés | 624 | 60.9% | 7.2 | 3.8 | 439€ | 72% | 16% |
| C2 Captifs de la grande distribution | 249 | 24.3% | 3.8 | 2.8 | 408€ | 28% | 6% |
| C3 Multi-canal intensifs | 79 | 7.7% | 11.1 | 9.5 | 513€ | 97% | 67% |
| C4 Explorateurs conventionnels | 47 | 4.6% | 11.0 | 6.1 | 480€ | 100% | 19% |
| C5 Adeptes de la proximité | 26 | 2.5% | 6.3 | 3.3 | 320€ | 81% | 8% |

### 1d. Les classes diffèrent par la COMBINAISON de canaux, pas seulement l'intensité (réfute AD-2)

Usage **régulier** (≥1×/mois) par canal, en % de la classe :

| Classe | Hyper/Super | Hard discount | Épiceries | Surgelés | Bio | Marché | VD agri. | Paniers int. | Artisans | Coop. | Vrac |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | 100 | 62 | 33 | 32 | 19 | 42 | 16 | 2 | 64 | 2 | 4 |
| C2 | 100 | 53 | 13 | 22 | 8 | 20 | 6 | 1 | 49 | 0 | 1 |
| C3 | 100 | 96 | 94 | 86 | 86 | 84 | 67 | 57 | 78 | 68 | 77 |
| C4 | 100 | 96 | 79 | 81 | 77 | 77 | 19 | 0 | 72 | 0 | 0 |
| C5 | 0 | 62 | 38 | 27 | 23 | 50 | 8 | 0 | 62 | 15 | 12 |

*Lecture : les « adeptes de la proximité » (C5) sont le seul groupe à faible hyper/super régulier (combinaison qualitativement distincte, non un simple niveau d'intensité) ; explorateurs (C4) et intensifs (C3) ont une largeur de répertoire proche mais une intensité VD très différente (19% vs 67%). La partition capte donc bien des configurations, pas un seul axe.*

## 2. Sensibilité : définition de la VD × dénominateur (R1-4, AD-1)

| Définition de la vente directe | n | % ménages | Part budget /population | Part budget /réguliers |
|--------------------------------|---|-----------|-------------------------|------------------------|
| Inclusive — union des 2 portes (canal 7 ∪ marché direct) | 666 | 65.0% | — | — |
| Pénétration canal 7 (toute fréquence) | 509 | 49.7% | 1.5% | — |
| Régulière — canal 7 ≥ 1×/mois | 177 | 17.3% | 1.5% | 8.5% |

*Le « paradoxe » survit à la mise à plat : même en retenant la définition la plus stricte (régulière, 17.3%), la part budgétaire chez les seuls réguliers (8.5%) reste minoritaire ; et à l'inverse la diffusion large (65.0%) coexiste avec un poids national de 1.5%. L'écart adhésion/poids n'est pas un artefact d'un choix de dénominateur.*

### 2b. Intervalles de confiance (Wilson 95%) des taux clés

| Indicateur | n / N | % | IC95% |
|-----------|-------|---|-------|
| VD inclusive | 666/1025 | 65.0% | [62.0–67.8] |
| Pénétration canal 7 | 509/1025 | 49.7% | [46.6–52.7] |
| VD régulière | 177/1025 | 17.3% | [15.1–19.7] |

## 3. Robustesse des déterminants (R1-3)

**VD inclusive (65%)** — DV = `vente_directe`. Pseudo-R² McFadden = 0.029, N = 1025, événements = 666. Diplôme bac+3+ : OR = 1.89, p = 0.003.

**VD régulière (17%)** — DV = `vd_regulier`. Pseudo-R² McFadden = 0.016, N = 1025, événements = 177. Diplôme bac+3+ : OR = 1.22, p = 0.451.

### 3b. Colinéarité entre déterminants sociaux

- V de Cramér diplôme × CSP = **0.29** (association modérée : les deux variables partagent de l'information, ce qui explique l'atténuation de l'effet « cadres » une fois le diplôme introduit).
- Corrélation de Spearman diplôme × budget = **0.06** (faible : le diplôme n'est pas un proxy du budget).

## 4. Intermittence vs abandon + période de terrain (R2, AD-3)

**Période de terrain : septembre** (les questions de récence portent sur « le mois de Septembre »). Mois de pleine saison pour les marchés et les produits locaux : la récence des formes directes est, si biais il y a, plutôt *sur*-estimée que sous-estimée — l'abandon relevé n'est donc pas un artefact de basse saison.

Récence par forme, en distinguant **intermittence** (achète mais pas ce mois-ci) et **abandon vrai** (n'achète plus) :

| Forme | base n | Récent | Intermittence (pas ce mois) | **Abandon vrai** | Jamais/ne connaît |
|-------|:---:|:---:|:---:|:---:|:---:|
| Boulanger (conv.) | 893 | 58% | 21% | **10%** | 11% |
| Marché (producteur) | 810 | 59% | 30% | **6%** | 5% |
| Boucher (conv.) | 893 | 38% | 32% | **17%** | 13% |
| Primeur (conv.) | 893 | 37% | 34% | **17%** | 13% |
| À la ferme | 509 | 34% | 35% | **16%** | 15% |
| Magasin de producteurs | 509 | 20% | 34% | **15%** | 31% |
| Halle commerçante | 509 | 17% | 35% | **19%** | 29% |
| Foire / salon | 509 | 7% | 34% | **18%** | 42% |
| Panier en ligne | 509 | 6% | 11% | **14%** | 70% |

*L'« abandon vrai » (colonne en gras) reste modéré (15–19% pour les formes directes) : l'essentiel du « 46% n'ont pas acheté ce mois-ci » relève de l'intermittence, non du décrochage. Le titre porte sur le passage essai→habitude, que traduit surtout l'intermittence ; le décrochage définitif, lui, est limité.*

### 4b. Sécurisation des chiffres AMAP (Q46)

Q46 « achetez-vous des produits dans le cadre d'une AMAP ? » — base = 509 acheteurs directs. Modalités : 1=Oui, 2=a cessé, 3=jamais, 4=ne connaît pas.

| Statut AMAP | n | % base |
|-------------|---|--------|
| Client actuel (1) | 41 | 8% |
| A cessé (2) | 75 | 15% |
| Jamais (3) | 157 | 31% |
| Ne connaît pas l'AMAP (4) | 236 | 46% |

- **Taux d'abandon AMAP** = 75 / (41+75) clients passés ou présents = **65%** (IC95% Wilson [56–73], n = 116). Effectif faible → à donner avec son n et son IC.
- **Notoriété** : 236/509 = **46%** des acheteurs directs déclarent ne pas savoir ce qu'est une AMAP.

## 5. Ordre de grandeur du gain de conversion (R3-2)

Aujourd'hui, 177 ménages réguliers (17.3%) portent une part nationale de 1.5% à une intensité de 8.5% de leur budget. Si les 332 essayeurs irréguliers (soit 32% des ménages) atteignaient la même régularité et intensité, la part nationale de la vente directe passerait mécaniquement d'environ **1.5% à ≈ 4.2%** — un quasi-triplement. À l'inverse, le potentiel de recrutement est ténu (déjà 65% de pénétration). Le levier budgétaire est donc la conversion, non l'acquisition. *(Calcul illustratif toutes choses égales par ailleurs, intensité des convertis supposée égale à celle des réguliers actuels.)*
