<!-- markdownlint-disable MD013 -->
# Candidat : QuantumRFFingerprinting

* **Domaine principal :** Cybersécurité & Résilience (Hardware/Quantique)
* **Modèle économique :** B2B
* **Cible :** Défense, aérospatial, opérateurs d'infrastructures critiques (satellites, drones), télécommunications 5G/6G.
* **Le problème urgent :** L'usurpation (spoofing) de signaux radiofréquences et GPS menace de plus en plus les flottes de drones, la navigation maritime et les constellations de satellites. Les signatures cryptographiques classiques ne peuvent authentifier le matériel émetteur lui-même.
* **L'approche technique :** Utilisation de capteurs quantiques à centre NV (Azote-Lacune) dans le diamant pour analyser les variations infimes et uniques de la signature électromagnétique (bruit de phase, imperfections de l'oscillateur) de chaque émetteur radio. Création d'un système Zero-Trust physique, authentifiant l'origine matérielle des signaux en temps réel, impossible à cloner.
* **Pourquoi une solution générique/SaaS classique échoue :** La cryptographie logicielle peut être volée ou compromise (clés exfiltrées). Cette approche authentifie l'empreinte physique unique (PUF) des composants analogiques, nécessitant du matériel quantique ultra-sensible et des algorithmes de traitement du signal de pointe, hors de portée d'une solution 100% logicielle.
* **Risques majeurs & Dépendances :** Taille, poids et consommation (SWaP) du capteur quantique pour l'embarquer sur des petits drones, complexité du calibrage face au bruit ambiant, nécessité de matériel spécialisé très coûteux.
