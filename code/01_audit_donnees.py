#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stade 2 — Audit des données réelles (enquête 24407, approvisionnement alimentaire).
Produit un rapport de structure lisible dans articles/stade2_audit_donnees.md.

Aucune donnée individuelle n'est écrite : uniquement des agrégats.
Données brutes : data/raw/24407_Export.xlsx (local, non poussé sur GitHub).
"""
import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "data/raw/24407_Export.xlsx"
OUT = ROOT / "articles/stade2_audit_donnees.md"

# ---- Référentiels (depuis le plan de codage) -------------------------------
CANAUX = {
    1: "Hyper/Super/Supérette grandes enseignes (+ drive)",
    2: "Hard discount (Lidl, Aldi, Leader price…)",
    3: "Épiceries indépendantes, de quartier, fines (+ drive)",
    4: "Magasins de surgelés (Picard, Thiriet, Argel…)",
    5: "Magasins spécialisés Bio (Biocoop, Naturalia…)",
    6: "Marché (agriculteurs, artisans, revendeurs)",
    7: "VENTE DIRECTE aux agriculteurs (AMAP, magasins de producteurs, ferme, paniers précommande, La Ruche…)",
    8: "Paniers en ligne via intermédiaire (Potagercity…)",
    9: "Artisans/commerçants spécialisés (boucher, boulanger, primeur…)",
    10: "Épicerie participative/associative, supermarché coopératif",
    11: "Magasin vrac / produits locaux (Day by day…)",
    12: "Magasin d'aide alimentaire (épicerie sociale/solidaire)",
    13: "Autre",
}
FREQ = {1: "Plusieurs fois/semaine", 2: "1 fois/semaine", 3: "2-3 fois/mois",
        4: "1 fois/mois", 5: "Moins d'1 fois/mois", 6: "Seulement événements",
        7: "Jamais"}
SEXE = {1: "Homme", 2: "Femme", 3: "Autre"}
AGE = {1: "20-24", 2: "25-34", 3: "35-44", 4: "45-54", 5: "55-64", 6: "65 et +"}
CSP = {1: "Agriculteurs/artisans/commerçants/chefs d'ent.",
       2: "Cadres et prof. libérales", 3: "Professions intermédiaires",
       4: "Employés et ouvriers", 5: "Retraités",
       6: "Inactifs/autres (étudiants, sans emploi, au foyer)"}
Q4 = {1: "Oui, intégralement", 2: "Oui, partiellement"}

lines = []
def w(s=""):
    lines.append(s)

# ---- Chargement ------------------------------------------------------------
df = pd.read_excel(XLSX, sheet_name="Données_RepNat")
surplus = pd.read_excel(XLSX, sheet_name="Surplus")
N = len(df)

w("---")
w('title: "Stade 2A — Rapport d\'audit des données"')
w('projet: "Place de la vente directe dans les stratégies d\'approvisionnement"')
w("source: data/raw/24407_Export.xlsx (onglet Données_RepNat)")
w("date: 2026-06-29")
w("statut: \"Audit automatique — à valider (checkpoint)\"")
w("---")
w()
w("# Stade 2A — Audit des données réelles")
w()
w("> Rapport généré par `code/01_audit_donnees.py`. Aucune donnée")
w("> individuelle n'est reproduite — uniquement des agrégats.")
w()
w("## 1. Vue d'ensemble")
w()
w(f"- **Échantillon principal (Données_RepNat)** : **{N} répondants** × {df.shape[1]} variables")
w(f"- **Onglet Surplus** : {len(surplus)} répondants (sur-échantillon — à discuter, exclu par défaut de l'analyse représentative)")
w(f"- **Variables** : socio-démographiques (Q1-Q5 + recodages), fréquence par canal (Q6_1..Q6_13),")
w(f"  budget mensuel (Q8), part de budget par canal (Q9_1..Q9_13), motivations détaillées par canal (Q10+).")
w()

# ---- Profil sociodémographique --------------------------------------------
w("## 2. Profil sociodémographique de l'échantillon")
w()
def distrib(col, labels, titre):
    w(f"**{titre}** (`{col}`)")
    w()
    w("| Modalité | n | % |")
    w("|----------|---|---|")
    vc = df[col].value_counts(dropna=False).sort_index()
    for k, n in vc.items():
        lab = labels.get(k, f"[code {k}]") if not pd.isna(k) else "Manquant"
        w(f"| {lab} | {n} | {100*n/N:.1f}% |")
    w()

distrib("Q1", SEXE, "Sexe")
distrib("recode_age", AGE, "Âge (recodé)")
distrib("recode_csp", CSP, "CSP (recodée)")
distrib("Q4", Q4, "Responsable des achats alimentaires du foyer")

# Géographie (région / taille agglo si présentes)
if "Q5_region" in df.columns:
    nreg = df["Q5_region"].nunique(dropna=True)
    w(f"**Couverture géographique** : {nreg} modalités de région renseignées "
      f"(`Q5_region`), code postal + recodages INSEE/UDA/TUU disponibles.")
    w()

# ---- Budget alimentaire ----------------------------------------------------
w("## 3. Budget alimentaire mensuel du foyer (Q8, en €)")
w()
q8 = pd.to_numeric(df["Q8"], errors="coerce")
w("| Statistique | Valeur |")
w("|-------------|--------|")
w(f"| n renseigné | {q8.notna().sum()} |")
w(f"| Moyenne | {q8.mean():.0f} € |")
w(f"| Médiane | {q8.median():.0f} € |")
w(f"| 1er quartile | {q8.quantile(.25):.0f} € |")
w(f"| 3e quartile | {q8.quantile(.75):.0f} € |")
w(f"| Min – Max | {q8.min():.0f} – {q8.max():.0f} € |")
w()

# ---- Fréquentation par canal (Q6) -----------------------------------------
w("## 4. Fréquentation des canaux (Q6) — le cœur de l'analyse")
w()
w("Échelle Q6 : 1=Plusieurs fois/sem · 2=1 fois/sem · 3=2-3 fois/mois · "
  "4=1 fois/mois · 5=Moins d'1 fois/mois · 6=Événements · 7=Jamais.")
w()
w("- **Pénétration** = % de répondants qui fréquentent le canal (Q6 ≠ 7 *Jamais*).")
w("- **Réguliers** = % qui le fréquentent au moins 1 fois/mois (Q6 ≤ 4).")
w()
w("| # | Canal | Pénétration | Réguliers (≥1×/mois) |")
w("|---|-------|-------------|----------------------|")
penetr = {}
for i in range(1, 14):
    col = f"Q6_{i}"
    if col not in df.columns:
        continue
    s = pd.to_numeric(df[col], errors="coerce")
    pen = (s != 7).sum() / N * 100
    reg = (s <= 4).sum() / N * 100
    penetr[i] = pen
    star = " ⭐" if i == 7 else ""
    w(f"| {i} | {CANAUX[i][:60]}{star} | {pen:.1f}% | {reg:.1f}% |")
w()

# ---- Zoom vente directe et circuits courts --------------------------------
w("## 5. Zoom — vente directe et circuits courts")
w()
w("Trois canaux relèvent des circuits courts / vente directe :")
w()
for i in (6, 7, 8):
    col = f"Q6_{i}"
    s = pd.to_numeric(df[col], errors="coerce")
    w(f"### Canal {i} — {CANAUX[i]}")
    w()
    w("| Fréquence | n | % |")
    w("|-----------|---|---|")
    vc = s.value_counts(dropna=False).sort_index()
    for k, n in vc.items():
        lab = FREQ.get(k, f"[{k}]") if not pd.isna(k) else "Manquant"
        w(f"| {lab} | {n} | {100*n/N:.1f}% |")
    w()

# ---- Part de budget par canal (Q9) ----------------------------------------
w("## 6. Part du budget alimentaire par canal (Q9, en %)")
w()
w("`Q9_x` n'est renseigné que pour les canaux effectivement fréquentés ; "
  "les non-acheteurs sont en valeur manquante (interprétée comme 0% de part).")
w()
w("| # | Canal | Part moy. (tous, NA=0) | Part moy. (acheteurs) | n acheteurs |")
w("|---|-------|------------------------|------------------------|-------------|")
for i in range(1, 14):
    col = f"Q9_{i}"
    if col not in df.columns:
        continue
    s = pd.to_numeric(df[col], errors="coerce")
    buyers = s.notna().sum()
    mean_all = s.fillna(0).mean()
    mean_buy = s.mean() if buyers else float("nan")
    star = " ⭐" if i == 7 else ""
    w(f"| {i} | {CANAUX[i][:48]}{star} | {mean_all:.1f}% | {mean_buy:.1f}% | {buyers} |")
w()
# Cohérence : somme des parts par répondant
q9cols = [f"Q9_{i}" for i in range(1, 14) if f"Q9_{i}" in df.columns]
sums = df[q9cols].apply(pd.to_numeric, errors="coerce").fillna(0).sum(axis=1)
w(f"**Contrôle de cohérence** : somme des parts Q9 par répondant — "
  f"moyenne {sums.mean():.1f}%, médiane {sums.median():.1f}%, "
  f"% à 100±5 : {((sums>=95)&(sums<=105)).mean()*100:.1f}%.")
w()

# ---- Qualité des données ---------------------------------------------------
w("## 7. Qualité des données (valeurs manquantes, variables clés)")
w()
key = ["Q1", "recode_age", "recode_csp", "Q4", "Q8"] + [f"Q6_{i}" for i in range(1, 14)]
w("| Variable | % manquant |")
w("|----------|------------|")
for c in key:
    if c in df.columns:
        miss = df[c].isna().mean() * 100
        w(f"| {c} | {miss:.1f}% |")
w()
w(f"- Doublons de l'identifiant `Num` : {df['Num'].duplicated().sum()}")
w(f"- Lignes entièrement vides : {df.isna().all(axis=1).sum()}")
w()

# ---- Sortie ----------------------------------------------------------------
OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Rapport écrit : {OUT}")
print(f"N={N} | pénétration vente directe (Q6_7≠Jamais) = {penetr.get(7):.1f}%")
