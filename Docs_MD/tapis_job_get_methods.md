<!-- # Tapis Job Retrieval Methods

Here's a **detailed breakdown of the various `getJob...` and related job-fetching methods** available in the **Tapis v3 Python SDK** (`tapis3`) under the **Jobs API**.

These commands are used to **retrieve detailed information about specific jobs**, not to list/filter many jobs (that's what `listJobs()` is for).

---

## Overview: Tapis Job Retrieval Methods

### Primary methods include:

| Method                   | Description                                      |
| ------------------------ | ------------------------------------------------ |
| `getJob()`               | Get full details of a specific job by ID         |
| `getJobStatus()`         | Get the current status (only) of a job           |
| `getJobOutputList()`     | List files in the job's archived output          |
| `getJobOutputDownload()` | Download a specific output file                  |
| `getJobRequest()`        | View the original job request (input)    (NOT AVAILABLE)         |
| `getJobHistory()`        | Retrieve the job's status history (timeline)     |
| `getJobPermissions()`    | Get access permissions for a job          (NOT AVAILABLE)        |
| `getJobSearch()`         | (Advanced) Query jobs via a backend search index  (NOT AVAILABLE)|



1. ## **getJob(job_id)**
    
    ### Purpose:
    
    Get **all available metadata and configuration details** for a specific job.
    
    ### Example:
    
    ```python
    job = client.jobs.getJob(job_id='myuser-job-abc123')
    print(job.status, job.appId, job.created)
    ```
    
    This returns the full job object, including:
    
    * Metadata (ID, appId, owner)
    * Parameters and inputs
    * Execution and archive info
    * Resource usage (memory, cores, etc.)
    
    
    **Common Queryable Fields**
    These fields can be accessed from job objects returned by *listJobs()*:
    
    | Field             | Description                                                           |
    | ----------------- | --------------------------------------------------------------------- |
    | `id`              | Unique job ID                                                         |
    | `owner`           | Username of the job submitter                                         |
    | `tenant`          | Tapis tenant the job belongs to                                       |
    | `appId`           | ID of the application the job is based on                             |
    | `status`          | Current job status (e.g., `PENDING`, `RUNNING`, `FINISHED`, `FAILED`) |
    | `created`         | Timestamp when job was created                                        |
    | `lastUpdated`     | Timestamp when job was last modified                                  |
    | `archiveSystemId` | ID of the system where job output is archived                         |
    | `archivePath`     | Path to archived output                                               |
    | `execSystemId`    | Execution system used to run the job                                  |
    | `ownerString`     | Same as `owner`, often used in filters                                |
    | `parameterSet`    | Parameters passed to the job                                          |
    | `uuid`            | Universally unique identifier                                         |
    | `parentUuid`      | UUID of a parent job (for child/sub-jobs)                             |
    | `tags`            | List of user-defined tags on the job                                  |
    
    
    
    **Job Status Values (for Filtering)**
    
    Common values you can use for the `status` field:
    
    * `PENDING`
    * `STAGING_INPUTS`
    * `RUNNING`
    * `FINISHED`
    * `FAILED`
    * `CANCELLED`
    * `PAUSED`
    * `BLOCKED`
    
    You can filter jobs by status like:
    
    ```python
    jobs = client.jobs.listJobs(status='FINISHED')
    ```
    
    Or via search:
    
    ```python
    search_query = json.dumps({"status": "FAILED"})
    jobs = client.jobs.listJobs(search=search_query)
    ```

1. ## **getJobStatus(job_id)**
    
    ### Purpose:
    
    Get the **current status only** (lightweight version of `getJob()`).
    
    ### Example:
    
    ```python
    status = client.jobs.getJobStatus(job_id='myuser-job-abc123')
    print(status.status, status.message)
    ```
    
    Useful for lightweight polling.

1. ## **getJobOutputList(job_id)**

    ### Purpose:
    
    List the **files** that were archived after the job finished.
    
    ### Example:
    
    ```python
    files = client.jobs.getJobOutputList(job_id='myuser-job-abc123')
    for f in files:
        print(f.name, f.size, f.lastModified)
    ```
    
    Returns a list of file objects with:
    
    * `name`
    * `size`
    * `lastModified`

1. ## **getJobOutputDownload(job_id, path)**
    
    ### Purpose:
    
    **Download a specific file** from a job's archive output.
    
    ### Example:
    
    ```python
    output_file = client.jobs.getJobOutputDownload(
        job_id='myuser-job-abc123',
        path='results/output.txt'
    )
    
    # Save the file locally
    with open("output.txt", "wb") as f:
        f.write(output_file)
    ```
    
    You must know the relative path from `getJobOutputList()`.


1. ## **getJobHistory(job_id)**
    
    ### Purpose:
    
    Retrieve a **timestamped history** of the job’s lifecycle (status changes).
    
    ### Example:
    
    ```python
    history = client.jobs.getJobHistory(job_id='myuser-job-abc123')
    for event in history:
        print(event.status, event.timestamp)
    ```
    
    Useful for analyzing job execution progress.
   

## Quick Summary Table

| Method                   | Returns                | Use Case                     |
| ------------------------ | ---------------------- | ---------------------------- |
| `getJob()`               | Full job object        | Inspect all details          |
| `getJobStatus()`         | Status + message       | Lightweight polling          |
| `getJobOutputList()`     | File list              | Browse archived results      |
| `getJobOutputDownload()` | File binary            | Download output              |
| `getJobHistory()`        | Status change history  | Debugging or visualization   |



## Sample Workflow (All Together)

```python
job_id = "myuser-job-abc123"

# Get metadata
job = client.jobs.getJob(job_id)
print(f"Job {job.id} on app {job.appId} - Status: {job.status}")

# Check history
history = client.jobs.getJobHistory(job_id)
for h in history:
    print(h.status, h.timestamp)

# See outputs
files = client.jobs.getJobOutputList(job_id)
print("Archived files:")
for f in files:
    print(f.name)

# Download output
file_content = client.jobs.getJobOutputDownload(job_id, path="results/output.txt")
with open("output.txt", "wb") as f:
    f.write(file_content)
```

 -->