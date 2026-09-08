<!-- markdownlint-disable MD013 -->
# Candidat : Exoskeleton Myoelectric Decoder

- **Domaine principal :** Robotique & Systèmes embarqués
- **Modèle économique :** B2B (Licensing Software & Edge AI)
- **Cible :** Fabricants d'exosquelettes industriels et médicaux, entreprises de prothèses robotiques
- **Le problème urgent :** Le contrôle des prothèses et exosquelettes via les signaux musculaires de surface (EMG) est lent, erratique et nécessite une recalibration constante liée à la sueur ou la fatigue musculaire. Cela crée un rejet massif de la technologie par les utilisateurs (friction d'adoption).
- **L'approche technique :** Un modèle d'IA "on-device" (Edge AI) ultra-léger, entraîné sur des données biométriques massives, capable de décoder l'intention motrice humaine (les signaux myoélectriques bruités) en temps réel (< 20 ms), sans recalibration. L'IA prédit le mouvement avant même que le muscle ne se contracte complètement.
- **Pourquoi une solution générique/SaaS classique échoue :** Il faut une inférence à latence ultra-faible fonctionnant sur des microcontrôleurs embarqués à faible consommation d'énergie (sans accès Cloud). Une API Cloud introduirait un lag inacceptable et dangereux pour le mouvement physique.
- **Risques majeurs & Dépendances :** Collecte d'un jeu de données diversifié de signaux EMG (différents types de corps, âges, conditions). Le verrou matériel : nécessité de s'intégrer avec les capteurs électrodes propriétaires des différents constructeurs hardware.
