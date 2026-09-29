<!-- markdownlint-disable MD013 -->
# Candidat : Climate Grid Inertia Simulator

* **Domaine principal :** ClimateTech & Énergie
* **Modèle économique :** B2B
* **Cible :** Gestionnaires de réseaux de transport (RTE, National Grid, TSO), opérateurs de fermes éoliennes/solaires
* **Le problème urgent :** La transition vers les énergies renouvelables (éolien, solaire) remplace les générateurs rotatifs lourds (centrales nucléaires/charbon) par des onduleurs électroniques. Cela supprime l'"inertie physique" du réseau, augmentant drastiquement le risque de blackouts instantanés en cas de fluctuation soudaine de la fréquence électrique.
* **L'approche technique :** Un jumeau numérique temps réel de la grille électrique utilisant l'IA physics-informed pour simuler et prédire les creux de tension et la stabilité transitoire. Le système orchestre dynamiquement les parcs de batteries (BESS) et les onduleurs grid-forming pour injecter de l'inertie synthétique ultra-rapide.
* **Pourquoi une solution générique/SaaS classique échoue :** Les dynamiques de grille se mesurent en millisecondes. Les logiciels SCADA classiques sont réactifs et trop lents. Un modèle IA standard hallucinerait les lois de Kirchhoff, ce qui est inacceptable pour un système critique : le modèle doit être strictement contraint par la physique électromagnétique.
* **Risques majeurs & Dépendances :** Réglementation stricte des TSOs, difficulté d'intégration avec l'équipement hardware existant (onduleurs hétérogènes), cycle de vente extrêmement long (B2G/Monopoles d'État), responsabilité juridique colossale en cas de défaillance entraînant un blackout.
