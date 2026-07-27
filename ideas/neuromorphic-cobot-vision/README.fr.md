<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

[ 🇬🇧 English Version ](./README.md)

# SpikingSight Robotics

> **Résumé exécutif :** L'intégration de capteurs de vision événementielle (Event-based cameras / Neuromorphic sensors) où chaque pixel est indépendant et ne signale qu'un changement de luminosité (micros-secondes). Couplé avec des Spiking Neural Networks (SNNs) asynchrones exécutés sur des puces neuromorphiques (ex: Akida, Loihi) pour traiter le flux de données clairsemé avec une consommation d'énergie de l'ordre du milliwatt et une latence quasi-nulle.

![Type: Model](https://img.shields.io/badge/Model-B2B%20%28Vente%20de%20hardware%2Fmodules%20%2B%20licence%20logicielle%29-blue)
![Target: 100k ARR](https://img.shields.io/badge/ARR_Target-100k%E2%82%AC-green)
![Score: Pending](https://img.shields.io/badge/Composite_Score-En_attente-yellow)

---

## 1. Aperçu visuel & Effet Wahou

```mermaid
graph TD
    %% Schéma comparatif Problème vs Solution ou Flux d'architecture
    Probleme["État Actuel"] --> Solution["État SpikingSight Robotics"]
```

## 2. La thèse contrariante (Peter Thiel Style)

**La croyance populaire :** Les solutions généralistes IA peuvent résoudre ce problème.

**La vérité cachée :** Les frameworks IA actuels (PyTorch, TensorFlow) sont conçus pour des tenseurs denses et synchrones sur GPU. Le SaaS cloud ajoute de la latence réseau interdisant tout asservissement réactif d'un bras robotique. L'innovation requiert une refonte complète de la pile logicielle (vers l'asynchrone par événements) au plus près du capteur.

## 3. Le problème & La cible

**Modèle économique :** B2B (Vente de hardware/modules + licence logicielle)

**Cible précise :** Fabricants de robots collaboratifs (cobots), drones industriels autonomes, logistique d'entrepôt ultra-rapide.

**La douleur urgente :** Les systèmes de vision par ordinateur basés sur des caméras standards (RGB) génèrent 30 à 60 images complètes par seconde, saturant la bande passante et la puissance de calcul embarquée. Pour des robots évoluant très rapidement dans des environnements dynamiques, cela induit une latence fatale (motion blur, délais de réaction) et vide les batteries à cause du traitement GPU lourd.

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

**Moat (Barrière à l'entrée) :** Les SNNs sont notoirement difficiles à entraîner (la rétropropagation classique de gradient ne fonctionne pas directement sur les "spikes" discrets). Écosystème matériel neuromorphique encore jeune et coûteux.

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
