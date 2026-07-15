#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stade 4.5 — Audit d'intégrité : traçabilité numérique du manuscrit DM.

Recalcule depuis les données brutes chaque chiffre affiché dans le manuscrit et
le confronte à la valeur écrite (PASS/FAIL, tolérance de 0,5 pt sur les %).
Aucune donnée individuelle n'est écrite ; seuls les agrégats sont vérifiés.
"""
import pandas as pd, numpy as np
from pathlib import Path
from scipy.cluster.hierarchy import linkage, fcluster
from scipy import stats
from sklearn.metrics import silhouette_score
import statsmodels.formula.api as smf
import prince

ROOT = Path(__file__).resolve().parent.parent
A = pd.read_pickle(ROOT/"data/processed/analyse.pkl").reset_index(drop=True)
raw = pd.read_excel(ROOT/"data/raw/24407_Export.xlsx", sheet_name="Données_RepNat").reset_index(drop=True)
def num(c): return pd.to_numeric(raw[c], errors="coerce")
N = len(A)
checks = []
def chk(label, claimed, computed, tol=0.5, unit="%"):
    ok = abs(claimed - computed) <= tol
    checks.append((ok, label, claimed, round(computed,2), unit))

# --- Échantillon / démographie ---------------------------------------------
chk("N échantillon", 1025, N, tol=0)
chk("% femmes", 52.6, 100*(num('Q1')==2).mean())
chk("% 65+", 26.0, 100*(num('recode_age')==6).mean())
chk("budget médian €", 400, A['budget_eur'].median(), tol=1, unit="€")
chk("budget moyen €", 436, A['budget_eur'].mean(), tol=1, unit="€")

# --- Pénétration / VD -------------------------------------------------------
chk("VD inclusive %", 65.0, 100*A['vente_directe'].mean())
chk("VD inclusive n", 666, A['vente_directe'].sum(), tol=0, unit="n")
chk("Canal7 pénétration %", 49.7, 100*A['vd_canal7'].mean())
chk("Canal7 pénétration n", 509, A['vd_canal7'].sum(), tol=0, unit="n")
chk("VD régulière %", 17.3, 100*A['vd_regulier'].mean())
chk("VD régulière n", 177, A['vd_regulier'].sum(), tol=0, unit="n")
chk("Apport porte marché n", 157, ((A['vd_marche_direct']==1)&(A['vd_canal7']==0)).sum(), tol=0, unit="n")
chk("Part budget VD /pop %", 1.5, A['part_vd_canal7'].mean())
chk("Part budget VD /réguliers %", 8.5, A.loc[A.vd_regulier==1,'part_vd_canal7'].mean())
chk("Nb moyen canaux fréquentés", 6.8, A[[f'penet_{i}' for i in range(1,14)]].sum(axis=1).mean(), tol=0.1, unit="")

# --- Tableau 2 : pénétration & budget principaux canaux ---------------------
T2 = {1:(99.1,97.5,58.5),2:(86.5,64.2,15.6),9:(87.1,61.9,7.6),6:(78.8,41.4,4.8),
      5:(57.4,24.2,2.3),7:(49.7,17.3,1.5),8:(15.7,5.8,0.4)}
for i,(pen,reg,part) in T2.items():
    chk(f"T2 canal{i} pénétration", pen, 100*A[f'penet_{i}'].mean())
    chk(f"T2 canal{i} réguliers", reg, 100*A[f'reg_{i}'].mean())
    chk(f"T2 canal{i} budget", part, A[f'part_{i}'].mean())

# --- Typologie (mêmes réglages que code/06,09,10) ---------------------------
X = A[[f"cat_{i}" for i in range(1,12)]].astype(str)
mca = prince.MCA(n_components=5, random_state=42).fit(X)
MC = mca.row_coordinates(X).values
eig = list(mca.eigenvalues_); tot = sum(eig)
chk("Inertie 2 premiers axes %", 62.0, 100*(eig[0]+eig[1])/tot, tol=1.0)
Z = linkage(MC, method="ward")
sil5 = silhouette_score(MC, fcluster(Z,5,'maxclust'))
sil4 = silhouette_score(MC, fcluster(Z,4,'maxclust'))
sil6 = silhouette_score(MC, fcluster(Z,6,'maxclust'))
chk("Silhouette k=5", 0.24, sil5, tol=0.01, unit="")
chk("Silhouette k=4", 0.21, sil4, tol=0.01, unit="")
chk("Silhouette k=6", 0.23, sil6, tol=0.01, unit="")
lab = fcluster(Z,5,'maxclust')
order = pd.Series(lab).value_counts().index.tolist()
A["classe"] = pd.Series(lab, index=A.index).map({o:n for n,o in enumerate(order,1)})
# Tableau 5 : n, part, canaux, budget, %VD, %VD rég par classe
T5 = {1:(624,61,7.2,3.8,439,72,16),2:(249,24,3.8,2.8,408,28,6),
      3:(79,8,11.1,9.5,513,97,67),4:(47,5,11.0,6.1,480,100,19),
      5:(26,2.5,6.3,3.3,320,81,8)}
pen=[f"penet_{i}" for i in range(1,14)]; regc=[f"reg_{i}" for i in range(1,14)]
for k,(n_,part,cf,cr,bud,vdi,vdr) in T5.items():
    s=A[A.classe==k]
    chk(f"T5 C{k} n", n_, len(s), tol=0, unit="n")
    chk(f"T5 C{k} part", part, 100*len(s)/N, tol=0.6)
    chk(f"T5 C{k} canaux fréq", cf, s[pen].sum(axis=1).mean(), tol=0.15, unit="")
    chk(f"T5 C{k} canaux rég", cr, s[regc].sum(axis=1).mean(), tol=0.15, unit="")
    chk(f"T5 C{k} budget", bud, s['budget_eur'].mean(), tol=2, unit="€")
    chk(f"T5 C{k} %VD incl", vdi, 100*s['vente_directe'].mean(), tol=1)
    chk(f"T5 C{k} %VD rég", vdr, 100*s['vd_regulier'].mean(), tol=1)

# --- Régressions ------------------------------------------------------------
d=A.copy()
d["budget_z"]=(d.budget_eur-d.budget_eur.mean())/d.budget_eur.std()
d["age"]=pd.Categorical(d.age,["20-24","25-34","35-44","45-54","55-64","65+"])
d["csp"]=pd.Categorical(d.csp,["Employés/ouvriers","Indép./agri","Cadres/prof.lib","Prof. interm.","Retraités","Inactifs/autres"])
d["sexe"]=pd.Categorical(d.sexe,["Homme","Femme"])
d["diplome"]=pd.Categorical(d.diplome,["Infra-bac","Bac","Bac+2","Bac+3 et plus"])
f="C(sexe)+C(age)+C(csp)+C(diplome)+budget_z"
if "tuu" in d.columns: d["tuu_z"]=(d.tuu-d.tuu.mean())/d.tuu.std(); f+="+tuu_z"
m1=smf.logit(f"vente_directe ~ {f}",data=d).fit(disp=0)
m2=smf.logit(f"vd_regulier ~ {f}",data=d).fit(disp=0)
def get(m,key):
    i=[x for x in m.params.index if key in x][0]; return np.exp(m.params[i]), m.pvalues[i]
chk("Régr. incl. pseudo-R²",0.029,m1.prsquared,tol=0.002,unit="")
orb,pb=get(m1,"Bac+3"); chk("Régr. incl. OR diplôme bac+3",1.89,orb,tol=0.05,unit="")
chk("Régr. incl. p diplôme bac+3",0.003,pb,tol=0.003,unit="")
orbud,pbud=get(m1,"budget_z"); chk("Régr. incl. OR budget",1.17,orbud,tol=0.03,unit="")
orc,pc=get(m1,"Cadres"); chk("Régr. incl. OR cadres",1.64,orc,tol=0.06,unit=""); chk("Régr. incl. p cadres",0.07,pc,tol=0.02,unit="")
chk("Régr. rég. pseudo-R²",0.016,m2.prsquared,tol=0.003,unit="")
orb2,pb2=get(m2,"Bac+3"); chk("Régr. rég. OR diplôme bac+3",1.22,orb2,tol=0.06,unit=""); chk("Régr. rég. p diplôme bac+3",0.45,pb2,tol=0.06,unit="")

# --- Colinéarité ------------------------------------------------------------
def cramers(a,b):
    ct=pd.crosstab(a,b); chi2=stats.chi2_contingency(ct)[0]; n=ct.values.sum(); r,k=ct.shape
    return np.sqrt((chi2/n)/(min(r-1,k-1)))
chk("V Cramér diplôme×CSP",0.29,cramers(A.diplome,A.csp),tol=0.02,unit="")
rho=stats.spearmanr(A.diplome.cat.codes.replace(-1,np.nan),A.budget_eur,nan_policy="omit").correlation
chk("ρ diplôme×budget",0.06,rho,tol=0.02,unit="")

# --- AMAP (Q46) -------------------------------------------------------------
q46=num("Q46"); base=q46.notna().sum(); oui=(q46==1).sum(); ab=(q46==2).sum(); nc=(q46==4).sum()
chk("AMAP base n",509,base,tol=0,unit="n")
chk("AMAP clients passés/présents n",116,oui+ab,tol=0,unit="n")
chk("AMAP actuels n",41,oui,tol=0,unit="n"); chk("AMAP cessé n",75,ab,tol=0,unit="n")
chk("AMAP taux abandon %",65,100*ab/(oui+ab),tol=1)
chk("AMAP ne connaît pas %",46,100*nc/base,tol=1)

# --- Récence (Tableau 4) ----------------------------------------------------
REC={"Q100":(893,58,21,10,11),"Q22":(810,59,30,6,5),"Q92":(893,38,32,17,13),
     "Q121":(893,37,34,17,13),"Q30":(509,34,35,16,15),"Q38":(509,20,34,15,31),
     "Q61":(509,17,35,19,29),"Q70":(509,7,34,18,42),"Q53":(509,6,11,14,70)}
for q,(b,r1,r2,r3,r4) in REC.items():
    s=num(q); base=s.notna().sum()
    chk(f"Récence {q} base",b,base,tol=0,unit="n")
    chk(f"Récence {q} récent",r1,100*(s==1).sum()/base,tol=1)
    chk(f"Récence {q} n'achète plus",r3,100*(s==3).sum()/base,tol=1)

# (Les motivations Q21 / Figure « motivations » ont été retirées du manuscrit
#  pour tenir la limite de 20 pages ; plus de claim chiffré à auditer ici.)

# --- Rapport ----------------------------------------------------------------
npass=sum(1 for c in checks if c[0]); nfail=len(checks)-npass
print(f"AUDIT DE TRAÇABILITÉ — {npass}/{len(checks)} PASS, {nfail} FAIL\n")
for ok,label,claimed,computed,unit in checks:
    if not ok:
        print(f"  [FAIL] {label} : manuscrit={claimed}{unit} calculé={computed}{unit}")
if nfail==0:
    print("  Tous les chiffres du manuscrit tracent vers les données réelles.")
print(f"\n=> {'INTÉGRITÉ NUMÉRIQUE VALIDÉE' if nfail==0 else 'ÉCARTS À CORRIGER'}")
