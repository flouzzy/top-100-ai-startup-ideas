<!-- markdownlint-disable MD013 -->

# Candidat : Subsea Acoustic SNN Detector

- **Domaine principal :** Cybersécurité & Résilience / Robotique
- **Modèle économique :** B2B / B2G
- **Cible :** Opérateurs d'infrastructures critiques sous-marines (câbles internet transocéaniques, pipelines, éolien offshore), marines nationales.
- **Le problème urgent :** L'infrastructure sous-marine mondiale est vulnérable aux sabotages physiques. Surveiller des milliers de kilomètres de câbles repose sur des capteurs acoustiques (hydrophones, DAS sur fibre optique) qui génèrent une quantité massive de données brutes. Remonter ces données à la surface pour analyse cloud est impossible en raison de la bande passante sous-marine quasi-nulle. L'analyse locale (sur batterie) épuise l'énergie en quelques jours à cause des CPU classiques.
- **L'approche technique :** Un processeur de signal acoustique embarqué basé sur des réseaux de neurones à impulsions (SNN - Neuromorphic Computing). Il écoute en continu avec une consommation électrique de l'ordre du microwatt, ne s'activant ("spiking") que lorsqu'il reconnaît l'empreinte acoustique spécifique d'une menace (ex: ROV, sous-marin de poche, outil de découpe), permettant un déploiement autonome sur plusieurs années sans recharge.
- **Pourquoi une solution générique/SaaS classique échoue :** Les algorithmes de détection d'anomalies audio classiques (DSP, Transformers) requièrent des accélérateurs IA (GPU/TPU) incompatibles avec les contraintes drastiques de puissance (millivatts) des bouées ou noeuds sous-marins isolés.
- **Risques majeurs & Dépendances :** Le bruit de fond océanique est extrêmement complexe (biologique, sismique, météorologique) et évolutif, ce qui rend l'entraînement de SNN sans faux positifs très difficile. Le hardware neuromorphique durci pour les abysses (pression, froid) reste expérimental.
