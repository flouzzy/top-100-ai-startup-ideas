<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : PQC CBOM Radar

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B
- **Cible :** CISO (Chief Information Security Officers) et responsables d'infrastructures critiques (Énergie, Défense, Finance).
- **Le problème urgent :** Les agences de sécurité nationales (ANSSI, CISA, NSA) imposent une migration vers la cryptographie post-quantique (PQC) avant 2030 pour contrer la menace "Store Now, Decrypt Later". Cependant, les grandes entreprises ignorent où se cachent leurs clés et algorithmes vulnérables (RSA, ECC) dans des millions de lignes de code legacy, des firmwares industriels et des systèmes embarqués non documentés. L'impossibilité de cartographier ces dépendances expose ces infrastructures à des risques de non-conformité et de piratage massif.
- **L'approche technique :** Un moteur d'analyse statique et dynamique de binaires (Deep Binary Analysis) capable de générer un CBOM (Cryptographic Bill of Materials). L'outil décompile le code machine et les firmwares legacy pour détecter les appels aux librairies cryptographiques obsolètes via des heuristiques et de l'analyse de flux, générant une cartographie précise sans nécessiter le code source original.
- **Pourquoi une solution générique/SaaS classique échoue :** L'analyse doit se faire on-premise (Air-Gapped) sur des systèmes industriels critiques (OT) ou du code compilé (sans code source). Un LLM classique ou un scanner cloud ne peut pas analyser des binaires complexes, ni déchiffrer des firmwares propriétaires en ARM ou MIPS. L'IP et les données cryptographiques sont beaucoup trop sensibles pour être envoyées sur une API tierce.
- **Risques majeurs & Dépendances :** Complexité technique extrême de la décompilation multi-architectures. Cycles de vente très longs (12 à 24 mois) typiques des infrastructures critiques et des gouvernements. Dépendance à la standardisation définitive des algorithmes PQC par le NIST.
