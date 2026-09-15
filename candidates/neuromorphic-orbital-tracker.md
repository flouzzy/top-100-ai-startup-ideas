<!-- markdownlint-disable MD013 -->

# Candidat : Neuromorphic Orbital Tracker

- **Domaine principal :** World Models & Simulation physique / Deep Tech Infra
- **Modèle économique :** B2B / B2G
- **Cible :** US Space Force, opérateurs de Space Situational Awareness (LeoLabs), et opérateurs de constellations de satellites (Starlink, Kuiper).
- **Le problème urgent :** Le suivi des débris spatiaux et des manœuvres hostiles de satellites en orbite basse (LEO) repose sur des radars et télescopes optiques standards (frame-based). Ces capteurs sont saturés par la quantité d'objets, génèrent des téraoctets de données vides (le ciel noir), et ont une latence trop élevée pour repérer des anomalies cinématiques à très grande vitesse.
- **L'approche technique :** Un réseau de télescopes terrestres et orbitaux équipés de capteurs neuromorphiques (Event-based cameras). Au lieu de capturer des images à intervalle régulier, chaque pixel réagit indépendamment et instantanément uniquement aux changements de luminosité. Associé à un réseau de neurones à impulsions (SNN) sur des puces asynchrones, le système suit des milliers de débris à très haute vitesse avec une résolution temporelle de la microseconde, en consommant quelques milliwatts de puissance de calcul.
- **Pourquoi une solution générique/SaaS classique échoue :** Les algorithmes classiques de Computer Vision (CNN) sont inadaptés aux flux de données asynchrones (Event-based). Cela nécessite un couplage étroit entre un hardware optique très spécifique et une architecture logicielle (SNN) totalement différente des architectures Von Neumann classiques.
- **Risques majeurs & Dépendances :** Manque d'outils de compilation matures pour le hardware neuromorphique. Les capteurs neuromorphiques haute résolution spatiale sont encore coûteux et difficiles à produire à l'échelle spatiale (rad-hard).
