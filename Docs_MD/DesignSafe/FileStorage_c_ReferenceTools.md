# File Storage: Reference Tools

## Quick Reference: Cheat Sheet

:::{admonition} **Storage Cheat Sheet**

* **MyData** → Your personal notebook

  * Private, backed up, long-term
  * Best for personal files, scripts, tests

* **MyProjects** → Shared filing cabinet

  * Collaborative, long-term, curation-ready
  * Best for team data, archiving, publication

* **Work** → Scratchpad for active jobs

  * High-performance, temporary, not backed up
  * Best for staging inputs & writing job outputs

**Rule of Thumb:**

* *If it’s important, back it up (MyData or MyProjects).*
* *If it’s temporary, run it in Work.*
:::

---

## Common Mistakes to Avoid

:::{admonition} ⚠️ Storage Pitfalls

1. **Leaving important results in Work**

   * Work is **not backed up** and may be purged without warning.
   * Always copy valuable results to MyProjects or MyData.

2. **Using MyData for team projects**

   * Files in MyData are private unless explicitly shared.
   * Use MyProjects for collaboration.

3. **Relying on CommunityData or Published for active work**

   * These directories are **read-only**.
   * They are for reference only.

4. **Running HPC jobs directly from Corral**

   * Corral is network-mounted and slower for I/O-intensive workloads.
   * Always stage input/output to Work for active jobs.

5. **Confusing Work with long-term project storage**

   * Work is high-performance but temporary.
   * Use MyProjects for durable project data.

**Remember:** Corral = archive, Work = scratch, Node-local = temporary runtime.
:::

---

## Storage Decision Tree

:::{admonition} **Which Storage Should I Use?**

* **Step 1: Are you running a compute job?**

  * **Yes** → Use **Work** for job inputs/outputs (fast I/O).
  * **No** → Continue ↓

* **Step 2: Do you need to share the data with a team?**

  * **Yes** → Use **MyProjects** (collaboration, publication).
  * **No** → Continue ↓

* **Step 3: Do you just need a private workspace?**

  * **Yes** → Use **MyData** (personal, backed up).
  * **No** → Continue ↓

* **Step 4: Is this public reference data you need to *read*?**

  * **Yes** → Access from **CommunityData** or **Published** (read-only).
  * **No** → Re-check your workflow; you may be mixing storage types.

**In short:**

* **Work** = jobs (fast, temporary).
* **MyProjects** = team (shared, curation-ready).
* **MyData** = personal (private, backed up).
* **Community/Published** = reference only.

:::
