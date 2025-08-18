def show_text_file_in_accordion(folderPathList, filenameList, background='#d4fbff'):
    """
    Search for specified text files in one or more folders (recursively) and display
    each found file inside a collapsible accordion block in a Jupyter notebook,
    with a copy-to-clipboard button.

    Parameters
    ----------
    folderPathList : str or list of str
        Path(s) to folders to search through (recursively). Accepts a single string 
        or a list of strings. '~' is expanded to the user home.

    filenameList : str or list of str
        Names of files to look for. Accepts a single string or a list of strings.

    background : str, default='#d4fbff'
        Background color for the file content area.

    Returns
    -------
    None
        Displays formatted HTML blocks with copy buttons directly in the notebook output.

    Example
    -------
    show_text_file_in_accordion("~/MyProjects/ProjectA", ["slurm.sub", "params.json"])

    Author
    ------
    Silvia Mazzoni, DesignSafe (silviamazzoni@yahoo.com)

    Date
    ----
    2025-08-14

    Version
    -------
    1.0
    """

    from IPython.display import display, HTML
    import os
    import uuid

    if isinstance(folderPathList, str):
        folderPathList = [folderPathList]
    if isinstance(filenameList, str):
        filenameList = [filenameList]

    for folderPath in folderPathList:
        folderPath = os.path.expanduser(folderPath)
        for root, _, files in os.walk(folderPath):
            for thisFilename in filenameList:
                if thisFilename in files:
                    filepath = os.path.join(root, thisFilename)
                    try:
                        with open(filepath, "r", encoding="utf-8") as file:
                            content = file.read()
                    except Exception as e:
                        continue

                    unique_id = uuid.uuid4().hex  # unique id for each block to attach copy

                    html = f"""
                      <details style="margin-top:1em; font-family:monospace; background:white; 
                          padding:0.25em; border-radius:6px; border:1px solid #ccc;">
                        <summary style="cursor:pointer; font-weight:bold; background:white; 
                          padding:0.3em 0.5em; border-radius:4px;">{thisFilename}</summary>

                        <button onclick="navigator.clipboard.writeText(document.getElementById('{unique_id}').innerText)">
                          📋 Copy
                        </button>
                        <pre id="{unique_id}" style="white-space:pre-wrap; margin:0.25em 0 0 0; 
                            background:{background}; padding:.3em; border-radius:5px;">
<b># {filepath}</b>\n{content}</pre>
                      </details>
                    """
                    display(HTML(html))
