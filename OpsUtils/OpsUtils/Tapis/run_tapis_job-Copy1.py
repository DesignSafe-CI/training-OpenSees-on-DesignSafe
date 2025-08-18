def run_tapis_job(t,tapisInput,askConfirmJob = True,
                  monitor_job=True,askConfirmMonitorRT=True,
                  get_job_history=False,get_job_metadata=False,get_job_filedata = False
                 ):
    """
    Runs a full Tapis job workflow in one call: build description, submit, monitor, get history, and metadata.

    This is a convenience wrapper that automates the typical workflow:
        1. Builds the job description from `tapisInput`.
        2. Submits the job (optionally confirming with the user).
        3. Monitors the job in real-time (optional).
        4. Retrieves and prints the job history (optional).
        5. Prints metadata and tries to reconstruct local archive directory (optional).

    Parameters
    ----------
    t : object
        An authenticated Tapis client instance (e.g., from `tapis3`).
    tapisInput : dict
        Input dictionary containing job parameters (name, appId, etc.), typically
        used by `get_tapis_job_description()`.
    askConfirmJob : bool, optional
        If True (default), asks for confirmation before submitting the job.
    monitor_job : bool, optional
        If True (default), monitors the job status in real-time after submission.
    askConfirmMonitorRT : bool, optional
        If True (default), asks for confirmation before starting real-time monitoring.
    get_job_history : bool, optional
        If True (-), retrieves and prints the job history after monitoring.
    get_job_metadata : bool, optional
        If True (-), prints metadata and tries to reconstruct local archive info.
    get_job_filedata: bool, optional
        If True (-), prints file contents

    Returns
    -------
    list
        A list of results:
            [jobUuid, job_description, submitted_job, job_start_time, JobHistory, archiveSystemDir]
        - jobUuid : str, UUID of the submitted job.
        - job_description : dict, input job description.
        - submitted_job : object, full Tapis job object.
        - job_start_time : float, local epoch time of submission.
        - JobHistory : object or dict, job history data if retrieved.
        - archiveSystemDir : str or dict, local archive info if retrieved.

    Example
    -------
    >>> [jobUuid, desc, submitted, start_time, history, archive] = run_tapis_job(t, tapisInput)
    >>> print("Job UUID:", jobUuid)
    """
    # Silvia Mazzoni, 2025
    from OpsUtils import OpsUtils
    import os
    job_description = OpsUtils.get_tapis_job_description(t,tapisInput)
    if job_description==-1:
        return {'runJobStatus':'Incomplete'}
    returnDict = OpsUtils.submit_tapis_job(t,job_description,askConfirmJob)
    if returnDict['runJobStatus'] == 'Finished':
        print('job_start_time:',returnDict['job_start_time'])
        jobUuid = returnDict['jobUuid']
        JobHistory = {}
        JobMetadata = {}
        JobFiledata = {}
        if monitor_job:
            OpsUtils.monitor_tapis_job(t,jobUuid,returnDict['job_start_time'],askConfirmMonitorRT)
            JobMetadata = OpsUtils.get_tapis_job_status(t,jobUuid,tapisInput)
            if get_job_metadata:
                JobMetadata = OpsUtils.get_tapis_job_metadata(t,jobUuid,tapisInput)
            if get_job_history:
                JobHistory = OpsUtils.get_tapis_job_history_data(t,jobUuid)
            if get_job_filedata:
                JobFiledata = OpsUtils.get_tapis_job_all_files(t,jobUuid)
    
    
    
          
        # print('Done!')
        returnDict['job_description'] = job_description
        returnDict['JobHistory'] = JobHistory
        returnDict['JobMetadata'] = JobMetadata
        returnDict['JobFiledata'] = JobFiledata
        returnDict['runJobStatus'] = 'Finished'

    
    return returnDict