<!-- markdownlint-disable MD013 -->

# Candidat : Agent Liability Blackbox

- **Domaine principal :** IA & Agents autonomes
- **Modèle économique :** B2B
- **Cible :** Entreprises déployant des agents IA autonomes (banques, santé, e-commerce), assureurs spécialisés en cyber-risques IA
- **Le problème urgent :** Lorsqu'un agent IA autonome prend une décision entraînant une perte financière ou une violation légale, il est impossible de tracer exactement pourquoi cette décision a été prise. Cela paralyse le déploiement d'agents en production par peur de non-conformité et rend les polices d'assurance impossibles à tarifer.
- **L'approche technique :** Création d'un "Flight Data Recorder" inaltérable (boîte noire) pour agents IA. Le système capture l'arbre de décision cryptographique (Merkle tree) de l'agent, l'état du contexte (mémoire court terme), les appels API effectués, et signe l'ensemble avec un horodatage immuable sur un registre Zero-Trust bas niveau.
- **Pourquoi une solution générique/SaaS classique échoue :** Les logs de serveurs classiques (Datadog, Splunk) sont modifiables et ne capturent pas l'état non-déterministe d'un LLM orchestrant un workflow. Il faut un ancrage cryptographique qui prouve l'état de l'agent _au moment de l'inférence_ avec non-répudiation.
- **Risques majeurs & Dépendances :** Overhead (latence) ajouté lors des appels d'agents, adoption lente par manque de standards légaux clairs sur la responsabilité des agents IA, complexité d'intégration avec de multiples frameworks d'orchestration (LangChain, AutoGen, etc.).
