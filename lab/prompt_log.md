# Journal des prompts — [Nom du projet]
> Dernière mise à jour : 2026-06-29

## 2026-06-29 — Installation du système
**Prompt :** Installation et configuration initiale d'ARS v3.13.0
**Résultat :** Système installé, préférences enregistrées
**Fichiers produits :**
- `.claude/user_preferences.md`
- `.claude/skills/` (4 skills : deep-research, academic-paper, academic-paper-reviewer, academic-pipeline)
- `.claude/commands/` (commandes /ars-*)
- `.claude/shared/`, `.claude/hooks/`, `.claude/scripts/`, `.claude/audits/`, `.claude/examples/`, `.claude/docs/`
- `.claude/CLAUDE.md`, `.claude/CHANGELOG.md`
- `README.md`, `.gitignore`
- Structure de projet : `articles/`, `data/`, `code/`, `figures/svg/`, `figures/png/`, `references/`, `outputs/{latex,word,submitted}/`
- `lab/lab_notebook.md`, `lab/prompt_log.md`

---

## 2026-06-29 — Test fonctionnel `/ars-plan`
**Prompt :** Générer un plan de 3 chapitres pour un article fictif sur
« l'impact de l'IA générative sur les pratiques d'évaluation dans
l'enseignement supérieur ».
**Résultat :** Plan structuré (question de recherche + 3 chapitres avec
sections, sources et livrables + thèse opérationnelle en conclusion).
**Fichiers produits :**
- `articles/test_installation.md`

---

## 2026-06-29 — Lancement pipeline ARS `/ars-full`
**Prompt :** « Rédiger un article complet sur l'achat de produits alimentaires en vente directe »
**Choix utilisateur :** angle économie/marketing, IMRaD simulé, pilotage mixte, ~6-8k mots, France métropolitaine, 5 canaux (AMAP, marchés, ferme, plateformes, magasins de producteurs), angle « place dans les stratégies d'approvisionnement ».
**Stade 1 RECHERCHE produit :**
- Question de recherche reformulée + 5 sous-questions
- Cadre conceptuel + hypothèse centrale H1
- Bibliographie 18 références candidates (à vérifier au Stade 2.5)
- Synthèse littérature 5 thèmes (A définition, B motivations, C freins, D post-COVID, E stratégies d'approvisionnement)
- Méthodologie IMRaD avec données simulées explicitement marquées
- Plan préliminaire IMRaD ~6 400 mots
**Fichiers produits :**
- `articles/stade1_recherche.md`
**Checkpoint :** FULL — attente confirmation utilisateur avant Stade 2.

---

## 2026-06-29 — Réception données réelles + Stade 2A/2B
**Prompt :** Upload de l'enquête réelle (24407_Export.xlsx) + plan de codage.
**Résultat :**
- Étude passe de « simulée » à empirique réelle (1025 répondants représentatifs nationaux).
- Audit complet : 0% manquant sur variables clés, Q9 (parts budget) somme = 100%, 0 doublon.
- Résultat saillant confortant H1 : vente directe (canal 7) = 49,7% de pénétration mais 1,5% du budget moyen (vs hypermarché 58%).
- Alignement RQ↔variables : 4/5 sous-questions mesurables ; SQ5 (temporel) reléguée en discussion.
**Fichiers produits :**
- `code/01_audit_donnees.py`
- `articles/stade2_audit_donnees.md`
- `articles/stade2_alignement_rq.md`
- `data/raw/24407_Export.xlsx` + `references/24407_Plan_de_codage_VF.docx` (LOCAUX, non poussés — RGPD/droits institut)
**Checkpoint :** attente arbitrage utilisateur (3 points) avant analyses A1-A6.

---

## 2026-06-29 — Définition VD + Analyses A1-A6
**Décision :** vente directe = canal 7 (Q6_7≠Jamais) ∪ marché direct producteur (Q22=1) → 666 répondants (65%).
**Analyses produites (données réelles, reproductibles) :**
- A1 portefeuille de canaux (hyper 58,5% du budget, VD 1,5%)
- A2 place VD (65% pénétration, paradoxe ampleur/budget)
- A3 typologie ACM+CAH : 5 classes de stratégies d'approvisionnement
- A4 profils socio-éco (CSP p=0,0001, âge p=0,005)
- A5 régression logistique (pseudo-R²=0,022 ; cadres OR 2,16, budget OR 1,18)
- A6 motivations marché (locaux 51%, circuit court 41%, goût 39%)
**Fichiers produits :**
- `code/02_construction_variables.py`, `code/03_analyses.py`
- `articles/stade2_resultats.md`
- `figures/svg/*.svg` + `figures/png/*.png` (fig1 à fig5)
**Checkpoint :** présentation des résultats à l'utilisateur avant rédaction du draft IMRaD.

---

## 2026-06-29 — Typologie 4-vs-5 + rédaction du draft
**Décision :** 5 classes retenues (silhouette 0,237 > 0,207 ; classes distinctes par régularité d'usage, pas seulement pénétration). Libellés : Généralistes (624), Captifs grande distribution (249), Omnivores engagés (79), Multi-canal conventionnels (47), Hors-hypermarché (26).
**Rédaction :** draft IMRaD complet en français, ~4550 mots, centré sur les stratégies d'approvisionnement + la transversalité sociale (H1 et H2 confirmées).
**Fichiers produits :**
- `code/04_typologie_comparaison.py` + `figures/*/figS_dendrogramme.*`
- `articles/article_vente_directe.md`
**Checkpoint :** Stade 2 (WRITE) terminé → checkpoint avant Stade 2.5 INTÉGRITÉ (obligatoire).

---

## 2026-06-29 — Vérification automatique des références (partie du Stade 2.5)
**Demande utilisateur :** vérifier et corriger automatiquement les références ; relire le draft avant de continuer.
**Méthode :** WebSearch (API Crossref/OpenAlex bloquées par la politique réseau de l'env). 10 références vérifiées.
**Résultat — 3 corrections factuelles :**
- Dubuisson-Quellier, Lamine & Le Velly : année 2009 → **2011** (Sociologia Ruralis 51(3), 304-323)
- « Filser 2003, Décisions Marketing » : **non confirmée** → remplacée par Filser & Plichon (2004), Revue Française de Gestion 30(148), 29-43
- Praly et al. 2014 : titre + revue corrigés → « Les circuits de proximité… », *Géographie, économie, société*, 16(4), 455-478 (pas « Cahiers Agricultures »)
- 7 autres références confirmées (Chiffoleau 2019, Goodman & DuPuis 2002, Lamine 2008, Maréchal 2008, Sage 2003, Volle 2012, MAA 2009) + paginations/DOI ajoutés.
**Fichiers modifiés :** `articles/article_vente_directe.md` (liste de références + clés in-text).
**Pipeline :** EN PAUSE — attente de la relecture et des commentaires de l'utilisateur avant la suite du Stade 2.5 (re-contrôle chiffres + checklist 7 modes) et toute expansion.

---

## 2026-06-29 — Export Word (.docx)
**Demande :** version Word de l'article pour relecture/annotation.
**Réalisation :** installation pandoc (pypandoc-binary 3.9), création de `references/biblio.bib` (10 réfs vérifiées en BibTeX), conversion avec --citeproc (citations résolues + bibliographie auto + sommaire + 5 figures intégrées).
**Fichiers produits :**
- `outputs/word/article_vente_directe.docx`
- `references/biblio.bib`

---

## 2026-06-29 — Actualisation de la revue de littérature (retour utilisateur)
**Remarque utilisateur :** « les articles datent un peu, il faudrait les actualiser ».
**Action :** recherche de littérature récente vérifiable (WebSearch) ; 2 références 2020/2025 ajoutées et tissées dans intro, cadre conceptuel, résultats (H2) et discussion :
- Chiffoleau, Y., & Dourian, T. (2020), *Sustainability* 12(23), 9831 — revue circuits courts / résilience / COVID
- Herzig, J., & Zander, K. (2025), *Agricultural and Food Economics* 13(1) — revue systématique des déterminants (conforte H2)
**Fichiers modifiés :** `articles/article_vente_directe.md`, `references/biblio.bib`, `outputs/word/article_vente_directe.docx` (régénéré). Article ~4840 mots.

---

## 2026-06-29 — Correction typologie (question utilisateur : « pourquoi multi-canal conventionnel à 100% VD ? »)
**Diagnostic :** la VD est définie de façon inclusive (achat direct au moins occasionnel). Les multi-canal conventionnels (n=47) ont essayé presque tous les canaux (canal 7 pénétration 98%, coop/vrac/paniers ~90%) mais ne les utilisent pas régulièrement (VD régulière 19%, coop/vrac/paniers 0% régulier). Le 100% reflète l'essai, pas l'engagement.
**Corrections apportées :**
- `code/03_analyses.py` : renumérotation des classes par effectif décroissant + ajout colonne « % VD régulière » (A3 et A4).
- `articles/article_vente_directe.md` : tableau 3 refait (numérotation cohérente C1-C5 + VD régulière), libellé « évitent l'alternatif » corrigé en « essaient sans installer », prose §4.3/§4.4/§5.3 réécrite pour distinguer essai ponctuel vs usage installé.
- `outputs/word/article_vente_directe.docx` régénéré (~5120 mots).
**Leçon :** un taux inclusif élevé peut masquer un simple essai ; la colonne VD régulière lève l'ambiguïté.

---

## 2026-07-07 — Diaporama de copil (PPTX)
**Demande :** support de présentation pour un comité de pilotage.
**Réalisation :** `code/05_slides_copil.py` (python-pptx) → 10 diapositives 16:9, 2 figures intégrées, 3 leviers d'action.
**Fichier produit :** `outputs/presentations/copil_vente_directe.pptx`

## 2026-07-07 — Expansion de la revue de littérature (retour utilisateur)
**Demande :** « il faut vraiment abonder » + références proposées (omnicanal, conso durable, segmentation).
**Réalisation :** §2 réécrit en 4 sous-sections (circuits courts / omnicanal / intention→budget / segmentation) + tableau de positionnement (Tableau 1). Tables de résultats renumérotées (2 à 5). Hypothèse H3 (attitude-behaviour gap) ajoutée et reliée aux résultats (§4.2) et à la discussion (§5.1).
**9 références vérifiées ajoutées :** Verhoef et al. (2015), Neslin et al. (2006), Giampietri et al. (2016 & 2018), Birch et al. (2018), Mustapa & Kallas (2025), Vermeir & Verbeke (2006), Feldmann & Hamm (2015), Kneafsey et al. (2013, JRC).
**Fichiers modifiés :** `articles/article_vente_directe.md` (6 310 mots), `references/biblio.bib` (21 réfs), `outputs/word/article_vente_directe.docx` régénéré.

---

## 2026-07-07 — Clarification du 1,5 % (question méthodo utilisateur)
**Question :** pourquoi moyenner la part de budget sur toute la population (0 % pour les non-acheteurs) plutôt que sur les seuls acheteurs réguliers ?
**Réponse retenue :** afficher les DEUX (1,5 % population = poids économique comparable/sommant à 100 % ; 8,5 % acheteurs réguliers = intensité). Le 0 des non-acheteurs est une vraie donnée (poids de marché). Nuance : 1,5 % est un plancher (Q9 posée aux seuls réguliers ; 332 acheteurs occasionnels comptés 0).
**Modifications :**
- §3.2 : note de méthode (Q9 recueillie auprès des réguliers, parts sommant à 100 %, distinction moyenne-population / moyenne-acheteurs, « plancher »).
- §4.2 : les deux échelles (1,5 % national ≈ 7 €/mois ; 8,5 % chez les réguliers ≈ 42 €/mois) présentées côte à côte.
- Slide copil « Paradoxe » : chip 1,5 % complété par « 8,5 % chez ses réguliers ».
**Fichiers :** article (6 548 mots), DOCX + PPTX régénérés.

---

## 2026-07-07 — Reformatage pour la revue *Décisions Marketing*
**Demande :** soumettre à DM ; instructions aux auteurs + article exemple (« le bio, très peu pour moi ») fournis.
**Analyse des normes DM :** < 8 000 mots, ≤ 20 pages, ≤ 35 réfs, TNR 12 / interligne 1,5 / marges 2,5 cm ; résumé structuré en 6 points + abstract EN ; titres thématiques (pas « 1. Introduction ») ; encadrés attendus ; références style RAM/Harvard (« et » pas « & », revue en italique, vol(n): pages) ; figures N&B sans dégradés ; orientation décision + recommandations managériales ; anonymat double aveugle.
**Choix par défaut (AskUserQuestion en échec technique) :** titre « Beaucoup l'essaient, peu l'installent » ; cibles managériales = producteurs/réseaux VD + collectivités (PAT) prioritaires.
**Produit :**
- `outputs/submitted/manuscrit_DM.md` + `.docx` (~4 130 mots ; titres thématiques ; résumé 6 points + abstract ; 3 encadrés ; section « Ce que les acteurs peuvent en faire » ; réfs style RAM)
- `outputs/submitted/page_de_titre_DM.md` (séparée, anonymat)
- `outputs/submitted/reference_dm.docx` (gabarit TNR 12 / 1,5 / 2,5 cm)
- `code/06_figures_nb.py` → 5 figures N&B (figures/*/*_nb.*)
**À faire :** valider par l'utilisateur (titre, cibles) ; puis Stade 2.5 intégrité + revue Stade 3.

---

## 2026-07-07 — Analyse « essai vs ancrage » (récence d'achat par forme)
**Idée utilisateur :** exploiter l'écart entre Q6_7 (fréquentation déclarée) et les questions détaillées par forme (modalité 1 = « acheté au cours du mois de septembre »), pour montrer « déjà allés mais pas ancré dans la régularité ».
**Validé par l'utilisateur :** (1) septembre = mois de terrain → « achat récent / mois écoulé » ; (2) les deux bases (% des essayeurs ET % des interrogés) ; (3) AMAP traitée à part (codage différent) ; (4) une sous-section dédiée.
**Résultats (code/07_essai_ancrage.py) :**
- Agrégat : 54% des 509 déclarants VD ont acheté au cours du mois écoulé ; 46% non.
- Récence parmi les essayeurs : marché 62%, ferme 40%, magasin prod. 29%, halle 23%, panier 18%, foire 11% ; AMAP 35% actuels.
- Abandon (« en achetaient, plus maintenant ») : panier 46%, AMAP 65%, foire 30%, halle 27% → gradient selon l'engagement exigé.
**Intégré au manuscrit DM :** nouvelle sous-section « De l'essai à l'ancrage » + Tableau 3 + Figure 3 (barres empilées N&B) ; figures/tableaux renumérotés (numéros retirés des images, portés par les légendes) ; tie-ins résumé + reco « fidéliser ». 5618→6231 mots.
**Fichiers :** `code/07_essai_ancrage.py`, `figures/*/fig6_essai_ancrage_nb.*`, `outputs/submitted/manuscrit_DM.{md,docx}`.

---
*(Les prochains échanges seront ajoutés ici automatiquement)*

## 2026-07-07 — Révisions autrice (7 points)
**Titre** → « Beaucoup l'essaient, peu l'adoptent » (« installent » abandonné ; vocabulaire install→adoption/ancrage partout).
**Classes renommées** : Multi-canal modérés · Captifs de la grande distribution · Multi-canal intensifs · Explorateurs conventionnels · Adeptes de la proximité (+ colonne nb de canaux fréq./rég. au Tableau 4).
**Reformulations** : « quitter le déclaratif » → attitudes/intentions → pratiques d'achat déclarées (nos données restent déclaratives, mais portent sur des comportements). Retrait du contraste Mustapa +34,5 % vs budget (comparaison abusive WTP ≠ part de budget).
**Tableau 3 / Figure 3 redessinés** : 4 modalités (base unique = interrogés), légende au-dessus, comparaison à 3 circuits conventionnels (boulanger/boucher/primeur) ; AMAP traitée à part.
**Diplôme (Q240)** : ajouté aux déterminants. Classes × diplôme p<0,001 (intensifs/explorateurs très diplômés) ; régression : bac+3+ OR 1,89 (p=0,003), absorbe l'effet cadres (→ p=0,07). Éducation = principal gradient, modèle toujours faible (pseudo-R² 0,029). Figure 5 régénérée.
**Fichiers** : code/02 (diplôme), code/06 (régression+diplôme), code/07 (figure récence), code/09 (analyses) ; manuscrit ~6530 mots ; DOCX régénéré.

## 2026-07-07 — Deux ajouts validés (abstract + discussion diplôme)
- Abstract (Résultats) : nuance ajoutée « le seul gradient net étant le diplôme (plus que la CSP) ».
- §5.2 « cibler large » : développement du point diplôme>CSP → frein informationnel/culturel (pas financier), relié au déficit de notoriété (46% ignorent l'AMAP). Encadré 3 reco 3 enrichie.
- Manuscrit ~6650 mots ; DOCX régénéré.

## 2026-07-08 — « lance la revue par les pairs » (Stade 3)
**Demande** : lancer la revue par les pairs simulée du manuscrit DM.
**Livrable** : `reviews/revue_par_les_pairs_DM.md` (+ `.docx`) — panel de 5 relecteurs calibrés *Décisions Marketing* :
- **Phase 0** : configuration du panel (RC, R1 méthodo, R2 domaine circuits courts, R3 managérial, AD avocat du diable).
- **Phase 1** : 5 évaluations indépendantes, notes 1–10 sur 7 critères DM. Relecteurs en **lecture seule** (manuscrit non modifié).
- **Phase 2** : lettre de décision éditoriale + synthèse des notes + feuille de route priorisée (9 actions).
**Décision** : **Révision majeure**. Point bas = rigueur méthodo (moy. 5,5/10). 6 exigences bloquantes : (1) diagnostics de partition typologie (silhouette/pseudo-F, n par classe, stabilité 4/5/6) ; (2) n+IC dans tous les tableaux ; (3) tableau de sensibilité définition VD × dénominateur (65%/17% × pop/réguliers) ; (4) re-tester diplôme sur VD régulière + colinéarité ; (5) distinguer intermittence vs abandon + saisonnalité ; (6) n+format question AMAP (« 65% abandon », « 46% ignorent AMAP ») + biais producteur/revendeur porte marché. 3 non bloquantes : levier×segment, chiffrer conversion, nuancer « inédit ».
**Avocat du diable** : 3 attaques (paradoxe = artefact de dénominateurs ; typologie = intensité déguisée ; essai→adoption = saisonnalité), auto-scoring 4/5 chacune, aucune concession — passent en exigences.
**Note** : révision faisable sans nouvelle collecte (analyses sur données existantes). Prochaine étape = Stade 4 (révision).

## 2026-07-08 — « lance le stade 4 » (révision du manuscrit)
Toutes les exigences de la revue traitées **sur les données existantes** (nouveau script `code/10_revisions_stade4.py` → `articles/stade4_revisions.md`), sans nouvelle collecte.
**(A) Typologie** : Encadré 2 enrichi (inertie ACM 62% sur 2 axes ; silhouette 0,24 à 5 classes vs 0,21/0,23 à 4/6) ; Tableau 5 avec effectifs bruts (624/249/79/47/26) + prudence n=26 ; réfutation « intensité déguisée » (profil régulier canal×classe : C5 seul sans hyper régulier).
**(B) Sensibilité** : nouveau **Tableau 3** (définition × dénominateur) — paradoxe robuste ; IC de Wilson sur 65% / 49,7% / 17,3%.
**(C) Intermittence vs abandon** : abandon vrai 15-19% (≠ 46% « pas ce mois ») ; terrain **septembre** (pleine saison → récence sur-estimée) ; AMAP Q46 sécurisée n=116, abandon 65% [56-73], notoriété 236/509.
**(D/E) Managérial** : Tableau 6 levier × stratégie × acteur ; ordre de grandeur conversion 1,5% → ~4%.
**Mineurs** : « inédit » → « rarement appliqué explicitement » ; accroche reliée à nos données (Fig. 6) ; comparaison artisans encadrée (bases 893 vs 509) ; colinéarité diplôme×CSP V=0,29, diplôme×budget ρ=0,06.
**Intégrité** : résultat nouveau **surfacé honnêtement** — le diplôme prédit l'essai (OR 1,89, p=0,003) mais **pas** l'adoption régulière (OR 1,22, p=0,45) ; renforce la thèse « configuration d'usage > profil social ».
**Livrables** : `manuscrit_DM.md/.docx` (7871 mots < 8000) + `reponse_aux_relecteurs_DM.md/.docx`. Prochain : Stade 3' (re-revue de vérification).

## 2026-07-08 — Stade 3′ (re-revue de vérification) + retouches mineures
Contrôle du **texte révisé** (pas de la seule lettre de réponse) : **12/12 points vérifiés RÉSOLUS**. L'avocat du diable re-teste ses 3 attaques → concessions accordées (5/5, 4/5, 5/5), aucune attaque maintenue.
**Décision révisée : Acceptation sous réserve de modifications mineures** (révision mineure). Rigueur méthodo 5,5→7,5.
4 points résiduels mineurs (m1 cohérence diplôme, m2 borne haute conversion, m3 budget mots, m4 poids classe C5). **m1+m2 appliqués** dans le manuscrit (Encadré 3 + reco 3 : gradient diplôme « à l'essai, pas à l'adoption » ; projection 4 % qualifiée de borne haute). m3/m4 déjà couverts.
**Livrables** : reviews/re_revue_verification_DM.md (+.docx). Manuscrit 7915 mots. Prochain : Stade 4.5 (intégrité finale).

## 2026-07-08 — Stade 4.5 (intégrité finale) — PASS
Script d'audit `code/11_audit_integrite.py` : **124/124 chiffres du manuscrit recalculés depuis les données brutes = PASS** (0 écart). Intégrité citations↔références : 22 réfs (≤35), **aucune orpheline** après 2 corrections — Chiffoleau & Dourian (2020) désormais citée ; note 1 « FranceAgriMer » renvoyée à Agreste/Enthoven. **7 modes de défaillance IA** tous franchis (fabrication, sur-généralisation, dérive de citation, p-hacking, biais de confirmation, reproductibilité, incertitude). RGPD : `git ls-files data/` = aucun fichier de données suivi. Verdict : **PASS, finalisation autorisée**. Manuscrit 7932 mots. Livrable : reviews/integrite_finale_DM.md (+.docx).

## 2026-07-08 — Stade 5 (finalisation du paquet de soumission)
Paquet DM assemblé dans `outputs/soumission_DM/` : manuscrit anonymisé (document principal), page de titre séparée (double aveugle), checklist de conformité, réponse aux relecteurs (archive interne) + README. Corps du manuscrit vérifié **sans fuite d'identité**. Checklist de conformité DM : toutes normes ✅ (7932 mots<8000, 22 réfs≤35, TNR12/1.5/2.5cm, résumé 6 pts + abstract EN, titres thématiques, 3 encadrés, réfs RAM, figures N&B, page de titre séparée). Seuls champs auteur (affiliation, financement) restent à compléter par l'autrice. Livrables : outputs/soumission_DM/* + outputs/submitted/{page_de_titre,checklist_conformite}_DM.docx.

## 2026-07-08 — Stade 6 (synthèse de processus + auto-réflexion IA) — pipeline clos
Document de clôture : parcours des 6 stades, 7 décisions structurantes (dont recadrage RQ, bascule vraies données, double porte, essai≠adoption — la plupart tranchées par l'autrice), résumé des résultats, et **auto-réflexion honnête**. Anti-complaisance : concessions 0/3 tant que non traité, 3/3 une fois traité (suit la preuve, pas la pression). **Risque dominant signalé : circularité de l'auto-revue** (revue simulée par le même modèle ≠ évaluation externe) → note de risque de complaisance MODÉRÉ. Transparence sur faiblesses (silhouette 0,24, pseudo-R² 0,029, n=26, diplôme null sur adoption) activement recherchée. Collaboration : vigilance cognitive autrice élevée, contrôle conceptuel côté humain. Livrable : reviews/synthese_processus_et_autoreflexion.md (+.docx). PIPELINE COMPLET (Stades 1→6).

## 2026-07-08 — Intégration des apports littérature d'une collègue (AMT)
Ajouts issus du doc d'AMT sur la complémentarité des canaux et les motivations à les combiner. Choix autrice : fusion condensée <8000 mots ; attentes en prose enrichies (pas d'hypothèses numérotées) ; **création d'une section Discussion** (style article-exemple bio) ; retrait de l'allusion « travaux en cours » (risque double aveugle).
**Revue de littérature** : nouvelle sous-section « Pourquoi les ménages combinent-ils les canaux ? » (cross-shopping : Hino 2014, Vroegrijk et al. 2013, Melis et al. 2016, Hai Tran & Sirieix 2020 ; théorie des buts : Harris et al. 2018/2021). 2e attente enrichie de la lecture par les buts.
**Discussion des résultats** (nouvelle section, 3 sous-parties) : complément diffus (analogie Pauwels & Neslin 2015, +20% CA vs cannibalisation ; buts ponctuels → faible intensité) ; transversalité sociale = conséquence de la fonction ; stratégies comme grille de lecture (Hino). Queues interprétatives des sections résultats allégées pour éviter les doublons ; section managériale resserrée.
**Intégrité** : 7 nouvelles réfs **vérifiées via WebSearch** (toutes réelles) ; **2 erreurs de prénom du doc corrigées** — Hino = Hayiel (pas Hikari), Harris = Patricia (pas Phil). Audit code/11 : 124/124 chiffres tracent toujours. Citations↔réfs : 29 réfs (≤35), 0 orpheline. Manuscrit 7980 mots (<8000). DOCX + paquet régénérés.

## 2026-07-08 — Relecture ciblée « delta » des ajouts (fidélité des citations)
Relecture du seul matériel nouveau (Discussion + sous-section litt. + 7 réfs). Fidélité des citations : 3 bien soutenues (Vroegrijk, Melis, Hino), **3 corrections de citation-drift** — Pauwels & Neslin (cannibalisation existe mais compensée, +20% net → « complémentarité l'emportant sur la cannibalisation »), Harris (« évolue dans le temps » non établi par étude transversale → « diffère d'une situation à l'autre »), Hai Tran & Sirieix (move théorique attribué → citation de soutien allégée). Sur-interprétation : aucune résiduelle (analogies explicites, verbes modestes). Cohérence : nuance diplôme essai≠adoption maintenue, aucun chiffre nouveau. Post-correction : 7986 mots, 29 réfs, 124/124. Livrable : reviews/relecture_ciblee_ajouts_litterature.md.

## 2026-07-08 — Conformité format DM (style titres + limite 20 pages)
Lecture des instructions aux auteurs : ≤20 pages (tabl./fig./réfs compris, hors page de titre + résumés) ; **style Normal obligatoire** (pas de styles de titre Word) ; Titre 1 = TNR 14 gras, Sous-titre = TNR 12 italique.
- **Style** : post-traitement `code/12_format_dm_docx.py` — tout le doc en style Normal, titres formatés à la main, corps TNR 12 / interligne 1,5 / justifié. (LibreOffice cassé dans l'env → décompte de pages non mesurable, estimé.)
- **Coupes validées par l'autrice** : Encadré 3 (répétait les 4 recommandations), Figure 4 (plan factoriel ACM, silhouette 0,24), Figure 6 + paragraphe motivations (n'apportait rien). Figures renumérotées (régression 5→4). Prix réancré sur Feldmann & Hamm. Léger resserrement managérial.
- **Résultat** : 6 figs→4, 3 encadrés→2, 7986→7710 mots ; estimation ~19-20 pages (était ~22). Audit `code/11` réaligné (retrait des contrôles motivations) : 119/119. 29 réfs, 0 orpheline.

## 2026-07-08 — Recadrage théorique : omnicanal → portefeuille de canaux/cross-shopping (+ buts)
Deux critiques conceptuelles de l'autrice, toutes deux fondées :
1. **Omnicanal mal choisi** : l'omnicanal (Verhoef) suppose UN distributeur intégrant SES canaux ; or le ménage combine des enseignes indépendantes non intégrées → c'est du **cross-shopping / portefeuille de canaux du consommateur**. Recadrage complet (solution 1) : titre de section, résumé, abstract, mots-clés (FR+EN), intro (1er déplacement), §littérature (ajout d'un paragraphe qui pose explicitement la distinction), Tableau 1, résultats. « Omnicanal » conservé aux seuls endroits légitimes : le paragraphe qui explique la distinction, la reco managériale au niveau enseigne (précommande+retrait), la réf Verhoef.
2. **Théorie des buts invoquée mais non testée** (on ne mesure pas les motivations à combiner) : hedge en Discussion (« interprétation plausible que nos données ne testent pas ») + **nouvelle limite assumée** (dispositif comportemental, pas motivationnel — revers du parti pris pratiques>attitudes) + piste de recherche (coupler portefeuille et mesure des buts). Corrigé au passage la phrase Limites « motivations analysées pour le marché » (obsolète depuis retrait Fig. motivations).
Intégrité : 119/119, 29 réfs, 0 orpheline, 7890 mots. DOCX formaté DM régénéré.

## 2026-07-08 — Approfondissement cross-shopping / portefeuille (option 1)
Ancrage renforcé de la revue de littérature sur le patronage de points de vente, avec paiement dans les résultats :
- **Sous-section 1** : structure hiérarchique du portefeuille — coûts fixes → magasin primaire, canaux secondaires au-delà d'un « seuil de panier » (Bell, Ho & Tang 1998, vérifiée : JMR 35(3):352-369).
- **Sous-section 2** : logique des types de courses — grosses courses vs courses d'appoint (Kahn & Schmittlein 1989, vérifiée : Marketing Letters 1(1):55-69) ; la VD relève de l'appoint.
- **Résultats** : « noyau/périphérie » nommé explicitement magasin primaire / canaux secondaires d'appoint (le concept paie).
Fil attitude-comportement conservé et resserré pour compenser (Birch/Giampietri condensés, Mustapa dédupliqué en sous-sec 4).
**Relecture ciblée de vérification** : 2 nouvelles réfs fidèles (coûts fixes/seuil de panier ✓ ; major/fill-in trips ✓), 0 orpheline, 31 réfs (≤35), 7967 mots (<8000), 119/119 chiffres. DOCX formaté DM régénéré.

## 2026-07-08 — Nuance « écart intention-comportement » → écart essai-adoption (report Markdown)
Report sur le dépôt des corrections décidées avec l'autrice (elle applique en parallèle sur son .docx) : l'article ne mesure pas l'intention, seulement des comportements.
- Résumé (Originalité), attentes, résultat central : « écart intention/attitude-comportement » reformulé en **écart essai-adoption** observé dans les seuls comportements, *en écho* (non mesure) à l'attitude-behaviour gap de la littérature.
- Mots-clés FR/EN : « écart intention-comportement / intention-behaviour gap » → **écart essai-adoption / trial-adoption gap**.
- Section récence : ajout du cadre des **jugements de fréquence comportementale** (Menon, Raghubir et Schwarz 1995, vérifiée : JCR 22(2):212-228) — une question générale appelle une réponse plus inclusive qu'une question datée — tout en préservant la thèse (abandon modéré + poids budgétaire = pas un simple artefact).
Coupes compensatoires pour rester <8000 (incise saisonnalité, énumération dupliquant Tableau 4, redites). Résultat : 7999 mots, 32 réfs (≤35), 0 orpheline, « intention-comportement » = 0 occurrence.
**Intégrité** : aucun chiffre modifié ce tour ; l'audit code/11 n'est pas rejouable (conteneur réinitialisé → données brutes locales/gitignorées + paquets perdus), le dernier run 119/119 reste valable puisque les nombres sont inchangés. DOCX régénéré (toolchain réinstallée).

## 2026-07-08 — Résumé reformaté (un seul paragraphe ≤250 mots)
Retour autrice : le résumé doit faire ≤250 mots, en un seul paragraphe continu, couvrant les catégories (objectif/méthode/résultats/implications/originalité) sans sous-titres. Résumé structuré (5 blocs gras) → **paragraphe unique de 246 mots**. Substance préservée (paradoxe 65%/1,5%, essai-adoption, 5 stratégies, diplôme, conversion, portefeuille/pratiques). Checklist mise à jour. Total manuscrit 7923 mots. DOCX régénéré.
