<!-- markdownlint-disable MD013 -->

# Candidat : Nanopore Protein Sequencer

- **Domaine principal :** Biotech & Bio-informatique
- **Modèle économique :** B2B
- **Cible :** Laboratoires pharmaceutiques (découverte de médicaments, anticorps), centres de recherche en protéomique, hôpitaux (diagnostic de précision).
- **Le problème urgent :** Le séquençage de l'ADN est rapide et peu cher (génomique), mais l'ADN n'est que le plan. Ce sont les protéines (protéomique) qui exécutent les fonctions biologiques et causent les maladies. Actuellement, le séquençage des protéines se fait par spectrométrie de masse, une technique lente, chère, qui demande des échantillons massifs et détruit l'information structurelle. Il n'existe pas de séquenceur de protéines "single-molecule" à haut débit.
- **L'approche technique :** Séquençage direct des protéines par passage à travers des nanopores biologiques ou solides (silicium), lus par des capteurs de courant électrique quantique. Un moteur IA (Transformers/RNN) décode en temps réel le signal électrique perturbé par les acides aminés, y compris les modifications post-traductionnelles (PTM), molécule par molécule.
- **Pourquoi une solution générique/SaaS classique échoue :** C'est un problème intriqué de nanotechnologie matérielle (créer des pores de la taille d'un acide aminé), de chimie (déplier et tirer la protéine dans le pore) et de traitement du signal de très bas niveau (décoder le courant en temps réel). Le logiciel seul est inutile sans l'innovation wet-lab/hardware.
- **Risques majeurs & Dépendances :** Complexité extrême de la physique des polymères (les protéines ont 20 acides aminés de charges différentes, contre 4 nucléotides pour l'ADN), bruit électrique massif dans la lecture du signal, années de R&D requises avant un prototype viable.
