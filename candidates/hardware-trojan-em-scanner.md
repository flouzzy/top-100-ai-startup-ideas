<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Hardware Trojan EM Scanner

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B
- **Cible :** Défense nationale, fabricants de systèmes critiques (aérospatial, médical, infrastructures), agences de renseignement.
- **Le problème urgent :** Avec la chaîne d'approvisionnement globale des puces électroniques, il est presque impossible de garantir qu'aucun "Hardware Trojan" (portes dérobées physiques) n'a été inséré dans le silicium lors de la fonderie offshore. Une puce certifiée peut cacher des kill-switches.
- **L'approche technique :** Système de scan non destructif combinant microscopie par émission électromagnétique (EM) à ultra-haute résolution et modèles d'IA pré-entraînés pour analyser les signatures spectrales et identifier les écarts infimes par rapport au "Golden Layout" (le design original de la puce).
- **Pourquoi une solution générique/SaaS classique échoue :** Ce problème relève du matériel physique (side-channel analysis, ingénierie inverse). Le logiciel pur ne peut rien contre une modification physique du silicium au niveau du nanomètre. Cela demande des équipements de mesure de pointe et des algorithmes de traitement de signal spécialisés.
- **Risques majeurs & Dépendances :** Besoin de matériel très coûteux (microscopes EM), difficulté d'accès aux "Golden Layouts" protégés par la propriété intellectuelle, complexité avec les puces 3D.
