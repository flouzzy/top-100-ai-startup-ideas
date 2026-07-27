<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Foundation Physics Engine for Autonomy

- **Domaine principal :** World Models / Robotique
- **Modèle économique :** B2B
- **Cible :** Constructeurs de robots humanoïdes (Boston Dynamics, Figure), opérateurs d'entrepôts automatisés, fabricants de drones industriels.
- **Le problème urgent :** Entraîner des robots dans le monde réel (Sim2Real gap) est dangereux, lent et coûteux (casser des bras robotiques à 100k$). Les simulateurs classiques (MuJoCo, Isaac Gym) sont trop rigides, déterministes et peinent à modéliser la physique molle (tissus, liquides, poudres) ou les micro-frictions, rendant le transfert vers la réalité chaotique.
- **L'approche technique :** Un moteur physique 100% neuronal (Neural Physics Engine). Au lieu de résoudre des équations rigides, le système utilise des graphes neuronaux spatio-temporels pré-entraînés sur des milliers d'heures de vidéos du monde réel pour générer des simulations infinies, photoréalistes, obéissant à la physique de manière émergente.
- **Pourquoi une solution générique/SaaS classique échoue :** Les moteurs de jeu (Unreal, Unity) sont faits pour paraître beaux, pas pour être physiquement précis au micron pour des capteurs haptiques ou des actuateurs haute fréquence. Un LLM textuel ne sait pas coordonner la proprioception d'un robot à 20 degrés de liberté attrapant un objet glissant.
- **Risques majeurs & Dépendances :** Besoin massif de calcul (GPU clusters) pour l'entraînement du modèle fondamental. Prouver que la "physique hallucinée" ne crée pas de biais de sécurité critiques lors du déploiement en conditions réelles (safety alignment of physics).
