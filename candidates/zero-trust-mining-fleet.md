<!-- markdownlint-disable MD013 -->

# Candidat : Zero Trust Mining Fleet

- **Domaine principal :** Cybersécurité
- **Modèle économique :** B2B
- **Cible :** Les conglomérats miniers mondiaux (Rio Tinto, BHP) et les opérateurs d'infrastructures lourdes autonomes (ports, agriculture de précision).
- **Le problème urgent :** Les flottes de camions autonomes (haul trucks) massives de 400 tonnes sont des réseaux IoT géants sur roues. Un hack de ces véhicules ou de leurs systèmes de gestion de flotte (FMS) peut causer des destructions matérielles massives, des arrêts de production coûtant des millions par heure, voire des pertes humaines.
- **L'approche technique :** Un OS de communication V2X (Vehicle-to-Everything) cryptographiquement scellé au niveau matériel. Il implémente un Zero-Trust décentralisé : chaque commande de freinage, de direction ou de routing nécessite un consensus cryptographique local entre les nœuds du véhicule et l'infrastructure de la mine, rejetant instantanément les injections externes.
- **Pourquoi une solution générique/SaaS classique échoue :** Un pare-feu IT classique ne protège pas contre une compromission du réseau OT (Operation Technology) interne, et l'authentification cloud introduit une latence inacceptable pour des véhicules autonomes nécessitant des temps de réaction en millisecondes.
- **Risques majeurs & Dépendances :** Adoption lente due à l'aversion au risque des industriels miniers, difficulté d'intégration avec les systèmes OEM existants fermés (Caterpillar, Komatsu), et besoin d'une résilience absolue (uptime 99.999%).
