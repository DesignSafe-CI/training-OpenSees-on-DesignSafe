# Step 1: Explore All Jobs
***General Queries getJobList()***

The first step in working with Tapis jobs is to **get an overview of all your past and current runs**. Using `getJobList()`, you can retrieve summary metadata such as job IDs, owners, applications used, creation dates, and statuses. This broad view is useful for:

* Building a searchable index or DataFrame of jobs,
* Filtering by status (e.g., only finished or failed jobs), and
* Deciding which jobs to examine in more detail.

Think of this as your **dashboard view**: it gives you a wide-angle snapshot of your work across Tapis before zooming into specific jobs.

---

The **getJobList()** method retrieves a list of jobs, which can be filtered using a variety of fields. This is typically your first step when exploring job data.

**Example Use:**

```python
jobs = client.jobs.getJobList()
for job in jobs:
    print(job.id, job.status, job.created)
```

Each job is returned as a **TapisResult object**, which can be inspected with:

```python
job = jobs[0]
print(dir(job))          # All attributes
print(job.__dict__)      # Dictionary view
```

---

## Queryable Fields for *getJobList()*

The *getJobList()* method does not accept all of the following fields directly, but these attributes are available on returned objects and can be filtered programmatically:

| Field             | Description                                      |
| ----------------- | ------------------------------------------------ |
| *id*              | Unique job ID                                    |
| *uuid*            | Universally unique identifier                    |
| *owner*           | Username of the job submitter                    |
| *tenant*          | Tapis tenant the job belongs to                  |
| *appId*           | Application used to launch the job               |
| *status*          | Current job status (*RUNNING*, *FINISHED*, etc.) |
| *created*         | Timestamp when job was created                   |
| *lastUpdated*     | Timestamp when job was last updated              |
| *execSystemId*    | Execution system where job ran                   |
| *archiveSystemId* | ID of archive system for outputs                 |
| *archivePath*     | Path to archived output                          |
| *parameterSet*    | Parameters and arguments submitted               |
| *tags*            | User-defined tags                                |

---

## Available Job Status Values

| Status           | Meaning               |
| ---------------- | --------------------- |
| *PENDING*        | Waiting to start      |
| *STAGING_INPUTS* | Preparing inputs      |
| *RUNNING*        | Job is active         |
| *FINISHED*       | Completed normally    |
| *FAILED*         | Failed to complete    |
| *CANCELLED*      | Cancelled by user     |
| *PAUSED*         | Paused manually       |
| *BLOCKED*        | Waiting on dependency |

---

### Sample Job Object (Example Output)

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

Note: Some fields (e.g. *startTime*, *endTime*) may be *null* if the job hasn’t started or completed.
