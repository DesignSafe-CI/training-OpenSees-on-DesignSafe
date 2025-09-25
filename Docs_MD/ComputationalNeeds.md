## Computational Needs

Users run many different kinds of analyses on DesignSafe, and not all of them stress the hardware in the same way. To make this clearer, we separate the information into two parts:

1. **Analysis Types** — describes what each type of workload is, with examples of how it is used in earthquake engineering and simulation.
2. **Computational Needs** — summarizes the demands of each workload in terms of memory, CPU/GPU usage, scalability, and speed sensitivity.

This separation emphasizes two points:

* **Conceptual clarity** → Users can first identify the type of analysis they’re doing without worrying about compute details.
* **Computational diversity** → Some tasks are trivially parallel (Monte Carlo, sweeps), while others are memory-bound (coupled simulations) or GPU-accelerated (ML training).
* **Scalable *and* adaptable environments** → DesignSafe provides access to HPC resources that are both scalable and adaptable, because there is no “one-size-fits-all” solution. Some workloads benefit from spreading across many nodes (parallel Monte Carlo), while others require large memory per node (coupled multiphysics). Importantly, you can’t simply add more nodes as a simulation grows in scope — different analysis types demand different strategies for scaling.

---

### 1. Analysis Types

The following table provides an overview of the kinds of analyses that users may run on DesignSafe:

| Analysis Type                 | Description                                                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Parallel Monte Carlo**      | Monte Carlo methods involve running repeated random samples to solve deterministic problems that are too complex for direct computation.                         |
| **Parametric Sweeps**         | Run a model or simulation across a range of input parameters to study system behavior or performance variation.                                                  |
| **ML Training Loops**         | ML training involves iterative updates to a model's parameters using a training dataset.                                                                         |
| **Coupled Simulations**       | Simultaneously simulate multiple interacting physical domains or solvers (e.g., fluid + structure, heat + stress).                                               |
| **Stepwise Simulation**       | A sequential, time-marching simulation solving physical phenomena across a time domain, e.g., using finite difference, finite element, or finite volume methods. |
| **Batch Pre/Post-Processing** | Transform or clean a large batch of data files or inputs to prepare for further analysis or training.                                                            |

---

### 2. Computational Needs

The table below shows how these analyses differ in their computational characteristics. This helps users match their workload to the right DesignSafe resource (e.g., JupyterHub, HPC batch jobs, or Tapis apps):

| Analysis Type                 | Memory Usage     | CPU vs GPU             | Parallelism Needs | Speed Sensitivity | Reason / Notes                                                                                                  |
| ----------------------------- | ---------------- | ---------------------- | ----------------- | ----------------- | --------------------------------------------------------------------------------------------------------------- |
| **Parallel Monte Carlo**      | 🔹 Low–Moderate  | ✅ CPU preferred        | 🔹 High           | 🔸 Low–Moderate   | Trivially parallel: each run is independent; minimal memory overhead, great for CPU clusters or grid computing. |
| **Parametric Sweeps**         | 🔹 Low–Moderate  | ✅ CPU preferred        | 🔹 High           | 🔸 Low–Moderate   | Like Monte Carlo, easily parallelized with little inter-process communication.                                  |
| **ML Training Loops**         | 🔸 Moderate–High | 🔴 GPU accelerated     | 🔹 Moderate–High  | 🔴 High           | GPU-accelerated for fast matrix ops; training requires high compute, memory usage depends on model size.        |
| **Coupled Simulations**       | 🔴 High          | ✅ CPU dominated        | 🔸 Low–Moderate   | 🔴 High           | Memory-intensive due to mesh/data exchange between solvers; limited parallelization unless domain-decomposed.   |
| **Stepwise Simulation**       | 🔸 Moderate      | ✅ CPU preferred        | 🔸 Moderate       | 🔸 Moderate       | Each step may use iterative solvers; memory builds with history data.                                           |
| **Batch Pre/Post-Processing** | 🔹 Low           | ✅🔴 CPU or GPU capable | 🔹 High           | 🔸 Low–Moderate   | Lightweight tasks like data cleaning, often highly parallel and not memory-intensive.                           |

---

### How to Use These Tables

* If your workload looks like **Monte Carlo** or **parametric sweeps** → Use a job array, since these are *embarrassingly parallel*.
* If you are doing a **stepwise time simulation** → Expect moderate scaling, and prefer CPU jobs with sufficient walltime.
* If you are combining **multiple solvers (coupled simulation)** → Prioritize **memory per node** and consider domain decomposition.
* If you are doing **ML training or pre/post-processing** → These may use different DesignSafe resources (Python/GPU environments, batch preprocessing tools).

> **Key takeaway:** On DesignSafe, HPC resources are not just about scaling “up” by adding more nodes — they are also about adapting to the computational profile of your analysis. Each workload has its own “best fit” execution environment.
