# TapisJob Schema
Here's a **full example schema** of a typical **Tapis job object** as returned by the `client.jobs.listJobs()` method in the Python SDK.

This will help you see exactly what fields are available for inspection, filtering, or display.



## Full Tapis Job Object Schema (Example Output)

Here's a **full example schema** of a typical **Tapis job object** as returned by the `client.jobs.listJobs()` method in the Python SDK.

This will help you see exactly what fields are available for inspection, filtering, or display.

Below is a **representative example** of a `TapisResult` job object, with typical fields and values you'd encounter:

```json
{
  "id": "myuser-job-abc123",
  "uuid": "e76db0e1-f5b5-4b0a-882a-8a74fa30e9f0",
  "tenant": "tacc",
  "owner": "myuser",
  "appId": "my-app-1.0.0",
  "appVersion": "1.0.0",
  "description": "Test job submission",
  "created": "2025-05-01T12:34:56.000Z",
  "lastUpdated": "2025-05-01T12:40:12.000Z",
  "status": "FINISHED",
  "startTime": "2025-05-01T12:35:00.000Z",
  "endTime": "2025-05-01T12:40:00.000Z",
  "execSystemId": "tacc-exec-01",
  "archiveSystemId": "tacc-archive-01",
  "archivePath": "myuser/jobs/myuser-job-abc123",
  "archiveUrl": "https://tapis.io/jobs/v3/media/myuser/job-abc123/output",
  "parameterSet": {
    "appArgs": [
      { "arg": "--input", "name": "inputFile", "value": "data.txt" }
    ],
    "schedulerOptions": [],
    "envVariables": [],
    "archiveFilter": {}
  },
  "tags": ["projectA", "experiment1"],
  "notes": {
    "description": "Initial run of experiment",
    "dataSource": "HPC"
  },
  "inputs": {
    "inputFile": "tacc://tacc-storage/data/input/data.txt"
  },
  "fileInputs": [],
  "execSystemExecDir": "/work/myuser/jobs/myuser-job-abc123",
  "execSystemInputDir": "/work/myuser/input",
  "execSystemOutputDir": "/work/myuser/output",
  "parentUuid": null,
  "childJobs": [],
  "isMpi": false,
  "mpiCmd": null,
  "maxMinutes": 30,
  "nodeCount": 1,
  "coresPerNode": 4,
  "memoryMB": 8192,
  "archiveOnAppError": true,
  "createdBy": "myuser",
  "updatedBy": "myuser",
  "sharedAppCtx": false
}
```

> ⚠️ **Note:** Not every job will include every field — for example, `startTime`, `endTime`, or `childJobs` might be `null` if the job hasn’t started or isn’t part of a workflow.



## Common Fields to Query or Use

| Field                                            | Description                             | Useful For                            |
| ------------------------------------------------ | --------------------------------------- | ------------------------------------- |
| `id`, `uuid`                                     | Identifiers                             | Referencing or querying specific jobs |
| `owner`                                          | Username who submitted the job          | Filtering jobs by user                |
| `status`                                         | Job state (`RUNNING`, `FINISHED`, etc.) | Monitoring job lifecycle              |
| `appId`                                          | App used to launch the job              | Grouping by application               |
| `created`, `lastUpdated`, `startTime`, `endTime` | Timestamps                              | Time-based queries                    |
| `execSystemId`                                   | Where the job ran                       | Auditing resources                    |
| `archiveSystemId`, `archivePath`                 | Where output is stored                  | Accessing results                     |
| `tags`                                           | User-defined labels                     | Custom grouping or search             |
| `notes`                                          | Optional metadata                       | Storing job context or purpose        |
| `parameterSet`, `inputs`                         | Input args and files                    | Reproducibility and debugging         |



## Accessing in Python

When you call:

```python
jobs = client.jobs.listJobs()
```

Each `job` in `jobs` is a `TapisResult` object. You can access fields like:

```python
for job in jobs:
    print(job.id, job.status, job.created)
    print(job.parameterSet.appArgs)
```

Or convert to a dictionary for flexible use:

```python
job_dict = job.__dict__
print(job_dict["appId"])
```
