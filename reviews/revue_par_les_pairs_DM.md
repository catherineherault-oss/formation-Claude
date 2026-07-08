# Revue par les pairs — évaluation simulée

**Manuscrit évalué :** « Beaucoup l'essaient, peu l'adoptent » — La vente directe dans les stratégies d'approvisionnement des ménages français
**Revue cible :** *Décisions Marketing* (DM)
**Type d'évaluation :** double aveugle, panel de 5 relecteurs + avocat du diable
**Date :** 8 juillet 2026

> **Nature de ce document.** Il s'agit d'une **simulation** de processus éditorial produite par le pipeline ARS (Stade 3). Elle vise à identifier, *avant soumission réelle*, les points qu'un comité de lecture de *Décisions Marketing* soulèverait très probablement. Les relecteurs sont des personas calibrés sur les normes et attentes de la revue ; leurs commentaires sont fondés sur le seul contenu du manuscrit. Aucun n'a modifié le texte (règle de lecture seule). Ce document ne remplace pas une évaluation réelle et n'engage pas la revue.

---

## Phase 0 — Configuration du panel

Détection automatique du domaine : **marketing / comportement du consommateur — distribution et circuits alimentaires** ; méthode dominante : **enquête quantitative représentative, typologie (ACM + CAH), régression logistique** ; visée : **contribution managériale** (adéquate au positionnement de *DM*).

| Rôle | Persona | Focale d'évaluation | Poids dans la décision |
|------|---------|---------------------|------------------------|
| **Rédacteur en chef (RC)** | Éditeur *DM*, spécialiste distribution & marketing alimentaire | Adéquation revue, contribution, intérêt managérial, tenue d'ensemble | Décision finale |
| **R1 — Méthodologie** | Statisticien / méthodologue quanti (segmentation, modèles de choix) | Robustesse ACM+CAH, régression, définition des variables, inférence | Fort |
| **R2 — Domaine** | Chercheur circuits courts / sociologie de la consommation alimentaire | Justesse des concepts, ancrage littérature CC, mesure de la « vente directe » | Fort |
| **R3 — Perspective managériale** | Praticien-chercheur (PAT, chambres d'agriculture, distribution) | Actionnabilité, valeur pour le lecteur *DM*, encadrés | Moyen |
| **AD — Avocat du diable** | Relecteur adversarial | Attaque les revendications centrales : le paradoxe, la typologie, l'« adoption » | Bloquant si finding CRITIQUE |

**Critères de notation (échelle 1–10, calibrage *DM*) :** Adéquation revue · Originalité/Contribution · Ancrage théorique · Rigueur méthodologique · Validité des résultats · Implications managériales · Clarté/Rédaction.

---

## Phase 1 — Évaluations indépendantes

### R1 — Relecteur méthodologie

**Recommandation : Révision majeure.**

Le manuscrit est méthodologiquement sérieux pour une revue managériale : échantillon représentatif national, décomposition budgétaire à somme 100 %, triangulation fréquence / budget / récence. La démarche est honnête — les auteur·e·s ne masquent pas la faiblesse de leurs modèles. C'est appréciable. Mais plusieurs choix, aujourd'hui sous-documentés, fragilisent les conclusions et doivent être étayés.

**Points majeurs.**

1. **La typologie est peu robuste et le manuscrit n'en donne pas les diagnostics.** L'Encadré 2 mentionne « un indicateur de qualité de partition » sans le chiffrer. Or une CAH sur coordonnées d'ACM produit fréquemment des partitions à silhouette faible et à classes très déséquilibrées. Ici, les cinq classes vont de 61 % à 2,5 % de l'échantillon : la plus petite (« adeptes de la proximité ») ne compte qu'une poignée de ménages. Il faut **publier les diagnostics** : silhouette (ou pseudo-F / critère de Calinski-Harabasz), inertie expliquée par les axes d'ACM retenus, effectifs bruts (n) de chaque classe, et surtout une **analyse de stabilité** (bootstrap ou comparaison 4/5/6 classes). Sans cela, le lecteur ne peut pas juger si les cinq stratégies sont un résultat ou un artefact de la méthode. La phrase « retenu sur la base d'un indicateur de qualité de partition et de l'interprétabilité » est, en l'état, invérifiable.

2. **Effectifs bruts absents partout.** Le Tableau 4 donne des pourcentages (61 %, 24 %…) mais aucun n. Idem pour les croisements diplôme × stratégie évoqués en section « déterminants » (« 42 à 43 % de bac+3 »). Sur une classe à 2,5 % (~26 ménages), un pourcentage de sous-catégorie repose sur très peu d'observations et ne devrait pas être commenté finement — ce que le manuscrit reconnaît d'ailleurs en limites, mais après l'avoir fait. **Ajouter les n** dans tous les tableaux et **assortir d'intervalles de confiance** les pourcentages clés.

3. **La régression est quasi nulle et sur-interprétée par endroits.** Un pseudo-R² de McFadden de 0,029 signifie que le modèle n'explique presque rien. Les auteur·e·s le disent — et en font même, à juste titre, un résultat (« déterminants ténus »). Mais alors il faut être cohérent : un odds-ratio isolé et significatif (diplôme bac+3 : OR = 1,89) dans un modèle qui n'explique rien doit être présenté avec la plus grande prudence, car sa robustesse est douteuse. Je demande : (a) le **n effectif** de la régression et le taux d'événements (VD = 1) ; (b) un **test de la variable dépendante** — la définition à « double porte » mélange un canal (Q6_7) et un item de marché (Q22), ce qui peut créer de l'hétérogénéité ; refaire le modèle sur la définition **régulière** (17 %) en variable dépendante pour vérifier que le gradient diplôme tient ; (c) la matrice de corrélation diplôme/CSP/budget (colinéarité probable, qui explique l'évanouissement de l'effet « cadres »).

4. **La sensibilité de la définition de la vente directe n'est pas testée.** Tout l'article bascule selon qu'on retient 65 % (pénétration, union des deux portes) ou 17 % (régulier). Le titre lui-même (« beaucoup l'essaient, peu l'adoptent ») EST cette sensibilité. C'est légitime — mais il faut un **tableau de sensibilité** montrant comment les résultats clés (poids budgétaire, déterminants, typologie) se déplacent selon la définition retenue. Actuellement le lecteur doit reconstituer lui-même que « 65 % » et « 1,5 % » ne portent pas sur le même dénominateur.

5. **Le comparateur conventionnel du Tableau 3 repose sur des bases différentes (n = 893 artisans vs n = 509 acheteurs directs).** Comparer des %-ligne calculés sur des populations distinctes est acceptable si c'est explicité — ce que fait la note de tableau — mais la lecture « le boucher (37 %) est au niveau de l'achat à la ferme (34 %) » sous-entend une comparabilité que les bases différentes ne garantissent pas (populations non identiques, biais de sélection). À **encadrer** : soit restreindre la comparaison à la sous-population commune, soit reformuler pour ne pas suggérer une équivalence stricte.

**Points mineurs.** Préciser la période de terrain (une enquête de septembre biaiserait la récence pour les produits saisonniers — cf. R2). Donner la formulation exacte de la question de récence et de la question AMAP (traitée « à part »). Indiquer le mode d'administration (en ligne ? face-à-face ?) et le taux de participation.

**Notes.** Adéquation revue 8 · Originalité 7 · Théorie 6 · **Rigueur méthodo 5** · Validité résultats 6 · Implications 8 · Clarté 8.

---

### R2 — Relecteur domaine (circuits courts / consommation alimentaire)

**Recommandation : Révision majeure (proche de mineure sur le fond, majeure sur la mesure).**

Contribution réelle et bienvenue. La littérature française et européenne sur les circuits courts souffre effectivement d'un déficit de données représentatives côté ménage : la plupart des travaux sont qualitatifs, monographiques ou portent sur des populations d'acheteurs déjà engagés. Poser la vente directe **dans le portefeuille de canaux** et la mesurer sur un échantillon national est une contribution que *DM* a intérêt à publier. Le mobilisé (Enthoven & Van den Broeck, Chiffoleau, Dubuisson-Quellier, Feldmann & Hamm) est pertinent et à jour. J'ai néanmoins des réserves de fond sur la **définition de l'objet** et sur quelques raccourcis.

**Points majeurs.**

1. **La « double porte » gonfle mécaniquement la pénétration et mérite discussion, pas seulement justification.** Réunir « achat direct aux agriculteurs hors marché » et « achat à un producteur sur le marché » pour atteindre 65 % est défendable conceptuellement (le marché est bien un lieu de contact direct). Mais l'item « marché » ne distingue pas toujours, dans l'esprit du répondant, le producteur du revendeur — c'est un problème classique et documenté. Les 157 ménages ajoutés par cette porte reposent sur une **auto-déclaration d'achat "directement auprès d'un producteur"** dont la fiabilité est incertaine (beaucoup de « producteurs » de marché sont des revendeurs). Il faut discuter ce biais, pas seulement l'invoquer comme un gain de couverture. Sinon le chiffre-phare (65 %) prête le flanc.

2. **L'AMAP est traitée « à part » et pourtant mobilisée dans une des conclusions les plus fortes (65 % d'abandon).** Ce « 65 % d'abandon des AMAP » est frappant et repris en Encadré 3 et en implications. Or il provient d'une question au format différent (sans référence au mois écoulé), sur une **sous-population de clients passés ou présents** dont l'effectif n'est pas donné. Si cet effectif est faible, le chiffre est fragile ; s'il est robuste, c'est un résultat marquant qui mérite son propre développement. **Donner le n** et harmoniser le statut de ce chiffre (soit résultat pleinement intégré, soit signalé comme indicatif).

3. **Confusion possible entre "notoriété" et "non-réponse".** Le manuscrit interprète la modalité « ne connaît pas cette forme » comme un **déficit de notoriété** (46 % ignorent ce qu'est une AMAP). C'est une lecture forte. Une part de ces réponses peut relever de la non-familiarité avec le *terme* plutôt que du *dispositif*, ou d'un désengagement de la question. Le « 46 % qui ignorent l'AMAP » **parmi des acheteurs directs** est contre-intuitif et central dans l'argumentaire ; il faut le sécuriser (formulation exacte de l'item, part de non-réponse, cohérence avec d'autres enquêtes de notoriété type ADEME/FranceAgriMer).

4. **Saisonnalité.** La récence « le mois écoulé » est très sensible à la période d'enquête pour des produits de circuit court fortement saisonniers (fruits, légumes, marchés de plein air). Une enquête d'hiver et une enquête d'été ne donneraient pas la même photo. **Préciser la période** et discuter ce que cela implique pour la lecture « de l'essai à l'adoption » — l'abandon apparent pouvant être une simple intermittence saisonnière plutôt qu'un décrochage.

5. **Cadre omnicanal : contribution réelle mais revendication d'inédit à tempérer.** L'application du cadre omnicanal (Verhoef, Neslin) à l'alimentation locale est stimulante et bien menée. Mais affirmer que « l'application explicite du cadre omnicanal à l'alimentation directe reste inédite » est risqué : des travaux en *food retailing* et en *local food channel choice* mobilisent déjà des logiques multicanal. **Nuancer** (« rarement appliqué de façon explicite » plutôt que « inédit ») évite qu'un relecteur exhibe un contre-exemple.

**Points mineurs.** L'introduction (« sur un marché de plein vent, la moitié des clients… ») est vivante mais l'accroche gagnerait une source. Vérifier « 6,8 canaux » (moyenne) — sensible à la définition de « fréquente ». Le terme « adoptent » du titre est bien choisi (cf. littérature diffusion/adoption) mais mériterait d'être relié explicitement à ce cadre en discussion.

**Notes.** Adéquation revue 8 · Originalité 7 · **Théorie 7** · Rigueur méthodo 6 · Validité résultats 6 · Implications 8 · Clarté 9.

---

### R3 — Relecteur perspective managériale

**Recommandation : Révision mineure.**

De mon point de vue — celui du lecteur de *DM* qui cherche un enseignement actionnable — c'est un bon article. Le renversement de diagnostic (le problème n'est pas l'acquisition mais la rétention) est clair, contre-intuitif et utile. Les quatre recommandations de l'Encadré 3 sont directement lisibles par un producteur, une chambre d'agriculture ou un porteur de PAT. C'est exactement le registre attendu par la revue. Mes réserves portent sur la **spécificité** et la **preuve** des recommandations, pas sur leur pertinence.

**Points à renforcer.**

1. **Les recommandations sont justes mais génériques.** « Fidéliser plutôt que recruter », « investir la logistique », « communiquer local et qualité » sont des conseils solides mais que beaucoup d'acteurs formulent déjà. La valeur ajoutée de l'article serait de les **différencier par stratégie d'approvisionnement** : que faire, concrètement, pour convertir un « explorateur conventionnel » (essaie tout, ne retient rien) par rapport à un « multi-canal modéré » ? Le manuscrit affirme que « chaque configuration appelle un levier différent » — il faut alors **livrer ce tableau levier × segment**, qui serait le vrai apport managérial et distinguerait l'article des rapports professionnels existants.

2. **Chiffrer l'enjeu.** L'article dit que convertir les 48 % d'essayeurs irréguliers « produirait un effet budgétaire bien supérieur au recrutement ». C'est l'argument central côté action — il faut l'**objectiver** par un ordre de grandeur (même grossier) : si un essayeur irrégulier passait à la fréquence d'un régulier, quel gain de part de budget ? Un back-of-the-envelope crédible rendrait la recommandation nettement plus convaincante pour un décideur.

3. **À qui s'adresse chaque recommandation ?** Le manuscrit vise « producteurs et réseaux », « collectivités », « grande distribution ». Bien. Mais les leviers diffèrent radicalement selon l'acteur. Une **table d'acteurs** (producteur isolé / réseau / collectivité / GMS → levier prioritaire) clarifierait l'actionnabilité et éviterait l'effet catalogue.

4. **Encadrés : très bon dispositif *DM*.** Les trois encadrés méthode + l'encadré recommandations sont bien pensés et fidèles au format de la revue. Suggestion : un **encadré « en pratique »** avec un mini-cas ou un exemple concret de dispositif de régularité (drive fermier, abonnement souple) ancrerait les conseils.

**Notes.** Adéquation revue 9 · Originalité 7 · Théorie 6 · Rigueur méthodo 6 · Validité résultats 7 · **Implications 7** · Clarté 9.

---

### AD — Avocat du diable

**Mandat :** attaquer les revendications centrales. Aucun *finding* CRITIQUE bloquant l'acceptation n'est retenu après vérification — mais **trois attaques sérieuses** doivent recevoir une réponse explicite en révision, faute de quoi elles redeviendront bloquantes.

**Attaque 1 — Le « paradoxe » est en partie une construction du choix des dénominateurs.**
Le résultat-phare oppose « 65 % des ménages » à « 1,5 % du budget ». Mais 65 % est une pénétration à définition maximale (double porte, tout achat même unique) et 1,5 % une part budgétaire moyenne sur *toute* la population, plancher par construction (budget non demandé aux non-réguliers, comptés à 0). On compare donc le chiffre le plus généreux possible à gauche au plus conservateur possible à droite. Le « paradoxe » est réel dans son principe (adhésion large ≠ poids budgétaire), mais **son amplitude est en partie un artefact de cadrage**. *Réponse attendue :* présenter, côte à côte et sur bases explicites, pénétration régulière (17 %) ET part chez les réguliers (8,5 %) — ce que l'article fait, mais dispersé. Le paradoxe doit survivre à la mise à plat des dénominateurs. Je pense qu'il survit, atténué ; il faut le montrer.

**Attaque 2 — La typologie ne "fait émerger" peut-être rien.**
« La typologie fait émerger cinq stratégies distinctes. » Avec une classe à 61 % et une à 2,5 %, une lecture adverse est : *il y a un gros groupe indifférencié (la majorité des Français) et quelques petits groupes de queue de distribution*, ce qui n'est pas une "typologie de stratégies" mais la structure ordinaire d'une intensité d'usage (peu / moyen / beaucoup). *Réponse attendue :* diagnostics de partition (cf. R1) + démonstration que les cinq classes diffèrent sur la **combinaison** de canaux et pas seulement sur un axe unique d'intensité (sinon un simple score d'intensité suffirait et la CAH est superflue). Si les classes ne se distinguent que par « combien de canaux », il faut le dire et simplifier l'argument.

**Attaque 3 — Le récit "essai → adoption" pourrait n'être qu'une saisonnalité.**
« 46 % n'ont rien acheté au cours du mois écoulé » est lu comme un défaut de rétention. Lecture adverse : pour des produits saisonniers achetés en circuit court, ne pas avoir acheté *ce mois-ci* est **normal et attendu**, pas un signe d'abandon. Le vrai abandon (« n'achète plus ») est bien plus bas (15-18 % selon les formes). L'article amalgame par moments « pas ce mois-ci » (intermittence) et « décrochage » (abandon). *Réponse attendue :* distinguer nettement, dans le texte et pas seulement dans le tableau, **intermittence** et **abandon** ; ne pas laisser la formule-titre reposer sur la confusion des deux. Le taux d'abandon vrai (colonne « n'achète plus ») est le bon indicateur de non-rétention, et il est modéré.

**Auto-scoring de la solidité des attaques (protocole anti-complaisance, 1–5) :** Attaque 1 = 4/5 · Attaque 2 = 4/5 · Attaque 3 = 4/5. Aucune n'est réfutée par le manuscrit en l'état ⇒ aucune concession ; les trois passent en exigences de révision.

**Ce que l'AD ne conteste pas** (et qui tient) : la contribution « côté ménage sur données représentatives » est réelle ; le déficit de données représentatives est avéré ; l'honnêteté des limites est exemplaire ; l'écriture est de qualité publiable.

**Notes.** Adéquation revue 7 · Originalité 6 · Théorie 6 · Rigueur méthodo 5 · Validité résultats 5 · Implications 7 · Clarté 8.

---

## Phase 2 — Lettre de décision éditoriale (Rédacteur en chef)

**Décision : RÉVISION MAJEURE (Major Revision).**

Chère Autrice, cher Auteur,

Votre manuscrit « Beaucoup l'essaient, peu l'adoptent » a été évalué par quatre relecteurs et soumis à une lecture adversariale. Je partage l'avis d'ensemble du comité : **le sujet, l'angle et la contribution correspondent bien à *Décisions Marketing***, et l'article a de réelles qualités — une question managériale nette, un renversement de diagnostic contre-intuitif (rétention plutôt qu'acquisition), des données représentatives rares sur ce terrain, une écriture claire et un usage des encadrés fidèle à l'esprit de la revue. L'honnêteté avec laquelle vous exposez les limites de vos modèles a été unanimement saluée.

Il ne s'agit donc pas de refonder l'article, mais de **sécuriser sa charpente probante**. Trois exigences structurantes ressortent, convergentes entre les relecteurs :

**(A) Transparence méthodologique de la typologie et des effectifs (R1, AD-2).** Le cœur analytique — les cinq stratégies — n'est aujourd'hui pas vérifiable par le lecteur. Vous devez publier les diagnostics de partition (silhouette ou pseudo-F, inertie des axes d'ACM, effectifs bruts n de chaque classe), une analyse de stabilité (comparaison 4/5/6 classes) et démontrer que les classes diffèrent par la *combinaison* de canaux et non par un simple axe d'intensité. Ajoutez les n dans tous les tableaux et des intervalles de confiance sur les pourcentages clés ; entourez de prudence explicite tout commentaire sur la plus petite classe.

**(B) Robustesse du résultat-phare aux dénominateurs et à la définition (R1-4, AD-1).** Le contraste 65 % / 1,5 % est votre signature, mais il oppose la mesure la plus généreuse à la plus conservatrice. Ajoutez un **tableau de sensibilité** (pénétration inclusive / régulière × part sur toute la population / chez les réguliers) et montrez que le paradoxe survit à cette mise à plat. Testez la robustesse du gradient « diplôme » sur la définition régulière de la vente directe.

**(C) Distinguer intermittence et abandon ; sécuriser la mesure (R2, AD-3).** Le récit « de l'essai à l'adoption » doit cesser d'amalgamer « pas acheté ce mois-ci » (possible saisonnalité) et « n'achète plus » (abandon réel). Précisez la période de terrain, discutez la saisonnalité, donnez le n et le format exact de la question AMAP (le « 65 % d'abandon » et le « 46 % qui ignorent l'AMAP » sont trop centraux pour rester sous-documentés), et discutez le biais producteur/revendeur de la « porte marché ».

S'ajoutent deux demandes à forte valeur ajoutée, non bloquantes mais vivement encouragées :

**(D) Différencier les recommandations par segment et par acteur (R3-1, R3-3).** Livrez le tableau *levier × stratégie d'approvisionnement* que le texte promet, et une table d'acteurs (producteur / réseau / collectivité / GMS). C'est ce qui distinguera l'article d'un rapport professionnel.

**(E) Chiffrer l'enjeu de conversion (R3-2)** par un ordre de grandeur du gain budgétaire potentiel.

**Points mineurs** à traiter : nuancer la revendication d'« inédit » sur le cadre omnicanal (« rarement appliqué explicitement ») ; sourcer l'accroche d'introduction ; préciser mode d'administration et participation ; encadrer la comparaison artisans (bases n = 893 vs 509) pour ne pas suggérer une équivalence stricte.

**Conformité aux normes *DM* :** longueur (~6 750 mots < 8 000 ✔), références (~24 ≤ 35 ✔), résumé structuré ✔, abstract EN ✔, encadrés ✔, figures N&B ✔, titres thématiques ✔, page de titre séparée ✔. La forme est conforme ; ne l'alourdissez pas — plusieurs demandes ci-dessus peuvent loger en encadré méthode ou en annexe en ligne pour préserver le budget de mots.

Nous serions heureux de recevoir une version révisée accompagnée d'une **lettre de réponse point par point**. Les exigences (A), (B) et (C) conditionnent l'acceptation ; (D) et (E) en renforceraient nettement la portée.

Avec nos encouragements,
*Le Rédacteur en chef, pour le comité de lecture*

---

## Synthèse des notes

| Critère (1–10) | R1 | R2 | R3 | AD | Moyenne |
|----------------|:--:|:--:|:--:|:--:|:-------:|
| Adéquation revue | 8 | 8 | 9 | 7 | **8,0** |
| Originalité / contribution | 7 | 7 | 7 | 6 | **6,75** |
| Ancrage théorique | 6 | 7 | 6 | 6 | **6,25** |
| Rigueur méthodologique | 5 | 6 | 6 | 5 | **5,5** |
| Validité des résultats | 6 | 6 | 7 | 5 | **6,0** |
| Implications managériales | 8 | 8 | 7 | 7 | **7,5** |
| Clarté / rédaction | 8 | 9 | 9 | 8 | **8,5** |

**Décision consolidée : Révision majeure.** Consensus : contribution et adéquation *DM* fortes, rédaction excellente ; le point bas est la **rigueur méthodologique** (transparence de la typologie, robustesse aux dénominateurs, distinction intermittence/abandon). Aucune faiblesse rédhibitoire — l'article est publiable moyennant une révision ciblée et faisable.

---

## Feuille de route de révision (priorisée)

| # | Priorité | Action | Bloquant ? | Où | Coût |
|---|----------|--------|:----------:|----|------|
| 1 | 🔴 Haute | Diagnostics de partition (silhouette/pseudo-F, inertie ACM, **n par classe**) + stabilité 4/5/6 classes | Oui (A) | Encadré 2 / annexe | Moyen |
| 2 | 🔴 Haute | Ajouter **n** et IC dans Tableaux 2–4 ; prudence explicite sur la classe à 2,5 % | Oui (A) | Tableaux | Faible |
| 3 | 🔴 Haute | **Tableau de sensibilité** définition × dénominateur (65 %/17 % × pop/réguliers) | Oui (B) | Section « répandue mais marginale » | Moyen |
| 4 | 🔴 Haute | Re-tester le gradient **diplôme** sur la VD régulière ; donner n régression + colinéarité diplôme/CSP/budget | Oui (B) | Section « déterminants » | Moyen |
| 5 | 🔴 Haute | Distinguer **intermittence** (« pas ce mois-ci ») et **abandon** (« n'achète plus ») dans le texte ; discuter **saisonnalité** + période de terrain | Oui (C) | Section « essai/adoption » | Faible |
| 6 | 🔴 Haute | **n + format** de la question AMAP ; sécuriser « 65 % d'abandon » et « 46 % ignorent l'AMAP » ; biais producteur/revendeur de la porte marché | Oui (C) | Section « essai/adoption » + limites | Moyen |
| 7 | 🟠 Moyenne | Tableau **levier × stratégie** + table d'acteurs (producteur/réseau/collectivité/GMS) | Non (D) | Section recommandations / Encadré 3 | Moyen |
| 8 | 🟠 Moyenne | Chiffrer l'ordre de grandeur du **gain de conversion** des essayeurs irréguliers | Non (E) | Recommandation 1 | Faible |
| 9 | 🟡 Basse | Nuancer « inédit » → « rarement appliqué explicitement » ; sourcer l'accroche ; mode d'administration & participation ; encadrer la comparaison artisans | Non | Introduction / méthode / Tableau 3 | Faible |

**Estimation :** révision faisable sans nouvelle collecte (toutes les analyses demandées se font sur les données existantes). Les items 1–6 conditionnent l'acceptation ; 7–8 augmentent sensiblement la valeur managériale ; 9 sécurise contre des objections faciles.

---

*Évaluation simulée produite par le pipeline ARS — Stade 3 (academic-paper-reviewer). Relecteurs en lecture seule : le manuscrit n'a pas été modifié. Ce document alimente le Stade 4 (révision).*
