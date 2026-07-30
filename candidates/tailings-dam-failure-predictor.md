<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Tailings Dam Failure Predictor

- **Domaine principal :** IA & Agents autonomes (Appliqué à l'Infra/Minier)
- **Modèle économique :** B2B
- **Cible :** Sociétés minières globales (Rio Tinto, Vale, BHP), assureurs industriels, agences environnementales.
- **Le problème urgent :** Les ruptures de barrages de résidus miniers (tailings dams) provoquent des catastrophes écologiques et humaines majeures (ex: Brumadinho). La surveillance actuelle est fragmentée, réactive, et rate les signaux faibles précurseurs de liquéfaction des sols.
- **L'approche technique :** Modèle prédictif spatio-temporel multimodal ingérant en temps réel l'InSAR (satellite), la sismicité, la pression interstitielle (capteurs IoT) et les données météorologiques. Utilisation de réseaux de neurones informés par la physique (PINN) pour modéliser la mécanique des sols et alerter avant la rupture.
- **Pourquoi une solution générique/SaaS classique échoue :** C'est un problème de physique complexe et de fusion de données multi-échelles. Un tableau de bord SaaS standard ne comprend pas la mécanique des fluides et la géotechnique nécessaires pour anticiper un effondrement non-linéaire.
- **Risques majeurs & Dépendances :** Besoin d'accéder aux données historiques privées des mines (souvent réticentes à partager), difficulté d'installation d'IoT dans des zones isolées, et le risque légal massif en cas de faux négatif (la responsabilité en cas de rupture).
