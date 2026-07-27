<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : GPS-Denied Swarm

- **Domaine principal :** Robotique & Systèmes embarqués
- **Modèle économique :** B2G / B2B
- **Cible :** Défense, sécurité civile (recherche et sauvetage en sous-sol), inspection industrielle complexe (canalisations, mines profondes).
- **Le problème urgent :** Les flottes de drones ou de robots terrestres dépendent presque exclusivement du GPS pour la navigation globale. Dans des environnements "GPS-denied" (brouillage militaire, bunkers souterrains, mines effondrées), les flottes deviennent aveugles, incapables de se coordonner spatialement ou de cartographier leur environnement collectivement, ce qui rend l'exploration de ces zones mortelle ou impossible.
- **L'approche technique :** Un système de navigation inertielle collaborative (Collaborative SLAM - Simultaneous Localization and Mapping). En fusionnant les données de capteurs inertiels ultra-précis (centrale à inertie) et les flux LiDAR/VIO (Visual Inertial Odometry) distribués sur plusieurs robots, la flotte recalibre sa position absolue de manière décentralisée via un réseau M2M (mesh network ultra-wideband), sans aucun signal externe.
- **Pourquoi une solution générique/SaaS classique échoue :** C'est un problème d'algorithmique embarquée temps réel (Edge Computing) et de fusion de données multi-capteurs contrainte par de faibles puissances de calcul et une bande passante réseau instable. Un LLM ne sert à rien pour résoudre des matrices de covariance distribuées ou filtrer du bruit inertiel en microsecondes.
- **Risques majeurs & Dépendances :** Complexité mathématique du Collaborative SLAM (dérive exponentielle des erreurs inertielles), nécessité de matériel robuste face aux chocs/interférences, cycles de vente gouvernementaux (B2G) lents et exigeants.
