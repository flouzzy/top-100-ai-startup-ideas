<!-- markdownlint-disable MD013 -->
# Candidat : World Model for Autonomous Driving

* **Domaine principal :** World Models & Simulation physique
* **Modèle économique :** B2B
* **Cible :** Constructeurs automobiles (OEMs), entreprises de robotique, développeurs de systèmes ADAS et gestionnaires de flottes autonomes
* **Le problème urgent :** L'entraînement des systèmes autonomes nécessite de parcourir des millions de kilomètres dans le monde réel. Ce processus est extrêmement lent, coûteux, dangereux, et échoue systématiquement à capturer les "corner cases" (situations extrêmes ou rares) de manière répétable, bloquant le déploiement sécurisé de l'autonomie de niveau 4/5.
* **L'approche technique :** Développement d'un moteur de physique neuronale combiné à des modèles génératifs spatio-temporels. Le système prédit de manière probabiliste les états futurs du monde à partir d'entrées sensorielles multimodales, générant un environnement immersif, photoréaliste et physiquement exact pour simuler des scénarios infinis.
* **Pourquoi une solution générique/SaaS classique échoue :** Un simulateur 3D classique (ex: Unity, Unreal) nécessite de coder en dur des règles physiques et des scripts comportementaux. Il ne peut pas générer l'infinité de variations stochastiques du monde réel (météo, comportements humains imprévisibles, usure des matériaux) qui sont cruciales pour tester la robustesse des modèles de perception et de contrôle.
* **Risques majeurs & Dépendances :** Besoin d'une puissance de calcul colossale pour l'entraînement du modèle de fondation (GPU clusters), dépendance initiale à des datasets réels de très haute qualité pour le bootstrap, et incertitude quant à la validation de ces simulations par les régulateurs pour l'homologation de sécurité.
