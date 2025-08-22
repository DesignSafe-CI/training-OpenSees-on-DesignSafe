from __future__ import annotations
def get_user_work_path(
    t,
    system_id: str = "stampede3",
    *,
    valid_systems: Iterable[str] = ("stampede3", "ls6", "frontera"),
    app_suffix: str = "-credential",
    job_name: str = "getWork",
) -> Path:
    """
    Return the user's *work* directory for a given HPC system by submitting the
    system-specific “credential” Tapis app and parsing its archive path.

    Parameters
    ----------
    t : Tapipy client
        An authenticated Tapipy v3 client (e.g., `from tapipy.tapis import Tapis`).
    system_id : str, optional
        Target HPC system key (e.g., "stampede3", "ls6", "frontera"). Case-insensitive.
    valid_systems : Iterable[str], optional
        Acceptable system identifiers. Used for validation.
    app_suffix : str, optional
        Suffix used to form the credential app ID (default: "-credential").
        The credential app is assumed to follow the pattern: `{system_id}{app_suffix}`.
    job_name : str, optional
        Name to assign to the submitted credential job.

    Returns
    -------
    pathlib.Path
        The resolved *work* directory as a `Path`.

    Raises
    ------
    ValueError
        If `system_id` is not recognized, if the app cannot be found, or
        if the archive directory cannot be parsed reliably.
    RuntimeError
        If the credential job submission fails or the response is missing fields.

    Notes
    -----
    - This function **does not** print; it raises exceptions for callers to handle.
    - It uses `apps.getAppLatestVersion(appId=...)` then submits that version.
      If your site does not expose that endpoint, replace with `apps.getApp(appId=..., appVersion="latest")`.
    - We parse the returned `archiveSystemDir` and truncate at the first occurrence
      of `/{system_id}` boundary to get a stable “work” root, e.g.
      `/work2/01121/{system_id}`.

    Author
    ------
    Silvia Mazzoni, DesignSafe (silviamazzoni@yahoo.com)

    Date
    ----
    2025-08-14

    Version
    -------
    1.0
    """
    
    
    import re
    from pathlib import Path
    from typing import Iterable, Optional

    sys_key = system_id.strip().lower()
    valid = {s.lower() for s in valid_systems}
    if sys_key not in valid:
        raise ValueError(
            f"Unknown system '{system_id}'. Choose one of: {sorted(valid)}"
        )

    app_id = f"{sys_key}{app_suffix}"

    # 1) Resolve app version
    try:
        # If your Tapipy version doesn't have getAppLatestVersion, swap for getApp(..., appVersion="latest")
        latest = t.apps.getAppLatestVersion(appId=app_id)
        app_version = getattr(latest, "version", None) or "latest"
    except Exception as exc:
        # Fallback if the endpoint differs on your deployment
        try:
            app = t.apps.getApp(appId=app_id, appVersion="latest")
            app_version = getattr(app, "version", None) or "latest"
        except Exception as exc2:
            raise ValueError(
                f"Could not resolve latest version for appId='{app_id}'. "
                f"Original errors: {exc!r}; {exc2!r}"
            )

    # 2) Submit the credential job
    try:
        submitted_job = t.jobs.submitJob(
            name=job_name, appId=app_id, appVersion=app_version
        )
    except Exception as exc:
        raise RuntimeError(
            f"Credential job submission failed for appId='{app_id}', "
            f"version='{app_version}': {exc}"
        )

    # 3) Extract archive path and derive work dir
    archive_dir = getattr(submitted_job, "archiveSystemDir", None)
    if not archive_dir:
        raise RuntimeError(
            "Response missing 'archiveSystemDir'; cannot derive work directory."
        )

    # Robustly truncate at '/{system_id}' boundary (case-insensitive), preserving that token
    # Example: '/work2/01121/stampede3/home/…' -> '/work2/01121/stampede3'
    pattern = re.compile(rf"^(.*?/(?i:{re.escape(sys_key)}))(?:/|$)")
    m = pattern.search(archive_dir)
    if not m:
        # As a conservative fallback, try exact substring match (case-insensitive)
        idx = archive_dir.lower().find(f"/{sys_key}")
        if idx == -1:
            raise ValueError(
                f"Could not parse work path from archiveSystemDir='{archive_dir}' "
                f"using system tag '{sys_key}'."
            )
        work_dir = archive_dir[: idx + 1 + len(sys_key)]
    else:
        work_dir = m.group(1)

    return Path(work_dir)

