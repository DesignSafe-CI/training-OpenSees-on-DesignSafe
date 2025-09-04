# Process Overview
**Submitting to OpenSeesMP using Tapipy (Python)**

This example illustrates the workflow for submitting a parallel **OpenSeesMP** job to **TACC Stampede3** using the **Tapis Python SDK (Tapipy)**.

> This example is intended as a conceptual guide rather than a ready-to-run script. The commands demonstrate the overall process, but may require modification to work in your environment.


## Prerequisites

Before you begin:

* You have a **DesignSafe account**
* You are configured to use the **TACC Tapis tenant**
    Being configured for a tenant (e.g. tacc) means your CLI or SDK knows:
    * Where to authenticate (https://tacc.tapis.io)
    * What tenant-specific APIs you’ll be using (app)
    These are part of obtaining the access token, which has been shown elsewhere in the documentation.
* You’ve obtained an **access token** and instantiated a `Tapis` client
* Your **input folder** is already uploaded to a Tapis-accessible system like `designsafe.storage.default`

## Example Input Directory Structure

Let’s assume you uploaded the following folder to your storage:

```
designsafe.storage.default:/myuser/projects/opensees-tests/run01/
├── model.tcl
├── loads/ground1.at2
└── params.txt
```

## Submit a Job Using Tapipy

```python
from tapipy.tapis import Tapis
from datetime import datetime

# Step 1: Connect to the Tapis API
t = Tapis(
    base_url="https://tacc.tapis.io",
    access_token="your_access_token"
)

# Step 2: Define the job details
job = t.jobs.submitJob({
    "name": f"openseesMP-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
    "appId": "opensees-mp-s3",
    "version" : "latest",
    "nodeCount": 2,
    "coresPerNode": 48,
    "maxMinutes": 120,
    "inputs": {
        "inputDirectory": "designsafe.storage.default:/myuser/projects/opensees-tests/run01"
    },
    "parameters": {
        "Main Script": "model.tcl"
    }
})

print(f"Submitted job ID: {job.id}")
```

## Important Notes

| Field                        | Explanation                                                             |
| ---------------------------- | ----------------------------------------------------------------------- |
| `appId`                      | Must match the registered ID for the OpenSeesMP app: `"opensees-mp-s3"` |
| `inputDirectory`             | Full Tapis URI to your input directory — must exist                     |
| `Main Script`                | Exact filename of your `.tcl` file within that directory                |
| `nodeCount` & `coresPerNode` | Define how many Stampede3 resources your job will use                   |
| `maxMinutes`                 | Job wall time (you may adjust as needed)                                |

## Monitoring the Job

You can track or inspect your job via Tapipy:

```python
# List jobs submitted by your user
t.jobs.getJobs()

# Get job status
job_info = t.jobs.getJob(job.id)
print(job_info.status)

# Get archive location
print(f"Results archived to: {job_info.archivePath}")
```

## Downloading Results

After your job finishes, the output files (including `.out`, `.err`, and any OpenSees results) are archived to your `$WORK` directory on Stampede3:

```python
archive_uri = job_info.archivePath

# Example: use Tapis Files API to list or download
t.files.listFiles(systemId="stampede3", path=archive_uri)
```

## Summary

This workflow allows you to:

* Programmatically submit OpenSeesMP jobs from Python
* Automate batch simulations or parametric sweeps
* Integrate with Jupyter Notebooks or external orchestration scripts


