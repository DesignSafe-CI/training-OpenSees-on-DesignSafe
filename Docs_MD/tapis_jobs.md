# Tapis Jobs

Tapis Jobs let you submit and run computational tasks on remote systems (HPC clusters, cloud VMs, containers) through a consistent API (Web Portal, Tapipy/Python, CLI, or direct HTTP).

## What is a Job?

A **job** is a single execution of a registered **Tapis App** with your inputs, parameters, and resource requests. Submitting a job tells Tapis: *“Run this app with these settings on that system.”*

**Tapis** will take care of:

* Staging input data
* Running the app
* Monitoring progress
* Archiving results


### Key properties (why jobs matter)

Jobs are:
:::{dropdown} Portable -- The job can be run in a different environment with minimal changes.

When a job is described as **portable** in the context of Tapis (or HPC workflows in general), it means:

***The job can be moved or rerun in a different environment without requiring major changes.***

More specifically:

| Portability Means…                  | In Tapis Jobs                                                                                                               |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Not tied to a single machine** | You can run the same job on different execution systems (e.g., Stampede3, Frontera) as long as the app is registered there. |
| **Encapsulated configuration**   | The job includes references to all the inputs, parameters, and resource requests it needs.                                  |
| **Repeatable and reproducible**  | Because the job schema is structured and versioned, you can re-run it later (or elsewhere) with the same result.            |
| **Remotely accessible**          | You don’t need to be logged into a specific cluster — you can submit and manage jobs from anywhere via API.                 |
| **Scriptable and automatable**   | You can define and launch the job using code (e.g., Python, Bash, JSON) rather than manual setup on one system.             |

---

**Example: Why Portability Matters**

You define a job for an OpenSees simulation with:

* Input files stored on a Tapis-accessible system
* Parameters defined in JSON
* App version set to *openseesmp-3.5.0*
* Target system: *stampede3*

Later, you can:

* Change the system to *frontera* (if supported),
* Use the same app and inputs,
* Submit the same job again — without rewriting everything.

This is **portability**: you separate the "what to run" from "where to run it."

:::


:::{dropdown} Asynchronous -- The job runs independently after submission.
When a Tapis **job is asynchronous**, it means:

***The job runs independently after submission***

In more detail:

| Asynchronous Means…                   | In Tapis Jobs                                                                                                  |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **You don’t have to wait**          | When you submit a job, you immediately get a response (job ID), and your script or notebook can move on.       |
| **The job runs in the background** | Tapis handles the job lifecycle (staging → running → archiving) without requiring you to stay connected.       |
| **You can check on it later**      | You can monitor status (`PENDING`, `RUNNING`, `FINISHED`, etc.) and fetch outputs when it’s done.              |
| **Useful for large or long tasks** | Asynchronous execution is ideal for simulations that take minutes, hours, or even days to finish.              |
| **Job state is managed by Tapis**  | Tapis maintains a full record of job metadata, status, inputs/outputs, and logs — independent of your session. |

---

### Why This Matters

If jobs were synchronous:

* Your code would **pause and wait** until the job finished.
* You couldn’t submit multiple jobs efficiently.
* Long-running jobs would **block your workflow**.

With **asynchronous jobs**, you can:

* Fire off a job from a notebook or script,
* Continue working or even log off,
* Check the results later — or trigger automated post-processing.


:::

:::{dropdown} Managed by a lifecycle of states -- making it easy to monitor.

When a Tapis job is **managed by a lifecycle of states**, it means that Tapis tracks and controls the job as it moves through a **series of well-defined phases**, from the moment it’s submitted until it completes (or fails).


**Job Lifecycle States Explained**

| State                | What It Means                                                                    |
| -------------------- | -------------------------------------------------------------------------------- |
| *PENDING*            | The job has been submitted, but it hasn't started running yet.                   |
| *STAGING_INPUTS*     | Tapis is copying your input files to the execution system.                       |
| *QUEUED*             | The job is in the HPC system's queue, waiting for resources to become available. |
| *RUNNING*            | The job is actively executing on the compute system.                             |
| *ARCHIVING*          | Tapis is saving output files to your archive system (e.g., Corral).              |
| *FINISHED*           | The job completed successfully and outputs were archived.                        |
| *FAILED*             | Something went wrong — bad input, runtime error, system issue, etc.              |
| *CANCELLED*          | The job was manually cancelled before it could finish.                           |
| *BLOCKED* / *PAUSED* | Special cases where execution is held up due to system policies or errors.       |

---

### Why This Matters

This lifecycle gives you a **clear, trackable view** of your job’s progress. You can:

* **Query the current status** at any time with `getJob()` or `getJobStatus()`
* **Filter jobs** based on state (e.g., show all `FAILED` jobs)
* **Trigger next steps** (e.g., post-processing) when a job reaches `FINISHED`
* **Debug problems** when a job ends in `FAILED` or never leaves `PENDING`


---

### Summary

Tapis job states act like a **workflow timeline**. Every job moves through this timeline in a predictable way — and Tapis exposes this information so you can automate, monitor, or troubleshoot your research more easily.

:::


### Typical job submission interfaces

* **Web Portal** (forms)
* **Python (Tapipy)** (scripts/notebooks)
* **Tapis CLI**
* **HTTP (cURL/JSON)**

Tapis handles: input staging, execution, status tracking, and result archiving.

---

## Querying Completed Jobs

Use these patterns after jobs finish (or while they’re running) to inspect, filter, and retrieve results. 

:::{dropdown} With Tapipy (Python)
Here is a sample of the basic commands you can use -- we will dig into each in the next sections.

```python
from tapipy.tapis import Tapis
import json

t = Tapis(base_url="https://tacc.tapis.io", 
          username="YOUR_USER", password="YOUR_PASS")
t.get_tokens()

# 1) List your recent jobs
jobs = t.jobs.listJobs()  # optionally use limit, orderBy, etc.
print(len(jobs), "jobs listed")

# 2) Filter by status (e.g., only FINISHED)
finished = t.jobs.listJobs(status="FINISHED")

# 3) Search by field (e.g., FAILED)
search = json.dumps({"status": "FAILED"})
failed = t.jobs.listJobs(search=search)

# 4) Inspect a specific job
j = t.jobs.getJob(jobUUID=finished[0].id)
print(j.status, j.appId, j.execSystemExecDir)

# 5) List job outputs
files = t.jobs.getJobOutputList(jobUUID=j.id)
for f in files:
    print(f.name, f.length)

# 6) Download a specific output (path is relative to job archive root)
content = t.jobs.getJobOutputDownload(jobUUID=j.id, 
                                      path="stdout.txt")
with open("stdout.txt","wb") as fh:
    fh.write(content)
```

Integrate the above commands into your Jupyter Notebook so you can have a powerful and complete workflow.

:::



:::{dropdown} From the Web Portal

* Open **Jobs** → search/filter by **Status**, **App**, **System**, or **Date**.
* Click a job to view logs, parameters, and outputs; download files or pass them to downstream steps.

:::

### Understanding Results

* Outputs are archived to your configured archive system/path.
* Browse/download, reuse as inputs to another job, or share with collaborators.

### Why this matters for workflows

* Structured job records + consistent lifecycle → reproducibility, automation (e.g., trigger post-processing on *FINISHED*), and easier debugging on *FAILED*.

