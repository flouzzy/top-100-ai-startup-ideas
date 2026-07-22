<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->

# Candidat : RAGShield

* **Modèle économique :** B2B
* **Cible :** Entreprises déployant des applications d'IA générative (pipelines RAG), RSSI (CISO) et équipes Data Engineering.
* **Le problème urgent :** L'ingestion de documents tiers (CVs, emails, PDF) dans les bases vectorielles expose l'entreprise aux injections de prompt indirectes. Un attaquant peut glisser des instructions invisibles dans un document pour pirater le LLM d'entreprise, entraînant l'exfiltration de données confidentielles ou l'exécution d'actions malveillantes.
* **L'approche technique :** Pare-feu applicatif (WAF pour IA) agissant comme un proxy de sanitisation entre les sources de données et la base vectorielle. Il combine analyse syntaxique déterministe, modèles de classification légers (heuristiques) et isolation stricte pour neutraliser les "payloads" malveillants avant l'étape d'embedding et d'inférence.
* **Pourquoi ChatGPT/Gemini échoue seul :** Par conception, un LLM ne sait pas isoler parfaitement les instructions du système des données injectées dans son contexte. Même avec un "system prompt" robuste, une donnée corrompue dans le RAG prendra souvent le pas sur les règles de sécurité.
