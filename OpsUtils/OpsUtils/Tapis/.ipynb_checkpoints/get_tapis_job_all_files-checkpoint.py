def get_tapis_job_all_files(
    t, jobUuid, 
    displayIt=10, 
    target_dir=False, 
    overwrite=False,
    display_file_content=True
):
    """
    Recursively retrieves all output files from a Tapis job, optionally downloading them.

    This function connects to the Tapis job output system, traverses the job's complete 
    output directory structure recursively, and collects:

    - Local-style relative file paths (to recreate directory structure on disk),
    - Full absolute Tapis paths for direct API use or metadata,
    - Raw item objects returned by Tapis (which include size, lastModified, etc.),
    - The total file count.

    It can also automatically download these files into a local directory, preserving
    the folder hierarchy.

    Parameters
    ----------
    t : Tapis
        An authenticated Tapis client object (typically created with connect_tapis()).

    jobUuid : str
        The UUID of the Tapis job whose output files you want to inspect or download.

    displayIt : bool or int, optional
        Controls printed output:
            - False or 0: completely silent.
            - True or 1: prints all files in all directories.
            - int >= 2: prints at most `displayIt` files per directory,
                        then indicates suppression.

    target_dir : bool, None, or str, optional
        Determines whether to download files:
            - False or None: does not download files, only lists them.
            - True: downloads files into a default directory './OutFiles_{jobUuid}'.
            - str: downloads files into the specified local directory.

    overwrite : bool, optional
        If True, overwrites existing local files. If False (default), skips already
        existing files.

    Returns
    -------
    dict
        {
            'Nfiles': total number of files found,
            'LocalPath': list of relative paths (like 'results/output.txt'),
            'FullPath': list of absolute Tapis paths (like '/tapis/jobs/v2/...'),
            'Items': list of raw Tapis file objects (metadata)
        }

    Examples
    --------
    # Just list files, print up to 5 per directory
    >>> outputs = get_tapis_job_all_files(t, jobUuid, displayIt=5)

    # List all files without printing anything
    >>> outputs = get_tapis_job_all_files(t, jobUuid, displayIt=False)

    # Download into default './OutFiles_{jobUuid}'
    >>> outputs = get_tapis_job_all_files(t, jobUuid, target_dir=True)

    # Download into a custom directory, overwriting if needed
    >>> outputs = get_tapis_job_all_files(t, jobUuid, target_dir="my_results", overwrite=True)

    Notes
    -----
    - Downloads replicate the Tapis directory structure inside the chosen local folder.
    - Use 'LocalPath' and 'FullPath' together to pair local save paths with original remote locations.
    - The 'Items' list provides full Tapis metadata for each file, which can be useful for logs.
    """
    # Silvia Mazzoni, 2025

    import os
    import OpsUtils
    def view_tapis_file_in_accordion(selected_path):
        import ipywidgets as widgets
        from IPython.display import display, clear_output

        
    
        view_select_out = widgets.Output()
        view_select_out_acc = widgets.Accordion(children=[view_select_out])
        view_select_out_acc.set_title(0, f" View File: {selected_path}")
        # view_select_out_acc.selected_index = 0
        display(view_select_out_acc)
        with view_select_out:
            if not os.path.splitext(selected_path)[-1] in ['.zip','.ZIP']:
                clear_output()
                if selected_path:
                    local_file = selected_path.split('/')[-1]
                    # print('selected_path',selected_path)
                    data = t.jobs.getJobOutputDownload(jobUuid=jobUuid, outputPath=selected_path)
                    print(f" Viewing: {selected_path}")
                    textarea = widgets.Textarea(
                        value=data,
                        placeholder='',
                        description='',
                        disabled=False,
                        layout=widgets.Layout(width='100%', height='500px')
                    )
                    display(textarea)
                else:
                    print(" No output file selected to download.")
            else:
                print("can't display content")


    # normalize displayIt
    if isinstance(displayIt, bool):
        displayLevel = 1 if displayIt else 0
        displayLimit = None
    elif isinstance(displayIt, int):
        displayLevel = 1
        displayLimit = displayIt if displayIt >= 2 else None
    else:
        displayLevel = 0
        displayLimit = None    

    if displayLevel>=1:
        import ipywidgets as widgets
        from IPython.display import display, clear_output
        from OpsUtils import OpsUtils
        filedata_out = widgets.Output()
        filedata_accordion = widgets.Accordion(children=[filedata_out])
        filedata_accordion.set_title(0, f'Job Filedata   ({jobUuid})')
        filedata_accordion.selected_index = 0
        display(filedata_accordion)
        
    if displayLevel>=1:
        with filedata_out:
            print('----------------------------')
            print(f'JOB: {jobUuid}')
            print('----------------------------')
    
    # determine local download dir
    if target_dir is True:
        download_dir = f"./OutFiles_{jobUuid}"
    elif isinstance(target_dir, str):
        download_dir = target_dir
    else:
        download_dir = None  # no download

    if displayLevel>=1:
        if download_dir != None:
            with filedata_out:
                print('----------------------------')
                print(f'TARGET DIR: {download_dir}')
                print('----------------------------')
    view_direct_out = widgets.Output()
    def get_files_recursive(view_direct_out,path=""):
        Nfiles = 0
        returnFiles = []
        returnFilesPath = []
        returnItems = []

        output_path = path if path else "."
        output_items = t.jobs.getJobOutputList(jobUuid=jobUuid, outputPath=output_path)

        # split into dirs vs files
        output_items_dirs = [item for item in output_items if getattr(item, "type", "") == "dir"]
        output_items_files = [item for item in output_items if getattr(item, "type", "") != "dir"]
        output_items_ordered = output_items_files + output_items_dirs

        
        printed_count = 0
        Nstopp = 0
        hereDisplay = True
        if displayLevel >= 1:
            if len(output_items_files)>0:
                firstCase = output_items_files[0].path
                dirr = os.path.dirname(firstCase)
                with view_direct_out:
                    print(f' {dirr}')
            with view_direct_out:
                print(f'  {len(output_items_files)} files & {len(output_items_dirs)} directories:')
            print(f'      {len(output_items_files)} files & {len(output_items_dirs)} directories')

        for item in output_items_ordered:
            remote_path = os.path.join(path, item.name) if path else item.name

            if getattr(item, "type", "") == "dir":
                if displayLevel >= 1:
                    # print('----------------------------')
                    # print(f'DIRECTORY: {remote_path}')
                    # print(f'DIRECTORY: {remote_path}\n{item.path}')
                    view_direct_out = widgets.Output()
                    view_direct_out_acc = widgets.Accordion(children=[view_direct_out])
                    view_direct_out_acc.set_title(0, f"DIRECTORY: {remote_path}")
                    # view_direct_out_acc.selected_index = 0
                    display(view_direct_out_acc)

                Nhere, hereFiles, hereFilesPath, hereItems = get_files_recursive(view_direct_out,remote_path)
                Nfiles += Nhere
                returnFiles.extend(hereFiles)
                returnFilesPath.extend(hereFilesPath)
                returnItems.extend(hereItems)
            else:
                returnFiles.append(remote_path)
                returnFilesPath.append(item.path)
                returnItems.append(item)
                Nfiles += 1

                # print tree
                if displayLevel >= 1 and (displayLimit is None or printed_count < displayLimit):
                    with view_direct_out:
                        if not download_dir:
                            if display_file_content:
                                view_tapis_file_in_accordion(remote_path)
                            else:
                                print(f'    FILE: {remote_path}')
                        printed_count += 1
                        if displayLimit is not None and printed_count == displayLimit:
                            Nstopp = Nfiles

                # download if needed
                if download_dir:
                    # print('download_dir',download_dir)
                    # print('remote_path',remote_path)
                    local_file_path = os.path.join(download_dir, remote_path)
                    homePath = os.path.expanduser('~')
                    local_file_path = os.path.join(homePath, local_file_path)
                    local_dir = os.path.dirname(local_file_path)
                    # print('local_file_path',local_file_path)
                    # print('local_dir',local_dir)
                    os.makedirs(local_dir, exist_ok=True)

                    if os.path.exists(local_file_path) and not overwrite:
                        if hereDisplay:
                            print(f"    [SKIP] {local_file_path} (already exists)")
                        continue

                    if hereDisplay:
                        print(f"        [DOWNLOADING] {remote_path} -> {local_file_path}")
                    data = t.jobs.getJobOutputDownload(jobUuid=jobUuid, outputPath=remote_path)
                    with open(local_file_path, "wb") as f:
                        f.write(data)

                if displayLevel >= 1 and hereDisplay and Nstopp != 0:
                    print(f'\n          ........(suppressing additional-file display beyond {displayLimit})')
                    hereDisplay = False

        
        
        return Nfiles, returnFiles, returnFilesPath, returnItems

    if displayIt:
        with filedata_out:
            print('----------------------------')
            print('DIRECTORY: "."')
            view_direct_out = widgets.Output()
            view_direct_out_acc = widgets.Accordion(children=[view_direct_out])
            view_direct_out_acc.set_title(0, f'DIRECTORY: "."')
            # view_direct_out_acc.selected_index = 0
            display(view_direct_out_acc)
            Nfiles, FileList, FilesPathList, itemsList = get_files_recursive(view_direct_out)
    else:
        Nfiles, FileList, FilesPathList, itemsList = get_files_recursive(view_direct_out)

    if displayIt:
        with filedata_out:
            print(f"\nA total of {Nfiles} job-output files have been found"
                  f"{' and downloaded' if download_dir else ''}"
                "!")

    return {
        'Nfiles': Nfiles,
        'LocalPath': FileList,
        'FullPath': FilesPathList,
        'Items': itemsList
    }
