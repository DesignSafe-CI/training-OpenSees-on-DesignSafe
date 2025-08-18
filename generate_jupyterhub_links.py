# import os
# import yaml
# from urllib.parse import quote

# # === Configuration ===
# TOC_PATH = "_toc.yml"
# OUTPUT_MD = "open_in_jupyterhub.md"
# BASE_PREFIX = "CommunityData"  # or "MyData", "Projects" if needed

# def parse_toc(toc_path):
#     with open(toc_path, 'r') as f:
#         toc = yaml.safe_load(f)

#     def extract_files(entries):
#         files = []
#         for item in entries:
#             if isinstance(item, dict):
#                 if "file" in item:
#                     files.append(item["file"])
#                 if "sections" in item:
#                     files += extract_files(item["sections"])
#         return files

#     return extract_files(toc)

# def generate_link_block(notebook_path):
#     filename = os.path.basename(notebook_path)
#     encoded_path = quote(f"{BASE_PREFIX}/{notebook_path}.ipynb")
#     jupyterhub_url = f"https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/{encoded_path}"
#     download_link = f"{notebook_path}.ipynb"

#     return f"""### {filename}

# - [Open in DesignSafe JupyterHub]({jupyterhub_url})
# - [Download notebook]({download_link})

# """

# def main():
#     notebook_files = parse_toc(TOC_PATH)
#     link_blocks = [generate_link_block(path) for path in notebook_files if path.endswith(".ipynb") or os.path.exists(path + ".ipynb")]

#     header = "# Access Notebooks in DesignSafe JupyterHub\n\nBelow are links to open or download each notebook in this book.\n\n"
#     full_content = header + "\n".join(link_blocks)

#     with open(OUTPUT_MD, 'w') as f:
#         f.write(full_content)

#     print(f"✅ Written: {OUTPUT_MD}")

# if __name__ == "__main__":
#     main()
