<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->

# Candidat : Agent Circuit Breaker

* **Modèle économique :** M2M
* **Cible :** Les entreprises déployant des essaims d'agents autonomes, les fournisseurs de plateformes Agentic et les équipes FinOps/DevOps.
* **Le problème urgent :** Les agents autonomes peuvent facilement entrer dans des boucles infinies de raisonnement ou de communication (l'agent A demande à l'agent B qui redemande à l'agent A), générant des appels API en cascade qui brûlent les budgets (token burn) et risquent de saturer les infrastructures internes (DDoS accidentel).
* **L'approche technique :** Un "coupe-circuit" (circuit breaker) au niveau de la couche réseau/API qui analyse les graphes d'appels inter-agents en temps réel. Il détecte les modèles cycliques, les pics anormaux de fréquence ou l'escalade des coûts, puis met en pause de manière préventive les instances d'agents défectueux.
* **Pourquoi ChatGPT/Gemini échoue seul :** Un LLM n'a pas conscience de la topologie globale du réseau ni de sa consommation financière globale en temps réel. Une boucle infinie est un problème d'orchestration distribuée qui nécessite une supervision externe de l'état du système, impossible à résoudre par un simple ajustement de prompt.
