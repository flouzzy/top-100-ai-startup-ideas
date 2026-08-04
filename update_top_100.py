import os
import re
import urllib.parse
import shutil
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
    model = "Unknown"
    m_model_badge = re.search(r'badge/(?:Mod%C3%A8le|Model|Modèle)-([^-]+)-', content)

    if m_model_badge:
        raw_model = urllib.parse.unquote(m_model_badge.group(1).strip())
        model = raw_model.replace("_", " ")
        model = model.replace("%20", " ").replace("%2F", "/").replace("%28", "(").replace("%29", ")").replace("%2C", ",")
        if model.endswith("(Revenue split on "):
            model = model.replace("(Revenue split on ", "(Revenue split on arbitrage)")
        elif model.endswith("(Revenue split on"):
            model = model.replace("(Revenue split on", "(Revenue split on arbitrage)")
        if model.endswith("(Software Licensing / Edge "):
            model = model.replace("(Software Licensing / Edge ", "(Software Licensing / Edge API)")
        elif model.endswith("(Software Licensing / Edge"):
            model = model.replace("(Software Licensing / Edge", "(Software Licensing / Edge API)")
    else:
        m_model_alt = re.search(r'!\[.*?Type:\s*(.+?)\]', content)
        if m_model_alt:
            model = m_model_alt.group(1).strip()

    # Scores
    vc_score = 0
    terrain_score = 0
    composite = 0

    m_comp = re.search(r'badge/(?:Score_Composite|Composite_Score)-([^-]+)-', content)
    if m_comp:
        comp_str = urllib.parse.unquote(m_comp.group(1).strip())
        if re.match(r'^[\d\.]+$', comp_str):
            composite = float(comp_str)
        elif comp_str not in ['Pending', 'En évaluation', 'En attente d\'évaluation', "En attente d'évaluation"]:
            m_comp_num = re.search(r'([\d\.]+)', comp_str)
            if m_comp_num:
                composite = float(m_comp_num.group(1))

    # Match with or without markdown bold asterisks and handle various spacings
    # E.g. | TOTAL | 89 / 100 | 81 / 100 |  or | **TOTAL** | **89 / 100** | **81 / 100** |
    m_total = re.search(r'\|\s*\**TOTAL\**\s*\|\s*\**([-\d\.]+)\s*/\s*100\**\s*\|\s*\**([-\d\.]+)\s*/\s*100\**\s*\|', content, re.IGNORECASE)
    if not m_total:
        # Try a more relaxed regex just in case
        m_total = re.search(r'\|\s*\*?TOTAL\*?\s*\|\s*\*?([-\d\.]+)\s*/\s*100\*?\s*\|\s*\*?([-\d\.]+)\s*/\s*100\*?\s*\|', content, re.IGNORECASE)
    if not m_total:
        # Fallback to scanning lines
        lines = content.split('\n')
        for line in lines:
            if 'TOTAL' in line.upper():
                # Extract numbers before / 100
                nums = re.findall(r'([-\d\.]+)\s*/\s*100', line)
                if len(nums) >= 2:
                    m_total = type('obj', (object,), {'group': lambda self, i: nums[i-1]})()
                    break

    if m_total:
        s_vc = m_total.group(1).strip()
        s_ter = m_total.group(2).strip()
        if s_vc != '--':
            vc_score = float(s_vc)
        if s_ter != '--':
            terrain_score = float(s_ter)

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
relegated = results[100:]

# Archive relegated ideas
if not os.path.exists('archive'):
    os.makedirs('archive')

for r in relegated:
    src_dir = os.path.join('ideas', r['dir'])
    dst_dir = os.path.join('archive', r['dir'])
    if os.path.exists(src_dir):
        # Handle case where directory already exists in archive
        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir)
        shutil.move(src_dir, 'archive/')
        print(f"Archived {r['dir']}")

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
