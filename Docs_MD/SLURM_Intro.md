# SLURM

**SLURM** (Simple Linux Utility for Resource Management) is an open-source job scheduler used in most large supercomputers — including TACC — to manage who runs what, where, and when.

Think of SLURM as the traffic cop and air traffic controller for a supercomputer:
- You ask SLURM to run your program.
- It finds the right hardware (nodes/cores).
- It decides when your job can run based on availability and fairness.
- It starts your job, monitors it, and lets you know when it finishes.

## What Does SLURM Do?
- Schedules jobs across a supercomputer cluster.
- Allocates resources (CPU cores, memory, GPUs).
- Queues jobs if resources aren’t currently available.
- Monitors and tracks job progress.
- Logs results and resource usage for accounting and reproducibility.


## SLURM in DesignSafe Apps

In DesignSafe Web Portal Apps, SLURM is **completely hidden from the user** — but it’s still doing all the work behind the scenes.

When you launch a job through the web interface:

1. You select the app (OpenSees, MATLAB, Jupyter, etc.).
2. You set parameters (e.g. number of cores, run time, input file).
3. DesignSafe:

   * Fills in a JSON job description.
   * Maps it to a SLURM template script.
   * Submits the job via the **Tapis API** to TACC.
   * Monitors the run and stages files back when complete.

Behind the scenes, your job runs on a TACC machine like **Stampede3**, with SLURM allocating the compute resources and managing the run.


## Why Learn to Write Your Own SLURM Scripts?

Once you understand how the DesignSafe apps stage files, load modules, and run on TACC, you’re ready to take the next step:
**Writing and submitting SLURM job scripts directly on Stampede3 (or another TACC system)**.

This unlocks full flexibility:

* Launch **parameter sweeps** with shell loops or job arrays
* Fine-tune **MPI or OpenMP** configuration
* Chain multiple programs (preprocessing → simulation → postprocessing)
* Coordinate complex workflows or custom software stacks

> Writing your own SLURM scripts gives you **low-level control of HPC resources** — perfect for advanced studies, large batch workflows, or research automation.
