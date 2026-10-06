<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : PQC IoT Enclave Microchip

* **Domaine principal :** Deep Tech & Cybersécurité
* **Modèle économique :** B2B
* **Cible :** Fabricants d'appareils médicaux connectés, Constructeurs automobiles, Industriels IoT (Chief Product Security Officers).
* **Le problème urgent :** Des milliards de dispositifs IoT critiques (pacemakers, freins de voitures, compteurs intelligents) sont déployés pour des décennies et utilisent des algorithmes cryptographiques (RSA, ECC) qui seront cassés par des ordinateurs quantiques (Harvest Now, Decrypt Later).
* **L'approche technique :** Conception d'une IP Core (Propriété Intellectuelle pour semi-conducteurs) sous forme d'une enclave sécurisée matérielle intégrant nativement et de manière accélérée les algorithmes de cryptographie post-quantique standardisés par le NIST (ex: Kyber, Dilithium). L'IP est optimisée pour des microcontrôleurs à très faible consommation d'énergie et de mémoire.
* **Pourquoi une solution générique/SaaS classique échoue :** Une mise à jour logicielle over-the-air (OTA) ne suffit pas. L'implémentation logicielle d'algorithmes PQC sur de petits microcontrôleurs consomme trop de batterie, ralentit l'appareil et libère trop de chaleur. Il faut une accélération matérielle dédiée (ASIC/FPGA) pour rendre le PQC viable sur l'IoT Edge.
* **Risques majeurs & Dépendances :** Cycle de vie des puces très long (les fabricants sont lents à adopter de nouveaux designs de silicium), normes PQC encore en cours de finalisation, concurrence féroce des géants de l'ARM et des fonderies qui pourraient intégrer leurs propres solutions.
