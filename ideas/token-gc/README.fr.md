<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

[ 🇬🇧 English Version ](./README.md)

# TokenGC (Context Garbage Collector)

> **Résumé exécutif :** Un middleware agissant comme un garbage collector pour compresser les historiques de conversation en graphes de connaissances et purger les tokens morts, réduisant les coûts d'API.

![Type: Model](https://img.shields.io/badge/Model-M2M%2FB2B-blue)
![Target: 100k ARR](https://img.shields.io/badge/ARR_Target-100k%E2%82%AC-green)
![Score: Pending](https://img.shields.io/badge/Composite_Score-Pending-yellow)

---

## 1. Aperçu visuel

```mermaid
graph TD
    %% Architecture
    A["Agent IA"] -->|Contexte Lourd| B{"Proxy TokenGC"}
    B -->|Compression en Graphe| C["Moteur de Purge"]
    C -->|Prompt Allégé| D["API LLM"]
```

## 2. La thèse contrariante (Peter Thiel Style)

**La croyance populaire :** Il suffit de demander au LLM de résumer son propre contexte pour économiser des tokens.

**La vérité cachée :** Demander un résumé au LLM consomme précisément les tokens qu'on cherche à économiser ; l'optimisation doit se faire au niveau réseau avant l'inférence.

## 3. Le problème & La cible

**Modèle économique :** M2M / B2B
**Cible précise :** Entreprises développant des agents autonomes ou systèmes multi-agents interagissant en continu.
**La douleur urgente :** Les agents accumulent un contexte massif, faisant exploser les coûts (facturation au token) et augmentant la latence à chaque appel.

## 4. Architecture technique & Plomberie

**L'approche technique :** Proxy middleware agissant comme Garbage Collector. Identifie les états résolus, compresse l'historique et purge les tokens morts avant transmission au LLM.

```mermaid
sequenceDiagram
    participant Ag as "Agent"
    participant GC as "TokenGC"
    participant API as "LLM API"
    Ag->>GC: Request with 10k tokens (Logs + History)
    GC->>GC: Identify Dead Tokens & Summarize
    GC->>API: Request with 500 tokens
    API-->>GC: Standard Response
    GC-->>Ag: Response (Saved $0.05)
```

## 5. Modèle économique & Viabilité financière

| Métrique                        | Valeur                                         |
| :------------------------------ | :--------------------------------------------- |
| **Structure de prix**           | Percentage of tokens saved or Flat Volume Tier |
| **Objectif 12 mois**            | 200 Dev Teams                                  |
| **Calcul du CA (Target 100k€)** | 200 teams \* $500/mo = $100k/mo                |
| **Marge brute estimée**         | 90%                                            |

## 6. Moteur de distribution & Fossé défensif (Moat)

**Stratégie d'acquisition :** Intégration comme plugin middleware dans les frameworks (LangChain, LlamaIndex).

**Moat (Barrière à l'entrée) :** Les LLMs sont stateless. L'optimisation doit se faire au niveau de l'infrastructure réseau/API avant l'appel coûteux, pas par un prompt.

## 7. Grille d'évaluation détaillée

| Critère                               | Score VC (/100) | Score Terrain (/100) |
| :------------------------------------ | :-------------- | :------------------- |
| **Thèse & Monopole / Urgence**        | 20 / 25         | 20 / 25              |
| **Moat / Résistance aux LLM natifs**  | 22 / 25         | 19 / 25              |
| **Scalabilité / Friction d'adoption** | 25 / 25         | 21 / 25              |
| **Unit Economics / ROI direct**       | 24 / 25         | 18 / 25              |
| **TOTAL**                             | 91 / 100        | 78 / 100             |

> **Verdict VC :** Token GC s'attaque au tueur silencieux de la rentabilité de l'IA : la surconsommation de tokens par des agents inefficaces. En offrant un ramasse-miettes pour l'usage API, il garantit un ROI financier immédiat aux développeurs, consolidant sa place dans la stack IA moderne. Le modèle d'adoption sans friction et la tarification à l'usage conduisent à une scalabilité spectaculaire.
> **Verdict Terrain :** Cette solution répond à un besoin critique pour le marché cible, justifiant son excellent score d'urgence (20/25). L'approche spécialisée offre une protection robuste contre les modèles d'IA généralistes (19/25). Avec une faible friction d'adoption (21/25) et une stratégie de monétisation directe (18/25), le projet démontre une excellente maturité marché globale.
