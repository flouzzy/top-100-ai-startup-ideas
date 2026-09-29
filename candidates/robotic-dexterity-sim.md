<!-- markdownlint-disable MD013 -->
# Candidat : Robotic Dexterity Simulator

* **Domaine principal :** Robotique & Systèmes embarqués
* **Modèle économique :** B2B
* **Cible :** Entreprises de robotique humanoïde, e-commerce/logistique (tri de colis), industrie manufacturière de précision
* **Le problème urgent :** Les bras robotiques excellent dans les mouvements pré-programmés mais échouent lamentablement à manipuler des objets déformables, transparents ou inédits en temps réel. L'entraînement par renforcement (RL) dans le monde réel endommage les robots et prend des années de collecte de données.
* **L'approche technique :** Un simulateur physique ultra-réaliste focalisé sur la mécanique de contact par frottement (frictional contact) et les capteurs tactiles (elastography). Il génère des environnements virtuels où les politiques de contrôle robotique (RL) s'entraînent avec une physique des matériaux exacte, garantissant un "sim-to-real transfer" sans réentraînement physique (Zero-Shot).
* **Pourquoi une solution générique/SaaS classique échoue :** Les moteurs physiques de jeux vidéo (PhysX, Havok) utilisent des approximations pour la vitesse (rigid body dynamics), qui sont fondamentalement erronées pour la préhension robotique (soft-body, déformation, friction dynamique). Le transfert vers le monde réel est alors impossible.
* **Risques majeurs & Dépendances :** La complexité mathématique de la simulation de contact (Linear Complementarity Problems), le besoin de modélisation extrêmement précise des capteurs hardware spécifiques à chaque constructeur, et la concurrence des laboratoires de recherche ouverts.
