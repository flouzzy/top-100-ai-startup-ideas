<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : GridSwarm V2G

- **Domaine principal :** IA & Agents autonomes / ClimateTech / Énergie
- **Modèle économique :** B2B2C / B2B (Revenue split sur l'arbitrage)
- **Cible :** Opérateurs de réseaux de transmission (RTE, National Grid), gestionnaires de flottes de véhicules électriques (EV), agrégateurs d'énergie.
- **Le problème urgent :** L'intégration massive des énergies renouvelables intermittentes (solaire/éolien) déstabilise la fréquence du réseau électrique (50/60 Hz). La solution est le Vehicle-to-Grid (V2G) utilisant les batteries des millions d'EV comme stockage distribué, mais coordonner les cycles de charge/décharge de millions de véhicules aléatoirement connectés, sans dégrader leurs batteries ni frustrer les utilisateurs, est un cauchemar d'optimisation stochastique à grande échelle.
- **L'approche technique :** Un essaim d'agents autonomes hiérarchisés (Multi-Agent Reinforcement Learning - MARL). Chaque véhicule possède un agent "local" qui optimise sa propre durée de vie de batterie et les besoins de mobilité de l'utilisateur. Ces agents négocient de manière asynchrone (via un protocole d'enchères léger) avec des agents "régionaux" pour offrir des services de régulation de fréquence au réseau en temps réel, garantissant la stabilité du grid sans point de défaillance central.
- **Pourquoi une solution générique/SaaS classique échoue :** Les solveurs d'optimisation linéaire traditionnels (MILP) ne scalent pas au-delà de quelques milliers de nœuds en temps réel. Une approche cloud centralisée souffre de latence et de vulnérabilité, alors que la régulation de fréquence exige des réactions en millisecondes et une architecture décentralisée.
- **Risques majeurs & Dépendances :** Hétérogénéité des protocoles de bornes de recharge et des constructeurs automobiles (manque de standardisation V2G bidirectionnelle). Acceptation par l'utilisateur final de laisser l'IA "décharger" sa voiture (garanties d'état de charge (SoC) requises).
