<!-- markdownlint-disable MD013 -->

# Candidat : Neuromorphic Proprioception

- **Domaine principal :** Robotique & Systèmes embarqués
- **Modèle économique :** B2B
- **Cible :** Fabricants de robots humanoïdes, de bras robotiques collaboratifs (cobots) et d'exosquelettes.
- **Le problème urgent :** Les robots humanoïdes et manipulateurs avancés actuels ont une "peau" morte. Leur manque de sens du toucher (proprioception fine et perception tactile) les rend maladroits, dangereux pour les humains et incapables de manipuler des objets souples ou fragiles avec la dextérité humaine, limitant leur déploiement hors des usines structurées.
- **L'approche technique :** Une infrastructure complète de perception tactile basée sur des puces neuromorphiques (Spiking Neural Networks - SNN) couplées à des peaux électroniques (e-skin) à haute densité de capteurs. Le système traite l'information sensorielle par événements asynchrones, imitant le système nerveux humain pour une latence ultra-faible (microsecondes) et une consommation énergétique quasi nulle au repos.
- **Pourquoi une solution générique/SaaS classique échoue :** L'approche classique (échantillonnage de milliers de capteurs de pression à 1000 Hz vers un CPU central) sature le bus de données et consomme trop de puissance de calcul et d'énergie pour être embarquée. C'est un goulot d'étranglement strictement matériel et architectural (besoin d'informatique neuromorphique event-based).
- **Risques majeurs & Dépendances :** Immaturité de la fabrication de peaux électroniques durables (résistance mécanique) ; coût de production des ASICs neuromorphiques personnalisés ; difficulté à intégrer les algorithmes SNN avec les contrôleurs cinématiques classiques existants.
