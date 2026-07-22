<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->

# Candidat : Agent Firewall

* **Modèle économique :** M2M / B2B
* **Cible :** Entreprises déployant des agents IA autonomes (Customer Success, DevTools, RPA) interagissant avec leurs bases de données ou API internes.
* **Le problème urgent :** Les agents IA sont vulnérables aux injections de prompt et aux hallucinations. Laisser un agent exécuter des requêtes API sans filet de sécurité externe risque de provoquer des fuites de données (PII), des suppressions accidentelles de bases de données, ou la consommation incontrôlée de ressources coûtant des millions.
* **L'approche technique :** Un pare-feu API (reverse proxy) agnostique au LLM qui intercepte les "Function Calls" et appels réseau des agents IA. Il valide chaque requête contre des politiques RBAC (Role-Based Access Control) déterministes, bloque les requêtes anormales, et déclenche des circuits d'approbation "Human-in-the-Loop" pour les actions destructrices avant d'autoriser l'exécution vers le système final.
* **Pourquoi ChatGPT/Gemini échoue seul :** Un LLM ne peut pas sécuriser ses propres actions de manière fiable de façon probabiliste. Les directives système du type "ne supprime jamais de données" peuvent être contournées. Une infrastructure de validation déterministe externe est indispensable.
