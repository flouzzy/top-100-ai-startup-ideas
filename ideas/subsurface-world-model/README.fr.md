<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

[ 🇬🇧 English Version ](./README.md)

# Lithos Twin

> **Résumé exécutif :** Un "World Model" du sous-sol intégrant de multiples modalités (sismique, gravimétrique, électromagnétique, données de forages passés) pour générer un jumeau numérique probabiliste et continu de la croûte terrestre. Utilisation de modèles de diffusion conditionnels pour générer des millions de scénarios géologiques plausibles et réduire l'incertitude avant tout forage.

![Type: Model](https://img.shields.io/badge/Model-B2B-blue)
![Target: 100k ARR](https://img.shields.io/badge/ARR_Target-100k%E2%82%AC-green)
![Score: Pending](https://img.shields.io/badge/Composite_Score-En_attente-yellow)

---

## 1. Aperçu visuel & Effet Wahou

```mermaid
graph TD
    %% Schéma comparatif Problème vs Solution ou Flux d'architecture
    Probleme["État Actuel"] --> Solution["État Lithos Twin"]
```

## 2. La thèse contrariante (Peter Thiel Style)

**La croyance populaire :** Les solutions généralistes IA peuvent résoudre ce problème.

**La vérité cachée :** Il s'agit d'un problème d'inversion géophysique massivement sous-contraint (trouver la structure 3D à partir de signaux de surface limités). Un outil data standard ne gère pas les tenseurs 3D voxélisés à l'échelle kilométrique, ni la physique de propagation des ondes (équation des ondes).

## 3. Le problème & La cible

**Modèle économique :** B2B

**Cible précise :** Entreprises de géothermie, miniers de transition énergétique (Lithium, Cuivre), opérateurs de stockage géologique de carbone (CCS).

**La douleur urgente :** L'exploration du sous-sol profond est aveugle, lente et coûteuse (forages exploratoires à plusieurs millions). Les modèles géologiques 3D actuels sont statiques, déconnectés de la réalité en temps réel, et la sismique 3D requiert des mois de traitement de signal lourd. L'incertitude bloque le financement de projets géothermiques et de séquestration carbone.

## 4. Architecture technique & Plomberie

```mermaid
sequenceDiagram
    %% Schéma de séquence ou d'interaction entre l'utilisateur, l'IA et le système
    Utilisateur->>Systeme: Action
    Systeme-->>Utilisateur: Reponse
```

## 5. Modèle économique & Viabilité financière

| Métrique                    | Valeur                        |
| --------------------------- | ----------------------------- |
| Structure de prix           | Abonnement SaaS               |
| Objectif 12 mois            | 10 clients                    |
| Calcul du CA (Target 100k€) | 10 clients \* 10k€/an = 100k€ |
| Marge brute estimée         | 80%                           |

## 6. Moteur de distribution & Fossé défensif (Moat)

**Stratégie d'acquisition :** Vente directe B2B

**Moat (Barrière à l'entrée) :** La rareté et la fragmentation des données géologiques (souvent jalousement gardées par les majors pétrolières). La validation sur le terrain est lente (un forage prend des mois).

## 7. Grille d'évaluation détaillée

| Critère                           | Score VC (/100) | Score Terrain (/100) |
| --------------------------------- | --------------- | -------------------- |
| Thèse & Monopole / Urgence        | -- / 25         | -- / 25              |
| Moat / Résistance aux LLM natifs  | -- / 25         | -- / 25              |
| Scalabilité / Friction d'adoption | -- / 25         | -- / 25              |
| Unit Economics / ROI direct       | -- / 25         | -- / 25              |
| **TOTAL**                         | **-- / 100**    | **-- / 100**         |

> **Verdict VC :** En attente d'évaluation.

> **Verdict Terrain :** En attente d'évaluation.
