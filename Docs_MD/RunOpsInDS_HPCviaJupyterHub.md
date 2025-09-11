# OpenSees on HPC
***OpenSees on HPC via JupyterHub***

DesignSafe’s JupyterHub provides an interactive environment where you can prepare, submit, and monitor jobs directly on TACC’s HPC systems. Instead of writing your own SLURM scripts, you can use **Tapis Apps**—predefined job templates that take care of loading the correct modules, staging input files, running OpenSees on HPC nodes, and saving results back to your storage.

Running OpenSees this way is especially useful when you want to combine the flexibility of Jupyter notebooks with the power of HPC. You can test or pre-process models interactively, then submit larger production runs to Stampede3 without leaving JupyterHub.

When comparing the three available workflows:

* **Web Portal → HPC**
  Easiest to use with a point-and-click interface, but less flexible for automation or scripting.
* **JupyterHub → Local**
  Good for testing small models interactively, but limited to the resources available in JupyterHub (single node).
* **JupyterHub → HPC via Tapis Apps**
  Combines the best of both: scripting and automation from JupyterHub with the full scalability of HPC.

**Step-by-step workflow:**

1. Prepare your OpenSees input files in your DesignSafe storage -- you can do this within JupyterHub
2. Select the appropriate Tapis App (e.g., OpenSeesMP for parallel jobs).
3. Submit the job from a Jupyter notebook or terminal using the app definition.
4. Tapis stages files, launches the job on HPC, and manages the scheduler.
5. Results are returned to your designated storage for post-processing.
6. Postporcess and prepare publication-quality material in JupyterHub.

All of the above steps can be managed from a single Jupyter Notebook.

This approach ensures that you use the same standardized OpenSees applications available through the Web Portal and the Tapis API, keeping your workflows consistent across platforms.
