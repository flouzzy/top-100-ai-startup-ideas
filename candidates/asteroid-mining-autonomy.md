<!-- markdownlint-disable MD013 -->

# Candidat : Asteroid Mining Autonomy Engine

- **Domaine principal :** Robotique & Systèmes embarqués (Space Tech)
- **Modèle économique :** B2B
- **Cible :** Agences spatiales (NASA, ESA) et entreprises privées d'exploitation spatiale (AstroForge, Karman+), constructeurs de sondes spatiales.
- **Le problème urgent :** L'extraction de ressources sur des astéroïdes (eau, platine, terres rares) implique des opérations robotiques complexes à plusieurs millions de kilomètres de la Terre. La latence des communications (plusieurs minutes à dizaines de minutes) rend le téléguidage humain impossible. Les robots doivent être capables de percevoir, d'analyser la surface, de forer et de réagir aux anomalies physiques en totale autonomie spatiale.
- **L'approche technique :** Moteur de perception spatiale temps réel et de contrôle moteur embarqué, résistant aux radiations (rad-hard compute). Utilisation de réseaux de neurones pour le SLAM en microgravité et la manipulation d'outils d'excavation, avec des modèles physiques de contact pour s'ancrer et forer sur des surfaces à très faible gravité et de composition inconnue.
- **Pourquoi une solution générique/SaaS classique échoue :** Un modèle d'IA cloud classique ne fonctionne pas sans connexion internet permanente et à faible latence. Le système doit tourner en Edge strict sur des puces tolérantes aux radiations (FPGA/ASIC spécialisés) avec des contraintes d'énergie drastiques, nécessitant une compréhension profonde de la physique des corps célestes.
- **Risques majeurs & Dépendances :** Coûts de R&D prohibitifs pour la validation spatiale, accès au hardware spatial pour les tests, lenteur des missions spatiales pour valider en condition réelle, traité de l'espace sur l'exploitation des ressources.
