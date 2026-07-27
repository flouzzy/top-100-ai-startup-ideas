<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Aeolus Swarm Engine

- **Domaine principal :** World Models / ClimateTech
- **Modèle économique :** B2B
- **Cible :** Opérateurs de parcs éoliens offshore et gestionnaires de réseaux électriques (Ørsted, Vestas, RWE).
- **Le problème urgent :** L'effet de sillage (wake effect) réduit l'efficacité énergétique des parcs éoliens jusqu'à 20%. Les modèles aérodynamiques actuels (CFD - Computational Fluid Dynamics) prennent des semaines à tourner sur des supercalculateurs, rendant impossible l'ajustement dynamique en temps réel des turbines selon les micro-changements météorologiques.
- **L'approche technique :** Un moteur de physique neuronale (Neural Physics Engine) entraîné sur des simulations CFD historiques et des données capteurs IoT temps réel. Il simule instantanément la mécanique des fluides pour des parcs entiers et orchestre l'orientation des turbines (yaw) comme un essaim unifié pour minimiser les turbulences et maximiser la capture d'énergie.
- **Pourquoi une solution générique/SaaS classique échoue :** Un LLM ne comprend pas les équations de Navier-Stokes. Les SaaS d'analytics traditionnels s'appuient sur des données passées et des règles heuristiques simples, incapables de modéliser les dynamiques non-linéaires 3D de l'air en temps réel à l'échelle d'un parc de 100 turbines.
- **Risques majeurs & Dépendances :** Besoin massif de données CFD haute-fidélité pour l'entraînement initial (coûts compute énormes). Dépendance aux API de contrôle (souvent propriétaires) des fabricants de turbines (OEMs) pour agir sur le yaw.
