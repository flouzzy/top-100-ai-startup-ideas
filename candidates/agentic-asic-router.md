<!-- markdownlint-disable MD013 -->

# Candidat : Agentic ASIC Router

- **Domaine principal :** IA & Agents autonomes / Deep Tech Infra
- **Modèle économique :** B2B
- **Cible :** Fabricants de puces fabless, concepteurs de semi-conducteurs spécialisés (AI accelerators, IoT, edge computing), fonderies (TSMC, Samsung).
- **Le problème urgent :** Le processus de "place and route" (P&R) pour la conception de puces (ASIC) est devenu un goulet d'étranglement majeur. Les logiciels d'Electronic Design Automation (EDA) traditionnels demandent des mois de travail itératif humain pour optimiser l'agencement spatial des milliards de transistors afin de réduire la consommation d'énergie (PPA: Power, Performance, Area). Le coût de développement d'une puce explose et retarde le time-to-market.
- **L'approche technique :** Un écosystème d'agents autonomes d'ingénierie utilisant des réseaux de neurones graphiques (GNN) et de l'apprentissage par renforcement (RL) pour explorer l'espace de conception massivement en parallèle. Les agents négocient entre eux les ressources spatiales et temporelles du silicium pour accomplir un "place and route" en quelques jours au lieu de plusieurs mois, produisant des configurations non intuitives mais physiquement supérieures.
- **Pourquoi une solution générique/SaaS classique échoue :** L'EDA est un monopole logiciel complexe avec une forte adhérence (vendor lock-in) et s'appuie sur des heuristiques traditionnelles. Un LLM textuel ne peut pas comprendre les contraintes de conception de géométrie spatiale 3D, les règles de conception (DRC) des fonderies et l'électromagnétisme.
- **Risques majeurs & Dépendances :** Besoin d'accéder aux données d'entraînement propriétaires des processus de fonderie (PDK - Process Design Kits) ultra-secrets ; résistance de l'écosystème EDA existant ; vérification formelle absolue (une erreur coûte des millions en masques de gravure).
