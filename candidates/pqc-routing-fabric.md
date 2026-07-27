<!-- markdownlint-disable MD013 -->

# Candidat : Post-Quantum Routing Fabric (PQRF)

- **Domaine principal :** Cybersécurité & Résilience / Quantique
- **Modèle économique :** B2B (Enterprise/Telco)
- **Cible :** Opérateurs télécoms de niveau 1 (Tier-1), grandes banques, datacenters cloud (AWS, Azure), gouvernements.
- **Le problème urgent :** La menace "Harvest Now, Decrypt Later" (HNDL). Les attaquants stockent actuellement le trafic réseau chiffré (RSA/ECC) pour le déchiffrer dès qu'un ordinateur quantique tolérant aux pannes sera disponible, compromettant les secrets d'État et bancaires d'aujourd'hui.
- **L'approche technique :** Implémentation de routeurs SDN (Software-Defined Networking) hybrides qui encapsulent et découpent le trafic de bout en bout en temps réel à très haut débit en utilisant les algorithmes standardisés NIST PQC (CRYSTALS-Kyber/Dilithium), sans pénaliser la latence.
- **Pourquoi une solution générique/SaaS classique échoue :** Un simple patch logiciel au niveau de la couche applicative (L7) est insuffisant, il faut chiffrer massivement au niveau des couches réseau (L2/L3) avec une accélération matérielle (FPGA/ASIC) pour supporter des térabits de trafic sans goulet d'étranglement.
- **Risques majeurs & Dépendances :** Les algorithmes PQC génèrent des clés et des signatures plus larges, ce qui peut saturer les buffers des routeurs existants. Dépendance forte aux standards en cours d'évolution et à la compatibilité matérielle legacy.
