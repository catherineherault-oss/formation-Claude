#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
De l'essai à l'ancrage : récence d'achat par forme de vente directe.
Compare la fréquentation déclarée (Q6_7) aux questions détaillées par forme
(Q22 marché, Q30 ferme, Q38 magasin de producteurs, Q46 AMAP, Q53 panier,
Q61 halle, Q70 foire/salon), dont la modalité 1 = « acheté au cours du mois
de septembre » (achat récent/actif).

Sortie : tableau chiffré (stdout) + figures/png/fig6_essai_ancrage_nb.png (+ svg).
Aucune donnée individuelle écrite.
"""
import pandas as pd, numpy as np
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
df = pd.read_excel(ROOT/"data/raw/24407_Export.xlsx", sheet_name="Données_RepNat")
def num(c): return pd.to_numeric(df[c], errors="coerce")
plt.rcParams.update({"font.size":10, "font.family":"serif"})

# Formes à split « septembre » : 1=récent, 2=achète mais pas ce mois, 3=a cessé, 4=jamais, (5=ne sait pas)
FORMES = [("Q22","Marché (au producteur)"), ("Q30","À la ferme"),
          ("Q38","Magasin de producteurs"), ("Q61","Halle commerçante"),
          ("Q53","Panier en ligne (La Ruche…)"), ("Q70","Foire / salon")]

print("Forme | ont déjà essayé | récent(mois) | achète mais pas ce mois | a cessé")
data=[]
for q,lab in FORMES:
    s=num(q); ever=int(((s>=1)&(s<=3)).sum())
    rec,notrec,stop=int((s==1).sum()),int((s==2).sum()),int((s==3).sum())
    data.append((lab, 100*rec/ever, 100*notrec/ever, 100*stop/ever, ever))
    print(f"{lab:<28} ever={ever:>4} | {100*rec/ever:>4.0f}% | {100*notrec/ever:>4.0f}% | {100*stop/ever:>4.0f}%")

# AMAP : codage différent (1=Oui actuel, 2=a cessé, 3=jamais, 4=ne sait pas)
a=num("Q46"); ever_a=int(((a==1)|(a==2)).sum())
print(f"{'AMAP (Oui/cessé)':<28} ever={ever_a:>4} | actuel {100*(a==1).sum()/ever_a:.0f}% | cessé {100*(a==2).sum()/ever_a:.0f}%")

# Agrégat : parmi les déclarants VD agriculteurs (Q6_7 != Jamais), part ayant acheté récemment
q67=num("Q6_7"); base=(q67!=7)
anyrec=pd.concat([(num(q)==1) for q in ["Q30","Q38","Q53","Q61","Q70"]]+[(num("Q46")==1)],axis=1).any(axis=1)
print(f"\nDéclarent fréquenter la VD agriculteurs (Q6_7≠Jamais) : {int(base.sum())}")
print(f"  … ont acheté au cours du mois (≥1 forme) : {int((base&anyrec).sum())} "
      f"({100*(base&anyrec).sum()/base.sum():.0f}%)")
print(f"  … n'ont rien acheté récemment            : {int((base&~anyrec).sum())} "
      f"({100*(base&~anyrec).sum()/base.sum():.0f}%)")

# ---- Figure 6 (N&B, barres empilées 100 %) ---------------------------------
data.sort(key=lambda r:r[1])
labs=[d[0] for d in data]; rec=[d[1] for d in data]; notrec=[d[2] for d in data]; stop=[d[3] for d in data]
fig,ax=plt.subplots(figsize=(9,4.5)); y=range(len(labs))
ax.barh(y,rec,color="0.25",edgecolor="black",label="A acheté au cours du mois (récent)")
ax.barh(y,notrec,left=rec,color="0.6",edgecolor="black",label="Achète encore, mais pas ce mois-ci")
ax.barh(y,stop,left=[rec[i]+notrec[i] for i in y],color="white",edgecolor="black",
        hatch="////",label="En achetait, mais plus maintenant")
for i in y:
    if rec[i]>6: ax.text(rec[i]/2,i,f"{rec[i]:.0f}%",va="center",ha="center",color="white",fontsize=8)
    if stop[i]>6: ax.text(rec[i]+notrec[i]+stop[i]/2,i,f"{stop[i]:.0f}%",va="center",ha="center",fontsize=8)
ax.set_yticks(list(y)); ax.set_yticklabels([f"{labs[i]} (n={data[i][4]})" for i in y])
ax.set_xlabel("Répartition des ménages ayant DÉJÀ acheté via cette forme (%)")
ax.set_title("De l'essai à l'ancrage — récence d'achat par forme de vente directe")
ax.legend(fontsize=8,loc="lower right",framealpha=1); ax.set_xlim(0,100)
fig.savefig(ROOT/"figures/svg/fig6_essai_ancrage_nb.svg",bbox_inches="tight")
fig.savefig(ROOT/"figures/png/fig6_essai_ancrage_nb.png",dpi=300,bbox_inches="tight")
print("\nFigure écrite : figures/png/fig6_essai_ancrage_nb.png")
