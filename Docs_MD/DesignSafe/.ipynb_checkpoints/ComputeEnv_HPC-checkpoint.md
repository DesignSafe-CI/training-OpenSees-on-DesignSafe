# HPC on TACC
***Understanding the TACC HPC Environment***

DesignSafe computations are powered by the **Texas Advanced Computing Center (TACC)**, which hosts world-class high-performance computing (HPC) systems like **Stampede3**, **Frontera**, and **Lonestar6**. These systems allow researchers to run simulations and workflows at a scale far beyond what's possible on a personal computer or basic virtual machine.

## What Makes HPC Different?

Unlike single-node environments like VMs or JupyterHub containers, HPC systems allow you to run simulations across **multiple compute nodes**, each with dozens of CPU cores and large amounts of memory. But it’s not just about node counts — HPC performance depends on:

* **Processor architecture and clock speed**
* **Cores per node** (e.g., 48–128)
* **Memory per node**, which may be fixed or configurable
* **Interconnect speed** between nodes (important for MPI-parallel jobs)
* **I/O performance** to and from large-scale parallel file systems

TACC systems are designed to optimize all of these aspects, supporting simulations and workflows that are compute- or memory-intensive, I/O-heavy, or parallelized across thousands of cores.


In HPC environments like TACC, jobs are submitted to a **scheduler** that manages resource usage across thousands of users. To make informed decisions about how to configure and run your jobs, it's important to understand the key components of this ecosystem.

## Core Concepts You’ll See Throughout This Module

These terms will be referenced **again and again** — feel free to click into any linked term for a deeper explanation, or simply return to this list later as needed:

* **Node**: A full physical machine allocated to your job. Independent computing units. A single node typically contains multiple CPU cores and a set amount of memory. You request nodes using the `nodeCount` attribute in Tapis.
* **Core**: A single CPU within a node; jobs can run in parallel across multiple cores.
* **Cores per Node**: The number of CPU cores available on each node. For example, on Stampede3, each compute node has 48 cores. This is set using the `processorsPerNode` attribute.
* **Memory per Node**: The amount of RAM available on each node. Memory capacity can vary between queues and systems. Tapis allows you to request this via `memoryPerNode`.
* **Queue (Partition)**: helps determine *when* your job runs, based on runtime and resource requirements. It's a waiting line for jobs, organized by system, job type, and size. You select a queue using the `batchQueue` attribute. 
    

* **Allocation**: Your granted share of computing resources, like CPU hours or access to specific systems. All jobs consume Service Units (SUs) from a TACC allocation. These allocations define how much compute time you can use on a given system.
* **SLURM**: The job scheduler (workload manager) that dispatches your jobs to available nodes.
* **SLURM Job File**: is a script that defines your job’s inputs, resources, and runtime behavior. Job parameters include cores, memory, wall time, and commands.

Each of these plays a role in how your job is scheduled, executed, and monitored.

Depending on system load and job size, your **queue wait time** may be shorter or longer than the job’s actual runtime.Efficient HPC usage requires balancing your resource request: requesting too much can increase wait time, while too little may cause job failure or underperformance.



## HPC Hardware Architecture at TACC

TACC systems consist of hundreds or thousands of **compute nodes**, each with:

* Dozens of CPU cores (e.g., 48 on Stampede3),
* Shared memory (RAM),
* High-speed network interconnects for parallel communication.

* Here's a conceptual diagram showing how **nodes**, **cores**, **queues**, and **allocations** are organized within TACC systems:

    ```
    +-----------------------------------------------------------+
    |                  TACC High-Performance System             |
    |                                                           |
    |  +-------------------+   +-------------------+            |
    |  |    Queue: skx     |   |  Queue: skx-dev   |            |
    |  |-------------------|   |-------------------|            |
    |  | +---------------+ |   | +---------------+ |            |
    |  | |  Node 1       | |   | |  Node A       | |            |
    |  | | Core 0        | |   | | Core 0        | |            |
    |  | | Core 1        | |   | | Core 1        | |            |
    |  | | ...           | |   | | ...           | |            |
    |  | | Core 47       | |   | | Core 47       | |            |
    |  | +---------------+ |   | +---------------+ |            |
    |  | +---------------+ |   | +---------------+ |            |
    |  | |  Node N       | |   | |  Node M       | |            |
    |  | +---------------+ |   | +---------------+ |            |
    |  +-------------------+   +-------------------+            |
    |                                                           |
    |  Allocations track total usage across queues and systems  |
    +-----------------------------------------------------------+
    ```

* **Notes:**
    
    * Each **queue** (e.g., `skx`, `development`, `normal`) manages a pool of compute nodes.
    * Each **node** contains a fixed number of **CPU cores** (e.g., 48 on Stampede3).
    * Your **TACC allocation** defines how many total **Service Units (SUs)** you can spend across the system.
    * Tapis jobs specify how many nodes and cores to request from a given queue.


## Interactive Sessions for Testing

Before submitting large production jobs, you can **connect interactively to the system** to test scripts, troubleshoot errors, or run small-scale jobs:

1. **SSH** into a TACC login node
2. Use `idev` to request an **interactive compute node**
3. Run commands in real time to debug, monitor, or explore

This is especially useful for:

* Validating SLURM scripts
* Troubleshooting runtime errors
* Checking CPU/memory usage

## File Movement and Data Staging

Your jobs **don’t run directly** from the DesignSafe **My Data** storage. Instead:

* Input files are staged to TACC’s **work** or **scratch** file systems -- data access is much faster this way.
* Output files are written to these systems and must be copied back afterward

DesignSafe simplifies this through:

* The **Web Portal**, which handles staging automatically
* **Tapis**, which automates job execution, file transfers, and cleanup

## CPU vs GPU Nodes

Some systems, such as **Frontera** or **Vista**, also offer **GPU nodes** that support deep learning and CUDA-enabled applications. These nodes are not typically used for OpenSees, but they are available for workflows involving image analysis, neural networks, or accelerated solvers.


---

We have introduced these concepts here because they will appear **again and again throughout this module**. This page serves as a **high-level reference** you can revisit anytime.

You’re welcome to jump into the sections below now to explore each concept in more detail—or simply return to them later as they come up in real examples.

