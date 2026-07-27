<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Kessler Shield Orbitals

- **Domaine principal :** Deep Tech & Infra / Communications spatiales / IA
- **Modèle économique :** B2B / B2G (Space-as-a-Service)
- **Cible :** Opérateurs de méga-constellations (Starlink, Kuiper), gouvernements, assureurs spatiaux.
- **Le problème urgent :** Le syndrome de Kessler menace l'orbite terrestre basse (LEO). Les radars terrestres (Space Force) ont une résolution limitée (>10cm) et d'immenses angles morts temporels (ils ne "voient" pas tout en permanence). Les opérateurs de satellites doivent effectuer des manœuvres d'évitement coûteuses (perte de carburant, durée de vie réduite) souvent basées sur de fausses alertes, ou pire, se prendre des débris non catalogués de la taille d'une bille.
- **L'approche technique :** Le déploiement d'une constellation distribuée de micro-satellites équipés de capteurs optiques et LiDAR collaboratifs, formant un réseau maillé de perception (Edge AI). Les nœuds s'échangent des embeddings de détection (pas de données brutes) pour calculer en orbite (compute in space) et en temps réel l'orbite précise et la taille des débris millimétriques, envoyant des alertes d'évitement déterministes.
- **Pourquoi une solution générique/SaaS classique échoue :** Télécharger le flux vidéo/LiDAR brut de centaines de satellites vers la Terre pour traitement cloud (SaaS classique) dépasserait la bande passante disponible et introduirait une latence critique. L'IA doit fonctionner dans l'environnement radioactif spatial sur des composants rad-hard avec très peu d'énergie (SWaP-C).
- **Risques majeurs & Dépendances :** CAPEX massif pour le lancement de la constellation initiale. Réglementation complexe sur les opérations spatiales autonomes et la responsabilité en cas de collision manquée.
