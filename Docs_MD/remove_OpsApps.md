<!-- # OpenSees Tapis Appsxxx
***OpenSees Tapis Apps on DesignSafe***

DesignSafe has developed and published three official Tapis apps for running OpenSees:

* **OpenSeesEXPRESS** – for sequential simulations
* **OpenSeesMP** – for parallel simulations
* **OpenSeesSP** – for single-processor jobs

These apps can be launched directly from the DesignSafe **Apps & Tools** page. The web portal provides an intuitive graphical interface for submitting jobs. You begin by selecting the app, specifying input files and runtime parameters, and then pressing the "Submit" button. Behind the scenes, the interface constructs a valid Tapis job request and sends it to the Tapis Jobs service.

This abstraction allows researchers to launch simulations efficiently—without writing job scripts or accessing the command line on a remote cluster. Whether you're working through the portal, a Jupyter notebook, or a custom workflow, the Tapis apps provide a consistent and scalable way to run OpenSees on TACC resources.


##  Tapis Submission Flow: OpenSeesMP on Stampede3

```
flowchart TD
    A[🖥️ User Submits Job<br>via Web Portal (OpenSeesMP App)] --> B[📄 App Definition (app.json + profile.json)]
    B --> C[🧰 Tapis Builds SLURM Script<br>with OpenSeesMP Settings]
    C --> D[🚀 Job Submitted via Tapis<br>to SLURM on Stampede3]
    D --> E[🖴 Input Files Staged to<br>$SCRATCH on Stampede3]
    E --> F[🧮 Job Runs: ibrun OpenSeesMP<br>mymodel.tcl on N MPI Ranks]
    F --> G[📂 Output Files Collected<br>from $SCRATCH]
    G --> H[📦 Output Returned to<br>My Data in DesignSafe]
```



## Step-by-Step: How an OpenSeesMP App Runs

| Step                      | What Happens                                                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A. Job Submission**     | You fill out the **OpenSeesMP app form** on the DesignSafe web portal: choose your input `.tcl` file, number of cores, wall time, etc.            |
| **B. App Definition**     | Tapis uses the app’s `app.json` and `profile.json` to know which executable to run (`OpenSeesMP`), how to load modules, and where to mount files. |
| **C. SLURM Script Built** | A `job.slurm` script is generated automatically using your inputs and the app template.                                                           |
| **D. Submission to TACC** | The job is submitted to **SLURM on Stampede3** via the Tapis Jobs API.                                                                            |
| **E. File Staging**       | Input files are copied from your DesignSafe workspace (My Data) to your `$SCRATCH` folder on Stampede3 — enabling fast I/O.                       |
| **F. Job Execution**      | SLURM launches the job using `ibrun OpenSeesMP mymodel.tcl`, running your model in parallel across N MPI processes.                               |
| **G. Output Collection**  | Output files (e.g., `.out`, `.err`, `.log`, or custom result files) are gathered from `$SCRATCH`.                                                 |
| **H. Return to My Data**  | All outputs are returned automatically to your DesignSafe **My Data** space, where you can download them or begin post-processing.                |


###  Key Advantages for OpenSees Users

* No need to write your own `job.slurm` or manage module loading.
* Runs on Stampede3’s full production queue with efficient MPI execution.
* Automatically stages files for performance and reproducibility.
* Output is automatically returned and organized in your DesignSafe workspace.

:::{note}
Ideal for users running medium-to-large parallel OpenSeesMP models and those who want repeatable, scalable HPC workflows without deep SLURM experience.
:::
 -->