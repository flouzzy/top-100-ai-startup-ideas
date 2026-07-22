<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->

# Candidat : AgentAuth

* **Modèle économique :** M2M
* **Cible :** Les entreprises déployant des agents autonomes IA qui interagissent avec des API internes ou tierces (SaaS, ERP, FinTech).
* **Le problème urgent :** Les agents IA ont besoin de droits d'accès pour agir. Actuellement, les développeurs leur confient des clés d'API globales (souvent celles d'utilisateurs humains) avec des privilèges excessifs. En cas d'attaque (prompt injection) ou d'hallucination, l'agent peut exécuter des actions destructrices non autorisées, créant un risque de sécurité critique.
* **L'approche technique :** Une infrastructure IAM (Identity and Access Management) conçue pour les agents. Le système délivre des jetons d'accès éphémères et à portée dynamique (Dynamic Scoping) basés sur l'intention de l'agent, et agit comme un proxy de sécurité validant chaque appel M2M avant son exécution.
* **Pourquoi ChatGPT/Gemini échoue seul :** Un modèle d'IA génère des requêtes mais ne peut pas sécuriser son propre environnement d'exécution ni gérer l'authentification réseau avec révocation en temps réel. La solution repose sur une couche de sécurité infrastructurelle et cryptographique, indépendante du LLM lui-même.
