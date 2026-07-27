<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Microfluidic Routing OS

- **Domaine principal :** Biotech & Robotique
- **Modèle économique :** B2B
- **Cible :** Startups de biologie synthétique (SynBio), laboratoires de tests cliniques haut débit, "Cloud Labs" (Ginkgo Bioworks, Emerald Cloud Lab).
- **Le problème urgent :** L'automatisation des "wet-labs" (laboratoires de chimie/biologie) est freinée par la tuyauterie. Les robots pipeteurs standards sont lents et sujets à la contamination croisée. Les puces microfluidiques offrent une automatisation massive à l'échelle du picolitre, mais elles sont hardcodées physiquement (un circuit de canaux statiques) ; changer d'expérience (protocole) nécessite de fabriquer une nouvelle puce de silicium ou de polymère.
- **L'approche technique :** Un "Operating System" pour l'ElectroWetting-On-Dielectric (EWOD) ou microfluidique numérique. Il s'agit d'un compilateur qui prend un protocole biologique écrit en haut niveau (Python/BioCoder) et calcule dynamiquement le routage des gouttelettes d'ADN, de réactifs et d'enzymes sur une grille de pixels électro-mouillables en temps réel. Il optimise les chemins pour éviter les collisions et la contamination.
- **Pourquoi une solution générique/SaaS classique échoue :** C'est un problème de routage FPGA (EDA - Electronic Design Automation), mais appliqué à la dynamique des fluides. Un SaaS classique ne peut pas gérer les contraintes physiques bas niveau (tension, mouillabilité de la surface, viscosité changeante d'une goutte de sang par rapport à de l'eau) requises pour faire bouger des liquides avec des champs électriques de manière fiable.
- **Risques majeurs & Dépendances :** La technologie matérielle sous-jacente (puces EWOD haute densité) est encore coûteuse à produire en masse. Nécessité d'une intégration parfaite entre le modèle physique du logiciel et les imperfections de fabrication du hardware.
