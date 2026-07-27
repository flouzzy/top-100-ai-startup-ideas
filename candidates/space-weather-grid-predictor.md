<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Space Weather Grid Predictor

- **Domaine principal :** ClimateTech & Énergie / World Models
- **Modèle économique :** B2B / B2G
- **Cible :** Opérateurs de réseaux de transmission électrique (TSO) nationaux, gestionnaires de parcs solaires à grande échelle et compagnies d'assurance d'infrastructures.
- **Le problème urgent :** Les éjections de masse coronale (CME) et les tempêtes géomagnétiques induisent des Courants Géomagnétiquement Induits (GIC) directement dans les réseaux électriques terrestres (haute tension). Ces courants continus saturent les transformateurs géants, provoquant des surchauffes explosives, des pannes en cascade (blackouts) et la destruction d'équipements valant des millions, avec des délais de remplacement de plusieurs années (supply chain très contrainte pour les transformateurs THT).
- **L'approche technique :** Un modèle génératif spatio-temporel (Neural Earth Simulator) combinant les flux de données satellitaires héliophysiques en temps réel (DSCOVR, SOHO) avec la modélisation géophysique profonde 3D de la résistivité du manteau terrestre local et la topologie du réseau électrique. Le système prédit l'intensité exacte du GIC par transformateur individuel avec 24 à 48 heures d'avance, recommandant des réacheminements de charge ou des déconnexions préventives.
- **Pourquoi une solution générique/SaaS classique échoue :** Les prévisions spatiales de la NOAA sont de macro-niveau (zones planétaires). Pour agir, un TSO a besoin d'une résolution physique à l'échelle du transformateur individuel. Il faut coupler l'électromagnétisme magnétohydrodynamique (MHD) de l'ionosphère avec les modèles de flux de puissance CA/CC terrestres.
- **Risques majeurs & Dépendances :** La rareté des événements extrêmes (type Événement de Carrington) rend difficile l'entraînement et la validation complète du modèle sans overfitting sur les données des petites tempêtes. Réticence des TSO à automatiser les coupures de réseau sur la base d'une prédiction d'IA.
