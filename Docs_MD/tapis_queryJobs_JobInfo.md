# Step 2: Inspect a Specific Job
***A Deep Dive into a Specific Job***

Once you’ve identified a job of interest from your list, the next step is to **drill down into its details**. Tapis provides several functions for this, depending on how much information you need:

* `getJob(job_id)` — returns the full configuration and metadata.
* `getJobStatus(job_id)` — retrieves only the current status (lightweight polling).
* `getJobHistory(job_id)` — shows a timestamped lifecycle of state changes.

These functions allow you to **trace how a job was submitted, how it ran, and how it ended**, making them essential for debugging, auditing, and performance tuning.

---

Once you know a job’s ID, you can retrieve complete details or lighter-weight status information.

## Primary Retrieval Methods

| Method                   | Description                                     | Typical Use                 |
| ------------------------ | ----------------------------------------------- | --------------------------- |
| *getJob(job_id)*         | Full details of a specific job by ID            | Inspect config and metadata |
| *getJobStatus(job_id)*   | Lightweight status only                         | Poll status                 |
| *getJobHistory(job_id)*  | Lifecycle history of status changes             | Debug or audit              |
| *getJobOutputList()*     | List files in the job’s archived output         | Browse results              |
| *getJobOutputDownload()* | Download a specific output file                 | Retrieve results            |

---

## *getJob(job_id)*

### Purpose:
Retrieve **all available metadata and configuration** for a specific job.

### Example:
```python
job = client.jobs.getJob(job_id="myuser-job-abc123")
print(job.status, job.appId, job.created)
```

Returns full configuration, including:
* Job metadata
* App parameters
* Execution system
* Archive system
* Resource usage (nodes, memory, cores)

### Common Queryable Fields
These fields can be accessed from job objects returned by *listJobs()*:

| Field             | Description                                                           |
| ----------------- | --------------------------------------------------------------------- |
| *id*              | Unique job ID                                                         |
| *owner*           | Username of the job submitter                                         |
| *tenant*          | Tapis tenant the job belongs to                                       |
| *appId*           | ID of the application the job is based on                             |
| *status*          | Current job status (e.g., *PENDING*, *RUNNING*, *FINISHED*, *FAILED*) |
| *created*         | Timestamp when job was created                                        |
| *lastUpdated*     | Timestamp when job was last modified                                  |
| *archiveSystemId* | ID of the system where job output is archived                         |
| *archivePath*     | Path to archived output                                               |
| *execSystemId*    | Execution system used to run the job                                  |
| *ownerString*     | Same as *owner*, often used in filters                                |
| *parameterSet*    | Parameters passed to the job                                          |
| *uuid*            | Universally unique identifier                                         |
| *parentUuid*      | UUID of a parent job (for child/sub-jobs)                             |
| *tags*            | List of user-defined tags on the job                                  |



### Job Status Values (for Filtering)

Common values you can use for the *status* field:

* *PENDING*
* *STAGING_INPUTS*
* *RUNNING*
* *FINISHED*
* *FAILED*
* *CANCELLED*
* *PAUSED*
* *BLOCKED*

You can filter jobs by status like:

```python
jobs = client.jobs.listJobs(status='FINISHED')
```

Or via search:

```python
search_query = json.dumps({"status": "FAILED"})
jobs = client.jobs.listJobs(search=search_query)
```
---

## *getJobStatus(job_id)*

### Purpose:
Get the **current status only**.

### Example:
```python
status = client.jobs.getJobStatus(job_id="myuser-job-abc123")
print(status.status, status.message)
```

Lightweight — ideal for polling loops.

---

## *getJobHistory(job_id)*

### Purpose:
Retrieve a **timestamped history** of job status changes.

### Example:
```python
history = client.jobs.getJobHistory(job_id="myuser-job-abc123")
for event in history:
    print(event.status, event.timestamp)
```

Useful for debugging, auditing, or analyzing runtime progression.

