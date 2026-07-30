import os
import re
import urllib.parse
from datetime import datetime

results = []

for d in os.listdir('ideas'):
    if not os.path.isdir(os.path.join('ideas', d)): continue
    filepath = os.path.join('ideas', d, 'README.md')
    if not os.path.exists(filepath): continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Title
    m_title = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = m_title.group(1).strip() if m_title else d

    # Model
    # Try finding badge/...-B2B-... first
    m_model = re.search(r'badge/(?:Mod%C3%A8le|Model|Modèle)-([^-]+)-', content)
    if not m_model:
        m_model = re.search(r'!\[.*?Type:\s*(.+?)\]', content)

    if m_model:
        model = urllib.parse.unquote(m_model.group(1).strip())
    else:
        model = "Unknown"

    # Scores
    vc_score = 0
    terrain_score = 0
    composite = 0

    # Check if there is an explicitly evaluated Composite Score in the badge
    m_comp = re.search(r'badge/(?:Score_Composite|Composite_Score)-([^-]+)-', content)
    if m_comp:
        comp_str = urllib.parse.unquote(m_comp.group(1).strip())
        # Try to parse it to float if it looks like a number, but usually it's "Pending" or "En évaluation" if missing
        if re.match(r'^[\d\.]+$', comp_str):
            composite = float(comp_str)
        elif comp_str != 'Pending' and comp_str != 'En évaluation':
            # It might have a trailing /100 or something, let's try to extract numbers
            m_comp_num = re.search(r'([\d\.]+)', comp_str)
            if m_comp_num:
                composite = float(m_comp_num.group(1))

    # Parse VC and Terrain from table
    m_total = re.search(r'\|\s*\**TOTAL\**\s*\|\s*\**([-\d\.]+)\s*/\s*100\**\s*\|\s*\**([-\d\.]+)\s*/\s*100\**\s*\|', content, re.IGNORECASE)
    if m_total:
        s_vc = m_total.group(1).strip()
        s_ter = m_total.group(2).strip()

        if s_vc != '--':
            vc_score = float(s_vc)

        if s_ter != '--':
            terrain_score = float(s_ter)

    # Calculate composite if missing and we have at least one score or if both are zero
    # Actually formula is just VC*0.5 + Terrain*0.5. If both 0, it's 0.
    # If one is missing (0), it still gets calculated as (score*0.5)
    calculated_comp = (vc_score * 0.5) + (terrain_score * 0.5)
    if composite == 0 and calculated_comp > 0:
        composite = calculated_comp

    results.append({
        'dir': d,
        'title': title,
        'model': model,
        'vc': vc_score,
        'terrain': terrain_score,
        'composite': composite
    })

results.sort(key=lambda x: (-x['composite'], x['title'].lower()))
top_100 = results[:100]

def fmt_score(score):
    if score == int(score):
        return f"{int(score)}"
    return f"{score:.1f}"

def format_score_display(score):
    if score == 0:
        return "--"
    return fmt_score(score)

def generate_markdown_table(lang):
    if lang == "fr":
        lines = [
            "| Rang | Modèle | Startup | Score Composite | Score VC | Score Terrain | Fiche détaillée |",
            "| :---: | :---: | :--- | :---: | :---: | :---: | :---: |"
        ]
        consulter = "Consulter"
    else:
        lines = [
            "| Rank | Model | Startup | Composite Score | VC Score | Terrain Score | Detailed Sheet |",
            "| :---: | :---: | :--- | :---: | :---: | :---: | :---: |"
        ]
        consulter = "View"

    for i, r in enumerate(top_100):
        rank = f"**{i+1:03d}**"

        comp_disp = f"**{format_score_display(r['composite'])}/100**"
        vc_disp = f"{format_score_display(r['vc'])}/100"
        ter_disp = f"{format_score_display(r['terrain'])}/100"

        link = f"[{consulter}](./ideas/{r['dir']}/README.md)"

        row = f"| {rank} | {r['model']} | **{r['title']}** | {comp_disp} | {vc_disp} | {ter_disp} | {link} |"
        lines.append(row)

    return "\n".join(lines)

table_fr = generate_markdown_table("fr")
table_en = generate_markdown_table("en")

today = datetime.now().strftime('%Y-%m-%d')
timestamp_fr = f"\n_Dernière mise à jour : {today}_\n"
timestamp_en = f"\n_Last updated: {today}_\n"

def update_file(filepath, header_text, table, timestamp):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    header_idx = content.find(header_text)
    if header_idx == -1:
        print(f"Could not find header in {filepath}")
        return

    pre_header = content[:header_idx] + header_text + "\n\n"
    post_header_content = content[header_idx + len(header_text):]

    m_next_section = re.search(r'\n(##\s+.*)', post_header_content)
    if m_next_section:
        rest_of_file = post_header_content[m_next_section.start():]
    else:
        rest_of_file = ""

    new_content = pre_header + table + "\n" + timestamp + rest_of_file

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        print(f"Updated {filepath}")

update_file('README.fr.md', "## 📊 Le Classement Top 100", table_fr, timestamp_fr)
update_file('README.md', "## 📊 The Top 100 Ranking", table_en, timestamp_en)
