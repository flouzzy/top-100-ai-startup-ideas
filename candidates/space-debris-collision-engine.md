<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Orbital Kinetics Engine

* **Domaine principal :** World Models & Simulation physique
* **Modèle économique :** B2B / B2G
* **Cible :** Opérateurs de satellites LEO/GEO, Agences spatiales (ESA, NASA, Space Force), Assureurs spatiaux.
* **Le problème urgent :** Avec la multiplication des méga-constellations, le risque de syndrome de Kessler (réaction en chaîne de collisions de débris) devient critique. Les modèles actuels (SGP4) sont trop lents et imprécis pour gérer des centaines de milliers de conjonctions dynamiques en temps réel.
* **L'approche technique :** Un moteur de physique neuronale (Neural Physics Engine) qui utilise des Graph Neural Networks pour simuler les trajectoires de millions de débris spatiaux et de satellites actifs avec une précision métrique, intégrant les perturbations atmosphériques et la pression de radiation solaire en temps réel.
* **Pourquoi une solution générique/SaaS classique échoue :** Le calcul des orbites perturbées de N-corps est extrêmement lourd computationnellement. Un LLM n'a aucune notion de la mécanique céleste ni des équations différentielles nécessaires. C'est un problème de physique computationnelle nécessitant un modèle substitut (surrogate model) accéléré par IA.
* **Risques majeurs & Dépendances :** Accès aux données radars/optiques de suivi (souvent classifiées), fiabilité à 99.999% requise pour justifier une manœuvre d'évitement, concurrence des entités gouvernementales.
