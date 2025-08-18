# def submit_tapis_job(t,job_description,askConfirmJob = True):
#     """
#     Submits a job to the Tapis jobs service, with optional interactive confirmation.

#     This function uses the provided authenticated Tapis client to submit a job defined
#     by the `job_description` dictionary. By default, it prompts the user to confirm
#     submission, which helps avoid accidental job launches.

#     If the user confirms, it submits the job, prints the assigned job UUID, and
#     records the local submission time.

#     Parameters
#     ----------
#     t : object
#         An authenticated Tapis client instance (e.g., from `tapis3`).
#     job_description : dict
#         A dictionary specifying the Tapis job to submit, typically produced by
#         `get_tapis_job_description()` or similar helper.
#     askConfirmJob : bool, optional
#         If True (default), prompts the user to confirm submission. If False,
#         submits immediately without asking.

#     Returns
#     -------
#     list
#         If submission proceeds, returns a list:
#             [jobUuid (str), submitted_job (object), job_start_time (float)]
#         - jobUuid: UUID string of the submitted job.
#         - submitted_job: full job object returned by Tapis.
#         - job_start_time: epoch time of submission (from `time.time()`).

#         If submission is canceled, prints a notice and returns:
#             ['', 0]

#     Prints
#     ------
#     Messages indicating whether submission was confirmed, cancelled, or completed,
#     along with the assigned Tapis job UUID.

#     Example
#     -------
#     >>> job_info = submit_tapis_job(t, job_description)
#     >>> if job_info:
#     ...     jobUuid, submitted_job, job_start_time = job_info
#     ...     print("Job UUID:", jobUuid)
#     """
#     # Silvia Mazzoni, 2025
#     import time
#     #askConfirmJob; # make false if you definitly want to submit without user confirmation.
#     if askConfirmJob:
#         ConfirmJob = input(f'Are you sure you want to submit the job? (press n to cancel, any key to confirm): ')
#     else:
#         ConfirmJob = 'y' ;
    
#     # GO!
#     if len(ConfirmJob)>0 and ConfirmJob.lower()[0] == 'n':
#         print('okey, bye!')
#         submitted_job = ''
#         jobUuid = 0
#     else:
#         # Submit job
#         print("Submitting Job")
#         submitted_job = t.jobs.submitJob(**job_description)
#         jobUuid=submitted_job.uuid
#         print(f"Job submitted! ID: {jobUuid}")
#         job_start_time = time.time()
#         # print(f"Job Start Time: {job_start_time}")
#         return [jobUuid,submitted_job,job_start_time]