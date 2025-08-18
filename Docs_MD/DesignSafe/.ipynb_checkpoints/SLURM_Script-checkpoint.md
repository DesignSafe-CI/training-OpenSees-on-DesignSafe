# Job Script
***SLURM scripts are required to run batch jobs on Stampede3.***

**SLURM** (Simple Linux Utility for Resource Management) is an open-source job scheduler used in most large supercomputers — including TACC — to manage who runs what, where, and when.

This guide explains how to create and submit a SLURM job script to run your jobs on the **Stampede3** supercomputer at the **Texas Advanced Computing Center (TACC)**.
You may access the complete Stampede3 documentation via: https://docs.tacc.utexas.edu/hpc/stampede3/<br>
Note that the example script in the TACC documentation may not be up to date, but the fundamental concepts don't change.<br>

## What Is a SLURM Job Script?

A **SLURM job script** is a bash script containing:
- Resource requests (CPU, memory, time, etc.)
- Job configuration parameters
- Commands to load software modules and run applications

SLURM (Simple Linux Utility for Resource Management) is the scheduler used to queue, allocate, and manage jobs on TACC systems like Stampede3.


## Sample SLURM Job Script for Stampede3

Here’s a **basic but detailed SLURM job script** for Stampede3:

```bash
#!/bin/bash
#----------------------------------------------------
# SLURM Job Script for Stampede3 at TACC
#----------------------------------------------------
#SBATCH -A my_allocation         # Allocation name (from TACC allocation)
#SBATCH -J my_job_name           # Job name
#SBATCH -o my_job_name.o%j       # Standard-output path (%j expands to jobId)
#SBATCH -e my_job_name.e%j       # Standard-error file path
#SBATCH -N 2                     # Number of nodes
#SBATCH -n 48                    # Total number of MPI tasks (usually cores)
#SBATCH -p skx                   # Queue/partition name
#SBATCH -t 120                   # Wall time (minutes)
#SBATCH --mail-user=your_email@utexas.edu   # Email for notifications
#SBATCH --mail-type=all          # Send email on job start, end, and fail


#----------------------------------------------------
# Load required modules
#----------------------------------------------------
module load hdf5/1.14.4
module load opensees

#----------------------------------------------------
# Job environment info (optional but helpful)
#----------------------------------------------------
echo "Job ID: $SLURM_JOB_ID"
echo "Running on nodes: $SLURM_JOB_NODELIST"
echo "Number of nodes: $SLURM_JOB_NUM_NODES"
echo "Number of cores: $SLURM_NTASKS"

#----------------------------------------------------
# Run your application
#----------------------------------------------------
# Example: MPI-based program
ibrun ./my_mpi_program input.dat

#----------------------------------------------------
# End of script
#----------------------------------------------------
```

## Explanation of Key SLURM Parameters

| SLURM Directive           | Purpose |
|---------------------------|---------|
| `#SBATCH -A my_allocation` | Specifies the allocation/project under which this job will be charged. You must have an active TACC allocation. |
| `#SBATCH -J my_job_name`  | Sets a descriptive name for your job. Useful for tracking it in the queue and output files. |
| `#SBATCH -o my_job_name.o%j` | Redirects standard output to a file. `%j` auto-inserts the job ID. |
| `#SBATCH -e my_job_name.e%j` | Redirects standard error output to a file. Keeping error and output separate can help debug issues. |
| `#SBATCH -N 2`            | Requests 2 full nodes. |
| `#SBATCH -n 46`           | Specifies the **total number of tasks** (processes). For MPI, this typically equals the total number of cores. |
| `#SBATCH -p skx`       | Chooses the `normal` queue (partition). Other options include `development`, `largemem`, etc. |
| `#SBATCH -t 120`     | Sets the wall-clock time limit (in minutes). Jobs exceeding this will be terminated. |
| `#SBATCH --mail-user=email@domain.edu` | Email address to notify about job events (start, end, failure). |
| `#SBATCH --mail-type=all` | When to send emails: `BEGIN`, `END`, `FAIL`, `ALL`, etc. |





