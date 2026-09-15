<!-- markdownlint-disable MD013 -->

# Candidat : Neuro-symbolic Alloy Forge

- **Domaine principal :** Deep Tech Infra / World Models
- **Modèle économique :** B2B
- **Cible :** Aéronautique, aérospatial, constructeurs de moteurs (Rolls-Royce, Safran), et métallurgie de pointe.
- **Le problème urgent :** Découvrir de nouveaux "Superalliages" (High-Entropy Alloys - HEA) capables de résister à la corrosion, aux températures extrêmes (turbines à hydrogène, hypersonique) tout en restant légers prend des décennies de tests empiriques d'essais-erreurs en fonderie. L'espace chimique combinatoire des alliages métalliques est infiniment vaste.
- **L'approche technique :** Une plateforme de découverte de matériaux combinant l'IA générative (GNN - Graph Neural Networks) avec des solveurs symboliques de thermodynamique (CALPHAD). L'IA propose des microstructures d'alliages atypiques à 5 ou 6 éléments, et le moteur symbolique valide instantanément leur stabilité de phase, leurs propriétés mécaniques (module d'élasticité) et leur résistance à l'oxydation, avant toute coulée physique.
- **Pourquoi une solution générique/SaaS classique échoue :** L'IA générative pure (comme AlphaFold) hallucine souvent des métaux impossibles à fabriquer (qui se séparent en plusieurs phases au refroidissement). Il est impératif d'ancrer le réseau de neurones dans les lois fondamentales de la thermodynamique métallurgique symbolique pour garantir la viabilité physique des alliages proposés.
- **Risques majeurs & Dépendances :** Besoin de laboratoires partenaires (fonderies robotisées) pour réaliser les "wet-lab" métallurgiques et valider les prédictions, bouclant ainsi la boucle d'apprentissage. Le manque de bases de données publiques propres sur les échecs de coulée biaise les modèles d'IA initiaux.
