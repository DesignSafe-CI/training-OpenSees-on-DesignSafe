def view_tapis_file_in_accordion(selected_path):
    import ipywidgets as widgets
    from IPython.display import display, clear_output

    view_select_out = widgets.Output()
    view_select_out_acc = widgets.Accordion(children=[view_select_out])
    view_select_out_acc.set_title(0, f" View: {selected_path}")
    view_select_out_acc.selected_index = 0
    display(view_select_out_acc)
    with view_select_out:
        clear_output()
        if selected_path:
            local_file = selected_path.split('/')[-1]
            # print('selected_path',selected_path)
            jobUuid = uuid_dropdown.value
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
