#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stade 2 — Analyses principales A1–A6 (enquête 24407).
Produit : articles/stade2_resultats.md + figures (SVG vectoriel + PNG 300 dpi).

A1 Portefeuille de canaux        A4 Profils socio-éco des classes
A2 Place de la vente directe     A5 Déterminants de l'usage VD (régression)
A3 Typologie (ACM + CAH)         A6 Motivations (marchés, Q21)

Toutes les sorties sont RÉELLES et reproductibles. Aucune donnée individuelle
n'est écrite dans les livrables (agrégats uniquement).
"""
import pandas as pd, numpy as np
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.cluster import AgglomerativeClustering
import statsmodels.formula.api as smf
import prince

ROOT = Path(__file__).resolve().parent.parent
A = pd.read_pickle(ROOT / "data/processed/analyse.pkl")
N = len(A)
FIG_SVG = ROOT / "figures/svg"; FIG_PNG = ROOT / "figures/png"
FIG_SVG.mkdir(parents=True, exist_ok=True); FIG_PNG.mkdir(parents=True, exist_ok=True)
OUT = ROOT / "articles/stade2_resultats.md"

CANAUX = {1:"Hyper/Super",2:"Hard discount",3:"Épiceries indép.",4:"Surgelés",
    5:"Bio spécialisé",6:"Marché",7:"Vente directe agri",8:"Paniers interm.",
    9:"Artisans/comm.",10:"Coop./participatif",11:"Vrac/locaux",
    12:"Aide alimentaire",13:"Autre"}
MOTIFS = {1:"Découvrir des nouveautés",2:"Flâner dans les rayons",
    3:"Produits de grandes marques",4:"Produits locaux",
    5:"Soutenir agriculteurs/éco. locale",6:"Rencontrer, discuter",
    7:"Diversité/large choix",8:"Tout au même endroit",9:"Produits Bio",
    10:"Proximité du lieu",11:"Praticité d'accès (trajet)",12:"Prix, promotions",
    13:"Qualité nutritionnelle",14:"Goût des produits",15:"Produits circuit court",
    16:"Services associés",17:"Produits introuvables ailleurs",18:"Autre"}

plt.rcParams.update({"font.size":10,"axes.grid":False})
def savefig(fig, name):
    fig.savefig(FIG_SVG/f"{name}.svg", bbox_inches="tight")
    fig.savefig(FIG_PNG/f"{name}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

L=[]
def w(s=""): L.append(s)

w("---"); w('title: "Stade 2C — Résultats d\'analyse (données réelles)"')
w("date: 2026-06-29"); w("source: enquête 24407, N=1025, échantillon représentatif national")
w("statut: \"Résultats reproductibles — à valider (checkpoint)\""); w("---"); w()
w("# Stade 2C — Résultats")
w()
w("> Généré par `code/03_analyses.py` à partir de `data/processed/analyse.pkl`.")
w("> **Définition vente directe (VD)** : achat direct aux agriculteurs (canal 7, Q6_7≠Jamais)")
w("> OU achat direct au producteur sur les marchés (Q22=1). VD = "
  f"**{A['vente_directe'].sum()} répondants ({100*A['vente_directe'].mean():.1f}%)**.")
w()

# ======================================================================= A1
w("## A1 — Le portefeuille de canaux des ménages")
w()
rows=[]
for i in range(1,14):
    pen=100*A[f"penet_{i}"].mean(); reg=100*A[f"reg_{i}"].mean()
    part=A[f"part_{i}"].mean()
    rows.append((i,CANAUX[i],pen,reg,part))
w("| # | Canal | Pénétration | Réguliers (≥1×/mois) | Part budget moy. |")
w("|---|-------|-------------|----------------------|------------------|")
for i,c,pen,reg,part in rows:
    star=" ⭐" if i==7 else ""
    w(f"| {i} | {c}{star} | {pen:.1f}% | {reg:.1f}% | {part:.1f}% |")
w()
w(f"Nombre moyen de canaux fréquentés par ménage : "
  f"**{A[[f'penet_{i}' for i in range(1,14)]].sum(axis=1).mean():.1f}**.")
w()
# Figure A1 : part de budget moyenne par canal (barres)
order=sorted(rows,key=lambda r:-r[4])
fig,ax=plt.subplots(figsize=(8,5))
labels=[r[1] for r in order]; vals=[r[4] for r in order]
cols=["#c0392b" if r[0]==7 else "#5b8db8" for r in order]
ax.barh(labels[::-1],vals[::-1],color=cols[::-1])
ax.set_xlabel("Part moyenne du budget alimentaire (%)")
ax.set_title("Figure 1 — Part du budget alimentaire par canal (N=1025)")
for y,v in enumerate(vals[::-1]): ax.text(v+0.4,y,f"{v:.1f}%",va="center",fontsize=8)
savefig(fig,"fig1_part_budget_canal")
w("![Figure 1](../figures/png/fig1_part_budget_canal.png)")
w("*Figure 1 — Part moyenne du budget alimentaire par canal. La vente directe (rouge) est marginale en budget.*")
w()

# ======================================================================= A2
w("## A2 — La place de la vente directe")
w()
w("| Composante | n | % de l'échantillon |")
w("|------------|---|--------------------|")
w(f"| VD via canal 7 (direct agriculteurs) | {A['vd_canal7'].sum()} | {100*A['vd_canal7'].mean():.1f}% |")
w(f"| VD via marché direct producteur (Q22=1) | {A['vd_marche_direct'].sum()} | {100*A['vd_marche_direct'].mean():.1f}% |")
w(f"| **VD (union, définition retenue)** | **{A['vente_directe'].sum()}** | **{100*A['vente_directe'].mean():.1f}%** |")
w(f"| dont VD régulière (canal 7 ≥1×/mois) | {A['vd_regulier'].sum()} | {100*A['vd_regulier'].mean():.1f}% |")
w()
w("**Paradoxe central** : la vente directe touche **2 ménages sur 3** mais ne "
  f"pèse que **{A['part_vd_canal7'].mean():.1f}% du budget** alimentaire (part propre du canal 7 ; "
  "la fraction directe des achats sur marché n'est pas isolable dans Q9_6 — *caveat*). "
  "→ canal de complémentarité, non de substitution.")
w()
# Figure A2 : distribution fréquence canal 7
fig,ax=plt.subplots(figsize=(7,4))
FREQ={1:"Plus.×/sem",2:"1×/sem",3:"2-3×/mois",4:"1×/mois",5:"<1×/mois",6:"Événements",7:"Jamais"}
vc=A["freq_7"].value_counts().sort_index()
ax.bar([FREQ[k] for k in vc.index],vc.values,color="#c0392b")
ax.set_ylabel("Nombre de répondants"); ax.set_title("Figure 2 — Fréquence d'achat direct aux agriculteurs (canal 7)")
plt.xticks(rotation=30,ha="right")
savefig(fig,"fig2_frequence_canal7")
w("![Figure 2](../figures/png/fig2_frequence_canal7.png)")
w("*Figure 2 — Fréquence d'achat en vente directe aux agriculteurs (canal 7).*")
w()

# ======================================================================= A3
w("## A3 — Typologie des stratégies d'approvisionnement (ACM + CAH)")
w()
active=[f"cat_{i}" for i in range(1,12)]   # canaux 1..11
X=A[active].astype(str)
mca=prince.MCA(n_components=5,random_state=42).fit(X)
coords=mca.row_coordinates(X)
try:
    inertia=mca.eigenvalues_summary
    inertie_txt=str(inertia.iloc[:3].to_dict())
except Exception:
    inertie_txt="(résumé d'inertie indisponible selon version prince)"
K=5
hc=AgglomerativeClustering(n_clusters=K,linkage="ward")
raw_lab=hc.fit_predict(coords.values)
# Renumérotation stable par effectif décroissant : C1 = classe la plus nombreuse
order=pd.Series(raw_lab).value_counts().index.tolist()
remap={old:new for new,old in enumerate(order,start=1)}
A["classe"]=pd.Series(raw_lab,index=A.index).map(remap)
w(f"ACM sur 11 canaux (3 niveaux), CAH de Ward en **{K} classes** sur 5 axes factoriels "
  "(numérotées par effectif décroissant).")
w()
# Profil : pénétration par canal et par classe
w("**Taux de fréquentation (pénétration) par canal et par classe.** "
  "La colonne **% VD** applique la définition inclusive (achat direct au moins occasionnel) ; "
  "**% VD rég.** ne compte que l'achat direct régulier au producteur (canal 7 ≥ 1×/mois), "
  "ce qui distingue l'essai ponctuel de l'usage installé.")
w()
hdr="| Classe (n) | " + " | ".join(CANAUX[i] for i in range(1,12)) + " | % VD | % VD rég. |"
w(hdr); w("|"+"---|"*(14))
for k in range(1,K+1):
    sub=A[A["classe"]==k]; nk=len(sub)
    cells=[f"{100*sub[f'penet_{i}'].mean():.0f}" for i in range(1,12)]
    w(f"| C{k} (n={nk}) | " + " | ".join(cells)
      + f" | {100*sub['vente_directe'].mean():.0f}% | {100*sub['vd_regulier'].mean():.0f}% |")
w()
# Figure A3 : plan factoriel coloré par classe
fig,ax=plt.subplots(figsize=(7,6))
for k in range(1,K+1):
    m=A["classe"]==k
    ax.scatter(coords.values[m.values,0],coords.values[m.values,1],s=10,alpha=.5,label=f"C{k}")
ax.set_xlabel("Axe 1"); ax.set_ylabel("Axe 2")
ax.set_title("Figure 3 — Plan factoriel ACM, classes CAH")
ax.legend(markerscale=2,fontsize=8); ax.axhline(0,color="grey",lw=.5); ax.axvline(0,color="grey",lw=.5)
savefig(fig,"fig3_plan_factoriel")
w("![Figure 3](../figures/png/fig3_plan_factoriel.png)")
w("*Figure 3 — Plan factoriel (axes 1-2) de l'ACM, coloré par classe de stratégie.*")
w()

# ======================================================================= A4
w("## A4 — Profil socio-économique des classes")
w()
def profil(var,titre):
    w(f"**{titre} × classe** (% en ligne)")
    w()
    ct=pd.crosstab(A["classe"],A[var],normalize="index")*100
    chi2,p,_,_=stats.chi2_contingency(pd.crosstab(A["classe"],A[var]))
    cols=list(ct.columns)
    w("| Classe | "+" | ".join(str(c) for c in cols)+" |")
    w("|"+"---|"*(len(cols)+1))
    for k in ct.index:
        w(f"| C{k} | "+" | ".join(f"{ct.loc[k,c]:.0f}%" for c in cols)+" |")
    w(f"\nχ²(p) = {p:.4f} {'(significatif)' if p<0.05 else '(n.s.)'}")
    w()
profil("csp","CSP")
profil("age","Âge")
# Budget moyen par classe
w("**Budget alimentaire mensuel moyen par classe :**")
w()
w("| Classe | Budget moyen (€) | % VD (inclusif) | % VD régulière |")
w("|--------|------------------|-----------------|----------------|")
for k in range(1,K+1):
    sub=A[A["classe"]==k]
    w(f"| C{k} | {sub['budget_eur'].mean():.0f} € | {100*sub['vente_directe'].mean():.0f}% | {100*sub['vd_regulier'].mean():.0f}% |")
w()

# ======================================================================= A5
w("## A5 — Déterminants de l'usage de la vente directe (régression logistique)")
w()
d=A.copy()
d["budget_z"]=(d["budget_eur"]-d["budget_eur"].mean())/d["budget_eur"].std()
d["age"]=pd.Categorical(d["age"],["20-24","25-34","35-44","45-54","55-64","65+"])
d["csp"]=pd.Categorical(d["csp"],["Employés/ouvriers","Indép./agri","Cadres/prof.lib",
    "Prof. interm.","Retraités","Inactifs/autres"])
d["sexe"]=pd.Categorical(d["sexe"],["Homme","Femme"])
formula="vente_directe ~ C(sexe) + C(age) + C(csp) + budget_z"
if "tuu" in d.columns:
    d["tuu_z"]=(d["tuu"]-d["tuu"].mean())/d["tuu"].std()
    formula+=" + tuu_z"
m=smf.logit(formula,data=d).fit(disp=0)
params=m.params; conf=m.conf_int(); ors=np.exp(params); orc=np.exp(conf); pv=m.pvalues
w(f"Modèle : `{formula}`. Pseudo-R² (McFadden) = {m.prsquared:.3f}, N = {int(m.nobs)}.")
w()
w("| Variable | Odds-ratio | IC95% | p |")
w("|----------|-----------|-------|---|")
def clean(idx):
    return idx.replace("C(","").replace(")","").replace("[T.","=").replace("]","")
for idx in params.index:
    if idx=="Intercept": continue
    sig="**" if pv[idx]<0.05 else ""
    w(f"| {clean(idx)} | {sig}{ors[idx]:.2f}{sig} | [{orc.loc[idx].iloc[0]:.2f}–{orc.loc[idx].iloc[1]:.2f}] | {pv[idx]:.3f} |")
w()
w("*Lecture : OR>1 = probabilité accrue d'acheter en vente directe. "
  "Référence : Homme, 20-24 ans, Employés/ouvriers. En gras = p<0,05.*")
w()
# Figure A5 : forest plot des OR significatifs
sigidx=[i for i in params.index if i!="Intercept"]
fig,ax=plt.subplots(figsize=(7,max(3,0.4*len(sigidx))))
yl=[clean(i) for i in sigidx]; xs=[ors[i] for i in sigidx]
errlo=[ors[i]-orc.loc[i].iloc[0] for i in sigidx]; errhi=[orc.loc[i].iloc[1]-ors[i] for i in sigidx]
cols=["#c0392b" if pv[i]<0.05 else "#999999" for i in sigidx]
ax.errorbar(xs,range(len(yl)),xerr=[errlo,errhi],fmt="o",ecolor="grey",mfc="none",ls="none")
for y,(x,c) in enumerate(zip(xs,cols)): ax.plot(x,y,"o",color=c)
ax.axvline(1,color="black",lw=.8,ls="--"); ax.set_yticks(range(len(yl))); ax.set_yticklabels(yl,fontsize=8)
ax.set_xlabel("Odds-ratio (échelle linéaire)"); ax.set_title("Figure 4 — Déterminants de l'usage de la vente directe")
savefig(fig,"fig4_regression_or")
w("![Figure 4](../figures/png/fig4_regression_or.png)")
w("*Figure 4 — Odds-ratios (rouge = significatif à 5%). Référence : Homme, 20-24 ans, Employés/ouvriers.*")
w()

# ======================================================================= A6
w("## A6 — Motivations d'achat sur les marchés (Q21, population marché)")
w()
df_raw=pd.read_excel(ROOT/"data/raw/24407_Export.xlsx",sheet_name="Données_RepNat")
top3=pd.concat([pd.to_numeric(df_raw[c],errors="coerce") for c in ["Q21_1","Q21_2","Q21_3"]])
cnt=top3.value_counts()
base=df_raw["Q21_1"].notna().sum()
w(f"Base : {base} répondants fréquentant les marchés et ayant classé leurs motivations.")
w("Fréquence de citation dans le top 3 :")
w()
w("| Rang | Motivation | Citations top-3 | % base |")
w("|------|-----------|-----------------|--------|")
for r,(item,c) in enumerate(cnt.head(8).items(),1):
    if pd.isna(item) or item==0: continue
    w(f"| {r} | {MOTIFS.get(int(item),'?')} | {int(c)} | {100*c/base:.0f}% |")
w()
# Figure A6
fig,ax=plt.subplots(figsize=(8,5))
items=[(MOTIFS.get(int(i),'?'),c) for i,c in cnt.head(8).items() if not pd.isna(i) and i!=0]
labs=[x[0] for x in items][::-1]; vs=[x[1] for x in items][::-1]
ax.barh(labs,vs,color="#27ae60")
ax.set_xlabel("Citations dans le top 3 des motivations")
ax.set_title("Figure 5 — Motivations d'achat sur les marchés")
savefig(fig,"fig5_motivations_marche")
w("![Figure 5](../figures/png/fig5_motivations_marche.png)")
w("*Figure 5 — Principales motivations d'achat sur les marchés (classement top 3).*")
w()

OUT.write_text("\n".join(L),encoding="utf-8")
print("Résultats écrits :",OUT)
print("Classes CAH (effectifs) :",A["classe"].value_counts().sort_index().to_dict())
print("Pseudo-R2 régression :",round(m.prsquared,3))
print("Figures :",sorted(p.name for p in FIG_PNG.glob('*.png')))
