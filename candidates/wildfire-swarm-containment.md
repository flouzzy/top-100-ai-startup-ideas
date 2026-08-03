<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Wildfire Swarm Containment

- **Domaine principal :** Robotique & Systèmes embarqués
- **Modèle économique :** B2B / B2G
- **Cible :** Agences gouvernementales de gestion des feux de forêt, services d'urgence, et grandes compagnies d'assurance.
- **Le problème urgent :** Les mégafeux deviennent incontrôlables en raison du changement climatique. Les méthodes de lutte actuelles (avions bombardiers d'eau lourds, équipes au sol) sont dangereuses, lentes à déployer de nuit, et inefficaces lors des premières heures critiques (l'attaque initiale) où le feu peut encore être contenu.
- **L'approche technique :** Déploiement de flottes de drones autonomes en essaim (Swarm Robotics) coordonnés par un système de perception spatiale en temps réel. L'essaim modélise la propagation du feu (Neural Physics) pour larguer avec une précision millimétrique des retardants chimiques ciblés, créant des lignes de coupe-feu de manière dynamique, de jour comme de nuit, sans pilote humain.
- **Pourquoi une solution générique/SaaS classique échoue :** L'orchestration d'un essaim dans un environnement thermique extrême (fumée, vents violents, absence de GPS) nécessite une fusion de capteurs locaux (LIDAR, infrarouge) et une intelligence distribuée au niveau du Edge (Edge AI), impossible à réaliser avec un simple logiciel de contrôle de drone centralisé.
- **Risques majeurs & Dépendances :** Réglementations aériennes strictes pour les vols autonomes en essaim (BVLOS), fiabilité du matériel dans des conditions extrêmes (chaleur, turbulences), et logistique de rechargement/maintenance de la flotte sur le terrain.
