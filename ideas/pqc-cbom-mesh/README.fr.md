<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

[ 🇬🇧 English Version ](./README.md)

# PQC CBOM & Migration Mesh

> **Résumé exécutif :** Conception d'un agent de découverte bas niveau (eBPF, analyseurs de paquets profonds, scanners de binaires statiques/dynamiques) capable de générer automatiquement un CBOM standardisé en temps réel. Mise en place d'un "Cryptographic Mesh" (un plan de contrôle réseau) permettant l'agilité cryptographique : l'interception et le wrapping des appels cryptographiques legacy pour y injecter du chiffrement hybride (Classique + PQC) de façon transparente pour l'application d'origine.

![Type: Model](https://img.shields.io/badge/Model-B2B%20%2F%20M2M-blue)
![Target: 100k ARR](https://img.shields.io/badge/ARR_Target-100k%E2%82%AC-green)
![Score: Pending](https://img.shields.io/badge/Composite_Score-En_attente-yellow)

---

## 1. Aperçu visuel & Effet Wahou

```mermaid
graph TD
    %% Schéma comparatif Problème vs Solution ou Flux d'architecture
    Probleme["État Actuel"] --> Solution["État PQC CBOM & Migration Mesh"]
```

## 2. La thèse contrariante (Peter Thiel Style)

**La croyance populaire :** Les solutions généralistes IA peuvent résoudre ce problème.

**La vérité cachée :** Un LLM ou un SaaS standard ne peut pas analyser des binaires compilés legacy, inspecter le trafic TLS en temps réel à l'échelle d'un cluster Kubernetes, ou intercepter des appels kernel (via eBPF). Le problème nécessite de l'ingénierie système bas niveau, une intégration profonde dans l'infrastructure, et une conformité rigoureuse avec des algorithmes mathématiques complexes. Une feuille Excel de suivi est inutile face à des milliers de microservices changeant quotidiennement.

## 3. Le problème & La cible

**Modèle économique :** B2B / M2M

**Cible précise :** CISOs (Chief Information Security Officers), architectes de sécurité et responsables de la conformité dans les secteurs critiques (banque, défense, télécoms, santé). Ce sont eux qui détiennent les budgets de conformité et de cyber-résilience.

**La douleur urgente :** La menace "Harvest Now, Decrypt Later" (HNDL). Les ordinateurs quantiques menacent de casser les standards de chiffrement actuels (RSA, ECC). Les entreprises n'ont aucune visibilité exhaustive sur les algorithmes cryptographiques déployés dans leur immense infrastructure legacy. Ne pas cartographier (via un CBOM - Cryptography Bill of Materials) et ne pas migrer vers des algorithmes PQC (Post-Quantum Cryptography) d'ici l'arrivée des normes définitives du NIST expose à des vols massifs de données rétroactifs, et à de lourdes pénalités de non-conformité. L'urgence est d'auditer dynamiquement et de migrer sans casser les systèmes en production.

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

**Moat (Barrière à l'entrée) :** Les cycles de vente dans la défense et la banque sont extrêmement longs. La dépendance au rythme de standardisation (NIST, ANSSI) et l'adoption par les navigateurs/OS de base. Risque de dégradation des performances réseau ou de latence lors de l'utilisation d'algorithmes PQC plus lourds (clés plus grandes) ou de l'analyse en temps réel. Forte barrière à l'entrée nécessitant des talents rares en cryptographie et ingénierie système.

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
