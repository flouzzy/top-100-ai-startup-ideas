<!-- markdownlint-disable MD013 -->
# Candidat : MedShield PQC

* **Domaine principal :** Cybersécurité & Résilience
* **Modèle économique :** B2B
* **Cible :** Fabricants de dispositifs médicaux implantables actifs (pacemakers, pompes à insuline, neurostimulateurs) comme Medtronic, Abbott, Boston Scientific.
* **Le problème urgent :** Avec l'avènement imminent de l'informatique quantique (Q-Day), les algorithmes cryptographiques asymétriques actuels (RSA, ECC) protégeant les communications télémétriques des implants médicaux deviendront obsolètes. Une faille permettrait des attaques fatales (altération du rythme cardiaque, surdose d'insuline). Le remplacement matériel post-implantation étant impossible, il faut une solution logicielle ultra-légère.
* **L'approche technique :** Implémentation d'une bibliothèque cryptographique Post-Quantique (PQC) conçue spécifiquement pour des environnements extrêmement contraints (Low-Power, Low-Memory). L'approche repose sur des mathématiques basées sur les réseaux (Lattice-based cryptography) optimisées en assembleur pour les microcontrôleurs embarqués des implants, permettant des mises à jour OTA (Over-The-Air) cryptographiquement sûres sans épuiser la batterie.
* **Pourquoi une solution générique/SaaS classique échoue :** Les bibliothèques PQC standards (comme celles du NIST) sont trop lourdes en termes d'empreinte mémoire et de consommation énergétique pour fonctionner sur l'architecture minimale d'un pacemaker. Un SaaS cloud est inutile : le calcul cryptographique doit se faire en local, sur la puce de l'implant, avec une consommation mesurée en micro-watts.
* **Risques majeurs & Dépendances :** Certification très lourde de la FDA/MDR européenne (dispositifs de classe III), risque vital en cas de bug de l'implémentation (responsabilité civile colossale), contraintes matérielles extrêmes limitant le choix des algorithmes mathématiques viables.
