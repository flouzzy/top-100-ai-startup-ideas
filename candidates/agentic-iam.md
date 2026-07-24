<!-- markdownlint-disable MD013 -->

# Candidat : AgentGuard (IAM pour Agents Autonomes)

- **Modèle économique :** M2M / B2B
- **Cible :** Les entreprises, DSI, et développeurs déployant des flottes d'agents IA autonomes ayant accès à des outils internes (AWS, Salesforce, GitHub, bases de données).
- **Le problème urgent :** Les agents IA se voient actuellement confier des clés d'API statiques avec des privilèges excessifs ("God mode") pour accomplir leurs tâches. En cas d'hallucination, de prompt injection, ou de détournement, un agent peut causer des dégâts irréversibles (effacement de bases de données, fuite de données confidentielles). Il manque cruellement d'un système de gestion des accès à granularité fine et dynamique pour les identités non-humaines.
- **L'approche technique :** Un système d'Identity and Access Management (IAM) dédié aux agents. Une API Gateway (Proxy) qui intercepte les appels outils/API des agents. Au lieu de clés statiques, le système délivre des tokens éphémères (Just-in-Time access) basés sur le contexte de la tâche. Intégration de politiques "Zero Trust", validation déterministe des paramètres de requêtes, et kill switch automatique en cas de déviation comportementale de l'agent.
- **Pourquoi ChatGPT/Gemini échoue seul :** Un LLM ne peut pas sécuriser sa propre exécution. Un prompt défensif du type "N'utilise tes droits que pour lire les données" peut être contourné par une simple attaque de prompt injection. La sécurité doit être assurée par une couche réseau déterministe et externe, imperméable aux manipulations du modèle, garantissant cryptographiquement les frontières d'action de l'agent.
