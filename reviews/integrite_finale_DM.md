# Rapport d'intégrité finale (Stade 4.5)

**Manuscrit :** « Beaucoup l'essaient, peu l'adoptent » — La vente directe dans les stratégies d'approvisionnement des ménages français
**Revue cible :** *Décisions Marketing*
**Objet :** dernier verrou avant finalisation — traçabilité numérique, intégrité bibliographique, gouvernance des données, et passage au crible des 7 modes de défaillance de la recherche assistée par IA.
**Date :** 8 juillet 2026

> Ce rapport est le **gate d'intégrité** du pipeline : il ne juge pas la qualité éditoriale (déjà traitée aux Stades 3/3′) mais l'**honnêteté et la traçabilité** de chaque affirmation quantitative et de chaque source. Verdict binaire : PASS (finalisation autorisée) ou BLOCK.

---

## 1. Traçabilité numérique — recalcul intégral depuis les données brutes

Un script d'audit (`code/11_audit_integrite.py`) **recalcule depuis `24407_Export.xlsx`** chaque chiffre affiché dans le manuscrit et le confronte à la valeur écrite (tolérance 0,5 pt sur les %).

**Résultat : 124 / 124 contrôles PASS, 0 écart.**

Périmètre vérifié (échantillon exhaustif des chiffres du texte) :
- Échantillon et démographie (N = 1 025, 52,6 % femmes, 26,0 % 65+, budget médian 400 € / moyen 436 €).
- Pénétration et budget de la vente directe (65,0 % / n = 666 ; 49,7 % / n = 509 ; 17,3 % / n = 177 ; 1,5 % ; 8,5 % ; apport porte marché n = 157 ; 6,8 canaux).
- **Tableau 2** (pénétration / réguliers / budget des 7 canaux principaux) — 21 valeurs.
- **Typologie** : inertie ACM (62 % sur 2 axes), silhouettes (0,24 / 0,21 / 0,23), **Tableau 5** (effectifs 624/249/79/47/26, parts, canaux, budgets, % VD inclusive et régulière) — 35 valeurs.
- **Régressions** : pseudo-R² 0,029 et 0,016 ; OR diplôme bac+3 1,89 (p 0,003) sur l'essai, 1,22 (p 0,45) sur l'adoption ; OR budget 1,17 ; OR cadres 1,64 (p 0,07).
- **Colinéarité** : V de Cramér diplôme × CSP 0,29 ; ρ diplôme × budget 0,06.
- **AMAP** (Q46) : base 509 ; 41 actuels + 75 cessé = 116 ; abandon 65 % ; ne connaît pas 46 %.
- **Récence** (Tableau 4) : bases et taux « récent » / « n'achète plus » des 9 formes.
- **Motivations** (Q21) : locaux 51 %, circuit court 41 %, goût 39 %, soutien 34 %, prix 18 %.

**Conclusion 1 : aucune valeur inventée ou dérivée d'une mémoire du modèle ; tout provient des données de l'enquête.**

---

## 2. Intégrité bibliographique (citations ↔ références)

Contrôle bidirectionnel automatisé + revue manuelle.

- **22 références** (norme *DM* : ≤ 35 ✔).
- **Aucune référence orpheline** (toute entrée est citée dans le corps) — après correction de **Chiffoleau et Dourian (2020)**, jusque-là listée mais non citée, désormais rattachée à l'argument « raccourcir la chaîne n'est pas en soi une réponse ».
- **Aucune citation sans entrée** — après reformulation de la note 1, où « FranceAgriMer » figurait comme source nommée sans référence datée ; renvoyée à Agreste (2023) et Enthoven et Van den Broeck (2021), toutes deux référencées.
- **Existence des sources** : les 22 références ont été vérifiées (Stade 2.5, recoupement Web) ; aucune référence fantôme. Les corrections factuelles antérieures (Agreste 2023 en remplacement de Kneafsey ; Enthoven et Van den Broeck 2021, *Agricultural Systems* 193:103226) sont maintenues.

**Conclusion 2 : appareil bibliographique clos et cohérent.**

---

## 3. Les 7 modes de défaillance de la recherche assistée par IA

| # | Mode de défaillance | Constat sur ce manuscrit | Statut |
|---|---------------------|--------------------------|:------:|
| 1 | **Fabrication / hallucination** (données ou citations inventées) | 124/124 chiffres tracés aux données ; 0 référence fantôme ; aucune donnée simulée. | ✅ PASS |
| 2 | **Sur-généralisation** au-delà des données | Bornes explicites : transversal (pas de causalité), déclaratif, terrain de septembre, C5 à n = 26, 65 % présenté comme borne haute, silhouette modérée assumée. | ✅ PASS |
| 3 | **Dérive de citation** (source ne soutenant pas la thèse) | Vérification par échantillon : Herzig et Zander (2025) → faible pouvoir explicatif du sociodémographique ✓ ; Feldmann et Hamm (2015) → freins d'inconvénience/disponibilité ✓ ; Mustapa et Kallas (2025) → méta-analyse WTP ✓ ; Verhoef (2015)/Neslin (2006) → omnicanal ✓. | ✅ PASS |
| 4 | **p-hacking / rapport sélectif** | Le pseudo-R² quasi nul est rapporté, non caché ; les effets non significatifs (sexe, âge, agglomération) sont donnés ; le résultat nul du diplôme sur l'adoption est **surfacé**. | ✅ PASS |
| 5 | **Biais de confirmation** (ignorer le contradictoire) | Le manuscrit intègre activement le contradictoire : diplôme ne prédit pas l'adoption ; abandon vrai modéré (≠ récit catastrophiste) ; distinction intermittence/abandon ; les 3 attaques de l'avocat du diable ont été traitées, non écartées. | ✅ PASS |
| 6 | **Échec de reproductibilité** | Pipeline complet et déterministe (`code/02`→`code/11`, `random_state=42`) ; script d'audit rejoue tous les chiffres ; données brutes locales et **gitignorées**, seuls les agrégats publiés (RGPD). | ✅ PASS |
| 7 | **Représentation trompeuse de l'incertitude** | IC de Wilson sur les taux clés ; réserves de faible effectif explicites (C5, AMAP n = 116) ; projections étiquetées « borne haute / illustratif » ; bases de comparaison différentes signalées (893 vs 509). | ✅ PASS |

**Conclusion 3 : les 7 modes sont franchis sans blocage.** Le manuscrit se distingue par une gestion active de ses propres faiblesses (modes 4 et 5), plutôt que par leur dissimulation.

---

## 4. Gouvernance des données (RGPD)

- Les données individuelles (`24407_Export.xlsx`, codebook) restent **locales et gitignorées** ; `git ls-files data/` ne renvoie **aucun** fichier de données (hors `.gitkeep`).
- Les livrables ne publient que des **agrégats** (parts, taux, effectifs de classe) ; aucune ligne individuelle n'est écrite dans les articles, figures ou scripts de sortie.
- Le script d'audit lui-même n'imprime que des agrégats.

**Conclusion 4 : gouvernance conforme.**

---

## Verdict

**INTÉGRITÉ FINALE : PASS.** Le manuscrit est autorisé à passer en finalisation (Stade 5).

Aucun blocage. Les deux seuls écarts détectés (une référence orpheline, une source nommée non référencée) étaient d'ordre bibliographique et ont été corrigés séance tenante ; ils ne touchaient aucun résultat. La traçabilité numérique est totale (124/124), l'incertitude est représentée honnêtement, et le manuscrit surfacte ses résultats défavorables au lieu de les taire.

**Manuscrit :** 7 932 mots (< 8 000 ✔) · 6 figures · 6 tableaux · 22 références.

---

*Rapport d'intégrité produit par le pipeline ARS — Stade 4.5. Contrôles reproductibles via `code/11_audit_integrite.py`. Étape suivante : Stade 5 (finalisation du paquet de soumission).*
