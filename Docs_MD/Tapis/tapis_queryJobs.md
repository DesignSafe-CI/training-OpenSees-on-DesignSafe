# Query and Retrieve Jobs

***Explore, Inspect, and Download Outputs with the Tapis v3 Python SDK (Tapipy)***


Tapis allows you to retrieve both **metadata** and **actual data (outputs)** for all your jobs — whether they were submitted directly through Tapis or via any DesignSafe application (such as the OpenSeesMP and OpenSeesSP web portal apps).



## Three levels of job information

When working with Tapis, you typically follow a **three-step process** to explore and extract job data. Each step has dedicated functions suited for that stage:

1. **Explore all jobs (overview metadata)**
   - **List jobs** — get overview metadata across many jobs.
   - Use *getJobList()* to retrieve high-level metadata for **all your jobs**, such as job names, UUIDs, submission times, statuses, and applications used.
   - This is perfect for building a summary DataFrame to explore your jobs and decide which one to examine in detail.

2. **Get detailed metadata for a specific job**
   - **Inspect a specific job** — retrieve full configuration and lifecycle.
   - Once you identify a job of interest (via its UUID), you can retrieve full metadata and execution details with:
     - *getJob(uuid)* for complete job configuration and input/output settings.
     - *getJobStatus(uuid)* for current execution state and progress.
     - *getJobHistory(uuid)* to see a timeline of events and status changes — helpful for performance tuning or debugging failures.

3. **Access and download job outputs**
   - **Retrieve outputs** — browse and download results.
   -  After you’ve drilled into a specific job, use:
     - *getJobOutputList(uuid)* to list all output files and folders produced by the job.
     - *getJobOutputDownload(uuid, outputPath)* to download individual files to your local workspace.

## Quick reference: Tapis job retrieval functions

| **Function**            | **What it retrieves**                                 | **Typical use**                                    |
|--------------------------|------------------------------------------------------|---------------------------------------------------|
| *getJobList()*           | High-level metadata for all your jobs <br>(name, UUID, status, app, submission time) | Build a summary DataFrame to explore or filter jobs. |
| *getJob(uuid)*           | Full detailed metadata for a specific job <br>(inputs, outputs, parameters) | Inspect how a job was configured. |
| *getJobStatus(uuid)*     | Current execution status and progress.               | Check if a job is still running or completed. |
| *getJobHistory(uuid)*    | Timeline of events and state transitions.            | Debug or optimize job stages. |
| *getJobOutputList(uuid)* | Lists all output files and folders from the job.     | See what data was produced. |
| *getJobOutputDownload(uuid, outputPath)* | Downloads a specific output file. | Retrieve results, logs, or data files to your local machine. |



## Recommended workflow

| **Step**                           | **Function**               | **What it retrieves**                                 | **Use it to...**                                   |
|------------------------------------|----------------------------|------------------------------------------------------|---------------------------------------------------|
| **1. Explore all jobs**         | *getJobList()*             | High-level metadata for all jobs                     | Build a searchable DataFrame of all your runs. |
| **2. Drill into metadata**      | *getJob(uuid)* <br> *getJobStatus(uuid)* <br> *getJobHistory(uuid)* | Detailed config, current state, and event history | Understand exactly how the job was set up and how it progressed. |
| **3. Retrieve job outputs**     | *getJobOutputList(uuid)* <br> *getJobOutputDownload(uuid, outputPath)* | List and download output files | Access your simulation or analysis results. |


This **three-step strategy** — starting from a broad overview, then narrowing down to detailed metadata, and finally accessing job outputs — makes your Tapis workflows **clear, modular, and easy to maintain**.


