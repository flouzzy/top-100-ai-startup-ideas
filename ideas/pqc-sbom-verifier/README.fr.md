<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
<!-- markdownlint-disable MD033 MD041 -->

[🇬🇧 English Version](./README.md)

# PQCBom

> **Résumé exécutif :** Post-Quantum Cryptography SBOM Verifier

![Type: B2B](https://img.shields.io/badge/Model-B2B-blue)
![Target: 100k ARR](https://img.shields.io/badge/ARR_Target-100k%E2%82%AC-green)
![Score: Pending](https://img.shields.io/badge/Composite_Score-En_attente-yellow)

---

## 1. Aperçu visuel & Effet Wahou

```mermaid
graph TD
    %% Schéma comparatif Problème vs Solution ou Flux d'architecture
    A[Problème] --> B[Solution]
```

## 2. La thèse contrariante (Peter Thiel Style)

- **La croyance populaire :** [Ce que la majorité pense sur ce marché]
- **La vérité cachée :** [La réalité non intuitive exploitée par cette startup]

## 3. Le problème & La cible

- **Modèle économique :** B2B
- **Cible précise :** RSSI (CISO), équipes DevSecOps d'infrastructures critiques (Banques, Défense, Santé) et éditeurs de logiciels.
- **La douleur urgente :** Avec l'arrivée imminente des ordinateurs quantiques, les algorithmes de chiffrement actuels (RSA, ECC) deviendront obsolètes ("Q-Day"). La transition vers la cryptographie post-quantique (PQC) est obligatoire. Cependant, les entreprises ne savent pas exactement où se cachent les vulnérabilités cryptographiques dans leur chaîne d'approvisionnement logicielle tentaculaire (dépendances open source, bibliothèques tierces), rendant la remédiation impossible.

## 4. Architecture technique & Plomberie

```mermaid
sequenceDiagram
    %% Schéma de séquence ou d'interaction entre l'utilisateur, l'IA et le système
    participant U as Utilisateur
    participant S as Système
    U->>S: Requête
    S-->>U: Réponse
```

## 5. Modèle économique & Viabilité financière

| Métrique                        | Valeur                                                          |
| ------------------------------- | --------------------------------------------------------------- |
| **Structure de prix**           | [Prix / Modèle d'abonnement / Commission]                       |
| **Objectif 12 mois**            | [Nombre exact de clients/utilisateurs/transactions nécessaires] |
| **Calcul du CA (Target 100k€)** | [Formule mathématique exacte]                                   |
| **Marge brute estimée**         | [Marge en %]                                                    |

## 6. Moteur de distribution & Fossé défensif (Moat)

- **Stratégie d'acquisition :** [Viralité B2C, réseau C2C, acquisition B2B directe, adhésion dev M2M]
- **Moat (Barrière à l'entrée) :** Les scanners SBOM traditionnels (Trivy, Snyk) détectent les CVE connues ou les noms de packages. Ils ne comprennent pas l'implémentation cryptographique bas niveau (ex: si une lib custom implémente secrètement du RSA-1024 en dur). Cela requiert de l'analyse sémantique de code, de la décompilation de binaires et une compréhension de la taxonomie cryptographique.

## 7. Grille d'évaluation détaillée

| Critère                               | Score VC (/100) | Score Terrain (/100) |
| ------------------------------------- | --------------- | -------------------- |
| **Thèse & Monopole / Urgence**        | -- / 25         | -- / 25              |
| **Moat / Résistance aux LLM natifs**  | -- / 25         | -- / 25              |
| **Scalabilité / Friction d'adoption** | -- / 25         | -- / 25              |
| **Unit Economics / ROI direct**       | -- / 25         | -- / 25              |
| **TOTAL**                             | **-- / 100**    | **-- / 100**         |

> **Verdict VC :** En attente d'évaluation.
>
> **Verdict Terrain :** En attente d'évaluation.
