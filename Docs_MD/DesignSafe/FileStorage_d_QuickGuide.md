# File Storage: Quick Training Guide

In HPC, every job either starts or ends with **data**. Choosing the right storage location avoids slowdowns, data loss, or confusion.

---

## Storage Cheat Sheet

* **MyData** → Your personal notebook

  * Private, backed up, long-term
  * Best for personal files, scripts, tests

* **MyProjects** → Shared filing cabinet

  * Collaborative, curation-ready, long-term
  * Best for team data, archiving, publication

* **Work** → Scratchpad for jobs

  * High-performance, temporary, not backed up
  * Best for staging inputs & writing job outputs

**Rule of Thumb:**

* If it’s important → put it in **MyData** or **MyProjects**
* If it’s temporary → use **Work**

---

## Common Mistakes to Avoid

⚠️ **Don’t leave results in Work** — it’s not backed up
⚠️ **Don’t use MyData for teams** — use MyProjects instead
⚠️ **Don’t try to save to Community/Published** — they’re read-only
⚠️ **Don’t run jobs directly from Corral** — stage to Work first

---

## Storage Decision Tree

**Are you running a compute job?**
→ Yes → **Work**
→ No → Do you need to share?
  → Yes → **MyProjects**
  → No → **MyData**

Public reference data? → **Community/Published** (read-only)

## Visualizing the Data Flow

The diagram below illustrates how data moves between storage systems. Node-local storage sits inside the compute jobs “black box,” representing storage available only while your job runs.

<img src="../../_images/FileStorageOnDesignSafe.png" alt="FileStorage On DesignSafe" width="75%" />  
