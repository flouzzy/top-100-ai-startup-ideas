<!-- markdownlint-disable MD013 -->
# Candidat : PQCHardwareEnclave

* **Domaine principal :** Cybersécurité & Résilience (Quantique/PQC)
* **Modèle économique :** B2B
* **Cible :** Fabricants d'IoT industriels, équipementiers de télécommunications, fournisseurs d'infrastructures cloud.
* **Le problème urgent :** L'approche de l'ordinateur quantique tolérant aux pannes (Q-Day) rend la cryptographie asymétrique actuelle obsolète. La mise à jour des parcs d'équipements embarqués existants (IoT, routeurs) vers des algorithmes post-quantiques (PQC) est souvent impossible à cause des contraintes de mémoire et de puissance de calcul de ces appareils.
* **L'approche technique :** Conception d'une enclave sécurisée (Trusted Execution Environment - TEE) sur puce (SoC/ASIC) optimisée au niveau matériel pour exécuter des algorithmes cryptographiques PQC (NIST, ex: Kyber, Dilithium) avec un encombrement mémoire et énergétique drastiquement réduit (accélération matérielle).
* **Pourquoi une solution générique/SaaS classique échoue :** La cryptographie post-quantique est particulièrement gourmande en mémoire et en bande passante. Une solution purement logicielle (mise à jour OTA) saturerait le CPU des petits appareils industriels. Il faut une intégration silicon (matérielle) dédiée.
* **Risques majeurs & Dépendances :** Longueur des cycles de conception de semi-conducteurs (tape-out), standardisation encore en cours des algorithmes par le NIST, résistance au remplacement complet du matériel de la part de l'industrie.
