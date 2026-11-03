<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : HapticEarth Teleop

* **Domaine principal :** Robotique & Systèmes embarqués
* **Modèle économique :** B2B
* **Cible :** Compagnies minières mondiales (BHP, Rio Tinto), opérateurs de forage offshore et entreprises d'intervention en milieux hostiles (nucléaire).
* **Le problème urgent :** L'automatisation complète des engins miniers lourds échoue souvent face aux imprévus géologiques ou conditions extrêmes. Le pilotage à distance actuel (téléopération) est inefficace et dangereux à cause du manque de retour sensoriel, causant accidents et baisse de rendement.
* **L'approche technique :** Système de téléopération immersive avec retour de force haptique ultra-basse latence, couplé à un jumeau numérique 3D généré en temps réel (via LiDAR/SLAM). L'opérateur "sent" la résistance de la roche ou du terrain, assisté par une IA qui filtre les mouvements parasites et compense la latence du réseau.
* **Pourquoi une solution générique/SaaS classique échoue :** Ce n'est pas un problème logiciel : il faut concevoir des interfaces matérielles haptiques robustes, des algorithmes de contrôle-commande prédictifs (pour contrer la latence réseau), et un pipeline de perception 3D embarqué sur des machines de plusieurs tonnes.
* **Risques majeurs & Dépendances :** Adoption par les syndicats miniers, fiabilité des réseaux (5G privée / Satellite LEO) pour maintenir une latence <50ms indispensable à l'haptique.
