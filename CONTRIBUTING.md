<!-- markdownlint-disable MD013 MD033 MD060 MD036 MD041 -->

*[🇫🇷 Version Française](./CONTRIBUTING.fr.md)*

# Contribution Guide to the Top 100 AI Startup Ideas Index

Thank you for your interest in updating and enriching the index! This repository uses a strict evaluation protocol to ensure that only very high value-added ideas enter the Top 100.

## 📥 How to propose a new idea?

1. **Fork** the repository.
2. Create a new sheet in the `candidates/` folder following the naming convention: `name-of-your-idea.md`.
3. Strictly follow the sheet template (Contrarian thesis, Target, Architecture, Unit Economics, Moat).
4. Open a **Pull Request (PR)** to the `main` branch.

## ⚙️ Direct elimination criteria (Red Flags)

Your PR will be rejected if:

* The idea is a simple "wrapper" or a thin graphical interface around a mainstream LLM without any barrier to entry.
* The economic model relies on hope without precise quantification of access to €100k ARR or equivalent volume.
* The idea can be completely solved by a user typing a standard prompt on ChatGPT/Gemini.

## 🔄 Evaluation process

Each proposal in `candidates/` is submitted to the VC and Terrain evaluation prompts. If its Composite Score exceeds the score of the 100th idea in the current index:

1. The idea enters the `ideas/` folder at the corresponding rank.
2. The 100th ranked idea is relegated to the `archive/` folder.
3. The global `README.md` ranking is realigned.
