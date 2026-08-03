<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Lunar Regolith Construction Sim

- **Domaine principal :** Robotique & Systèmes embarqués (Spatial)
- **Modèle économique :** B2B / B2G
- **Cible :** Agences spatiales (Artemis), entreprises de construction extraterrestre, fabricants de robots miniers spatiaux.
- **Le problème urgent :** Construire des habitats ou des pistes d'atterrissage sur la Lune ou Mars avec du matériel terrestre est économiquement impossible (coût de lancement exorbitant). L'utilisation des ressources in-situ (ISRU - impression 3D de régolithe) est nécessaire, mais le comportement granulaire du régolithe (abrasif, électrostatique, sous faible gravité) fait systématiquement s'enrayer les robots constructeurs actuels.
- **L'approche technique :** Un environnement de simulation de dynamique granulaire (Discrete Element Method - DEM) accéléré par IA (Neural Surrogate Models) qui modélise le comportement mécanique, thermique et électrostatique du régolithe lunaire en gravité réduite. Cela permet d'entraîner par renforcement (RL) les robots constructeurs avant leur déploiement.
- **Pourquoi une solution générique/SaaS classique échoue :** Les simulateurs de BTP classiques ne gèrent pas la physique granulaire sous vide et microgravité, ni les charges électrostatiques extrêmes qui collent la poussière aux mécanismes. La boucle sim-to-real spatiale nécessite des modèles physiques de pointe.
- **Risques majeurs & Dépendances :** Le calendrier réel des missions habitées lunaires (retards probables), la difficulté de simuler parfaitement une poussière cosmique que l'on n'a étudiée qu'en faibles quantités sur Terre, et le coût de l'entraînement RL complexe.
