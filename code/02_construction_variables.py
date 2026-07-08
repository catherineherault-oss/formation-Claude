#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stade 2 — Construction des variables d'analyse (enquête 24407).

Décisions verrouillées (checkpoint 2026-06-29) :
  • Échantillon : Données_RepNat uniquement (N=1025). Surplus EXCLU.
  • Vente directe (VD) = (Q6_7 ≠ Jamais)  OU  (Q22 == 1)
        - Q6_7 : achat direct aux agriculteurs (AMAP, magasin de producteurs,
          ferme, paniers précommande type La Ruche)
        - Q22==1 : sur les marchés, achète directement au producteur ET en a
          acheté au cours du mois de septembre (acheteur actif)

Sortie : data/processed/analyse.parquet  (individuel → local, non poussé).
"""
import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "data/raw/24407_Export.xlsx"
OUTDIR = ROOT / "data/processed"
OUTDIR.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(XLSX, sheet_name="Données_RepNat")
N = len(df)

def num(c):
    return pd.to_numeric(df[c], errors="coerce")

a = pd.DataFrame(index=df.index)
a["id"] = df["Num"]

# ---- Socio-démographique ---------------------------------------------------
a["sexe"] = num("Q1").map({1: "Homme", 2: "Femme", 3: "Autre"})
a["age"] = num("recode_age").map({1: "20-24", 2: "25-34", 3: "35-44",
                                  4: "45-54", 5: "55-64", 6: "65+"})
a["csp"] = num("recode_csp").map({
    1: "Indép./agri", 2: "Cadres/prof.lib", 3: "Prof. interm.",
    4: "Employés/ouvriers", 5: "Retraités", 6: "Inactifs/autres"})
a["responsable_achats"] = num("Q4").map({1: "Intégralement", 2: "Partiellement"})
a["budget_eur"] = num("Q8")
# Diplôme (Q240) recodé en 4 niveaux : Infra-bac / Bac / Bac+2 / Bac+3 et plus
a["diplome"] = pd.cut(num("Q240"), bins=[0, 3, 4, 5, 8],
                      labels=["Infra-bac", "Bac", "Bac+2", "Bac+3 et plus"])
# Taille d'unité urbaine si disponible
if "Q5_tuu" in df.columns:
    a["tuu"] = num("Q5_tuu")
if "Q5_region" in df.columns:
    a["region"] = df["Q5_region"]
if "Q5_uda9" in df.columns:
    a["uda9"] = df["Q5_uda9"]

# ---- Fréquence par canal (Q6_1..Q6_13), échelle 1..7 -----------------------
CANAUX = {
    1: "Hyper/Super", 2: "Hard discount", 3: "Épiceries indép.",
    4: "Surgelés", 5: "Bio spécialisé", 6: "Marché", 7: "Vente directe agri",
    8: "Paniers interm.", 9: "Artisans/commerçants", 10: "Coop./participatif",
    11: "Vrac/locaux", 12: "Aide alimentaire", 13: "Autre"}
for i in range(1, 14):
    f = num(f"Q6_{i}")
    a[f"freq_{i}"] = f                          # 1..7 brut
    a[f"penet_{i}"] = (f != 7).astype(int)      # fréquente (≠ Jamais)
    a[f"reg_{i}"] = (f <= 4).astype(int)        # ≥ 1 fois/mois
    # Recodage 3 niveaux pour ACM
    a[f"cat_{i}"] = pd.cut(f, bins=[0, 4, 6, 7],
                           labels=["Régulier", "Occasionnel", "Jamais"])

# ---- Part de budget par canal (Q9_1..Q9_13), NA = 0 ------------------------
for i in range(1, 14):
    a[f"part_{i}"] = num(f"Q9_{i}").fillna(0.0)

# ---- VARIABLE CIBLE : vente directe ---------------------------------------
q6_7 = num("Q6_7")
q22 = num("Q22")
a["vd_canal7"] = (q6_7 != 7).astype(int)
a["vd_marche_direct"] = (q22 == 1).astype(int)
a["vente_directe"] = ((q6_7 != 7) | (q22 == 1)).astype(int)

# Intensité VD (pour analyses secondaires) : régulier sur canal 7
a["vd_regulier"] = (q6_7 <= 4).astype(int)

# Part de budget « direct producteur » identifiable proprement = Q9_7 seul
# (la part directe au sein du marché Q9_6 n'est pas isolable → caveat)
a["part_vd_canal7"] = num("Q9_7").fillna(0.0)

# ---- Sauvegarde ------------------------------------------------------------
out = OUTDIR / "analyse.pkl"
a.to_pickle(out)

print(f"Jeu d'analyse construit : {out}")
print(f"N = {len(a)}")
print(f"Vente directe (définition retenue) : {a['vente_directe'].sum()} "
      f"({100*a['vente_directe'].mean():.1f}%)")
print(f"  • via canal 7        : {a['vd_canal7'].sum()}")
print(f"  • via marché Q22==1  : {a['vd_marche_direct'].sum()}")
print(f"  • apport propre Q22  : {((a['vd_marche_direct']==1)&(a['vd_canal7']==0)).sum()}")
print(f"Part budget direct-producteur (canal 7, moy.) : {a['part_vd_canal7'].mean():.1f}%")
