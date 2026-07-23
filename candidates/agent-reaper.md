<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->
# Candidat : Agent Reaper

* **Modèle économique :** B2B / M2M
* **Cible :** Équipes FinOps, DevOps et ingénieurs IA gérant des flottes d'agents autonomes en production.
* **Le problème urgent :** Les agents autonomes peuvent entrer dans des boucles infinies, des hallucinations récursives ou des tâches "zombies" (ghost tasks) où ils continuent de s'interroger mutuellement ou d'appeler des API externes sans fin. Cela entraîne une surconsommation massive de crédits d'API (token burn), l'épuisement des quotas de requêtes (rate limits) et des factures cloud/API explosives et inattendues.
* **L'approche technique :** Un "Circuit Breaker" (disjoncteur) et "Garbage Collector" au niveau réseau dédié aux agents IA. Le système surveille les modèles d'appels API, la vélocité de consommation des tokens et la répétition sémantique des requêtes M2M. Dès qu'un schéma de boucle infinie ou de processus zombie est détecté, le système coupe l'accès réseau de l'agent fautif et déclenche une alerte.
* **Pourquoi ChatGPT/Gemini échoue seul :** Un LLM ne peut pas monitorer sa propre consommation d'API ni détecter qu'il est coincé dans une boucle infinie au niveau de l'infrastructure. Il n'a pas conscience de la facturation cloud en temps réel. Une couche d'infrastructure réseau déterministe est indispensable pour agir comme un "kill switch" financier et opérationnel.
