<!-- markdownlint-disable MD013 -->
# Candidat : AgentWall (Firewall pour Agents Autonomes via API)

* **Domaine principal :** IA & Agents autonomes / Cybersécurité
* **Modèle économique :** B2B / M2M
* **Cible :** Entreprises déployant des flottes d'agents IA autonomes, fournisseurs de plateformes LLM (OpenAI, Anthropic) et équipes DevSecOps.
* **Le problème urgent :** Les agents IA autonomes interagissent de plus en plus avec des API d'entreprise, exécutant des actions en chaîne (RPA 2.0). Les firewalls traditionnels (WAF) ou les gestions d'API (API Gateways) ne savent pas distinguer une requête d'un agent malveillant ou halluciné d'une requête légitime. Un agent compromis (Prompt Injection) peut exfiltrer des données ou déclencher des transactions destructrices sans être détecté par les règles de sécurité statiques.
* **L'approche technique :** Développement d'un "API Firewall Intentionnel" qui intercepte les requêtes M2M générées par des IA. Le système utilise un modèle sémantique en temps réel pour reconstruire le "graphe d'intention" de l'agent. Il valide cryptographiquement l'intégrité de la chaîne d'instructions de l'agent, bloquant les déviations sémantiques ou les injections comportementales (Behavioral Zero-Trust).
* **Pourquoi une solution générique/SaaS classique échoue :** Les WAF actuels cherchent des signatures (SQLi, XSS) ou des anomalies de volume. Une attaque par agent IA ressemble à du trafic parfaitement légitime au niveau syntaxique (JSON, headers valides), seule l'intention logique et le contexte sémantique sont altérés. Il faut un moteur d'inférence sémantique ultra-rapide (faible latence) directement au niveau de l'API Gateway.
* **Risques majeurs & Dépendances :** Le défi de la latence (ajouter de l'IA sur chaque call API M2M sans ralentir le système global). Risque de faux positifs bloquant des opérations critiques. Nécessité d'intégration profonde avec les standards d'API Management existants (Kong, Apigee).
