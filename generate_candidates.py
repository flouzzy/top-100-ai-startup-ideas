import os

candidates = [
    {
        "filename": "bio-os-synthetic.md",
        "title": "BioOS Synthetic",
        "domaine": "Biotech & Bio-informatique",
        "modele": "B2B",
        "cible": "Laboratoires pharmaceutiques et biotechs de phase pré-clinique (Directeurs R&D, Head of Synthetic Biology).",
        "probleme": "La conception de circuits génétiques pour les thérapies cellulaires (ex. CAR-T) nécessite des mois d'essais-erreurs in-vivo/in-vitro, coûtant des millions sans garantie que les cellules modifiées n'attaquent pas les tissus sains (toxicité off-target).",
        "approche": "Un \"compilateur\" de biologie synthétique couplé à un jumeau numérique cellulaire (World Model biologique) qui simule l'expression génique dynamique et les interactions protéiques avant toute synthèse en laboratoire.",
        "pourquoi_echec": "Un LLM ne comprend pas la cinétique biochimique spatio-temporelle ni les repliements protéiques en 3D dans le cytoplasme. Nécessite des modèles physiques prédictifs (physique statistique, thermodynamique) entraînés sur des données multi-omiques propriétaires.",
        "risques": "Accès aux données omiques massives de haute qualité, puissance de calcul GPU extrême (équivalent dynamique moléculaire), validation biologique en wet-lab incontournable pour prouver le modèle."
    },
    {
        "filename": "qkd-ot-network.md",
        "title": "QKD OT Guardian",
        "domaine": "Cybersécurité & Quantique",
        "modele": "B2B",
        "cible": "Opérateurs d'infrastructures critiques (réseaux électriques, centrales nucléaires, stations d'épuration) (CISO, OT Security Managers).",
        "probleme": "Les réseaux opérationnels (OT/ICS) utilisent des protocoles industriels legacy vulnérables aux attaques \"Store Now, Decrypt Later\" par de futurs ordinateurs quantiques. La mise à jour matérielle des automates (PLC) est financièrement et physiquement impossible à grande échelle.",
        "approche": "Un orchestrateur réseau de distribution de clés quantiques (QKD) et cryptographie post-quantique (PQC) agissant comme une surcouche de sécurité (Zero-Trust hardware gateway) placée devant les réseaux OT existants sans modifier les terminaux finaux.",
        "pourquoi_echec": "Les VPN/SaaS de sécurité traditionnels ajoutent trop de latence pour le contrôle industriel temps-réel (qui exige des temps de réponse < 5ms) et s'appuient sur une cryptographie classique (RSA/ECC) vouée à devenir obsolète.",
        "risques": "Standardisation PQC (NIST) encore en cours, coût matériel des passerelles QKD, nécessité de certifications industrielles strictes (IEC 62443)."
    },
    {
        "filename": "sim-to-real-engine.md",
        "title": "Neural Physics Engine",
        "domaine": "World Models & Robotique",
        "modele": "B2B",
        "cible": "Fabricants de robots humanoïdes et constructeurs automobiles autonomes (Head of Robotics, VP Autonomy).",
        "probleme": "L'entraînement de politiques de contrôle robotique dans le monde réel est trop lent et coûteux. Le transfert des simulations actuelles vers la réalité (sim-to-real gap) échoue à cause de la modélisation inexacte de la physique de contact (friction, matériaux déformables).",
        "approche": "Un moteur de \"Neural Physics\" qui remplace les solveurs physiques classiques par des réseaux de neurones graphiques (GNN) capables d'apprendre et de simuler la physique de contact complexe, les fluides et les objets mous en temps réel avec un rendu différentiable.",
        "pourquoi_echec": "Les moteurs de jeu existants (Unreal, Unity) privilégient l'apparence visuelle sur la précision physique rigoureuse. Les LLMs n'ont aucune notion de la physique spatiale, de la gravité, ou de la dynamique des corps rigides.",
        "risques": "Dépendance au hardware (NVIDIA Omniverse), difficulté à prouver l'universalité du solveur neuronal sur de nouveaux matériaux, barrière technologique extrêmement élevée."
    },
    {
        "filename": "grid-inertia-synthesizer.md",
        "title": "Grid Inertia Synthesizer",
        "domaine": "ClimateTech & Énergie",
        "modele": "B2B",
        "cible": "Gestionnaires de réseau de transport (TSO) et producteurs d'EnR (RTE, National Grid, opérateurs de parcs éoliens/solaires).",
        "probleme": "La transition vers les énergies renouvelables supprime \"l'inertie tournante\" des grosses turbines fossiles, rendant les réseaux électriques de plus en plus instables et sujets aux blackouts lors des fluctuations de fréquence.",
        "approche": "Un contrôleur matériel/logiciel (edge computing) pour onduleurs massifs (Grid-forming inverters) couplé à une IA de prédiction de micro-instabilités qui synthétise de l'inertie virtuelle en injectant ou absorbant de la puissance en quelques millisecondes via des batteries décentralisées.",
        "pourquoi_echec": "Problème cyber-physique critique nécessitant un contrôle bas-niveau ultra-rapide (sub-cycle AC) au niveau du hardware. Un SaaS cloud introduirait une latence fatale entraînant l'effondrement du réseau.",
        "risques": "Réglementations des réseaux très lentes à évoluer, besoin de capitaux importants pour le déploiement matériel, responsabilité légale en cas de coupure de courant majeure."
    },
    {
        "filename": "pqc-sbom-validator.md",
        "title": "Quantum Safe SBOM",
        "domaine": "Cybersécurité & Résilience",
        "modele": "B2B",
        "cible": "Editeurs de logiciels gouvernementaux, sous-traitants défense, institutions financières (DevSecOps, CISO).",
        "probleme": "Il est impossible de garantir qu'une bibliothèque open-source tierce insérée dans une chaîne de CI/CD ne contient pas de portes dérobées ou que sa signature cryptographique n'a pas été compromise face aux futures menaces quantiques.",
        "approche": "Une plateforme d'analyse d'AST (Abstract Syntax Tree) sémantique qui trace la provenance du code source jusqu'au binaire final, en signant de manière indélébile chaque étape de la compilation via un registre distribué utilisant la cryptographie Post-Quantique.",
        "pourquoi_echec": "Les scanners de vulnérabilités classiques (SCA) se contentent de comparer des versions de packages avec une base de données de CVE connue, sans comprendre la structure du code ou détecter des malwares \"zero-day\" insérés lors de la compilation.",
        "risques": "Adoption des standards PQC, intégration complexe dans l'écosystème fragmenté des outils de CI/CD (GitHub, GitLab, Jenkins), besoin de convaincre les développeurs open-source d'adopter le standard."
    },
    {
        "filename": "m2m-agent-bandwidth-broker.md",
        "title": "M2M Bandwidth Broker",
        "domaine": "IA & Agents autonomes",
        "modele": "M2M",
        "cible": "Flottes de drones autonomes, véhicules autonomes, réseaux IoT industriels (VP of Operations, Fleet Managers).",
        "probleme": "Avec la prolifération d'agents IA embarqués fonctionnant en essaim, les réseaux de communication (5G, satellite) sont saturés par des échanges de données brutes, entraînant des latences qui paralysent la prise de décision collective en temps réel.",
        "approche": "Un protocole de marché décentralisé M2M opérant au niveau de la couche réseau (Layer 3/4) où les agents IA \"enchérissent\" dynamiquement pour la bande passante et le temps de calcul Edge, en compressant sémantiquement les informations critiques via des représentations latentes.",
        "pourquoi_echec": "Les API REST ou MQTT sont trop bavards et centralisés pour des flottes déconnectées (Edge). Nécessite une orchestration de réseau ad-hoc, du peer-to-peer, et une tarification algorithmique à la milliseconde que le cloud ne peut gérer.",
        "risques": "Nécessite une masse critique de machines adoptant le protocole pour que le marché soit liquide, dépendance au matériel réseau embarqué, adoption par les constructeurs matériels."
    },
    {
        "filename": "zero-trust-space-mesh.md",
        "title": "Space Mesh ZT",
        "domaine": "Deep Tech Infra & Cybersécurité",
        "modele": "B2B",
        "cible": "Opérateurs de constellations de satellites LEO, agences spatiales, fournisseurs de télécommunications (Space Systems Engineers, CISO).",
        "probleme": "Les réseaux spatiaux (LEO) communiquant via des liens laser optiques sont vulnérables aux attaques d'interception, à l'usurpation d'identité et à la prise de contrôle d'un nœud satellite, menaçant l'intégrité globale du réseau.",
        "approche": "Une infrastructure de sécurité Zero-Trust ultra-légère conçue spécifiquement pour les systèmes d'exploitation en temps réel (RTOS) spatiaux. Implémente une authentification mutuelle continue et un routage dynamique résilient aux rayonnements cosmiques.",
        "pourquoi_echec": "Les environnements spatiaux ont de fortes contraintes de puissance (SWaP), de calcul et subissent des retards de propagation (Doppler). Les solutions Zero-Trust cloud terrestres (ex. Zscaler) sont incompatibles.",
        "risques": "Cycle de vente très long (spécifications aérospatiales), difficulté à tester en orbite réelle, coûts d'intégration avec les fournisseurs de bus satellitaires."
    },
    {
        "filename": "llm-hardware-obfuscator.md",
        "title": "Hardware Obfuscator AI",
        "domaine": "Deep Tech & IA",
        "modele": "B2B",
        "cible": "Concepteurs de puces IA (Fabless), fonderies de semi-conducteurs, IP cores providers (VP Hardware Engineering).",
        "probleme": "Le vol de propriété intellectuelle matérielle coûte cher. Les fonderies offshore peuvent cloner des plans de puces (GDSII), insérer des chevaux de Troie matériels ou surproduire pour le marché gris.",
        "approche": "Un moteur d'obfuscation de circuits logiques basé sur l'apprentissage par renforcement (RL). Il insère des \"portes factices\" et modifie la topologie du netlist pour que la puce ne fonctionne qu'après l'activation d'une clé cryptographique post-fabrication.",
        "pourquoi_echec": "La conception de circuits imprimés nécessite de respecter des contraintes physiques (PPA : Power, Performance, Area). L'IA doit opérer sur des graphes représentant des milliards de transistors sans dégrader les performances de la puce finale, ce qu'aucun SaaS logiciel classique ne fait.",
        "risques": "Validation par les fonderies géantes (TSMC, Samsung), réticence des ingénieurs hardware à modifier leurs workflows, augmentation possible de la surface de silicium."
    },
    {
        "filename": "co2-mineralization-tracker.md",
        "title": "Geo Carbon MRV",
        "domaine": "ClimateTech",
        "modele": "B2B",
        "cible": "Acheteurs de crédits carbone industriels, opérateurs de capture et stockage de carbone (CCS), auditeurs de durabilité.",
        "probleme": "Les marchés du carbone manquent de confiance (greenwashing). Prouver physiquement et de manière inaltérable qu'une tonne spécifique de CO2 a été enfouie et minéralisée dans la roche est extrêmement difficile.",
        "approche": "Un système IoT combinant des capteurs sismiques de fond de puits et un World Model géophysique qui valide la réaction chimique de minéralisation en temps réel et émet un certificat cryptographiquement lié à la donnée capteur brute.",
        "pourquoi_echec": "La mesure, le rapport et la vérification (MRV) basés sur des feuilles de calcul sont falsifiables. Il faut intégrer du hardware de mesure géologique avec de la modélisation thermodynamique souterraine.",
        "risques": "Coût de déploiement des capteurs en puits profond, complexité d'interprétation des données géophysiques, viabilité économique des projets CCS."
    },
    {
        "filename": "multi-omic-aging-clock.md",
        "title": "Deep Omic Clock",
        "domaine": "Biotech",
        "modele": "B2B",
        "cible": "Cliniques de longévité, compagnies d'assurance vie, chercheurs en géroscience (CMO, Actuaires).",
        "probleme": "L'âge chronologique est un mauvais indicateur de risque. Les horloges épigénétiques actuelles sont unidimensionnelles et manquent de précision pour cibler des interventions cliniques personnalisées ou valider l'efficacité de thérapies anti-âge.",
        "approche": "Un modèle d'apprentissage profond multimodal intégrant l'épigénome, le protéome, le microbiome et les données cliniques longitudinales pour créer un World Model de vieillissement biologique, capable de simuler l'effet de molécules géroprotectrices.",
        "pourquoi_echec": "L'intégration multi-omique confronte au fléau de la dimensionnalité. Nécessite des architectures d'IA spécialisées (Transformers biologiques) pour extraire des signaux causaux complexes, impossibles avec un outil d'analyse de données standard.",
        "risques": "Accès aux données longitudinales très coûteuses, difficulté réglementaire (FDA) pour valider des biomarqueurs du vieillissement, acceptation éthique."
    }
]

template = """<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->
# Candidat : {title}

* **Domaine principal :** {domaine}
* **Modèle économique :** {modele}
* **Cible :** {cible}
* **Le problème urgent :** {probleme}
* **L'approche technique :** {approche}
* **Pourquoi une solution générique/SaaS classique échoue :** {pourquoi_echec}
* **Risques majeurs & Dépendances :** {risques}
"""

os.makedirs("candidates", exist_ok=True)

for c in candidates:
    content = template.format(**c)
    filepath = os.path.join("candidates", c["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
