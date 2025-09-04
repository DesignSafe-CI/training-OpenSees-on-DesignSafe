<!-- # Accessing HPC
***Accessing HPC as an Execution Environment***

High Performance Computing (HPC) systems like **Stampede3** at TACC are powerful clusters designed to run large-scale simulations and data analyses. But unlike a personal computer, you don't "run programs" directly on the machine — you interact with a **layered environment** designed for security, scalability, and fairness across many users.

This section explains how jobs actually run on HPC systems and how environments like **JupyterHub** and **SSH** provide you access.


## The HPC Architecture: Windows into the Machine

HPC systems are built around **specialized roles**:

| Component           | Purpose                                                                              |
| ------------------- | ------------------------------------------------------------------------------------ |
| **Login nodes**     | Where users connect (via SSH or JupyterHub); used for editing, setup, and submission |
| **Compute nodes**   | Where jobs actually run — powerful nodes allocated by the SLURM scheduler            |
| **Storage systems** | */home*, */work*, and */scratch* directories used to store input/output data         |

When you connect to TACC via SSH or through JupyterHub, you're not entering a compute node — you're accessing a **login node**, a shared environment meant for lightweight tasks like file editing, compiling, or launching jobs.


## Submitting Jobs: You're Not Running Code Directly

Unlike desktop computing, you don’t run code interactively on compute nodes. Instead, you:

1. **Write a job script** (SLURM batch script).
2. **Submit it to the scheduler** (*sbatch job.slurm*).
3. **SLURM queues the job** and allocates compute nodes when resources become available.
4. The job then runs **without further input** from you — like launching a rocket.

> Think of it as dropping off your luggage at the airport: you don’t control which plane it goes on, but it eventually gets loaded, routed, and delivered.


## TACC's JupyterHub on HPC (e.g., TACC TAP)

JupyterHub at TACC (such as the TAP system) provides a **web-based interface** to HPC — but it's still built on the same login-and-compute-node model.

:::{note} 
This is not the same environment as the DesignSafe HPC Jupyter Labs
:::

* When you launch a JupyterHub session, you are **assigned a dedicated compute node** (usually a Kubernetes-managed container or virtual node).
* That node gives you interactive access with resources (e.g., 8 cores, 20 GB RAM).
* Behind the scenes, your session is submitted as a **job request**, just like a batch job — but it's configured to give you real-time interactivity.

This is why:

* Jupyter notebooks can be slow to start (they're queued).
* You’re limited in how many sessions you can run at once (node allocation).
* You have access to full CPU/RAM, unlike the shared login node.

## DesignSafe's Jupyter Lab on HPC (CPU and GPU)

DesignSafe now offers a powerful interface for working directly on HPC resources: JupyterLab HPC (CPU), JupyterLab HPC (GPU), and Jupyter HPC Native. These options may grow and/or evolve over time.

Although these environments were originally introduced to support machine learning workflows, they are also ideal for users running OpenSees, Python-based simulations, or other research code that benefits from interactive access to full compute nodes.

This topic is covered in its own section elsewhere.

## idev: Temporary Interactive Nodes

If you want a **real shell** on a compute node (for testing, compiling, or small test runs), TACC provides *idev*, an interactive job tool:

```bash
idev -N 1 -n 4 -p development -t 00:30:00
```

This requests a short interactive session on a compute node, allowing you to:

* Run commands directly on the node
* Test MPI/OpenMP configurations
* Debug job scripts before scaling up


## Summary: HPC Access Model

* **Login Nodes** = Entry points, not for computation
* **Compute Nodes** = Where actual work happens
* **JupyterHub (TAP)** = Submits interactive jobs behind the scenes
* **Design HPC Jupyter** = Submits interactive jobs behind the scenes
* **SLURM Scheduler** = Manages when/where your job runs
* **idev** = Grants a shell session on a compute node for testing

Understanding this access model helps explain why:

* Jobs don’t start instantly
* You can't "just run" scripts from your terminal
* Jupyter sessions and SLURM jobs are part of the same queueing system
 -->