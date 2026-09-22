<!-- markdownlint-disable MD013 -->

# Candidat : Réseau Maillé PQC Inter-Satellites (Sat-to-Sat PQC Mesh)

- **Domaine principal :** Cybersécurité & Résilience / Deep Tech Infra
- **Modèle économique :** B2B / B2G
- **Cible :** Opérateurs de constellations de satellites (Starlink, Kuiper, OneWeb), agences spatiales (ESA, NASA), et forces armées (Space Force).
- **Le problème urgent :** Les liaisons de communication optiques (laser) inter-satellites (ISL) sont de plus en plus déployées pour créer un réseau maillé en orbite. Ces flux spatiaux transmettent l'intégralité du trafic internet et militaire non chiffré PQC. Une attaque de type "store now, decrypt later" (avec de futurs ordinateurs quantiques) via un satellite espion interceptant la lumière laser pourrait compromettre tout le trafic de la constellation.
- **L'approche technique :** Un module optique hardware plug-and-play pour satellites LEO (Low Earth Orbit) qui applique en temps réel un protocole d'encapsulation cryptographique post-quantique (ex: Crystals-Kyber) directement au niveau physique/photonique du lien laser, avant transmission atmosphérique ou inter-orbitale, sans ajouter de latence insoutenable au routage IP.
- **Pourquoi une solution générique/SaaS classique échoue :** L'environnement spatial (radiations cosmiques causant des bit-flips, variations extrêmes de température, contraintes SWaP - Size, Weight, and Power) détruit les routeurs ou serveurs terrestres standards. Le module nécessite une conception ASIC rad-hardened (durcie contre les radiations) spécifique.
- **Risques majeurs & Dépendances :** Coût très élevé du prototypage spatial et des tests en orbite (In-Orbit Demonstration), cycle de vente extrêmement long (B2G/Defense) avec des exigences de certification de sécurité drastiques.
