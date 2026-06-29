---
title: "Stade 2B — Alignement question de recherche ↔ données"
date: 2026-06-29
statut: "À valider (checkpoint)"
---

# Stade 2B — Alignement RQ ↔ données réelles

L'enquête 24407 colle **remarquablement bien** à la question de recherche.
Voici, sous-question par sous-question, ce que les données permettent.

## Correspondance sous-questions ↔ variables

| Sous-question (Stade 1) | Variables disponibles | Mesurable ? |
|--------------------------|------------------------|-------------|
| **SQ1 — Architecture des canaux** : quels canaux combinés, à quelle fréquence | `Q6_1..Q6_13` (fréquence, échelle 1-7) | ✅ Pleinement |
| **SQ2 — Part dans le budget** : part du budget en vente directe selon les profils | `Q9_1..Q9_13` (% par canal) + `Q8` (budget €) + socio-démo | ✅ Pleinement (parts cohérentes, somme = 100%) |
| **SQ3 — Logique de répartition** : critères d'arbitrage entre canaux | Motivations par canal (Q21+), raisons de non-achat (Q10-20, texte libre) | ✅ Oui (motivations structurées + verbatims) |
| **SQ4 — Profils de stratégies** : typologie d'approvisionnement | `Q6_1..Q6_13` → ACM + CAH ; profils croisés socio-démo | ✅ Pleinement |
| **SQ5 — Évolutions récentes** (COVID, inflation) | ⚠️ Pas de variable temporelle directe (enquête transversale) | ⚠️ Partiel — à traiter en discussion, pas en résultat |

**Verdict :** 4 sous-questions sur 5 sont directement mesurables. La SQ5
(évolutions temporelles) ne peut pas être testée — l'enquête est
transversale (un seul point dans le temps). Je propose de la **reléguer à
la discussion** (mise en perspective avec la littérature post-COVID) plutôt
que d'en faire un résultat empirique. 

## Ce que les données disent déjà (aperçu, à confirmer en analyse)

L'audit livre un premier résultat qui **conforte l'hypothèse H1** :

- **L'hypermarché reste hégémonique** : 99 % de pénétration, **58 % du
  budget alimentaire** moyen.
- **La vente directe (canal 7) est répandue mais marginale en budget** :
  fréquentée par **49,7 %** des ménages, mais seulement **17,3 %** la
  fréquentent au moins une fois par mois, et elle ne pèse que **1,5 % du
  budget moyen** (8,5 % chez ses seuls acheteurs).
- Les circuits courts au sens large (marché + vente directe + paniers)
  pèsent davantage par la **fréquentation occasionnelle** que par la
  **part de budget** → signature typique d'un **canal de complémentarité
  ciblée**, pas de substitution.

→ C'est exactement la thèse « la vente directe occupe rarement la place de
canal principal ». Les données la soutiennent ; reste à la **quantifier
proprement** et à identifier **qui** s'en écarte (les profils où la vente
directe pèse réellement).

## Plan d'analyse révisé (vraies données)

| # | Analyse | Méthode | Variables | Sortie |
|---|---------|---------|-----------|--------|
| A1 | Description du portefeuille de canaux | Stats descriptives, pénétration, parts | Q6_*, Q9_*, Q8 | Tableau + figure barres |
| A2 | Place de la vente directe | Focus canaux 6/7/8, distribution de fréquence et de part | Q6_6/7/8, Q9_6/7/8 | Figure + tableau |
| A3 | **Typologie des stratégies d'approvisionnement** | ACM sur Q6_* puis CAH | Q6_1..Q6_13 | 4-5 classes + figure plan factoriel |
| A4 | Profil socio-éco des classes | Tris croisés + tests χ² | classes × Q1/age/CSP/Q8/géo | Tableau de profils |
| A5 | **Déterminants de l'usage de la vente directe** | Régression logistique (acheteur vente directe O/N) | Q6_7 dichotomisé ~ socio-démo | Tableau odds-ratios |
| A6 | Motivations des acheteurs en vente directe | Analyse des classements Q21+ / raisons | motivations par canal | Tableau hiérarchisé |

Chaque analyse produira une figure en **SVG (vectoriel) + PNG (300 dpi)**
selon vos préférences, et toutes les sorties chiffrées seront **réelles et
reproductibles** depuis `code/`.

## Points à trancher avec vous

1. **Onglet « Surplus » (75 répondants)** : exclu par défaut de l'analyse
   représentative nationale. À confirmer (sinon je peux l'intégrer en
   analyse de robustesse).
2. **Définition de « vente directe »** : strictement le canal 7
   (directement aux agriculteurs) ? Ou élargie au marché auprès
   d'agriculteurs (canal 6) et aux paniers via intermédiaire (canal 8) ?
   Cela change le périmètre des résultats.
3. **SQ5 (évolutions temporelles)** : confirmée en discussion seulement
   (pas de données longitudinales).
