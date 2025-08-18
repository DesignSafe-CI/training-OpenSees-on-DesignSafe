# File Storage
***Understanding Storage on DesignSafe***

In high-performance computing, **every job either starts, ends, or both starts *and* ends with data**. Whether you're running a small script or a large-scale simulation, your workflow involves reading input files and writing output results.

Understanding where that data lives — and how quickly it can be accessed or saved — is critical to optimizing both your **job performance** and **research productivity**. Choosing the right storage location for each phase of your workflow helps avoid unnecessary slowdowns, data loss, or complexity in moving files around.
    
## Why File Storage Matters in HPC

When running jobs on HPC systems like Stampede3, **data input/output (I/O)** — reading and writing files — is often the **slowest part** of the workflow. Even with powerful CPUs and GPUs, your job can be bottlenecked if it's waiting on file access.

Optimizing **where** and **when** your data is accessed can significantly improve both **compute performance** and **researcher efficiency**. Choosing the right storage system — whether it's on Corral, Stampede3, or even directly on the compute node — can make a big difference.
    
## DesignSafe Storage Systems Overview

| Storage Type   | Description                                                    |
| -------------- | -------------------------------------------------------------- |
| **MyData**     | User’s personal home directory              |
| **MyProjects** | Private project-specific data shared among team members        |
| **Community**  | Public datasets and shared examples                            |
| **Published**  | Public published datasets (NHERI, NEES)                        |


## System-Specific Storage Systems

| Storage Type   | Description                                                    |
| -------------- | -------------------------------------------------------------- |
| **Scratch**    | Temporary high-speed local storage on Stampede3                |
| **Home**       | Personal UNIX home directory on Stampede3                      |
| **Work**       | "Shared" project workspace |

Work is a "shared allocation" because the storage itself is shared by a group of individuals, however, by default, these individuals only have access to their own subfolder.