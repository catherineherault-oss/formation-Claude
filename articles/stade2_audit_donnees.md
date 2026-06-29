---
title: "Stade 2A — Rapport d'audit des données"
projet: "Place de la vente directe dans les stratégies d'approvisionnement"
source: data/raw/24407_Export.xlsx (onglet Données_RepNat)
date: 2026-06-29
statut: "Audit automatique — à valider (checkpoint)"
---

# Stade 2A — Audit des données réelles

> Rapport généré par `code/01_audit_donnees.py`. Aucune donnée
> individuelle n'est reproduite — uniquement des agrégats.

## 1. Vue d'ensemble

- **Échantillon principal (Données_RepNat)** : **1025 répondants** × 406 variables
- **Onglet Surplus** : 75 répondants (sur-échantillon — à discuter, exclu par défaut de l'analyse représentative)
- **Variables** : socio-démographiques (Q1-Q5 + recodages), fréquence par canal (Q6_1..Q6_13),
  budget mensuel (Q8), part de budget par canal (Q9_1..Q9_13), motivations détaillées par canal (Q10+).

## 2. Profil sociodémographique de l'échantillon

**Sexe** (`Q1`)

| Modalité | n | % |
|----------|---|---|
| Homme | 486 | 47.4% |
| Femme | 539 | 52.6% |

**Âge (recodé)** (`recode_age`)

| Modalité | n | % |
|----------|---|---|
| 20-24 | 78 | 7.6% |
| 25-34 | 162 | 15.8% |
| 35-44 | 172 | 16.8% |
| 45-54 | 180 | 17.6% |
| 55-64 | 166 | 16.2% |
| 65 et + | 267 | 26.0% |

**CSP (recodée)** (`recode_csp`)

| Modalité | n | % |
|----------|---|---|
| Agriculteurs/artisans/commerçants/chefs d'ent. | 46 | 4.5% |
| Cadres et prof. libérales | 114 | 11.1% |
| Professions intermédiaires | 159 | 15.5% |
| Employés et ouvriers | 308 | 30.0% |
| Retraités | 288 | 28.1% |
| Inactifs/autres (étudiants, sans emploi, au foyer) | 110 | 10.7% |

**Responsable des achats alimentaires du foyer** (`Q4`)

| Modalité | n | % |
|----------|---|---|
| Oui, intégralement | 759 | 74.0% |
| Oui, partiellement | 266 | 26.0% |

**Couverture géographique** : 12 modalités de région renseignées (`Q5_region`), code postal + recodages INSEE/UDA/TUU disponibles.

## 3. Budget alimentaire mensuel du foyer (Q8, en €)

| Statistique | Valeur |
|-------------|--------|
| n renseigné | 1025 |
| Moyenne | 436 € |
| Médiane | 400 € |
| 1er quartile | 250 € |
| 3e quartile | 550 € |
| Min – Max | 1 – 4000 € |

## 4. Fréquentation des canaux (Q6) — le cœur de l'analyse

Échelle Q6 : 1=Plusieurs fois/sem · 2=1 fois/sem · 3=2-3 fois/mois · 4=1 fois/mois · 5=Moins d'1 fois/mois · 6=Événements · 7=Jamais.

- **Pénétration** = % de répondants qui fréquentent le canal (Q6 ≠ 7 *Jamais*).
- **Réguliers** = % qui le fréquentent au moins 1 fois/mois (Q6 ≤ 4).

| # | Canal | Pénétration | Réguliers (≥1×/mois) |
|---|-------|-------------|----------------------|
| 1 | Hyper/Super/Supérette grandes enseignes (+ drive) | 99.1% | 97.5% |
| 2 | Hard discount (Lidl, Aldi, Leader price…) | 86.5% | 64.2% |
| 3 | Épiceries indépendantes, de quartier, fines (+ drive) | 68.6% | 35.2% |
| 4 | Magasins de surgelés (Picard, Thiriet, Argel…) | 74.3% | 36.0% |
| 5 | Magasins spécialisés Bio (Biocoop, Naturalia…) | 57.4% | 24.2% |
| 6 | Marché (agriculteurs, artisans, revendeurs) | 78.8% | 41.4% |
| 7 | VENTE DIRECTE aux agriculteurs (AMAP, magasins de producteur ⭐ | 49.7% | 17.3% |
| 8 | Paniers en ligne via intermédiaire (Potagercity…) | 15.7% | 5.8% |
| 9 | Artisans/commerçants spécialisés (boucher, boulanger, primeu | 87.1% | 61.9% |
| 10 | Épicerie participative/associative, supermarché coopératif | 22.9% | 7.0% |
| 11 | Magasin vrac / produits locaux (Day by day…) | 21.5% | 8.7% |
| 12 | Magasin d'aide alimentaire (épicerie sociale/solidaire) | 12.3% | 5.3% |
| 13 | Autre | 8.9% | 6.3% |

## 5. Zoom — vente directe et circuits courts

Trois canaux relèvent des circuits courts / vente directe :

### Canal 6 — Marché (agriculteurs, artisans, revendeurs)

| Fréquence | n | % |
|-----------|---|---|
| Plusieurs fois/semaine | 18 | 1.8% |
| 1 fois/semaine | 162 | 15.8% |
| 2-3 fois/mois | 118 | 11.5% |
| 1 fois/mois | 126 | 12.3% |
| Moins d'1 fois/mois | 217 | 21.2% |
| Seulement événements | 167 | 16.3% |
| Jamais | 217 | 21.2% |

### Canal 7 — VENTE DIRECTE aux agriculteurs (AMAP, magasins de producteurs, ferme, paniers précommande, La Ruche…)

| Fréquence | n | % |
|-----------|---|---|
| Plusieurs fois/semaine | 11 | 1.1% |
| 1 fois/semaine | 39 | 3.8% |
| 2-3 fois/mois | 57 | 5.6% |
| 1 fois/mois | 70 | 6.8% |
| Moins d'1 fois/mois | 164 | 16.0% |
| Seulement événements | 168 | 16.4% |
| Jamais | 516 | 50.3% |

### Canal 8 — Paniers en ligne via intermédiaire (Potagercity…)

| Fréquence | n | % |
|-----------|---|---|
| 1 fois/semaine | 22 | 2.1% |
| 2-3 fois/mois | 14 | 1.4% |
| 1 fois/mois | 23 | 2.2% |
| Moins d'1 fois/mois | 45 | 4.4% |
| Seulement événements | 57 | 5.6% |
| Jamais | 864 | 84.3% |

## 6. Part du budget alimentaire par canal (Q9, en %)

`Q9_x` n'est renseigné que pour les canaux effectivement fréquentés ; les non-acheteurs sont en valeur manquante (interprétée comme 0% de part).

| # | Canal | Part moy. (tous, NA=0) | Part moy. (acheteurs) | n acheteurs |
|---|-------|------------------------|------------------------|-------------|
| 1 | Hyper/Super/Supérette grandes enseignes (+ drive | 58.5% | 60.0% | 999 |
| 2 | Hard discount (Lidl, Aldi, Leader price…) | 15.6% | 24.3% | 658 |
| 3 | Épiceries indépendantes, de quartier, fines (+ d | 3.1% | 8.8% | 361 |
| 4 | Magasins de surgelés (Picard, Thiriet, Argel…) | 3.7% | 10.1% | 369 |
| 5 | Magasins spécialisés Bio (Biocoop, Naturalia…) | 2.3% | 9.7% | 248 |
| 6 | Marché (agriculteurs, artisans, revendeurs) | 4.8% | 11.7% | 424 |
| 7 | VENTE DIRECTE aux agriculteurs (AMAP, magasins d ⭐ | 1.5% | 8.5% | 177 |
| 8 | Paniers en ligne via intermédiaire (Potagercity… | 0.4% | 6.1% | 59 |
| 9 | Artisans/commerçants spécialisés (boucher, boula | 7.6% | 12.2% | 634 |
| 10 | Épicerie participative/associative, supermarché  | 0.4% | 5.7% | 72 |
| 11 | Magasin vrac / produits locaux (Day by day…) | 0.5% | 5.8% | 89 |
| 12 | Magasin d'aide alimentaire (épicerie sociale/sol | 0.4% | 6.8% | 54 |
| 13 | Autre | 1.3% | 20.7% | 65 |

**Contrôle de cohérence** : somme des parts Q9 par répondant — moyenne 100.0%, médiane 100.0%, % à 100±5 : 100.0%.

## 7. Qualité des données (valeurs manquantes, variables clés)

| Variable | % manquant |
|----------|------------|
| Q1 | 0.0% |
| recode_age | 0.0% |
| recode_csp | 0.0% |
| Q4 | 0.0% |
| Q8 | 0.0% |
| Q6_1 | 0.0% |
| Q6_2 | 0.0% |
| Q6_3 | 0.0% |
| Q6_4 | 0.0% |
| Q6_5 | 0.0% |
| Q6_6 | 0.0% |
| Q6_7 | 0.0% |
| Q6_8 | 0.0% |
| Q6_9 | 0.0% |
| Q6_10 | 0.0% |
| Q6_11 | 0.0% |
| Q6_12 | 0.0% |
| Q6_13 | 0.0% |

- Doublons de l'identifiant `Num` : 0
- Lignes entièrement vides : 0
