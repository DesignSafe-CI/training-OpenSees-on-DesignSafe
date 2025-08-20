## Training Objectives

In this training module, you’ll learn **how to “run” OpenSees from different computational environments within DesignSafe** — whether that’s the Jupyter Hub, the Web Portal, Tapis, or direct HPC command-line access.

Beyond OpenSees-specific workflows, this training covers the **core fundamentals necessary to build scalable and efficient scientific workflows** that optimize the resources available through **TACC and DesignSafe**. We'll discuss how to:

* Understand the **hardware architecture at TACC**, and how to best match job types to system capabilities.
* Use the **“software” infrastructure** that supports computation at scale — including **Tapis**, the **Tapis API**, and **task-specific Tapis Apps** available on DesignSafe.
* Navigate **file storage systems** on DesignSafe, including data staging, transfer, and archival strategies.
* Interact with different computational environments — from terminal-based CLI to Jupyter notebooks and batch script submissions — and know when to use each.

---

By the end of this module, you’ll know how to:

* **Use the DesignSafe Web Portal** to submit OpenSees jobs without writing any batch scripts.
* **Launch OpenSees from within a Jupyter notebook**, passing in variables or dynamically generating input files.
* **Run OpenSees directly from a terminal or Jupyter notebook**, using both Tcl and Python scripts.
* **Submit OpenSees jobs to the HPC system on TACC via SLURM**, providing input files and specifying resources like cores and wall time.
* **Automate large parameter studies** by modifying script values on the fly or using loops in Python.
* **Leverage Tapis APIs** to submit and monitor multiple jobs programmatically.
