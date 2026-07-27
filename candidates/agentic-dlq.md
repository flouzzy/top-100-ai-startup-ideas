<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Agentic DLQ

* **Modèle économique :** B2B
* **Cible :** Les équipes d'ingénierie, les ingénieurs MLOps et les plateformes RPA déployant des agents autonomes complexes en production.
* **Le problème urgent :** Lorsqu'un agent autonome échoue de manière inattendue ou "plante" au milieu d'une tâche complexe (ex: flux asynchrones, appels d'API multiples), son état d'exécution et son contexte de raisonnement sont perdus. Cela oblige à recommencer toute la tâche depuis le début, ce qui entraîne un gaspillage massif de tokens, des échecs non résolus et une incapacité à déboguer efficacement les erreurs en production.
* **L'approche technique :** Une infrastructure de "Dead Letter Queue" (DLQ) spécialement conçue pour les flux agentiques. En cas de défaillance, le système capture instantanément l'état complet de l'agent (historique des prompts, variables d'environnement, état de l'API, mémoire de travail). Ce "dump" est stocké en toute sécurité, permettant à un ingénieur ou à un agent réparateur de corriger l'erreur, puis de relancer l'agent (hot-resume) exactement là où il s'était arrêté.
* **Pourquoi ChatGPT/Gemini échoue seul :** Les LLMs sont par nature sans état (stateless) et ne disposent pas d'un système de gestion de l'exécution ou d'interruption. Un LLM ne peut pas "mettre en pause" son propre environnement technique défaillant pour permettre une intervention externe. Capturer un crash applicatif et orchestrer un hot-resume nécessite une tuyauterie infrastructurelle externe robuste, totalement hors de portée d'une simple requête de modèle.
