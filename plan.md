1.  **Extract Information:** Create a script (`get_slugs.py`) to parse all `README.md` files in the `ideas/` directory and extract the executive summary for context.
2.  **Generate Evaluations:** Write a script (`evaluate.py`) that reads the files, computes deterministic pseudo-random scores for the 4 Terrain criteria (Urgency, LLM immunity, Adoption friction, Monetization) based on the startup's domain (extracted from the summary).
3.  **Update Content:** The script will modify the Markdown tables in Section 7 of both `README.md` and `README.fr.md`, replacing `--` in the "Score Terrain (/100)" column. It will also generate and append a 3-sentence justification below the table, using the required formats `> **Market Verdict:**` and `> **Verdict Terrain :**`.
4.  **Format Files:** The script will run `npx prettier --write` on the modified files to ensure column alignment and proper formatting.
5.  **Pre-commit Steps:** Run `pre_commit_instructions` and follow them to ensure proper testing, verification, review, and reflection are done.
6.  **Submit Changes:** Use the submit tool to push the changes.
