# Tapis-Job Submittal
***How to Run Remote Apps on HPC Systems***

Tapis Jobs allow you to **submit** and **run computational tasks** on remote systems — such as HPC clusters, cloud VMs, and containerized environments — through a standardized API like Tapipy or the Web Portal.

A **Job Submission** is a request you send to Tapis that says: *“Run this app, using these specific inputs and parameters, on this system, with these resources.”*

Each job is built around a **registered Tapis App**, which defines:
* The executable to run (script, binary, or container)
* Required input files and parameters
* The target execution system

Tapis will take care of:
* Staging input data
* Running the app
* Monitoring progress
* Archiving results

---
## Submitting a Job
Jobs can be submitted through various interfaces:
* **Web portal**: Click-to-submit via graphical forms
* **Python (Tapipy)**: Script and automate submissions
* **Tapis CLI**: Submit jobs using terminal commands
Behind the scenes, all submissions follow the same general pattern.

## What Happens When You Submit a Job

Submitting a job is how you run a Tapis App with your own data, configuration, and compute resources. Whether you're using the Web UI, CLI, or Python (Tapipy), the core process is the same:

1. **Choose an App**
   Specify the *appId*, such as *opensees-mp-s3*.

2. **Provide Inputs & App Parameters**
   Supply input files and any runtime parameters defined by the app schema.

3. **Define Execution Settings** (Job Attributes)
   Request compute resources: node count, core count, walltime, queue.

4. **Tapis Builds and Submits the Job**
   Inputs are staged, a scheduler-submission script is created by injecting your values (e.g. SLURM), and the job is queued.

5. **Execution & Monitoring**
   Tapis submits the job to the specified execution system and tracks its status. You can monitor it using the API, CLI, or portal.

6. **Archiving**
   Outputs are collected and saved to a defined archive system and path. You can browse, download, or reuse the data in other workflows.

> On shared systems like **Stampede3**, jobs may queue before running due to demand — this delay is the trade-off for accessing powerful resources.

---

## Submitting Jobs with Tapipy


Below is the typical workflow for submitting and managing jobs directly from Python, using Tapipy (Python SDK):


:::{dropdown} **Install Tapipy**

Run this once to install the SDK:

```bash
pip install tapipy
```
:::

:::{dropdown} **Connect to Tapis**

Create the client and log in:

```python
from tapipy.tapis import Tapis

# Replace with your credentials
t = Tapis(
    base_url="https://tacc.tapis.io",
    username="your-username",
    password="your-password",
    account_type="tacc"
)

t.get_tokens()  # Log in to Tapis
```

**Tip:** You only need to call *get_tokens()* once per session.

:::

:::{dropdown} **Submit a Job**

You need to know:

* App ID (*appId*) — already registered in Tapis
* Archive system ID (e.g. *"tacc-archive"*)
* Where you want your outputs to be stored (*archivePath*)

* **Example Submission**

    ```python
    job = t.jobs.submitJob(
        jobName="my-first-job",
        appId="hello-world-1.0",
        parameters={},      # Replace with actual app parameters if needed
        fileInputs=[],      # Or provide input files here
        archiveSystemId="tacc-archive",
        archivePath="myuser/outputs/hello-job",
        archiveOnAppError=True
    )
    
    print("Job submitted!")
    print("Job ID:", job.id)
    print("Status:", job.status)
    ```

:::

:::{dropdown} **Check Job Status**

You can check on your job:

```python
job = t.jobs.getJob(jobUUID=job.id)
print("Current Status:", job.status)
```

Or just the status field directly:

```python
status = t.jobs.getJobStatus(jobUUID=job.id)
print(status.status)
```
* **Job Status Values (for Filtering)**

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

:::

:::{dropdown} **Download Job Outputs**

* **List available files**

```python
files = t.jobs.getJobOutputList(jobUUID=job.id)
for f in files:
    print(f.name, f.length)
```

* **Download a file:

```python
output = t.jobs.getJobOutputDownload(
    jobUUID=job.id,
    path="stdout.txt"
)

with open("stdout.txt", "wb") as f:
    f.write(output)
```

The file paths (like *"stdout.txt"*) depend on how your app writes output.

:::


---

## At a Glance: Job Submission Components

| Component           | Role                                      |
| ------------------- | ----------------------------------------- |
| *name*              | A label for your job                      |
| *appId*             | The app you're running                    |
| *inputs*            | Files needed for execution                |
| *parameters*        | Configurable runtime values               |
| *nodeCount*         | Number of compute nodes requested         |
| *processorsPerNode* | Number of CPU cores per node              |
| *maxRunTime*        | Walltime for job execution                |
| *archivePath*       | Where to store output files after the run |
| *archiveSystemId*   | Storage system for archiving              |
| *archiveOnAppError* | Whether to archive even if the job fails  |

---

## Why This Matters for Scientific Workflows
The use of templates, like the one for OpenSeesMP, is a cornerstone of scalable research computing. They:
* Reduce errors by automating input/output handling
* Enable interoperability across projects, tools, and platforms
* Integrate seamlessly with Jupyter, Web Portals, and Tapis-powered APIs

Most importantly, they allow researchers to focus on science, not infrastructure.

```{tip}
* Use *client.apps.getApps()* to browse available apps. (if available)
* Use *client.systems.getSystems()* to find storage or execution systems you have access to. *(see next section)*
* Input files must already be available on a Tapis-accessible system, or uploaded ahead of time.
```