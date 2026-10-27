<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : NeuralAeroSim

* **Domaine principal :** World Models & Simulation physique
* **Modèle économique :** B2B
* **Cible :** Constructeurs aéronautiques, entreprises spatiales (lanceurs réutilisables), start-ups du vol hypersonique et agences de défense.
* **Le problème urgent :** La conception et le test de véhicules hypersoniques nécessitent des simulations de mécanique des fluides (CFD) extrêmement coûteuses en temps de calcul et des tests en soufflerie hypersonique rares et hors de prix. Cela ralentit drastiquement la R&D et multiplie les coûts par des dizaines de millions pour la certification thermique et aérodynamique.
* **L'approche technique :** Développement d'un Neural Physics Engine qui utilise un réseau de neurones informés par la physique (PINNs - Physics-Informed Neural Networks) pour simuler l'aérodynamique et la thermodynamique hypersonique (Mach 5+). Il prédit les ondes de choc, le transfert de chaleur et l'ablation des matériaux en temps réel au lieu de semaines de calculs sur supercalculateurs.
* **Pourquoi une solution générique/SaaS classique échoue :** Les outils de simulation CFD classiques résolvent les équations de Navier-Stokes par éléments finis, ce qui est fondamentalement lent et non différentiable pour l'optimisation générative. Un LLM ou une simple approche SaaS ne peut pas comprendre ni générer des champs physiques 3D complexes, car ils manquent de modélisation spatiale et de contraintes physiques strictes.
* **Risques majeurs & Dépendances :** Nécessité d'accès à des jeux de données d'entraînement CFD massifs et qualitatifs ou à des données de vol réelles (hautement confidentielles/classifiées). Besoin initial de très grande puissance de calcul (GPU) pour l'entraînement du World Model avant l'inférence.
