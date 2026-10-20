<!-- markdownlint-disable MD013 -->
# Candidat : GridEdge (Smart Grid Edge Router)

* **Domaine principal :** ClimateTech & Énergie / Deep Tech Infra
* **Modèle économique :** B2B
* **Cible :** Gestionnaires de réseaux de distribution (DSO - Enedis, PG&E), opérateurs de microgrids (Microgrids) et agrégateurs de flexibilité.
* **Le problème urgent :** L'intégration massive d'énergies renouvelables intermittentes (solaire, éolien) et la prolifération des véhicules électriques (V2G) déstabilisent la fréquence et la tension des réseaux électriques locaux. L'architecture centralisée (SCADA) traditionnelle souffre d'une latence trop élevée pour réagir aux fluctuations de l'ordre de la milliseconde à la périphérie (Edge) du réseau.
* **L'approche technique :** Matériel embarqué (Routeurs Edge matériels durcis) couplé à une IA de contrôle local (Reinforcement Learning) déployé dans les postes de transformation locaux. Ils agissent comme des "routeurs internet pour l'électricité", prenant des décisions autonomes de délestage, d'injection ou de stockage de puissance active/réactive (en millisecondes) sans attendre l'ordre du cloud central.
* **Pourquoi une solution générique/SaaS classique échoue :** Un SaaS cloud traditionnel implique un round-trip (latence réseau) trop lent pour prévenir une chute de fréquence locale (blackout). Cela nécessite une convergence hardware (silicon, capteurs de puissance) et software embarqué (Edge AI temps réel strict, OS temps réel - RTOS).
* **Risques majeurs & Dépendances :** Hardware : concevoir des équipements industriels certifiés. Cycles de vente extrêmement longs et complexes avec les monopoles de distribution d'énergie.
