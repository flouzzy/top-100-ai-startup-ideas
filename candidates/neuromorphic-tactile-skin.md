<!-- markdownlint-disable MD013 -->
# Candidat : Neuromorphic Tactile Skin

- **Domaine principal :** Robotique & Systèmes embarqués
- **Modèle économique :** B2B
- **Cible :** Fabricants de robots humanoïdes (Tesla, Figure), entreprises de logistique automatisée (Amazon), et concepteurs de prothèses médicales avancées.
- **Le problème urgent :** Les mains robotiques actuelles manquent de dextérité fine car elles s'appuient principalement sur la vision par ordinateur, qui souffre d'occlusions. Les capteurs tactiles existants génèrent des volumes de données continus trop lourds à traiter en temps réel (latence) et sont fragiles.
- **L'approche technique :** Création d'une "peau" polymère intégrant des milliers de micro-capteurs de pression et de cisaillement, reliés à une architecture de puce neuromorphique (Spiking Neural Networks) qui ne transmet que les "événements" de changement (asynchrones), réduisant la latence à la microseconde et la consommation d'énergie de 99%.
- **Pourquoi une solution générique/SaaS classique échoue :** Le goulot d'étranglement se situe au niveau de l'architecture de von Neumann classique et de la transmission de données physiques. Il faut inventer de nouveaux matériaux souples conducteurs, concevoir des ASIC neuromorphiques dédiés, et écrire de nouveaux paradigmes d'apprentissage (Spike Timing Dependent Plasticity) pour le contrôle moteur.
- **Risques majeurs & Dépendances :** Complexité de fabrication (intégration de puces dures sur des substrats étirables), durée de vie des matériaux sous des millions de cycles de déformation, difficulté à standardiser l'interface avec les OS robotiques existants (ROS).
