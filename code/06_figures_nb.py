#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figures en NOIR ET BLANC pour la soumission Décisions Marketing
(N&B, hachures plutôt que dégradés de gris). Sorties : figures/png/*_nb.png (+ svg).
"""
import pandas as pd, numpy as np
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster
import statsmodels.formula.api as smf
import prince

ROOT=Path(__file__).resolve().parent.parent
A=pd.read_pickle(ROOT/"data/processed/analyse.pkl")
raw=pd.read_excel(ROOT/"data/raw/24407_Export.xlsx",sheet_name="Données_RepNat")
FIGP=ROOT/"figures/png"; FIGS=ROOT/"figures/svg"
plt.rcParams.update({"font.size":10,"font.family":"serif","axes.grid":False})

def save(fig,name):
    fig.savefig(FIGS/f"{name}.svg",bbox_inches="tight")
    fig.savefig(FIGP/f"{name}.png",dpi=300,bbox_inches="tight")
    plt.close(fig)

CAN={1:"Hyper/Super",2:"Hard discount",3:"Épiceries indép.",4:"Surgelés",
 5:"Bio spécialisé",6:"Marché",7:"Vente directe agri.",8:"Paniers interm.",
 9:"Artisans/comm.",10:"Coop./participatif",11:"Vrac/locaux",12:"Aide alim.",13:"Autre"}

# ---- Fig 1 : part de budget par canal (N&B) --------------------------------
rows=[(i,CAN[i],A[f"part_{i}"].mean()) for i in range(1,14)]
rows.sort(key=lambda r:r[2])
fig,ax=plt.subplots(figsize=(8,5))
for y,(i,lab,val) in enumerate(rows):
    hatch="////" if i==7 else None
    col="0.25" if i==7 else "0.6"
    ax.barh(y,val,color=col,edgecolor="black",hatch=hatch)
    ax.text(val+0.4,y,f"{val:.1f}%",va="center",fontsize=8)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[1] for r in rows])
ax.set_xlabel("Part moyenne du budget alimentaire (%)")
ax.set_title("Part du budget alimentaire par canal (n = 1 025)")
save(fig,"fig1_part_budget_canal_nb")

# ---- Fig 2 : fréquence canal 7 (N&B) ---------------------------------------
FREQ={1:"Plus.×/sem",2:"1×/sem",3:"2-3×/mois",4:"1×/mois",5:"<1×/mois",6:"Événements",7:"Jamais"}
vc=A["freq_7"].value_counts().sort_index()
fig,ax=plt.subplots(figsize=(7,4))
ax.bar([FREQ[k] for k in vc.index],vc.values,color="0.55",edgecolor="black")
ax.set_ylabel("Nombre de répondants")
ax.set_title("Fréquence d'achat direct aux agriculteurs")
plt.xticks(rotation=30,ha="right")
save(fig,"fig2_frequence_canal7_nb")

# ---- Typologie (pour fig 3) ------------------------------------------------
X=A[[f"cat_{i}" for i in range(1,12)]].astype(str)
MC=prince.MCA(n_components=5,random_state=42).fit(X).row_coordinates(X).values
Z=linkage(MC,method="ward")
lab=fcluster(Z,5,criterion="maxclust")
order=pd.Series(lab).value_counts().index.tolist()
remap={o:n for n,o in enumerate(order,1)}
A["classe"]=pd.Series(lab,index=A.index).map(remap)
# fig 3 : plan factoriel, marqueurs distincts N&B
markers=["o","s","^","D","x"]; fills=["none","0.3","0.6","none","black"]
fig,ax=plt.subplots(figsize=(7,6))
for k in range(1,6):
    m=(A["classe"]==k).values
    ax.scatter(MC[m,0],MC[m,1],s=22,marker=markers[k-1],
               facecolors=fills[k-1] if fills[k-1]!="none" else "none",
               edgecolors="black",linewidths=0.7,label=f"C{k}",alpha=.8)
ax.axhline(0,color="0.7",lw=.5); ax.axvline(0,color="0.7",lw=.5)
ax.set_xlabel("Axe 1"); ax.set_ylabel("Axe 2")
ax.set_title("Plan factoriel (ACM) et classes de stratégie")
ax.legend(fontsize=8,markerscale=1.2)
save(fig,"fig3_plan_factoriel_nb")

# ---- Fig 4 : régression (forest plot N&B) ----------------------------------
d=A.copy()
d["budget_z"]=(d["budget_eur"]-d["budget_eur"].mean())/d["budget_eur"].std()
d["age"]=pd.Categorical(d["age"],["20-24","25-34","35-44","45-54","55-64","65+"])
d["csp"]=pd.Categorical(d["csp"],["Employés/ouvriers","Indép./agri","Cadres/prof.lib",
    "Prof. interm.","Retraités","Inactifs/autres"])
d["sexe"]=pd.Categorical(d["sexe"],["Homme","Femme"])
f="vente_directe ~ C(sexe)+C(age)+C(csp)+budget_z"
if "tuu" in d.columns:
    d["tuu_z"]=(d["tuu"]-d["tuu"].mean())/d["tuu"].std(); f+="+tuu_z"
m=smf.logit(f,data=d).fit(disp=0)
orv=np.exp(m.params); ci=np.exp(m.conf_int()); pv=m.pvalues
idx=[i for i in m.params.index if i!="Intercept"]
def cl(s): return s.replace("C(","").replace(")","").replace("[T.","=").replace("]","")
fig,ax=plt.subplots(figsize=(7,max(3,0.4*len(idx))))
for y,i in enumerate(idx):
    lo=orv[i]-ci.loc[i].iloc[0]; hi=ci.loc[i].iloc[1]-orv[i]
    ax.errorbar(orv[i],y,xerr=[[lo],[hi]],fmt="o",color="black",
                mfc=("black" if pv[i]<0.05 else "white"),mec="black",capsize=3)
ax.axvline(1,color="black",lw=.8,ls="--")
ax.set_yticks(range(len(idx))); ax.set_yticklabels([cl(i) for i in idx],fontsize=8)
ax.set_xlabel("Odds-ratio (points pleins : significatifs à 5 %)")
ax.set_title("Déterminants de l'usage de la vente directe")
save(fig,"fig4_regression_or_nb")

# ---- Fig 5 : motivations marché (N&B) --------------------------------------
MOT={1:"Découvrir nouveautés",2:"Flâner",3:"Grandes marques",4:"Produits locaux",
 5:"Soutien agriculteurs",6:"Rencontrer",7:"Diversité/choix",8:"Tout au même endroit",
 9:"Produits Bio",10:"Proximité",11:"Praticité",12:"Prix/promotions",
 13:"Qualité nutritionnelle",14:"Goût",15:"Circuit court",16:"Services",17:"Introuvables ailleurs",18:"Autre"}
top3=pd.concat([pd.to_numeric(raw[c],errors="coerce") for c in ["Q21_1","Q21_2","Q21_3"]])
cnt=top3.value_counts(); base=raw["Q21_1"].notna().sum()
items=[(MOT.get(int(i),"?"),c) for i,c in cnt.head(8).items() if not pd.isna(i) and i!=0]
items=items[::-1]
fig,ax=plt.subplots(figsize=(8,5))
ax.barh([x[0] for x in items],[x[1] for x in items],color="0.5",edgecolor="black")
ax.set_xlabel(f"Citations dans le top 3 (base : {base} répondants)")
ax.set_title("Motivations d'achat sur les marchés")
save(fig,"fig5_motivations_marche_nb")

print("Figures N&B générées :",sorted(p.name for p in FIGP.glob('*_nb.png')))
