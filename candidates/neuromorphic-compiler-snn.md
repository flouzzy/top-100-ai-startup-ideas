<!-- markdownlint-disable MD013 -->

# Candidat : SynaptoCompile Edge

- **Domaine principal :** Deep Tech (Semi-conducteurs) / IA
- **Modèle économique :** B2B (SaaS / Licensing IP)
- **Cible :** Concepteurs de puces (Fabless, Intel, BrainChip), fabricants d'appareils IoT autonomes (wearables, capteurs spatiaux).
- **Le problème urgent :** L'inférence IA (Computer Vision, Audio) sur des appareils Edge alimentés par batterie (IoT, drones, implants) consomme trop d'énergie. Les réseaux de neurones classiques (CNN/Transformer) sont inadaptés aux contraintes de micro-watts.
- **L'approche technique :** Un compilateur logiciel universel qui traduit automatiquement les modèles d'apprentissage profond standard (PyTorch/TensorFlow) en Réseaux de Neurones à Impulsions (Spiking Neural Networks - SNN), optimisés pour s'exécuter sur des puces neuromorphiques à très faible consommation d'énergie fonctionnant par événements (event-based).
- **Pourquoi une solution générique/SaaS classique échoue :** La compilation vers des SNN est fondamentalement différente du calcul tensoriel dense (GPU/TPU). Elle requiert un routage temporel et asynchrone des "spikes" que les compilateurs ML classiques (TVM, XLA) ne peuvent pas gérer sans perte massive de précision.
- **Risques majeurs & Dépendances :** Le marché du matériel neuromorphique est encore naissant et très fragmenté. Si des puces classiques (NPU ultra-low power) deviennent suffisamment efficaces, l'avantage compétitif des SNN (et donc du compilateur) pourrait disparaître.
