<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Q-Shield IoT

- **Domaine principal :** Cybersécurité / Quantique / Systèmes embarqués
- **Modèle économique :** M2M / B2B
- **Cible :** Industriels des infrastructures critiques (réseaux électriques, traitement des eaux, dispositifs médicaux implantables).
- **Le problème urgent :** Q-Day (le moment où un ordinateur quantique cassera le chiffrement RSA/ECC) approche. Des milliards de capteurs et d'actuateurs industriels (IIoT) avec très peu de mémoire et de puissance de calcul (microcontrôleurs) ne peuvent pas faire tourner les algorithmes cryptographiques post-quantiques (PQC) standards récemment approuvés par le NIST (trop lourds). "Store now, decrypt later" expose déjà leurs données de télémétrie actuelles.
- **L'approche technique :** Une implémentation ultra-allégée (bare-metal) et accélérée matériellement (ou par co-design HW/SW) d'algorithmes PQC spécifiques (ex: cristaux-Kyber) packagée comme un RTOS (Real-Time Operating System) minimaliste ou un firmware bootloader pour l'IIoT legacy et futur, permettant l'échange de clés asymétriques sécurisées sous contrainte de micro-watts et de kilo-octets.
- **Pourquoi une solution générique/SaaS classique échoue :** Les solutions de cybersécurité classiques opèrent au niveau applicatif ou réseau (firewalls, proxys) et requièrent des agents lourds (Linux/Windows). Ici le défi est mathématique, bas niveau (C/Rust sur ARM Cortex-M), et soumis à des contraintes physiques (énergie, latence temps-réel) inaccessibles aux SaaS cloud.
- **Risques majeurs & Dépendances :** Adoption lente du marché due aux cycles de vie de 10-20 ans du matériel industriel. Dépendance à l'évolution de la standardisation NIST et à la capacité de mettre à jour le firmware de systèmes déployés sans les briquer.
