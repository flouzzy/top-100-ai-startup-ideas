<!-- markdownlint-disable MD013 -->
# Candidat : Post-Quantum Cryptography (PQC) Migration Orchestrator

* **Domaine principal :** Cybersécurité & Résilience
* **Modèle économique :** B2B
* **Cible :** Banques, institutions financières, gouvernements, défense, et grandes entreprises SaaS
* **Le problème urgent :** L'arrivée imminente des ordinateurs quantiques fault-tolerant (Q-Day) menace de casser instantanément les chiffrements RSA et ECC actuels (algorithme de Shor). La stratégie de "Store now, decrypt later" implique que les données critiques volées aujourd'hui seront lisibles demain. La migration vers les standards PQC (NIST) sur des infrastructures massives est un cauchemar logistique et technique.
* **L'approche technique :** Une plateforme d'orchestration de l'agilité cryptographique. Elle cartographie automatiquement (SBOM cryptographique) toutes les dépendances de chiffrement d'une architecture, gère la rotation automatisée des clés vers des algorithmes résistants au quantique (ex: Kyber, Dilithium), et intègre un mode hybride pour assurer la rétrocompatibilité lors de la transition.
* **Pourquoi une solution générique/SaaS classique échoue :** Remplacer un algorithme cryptographique au sein d'une infrastructure implique de modifier le code source, de re-certifier des modules HSM (Hardware Security Modules) et de gérer l'augmentation de la taille des clés et des signatures PQC qui cassent les protocoles réseau standards. Une simple mise à jour logicielle classique ne suffit pas.
* **Risques majeurs & Dépendances :** Standards du NIST encore en phase d'adoption finale, risque de bugs d'implémentation dans la cryptographie (fatal pour la sécurité), friction énorme avec les architectures legacy qui n'ont pas la puissance de calcul pour les algorithmes PQC.
