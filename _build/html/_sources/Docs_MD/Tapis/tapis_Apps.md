# Tapis Apps
***Simplifying HPC Job Execution on DesignSafe***

**Tapis Apps** are pre-configured software templates that let researchers run simulations, analyses, and data workflows on high-performance computing (HPC) systems — **without needing to write job scripts or manage SLURM directly**.

These apps are available through the **DesignSafe Web Portal**, or programmatically via **Jupyter notebooks** or the **Tapis CLI**. Each app encapsulates all the information needed to run a specific scientific application — such as **OpenSees**, **OpenFOAM**, or custom tools — using best practices for performance and reproducibility.



## What Do Tapis Apps Do?

When you submit a job via a Tapis App, the system automatically:

* **Generates a SLURM script** tailored to the app
* **Stages your input files** to the HPC system (e.g. `$SCRATCH`)
* **Submits the job** to the correct queue on a system like Stampede3
* **Runs the job** with the right environment, modules, and executable
* **Returns the output** back to your DesignSafe workspace (**My Data**)

Tapis handles the technical complexity behind the scenes — including queueing, execution, module loading, and file movement — so you can focus on the science.

> Under the hood, your app submission becomes a SLURM batch job, executed on a system like **Stampede3** or **Frontera**.
> Tapis also supports other schedulers (e.g. PBS) and execution types if the underlying system is configured for them.



## Typical Inputs to a DesignSafe Tapis App

Whether submitted through the web portal or programmatically, most apps expect:

* **Main input file** (e.g., `model.tcl` for OpenSees or `input.json` for a custom workflow)
* **Supporting files** (e.g., data sets, configuration files, libraries)
* **Run parameters** (e.g., number of cores, wall time, flags)
* **Output preferences** (optional controls over where and how results are returned)

Because the app handles the SLURM environment for you, **you don’t need to write a job script manually** — unless you want more advanced control.


## Why Use Tapis Apps?

Tapis apps provide major benefits:

| Benefit                       | What It Does                                                                                 |
| ----------------------------- | -------------------------------------------------------------------------------------------- |
| **Simplifies HPC access**     | No need to SSH, stage files manually, or write job scripts                                   |
| **Standardizes environments** | Ensures the right modules, compilers, and binaries are used across all users                 |
| **Optimizes performance**     | Automatically runs jobs from fast storage (e.g., `$SCRATCH`) for best I/O performance        |
| **Automates file handling**   | Input/output files are transferred cleanly between your DesignSafe workspace and HPC systems |
| **Enables reproducibility**   | Job metadata and configuration are tracked and reproducible for later re-use                 |

This means researchers can focus on **engineering and science**, while Tapis ensures jobs are run efficiently and consistently across HPC systems.

Yes! A **visual mapping of the Tapis submission flow** is a diagram or flowchart that helps users understand *how a Tapis App job moves from your input to execution on the HPC system and back*. This helps demystify what happens behind the scenes — especially for users who are used to the Web Portal and want to transition to scripting or custom workflows.


### Visual: Tapis Job Submission Flow (Web Portal or API)

```
flowchart TD
    A[🖥️ User Submits Job<br>via Web Portal or API] --> B[📄 Tapis App Template<br>Defines Execution Parameters]
    B --> C[🧰 Tapis Builds SLURM Script<br>from App JSON + User Inputs]
    C --> D[🚀 Job Submitted to SLURM<br>on Execution System (e.g. Stampede3)]
    D --> E[🖴 Input Files Staged to<br>$SCRATCH Directory]
    E --> F[🧮 Job Executes on Compute Node<br>(with requested modules/resources)]
    F --> G[📂 Output Files Collected and<br>Staged Back to DesignSafe "My Data"]
    G --> H[📊 User Downloads Results<br>or Launches Post-Processing]
```

---

### 📘 What Each Step Represents

| Step  | Description                                                                                                          |
| ----- | -------------------------------------------------------------------------------------------------------------------- |
| **A** | You initiate a job using the web portal, CLI, or Python SDK.                                                         |
| **B** | The Tapis App template (e.g. `app.json`, `profile.json`) defines required inputs, resources, and execution behavior. |
| **C** | Tapis automatically generates a SLURM batch script using your inputs.                                                |
| **D** | The job is queued and submitted to the appropriate HPC scheduler (SLURM).                                            |
| **E** | Your input files are copied from DesignSafe (My Data) to `$SCRATCH` for fast access.                                 |
| **F** | The job runs on a compute node using the correct software modules and runtime environment.                           |
| **G** | Output files are moved back to your DesignSafe workspace (`My Data`).                                                |
| **H** | You view/download results, or chain a follow-up job (e.g., post-processing).                                         |






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
