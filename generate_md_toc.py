import yaml
from pathlib import Path

import nbformat

from urllib.parse import quote

# things to go ahead and do
doTagCells = True
doJubHubLinks = True
doAppendTOC = False
addNBicon = False # they are distracting

jupyterNotebooksPath_start = f"https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/"
jupyterNotebooksPath_mid = f"CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/"

# https://jupyter.designsafe-ci.org/hub/user-redirect/lab/tree/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks


def get_notebook_link(notebook_path):
    encoded = quote(f"{jupyterNotebooksPath_mid}{notebook_path}")
    return f"{jupyterNotebooksPath_start}{encoded}"

def generate_jupyterhub_links(notebook_path):
    # encoded = quote(f"{jupyterNotebooksPath_mid}{notebook_path}")
    jupyter_link = get_notebook_link(notebook_path)
    download_link = notebook_path
    # return f"\n      <sub>📂 [Open in JupyterHub]({jupyter_link}) • 💾 [Download]({download_link})</sub>"
    return f"\n      <sub>📂 <a href='{jupyter_link}' target='_blank'>Open in JupyterHub</a></sub>"



# def insert_designsafe_button(notebook_path, position='top'):
#     encoded = quote(f"CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/{notebook_path}")
#     base_url = f"https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/{encoded}"

#     nb_path = Path(notebook_path)
#     nb = nbformat.read(nb_path, as_version=4)

#     # Construct relative path for the notebook link
#     relative_path = nb_path.as_posix()
#     designsafe_url = f"{base_url}/{relative_path}"

#     # Create the markdown cell with button
#     button_md = nbformat.v4.new_markdown_cell(f"""
# <a href="{designsafe_url}" target="_blank">
#     <button style="padding:8px 16px;font-size:16px;">🔗 Open in DesignSafe</button>
# </a>
# """)

#     # Only insert if not already present
#     existing_button = any(
#         cell.cell_type == 'markdown' and 'Open in DesignSafe' in cell.source
#         for cell in nb.cells[:2]  # Check first few cells
#     )
#     if not existing_button:
#         if position == 'top':
#             nb.cells.insert(0, button_md)
#         elif position == 'bottom':
#             nb.cells.append(button_md)

#     nbformat.write(nb, nb_path)


def get_heading_from_file(file_path):
    """Extract the first level-1 Markdown heading from a file."""
    if file_path.endswith(".ipynb") or file_path.endswith(".py"):
        return get_heading_from_notebook(file_path)
    else:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip().startswith("# "):
                        # print('line',line.strip().lstrip("# ").strip())
                        return line.strip().lstrip("# ").strip()
                # try to look for next level of heading....
                for line in f:
                    if line.strip().startswith("## "):
                        print('two #')
                        return line.strip().lstrip("## ").strip()
        except FileNotFoundError:
            print('FileNotFoundError')
            return Path(file_path).stem  # fallback if file doesn't exist
        return Path(file_path).stem  # fallback if no heading found


def get_heading_from_notebook(notebook_path):
    functionTagMap = {'# Local Utilities Library':'remove-input','OpsUtils.show_video':'remove-input','OpsUtils.show_text_file_in_accordion':'remove-input'}
    # Load notebook
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)

        for idx, cell in enumerate(nb['cells']):
            if cell['cell_type'] == 'markdown':
                original_text = cell['source']
                if original_text[0:2] == "# ":
                    lines = cell.source.splitlines()
                    for i, line in enumerate(lines):
                        if line.startswith("# "):
                            return line.strip().lstrip("# ").strip()
    except FileNotFoundError:
        print('FileNotFoundError')
        return Path(file_path).stem  # fallback if file doesn't exist
    return Path(file_path).stem  # fallback if no heading found






def tag_cells(notebook_path):
    functionTagMap = {'# Local Utilities Library':'remove-input','OpsUtils.show_video':'remove-input','OpsUtils.show_text_file_in_accordion':'remove-input'}
    # Load notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    jupyter_link = get_notebook_link(notebook_path)
    myIcon = '📒'
    space = ' '
    myIconLink = f'<a><href="{jupyter_link}" target="_blank">{myIcon}</a> '
    addNBicon_here = addNBicon
    for idx, cell in enumerate(nb['cells']):
        # print(addNBicon_here)
        if addNBicon_here:
            if cell['cell_type'] == 'markdown':
                original_text = cell['source']
                if original_text[0:2] == "# " and not myIcon in original_text:
                    lines = cell.source.splitlines()
                    for i, line in enumerate(lines):
                        if line.startswith("# ") and myIcon not in line:
                            lines[i] = line + " " + myIcon
                            cell.source = "\n".join(lines)
                            addNBicon_here = False
                            break  # Only modify the first heading

        if cell['cell_type'] == 'code':
            for my_function_call,tag_name in functionTagMap.items():
                if my_function_call in cell['source']:
                    # Initialize metadata if missing
                    if 'tags' not in cell['metadata']:
                        cell['metadata']['tags'] = []

                    # Avoid duplicate tags
                    if tag_name not in cell['metadata']['tags']:
                        cell['metadata']['tags'].append(tag_name)
                        # print(f"Tagged cell {idx} with '{tag_name}'")

    # Write back to file
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print(f"Updated notebook saved: {notebook_path}")
    
    
def format_link(file_path):
    """Create a Markdown link with optional JupyterHub links."""

    title = get_heading_from_file(file_path)
    
    if title == 'Table of Contents':
        return ''
    link_line = f"[{title}]({file_path})"
    
    if file_path.endswith(".ipynb") or file_path.endswith(".py"):
        if doJubHubLinks:
            link_line += generate_jupyterhub_links(file_path)
        # add tags to cells that call certain functions
        if doTagCells:
            tag_cells(file_path)
    
    return link_line


def format_link_old(file_path):
    """Create a Markdown link with the actual heading as the title."""
    title = get_heading_from_file(file_path)
    return f"[{title}]({file_path})"

def process_chapters(chapters, indent=0):
    import os
    lines = []
    prefix = "  " * indent + "- "
    for chapter in chapters:
        if 'file' in chapter:
            file_path = chapter['file']
            if os.path.isfile(file_path):
                # print(f"The file exists: {file_path}")
                format_link_return = format_link(file_path)
                if len(format_link_return)>0:
                    lines.append(prefix + format_link_return)
            else:
                print(f"The file does NOT exist: {file_path}")
        if 'sections' in chapter:
            lines.extend(process_chapters(chapter['sections'], indent + 1))
    return lines

def generate_markdown_toc(toc_yaml_path="_toc.yml"):
    with open(toc_yaml_path, "r", encoding="utf-8") as f:
        toc = yaml.safe_load(f)

    if doAppendTOC:
        lines = ["\n## Table of Contents\n"]
    else:
        lines = ["\n# Table of Contents\n"]

    if 'parts' in toc:
        for part in toc['parts']:
            if 'caption' in part:
                if part['caption'] == 'Table of Contents':
                    continue
                if doAppendTOC:
                    lines.append(f"### {part['caption']}")
                else:
                    lines.append(f"## {part['caption']}")
            lines.extend(process_chapters(part.get('chapters', [])))
            lines.append("")
    elif 'chapters' in toc:
        lines.extend(process_chapters(toc['chapters']))

    return "\n".join(lines)


def generate_files(readme0_path="", toc_yaml_path="_toc.yml",
                   output_toc_path="generated_toc.md",
                   github_readme_path="README.md"):



    # Generate ToC
    toc_md = generate_markdown_toc(toc_yaml_path).strip()

    # Save ToC for Jupyter Book `{include}`
    with open(output_toc_path, "w", encoding="utf-8") as f:
        f.write(toc_md + "\n")
    print(f"✅ Wrote {output_toc_path}")

    # Generate GitHub-friendly README
    # Read intro
    ## you could use readme0_path = "readme0.md"
    if len(readme0_path)>0:
        with open(readme0_path, "r", encoding="utf-8") as f:
            intro = f.read().strip()   
            
        with open(github_readme_path, "w", encoding="utf-8") as f:
            if doAppendTOC:
                f.write(intro + "\n\n" + toc_md + "\n")
            else:
                f.write(intro)
        print(f"✅ Wrote {github_readme_path} (for GitHub)")

# Run the generator
if __name__ == "__main__":
    generate_files()

