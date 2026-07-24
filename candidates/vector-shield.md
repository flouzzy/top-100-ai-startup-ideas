<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->

# Candidat : VectorShield

* **Modèle économique :** B2B
* **Cible :** Les entreprises (banques, assurances, e-commerce, santé) déployant des assistants IA ou des agents autonomes basés sur des LLMs en production.
* **Le problème urgent :** Les applications LLM sont vulnérables aux attaques par injection de prompt ("jailbreaks") et à l'exfiltration de données sensibles. Cela expose les entreprises à des risques de sécurité majeurs, des fuites de données personnelles (PII) et des conséquences légales coûteuses si l'IA agit de manière non conforme ou divulgue des secrets d'entreprise.
* **L'approche technique :** Un proxy inversé (reverse proxy) ou une passerelle API positionnée entre l'application cliente et l'API du LLM. Ce système analyse en temps réel les requêtes entrantes pour détecter les intentions malveillantes via des modèles de classification rapides, et filtre les réponses sortantes pour caviarder les données sensibles ou bloquer les hallucinations critiques avant qu'elles n'atteignent l'utilisateur.
* **Pourquoi ChatGPT/Gemini échoue seul :** Un LLM de base est conçu pour générer du texte, pas pour garantir la sécurité systémique de ses propres entrées/sorties. Les instructions système (system prompts) peuvent toujours être contournées par des attaques sophistiquées. Une couche de sécurité déterministe et externe est indispensable pour bloquer les requêtes malveillantes avant même qu'elles ne soient traitées par le LLM coûteux, économisant ainsi des tokens et garantissant une politique de sécurité stricte.
