<!-- markdownlint-disable MD013 -->

# Candidat : Kessler Orbital Twin

- **Domaine principal :** World Models / Systèmes embarqués (Spatial)
- **Modèle économique :** B2B / B2G
- **Cible :** Opérateurs de constellations de satellites (SpaceX, Kuiper), agences spatiales (NASA, ESA), assureurs spatiaux.
- **Le problème urgent :** Le syndrome de Kessler : l'orbite basse terrestre (LEO) est de plus en plus saturée. Les collisions entre débris spatiaux et satellites génèrent des nuages incontrôlables, menaçant l'ensemble de l'économie spatiale et la connectivité mondiale.
- **L'approche technique :** Un "World Model" spatio-temporel temps réel ingérant des données radars, optiques et télémétriques pour simuler la cinématique de millions d'objets orbitaux. Il utilise des réseaux de neurones informés par la physique (PINNs) pour calculer les probabilités de conjonction avec des heures d'avance et ordonner des manœuvres d'évitement.
- **Pourquoi une solution générique/SaaS classique échoue :** Les calculs de mécanique céleste classique sont trop lents pour une mise à l'échelle sur 100 000 objets. Une IA classique sans contraintes physiques (lois de Kepler, traînée atmosphérique variable) hallucinerait les trajectoires.
- **Risques majeurs & Dépendances :** Dépendance critique à la qualité et la fréquence des données radar de l'US Space Command ou de fournisseurs privés (LeoLabs). Puissance de calcul HPC continue requise.
