<!-- markdownlint-disable MD013 -->
# Candidat : NeuroSpike Prosthetics

* **Domaine principal :** Robotique & Systèmes embarqués
* **Modèle économique :** B2B2C
* **Cible :** Fabricants de prothèses bioniques (Össur, Ottobock), centres de rééducation spécialisés, et amputés.
* **Le problème urgent :** Le contrôle des prothèses myoélectriques actuelles est lent, peu intuitif et très limité (souvent réduit à l'ouverture/fermeture basique de la main). Le cerveau envoie des signaux électromyographiques (EMG) complexes, mais le matériel classique n'est pas assez rapide ou sophistiqué pour décoder ces intentions motrices fines et fluides en temps réel. La latence induit une énorme fatigue cognitive chez le patient.
* **L'approche technique :** Intégration d'une architecture neuromorphique (Spiking Neural Networks - SNN) directement sur la puce embarquée de la prothèse. Contrairement aux réseaux de neurones classiques, les SNN imitent les décharges électriques du cerveau, traitant les signaux EMG multicanaux avec une latence quasi nulle (<5ms) et une consommation d'énergie infime. Cela permet un décodage "continu" et multifactoriel de l'intention de mouvement (bouger plusieurs doigts simultanément avec force variable).
* **Pourquoi une solution générique/SaaS classique échoue :** L'envoi des données dans le cloud pour traitement introduirait une latence inacceptable pour le mouvement en temps réel. Un processeur (CPU/GPU) classique embarqué viderait la batterie de la prothèse en quelques heures et chaufferait trop. Il faut un couplage spécifique entre capteurs hardware, puces neuromorphiques et algorithmes SNN bas niveau.
* **Risques majeurs & Dépendances :** Maturité actuelle des puces neuromorphiques (ex: Loihi d'Intel, Akida de BrainChip), complexité de la calibration personnalisée des algorithmes SNN pour chaque patient (le signal EMG de chaque moignon est unique), et barrières réglementaires médicales (marquage CE, FDA).
