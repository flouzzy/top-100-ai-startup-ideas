<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : InertialPulse Nav

* **Domaine principal :** Robotique / Cybersécurité
* **Modèle économique :** B2B / B2G
* **Cible :** Fabricants de drones (DJI, Skydio), armées, flottes de livraison autonome et opérateurs d'infrastructures critiques.
* **Le problème urgent :** La navigation des drones et systèmes autonomes dépend presque exclusivement du GPS/GNSS, qui est extrêmement vulnérable au brouillage (jamming) et à l'usurpation (spoofing), rendant les vols autonomes dangereux ou impossibles en zone de conflit ou en environnement urbain dense.
* **L'approche technique :** Système de navigation inertielle quantique miniaturisé (Quantum Inertial Measurement Unit - Q-IMU) couplé à de la vision par ordinateur par événements (Neuromorphic Vision). Permet une navigation de précision absolue sans aucun signal externe, résiliente par conception.
* **Pourquoi une solution générique/SaaS classique échoue :** C'est un défi purement matériel (physique atomique) couplé à du traitement du signal ultra-basse latence sur la plateforme embarquée, que le software seul ne peut résoudre.
* **Risques majeurs & Dépendances :** Défis d'ingénierie majeurs pour miniaturiser les capteurs quantiques (chambres à vide, lasers) au format SWaP-C (pour drone de quelques kilos), et coûts de production initiaux très élevés.
