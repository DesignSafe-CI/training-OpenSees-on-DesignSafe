## Debugging and Monitoring Tips

* Use `print` or `puts` statements to identify which process is active
* Check Slurm `.out`/`.err` files or use `squeue` to monitor job status
* Use Tapis job history panel or `t.jobs.getJobStatus()` to track progress
* In Python:
  * Get rank with `ops.getPID()` or `MPI.COMM_WORLD.Get_rank()`
  * Use `os.getcwd()` and `os.listdir()` to inspect files during execution
