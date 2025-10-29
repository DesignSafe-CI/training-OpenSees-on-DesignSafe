# Training Objectives

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

---

### Introductory Webinar

On September 17, 2025 we held a webinar introducing this training document. This webinar introduced DesignSafe as a unified platform for advancing natural hazards research, offering integrated tools for data management, interactive modeling, and high-performance computing. Using OpenSees as the primary case study, participants explored how to design and scale computational workflows — from small exploratory runs to automated HPC pipelines. The session emphasized the complete scientific workflow lifecycle, including model setup, job submission, monitoring, and results management. While focused on earthquake engineering, the strategies presented are broadly transferable to other domains such as CFD, climate modeling, and structural simulation.

[Click here](https://youtu.be/hexvyWy6G20?si=bo-n58AZ3loR0VuF) to access to the recording.

:::{dropdown} Presentation Slides

<div id="slideShow_WebinarSlides">
<script>
    addSlides("slideShow_WebinarSlides","../_static/Webinar/WebinarSlides/Slide","JPG",1,29)
</script>

:::

---
## Training Material

### Using the Training Notebooks

The pages in the training modules are **generated directly from Jupyter notebooks**. These notebooks are designed to be **templates for your own work** — you should *never start from scratch*. Instead:

* The notebooks are stored in the **DesignSafe Community Data folder**.
  * You can run them there, but you **cannot save changes** in Community Data.
  * Also, some notebooks include inputs such as job definitions or file paths that are specific to *my user account*.
    
* To work effectively, you should **copy the notebooks** to your own storage (e.g., **\~/MyData**).
* **Edit, duplicate, or modify** the appropriate cells to fit your workflow.

You can recognize a notebook-based page because it has an **“Open in DesignSafe”** button at the very top. Clicking it will bring you to **JupyterHub in DesignSafe**, where you’ll be prompted to log in (or create an account). I recommend copying **only relevant notebooks in the folder** into your path, as I may be editing the existing notebooks or adding new ones.

---

### Python Function Library

Alongside the notebooks, this training relies on a **custom library of Python functions** that I have developed. This library is stored in **DesignSafe Community Data** and is used extensively throughout the modules.

* You *can* copy the library directly from Community Data, but I **don’t recommend it**, since I am continually updating and improving it.
* Instead, look at the **script near the top of any notebook** that uses the library — copy that snippet into your own path so you can use a stable version of the library in your work.

