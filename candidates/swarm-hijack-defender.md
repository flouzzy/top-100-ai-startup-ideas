<!-- markdownlint-disable MD013 -->

# Candidat : Swarm Hijack Defender

- **Domaine principal :** Cybersécurité & Résilience / Robotique
- **Modèle économique :** B2B / B2G
- **Cible :** Armées, opérateurs logistiques de drones (Amazon, Zipline), services de secours.
- **Le problème urgent :** Avec le déploiement massif de flottes de drones autonomes (swarms) communicant entre eux, une nouvelle menace apparaît : la subversion de l'essaim. Un attaquant injectant un faux nœud ou des données erronées (spoofing GPS/RF) peut provoquer des réactions en chaîne (brouillage de la topologie, crashs collectifs, détournement de la mission).
- **L'approche technique :** Un protocole de consensus décentralisé byzantin ultra-léger (embarqué sur les microcontrôleurs des drones) couplé à une analyse comportementale en temps réel (machine learning). Chaque drone surveille la cinématique et les communications de ses voisins (Swarm Immunology). Si un nœud dévie physiquement de l'intention collective ou émet des vecteurs aberrants, il est cryptographiquement isolé (quarantaine) par le reste de l'essaim.
- **Pourquoi une solution générique/SaaS classique échoue :** Les solutions de cybersécurité cloud ont trop de latence. Dans un essaim, les décisions de rejet doivent se prendre en millisecondes, sans connexion centrale (edge-natif), en s'appuyant sur les lois de la physique (vérification que le message est cohérent avec la position physique du drone émetteur).
- **Risques majeurs & Dépendances :** Faux positifs conduisant l'essaim à se fragmenter inutilement ; consommation énergétique des calculs cryptographiques et de l'IA sur la batterie limitée du drone.
