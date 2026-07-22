<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->

[ 🇬🇧 English Version ](./README.md)

# Agent Firewall

> **Résumé exécutif :** Un pare-feu API agnostique au LLM qui intercepte et valide les "Function Calls" des agents IA contre des politiques déterministes.

![Type: Model](https://img.shields.io/badge/Model-M2M%20%2F%20B2B-blue)
![Target: 100k ARR](https://img.shields.io/badge/ARR_Target-100k%E2%82%AC-green)
![Score: Pending](https://img.shields.io/badge/Composite_Score-Pending-yellow)

---

## 1. Aperçu visuel

```mermaid
graph TD
    %% Flux d'architecture
    A["Agent IA"] -->|Requête API / Function Call| B["Agent Firewall (Reverse Proxy)"]
    B -->|Validation RBAC| C{"Politique Valide ?"}
    C -->|Oui| D["Exécution Système Cible"]
    C -->|Non / Destructeur| E["Validation Humaine (Human-in-the-Loop)"]
    E -->|Approuvé| D
    E -->|Rejeté| F["Blocage Requête"]
```

## 2. La thèse contrariante (Peter Thiel Style)

La croyance populaire : L'amélioration des directives système (prompts) suffit à sécuriser les actions d'un agent IA.
La vérité cachée : Un LLM est un système probabiliste et ne peut sécuriser ses actions de manière fiable. Une infrastructure de validation déterministe externe est indispensable.

## 3. Le problème & La cible

Modèle économique : M2M / B2B
Cible précise : Entreprises déployant des agents IA autonomes (Customer Success, DevTools, RPA) interagissant avec leurs bases de données ou API internes.
La douleur urgente : Vulnérabilité aux injections de prompt et hallucinations entraînant des fuites de données (PII), suppressions accidentelles, ou consommation de ressources incontrôlée.

## 4. Architecture technique & Plomberie

```mermaid
sequenceDiagram
    %% Schéma de séquence
    participant Agent as Agent IA
    participant Firewall as Pare-feu
    participant System as Système Cible
    participant Human as Humain

    Agent->>Firewall: Demande d'action
    Firewall->>Firewall: Validation déterministe RBAC
    alt Action Risquée
        Firewall->>Human: Demande d'approbation
        Human-->>Firewall: Approuvé
    end
    Firewall->>System: Exécution
    System-->>Firewall: Réponse
    Firewall-->>Agent: Résultat
```

## 5. Modèle économique & Viabilité financière

| Métrique                    | Valeur                                     |
| --------------------------- | ------------------------------------------ |
| Structure de prix           | Abonnement B2B basé sur le volume de proxy |
| Objectif 12 mois            | 100 clients entreprise                     |
| Calcul du CA (Target 100k€) | Clients \* Abonnement                      |
| Marge brute estimée         | 80-90%                                     |

## 6. Moteur de distribution & Fossé défensif (Moat)

Stratégie d'acquisition : Acquisition B2B directe (SecOps, DevOps), intégration développeur.
Moat (Barrière à l'entrée) : Couche de validation externe et déterministe qui ne peut pas être remplacée nativement par une simple mise à jour d'OpenAI ou Google.

## 7. Grille d'évaluation détaillée

| Critère                           | Score VC (/100) | Score Terrain (/100) |
| --------------------------------- | --------------- | -------------------- |
| Thèse & Monopole / Urgence        | 22 / 25         | -- / 25              |
| Moat / Résistance aux LLM natifs  | 24 / 25         | -- / 25              |
| Scalabilité / Friction d'adoption | 21 / 25         | -- / 25              |
| Unit Economics / ROI direct       | 23 / 25         | -- / 25              |
| **TOTAL**                         | **90 / 100**    | **-- / 100**         |

> **Verdict VC :** Agent Firewall établit un point de contrôle critique pour les interactions M2M, créant des coûts de changement élevés. Son approche déterministe résout une douleur aiguë des entreprises que l'amélioration des LLM ne peut résoudre seule. D'excellents 'unit economics' grâce au modèle basé sur le volume de proxy.

> **Verdict Terrain :** En attente d'évaluation.
