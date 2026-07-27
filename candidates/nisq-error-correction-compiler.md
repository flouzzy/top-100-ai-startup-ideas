<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : NISQ Error Correction Compiler

- **Domaine principal :** Quantique
- **Modèle économique :** B2B
- **Cible :** Laboratoires de recherche quantique (IBM, Google, universités), entreprises du domaine de la chimie des matériaux et de la pharmacie explorant des algorithmes quantiques.
- **Le problème urgent :** Les ordinateurs quantiques actuels (NISQ - Noisy Intermediate-Scale Quantum) sont limités par le taux d'erreur de leurs qubits (bruit thermique, diaphonie). Exécuter un algorithme un peu profond entraîne une décohérence totale avant la fin du calcul, rendant les résultats inexploitables pour des cas d'usage industriels (comme la simulation moléculaire).
- **L'approche technique :** Un compilateur d'algorithmes quantiques basé sur le Machine Learning qui optimise dynamiquement le placement et le routage des portes quantiques en fonction de la topologie matérielle spécifique et du profil de bruit en temps réel de chaque qubit (caractérisation dynamique). Il injecte automatiquement des séquences de découplage dynamique et de mitigation d'erreur (ZNE - Zero Noise Extrapolation) au niveau impulsionnel (pulse-level).
- **Pourquoi une solution générique/SaaS classique échoue :** L'optimisation au niveau des portes logiques (Qiskit, Cirq) est insuffisante. Il faut descendre au niveau de la physique du contrôle micro-onde (pulse) et utiliser des modèles probabilistes pour prédire les erreurs de diaphonie (crosstalk) spécifiques au hardware ciblé, ce qui requiert un couplage profond avec l'API bas niveau de la machine quantique.
- **Risques majeurs & Dépendances :** Le matériel quantique évolue vite. Si l'informatique quantique à correction d'erreur (Fault Tolerant Quantum Computing) arrive plus tôt que prévu, l'utilité des solutions de mitigation NISQ s'effondrera. Dépendance totale à l'accès API très bas niveau accordé par les fabricants de hardware quantique.
