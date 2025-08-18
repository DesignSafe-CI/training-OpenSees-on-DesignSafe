# Understanding Paths

***Why Paths Matter When Running Applications***

A **path** is a string that describes the **location of a file or directory** in a storage system. It tells applications—like OpenSees or any Tapis App—**where to find input data and where to save outputs**, whether that’s in your **MyData**, **MyProjects**, or **shared workspace**, such as Stampede3.

On DesignSafe, you’ll often need to specify **full file paths** when working in environments such as:

* **JupyterHub**
* **Tapis**
* **Stampede3 (HPC)**

But **path formats vary** depending on the system, and each storage system is **mounted differently**:

| Environment    | Path Format               | Example                                                    |
| -------------- | ------------------------- | ---------------------------------------------------------- |
| **JupyterHub** | Mounted virtual folders   | `/home/jovyan/MyData/myfile.tcl`                           |
| **Stampede3**  | Absolute UNIX-style paths | `/scratch/01234/username/project/run01/input.tcl`          |
| **Tapis**      | URI-style references      | `tapis://designsafe.storage.community/myproject/input.tcl` |



## Why Paths Behave Differently

Although these systems all live under the DesignSafe umbrella, they are **physically separate compute and storage systems**, and each mounts file systems differently:

* All file systems (e.g., MyData, Community, Projects, Work, and even Scratch) are **mounted on the DesignSafe Data Depot backend**, even if you can’t see them all in the **web portal**.
* For example, **Stampede3’s `/scratch` directory is mounted**, but **not exposed** in the Data Depot interface.
* The **`Work` directory is your shared path**: it is mounted on both **JupyterHub and Stampede3**, meaning you can **exchange files** easily between your notebook session and an HPC job.
* However, files written to **Stampede’s scratch** during execution **cannot be directly accessed** from JupyterHub or Data Depot unless they are **copied to `Work` or `MyData`**. While the Data Depot doesn't give you direct access to scratch, it may give you access to them as the "execution directory" while a job is running.
* **Tapis can access all of these systems**, making it a unifying layer for automation, but it still requires you to provide the correct path for the system you're referencing.



## Why This Matters

Understanding which storage systems are available—and how they’re mounted—will help you avoid common issues like:

* File not found errors
* Job failures due to incorrect input/output paths
* Confusion when outputs don’t appear where you expect



## Takeaway

Yes, file management across DesignSafe can feel complex—because **each system is designed for a specific purpose**, and their **physical separation affects access**. But understanding these mount relationships gives you powerful control over:

* **How and where you store inputs**
* **How to retrieve outputs after a job**
* **How to write portable workflows across Jupyter, Tapis, and Stampede3**

By being intentional with your file paths and storage targets, you can **avoid disconnections**, streamline your workflows, and fully leverage the power of DesignSafe’s infrastructure.
