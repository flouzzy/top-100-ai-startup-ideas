<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Semiconductor Acoustic Microscopy

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B
- **Cible :** Fonderies de puces (TSMC, Intel), concepteurs fabless (Nvidia, AMD), fournisseurs de défense, et data centers critiques.
- **Le problème urgent :** L'insertion de trojans matériels (hardware trojans) ou de puces contrefaites dans la supply chain de semi-conducteurs. Les méthodes d'inspection optique ou par rayons X actuelles sont soit destructives, soit trop lentes pour examiner chaque puce, laissant les infrastructures critiques vulnérables à des kill-switches physiques indétectables au niveau logiciel.
- **L'approche technique :** L'utilisation de la microscopie acoustique à haute fréquence couplée à un modèle d'IA générative pour cartographier et analyser la signature acoustique 3D de l'intérieur d'une puce finie (sans l'ouvrir). Le modèle compare cette empreinte au "Golden Layout" d'origine pour détecter la moindre altération nanométrique.
- **Pourquoi une solution générique/SaaS classique échoue :** Un logiciel antivirus, un pare-feu ou un EDR ne peut pas détecter une porte dérobée gravée dans le silicium lui-même. La solution nécessite une combinaison profonde de matériel de détection physique spécialisé (capteurs ultrasoniques) et de modèles d'IA capables de traiter des ondes complexes.
- **Risques majeurs & Dépendances :** Difficulté de miniaturiser ou de rendre la vitesse de scan viable pour les lignes de production de masse, coût élevé de l'équipement matériel, difficulté d'obtenir les plans de conception ("Golden Layouts") propriétaires des puces auprès des fabricants.
