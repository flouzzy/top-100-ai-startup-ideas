<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Rad-Hard RISC-V Hypervisor

- **Domaine principal :** Robotique & Systèmes embarqués (Spatial/Nucléaire)
- **Modèle économique :** B2B
- **Cible :** Agences spatiales (NASA, ESA), constructeurs de satellites commerciaux, opérateurs de centrales nucléaires, robotique de démantèlement extrême.
- **Le problème urgent :** L'électronique spatiale et nucléaire (soumise aux radiations) nécessite des puces "rad-hard" (durcies contre les radiations) extrêmement chères, propriétaires et très lentes (souvent de l'architecture dépassée). Exécuter des IAs modernes de navigation ou de traitement d'images de manière sûre dans l'espace est quasiment impossible sans subir des bit-flips constants (Single Event Upsets).
- **L'approche technique :** Un hyperviseur logiciel ultra-sécurisé couplé à une architecture de processeur RISC-V open-source optimisée pour le "soft-error mitigation". Il utilise la redondance modulaire triple (TMR) au niveau logiciel et micro-architectural pour corriger les erreurs induites par les radiations de manière transparente sur du silicium commercial de pointe (COTS).
- **Pourquoi une solution générique/SaaS classique échoue :** C'est du développement de système d'exploitation bas niveau embarqué (Ring 0 / Bare Metal) couplé à de la conception de micro-architecture (RTL). Aucune API cloud ou LLM ne peut protéger physiquement un registre CPU contre un rayonnement cosmique en temps réel avec des garanties de temps d'exécution déterministes.
- **Risques majeurs & Dépendances :** Certification spatiale extrêmement rigoureuse (coûts et temps massifs), tests d'irradiation nécessaires dans des cyclotrons (accès limité et coûteux), résistance des acteurs traditionnels du spatial.
