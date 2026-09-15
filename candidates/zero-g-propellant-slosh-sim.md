<!-- markdownlint-disable MD013 -->

# Candidat : Zero-G Propellant Slosh Neural Engine

- **Domaine principal :** World Models & Simulation physique / Deep Tech Infra
- **Modèle économique :** B2B
- **Cible :** Fabricants de lanceurs spatiaux (SpaceX, Rocket Lab, ArianeGroup), opérateurs de remorqueurs spatiaux (Space Tugs) et de satellites à propulsion liquide.
- **Le problème urgent :** En microgravité, le carburant liquide (ergols) dans les réservoirs d'un engin spatial flotte et se déplace de manière chaotique (phénomène de "slosh"). Ce ballottement modifie le centre de gravité en temps réel, rendant les manœuvres d'amarrage, de changement d'orbite, ou le rallumage des moteurs extrêmement dangereux et difficiles à contrôler. Les simulations CFD traditionnelles sont beaucoup trop lentes pour être exécutées en temps réel à bord.
- **L'approche technique :** Un réseau de neurones informé par la physique (PINN) entraîné spécifiquement sur des données de mécanique des fluides en apesanteur. Ce modèle agit comme un jumeau numérique ultra-léger et rapide, capable de prédire le ballottement des fluides (slosh dynamics) en temps réel avec une précision CFD, permettant à l'ordinateur de bord d'anticiper et de compenser les perturbations inertielles instantanément.
- **Pourquoi une solution générique/SaaS classique échoue :** Les solveurs Navier-Stokes classiques nécessitent des supercalculateurs et des jours de calcul, ce qui est impossible sur les processeurs rad-hard limités en orbite. Un modèle IA généraliste ne respectera pas les lois strictes de conservation de la masse et de l'énergie (besoin d'architecture PINN).
- **Risques majeurs & Dépendances :** Besoin de données d'entraînement massives issues de vols spatiaux réels (vols paraboliques ou télémétrie satellitaire) très difficiles à obtenir. Validation critique : une erreur de l'algorithme peut entraîner la perte du véhicule.
