<!-- markdownlint-disable MD013 -->
# Candidat : Hardware Trojan Scanner

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B
- **Cible :** Fabricants de semi-conducteurs, armée, aérospatial, opérateurs de datacenters cloud
- **Le problème urgent :** Avec la chaîne d'approvisionnement globale des puces (fabriquées souvent à l'étranger), le risque d'insertion de "Hardware Trojans" (portes dérobées physiques ajoutées au niveau du silicium pour provoquer des pannes ou fuir des données) est massif et indétectable par la sécurité logicielle.
- **L'approche technique :** Utilisation de l'IA (Computer Vision avancée et Graph Neural Networks) pour comparer les plans CAO d'origine (GDSII) avec des images au microscope électronique à balayage (SEM) des puces après fabrication, afin de détecter des altérations de l'ordre du nanomètre dans la fonderie.
- **Pourquoi une solution générique/SaaS classique échoue :** C'est un problème d'inspection de milliards de transistors physiques. Une vérification manuelle ou par simple algorithme heuristique est mathématiquement impossible en temps raisonnable vu la densité des puces modernes (5nm et moins).
- **Risques majeurs & Dépendances :** Besoin d'accéder à des microscopes électroniques hors de prix. Secret industriel extrême rendant l'accès aux designs CAO (IP) très difficile pour entraîner les modèles. Vente uniquement possible si certifié par des agences gouvernementales.
