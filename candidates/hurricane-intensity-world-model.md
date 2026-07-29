<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Hurricane Intensity World Model

- **Domaine principal :** World Models & Simulation physique
- **Modèle économique :** B2B
- **Cible :** Réassureurs mondiaux (Swiss Re, Munich Re), fonds de cat bonds, gouvernements côtiers et agences de gestion des urgences (FEMA)
- **Le problème urgent :** L'intensité des ouragans s'amplifie plus rapidement (rapid intensification) en raison du réchauffement des océans. Les modèles météorologiques actuels (statiques et statistiques) peinent à prédire la force du vent à l'impact géolocalisé avec précision, entraînant des pertes se chiffrant en dizaines de milliards de dollars pour les assureurs en raison de provisions mal ajustées et d'évacuations inefficaces.
- **L'approche technique :** Un jumeau numérique océan-atmosphère en temps réel (Neural Physics Engine) combinant des données satellites multiphysiques, de température de surface et de l'apprentissage profond (Transformers spatio-temporels) pour simuler la dynamique des fluides avec une granularité au kilomètre carré et prédire les pics d'intensité 72 heures à l'avance.
- **Pourquoi une solution générique/SaaS classique échoue :** L'équation de Navier-Stokes à l'échelle d'un cyclone est impossible à résoudre en temps réel avec le calcul traditionnel ou un LLM. Il nécessite un moteur physique neuronal capable de modéliser les intéractions complexes thermodynamiques à grande échelle sans les coûts immenses des supercalculateurs traditionnels.
- **Risques majeurs & Dépendances :** Accès coûteux et complexe aux flux de données satellites de pointe en temps réel, dépendance à une puissance de calcul massive pour l'entraînement (clusters H100), scepticisme initial des actuaires face à des modèles "boîte noire".
