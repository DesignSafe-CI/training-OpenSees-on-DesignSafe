# App Input Categories

Understanding the difference between **inputs**, **parameters**, **configuration**, and **outputs** in Tapis (and DesignSafe apps) is essential for designing effective, user-friendly apps.

Here’s a clear breakdown of each:

---

:::{dropdown} 1. **Inputs**

**Files or directories** the user provides to the app.

### Purpose:

To make **actual files** (e.g., data, scripts, models) available to your code at runtime.

### Characteristics:

* Defined in `app-definition.json` under `"inputs"`
* Must be **URI** paths (usually pointing to Tapis storage)
* Automatically staged by Tapis into the job's working directory
* Available in your `wrapper.sh` via environment variables (`$input_name`)

### Example:

```json
"inputs": [
  {
    "id": "model_dir",
    "details": {
      "label": "Model Directory",
      "description": "Folder containing .tcl files"
    },
    "required": true,
    "inputType": "URI"
  }
]
```

In `wrapper.sh`:

```bash
OpenSees "$model_dir/main.tcl"
```

:::

:::{dropdown} 2. **Parameters**

**User-specified values (strings, numbers, enums)** passed to your app — not files.

### Purpose:

To customize behavior like iteration counts, filenames, flags, or option settings.

### Characteristics:

* Defined in `"parameters"` in `app-definition.json`
* Show up as text boxes, dropdowns, etc. in DesignSafe GUI
* Available in `wrapper.sh` as `$parameter_name`
* Can be overridden at job submission time

### Example:

```json
"parameters": [
  {
    "id": "script_name",
    "details": {
      "label": "Script Filename",
      "description": "Which TCL file to run?",
      "type": "string"
    },
    "value": {
      "default": "main.tcl"
    }
  }
]
```

In `wrapper.sh`:

```bash
OpenSees "$model_dir/$script_name"
```

:::

:::{dropdown} 3. **Configuration** (❗ Not a formal section in Tapis JSON)

This term usually refers to **execution settings** passed at job submission time, like:

| Configuration Key | Example     | What It Controls        |
| ----------------- | ----------- | ----------------------- |
| `executionSystem` | stampede3   | Which machine to run on |
| `nodeCount`       | 2           | How many nodes          |
| `coresPerNode`    | 32          | Processors per node     |
| `queue`           | skx         | Queue to submit job to  |
| `maxRunTime`      | 01:00:00    | Wall time               |
| `memory`          | 8GB         | Memory allocation       |

You don’t define these in `app-definition.json`, but users or scripts pass them when submitting the job.

Example in Python:

```python
client.jobs.submitJob({
    "executionSystem": "stampede3",
    "nodeCount": 2,
    "coresPerNode": 32,
    "maxRunTime": "01:00:00",
    ...
})
```

---

## 4. **Outputs**
:::{dropdown} 
**Files your app generates** and wants to preserve.

### Purpose:

To let Tapis know **what to archive and return** after the job finishes.

### Characteristics:

* Defined in `"outputs"` in `app-definition.json`
* Files must be created by your script in the working directory
* Tapis will copy them to archive storage

### Example:

```json
"outputs": [
  {
    "id": "output.log",
    "value": {
      "default": "output.log"
    }
  }
]
```

In `wrapper.sh`:

```bash
ibrun OpenSees "$model_dir/$script_name" > output.log
```
:::

---

## Analogy Summary

| Component       | Think of It Like...     | Use For                    |
| --------------- | ----------------------- | -------------------------- |
| `inputs`        | 📂 Uploaded files       | Data, models, scripts      |
| `parameters`    | 🎛 User-config settings | File names, numbers, flags |
| `configuration` | ⚙️ Job resource options | Nodes, queue, time         |
| `outputs`       | 📤 What you want back   | Log files, results, CSVs   |

---

## Tapis Job Flow Diagram

Here's a **clear diagram-style explanation** (text-based for now) showing how **inputs**, **parameters**, **configuration**, and **outputs** flow through a Tapis/DesignSafe job.

```
                 ┌──────────────────────────────┐
                 │      DesignSafe GUI /        │
                 │  Job Submission via Tapipy   │
                 └────────────┬─────────────────┘
                              │
                              ▼
               ┌───────────────────────────────┐
               │        Job Submission         │
               │  ┌──────────────────────────┐ │
               │  │      inputs (URIs)       │ │  📁 Files: user uploads (e.g. .tcl, .csv)
               │  ├──────────────────────────┤ │
               │  │     parameters (values)  │ │  🎛 Settings: user types or selects
               │  ├──────────────────────────┤ │
               │  │  configuration (runtime) │ │  ⚙️ Resources: nodes, cores, time, queue
               │  └──────────────────────────┘ │
               └────────────┬──────────────────┘
                            │
                            ▼
       ┌──────────────────────────────────────────────┐
       │       Tapis Job Staging / Initialization     │
       │                                              │
       │  ✔ Copies all `inputs` into job directory    │
       │  ✔ Sets environment variables for all inputs │
       │    and parameters                            │
       │  ✔ Launches job on specified execution system│
       └────────────────────────┬─────────────────────┘
                                │
                                ▼
                 ┌────────────────────────────┐
                 │     wrapper.sh executes    │
                 │                            │
                 │  Example:                  │
                 │  cd $SCRATCH/$JOB_NAME     │
                 │  module load OpenSees      │
                 │  ibrun OpenSees "$model_dir/$script_name" │
                 └────────────────────────────┘
                                │
                                ▼
                 ┌────────────────────────────┐
                 │      Job Output Files      │
                 │  Files written to:         │
                 │    - output.log            │
                 │    - results.csv           │
                 │                            │
                 │  Must match defined `outputs` in app.json
                 └────────────────────────────┘
                                │
                                ▼
         ┌─────────────────────────────────────────────┐
         │  Tapis automatically archives defined outputs│
         │   to user's storage (e.g., DesignSafe Depot) │
         └─────────────────────────────────────────────┘
```

---

### Quick Legend

| Element           | What It Does                        | Defined In            |
| ----------------- | ----------------------------------- | --------------------- |
| **inputs**        | Files copied into job dir           | `app-definition.json` |
| **parameters**    | Values passed as shell variables    | `app-definition.json` |
| **configuration** | Execution settings like nodes/queue | `submitJob()` call    |
| **outputs**       | Files that are saved post-execution | `app-definition.json` |
