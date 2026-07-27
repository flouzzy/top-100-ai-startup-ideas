<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Neural Physics Engine

- **Domaine principal :** World Models & Robotique
- **Modèle économique :** B2B
- **Cible :** Fabricants de robots humanoïdes et constructeurs automobiles autonomes (Head of Robotics, VP Autonomy).
- **Le problème urgent :** L'entraînement de politiques de contrôle robotique dans le monde réel est trop lent et coûteux. Le transfert des simulations actuelles vers la réalité (sim-to-real gap) échoue à cause de la modélisation inexacte de la physique de contact (friction, matériaux déformables).
- **L'approche technique :** Un moteur de "Neural Physics" qui remplace les solveurs physiques classiques par des réseaux de neurones graphiques (GNN) capables d'apprendre et de simuler la physique de contact complexe, les fluides et les objets mous en temps réel avec un rendu différentiable.
- **Pourquoi une solution générique/SaaS classique échoue :** Les moteurs de jeu existants (Unreal, Unity) privilégient l'apparence visuelle sur la précision physique rigoureuse. Les LLMs n'ont aucune notion de la physique spatiale, de la gravité, ou de la dynamique des corps rigides.
- **Risques majeurs & Dépendances :** Dépendance au hardware (NVIDIA Omniverse), difficulté à prouver l'universalité du solveur neuronal sur de nouveaux matériaux, barrière technologique extrêmement élevée.
