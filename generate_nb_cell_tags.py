import yaml
from pathlib import Path

from urllib.parse import quote

def generate_jupyterhub_links(notebook_path):
    encoded = quote(f"CommunityData/OpenSees/{notebook_path}")
    jupyter_link = f"https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/{encoded}"
    download_link = notebook_path
    return f"\n      <sub>📂 [Open in JupyterHub]({jupyter_link}) • 💾 [Download]({download_link})</sub>"



def get_heading_from_file(file_path):
    """Extract the first level-1 Markdown heading from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith("# "):
                    return line.strip().lstrip("# ").strip()
    except FileNotFoundError:
        return Path(file_path).stem  # fallback if file doesn't exist
    return Path(file_path).stem  # fallback if no heading found


def format_link(file_path):
    """Create a Markdown link with optional JupyterHub links."""
    title = get_heading_from_file(file_path)
    link_line = f"[{title}]({file_path})"
    
    if file_path.endswith(".ipynb") or file_path.endswith(".py"):
        link_line += generate_jupyterhub_links(file_path)
    
    return link_line


def format_link_old(file_path):
    """Create a Markdown link with the actual heading as the title."""
    title = get_heading_from_file(file_path)
    return f"[{title}]({file_path})"

def process_chapters(chapters, indent=0):
    lines = []
    prefix = "  " * indent + "- "
    for chapter in chapters:
        if 'file' in chapter:
            lines.append(prefix + format_link(chapter['file']))
        if 'sections' in chapter:
            lines.extend(process_chapters(chapter['sections'], indent + 1))
    return lines

def generate_markdown_toc(toc_yaml_path="_toc.yml"):
    with open(toc_yaml_path, "r", encoding="utf-8") as f:
        toc = yaml.safe_load(f)

    lines = ["\n## Table of Contents\n"]

    if 'parts' in toc:
        for part in toc['parts']:
            if 'caption' in part:
                lines.append(f"### {part['caption']}")
            lines.extend(process_chapters(part.get('chapters', [])))
            lines.append("")
    elif 'chapters' in toc:
        lines.extend(process_chapters(toc['chapters']))

    return "\n".join(lines)


def generate_nb_cell_tags(toc_yaml_path="_toc.yml"):

    with open(toc_yaml_path, "r", encoding="utf-8") as f:
        toc = yaml.safe_load(f)

    lines = ["\n## Table of Contents\n"]

    if 'parts' in toc:
        for part in toc['parts']:
            if 'caption' in part:
                lines.append(f"### {part['caption']}")
            lines.extend(process_chapters(part.get('chapters', [])))
            lines.append("")
    elif 'chapters' in toc:
        lines.extend(process_chapters(toc['chapters']))
    
    
    
    if file_path.endswith(".ipynb") or file_path.endswith(".py"):
        link_line += generate_jupyterhub_links(file_path)

    # Generate ToC
    toc_md = generate_markdown_toc(toc_yaml_path).strip()

    # Save ToC for Jupyter Book `{include}`
    with open(output_toc_path, "w", encoding="utf-8") as f:
        f.write(toc_md + "\n")
    print(f"✅ Wrote {output_toc_path}")

    # Generate GitHub-friendly README
    with open(github_readme_path, "w", encoding="utf-8") as f:
        f.write(intro + "\n\n" + toc_md + "\n")
    print(f"✅ Wrote {github_readme_path} (for GitHub)")

# Run the generator
if __name__ == "__main__":
    generate_files()

