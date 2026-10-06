<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Abyssal Swarm Autonomy

* **Domaine principal :** Robotique & Systèmes embarqués
* **Modèle économique :** B2B
* **Cible :** Sociétés d'exploration minière sous-marine, Organismes de recherche océanographique, Défense (Guerre navale).
* **Le problème urgent :** L'exploration et l'exploitation des nodules polymétalliques (terres rares cruciales pour la transition énergétique) dans les plaines abyssales sont impossibles avec les robots câblés (ROV) actuels ou les grands AUV solitaires, limités par la communication et le manque de conscience spatiale adaptative.
* **L'approche technique :** Un système d'exploitation pour essaims de micro-AUVs (Autonomous Underwater Vehicles) communiquant par ondes acoustiques et modems optiques. Ils partagent une carte bathymétrique locale en temps réel et coordonnent leurs actions de prélèvement sans endommager l'écosystème fragile environnant, sans GPS ni lien direct avec la surface.
* **Pourquoi une solution générique/SaaS classique échoue :** La communication sous l'eau est caractérisée par une bande passante extrêmement faible, une latence élevée et des interférences multipath. Les algorithmes d'essaim cloud-based ou les agents IA gourmands en données sont inutiles ici. Tout doit tourner en Edge sur des processeurs à très basse consommation.
* **Risques majeurs & Dépendances :** Pression extrême (défaillances mécaniques fréquentes), forte opposition environnementale et incertitude réglementaire internationale (Autorité internationale des fonds marins), perte de matériel coûteuse.
