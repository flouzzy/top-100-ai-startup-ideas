<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Post-Quantum Cryptography Migration Orchestrator

- **Domaine principal :** Cybersécurité & Résilience / Quantique
- **Modèle économique :** B2B
- **Cible :** Banques systémiques, organismes gouvernementaux, opérateurs d'infrastructures critiques (OIV), et réseaux de télécommunications.
- **Le problème urgent :** La menace "Harvest Now, Decrypt Later" (récolter aujourd'hui, décrypter plus tard) expose les secrets d'État et financiers aux futurs ordinateurs quantiques. Les gouvernements (NIST, ANSSI) exigent une migration d'ici 2030, mais les architectures IT actuelles contiennent des milliers de certificats et dépendances RSA/ECC entremêlés, sans inventaire précis.
- **L'approche technique :** Un moteur d'analyse bas niveau de flux réseau et de SBOM (Software Bill of Materials) cryptographique, qui identifie chaque instance de crypto vulnérable (dans les binaires, API, firmwares), et injecte de manière dynamique des couches de crypto-agilité (algorithmes PQC comme Kyber ou Dilithium) via des proxys ou des patchs automatisés sans downtime.
- **Pourquoi une solution générique/SaaS classique échoue :** Un simple scanner de vulnérabilités SaaS ne détecte pas les bibliothèques cryptographiques compilées en dur dans des systèmes legacy ou des contrôleurs industriels. Il faut une analyse statique de binaires et une inspection profonde de paquets (DPI) pour repérer les échanges d'échange de clés asymétriques cachés.
- **Risques majeurs & Dépendances :** L'évolution des normes du NIST (si les algorithmes PQC choisis s'avèrent vulnérables, ce qui est déjà arrivé). Les performances (les clés PQC sont beaucoup plus grandes, ce qui peut saturer les bandes passantes réseau et ralentir les systèmes embarqués).
