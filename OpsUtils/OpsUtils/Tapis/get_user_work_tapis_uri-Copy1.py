from __future__ import annotations

from typing import Iterable, Sequence


def get_user_work_tapis_uri(
    t,
    system_id: str = "stampede3",
    *,
    valid_systems: Iterable[str] = ("stampede3", "ls6", "frontera"),
    tapis_work_system_id: str = "cloud.data",
    app_suffix: str = "-credential",
    job_name: str = "getWork",
    ensure_trailing_slash: bool = False,
) -> str:
    """
    Return the user's **Work base** as a Tapis URI for the given HPC system.

    The function submits the system's credential app, reads the job's
    `archiveSystemDir` (an HPC filesystem path), extracts the Work root,
    Examples
    --------

    Parameters
    ----------
    t : Tapipy client
        Authenticated Tapis v3 client.
    system_id : {"stampede3","ls6","frontera"}
        Target HPC system (case-insensitive).
    valid_systems : Iterable[str]
        Allowed system IDs for validation.
    app_suffix : str
        Suffix for the credential app (default: "-credential"), pattern:
        `{system_id}{app_suffix}`.
    job_name : str
        Name assigned to the temporary credential job.
    tapis_work_system_id : str
        Tapis system ID that fronts the Work storage (DesignSafe: "cloud.data").
    work_roots : Sequence[str]
        Acceptable HPC Work root directory names to detect in archive paths
        (e.g., "work", "work2", ...).
    ensure_trailing_slash : bool
        If True, return URI with a trailing "/" (recommended).

    Returns
    -------
    str
        Tapis URI for the user's Work base on the given system, e.g.:
        "tapis://cloud.data/work/01121/jdoe/stampede3/"

    Raises
    ------
    ValueError
        Unknown system_id, or the expected segments cannot be parsed.
    RuntimeError
        App resolution or job submission failed, or response missing fields.

    Author
    ------
    Silvia Mazzoni, DesignSafe (silviamazzoni@yahoo.com)
    copyright: 2025
    """
    from OpsUtils import OpsUtils
    sys_key = system_id.strip().lower()
    valid = {s.lower() for s in valid_systems}
    if sys_key not in valid:
        raise ValueError(f"Unknown system '{system_id}'. Choose one of: {sorted(valid)}")

    app_id = f"{sys_key}{app_suffix}"

    # Resolve latest app version
    try:
        latest = t.apps.getAppLatestVersion(appId=app_id)
        app_version = getattr(latest, "version", None) or "latest"
    except Exception:
        try:
            app = t.apps.getApp(appId=app_id, appVersion="latest")
            app_version = getattr(app, "version", None) or "latest"
        except Exception as exc2:
            raise RuntimeError(
                f"Could not resolve latest version for appId='{app_id}': {exc2}"
            )

    # Submit temporary credential job
    try:
        submitted_job = t.jobs.submitJob(name=job_name, appId=app_id, appVersion=app_version)
    except Exception as exc:
        raise RuntimeError(
            f"Credential job submission failed for appId='{app_id}', version='{app_version}': {exc}"
        )

    archiveSystemDir = getattr(submitted_job, "archiveSystemDir", None)
    if not archiveSystemDir or not isinstance(archiveSystemDir, str):
        raise RuntimeError("Response missing string field 'archiveSystemDir'.")
        
    # Extract HPC archive path
    workDir = archiveSystemDir.split(system_id)[0]
    
    workDir = workDir.strip("/")
    uri = f'tapis://{tapis_work_system_id}/{workDir}/{system_id}'
    if ensure_trailing_slash:
        uri = f'{uri}/'
    # print('uri',uri)    
    return uri
