<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Immutable Carbon Sequestration Audit Oracle

- **Domaine principal :** ClimateTech / Deep Tech
- **Modèle économique :** B2B
- **Cible :** Sociétés de DAC (Direct Air Capture), gestionnaires de crédits carbone, régulateurs gouvernementaux, et grandes entreprises achetant des crédits (Microsoft, Stripe).
- **Le problème urgent :** Le marché des crédits carbone est entaché de fraudes, de double comptage et d'estimations approximatives. Acheter des crédits pour la séquestration physique (dans la roche ou le béton) demande des audits manuels lents, coûteux et facilement falsifiables, ce qui limite le financement de ces infrastructures massives.
- **L'approche technique :** Un réseau de capteurs physiques (spectroscopie laser, géophysique) reliés à des enclaves sécurisées (TEE) qui enregistrent le volume exact de $CO_2$ minéralisé. Les données sont validées cryptographiquement et ancrées de façon immuable, générant des "Smart Carbon Credits" auditables en temps réel via une API.
- **Pourquoi une solution générique/SaaS classique échoue :** Un simple logiciel comptable dépend des données saisies manuellement. Si le capteur peut être spoofé ou la base de données altérée, le crédit perd sa valeur certifiée. Il faut lier matériel inviolable, physique des roches, et cryptographie.
- **Risques majeurs & Dépendances :** Standardisation fragmentée du marché du carbone. Coût matériel des capteurs (CAPEX) et maintenance dans des environnements hostiles.
