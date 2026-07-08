# Réponse aux relecteurs

**Manuscrit :** « Beaucoup l'essaient, peu l'adoptent » — La vente directe dans les stratégies d'approvisionnement des ménages français
**Revue :** *Décisions Marketing* — décision : **révision majeure**

Nous remercions le comité de lecture et les quatre relecteurs pour une évaluation à la fois exigeante et constructive. Toutes les analyses demandées ont pu être conduites **sur les données existantes**, sans nouvelle collecte. Ci-dessous, chaque exigence est reprise (R = relecteur, AD = avocat du diable), suivie de notre réponse et de la localisation de la modification. Les ajouts de calcul sont reproductibles (`code/10_revisions_stade4.py` → `articles/stade4_revisions.md`).

---

## Exigences bloquantes

### (A) Transparence de la typologie — diagnostics et effectifs (R1, AD-2)

**Demande.** Publier les diagnostics de partition (silhouette / pseudo-F, inertie ACM, effectifs par classe), une analyse de stabilité (4/5/6 classes), et démontrer que les classes diffèrent par la *combinaison* de canaux et non par un simple axe d'intensité. Ajouter les n dans tous les tableaux.

**Réponse — traité.**
- **Encadré 2** enrichi : les deux premiers axes d'ACM concentrent 62 % de l'inertie ; la solution à 5 classes **maximise la silhouette moyenne (0,24**, contre 0,21 à 4 classes et 0,23 à 6), la découpe à 6 ne faisant que scinder le plus gros groupe. La silhouette modérée est explicitement qualifiée et son interprétation (configurations dominantes, non frontières nettes) est posée.
- **Tableau 5** porte désormais les **effectifs bruts** de chaque classe (624 / 249 / 79 / 47 / 26) et une note de prudence sur la plus petite (n = 26).
- **Réfutation de l'attaque « intensité déguisée » (AD-2).** Le calcul de l'usage régulier canal par canal et par classe (reporté dans `articles/stade4_revisions.md`, §1d) montre que les « adeptes de la proximité » sont le **seul groupe sans hyper/super régulier** (différence de *combinaison*, pas d'intensité), et que explorateurs (répertoire large, VD régulière 19 %) et intensifs (répertoire large, VD régulière 67 %) se distinguent à largeur égale : la partition capte bien des configurations. Ce point est résumé au §« Cinq stratégies ».
- **n ajoutés** aux Tableaux 2, 5 et 6 ; IC de Wilson ajoutés aux taux clés (voir B).

### (B) Robustesse du résultat-phare aux dénominateurs et à la définition (R1-4, AD-1)

**Demande.** Ajouter un tableau de sensibilité (pénétration inclusive / régulière × part sur toute la population / chez les réguliers) et montrer que le paradoxe survit. Tester le gradient diplôme sur la définition régulière.

**Réponse — traité.**
- Nouveau **Tableau 3 (sensibilité)** croisant les trois définitions de la vente directe (inclusive 65 % / pénétration 49,7 % / régulière 17,3 %) avec les deux dénominateurs budgétaires (population / réguliers). Le texte qui l'introduit montre que **le paradoxe survit** : sous la définition la plus stricte, la part chez les seuls réguliers (8,5 %) reste minoritaire ; la diffusion large (65 %) coexiste avec un poids national de 1,5 % quelle que soit la porte. L'écart n'est pas un artefact de dénominateur (réponse directe à AD-1).
- **IC de Wilson (95 %)** ajoutés sur les taux clés (65,0 % [62,0–67,8] ; 49,7 % [46,6–52,7] ; 17,3 % [15,1–19,7]).
- **Test sur la VD régulière (R1-4) :** voir (C)/section déterminants — l'effet du diplôme **ne tient pas** sur la définition régulière, ce que nous rapportons honnêtement.

### (C) Distinguer intermittence et abandon ; sécuriser la mesure (R2, AD-3)

**Demande.** Cesser d'amalgamer « pas acheté ce mois-ci » (saisonnalité possible) et « n'achète plus » (abandon). Préciser la période de terrain. Donner n et format de la question AMAP. Discuter le biais producteur/revendeur de la porte marché.

**Réponse — traité.**
- **Période de terrain précisée : septembre** (Encadré 1). Mois de pleine saison pour les marchés : la récence des formes directes est plutôt *sur*-estimée que minorée — l'abandon relevé n'est donc pas un artefact de basse saison (réponse à AD-3).
- **Distinction explicite intermittence / abandon** au §« De l'essai à l'adoption » : le « 46 % qui n'ont rien acheté ce mois-là » relève largement de l'**intermittence** ; l'**abandon vrai** (colonne « n'achète plus » du Tableau 4) reste **modéré (15–19 %** selon les formes). Le titre porte sur le passage essai → habitude (intermittence), non sur un décrochage définitif, qui est limité.
- **AMAP sécurisée (Tableau via §4b des calculs) :** la question Q46 et ses modalités sont explicitées ; le « 65 % d'abandon » est désormais assorti de son effectif (**n = 116** clients passés ou présents : 41 actuels, 75 ayant cessé) et de son **IC (56–73)**, avec mention explicite du faible effectif. Le « 46 % qui ignorent l'AMAP » est rapporté sur base claire (236/509 acheteurs directs).
- **Biais producteur/revendeur de la porte marché** : discuté au §« Limites » (l'item « marché direct producteur » repose sur une auto-déclaration dont la fiabilité est incertaine, une partie des « producteurs » de marché étant des revendeurs — la pénétration inclusive constitue donc une borne haute).

---

## Demandes à forte valeur ajoutée (non bloquantes)

### (D) Différencier les recommandations par segment et par acteur (R3-1, R3-3)

**Traité.** Nouveau **Tableau 6 « levier prioritaire par stratégie et par acteur »** : chaque configuration d'approvisionnement est reliée à son levier (convertir / accès-notoriété / maintenir / basculer / sécuriser l'offre) et à l'acteur le mieux placé (producteurs, réseaux, collectivités). Le texte oriente l'effort de conversion vers les modérés et les explorateurs, l'accès vers les captifs, le maintien vers les intensifs.

### (E) Chiffrer l'enjeu de conversion (R3-2)

**Traité.** Un ordre de grandeur est ajouté à la recommandation « fidéliser » : si les essayeurs irréguliers atteignaient la régularité et l'intensité des réguliers actuels, la part nationale de la vente directe passerait d'environ **1,5 % à ≈ 4 %** (quasi-triplement), hors de portée du seul recrutement. Calcul illustratif toutes choses égales par ailleurs, explicité comme tel.

---

## Points mineurs

| Point (relecteur) | Réponse |
|-------------------|---------|
| Nuancer « inédit » sur le cadre omnicanal (R2) | Reformulé en « rarement appliqué de façon explicite ». |
| Sourcer l'accroche d'introduction (R2) | L'accroche renvoie désormais explicitement à nos propres données (Figure 6 : produits locaux 51 %, soutien aux agriculteurs 34 %). |
| Encadrer la comparaison artisans, bases n = 893 vs 509 (R1) | Note ajoutée au §récence : la comparaison éclaire les ordres de grandeur « sans prétendre à une équivalence stricte entre populations ». |
| Colinéarité diplôme / CSP / budget (R1-3) | Ajoutée à la section déterminants : V de Cramér diplôme × CSP = 0,29 (explique l'atténuation de l'effet « cadres ») ; corrélation diplôme × budget = 0,06 (le diplôme n'est pas un proxy du revenu). |
| Mode d'administration / participation (R1) | Le terrain de septembre et la construction par quotas sont précisés ; le taux de participation d'un panel à quotas n'est pas disponible et n'est pas revendiqué. |

---

## Note d'intégrité sur un résultat révisé

En réponse à la demande (B)/R1-4 de tester le gradient éducatif sur la définition régulière, nous rapportons un résultat que la première version n'explicitait pas : **l'effet du diplôme porte sur l'essai, non sur l'adoption régulière**. Sur la VD inclusive, le bac+3 a un odds-ratio de 1,89 (p = 0,003) ; sur la VD régulière, il retombe à 1,22 (p = 0,45). Nous avons choisi de **surfacer** ce contraste plutôt que de le taire : il renforce la thèse centrale (le profil social prédit à peine qui essaie, et quasiment pas qui adopte — c'est la configuration d'usage qui compte). La section « déterminants » a été amendée en conséquence.

---

*Toutes les modifications sont intégrées à `manuscrit_DM.md` (et au `.docx`). Les calculs justificatifs sont reproductibles via `code/10_revisions_stade4.py`.*
