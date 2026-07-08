# Cahier de laboratoire — [Nom du projet]
> Dernière mise à jour : 2026-07-08

## Synthèse de la recherche en cours
*(Résumé de 3-5 phrases de ce qu'on cherche à comprendre ou produire)*

Le projet n'est pas encore défini. Le système Academic Research Skills v3.13.0
a été installé et configuré pour Catherine Hérault. Les préférences sont :
communication en français, articles en français, format de sortie Word/DOCX.

## Directions explorées
| Date       | Direction                                  | Statut   | Observations                              |
|------------|--------------------------------------------|----------|-------------------------------------------|
| 2026-06-29 | Installation et configuration ARS v3.13.0  | Terminé  | 617 fichiers installés dans .claude/      |
| 2026-06-29 | Test fonctionnel : plan d'article fictif   | Terminé  | Plan 3 chapitres sur IA générative & évaluation supérieure |
| 2026-06-29 | Démarrage projet : vente directe alimentaire | En cours | RQ recadrée sur « place dans stratégies d'approvisionnement », 5 canaux, France métropolitaine |
| 2026-06-29 | Stade 1 RECHERCHE (pipeline ARS)           | Terminé  | RQ Brief + biblio 18 réfs + synthèse 5 thèmes + méthode IMRaD simulé |
| 2026-06-29 | Réception données réelles (enquête 24407)  | Terminé  | Étude devient empirique réelle (plus simulée). 1025 répondants représentatifs. |
| 2026-06-29 | Stade 2A AUDIT des données                 | Terminé  | N=1025, 0% manquant clés, Q9 somme=100%. Vente directe : 49,7% pénétration, 1,5% budget |
| 2026-06-29 | Stade 2B ALIGNEMENT RQ↔variables           | Terminé  | 4/5 sous-questions mesurables ; SQ5 (temporel) → discussion |
| 2026-06-29 | Définition VD verrouillée                  | Terminé  | VD = canal 7 ∪ (Q22=1, marché direct producteur) = 666 (65%) |
| 2026-06-29 | Stade 2C ANALYSES A1-A6                     | Terminé  | Descriptif + typologie ACM/CAH (5 classes) + régression + motivations ; 5 figures |
| 2026-06-29 | Choix typologie 4 vs 5 classes             | Terminé  | 5 classes retenues (silhouette 0,237 ; classes distinctes par régularité) |
| 2026-06-29 | Stade 2 RÉDACTION draft IMRaD              | Terminé  | article_vente_directe.md, ~4550 mots, focus stratégies + transversalité sociale |
| 2026-06-29 | Vérif + correction des références           | Terminé  | 3 corrections factuelles (année/revue/réf fantôme) via WebSearch |
| 2026-06-29 | Export Word (.docx)                         | Terminé  | pandoc + citeproc ; outputs/word/article_vente_directe.docx |
| 2026-06-29 | Actualisation revue de littérature (retour utilisateur) | Terminé | +2 réfs récentes vérifiées : Chiffoleau & Dourian 2020, Herzig & Zander 2025 |
| 2026-06-29 | Correction typologie (retour utilisateur)  | Terminé  | Ajout colonne « VD régulière » ; multi-canal conv. = 100% VD inclusif mais 19% régulier (essai large ≠ engagement) ; classes renumérotées ; libellé « évitent » corrigé |
| 2026-07-07 | Diaporama copil (PPTX)                     | Terminé  | 10 diapos, 2 figures, 3 leviers d'action ; outputs/presentations/ |
| 2026-07-07 | Expansion revue de littérature (retour utilisateur) | Terminé | §2 réécrit en 4 sous-sections + tableau de positionnement ; +9 réfs vérifiées (omnicanal, conso durable, segmentation) ; H3 ajoutée ; article 5120→6310 mots |
| 2026-07-07 | Clarification métrique budget (1,5% vs 8,5%) | Terminé | Deux échelles présentées ; note de méthode §3.2 |
| 2026-07-07 | Ciblage revue : Décisions Marketing         | En cours | Instructions + article exemple analysés ; manuscrit reformaté au format DM |
| 2026-07-07 | Manuscrit format DM produit                 | Terminé  | Titre accroche, résumé 6 points + abstract EN, 3 encadrés, section implications managériales, réfs style RAM, figures N&B, page de titre séparée (anonymat) |
| 2026-07-07 | Ré-enrichissement manuscrit DM              | Terminé  | Restauration substance (cadre + positionnement, managérial, profils classes) : 4136→5618 mots |
| 2026-07-07 | Analyse « essai vs ancrage » (retour utilisateur) | Terminé | Récence d'achat par forme (Q22/30/38/46/53/61/70) : 54% des déclarants VD ont acheté le mois écoulé ; abandon jusqu'à 65% (AMAP). Nouvelle sous-section + Tableau 3 + Figure 3 ; 6231 mots |
| 2026-07-08 | Révisions auteur round 2 (7 points) | Terminé | Cadre déclaratif (WTP Mustapa), Tableau 3 clarifié + note + comparateurs conventionnels, titre « adoptent », 5 stratégies nommées + n canaux, diplôme ajouté (Q240) aux croisements et à la régression (OR bac+3 = 1,89) ; manuscrit ~6744 mots |
| 2026-07-08 | Stade 3 REVUE PAR LES PAIRS simulée | Terminé | Panel 5 relecteurs DM (RC, méthodo, domaine, managérial, avocat du diable). Décision : **Révision majeure**. Point bas = rigueur méthodo 5,5/10. 6 exigences bloquantes (diagnostics typologie, n+IC, sensibilité définition/dénominateur, diplôme sur VD régulière, intermittence vs abandon, n AMAP) + 3 non bloquantes. reviews/revue_par_les_pairs_DM.md (+.docx) |

## Hypothèses
| # | Hypothèse | Confirmée / Infirmée / En cours | Source |
|---|-----------|----------------------------------|--------|
| H1 | La vente directe occupe rarement la place de canal principal ; elle s'inscrit dans des stratégies de complémentarité ciblée | **Confirmée** — VD 65% pénétration mais 1,5% budget (canal 7) vs hyper 58% | articles/stade2_resultats.md |
| H2 | L'usage de la vente directe est faiblement déterminé par le profil socio-démo (transversalité sociale) | **Soutenue** — pseudo-R²=0,022 ; seuls cadres/prof.lib (OR 2,16) et budget (OR 1,18) significatifs | A5, articles/stade2_resultats.md |
| H3 | L'adhésion déclarée à la VD dépasse largement son poids budgétaire réel (attitude-behaviour gap) | **Confirmée** — 65% de pratiquants mais ~1,5% du budget ; contraste avec +34,5% de consentement à payer (Mustapa & Kallas 2025) | §2.5, §4.2, §5.1 |

## Choix effectués
| Date       | Décision                       | Justification                          | Alternatives écartées          |
|------------|--------------------------------|----------------------------------------|--------------------------------|
| 2026-06-29 | Format de sortie : Word/DOCX   | Collaboration et annotation faciles    | LaTeX (Overleaf), Les deux     |
| 2026-06-29 | Langue de communication : FR   | Préférence utilisateur                 | English                        |
| 2026-06-29 | Langue d'article : FR          | Préférence utilisateur                 | English, Bilingual             |
| 2026-06-29 | Angle marketing/économie       | Choix utilisateur                      | Sociologie, santé publique, pluridisciplinaire |
| 2026-06-29 | Type d'article : IMRaD simulé  | Choix utilisateur ; étiquetage strict des données | Revue littérature, théorique |
| 2026-06-29 | Périmètre : France métropolitaine | Litt. plus riche, cadre homogène     | Europe, international          |
| 2026-06-29 | RQ recadrée sur stratégies d'approvisionnement | Apport plus original que « motivations » | Motivations, segmentation, valeur perçue |

## Notes libres
*(Observations, intuitions, questions ouvertes)*

- Le cahier de laboratoire est mis à jour automatiquement après chaque
  échange substantiel. Aucune action manuelle n'est requise.
- Pour démarrer un projet, demander à Claude : « Je veux écrire un article
  sur [sujet] » ou utiliser `/ars-plan`.
