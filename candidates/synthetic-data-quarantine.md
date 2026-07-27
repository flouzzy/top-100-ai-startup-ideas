<!-- markdownlint-disable MD013 -->
# Candidat : Synthetic Data Quarantine

* **Modèle économique :** B2B (Infrastructure Data & ML Ops)
* **Cible :** Ingénieurs ML, Data Scientists et équipes Data des entreprises développant ou affinant des modèles d'IA (Fine-tuning, RAG, LLM from scratch).
* **Le problème urgent :** Le "Model Collapse". Internet est inondé de données générées par l'IA. Si une entreprise entraîne ou fine-tune ses modèles sur ces données synthétiques non filtrées, la qualité du modèle se dégrade rapidement (perte de diversité, amplification des biais, hallucinations). Cela coûte des millions en compute (GPU) gâché et ruine la fiabilité des modèles de production.
* **L'approche technique :** Un système de pipeline de données (API/Gateway) qui analyse les flux de données d'entraînement en temps réel. Il utilise des modèles de détection d'artefacts génératifs (watermarks invisibles, perplexité, anomalies statistiques) pour identifier, scorer et mettre en quarantaine les données probables d'être générées par l'IA avant qu'elles n'intègrent le dataset final.
* **Pourquoi ChatGPT/Gemini échoue seul :** Un LLM ne peut pas s'auto-évaluer efficacement sur des pétaoctets de données pour détecter s'il a généré ou non une donnée. C'est un problème d'infrastructure de données massives (Big Data) et d'analyse probabiliste à grande échelle, nécessitant une tuyauterie dédiée et des algorithmes de détection spécifiques (détection de filigranes, analyse de distribution de tokens), et non un simple prompt.
