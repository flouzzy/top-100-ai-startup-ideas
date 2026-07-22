<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->

# Candidat : AgentScope

* **Modèle économique :** M2M
* **Cible :** Les équipes d'ingénierie et de sécurité (SecOps, DevOps) déployant des agents autonomes IA.
* **Le problème urgent :** Les agents IA autonomes nécessitent des clés d'API (AWS, GitHub, Stripe) pour agir. Cependant, une simple injection de prompt ou une hallucination peut détourner ces permissions étendues, causant des fuites de données ou la destruction d'infrastructures. Fournir des clés d'API statiques et puissantes à des systèmes non-déterministes représente un risque de sécurité critique.
* **L'approche technique :** Un proxy de sécurité API (reverse proxy intelligent) entre les agents et les services tiers. L'agent utilise des identifiants restreints ; le proxy intercepte les requêtes, vérifie cryptographiquement l'intention et le périmètre d'action autorisé (via des politiques "Zero Trust" strictes), puis provisionne à la volée des jetons d'accès éphémères (Just-in-Time) aux privilèges minimaux vers l'API cible réelle.
* **Pourquoi ChatGPT/Gemini échoue seul :** Un LLM ne peut pas garantir de manière déterministe qu'il ne se fera pas tromper par un prompt malveillant. Les sécurités basées uniquement sur des "prompts systèmes" sont facilement contournables. La véritable sécurisation doit être appliquée au niveau du réseau et du routage de l'infrastructure, hors d'atteinte du raisonnement du modèle IA.
