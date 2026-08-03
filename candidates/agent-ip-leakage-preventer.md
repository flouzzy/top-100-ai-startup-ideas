<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Agent IP Leakage Preventer

- **Domaine principal :** IA & Agents autonomes
- **Modèle économique :** B2B
- **Cible :** Grandes entreprises, CISO (Chief Information Security Officer), CTO déployant des flottes d'agents IA autonomes (RAG internes, analyse de code, automatisation financière).
- **Le problème urgent :** Avec la prolifération des agents autonomes d'entreprise communiquant entre eux et avec l'extérieur, il existe un risque massif d'exfiltration furtive de propriété intellectuelle (code, données financières, secrets d'affaires) via des canaux couverts par le comportement complexe de l'agent.
- **L'approche technique :** Implémentation d'un pare-feu de contexte et d'intention (Intent & Context Firewall) au niveau de l'orchestration des agents. Ce système analyse le flux de pensée et les appels API (tool use) en temps réel, appliquant une gouvernance cryptographique stricte sur l'autorisation de mouvement des données sensibles.
- **Pourquoi une solution générique/SaaS classique échoue :** Les DLP (Data Loss Prevention) classiques échouent car les agents IA peuvent reformuler, résumer ou fragmenter l'IP pour contourner les filtres à mots-clés. Il faut un modèle de vérification sémantique capable d'auditer le raisonnement de l'agent.
- **Risques majeurs & Dépendances :** Latence introduite dans le processus de réflexion de l'agent (agent loop), intégration complexe avec de multiples frameworks d'orchestration (LangChain, AutoGen), et nécessité d'une confiance absolue (zero-trust) dans le système de prévention lui-même.
