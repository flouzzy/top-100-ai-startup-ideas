<!-- markdownlint-disable MD013 -->

# Candidat : Furtivité Acoustique Active pour VTOL (VTOL Active Acoustic Stealth)

- **Domaine principal :** Robotique & Systèmes embarqués / Deep Tech Infra
- **Modèle économique :** B2B
- **Cible :** Constructeurs de drones de livraison lourds, de taxis volants (eVTOL) comme Joby ou Lilium, et acteurs de la défense urbaine.
- **Le problème urgent :** Les drones et eVTOLs sont conçus pour fonctionner en milieu urbain, mais leurs rotors génèrent une pollution sonore massive (haute fréquence et basses vibrations) qui empêche l'acceptation sociale, l'approbation réglementaire des vols urbains massifs, et les rend extrêmement détectables pour les cas d'usage défense.
- **L'approche technique :** Un système d'annulation active du bruit spatialisé (Active Noise Control) appliqué en temps réel. Des micro-actionneurs piézoélectriques intégrés aux pales des rotors modifient dynamiquement leur profil aérodynamique (morphing wing) tandis que des haut-parleurs vectoriels projettent des ondes sonores destructrices (anti-bruit) parfaitement alignées avec la phase acoustique du moteur, créant un "cône de silence" sous l'appareil.
- **Pourquoi une solution générique/SaaS classique échoue :** C'est un défi d'ingénierie cyber-physique temps réel extrême. Le logiciel doit piloter du hardware piézoélectrique à des fréquences de plusieurs kHz avec une latence quasi nulle, nécessitant des contrôleurs embarqués spécifiques (Edge AI) et de la science des matériaux.
- **Risques majeurs & Dépendances :** Fatigue mécanique des pales à cause du morphing piézoélectrique continu, ajout de poids pénalisant l'autonomie (Payload/Range penalty), et complexité de certification aéronautique.
