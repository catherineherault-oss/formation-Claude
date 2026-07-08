#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figure « De l'essai à l'adoption » : récence d'achat par forme de vente directe
(4 modalités), comparée à trois circuits conventionnels spécialisés (artisans).
Sortie : figures/png/fig6_essai_ancrage_nb.png (+ svg). N&B, légende au-dessus.
"""
import pandas as pd, numpy as np
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
raw = pd.read_excel(ROOT/"data/raw/24407_Export.xlsx", sheet_name="Données_RepNat")
def num(c): return pd.to_numeric(raw[c], errors="coerce")
plt.rcParams.update({"font.size":10, "font.family":"serif"})

# Codage commun : 1=acheté le mois écoulé, 2=achète mais pas ce mois-ci,
# 3=n'achète plus (a cessé), 4=jamais (5=ne sait pas -> exclu).
CHANS = [("Q100","Boulanger (conv.)"), ("Q22","Marché (au producteur)"),
         ("Q92","Boucher (conv.)"), ("Q121","Primeur (conv.)"),
         ("Q30","À la ferme"), ("Q38","Magasin de producteurs"),
         ("Q61","Halle commerçante"), ("Q70","Foire / salon"),
         ("Q53","Panier en ligne")]
rows=[]
for q,lab in CHANS:
    s=num(q); base=((s>=1)&(s<=4)).sum()
    rows.append((lab, base, *[100*(s==k).sum()/base for k in (1,2,3,4)]))
fd=pd.DataFrame(rows, columns=["canal","base","recent","pas_ce_mois","nachete_plus","jamais"])
fd=fd.sort_values("recent", ascending=False).reset_index(drop=True)

fig,ax=plt.subplots(figsize=(9.5,5))
y=range(len(fd))
segs=[("recent","0.20","Acheté le mois écoulé",None),
      ("pas_ce_mois","0.50","Achète, mais pas ce mois-ci",None),
      ("nachete_plus","0.78","N'achète plus (a cessé)","...."),
      ("jamais","white","Jamais (via cette forme)","////")]
left=np.zeros(len(fd))
for col,c,lbl,h in segs:
    ax.barh(y, fd[col], left=left, color=c, edgecolor="black", hatch=h, label=lbl)
    for i in range(len(fd)):
        if fd[col].iloc[i] > 7:
            ax.text(left[i]+fd[col].iloc[i]/2, i, f"{fd[col].iloc[i]:.0f}",
                    va="center", ha="center", fontsize=7,
                    color="white" if c in ("0.20","0.50") else "black")
    left = left + fd[col].values
ax.set_yticks(list(y))
ax.set_yticklabels([f"{r.canal}  (n={int(r.base)})" for r in fd.itertuples()], fontsize=9)
ax.set_xlim(0,100); ax.set_xlabel("Répartition des personnes interrogées sur la forme (%)")
ax.invert_yaxis()
ax.legend(ncol=2, fontsize=8, loc="lower center", bbox_to_anchor=(0.5,1.02), frameon=False)
fig.savefig(ROOT/"figures/svg/fig6_essai_ancrage_nb.svg", bbox_inches="tight")
fig.savefig(ROOT/"figures/png/fig6_essai_ancrage_nb.png", dpi=300, bbox_inches="tight")
print("Figure récence (4 modalités + artisans) générée.")
print(fd.round(0).to_string(index=False))
