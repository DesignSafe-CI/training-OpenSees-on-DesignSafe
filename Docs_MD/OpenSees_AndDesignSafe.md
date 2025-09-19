# OpenSees on DesignSafe

**OpenSees** was conceptualized, designed, and developed with **parallel computing** as a core objective. A parallel computing application leverages multiple processors working simultaneously — not only on independent tasks but also on interdependent tasks where processors exchange information.

Building on these design principles, OpenSees now includes **3 + 1 applications**, each optimized for different objectives and computational models.

**DesignSafe**, through the Texas Advanced Computing Center (**TACC**), provides multiple platforms to run these OpenSees applications. Each platform is designed with **scalability and adaptability** in mind, supporting a wide range of project objectives, sizes, and scopes.

The **choice of OpenSees application and DesignSafe platform** depends on your project needs, which may change across different stages of your work. The integrated environment on DesignSafe allows you to move seamlessly between platforms, scaling your workflows as needed. Importantly, scaling is not simply a matter of “adding more nodes” — different analyses demand different strategies, whether memory-intensive, embarrassingly parallel, or GPU-accelerated.

---

## Workflows for OpenSees on DesignSafe

There are four main ways to run OpenSees on DesignSafe:

1. **Submit jobs to HPC from the Web Portal via Tapis Apps**
2. **Run OpenSees directly within JupyterHub**
3. **Submit jobs to HPC from JupyterHub using Tapis Apps**
4. **Manually submit SLURM jobs to HPC from a login node**

These workflows are illustrated below:

<img src="../_images/WaysToRunOpenSeesOnDS_all.jpg" alt="Workflows for OpenSees on DesignSafe" width="75%" />  

---

## Recommendations

### 1. Run small to medium jobs within JupyterHub

* No wait time, no walltime limits.
* Allocated with **8 processors**.

  <img src="../_images/WaysToRunOpenSeesOnDS_JupHub.jpg" alt="Workflows for OpenSees on DesignSafe -- Jupyter Hub" width="50%" />  

### 2. Submit medium to large jobs to HPC from JupyterHub

* The most efficient workflow for job and file management.

  <img src="../_images/WaysToRunOpenSeesOnDS_HPC.jpg" alt="Workflows for OpenSees on DesignSafe HPC" width="50%" />  

