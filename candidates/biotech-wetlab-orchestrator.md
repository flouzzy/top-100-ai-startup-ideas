<!-- markdownlint-disable MD013 -->
# Candidat : BiotechWetlabOrchestrator

* **Domaine principal :** Biotech & Bio-informatique
* **Modèle économique :** B2B
* **Cible :** Startups de biologie de synthèse, CROs (Contract Research Organizations), départements R&D de grands groupes pharmaceutiques.
* **Le problème urgent :** L'automatisation des laboratoires humides (wet-labs) est bloquée par l'incompatibilité des API et des standards entre différents équipements (robots de pipetage, spectromètres, incubateurs). La conception expérimentale (Design of Experiments - DoE) par l'IA ne peut pas se traduire directement en commandes d'exécution physique fiables, créant un goulot d'étranglement majeur.
* **L'approche technique :** Création d'une plateforme d'orchestration (OS) agnostique au matériel avec un compilateur traduisant les expériences biologiques conçues par IA (protocoles haut niveau) en instructions machine standardisées (bas niveau) pour n'importe quel robot de laboratoire. Un système de gestion d'agents autonomes surveille et corrige les erreurs de manipulation en temps réel.
* **Pourquoi une solution générique/SaaS classique échoue :** Les LIMS (Laboratory Information Management Systems) actuels sont passifs (gestion documentaire). Une solution d'orchestration wet-lab nécessite le développement de drivers spécifiques pour du matériel de laboratoire fermé, la gestion des variables physiques (température, volumes microscopiques) et un feedback loop en temps réel pour l'IA, s'apparentant à un système d'exploitation industriel de pointe.
* **Risques majeurs & Dépendances :** Refus des fabricants d'équipements de laboratoire d'ouvrir leurs API (vendor lock-in), complexité de la standardisation des protocoles biologiques, marge d'erreur tolérée quasi nulle dans les expériences critiques.
