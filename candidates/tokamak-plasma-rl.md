<!-- markdownlint-disable MD013 -->

# Candidat : PlasmaGuard RL

- **Domaine principal :** ClimateTech (Fusion) / Deep Tech
- **Modèle économique :** B2B (Partenariat R&D / Licensing)
- **Cible :** Startups de fusion nucléaire (Commonwealth Fusion Systems, Tokamak Energy), instituts de recherche (ITER).
- **Le problème urgent :** La stabilisation du plasma dans un réacteur de fusion (Tokamak ou Stellarator) est extrêmement complexe. Les instabilités magnétiques détruisent le confinement du plasma en quelques millisecondes, empêchant d'atteindre une fusion nette positive (Q>1) de manière soutenue.
- **L'approche technique :** Contrôle actif par Apprentissage par Renforcement Profond (Deep RL). L'IA est entraînée dans des simulateurs magnétohydrodynamiques (MHD) ultra-précis pour ajuster les bobines magnétiques à des fréquences de plusieurs kilohertz afin de réprimer les instabilités dès leur formation.
- **Pourquoi une solution générique/SaaS classique échoue :** Les contrôleurs PID classiques de l'industrie sont trop lents et rigides face à la nature chaotique et non-linéaire du plasma. Un logiciel SaaS n'a pas les boucles de rétroaction à ultra-faible latence (micro-secondes) requises pour interagir avec le matériel.
- **Risques majeurs & Dépendances :** Le "Sim-to-Real gap" (l'écart entre la simulation MHD et la réalité physique du réacteur) peut rendre l'agent RL inutile ou dangereux s'il n'est pas parfaitement calibré. Dépendance totale à l'avancement matériel de l'industrie de la fusion.
