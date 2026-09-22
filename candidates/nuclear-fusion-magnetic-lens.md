<!-- markdownlint-disable MD013 -->

# Candidat : Lentille Magnétique pour Fusion Nucléaire (Nuclear Fusion Magnetic Lens)

- **Domaine principal :** ClimateTech & Énergie / Deep Tech Infra
- **Modèle économique :** B2B
- **Cible :** Startups de fusion nucléaire privées (Commonwealth Fusion Systems, Helion) et grands projets gouvernementaux (ITER).
- **Le problème urgent :** Le confinement du plasma dans un Tokamak à 100 millions de degrés nécessite des électroaimants supraconducteurs colossaux. Même avec des aimants HTS (High-Temperature Superconductors), les instabilités magnétiques du plasma (disruptions) causent la perte de la réaction de fusion ou détruisent la paroi interne du réacteur, bloquant l'atteinte du seuil de rentabilité énergétique (Q>1) continu.
- **L'approche technique :** Une "lentille magnétique" active pilotée par un agent IA de renforcement (Reinforcement Learning) qui contrôle un réseau ultra-rapide de bobines d'induction secondaires entourant la chambre. Elle prédit (World Model) et corrige les turbulences magnétiques du plasma à la microseconde, agissant comme un stabilisateur dynamique actif (active noise cancellation pour le plasma).
- **Pourquoi une solution générique/SaaS classique échoue :** L'inférence du modèle d'IA doit tourner localement (pas de cloud possible à cause de la latence) et piloter directement du hardware électromagnétique extrême dans un environnement hautement radiatif.
- **Risques majeurs & Dépendances :** Dépendance totale à l'avancement global de la filière fusion (si aucun réacteur n'est commercialisé, pas de clients), et besoin d'une résilience matérielle extrême contre le bombardement de neutrons rapides du plasma.
