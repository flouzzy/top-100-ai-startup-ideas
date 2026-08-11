<!-- markdownlint-disable MD013 -->

# Candidat : Photonic AI Interconnect

- **Domaine principal :** Deep Tech Infra / Matériaux avancés
- **Modèle économique :** B2B
- **Cible :** Hyperscalers (AWS, Google, Meta), concepteurs de supercalculateurs, fabricants de puces (NVIDIA, AMD).
- **Le problème urgent :** L'entraînement des méga-modèles d'IA (LLMs, World Models) est limité par le "mur de la mémoire" et la bande passante inter-puces (interconnects). Les connexions électriques en cuivre (PCIe, NVLink) atteignent leurs limites physiques en termes de chaleur, de latence et de consommation énergétique à l'échelle d'un datacenter.
- **L'approche technique :** Remplacer les bus électriques par une architecture photonique sur silicium (Silicon Photonics) intégrée directement sur le boîtier de la puce (Co-Packaged Optics - CPO). Utilisation de lasers multiplexés en longueur d'onde (WDM) pour transmettre des téraoctets de données par seconde entre les GPU avec une consommation énergétique quasi-nulle par bit transmis et une latence de propagation purement optique.
- **Pourquoi une solution générique/SaaS classique échoue :** C'est un défi fondamental de physique des semi-conducteurs et d'ingénierie optique (couplage laser-fibre, guides d'ondes nanométriques). Aucune optimisation logicielle des graphes de calcul ne peut compenser la limite de vitesse des électrons dans le cuivre.
- **Risques majeurs & Dépendances :** Fiabilité à long terme des lasers intégrés face à la chaleur des GPU ; coût de fabrication (nécessite des usines de silicium photonique spécialisées) ; alignement micrométrique des fibres optiques lors de l'assemblage (packaging).
