# Job Input

When submitting a job to the TACC HPC systems using SLURM -- whether through the DesignSafe portal, TACC web portal, or command line -- you must provide a set of input parameters. These parameters control how your job runs, how many resources it uses, and where input/output files are stored.


## Parameters for All HPC Jobs

These input fields are required for **all types of jobs**, regardless of what software or simulation tool you're running.


:::{dropdown} **Allocation**

Specify the TACC **allocation account** to charge for this job. A TACC allocation is a grant of computing resources -- such as CPU/GPU time, storage space, or access to specific systems -- on TACC’s supercomputers.

- This is often associated with a funded research project or proposal.
- Choose from the list of allocations available to your user account.
- If unsure, consult your PI or project manager.
- Check on your allocations by accessing your [TACC User Portal](https://portal.tacc.utexas.edu/) directly.

:::

:::{dropdown} **Queue**

Select the **queue (also known as a partition)** where the job should run.

- Different queues support different workloads .
- Refer to the Queue documentation to determine the best choice based on job duration and resources.


:::

:::{dropdown} **Maximum Job Runtime**

The **maximum wall-clock time** your job should run, in .

- Your job will be **terminated automatically** if it exceeds this time.
- Shorter runtimes typically result in faster scheduling.
- Platform-specific limits apply (e.g., usually 48 hours for the `normal` queue).
- When submitting job runtime in a SLURM script, it is specified in `HH:MM:SS` format _Example_: `02:00:00` for 2 hours.
- Note: The time required to transfer your data files to and from scratch is included in your job run time. --> Make sure you leave enough time for data transfer, otherwise you will have to transfer your results manually via ssh from scratch to your data.

:::

:::{dropdown} **Node Count**

The number of **compute nodes** your job requires.

- Each node is an independent machine.
- You are billed per node, so only request what you need.
- Default is often 2 nodes, but smaller jobs may only need 1.

:::

:::{dropdown} **Cores per Node**

The number of **CPU cores (processors) per node** to use.

- Total processes = `Node Count × Cores per Node`.
- More cores = higher parallelism, but also higher memory use.
- For memory-heavy jobs, consider using **fewer cores per node** to allocate more memory per core.

_Note_: Many TACC systems have 56 cores per node.

:::

:::{dropdown} **Job Name**

A **custom name** for your job.

- Helps you identify jobs in the SLURM job queue and job output.
- This name will also appear in output directories and logs.
- Useful when submitting multiple jobs.

:::

:::{dropdown} **Archive System**

Specifies the **storage system** where job results will be saved after execution.

- Defaults to `designsafe.storage.default` or another predefined system.
- Best left at the default value unless you have specific storage needs.

:::

:::{dropdown} **Archive Directory**

The **folder** where output files will be copied after the job completes.

- This is usually inside your **MyData** space.
- You can specify a custom location if needed, but the default is recommended.
- Output directories are automatically named using the job name and timestamp.

:::

## Additional Parameters
These may be **Required by some Applications**

Some DesignSafe applications automatically generate the SLURM job script for you. Others — like the **OpenSees Web-Portal app** — may also prompt you for additional parameters to handle extra tasks.

For example, the OpenSees Web-Portal app not only prepares the SLURM input but also **copies your input files to the scratch directory on the HPC system**, runs your analysis there (which is faster due to high-performance scratch storage, taking full advantage of the HPC architecture.), and then **retrieves the results back to your DesignSafe workspace** once the job completes.



:::{dropdown} **Input Directory**

This directory contains **all input files** for your job.

- Includes your main script and any secondary files.
- This directory is **copied to the HPC system** at job start.
- Once the job finishes, the entire folder (including outputs) is copied to the output/archive location.

:::

:::{dropdown} **Main Script**

The name of the **main input file** that the application, such as OpenSees, should execute.

- Must be located inside the **Input Directory**.
- This file is passed to the proarm as a command-line argument.
- All other script calls must originate from this file.

```{tip}
se relative paths inside your input script so they still work after the input folder is copied.
```

:::

## Summary Table

| Parameter             | Applies To        | Description |
|-----------------------|------------------|-------------|
| -- Job Parameters -- |
| **Allocation**        | All jobs          | Select which TACC allocation/account to charge. |
| **Queue**             | All jobs          | HPC queue to run in (e.g., `skx`,`skx-dev`). |
| **Max Runtime**       | All jobs          | Maximum wall-clock runtime for the job. |
| **Node Count**        | All jobs          | Number of compute nodes to request. |
| **Cores per Node**    | All jobs          | Number of processors per node. |
| **Job Name**          | All jobs          | Descriptive name for the job (for tracking/logging). |
| **Archive System**    | All jobs          | Storage system for saving job results. |
| **Archive Directory** | All jobs          | Folder to save job output files. |
| -- OpenSees-Analysis Parameters -- |
| **Input Directory**   | Some jobs         | Folder with scripts and input files. |
| **Main Script**       | Some jobs         | Main input script passed to the application at runtime. |

