<!-- markdownlint-disable MD013 -->

# Candidat : Multi-Agent Memory Isolation

- **Domaine principal :** IA & Agents autonomes
- **Modèle économique :** B2B
- **Cible :** Grandes entreprises déployant des flottes d'agents IA autonomes internes (RH, Finance, Legal) et fournisseurs d'infrastructures d'IA (Hyperscalers).
- **Le problème urgent :** Lorsque plusieurs agents IA autonomes collaborent et partagent des mémoires contextuelles (Vector Databases) au sein d'une entreprise, les frontières de confidentialité explosent. Un agent "Support" pourrait accidentellement accéder et fuiter des données salariales mémorisées par un agent "RH", créant un cauchemar de conformité (RGPD, HIPAA).
- **L'approche technique :** Création d'une couche d'isolation de mémoire vectorielle basée sur le chiffrement homomorphe partiel (FHE) ou des environnements d'exécution de confiance (TEE). Les agents interrogent et partagent des concepts mathématiques sans jamais déchiffrer le texte sous-jacent, garantissant un cloisonnement strict (Role-Based Memory Access) au niveau du vecteur.
- **Pourquoi une solution générique/SaaS classique échoue :** L'IAM classique (Identity and Access Management) fonctionne sur des fichiers ou des bases SQL structurées. Il est inopérant sur les plongements vectoriels (embeddings) flous et sémantiques. Les LLMs ne peuvent pas "oublier" ou garantir l'isolement sans une architecture cryptographique bas niveau sur leur couche de mémoire à long terme.
- **Risques majeurs & Dépendances :** Le surcoût computationnel massif (latence) du chiffrement homomorphe sur les opérations de similarité cosinus, la complexité d'intégration avec les bases de données vectorielles existantes (Pinecone, Milvus), dégradation potentielle de la qualité des réponses des agents.
