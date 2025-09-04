<!-- # Tapis Apps
***Tapis Applications***

DesignSafe and TACC provide a suite of **pre-configured applications (“apps”)** that let you run common workflows on HPC systems through a web interface or programmatic submissions. Each app is tailored to a specific software package — for example, OpenSees, OpenFOAM, or custom post-processing tools. These apps manage every aspect of the **SLURM** job for you automatically using **Tapis** in the background.

These apps handle much of the complexity of HPC job submission for you:

* **Create SLURM job scripts automatically**
* **Copy your input files to the HPC scratch space** (for faster execution)
* **Run the job on the appropriate compute nodes**
* **Return the output files back to your DesignSafe workspace**

This ensures your analyses take full advantage of TACC’s architecture without requiring you to manually stage files, write job scripts, or run `sbatch` by hand.

These apps use Tapis -- the TACC API -- to submit jobs to the HPC system.

## Typical inputs to a DesignSafe app

When submitting through the Web Portal, apps typically expect:

* **Main input file(s)**: e.g., your `model.tcl` or `model.py`
* **Optional supporting files**: additional scripts, data, or property definitions
* **Run parameters**: like number of cores, wall time, or special flags (depending on the app)
* **Output preferences**: sometimes you can specify where or how results are organized

Because the apps create the SLURM environment for you, you don’t usually need to write your own job scripts — though advanced users can still do so for more direct control.

### Why have these apps?

DesignSafe apps exist to:

* **Abstract away the HPC job management**, so you don’t have to manually write SLURM scripts, handle staging to scratch, or monitor low-level resource details.

* **Standardize the environment**, so everyone gets compatible modules, compilers, and optimized builds — which matters a lot for packages like OpenSeesMP, OpenFOAM, or ADCIRC.

* **Automate file movement**, copying your inputs to the fastest storage (scratch) for execution and returning your outputs cleanly to your DesignSafe workspace (**My Data**) afterward.

This helps researchers stay focused on engineering problems, while still leveraging the full performance of TACC’s supercomputers.

Perfect — here’s a **short, strong concluding box** you can drop at the end of that section. It gives your readers a clear invitation to move into even more advanced, fully customized workflows, while still tying it back to everything they’ve learned from the apps.

### Still want more control?

If you’re ready to move beyond what the Web Portal apps automate for you, you have two powerful options:

* **Write your own SLURM scripts**

  * Use the DesignSafe app repositories as reference templates to see exactly how to load modules, set up MPI runs, and stage your files.
  * This gives you maximum flexibility — you can bundle thousands of parameter sets, fine-tune MPI ranks, and precisely control I/O.

* **Use Tapis from Python (or directly via the CLI)**

  * Submit jobs programmatically from a Jupyter notebook or Python script.
  * Automate ensembles, parameter sweeps, and even hybrid workflows that combine pre-processing, HPC analysis, and post-processing in a single pipeline.

This is often the **next step** after mastering the Web Portal apps. You get the same robust environment setup, but can orchestrate complex multi-job studies exactly the way your research demands.


 -->