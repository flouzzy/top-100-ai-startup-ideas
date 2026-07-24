<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

[ 🇬🇧 English Version ](./README.md)

# AgentSaga

> **Résumé exécutif :** AgentSaga est un orchestrateur d'exécution offrant des capacités de transactions distribuées et de rollback garanti (pattern Saga) pour les agents IA autonomes.

![Type: Model](https://img.shields.io/badge/Model-M2M_/_B2B-blue)
![Target: 100k ARR](https://img.shields.io/badge/ARR_Target-100k%E2%82%AC-green)
![Score: Pending](https://img.shields.io/badge/Composite_Score-Pending-yellow)

---

## 1. Aperçu visuel & Effet Wahou

```mermaid
graph TD
    %% Architecture Diagram
    A["Intention de l'Agent"] --> B["Orchestrateur AgentSaga"]
    B --> C{"Étape 1 : Réservation Vol"}
    C -->|Succès| D{"Étape 2 : Réservation Hôtel"}
    C -->|Échec| E["Annulation Workflow"]
    D -->|Succès| F{"Étape 3 : Location Voiture"}
    D -->|Échec| G["Déclenche Compensation : Annuler Vol"]
    F -->|Succès| H["Transaction Complète"]
    F -->|Échec| I["Déclenche Compensation : Annuler Hôtel & Vol"]
```

## 2. La thèse contrariante (Peter Thiel Style)

**La croyance populaire :** Le marché part du principe que les grands modèles de langage (LLM) peuvent s'auto-corriger et annuler proprement leurs erreurs si on leur fournit un contexte suffisant via un prompt.

**La vérité cachée :** Les LLM manquent de déterminisme et échouent souvent en plein processus. Une véritable intégrité transactionnelle pour les workflows agentiques nécessite un broker d'orchestration asynchrone qui impose des rollbacks déterministes, fonctionnant de manière totalement indépendante de l'état probabiliste du LLM.

## 3. Le problème & La cible

**Modèle économique :** M2M / B2B

**Cible précise :** Les équipes d'ingénierie, plateformes RPA et entreprises déployant des agents autonomes orchestrant des flux complexes multi-API (e.g., e-commerce, réservations de voyages, orchestration ERP).

**La douleur urgente :** Lorsqu'un agent autonome exécute une suite d'actions sur plusieurs systèmes externes (par exemple : réserver un vol, puis un hôtel, puis louer une voiture) et échoue sur la dernière étape, les actions précédemment validées restent actives. L'incapacité à annuler de manière sûre et prédictible les transactions partielles entraîne des pertes financières directes, des états incohérents dans le système d'information de l'entreprise et des réclamations clients massives.

## 4. Architecture technique & Plomberie

```mermaid
sequenceDiagram
    %% System Flow
    participant User
    participant Agent LLM
    participant Broker AgentSaga
    participant API 1
    participant API 2

    User->>Agent LLM: Exécuter tâche multi-étapes
    Agent LLM->>Broker AgentSaga: Initier Transaction Saga
    Broker AgentSaga->>API 1: Exécuter Étape 1
    API 1-->>Broker AgentSaga: Succès (État Sauvegardé)
    Broker AgentSaga->>API 2: Exécuter Étape 2
    API 2-->>Broker AgentSaga: Échec ! (e.g. Carte Refusée)
    Broker AgentSaga->>Broker AgentSaga: Intercepter Échec
    Broker AgentSaga->>API 1: Exécuter Compensation (Rollback) Étape 1
    API 1-->>Broker AgentSaga: Rollback Confirmé
    Broker AgentSaga-->>Agent LLM: Transaction Annulée & État Nettoyé
    Agent LLM-->>User: Échec de la tâche, toutes actions partielles annulées
```

## 5. Modèle économique & Viabilité financière

| Métrique                        | Valeur                                                            |
| ------------------------------- | ----------------------------------------------------------------- |
| **Structure de prix**           | Niveaux API basés sur l'usage / 500$ base mensuelle par locataire |
| **Objectif 12 mois**            | 200 clients entreprises ou intégrations plateformes               |
| **Calcul du CA (Target 100k€)** | 200 clients _ 500$/mois _ 12 mois                                 |
| **Marge brute estimée**         | 85%                                                               |

## 6. Moteur de distribution & Fossé défensif (Moat)

**Stratégie d'acquisition :** Adoption par les développeurs via des SDK et outils open-source, couplée à des ventes directes B2B aux grandes plateformes RPA et de création d'agents.

**Moat (Barrière à l'entrée) :** Un fournisseur pur LLM (OpenAI, Google) ne peut pas garantir nativement l'orchestration atomique de l'état à travers des systèmes externes disparates sans construire une couche d'orchestration dédiée avec gestion de l'état. Les concurrents ne peuvent pas répliquer cette fiabilité uniquement via de meilleurs prompts ou de plus grands modèles ; cela requiert une infrastructure architecturale fondamentalement différente (le broker Saga).

## 7. Grille d'évaluation détaillée

| Critère                               | Score VC (/100) | Score Terrain (/100) |
| ------------------------------------- | --------------- | -------------------- |
| **Thèse & Monopole / Urgence**        | -- / 25         | -- / 25              |
| **Moat / Résistance aux LLM natifs**  | -- / 25         | -- / 25              |
| **Scalabilité / Friction d'adoption** | -- / 25         | -- / 25              |
| **Unit Economics / ROI direct**       | -- / 25         | -- / 25              |
| **TOTAL**                             | -- / 100        | -- / 100             |

> **Verdict VC :** En attente d'évaluation.

> **Verdict Terrain :** En attente d'évaluation.
