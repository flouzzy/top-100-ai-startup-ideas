<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->

# Candidat : Smart Grid Quantum Optimizer

- **Domaine principal :** Quantique / ClimateTech
- **Modèle économique :** B2B
- **Cible :** Gestionnaires de réseau de transport (RTE, National Grid), producteurs d'énergie renouvelable.
- **Le problème urgent :** L'intégration massive d'énergies renouvelables intermittentes (éolien, solaire) et de véhicules électriques déstabilise les réseaux électriques (problème d'inertie). L'optimisation du dispatching en temps réel est un problème mathématique NP-difficile (Unit Commitment Problem) que les supercalculateurs classiques mettent trop de temps à résoudre, entraînant des pertes massives et des risques de blackout.
- **L'approche technique :** Un solveur hybride (Quantum-Inspired / Annealing) qui modélise le réseau électrique comme un graphe complexe. Il utilise des algorithmes quantiques variationnels (VQA) pour trouver l'optimum global de distribution d'énergie et de tarification dynamique en quelques secondes au lieu de plusieurs heures.
- **Pourquoi une solution générique/SaaS classique échoue :** Les algorithmes heuristiques actuels (Mixed-Integer Linear Programming) atteignent leurs limites avec la décentralisation exponentielle des nœuds du réseau. Le cloud classique scale mal sur ces problèmes d'optimisation combinatoire pure.
- **Risques majeurs & Dépendances :** La viabilité à court terme dépend de la maturité du Quantum Annealing (ex: D-Wave) ou des algorithmes quantiques inspirés tournant sur des GPU classiques (Tensor Networks) en attendant l'avantage quantique prouvé.
