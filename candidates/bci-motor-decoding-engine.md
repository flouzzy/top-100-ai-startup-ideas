<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : BCI Motor Decoding Engine

- **Domaine principal :** Biotech & Bio-informatique (Neurotech)
- **Modèle économique :** B2B
- **Cible :** Fabricants de prothèses robotiques, startups d'implants neuronaux, hôpitaux de rééducation.
- **Le problème urgent :** Les interfaces cerveau-machine (BCI) actuelles peinent à traduire l'activité neuronale brute en mouvements fluides et complexes (par exemple, jouer au piano ou saisir un objet fragile). La calibration est longue, spécifique à chaque patient, et le signal se dégrade avec le temps (cicatrisation autour des électrodes).
- **L'approche technique :** Un moteur d'apprentissage profond (Foundation Model) pour le décodage moteur, pré-entraîné sur de vastes ensembles de données de dynamique cérébrale inter-patients. Le modèle utilise l'adaptation de domaine en temps réel pour compenser la dérive des signaux et traduire l'intention motrice en cinématique robotique fluide sans recalibration quotidienne lourde.
- **Pourquoi une solution générique/SaaS classique échoue :** L'analyse de données EEG/ECoG classique repose sur des filtres manuels et des algorithmes linéaires (Kalman) incapables de capturer la dynamique non-linéaire complexe du cerveau. Il faut une architecture IA spécialisée à très faible latence fonctionnant sur des puces embarquées (Edge AI).
- **Risques majeurs & Dépendances :** Obstacles éthiques et réglementaires massifs, difficulté d'acquisition de données neuronales invasives à grande échelle, et risques de biocompatibilité matérielle à long terme des implants.
