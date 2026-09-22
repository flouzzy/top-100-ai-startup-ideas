<!-- markdownlint-disable MD013 -->

# Candidat : Décodeur Neuronal à Impulsions pour BCI (Spiking Neural Decoder for BCI)

- **Domaine principal :** Biotech & Bio-informatique / IA
- **Modèle économique :** B2B2C
- **Cible :** Fabricants de hardware BCI (Interfaces Cerveau-Machine) invasifs et non invasifs, centres de rééducation neurologique, et patients atteints du syndrome d'enfermement (Locked-in).
- **Le problème urgent :** Les systèmes de décodage des ondes cérébrales actuels utilisent des architectures Deep Learning (CNN/RNN) qui sont très gourmandes en énergie et génèrent beaucoup de latence. Si on doit implanter la puce de traitement dans le crâne, la dissipation thermique (TDP) du calcul neuronal classique brûle littéralement les tissus cérébraux environnants (limite thermique très stricte).
- **L'approche technique :** Un processeur neuromorphique dédié au BCI exécutant des Réseaux de Neurones à Impulsions (Spiking Neural Networks - SNN). Les SNN imitent la façon dont le cerveau fonctionne (basé sur des événements discrets, donc très peu d'énergie au repos) permettant un décodage moteur temps réel "on-chip" avec une consommation électrique en microwatts, évitant la chauffe crânienne.
- **Pourquoi une solution générique/SaaS classique échoue :** L'envoi de données brutes BCI vers un cloud a trop de latence et pose d'énormes problèmes de sécurité (piratage du flux moteur du cerveau). Le traitement "on-device" classique consomme trop. La création d'un ASIC neuromorphique spécifique est requise.
- **Risques majeurs & Dépendances :** Approbation FDA pour les implants médicaux actifs avec intelligence embarquée, difficulté d'entraînement de modèles SNN (absence de backpropagation classique), et miniaturisation du hardware.
