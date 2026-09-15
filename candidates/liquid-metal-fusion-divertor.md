<!-- markdownlint-disable MD013 -->

# Candidat : Liquid Metal Divertor Sim

- **Domaine principal :** ClimateTech & Énergie / World Models
- **Modèle économique :** B2B
- **Cible :** Startups de fusion nucléaire (Commonwealth Fusion Systems, Tokamak Energy), instituts de recherche publics (ITER, DEMO).
- **Le problème urgent :** Dans un réacteur à fusion (Tokamak), le "divertor" est la pièce d'échappement qui reçoit les cendres thermiques du plasma. Il subit des flux de chaleur extrêmes (plus intenses qu'à la surface du soleil) qui détruisent les alliages de tungstène les plus solides en quelques mois. Sans divertor résistant, la fusion commerciale est impossible, et les matériaux solides semblent avoir atteint leurs limites physiques.
- **L'approche technique :** Un moteur de simulation magnétohydrodynamique (MHD) couplé à une IA prédictive pour concevoir des divertors à métaux liquides (ex: Lithium ou Étain fondu coulant sur une structure poreuse). Le jumeau numérique simule l'interaction complexe entre le métal fluide, le champ magnétique intense du tokamak et le plasma brûlant, permettant d'optimiser le débit et la capillarité pour empêcher l'évaporation du métal liquide.
- **Pourquoi une solution générique/SaaS classique échoue :** Les codes CFD traditionnels échouent à simuler le couplage intime de la mécanique des fluides en régime turbulent, de l'électromagnétisme (effets de force de Lorentz sur le métal conducteur) et des transferts thermiques extrêmes au sein d'une même matrice temporelle. C'est un pur problème de World Model physique ultra-spécialisé.
- **Risques majeurs & Dépendances :** Validation expérimentale extrêmement complexe, dépendant du temps de fonctionnement très rare et coûteux des tokamaks existants. La corrosion des structures sous-jacentes par le métal liquide reste un défi majeur non modélisable facilement.
