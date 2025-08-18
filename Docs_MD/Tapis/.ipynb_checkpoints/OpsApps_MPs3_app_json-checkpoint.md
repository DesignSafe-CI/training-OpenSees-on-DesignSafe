# app.json
    
This file declares the app to the Tapis system. It defines how the app runs, what files and parameters it expects, what system it runs on, and how results are stored.

## Key Fields Explained

| Field                        | Meaning                                                          |
| ---------------------------- | ---------------------------------------------------------------- |
| `id`                         | App identifier (`opensees-mp-s3`)                                |
| `runtime`                    | `"ZIP"` — unpacked file-based runtime (not a container)          |
| `jobType`                    | `"BATCH"` — submits to SLURM queue as a scheduled job            |
| `execSystemId`               | `"stampede3"` — the compute cluster where this app runs          |
| `execSystemLogicalQueue`     | `"skx"` — Stampede3 Skylake queue                                |
| `nodeCount` / `coresPerNode` | 2 nodes × 48 cores (default)                                     |
| `archiveSystemId`            | `"stampede3"` — output is saved back to user's `$WORK` directory |
| `isMpi`                      | `false` (handled manually using ibrun)                           |

## Inputs

| Input Name        | Description                                                               |
| ----------------- | ------------------------------------------------------------------------- |
| `Input Directory` | A **folder** containing all input files, including the main `.tcl` script |
| `Main Script`     | The filename of the `.tcl` script (e.g., `"model.tcl"`)                   |

## Parameters

```json
"appArgs": [
  {
    "name": "mainProgram",
    "arg": "OpenSeesMP",
    "inputMode": "FIXED"
  },
  {
    "name": "Main Script",
    "description": "...",
    "inputMode": "REQUIRED"
  }
]
```

* `mainProgram` = `"OpenSeesMP"` is fixed and passed as `$1` to the script
* `"Main Script"` = passed as `$2`, the filename to execute

## Output Archiving

Output files, including `.out`, `.err`, and simulation results, are archived to:

```
$WORK/tapis-jobs-archive/<date>/<jobname>-<uuid>/
```

This allows for future access and reproducibility.

