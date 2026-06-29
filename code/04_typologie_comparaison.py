#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stade 2 — Comparaison des solutions de typologie (k = 3, 4, 5, 6).
Aide à trancher entre 4 et 5 classes. Produit un dendrogramme + métriques.
"""
import pandas as pd, numpy as np
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from sklearn.metrics import silhouette_score
import prince

ROOT = Path(__file__).resolve().parent.parent
A = pd.read_pickle(ROOT / "data/processed/analyse.pkl")
CAN = {1:"Hyper",2:"Discount",3:"Épic.indép",4:"Surgelés",5:"Bio",6:"Marché",
       7:"VteDirecte",8:"Paniers",9:"Artisans",10:"Coop",11:"Vrac"}

active = [f"cat_{i}" for i in range(1, 12)]
X = A[active].astype(str)
mca = prince.MCA(n_components=5, random_state=42).fit(X)
C = mca.row_coordinates(X).values
Z = linkage(C, method="ward")

print("=== Silhouette (sur 5 axes ACM) ===")
for k in (3, 4, 5, 6):
    lab = fcluster(Z, k, criterion="maxclust")
    sil = silhouette_score(C, lab)
    sizes = pd.Series(lab).value_counts().sort_index().to_dict()
    print(f"k={k} : silhouette={sil:.3f} | effectifs={sizes}")

print("\n=== Profils k=4 (pénétration % par canal + %VD + budget) ===")
def profils(k):
    lab = fcluster(Z, k, criterion="maxclust")
    A["c"] = lab
    rows = []
    for cl in sorted(set(lab)):
        sub = A[A["c"] == cl]
        prof = {CAN[i]: round(100*sub[f"penet_{i}"].mean()) for i in range(1, 12)}
        prof["n"] = len(sub)
        prof["%VD"] = round(100*sub["vente_directe"].mean())
        prof["budget"] = round(sub["budget_eur"].mean())
        rows.append((cl, prof))
    return rows

for cl, prof in profils(4):
    print(f"\nC{cl} (n={prof['n']}, %VD={prof['%VD']}, budget={prof['budget']}€)")
    print("  " + " ".join(f"{k}:{prof[k]}" for k in CAN.values()))

print("\n=== Profils k=5 (rappel) ===")
for cl, prof in profils(5):
    print(f"C{cl} (n={prof['n']}, %VD={prof['%VD']}, budget={prof['budget']}€) "
          + " ".join(f"{k}:{prof[k]}" for k in CAN.values()))

# Dendrogramme
fig, ax = plt.subplots(figsize=(9, 4))
dendrogram(Z, truncate_mode="lastp", p=20, ax=ax, color_threshold=0,
           above_threshold_color="#5b8db8")
ax.set_title("Dendrogramme CAH (Ward, 20 dernières fusions)")
ax.set_xlabel("Classes agrégées"); ax.set_ylabel("Distance de fusion")
fig.savefig(ROOT/"figures/svg/figS_dendrogramme.svg", bbox_inches="tight")
fig.savefig(ROOT/"figures/png/figS_dendrogramme.png", dpi=300, bbox_inches="tight")
plt.close(fig)
print("\nDendrogramme écrit : figures/png/figS_dendrogramme.png")
