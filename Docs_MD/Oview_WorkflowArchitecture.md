# Workflow Architecture
***Execution, Interface, and Automation***

Understanding how jobs are submitted, where they run, and how you interact with the underlying systems is essential for building **scalable, portable, and efficient workflows** on DesignSafe and TACC.

To guide you through the full landscape, we divide the system into three key layers, as shown in the diagram below:

* **Execution Environments** — Where your jobs are actually run
* **Interface Environments** — How you access the execution environments, interact with DesignSafe, and prepare/submit/postprocess jobs
* **APIs** — The middleware that interface connects your tools to compute resources (e.g., Tapis)

---
The following diagram gives you a snapshot of the workflow we will be presenting in this training module.

<img src="../_images/ComputeWorkflow.jpg" alt="Compute Environment" width="75%" />


<br>

Let's study detail each of these three layers:

## Execution Environments
:::{dropdown} *Where Your Jobs Run*

Your analysis ultimately executes on one of the following back-end systems:

1. **JupyterHub Containers (Kubernetes Cluster)**
   Interactive development environments running on a shared Kubernetes-managed cluster at TACC. Each user gets an **isolated container** with **up to 8 CPU cores and 20 GB RAM**. Still limited to **single-node** execution.

1. **Virtual Machines (VMs)**
   Used for targeted, often sequential workloads (e.g., OpenSees-EXPRESS). Typically limited to a **single node** and may be **shared among users**.
   * **OpenSees-EXPRESS** is a **Submit-Only VM** -- it receives jobs via Tapis with no interactive login.
   * The **OpenSees Interactive VM** has been deprecated in favor of JupyterHub Containers.


1. **HPC Systems at TACC**
   Jobs requiring larger compute resources or distributed execution run on supercomputers like:

   * **Stampede3** (general-purpose, multi-node)
   * **Frontera**, **Vista**, or **Lonestar6** (specialized or experimental resources)

   These require **batch submission** through the SLURM scheduler.

:::

## Interface Environments

:::{dropdown} *How You Access the Compute Systems*

1. **JupyterHub (Kubernetes)**
   Interactive senvironment for iterative development and testing. It is the primary portal for integrated scripting, visualization, and job orchestration. NOTE: You can also submit jobs to HPC from notebooks via the Tapis API.

1. **Web Portal**
   Web-portal interface for easy click-button job submittal, enabling users to launch and monitor computations without needing detailed command-line knowledge. This browser-based interface is used for launching preconfigured jobs to HPC using Tapis Apps (OpenSees, OpenSeesSP, OpenSeesMP). Ideal for quick submissions with no scripting required.

1. **SSH (Terminal Login)**
   Seamless direct command-line access to HPC clusters for fine-grained control. Full control for advanced users: edit files, manage directories, load modules, and submit custom SLURM scripts directly within the HPC.

1. **Jupyter on HPC Nodes**
   Launches JupyterLab directly on CPU or GPU nodes (e.g., Stampede3, Vista, or Frontera). This option is great if you require a single node with access to all of the node's memory and cores. However, it is not recommended due to queue wait and single-node restriction.

:::

## Tapis API

:::{dropdown} *How Interfaces Submit Jobs to Execution Resources*

The Tapis API enables you to automate computations, data management, and complex workflows directly from Python or other tools. It is the **middleware and job orchestration API** that connects interfaces (like JupyterHub or the Web Portal) to execution environments (like Stampede3 or VMs). It creates the SLURM job and submits it to the HPC automatically. It enables:

* **Programmatic job submission** via Python or CLI
* **Secure file transfer and job staging**
* **Integration with Web Portal (via preconfigured Tapis Apps)**
* **Monitoring, automation, and reproducibility**

You may use Tapis:

* **Directly**, via Tapipy or REST API calls in your Jupyter notebooks
* **Indirectly**, when submitting jobs via the Web Portal or CLI
* **Through Tapis Apps**, which bundle input handling, SLURM configuration, and output retrieval

This architecture supports a **modular and scalable workflow**, empowering both beginners and advanced users to take full advantage of TACC's compute power.

:::

Now that we’ve mapped the environments and how they connect, let’s compare your available options side-by-side and choose the right workflow for your needs.