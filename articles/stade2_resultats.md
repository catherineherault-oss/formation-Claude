---
title: "Stade 2C — Résultats d'analyse (données réelles)"
date: 2026-06-29
source: enquête 24407, N=1025, échantillon représentatif national
statut: "Résultats reproductibles — à valider (checkpoint)"
---

# Stade 2C — Résultats

> Généré par `code/03_analyses.py` à partir de `data/processed/analyse.pkl`.
> **Définition vente directe (VD)** : achat direct aux agriculteurs (canal 7, Q6_7≠Jamais)
> OU achat direct au producteur sur les marchés (Q22=1). VD = **666 répondants (65.0%)**.

## A1 — Le portefeuille de canaux des ménages

| # | Canal | Pénétration | Réguliers (≥1×/mois) | Part budget moy. |
|---|-------|-------------|----------------------|------------------|
| 1 | Hyper/Super | 99.1% | 97.5% | 58.5% |
| 2 | Hard discount | 86.5% | 64.2% | 15.6% |
| 3 | Épiceries indép. | 68.6% | 35.2% | 3.1% |
| 4 | Surgelés | 74.3% | 36.0% | 3.7% |
| 5 | Bio spécialisé | 57.4% | 24.2% | 2.3% |
| 6 | Marché | 78.8% | 41.4% | 4.8% |
| 7 | Vente directe agri ⭐ | 49.7% | 17.3% | 1.5% |
| 8 | Paniers interm. | 15.7% | 5.8% | 0.4% |
| 9 | Artisans/comm. | 87.1% | 61.9% | 7.6% |
| 10 | Coop./participatif | 22.9% | 7.0% | 0.4% |
| 11 | Vrac/locaux | 21.5% | 8.7% | 0.5% |
| 12 | Aide alimentaire | 12.3% | 5.3% | 0.4% |
| 13 | Autre | 8.9% | 6.3% | 1.3% |

Nombre moyen de canaux fréquentés par ménage : **6.8**.

![Figure 1](../figures/png/fig1_part_budget_canal.png)
*Figure 1 — Part moyenne du budget alimentaire par canal. La vente directe (rouge) est marginale en budget.*

## A2 — La place de la vente directe

| Composante | n | % de l'échantillon |
|------------|---|--------------------|
| VD via canal 7 (direct agriculteurs) | 509 | 49.7% |
| VD via marché direct producteur (Q22=1) | 478 | 46.6% |
| **VD (union, définition retenue)** | **666** | **65.0%** |
| dont VD régulière (canal 7 ≥1×/mois) | 177 | 17.3% |

**Paradoxe central** : la vente directe touche **2 ménages sur 3** mais ne pèse que **1.5% du budget** alimentaire (part propre du canal 7 ; la fraction directe des achats sur marché n'est pas isolable dans Q9_6 — *caveat*). → canal de complémentarité, non de substitution.

![Figure 2](../figures/png/fig2_frequence_canal7.png)
*Figure 2 — Fréquence d'achat en vente directe aux agriculteurs (canal 7).*

## A3 — Typologie des stratégies d'approvisionnement (ACM + CAH)

ACM sur 11 canaux (3 niveaux), CAH de Ward en **5 classes** sur 5 axes factoriels.

**Taux de fréquentation (pénétration) par canal et par classe :**

| Classe (n) | Hyper/Super | Hard discount | Épiceries indép. | Surgelés | Bio spécialisé | Marché | Vente directe agri | Paniers interm. | Artisans/comm. | Coop./participatif | Vrac/locaux | % VD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 (n=624) | 100 | 91 | 80 | 84 | 66 | 91 | 55 | 8 | 96 | 19 | 15 | 72% |
| C2 (n=79) | 100 | 97 | 100 | 94 | 96 | 95 | 92 | 87 | 94 | 87 | 92 | 97% |
| C3 (n=249) | 100 | 71 | 25 | 41 | 15 | 38 | 14 | 2 | 60 | 0 | 2 | 28% |
| C4 (n=47) | 100 | 98 | 96 | 100 | 100 | 100 | 98 | 74 | 96 | 94 | 91 | 100% |
| C5 (n=26) | 65 | 77 | 62 | 65 | 58 | 81 | 42 | 15 | 88 | 19 | 15 | 81% |

![Figure 3](../figures/png/fig3_plan_factoriel.png)
*Figure 3 — Plan factoriel (axes 1-2) de l'ACM, coloré par classe de stratégie.*

## A4 — Profil socio-économique des classes

**CSP × classe** (% en ligne)

| Classe | Cadres/prof.lib | Employés/ouvriers | Inactifs/autres | Indép./agri | Prof. interm. | Retraités |
|---|---|---|---|---|---|---|
| C1 | 11% | 28% | 9% | 5% | 18% | 30% |
| C2 | 19% | 41% | 10% | 4% | 14% | 13% |
| C3 | 7% | 33% | 16% | 4% | 9% | 30% |
| C4 | 21% | 30% | 9% | 6% | 19% | 15% |
| C5 | 8% | 27% | 4% | 0% | 19% | 42% |

χ²(p) = 0.0001 (significatif)

**Âge × classe** (% en ligne)

| Classe | 20-24 | 25-34 | 35-44 | 45-54 | 55-64 | 65+ |
|---|---|---|---|---|---|---|
| C1 | 7% | 15% | 16% | 18% | 17% | 27% |
| C2 | 14% | 25% | 24% | 18% | 10% | 9% |
| C3 | 7% | 14% | 19% | 15% | 15% | 29% |
| C4 | 9% | 21% | 15% | 30% | 11% | 15% |
| C5 | 8% | 15% | 4% | 15% | 23% | 35% |

χ²(p) = 0.0048 (significatif)

**Budget alimentaire mensuel moyen par classe :**

| Classe | Budget moyen (€) | % vente directe |
|--------|------------------|-----------------|
| C1 | 439 € | 72% |
| C2 | 513 € | 97% |
| C3 | 408 € | 28% |
| C4 | 480 € | 100% |
| C5 | 320 € | 81% |

## A5 — Déterminants de l'usage de la vente directe (régression logistique)

Modèle : `vente_directe ~ C(sexe) + C(age) + C(csp) + budget_z + tuu_z`. Pseudo-R² (McFadden) = 0.022, N = 1025.

| Variable | Odds-ratio | IC95% | p |
|----------|-----------|-------|---|
| sexe=Femme | 0.91 | [0.70–1.18] | 0.478 |
| age=25-34 | 1.00 | [0.56–1.79] | 0.991 |
| age=35-44 | 0.87 | [0.49–1.55] | 0.638 |
| age=45-54 | 0.98 | [0.55–1.74] | 0.953 |
| age=55-64 | 1.02 | [0.57–1.84] | 0.936 |
| age=65+ | 1.09 | [0.43–2.81] | 0.851 |
| csp=Indép./agri | 1.06 | [0.56–2.01] | 0.866 |
| csp=Cadres/prof.lib | **2.16** | [1.31–3.55] | 0.003 |
| csp=Prof. interm. | **1.60** | [1.06–2.41] | 0.027 |
| csp=Retraités | 1.42 | [0.62–3.24] | 0.406 |
| csp=Inactifs/autres | 0.82 | [0.52–1.30] | 0.407 |
| budget_z | **1.18** | [1.02–1.37] | 0.028 |
| tuu_z | 0.97 | [0.85–1.11] | 0.635 |

*Lecture : OR>1 = probabilité accrue d'acheter en vente directe. Référence : Homme, 20-24 ans, Employés/ouvriers. En gras = p<0,05.*

![Figure 4](../figures/png/fig4_regression_or.png)
*Figure 4 — Odds-ratios (rouge = significatif à 5%). Référence : Homme, 20-24 ans, Employés/ouvriers.*

## A6 — Motivations d'achat sur les marchés (Q21, population marché)

Base : 810 répondants fréquentant les marchés et ayant classé leurs motivations.
Fréquence de citation dans le top 3 :

| Rang | Motivation | Citations top-3 | % base |
|------|-----------|-----------------|--------|
| 1 | Produits locaux | 414 | 51% |
| 2 | Produits circuit court | 332 | 41% |
| 3 | Goût des produits | 314 | 39% |
| 4 | Soutenir agriculteurs/éco. locale | 272 | 34% |
| 5 | Prix, promotions | 145 | 18% |
| 6 | Qualité nutritionnelle | 140 | 17% |
| 8 | Proximité du lieu | 114 | 14% |

![Figure 5](../figures/png/fig5_motivations_marche.png)
*Figure 5 — Principales motivations d'achat sur les marchés (classement top 3).*
