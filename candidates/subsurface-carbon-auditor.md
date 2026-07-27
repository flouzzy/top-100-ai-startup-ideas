<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Subsurface Carbon Auditor

- **Domaine principal :** ClimateTech & Énergie
- **Modèle économique :** B2B
- **Cible :** Opérateurs de capture et stockage de carbone (CCS), acteurs de l'industrie lourde (ciment, acier), fonds d'investissement ESG, certificateurs carbone.
- **Le problème urgent :** L'industrie de la séquestration géologique du carbone (enfouir le CO2 sous terre) est entachée d'incertitudes quantitatives. Une fois injecté dans des réservoirs salins ou géologiques profonds, il est extrêmement difficile de prouver (auditabilité) que le carbone reste bien confiné, ne fuit pas, et se minéralise comme prévu au fil du temps. Sans cette preuve indiscutable, les crédits carbone générés perdent leur valeur (greenwashing).
- **L'approche technique :** Une plateforme de jumeaux géophysiques (Geophysical World Models) couplant des réseaux de capteurs sismiques distribués (géophones) et l'analyse gravimétrique haute précision. Elle utilise l'inversion sismique (Full Waveform Inversion) accélérée par GPU/IA pour "scanner" le sous-sol en 4D, quantifiant le volume exact de panaches de CO2 et détectant les micro-fuites potentielles, rendant le stockage géologique incontestablement auditable.
- **Pourquoi une solution générique/SaaS classique échoue :** La modélisation de la dynamique des fluides poreux (écoulement multiphasique) dans des roches hétérogènes est un défi de physique computationnelle lourd, nécessitant de traiter des pétaoctets de données sismiques brutes. Aucune interface SaaS web classique ou modèle d'IA textuelle ne peut traiter ce signal physique massif sans une architecture de calcul haute performance (HPC) dédiée à la géophysique.
- **Risques majeurs & Dépendances :** Coût très élevé du déploiement des capteurs géophysiques sur le terrain (capex), incertitude réglementaire concernant les standards de monitoring du CCS, acceptabilité sociale des projets d'enfouissement massif.
