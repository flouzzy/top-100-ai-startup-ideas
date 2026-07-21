# Guide de Contribution au Top 100 AI Startup Ideas Index

Merci de votre intérêt pour la mise à jour et l'enrichissement de l'index ! Ce dépôt utilise un protocole strict d'évaluation pour garantir que seules les idées à très haute valeur ajoutée intègrent le Top 100.

## 📥 Comment proposer une nouvelle idée ?

1. **Forkez** le dépôt.
2. Créez une nouvelle fiche dans le dossier `candidates/` en suivant la nomenclature : `nom-de-votre-idee.md`.
3. Respectez impérativement le template de fiche (Thèse contrariante, Cible, Architecture, Unit Economics, Moat).
4. Ouvrez une **Pull Request (PR)** vers la branche `main`.

## ⚙️ Critères d'élimination directe (Red Flags)

Votre PR sera rejetée si :
* L'idée est un simple "wrapper" ou une interface graphique fine autour d'un LLM grand public sans aucune barrière à l'entrée.
* Le modèle économique repose sur de l'espoir sans chiffrage précis de l'accès aux 100k€ d'ARR ou équivalent de volume.
* L'idée peut être intégralement résolue par un utilisateur tapant un prompt standard sur ChatGPT/Gemini.

## 🔄 Processus d'évaluation

Chaque proposition dans `candidates/` est soumise aux prompts d'évaluation VC et Terrain. Si son Score Composite dépasse la note de la 100ème idée de l'index actuel :
1. L'idée intègre le dossier `ideas/` au rang correspondant.
2. L'idée classée 100ème est reléguée dans le dossier `archive/`.
3. Le classement global `README.md` est réaligné.
