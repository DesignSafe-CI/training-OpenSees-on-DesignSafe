# OpenSeesPy Parallel

***Options for MultiProcess OpenSeesPy***

Running OpenSeesPy in parallel can dramatically reduce run times for large models or many independent simulations.
The optimal method depends on:

* **Interaction needs** – Do tasks share data (MPI) or run independently?
* **Execution environment** – Local machine, HPC system, or Jupyter?
* **Control level** – Simple launch vs. fine-grained process coordination?

The table below summarizes when to use each approach.

| Method                   | Best For                                   | Runs In                        | Communication Support | Jupyter Compatibility |
| ------------------------ | ------------------------------------------ | ------------------------------ | --------------------- | --------------------- |
| **Built-in MPI**         | Distributed-memory parallel runs           | HPC batch jobs, terminal       | ✅ Yes                 | ⚠️ Limited            |
| **mpi4py**             | Custom MPI communication/control in Python | HPC batch jobs, terminal       | ✅ Yes                 | ⚠️ Limited            |
| **concurrent.futures** | Embarrassingly parallel independent jobs   | Anywhere (local, HPC, Jupyter) | ❌ No                  | ✅ Yes                 |

---

### How to Choose

* Need **full MPI** and minimal code changes? → **Built-in MPI**
* Need **custom MPI logic** in Python? → **mpi4py**
* Jobs are **independent**? → **concurrent.futures**

---

### Parallel Methods

:::{dropdown} 1. Built-in MPI in OpenSeesPy

OpenSeesPy comes with optional MPI functionality compiled in. To use it, run your script with *mpiexec*, just like you would with OpenSeesMP:

```
mpiexec -n 4 python model.py
```

Inside your script:

```
ops.start()
pid = ops.getPID()
np = ops.getNP()      
```

⚠️ This MPI method may not work well in **Jupyter Notebooks** or certain IDEs, due to how those environments handle parallel processes. It **does** work reliably on HPC systems like **Stampede3**.

:::

:::{dropdown} 2. Using the *mpi4py* Python Package

An alternative and flexible method is to use the *mpi4py* package. This allows you to directly control MPI behavior within Python, giving you more custom control over communication and process logic.

You still run the script using *mpiexec*:

```
mpiexec -n 4 python model_mpi4py.py
```

Inside your script:

```
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
```

This gives you access to each process's rank and the total number of processes, allowing you to divide and coordinate tasks.

:::

:::{dropdown} 3. Optional: Parallel Execution via *concurrent.futures*

If your tasks are **independent** (e.g., many separate simulations), you don't need full MPI.

You can instead use Python's built-in *concurrent.futures* module to manage multiple subprocesses in parallel.

Example:

```
import os
from concurrent.futures import ProcessPoolExecutor

def run_simulation(job_id):
    os.system(f'python input_Parallel_concurrent_futures.py {job_id}')

with ProcessPoolExecutor(max_workers=4) as executor:
    executor.map(run_simulation, range(4))
```

This approach is ideal for **Monte Carlo simulations**, **parameter studies**, or **batch runs** where the simulations don't need to communicate with each other.

Works with both *python* and *OpenSees* commands:

```
os.system("OpenSees model.tcl")
```

```
os.system("python model.py")
```

:::

---

```{admonition} Key Notes
- **Built-in MPI** → Minimal code changes, good for full parallel models, best on HPC/terminal.  
- **mpi4py** → Maximum MPI control, custom communication, more coding effort.  
- **concurrent.futures** → Best for independent jobs, works anywhere, no MPI needed.  
- Jupyter is best for **independent jobs**; for MPI, prefer HPC batch or terminal.  
```

