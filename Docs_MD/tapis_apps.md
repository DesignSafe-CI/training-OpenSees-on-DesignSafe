# Tapis Apps

**Tapis Apps** are pre-configured software templates that let researchers run simulations, analyses, and data workflows on high-performance computing (HPC) systems — **without needing to write job scripts or manage SLURM directly**. They encapsulate the executable, expected inputs/parameters, and the target execution system so you don’t have to write or maintain scheduler scripts.


A **Tapis App** is a preconfigured, reusable execution template that defines:

* The **executable** (binary/script/container),
* The **inputs and parameters** it expects,
* The **target execution system** and runtime environment.

***Apps decouple *what to run* from *where/how to run it*, so users don’t need to write scheduler scripts or manage modules.***

---
## Which Apps to Use

You can use registered Tapis Apps (e.g., OpenSees, OpenFOAM), or you can write your own -- using a registered app as a tempate.

The registered apps are available through the **DesignSafe Web Portal**, or programmatically via **Jupyter notebooks** or the **Tapis CLI**. Each app encapsulates all the information needed to run a specific scientific application — such as **OpenSees**, **OpenFOAM**, or custom tools — using best practices for performance and reproducibility.


---
## Why Use Tapis Apps?

* **Consistent UX:** same workflow across systems and schedulers.
* **Reproducible:** versions, defaults, and metadata are tracked.
* **Portable:** works from the Web Portal, Python (Tapipy), or CLI.

Tapis apps provide major benefits:

| Benefit                       | What It Does                                                                                 |
| ----------------------------- | -------------------------------------------------------------------------------------------- |
| **Simplifies HPC access**     | No need to SSH, stage files manually, or write job scripts                                   |
| **Standardizes environments** | Ensures the right modules, compilers, and binaries are used across all users                 |
| **Optimizes performance**     | Automatically runs jobs from fast storage (e.g., `$SCRATCH`) for best I/O performance        |
| **Automates file handling**   | Input/output files are transferred cleanly between your DesignSafe workspace and HPC systems |
| **Enables reproducibility**   | Job metadata and configuration are tracked and reproducible for later re-use                 |

This means researchers can focus on **engineering and science**, while Tapis ensures jobs are run efficiently and consistently across HPC systems.

---

## What Do Tapis Apps Do?

When you submit a job via a Tapis App, the system automatically:

* **Generates a SLURM script** tailored to the app
* **Stages your input files** to the HPC system (e.g. `$SCRATCH`)
* **Submits the job** to the correct queue on a system like Stampede3
* **Runs the job** with the right environment, modules, and executable
* **Returns the output** back to your DesignSafe workspace (**My Data**)

*This process overlaps steps 4-6 in the Jub submittal described above. *

Tapis handles the technical complexity behind the scenes — including queueing, execution, module loading, and file movement — so you can focus on the science.

> Under the hood, your app submission becomes a SLURM batch job, executed on a system like **Stampede3** or **Frontera**.


---
## Typical Inputs to a DesignSafe Tapis App

Whether submitted through the web portal or programmatically, most apps expect:

* **Main input file** (e.g., `model.tcl` for OpenSees or `input.json` for a custom workflow)
* **Supporting files** (e.g., data sets, configuration files, libraries)
* **Run parameters** (e.g., number of cores, wall time, flags)
* **Output preferences** (optional controls over where and how results are returned)

Because the app handles the SLURM environment for you, **you don’t need to write a job script manually** — unless you want more advanced control.

---
## What Happens When You Submit a Job

Submitting a job is how you run a Tapis App with your own data, configuration, and compute resources. Whether you're using the Web UI, CLI, or Python (Tapipy), the core process is the same:

1. **Choose an App**
   
   Specify the *appId*, such as *opensees-mp-s3*.

3. **Provide Inputs & App Parameters**

   Supply input files and any runtime parameters defined by the app schema.

5. **Define Execution Settings** (Job Attributes)

   Request compute resources: node count, core count, walltime, queue.

7. **Tapis Builds and Submits the Job**

   Inputs are staged, a scheduler-submission script is created by injecting your values (e.g. SLURM), and the job is queued.

9. **Execution & Monitoring**

   Tapis submits the job to the specified execution system and tracks its status. You can monitor it using the API, CLI, or portal.

11. **Archiving**

Outputs are collected and saved to a defined archive system and path. You can browse, download, or reuse the data in other workflows.

> On shared systems like **Stampede3**, jobs may queue before running due to demand — this delay is the trade-off for accessing powerful resources.


::::{dropdown} Submitting Jobs with Tapipy -- Example


Below is the typical workflow for submitting and managing jobs directly from Python, using Tapipy (Python SDK):


:::{dropdown} **Install Tapipy**

Run this once to install the SDK:

```bash
pip install tapipy
```

tapipy may have already been installed in Jupyter Hub.
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

::::

---

## Going Beyond the Web Portal

Once you're comfortable using apps through the DesignSafe interface, you can unlock even more power by stepping into **customized or programmatic workflows**.

### Want more control?

You have two great options:

#### 1. **Write Your Own SLURM Scripts**

* Base them on examples from the Tapis app repositories.
* Fully customize job arrays, MPI layout, I/O paths, and hybrid workflows.
* Ideal for power users coordinating multi-step or multi-job analyses.

#### 2. **Use Tapis from Python or the CLI**

* Submit jobs programmatically from Jupyter Notebooks or Python scripts.
* Automate parameter sweeps, ensembles, or linked pre/post-processing workflows.
* Leverage the same execution environments used by the Web Portal — just with more control.

This is often the **next step** after mastering the Web Portal — combining the **reliability of Tapis apps** with the **flexibility of scripting and automation**.


## Why This Matters for Scientific Workflows
The use of templates, like the one for OpenSeesMP, is a cornerstone of scalable research computing. They:
* Reduce errors by automating input/output handling
* Enable interoperability across projects, tools, and platforms
* Integrate seamlessly with Jupyter, Web Portals, and Tapis-powered APIs

Most importantly, they allow researchers to focus on science, not infrastructure.

---

## Learn more

* Tapis Jobs (API & states): *Tapis Jobs Documentation*
* App templates and examples (OpenSees et al.): DesignSafe/TACC **WMA-Tapis-Templates** repository

