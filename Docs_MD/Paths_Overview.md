# Working with Paths

***Why Paths Matter When Running Applications***

A **path** is the address of a file or directory. It tells applications—like OpenSees or any Tapis app—**where to find inputs and where to write outputs** across your storage spaces (*MyData*, *MyProjects*, shared work areas, and HPC systems like Stampede3).

---

## Relative vs. Full (Absolute) Paths

**Relative path**

* Interpreted **from your current working directory (CWD)**.
* Short and convenient when you’re “already in” the right folder.
* **Does not start with `/`**.
* Changes meaning if your CWD changes.

**Full (absolute) path**

* The **complete address from the filesystem root**, starting with **/**.
* Works regardless of CWD—**safer for batch jobs, Tapis jobs, and SLURM**.
* Often uses env vars (*$HOME*, *$WORK*, *$SCRATCH*) for portability.

**What Jupyter shows vs. what the OS/HPC uses**

* The **Jupyter file browser** and notebooks operate relative to the notebook’s CWD, so *data/run1.csv* “just works” there.
* HPC/Tapis launchers may change CWD; **absolute paths are more reliable** in wrappers and batch jobs.

### Quick examples

| Context                             | You write                         | Resolves to                     |
| ----------------------------------- | --------------------------------- | ------------------------------- |
| Relative (CWD = */home/user/book/*) | *data/run1.csv*                   | */home/user/book/data/run1.csv* |
| “Go up one level”                   | *../inputs/record.at2*            | */home/user/inputs/record.at2*  |
| Full (absolute)                     | */home/user/book/data/run1.csv*   | Always that path                |
| Home shortcut                       | *~/book/data/run1.csv*            | *$HOME/book/data/run1.csv*      |
| HPC env var                         | *$WORK/myproj/cases/c1*           | Your site’s “work” area         |
| Python (portable)                   | *Path("data/run1.csv").resolve()* | Absolute path computed from CWD |

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

## When to Use Relative vs. Full Paths

* **Use relative paths** for quick local work **inside Jupyter** when you control CWD (notebooks, small scripts).
* **Use full paths** when:

  * Submitting **Tapis** or **SLURM** jobs (launchers may change CWD).
  * Sharing inputs/outputs across scripts, nodes, or users.
  * Writing **reusable automation** that must run from any directory.

---

:::{dropdown}Practical Recipes

**In a Notebook (Python):**

```python
from pathlib import Path
print("CWD:", Path.cwd())                           # where you are
print("Absolute:", Path("data/run1.csv").resolve()) # get a full path
print("Home:", Path("~").expanduser())              # your home dir
```

**In a shell (terminal or notebook cell):**

```bash
pwd                  # show current directory
echo "$HOME"         # home
echo "$WORK"         # HPC work area (if defined by site)
# show absolute path (many Linux systems)
readlink -f data/run1.csv
```

**Anchor relative paths to a script’s location (Python):**

```python
from pathlib import Path
BASE = Path(__file__).resolve().parent
inp = BASE / "inputs" / "model.tcl"    # stable even if CWD changes
```

**Keep outputs portable (Python):**

```python
outdir = Path("~/results").expanduser()
outdir.mkdir(parents=True, exist_ok=True)
f = outdir / "run1.csv"
```

**Tapis transfers (conceptual):**

* Think: **`(systemId="designsafe.storage.default", path="/Users/you/inputs/model.tcl")`**
* For HPC job I/O, your wrapper will typically use **absolute filesystem paths** on the compute system (e.g., `$WORK/myproj/...`).

:::
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