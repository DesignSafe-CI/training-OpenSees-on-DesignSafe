# Tapis: File Management
***How DesignSafe File Storage and Tapis Work Together***

Tapis powers file access and job submission on DesignSafe. It provides a consistent interface to interact with **multiple storage systems** and **compute environments**, making it easier to manage data before, during, and after simulation workflows.

With Tapis, you can:

* **List, upload, download, move, and delete files** across different storage systems
* **Stage input files** (e.g., move from long-term storage to a compute node)
* **Collect outputs automatically** and return them to Corral or MyData
* Use the same scripting or automation tools across storage locations

Tapis acts as the **glue** between DesignSafe’s storage and compute environments, streamlining data movement and improving reproducibility.

---

## Storage Systems on DesignSafe

Tapis connects to several distinct file storage systems, each with a unique role. You interact with them using **URI-style paths** like:

```
tapis://<system-name>/<relative-path>
```

Here’s a reference table for commonly used Tapis paths:

| Storage Type        | Example Tapis Path                              | Notes                                  |
| ------------------- | ----------------------------------------------- | -------------------------------------- |
| **MyData**          | `tapis://designsafe.storage.default/jdoe/`      | Your personal storage                  |
| **Work**            | `tapis://cloud.data/work/05072/jdoe/stampede3/` | Shared group allocation; used for jobs |
| **Community**       | `tapis://designsafe.storage.community/`         | Public files from the community        |
| **MyProjects**      | `tapis://project-61bab56…`                      | Linked to specific DesignSafe projects |
| **NHERI Published** | `tapis://designsafe.storage.published/PRJ-1628` | Archived datasets                      |
| **NEES Published**  | `tapis://nees.public/NEES-2`                    | Legacy NEES content                    |
| **Scratch**         | *Not available through Tapis*                   | Temporary compute storage              |
| **Home**            | *Not available through Tapis*                   | Home directories on HPC systems        |

⚠️ Each URI must include the correct **system name** and **path** (which often includes your username, group ID, or project ID). There is **no built-in Tapis command** to automatically discover your base paths — but you can find them manually (see below).

---

## Understanding Tapis Paths in Practice

Although Tapis paths look like web URLs, they reference files stored across different systems such as:

* **Corral** (long-term storage for MyData, Community, and Projects)
* **Stampede3** compute system (`/work`, `/home`, `/scratch`)
* **JupyterHub**, **OpenSees VMs**, or containerized environments

Each environment may **mount or reference file locations differently**, so it’s important to understand how your job or script will access data.

For example, a job running on Stampede3 using `OpenSeesMP` will expect paths under `/work` or `/scratch`, while a Jupyter notebook may refer to the same data using a Corral-based Tapis URI.

---

## How to Locate Your Tapis Paths (Manual Method)

Until automated tools are provided, here’s a reliable method to find valid Tapis paths:

### 🔍 To find your `/work` path on Stampede3:

1. Go to the OpenSeesMP App on DesignSafe: 'https://www.designsafe-ci.org/workspace/opensees-mp-s3'.
2. Start creating a job (no need to submit it).
3. In the **Input Directory** field, click the folder icon to browse.
4. Navigate to your work folder and select it.
5. Copy the **full Tapis URI** shown in the field — e.g.:

   ```
   tapis://cloud.data/work/05072/silvia/stampede3/somefolder
   ```
6. Use the **base portion** in scripts:

   ```
   tapis://cloud.data/work/05072/silvia/
   ```

```{tip}
Repeat this for each storage system you use and **save the paths** in a file like `user_paths.json`. This will simplify scripting and avoid repeated lookups. We’ll walk through this during the training session.
```

---

This approach ensures you’re using correct and consistent Tapis URIs across different tools, scripts, and environments—an essential skill for automating job submissions and managing your project data efficiently on DesignSafe.
