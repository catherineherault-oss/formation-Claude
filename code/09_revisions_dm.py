#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Révisions DM (retours autrice) : diplôme × classes, diplôme en régression,
nb de canaux par classe, données de la figure récence 4-modalités + comparaison artisans."""
import pandas as pd, numpy as np
from pathlib import Path
from scipy.cluster.hierarchy import linkage, fcluster
from scipy import stats
import statsmodels.formula.api as smf
import prince

ROOT=Path(__file__).resolve().parent.parent
A=pd.read_pickle(ROOT/"data/processed/analyse.pkl")
raw=pd.read_excel(ROOT/"data/raw/24407_Export.xlsx",sheet_name="Données_RepNat").reset_index(drop=True)
A=A.reset_index(drop=True)
def num(c): return pd.to_numeric(raw[c],errors="coerce")

# ---- Diplôme (Q240) recodé en 4 niveaux ------------------------------------
dip=num("Q240")
A["diplome"]=pd.cut(dip,bins=[0,3,4,5,8],labels=["Infra-bac","Bac","Bac+2","Bac+3 et plus"])
print("Diplôme (recodé) :",dict(A["diplome"].value_counts()))

# ---- Clusters (mêmes que le manuscrit) -------------------------------------
X=A[[f"cat_{i}" for i in range(1,12)]].astype(str)
MC=prince.MCA(n_components=5,random_state=42).fit(X).row_coordinates(X).values
lab=fcluster(linkage(MC,method="ward"),5,criterion="maxclust")
order=pd.Series(lab).value_counts().index.tolist()
A["classe"]=pd.Series(lab,index=A.index).map({o:n for n,o in enumerate(order,1)})
NAMES={1:"C1",2:"C2",3:"C3",4:"C4",5:"C5"}

print("\n=== Nb moyen de canaux par classe ===")
pen=[f"penet_{i}" for i in range(1,14)]; reg=[f"reg_{i}" for i in range(1,14)]
for k in range(1,6):
    s=A[A.classe==k]
    print(f"  C{k} (n={len(s)}): fréquentés={s[pen].sum(axis=1).mean():.1f} | réguliers={s[reg].sum(axis=1).mean():.1f} | budget={s['budget_eur'].mean():.0f}€ | %VD={100*s['vente_directe'].mean():.0f}")

print("\n=== Diplôme × classe (% en ligne) ===")
ct=pd.crosstab(A["classe"],A["diplome"],normalize="index")*100
chi2,p,_,_=stats.chi2_contingency(pd.crosstab(A["classe"],A["diplome"]))
print(ct.round(0).to_string()); print(f"χ² p = {p:.4f}")

# ---- Régression avec diplôme -----------------------------------------------
print("\n=== Régression logistique VD + DIPLÔME ===")
d=A.copy()
d["budget_z"]=(d["budget_eur"]-d["budget_eur"].mean())/d["budget_eur"].std()
d["age"]=pd.Categorical(d["age"],["20-24","25-34","35-44","45-54","55-64","65+"])
d["csp"]=pd.Categorical(d["csp"],["Employés/ouvriers","Indép./agri","Cadres/prof.lib","Prof. interm.","Retraités","Inactifs/autres"])
d["sexe"]=pd.Categorical(d["sexe"],["Homme","Femme"])
d["diplome"]=pd.Categorical(d["diplome"],["Infra-bac","Bac","Bac+2","Bac+3 et plus"])
f="vente_directe ~ C(sexe)+C(age)+C(csp)+C(diplome)+budget_z"
if "tuu" in d.columns:
    d["tuu_z"]=(d["tuu"]-d["tuu"].mean())/d["tuu"].std(); f+="+tuu_z"
m=smf.logit(f,data=d).fit(disp=0)
orv=np.exp(m.params); ci=np.exp(m.conf_int()); pv=m.pvalues
print(f"pseudo-R2={m.prsquared:.3f} N={int(m.nobs)}")
for i in m.params.index:
    if i=="Intercept": continue
    star="*" if pv[i]<0.05 else " "
    print(f"  {i:<28} OR={orv[i]:.2f}{star} [{ci.loc[i].iloc[0]:.2f}-{ci.loc[i].iloc[1]:.2f}] p={pv[i]:.3f}")

# ---- Récence 4 modalités : formes directes + comparaison artisans ----------
print("\n=== Récence 4 modalités (% des interrogés, hors 'ne sait pas') ===")
chans=[("Q100","Boulanger*"),("Q22","Marché (producteur)"),("Q92","Boucher*"),
       ("Q121","Primeur*"),("Q30","À la ferme"),("Q38","Magasin de producteurs"),
       ("Q61","Halle commerçante"),("Q53","Panier en ligne"),("Q70","Foire/salon")]
print(f"{'Canal':<26}{'base':>6}{'récent':>8}{'pas ce mois':>12}{'n''achète+':>11}{'jamais':>8}")
figdata=[]
for q,lab in chans:
    s=num(q); base=((s>=1)&(s<=4)).sum()
    r=[100*(s==k).sum()/base for k in (1,2,3,4)]
    figdata.append((lab,base,*r))
    print(f"{lab:<26}{base:>6}{r[0]:>7.0f}%{r[1]:>11.0f}%{r[2]:>10.0f}%{r[3]:>7.0f}%")
pd.DataFrame(figdata,columns=["canal","base","recent","pas_ce_mois","nachete_plus","jamais"]).to_pickle(ROOT/"data/processed/recence_fig.pkl")
print("\n(* = circuit conventionnel spécialisé, pour comparaison)")
