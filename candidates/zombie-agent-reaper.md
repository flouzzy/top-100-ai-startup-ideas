<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->

# Candidat : ZombieAgent Reaper

* **Modèle économique :** B2B
* **Cible :** Équipes FinOps, CloudOps et DevOps dans les entreprises déployant des agents autonomes.
* **Le problème urgent :** Les développeurs déploient des agents autonomes, mais oublient souvent de les désactiver. Ces "agents zombies" continuent de tourner en boucle, d'interroger des API payantes et de consommer des tokens LLM très coûteux (factures astronomiques inutiles et risques de sécurité).
* **L'approche technique :** Un Control Plane qui s'intègre aux environnements cloud et aux plateformes de déploiement d'agents. Il analyse le trafic réseau et les appels API (via un proxy réseau ou eBPF) pour identifier les comportements d'agents inactifs ou redondants, et suspend automatiquement leurs processus selon des règles de TTL et de budget.
* **Pourquoi ChatGPT/Gemini échoue seul :** Un LLM n'a aucune visibilité sur l'infrastructure cloud ou l'orchestration des processus. Il ne peut pas surveiller l'activité réseau en arrière-plan ni intervenir au niveau système pour suspendre une tâche zombie.
