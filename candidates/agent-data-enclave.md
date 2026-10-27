<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Agent Data Enclave

* **Domaine principal :** IA & Agents autonomes / Cybersécurité
* **Modèle économique :** B2B
* **Cible :** Consortia de R&D (ex: pharma, automobile), institutions financières, grandes entreprises voulant croiser des données sans les exposer (B2B multi-tenant).
* **Le problème urgent :** Les entreprises souhaitent utiliser des agents IA pour analyser des bases de données croisées entre partenaires commerciaux afin d'optimiser la chaîne logistique, la recherche médicale ou la détection de fraudes. Cependant, partager les données brutes est impossible pour des raisons réglementaires (RGPD), de confidentialité ou de protection de la propriété intellectuelle.
* **L'approche technique :** Création d'une infrastructure "Secure Data Enclave" (TEE - Trusted Execution Environment) combinée avec du Federated Learning ou de la cryptographie homomorphe. Les agents IA partenaires peuvent envoyer des requêtes ou des modèles locaux dans l'enclave, s'y exécuter sur les données combinées, et ne faire ressortir que les résultats agrégés ou le modèle mis à jour, garantissant qu'aucun agent ne peut exfiltrer les données sources.
* **Pourquoi une solution générique/SaaS classique échoue :** Les plateformes SaaS d'analyse de données requièrent de centraliser les données en clair dans le cloud, créant un point de défaillance majeur de confidentialité. Une solution sans chiffrement matériel (TEE) ou cryptographique ne peut prouver l'étanchéité des données face aux autres participants ou à l'hébergeur cloud.
* **Risques majeurs & Dépendances :** Complexité de mise en place (DevOps lourd pour le TEE). L'exécution d'agents IA (surtout LLMs) au sein d'environnements chiffrés ou de TEEs (comme Intel SGX / AWS Nitro) souffre souvent de limitations de mémoire ou de pénalités de performance massives.
