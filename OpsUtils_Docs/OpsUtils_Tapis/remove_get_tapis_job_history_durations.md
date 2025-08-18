<!-- # get_tapis_job_history_durations
***get_tapis_job_history_durations(t,jobUuid,getMetadata=True,printAllAll = False,printAllOut = False,printSteps = True,printDurations = True,printInput = True,returnData=False)***

This is an **advanced analysis and reporting function** that takes a **Tapis job UUID** (from DesignSafe/TACC via the Tapis client **t**) and:

* Processes the entire **job history events log**,
* Measures durations of each computational stage,
* Summarizes data transfer details (input / archive transactions),
* Collects any error messages,
* Retrieves and prints key job metadata,
* And builds structured dictionaries you can use for deeper analysis.

It’s a **diagnostic & audit tool** for understanding exactly what happened during a TACC or DesignSafe job, how long each stage took, and where problems occurred.

---

### How it works step by step

#### 1. Gets the full TACC/Tapis job history

```python
JobHistory = t.jobs.getJobHistory(jobUuid=jobUuid)
```

This pulls every event related to the job lifecycle: status changes, file transfers, errors, etc.

---

#### 2. Iterates through each history line

For each event it:

* Flattens the dictionary using **OpsUtils.flatten_dict** to easily access nested fields.
* Handles different event types:

  * **JOB_NEW_STATUS**: captures transitions like **QUEUED → RUNNING → FINISHED**, calculates how long each status lasted, and builds a total duration.
  * **JOB_INPUT_TRANSACTION_ID / JOB_ARCHIVE_TRANSACTION_ID**: records file transfer metrics and how long transfers took.
  * **JOB_ERROR_MESSAGE**: collects structured error information.
  * Any other events: prints out details so you can see unexpected logs.

---

#### 3. Builds structured summaries

* **STATdur**: human-readable list of stage durations.
* **stageDict**: dictionary storing exact timestamps & durations by job status.
* **transfersDict**: input/archive transfer summaries (bytes transferred, durations).
* **JobErrorList**: list of any captured error messages.
* **stagesSTRlist**: pretty-printed log of all stages.
* **AllOutList**: exhaustive printout of every field in the history for full audits.

---

#### 4. Prints summary sections based on flags

* Prints detailed timelines, transfers, durations, and errors based on:

  * `printAllOut`, `printSteps`, `printDurations`, `printInput`.
* If `printAllAll` is `True`, it enables *all* of them for a complete dump.

---

#### 5. Retrieves top-level job metadata

If *getMetadata* is *True*, it also calls:

```python
job_response = t.jobs.getJob(jobUuid=jobUuid)
```

and prints core info like *uuid*, *name*, *status*, *appId*, *created*.

---

#### 6. Optionally returns all collected data

If `returnData=True`, it returns a dictionary containing:

| Key                   | Description                             |
| --------------------- | --------------------------------------- |
| `'StagesMetricsDict'` | Durations & timestamps by job status    |
| `'StagesList'`        | Pretty list of stage changes & messages |
| `'DataTransfersDict'` | Input/archive transfer details          |
| `'JobErrorList'`      | Any captured error messages             |
| `'MetadataDict'`      | Core job metadata                       |

---

### Typical use

```python
process_tacc_job_history(
    t, 
    jobUuid="12ab-34cd-56ef...",
    getMetadata=True,
    printAllAll=False,
    printSteps=True,
    printDurations=True,
    printInput=True,
    returnData=False
)
```

Use **returnData=True** to get structured metrics for dashboards, plots, or automated logs.

---

###  Why this is powerful

It gives you a **complete deep dive into what happened inside a TACC job**:

* How long was it queued? How long did the actual computation take?
* How much data was transferred, and how long did it take?
* Were there any job-level errors or special conditions?
* What was the final status and total runtime?

All from one function call — great for performance tuning or debugging failed runs.

---

 **In short:**
*process_tacc_job_history* is your **all-in-one auditing, timing, and troubleshooting tool** for TACC jobs, turning raw event logs into clear metrics and summaries.

---

###  Quick start examples for *process_tacc_job_history*

Choose the level of detail you want:

---

####  Minimal summary (just durations + main steps)
```python
process_tacc_job_history(
    t, 
    jobUuid, 
    printSteps=True, 
    printDurations=True
)
````

---

####  Include data transfers

```python
process_tacc_job_history(
    t, 
    jobUuid, 
    printSteps=True, 
    printDurations=True, 
    printInput=True
)
```

---

####  Full debug output (all history, all details)

```python
process_tacc_job_history(
    t, 
    jobUuid, 
    printAllAll=True
)
```

---

####  Structured data only (for dashboards, plots, logs)

```python
job_data = process_tacc_job_history(
    t, 
    jobUuid, 
    returnData=True, 
    printSteps=False, 
    printDurations=False, 
    printInput=False
)
```

You can then explore:

```python
job_data.keys()
# → dict_keys(['StagesMetricsDict', 'StagesList', 'DataTransfersDict', 'JobErrorList', 'MetadataDict'])
```

---

This makes it easy to switch from a quick human-readable summary to full audit logs or structured data for automation.



#### Files
You can find these files in Community Data.

```{dropdown} get_tapis_job_history_durations.py
:icon: file-code
```{literalinclude} ../../../OpsUtils/OpsUtils/Tapis/get_tapis_job_history_durations.py
:language: none
```


---

**Author:** Silvia Mazzoni, DesignSafe (silviamazzoni@yahoo.com)
**Date:** 2025-08-14
**Version:** 1.0 -->