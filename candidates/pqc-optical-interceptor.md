<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : PQC Optical Interceptor

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B / B2G
- **Cible :** Banques centrales, agences de renseignement, grandes institutions financières, opérateurs de datacenters.
- **Le problème urgent :** L'attaque "Store Now, Decrypt Later" (SNDL). Des acteurs étatiques aspirent massivement le trafic internet chiffré aujourd'hui dans l'espoir de le déchiffrer demain avec des ordinateurs quantiques. La cryptographie RSA/ECC actuelle sera brisée (algorithme de Shor), exposant rétroactivement des secrets d'État, des transactions financières et des propriétés intellectuelles.
- **L'approche technique :** Un boîtier d'interception et de ré-encapsulation hardware (Appliance réseau de couche 1/2) qui s'installe directement sur la fibre optique (Data Center Interconnects - DCI). Il intercepte le trafic TLS existant et applique de manière transparente une couche de chiffrement post-quantique (Post-Quantum Cryptography - algorithmes NIST comme CRYSTALS-Kyber) à très haut débit (Tbps) sans modifier les applications métiers.
- **Pourquoi une solution générique/SaaS classique échoue :** L'implémentation de PQC au niveau applicatif (SaaS) requiert des années de refonte du code legacy. Ce problème nécessite une solution au niveau du silicium (FPGA/ASIC) capable de traiter des flux optiques massifs en temps réel avec une latence quasi-nulle, impliquant des compétences pointues en cryptographie matérielle et en photonique.
- **Risques majeurs & Dépendances :** Évolution rapide des standards cryptographiques NIST, résistance des acheteurs face au "black box hardware", complexité extrême du design de puces FPGA à très haut débit.
