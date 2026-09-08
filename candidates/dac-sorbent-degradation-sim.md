<!-- markdownlint-disable MD013 -->

# Candidat : DAC Sorbent Degradation Simulator

- **Domaine principal :** ClimateTech & Énergie / World Models
- **Modèle économique :** B2B
- **Cible :** Startups de Direct Air Capture (DAC), entreprises d'ingénierie environnementale, pétroliers en transition.
- **Le problème urgent :** Le captage direct du CO2 dans l'air (DAC) repose sur des matériaux sorbants (amines, MOFs) coûteux. Ces matériaux se dégradent rapidement (perte de capacité de captage) à cause de l'oxydation thermique lors des cycles de régénération (chauffage pour libérer le CO2) et de l'empoisonnement par des gaz traces (SOx, NOx) ou l'humidité. Prévoir la durée de vie de ces matériaux à l'échelle d'une usine coûte des millions en remplacement prématuré ou en inefficacité.
- **L'approche technique :** Un jumeau numérique chimique utilisant des réseaux de graphes neuronaux pour modéliser la cinétique de dégradation des matériaux sorbants. Il simule des millions de cycles de sorption/désorption sous des conditions atmosphériques et thermiques variables, permettant aux ingénieurs de concevoir de nouvelles structures moléculaires (MOFs) intrinsèquement résistantes ou d'optimiser les profils de température de l'usine pour maximiser la durée de vie du sorbant.
- **Pourquoi une solution générique/SaaS classique échoue :** La dégradation chimique est un processus hors équilibre complexe. Les logiciels de simulation de procédés chimiques (comme Aspen Plus) ne modélisent pas l'usure atomique des nanomatériaux poreux, et l'IA classique manque de compréhension des mécanismes de chimisorption.
- **Risques majeurs & Dépendances :** La complexité de la validation empirique (les tests de vieillissement accéléré in vitro prennent des mois). La diversité des matériaux sorbants nécessite des modèles spécifiques à chaque chimie (difficile à généraliser).
