<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : AgentTrust Gateway

* **Domaine principal :** IA & Agents autonomes / Cybersécurité
* **Modèle économique :** B2B
* **Cible :** Grandes entreprises (banques, assurances, pharma) déployant des flottes d'agents IA autonomes internes ou externes.
* **Le problème urgent :** Les agents IA autonomes (qui utilisent des outils, exécutent du code, lisent des bases de données) échappent au contrôle des firewalls classiques et des outils IAM (Identity and Access Management), créant un risque critique d'exfiltration de données, d'actions non autorisées (ex: virement bancaire par hallucination) et de non-conformité.
* **L'approche technique :** Création d'un pare-feu sémantique et comportemental dédié aux agents IA, interceptant les appels API, analysant l'intention en temps réel avec des modèles de vérification formelle, et appliquant des politiques de sécurité strictes au niveau des "actions" (Tools/Functions) plutôt que des simples requêtes HTTP.
* **Pourquoi une solution générique/SaaS classique échoue :** Les WAF (Web Application Firewalls) ou solutions DLP (Data Loss Prevention) traditionnelles regardent des patterns statiques ou regex. L'action d'un agent IA est dynamique, contextuelle et requiert une compréhension sémantique de l'objectif pour être bloquée ou autorisée.
* **Risques majeurs & Dépendances :** Latence introduite par l'analyse sémantique, faux positifs bloquant des processus métiers légitimes, évolution rapide des architectures d'agents autonomes.
