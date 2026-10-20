<!-- markdownlint-disable MD013 -->
# Candidat : EdgeCrash (Autonomous Vehicle Corner-Case Simulator)

* **Domaine principal :** World Models & Simulation physique / IA
* **Modèle économique :** B2B
* **Cible :** Constructeurs de véhicules autonomes (Waymo, Cruise, Tesla), fabricants de capteurs LiDAR, régulateurs de sécurité automobile.
* **Le problème urgent :** Les systèmes de conduite autonome accumulent des milliards de kilomètres de données réelles "ennuyeuses" (conduite sur autoroute rectiligne), mais manquent cruellement de données sur les "Corner Cases" (situations rares, dangereuses et complexes : ex: enfant qui court derrière un camion dans la neige, capteur aveuglé par le soleil). Il est physiquement impossible de filmer tous ces scénarios dans le monde réel sans tuer des gens.
* **L'approche technique :** Un moteur de rendu neuronal (Neural Rendering / NeRFs / Gaussian Splatting) couplé à un simulateur de physique déterministe. Il génère synthétiquement des flux vidéo, radar et LiDAR multi-modaux photoréalistes en temps réel. Il crée des scénarios adversariens, manipulant les conditions météorologiques, la lumière et la physique des crashs pour "stress-tester" les algorithmes de perception de l'IA (Closed-loop simulation).
* **Pourquoi une solution générique/SaaS classique échoue :** Les moteurs de jeu vidéo traditionnels (Unreal Engine, Unity) génèrent des images "propres" (Game Engines). Ils ne simulent pas le bruit microscopique des photons frappant un capteur CMOS ou les réflexions complexes d'un faisceau LiDAR sur du verre mouillé. L'IA autonome voit la différence et s'entraîne mal (Domain Gap).
* **Risques majeurs & Dépendances :** Le problème du "Sim-to-Real gap" : si les données générées ne sont pas parfaitement conformes à la physique de la lumière, le réseau de neurones de la voiture apprendra les mauvaises choses. Demande une puissance de calcul massive pour générer de la vidéo/3D haute fidélité.
