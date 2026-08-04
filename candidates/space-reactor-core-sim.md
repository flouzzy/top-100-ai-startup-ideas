<!-- markdownlint-disable MD013 -->

# Candidat : Space Reactor Core Sim

- **Domaine principal :** Deep Tech & Infra (Spatial)
- **Modèle économique :** B2G / B2B
- **Cible :** Agences spatiales (NASA, ESA, CNSA), startups du New Space visant l'exploitation minière lunaire ou la propulsion vers Mars, constructeurs de petits réacteurs modulaires (SMR).
- **Le problème urgent :** L'exploration spatiale lointaine et les bases lunaires/martiennes nécessitent une énergie dense et continue que le solaire ne peut fournir. Les micro-réacteurs nucléaires spatiaux sont la seule solution, mais on ne peut pas les tester facilement sur Terre de manière réaliste (à cause de la gravité, du vide et des radiations terrestres différentes), ce qui bloque l'obtention des licences de vol.
- **L'approche technique :** Un moteur de simulation multiphysique spatio-temporelle (World Model des rayonnements et de la thermohydraulique en microgravité) couplé à des algorithmes de transport de neutrons de Monte Carlo accélérés par GPU pour certifier numériquement le comportement du réacteur, les boucles d'évacuation de la chaleur (caloducs) et la dégradation des matériaux en conditions spatiales.
- **Pourquoi une solution générique/SaaS classique échoue :** Les codes de simulation nucléaire civils terrestres (OpenMC, MCNP) supposent la gravité terrestre pour le transfert de chaleur (convection naturelle). Il faut recoder fondamentalement les lois physiques pour la microgravité et le vide spatial, avec une certification de niveau agence spatiale.
- **Risques majeurs & Dépendances :** Réglementation ITAR/export control ultra-stricte limitant le marché adressable ; besoin d'une validation expérimentale par de rares expériences en tour d'impesanteur ou en orbite pour calibrer le modèle ; lenteur de l'adoption institutionnelle.
