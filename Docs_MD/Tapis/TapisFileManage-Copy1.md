# Tapis: File Management
***How DesignSafe File Storage and Tapis Work Together***

The objective of this section is to explain clearly to users (especially beginners) how Tapis paths work across different systems, with an emphasis on DesignSafe nuances.

Tapis is the system that powers data access and job submission on DesignSafe. It provides a unified interface to interact with **multiple file storage systems**, including:

* **Corral** (DesignSafe’s long-term data repository)
* **Compute system file spaces** like `/work`, `/scratch`, and `/home` on Stampede3

With Tapis, you can **list, upload, download, move, and delete files** across these systems using a common API — whether through the DesignSafe portal, Python scripts, or automation tools.

This allows you to:

* Stage input files from Corral to a compute system before a job runs
* Automatically collect output and move it back to Corral afterward
* Manage project data consistently, regardless of where it physically resides

Tapis acts as the **glue** between storage locations and compute workflows, helping streamline data movement and improve reproducibility.

## Tapis Path Format

Tapis uses a URI-like format to reference files:

```
tapis://<system-name>/<path-to-file-or-directory>
```

For example:

```
tapis://designsafe.storage.default/<username>/project/data.txt
```

This abstraction hides the underlying differences between systems — but only up to a point. In practice, you must still be aware of how different systems mount and reference storage.

When working with Tapis on the DesignSafe platform, it is essential to understand that paths to files and directories are not uniform across all systems. 
Each computing environment (e.g., Stampede3, JupyterHub, OpenSees VM) may reference your files differently, and Tapis expects a unique format that resembles a URL or 
HTTP-style string.
