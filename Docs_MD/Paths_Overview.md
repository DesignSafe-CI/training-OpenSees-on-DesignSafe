# Working with Paths

***Why Paths Matter When Running Applications***

A **path** is the address of a file or directory. It tells applications—like OpenSees or any Tapis app—**where to find inputs and where to write outputs** across your storage spaces (*MyData*, *MyProjects*, shared work areas, and HPC systems like Stampede3).



---

## Path Formats by Environment

Path formats vary by system, and each storage is **mounted differently**.

| Environment    | Path Format                           | Example                                                    |
| -------------- | ------------------------------------- | ---------------------------------------------------------- |
| **JupyterHub** | Mounted home/workspaces (Linux paths) | */home/jovyan/MyData/myfile.tcl*                           |
| **Stampede3**  | Absolute UNIX paths                   | */scratch/01234/username/project/run01/input.tcl*          |
| **Tapis**      | System + path (URI-like reference)    | *tapis://designsafe.storage.community/myproject/input.tcl* |

> **Note:** In Tapis code you usually pass ***systemId* + *path*** rather than a literal *tapis://* URI; the URI form is a convenient shorthand for documentation.

---

## Why Paths Behave Differently on DesignSafe

Although they’re under the DesignSafe umbrella, **compute and storage systems are physically separate**, and mounts differ:

* All file systems (MyData, Community, Projects, Work, Scratch) are mounted on the **Data Depot backend**, even if not all are visible in the web UI.
* *Stampede3 /scratch* is mounted on HPC but **not directly exposed** in the Data Depot interface.
* ***Work* is your shared bridge**: it’s mounted on **both JupyterHub, Stampede3, and Data Depot**, so you can **exchange files** between notebooks and HPC jobs.
* Files written to **Stampede3 scratch** during execution **aren’t visible** in JupyterHub/Data Depot **unless you copy them** to *Work* or *MyData*. (During an active job, the portal may show an *execution directory* view, but that’s transient.)
* **Tapis can access all of these systems**—it’s a unifying layer—but you must provide **the correct path for the target system** in Tapis format (more on this later).

---

## Common Errors & Quick Fixes

* **File not found in jobs** → Use **full paths** or anchor relative paths to a known base.
* **Works in Jupyter, fails on HPC** → CWD differs; switch to **absolute paths** or expand `~`/env vars.
* **Scratch outputs “missing” in Jupyter** → Copy results from **Scratch → Work/MyData** before inspecting in Jupyter.
* **Spaces in paths** → Avoid them. Otherwise, quote carefully or use `pathlib.Path`.

---

## Why This Matters

Understanding mounts and path semantics helps you avoid:

* “File not found” errors
* Job failures due to incorrect I/O locations
* Confusion when outputs “disappear” (they’re in Scratch, not Work)

With the right path strategy you can:

* Place inputs where jobs can read them quickly,
* Retrieve outputs reliably,
* Write **portable workflows** that run across Jupyter, Tapis, and Stampede3 without edits.

---

:::{admonition}One-Paragraph Takeaway

Relative paths are **shortcuts from where you’re standing** (your CWD); full paths are the **complete address**. Jupyter emphasizes relative convenience; **HPC/Tapis workflows are safer with full paths** and environment variables. Use `pathlib` to resolve and compose paths cleanly, rely on **`Work`** as your bridge between Jupyter and Stampede3, and copy any **Scratch** results you need to keep into **Work** or **MyData**.
:::