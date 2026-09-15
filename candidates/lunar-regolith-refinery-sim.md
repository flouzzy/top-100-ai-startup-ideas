<!-- markdownlint-disable MD013 -->

# Candidat : Lunar Regolith Refinery Sim

- **Domaine principal :** Deep Tech Infra
- **Modèle économique :** B2B
- **Cible :** Agences spatiales (NASA, ESA), startups minières spatiales, entreprises de construction extra-terrestre
- **Le problème urgent :** L'extraction de minéraux et d'oxygène à partir du régolithe lunaire est essentielle pour l'exploration spatiale à long terme (ISRU - In-Situ Resource Utilization), mais les tests physiques coûtent des milliards (lancement de prototypes) et échouent souvent à cause du comportement imprévu de la poussière lunaire abrasive dans le vide et en faible gravité.
- **L'approche technique :** Un moteur de physique granulaire multi-échelles (Discrete Element Method - DEM) couplé à des modèles thermochimiques fonctionnant sur GPU. Il simule exactement comment le régolithe va fondre, s'agglomérer ou se fracturer sous l'effet de lasers ou de réactions d'électrolyse dans les conditions lunaires.
- **Pourquoi une solution générique/SaaS classique échoue :** Les moteurs de jeu physique (Unity, Unreal) font de la physique approchée. Il faut ici une physique d'ingénierie absolue (calculée particule par particule) couplée à des équations d'état thermodynamiques qui n'existent pas dans les outils CAO standards.
- **Risques majeurs & Dépendances :** Marché de niche extrêmement restreint à court terme (faible TAM actuel). Nécessite des données expérimentales limitées (échantillons d'Apollo) pour valider le modèle physique, risque technologique de surapprentissage des modèles sur des données terrestres.
