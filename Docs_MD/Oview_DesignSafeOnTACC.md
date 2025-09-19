# DesignSafe & TACC

**DesignSafe** offers a comprehensive environment for conducting, managing, and analyzing workflows related to natural hazards engineering. It combines interactive tools, data services, and computational resources to support your entire research lifecycle — from model development to large-scale simulations to advanced post-processing.

At its core, DesignSafe is tightly integrated with the **Texas Advanced Computing Center (TACC)**, which supplies the <u>high-performance computing (HPC) systems and large-scale storage</u> required to execute demanding analyses. Most jobs submitted through DesignSafe — whether via the web portal, Jupyter notebooks, or automated pipelines — ultimately run on TACC’s powerful supercomputers like **Stampede3**, making it possible to carry out simulations that would be unfeasible on local machines.

DesignSafe’s platform is built with **flexibility and scalability in mind!**


## Varying Computational Needs
The following table provies an example of the different computation needs for different types of analyses:


<img src="../_images/VaryingComputationalNeeds.jpg" alt="Varying Computational Needs" width="50%" />



| Analysis Type            | Memory Usage                          | CPU vs GPU                  | Parallelism Needs                  | Speed Sensitivity                  | Description + Reason / Notes |
|---------------------------|---------------------------------------|-----------------------------|-------------------------------------|-------------------------------------|-------------------------------|
| Parallel Monte Carlo      | <span style="background-color:#b3e5fc;">Low–Moderate</span> | ✅ CPU preferred             | <span style="background-color:#b3e5fc;">High</span>           | <span style="background-color:#ffe082;">Low–Moderate</span> | Monte Carlo methods involve running repeated random samples to solve deterministic problems that are too complex for direct computation. Trivially parallel: each run is independent; minimal memory overhead, great for CPU clusters or grid computing. |
| Parametric Sweeps         | <span style="background-color:#b3e5fc;">Low–Moderate</span> | ✅ CPU preferred             | <span style="background-color:#b3e5fc;">High</span>           | <span style="background-color:#ffe082;">Low–Moderate</span> | Run a model or simulation across a range of input parameters to study system behavior or performance variation. Like Monte Carlo, easily parallelized with little inter-process communication. |
| ML Training Loops         | <span style="background-color:#ffe082;">Moderate–High</span> | <span style="background-color:#ef9a9a;">GPU accelerated</span> | <span style="background-color:#b3e5fc;">Moderate–High</span> | <span style="background-color:#ef9a9a;">High</span> | ML training involves iterative updates to a model's parameters using a training dataset. GPU-accelerated for fast matrix ops; training requires high compute, memory usage depends on model size. |
| Coupled Simulations       | <span style="background-color:#ef9a9a;">High</span> | ✅ CPU dominated             | <span style="background-color:#ffe082;">Low–Moderate</span>   | <span style="background-color:#ef9a9a;">High</span> | Simultaneously simulate multiple interacting physical domains or solvers (e.g., fluid + structure, heat + stress). Memory-intensive due to mesh/data exchange between solvers; limited parallelization unless domain-decomposed. |
| Stepwise Simulation       | <span style="background-color:#ffe082;">Moderate</span> | ✅ CPU preferred             | <span style="background-color:#ffe082;">Moderate</span>       | <span style="background-color:#ffe082;">Moderate</span> | A sequential, time-marching simulation solving physical phenomena across a time domain, e.g., using finite difference, finite element, or finite volume methods. Each step may use iterative solvers; memory builds with history data. |
| Batch Pre/Post-Processing | <span style="background-color:#b3e5fc;">Low</span> | ✅🔴 CPU or GPU capable       | <span style="background-color:#b3e5fc;">High</span>           | <span style="background-color:#ffe082;">Low–Moderate</span> | Transform or clean a large batch of data files or inputs to prepare for further analysis or training. Lightweight tasks like data cleaning, often highly parallel and not memory-intensive. |
| **Legend**                | colspan=6><span style="background-color:#b3e5fc; font-size:90%;">Blue = Low</span> &nbsp; | <span style="background-color:#ffe082; font-size:90%;">Yellow = Moderate</span> &nbsp; | <span style="background-color:#ef9a9a; font-size:90%;">Red = High</span> &nbsp; | *Key for colored cells* |
