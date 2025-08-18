# File-Storage Guide
***DesignSafe Storage Guide: MyData, MyProjects, and Work***

DesignSafe offers several storage areas to support different stages of your research workflow. Each serves a distinct purpose, and selecting the correct storage location will help you work efficiently, share data correctly, and ensure data integrity.

DesignSafe includes multiple storage systems, each with its own conventions:

* **MyData**: Standard "home" directory. Accessible from most environments.
* **MyProjects**: Project-Specific shared datasets accessible only to users in project
* **Work**: Shared project space; requires both username and group/project ID.
* **CommunityData**: Public datasets and examples.
* **Published**: Public published datasets.

CommunityData and Published are read-only directories -- you cannot save to these directories during your work, hence we will not discuss them in this particualr section.

## Overview Table

| Storage Area   | Purpose                                     | Access                              | Persistence                            | Performance |
| -------------- | ------------------------------------------- | ----------------------------------- | -------------------------------------- | ----------- |
| **MyData**     | Personal storage                            | Private (owner only, unless shared) | Long-term, backed up                   | Standard    |
| **MyProjects** | Project-based collaborative storage         | Shared with project team            | Long-term, archival, and publication   | Standard    |
| **Work**       | High-performance scratch space for HPC jobs | Accessible from compute nodes, data depot, and JupyterHub (owner only, unless shared)       | Long-term, NOT backed up               | High        |


:::{admonition} **MyData**

*Personal private storage space.*

* For your own files: input files, scripts, outputs, notes, small test datasets.
* Only visible to you unless files are explicitly shared.
* Ideal for:

  * Early-stage work and drafts.
  * Preparing input files.
  * Testing small runs and simulations.
  * Personal scripts and tools.
  * Storing results for personal review.
* Not directly tied to publication or curation.
* Long-term persistence (subject to overall DesignSafe storage allocations).

***Use MyData when you’re working solo or building/testing something privately.***

:::

:::{admonition} **MyProjects**

*Collaborative project-based storage.*

* Linked to a DesignSafe project ID created in the portal.
* Accessible to all project team members.
* Supports:

  * Team data sharing.
  * Large experiments and simulations.
  * Multi-user workflows.
  * Data curation and publication (via DesignSafe Data Depot).
* Allows curation for formal publication, DOI assignment, and public discoverability.
* Long-term storage for finalized data.
* Ideal for:

  * Collaborative input/output data.
  * Shared analysis results.
  * Any data intended for public release.
  * Archival storage associated with funded projects.

***Use MyProjects when you’re collaborating, sharing data with others, or preparing data for publication.***

:::


:::{admonition} **Work**

*Temporary high-performance scratch storage.*

* Optimized for active HPC jobs.
* Mounted directly to compute nodes for fast I/O.
* Ideal for:

  * Staging large input files before compute jobs.
  * Writing large output files during simulations.
  * Handling temporary files created during large-scale runs.
  * Fast read/write during computational processing.
* Quota limits usually based on TACC allocation.

***Use Work for temporary, high-performance storage while running HPC jobs. Do not use Work for long-term data storage. Always move important results from Work to MyProjects or MyData after your job completes.***

:::

## Typical Research Workflow Example

1. **Prepare input files and test scripts** → store in **MyData**
2. **Share input files with project team** → upload to **MyProjects**
3. **Transfer large datasets to Work** before running compute jobs
4. **Run HPC jobs** (OpenSees, simulations, analyses) → read/write to **Work**
5. **After jobs complete:**
  - Review results
  - Copy important files back to **MyProjects** for collaboration or curation
  - Copy personal files back to **MyData** for personal use
  - Allow temporary files to expire from **Work**

## Key Rules of Thumb

| Question                                      | Use This Storage |
| --------------------------------------------- | ---------------- |
| Do I need private personal space?             | **MyData**       |
| Do I need to share with my team?              | **MyProjects**   |
| Do I need high-speed file access for compute? | **Work**         |
| Am I publishing or curating data?             | **MyProjects**   |
| Is this just for a temporary job run?         | **Work**         |

## Paths and Access Summary

| Storage    | Access Path Example                      | Available On                           |
| ---------- | ---------------------------------------- | -------------------------------------- |
| MyData     | `/corral-repl/tg/portal/<username>/`     | Web portal, JupyterHub, Interactive VM |
| MyProjects | `/corral-repl/tg/projects/<project-id>/` | Web portal, JupyterHub, Interactive VM |
| Work       | `/work/<username>/<allocation>/`         | Stampede3, Frontera, HPC queues        |

*Note: Paths may vary slightly depending on system updates — always check your current allocation info.*

## Best Practice Advice

* Treat **MyData** like your personal notebook.
* Treat **MyProjects** like your shared filing cabinet.
* Treat **Work** like your scratchpad — fast but disposable.
* Always backup any critical results out of Work after jobs finish.
* Use MyProjects when preparing data for curation or publication.
