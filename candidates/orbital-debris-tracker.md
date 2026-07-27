<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Orbital Debris Predictive Network

- **Domaine principal :** Deep Tech & Infra / Robotique
- **Modèle économique :** B2B
- **Cible :** Opérateurs de constellations de satellites (SpaceX, Amazon Kuiper), agences spatiales gouvernementales (NASA, ESA), et assureurs spatiaux.
- **Le problème urgent :** Le syndrome de Kessler devient une réalité. Avec des dizaines de milliers de nouveaux satellites en LEO (Low Earth Orbit), la probabilité de collisions catastrophiques augmentent de façon exponentielle, menaçant des milliards d'infrastructures et l'accès même à l'espace. Le suivi actuel basé sur les radars au sol est trop lent, imprécis, et ne suit que les gros débris.
- **L'approche technique :** Un réseau de capteurs optiques et LiDAR embarqués directement en tant que "hosted payloads" sur des satellites commerciaux, couplé à une IA de perception spatiale temps réel à l'edge pour détecter, caractériser et cataloguer de manière autonome les micro-débris (<10cm) non tracés. Les données alimentent un World Model orbital pour l'évitement automatisé.
- **Pourquoi une solution générique/SaaS classique échoue :** Les bases de données existantes (comme celle de l'US Space Command) sont des systèmes fermés et basés sur des architectures monolithiques incapables de traiter la fusion de capteurs en orbite à la milliseconde près. Les modèles de trajectoire classiques divergent trop vite sans données visuelles locales.
- **Risques majeurs & Dépendances :** Coût exorbitant de lancement des charges utiles. Nécessité d'obtenir des partenariats avec les opérateurs de satellites pour héberger les capteurs. Résilience du hardware au rayonnement cosmique.
