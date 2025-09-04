## Job Workflow
***SLURM-Job Submission Workflow***

1. ### Job Submission

    You submit a job with a **job script** that specifies:
    
    - Number of nodes and cores (e.g., *32 cores on 4 nodes* -- *--ntasks=32*, *--nodes=4*)
    - Maximum runtime (e.g., *4 hours* -- *--time=04:00:00*)
    - Memory requirements (e.g., *--mem=16G*)
    - Partition (queue) to submit to (**NODE TYPE** -- *--partition=skx*)
    - Allocation (**project**)
    - Submit with: *sbatch job_script.sh*

1. ### Job Enters the Queue
    - Your job enters the **SLURM queue** and is assigned a **priority**.
    - You can **monitor the queue status** using SLURM commands (e.g., *squeue*, *sacct*, etc.)

1. ### SLURM Schedules the Job
    SLURM decides when and where to run your job based on:
    
    - **Requested resources**: Number of nodes, memory, and runtime.
    - **Queue priority**: System policies may prioritize shorter/smaller jobs.
    - **Current system load**: Jobs may wait until required nodes become free.

1. ### Job Execution
    - Once sufficient resources are available, **SLURM starts the job**.
    - Your job runs on the assigned compute nodes for the allocated time.

1. ### Job Completion
    When the job finishes:
    
    - **Output files** and **logs** (e.g., *SLURM-<jobID>.out*) are generated.
    - You can **check results and performance**.
