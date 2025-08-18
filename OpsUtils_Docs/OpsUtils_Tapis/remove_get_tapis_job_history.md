# get_tapis_job_history
***get_tapis_job_history(t, jobUuid, print_all=False,return_values=False)***

This function fetches the complete history of a specified Tapis job from the Tapis jobs service and prints a structured, table-style summary.
Can display either only the **most recent step** (default) or **all history steps**.

**Inputs:**

* *t* (*Tapis client object*):
  Authenticated Tapis client instance (from *tapis3* or *py-tapis*), used to connect and retrieve job information.
* *jobUuid* (*str*):
  The UUID of the job whose history is being queried.
* *print_all* (*bool*, optional):
  If *True*, prints **all history steps** in order. If *False* (default), prints **only the latest step**.
* *return_values* : bool, optional
    If True, it returns the list. this causes a data dump when called alone.
    Default is False.

**Outputs:**

* Returns a **list of history event objects** describing the job lifecycle.

**Behavior:**

* Prints a clear, table-style report of each selected history step, showing flattened key-value pairs for easy reading.
* Skips empty or null values for a cleaner display.

**Example usage:**

```python
history = get_tapis_job_history(t, "a1b2c3d4-5678-90ef-ghij-klmnopqrstuv", print_all=True)
```


#### Files
You can find these files in Community Data.

```{dropdown} get_tapis_job_history.py
:icon: file-code
```{literalinclude} ../../OpsUtils/OpsUtils/Tapis/get_tapis_job_history.py
:language: none
```


---

**Author:** Silvia Mazzoni, DesignSafe (silviamazzoni@yahoo.com)
**Date:** 2025-08-14
**Version:** 1.0