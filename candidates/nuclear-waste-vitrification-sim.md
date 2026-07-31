<!-- markdownlint-disable MD013 -->
# Candidat : VitriSim

* **Domaine principal :** World Models & Simulation physique
* **Modèle économique :** B2B / B2G
* **Cible :** Agences nationales de gestion des déchets radioactifs, exploitants de centrales nucléaires (EDF, Tepco) et sous-traitants en démantèlement.
* **Le problème urgent :** Le processus de vitrification des déchets nucléaires de haute activité (HA) est extrêmement complexe, coûteux et lent. Les erreurs de formulation ou de maîtrise des températures dans les fours à induction (entraînant des cristallisations parasites) coûtent des dizaines de millions d'euros par raté et allongent drastiquement les délais de sécurisation. L'impossibilité de tester physiquement à l'échelle sans générer des déchets supplémentaires rend l'optimisation itérative quasi impossible.
* **L'approche technique :** Création d'un jumeau numérique basé sur un Neural Physics Engine capable de modéliser les dynamiques magnéto-hydrodynamiques et thermodynamiques du verre en fusion (mélangé aux produits de fission) en temps réel. Le système combine des modèles de dynamique moléculaire multi-échelles avec un apprentissage profond informé par la physique (PINNs) pour prédire la stabilité de la matrice vitreuse selon des variables d'entrée fluctuantes.
* **Pourquoi une solution générique/SaaS classique échoue :** Un LLM ou un tableur ne peut pas résoudre les équations différentielles partielles de Navier-Stokes couplées aux effets magnétiques et chimiques à haute température. Il faut un moteur de simulation spécialisé, brevetable et entraîné sur des données historiques de vitrification hautement classifiées et propriétaires.
* **Risques majeurs & Dépendances :** Accès très restreint aux données d'entraînement industrielles réelles (secret industriel/défense), puissance de calcul requise (HPC pour l'inférence des modèles physiques), et temps de R&D très long nécessitant des doctorants en physique des matériaux et simulation numérique.
