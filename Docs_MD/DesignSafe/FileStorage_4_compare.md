# File Storage Comparison
***Comparing Storage Options***

Here is a **compact comparison table** that shows at a glance how **Corral**, **Work**, and **Node-local** differ in persistence, performance, and access. You can immediately see why Corral is for **long-term use**, while Work and node-local are for **jobs**.

| Storage Type   | Persistence                    | Performance        | Access From                             | Best Use Case                         |
| -------------- | ------------------------------ | ------------------ | --------------------------------------- | ------------------------------------- |
| **Corral**     | Long-term, backed up           | Moderate (network) | Data Depot, JupyterHub, VMs, Tapis      | Archiving, collaboration, publication |
| **Work**       | Long-term (not backed up)      | High (on system)   | Compute systems, Data Depot, JupyterHub | Staging input/output files for jobs   |
| **Node-local** | Temporary (deleted at job end) | Very High (local)  | Only during active compute job          | Fast scratch I/O during runtime       |


✅ This table makes the tradeoffs clear:

* **Corral** = safe, shared, persistent → but slower.
* **Work** = faster, system-mounted, but not backed up.
* **Node-local** = fastest, but ephemeral.

*Prepare in Corral → Run in Work/Node-local → Archive back to Corral!!*
