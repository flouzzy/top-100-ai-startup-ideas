<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->
# Candidat : TokenGC (Context Garbage Collector)

* **Modèle économique :** M2M / B2B
* **Cible :** Entreprises développant des agents autonomes ou des systèmes multi-agents (DevTools, RPA IA, Customer Support automatisé) qui interagissent de manière continue.
* **Le problème urgent :** Les agents autonomes en boucle infinie (ou sur des tâches longues) accumulent un contexte massif. À chaque appel API, l'historique complet est renvoyé, ce qui fait exploser les coûts (facturation au token entrant), provoque des hallucinations (dilution de l'attention) et augmente considérablement la latence. Les développeurs gaspillent des ressources API pour des données de contexte "mortes" ou obsolètes.
* **L'approche technique :** Un proxy middleware entre l'agent et le fournisseur de LLM qui analyse le flux de contexte en temps réel. Il agit comme un "Garbage Collector" : il identifie les états résolus, compresse les historiques de conversation en graphes de connaissances (ou vecteurs denses), et purge les "tokens morts" (réflexions inutiles, logs intermédiaires) avant de transmettre la requête au LLM.
* **Pourquoi ChatGPT/Gemini échoue seul :** Les LLMs sont stateless. Ils n'ont pas la capacité de modifier ou d'optimiser le payload réseau qui leur est envoyé avant qu'il ne leur coûte du calcul. Demander à Gemini de "résumer la conversation" consomme précisément les tokens qu'on cherche à économiser, et ne gère pas l'optimisation au niveau de l'infrastructure réseau/API.
