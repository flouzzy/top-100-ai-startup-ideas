<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : OrbitQ-Shield

* **Domaine principal :** Cybersécurité & Résilience / Deep Tech Infra
* **Modèle économique :** B2B / B2G
* **Cible :** Opérateurs de constellations de satellites (Starlink, Kuiper), agences spatiales (ESA, NASA) et armées, qui gèrent des communications ultra-sensibles.
* **Le problème urgent :** Les liaisons de communication par satellite (LEO/GEO) s'appuient sur des standards de cryptographie asymétrique (RSA, ECC) qui seront vulnérables aux attaques "Store Now, Decrypt Later" via l'informatique quantique d'ici la fin de la décennie.
* **L'approche technique :** Implémentation d'une pile logicielle et matérielle de Post-Quantum Cryptography (PQC) optimisée pour les ressources contraintes (SWaP-C : Size, Weight, Power, and Cost) des satellites, intégrant des algorithmes résistants au quantique (NIST standards) et des protocoles de distribution quantique de clés (QKD) spatiaux.
* **Pourquoi une solution générique/SaaS classique échoue :** Les bibliothèques PQC standards sont trop lourdes et gourmandes en énergie pour les puces embarquées des satellites (FPGA/ASIC endurcis contre les radiations). Il faut une optimisation au niveau bare-metal.
* **Risques majeurs & Dépendances :** Certification très longue (critères communs, aérospatial), besoin de tests en orbite coûteux, et évolutions incertaines des standards cryptographiques.
