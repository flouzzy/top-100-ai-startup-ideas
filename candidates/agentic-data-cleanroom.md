<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->

# Candidat : Agentic Data Cleanroom

- **Domaine principal :** IA & Agents autonomes
- **Modèle économique :** B2B
- **Cible :** Consortiums industriels, hôpitaux, institutions financières collaborant sur l'entraînement d'IA mais refusant de partager leurs données brutes.
- **Le problème urgent :** L'entraînement de grands modèles (LLM ou World Models) spécialisés nécessite la fusion de données ultra-sensibles provenant de multiples entités concurrentes. Les approches classiques de fédération d'apprentissage (Federated Learning) sont lentes, complexes à orchestrer, et n'offrent pas de garanties cryptographiques prouvables contre l'ingénierie inverse.
- **L'approche technique :** Une infrastructure de Cleanroom (chambre blanche de données) opérée par des agents IA autonomes utilisant des environnements d'exécution de confiance (TEE - Trusted Execution Environments) et du Multi-Party Computation (MPC). Les agents négocient les paramètres, valident le code d'entraînement de manière sécurisée, l'exécutent dans l'enclave, et ne restituent que les poids du modèle agrégé sans qu'aucun humain n'ait accès aux données.
- **Pourquoi une solution générique/SaaS classique échoue :** Un simple partage de fichiers ou un espace cloud standard n'offre pas de sécurité au niveau matériel (hardware enclave). Les solutions de chiffrement classiques ne permettent pas de faire des calculs sur des données chiffrées avec la vélocité nécessaire pour le deep learning.
- **Risques majeurs & Dépendances :** Surcoût de calcul lié à la sécurité (overhead) et limitation de la mémoire dans les TEE (ex: Intel SGX / AMD SEV) qui freine l'entraînement de modèles massifs.
