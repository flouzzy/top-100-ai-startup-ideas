<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Smart Dust Agricultural Mesh

- **Domaine principal :** Deep Tech & Infra
- **Modèle économique :** B2B
- **Cible :** Grandes exploitations agricoles commerciales (agro-industrie), coopératives, producteurs de cultures à très haute valeur ajoutée (viticulture, serres industrielles).
- **Le problème urgent :** L'agriculture de précision souffre d'un manque de données micro-locales. Les satellites ou les drones donnent une macro-vision, mais ne peuvent pas détecter le stress hydrique ou l'apparition de mycélium fongique au niveau d'une plante individuelle. Le surdosage préventif de pesticides et d'eau coûte des milliards et détruit les sols de manière irréversible.
- **L'approche technique :** Le déploiement par drone de "Smart Dust" (poussière intelligente) : des capteurs MEMS (Micro-Electro-Mechanical Systems) biodégradables de la taille d'un grain de sable. Ce hardware extrême intègre des capteurs chimiques et d'humidité. Le système comprend un protocole de communication RF ultra-basse consommation (backscatter) créant un réseau maillé (mesh network) éphémère qui envoie la télémétrie granulaire au centimètre carré vers un edge-computer.
- **Pourquoi une solution générique/SaaS classique échoue :** L'innovation est purement matérielle (développement de SoC biodégradables) et au niveau de la couche physique des réseaux sans fil. Les logiciels d'agriculture prédictive basés sur le cloud ne peuvent pas opérer sans ces données intimes du terrain, qui n'ont jamais été captées à cette échelle.
- **Risques majeurs & Dépendances :** La fabrication de semi-conducteurs biodégradables de cette taille est à la limite de la recherche fondamentale (TRL bas), risque réglementaire sur l'éparpillement de micro-électronique dans les cultures alimentaires, durée de vie des batteries/récupération d'énergie, fiabilité des transmissions RF à travers la canopée des cultures.
