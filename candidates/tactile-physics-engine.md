<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Tactile Physics Engine

- **Domaine principal :** Robotique & Systèmes embarqués
- **Modèle économique :** B2B
- **Cible :** Fabricants de robots industriels, intégrateurs logistiques, entreprises de robotique humanoïde.
- **Le problème urgent :** Les bras robotiques actuels excellent dans la manipulation rigide (souder des voitures), mais échouent lamentablement à manipuler des objets déformables, fragiles ou inconnus (textiles, câbles, produits frais). L'absence de compréhension physique du "toucher" entraîne une casse matérielle importante, limitant l'automatisation dans des secteurs comme la logistique e-commerce, l'agriculture ou le textile.
- **L'approche technique :** Un moteur de simulation physique (World Model) multimodal qui fusionne en temps réel la vision par ordinateur avec des capteurs tactiles haute résolution (ex: GelSight). Il crée une représentation interne déformable (mesh) de l'objet manipulé pour ajuster l'impédance et la force de préhension des effecteurs en boucle fermée (closed-loop control) à haute fréquence.
- **Pourquoi une solution générique/SaaS classique échoue :** L'inférence LLM/VLM est trop lente (latence > 100ms) et abstraite. Il faut des réseaux de neurones continus (PINNs - Physics-Informed Neural Networks) compilés pour tourner sur du hardware Edge (FPGA/ASIC) à plus de 1000 Hz, avec une intégration intime du hardware (capteurs élastomères et moteurs).
- **Risques majeurs & Dépendances :** Fragilité mécanique et usure des capteurs tactiles en environnement industriel, nécessité de construire des jumeaux numériques extrêmement précis pour l'entraînement (Sim2Real gap), barrière à l'entrée matérielle élevée.
