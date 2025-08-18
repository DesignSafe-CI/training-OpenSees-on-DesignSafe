# Step 3: Retrieve Output

Perfect 👍 — here’s the expanded **Step 3 introduction with a best-practice note** included:

Once a job has completed, the final step is to **explore and retrieve its outputs**. Tapis automatically archives all files produced by your job into the designated archive system and path. These outputs may include:

* **Primary results** (e.g., simulation data, processed files)
* **Log and status files** (`.out`, `.err`)
* **Intermediate data** generated during execution

Tapis provides two key functions for working with archived results:

* `getJobOutputList(job_id)` — Browse and list all files and folders in the archive.
* `getJobOutputDownload(job_id, path)` — Retrieve specific files for local use.

This separation makes it easy to **see what a job produced** before downloading, and ensures workflows can scale — whether you just need a quick log file for debugging or a large dataset for post-processing.

### Best Practice: Start with Logs

Before downloading large result files, always check the `.out` (standard output) and `.err` (error output) files. These are the **first place to look** to confirm that:

* Your job executed correctly,
* Inputs were staged properly, and
* No errors occurred during runtime.

By reviewing logs first, you can avoid unnecessary downloads of large files from failed or incomplete jobs and quickly pinpoint issues.

---


## *getJobOutputList(job_id)*

### Purpose:
List archived output files.

### Example:
```python
files = client.jobs.getJobOutputList(job_id="myuser-job-abc123")
for f in files:
    print(f.name, f.size, f.lastModified)
```

---

## *getJobOutputDownload(job_id, path)*

### Purpose:
Download a specific file.

### Example:
```python
output_file = client.jobs.getJobOutputDownload(
    job_id="myuser-job-abc123",
    path="results/output.txt"
)

with open("output.txt", "wb") as f:
    f.write(output_file)
```

You must know the relative path from *getJobOutputList()*.

## Accessing and Downloading Outputs

After metadata retrieval, pull job results with:

* ```getJobOutputList()``` → List available files/folders.
* ```getJobOutputDownload()``` → Download specific files locally.

**Example Combined Workflow:**

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
for f in files:
    print(f.name, f.size)

# Download output
content = client.jobs.getJobOutputDownload(job_id, path="results/output.txt")
with open("output.txt", "wb") as f:
    f.write(content)
```

:::
