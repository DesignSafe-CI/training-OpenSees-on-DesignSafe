<!-- # Querying Tapis Jobs
**Querying Tapis Jobs with Python SDK: <br>
(1) Listing Jobs → (2) Inspecting Individual Jobs → (3) Downloading Outputs and Deep Dive.**


In Tapis, there are two main ways to get job information:

1. **Listing Jobs** — to retrieve and filter multiple jobs based on metadata (using *getJobList()*).

2. **Retrieving Job Details** — to access full details, status, outputs, and logs for a specific job (using *getJob()*, *getJobStatus()*, etc).

This guide walks through both approaches using the Tapis Python SDK (Tapipy).



1. ## Listing Jobs — General Job Queries (*getJobList()*)

    The *getJobList()* method retrieves a list of jobs, which can be filtered using a variety of fields. This is typically your first step when exploring job data.
    
    **Example Use:**
    
    ```python
    jobs = client.jobs.getJobList()
    for job in jobs:
        print(job.id, job.status, job.created)
    ```
    
    Each *job* is a *TapisResult* object containing job metadata.
    
    ---
    
    ### Queryable Fields for *getJobList()*
    The getJobsList() method does not accept all of the following fields. However, you can use them to filter the TapisResult object.
    
    | Field             | Description                                      |
    | ----------------- | ------------------------------------------------ |
    | *id*              | Unique job ID                                    |
    | *owner*           | Username of the job submitter                    |
    | *tenant*          | Tapis tenant the job belongs to                  |
    | *appId*           | Application used to launch the job               |
    | *status*          | Current job status (*RUNNING*, *FINISHED*, etc.) |
    | *created*         | Timestamp when job was created                   |
    | *lastUpdated*     | Timestamp when job was last updated              |
    | *archiveSystemId* | ID of archive system for outputs                 |
    | *archivePath*     | Path to archived output                          |
    | *execSystemId*    | Execution system where job ran                   |
    | *parameterSet*    | Parameters and arguments submitted               |
    | *uuid*            | Universally unique identifier                    |
    | *tags*            | User-defined tags                                |
    
    
    ***Available Job Status Values***
    
    | Status           | Meaning              |
    | ---------------- | -------------------- |
    | *PENDING*        | Waiting to start     |
    | *STAGING_INPUTS* | Preparing inputs     |
    | *RUNNING*        | Job is active        |
    | *FINISHED*       | Completed normally   |
    | *FAILED*         | Failed to complete   |
    | *CANCELLED*      | Cancelled by user    |
    | *PAUSED*         | Paused manually      |
    | *BLOCKED*        | Blocked (dependency) |
    
    ---
    
    ### Inspect Available Attributes
    
    After retrieving jobs:
    
    ```python
    job = jobs[0]
    print(dir(job))          # All attributes
    print(job.__dict__)      # Dictionary view
    ```
    
    ---
    
    ### Sample Job Object (Example Output)
    
    Here’s a representative job object returned by *getJobList()*:
    
    ```json
    {
      "id": "myuser-job-abc123",
      "uuid": "e76db0e1-f5b5-4b0a-882a-8a74fa30e9f0",
      "tenant": "tacc",
      "owner": "myuser",
      "appId": "my-app-1.0.0",
      "status": "FINISHED",
      "created": "2025-05-01T12:34:56.000Z",
      "execSystemId": "tacc-exec-01",
      "archiveSystemId": "tacc-archive-01",
      "archivePath": "myuser/jobs/myuser-job-abc123",
      "parameterSet": {
        "appArgs": [
          { "arg": "--input", "name": "inputFile", "value": "data.txt" }
        ]
      },
      "tags": ["projectA", "experiment1"],
      "inputs": {
        "inputFile": "tacc://tacc-storage/data/input/data.txt"
      },
      "nodeCount": 1,
      "coresPerNode": 4,
      "memoryMB": 8192
    }
    ```
    
    Note: Some fields (e.g. *startTime*, *endTime*) may be *null* if job hasn’t started or completed.

1. ## Inspecting a Specific Job — Deep Dive (*getJob()* and related)

    Once you know a job's ID, you can retrieve complete details using *getJob()*.
    

    Retrieves full metadata for a single job.
    
    ```python
    job = client.jobs.getJob(job_id='myuser-job-abc123')
    print(job.status, job.appId, job.created)
    ```
    
    Returns full configuration, including:
    
    * Job metadata
    * App parameters
    * Execution system
    * Archive system
    * Resource usage (nodes, memory, cores)
    
    ---
    
    ### Other Detailed Retrieval Methods
    
    | Method                               | Description                         | Use Case         |
    | ------------------------------------ | ----------------------------------- | ---------------- |
    | *getJobStatus(job_id)*               | Lightweight status only             | Poll job status  |
    | *getJobHistory(job_id)*              | Full job lifecycle (status changes) | Debug or audit   |
    | *getJobOutputList(job_id)*           | List archived output files          | Browse results   |
    | *getJobOutputDownload(job_id, path)* | Download specific output file       | Retrieve results |
    
    ---
    
    #### Example Usage:
    
    ```python
    # Check job status
    status = client.jobs.getJobStatus(job_id)
    print(status.status)
    
    # See job history
    history = client.jobs.getJobHistory(job_id)
    for event in history:
        print(event.status, event.timestamp)
    
    # List output files
    files = client.jobs.getJobOutputList(job_id)
    for f in files:
        print(f.name, f.size)
    
    # Download output file
    file_content = client.jobs.getJobOutputDownload(job_id, path="results/output.txt")
    with open("output.txt", "wb") as f:
        f.write(file_content)
    ```
    
    
    ## Quick Summary Table
    
    | Purpose              | Use This Command           |
    | -------------------- | -------------------------- |
    | **List jobs**        | *getJobList()*               |
    | **Full job details** | *getJob(job_id)*           |
    | **Status only**      | *getJobStatus(job_id)*     |
    | **Job lifecycle**    | *getJobHistory(job_id)*    |
    | **List outputs**     | *getJobOutputList(job_id)* |
    | **Download file**    | *getJobOutputDownload()*   |
    
    ---

## Best Practice Workflow:

1. Use *getJobList()* to find jobs.
2. Use *getJob()* or *getJobStatus()* to drill into a job.
3. Use *getJobOutputList()* and *getJobOutputDownload()` to retrieve results. -->