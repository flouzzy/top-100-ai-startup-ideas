<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : QuantumRoute PQC

- **Domaine principal :** Cybersécurité & Quantique
- **Modèle économique :** B2B / M2M
- **Cible :** Fournisseurs de télécommunications, banques centrales, opérateurs de réseaux électriques (OIV/OSE).
- **Le problème urgent :** La transition vers la cryptographie post-quantique (PQC) nécessite de remplacer les protocoles de routage BGP et TLS actuels qui seront vulnérables aux attaques "Store Now, Decrypt Later" (SNDL) par des ordinateurs quantiques, risquant de compromettre les données d'infrastructure critique.
- **L'approche technique :** Routeur logiciel de niveau 3 et proxy PQC implémentant les standards NIST (Kyber/Dilithium) avec un overhead réseau minimal, intégrant un mécanisme de "Crypto-Agility" pour changer d'algorithme dynamiquement sans interruption de service (zero-downtime).
- **Pourquoi une solution générique/SaaS classique échoue :** Les SaaS de sécurité habituels gèrent la couche applicative. Ici, le problème se situe au niveau du routage de bas niveau et du transport (couches 3/4 du modèle OSI). Une feuille Excel ou un LLM ne peut pas intercepter et chiffrer des paquets réseau à des vitesses térabits avec de nouveaux algorithmes mathématiques.
- **Risques majeurs & Dépendances :** Adoption lente des standards PQC par les industriels, besoin de certification de sécurité stricte (FIPS, ANSSI), risques de performances (latence accrue due aux nouveaux algorithmes).
