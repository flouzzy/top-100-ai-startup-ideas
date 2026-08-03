<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : PQC EV Charging Grid

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B
- **Cible :** Opérateurs de réseaux de recharge de véhicules électriques (CPO), gestionnaires de réseaux électriques (DSO/TSO) et constructeurs automobiles.
- **Le problème urgent :** L'infrastructure de recharge pour véhicules électriques (VE) est un vecteur d'attaque massif sur le réseau électrique. Avec l'avènement imminent de l'informatique quantique, les protocoles cryptographiques actuels sécurisant les communications véhicule-borne-réseau (V2G/Plug&Charge) seront obsolètes, risquant des blackouts systémiques par manipulation coordonnée de la charge.
- **L'approche technique :** Implémentation d'une couche réseau Zero-Trust basée sur la cryptographie post-quantique (PQC - algorithmes résistants aux ordinateurs quantiques, ex: réseaux euclidiens) spécialement optimisée pour les systèmes embarqués (bornes de recharge et contrôleurs VE) ayant des contraintes de calcul et de bande passante strictes.
- **Pourquoi une solution générique/SaaS classique échoue :** Les solutions VPN ou pare-feu standards ne protègent pas contre la menace quantique (Harvest Now, Decrypt Later) et l'intégration PQC nécessite une ingénierie de bas niveau pour fonctionner sur les microcontrôleurs (MCU) spécifiques à l'industrie automobile et de l'énergie.
- **Risques majeurs & Dépendances :** Standardisation lente des protocoles industriels (ISO 15118), nécessité de mettre à jour physiquement le matériel existant, et compatibilité avec les exigences de temps réel strict du réseau électrique.
