<!-- markdownlint-disable MD013 -->

# Candidat : Geothermal Fracture Twin

- **Domaine principal :** ClimateTech & Énergie
- **Modèle économique :** B2B
- **Cible :** Exploitants de géothermie profonde (EGS - Enhanced Geothermal Systems), compagnies pétrolières en transition énergétique, utilities.
- **Le problème urgent :** La géothermie de nouvelle génération (EGS) nécessite de fracturer la roche en profondeur pour créer des réservoirs perméables là où l'eau ne circule pas naturellement. Un mauvais calcul entraîne des séismes induits coûteux et des puits secs (des millions de dollars perdus), bloquant le déploiement de cette énergie bas-carbone continue.
- **L'approche technique :** Un jumeau numérique géomécanique (World Model du sous-sol) combinant l'inversion de données sismiques en temps réel, la modélisation poromécanique par réseaux de neurones informés par la physique (PINNs), et la simulation de la propagation des fractures pour guider le forage et l'injection d'eau avec une précision sub-métrique.
- **Pourquoi une solution générique/SaaS classique échoue :** L'espace sous-terrain est par nature invisible et incertain. Les solveurs géologiques actuels (Petrel) sont lents et déterministes. Il faut modéliser la physique complexe du couplage thermo-hydro-mécanique (THM) sous haute pression et haute température.
- **Risques majeurs & Dépendances :** Manque de données d'entraînement open source haute résolution sur la croûte terrestre profonde ; responsabilité juridique en cas de sismicité induite non prévue par le modèle ; intégration avec le matériel de forage (capteurs fond de trou).
