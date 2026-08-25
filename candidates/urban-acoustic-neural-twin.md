<!-- markdownlint-disable MD013 -->
# Candidat : Urban Acoustic Neural Twin

- **Domaine principal :** World Models & Simulation physique
- **Modèle économique :** B2G / B2B
- **Cible :** Municipalités, urbanistes, constructeurs de transports (métros, tramways), et promoteurs immobiliers.
- **Le problème urgent :** La pollution sonore urbaine est un enjeu majeur de santé publique, réduisant l'espérance de vie et causant des maladies cardiovasculaires. Les simulations acoustiques actuelles (Ray Tracing audio) prennent des jours de calcul, sont limitées à de petites zones et échouent à modéliser la réflexion sonore complexe des nouveaux matériaux de construction.
- **L'approche technique :** Moteur de simulation acoustique spatiale à l'échelle d'une ville (Neural Twin) utilisant des réseaux de neurones informés par la physique (PINNs) pour résoudre l'équation des ondes en temps réel. Il intègre la géométrie urbaine 3D, les propriétés des matériaux et le trafic dynamique pour simuler la propagation du bruit de manière interactive.
- **Pourquoi une solution générique/SaaS classique échoue :** Les méthodes numériques traditionnelles (Boundary Element Method) ne scalent pas à la taille d'une métropole. Un LLM ou un SaaS standard n'a aucune compréhension des équations différentielles partielles régissant la physique ondulatoire et la diffraction dans des géométries urbaines complexes.
- **Risques majeurs & Dépendances :** Besoin massif de données pour calibrer le modèle (capteurs IoT acoustiques dispersés dans la ville), difficulté à modéliser la variabilité atmosphérique (vent, température) qui affecte la propagation du son, longue durée des cycles de vente (B2G).
