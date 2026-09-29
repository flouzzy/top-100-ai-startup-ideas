<!-- markdownlint-disable MD013 -->
# Candidat : Agentic Sovereign Data Mesh

* **Domaine principal :** IA & Agents autonomes
* **Modèle économique :** B2B
* **Cible :** Hôpitaux, consortiums de recherche pharmaceutique, défense, banques centrales (CBDC)
* **Le problème urgent :** L'entraînement de modèles d'IA sur des données hautement sensibles (Dossiers médicaux, données financières, IP militaire) est bloqué car les entités refusent ou n'ont pas le droit de centraliser leurs données (RGPD, souveraineté). Le Federated Learning classique est rigide, vulnérable aux attaques par inférence et nécessite une orchestration centralisée.
* **L'approche technique :** Un réseau maillé d'agents IA autonomes déployés directement dans les enclaves sécurisées (TEE - Trusted Execution Environments) de chaque participant. Les agents négocient, s'entraînent localement via des méthodes d'apprentissage décentralisé (Swarm Learning) et chiffrent les gradients avec la cryptographie homomorphe, éliminant tout nœud centralisateur.
* **Pourquoi une solution générique/SaaS classique échoue :** Un simple cloud sécurisé exige de faire confiance à l'hébergeur. Les solutions de Federated Learning classiques ne protègent pas contre le reverse-engineering des poids du modèle. Cette solution nécessite une intégration bas niveau avec l'infrastructure de cryptographie (FHE/TEE).
* **Risques majeurs & Dépendances :** Surcharge de calcul (overhead) introduite par la cryptographie homomorphe, bande passante réseau requise pour échanger les poids des modèles lourds, et le défi de l'auditabilité réglementaire d'un essaim d'agents autonomes distribués.
