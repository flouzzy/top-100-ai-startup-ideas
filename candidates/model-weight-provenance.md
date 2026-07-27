<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Model Weight Provenance

- **Domaine principal :** IA & Agents autonomes (Sécurité)
- **Modèle économique :** B2B
- **Cible :** Plateformes cloud (AWS, Azure), fournisseurs de modèles (OpenAI, Anthropic), entreprises d'IA critique (santé, défense, finance).
- **Le problème urgent :** L'attaque par "Model Poisoning" ou l'altération subreptice des poids (weights) d'un modèle open-source (ex: Llama). Si un attaquant modifie subtilement un checkpoint de modèle diffusé sur Hugging Face pour introduire une backdoor indétectable, les entreprises téléchargeant et déployant ce modèle héritent d'une vulnérabilité critique impossible à auditer via du code source.
- **L'approche technique :** Un système de traçabilité cryptographique et d'analyse de gradient de bout en bout pour les modèles d'apprentissage profond. Il combine le hachage cryptographique des tenseurs de poids à chaque étape de l'entraînement, des preuves à divulgation nulle de connaissance (Zero-Knowledge Proofs - ZKP) pour attester du dataset utilisé, et une analyse topologique des réseaux de neurones pour détecter les anomalies de poids post-téléchargement.
- **Pourquoi une solution générique/SaaS classique échoue :** Les scanners de vulnérabilités traditionnels (SAST/DAST) ne comprennent que le code (Python/C++), pas les matrices de millions de poids flottants. L'audit de modèles nécessite une expertise en sécurité ML, l'application de cryptographie avancée (ZKP) sur des structures de données massives (Go/TB de tenseurs), dépassant de loin les capacités d'un outil de cybersécurité standard ou d'un wrapper LLM.
- **Risques majeurs & Dépendances :** Surcharge computationnelle liée à la génération de preuves ZKP sur des gros modèles, manque de standardisation dans la supply chain ML (SBOM pour l'IA balbutiant), difficulté d'intégration profonde avec les frameworks d'entraînement (PyTorch/JAX).
