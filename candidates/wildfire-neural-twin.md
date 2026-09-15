<!-- markdownlint-disable MD013 -->

# Candidat : Wildfire Neural Twin

- **Domaine principal :** World Models & Simulation physique
- **Modèle économique :** B2B / B2G
- **Cible :** Agences gouvernementales de gestion des forêts, opérateurs de réseaux électriques (utilities), et compagnies d'assurance spécialisées dans les risques climatiques.
- **Le problème urgent :** Les modèles actuels de propagation des incendies de forêt sont lents, s'appuient sur des données statiques et peinent à modéliser les dynamiques de feu extrêmes induites par le micro-climat. Cela entraîne des évacuations tardives, des pertes d'infrastructures massives et des primes d'assurance incalculables.
- **L'approche technique :** Création d'un moteur de physique neuronale (Neural Physics Engine) ingérant en temps réel les données de télémétrie LIDAR, l'imagerie satellite infrarouge et les données de vent IoT pour simuler la thermodynamique de combustion et la dynamique des fluides à une résolution submétrique, des milliers de fois plus vite que les modèles CFD (Computational Fluid Dynamics) traditionnels.
- **Pourquoi une solution générique/SaaS classique échoue :** Un SaaS ou un simple modèle prédictif statistique ne peut pas capturer les non-linéarités de la mécanique des fluides et de la thermodynamique en temps réel. Il faut un modèle de monde (World Model) physique capable d'extrapoler les états futurs basés sur des lois physiques encodées dans les réseaux de neurones.
- **Risques majeurs & Dépendances :** Besoin massif en puissance de calcul (GPU) pour l'entraînement initial du modèle de base, accès critique et coûteux aux données satellites/LIDAR en temps réel, difficulté de validation sur le terrain lors d'événements extrêmes.
