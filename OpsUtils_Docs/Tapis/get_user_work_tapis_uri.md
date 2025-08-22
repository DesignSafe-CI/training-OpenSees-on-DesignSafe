# get_user_work_tapis_uri
***get_user_work_tapis_uri(t,system_id: str = "stampede3",*,valid_systems: Iterable[str] = ("stampede3", "ls6", "frontera"),app_suffix: str = "-credential",job_name: str = "getWork",) -> Path***

## Purpose

Return the user’s **work** directory on a target HPC system by submitting the
system’s *credential* app (e.g., *stampede3-credential*) and parsing the job’s
archive directory. This avoids hard-coding paths and stays aligned with site
conventions.

## Signature

```python
get_user_work_path(
    t,
    system_id: str = "stampede3",
    *,
    valid_systems: Iterable[str] = ("stampede3", "ls6", "frontera"),
    app_suffix: str = "-credential",
    job_name: str = "getWork",
) -> pathlib.Path
````

## How it works

1. Builds *app_id = f"{system_id}{app_suffix}"* (e.g., *stampede3-credential*).
2. Queries the app’s **latest** version.
3. Submits a tiny credential job.
4. Reads *archiveSystemDir* from the submission response.
5. Truncates that path at */{system_id}* to produce a stable **work** root
   (e.g., */work2/01121/stampede3*).

## Examples

```python
from tapipy.tapis import Tapis
from pathlib import Path

# Assume t is an authenticated Tapipy client
work_dir = get_user_work_path(t, "stampede3")
print(work_dir)  # -> /work2/01121/stampede3
```

Switching system:

```python
work_dir = get_user_work_path(t, "ls6")
```

## Errors & Troubleshooting

* **ValueError: Unknown system**
  Ensure *system_id* is one of the allowed systems or extend *valid_systems*.

* **Could not resolve latest version for app**
  Your site may not expose *getAppLatestVersion*. The helper falls back to
  *getApp(..., appVersion="latest")*. If both fail, confirm your app ID (e.g.,
  *stampede3-credential*) exists and you have permission to read it.

* **Response missing *archiveSystemDir* or cannot parse work path**
  Check the job definition for the credential app. If the archive path format
  changed, update the parsing rule (regex) accordingly.

## Design Notes

* Returns a *pathlib.Path* for convenient path ops.
* Raises exceptions (no *print*) so upstream callers can log or handle errors
  consistently.
* If your site’s naming differs (e.g., *-cred* instead of *-credential*), set
  *app_suffix* accordingly.


#### Files
You can find these files in Community Data.

```{dropdown} get_user_work_tapis_uri.py
:icon: file-code
```{literalinclude} ../../OpsUtils/OpsUtils/Tapis/get_user_work_tapis_uri.py
:language: none
```


---

**Author:** Silvia Mazzoni, DesignSafe (silviamazzoni@yahoo.com)
**Date:** 2025-08-14
**Version:** 1.0