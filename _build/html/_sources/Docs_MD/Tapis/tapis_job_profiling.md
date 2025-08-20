# Job Profiling
***Profiling Job State Durations to Improve Efficiency**

By tracking how long a job spends in each state (like *PENDING*, *QUEUED*, *RUNNING*, or *ARCHIVING*), users can **identify bottlenecks** in their workflow. This process is known as **profiling**.

For example:

* If a job spends **a long time in *PENDING* or *QUEUED***, it may indicate that your requested resources are too large, or you're using a busy system queue.
* If the job runs quickly but takes a long time in *ARCHIVING*, you might improve performance by writing fewer or smaller output files.
* If your job starts but immediately enters *FAILED*, it may signal issues with input files, runtime errors, or environment setup.

Profiling lets you:

* Optimize resource requests (e.g., memory, cores, wall time)
* Choose better execution queues or times of day
* Refactor I/O-heavy scripts
* Understand overhead (e.g., input staging or archiving delays)

Look at the **Job-History Data** to profile your jobs.

 *Profiling your job lifecycle helps you move from just "getting a job to run" to "running efficiently at scale."*
