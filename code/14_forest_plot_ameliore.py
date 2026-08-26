#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Forest plot AMÉLIORÉ des odds-ratios (VD inclusive) :
- échelle logarithmique ; regroupement par bloc ; OR [IC 95 %] annotés ;
- points pleins = significatifs à 5 % ;
- police type Times New Roman (Liberation Serif, métriquement identique) ;
- texte agrandi ; PAS de titre dans le schéma (→ légende du manuscrit).
Sortie : figures/png/fig4_regression_or_log_nb.png (+ svg). N&B pour DM.
"""
import pandas as pd, numpy as np
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullLocator
import matplotlib.transforms as mtransforms
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parent.parent
A = pd.read_pickle(ROOT/"data/processed/analyse.pkl")
# Police : Times New Roman si présent, sinon Liberation Serif (métriquement identique)
plt.rcParams.update({"font.family":"serif",
                     "font.serif":["Times New Roman","Liberation Serif","Tinos","DejaVu Serif"],
                     "font.size":14})

# ---- Régression exacte (identique à code/06) -------------------------------
d = A.copy()
d["budget_z"]=(d.budget_eur-d.budget_eur.mean())/d.budget_eur.std()
d["age"]=pd.Categorical(d.age,["20-24","25-34","35-44","45-54","55-64","65+"])
d["csp"]=pd.Categorical(d.csp,["Employés/ouvriers","Indép./agri","Cadres/prof.lib","Prof. interm.","Retraités","Inactifs/autres"])
d["sexe"]=pd.Categorical(d.sexe,["Homme","Femme"])
d["diplome"]=pd.Categorical(d.diplome,["Infra-bac","Bac","Bac+2","Bac+3 et plus"])
f="vente_directe ~ C(sexe)+C(age)+C(csp)+C(diplome)+budget_z"
if "tuu" in d.columns: d["tuu_z"]=(d.tuu-d.tuu.mean())/d.tuu.std(); f+="+tuu_z"
m=smf.logit(f,data=d).fit(disp=0)
orv=np.exp(m.params); ci=np.exp(m.conf_int()); pv=m.pvalues

LAB={"C(sexe)[T.Femme]":"Femme",
 "C(age)[T.25-34]":"25-34 ans","C(age)[T.35-44]":"35-44 ans","C(age)[T.45-54]":"45-54 ans",
 "C(age)[T.55-64]":"55-64 ans","C(age)[T.65+]":"65 ans et plus",
 "C(csp)[T.Indép./agri]":"Indépendants, agriculteurs","C(csp)[T.Cadres/prof.lib]":"Cadres, prof. libérales",
 "C(csp)[T.Prof. interm.]":"Professions intermédiaires","C(csp)[T.Retraités]":"Retraités",
 "C(csp)[T.Inactifs/autres]":"Inactifs, autres",
 "C(diplome)[T.Bac]":"Bac","C(diplome)[T.Bac+2]":"Bac+2","C(diplome)[T.Bac+3 et plus]":"Bac+3 et plus",
 "budget_z":"Budget alimentaire","tuu_z":"Taille d'agglomération"}
BLOCKS=[("Sexe (réf. : homme)",["C(sexe)[T.Femme]"]),
 ("Âge (réf. : 20-24 ans)",["C(age)[T.25-34]","C(age)[T.35-44]","C(age)[T.45-54]","C(age)[T.55-64]","C(age)[T.65+]"]),
 ("Catégorie socioprof. (réf. : employés, ouvriers)",["C(csp)[T.Indép./agri]","C(csp)[T.Cadres/prof.lib]","C(csp)[T.Prof. interm.]","C(csp)[T.Retraités]","C(csp)[T.Inactifs/autres]"]),
 ("Diplôme (réf. : infra-bac)",["C(diplome)[T.Bac]","C(diplome)[T.Bac+2]","C(diplome)[T.Bac+3 et plus]"]),
 ("Variables continues (par écart-type)",[k for k in ["budget_z","tuu_z"] if k in orv.index])]

rows=[]
for htitle,keys in BLOCKS:
    rows.append(("header",htitle,None,None,None,None))
    for k in keys:
        rows.append(("data",LAB[k],orv[k],ci.loc[k].iloc[0],ci.loc[k].iloc[1],pv[k]))
n=len(rows); ypos=list(range(n))[::-1]

fig,ax=plt.subplots(figsize=(10.5,0.5*n+0.8))
for (kind,label,o,lo,hi,p),y in zip(rows,ypos):
    if kind!="data": continue
    sig=p<0.05
    ax.plot([lo,hi],[y,y],"-",color="black",lw=1.3,zorder=2)
    for xb in (lo,hi): ax.plot([xb,xb],[y-0.14,y+0.14],"-",color="black",lw=1.3)
    ax.plot(o,y,"o",ms=8,mfc=("black" if sig else "white"),mec="black",mew=1.4,zorder=3)

ax.axvline(1,color="black",lw=1.0,ls="--",zorder=1)
ax.set_xscale("log"); ax.set_xlim(0.4,3.6)
ticks=[0.5,0.7,1,1.5,2,3]
ax.xaxis.set_major_locator(FixedLocator(ticks)); ax.xaxis.set_minor_locator(NullLocator())
ax.set_xticklabels([str(t) for t in ticks],fontsize=14)
ax.set_xlabel("Odds-ratio (échelle logarithmique) — point plein : significatif à 5 %",fontsize=15)

ax.set_yticks(ypos)
ax.set_yticklabels([("" if k=="header" else "   ")+lab for (k,lab,*_ ) in rows],fontsize=14)
for tick,(kind,*_ ) in zip(ax.get_yticklabels(),rows):
    if kind=="header": tick.set_fontweight("bold")
ax.tick_params(axis="y",length=0)
ax.set_ylim(-0.6,n-0.4)
for sp in ("top","right","left"): ax.spines[sp].set_visible(False)

# Colonne de droite : OR [IC] (+ * si significatif)
trans=mtransforms.blended_transform_factory(ax.transAxes,ax.transData)
ax.text(1.03,ypos[0],"OR [IC 95 %]",transform=trans,fontsize=13.5,fontweight="bold",va="center",ha="left")
for (kind,label,o,lo,hi,p),y in zip(rows,ypos):
    if kind!="data": continue
    star=" *" if p<0.05 else ""
    ax.text(1.03,y,f"{o:.2f} [{lo:.2f}–{hi:.2f}]{star}",transform=trans,fontsize=13.5,va="center",ha="left")

# PAS de titre dans le schéma (→ légende du manuscrit). Pas de note de bas non plus.
FIGP=ROOT/"figures/png"; FIGS=ROOT/"figures/svg"
fig.savefig(FIGS/"fig4_regression_or_log_nb.svg",bbox_inches="tight")
fig.savefig(FIGP/"fig4_regression_or_log_nb.png",dpi=300,bbox_inches="tight")
print("Forest plot régénéré (Times/Liberation Serif, texte agrandi, sans titre).")
print(f"N={int(m.nobs)} pseudo-R2={m.prsquared:.3f} — pour la légende.")
